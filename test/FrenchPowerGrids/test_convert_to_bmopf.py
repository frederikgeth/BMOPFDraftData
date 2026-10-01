# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Frederik Geth

import copy
import importlib.util
import json
import math
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("convert_to_bmopf", ROOT / "scripts/FrenchPowerGrids/convert_to_bmopf.py")
converter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(converter)


class ConversionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((ROOT / "test/data/FrenchPowerGrids/networks/11_MVFeeder0725.json").read_text())
        cls.target = converter.convert_network(cls.source, name="11_MVFeeder0725", cluster_size=326)

    def test_preserves_inventory_and_total_power(self):
        for src, dst in (("buses", "bus"), ("lines", "line"), ("loads", "load"), ("sources", "voltage_source")):
            self.assertEqual({v["id"] for v in self.source[src]}, set(self.target[dst]))
        for axis, field in ((0, "p_nom"), (1, "q_nom")):
            old = math.fsum(v[axis] for load in self.source["loads"] for v in load["powers"])
            new = math.fsum(v for load in self.target["load"].values() for v in load[field])
            self.assertEqual(old, new)
        self.assertEqual(self.target["extras"]["cluster_size"], 326)

    def test_line_units_and_pi_shunts(self):
        for line in self.source["lines"]:
            params = next(p for p in self.source["lines_params"] if p["id"] == line["params_id"])
            code = self.target["linecode"][params["id"]]
            length = self.target["line"][line["id"]]["length"]
            for i in range(len(line["phases"])):
                for j in range(len(line["phases"])):
                    for axis, prefix in ((0, "R_series"), (1, "X_series")):
                        self.assertAlmostEqual(
                            code[f"{prefix}_{i+1}_{j+1}"] * length,
                            params["z_line"][axis][i][j] * line["length"],
                        )
                    for axis, prefix in ((0, "G"), (1, "B")):
                        total = (code[f"{prefix}_from_{i+1}_{j+1}"] + code[f"{prefix}_to_{i+1}_{j+1}"]) * length
                        self.assertAlmostEqual(total, params["y_shunt"][axis][i][j] * line["length"])

    def test_voltage_bounds_use_original_voltage_pairs(self):
        for bus in self.source["buses"]:
            target = self.target["bus"][bus["id"]]
            prefix = "vpn" if bus["phases"] == "abcn" else "vpp"
            base = bus["nominal_voltage"] / math.sqrt(3) if prefix == "vpn" else bus["nominal_voltage"]
            self.assertEqual(target[prefix + "_min"], [base * bus["min_voltage_level"]] * 3)
            self.assertNotIn("v_min", target)

    def test_delta_and_wye_loads_remain_distinct(self):
        for load in self.source["loads"]:
            target = self.target["load"][load["id"]]
            self.assertEqual(target["configuration"], "WYE" if "n" in load["phases"] else "DELTA")

    def test_source_phasors_and_earth(self):
        for source in self.source["sources"]:
            target = self.target["voltage_source"][source["id"]]
            for original, magnitude, angle in zip(
                source["voltages"], target["v_magnitude"], target["v_angle"], strict=True
            ):
                self.assertAlmostEqual(original[0], magnitude * math.cos(angle))
                self.assertAlmostEqual(original[1], magnitude * math.sin(angle))
        for gc in self.source["ground_connections"]:
            if gc["element"]["type"] == "bus":
                self.assertEqual(self.target["bus"][gc["element"]["id"]]["perfectly_grounded_terminals"], ["n"])

    def test_core_loss_matches_open_circuit_test(self):
        for transformer in self.source["transformers"]:
            params = next(p for p in self.source["transformers_params"] if p["id"] == transformer["params_id"])
            shunt = self.target["shunt"][f"core:{transformer['id']}"]
            # Three delta coils, each seeing rated HV line-to-line voltage.
            loss = 3 * (shunt["G_1_1"] / 2) * params["uhv"] ** 2
            self.assertAlmostEqual(loss, params["p0"])

    def test_dyn11_no_load_phase_displacement(self):
        for transformer in self.target["transformer"]["delta_wye"].values():
            hv = {"1": 1 + 0j, "2": complex(-0.5, -math.sqrt(3) / 2), "3": complex(-0.5, math.sqrt(3) / 2)}
            delta, wye = transformer["terminal_map_from"], transformer["terminal_map_to"]
            lv = {wye[i]: hv[delta[i]] - hv[delta[(i - 1) % 3]] for i in range(3)}
            self.assertAlmostEqual(math.atan2(lv["1"].imag, lv["1"].real), math.pi / 6)

    def test_rejects_unsupported_physics(self):
        mutations = [
            ("transformers_params", "vg", "Dyn1"),
            ("transformers", "tap", 1.025),
            ("loads", "type", "current"),
            ("loads", "connect_neutral", False),
            ("ground_connections", "impedance", [1.0, 0.0]),
            ("sources", "connect_neutral", False),
            ("lines", "length", float("nan")),
            ("loads", "flexible_params", {}),
        ]
        for section, field, value in mutations:
            with self.subTest(section=section, field=field):
                source = copy.deepcopy(self.source)
                source[section][0][field] = value
                with self.assertRaises(converter.ConversionError):
                    converter.convert_network(source, name="bad")

    def test_conversion_is_pure_and_deterministic(self):
        original = copy.deepcopy(self.source)
        first = converter.convert_network(self.source, name="case")
        self.assertEqual(first, converter.convert_network(self.source, name="case"))
        first["extras"]["roseau"]["bus"][self.source["buses"][0]["id"]]["phases"] = "changed"
        self.assertEqual(self.source, original)

    def test_safe_output_and_source_hash(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder) / "case.json", Path(folder) / "case.bmopf.json"
            source.write_text(json.dumps(self.source))
            with self.assertRaises(converter.ConversionError):
                converter.convert_file(source, source, overwrite=True)
            result = converter.convert_file(source, output)
            self.assertEqual(len(result["meta"]["provenance"]["source_sha256"]), 64)
            self.assertEqual(json.loads(output.read_text()), result)
            with self.assertRaises(converter.ConversionError):
                converter.convert_file(source, output)


if __name__ == "__main__":
    unittest.main()
