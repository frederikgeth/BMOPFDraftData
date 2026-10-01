# Representative French Power Grids: BMOPF derivatives

150 power-flow models, retaining coupled conductor matrices and explicit LV neutrals. Source data lives in
[`test/data/FrenchPowerGrids/`](../../test/data/FrenchPowerGrids/). Data and data derivatives use
[Etalab Open Licence 2.0](License.md); the new conversion and validation code uses MIT.

## Files and reproduction

- `original/`: the 150 BMOPF JSONs, copied without changing their bytes, plus per-case analysis reports and topology trees.
- `validation/validation_summary.json`: original validation against both tested schemas.
- `validation/revalidation_summary.json`: validation after relocation, including report generation.
- `validation/tellegen_pf/`: all 150 native multiconductor solves and independent audit metrics.
- `validation/roseau_comparison/`: five fresh Roseau engine solves and comparisons; 145 cases were skipped at the trial-license limit.
- `import_manifest.json`: hashes of imported data, evidence and the adapted workflow.

All paths in the commands below are relative to the BMOPFDraftData repository root. The retained validation records
describe the original executions; absolute build paths inside historical provenance are left intact. New runs use
the relocated script defaults. See [`scripts/FrenchPowerGrids/README.md`](../../scripts/FrenchPowerGrids/README.md)
for the commands and dependencies.

## Conversion to BMOPF JSON

`scripts/FrenchPowerGrids/convert_to_bmopf.py` converts the 150 Roseau v5 files directly to the
[Task Force draft BMOPF JSON format](https://github.com/frederikgeth/bmopf-report/tree/main/draft_schema_and_networks).
The conversion uses Python's standard library and requires neither Roseau Load Flow nor a licence key.

```bash
# Regenerate every feeder in a separate directory
python3 scripts/FrenchPowerGrids/convert_to_bmopf.py --output-dir /tmp/french-bmopf-regenerated

# Convert one feeder to a separate directory
python3 scripts/FrenchPowerGrids/convert_to_bmopf.py test/data/FrenchPowerGrids/networks/11_MVFeeder0725.json --output-dir /tmp/french-bmopf

# Regenerate existing outputs explicitly
python3 scripts/FrenchPowerGrids/convert_to_bmopf.py --overwrite

# Run conversion regression checks
python3 -m unittest discover -s test/FrenchPowerGrids -p 'test_*.py' -v
```

The default output directory is `output/FrenchPowerGrids/original`, with files such as `11_MVFeeder0725.bmopf.json`.
Source files are preserved. Outputs include the upstream Open Licence 2.0 attribution, source file SHA-256,
and the corresponding `Cluster_Size.csv` weight. Geometry, CRS, conductor attributes, nameplate/test data,
and original grounding records are retained under `extras.roseau`.
Each electrical bus also carries `longitude` and `latitude` directly, matching the Springfield case convention.
They are copied from the source GeoJSON Point's `[longitude, latitude]` in EPSG:4326, without rounding or reprojection.
For example: `case["bus"][bus_id]["longitude"]` and `case["bus"][bus_id]["latitude"]`.
These two fields extend the strict draft BMOPF bus schema; the original geometry and CRS remain in metadata.
BMOPFTools can retain these fields in memory, but its current `write_bmopf` exporter strips bus coordinates.

The electrical mapping is:

| Roseau model | BMOPF representation |
| :--- | :--- |
| Bus phases `a,b,c,n` | String terminals `"1","2","3","n"` |
| Bus Point coordinates | Direct `longitude` / `latitude` fields in degrees (EPSG:4326) |
| MV voltage limits | Three phase-to-phase `vpp_min` / `vpp_max` values |
| LV voltage limits | Three phase-to-neutral `vpn_min` / `vpn_max` values, using nominal line-to-line voltage divided by √3 |
| Line lengths in km | Lengths in m |
| Series matrices in Ω/km | Full coupled `linecode` matrices in Ω/m |
| Total shunt matrices in S/km | Half at each line end, in S/m; no neutral elimination |
| Line ampacities | Per-conductor `i_max`, multiplied by the line's `max_loading` |
| `abc` power loads | `DELTA`, keeping dipole powers in `ab,bc,ca` order |
| `abcn` power loads | `WYE`, keeping explicit neutral and per-phase powers |
| Grounded source internal neutral | Three fixed phase-to-earth source phasors; angles in radians |
| Ideal LV bus grounding | `perfectly_grounded_terminals: ["n"]` |
| Dyn11 transformers | `delta_wye` with both terminal maps ordered `1,3,2` (plus LV neutral), preserving the LV +30° displacement |
| Transformer `z2` | Wye-side `r_series` / `x_series` in Ω |
| Transformer `ym` | Separate HV delta core-loss shunt, with nodal matrix `ym · DᵀD`; no referral across leakage |

The load model is omitted deliberately: constant power is the default in both the Task Force draft and BMOPFTools.
Separate core shunts and combined wye-side leakage fields keep the electrical model compatible with both schemas.
Direct bus coordinates use the Springfield extension described above.
The Dyn11 mapping follows
[Roseau's winding equations](https://roseau-load-flow.roseautechnologies.com/en/stable/models/Transformer/Three_Phase_Transformer.html)
and [BMOPFTools' transformer conventions](https://github.com/frederikgeth/BMOPFTools.jl/blob/main/docs/src/transformer_models.md).

**Transformer loading has a documented limitation:** the exported `s_rating` is `sn × max_loading` (1.1 × nameplate
in these files). BMOPFTools enforces a separate `s_rating/3` limit on each coil, whereas Roseau checks aggregate
three-phase apparent power. Under unbalanced loading the feasible sets differ. The original nameplate rating and
loading factor remain in metadata; the winding impedance and excitation are preserved independently of that cap.
The separate HV shunt also means the target transformer's own loading constraint excludes core excitation;
Roseau includes that contribution in its HV loading. Thus the loading constraints are not exactly equivalent even
though the complete transformer terminal physics matches.
The converter does not add DER, generator costs, or synthesised operational limits, and conversion alone does not
establish OPF feasibility.

The supported scope is the features present in this repository: multiphase v5 JSON, three/four-wire lines,
three-dipole constant-power loads, unity-tap Dyn11 transformers, one common earth, and ideal source/LV grounding.
Other vector groups, non-unity taps, switches, impedance grounding, disconnected neutrals, flexible loads, and
unknown fields are rejected with an error rather than silently dropped.

Validate with a Julia environment containing [BMOPFTools](https://github.com/frederikgeth/BMOPFTools.jl):

```bash
julia --project=/path/to/BMOPFTools.jl scripts/FrenchPowerGrids/validate_bmopf.jl output/FrenchPowerGrids/original test/data/FrenchPowerGrids/networks

# Optionally validate the electrical model against the Task Force schema as well
julia --project=/path/to/BMOPFTools.jl scripts/FrenchPowerGrids/validate_bmopf.jl output/FrenchPowerGrids/original test/data/FrenchPowerGrids/networks /path/to/draft_bmopf_schema.json
```

The validator checks coordinate types and degree ranges, then validates the electrical JSON before normalization,
excluding only the two explicitly checked coordinate extension fields. It runs BMOPFTools analysis, verifies source
hashes and exact coordinate equality with source bus Points, and compares
every transformer's complete primitive admittance (including its HV core shunt) with an independent construction
from Roseau's equations. It fails on schema/structural errors or transformer mismatches and reports the remaining
analysis findings separately. It does not run a power flow or certify a solved-network comparison with Roseau.
Two catalogue/preflight informational findings need explanation: its field catalogue flags
`extras` even though the JSON schema permits it, and its preflight check reports `I.PRE.NO_VOLT_BOUNDS` because it
looks for phase-to-ground bounds. The exported `vpn`/`vpp` bounds preserve the source voltage definitions and are
recognized by the solver; adding phase-to-ground limits to suppress that finding would change the model.
The initial implementation targets BMOPFTools revision `4f81be3dc85e44603d7232502d0102f46b118bda`, whose bundled schema
SHA-256 is `9dcf693edd7403455185b2e9eb7dd37f49351867821b4fa65d2fd6434fe8cacc`.
BMOPF is a draft; the schema URI identifies the format family, while this revision/hash records the tested tooling.
Validation covers all 150 feeders, including 89,870 direct bus coordinate pairs, with zero electrical schema or
structural errors. All 5,500 transformer primitive comparisons passed. The Python regression suite contains ten checks.

### Multiconductor power flow with Tellegen

All 150 converted feeders have been solved with the native `mc_pf` example from the local
[Tellegen](https://github.com/frederikgeth/tellegen), at revision
`6f0be90f561ad4b67d35848c4c70f98a3154e004` with the checkout's existing Cargo manifest change.
The runs preserve the full conductor matrices and explicit LV neutrals. The voltage envelope is disabled so
loads retain their original constant-power equations; the iteration limit is 200 and solver tolerances are unchanged.

To reproduce, build the example from the Tellegen checkout:

```bash
cargo build --locked --release --target-dir /tmp/french-tellegen-build \
  -p tellegen --no-default-features --features mc-pf --example mc_pf
```

Then run from this repository:

```bash
python3 scripts/FrenchPowerGrids/run_tellegen_pf.py --binary /tmp/french-tellegen-build/release/examples/mc_pf
```

All 150 cases converged in 5–26 iterations, using one matrix factorization each. The largest solver physical KCL
residual was `4.81e-8 A`. The runner independently checks terminal and component inventories, KCL, coupled line
pi-model equations, Dyn11 winding equations, core shunts, constant load powers, and complex-power balance.
All checks passed; the largest device-equation current residual was `1.29e-8 A`, and the largest complex-power
balance error was `5.62e-4 VA`.

Convergence does not establish operating-limit feasibility: 113 cases contain 219 phase-to-neutral voltages below
the input's 0.90 p.u. lower bound, with a minimum of 0.8806 p.u. The runner reports these separately from convergence
and electrical-equation checks. It does not certify line or transformer loading limits or compare solved voltages
with a Roseau solve; that comparison is a separate step below.

Per-case metrics are saved in `output/FrenchPowerGrids/validation/tellegen_pf/summary.json` and `summary.csv`; full terminal and element-port
results are compressed under `output/FrenchPowerGrids/validation/tellegen_pf/results/`. The initial run also records the local build command,
checkout status and source hashes in `build_provenance.json`; the runner records the executable and input hashes.
These generated reports are retained under `output/FrenchPowerGrids/validation/`.

### Direct comparison with Roseau's engine

`scripts/FrenchPowerGrids/compare_roseau_pf.py` solves the original Roseau JSON inputs and compares their results with the saved
Tellegen solves. It uses an existing `ROSEAU_LOAD_FLOW_LICENSE_KEY` when configured, otherwise Roseau's documented
[public trial license](https://roseau-load-flow.roseautechnologies.com/en/stable/License.html).
The activated license's bus limit determines which original feeders can run; the script skips larger feeders
without altering or splitting their models.

```bash
# In a Python 3.12+ environment with Roseau installed
python -m pip install 'roseau-load-flow==0.15.0'
python scripts/FrenchPowerGrids/compare_roseau_pf.py
```

The direct comparison passed for all five feeders covered by the public license's 50-bus limit:

| Feeder | Buses | Dyn11 transformers |
| :--- | ---: | ---: |
| `24_MVFeeder1514` | 17 | 1 |
| `44_MVFeeder1963` | 45 | 5 |
| `44_MVFeeder2707` | 5 | 0 |
| `52_MVFeeder1850` | 44 | 3 |
| `84_MVFeeder2419` | 5 | 0 |

The tested versions were `roseau-load-flow 0.15.0` and `roseau-load-flow-engine 0.19.1`, with the default
`newton_goldstein` solver and residual tolerance `1e-8`. Across 420 bus-conductor potentials and 1,440 element-terminal
current/power comparisons, the largest complex differences were `2.74e-9 V`, `1.88e-8 A`, and `5.80e-5 VA`.
The comparison uses conductor identities and original bus IDs, with no fitted phase rotation. It sums the separate
BMOPF core-shunt current into the transformer's HV current and reverses Tellegen's source injection sign to match
Roseau's current-into-element convention. The source's grounded internal neutral is omitted from the bus-terminal
comparison because it is eliminated analytically during conversion.

The acceptance tolerances are absolute plus relative: `1e-5 V + 1e-8 × magnitude`,
`1e-6 A + 1e-8 × magnitude`, and `1e-4 VA + 1e-8 × magnitude`. Input and executable hashes link the two sets of
results to the conversion and the original files. Reports are in `output/FrenchPowerGrids/validation/roseau_comparison/summary.json` and
`summary.csv`; full Roseau results are saved under `references/` as compressed JSON. The other 145 feeders are
explicitly marked `skipped_license_limit`, so this is direct engine agreement for five cases, not certification of
the complete dataset. An unlimited Roseau license allows the same script to compare all 150 cases.

Public reference material is also available:

- The [Roseau test fixtures](https://github.com/RoseauTechnologies/Roseau_Load_Flow/tree/aaae96f3db7e53cf4de2c894903e087d96c9d5e4/roseau/load_flow/models/tests/data)
  include saved complex voltages and currents, for example
  [an unbalanced three-phase network with line shunts](https://github.com/RoseauTechnologies/Roseau_Load_Flow/blob/aaae96f3db7e53cf4de2c894903e087d96c9d5e4/roseau/load_flow/models/tests/data/Network_3Ph_Unbalanced_Shunt.json).
  These are reference results for those small networks, rather than these 150 feeders.
- [CIRED 2024](https://github.com/RoseauTechnologies/2024_CIRED) contains the hosting-capacity paper's reproduction
  notebook and input load/PV profiles. Its notebook has no saved numerical outputs in the inspected revision
  `0d17d52a28aca19b688b718450ed08b9a1972671`.
- [Roseau's OpenDSS tutorials](https://github.com/RoseauTechnologies/Roseau_Load_Flow_Tutorials/tree/0d2baa633b379e68f30ca1281b8c28a6ea112aa7/OpenDSS/Tutorial_2)
  provide code to compare both engines on unbalanced LV models, including an explicit-neutral case. The inspected
  explicit-neutral notebook likewise contains no saved numerical outputs.

