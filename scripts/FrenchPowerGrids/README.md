# French grid conversion and validation

The four scripts in this directory and the associated tests under `test/FrenchPowerGrids/` use the MIT license.
The source dataset, converted JSONs and derived PF results use `etalab-2.0`; see the adjacent data-directory licenses.
Python conversion and the Tellegen runner require only Python 3.12+ and its standard library. Roseau is required
only for the cross-engine comparison. Julia validation requires a BMOPFTools environment with JSON3 and JSONSchema.

Run these commands from the BMOPFDraftData root; script defaults resolve paths relative to their own location.

```bash
# Regenerate elsewhere to compare with the checked-in output, or use --overwrite explicitly
python3 scripts/FrenchPowerGrids/convert_to_bmopf.py --output-dir /tmp/french-bmopf-regenerated

# Validate coordinates, electrical schemas, source hashes and transformer primitives;
# optionally render neighbouring reports and trees without rewriting the case JSONs
julia --project=/path/to/BMOPFTools.jl scripts/FrenchPowerGrids/validate_bmopf.jl --reports

# Native Tellegen PF: build from your Tellegen checkout first
# cargo build --locked --release --target-dir /tmp/french-tellegen-build \
#   -p tellegen --no-default-features --features mc-pf --example mc_pf
python3 scripts/FrenchPowerGrids/run_tellegen_pf.py --binary /tmp/french-tellegen-build/release/examples/mc_pf

# In a separate environment with Roseau installed:
python -m pip install -r scripts/FrenchPowerGrids/requirements-roseau.txt
python scripts/FrenchPowerGrids/compare_roseau_pf.py

python3 -m unittest discover -s test/FrenchPowerGrids -p 'test_*.py'
```

The converter retains version `0.1.1`: its electrical mapping and deterministic JSON serialization are unchanged.
Only default paths, license headers and documentation were adapted for this repository. Existing outputs retain
their original case-generator metadata and exact hashes. The validator gained defaults for this folder layout and
an optional `--reports` switch; generated reports analyze the electrical projection and do not alter coordinates.

By default the Roseau comparator uses the documented 50-bus public trial license. If
`ROSEAU_LOAD_FLOW_LICENSE_KEY` is configured it uses that license's actual bus limit. It does not split or shrink
feeders to fit a license. The retained comparison uses Roseau 0.15.0 / engine 0.19.1 and covers five original cases.

These are PF cases with original operating bounds. All 150 Tellegen solves converge, but 113 cases contain
undervoltages. Transformer aggregate-versus-per-coil loading constraints differ between source and target, as
explained in `output/FrenchPowerGrids/README.md`. The data does not constitute a curated or certified OPF benchmark set.
