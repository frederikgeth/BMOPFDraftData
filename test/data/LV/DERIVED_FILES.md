# LV1 derivatives moved from BMOPFTools

`lv1_14bus.json`, `lv1_14bus_timeseries.json`, and `lv1_14bus_report.md`
are derivatives of the CSIRO Australian MV/LV dataset described in `License.md`
(DOI: 10.25919/ghnz-bk28). They retain its CC BY-NC-SA 4.0 terms and attribution.
They were moved without content changes from BMOPFTools on 2026-09-12:

- `examples/lv1_14bus.json` → `LV/lv1_14bus.json`
- `examples/lv1_14bus_report.md` → `LV/lv1_14bus_report.md`
- `test/data/LV/lv1_14bus_timeseries.json` → `LV/lv1_14bus_timeseries.json`

The original `test/data/LV`, `MV`, `MVLVmeshed`, and combined `Master.dss`
were moved together, preserving relative OpenDSS redirects and licence notices.
Paths above are relative to this repository's `test/data` on the destination side.

BMOPFTools' dataset-backed tests and examples now use the explicitly set
`BMOPF_RESTRICTED_DATA` environment variable pointing to this `test/data`.
The script `BMOPFTools.jl/scripts/regenerate_lv1_14bus.jl` writes derived
JSON files here when that variable is set.
