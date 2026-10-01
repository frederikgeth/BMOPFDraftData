# BMOPF Network Summary: 75_MVFeeder0423

**Generated:** 2026-10-01 23:34:22  
**Findings:** 0 errors · 4 warnings · 115 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 24 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 221 |  |
| line | 196 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 312 | 692.867 kW, 207.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 24 |  |
| switch | 0 |  |
| transformer | 24 | Dyn11×24 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 42 | 41 | 2 | 0 |
| LV_236V | 236.0 V | 179 | 155 | 310 | 0 |

**Transformer transitions:**

- `75_MVLV077588_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV156203_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV017852_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV151962_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV028782_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV032803_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV150845_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV151758_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036157_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV028681_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV137872_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV051497_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002110_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV112643_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV172245_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002058_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047702_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV133784_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV091947_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067970_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV077743_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV105666_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV156253_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV028711_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 5 |
| Degree-1 buses | 81 |
| Tree depth (max hops) | 21 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 221 | 1 | 220 | 0 | 0 | 0 |
| Tier LV_236V | 179 | 24 | 155 | 0 | 0 | 0 |
| Tier MV_11.8kV | 42 | 1 | 41 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 24; skipped invalid branches: 0.

Galvanic zones: 25; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_BAZAS | MV_11.8kV | 42 | 0 | 0 | 24 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

842 declared bus terminals; 743 mapped line/closed-switch conductor edges; 99 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 24000.0 | 3.177 | 936 |
| q_nom | 0.0 | 7200.0 | 3.177 | 936 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.92 | 2590.0 | 1.393 | 196 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.525 | 24 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 204 of 312 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142207_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142090_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142055_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142117_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142121_consumption' has phase imbalance of 277.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142155_consumption' has phase imbalance of 272.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142126_consumption' has phase imbalance of 175.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142226_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142213_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142171_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142169_consumption' has phase imbalance of 62.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142232_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142122_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142105_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142158_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142128_consumption' has phase imbalance of 129.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142099_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142196_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142159_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142102_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142225_consumption' has phase imbalance of 21.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142141_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142214_consumption' has phase imbalance of 29.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142103_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142217_consumption' has phase imbalance of 157.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142052_consumption' has phase imbalance of 278.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142041_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142187_consumption' has phase imbalance of 246.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142096_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142184_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142036_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142215_consumption' has phase imbalance of 243.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142110_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142165_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142115_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142054_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142065_consumption' has phase imbalance of 216.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142212_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142201_consumption' has phase imbalance of 167.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142107_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142034_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142040_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142228_consumption' has phase imbalance of 24.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142120_consumption' has phase imbalance of 286.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142145_consumption' has phase imbalance of 174.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142188_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142151_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142100_consumption' has phase imbalance of 282.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1142119_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 312 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 692.867 kW |
| Total load Q | 207.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV077588_Transformer | 110.0 kVA | 7.5% |
| 75_MVLV156203_Transformer | 110.0 kVA | 30.5% |
| 75_MVLV017852_Transformer | 110.0 kVA | 18.9% |
| 75_MVLV151962_Transformer | 176.0 kVA | 11.1% |
| 75_MVLV028782_Transformer | 176.0 kVA | 6.8% |
| 75_MVLV032803_Transformer | 176.0 kVA | 9.3% |
| 75_MVLV150845_Transformer | 176.0 kVA | 15.3% |
| 75_MVLV151758_Transformer | 176.0 kVA | 27.0% |
| 75_MVLV036157_Transformer | 176.0 kVA | 25.4% |
| 75_MVLV028681_Transformer | 110.0 kVA | 5.4% |
| 75_MVLV137872_Transformer | 440.0 kVA | 21.2% |
| 75_MVLV051497_Transformer | 275.0 kVA | 20.5% |
| 75_MVLV002110_Transformer | 176.0 kVA | 18.9% |
| 75_MVLV112643_Transformer | 275.0 kVA | 7.1% |
| 75_MVLV172245_Transformer | 110.0 kVA | 2.9% |
| 75_MVLV002058_Transformer | 176.0 kVA | 36.7% |
| 75_MVLV047702_Transformer | 440.0 kVA | 22.5% |
| 75_MVLV133784_Transformer | 110.0 kVA | 3.0% |
| 75_MVLV091947_Transformer | 110.0 kVA | 9.0% |
| 75_MVLV067970_Transformer | 110.0 kVA | 0.2% |
| 75_MVLV077743_Transformer | 176.0 kVA | 27.5% |
| 75_MVLV105666_Transformer | 176.0 kVA | 7.7% |
| 75_MVLV156253_Transformer | 110.0 kVA | 14.5% |
| 75_MVLV028711_Transformer | 110.0 kVA | 24.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.69 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_LVBus1142190' (LV, 0.24 kV) has an electrical reach of 1.06 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 221 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 221 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 24 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 42 |
| LV_236V | 4-wire | 179 / 179 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 179 |
| Neutral branches | 155 |
| Grounding points | 24 |
| Neutral sections | 24 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| exactly_balanced | 1 |
| decoupled | 3 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 5 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 42 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 3 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, O_AM_54, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 5 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 3 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, O_AM_54, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 25 |
| Islands without voltage reference | 0 |
| Line impedance spread | 670.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 179 / 42 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 205 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 205 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1142034_production, 75_LVBus1142036_production, 75_LVBus1142038_production, 75_LVBus1142039_production, 75_LVBus1142040_production, 75_LVBus1142041_production, 75_LVBus1142042_production, 75_LVBus1142043_consumption, 75_LVBus1142043_production, 75_LVBus1142044_production, 75_LVBus1142045_production, 75_LVBus1142049_consumption, 75_LVBus1142049_production, 75_LVBus1142050_consumption, 75_LVBus1142050_production, 75_LVBus1142051_production, 75_LVBus1142052_production, 75_LVBus1142054_production, 75_LVBus1142055_production, 75_LVBus1142056_consumption, 75_LVBus1142056_production, 75_LVBus1142057_consumption, 75_LVBus1142057_production, 75_LVBus1142059_consumption, 75_LVBus1142059_production, 75_LVBus1142060_production, 75_LVBus1142062_consumption, 75_LVBus1142062_production, 75_LVBus1142065_production, 75_LVBus1142066_production, 75_LVBus1142067_production, 75_LVBus1142069_production, 75_LVBus1142071_consumption, 75_LVBus1142071_production, 75_LVBus1142072_production, 75_LVBus1142073_consumption, 75_LVBus1142073_production, 75_LVBus1142074_production, 75_LVBus1142075_consumption, 75_LVBus1142075_production, 75_LVBus1142076_production, 75_LVBus1142077_production, 75_LVBus1142078_production, 75_LVBus1142082_consumption, 75_LVBus1142082_production, 75_LVBus1142083_consumption, 75_LVBus1142083_production, 75_LVBus1142084_production, 75_LVBus1142085_consumption, 75_LVBus1142085_production, 75_LVBus1142086_production, 75_LVBus1142087_production, 75_LVBus1142088_production, 75_LVBus1142090_production, 75_LVBus1142091_production, 75_LVBus1142092_production, 75_LVBus1142093_consumption, 75_LVBus1142093_production, 75_LVBus1142094_production, 75_LVBus1142095_production, 75_LVBus1142096_production, 75_LVBus1142098_consumption, 75_LVBus1142098_production, 75_LVBus1142099_production, 75_LVBus1142100_production, 75_LVBus1142101_production, 75_LVBus1142102_production, 75_LVBus1142103_production, 75_LVBus1142104_production, 75_LVBus1142105_production, 75_LVBus1142107_production, 75_LVBus1142108_production, 75_LVBus1142109_production, 75_LVBus1142110_production, 75_LVBus1142111_consumption, 75_LVBus1142111_production, 75_LVBus1142112_production, 75_LVBus1142113_production, 75_LVBus1142115_production, 75_LVBus1142116_consumption, 75_LVBus1142116_production, 75_LVBus1142117_production, 75_LVBus1142119_production, 75_LVBus1142120_production, 75_LVBus1142121_production, 75_LVBus1142122_production, 75_LVBus1142123_consumption, 75_LVBus1142123_production, 75_LVBus1142124_production, 75_LVBus1142125_production, 75_LVBus1142126_production, 75_LVBus1142128_production, 75_LVBus1142129_production, 75_LVBus1142130_production, 75_LVBus1142132_consumption, 75_LVBus1142132_production, 75_LVBus1142134_production, 75_LVBus1142136_consumption, 75_LVBus1142136_production, 75_LVBus1142137_consumption, 75_LVBus1142137_production, 75_LVBus1142138_production, 75_LVBus1142139_consumption, 75_LVBus1142139_production, 75_LVBus1142140_consumption, 75_LVBus1142140_production, 75_LVBus1142141_production, 75_LVBus1142143_production, 75_LVBus1142144_production, 75_LVBus1142145_production, 75_LVBus1142147_consumption, 75_LVBus1142147_production, 75_LVBus1142148_production, 75_LVBus1142149_consumption, 75_LVBus1142149_production, 75_LVBus1142150_production, 75_LVBus1142151_production, 75_LVBus1142153_consumption, 75_LVBus1142153_production, 75_LVBus1142154_production, 75_LVBus1142155_production, 75_LVBus1142157_consumption, 75_LVBus1142157_production, 75_LVBus1142158_production, 75_LVBus1142159_production, 75_LVBus1142160_consumption, 75_LVBus1142160_production, 75_LVBus1142161_production, 75_LVBus1142163_consumption, 75_LVBus1142163_production, 75_LVBus1142164_consumption, 75_LVBus1142164_production, 75_LVBus1142165_production, 75_LVBus1142166_production, 75_LVBus1142167_consumption, 75_LVBus1142167_production, 75_LVBus1142168_production, 75_LVBus1142169_production, 75_LVBus1142170_production, 75_LVBus1142171_production, 75_LVBus1142177_production, 75_LVBus1142178_consumption, 75_LVBus1142178_production, 75_LVBus1142179_consumption, 75_LVBus1142179_production, 75_LVBus1142180_production, 75_LVBus1142182_consumption, 75_LVBus1142182_production, 75_LVBus1142184_production, 75_LVBus1142186_consumption, 75_LVBus1142186_production, 75_LVBus1142187_production, 75_LVBus1142188_production, 75_LVBus1142190_consumption, 75_LVBus1142190_production, 75_LVBus1142191_consumption, 75_LVBus1142191_production, 75_LVBus1142192_production, 75_LVBus1142193_consumption, 75_LVBus1142193_production, 75_LVBus1142195_production, 75_LVBus1142196_production, 75_LVBus1142198_consumption, 75_LVBus1142198_production, 75_LVBus1142199_production, 75_LVBus1142200_consumption, 75_LVBus1142200_production, 75_LVBus1142201_production, 75_LVBus1142203_production, 75_LVBus1142204_production, 75_LVBus1142205_production, 75_LVBus1142206_production, 75_LVBus1142207_production, 75_LVBus1142208_production, 75_LVBus1142209_production, 75_LVBus1142210_consumption, 75_LVBus1142210_production, 75_LVBus1142212_production, 75_LVBus1142213_production, 75_LVBus1142214_production, 75_LVBus1142215_production, 75_LVBus1142216_consumption, 75_LVBus1142216_production, 75_LVBus1142217_production, 75_LVBus1142218_consumption, 75_LVBus1142218_production, 75_LVBus1142219_consumption, 75_LVBus1142219_production, 75_LVBus1142220_consumption, 75_LVBus1142220_production, 75_LVBus1142221_production, 75_LVBus1142223_production, 75_LVBus1142225_production, 75_LVBus1142226_production, 75_LVBus1142228_production, 75_LVBus1142229_consumption, 75_LVBus1142229_production, 75_LVBus1142231_consumption, 75_LVBus1142231_production, 75_LVBus1142232_production, 75_LVBus1142233_production, 75_LVBus1142234_consumption, 75_LVBus1142234_production, 75_MVLV054856_consumption, 75_MVLV054856_production.

## 9. Data Quality Summary

**Total findings:** 119 (0 errors, 4 warnings, 115 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  204 of 312 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.69 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  205 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142130_consumption`  
  Load '75_LVBus1142130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142124_consumption`  
  Load '75_LVBus1142124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142207_consumption`  
  Load '75_LVBus1142207_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142090_consumption`  
  Load '75_LVBus1142090_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142055_consumption`  
  Load '75_LVBus1142055_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142117_consumption`  
  Load '75_LVBus1142117_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142121_consumption`  
  Load '75_LVBus1142121_consumption' has phase imbalance of 277.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142154_consumption`  
  Load '75_LVBus1142154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142155_consumption`  
  Load '75_LVBus1142155_consumption' has phase imbalance of 272.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142126_consumption`  
  Load '75_LVBus1142126_consumption' has phase imbalance of 175.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142226_consumption`  
  Load '75_LVBus1142226_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142134_consumption`  
  Load '75_LVBus1142134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142213_consumption`  
  Load '75_LVBus1142213_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142171_consumption`  
  Load '75_LVBus1142171_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142169_consumption`  
  Load '75_LVBus1142169_consumption' has phase imbalance of 62.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142144_consumption`  
  Load '75_LVBus1142144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142039_consumption`  
  Load '75_LVBus1142039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142232_consumption`  
  Load '75_LVBus1142232_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142109_consumption`  
  Load '75_LVBus1142109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142067_consumption`  
  Load '75_LVBus1142067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142208_consumption`  
  Load '75_LVBus1142208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142101_consumption`  
  Load '75_LVBus1142101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142069_consumption`  
  Load '75_LVBus1142069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142122_consumption`  
  Load '75_LVBus1142122_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142105_consumption`  
  Load '75_LVBus1142105_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142158_consumption`  
  Load '75_LVBus1142158_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142128_consumption`  
  Load '75_LVBus1142128_consumption' has phase imbalance of 129.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142099_consumption`  
  Load '75_LVBus1142099_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142195_consumption`  
  Load '75_LVBus1142195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142196_consumption`  
  Load '75_LVBus1142196_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142104_consumption`  
  Load '75_LVBus1142104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142170_consumption`  
  Load '75_LVBus1142170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142138_consumption`  
  Load '75_LVBus1142138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142159_consumption`  
  Load '75_LVBus1142159_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142102_consumption`  
  Load '75_LVBus1142102_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142148_consumption`  
  Load '75_LVBus1142148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142225_consumption`  
  Load '75_LVBus1142225_consumption' has phase imbalance of 21.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142084_consumption`  
  Load '75_LVBus1142084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142042_consumption`  
  Load '75_LVBus1142042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142141_consumption`  
  Load '75_LVBus1142141_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142214_consumption`  
  Load '75_LVBus1142214_consumption' has phase imbalance of 29.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142078_consumption`  
  Load '75_LVBus1142078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142060_consumption`  
  Load '75_LVBus1142060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142091_consumption`  
  Load '75_LVBus1142091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142223_consumption`  
  Load '75_LVBus1142223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142103_consumption`  
  Load '75_LVBus1142103_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142217_consumption`  
  Load '75_LVBus1142217_consumption' has phase imbalance of 157.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142095_consumption`  
  Load '75_LVBus1142095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142052_consumption`  
  Load '75_LVBus1142052_consumption' has phase imbalance of 278.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142041_consumption`  
  Load '75_LVBus1142041_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142187_consumption`  
  Load '75_LVBus1142187_consumption' has phase imbalance of 246.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142096_consumption`  
  Load '75_LVBus1142096_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142184_consumption`  
  Load '75_LVBus1142184_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142206_consumption`  
  Load '75_LVBus1142206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142221_consumption`  
  Load '75_LVBus1142221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142161_consumption`  
  Load '75_LVBus1142161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142051_consumption`  
  Load '75_LVBus1142051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142044_consumption`  
  Load '75_LVBus1142044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142036_consumption`  
  Load '75_LVBus1142036_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142215_consumption`  
  Load '75_LVBus1142215_consumption' has phase imbalance of 243.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142110_consumption`  
  Load '75_LVBus1142110_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142165_consumption`  
  Load '75_LVBus1142165_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142115_consumption`  
  Load '75_LVBus1142115_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142054_consumption`  
  Load '75_LVBus1142054_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142066_consumption`  
  Load '75_LVBus1142066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142203_consumption`  
  Load '75_LVBus1142203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142192_consumption`  
  Load '75_LVBus1142192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142065_consumption`  
  Load '75_LVBus1142065_consumption' has phase imbalance of 216.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142076_consumption`  
  Load '75_LVBus1142076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142112_consumption`  
  Load '75_LVBus1142112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142205_consumption`  
  Load '75_LVBus1142205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142233_consumption`  
  Load '75_LVBus1142233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142045_consumption`  
  Load '75_LVBus1142045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142094_consumption`  
  Load '75_LVBus1142094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142212_consumption`  
  Load '75_LVBus1142212_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142072_consumption`  
  Load '75_LVBus1142072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142199_consumption`  
  Load '75_LVBus1142199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142201_consumption`  
  Load '75_LVBus1142201_consumption' has phase imbalance of 167.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142177_consumption`  
  Load '75_LVBus1142177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142086_consumption`  
  Load '75_LVBus1142086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142074_consumption`  
  Load '75_LVBus1142074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142107_consumption`  
  Load '75_LVBus1142107_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142034_consumption`  
  Load '75_LVBus1142034_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142168_consumption`  
  Load '75_LVBus1142168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142204_consumption`  
  Load '75_LVBus1142204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142038_consumption`  
  Load '75_LVBus1142038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142040_consumption`  
  Load '75_LVBus1142040_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142228_consumption`  
  Load '75_LVBus1142228_consumption' has phase imbalance of 24.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142077_consumption`  
  Load '75_LVBus1142077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142129_consumption`  
  Load '75_LVBus1142129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142120_consumption`  
  Load '75_LVBus1142120_consumption' has phase imbalance of 286.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142088_consumption`  
  Load '75_LVBus1142088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142145_consumption`  
  Load '75_LVBus1142145_consumption' has phase imbalance of 174.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142092_consumption`  
  Load '75_LVBus1142092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142188_consumption`  
  Load '75_LVBus1142188_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142180_consumption`  
  Load '75_LVBus1142180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142151_consumption`  
  Load '75_LVBus1142151_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142100_consumption`  
  Load '75_LVBus1142100_consumption' has phase imbalance of 282.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1142119_consumption`  
  Load '75_LVBus1142119_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 312 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_LVBus1142190' (LV, 0.24 kV) has an electrical reach of 1.06 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  3 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, O_AM_54, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 5 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  3 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, O_AM_54, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  221 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  91 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1142038_consumption, 75_LVBus1142039_consumption, 75_LVBus1142040_consumption, 75_LVBus1142041_consumption, 75_LVBus1142042_consumption, 75_LVBus1142044_consumption, 75_LVBus1142045_consumption, 75_LVBus1142051_consumption, 75_LVBus1142052_consumption, 75_LVBus1142054_consumption, 75_LVBus1142055_consumption, 75_LVBus1142060_consumption, 75_LVBus1142065_consumption, 75_LVBus1142066_consumption, 75_LVBus1142067_consumption, 75_LVBus1142069_consumption, 75_LVBus1142072_consumption, 75_LVBus1142074_consumption, 75_LVBus1142076_consumption, 75_LVBus1142077_consumption, 75_LVBus1142078_consumption, 75_LVBus1142084_consumption, 75_LVBus1142086_consumption, 75_LVBus1142088_consumption, 75_LVBus1142090_consumption, 75_LVBus1142091_consumption, 75_LVBus1142092_consumption, 75_LVBus1142094_consumption, 75_LVBus1142095_consumption, 75_LVBus1142096_consumption, 75_LVBus1142099_consumption, 75_LVBus1142100_consumption, 75_LVBus1142101_consumption, 75_LVBus1142102_consumption, 75_LVBus1142103_consumption, 75_LVBus1142104_consumption, 75_LVBus1142105_consumption, 75_LVBus1142107_consumption, 75_LVBus1142109_consumption, 75_LVBus1142110_consumption, 75_LVBus1142112_consumption, 75_LVBus1142115_consumption, 75_LVBus1142117_consumption, 75_LVBus1142119_consumption, 75_LVBus1142120_consumption, 75_LVBus1142121_consumption, 75_LVBus1142122_consumption, 75_LVBus1142124_consumption, 75_LVBus1142126_consumption, 75_LVBus1142129_consumption, 75_LVBus1142130_consumption, 75_LVBus1142134_consumption, 75_LVBus1142138_consumption, 75_LVBus1142141_consumption, 75_LVBus1142144_consumption, 75_LVBus1142145_consumption, 75_LVBus1142148_consumption, 75_LVBus1142151_consumption, 75_LVBus1142154_consumption, 75_LVBus1142155_consumption, 75_LVBus1142158_consumption, 75_LVBus1142159_consumption, 75_LVBus1142161_consumption, 75_LVBus1142165_consumption, 75_LVBus1142168_consumption, 75_LVBus1142170_consumption, 75_LVBus1142171_consumption, 75_LVBus1142177_consumption, 75_LVBus1142180_consumption, 75_LVBus1142187_consumption, 75_LVBus1142188_consumption, 75_LVBus1142192_consumption, 75_LVBus1142195_consumption, 75_LVBus1142196_consumption, 75_LVBus1142199_consumption, 75_LVBus1142201_consumption, 75_LVBus1142203_consumption, 75_LVBus1142204_consumption, 75_LVBus1142205_consumption, 75_LVBus1142206_consumption, 75_LVBus1142207_consumption, 75_LVBus1142208_consumption, 75_LVBus1142212_consumption, 75_LVBus1142213_consumption, 75_LVBus1142215_consumption, 75_LVBus1142217_consumption, 75_LVBus1142221_consumption, 75_LVBus1142223_consumption, 75_LVBus1142226_consumption, 75_LVBus1142232_consumption, 75_LVBus1142233_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  156 group(s) of loads (312 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  4 group(s) of series lines (9 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  205 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1142034_production, 75_LVBus1142036_production, 75_LVBus1142038_production, 75_LVBus1142039_production, 75_LVBus1142040_production, 75_LVBus1142041_production, 75_LVBus1142042_production, 75_LVBus1142043_consumption, 75_LVBus1142043_production, 75_LVBus1142044_production, 75_LVBus1142045_production, 75_LVBus1142049_consumption, 75_LVBus1142049_production, 75_LVBus1142050_consumption, 75_LVBus1142050_production, 75_LVBus1142051_production, 75_LVBus1142052_production, 75_LVBus1142054_production, 75_LVBus1142055_production, 75_LVBus1142056_consumption, 75_LVBus1142056_production, 75_LVBus1142057_consumption, 75_LVBus1142057_production, 75_LVBus1142059_consumption, 75_LVBus1142059_production, 75_LVBus1142060_production, 75_LVBus1142062_consumption, 75_LVBus1142062_production, 75_LVBus1142065_production, 75_LVBus1142066_production, 75_LVBus1142067_production, 75_LVBus1142069_production, 75_LVBus1142071_consumption, 75_LVBus1142071_production, 75_LVBus1142072_production, 75_LVBus1142073_consumption, 75_LVBus1142073_production, 75_LVBus1142074_production, 75_LVBus1142075_consumption, 75_LVBus1142075_production, 75_LVBus1142076_production, 75_LVBus1142077_production, 75_LVBus1142078_production, 75_LVBus1142082_consumption, 75_LVBus1142082_production, 75_LVBus1142083_consumption, 75_LVBus1142083_production, 75_LVBus1142084_production, 75_LVBus1142085_consumption, 75_LVBus1142085_production, 75_LVBus1142086_production, 75_LVBus1142087_production, 75_LVBus1142088_production, 75_LVBus1142090_production, 75_LVBus1142091_production, 75_LVBus1142092_production, 75_LVBus1142093_consumption, 75_LVBus1142093_production, 75_LVBus1142094_production, 75_LVBus1142095_production, 75_LVBus1142096_production, 75_LVBus1142098_consumption, 75_LVBus1142098_production, 75_LVBus1142099_production, 75_LVBus1142100_production, 75_LVBus1142101_production, 75_LVBus1142102_production, 75_LVBus1142103_production, 75_LVBus1142104_production, 75_LVBus1142105_production, 75_LVBus1142107_production, 75_LVBus1142108_production, 75_LVBus1142109_production, 75_LVBus1142110_production, 75_LVBus1142111_consumption, 75_LVBus1142111_production, 75_LVBus1142112_production, 75_LVBus1142113_production, 75_LVBus1142115_production, 75_LVBus1142116_consumption, 75_LVBus1142116_production, 75_LVBus1142117_production, 75_LVBus1142119_production, 75_LVBus1142120_production, 75_LVBus1142121_production, 75_LVBus1142122_production, 75_LVBus1142123_consumption, 75_LVBus1142123_production, 75_LVBus1142124_production, 75_LVBus1142125_production, 75_LVBus1142126_production, 75_LVBus1142128_production, 75_LVBus1142129_production, 75_LVBus1142130_production, 75_LVBus1142132_consumption, 75_LVBus1142132_production, 75_LVBus1142134_production, 75_LVBus1142136_consumption, 75_LVBus1142136_production, 75_LVBus1142137_consumption, 75_LVBus1142137_production, 75_LVBus1142138_production, 75_LVBus1142139_consumption, 75_LVBus1142139_production, 75_LVBus1142140_consumption, 75_LVBus1142140_production, 75_LVBus1142141_production, 75_LVBus1142143_production, 75_LVBus1142144_production, 75_LVBus1142145_production, 75_LVBus1142147_consumption, 75_LVBus1142147_production, 75_LVBus1142148_production, 75_LVBus1142149_consumption, 75_LVBus1142149_production, 75_LVBus1142150_production, 75_LVBus1142151_production, 75_LVBus1142153_consumption, 75_LVBus1142153_production, 75_LVBus1142154_production, 75_LVBus1142155_production, 75_LVBus1142157_consumption, 75_LVBus1142157_production, 75_LVBus1142158_production, 75_LVBus1142159_production, 75_LVBus1142160_consumption, 75_LVBus1142160_production, 75_LVBus1142161_production, 75_LVBus1142163_consumption, 75_LVBus1142163_production, 75_LVBus1142164_consumption, 75_LVBus1142164_production, 75_LVBus1142165_production, 75_LVBus1142166_production, 75_LVBus1142167_consumption, 75_LVBus1142167_production, 75_LVBus1142168_production, 75_LVBus1142169_production, 75_LVBus1142170_production, 75_LVBus1142171_production, 75_LVBus1142177_production, 75_LVBus1142178_consumption, 75_LVBus1142178_production, 75_LVBus1142179_consumption, 75_LVBus1142179_production, 75_LVBus1142180_production, 75_LVBus1142182_consumption, 75_LVBus1142182_production, 75_LVBus1142184_production, 75_LVBus1142186_consumption, 75_LVBus1142186_production, 75_LVBus1142187_production, 75_LVBus1142188_production, 75_LVBus1142190_consumption, 75_LVBus1142190_production, 75_LVBus1142191_consumption, 75_LVBus1142191_production, 75_LVBus1142192_production, 75_LVBus1142193_consumption, 75_LVBus1142193_production, 75_LVBus1142195_production, 75_LVBus1142196_production, 75_LVBus1142198_consumption, 75_LVBus1142198_production, 75_LVBus1142199_production, 75_LVBus1142200_consumption, 75_LVBus1142200_production, 75_LVBus1142201_production, 75_LVBus1142203_production, 75_LVBus1142204_production, 75_LVBus1142205_production, 75_LVBus1142206_production, 75_LVBus1142207_production, 75_LVBus1142208_production, 75_LVBus1142209_production, 75_LVBus1142210_consumption, 75_LVBus1142210_production, 75_LVBus1142212_production, 75_LVBus1142213_production, 75_LVBus1142214_production, 75_LVBus1142215_production, 75_LVBus1142216_consumption, 75_LVBus1142216_production, 75_LVBus1142217_production, 75_LVBus1142218_consumption, 75_LVBus1142218_production, 75_LVBus1142219_consumption, 75_LVBus1142219_production, 75_LVBus1142220_consumption, 75_LVBus1142220_production, 75_LVBus1142221_production, 75_LVBus1142223_production, 75_LVBus1142225_production, 75_LVBus1142226_production, 75_LVBus1142228_production, 75_LVBus1142229_consumption, 75_LVBus1142229_production, 75_LVBus1142231_consumption, 75_LVBus1142231_production, 75_LVBus1142232_production, 75_LVBus1142233_production, 75_LVBus1142234_consumption, 75_LVBus1142234_production, 75_MVLV054856_consumption, 75_MVLV054856_production.

