# Texas7k p1uhs0_1247 reproduction workflow

This adapter converts one SMART-DS v0.9 / 2016 / Full_Texas substation, with
six feeders, to a fixed nominal-load BMOPF PF snapshot. It is deliberately
bounded to this input. Full-Texas processing and annual time series are outside
this pilot. The scripts are MIT licensed; source and derivative data follow
the OEDI registry's CC BY 3.0 US license. See
[source attribution and license evidence](../../test/data/Texas7k/SOURCE_NOTICE.md).

## Dependencies and source verification

Use Python 3.12. From the BMOPFDraftData root:

```sh
python3.12 -m venv /tmp/texas7k-venv
/tmp/texas7k-venv/bin/python -m pip install -r scripts/Texas7k/requirements.txt
/tmp/texas7k-venv/bin/python scripts/Texas7k/download_substation.py \
  --manifest test/data/Texas7k/source_manifest.json \
  --destination test/data/Texas7k/p1uhs0_1247
```

The download helper verifies existing files without network access, downloads
only missing manifest entries, and checks all 62 byte sizes and SHA-256 hashes.
The conversion driver also verifies the manifest before processing. Original
files are never edited. No external profile CSVs are needed.

Use a PowerIO CLI built from revision
`597fa930990d7b9d7278a0f7857ef1406859fc1c` (version 0.11.2), and its vendored
`powerio-dist/schemas/bmopf/0.2.0/bmopf.schema.json`. Its SHA-256 must be
`74d6c6de3637d52e42a26c4cb0584f51df70d69f360b236cf5e23afaf7669462`.
The schema is a pinned proposal; the adapter does not retrieve a moving schema.

Tellegen must provide the `mc_pf` native example. At the Tellegen repository
root it can be built with:

```sh
cargo build --release -p tellegen --example mc_pf --features mc-pf
```

The validation checkout was `6f0be90f561ad4b67d35848c4c70f98a3154e004`.
The committed reference used a cached executable whose build revision was not
independently established; `software_provenance.json` identifies the actual
binary by hash. Record your checkout and binary hash when using a fresh build.

## Reproduce the model, references, summary and figures

Choose a fresh working directory and supply the executable/schema paths:

```sh
/tmp/texas7k-venv/bin/python scripts/Texas7k/convert_substation.py \
  --source test/data/Texas7k/p1uhs0_1247 \
  --workdir /tmp/texas7k-reproduction \
  --powerio /path/to/powerio \
  --schema /path/to/powerio/powerio-dist/schemas/bmopf/0.2.0/bmopf.schema.json \
  --tellegen /path/to/tellegen/target/release/examples/mc_pf
```

The driver solves OpenDSS static controls, freezes regulator taps, retains
finite closed-switch impedances and asymmetric split-phase leakage equivalents,
rescales tap-dependent impedances, sets continuous line ratings, and adds
geographic coordinates to all original and internal buses. It validates the
electrical projection against the pinned schema, checking the two direct bus
coordinate extensions separately.

Outputs are under the workdir's `output/`: the BMOPF model, comparison reports,
transformer mapping, diagnostics, compressed OpenDSS/reference/parameter data,
PF summary, PNG/SVG figure, executable hashes and dependency versions. The
driver discards the large native port dump after computing the summary and
figure. Intermediate OpenDSS working models remain outside the repository.

Physics checks cover all 38,218 original voltage nodes. The allowed maximum
complex-voltage error is 3e-6 pu against the unchanged OpenDSS equipment and
5e-8 pu when only its numerical antifloat shunts are disabled. Independent
OpenDSS loading checks are included in the PF summary. Small differences in
timings, plot metadata, or floating-point rounding are not electrical changes.

## Check Tellegen geographic ingestion

Use Node.js and the built Tellegen engine WASM package containing `tellegen.js`
and `tellegen_bg.wasm`. The check exercises the browser viewer's ingestion API:

```sh
node scripts/Texas7k/check_map_import.mjs \
  output/Texas7kPilot/p1uhs0_1247.bmopf.json \
  /path/to/tellegen/packages/engine/dist/wasm-pkg \
  /tmp/texas7k-map-import-report.json
```

It requires geographic mode, every bus placed at its JSON longitude/latitude,
multiconductor PF support, and no import diagnostics. WASM and loader hashes
are recorded. This check is separate from the native PF solve.

## Regenerate only the PF summary and figure

Run the native example on an existing model, retaining its full result in a
temporary file:

```sh
/path/to/mc_pf output/Texas7kPilot/p1uhs0_1247.bmopf.json \
  output/Texas7kPilot/tellegen_options.json > /tmp/texas7k-native-result.json
/tmp/texas7k-venv/bin/python scripts/Texas7k/summarize_pf.py \
  --model output/Texas7kPilot/p1uhs0_1247.bmopf.json \
  --solution /tmp/texas7k-native-result.json \
  --opendss-snapshot /tmp/texas7k-reproduction/output/fixed_snapshot.dss \
  --output /tmp/texas7k-pf-figures
/tmp/texas7k-venv/bin/python scripts/Texas7k/plot_pf.py \
  --results /tmp/texas7k-pf-figures
```

Omit `--opendss-snapshot` to summarize Tellegen alone; this omits the independent
OpenDSS loading check and its transformer normal ratings. The 0.95/1.05 pu
screening thresholds are descriptive, not case constraints. The pilot has
voltage and loading violations and is not a curated OPF benchmark.
