# BMOPF Network Summary: 32_MVFeeder3323

**Generated:** 2026-10-01 23:34:09  
**Findings:** 0 errors · 4 warnings · 117 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 333 |  |
| line | 316 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 600 | 2.641 MW, 792.3 kvar |
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
| MV_11.8kV | 11.78 kV | 18 | 17 | 2 | 0 |
| LV_236V | 236.0 V | 315 | 299 | 598 | 0 |

**Transformer transitions:**

- `32_MVLV31765_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV32089_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV51133_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV48764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV48686_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV38223_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV39017_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV49500_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV67140_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV73919_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV57058_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV74442_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV73589_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV25333_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV74604_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV78282_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 15 |
| Degree-1 buses | 149 |
| Tree depth (max hops) | 23 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 333 | 1 | 332 | 0 | 0 | 0 |
| Tier LV_236V | 315 | 16 | 299 | 0 | 0 | 0 |
| Tier MV_11.8kV | 18 | 1 | 17 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 16; skipped invalid branches: 0.

Galvanic zones: 17; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_MVLV25333 | MV_11.8kV | 18 | 0 | 0 | 16 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1314 declared bus terminals; 1247 mapped line/closed-switch conductor edges; 67 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 68000.0 | 3.507 | 1800 |
| q_nom | 0.0 | 20400.0 | 3.507 | 1800 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.999 | 2650.0 | 2.532 | 316 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 693000.0 | 0.458 | 16 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 454 of 600 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271910_consumption' has phase imbalance of 243.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272028_consumption' has phase imbalance of 141.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272185_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272016_consumption' has phase imbalance of 257.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272127_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271956_consumption' has phase imbalance of 109.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272019_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271825_consumption' has phase imbalance of 146.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271974_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271962_consumption' has phase imbalance of 91.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272005_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272149_consumption' has phase imbalance of 139.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272146_consumption' has phase imbalance of 219.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271878_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271840_consumption' has phase imbalance of 144.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272155_consumption' has phase imbalance of 64.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272166_consumption' has phase imbalance of 53.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272012_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271983_consumption' has phase imbalance of 203.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272181_consumption' has phase imbalance of 156.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271934_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272199_consumption' has phase imbalance of 116.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272084_consumption' has phase imbalance of 28.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271899_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272026_consumption' has phase imbalance of 103.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272182_consumption' has phase imbalance of 29.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271827_consumption' has phase imbalance of 82.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272139_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272142_consumption' has phase imbalance of 28.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272056_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272184_consumption' has phase imbalance of 100.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272171_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271958_consumption' has phase imbalance of 91.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272163_consumption' has phase imbalance of 134.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271896_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271846_consumption' has phase imbalance of 64.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272031_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272147_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271926_consumption' has phase imbalance of 37.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272141_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272033_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271951_consumption' has phase imbalance of 33.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271854_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271898_consumption' has phase imbalance of 148.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271855_consumption' has phase imbalance of 100.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272176_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271986_consumption' has phase imbalance of 139.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271915_consumption' has phase imbalance of 49.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271938_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272168_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272077_consumption' has phase imbalance of 33.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272074_consumption' has phase imbalance of 39.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271930_consumption' has phase imbalance of 212.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271826_consumption' has phase imbalance of 106.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272053_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271981_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272159_consumption' has phase imbalance of 24.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272164_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272211_consumption' has phase imbalance of 53.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272061_consumption' has phase imbalance of 45.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271994_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271852_consumption' has phase imbalance of 95.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272202_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271984_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272179_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272032_consumption' has phase imbalance of 67.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271913_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272119_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272013_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272120_consumption' has phase imbalance of 69.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271897_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271843_consumption' has phase imbalance of 88.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272180_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271996_consumption' has phase imbalance of 110.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271982_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271965_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271838_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272161_consumption' has phase imbalance of 252.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271829_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272195_consumption' has phase imbalance of 50.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272172_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272132_consumption' has phase imbalance of 99.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271967_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272173_consumption' has phase imbalance of 140.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271909_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus271830_consumption' has phase imbalance of 108.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272015_consumption' has phase imbalance of 236.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272165_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus272039_consumption' has phase imbalance of 66.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 600 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus1118773' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus271867' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.641 MW |
| Total load Q | 792.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV31765_Transformer | 693.0 kVA | 31.2% |
| 32_MVLV32089_Transformer | 440.0 kVA | 41.3% |
| 32_MVLV51133_Transformer | 440.0 kVA | 21.9% |
| 32_MVLV48764_Transformer | 440.0 kVA | 28.6% |
| 32_MVLV48686_Transformer | 275.0 kVA | 27.5% |
| 32_MVLV38223_Transformer | 693.0 kVA | 65.7% |
| 32_MVLV39017_Transformer | 346.5 kVA | 76.1% |
| 32_MVLV49500_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV67140_Transformer | 440.0 kVA | 32.1% |
| 32_MVLV73919_Transformer | 176.0 kVA | 43.2% |
| 32_MVLV57058_Transformer | 440.0 kVA | 46.6% |
| 32_MVLV74442_Transformer | 275.0 kVA | 38.3% |
| 32_MVLV73589_Transformer | 275.0 kVA | 24.8% |
| 32_MVLV25333_Transformer | 693.0 kVA | 52.5% |
| 32_MVLV74604_Transformer | 176.0 kVA | 76.9% |
| 32_MVLV78282_Transformer | 693.0 kVA | 35.8% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.64 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus272045' (LV, 0.24 kV) has an electrical reach of 5.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 333 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 333 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 18 |
| LV_236V | 4-wire | 315 / 315 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 315 |
| Neutral branches | 299 |
| Grounding points | 16 |
| Neutral sections | 16 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| exactly_balanced | 1 |
| decoupled | 1 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 3 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 18 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 52 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 3 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
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
| Line impedance spread | 1130.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 315 / 18 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 455 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 455 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1118773_consumption, 32_LVBus1118773_production, 32_LVBus1135347_production, 32_LVBus1135348_production, 32_LVBus1161085_production, 32_LVBus1161086_production, 32_LVBus271824_consumption, 32_LVBus271824_production, 32_LVBus271825_production, 32_LVBus271826_production, 32_LVBus271827_production, 32_LVBus271828_consumption, 32_LVBus271828_production, 32_LVBus271829_production, 32_LVBus271830_production, 32_LVBus271832_consumption, 32_LVBus271832_production, 32_LVBus271834_production, 32_LVBus271836_consumption, 32_LVBus271836_production, 32_LVBus271838_production, 32_LVBus271839_production, 32_LVBus271840_production, 32_LVBus271842_production, 32_LVBus271843_production, 32_LVBus271844_consumption, 32_LVBus271844_production, 32_LVBus271845_production, 32_LVBus271846_production, 32_LVBus271847_production, 32_LVBus271849_production, 32_LVBus271850_production, 32_LVBus271852_production, 32_LVBus271853_production, 32_LVBus271854_production, 32_LVBus271855_production, 32_LVBus271857_production, 32_LVBus271858_production, 32_LVBus271860_production, 32_LVBus271862_consumption, 32_LVBus271862_production, 32_LVBus271863_production, 32_LVBus271865_production, 32_LVBus271867_production, 32_LVBus271869_consumption, 32_LVBus271869_production, 32_LVBus271871_production, 32_LVBus271873_production, 32_LVBus271874_consumption, 32_LVBus271874_production, 32_LVBus271876_consumption, 32_LVBus271876_production, 32_LVBus271878_production, 32_LVBus271879_consumption, 32_LVBus271879_production, 32_LVBus271880_consumption, 32_LVBus271880_production, 32_LVBus271882_production, 32_LVBus271884_consumption, 32_LVBus271884_production, 32_LVBus271885_consumption, 32_LVBus271885_production, 32_LVBus271886_consumption, 32_LVBus271886_production, 32_LVBus271887_consumption, 32_LVBus271887_production, 32_LVBus271888_consumption, 32_LVBus271888_production, 32_LVBus271889_production, 32_LVBus271891_consumption, 32_LVBus271891_production, 32_LVBus271892_consumption, 32_LVBus271892_production, 32_LVBus271893_consumption, 32_LVBus271893_production, 32_LVBus271894_consumption, 32_LVBus271894_production, 32_LVBus271896_production, 32_LVBus271897_production, 32_LVBus271898_production, 32_LVBus271899_production, 32_LVBus271900_production, 32_LVBus271902_consumption, 32_LVBus271902_production, 32_LVBus271903_consumption, 32_LVBus271903_production, 32_LVBus271905_consumption, 32_LVBus271905_production, 32_LVBus271906_consumption, 32_LVBus271906_production, 32_LVBus271907_consumption, 32_LVBus271907_production, 32_LVBus271908_production, 32_LVBus271909_production, 32_LVBus271910_production, 32_LVBus271911_consumption, 32_LVBus271911_production, 32_LVBus271912_consumption, 32_LVBus271912_production, 32_LVBus271913_production, 32_LVBus271914_consumption, 32_LVBus271914_production, 32_LVBus271915_production, 32_LVBus271917_consumption, 32_LVBus271917_production, 32_LVBus271918_consumption, 32_LVBus271918_production, 32_LVBus271919_production, 32_LVBus271921_consumption, 32_LVBus271921_production, 32_LVBus271922_consumption, 32_LVBus271922_production, 32_LVBus271924_consumption, 32_LVBus271924_production, 32_LVBus271925_consumption, 32_LVBus271925_production, 32_LVBus271926_production, 32_LVBus271927_production, 32_LVBus271928_consumption, 32_LVBus271928_production, 32_LVBus271930_production, 32_LVBus271931_consumption, 32_LVBus271931_production, 32_LVBus271932_consumption, 32_LVBus271932_production, 32_LVBus271933_consumption, 32_LVBus271933_production, 32_LVBus271934_production, 32_LVBus271935_production, 32_LVBus271937_consumption, 32_LVBus271937_production, 32_LVBus271938_production, 32_LVBus271939_production, 32_LVBus271941_consumption, 32_LVBus271941_production, 32_LVBus271942_production, 32_LVBus271944_consumption, 32_LVBus271944_production, 32_LVBus271946_consumption, 32_LVBus271946_production, 32_LVBus271947_consumption, 32_LVBus271947_production, 32_LVBus271948_production, 32_LVBus271950_consumption, 32_LVBus271950_production, 32_LVBus271951_production, 32_LVBus271953_consumption, 32_LVBus271953_production, 32_LVBus271955_consumption, 32_LVBus271955_production, 32_LVBus271956_production, 32_LVBus271957_consumption, 32_LVBus271957_production, 32_LVBus271958_production, 32_LVBus271959_consumption, 32_LVBus271959_production, 32_LVBus271961_consumption, 32_LVBus271961_production, 32_LVBus271962_production, 32_LVBus271964_consumption, 32_LVBus271964_production, 32_LVBus271965_production, 32_LVBus271966_consumption, 32_LVBus271966_production, 32_LVBus271967_production, 32_LVBus271969_consumption, 32_LVBus271969_production, 32_LVBus271971_consumption, 32_LVBus271971_production, 32_LVBus271973_consumption, 32_LVBus271973_production, 32_LVBus271974_production, 32_LVBus271975_production, 32_LVBus271976_consumption, 32_LVBus271976_production, 32_LVBus271978_consumption, 32_LVBus271978_production, 32_LVBus271979_consumption, 32_LVBus271979_production, 32_LVBus271980_consumption, 32_LVBus271980_production, 32_LVBus271981_production, 32_LVBus271982_production, 32_LVBus271983_production, 32_LVBus271984_production, 32_LVBus271985_consumption, 32_LVBus271985_production, 32_LVBus271986_production, 32_LVBus271989_consumption, 32_LVBus271989_production, 32_LVBus271990_production, 32_LVBus271992_consumption, 32_LVBus271992_production, 32_LVBus271993_consumption, 32_LVBus271993_production, 32_LVBus271994_production, 32_LVBus271996_production, 32_LVBus271997_production, 32_LVBus271999_consumption, 32_LVBus271999_production, 32_LVBus272001_consumption, 32_LVBus272001_production, 32_LVBus272002_consumption, 32_LVBus272002_production, 32_LVBus272003_consumption, 32_LVBus272003_production, 32_LVBus272004_consumption, 32_LVBus272004_production, 32_LVBus272005_production, 32_LVBus272006_production, 32_LVBus272007_consumption, 32_LVBus272007_production, 32_LVBus272008_consumption, 32_LVBus272008_production, 32_LVBus272009_consumption, 32_LVBus272009_production, 32_LVBus272010_consumption, 32_LVBus272010_production, 32_LVBus272011_production, 32_LVBus272012_production, 32_LVBus272013_production, 32_LVBus272014_consumption, 32_LVBus272014_production, 32_LVBus272015_production, 32_LVBus272016_production, 32_LVBus272017_consumption, 32_LVBus272017_production, 32_LVBus272018_production, 32_LVBus272019_production, 32_LVBus272021_consumption, 32_LVBus272021_production, 32_LVBus272023_consumption, 32_LVBus272023_production, 32_LVBus272025_consumption, 32_LVBus272025_production, 32_LVBus272026_production, 32_LVBus272027_consumption, 32_LVBus272027_production, 32_LVBus272028_production, 32_LVBus272029_consumption, 32_LVBus272029_production, 32_LVBus272031_production, 32_LVBus272032_production, 32_LVBus272033_production, 32_LVBus272034_production, 32_LVBus272036_production, 32_LVBus272038_production, 32_LVBus272039_production, 32_LVBus272040_consumption, 32_LVBus272040_production, 32_LVBus272041_production, 32_LVBus272043_production, 32_LVBus272045_consumption, 32_LVBus272045_production, 32_LVBus272047_consumption, 32_LVBus272047_production, 32_LVBus272049_consumption, 32_LVBus272049_production, 32_LVBus272051_consumption, 32_LVBus272051_production, 32_LVBus272053_production, 32_LVBus272054_consumption, 32_LVBus272054_production, 32_LVBus272055_consumption, 32_LVBus272055_production, 32_LVBus272056_production, 32_LVBus272058_consumption, 32_LVBus272058_production, 32_LVBus272059_consumption, 32_LVBus272059_production, 32_LVBus272060_consumption, 32_LVBus272060_production, 32_LVBus272061_production, 32_LVBus272063_consumption, 32_LVBus272063_production, 32_LVBus272064_consumption, 32_LVBus272064_production, 32_LVBus272065_consumption, 32_LVBus272065_production, 32_LVBus272066_consumption, 32_LVBus272066_production, 32_LVBus272068_consumption, 32_LVBus272068_production, 32_LVBus272069_production, 32_LVBus272071_consumption, 32_LVBus272071_production, 32_LVBus272072_consumption, 32_LVBus272072_production, 32_LVBus272073_consumption, 32_LVBus272073_production, 32_LVBus272074_production, 32_LVBus272076_consumption, 32_LVBus272076_production, 32_LVBus272077_production, 32_LVBus272078_consumption, 32_LVBus272078_production, 32_LVBus272079_consumption, 32_LVBus272079_production, 32_LVBus272081_consumption, 32_LVBus272081_production, 32_LVBus272082_consumption, 32_LVBus272082_production, 32_LVBus272083_consumption, 32_LVBus272083_production, 32_LVBus272084_production, 32_LVBus272085_consumption, 32_LVBus272085_production, 32_LVBus272087_production, 32_LVBus272089_consumption, 32_LVBus272089_production, 32_LVBus272091_consumption, 32_LVBus272091_production, 32_LVBus272092_consumption, 32_LVBus272092_production, 32_LVBus272093_consumption, 32_LVBus272093_production, 32_LVBus272095_production, 32_LVBus272097_consumption, 32_LVBus272097_production, 32_LVBus272099_production, 32_LVBus272101_consumption, 32_LVBus272101_production, 32_LVBus272103_consumption, 32_LVBus272103_production, 32_LVBus272105_production, 32_LVBus272107_production, 32_LVBus272109_consumption, 32_LVBus272109_production, 32_LVBus272110_production, 32_LVBus272112_consumption, 32_LVBus272112_production, 32_LVBus272113_consumption, 32_LVBus272113_production, 32_LVBus272114_consumption, 32_LVBus272114_production, 32_LVBus272115_consumption, 32_LVBus272115_production, 32_LVBus272116_production, 32_LVBus272117_consumption, 32_LVBus272117_production, 32_LVBus272119_production, 32_LVBus272120_production, 32_LVBus272121_production, 32_LVBus272123_consumption, 32_LVBus272123_production, 32_LVBus272124_consumption, 32_LVBus272124_production, 32_LVBus272126_consumption, 32_LVBus272126_production, 32_LVBus272127_production, 32_LVBus272128_consumption, 32_LVBus272128_production, 32_LVBus272130_consumption, 32_LVBus272130_production, 32_LVBus272131_consumption, 32_LVBus272131_production, 32_LVBus272132_production, 32_LVBus272134_consumption, 32_LVBus272134_production, 32_LVBus272135_consumption, 32_LVBus272135_production, 32_LVBus272136_consumption, 32_LVBus272136_production, 32_LVBus272138_consumption, 32_LVBus272138_production, 32_LVBus272139_production, 32_LVBus272141_production, 32_LVBus272142_production, 32_LVBus272144_production, 32_LVBus272146_production, 32_LVBus272147_production, 32_LVBus272148_consumption, 32_LVBus272148_production, 32_LVBus272149_production, 32_LVBus272151_consumption, 32_LVBus272151_production, 32_LVBus272153_consumption, 32_LVBus272153_production, 32_LVBus272154_consumption, 32_LVBus272154_production, 32_LVBus272155_production, 32_LVBus272156_consumption, 32_LVBus272156_production, 32_LVBus272158_consumption, 32_LVBus272158_production, 32_LVBus272159_production, 32_LVBus272160_production, 32_LVBus272161_production, 32_LVBus272163_production, 32_LVBus272164_production, 32_LVBus272165_production, 32_LVBus272166_production, 32_LVBus272167_production, 32_LVBus272168_production, 32_LVBus272169_production, 32_LVBus272171_production, 32_LVBus272172_production, 32_LVBus272173_production, 32_LVBus272175_consumption, 32_LVBus272175_production, 32_LVBus272176_production, 32_LVBus272177_consumption, 32_LVBus272177_production, 32_LVBus272179_production, 32_LVBus272180_production, 32_LVBus272181_production, 32_LVBus272182_production, 32_LVBus272184_production, 32_LVBus272185_production, 32_LVBus272189_consumption, 32_LVBus272189_production, 32_LVBus272190_consumption, 32_LVBus272190_production, 32_LVBus272191_consumption, 32_LVBus272191_production, 32_LVBus272193_consumption, 32_LVBus272193_production, 32_LVBus272194_production, 32_LVBus272195_production, 32_LVBus272197_consumption, 32_LVBus272197_production, 32_LVBus272198_consumption, 32_LVBus272198_production, 32_LVBus272199_production, 32_LVBus272200_consumption, 32_LVBus272200_production, 32_LVBus272201_consumption, 32_LVBus272201_production, 32_LVBus272202_production, 32_LVBus272204_consumption, 32_LVBus272204_production, 32_LVBus272205_consumption, 32_LVBus272205_production, 32_LVBus272206_consumption, 32_LVBus272206_production, 32_LVBus272207_production, 32_LVBus272209_consumption, 32_LVBus272209_production, 32_LVBus272210_consumption, 32_LVBus272210_production, 32_LVBus272211_production, 32_LVBus272212_consumption, 32_LVBus272212_production, 32_LVBus272214_consumption, 32_LVBus272214_production, 32_LVBus272216_consumption, 32_LVBus272216_production, 32_LVBus272218_consumption, 32_LVBus272218_production, 32_LVBus272219_consumption, 32_LVBus272219_production, 32_LVBus272220_consumption, 32_LVBus272220_production, 32_MVLV67403_consumption, 32_MVLV67403_production.

## 9. Data Quality Summary

**Total findings:** 121 (0 errors, 4 warnings, 117 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  454 of 600 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.64 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  455 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271910_consumption`  
  Load '32_LVBus271910_consumption' has phase imbalance of 243.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272028_consumption`  
  Load '32_LVBus272028_consumption' has phase imbalance of 141.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272185_consumption`  
  Load '32_LVBus272185_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272016_consumption`  
  Load '32_LVBus272016_consumption' has phase imbalance of 257.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272127_consumption`  
  Load '32_LVBus272127_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271956_consumption`  
  Load '32_LVBus271956_consumption' has phase imbalance of 109.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272019_consumption`  
  Load '32_LVBus272019_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271860_consumption`  
  Load '32_LVBus271860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271900_consumption`  
  Load '32_LVBus271900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271825_consumption`  
  Load '32_LVBus271825_consumption' has phase imbalance of 146.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271974_consumption`  
  Load '32_LVBus271974_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271962_consumption`  
  Load '32_LVBus271962_consumption' has phase imbalance of 91.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272005_consumption`  
  Load '32_LVBus272005_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272149_consumption`  
  Load '32_LVBus272149_consumption' has phase imbalance of 139.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272146_consumption`  
  Load '32_LVBus272146_consumption' has phase imbalance of 219.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271878_consumption`  
  Load '32_LVBus271878_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271840_consumption`  
  Load '32_LVBus271840_consumption' has phase imbalance of 144.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272155_consumption`  
  Load '32_LVBus272155_consumption' has phase imbalance of 64.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272166_consumption`  
  Load '32_LVBus272166_consumption' has phase imbalance of 53.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272012_consumption`  
  Load '32_LVBus272012_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271983_consumption`  
  Load '32_LVBus271983_consumption' has phase imbalance of 203.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272181_consumption`  
  Load '32_LVBus272181_consumption' has phase imbalance of 156.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271934_consumption`  
  Load '32_LVBus271934_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272199_consumption`  
  Load '32_LVBus272199_consumption' has phase imbalance of 116.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272084_consumption`  
  Load '32_LVBus272084_consumption' has phase imbalance of 28.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271899_consumption`  
  Load '32_LVBus271899_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272026_consumption`  
  Load '32_LVBus272026_consumption' has phase imbalance of 103.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272182_consumption`  
  Load '32_LVBus272182_consumption' has phase imbalance of 29.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271827_consumption`  
  Load '32_LVBus271827_consumption' has phase imbalance of 82.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272139_consumption`  
  Load '32_LVBus272139_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272142_consumption`  
  Load '32_LVBus272142_consumption' has phase imbalance of 28.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272056_consumption`  
  Load '32_LVBus272056_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272034_consumption`  
  Load '32_LVBus272034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272184_consumption`  
  Load '32_LVBus272184_consumption' has phase imbalance of 100.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272171_consumption`  
  Load '32_LVBus272171_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271958_consumption`  
  Load '32_LVBus271958_consumption' has phase imbalance of 91.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272163_consumption`  
  Load '32_LVBus272163_consumption' has phase imbalance of 134.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271896_consumption`  
  Load '32_LVBus271896_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271849_consumption`  
  Load '32_LVBus271849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272018_consumption`  
  Load '32_LVBus272018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272167_consumption`  
  Load '32_LVBus272167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271846_consumption`  
  Load '32_LVBus271846_consumption' has phase imbalance of 64.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272031_consumption`  
  Load '32_LVBus272031_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272147_consumption`  
  Load '32_LVBus272147_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271935_consumption`  
  Load '32_LVBus271935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271926_consumption`  
  Load '32_LVBus271926_consumption' has phase imbalance of 37.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272141_consumption`  
  Load '32_LVBus272141_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272033_consumption`  
  Load '32_LVBus272033_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271951_consumption`  
  Load '32_LVBus271951_consumption' has phase imbalance of 33.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271854_consumption`  
  Load '32_LVBus271854_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271898_consumption`  
  Load '32_LVBus271898_consumption' has phase imbalance of 148.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271855_consumption`  
  Load '32_LVBus271855_consumption' has phase imbalance of 100.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272176_consumption`  
  Load '32_LVBus272176_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271986_consumption`  
  Load '32_LVBus271986_consumption' has phase imbalance of 139.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271915_consumption`  
  Load '32_LVBus271915_consumption' has phase imbalance of 49.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271938_consumption`  
  Load '32_LVBus271938_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272168_consumption`  
  Load '32_LVBus272168_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272077_consumption`  
  Load '32_LVBus272077_consumption' has phase imbalance of 33.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272074_consumption`  
  Load '32_LVBus272074_consumption' has phase imbalance of 39.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271930_consumption`  
  Load '32_LVBus271930_consumption' has phase imbalance of 212.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271826_consumption`  
  Load '32_LVBus271826_consumption' has phase imbalance of 106.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272053_consumption`  
  Load '32_LVBus272053_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271981_consumption`  
  Load '32_LVBus271981_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272159_consumption`  
  Load '32_LVBus272159_consumption' has phase imbalance of 24.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272164_consumption`  
  Load '32_LVBus272164_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272211_consumption`  
  Load '32_LVBus272211_consumption' has phase imbalance of 53.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272061_consumption`  
  Load '32_LVBus272061_consumption' has phase imbalance of 45.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271994_consumption`  
  Load '32_LVBus271994_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271852_consumption`  
  Load '32_LVBus271852_consumption' has phase imbalance of 95.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272202_consumption`  
  Load '32_LVBus272202_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271984_consumption`  
  Load '32_LVBus271984_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272179_consumption`  
  Load '32_LVBus272179_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272032_consumption`  
  Load '32_LVBus272032_consumption' has phase imbalance of 67.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271913_consumption`  
  Load '32_LVBus271913_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272119_consumption`  
  Load '32_LVBus272119_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272013_consumption`  
  Load '32_LVBus272013_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272120_consumption`  
  Load '32_LVBus272120_consumption' has phase imbalance of 69.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271897_consumption`  
  Load '32_LVBus271897_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271843_consumption`  
  Load '32_LVBus271843_consumption' has phase imbalance of 88.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272180_consumption`  
  Load '32_LVBus272180_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271996_consumption`  
  Load '32_LVBus271996_consumption' has phase imbalance of 110.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271982_consumption`  
  Load '32_LVBus271982_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271965_consumption`  
  Load '32_LVBus271965_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271908_consumption`  
  Load '32_LVBus271908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271838_consumption`  
  Load '32_LVBus271838_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272161_consumption`  
  Load '32_LVBus272161_consumption' has phase imbalance of 252.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271829_consumption`  
  Load '32_LVBus271829_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272195_consumption`  
  Load '32_LVBus272195_consumption' has phase imbalance of 50.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272172_consumption`  
  Load '32_LVBus272172_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272006_consumption`  
  Load '32_LVBus272006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272011_consumption`  
  Load '32_LVBus272011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271839_consumption`  
  Load '32_LVBus271839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272132_consumption`  
  Load '32_LVBus272132_consumption' has phase imbalance of 99.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271967_consumption`  
  Load '32_LVBus271967_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272173_consumption`  
  Load '32_LVBus272173_consumption' has phase imbalance of 140.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271909_consumption`  
  Load '32_LVBus271909_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus271830_consumption`  
  Load '32_LVBus271830_consumption' has phase imbalance of 108.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272015_consumption`  
  Load '32_LVBus272015_consumption' has phase imbalance of 236.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272165_consumption`  
  Load '32_LVBus272165_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus272039_consumption`  
  Load '32_LVBus272039_consumption' has phase imbalance of 66.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 600 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus1118773' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus271867' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus272045' (LV, 0.24 kV) has an electrical reach of 5.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 3 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  333 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  35 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus271839_consumption, 32_LVBus271849_consumption, 32_LVBus271860_consumption, 32_LVBus271897_consumption, 32_LVBus271900_consumption, 32_LVBus271908_consumption, 32_LVBus271913_consumption, 32_LVBus271930_consumption, 32_LVBus271934_consumption, 32_LVBus271935_consumption, 32_LVBus271965_consumption, 32_LVBus271982_consumption, 32_LVBus271983_consumption, 32_LVBus271984_consumption, 32_LVBus272005_consumption, 32_LVBus272006_consumption, 32_LVBus272011_consumption, 32_LVBus272012_consumption, 32_LVBus272015_consumption, 32_LVBus272016_consumption, 32_LVBus272018_consumption, 32_LVBus272019_consumption, 32_LVBus272034_consumption, 32_LVBus272056_consumption, 32_LVBus272119_consumption, 32_LVBus272146_consumption, 32_LVBus272147_consumption, 32_LVBus272161_consumption, 32_LVBus272164_consumption, 32_LVBus272167_consumption, 32_LVBus272168_consumption, 32_LVBus272171_consumption, 32_LVBus272176_consumption, 32_LVBus272179_consumption, 32_LVBus272180_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  300 group(s) of loads (600 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  455 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1118773_consumption, 32_LVBus1118773_production, 32_LVBus1135347_production, 32_LVBus1135348_production, 32_LVBus1161085_production, 32_LVBus1161086_production, 32_LVBus271824_consumption, 32_LVBus271824_production, 32_LVBus271825_production, 32_LVBus271826_production, 32_LVBus271827_production, 32_LVBus271828_consumption, 32_LVBus271828_production, 32_LVBus271829_production, 32_LVBus271830_production, 32_LVBus271832_consumption, 32_LVBus271832_production, 32_LVBus271834_production, 32_LVBus271836_consumption, 32_LVBus271836_production, 32_LVBus271838_production, 32_LVBus271839_production, 32_LVBus271840_production, 32_LVBus271842_production, 32_LVBus271843_production, 32_LVBus271844_consumption, 32_LVBus271844_production, 32_LVBus271845_production, 32_LVBus271846_production, 32_LVBus271847_production, 32_LVBus271849_production, 32_LVBus271850_production, 32_LVBus271852_production, 32_LVBus271853_production, 32_LVBus271854_production, 32_LVBus271855_production, 32_LVBus271857_production, 32_LVBus271858_production, 32_LVBus271860_production, 32_LVBus271862_consumption, 32_LVBus271862_production, 32_LVBus271863_production, 32_LVBus271865_production, 32_LVBus271867_production, 32_LVBus271869_consumption, 32_LVBus271869_production, 32_LVBus271871_production, 32_LVBus271873_production, 32_LVBus271874_consumption, 32_LVBus271874_production, 32_LVBus271876_consumption, 32_LVBus271876_production, 32_LVBus271878_production, 32_LVBus271879_consumption, 32_LVBus271879_production, 32_LVBus271880_consumption, 32_LVBus271880_production, 32_LVBus271882_production, 32_LVBus271884_consumption, 32_LVBus271884_production, 32_LVBus271885_consumption, 32_LVBus271885_production, 32_LVBus271886_consumption, 32_LVBus271886_production, 32_LVBus271887_consumption, 32_LVBus271887_production, 32_LVBus271888_consumption, 32_LVBus271888_production, 32_LVBus271889_production, 32_LVBus271891_consumption, 32_LVBus271891_production, 32_LVBus271892_consumption, 32_LVBus271892_production, 32_LVBus271893_consumption, 32_LVBus271893_production, 32_LVBus271894_consumption, 32_LVBus271894_production, 32_LVBus271896_production, 32_LVBus271897_production, 32_LVBus271898_production, 32_LVBus271899_production, 32_LVBus271900_production, 32_LVBus271902_consumption, 32_LVBus271902_production, 32_LVBus271903_consumption, 32_LVBus271903_production, 32_LVBus271905_consumption, 32_LVBus271905_production, 32_LVBus271906_consumption, 32_LVBus271906_production, 32_LVBus271907_consumption, 32_LVBus271907_production, 32_LVBus271908_production, 32_LVBus271909_production, 32_LVBus271910_production, 32_LVBus271911_consumption, 32_LVBus271911_production, 32_LVBus271912_consumption, 32_LVBus271912_production, 32_LVBus271913_production, 32_LVBus271914_consumption, 32_LVBus271914_production, 32_LVBus271915_production, 32_LVBus271917_consumption, 32_LVBus271917_production, 32_LVBus271918_consumption, 32_LVBus271918_production, 32_LVBus271919_production, 32_LVBus271921_consumption, 32_LVBus271921_production, 32_LVBus271922_consumption, 32_LVBus271922_production, 32_LVBus271924_consumption, 32_LVBus271924_production, 32_LVBus271925_consumption, 32_LVBus271925_production, 32_LVBus271926_production, 32_LVBus271927_production, 32_LVBus271928_consumption, 32_LVBus271928_production, 32_LVBus271930_production, 32_LVBus271931_consumption, 32_LVBus271931_production, 32_LVBus271932_consumption, 32_LVBus271932_production, 32_LVBus271933_consumption, 32_LVBus271933_production, 32_LVBus271934_production, 32_LVBus271935_production, 32_LVBus271937_consumption, 32_LVBus271937_production, 32_LVBus271938_production, 32_LVBus271939_production, 32_LVBus271941_consumption, 32_LVBus271941_production, 32_LVBus271942_production, 32_LVBus271944_consumption, 32_LVBus271944_production, 32_LVBus271946_consumption, 32_LVBus271946_production, 32_LVBus271947_consumption, 32_LVBus271947_production, 32_LVBus271948_production, 32_LVBus271950_consumption, 32_LVBus271950_production, 32_LVBus271951_production, 32_LVBus271953_consumption, 32_LVBus271953_production, 32_LVBus271955_consumption, 32_LVBus271955_production, 32_LVBus271956_production, 32_LVBus271957_consumption, 32_LVBus271957_production, 32_LVBus271958_production, 32_LVBus271959_consumption, 32_LVBus271959_production, 32_LVBus271961_consumption, 32_LVBus271961_production, 32_LVBus271962_production, 32_LVBus271964_consumption, 32_LVBus271964_production, 32_LVBus271965_production, 32_LVBus271966_consumption, 32_LVBus271966_production, 32_LVBus271967_production, 32_LVBus271969_consumption, 32_LVBus271969_production, 32_LVBus271971_consumption, 32_LVBus271971_production, 32_LVBus271973_consumption, 32_LVBus271973_production, 32_LVBus271974_production, 32_LVBus271975_production, 32_LVBus271976_consumption, 32_LVBus271976_production, 32_LVBus271978_consumption, 32_LVBus271978_production, 32_LVBus271979_consumption, 32_LVBus271979_production, 32_LVBus271980_consumption, 32_LVBus271980_production, 32_LVBus271981_production, 32_LVBus271982_production, 32_LVBus271983_production, 32_LVBus271984_production, 32_LVBus271985_consumption, 32_LVBus271985_production, 32_LVBus271986_production, 32_LVBus271989_consumption, 32_LVBus271989_production, 32_LVBus271990_production, 32_LVBus271992_consumption, 32_LVBus271992_production, 32_LVBus271993_consumption, 32_LVBus271993_production, 32_LVBus271994_production, 32_LVBus271996_production, 32_LVBus271997_production, 32_LVBus271999_consumption, 32_LVBus271999_production, 32_LVBus272001_consumption, 32_LVBus272001_production, 32_LVBus272002_consumption, 32_LVBus272002_production, 32_LVBus272003_consumption, 32_LVBus272003_production, 32_LVBus272004_consumption, 32_LVBus272004_production, 32_LVBus272005_production, 32_LVBus272006_production, 32_LVBus272007_consumption, 32_LVBus272007_production, 32_LVBus272008_consumption, 32_LVBus272008_production, 32_LVBus272009_consumption, 32_LVBus272009_production, 32_LVBus272010_consumption, 32_LVBus272010_production, 32_LVBus272011_production, 32_LVBus272012_production, 32_LVBus272013_production, 32_LVBus272014_consumption, 32_LVBus272014_production, 32_LVBus272015_production, 32_LVBus272016_production, 32_LVBus272017_consumption, 32_LVBus272017_production, 32_LVBus272018_production, 32_LVBus272019_production, 32_LVBus272021_consumption, 32_LVBus272021_production, 32_LVBus272023_consumption, 32_LVBus272023_production, 32_LVBus272025_consumption, 32_LVBus272025_production, 32_LVBus272026_production, 32_LVBus272027_consumption, 32_LVBus272027_production, 32_LVBus272028_production, 32_LVBus272029_consumption, 32_LVBus272029_production, 32_LVBus272031_production, 32_LVBus272032_production, 32_LVBus272033_production, 32_LVBus272034_production, 32_LVBus272036_production, 32_LVBus272038_production, 32_LVBus272039_production, 32_LVBus272040_consumption, 32_LVBus272040_production, 32_LVBus272041_production, 32_LVBus272043_production, 32_LVBus272045_consumption, 32_LVBus272045_production, 32_LVBus272047_consumption, 32_LVBus272047_production, 32_LVBus272049_consumption, 32_LVBus272049_production, 32_LVBus272051_consumption, 32_LVBus272051_production, 32_LVBus272053_production, 32_LVBus272054_consumption, 32_LVBus272054_production, 32_LVBus272055_consumption, 32_LVBus272055_production, 32_LVBus272056_production, 32_LVBus272058_consumption, 32_LVBus272058_production, 32_LVBus272059_consumption, 32_LVBus272059_production, 32_LVBus272060_consumption, 32_LVBus272060_production, 32_LVBus272061_production, 32_LVBus272063_consumption, 32_LVBus272063_production, 32_LVBus272064_consumption, 32_LVBus272064_production, 32_LVBus272065_consumption, 32_LVBus272065_production, 32_LVBus272066_consumption, 32_LVBus272066_production, 32_LVBus272068_consumption, 32_LVBus272068_production, 32_LVBus272069_production, 32_LVBus272071_consumption, 32_LVBus272071_production, 32_LVBus272072_consumption, 32_LVBus272072_production, 32_LVBus272073_consumption, 32_LVBus272073_production, 32_LVBus272074_production, 32_LVBus272076_consumption, 32_LVBus272076_production, 32_LVBus272077_production, 32_LVBus272078_consumption, 32_LVBus272078_production, 32_LVBus272079_consumption, 32_LVBus272079_production, 32_LVBus272081_consumption, 32_LVBus272081_production, 32_LVBus272082_consumption, 32_LVBus272082_production, 32_LVBus272083_consumption, 32_LVBus272083_production, 32_LVBus272084_production, 32_LVBus272085_consumption, 32_LVBus272085_production, 32_LVBus272087_production, 32_LVBus272089_consumption, 32_LVBus272089_production, 32_LVBus272091_consumption, 32_LVBus272091_production, 32_LVBus272092_consumption, 32_LVBus272092_production, 32_LVBus272093_consumption, 32_LVBus272093_production, 32_LVBus272095_production, 32_LVBus272097_consumption, 32_LVBus272097_production, 32_LVBus272099_production, 32_LVBus272101_consumption, 32_LVBus272101_production, 32_LVBus272103_consumption, 32_LVBus272103_production, 32_LVBus272105_production, 32_LVBus272107_production, 32_LVBus272109_consumption, 32_LVBus272109_production, 32_LVBus272110_production, 32_LVBus272112_consumption, 32_LVBus272112_production, 32_LVBus272113_consumption, 32_LVBus272113_production, 32_LVBus272114_consumption, 32_LVBus272114_production, 32_LVBus272115_consumption, 32_LVBus272115_production, 32_LVBus272116_production, 32_LVBus272117_consumption, 32_LVBus272117_production, 32_LVBus272119_production, 32_LVBus272120_production, 32_LVBus272121_production, 32_LVBus272123_consumption, 32_LVBus272123_production, 32_LVBus272124_consumption, 32_LVBus272124_production, 32_LVBus272126_consumption, 32_LVBus272126_production, 32_LVBus272127_production, 32_LVBus272128_consumption, 32_LVBus272128_production, 32_LVBus272130_consumption, 32_LVBus272130_production, 32_LVBus272131_consumption, 32_LVBus272131_production, 32_LVBus272132_production, 32_LVBus272134_consumption, 32_LVBus272134_production, 32_LVBus272135_consumption, 32_LVBus272135_production, 32_LVBus272136_consumption, 32_LVBus272136_production, 32_LVBus272138_consumption, 32_LVBus272138_production, 32_LVBus272139_production, 32_LVBus272141_production, 32_LVBus272142_production, 32_LVBus272144_production, 32_LVBus272146_production, 32_LVBus272147_production, 32_LVBus272148_consumption, 32_LVBus272148_production, 32_LVBus272149_production, 32_LVBus272151_consumption, 32_LVBus272151_production, 32_LVBus272153_consumption, 32_LVBus272153_production, 32_LVBus272154_consumption, 32_LVBus272154_production, 32_LVBus272155_production, 32_LVBus272156_consumption, 32_LVBus272156_production, 32_LVBus272158_consumption, 32_LVBus272158_production, 32_LVBus272159_production, 32_LVBus272160_production, 32_LVBus272161_production, 32_LVBus272163_production, 32_LVBus272164_production, 32_LVBus272165_production, 32_LVBus272166_production, 32_LVBus272167_production, 32_LVBus272168_production, 32_LVBus272169_production, 32_LVBus272171_production, 32_LVBus272172_production, 32_LVBus272173_production, 32_LVBus272175_consumption, 32_LVBus272175_production, 32_LVBus272176_production, 32_LVBus272177_consumption, 32_LVBus272177_production, 32_LVBus272179_production, 32_LVBus272180_production, 32_LVBus272181_production, 32_LVBus272182_production, 32_LVBus272184_production, 32_LVBus272185_production, 32_LVBus272189_consumption, 32_LVBus272189_production, 32_LVBus272190_consumption, 32_LVBus272190_production, 32_LVBus272191_consumption, 32_LVBus272191_production, 32_LVBus272193_consumption, 32_LVBus272193_production, 32_LVBus272194_production, 32_LVBus272195_production, 32_LVBus272197_consumption, 32_LVBus272197_production, 32_LVBus272198_consumption, 32_LVBus272198_production, 32_LVBus272199_production, 32_LVBus272200_consumption, 32_LVBus272200_production, 32_LVBus272201_consumption, 32_LVBus272201_production, 32_LVBus272202_production, 32_LVBus272204_consumption, 32_LVBus272204_production, 32_LVBus272205_consumption, 32_LVBus272205_production, 32_LVBus272206_consumption, 32_LVBus272206_production, 32_LVBus272207_production, 32_LVBus272209_consumption, 32_LVBus272209_production, 32_LVBus272210_consumption, 32_LVBus272210_production, 32_LVBus272211_production, 32_LVBus272212_consumption, 32_LVBus272212_production, 32_LVBus272214_consumption, 32_LVBus272214_production, 32_LVBus272216_consumption, 32_LVBus272216_production, 32_LVBus272218_consumption, 32_LVBus272218_production, 32_LVBus272219_consumption, 32_LVBus272219_production, 32_LVBus272220_consumption, 32_LVBus272220_production, 32_MVLV67403_consumption, 32_MVLV67403_production.

