# BMOPF Network Summary: 11_MVFeeder3385

**Generated:** 2026-10-01 23:33:56  
**Findings:** 0 errors · 7 warnings · 90 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 510 |  |
| line | 493 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 860 | 10.23 MW, 3.07 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 16 |  |
| switch | 0 |  |
| transformer | 16 | Dyn11×16 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 69 | 68 | 10 | 0 |
| LV_236V | 236.0 V | 441 | 425 | 850 | 0 |

**Transformer transitions:**

- `11_MVLV18919_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV13574_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV48133_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV34525_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV59046_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV21406_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV71670_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV40086_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV22820_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV04376_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV54301_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV42629_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV69813_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV72171_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV22805_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV22790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 17 |
| Degree-1 buses | 202 |
| Tree depth (max hops) | 48 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 510 | 1 | 509 | 0 | 0 | 0 |
| Tier LV_236V | 441 | 16 | 425 | 0 | 0 | 0 |
| Tier MV_11.8kV | 69 | 1 | 68 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 16; skipped invalid branches: 0.

Galvanic zones: 17; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_MVBus58145 | MV_11.8kV | 69 | 0 | 0 | 16 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1971 declared bus terminals; 1904 mapped line/closed-switch conductor edges; 67 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 16 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 1.1e6 | 10.504 | 2580 |
| q_nom | 0.0 | 329000.0 | 10.504 | 2580 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.317 | 928.0 | 1.773 | 493 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 880000.0 | 0.6 | 16 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 746 of 860 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121357_consumption' has phase imbalance of 30.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121309_consumption' has phase imbalance of 82.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121184_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121520_consumption' has phase imbalance of 33.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121270_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121331_consumption' has phase imbalance of 57.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121485_consumption' has phase imbalance of 43.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121493_consumption' has phase imbalance of 64.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1331964_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121562_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121110_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121575_consumption' has phase imbalance of 20.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121272_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121526_consumption' has phase imbalance of 32.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121365_consumption' has phase imbalance of 41.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121444_consumption' has phase imbalance of 37.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121191_consumption' has phase imbalance of 30.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121170_consumption' has phase imbalance of 41.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121176_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121147_consumption' has phase imbalance of 44.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121423_consumption' has phase imbalance of 43.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121366_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121484_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121618_consumption' has phase imbalance of 128.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121409_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121464_consumption' has phase imbalance of 69.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121387_consumption' has phase imbalance of 63.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121438_consumption' has phase imbalance of 67.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121598_consumption' has phase imbalance of 47.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121470_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121323_consumption' has phase imbalance of 25.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121610_consumption' has phase imbalance of 89.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121422_consumption' has phase imbalance of 34.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121127_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121432_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121274_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121497_consumption' has phase imbalance of 57.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121504_consumption' has phase imbalance of 37.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121397_consumption' has phase imbalance of 22.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121321_consumption' has phase imbalance of 62.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121284_consumption' has phase imbalance of 36.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121530_consumption' has phase imbalance of 30.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121307_consumption' has phase imbalance of 119.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121119_consumption' has phase imbalance of 35.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121537_consumption' has phase imbalance of 52.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121153_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121159_consumption' has phase imbalance of 52.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121301_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121461_consumption' has phase imbalance of 37.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121587_consumption' has phase imbalance of 88.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121437_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121421_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121138_consumption' has phase imbalance of 36.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121273_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121458_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121308_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121393_consumption' has phase imbalance of 34.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121588_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121401_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121579_consumption' has phase imbalance of 47.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121324_consumption' has phase imbalance of 23.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121146_consumption' has phase imbalance of 62.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121435_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121139_consumption' has phase imbalance of 74.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121608_consumption' has phase imbalance of 37.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121214_consumption' has phase imbalance of 88.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121356_consumption' has phase imbalance of 22.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121420_consumption' has phase imbalance of 53.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1330783_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121276_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0121346_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 860 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0121552' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0121234' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0121542' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 10.23 MW |
| Total load Q | 3.07 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV18919_Transformer | 176.0 kVA | 0.0% |
| 11_MVLV13574_Transformer | 880.0 kVA | 75.5% |
| 11_MVLV48133_Transformer | 440.0 kVA | 61.8% |
| 11_MVLV34525_Transformer | 440.0 kVA | 70.2% |
| 11_MVLV59046_Transformer | 110.0 kVA | 22.7% |
| 11_MVLV21406_Transformer | 275.0 kVA | 66.6% |
| 11_MVLV71670_Transformer | 440.0 kVA | 90.5% ⚠ |
| 11_MVLV40086_Transformer | 440.0 kVA | 60.8% |
| 11_MVLV22820_Transformer | 110.0 kVA | 1.9% |
| 11_MVLV04376_Transformer | 693.0 kVA | 45.2% |
| 11_MVLV54301_Transformer | 550.0 kVA | 81.7% |
| 11_MVLV42629_Transformer | 693.0 kVA | 94.3% ⚠ |
| 11_MVLV69813_Transformer | 110.0 kVA | 13.6% |
| 11_MVLV72171_Transformer | 693.0 kVA | 66.6% |
| 11_MVLV22805_Transformer | 693.0 kVA | 66.0% |
| 11_MVLV22790_Transformer | 110.0 kVA | 14.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (10.23 MW).
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '11_MVLV71670_Transformer' is at 90.5% utilisation at nominal load — little OPF headroom.
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '11_MVLV42629_Transformer' is at 94.3% utilisation at nominal load — little OPF headroom.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '11_LVBus0121196' (LV, 0.24 kV) has an electrical reach of 2.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '11_LVBus0121397' (LV, 0.24 kV) has an electrical reach of 12.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '11_LVBus0121542' (LV, 0.24 kV) has an electrical reach of 2.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 510 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 510 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 69 |
| LV_236V | 4-wire | 441 / 441 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 441 |
| Neutral branches | 425 |
| Grounding points | 16 |
| Neutral sections | 16 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| decoupled | 1 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 2 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 69 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 74 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 61 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 59 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 56 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.DECOUPLED_PHASES]** 1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 17 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1240.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 441 / 69 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 747 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 747 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0121110_production, 11_LVBus0121112_production, 11_LVBus0121113_consumption, 11_LVBus0121113_production, 11_LVBus0121115_consumption, 11_LVBus0121115_production, 11_LVBus0121116_production, 11_LVBus0121117_consumption, 11_LVBus0121117_production, 11_LVBus0121118_production, 11_LVBus0121119_production, 11_LVBus0121121_consumption, 11_LVBus0121121_production, 11_LVBus0121122_production, 11_LVBus0121123_consumption, 11_LVBus0121123_production, 11_LVBus0121124_production, 11_LVBus0121126_consumption, 11_LVBus0121126_production, 11_LVBus0121127_production, 11_LVBus0121128_consumption, 11_LVBus0121128_production, 11_LVBus0121129_consumption, 11_LVBus0121129_production, 11_LVBus0121130_consumption, 11_LVBus0121130_production, 11_LVBus0121131_consumption, 11_LVBus0121131_production, 11_LVBus0121132_consumption, 11_LVBus0121132_production, 11_LVBus0121133_consumption, 11_LVBus0121133_production, 11_LVBus0121135_consumption, 11_LVBus0121135_production, 11_LVBus0121136_consumption, 11_LVBus0121136_production, 11_LVBus0121137_consumption, 11_LVBus0121137_production, 11_LVBus0121138_production, 11_LVBus0121139_production, 11_LVBus0121141_consumption, 11_LVBus0121141_production, 11_LVBus0121142_consumption, 11_LVBus0121142_production, 11_LVBus0121143_consumption, 11_LVBus0121143_production, 11_LVBus0121144_consumption, 11_LVBus0121144_production, 11_LVBus0121145_consumption, 11_LVBus0121145_production, 11_LVBus0121146_production, 11_LVBus0121147_production, 11_LVBus0121149_consumption, 11_LVBus0121149_production, 11_LVBus0121150_consumption, 11_LVBus0121150_production, 11_LVBus0121151_consumption, 11_LVBus0121151_production, 11_LVBus0121152_consumption, 11_LVBus0121152_production, 11_LVBus0121153_production, 11_LVBus0121154_consumption, 11_LVBus0121154_production, 11_LVBus0121156_consumption, 11_LVBus0121156_production, 11_LVBus0121157_consumption, 11_LVBus0121157_production, 11_LVBus0121158_consumption, 11_LVBus0121158_production, 11_LVBus0121159_production, 11_LVBus0121160_consumption, 11_LVBus0121160_production, 11_LVBus0121162_consumption, 11_LVBus0121162_production, 11_LVBus0121163_consumption, 11_LVBus0121163_production, 11_LVBus0121164_consumption, 11_LVBus0121164_production, 11_LVBus0121165_consumption, 11_LVBus0121165_production, 11_LVBus0121166_consumption, 11_LVBus0121166_production, 11_LVBus0121167_consumption, 11_LVBus0121167_production, 11_LVBus0121168_consumption, 11_LVBus0121168_production, 11_LVBus0121169_consumption, 11_LVBus0121169_production, 11_LVBus0121170_production, 11_LVBus0121172_consumption, 11_LVBus0121172_production, 11_LVBus0121173_consumption, 11_LVBus0121173_production, 11_LVBus0121174_consumption, 11_LVBus0121174_production, 11_LVBus0121175_consumption, 11_LVBus0121175_production, 11_LVBus0121176_production, 11_LVBus0121177_consumption, 11_LVBus0121177_production, 11_LVBus0121178_consumption, 11_LVBus0121178_production, 11_LVBus0121179_consumption, 11_LVBus0121179_production, 11_LVBus0121180_consumption, 11_LVBus0121180_production, 11_LVBus0121181_consumption, 11_LVBus0121181_production, 11_LVBus0121182_consumption, 11_LVBus0121182_production, 11_LVBus0121183_consumption, 11_LVBus0121183_production, 11_LVBus0121184_production, 11_LVBus0121186_consumption, 11_LVBus0121186_production, 11_LVBus0121187_consumption, 11_LVBus0121187_production, 11_LVBus0121188_consumption, 11_LVBus0121188_production, 11_LVBus0121189_consumption, 11_LVBus0121189_production, 11_LVBus0121190_production, 11_LVBus0121191_production, 11_LVBus0121192_consumption, 11_LVBus0121192_production, 11_LVBus0121193_consumption, 11_LVBus0121193_production, 11_LVBus0121194_consumption, 11_LVBus0121194_production, 11_LVBus0121196_consumption, 11_LVBus0121196_production, 11_LVBus0121198_consumption, 11_LVBus0121198_production, 11_LVBus0121200_consumption, 11_LVBus0121200_production, 11_LVBus0121202_consumption, 11_LVBus0121202_production, 11_LVBus0121204_consumption, 11_LVBus0121204_production, 11_LVBus0121206_consumption, 11_LVBus0121206_production, 11_LVBus0121208_production, 11_LVBus0121210_consumption, 11_LVBus0121210_production, 11_LVBus0121212_consumption, 11_LVBus0121212_production, 11_LVBus0121214_production, 11_LVBus0121216_consumption, 11_LVBus0121216_production, 11_LVBus0121218_consumption, 11_LVBus0121218_production, 11_LVBus0121220_consumption, 11_LVBus0121220_production, 11_LVBus0121222_consumption, 11_LVBus0121222_production, 11_LVBus0121224_consumption, 11_LVBus0121224_production, 11_LVBus0121226_consumption, 11_LVBus0121226_production, 11_LVBus0121228_consumption, 11_LVBus0121228_production, 11_LVBus0121229_production, 11_LVBus0121230_consumption, 11_LVBus0121230_production, 11_LVBus0121232_consumption, 11_LVBus0121232_production, 11_LVBus0121234_consumption, 11_LVBus0121234_production, 11_LVBus0121236_consumption, 11_LVBus0121236_production, 11_LVBus0121238_consumption, 11_LVBus0121238_production, 11_LVBus0121240_production, 11_LVBus0121241_consumption, 11_LVBus0121241_production, 11_LVBus0121242_consumption, 11_LVBus0121242_production, 11_LVBus0121244_consumption, 11_LVBus0121244_production, 11_LVBus0121245_consumption, 11_LVBus0121245_production, 11_LVBus0121246_consumption, 11_LVBus0121246_production, 11_LVBus0121247_consumption, 11_LVBus0121247_production, 11_LVBus0121248_consumption, 11_LVBus0121248_production, 11_LVBus0121249_production, 11_LVBus0121251_consumption, 11_LVBus0121251_production, 11_LVBus0121252_consumption, 11_LVBus0121252_production, 11_LVBus0121254_consumption, 11_LVBus0121254_production, 11_LVBus0121255_consumption, 11_LVBus0121255_production, 11_LVBus0121256_consumption, 11_LVBus0121256_production, 11_LVBus0121258_consumption, 11_LVBus0121258_production, 11_LVBus0121259_consumption, 11_LVBus0121259_production, 11_LVBus0121261_consumption, 11_LVBus0121261_production, 11_LVBus0121263_consumption, 11_LVBus0121263_production, 11_LVBus0121265_consumption, 11_LVBus0121265_production, 11_LVBus0121266_consumption, 11_LVBus0121266_production, 11_LVBus0121267_consumption, 11_LVBus0121267_production, 11_LVBus0121268_consumption, 11_LVBus0121268_production, 11_LVBus0121269_consumption, 11_LVBus0121269_production, 11_LVBus0121270_production, 11_LVBus0121271_consumption, 11_LVBus0121271_production, 11_LVBus0121272_production, 11_LVBus0121273_production, 11_LVBus0121274_production, 11_LVBus0121276_production, 11_LVBus0121277_consumption, 11_LVBus0121277_production, 11_LVBus0121278_consumption, 11_LVBus0121278_production, 11_LVBus0121279_consumption, 11_LVBus0121279_production, 11_LVBus0121280_consumption, 11_LVBus0121280_production, 11_LVBus0121281_consumption, 11_LVBus0121281_production, 11_LVBus0121282_consumption, 11_LVBus0121282_production, 11_LVBus0121283_consumption, 11_LVBus0121283_production, 11_LVBus0121284_production, 11_LVBus0121285_consumption, 11_LVBus0121285_production, 11_LVBus0121286_consumption, 11_LVBus0121286_production, 11_LVBus0121288_consumption, 11_LVBus0121288_production, 11_LVBus0121289_consumption, 11_LVBus0121289_production, 11_LVBus0121290_consumption, 11_LVBus0121290_production, 11_LVBus0121291_consumption, 11_LVBus0121291_production, 11_LVBus0121292_consumption, 11_LVBus0121292_production, 11_LVBus0121293_consumption, 11_LVBus0121293_production, 11_LVBus0121295_consumption, 11_LVBus0121295_production, 11_LVBus0121296_consumption, 11_LVBus0121296_production, 11_LVBus0121297_consumption, 11_LVBus0121297_production, 11_LVBus0121298_consumption, 11_LVBus0121298_production, 11_LVBus0121299_consumption, 11_LVBus0121299_production, 11_LVBus0121300_consumption, 11_LVBus0121300_production, 11_LVBus0121301_production, 11_LVBus0121302_consumption, 11_LVBus0121302_production, 11_LVBus0121303_consumption, 11_LVBus0121303_production, 11_LVBus0121304_consumption, 11_LVBus0121304_production, 11_LVBus0121305_consumption, 11_LVBus0121305_production, 11_LVBus0121306_production, 11_LVBus0121307_production, 11_LVBus0121308_production, 11_LVBus0121309_production, 11_LVBus0121311_consumption, 11_LVBus0121311_production, 11_LVBus0121312_consumption, 11_LVBus0121312_production, 11_LVBus0121313_consumption, 11_LVBus0121313_production, 11_LVBus0121314_consumption, 11_LVBus0121314_production, 11_LVBus0121315_production, 11_LVBus0121316_consumption, 11_LVBus0121316_production, 11_LVBus0121317_consumption, 11_LVBus0121317_production, 11_LVBus0121318_consumption, 11_LVBus0121318_production, 11_LVBus0121319_consumption, 11_LVBus0121319_production, 11_LVBus0121320_consumption, 11_LVBus0121320_production, 11_LVBus0121321_production, 11_LVBus0121322_consumption, 11_LVBus0121322_production, 11_LVBus0121323_production, 11_LVBus0121324_production, 11_LVBus0121325_production, 11_LVBus0121327_consumption, 11_LVBus0121327_production, 11_LVBus0121329_consumption, 11_LVBus0121329_production, 11_LVBus0121331_production, 11_LVBus0121333_consumption, 11_LVBus0121333_production, 11_LVBus0121334_consumption, 11_LVBus0121334_production, 11_LVBus0121335_consumption, 11_LVBus0121335_production, 11_LVBus0121337_consumption, 11_LVBus0121337_production, 11_LVBus0121339_consumption, 11_LVBus0121339_production, 11_LVBus0121340_consumption, 11_LVBus0121340_production, 11_LVBus0121342_consumption, 11_LVBus0121342_production, 11_LVBus0121344_consumption, 11_LVBus0121344_production, 11_LVBus0121346_production, 11_LVBus0121348_consumption, 11_LVBus0121348_production, 11_LVBus0121349_consumption, 11_LVBus0121349_production, 11_LVBus0121350_production, 11_LVBus0121351_consumption, 11_LVBus0121351_production, 11_LVBus0121352_consumption, 11_LVBus0121352_production, 11_LVBus0121353_consumption, 11_LVBus0121353_production, 11_LVBus0121354_consumption, 11_LVBus0121354_production, 11_LVBus0121355_consumption, 11_LVBus0121355_production, 11_LVBus0121356_production, 11_LVBus0121357_production, 11_LVBus0121359_consumption, 11_LVBus0121359_production, 11_LVBus0121360_production, 11_LVBus0121361_consumption, 11_LVBus0121361_production, 11_LVBus0121362_consumption, 11_LVBus0121362_production, 11_LVBus0121363_consumption, 11_LVBus0121363_production, 11_LVBus0121364_consumption, 11_LVBus0121364_production, 11_LVBus0121365_production, 11_LVBus0121366_production, 11_LVBus0121367_consumption, 11_LVBus0121367_production, 11_LVBus0121368_production, 11_LVBus0121370_consumption, 11_LVBus0121370_production, 11_LVBus0121371_consumption, 11_LVBus0121371_production, 11_LVBus0121372_production, 11_LVBus0121373_consumption, 11_LVBus0121373_production, 11_LVBus0121374_consumption, 11_LVBus0121374_production, 11_LVBus0121375_consumption, 11_LVBus0121375_production, 11_LVBus0121376_consumption, 11_LVBus0121376_production, 11_LVBus0121377_consumption, 11_LVBus0121377_production, 11_LVBus0121378_consumption, 11_LVBus0121378_production, 11_LVBus0121379_consumption, 11_LVBus0121379_production, 11_LVBus0121380_consumption, 11_LVBus0121380_production, 11_LVBus0121381_consumption, 11_LVBus0121381_production, 11_LVBus0121382_consumption, 11_LVBus0121382_production, 11_LVBus0121383_consumption, 11_LVBus0121383_production, 11_LVBus0121384_consumption, 11_LVBus0121384_production, 11_LVBus0121385_consumption, 11_LVBus0121385_production, 11_LVBus0121386_consumption, 11_LVBus0121386_production, 11_LVBus0121387_production, 11_LVBus0121389_consumption, 11_LVBus0121389_production, 11_LVBus0121390_consumption, 11_LVBus0121390_production, 11_LVBus0121392_consumption, 11_LVBus0121392_production, 11_LVBus0121393_production, 11_LVBus0121394_consumption, 11_LVBus0121394_production, 11_LVBus0121397_production, 11_LVBus0121399_consumption, 11_LVBus0121399_production, 11_LVBus0121401_production, 11_LVBus0121403_consumption, 11_LVBus0121403_production, 11_LVBus0121405_consumption, 11_LVBus0121405_production, 11_LVBus0121406_production, 11_LVBus0121409_production, 11_LVBus0121410_consumption, 11_LVBus0121410_production, 11_LVBus0121411_consumption, 11_LVBus0121411_production, 11_LVBus0121412_production, 11_LVBus0121413_consumption, 11_LVBus0121413_production, 11_LVBus0121414_consumption, 11_LVBus0121414_production, 11_LVBus0121415_consumption, 11_LVBus0121415_production, 11_LVBus0121416_consumption, 11_LVBus0121416_production, 11_LVBus0121417_production, 11_LVBus0121418_consumption, 11_LVBus0121418_production, 11_LVBus0121419_consumption, 11_LVBus0121419_production, 11_LVBus0121420_production, 11_LVBus0121421_production, 11_LVBus0121422_production, 11_LVBus0121423_production, 11_LVBus0121424_consumption, 11_LVBus0121424_production, 11_LVBus0121426_consumption, 11_LVBus0121426_production, 11_LVBus0121428_production, 11_LVBus0121430_consumption, 11_LVBus0121430_production, 11_LVBus0121431_consumption, 11_LVBus0121431_production, 11_LVBus0121432_production, 11_LVBus0121433_consumption, 11_LVBus0121433_production, 11_LVBus0121434_consumption, 11_LVBus0121434_production, 11_LVBus0121435_production, 11_LVBus0121436_consumption, 11_LVBus0121436_production, 11_LVBus0121437_production, 11_LVBus0121438_production, 11_LVBus0121439_consumption, 11_LVBus0121439_production, 11_LVBus0121441_consumption, 11_LVBus0121441_production, 11_LVBus0121442_consumption, 11_LVBus0121442_production, 11_LVBus0121443_consumption, 11_LVBus0121443_production, 11_LVBus0121444_production, 11_LVBus0121446_consumption, 11_LVBus0121446_production, 11_LVBus0121447_consumption, 11_LVBus0121447_production, 11_LVBus0121448_consumption, 11_LVBus0121448_production, 11_LVBus0121449_production, 11_LVBus0121451_consumption, 11_LVBus0121451_production, 11_LVBus0121452_consumption, 11_LVBus0121452_production, 11_LVBus0121453_consumption, 11_LVBus0121453_production, 11_LVBus0121454_consumption, 11_LVBus0121454_production, 11_LVBus0121455_consumption, 11_LVBus0121455_production, 11_LVBus0121456_production, 11_LVBus0121457_consumption, 11_LVBus0121457_production, 11_LVBus0121458_production, 11_LVBus0121460_consumption, 11_LVBus0121460_production, 11_LVBus0121461_production, 11_LVBus0121462_consumption, 11_LVBus0121462_production, 11_LVBus0121463_consumption, 11_LVBus0121463_production, 11_LVBus0121464_production, 11_LVBus0121465_consumption, 11_LVBus0121465_production, 11_LVBus0121466_production, 11_LVBus0121467_consumption, 11_LVBus0121467_production, 11_LVBus0121468_consumption, 11_LVBus0121468_production, 11_LVBus0121469_consumption, 11_LVBus0121469_production, 11_LVBus0121470_production, 11_LVBus0121473_consumption, 11_LVBus0121473_production, 11_LVBus0121474_consumption, 11_LVBus0121474_production, 11_LVBus0121476_consumption, 11_LVBus0121476_production, 11_LVBus0121478_consumption, 11_LVBus0121478_production, 11_LVBus0121480_consumption, 11_LVBus0121480_production, 11_LVBus0121481_consumption, 11_LVBus0121481_production, 11_LVBus0121483_consumption, 11_LVBus0121483_production, 11_LVBus0121484_production, 11_LVBus0121485_production, 11_LVBus0121486_consumption, 11_LVBus0121486_production, 11_LVBus0121487_production, 11_LVBus0121489_consumption, 11_LVBus0121489_production, 11_LVBus0121490_consumption, 11_LVBus0121490_production, 11_LVBus0121492_consumption, 11_LVBus0121492_production, 11_LVBus0121493_production, 11_LVBus0121494_consumption, 11_LVBus0121494_production, 11_LVBus0121495_consumption, 11_LVBus0121495_production, 11_LVBus0121496_consumption, 11_LVBus0121496_production, 11_LVBus0121497_production, 11_LVBus0121499_consumption, 11_LVBus0121499_production, 11_LVBus0121500_consumption, 11_LVBus0121500_production, 11_LVBus0121501_consumption, 11_LVBus0121501_production, 11_LVBus0121502_consumption, 11_LVBus0121502_production, 11_LVBus0121503_consumption, 11_LVBus0121503_production, 11_LVBus0121504_production, 11_LVBus0121506_consumption, 11_LVBus0121506_production, 11_LVBus0121507_consumption, 11_LVBus0121507_production, 11_LVBus0121508_production, 11_LVBus0121510_consumption, 11_LVBus0121510_production, 11_LVBus0121512_consumption, 11_LVBus0121512_production, 11_LVBus0121513_consumption, 11_LVBus0121513_production, 11_LVBus0121514_consumption, 11_LVBus0121514_production, 11_LVBus0121516_production, 11_LVBus0121517_consumption, 11_LVBus0121517_production, 11_LVBus0121519_consumption, 11_LVBus0121519_production, 11_LVBus0121520_production, 11_LVBus0121521_consumption, 11_LVBus0121521_production, 11_LVBus0121523_consumption, 11_LVBus0121523_production, 11_LVBus0121525_consumption, 11_LVBus0121525_production, 11_LVBus0121526_production, 11_LVBus0121528_consumption, 11_LVBus0121528_production, 11_LVBus0121529_consumption, 11_LVBus0121529_production, 11_LVBus0121530_production, 11_LVBus0121532_consumption, 11_LVBus0121532_production, 11_LVBus0121533_consumption, 11_LVBus0121533_production, 11_LVBus0121535_consumption, 11_LVBus0121535_production, 11_LVBus0121537_production, 11_LVBus0121538_consumption, 11_LVBus0121538_production, 11_LVBus0121540_production, 11_LVBus0121542_consumption, 11_LVBus0121542_production, 11_LVBus0121544_production, 11_LVBus0121546_production, 11_LVBus0121548_production, 11_LVBus0121550_consumption, 11_LVBus0121550_production, 11_LVBus0121552_consumption, 11_LVBus0121552_production, 11_LVBus0121554_consumption, 11_LVBus0121554_production, 11_LVBus0121555_consumption, 11_LVBus0121555_production, 11_LVBus0121557_production, 11_LVBus0121559_consumption, 11_LVBus0121559_production, 11_LVBus0121560_consumption, 11_LVBus0121560_production, 11_LVBus0121562_production, 11_LVBus0121563_consumption, 11_LVBus0121563_production, 11_LVBus0121564_consumption, 11_LVBus0121564_production, 11_LVBus0121566_consumption, 11_LVBus0121566_production, 11_LVBus0121567_consumption, 11_LVBus0121567_production, 11_LVBus0121568_consumption, 11_LVBus0121568_production, 11_LVBus0121569_consumption, 11_LVBus0121569_production, 11_LVBus0121570_consumption, 11_LVBus0121570_production, 11_LVBus0121571_consumption, 11_LVBus0121571_production, 11_LVBus0121572_consumption, 11_LVBus0121572_production, 11_LVBus0121573_consumption, 11_LVBus0121573_production, 11_LVBus0121575_production, 11_LVBus0121576_production, 11_LVBus0121578_consumption, 11_LVBus0121578_production, 11_LVBus0121579_production, 11_LVBus0121581_consumption, 11_LVBus0121581_production, 11_LVBus0121582_consumption, 11_LVBus0121582_production, 11_LVBus0121583_consumption, 11_LVBus0121583_production, 11_LVBus0121584_consumption, 11_LVBus0121584_production, 11_LVBus0121585_consumption, 11_LVBus0121585_production, 11_LVBus0121587_production, 11_LVBus0121588_production, 11_LVBus0121589_consumption, 11_LVBus0121589_production, 11_LVBus0121591_consumption, 11_LVBus0121591_production, 11_LVBus0121592_consumption, 11_LVBus0121592_production, 11_LVBus0121593_consumption, 11_LVBus0121593_production, 11_LVBus0121594_consumption, 11_LVBus0121594_production, 11_LVBus0121595_production, 11_LVBus0121596_consumption, 11_LVBus0121596_production, 11_LVBus0121598_production, 11_LVBus0121599_consumption, 11_LVBus0121599_production, 11_LVBus0121600_consumption, 11_LVBus0121600_production, 11_LVBus0121602_production, 11_LVBus0121604_consumption, 11_LVBus0121604_production, 11_LVBus0121605_consumption, 11_LVBus0121605_production, 11_LVBus0121607_consumption, 11_LVBus0121607_production, 11_LVBus0121608_production, 11_LVBus0121609_consumption, 11_LVBus0121609_production, 11_LVBus0121610_production, 11_LVBus0121612_consumption, 11_LVBus0121612_production, 11_LVBus0121613_consumption, 11_LVBus0121613_production, 11_LVBus0121614_consumption, 11_LVBus0121614_production, 11_LVBus0121615_consumption, 11_LVBus0121615_production, 11_LVBus0121617_consumption, 11_LVBus0121617_production, 11_LVBus0121618_production, 11_LVBus0121620_consumption, 11_LVBus0121620_production, 11_LVBus0121621_consumption, 11_LVBus0121621_production, 11_LVBus0121623_consumption, 11_LVBus0121623_production, 11_LVBus0121624_consumption, 11_LVBus0121624_production, 11_LVBus0121625_production, 11_LVBus1330774_consumption, 11_LVBus1330774_production, 11_LVBus1330775_consumption, 11_LVBus1330775_production, 11_LVBus1330776_consumption, 11_LVBus1330776_production, 11_LVBus1330777_consumption, 11_LVBus1330777_production, 11_LVBus1330778_consumption, 11_LVBus1330778_production, 11_LVBus1330779_consumption, 11_LVBus1330779_production, 11_LVBus1330780_production, 11_LVBus1330781_consumption, 11_LVBus1330781_production, 11_LVBus1330782_consumption, 11_LVBus1330782_production, 11_LVBus1330783_production, 11_LVBus1330784_consumption, 11_LVBus1330784_production, 11_LVBus1331956_consumption, 11_LVBus1331956_production, 11_LVBus1331957_consumption, 11_LVBus1331957_production, 11_LVBus1331958_consumption, 11_LVBus1331958_production, 11_LVBus1331959_consumption, 11_LVBus1331959_production, 11_LVBus1331960_consumption, 11_LVBus1331960_production, 11_LVBus1331961_consumption, 11_LVBus1331961_production, 11_LVBus1331962_production, 11_LVBus1331963_consumption, 11_LVBus1331963_production, 11_LVBus1331964_production, 11_LVBus1344841_consumption, 11_LVBus1344841_production, 11_LVBus1344842_consumption, 11_LVBus1344842_production, 11_LVBus1344843_consumption, 11_LVBus1344843_production, 11_LVBus1344844_consumption, 11_LVBus1344844_production, 11_LVBus1344845_consumption, 11_LVBus1344845_production, 11_LVBus1344846_consumption, 11_LVBus1344846_production, 11_LVBus1347826_consumption, 11_LVBus1347826_production, 11_MVLV28012_consumption, 11_MVLV28012_production, 11_MVLV29264_production, 11_MVLV35406_production, 11_MVLV63131_production, 11_MVLV70320_production.

## 9. Data Quality Summary

**Total findings:** 97 (0 errors, 7 warnings, 90 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  16 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  746 of 860 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (10.23 MW).
- **[W.OPS.XFMR_OVERLOADED]** `11_MVLV71670_Transformer`  
  Transformer '11_MVLV71670_Transformer' is at 90.5% utilisation at nominal load — little OPF headroom.
- **[W.OPS.XFMR_OVERLOADED]** `11_MVLV42629_Transformer`  
  Transformer '11_MVLV42629_Transformer' is at 94.3% utilisation at nominal load — little OPF headroom.
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  747 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121357_consumption`  
  Load '11_LVBus0121357_consumption' has phase imbalance of 30.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121309_consumption`  
  Load '11_LVBus0121309_consumption' has phase imbalance of 82.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121184_consumption`  
  Load '11_LVBus0121184_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121520_consumption`  
  Load '11_LVBus0121520_consumption' has phase imbalance of 33.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121270_consumption`  
  Load '11_LVBus0121270_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121331_consumption`  
  Load '11_LVBus0121331_consumption' has phase imbalance of 57.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121485_consumption`  
  Load '11_LVBus0121485_consumption' has phase imbalance of 43.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121493_consumption`  
  Load '11_LVBus0121493_consumption' has phase imbalance of 64.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1331964_consumption`  
  Load '11_LVBus1331964_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121562_consumption`  
  Load '11_LVBus0121562_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121110_consumption`  
  Load '11_LVBus0121110_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121575_consumption`  
  Load '11_LVBus0121575_consumption' has phase imbalance of 20.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121272_consumption`  
  Load '11_LVBus0121272_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121526_consumption`  
  Load '11_LVBus0121526_consumption' has phase imbalance of 32.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121365_consumption`  
  Load '11_LVBus0121365_consumption' has phase imbalance of 41.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121444_consumption`  
  Load '11_LVBus0121444_consumption' has phase imbalance of 37.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121191_consumption`  
  Load '11_LVBus0121191_consumption' has phase imbalance of 30.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121170_consumption`  
  Load '11_LVBus0121170_consumption' has phase imbalance of 41.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121176_consumption`  
  Load '11_LVBus0121176_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121147_consumption`  
  Load '11_LVBus0121147_consumption' has phase imbalance of 44.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121423_consumption`  
  Load '11_LVBus0121423_consumption' has phase imbalance of 43.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121366_consumption`  
  Load '11_LVBus0121366_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121484_consumption`  
  Load '11_LVBus0121484_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121618_consumption`  
  Load '11_LVBus0121618_consumption' has phase imbalance of 128.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121409_consumption`  
  Load '11_LVBus0121409_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121464_consumption`  
  Load '11_LVBus0121464_consumption' has phase imbalance of 69.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121387_consumption`  
  Load '11_LVBus0121387_consumption' has phase imbalance of 63.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121438_consumption`  
  Load '11_LVBus0121438_consumption' has phase imbalance of 67.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121598_consumption`  
  Load '11_LVBus0121598_consumption' has phase imbalance of 47.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121470_consumption`  
  Load '11_LVBus0121470_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121323_consumption`  
  Load '11_LVBus0121323_consumption' has phase imbalance of 25.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121610_consumption`  
  Load '11_LVBus0121610_consumption' has phase imbalance of 89.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121422_consumption`  
  Load '11_LVBus0121422_consumption' has phase imbalance of 34.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121127_consumption`  
  Load '11_LVBus0121127_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121432_consumption`  
  Load '11_LVBus0121432_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121274_consumption`  
  Load '11_LVBus0121274_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121497_consumption`  
  Load '11_LVBus0121497_consumption' has phase imbalance of 57.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121504_consumption`  
  Load '11_LVBus0121504_consumption' has phase imbalance of 37.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121397_consumption`  
  Load '11_LVBus0121397_consumption' has phase imbalance of 22.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121321_consumption`  
  Load '11_LVBus0121321_consumption' has phase imbalance of 62.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121449_consumption`  
  Load '11_LVBus0121449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121284_consumption`  
  Load '11_LVBus0121284_consumption' has phase imbalance of 36.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121530_consumption`  
  Load '11_LVBus0121530_consumption' has phase imbalance of 30.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121307_consumption`  
  Load '11_LVBus0121307_consumption' has phase imbalance of 119.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121119_consumption`  
  Load '11_LVBus0121119_consumption' has phase imbalance of 35.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121537_consumption`  
  Load '11_LVBus0121537_consumption' has phase imbalance of 52.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121153_consumption`  
  Load '11_LVBus0121153_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121159_consumption`  
  Load '11_LVBus0121159_consumption' has phase imbalance of 52.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121301_consumption`  
  Load '11_LVBus0121301_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121461_consumption`  
  Load '11_LVBus0121461_consumption' has phase imbalance of 37.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121587_consumption`  
  Load '11_LVBus0121587_consumption' has phase imbalance of 88.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121437_consumption`  
  Load '11_LVBus0121437_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121421_consumption`  
  Load '11_LVBus0121421_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121138_consumption`  
  Load '11_LVBus0121138_consumption' has phase imbalance of 36.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121273_consumption`  
  Load '11_LVBus0121273_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121458_consumption`  
  Load '11_LVBus0121458_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121308_consumption`  
  Load '11_LVBus0121308_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121393_consumption`  
  Load '11_LVBus0121393_consumption' has phase imbalance of 34.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121588_consumption`  
  Load '11_LVBus0121588_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121401_consumption`  
  Load '11_LVBus0121401_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121579_consumption`  
  Load '11_LVBus0121579_consumption' has phase imbalance of 47.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121324_consumption`  
  Load '11_LVBus0121324_consumption' has phase imbalance of 23.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121146_consumption`  
  Load '11_LVBus0121146_consumption' has phase imbalance of 62.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121435_consumption`  
  Load '11_LVBus0121435_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121139_consumption`  
  Load '11_LVBus0121139_consumption' has phase imbalance of 74.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121608_consumption`  
  Load '11_LVBus0121608_consumption' has phase imbalance of 37.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121214_consumption`  
  Load '11_LVBus0121214_consumption' has phase imbalance of 88.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121356_consumption`  
  Load '11_LVBus0121356_consumption' has phase imbalance of 22.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121420_consumption`  
  Load '11_LVBus0121420_consumption' has phase imbalance of 53.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1330783_consumption`  
  Load '11_LVBus1330783_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121276_consumption`  
  Load '11_LVBus0121276_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0121346_consumption`  
  Load '11_LVBus0121346_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 860 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0121552' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0121234' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0121542' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '11_LVBus0121196' (LV, 0.24 kV) has an electrical reach of 2.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '11_LVBus0121397' (LV, 0.24 kV) has an electrical reach of 12.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '11_LVBus0121542' (LV, 0.24 kV) has an electrical reach of 2.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  510 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  4 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus0121301_consumption, 11_LVBus0121346_consumption, 11_LVBus0121449_consumption, 11_LVBus1330783_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  430 group(s) of loads (860 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  747 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0121110_production, 11_LVBus0121112_production, 11_LVBus0121113_consumption, 11_LVBus0121113_production, 11_LVBus0121115_consumption, 11_LVBus0121115_production, 11_LVBus0121116_production, 11_LVBus0121117_consumption, 11_LVBus0121117_production, 11_LVBus0121118_production, 11_LVBus0121119_production, 11_LVBus0121121_consumption, 11_LVBus0121121_production, 11_LVBus0121122_production, 11_LVBus0121123_consumption, 11_LVBus0121123_production, 11_LVBus0121124_production, 11_LVBus0121126_consumption, 11_LVBus0121126_production, 11_LVBus0121127_production, 11_LVBus0121128_consumption, 11_LVBus0121128_production, 11_LVBus0121129_consumption, 11_LVBus0121129_production, 11_LVBus0121130_consumption, 11_LVBus0121130_production, 11_LVBus0121131_consumption, 11_LVBus0121131_production, 11_LVBus0121132_consumption, 11_LVBus0121132_production, 11_LVBus0121133_consumption, 11_LVBus0121133_production, 11_LVBus0121135_consumption, 11_LVBus0121135_production, 11_LVBus0121136_consumption, 11_LVBus0121136_production, 11_LVBus0121137_consumption, 11_LVBus0121137_production, 11_LVBus0121138_production, 11_LVBus0121139_production, 11_LVBus0121141_consumption, 11_LVBus0121141_production, 11_LVBus0121142_consumption, 11_LVBus0121142_production, 11_LVBus0121143_consumption, 11_LVBus0121143_production, 11_LVBus0121144_consumption, 11_LVBus0121144_production, 11_LVBus0121145_consumption, 11_LVBus0121145_production, 11_LVBus0121146_production, 11_LVBus0121147_production, 11_LVBus0121149_consumption, 11_LVBus0121149_production, 11_LVBus0121150_consumption, 11_LVBus0121150_production, 11_LVBus0121151_consumption, 11_LVBus0121151_production, 11_LVBus0121152_consumption, 11_LVBus0121152_production, 11_LVBus0121153_production, 11_LVBus0121154_consumption, 11_LVBus0121154_production, 11_LVBus0121156_consumption, 11_LVBus0121156_production, 11_LVBus0121157_consumption, 11_LVBus0121157_production, 11_LVBus0121158_consumption, 11_LVBus0121158_production, 11_LVBus0121159_production, 11_LVBus0121160_consumption, 11_LVBus0121160_production, 11_LVBus0121162_consumption, 11_LVBus0121162_production, 11_LVBus0121163_consumption, 11_LVBus0121163_production, 11_LVBus0121164_consumption, 11_LVBus0121164_production, 11_LVBus0121165_consumption, 11_LVBus0121165_production, 11_LVBus0121166_consumption, 11_LVBus0121166_production, 11_LVBus0121167_consumption, 11_LVBus0121167_production, 11_LVBus0121168_consumption, 11_LVBus0121168_production, 11_LVBus0121169_consumption, 11_LVBus0121169_production, 11_LVBus0121170_production, 11_LVBus0121172_consumption, 11_LVBus0121172_production, 11_LVBus0121173_consumption, 11_LVBus0121173_production, 11_LVBus0121174_consumption, 11_LVBus0121174_production, 11_LVBus0121175_consumption, 11_LVBus0121175_production, 11_LVBus0121176_production, 11_LVBus0121177_consumption, 11_LVBus0121177_production, 11_LVBus0121178_consumption, 11_LVBus0121178_production, 11_LVBus0121179_consumption, 11_LVBus0121179_production, 11_LVBus0121180_consumption, 11_LVBus0121180_production, 11_LVBus0121181_consumption, 11_LVBus0121181_production, 11_LVBus0121182_consumption, 11_LVBus0121182_production, 11_LVBus0121183_consumption, 11_LVBus0121183_production, 11_LVBus0121184_production, 11_LVBus0121186_consumption, 11_LVBus0121186_production, 11_LVBus0121187_consumption, 11_LVBus0121187_production, 11_LVBus0121188_consumption, 11_LVBus0121188_production, 11_LVBus0121189_consumption, 11_LVBus0121189_production, 11_LVBus0121190_production, 11_LVBus0121191_production, 11_LVBus0121192_consumption, 11_LVBus0121192_production, 11_LVBus0121193_consumption, 11_LVBus0121193_production, 11_LVBus0121194_consumption, 11_LVBus0121194_production, 11_LVBus0121196_consumption, 11_LVBus0121196_production, 11_LVBus0121198_consumption, 11_LVBus0121198_production, 11_LVBus0121200_consumption, 11_LVBus0121200_production, 11_LVBus0121202_consumption, 11_LVBus0121202_production, 11_LVBus0121204_consumption, 11_LVBus0121204_production, 11_LVBus0121206_consumption, 11_LVBus0121206_production, 11_LVBus0121208_production, 11_LVBus0121210_consumption, 11_LVBus0121210_production, 11_LVBus0121212_consumption, 11_LVBus0121212_production, 11_LVBus0121214_production, 11_LVBus0121216_consumption, 11_LVBus0121216_production, 11_LVBus0121218_consumption, 11_LVBus0121218_production, 11_LVBus0121220_consumption, 11_LVBus0121220_production, 11_LVBus0121222_consumption, 11_LVBus0121222_production, 11_LVBus0121224_consumption, 11_LVBus0121224_production, 11_LVBus0121226_consumption, 11_LVBus0121226_production, 11_LVBus0121228_consumption, 11_LVBus0121228_production, 11_LVBus0121229_production, 11_LVBus0121230_consumption, 11_LVBus0121230_production, 11_LVBus0121232_consumption, 11_LVBus0121232_production, 11_LVBus0121234_consumption, 11_LVBus0121234_production, 11_LVBus0121236_consumption, 11_LVBus0121236_production, 11_LVBus0121238_consumption, 11_LVBus0121238_production, 11_LVBus0121240_production, 11_LVBus0121241_consumption, 11_LVBus0121241_production, 11_LVBus0121242_consumption, 11_LVBus0121242_production, 11_LVBus0121244_consumption, 11_LVBus0121244_production, 11_LVBus0121245_consumption, 11_LVBus0121245_production, 11_LVBus0121246_consumption, 11_LVBus0121246_production, 11_LVBus0121247_consumption, 11_LVBus0121247_production, 11_LVBus0121248_consumption, 11_LVBus0121248_production, 11_LVBus0121249_production, 11_LVBus0121251_consumption, 11_LVBus0121251_production, 11_LVBus0121252_consumption, 11_LVBus0121252_production, 11_LVBus0121254_consumption, 11_LVBus0121254_production, 11_LVBus0121255_consumption, 11_LVBus0121255_production, 11_LVBus0121256_consumption, 11_LVBus0121256_production, 11_LVBus0121258_consumption, 11_LVBus0121258_production, 11_LVBus0121259_consumption, 11_LVBus0121259_production, 11_LVBus0121261_consumption, 11_LVBus0121261_production, 11_LVBus0121263_consumption, 11_LVBus0121263_production, 11_LVBus0121265_consumption, 11_LVBus0121265_production, 11_LVBus0121266_consumption, 11_LVBus0121266_production, 11_LVBus0121267_consumption, 11_LVBus0121267_production, 11_LVBus0121268_consumption, 11_LVBus0121268_production, 11_LVBus0121269_consumption, 11_LVBus0121269_production, 11_LVBus0121270_production, 11_LVBus0121271_consumption, 11_LVBus0121271_production, 11_LVBus0121272_production, 11_LVBus0121273_production, 11_LVBus0121274_production, 11_LVBus0121276_production, 11_LVBus0121277_consumption, 11_LVBus0121277_production, 11_LVBus0121278_consumption, 11_LVBus0121278_production, 11_LVBus0121279_consumption, 11_LVBus0121279_production, 11_LVBus0121280_consumption, 11_LVBus0121280_production, 11_LVBus0121281_consumption, 11_LVBus0121281_production, 11_LVBus0121282_consumption, 11_LVBus0121282_production, 11_LVBus0121283_consumption, 11_LVBus0121283_production, 11_LVBus0121284_production, 11_LVBus0121285_consumption, 11_LVBus0121285_production, 11_LVBus0121286_consumption, 11_LVBus0121286_production, 11_LVBus0121288_consumption, 11_LVBus0121288_production, 11_LVBus0121289_consumption, 11_LVBus0121289_production, 11_LVBus0121290_consumption, 11_LVBus0121290_production, 11_LVBus0121291_consumption, 11_LVBus0121291_production, 11_LVBus0121292_consumption, 11_LVBus0121292_production, 11_LVBus0121293_consumption, 11_LVBus0121293_production, 11_LVBus0121295_consumption, 11_LVBus0121295_production, 11_LVBus0121296_consumption, 11_LVBus0121296_production, 11_LVBus0121297_consumption, 11_LVBus0121297_production, 11_LVBus0121298_consumption, 11_LVBus0121298_production, 11_LVBus0121299_consumption, 11_LVBus0121299_production, 11_LVBus0121300_consumption, 11_LVBus0121300_production, 11_LVBus0121301_production, 11_LVBus0121302_consumption, 11_LVBus0121302_production, 11_LVBus0121303_consumption, 11_LVBus0121303_production, 11_LVBus0121304_consumption, 11_LVBus0121304_production, 11_LVBus0121305_consumption, 11_LVBus0121305_production, 11_LVBus0121306_production, 11_LVBus0121307_production, 11_LVBus0121308_production, 11_LVBus0121309_production, 11_LVBus0121311_consumption, 11_LVBus0121311_production, 11_LVBus0121312_consumption, 11_LVBus0121312_production, 11_LVBus0121313_consumption, 11_LVBus0121313_production, 11_LVBus0121314_consumption, 11_LVBus0121314_production, 11_LVBus0121315_production, 11_LVBus0121316_consumption, 11_LVBus0121316_production, 11_LVBus0121317_consumption, 11_LVBus0121317_production, 11_LVBus0121318_consumption, 11_LVBus0121318_production, 11_LVBus0121319_consumption, 11_LVBus0121319_production, 11_LVBus0121320_consumption, 11_LVBus0121320_production, 11_LVBus0121321_production, 11_LVBus0121322_consumption, 11_LVBus0121322_production, 11_LVBus0121323_production, 11_LVBus0121324_production, 11_LVBus0121325_production, 11_LVBus0121327_consumption, 11_LVBus0121327_production, 11_LVBus0121329_consumption, 11_LVBus0121329_production, 11_LVBus0121331_production, 11_LVBus0121333_consumption, 11_LVBus0121333_production, 11_LVBus0121334_consumption, 11_LVBus0121334_production, 11_LVBus0121335_consumption, 11_LVBus0121335_production, 11_LVBus0121337_consumption, 11_LVBus0121337_production, 11_LVBus0121339_consumption, 11_LVBus0121339_production, 11_LVBus0121340_consumption, 11_LVBus0121340_production, 11_LVBus0121342_consumption, 11_LVBus0121342_production, 11_LVBus0121344_consumption, 11_LVBus0121344_production, 11_LVBus0121346_production, 11_LVBus0121348_consumption, 11_LVBus0121348_production, 11_LVBus0121349_consumption, 11_LVBus0121349_production, 11_LVBus0121350_production, 11_LVBus0121351_consumption, 11_LVBus0121351_production, 11_LVBus0121352_consumption, 11_LVBus0121352_production, 11_LVBus0121353_consumption, 11_LVBus0121353_production, 11_LVBus0121354_consumption, 11_LVBus0121354_production, 11_LVBus0121355_consumption, 11_LVBus0121355_production, 11_LVBus0121356_production, 11_LVBus0121357_production, 11_LVBus0121359_consumption, 11_LVBus0121359_production, 11_LVBus0121360_production, 11_LVBus0121361_consumption, 11_LVBus0121361_production, 11_LVBus0121362_consumption, 11_LVBus0121362_production, 11_LVBus0121363_consumption, 11_LVBus0121363_production, 11_LVBus0121364_consumption, 11_LVBus0121364_production, 11_LVBus0121365_production, 11_LVBus0121366_production, 11_LVBus0121367_consumption, 11_LVBus0121367_production, 11_LVBus0121368_production, 11_LVBus0121370_consumption, 11_LVBus0121370_production, 11_LVBus0121371_consumption, 11_LVBus0121371_production, 11_LVBus0121372_production, 11_LVBus0121373_consumption, 11_LVBus0121373_production, 11_LVBus0121374_consumption, 11_LVBus0121374_production, 11_LVBus0121375_consumption, 11_LVBus0121375_production, 11_LVBus0121376_consumption, 11_LVBus0121376_production, 11_LVBus0121377_consumption, 11_LVBus0121377_production, 11_LVBus0121378_consumption, 11_LVBus0121378_production, 11_LVBus0121379_consumption, 11_LVBus0121379_production, 11_LVBus0121380_consumption, 11_LVBus0121380_production, 11_LVBus0121381_consumption, 11_LVBus0121381_production, 11_LVBus0121382_consumption, 11_LVBus0121382_production, 11_LVBus0121383_consumption, 11_LVBus0121383_production, 11_LVBus0121384_consumption, 11_LVBus0121384_production, 11_LVBus0121385_consumption, 11_LVBus0121385_production, 11_LVBus0121386_consumption, 11_LVBus0121386_production, 11_LVBus0121387_production, 11_LVBus0121389_consumption, 11_LVBus0121389_production, 11_LVBus0121390_consumption, 11_LVBus0121390_production, 11_LVBus0121392_consumption, 11_LVBus0121392_production, 11_LVBus0121393_production, 11_LVBus0121394_consumption, 11_LVBus0121394_production, 11_LVBus0121397_production, 11_LVBus0121399_consumption, 11_LVBus0121399_production, 11_LVBus0121401_production, 11_LVBus0121403_consumption, 11_LVBus0121403_production, 11_LVBus0121405_consumption, 11_LVBus0121405_production, 11_LVBus0121406_production, 11_LVBus0121409_production, 11_LVBus0121410_consumption, 11_LVBus0121410_production, 11_LVBus0121411_consumption, 11_LVBus0121411_production, 11_LVBus0121412_production, 11_LVBus0121413_consumption, 11_LVBus0121413_production, 11_LVBus0121414_consumption, 11_LVBus0121414_production, 11_LVBus0121415_consumption, 11_LVBus0121415_production, 11_LVBus0121416_consumption, 11_LVBus0121416_production, 11_LVBus0121417_production, 11_LVBus0121418_consumption, 11_LVBus0121418_production, 11_LVBus0121419_consumption, 11_LVBus0121419_production, 11_LVBus0121420_production, 11_LVBus0121421_production, 11_LVBus0121422_production, 11_LVBus0121423_production, 11_LVBus0121424_consumption, 11_LVBus0121424_production, 11_LVBus0121426_consumption, 11_LVBus0121426_production, 11_LVBus0121428_production, 11_LVBus0121430_consumption, 11_LVBus0121430_production, 11_LVBus0121431_consumption, 11_LVBus0121431_production, 11_LVBus0121432_production, 11_LVBus0121433_consumption, 11_LVBus0121433_production, 11_LVBus0121434_consumption, 11_LVBus0121434_production, 11_LVBus0121435_production, 11_LVBus0121436_consumption, 11_LVBus0121436_production, 11_LVBus0121437_production, 11_LVBus0121438_production, 11_LVBus0121439_consumption, 11_LVBus0121439_production, 11_LVBus0121441_consumption, 11_LVBus0121441_production, 11_LVBus0121442_consumption, 11_LVBus0121442_production, 11_LVBus0121443_consumption, 11_LVBus0121443_production, 11_LVBus0121444_production, 11_LVBus0121446_consumption, 11_LVBus0121446_production, 11_LVBus0121447_consumption, 11_LVBus0121447_production, 11_LVBus0121448_consumption, 11_LVBus0121448_production, 11_LVBus0121449_production, 11_LVBus0121451_consumption, 11_LVBus0121451_production, 11_LVBus0121452_consumption, 11_LVBus0121452_production, 11_LVBus0121453_consumption, 11_LVBus0121453_production, 11_LVBus0121454_consumption, 11_LVBus0121454_production, 11_LVBus0121455_consumption, 11_LVBus0121455_production, 11_LVBus0121456_production, 11_LVBus0121457_consumption, 11_LVBus0121457_production, 11_LVBus0121458_production, 11_LVBus0121460_consumption, 11_LVBus0121460_production, 11_LVBus0121461_production, 11_LVBus0121462_consumption, 11_LVBus0121462_production, 11_LVBus0121463_consumption, 11_LVBus0121463_production, 11_LVBus0121464_production, 11_LVBus0121465_consumption, 11_LVBus0121465_production, 11_LVBus0121466_production, 11_LVBus0121467_consumption, 11_LVBus0121467_production, 11_LVBus0121468_consumption, 11_LVBus0121468_production, 11_LVBus0121469_consumption, 11_LVBus0121469_production, 11_LVBus0121470_production, 11_LVBus0121473_consumption, 11_LVBus0121473_production, 11_LVBus0121474_consumption, 11_LVBus0121474_production, 11_LVBus0121476_consumption, 11_LVBus0121476_production, 11_LVBus0121478_consumption, 11_LVBus0121478_production, 11_LVBus0121480_consumption, 11_LVBus0121480_production, 11_LVBus0121481_consumption, 11_LVBus0121481_production, 11_LVBus0121483_consumption, 11_LVBus0121483_production, 11_LVBus0121484_production, 11_LVBus0121485_production, 11_LVBus0121486_consumption, 11_LVBus0121486_production, 11_LVBus0121487_production, 11_LVBus0121489_consumption, 11_LVBus0121489_production, 11_LVBus0121490_consumption, 11_LVBus0121490_production, 11_LVBus0121492_consumption, 11_LVBus0121492_production, 11_LVBus0121493_production, 11_LVBus0121494_consumption, 11_LVBus0121494_production, 11_LVBus0121495_consumption, 11_LVBus0121495_production, 11_LVBus0121496_consumption, 11_LVBus0121496_production, 11_LVBus0121497_production, 11_LVBus0121499_consumption, 11_LVBus0121499_production, 11_LVBus0121500_consumption, 11_LVBus0121500_production, 11_LVBus0121501_consumption, 11_LVBus0121501_production, 11_LVBus0121502_consumption, 11_LVBus0121502_production, 11_LVBus0121503_consumption, 11_LVBus0121503_production, 11_LVBus0121504_production, 11_LVBus0121506_consumption, 11_LVBus0121506_production, 11_LVBus0121507_consumption, 11_LVBus0121507_production, 11_LVBus0121508_production, 11_LVBus0121510_consumption, 11_LVBus0121510_production, 11_LVBus0121512_consumption, 11_LVBus0121512_production, 11_LVBus0121513_consumption, 11_LVBus0121513_production, 11_LVBus0121514_consumption, 11_LVBus0121514_production, 11_LVBus0121516_production, 11_LVBus0121517_consumption, 11_LVBus0121517_production, 11_LVBus0121519_consumption, 11_LVBus0121519_production, 11_LVBus0121520_production, 11_LVBus0121521_consumption, 11_LVBus0121521_production, 11_LVBus0121523_consumption, 11_LVBus0121523_production, 11_LVBus0121525_consumption, 11_LVBus0121525_production, 11_LVBus0121526_production, 11_LVBus0121528_consumption, 11_LVBus0121528_production, 11_LVBus0121529_consumption, 11_LVBus0121529_production, 11_LVBus0121530_production, 11_LVBus0121532_consumption, 11_LVBus0121532_production, 11_LVBus0121533_consumption, 11_LVBus0121533_production, 11_LVBus0121535_consumption, 11_LVBus0121535_production, 11_LVBus0121537_production, 11_LVBus0121538_consumption, 11_LVBus0121538_production, 11_LVBus0121540_production, 11_LVBus0121542_consumption, 11_LVBus0121542_production, 11_LVBus0121544_production, 11_LVBus0121546_production, 11_LVBus0121548_production, 11_LVBus0121550_consumption, 11_LVBus0121550_production, 11_LVBus0121552_consumption, 11_LVBus0121552_production, 11_LVBus0121554_consumption, 11_LVBus0121554_production, 11_LVBus0121555_consumption, 11_LVBus0121555_production, 11_LVBus0121557_production, 11_LVBus0121559_consumption, 11_LVBus0121559_production, 11_LVBus0121560_consumption, 11_LVBus0121560_production, 11_LVBus0121562_production, 11_LVBus0121563_consumption, 11_LVBus0121563_production, 11_LVBus0121564_consumption, 11_LVBus0121564_production, 11_LVBus0121566_consumption, 11_LVBus0121566_production, 11_LVBus0121567_consumption, 11_LVBus0121567_production, 11_LVBus0121568_consumption, 11_LVBus0121568_production, 11_LVBus0121569_consumption, 11_LVBus0121569_production, 11_LVBus0121570_consumption, 11_LVBus0121570_production, 11_LVBus0121571_consumption, 11_LVBus0121571_production, 11_LVBus0121572_consumption, 11_LVBus0121572_production, 11_LVBus0121573_consumption, 11_LVBus0121573_production, 11_LVBus0121575_production, 11_LVBus0121576_production, 11_LVBus0121578_consumption, 11_LVBus0121578_production, 11_LVBus0121579_production, 11_LVBus0121581_consumption, 11_LVBus0121581_production, 11_LVBus0121582_consumption, 11_LVBus0121582_production, 11_LVBus0121583_consumption, 11_LVBus0121583_production, 11_LVBus0121584_consumption, 11_LVBus0121584_production, 11_LVBus0121585_consumption, 11_LVBus0121585_production, 11_LVBus0121587_production, 11_LVBus0121588_production, 11_LVBus0121589_consumption, 11_LVBus0121589_production, 11_LVBus0121591_consumption, 11_LVBus0121591_production, 11_LVBus0121592_consumption, 11_LVBus0121592_production, 11_LVBus0121593_consumption, 11_LVBus0121593_production, 11_LVBus0121594_consumption, 11_LVBus0121594_production, 11_LVBus0121595_production, 11_LVBus0121596_consumption, 11_LVBus0121596_production, 11_LVBus0121598_production, 11_LVBus0121599_consumption, 11_LVBus0121599_production, 11_LVBus0121600_consumption, 11_LVBus0121600_production, 11_LVBus0121602_production, 11_LVBus0121604_consumption, 11_LVBus0121604_production, 11_LVBus0121605_consumption, 11_LVBus0121605_production, 11_LVBus0121607_consumption, 11_LVBus0121607_production, 11_LVBus0121608_production, 11_LVBus0121609_consumption, 11_LVBus0121609_production, 11_LVBus0121610_production, 11_LVBus0121612_consumption, 11_LVBus0121612_production, 11_LVBus0121613_consumption, 11_LVBus0121613_production, 11_LVBus0121614_consumption, 11_LVBus0121614_production, 11_LVBus0121615_consumption, 11_LVBus0121615_production, 11_LVBus0121617_consumption, 11_LVBus0121617_production, 11_LVBus0121618_production, 11_LVBus0121620_consumption, 11_LVBus0121620_production, 11_LVBus0121621_consumption, 11_LVBus0121621_production, 11_LVBus0121623_consumption, 11_LVBus0121623_production, 11_LVBus0121624_consumption, 11_LVBus0121624_production, 11_LVBus0121625_production, 11_LVBus1330774_consumption, 11_LVBus1330774_production, 11_LVBus1330775_consumption, 11_LVBus1330775_production, 11_LVBus1330776_consumption, 11_LVBus1330776_production, 11_LVBus1330777_consumption, 11_LVBus1330777_production, 11_LVBus1330778_consumption, 11_LVBus1330778_production, 11_LVBus1330779_consumption, 11_LVBus1330779_production, 11_LVBus1330780_production, 11_LVBus1330781_consumption, 11_LVBus1330781_production, 11_LVBus1330782_consumption, 11_LVBus1330782_production, 11_LVBus1330783_production, 11_LVBus1330784_consumption, 11_LVBus1330784_production, 11_LVBus1331956_consumption, 11_LVBus1331956_production, 11_LVBus1331957_consumption, 11_LVBus1331957_production, 11_LVBus1331958_consumption, 11_LVBus1331958_production, 11_LVBus1331959_consumption, 11_LVBus1331959_production, 11_LVBus1331960_consumption, 11_LVBus1331960_production, 11_LVBus1331961_consumption, 11_LVBus1331961_production, 11_LVBus1331962_production, 11_LVBus1331963_consumption, 11_LVBus1331963_production, 11_LVBus1331964_production, 11_LVBus1344841_consumption, 11_LVBus1344841_production, 11_LVBus1344842_consumption, 11_LVBus1344842_production, 11_LVBus1344843_consumption, 11_LVBus1344843_production, 11_LVBus1344844_consumption, 11_LVBus1344844_production, 11_LVBus1344845_consumption, 11_LVBus1344845_production, 11_LVBus1344846_consumption, 11_LVBus1344846_production, 11_LVBus1347826_consumption, 11_LVBus1347826_production, 11_MVLV28012_consumption, 11_MVLV28012_production, 11_MVLV29264_production, 11_MVLV35406_production, 11_MVLV63131_production, 11_MVLV70320_production.

