# BMOPF Network Summary: 53_MVFeeder1979

**Generated:** 2026-10-01 23:34:20  
**Findings:** 0 errors · 5 warnings · 74 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 313 |  |
| line | 292 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 538 | 5.073 MW, 1.52 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 20 |  |
| switch | 0 |  |
| transformer | 20 | Dyn11×20 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 31 | 30 | 14 | 0 |
| LV_236V | 236.0 V | 282 | 262 | 524 | 0 |

**Transformer transitions:**

- `53_MVLV72996_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV75202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV09839_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV59533_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV22834_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV71092_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV73154_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV36577_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV60091_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV59548_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV31405_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV67820_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV69659_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV13427_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV48252_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV31315_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV36589_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV68038_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV03439_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV03411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 13 |
| Degree-1 buses | 138 |
| Tree depth (max hops) | 33 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 313 | 1 | 312 | 0 | 0 | 0 |
| Tier LV_236V | 282 | 20 | 262 | 0 | 0 | 0 |
| Tier MV_11.8kV | 31 | 1 | 30 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 20; skipped invalid branches: 0.

Galvanic zones: 21; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 53_MVBus67346 | MV_11.8kV | 31 | 0 | 0 | 20 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1221 declared bus terminals; 1138 mapped line/closed-switch conductor edges; 83 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 260000.0 | 5.182 | 1614 |
| q_nom | 0.0 | 77900.0 | 5.182 | 1614 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.52 | 960.0 | 1.406 | 292 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 1.1e6 | 0.561 | 20 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 407 of 538 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284334_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus988786_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus988788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284187_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284215_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284343_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284090_consumption' has phase imbalance of 25.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284228_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284142_consumption' has phase imbalance of 54.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284223_consumption' has phase imbalance of 105.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284229_consumption' has phase imbalance of 283.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284339_consumption' has phase imbalance of 204.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284218_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284348_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284232_consumption' has phase imbalance of 268.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284332_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284338_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284217_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284144_consumption' has phase imbalance of 21.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284226_consumption' has phase imbalance of 117.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284140_consumption' has phase imbalance of 195.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284231_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus988787_consumption' has phase imbalance of 195.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284324_consumption' has phase imbalance of 166.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994760_consumption' has phase imbalance of 259.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284333_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284347_consumption' has phase imbalance of 250.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284234_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284320_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284214_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284141_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284342_consumption' has phase imbalance of 222.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284336_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1002219_consumption' has phase imbalance of 112.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284225_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284099_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus284349_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 538 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284109' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus1002026' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284379' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284193' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284146' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus1016166' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284247' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284295' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_VERN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284365' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284396' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus284207' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 5.073 MW |
| Total load Q | 1.52 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 53_MVLV72996_Transformer | 693.0 kVA | 22.9% |
| 53_MVLV75202_Transformer | 1.1 MVA | 26.7% |
| 53_MVLV09839_Transformer | 693.0 kVA | 31.2% |
| 53_MVLV59533_Transformer | 176.0 kVA | 0.0% |
| 53_MVLV22834_Transformer | 693.0 kVA | 21.2% |
| 53_MVLV71092_Transformer | 176.0 kVA | 0.0% |
| 53_MVLV73154_Transformer | 1.1 MVA | 31.3% |
| 53_MVLV36577_Transformer | 275.0 kVA | 18.9% |
| 53_MVLV60091_Transformer | 176.0 kVA | 0.0% |
| 53_MVLV59548_Transformer | 1.1 MVA | 41.2% |
| 53_MVLV31405_Transformer | 275.0 kVA | 11.6% |
| 53_MVLV67820_Transformer | 1.1 MVA | 37.0% |
| 53_MVLV69659_Transformer | 440.0 kVA | 24.5% |
| 53_MVLV13427_Transformer | 275.0 kVA | 25.2% |
| 53_MVLV48252_Transformer | 440.0 kVA | 35.8% |
| 53_MVLV31315_Transformer | 693.0 kVA | 40.9% |
| 53_MVLV36589_Transformer | 275.0 kVA | 16.9% |
| 53_MVLV68038_Transformer | 693.0 kVA | 17.1% |
| 53_MVLV03439_Transformer | 693.0 kVA | 34.8% |
| 53_MVLV03411_Transformer | 693.0 kVA | 19.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.07 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '53_LVBus284351' (LV, 0.24 kV) has an electrical reach of 10.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 313 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 313 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 31 |
| LV_236V | 4-wire | 282 / 282 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 282 |
| Neutral branches | 262 |
| Grounding points | 20 |
| Neutral sections | 20 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| exactly_balanced | 1 |
| decoupled | 2 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 4 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 31 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 21 |
| Islands without voltage reference | 0 |
| Line impedance spread | 167.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 282 / 31 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 408 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 408 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus1002026_consumption, 53_LVBus1002026_production, 53_LVBus1002027_production, 53_LVBus1002219_production, 53_LVBus1012972_consumption, 53_LVBus1012972_production, 53_LVBus1012973_consumption, 53_LVBus1012973_production, 53_LVBus1012974_production, 53_LVBus1016166_consumption, 53_LVBus1016166_production, 53_LVBus1023345_consumption, 53_LVBus1023345_production, 53_LVBus1023346_production, 53_LVBus1023347_consumption, 53_LVBus1023347_production, 53_LVBus284071_consumption, 53_LVBus284071_production, 53_LVBus284073_consumption, 53_LVBus284073_production, 53_LVBus284074_consumption, 53_LVBus284074_production, 53_LVBus284075_production, 53_LVBus284076_consumption, 53_LVBus284076_production, 53_LVBus284077_production, 53_LVBus284079_production, 53_LVBus284081_consumption, 53_LVBus284081_production, 53_LVBus284082_production, 53_LVBus284084_production, 53_LVBus284086_consumption, 53_LVBus284086_production, 53_LVBus284088_production, 53_LVBus284090_production, 53_LVBus284092_production, 53_LVBus284094_production, 53_LVBus284095_production, 53_LVBus284096_production, 53_LVBus284098_production, 53_LVBus284099_production, 53_LVBus284100_consumption, 53_LVBus284100_production, 53_LVBus284101_production, 53_LVBus284103_production, 53_LVBus284105_consumption, 53_LVBus284105_production, 53_LVBus284106_production, 53_LVBus284107_consumption, 53_LVBus284107_production, 53_LVBus284109_production, 53_LVBus284110_consumption, 53_LVBus284110_production, 53_LVBus284111_consumption, 53_LVBus284111_production, 53_LVBus284113_production, 53_LVBus284115_consumption, 53_LVBus284115_production, 53_LVBus284116_consumption, 53_LVBus284116_production, 53_LVBus284117_production, 53_LVBus284118_consumption, 53_LVBus284118_production, 53_LVBus284120_production, 53_LVBus284121_production, 53_LVBus284123_consumption, 53_LVBus284123_production, 53_LVBus284125_consumption, 53_LVBus284125_production, 53_LVBus284126_consumption, 53_LVBus284126_production, 53_LVBus284127_consumption, 53_LVBus284127_production, 53_LVBus284128_consumption, 53_LVBus284128_production, 53_LVBus284129_consumption, 53_LVBus284129_production, 53_LVBus284130_consumption, 53_LVBus284130_production, 53_LVBus284131_production, 53_LVBus284132_consumption, 53_LVBus284132_production, 53_LVBus284134_production, 53_LVBus284135_production, 53_LVBus284136_production, 53_LVBus284137_production, 53_LVBus284139_production, 53_LVBus284140_production, 53_LVBus284141_production, 53_LVBus284142_production, 53_LVBus284144_production, 53_LVBus284146_production, 53_LVBus284148_consumption, 53_LVBus284148_production, 53_LVBus284149_consumption, 53_LVBus284149_production, 53_LVBus284150_consumption, 53_LVBus284150_production, 53_LVBus284151_production, 53_LVBus284152_production, 53_LVBus284153_consumption, 53_LVBus284153_production, 53_LVBus284154_consumption, 53_LVBus284154_production, 53_LVBus284155_consumption, 53_LVBus284155_production, 53_LVBus284156_production, 53_LVBus284157_consumption, 53_LVBus284157_production, 53_LVBus284158_consumption, 53_LVBus284158_production, 53_LVBus284159_production, 53_LVBus284161_production, 53_LVBus284163_production, 53_LVBus284166_production, 53_LVBus284168_consumption, 53_LVBus284168_production, 53_LVBus284169_consumption, 53_LVBus284169_production, 53_LVBus284170_production, 53_LVBus284171_consumption, 53_LVBus284171_production, 53_LVBus284172_consumption, 53_LVBus284172_production, 53_LVBus284173_consumption, 53_LVBus284173_production, 53_LVBus284175_production, 53_LVBus284176_consumption, 53_LVBus284176_production, 53_LVBus284177_consumption, 53_LVBus284177_production, 53_LVBus284179_production, 53_LVBus284181_production, 53_LVBus284182_consumption, 53_LVBus284182_production, 53_LVBus284184_production, 53_LVBus284186_consumption, 53_LVBus284186_production, 53_LVBus284187_production, 53_LVBus284193_consumption, 53_LVBus284193_production, 53_LVBus284194_consumption, 53_LVBus284194_production, 53_LVBus284195_production, 53_LVBus284196_production, 53_LVBus284198_consumption, 53_LVBus284198_production, 53_LVBus284200_production, 53_LVBus284202_consumption, 53_LVBus284202_production, 53_LVBus284203_production, 53_LVBus284207_production, 53_LVBus284209_production, 53_LVBus284210_consumption, 53_LVBus284210_production, 53_LVBus284212_consumption, 53_LVBus284212_production, 53_LVBus284213_production, 53_LVBus284214_production, 53_LVBus284215_production, 53_LVBus284216_production, 53_LVBus284217_production, 53_LVBus284218_production, 53_LVBus284219_consumption, 53_LVBus284219_production, 53_LVBus284220_production, 53_LVBus284221_consumption, 53_LVBus284221_production, 53_LVBus284222_consumption, 53_LVBus284222_production, 53_LVBus284223_production, 53_LVBus284224_consumption, 53_LVBus284224_production, 53_LVBus284225_production, 53_LVBus284226_production, 53_LVBus284227_production, 53_LVBus284228_production, 53_LVBus284229_production, 53_LVBus284231_production, 53_LVBus284232_production, 53_LVBus284234_production, 53_LVBus284235_production, 53_LVBus284236_consumption, 53_LVBus284236_production, 53_LVBus284237_consumption, 53_LVBus284237_production, 53_LVBus284239_consumption, 53_LVBus284239_production, 53_LVBus284241_consumption, 53_LVBus284241_production, 53_LVBus284243_consumption, 53_LVBus284243_production, 53_LVBus284245_consumption, 53_LVBus284245_production, 53_LVBus284247_consumption, 53_LVBus284247_production, 53_LVBus284249_consumption, 53_LVBus284249_production, 53_LVBus284250_consumption, 53_LVBus284250_production, 53_LVBus284252_consumption, 53_LVBus284252_production, 53_LVBus284253_consumption, 53_LVBus284253_production, 53_LVBus284255_consumption, 53_LVBus284255_production, 53_LVBus284257_production, 53_LVBus284259_consumption, 53_LVBus284259_production, 53_LVBus284261_production, 53_LVBus284263_consumption, 53_LVBus284263_production, 53_LVBus284264_consumption, 53_LVBus284264_production, 53_LVBus284265_consumption, 53_LVBus284265_production, 53_LVBus284266_consumption, 53_LVBus284266_production, 53_LVBus284267_consumption, 53_LVBus284267_production, 53_LVBus284268_consumption, 53_LVBus284268_production, 53_LVBus284269_production, 53_LVBus284270_consumption, 53_LVBus284270_production, 53_LVBus284271_production, 53_LVBus284272_production, 53_LVBus284274_consumption, 53_LVBus284274_production, 53_LVBus284275_consumption, 53_LVBus284275_production, 53_LVBus284276_consumption, 53_LVBus284276_production, 53_LVBus284277_production, 53_LVBus284279_consumption, 53_LVBus284279_production, 53_LVBus284280_consumption, 53_LVBus284280_production, 53_LVBus284281_consumption, 53_LVBus284281_production, 53_LVBus284282_consumption, 53_LVBus284282_production, 53_LVBus284283_production, 53_LVBus284285_consumption, 53_LVBus284285_production, 53_LVBus284286_consumption, 53_LVBus284286_production, 53_LVBus284287_production, 53_LVBus284288_consumption, 53_LVBus284288_production, 53_LVBus284289_production, 53_LVBus284291_production, 53_LVBus284293_consumption, 53_LVBus284293_production, 53_LVBus284295_consumption, 53_LVBus284295_production, 53_LVBus284296_consumption, 53_LVBus284296_production, 53_LVBus284297_consumption, 53_LVBus284297_production, 53_LVBus284298_production, 53_LVBus284299_consumption, 53_LVBus284299_production, 53_LVBus284300_consumption, 53_LVBus284300_production, 53_LVBus284301_consumption, 53_LVBus284301_production, 53_LVBus284302_production, 53_LVBus284303_production, 53_LVBus284305_consumption, 53_LVBus284305_production, 53_LVBus284306_production, 53_LVBus284308_consumption, 53_LVBus284308_production, 53_LVBus284309_consumption, 53_LVBus284309_production, 53_LVBus284310_consumption, 53_LVBus284310_production, 53_LVBus284311_consumption, 53_LVBus284311_production, 53_LVBus284312_production, 53_LVBus284313_consumption, 53_LVBus284313_production, 53_LVBus284314_production, 53_LVBus284315_production, 53_LVBus284317_consumption, 53_LVBus284317_production, 53_LVBus284318_consumption, 53_LVBus284318_production, 53_LVBus284320_production, 53_LVBus284322_consumption, 53_LVBus284322_production, 53_LVBus284323_consumption, 53_LVBus284323_production, 53_LVBus284324_production, 53_LVBus284325_production, 53_LVBus284326_production, 53_LVBus284327_production, 53_LVBus284328_consumption, 53_LVBus284328_production, 53_LVBus284330_consumption, 53_LVBus284330_production, 53_LVBus284332_production, 53_LVBus284333_production, 53_LVBus284334_production, 53_LVBus284336_production, 53_LVBus284338_production, 53_LVBus284339_production, 53_LVBus284340_consumption, 53_LVBus284340_production, 53_LVBus284341_production, 53_LVBus284342_production, 53_LVBus284343_production, 53_LVBus284344_consumption, 53_LVBus284344_production, 53_LVBus284345_consumption, 53_LVBus284345_production, 53_LVBus284347_production, 53_LVBus284348_production, 53_LVBus284349_production, 53_LVBus284351_consumption, 53_LVBus284351_production, 53_LVBus284353_consumption, 53_LVBus284353_production, 53_LVBus284355_consumption, 53_LVBus284355_production, 53_LVBus284357_consumption, 53_LVBus284357_production, 53_LVBus284359_consumption, 53_LVBus284359_production, 53_LVBus284361_consumption, 53_LVBus284361_production, 53_LVBus284363_consumption, 53_LVBus284363_production, 53_LVBus284365_consumption, 53_LVBus284365_production, 53_LVBus284366_production, 53_LVBus284368_production, 53_LVBus284369_consumption, 53_LVBus284369_production, 53_LVBus284371_consumption, 53_LVBus284371_production, 53_LVBus284372_consumption, 53_LVBus284372_production, 53_LVBus284374_consumption, 53_LVBus284374_production, 53_LVBus284376_consumption, 53_LVBus284376_production, 53_LVBus284379_consumption, 53_LVBus284379_production, 53_LVBus284380_production, 53_LVBus284381_consumption, 53_LVBus284381_production, 53_LVBus284382_production, 53_LVBus284384_consumption, 53_LVBus284384_production, 53_LVBus284385_production, 53_LVBus284386_production, 53_LVBus284388_production, 53_LVBus284389_consumption, 53_LVBus284389_production, 53_LVBus284390_consumption, 53_LVBus284390_production, 53_LVBus284392_production, 53_LVBus284394_production, 53_LVBus284396_consumption, 53_LVBus284396_production, 53_LVBus284397_consumption, 53_LVBus284397_production, 53_LVBus284398_production, 53_LVBus284399_production, 53_LVBus284400_production, 53_LVBus284401_production, 53_LVBus284403_consumption, 53_LVBus284403_production, 53_LVBus284404_production, 53_LVBus284405_consumption, 53_LVBus284405_production, 53_LVBus284407_production, 53_LVBus982017_consumption, 53_LVBus982017_production, 53_LVBus982018_consumption, 53_LVBus982018_production, 53_LVBus983463_consumption, 53_LVBus983463_production, 53_LVBus984768_consumption, 53_LVBus984768_production, 53_LVBus984769_consumption, 53_LVBus984769_production, 53_LVBus988786_production, 53_LVBus988787_production, 53_LVBus988788_production, 53_LVBus994757_consumption, 53_LVBus994757_production, 53_LVBus994758_consumption, 53_LVBus994758_production, 53_LVBus994759_production, 53_LVBus994760_production, 53_MVLV32115_production, 53_MVLV32172_production, 53_MVLV38116_consumption, 53_MVLV38116_production, 53_MVLV65918_production, 53_MVLV66653_production, 53_MVLV73085_consumption, 53_MVLV73085_production, 53_MVLV83041_consumption, 53_MVLV83041_production.

## 9. Data Quality Summary

**Total findings:** 79 (0 errors, 5 warnings, 74 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  407 of 538 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.07 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  408 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284334_consumption`  
  Load '53_LVBus284334_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus988786_consumption`  
  Load '53_LVBus988786_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284101_consumption`  
  Load '53_LVBus284101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus988788_consumption`  
  Load '53_LVBus988788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284187_consumption`  
  Load '53_LVBus284187_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284215_consumption`  
  Load '53_LVBus284215_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284139_consumption`  
  Load '53_LVBus284139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284343_consumption`  
  Load '53_LVBus284343_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284090_consumption`  
  Load '53_LVBus284090_consumption' has phase imbalance of 25.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284228_consumption`  
  Load '53_LVBus284228_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284142_consumption`  
  Load '53_LVBus284142_consumption' has phase imbalance of 54.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284223_consumption`  
  Load '53_LVBus284223_consumption' has phase imbalance of 105.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284235_consumption`  
  Load '53_LVBus284235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284229_consumption`  
  Load '53_LVBus284229_consumption' has phase imbalance of 283.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284135_consumption`  
  Load '53_LVBus284135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284339_consumption`  
  Load '53_LVBus284339_consumption' has phase imbalance of 204.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284218_consumption`  
  Load '53_LVBus284218_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284348_consumption`  
  Load '53_LVBus284348_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284220_consumption`  
  Load '53_LVBus284220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284232_consumption`  
  Load '53_LVBus284232_consumption' has phase imbalance of 268.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284332_consumption`  
  Load '53_LVBus284332_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284338_consumption`  
  Load '53_LVBus284338_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284217_consumption`  
  Load '53_LVBus284217_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284144_consumption`  
  Load '53_LVBus284144_consumption' has phase imbalance of 21.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284226_consumption`  
  Load '53_LVBus284226_consumption' has phase imbalance of 117.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284140_consumption`  
  Load '53_LVBus284140_consumption' has phase imbalance of 195.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284231_consumption`  
  Load '53_LVBus284231_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994759_consumption`  
  Load '53_LVBus994759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284341_consumption`  
  Load '53_LVBus284341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus988787_consumption`  
  Load '53_LVBus988787_consumption' has phase imbalance of 195.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284324_consumption`  
  Load '53_LVBus284324_consumption' has phase imbalance of 166.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994760_consumption`  
  Load '53_LVBus994760_consumption' has phase imbalance of 259.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284333_consumption`  
  Load '53_LVBus284333_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284347_consumption`  
  Load '53_LVBus284347_consumption' has phase imbalance of 250.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284234_consumption`  
  Load '53_LVBus284234_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284320_consumption`  
  Load '53_LVBus284320_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284137_consumption`  
  Load '53_LVBus284137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284227_consumption`  
  Load '53_LVBus284227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284214_consumption`  
  Load '53_LVBus284214_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284141_consumption`  
  Load '53_LVBus284141_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284342_consumption`  
  Load '53_LVBus284342_consumption' has phase imbalance of 222.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284336_consumption`  
  Load '53_LVBus284336_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1002219_consumption`  
  Load '53_LVBus1002219_consumption' has phase imbalance of 112.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284136_consumption`  
  Load '53_LVBus284136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284225_consumption`  
  Load '53_LVBus284225_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284099_consumption`  
  Load '53_LVBus284099_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus284349_consumption`  
  Load '53_LVBus284349_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 538 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284109' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus1002026' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284379' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284193' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284146' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus1016166' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284247' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284295' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_VERN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284365' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284396' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus284207' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '53_LVBus284351' (LV, 0.24 kV) has an electrical reach of 10.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  313 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  33 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 53_LVBus284099_consumption, 53_LVBus284101_consumption, 53_LVBus284135_consumption, 53_LVBus284136_consumption, 53_LVBus284137_consumption, 53_LVBus284139_consumption, 53_LVBus284140_consumption, 53_LVBus284214_consumption, 53_LVBus284215_consumption, 53_LVBus284217_consumption, 53_LVBus284218_consumption, 53_LVBus284220_consumption, 53_LVBus284225_consumption, 53_LVBus284227_consumption, 53_LVBus284228_consumption, 53_LVBus284229_consumption, 53_LVBus284234_consumption, 53_LVBus284235_consumption, 53_LVBus284324_consumption, 53_LVBus284332_consumption, 53_LVBus284333_consumption, 53_LVBus284334_consumption, 53_LVBus284339_consumption, 53_LVBus284341_consumption, 53_LVBus284342_consumption, 53_LVBus284347_consumption, 53_LVBus284348_consumption, 53_LVBus284349_consumption, 53_LVBus988786_consumption, 53_LVBus988787_consumption, 53_LVBus988788_consumption, 53_LVBus994759_consumption, 53_LVBus994760_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  269 group(s) of loads (538 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  408 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus1002026_consumption, 53_LVBus1002026_production, 53_LVBus1002027_production, 53_LVBus1002219_production, 53_LVBus1012972_consumption, 53_LVBus1012972_production, 53_LVBus1012973_consumption, 53_LVBus1012973_production, 53_LVBus1012974_production, 53_LVBus1016166_consumption, 53_LVBus1016166_production, 53_LVBus1023345_consumption, 53_LVBus1023345_production, 53_LVBus1023346_production, 53_LVBus1023347_consumption, 53_LVBus1023347_production, 53_LVBus284071_consumption, 53_LVBus284071_production, 53_LVBus284073_consumption, 53_LVBus284073_production, 53_LVBus284074_consumption, 53_LVBus284074_production, 53_LVBus284075_production, 53_LVBus284076_consumption, 53_LVBus284076_production, 53_LVBus284077_production, 53_LVBus284079_production, 53_LVBus284081_consumption, 53_LVBus284081_production, 53_LVBus284082_production, 53_LVBus284084_production, 53_LVBus284086_consumption, 53_LVBus284086_production, 53_LVBus284088_production, 53_LVBus284090_production, 53_LVBus284092_production, 53_LVBus284094_production, 53_LVBus284095_production, 53_LVBus284096_production, 53_LVBus284098_production, 53_LVBus284099_production, 53_LVBus284100_consumption, 53_LVBus284100_production, 53_LVBus284101_production, 53_LVBus284103_production, 53_LVBus284105_consumption, 53_LVBus284105_production, 53_LVBus284106_production, 53_LVBus284107_consumption, 53_LVBus284107_production, 53_LVBus284109_production, 53_LVBus284110_consumption, 53_LVBus284110_production, 53_LVBus284111_consumption, 53_LVBus284111_production, 53_LVBus284113_production, 53_LVBus284115_consumption, 53_LVBus284115_production, 53_LVBus284116_consumption, 53_LVBus284116_production, 53_LVBus284117_production, 53_LVBus284118_consumption, 53_LVBus284118_production, 53_LVBus284120_production, 53_LVBus284121_production, 53_LVBus284123_consumption, 53_LVBus284123_production, 53_LVBus284125_consumption, 53_LVBus284125_production, 53_LVBus284126_consumption, 53_LVBus284126_production, 53_LVBus284127_consumption, 53_LVBus284127_production, 53_LVBus284128_consumption, 53_LVBus284128_production, 53_LVBus284129_consumption, 53_LVBus284129_production, 53_LVBus284130_consumption, 53_LVBus284130_production, 53_LVBus284131_production, 53_LVBus284132_consumption, 53_LVBus284132_production, 53_LVBus284134_production, 53_LVBus284135_production, 53_LVBus284136_production, 53_LVBus284137_production, 53_LVBus284139_production, 53_LVBus284140_production, 53_LVBus284141_production, 53_LVBus284142_production, 53_LVBus284144_production, 53_LVBus284146_production, 53_LVBus284148_consumption, 53_LVBus284148_production, 53_LVBus284149_consumption, 53_LVBus284149_production, 53_LVBus284150_consumption, 53_LVBus284150_production, 53_LVBus284151_production, 53_LVBus284152_production, 53_LVBus284153_consumption, 53_LVBus284153_production, 53_LVBus284154_consumption, 53_LVBus284154_production, 53_LVBus284155_consumption, 53_LVBus284155_production, 53_LVBus284156_production, 53_LVBus284157_consumption, 53_LVBus284157_production, 53_LVBus284158_consumption, 53_LVBus284158_production, 53_LVBus284159_production, 53_LVBus284161_production, 53_LVBus284163_production, 53_LVBus284166_production, 53_LVBus284168_consumption, 53_LVBus284168_production, 53_LVBus284169_consumption, 53_LVBus284169_production, 53_LVBus284170_production, 53_LVBus284171_consumption, 53_LVBus284171_production, 53_LVBus284172_consumption, 53_LVBus284172_production, 53_LVBus284173_consumption, 53_LVBus284173_production, 53_LVBus284175_production, 53_LVBus284176_consumption, 53_LVBus284176_production, 53_LVBus284177_consumption, 53_LVBus284177_production, 53_LVBus284179_production, 53_LVBus284181_production, 53_LVBus284182_consumption, 53_LVBus284182_production, 53_LVBus284184_production, 53_LVBus284186_consumption, 53_LVBus284186_production, 53_LVBus284187_production, 53_LVBus284193_consumption, 53_LVBus284193_production, 53_LVBus284194_consumption, 53_LVBus284194_production, 53_LVBus284195_production, 53_LVBus284196_production, 53_LVBus284198_consumption, 53_LVBus284198_production, 53_LVBus284200_production, 53_LVBus284202_consumption, 53_LVBus284202_production, 53_LVBus284203_production, 53_LVBus284207_production, 53_LVBus284209_production, 53_LVBus284210_consumption, 53_LVBus284210_production, 53_LVBus284212_consumption, 53_LVBus284212_production, 53_LVBus284213_production, 53_LVBus284214_production, 53_LVBus284215_production, 53_LVBus284216_production, 53_LVBus284217_production, 53_LVBus284218_production, 53_LVBus284219_consumption, 53_LVBus284219_production, 53_LVBus284220_production, 53_LVBus284221_consumption, 53_LVBus284221_production, 53_LVBus284222_consumption, 53_LVBus284222_production, 53_LVBus284223_production, 53_LVBus284224_consumption, 53_LVBus284224_production, 53_LVBus284225_production, 53_LVBus284226_production, 53_LVBus284227_production, 53_LVBus284228_production, 53_LVBus284229_production, 53_LVBus284231_production, 53_LVBus284232_production, 53_LVBus284234_production, 53_LVBus284235_production, 53_LVBus284236_consumption, 53_LVBus284236_production, 53_LVBus284237_consumption, 53_LVBus284237_production, 53_LVBus284239_consumption, 53_LVBus284239_production, 53_LVBus284241_consumption, 53_LVBus284241_production, 53_LVBus284243_consumption, 53_LVBus284243_production, 53_LVBus284245_consumption, 53_LVBus284245_production, 53_LVBus284247_consumption, 53_LVBus284247_production, 53_LVBus284249_consumption, 53_LVBus284249_production, 53_LVBus284250_consumption, 53_LVBus284250_production, 53_LVBus284252_consumption, 53_LVBus284252_production, 53_LVBus284253_consumption, 53_LVBus284253_production, 53_LVBus284255_consumption, 53_LVBus284255_production, 53_LVBus284257_production, 53_LVBus284259_consumption, 53_LVBus284259_production, 53_LVBus284261_production, 53_LVBus284263_consumption, 53_LVBus284263_production, 53_LVBus284264_consumption, 53_LVBus284264_production, 53_LVBus284265_consumption, 53_LVBus284265_production, 53_LVBus284266_consumption, 53_LVBus284266_production, 53_LVBus284267_consumption, 53_LVBus284267_production, 53_LVBus284268_consumption, 53_LVBus284268_production, 53_LVBus284269_production, 53_LVBus284270_consumption, 53_LVBus284270_production, 53_LVBus284271_production, 53_LVBus284272_production, 53_LVBus284274_consumption, 53_LVBus284274_production, 53_LVBus284275_consumption, 53_LVBus284275_production, 53_LVBus284276_consumption, 53_LVBus284276_production, 53_LVBus284277_production, 53_LVBus284279_consumption, 53_LVBus284279_production, 53_LVBus284280_consumption, 53_LVBus284280_production, 53_LVBus284281_consumption, 53_LVBus284281_production, 53_LVBus284282_consumption, 53_LVBus284282_production, 53_LVBus284283_production, 53_LVBus284285_consumption, 53_LVBus284285_production, 53_LVBus284286_consumption, 53_LVBus284286_production, 53_LVBus284287_production, 53_LVBus284288_consumption, 53_LVBus284288_production, 53_LVBus284289_production, 53_LVBus284291_production, 53_LVBus284293_consumption, 53_LVBus284293_production, 53_LVBus284295_consumption, 53_LVBus284295_production, 53_LVBus284296_consumption, 53_LVBus284296_production, 53_LVBus284297_consumption, 53_LVBus284297_production, 53_LVBus284298_production, 53_LVBus284299_consumption, 53_LVBus284299_production, 53_LVBus284300_consumption, 53_LVBus284300_production, 53_LVBus284301_consumption, 53_LVBus284301_production, 53_LVBus284302_production, 53_LVBus284303_production, 53_LVBus284305_consumption, 53_LVBus284305_production, 53_LVBus284306_production, 53_LVBus284308_consumption, 53_LVBus284308_production, 53_LVBus284309_consumption, 53_LVBus284309_production, 53_LVBus284310_consumption, 53_LVBus284310_production, 53_LVBus284311_consumption, 53_LVBus284311_production, 53_LVBus284312_production, 53_LVBus284313_consumption, 53_LVBus284313_production, 53_LVBus284314_production, 53_LVBus284315_production, 53_LVBus284317_consumption, 53_LVBus284317_production, 53_LVBus284318_consumption, 53_LVBus284318_production, 53_LVBus284320_production, 53_LVBus284322_consumption, 53_LVBus284322_production, 53_LVBus284323_consumption, 53_LVBus284323_production, 53_LVBus284324_production, 53_LVBus284325_production, 53_LVBus284326_production, 53_LVBus284327_production, 53_LVBus284328_consumption, 53_LVBus284328_production, 53_LVBus284330_consumption, 53_LVBus284330_production, 53_LVBus284332_production, 53_LVBus284333_production, 53_LVBus284334_production, 53_LVBus284336_production, 53_LVBus284338_production, 53_LVBus284339_production, 53_LVBus284340_consumption, 53_LVBus284340_production, 53_LVBus284341_production, 53_LVBus284342_production, 53_LVBus284343_production, 53_LVBus284344_consumption, 53_LVBus284344_production, 53_LVBus284345_consumption, 53_LVBus284345_production, 53_LVBus284347_production, 53_LVBus284348_production, 53_LVBus284349_production, 53_LVBus284351_consumption, 53_LVBus284351_production, 53_LVBus284353_consumption, 53_LVBus284353_production, 53_LVBus284355_consumption, 53_LVBus284355_production, 53_LVBus284357_consumption, 53_LVBus284357_production, 53_LVBus284359_consumption, 53_LVBus284359_production, 53_LVBus284361_consumption, 53_LVBus284361_production, 53_LVBus284363_consumption, 53_LVBus284363_production, 53_LVBus284365_consumption, 53_LVBus284365_production, 53_LVBus284366_production, 53_LVBus284368_production, 53_LVBus284369_consumption, 53_LVBus284369_production, 53_LVBus284371_consumption, 53_LVBus284371_production, 53_LVBus284372_consumption, 53_LVBus284372_production, 53_LVBus284374_consumption, 53_LVBus284374_production, 53_LVBus284376_consumption, 53_LVBus284376_production, 53_LVBus284379_consumption, 53_LVBus284379_production, 53_LVBus284380_production, 53_LVBus284381_consumption, 53_LVBus284381_production, 53_LVBus284382_production, 53_LVBus284384_consumption, 53_LVBus284384_production, 53_LVBus284385_production, 53_LVBus284386_production, 53_LVBus284388_production, 53_LVBus284389_consumption, 53_LVBus284389_production, 53_LVBus284390_consumption, 53_LVBus284390_production, 53_LVBus284392_production, 53_LVBus284394_production, 53_LVBus284396_consumption, 53_LVBus284396_production, 53_LVBus284397_consumption, 53_LVBus284397_production, 53_LVBus284398_production, 53_LVBus284399_production, 53_LVBus284400_production, 53_LVBus284401_production, 53_LVBus284403_consumption, 53_LVBus284403_production, 53_LVBus284404_production, 53_LVBus284405_consumption, 53_LVBus284405_production, 53_LVBus284407_production, 53_LVBus982017_consumption, 53_LVBus982017_production, 53_LVBus982018_consumption, 53_LVBus982018_production, 53_LVBus983463_consumption, 53_LVBus983463_production, 53_LVBus984768_consumption, 53_LVBus984768_production, 53_LVBus984769_consumption, 53_LVBus984769_production, 53_LVBus988786_production, 53_LVBus988787_production, 53_LVBus988788_production, 53_LVBus994757_consumption, 53_LVBus994757_production, 53_LVBus994758_consumption, 53_LVBus994758_production, 53_LVBus994759_production, 53_LVBus994760_production, 53_MVLV32115_production, 53_MVLV32172_production, 53_MVLV38116_consumption, 53_MVLV38116_production, 53_MVLV65918_production, 53_MVLV66653_production, 53_MVLV73085_consumption, 53_MVLV73085_production, 53_MVLV83041_consumption, 53_MVLV83041_production.

