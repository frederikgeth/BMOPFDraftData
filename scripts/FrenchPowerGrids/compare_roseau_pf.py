# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Frederik Geth

"""Compare saved native Tellegen results with fresh Roseau engine solves.

Uses the documented public trial license unless ROSEAU_LOAD_FLOW_LICENSE_KEY is
configured. Cases exceeding the activated license's bus limit are skipped.
Transformer HV currents include the separate BMOPF core shunt. Source currents
are compared using the current-into-element convention in both engines.
"""

import argparse
import csv
import gzip
import hashlib
import json
import math
import os
from collections import defaultdict
from datetime import UTC, datetime
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUBLIC_TRIAL_KEY = "A8C6DA-9405FB-E74FB9-C71C3C-207661-V3"
TERMINALS = {"a": "1", "b": "2", "c": "3", "n": "n"}
TOLERANCES = {"voltage_v": (1e-5, 1e-8), "current_a": (1e-6, 1e-8), "power_va": (1e-4, 1e-8)}


def phasor(value):
    if isinstance(value, dict):
        return complex(value["re"], value["im"])
    return complex(*value)


def compare_branches(reference, compare_port):
    for line in reference["lines"]:
        for side in (1, 2):
            for phase, current, potential in zip(
                line["phases"], line["results"][f"currents{side}"],
                line["results"][f"potentials{side}"], strict=True,
            ):
                compare_port("line", line["id"], line[f"bus{side}"], phase, current, potential)
    for transformer in reference["transformers"]:
        for side in ("hv", "lv"):
            for phase, current, potential in zip(
                transformer[f"phases_{side}"], transformer["results"][f"currents_{side}"],
                transformer["results"][f"potentials_{side}"], strict=True,
            ):
                compare_port("transformer", transformer["id"], transformer[f"bus_{side}"], phase,
                             current, potential, core=f"core:{transformer['id']}" if side == "hv" else None)


def compare_injections(reference, original_buses, compare_port):
    for kind, section in (("load", "loads"), ("source", "sources")):
        for element in reference[section]:
            for phase, current, potential in zip(
                element["phases"], element["results"]["currents"], element["results"]["potentials"], strict=True,
            ):
                # The source's ideal internal neutral is grounded, but is not a bus terminal in BMOPF.
                if phase == "n" and phase not in original_buses[element["bus"]]["phases"]:
                    if kind != "source" or abs(phasor(potential)) > 1e-8:
                        raise ValueError("Unexpected internal neutral")
                    continue
                compare_port(kind, element["id"], element["bus"], phase, current, potential)


def compare_results(original, reference, bmopf, tellegen):
    voltages = {(v["bus"], v["terminal"]): phasor(v["voltage"]) for v in tellegen["terminals"]}
    ports = defaultdict(complex)
    for port in tellegen["element_ports"]:
        ports[(port["kind"], port["element"], port["bus"], port["terminal"])] += phasor(
            port["current_into_element"]
        )
    for source in tellegen["source_reactions"]:
        bus = bmopf["voltage_source"][source["source"]]["bus"]
        ports[("source", source["source"], bus, source["terminal"])] -= phasor(source["current_into_network"])
    stats = {category: {"count": 0, "max_absolute_error": 0.0, "max_scaled_error": 0.0}
             for category in TOLERANCES}

    def compare(category, label, actual, expected):
        if not all(math.isfinite(x) for z in (actual, expected) for x in (z.real, z.imag)):
            raise ValueError(f"Non-finite phasor: {label}")
        error = abs(actual - expected)
        absolute, relative = TOLERANCES[category]
        scaled = error / (absolute + relative * max(abs(actual), abs(expected)))
        record = stats[category]
        record["count"] += 1
        if error > record["max_absolute_error"]:
            record["max_absolute_error"] = error
            record["worst_absolute_location"] = label
        if scaled > record["max_scaled_error"]:
            record["max_scaled_error"] = scaled
            record["worst_scaled_location"] = label

    original_buses = {b["id"]: b for b in original["buses"]}
    expected_nodes = {(key, TERMINALS[p]) for key, bus in original_buses.items() for p in bus["phases"]}
    if set(voltages) != expected_nodes:
        raise ValueError("Tellegen bus/terminal inventory differs from original")
    if {b["id"] for b in reference["buses"]} != set(original_buses):
        raise ValueError("Roseau bus inventory differs from original")
    for bus in reference["buses"]:
        for phase, value in zip(bus["phases"], bus["results"]["potentials"], strict=True):
            compare("voltage_v", f"bus:{bus['id']}:{phase}", voltages[(bus["id"], TERMINALS[phase])], phasor(value))

    def compare_port(kind, element, bus, phase, current, potential, core=None):
        key = (kind, element, bus, TERMINALS[phase])
        if key not in ports:
            raise ValueError(f"Missing Tellegen element terminal: {key}")
        actual = ports[key]
        if core is not None:
            actual += ports[("shunt", core, bus, TERMINALS[phase])]
        expected, voltage = phasor(current), phasor(potential)
        label = f"{kind}:{element}:{bus}:{phase}"
        compare("current_a", label, actual, expected)
        compare("power_va", label, voltages[(bus, TERMINALS[phase])] * actual.conjugate(),
                voltage * expected.conjugate())

    compare_branches(reference, compare_port)
    compare_injections(reference, original_buses, compare_port)
    return stats


def main():
    import roseau.load_flow as rlf

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=ROOT / "test/data/FrenchPowerGrids/networks")
    parser.add_argument("--bmopf-dir", type=Path, default=ROOT / "output/FrenchPowerGrids/original")
    parser.add_argument("--tellegen-dir", type=Path, default=ROOT / "output/FrenchPowerGrids/validation/tellegen_pf")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output/FrenchPowerGrids/validation/roseau_comparison")
    parser.add_argument("--tolerance", type=float, default=1e-8, help="Roseau solver residual tolerance")
    args = parser.parse_args()
    rlf.activate_license(os.getenv("ROSEAU_LOAD_FLOW_LICENSE_KEY") or PUBLIC_TRIAL_KEY)
    limit = rlf.get_license().max_nb_buses
    args.output_dir.mkdir(parents=True, exist_ok=True)
    refs_dir = args.output_dir / "references"
    refs_dir.mkdir(exist_ok=True)
    tellegen_report = json.loads((args.tellegen_dir / "summary.json").read_text())
    tellegen_cases = {row["case"]: row for row in tellegen_report["cases"]}
    rows = []
    for path in sorted(args.input_dir.glob("*.json")):
        raw = path.read_bytes()
        original = json.loads(raw)
        row = {"case": path.name, "bus_count": len(original["buses"]),
               "source_sha256": hashlib.sha256(raw).hexdigest()}
        if limit is not None and row["bus_count"] > limit:
            row["status"] = "skipped_license_limit"
            rows.append(row)
            continue
        try:
            bmopf_path = args.bmopf_dir / f"{path.stem}.bmopf.json"
            bmopf_raw = bmopf_path.read_bytes()
            bmopf = json.loads(bmopf_raw)
            entry = tellegen_cases[bmopf_path.name]
            if (entry["status"] != "passed" or entry["input_sha256"] != hashlib.sha256(bmopf_raw).hexdigest()
                    or bmopf["meta"]["provenance"]["source_sha256"] != row["source_sha256"]):
                raise ValueError("Tellegen result or original input provenance does not match")
            with gzip.open(args.tellegen_dir / entry["result_file"], "rt") as stream:
                tellegen = json.load(stream)
            network = rlf.ElectricalNetwork.from_json(path, include_results=False)
            row["roseau_iterations"], row["roseau_residual"] = network.solve_load_flow(
                max_iterations=200, tolerance=args.tolerance,
            )
            reference = network.to_dict(include_results=True)
            result_file = refs_dir / f"{path.stem}.roseau.json.gz"
            with gzip.open(result_file, "wt", encoding="utf-8") as stream:
                json.dump(reference, stream)
            row["reference_file"] = str(result_file.relative_to(args.output_dir))
            stats = compare_results(original, reference, bmopf, tellegen)
            row["comparisons"] = stats
            for category, values in stats.items():
                row[f"max_{category}_error"] = values["max_absolute_error"]
                row[f"max_{category}_scaled_error"] = values["max_scaled_error"]
            row["status"] = "passed" if all(v["max_scaled_error"] <= 1 for v in stats.values()) else "mismatch"
        except Exception as exc:
            row["status"] = "failed"
            row["error"] = str(exc)
        rows.append(row)
        print(f"{path.name}: {row['status']}", flush=True)
    report = {
        "created_utc": datetime.now(UTC).isoformat(), "roseau_load_flow_version": version("roseau-load-flow"),
        "roseau_engine_version": version("roseau-load-flow-engine"), "license_bus_limit": limit,
        "roseau_solver": "newton_goldstein", "roseau_tolerance": args.tolerance,
        "comparison_tolerances": TOLERANCES, "tellegen_binary_sha256": tellegen_report["binary_sha256"],
        "case_count": len(rows), "passed": sum(r["status"] == "passed" for r in rows),
        "skipped_license_limit": sum(r["status"] == "skipped_license_limit" for r in rows), "cases": rows,
    }
    (args.output_dir / "summary.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    flat_rows = [{k: v for k, v in row.items() if k != "comparisons"} for row in rows]
    with (args.output_dir / "summary.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(dict.fromkeys(k for row in flat_rows for k in row)))
        writer.writeheader()
        writer.writerows(flat_rows)
    eligible = len(rows) - report["skipped_license_limit"]
    print(f"Compared {eligible}; passed {report['passed']}; skipped {report['skipped_license_limit']} over license limit")
    raise SystemExit(0 if eligible > 0 and report["passed"] == eligible else 1)


if __name__ == "__main__":
    main()
