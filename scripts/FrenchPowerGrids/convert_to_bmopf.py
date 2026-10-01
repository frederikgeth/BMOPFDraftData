# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Frederik Geth

"""Convert this repository's Roseau v5 network files to draft BMOPF JSON.

Uses only the Python standard library; no Roseau installation or licence is needed.
See README.md for the electrical mapping and transformer loading limitation.
"""

import argparse
import copy
import csv
import hashlib
import json
import math
from pathlib import Path

VERSION = "0.1.1"
ROOT = Path(__file__).resolve().parents[2]
SCHEMA_URI = (
    "https://raw.githubusercontent.com/frederikgeth/bmopf-report/main/draft_schema_and_networks/draft_bmopf_schema.json"
)
TERMINALS = {"a": "1", "b": "2", "c": "3", "n": "n"}
SOURCE_URL = (
    "https://www.data.gouv.fr/fr/datasets/"
    "departs-hta-representatifs-pour-lanalyse-des-reseaux-de-distribution-francais/"
)

# Deliberately scoped to the model features present in these 150 feeders.
# Reject new physics rather than retaining it only as metadata.
FIELDS = {
    "grounds": "id",
    "potential_refs": "id ground",
    "buses": "id phases geometry nominal_voltage min_voltage_level max_voltage_level",
    "lines": "id bus1 bus2 phases geometry max_loading params_id length ground",
    "transformers": (
        "id bus_hv bus_lv phases_hv phases_lv connect_neutral_hv connect_neutral_lv max_loading params_id tap"
    ),
    "switches": "",
    "loads": "id bus phases connect_neutral type powers",
    "sources": "id bus phases connect_neutral type voltages",
    "lines_params": "id z_line y_shunt ampacities line_type materials insulators sections",
    "transformers_params": "id vg sn uhv ulv z2 ym i0 p0 psc vsc",
    "ground_connections": "id ground element phase impedance side on_connected",
}


class ConversionError(ValueError):
    """The source contains malformed or unsupported model data."""


def require(condition, message):
    if not condition:
        raise ConversionError(message)


def number(value, label, *, positive=False, nonnegative=False):
    require(isinstance(value, (int, float)) and not isinstance(value, bool), f"{label}: expected a number")
    require(math.isfinite(value), f"{label}: expected a finite number")
    require(not positive or value > 0, f"{label}: expected a positive number")
    require(not nonnegative or value >= 0, f"{label}: expected a nonnegative number")
    return value


def indexed(data, section):
    items = data[section]
    require(isinstance(items, list), f"{section}: expected an array")
    result = {}
    for item in items:
        require(isinstance(item, dict), f"{section}: expected objects")
        require(not (set(item) - set(FIELDS[section].split())), f"{section}: unsupported fields {set(item)}")
        key = item.get("id")
        require(isinstance(key, str) and key, f"{section}: expected a nonempty string ID")
        require(key not in result, f"{section}: duplicate ID {key}")
        result[key] = item
    return result


def terminal_map(phases):
    require(phases in ("abc", "abcn"), f"Unsupported phases: {phases}")
    return [TERMINALS[p] for p in phases]


def check_connection(buses, bus_id, phases):
    require(bus_id in buses, f"Unknown bus: {bus_id}")
    require(set(phases) <= set(buses[bus_id]["phases"]), f"{bus_id}: missing phases {phases}")


def matrix_entries(prefix, matrix, size, scale):
    require(isinstance(matrix, list) and len(matrix) == size, f"{prefix}: wrong matrix size")
    entries = {}
    for i, row in enumerate(matrix, 1):
        require(isinstance(row, list) and len(row) == size, f"{prefix}: matrix must be square")
        for j, value in enumerate(row, 1):
            entries[f"{prefix}_{i}_{j}"] = number(value, prefix) * scale
    return entries


def pair(value, label):
    require(isinstance(value, list) and len(value) == 2, f"{label}: expected [real, imaginary]")
    return complex(number(value[0], label), number(value[1], label))


def convert_network(data, *, name, cluster_size=None):
    """Return a new BMOPF dictionary without mutating the source dictionary."""
    require(data.get("version") == 5 and data.get("is_multiphase") is True, "Expected multiphase Roseau JSON v5")
    require(not (set(data) - (set(FIELDS) | {"version", "is_multiphase", "crs"})), "Unsupported top-level fields")
    require(set(FIELDS) <= set(data), "Missing Roseau component collections")
    require(not data["switches"], "Switch conversion is not implemented")
    tables = {key: indexed(data, key) for key in FIELDS}
    grounds = tables["grounds"]
    require(len(grounds) == 1, "Expected a single common earth")
    ground_id = next(iter(grounds))
    require(len(tables["potential_refs"]) == 1, "Expected a single earth potential reference")
    pref = next(iter(tables["potential_refs"].values()))
    require(pref.get("ground") == ground_id, "Potential reference must fix the common earth")
    require(data.get("crs", {}).get("data") == "EPSG:4326", "Bus longitude/latitude require EPSG:4326 geometry")

    out = {key: {} for key in ("bus", "linecode", "line", "load", "voltage_source", "shunt")}
    out["name"] = name
    out["transformer"] = {"delta_wye": {}}
    out["meta"] = {
        "$schema": SCHEMA_URI,
        "version": "0.1.0",
        "title": name,
        "license": "etalab-2.0",
        "data_sources": [
            {
                "name": "Seddik Yassine Abdelouadoud / Representative French Power Grids",
                "url": SOURCE_URL,
                "format": "Roseau Load Flow JSON",
                "version": "5",
            }
        ],
        "case_study_generator": {"tool": "convert_to_bmopf.py", "version": VERSION},
        "provenance": {
            "terminal_mapping": TERMINALS.copy(),
            "bus_coordinates": {"fields": ["longitude", "latitude"], "crs": "EPSG:4326"},
            "transformer_loading": (
                "s_rating = sn * max_loading. BMOPFTools applies s_rating/3 per coil; "
                "Roseau checks aggregate three-phase power. The OPF feasible sets differ under unbalance."
            ),
        },
    }
    out["extras"] = {
        "roseau": {
            "crs": copy.deepcopy(data.get("crs")),
            "grounds": copy.deepcopy(data["grounds"]),
            "potential_refs": copy.deepcopy(data["potential_refs"]),
            "ground_connections": copy.deepcopy(data["ground_connections"]),
            "bus": {},
            "line": {},
            "transformer": {},
            "line_parameters": copy.deepcopy(tables["lines_params"]),
            "transformer_parameters": copy.deepcopy(tables["transformers_params"]),
        }
    }
    extras = out["extras"]["roseau"]
    if cluster_size is not None:
        out["extras"]["cluster_size"] = cluster_size

    convert_buses(tables, out, extras)
    convert_linecodes(tables, out)
    convert_lines(tables, out, extras, ground_id)
    convert_loads(tables, out)
    convert_sources_and_grounding(tables, out, ground_id)
    convert_transformers(tables, out, extras)
    return out


def convert_buses(tables, out, extras):
    for key, bus in tables["buses"].items():
        phases = bus["phases"]
        target = {"terminal_names": terminal_map(phases)}
        geometry = bus.get("geometry", {})
        require(geometry.get("type") == "Point", f"{key}: expected Point geometry for bus coordinates")
        coordinates = geometry.get("coordinates")
        require(isinstance(coordinates, list) and len(coordinates) == 2, f"{key}: expected [longitude, latitude]")
        longitude = number(coordinates[0], f"{key} longitude")
        latitude = number(coordinates[1], f"{key} latitude")
        require(-180 <= longitude <= 180 and -90 <= latitude <= 90, f"{key}: coordinates outside degree ranges")
        target["longitude"] = longitude
        target["latitude"] = latitude
        nominal = number(bus["nominal_voltage"], key, positive=True)
        lower = number(bus["min_voltage_level"], key, nonnegative=True)
        upper = number(bus["max_voltage_level"], key, positive=True)
        require(lower <= upper, f"{key}: inverted voltage limits")
        prefix = "vpn" if phases == "abcn" else "vpp"
        base = nominal / math.sqrt(3) if phases == "abcn" else nominal
        target[f"{prefix}_min"] = [base * lower] * 3
        target[f"{prefix}_max"] = [base * upper] * 3
        out["bus"][key] = target
        extras["bus"][key] = {k: copy.deepcopy(v) for k, v in bus.items() if k != "id"}


def convert_linecodes(tables, out):
    for key, params in tables["lines_params"].items():
        size = len(params["ampacities"])
        require(size in (3, 4), f"{key}: expected 3 or 4 conductors")
        target = {"source": "import", "i_max": [number(v, key, positive=True) for v in params["ampacities"]]}
        for field, prefixes, scale in (
            ("z_line", ("R_series", "X_series"), 1 / 1000),
            ("y_shunt", ("G_from", "B_from"), 1 / 2000),
        ):
            require(len(params[field]) == 2, f"{key}: expected real/imaginary matrix pair")
            for prefix, matrix in zip(prefixes, params[field], strict=True):
                target.update(matrix_entries(prefix, matrix, size, scale))
                if field == "y_shunt":
                    target.update(matrix_entries(prefix.replace("from", "to"), matrix, size, scale))
        out["linecode"][key] = target


def convert_lines(tables, out, extras, ground_id):
    for key, line in tables["lines"].items():
        phases = line["phases"]
        tm = terminal_map(phases)
        for side in ("bus1", "bus2"):
            check_connection(tables["buses"], line[side], phases)
        require(line.get("ground") == ground_id, f"{key}: line shunts must use the common earth")
        require(line["params_id"] in out["linecode"], f"{key}: unknown line parameters")
        params = tables["lines_params"][line["params_id"]]
        require(len(params["ampacities"]) == len(tm), f"{key}: phase/matrix dimension mismatch")
        loading = number(line["max_loading"], key, positive=True)
        out["line"][key] = {
            "bus_from": line["bus1"],
            "bus_to": line["bus2"],
            "terminal_map_from": tm,
            "terminal_map_to": tm.copy(),
            "linecode": line["params_id"],
            "length": number(line["length"], key, positive=True) * 1000,
            "i_max": [v * loading for v in params["ampacities"]],
        }
        extras["line"][key] = {k: copy.deepcopy(v) for k, v in line.items() if k != "id"}


def convert_loads(tables, out):
    for key, load in tables["loads"].items():
        require(load["type"] == "power", f"{key}: only constant-power loads are supported")
        require(load.get("connect_neutral") in (None, True), f"{key}: disconnected neutrals are unsupported")
        tm = terminal_map(load["phases"])
        check_connection(tables["buses"], load["bus"], load["phases"])
        require(len(load["powers"]) == 3, f"{key}: expected three load dipoles")
        powers = [pair(v, key) for v in load["powers"]]
        out["load"][key] = {
            "bus": load["bus"],
            "configuration": "WYE" if "n" in tm else "DELTA",
            "terminal_map": tm,
            "p_nom": [v.real for v in powers],
            "q_nom": [v.imag for v in powers],
        }


def convert_sources_and_grounding(tables, out, ground_id):
    # Each source has an internal wye neutral grounded at earth, absent from its MV bus.
    grounded_sources = set()
    for key, connection in tables["ground_connections"].items():
        require(connection["ground"] == ground_id, f"{key}: unknown ground")
        require(connection["phase"] == "n" and connection.get("side") is None, f"{key}: unsupported grounding")
        require(pair(connection["impedance"], key) == 0, f"{key}: impedance grounding is unsupported")
        element = connection["element"]
        require(set(element) == {"type", "id"}, f"{key}: unsupported ground connection element")
        if element["type"] == "bus":
            check_connection(tables["buses"], element["id"], "n")
            out["bus"][element["id"]]["perfectly_grounded_terminals"] = ["n"]
        else:
            require(element["type"] == "source" and element["id"] in tables["sources"], f"{key}: unknown element")
            grounded_sources.add(element["id"])

    require(bool(tables["sources"]), "Expected at least one voltage source")
    for key, source in tables["sources"].items():
        require(source["type"] == "voltage" and source["phases"] == "abcn", f"{key}: unsupported source")
        require(source.get("connect_neutral") is None, f"{key}: unsupported source neutral connection")
        require(key in grounded_sources, f"{key}: source internal neutral must be ideally grounded")
        check_connection(tables["buses"], source["bus"], "abc")
        require(tables["buses"][source["bus"]]["phases"] == "abc", f"{key}: expected a three-wire source bus")
        require(len(source["voltages"]) == 3, f"{key}: expected three source voltages")
        voltages = [pair(v, key) for v in source["voltages"]]
        out["voltage_source"][key] = {
            "bus": source["bus"],
            "terminal_map": ["1", "2", "3"],
            "v_magnitude": [abs(v) for v in voltages],
            "v_angle": [math.atan2(v.imag, v.real) for v in voltages],
        }


def convert_transformers(tables, out, extras):
    for key, transformer in tables["transformers"].items():
        require(transformer["params_id"] in tables["transformers_params"], f"{key}: unknown transformer parameters")
        params = tables["transformers_params"][transformer["params_id"]]
        require(params["vg"] == "Dyn11", f"{key}: only Dyn11 is supported")
        require(
            transformer["phases_hv"] == "abc" and transformer["phases_lv"] == "abcn",
            f"{key}: unsupported windings",
        )
        require(transformer.get("connect_neutral_hv") is None, f"{key}: unsupported HV neutral connection")
        require(transformer.get("connect_neutral_lv") in (None, True), f"{key}: disconnected LV neutral")
        require(transformer["tap"] == 1.0, f"{key}: non-unity taps are not supported by the targeted draft schema")
        check_connection(tables["buses"], transformer["bus_hv"], "abc")
        check_connection(tables["buses"], transformer["bus_lv"], "abcn")
        z2, ym = pair(params["z2"], key), pair(params["ym"], key)
        number(z2.real, key, nonnegative=True)
        number(z2.imag, key, nonnegative=True)
        number(ym.real, key, nonnegative=True)
        out["transformer"]["delta_wye"][key] = {
            "bus_from": transformer["bus_hv"],
            "bus_to": transformer["bus_lv"],
            # Reverse BOTH maps: BMOPFTools' backward delta becomes Roseau's forward delta.
            "terminal_map_from": ["1", "3", "2"],
            "terminal_map_to": ["1", "3", "2", "n"],
            "v_nom_from": number(params["uhv"], key, positive=True),
            "v_nom_to": number(params["ulv"], key, positive=True),
            "s_rating": (
                number(params["sn"], key, positive=True) * number(transformer["max_loading"], key, positive=True)
            ),
            "r_series": z2.real,
            "x_series": z2.imag,
        }
        # HV delta core shunt: Ynodal = ym * D.T * D. Do not move it across leakage.
        shunt = {"bus": transformer["bus_hv"], "terminal_map": ["1", "2", "3"]}
        for prefix, value in (("G", ym.real), ("B", ym.imag)):
            shunt.update(
                {f"{prefix}_{i}_{j}": value * (2 if i == j else -1) for i in range(1, 4) for j in range(1, 4)}
            )
        out["shunt"][f"core:{key}"] = shunt
        extras["transformer"][key] = {k: copy.deepcopy(v) for k, v in transformer.items() if k != "id"}


def convert_file(source, destination, *, cluster_size=None, overwrite=False):
    """Convert atomically; never overwrite a source file or an existing output by default."""
    require(source.resolve() != destination.resolve(), "Output must not replace the source file")
    require(overwrite or not destination.exists(), f"Output already exists: {destination}; use --overwrite")
    raw = source.read_bytes()
    result = convert_network(json.loads(raw), name=source.stem, cluster_size=cluster_size)
    result["meta"]["provenance"]["source_file"] = source.name
    result["meta"]["provenance"]["source_sha256"] = hashlib.sha256(raw).hexdigest()
    encoded = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    temp = destination.with_suffix(destination.suffix + ".tmp")
    try:
        temp.write_text(encoded, encoding="utf-8")
        temp.replace(destination)
    finally:
        temp.unlink(missing_ok=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", nargs="?", type=Path, default=ROOT / "test/data/FrenchPowerGrids/networks", help="Roseau JSON file or directory"
    )
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output/FrenchPowerGrids/original")
    parser.add_argument("--cluster-sizes", type=Path, default=ROOT / "test/data/FrenchPowerGrids/Cluster_Size.csv")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    files = sorted(args.input.glob("*.json")) if args.input.is_dir() else [args.input]
    if not files or any(not p.is_file() for p in files):
        parser.error(f"No network JSON files found: {args.input}")
    with args.cluster_sizes.open(encoding="utf-8", newline="") as stream:
        sizes = {row["network_id"]: int(row["cluster_size"]) for row in csv.DictReader(stream)}
    destinations = [args.output_dir / f"{p.stem}.bmopf.json" for p in files]
    if any(p.resolve() == q.resolve() for p in files for q in destinations):
        parser.error("Output must not replace any source file")
    if not args.overwrite and any(p.exists() for p in destinations):
        parser.error("Outputs already exist; choose a new output directory or use --overwrite")
    counts = dict.fromkeys(("bus", "line", "load", "transformer"), 0)
    for source, destination in zip(files, destinations, strict=True):
        try:
            result = convert_file(source, destination, cluster_size=sizes.get(source.stem), overwrite=args.overwrite)
        except (ConversionError, KeyError, TypeError, json.JSONDecodeError) as exc:
            parser.exit(1, f"{source.name}: {exc}\n")
        for key in counts:
            counts[key] += len(result[key]["delta_wye"] if key == "transformer" else result[key])
    print(f"Converted {len(files)} networks to {args.output_dir}: {counts}")


if __name__ == "__main__":
    main()
