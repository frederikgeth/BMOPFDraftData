# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Frederik Geth

"""Run converted feeders with Tellegen's native mc_pf example and retain an audit.

The voltage envelope is disabled to preserve the constant-power input equations.
Each solve is checked against the input's terminal/component inventory, KCL,
load powers, line pi-model equations, Dyn11 equations, shunts, and power balance.
Input voltage-limit violations are reported separately from solver convergence.
"""

import argparse
import csv
import gzip
import hashlib
import json
import math
import subprocess
import time
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OPTIONS = {"voltage_envelope": False, "max_iterations": 200}
ABSOLUTE_CURRENT_TOLERANCE = 1e-6
RELATIVE_TOLERANCE = 1e-8


def complex_value(value):
    return complex(value["re"], value["im"])


def matrix_vector(element, real_prefix, imag_prefix, vector, scale=1.0):
    return [
        sum(complex(element.get(f"{real_prefix}_{i}_{j}", 0), element.get(f"{imag_prefix}_{i}_{j}", 0))
            * value * scale for j, value in enumerate(vector, 1))
        for i in range(1, len(vector) + 1)
    ]


def input_voltage_violations(case, voltages):
    violations = 0
    for key, bus in case["bus"].items():
        phases = [t for t in bus["terminal_names"] if t != "n"]
        for prefix in ("vpn", "vpp"):
            if prefix == "vpn":
                if "n" not in bus["terminal_names"]:
                    continue
                pairs = [(t, "n") for t in phases]
            else:
                pairs = [(phases[i], phases[(i + 1) % len(phases)]) for i in range(len(phases))]
            for bound, lower in (("min", True), ("max", False)):
                limits = bus.get(f"{prefix}_{bound}")
                if limits is None:
                    continue
                for (first, second), limit in zip(pairs, limits, strict=True):
                    value = abs(voltages[(key, first)] - voltages[(key, second)])
                    if (lower and value < limit - 1e-6) or (not lower and value > limit + 1e-6):
                        violations += 1
    return violations


def check_passive_laws(case, voltages, ports, compare):
    def at(bus, terminals):
        return [voltages[(bus, t)] for t in terminals]

    for key, line in case["line"].items():
        code = case["linecode"][line["linecode"]]
        bf, bt = line["bus_from"], line["bus_to"]
        tf, tt = line["terminal_map_from"], line["terminal_map_to"]
        vf, vt = at(bf, tf), at(bt, tt)
        shunt_from = matrix_vector(code, "G_from", "B_from", vf, line["length"])
        shunt_to = matrix_vector(code, "G_to", "B_to", vt, line["length"])
        series_current = [ports[("line", key)][(bf, t)] - y for t, y in zip(tf, shunt_from, strict=True)]
        drop = matrix_vector(code, "R_series", "X_series", series_current, line["length"])
        for i in range(len(tf)):
            # Express the voltage-law mismatch as a current using the diagonal impedance.
            z = complex(code[f"R_series_{i+1}_{i+1}"], code[f"X_series_{i+1}_{i+1}"]) * line["length"]
            compare((vf[i] - vt[i]) / z, drop[i] / z)
            compare(ports[("line", key)][(bt, tt[i])], -series_current[i] + shunt_to[i])
    for key, shunt in case["shunt"].items():
        bus, tm = shunt["bus"], shunt["terminal_map"]
        expected = matrix_vector(shunt, "G", "B", at(bus, tm))
        for terminal, current in zip(tm, expected, strict=True):
            compare(ports[("shunt", key)][(bus, terminal)], current)
    for key, transformer in case["transformer"]["delta_wye"].items():
        bf, bt = transformer["bus_from"], transformer["bus_to"]
        vh, vl = at(bf, ["1", "2", "3"]), at(bt, ["1", "2", "3", "n"])
        k = transformer["v_nom_to"] / (math.sqrt(3) * transformer["v_nom_from"])
        z = complex(transformer["r_series"], transformer["x_series"])
        il = [(vl[i] - vl[3] - k * (vh[i] - vh[(i + 1) % 3])) / z for i in range(3)]
        for i, terminal in enumerate(("1", "2", "3")):
            compare(ports[("transformer", key)][(bt, terminal)], il[i])
            compare(ports[("transformer", key)][(bf, terminal)], -k * (il[i] - il[(i - 1) % 3]))
        compare(ports[("transformer", key)][(bt, "n")], -sum(il))


def audit(case, result):
    voltages = {(v["bus"], v["terminal"]): complex_value(v["voltage"]) for v in result["terminals"]}
    expected_nodes = {(bus_id, t) for bus_id, bus in case["bus"].items() for t in bus["terminal_names"]}
    if set(voltages) != expected_nodes or len(voltages) != len(result["terminals"]):
        raise ValueError("Returned terminal inventory does not match the input")
    ports = defaultdict(dict)
    kcl = defaultdict(complex)
    incident_scale = defaultdict(float)
    powers = defaultdict(list)
    for port in result["element_ports"]:
        node = (port["bus"], port["terminal"])
        current = complex_value(port["current_into_element"])
        power = complex_value(port["power_into_element"])
        key = (port["kind"], port["element"])
        # Load dipoles may share terminals; passive-element terminals occur once.
        if port["kind"] != "load" and node in ports[key]:
            raise ValueError(f"Duplicate passive terminal: {key}, {node}")
        ports[key][node] = ports[key].get(node, 0j) + current
        kcl[node] += current
        incident_scale[node] += abs(current)
        powers[key].append(power)
        if not (math.isfinite(current.real) and math.isfinite(current.imag)
                and math.isfinite(power.real) and math.isfinite(power.imag)):
            raise ValueError("Non-finite element result")
    for kind in ("line", "shunt", "load", "transformer"):
        expected = set(case[kind]["delta_wye"] if kind == "transformer" else case[kind])
        actual = {element for element_kind, element in ports if element_kind == kind}
        if expected != actual:
            raise ValueError(f"{kind} component inventory mismatch")
    expected_sources = {(key, t) for key, source in case["voltage_source"].items() for t in source["terminal_map"]}
    if {(s["source"], s["terminal"]) for s in result["source_reactions"]} != expected_sources:
        raise ValueError("Source terminal inventory mismatch")
    source_power = 0j
    for source in result["source_reactions"]:
        node = (case["voltage_source"][source["source"]]["bus"], source["terminal"])
        current = complex_value(source["current_into_network"])
        kcl[node] -= current
        incident_scale[node] += abs(current)
        source_power += complex_value(source["power_into_network"])
    grounded = {(key, t) for key, bus in case["bus"].items() for t in bus.get("perfectly_grounded_terminals", [])}
    free_residuals = [(abs(kcl[node]), incident_scale[node]) for node in expected_nodes - grounded]
    max_kcl = max(value for value, _ in free_residuals)
    max_scaled_kcl = max(value / (ABSOLUTE_CURRENT_TOLERANCE + RELATIVE_TOLERANCE * scale)
                         for value, scale in free_residuals)
    max_law_residual = 0.0
    max_scaled_law_residual = 0.0

    def compare(actual, expected):
        nonlocal max_law_residual, max_scaled_law_residual
        difference = abs(actual - expected)
        scaled = difference / (ABSOLUTE_CURRENT_TOLERANCE + RELATIVE_TOLERANCE * max(abs(actual), abs(expected)))
        max_law_residual = max(max_law_residual, difference)
        max_scaled_law_residual = max(max_scaled_law_residual, scaled)

    check_passive_laws(case, voltages, ports, compare)
    max_load_power_error = 0.0
    for key, load in case["load"].items():
        expected = complex(math.fsum(load["p_nom"]), math.fsum(load["q_nom"]))
        actual = sum(powers[("load", key)])
        error = abs(actual - expected)
        max_load_power_error = max(max_load_power_error, error)
        if error > 1e-6 + RELATIVE_TOLERANCE * abs(expected):
            raise ValueError(f"{key}: load power differs from constant-power input by {error} VA")
    absorbed = sum(sum(values) for values in powers.values())
    balance = source_power - absorbed
    power_scale = sum(abs(value) for values in powers.values() for value in values)
    if abs(balance) > 1e-6 + RELATIVE_TOLERANCE * power_scale:
        raise ValueError(f"Complex-power balance mismatch: {balance} VA")
    if max_scaled_kcl > 1 or max_scaled_law_residual > 1:
        raise ValueError(
            f"Electrical residual failed: scaled KCL={max_scaled_kcl}, device laws={max_scaled_law_residual}"
        )
    return {
        "input_voltage_limit_violation_count": input_voltage_violations(case, voltages),
        "terminal_count": len(voltages), "audit_kcl_residual_a": max_kcl,
        "audit_scaled_kcl_residual": max_scaled_kcl,
        "audit_device_law_residual_a": max_law_residual,
        "audit_scaled_device_law_residual": max_scaled_law_residual,
        "max_load_power_error_va": max_load_power_error,
        "power_balance_error_w": balance.real, "power_balance_error_var": balance.imag,
        "source_power_w": source_power.real, "source_power_var": source_power.imag,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", required=True, type=Path, help="Tellegen's native mc_pf example executable")
    parser.add_argument("--input-dir", type=Path, default=ROOT / "output/FrenchPowerGrids/original")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output/FrenchPowerGrids/validation/tellegen_pf")
    parser.add_argument("--timeout", type=float, default=120)
    args = parser.parse_args()
    binary = args.binary.resolve()
    files = sorted(args.input_dir.glob("*.bmopf.json"))
    if not binary.is_file() or not files:
        parser.error("Expected an existing executable and converted .bmopf.json inputs")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results_dir = args.output_dir / "results"
    results_dir.mkdir(exist_ok=True)
    options_path = args.output_dir / "options.json"
    options_path.write_text(json.dumps(OPTIONS, indent=2) + "\n")
    rows = []
    for i, path in enumerate(files, 1):
        raw = path.read_bytes()
        row = {"case": path.name, "input_sha256": hashlib.sha256(raw).hexdigest()}
        start = time.monotonic()
        try:
            completed = subprocess.run(
                [str(binary), str(path.resolve()), str(options_path.resolve())],
                capture_output=True, text=True, timeout=args.timeout, check=False,
            )
            row["exit_code"] = completed.returncode
            if completed.returncode:
                raise ValueError(completed.stderr.strip() or "Solver returned a nonzero exit code")
            result = json.loads(completed.stdout)
            if not result["converged"]:
                raise ValueError("Solver reported non-convergence")
            row.update({k: result[k] for k in (
                "iterations", "physical_kcl_residual", "scaled_kcl_residual", "min_voltage_pu",
                "max_voltage_pu", "voltage_valid", "factorization_count", "matrix_dimension",
            )})
            row["voltage_violation_count"] = len(result["voltage_violations"])
            result_path = results_dir / (path.stem + ".pf.json.gz")
            with gzip.open(result_path, "wt", encoding="utf-8") as stream:
                stream.write(completed.stdout)
            row["result_file"] = str(result_path.relative_to(args.output_dir))
            row.update(audit(json.loads(raw), result))
            row["status"] = "passed"
        except (ValueError, KeyError, OSError, subprocess.TimeoutExpired) as exc:
            row["status"] = "failed"
            row["error"] = str(exc)
        row["elapsed_seconds"] = time.monotonic() - start
        rows.append(row)
        if i % 25 == 0 or row["status"] != "passed":
            passed = sum(r["status"] == "passed" for r in rows)
            print(f"{i}/{len(files)}: {passed} passed; {path.name}: {row['status']}", flush=True)
    report = {
        "created_utc": datetime.now(UTC).isoformat(), "binary": str(binary),
        "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest(), "options": OPTIONS,
        "audit_absolute_current_tolerance_a": ABSOLUTE_CURRENT_TOLERANCE,
        "audit_relative_tolerance": RELATIVE_TOLERANCE,
        "case_count": len(rows), "passed": sum(r["status"] == "passed" for r in rows), "cases": rows,
        "cases_outside_input_voltage_limits": sum(
            r.get("input_voltage_limit_violation_count", 0) > 0 for r in rows
        ),
        "total_input_voltage_limit_violations": sum(
            r.get("input_voltage_limit_violation_count", 0) for r in rows
        ),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with (args.output_dir / "summary.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Passed {report['passed']}/{len(rows)}; report: {args.output_dir / 'summary.json'}")
    raise SystemExit(0 if report["passed"] == len(rows) else 1)


if __name__ == "__main__":
    main()
