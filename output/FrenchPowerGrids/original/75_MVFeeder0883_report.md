# BMOPF Network Summary: 75_MVFeeder0883

**Generated:** 2026-10-01 23:34:22  
**Findings:** 0 errors · 5 warnings · 245 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 456 |  |
| line | 440 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 848 | 4.454 MW, 1.34 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 15 |  |
| switch | 0 |  |
| transformer | 15 | Dyn11×15 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 19 | 18 | 4 | 0 |
| LV_236V | 236.0 V | 437 | 422 | 844 | 0 |

**Transformer transitions:**

- `75_MVLV107034_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV164438_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV099664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV020927_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV046131_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV027766_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV101416_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV142069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV049433_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV125061_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV171391_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV028925_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV148823_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV154521_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV103669_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 11 |
| Degree-1 buses | 170 |
| Tree depth (max hops) | 28 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 456 | 1 | 455 | 0 | 0 | 0 |
| Tier LV_236V | 437 | 15 | 422 | 0 | 0 | 0 |
| Tier MV_11.8kV | 19 | 1 | 18 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 15; skipped invalid branches: 0.

Galvanic zones: 16; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_BXBRE | MV_11.8kV | 19 | 0 | 0 | 15 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1805 declared bus terminals; 1742 mapped line/closed-switch conductor edges; 63 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 51700.0 | 2.429 | 2544 |
| q_nom | 0.0 | 15500.0 | 2.429 | 2544 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.0 | 2600.0 | 2.442 | 440 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 440000.0 | 1.1e6 | 0.344 | 15 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 568 of 848 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261191_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260900_consumption' has phase imbalance of 57.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260923_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260973_consumption' has phase imbalance of 238.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261026_consumption' has phase imbalance of 162.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261234_consumption' has phase imbalance of 23.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261204_consumption' has phase imbalance of 58.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260824_consumption' has phase imbalance of 50.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260922_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261041_consumption' has phase imbalance of 30.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261230_consumption' has phase imbalance of 96.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261033_consumption' has phase imbalance of 33.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261199_consumption' has phase imbalance of 74.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260972_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260827_consumption' has phase imbalance of 63.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260957_consumption' has phase imbalance of 67.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261182_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261179_consumption' has phase imbalance of 24.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260826_consumption' has phase imbalance of 42.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261236_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261039_consumption' has phase imbalance of 67.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260846_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261263_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261081_consumption' has phase imbalance of 215.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261158_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260976_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260939_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260910_consumption' has phase imbalance of 39.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261118_consumption' has phase imbalance of 98.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261181_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261077_consumption' has phase imbalance of 57.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1952929_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261127_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1946357_consumption' has phase imbalance of 85.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260784_consumption' has phase imbalance of 76.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260967_consumption' has phase imbalance of 58.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261090_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261011_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260931_consumption' has phase imbalance of 76.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261139_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261115_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261082_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261079_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261192_consumption' has phase imbalance of 49.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260895_consumption' has phase imbalance of 29.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261102_consumption' has phase imbalance of 142.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261086_consumption' has phase imbalance of 40.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260942_consumption' has phase imbalance of 35.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260921_consumption' has phase imbalance of 35.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261157_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261104_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260812_consumption' has phase imbalance of 42.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1951677_consumption' has phase imbalance of 73.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261142_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261242_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261208_consumption' has phase imbalance of 55.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261177_consumption' has phase imbalance of 143.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260894_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261187_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260951_consumption' has phase imbalance of 61.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260974_consumption' has phase imbalance of 249.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261151_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260947_consumption' has phase imbalance of 104.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261120_consumption' has phase imbalance of 103.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261109_consumption' has phase imbalance of 43.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260790_consumption' has phase imbalance of 37.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261099_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260983_consumption' has phase imbalance of 22.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261080_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261023_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261028_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260948_consumption' has phase imbalance of 105.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261154_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261257_consumption' has phase imbalance of 177.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260997_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261138_consumption' has phase imbalance of 100.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261017_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261014_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261119_consumption' has phase imbalance of 77.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261045_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261013_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261159_consumption' has phase imbalance of 37.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261233_consumption' has phase imbalance of 21.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261152_consumption' has phase imbalance of 66.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1962031_consumption' has phase imbalance of 63.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260953_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261135_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261006_consumption' has phase imbalance of 86.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260991_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261122_consumption' has phase imbalance of 100.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260981_consumption' has phase imbalance of 69.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260823_consumption' has phase imbalance of 31.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261146_consumption' has phase imbalance of 96.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260774_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261150_consumption' has phase imbalance of 200.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261131_consumption' has phase imbalance of 49.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260851_consumption' has phase imbalance of 62.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261176_consumption' has phase imbalance of 79.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261203_consumption' has phase imbalance of 43.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261214_consumption' has phase imbalance of 129.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260791_consumption' has phase imbalance of 65.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261002_consumption' has phase imbalance of 142.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261170_consumption' has phase imbalance of 41.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261100_consumption' has phase imbalance of 110.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1934313_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1934319_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261136_consumption' has phase imbalance of 112.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260848_consumption' has phase imbalance of 34.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261132_consumption' has phase imbalance of 73.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261149_consumption' has phase imbalance of 81.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261009_consumption' has phase imbalance of 86.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260838_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261232_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261195_consumption' has phase imbalance of 48.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260793_consumption' has phase imbalance of 93.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260803_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1952930_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261056_consumption' has phase imbalance of 93.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260892_consumption' has phase imbalance of 196.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1934316_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261075_consumption' has phase imbalance of 40.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1934317_consumption' has phase imbalance of 94.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261143_consumption' has phase imbalance of 232.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260920_consumption' has phase imbalance of 124.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261101_consumption' has phase imbalance of 99.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261065_consumption' has phase imbalance of 94.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260935_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261004_consumption' has phase imbalance of 101.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260883_consumption' has phase imbalance of 39.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260788_consumption' has phase imbalance of 40.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261210_consumption' has phase imbalance of 43.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261129_consumption' has phase imbalance of 248.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260966_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261070_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261244_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260993_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260914_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261193_consumption' has phase imbalance of 131.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261046_consumption' has phase imbalance of 120.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260919_consumption' has phase imbalance of 92.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261178_consumption' has phase imbalance of 79.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261107_consumption' has phase imbalance of 61.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1963701_consumption' has phase imbalance of 250.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261180_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260778_consumption' has phase imbalance of 39.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260906_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260825_consumption' has phase imbalance of 275.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260907_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260969_consumption' has phase imbalance of 55.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260970_consumption' has phase imbalance of 42.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261246_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261059_consumption' has phase imbalance of 60.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260834_consumption' has phase imbalance of 34.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261198_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260904_consumption' has phase imbalance of 112.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261202_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261098_consumption' has phase imbalance of 108.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260996_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261038_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261114_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260941_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261054_consumption' has phase imbalance of 46.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261144_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261016_consumption' has phase imbalance of 53.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261012_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261218_consumption' has phase imbalance of 31.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261060_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260937_consumption' has phase imbalance of 93.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1952927_consumption' has phase imbalance of 23.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261130_consumption' has phase imbalance of 30.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261125_consumption' has phase imbalance of 37.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261072_consumption' has phase imbalance of 266.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261153_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260968_consumption' has phase imbalance of 38.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1934315_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261137_consumption' has phase imbalance of 54.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261035_consumption' has phase imbalance of 121.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260965_consumption' has phase imbalance of 149.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261112_consumption' has phase imbalance of 257.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261205_consumption' has phase imbalance of 202.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261103_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260971_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261110_consumption' has phase imbalance of 110.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261018_consumption' has phase imbalance of 75.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260829_consumption' has phase imbalance of 35.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260884_consumption' has phase imbalance of 146.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261078_consumption' has phase imbalance of 143.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261124_consumption' has phase imbalance of 86.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261037_consumption' has phase imbalance of 96.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260817_consumption' has phase imbalance of 53.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261231_consumption' has phase imbalance of 38.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260849_consumption' has phase imbalance of 215.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261106_consumption' has phase imbalance of 189.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261029_consumption' has phase imbalance of 40.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260898_consumption' has phase imbalance of 61.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1934314_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261209_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260938_consumption' has phase imbalance of 89.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260944_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261156_consumption' has phase imbalance of 73.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261074_consumption' has phase imbalance of 112.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260992_consumption' has phase imbalance of 103.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260893_consumption' has phase imbalance of 31.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260912_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260961_consumption' has phase imbalance of 57.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1951676_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261105_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261155_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261121_consumption' has phase imbalance of 49.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261042_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261247_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261094_consumption' has phase imbalance of 217.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261253_consumption' has phase imbalance of 139.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260977_consumption' has phase imbalance of 25.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260830_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0260975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0261251_consumption' has phase imbalance of 87.7%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 848 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0260910' has balanced aggregate load across 3 phase(s) (max spread 1.93%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.454 MW |
| Total load Q | 1.34 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV107034_Transformer | 440.0 kVA | 16.6% |
| 75_MVLV164438_Transformer | 693.0 kVA | 49.4% |
| 75_MVLV099664_Transformer | 693.0 kVA | 35.2% |
| 75_MVLV020927_Transformer | 693.0 kVA | 36.5% |
| 75_MVLV046131_Transformer | 1.1 MVA | 56.5% |
| 75_MVLV027766_Transformer | 693.0 kVA | 38.3% |
| 75_MVLV101416_Transformer | 693.0 kVA | 47.5% |
| 75_MVLV142069_Transformer | 693.0 kVA | 40.3% |
| 75_MVLV049433_Transformer | 1.1 MVA | 45.4% |
| 75_MVLV125061_Transformer | 1.1 MVA | 43.7% |
| 75_MVLV171391_Transformer | 440.0 kVA | 37.1% |
| 75_MVLV028925_Transformer | 440.0 kVA | 22.9% |
| 75_MVLV148823_Transformer | 440.0 kVA | 33.8% |
| 75_MVLV154521_Transformer | 693.0 kVA | 44.8% |
| 75_MVLV103669_Transformer | 1.1 MVA | 49.1% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.45 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 456 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 456 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 19 |
| LV_236V | 4-wire | 437 / 437 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 437 |
| Neutral branches | 422 |
| Grounding points | 15 |
| Neutral sections | 15 |
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
| 11.78 kV | 19 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 63 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 60 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 16 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1100.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 437 / 19 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 569 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 569 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0260764_consumption, 75_LVBus0260764_production, 75_LVBus0260766_consumption, 75_LVBus0260766_production, 75_LVBus0260767_consumption, 75_LVBus0260767_production, 75_LVBus0260768_consumption, 75_LVBus0260768_production, 75_LVBus0260769_consumption, 75_LVBus0260769_production, 75_LVBus0260770_consumption, 75_LVBus0260770_production, 75_LVBus0260771_consumption, 75_LVBus0260771_production, 75_LVBus0260772_consumption, 75_LVBus0260772_production, 75_LVBus0260773_consumption, 75_LVBus0260773_production, 75_LVBus0260774_production, 75_LVBus0260775_consumption, 75_LVBus0260775_production, 75_LVBus0260777_consumption, 75_LVBus0260777_production, 75_LVBus0260778_production, 75_LVBus0260779_consumption, 75_LVBus0260779_production, 75_LVBus0260780_consumption, 75_LVBus0260780_production, 75_LVBus0260781_consumption, 75_LVBus0260781_production, 75_LVBus0260782_consumption, 75_LVBus0260782_production, 75_LVBus0260783_consumption, 75_LVBus0260783_production, 75_LVBus0260784_production, 75_LVBus0260785_consumption, 75_LVBus0260785_production, 75_LVBus0260786_production, 75_LVBus0260788_production, 75_LVBus0260790_production, 75_LVBus0260791_production, 75_LVBus0260793_production, 75_LVBus0260795_consumption, 75_LVBus0260795_production, 75_LVBus0260796_consumption, 75_LVBus0260796_production, 75_LVBus0260797_consumption, 75_LVBus0260797_production, 75_LVBus0260798_consumption, 75_LVBus0260798_production, 75_LVBus0260799_consumption, 75_LVBus0260799_production, 75_LVBus0260800_consumption, 75_LVBus0260800_production, 75_LVBus0260801_consumption, 75_LVBus0260801_production, 75_LVBus0260802_production, 75_LVBus0260803_production, 75_LVBus0260804_consumption, 75_LVBus0260804_production, 75_LVBus0260805_consumption, 75_LVBus0260805_production, 75_LVBus0260807_consumption, 75_LVBus0260807_production, 75_LVBus0260808_consumption, 75_LVBus0260808_production, 75_LVBus0260809_consumption, 75_LVBus0260809_production, 75_LVBus0260810_consumption, 75_LVBus0260810_production, 75_LVBus0260811_consumption, 75_LVBus0260811_production, 75_LVBus0260812_production, 75_LVBus0260813_consumption, 75_LVBus0260813_production, 75_LVBus0260815_consumption, 75_LVBus0260815_production, 75_LVBus0260817_production, 75_LVBus0260819_production, 75_LVBus0260821_production, 75_LVBus0260823_production, 75_LVBus0260824_production, 75_LVBus0260825_production, 75_LVBus0260826_production, 75_LVBus0260827_production, 75_LVBus0260828_production, 75_LVBus0260829_production, 75_LVBus0260830_production, 75_LVBus0260831_consumption, 75_LVBus0260831_production, 75_LVBus0260832_production, 75_LVBus0260834_production, 75_LVBus0260836_consumption, 75_LVBus0260836_production, 75_LVBus0260838_production, 75_LVBus0260840_consumption, 75_LVBus0260840_production, 75_LVBus0260842_production, 75_LVBus0260844_consumption, 75_LVBus0260844_production, 75_LVBus0260846_production, 75_LVBus0260847_consumption, 75_LVBus0260847_production, 75_LVBus0260848_production, 75_LVBus0260849_production, 75_LVBus0260850_production, 75_LVBus0260851_production, 75_LVBus0260852_production, 75_LVBus0260853_consumption, 75_LVBus0260853_production, 75_LVBus0260854_production, 75_LVBus0260855_consumption, 75_LVBus0260855_production, 75_LVBus0260856_consumption, 75_LVBus0260856_production, 75_LVBus0260857_consumption, 75_LVBus0260857_production, 75_LVBus0260858_consumption, 75_LVBus0260858_production, 75_LVBus0260859_consumption, 75_LVBus0260859_production, 75_LVBus0260860_consumption, 75_LVBus0260860_production, 75_LVBus0260861_production, 75_LVBus0260862_consumption, 75_LVBus0260862_production, 75_LVBus0260863_production, 75_LVBus0260864_consumption, 75_LVBus0260864_production, 75_LVBus0260865_consumption, 75_LVBus0260865_production, 75_LVBus0260866_consumption, 75_LVBus0260866_production, 75_LVBus0260867_consumption, 75_LVBus0260867_production, 75_LVBus0260869_production, 75_LVBus0260870_production, 75_LVBus0260871_consumption, 75_LVBus0260871_production, 75_LVBus0260873_consumption, 75_LVBus0260873_production, 75_LVBus0260874_consumption, 75_LVBus0260874_production, 75_LVBus0260875_production, 75_LVBus0260876_consumption, 75_LVBus0260876_production, 75_LVBus0260878_consumption, 75_LVBus0260878_production, 75_LVBus0260879_consumption, 75_LVBus0260879_production, 75_LVBus0260880_production, 75_LVBus0260882_consumption, 75_LVBus0260882_production, 75_LVBus0260883_production, 75_LVBus0260884_production, 75_LVBus0260885_production, 75_LVBus0260887_consumption, 75_LVBus0260887_production, 75_LVBus0260888_consumption, 75_LVBus0260888_production, 75_LVBus0260889_consumption, 75_LVBus0260889_production, 75_LVBus0260890_production, 75_LVBus0260891_production, 75_LVBus0260892_production, 75_LVBus0260893_production, 75_LVBus0260894_production, 75_LVBus0260895_production, 75_LVBus0260896_production, 75_LVBus0260897_consumption, 75_LVBus0260897_production, 75_LVBus0260898_production, 75_LVBus0260900_production, 75_LVBus0260902_consumption, 75_LVBus0260902_production, 75_LVBus0260904_production, 75_LVBus0260905_consumption, 75_LVBus0260905_production, 75_LVBus0260906_production, 75_LVBus0260907_production, 75_LVBus0260910_production, 75_LVBus0260912_production, 75_LVBus0260914_production, 75_LVBus0260915_consumption, 75_LVBus0260915_production, 75_LVBus0260916_production, 75_LVBus0260917_production, 75_LVBus0260919_production, 75_LVBus0260920_production, 75_LVBus0260921_production, 75_LVBus0260922_production, 75_LVBus0260923_production, 75_LVBus0260925_consumption, 75_LVBus0260925_production, 75_LVBus0260926_production, 75_LVBus0260927_consumption, 75_LVBus0260927_production, 75_LVBus0260928_consumption, 75_LVBus0260928_production, 75_LVBus0260929_consumption, 75_LVBus0260929_production, 75_LVBus0260930_consumption, 75_LVBus0260930_production, 75_LVBus0260931_production, 75_LVBus0260932_consumption, 75_LVBus0260932_production, 75_LVBus0260933_consumption, 75_LVBus0260933_production, 75_LVBus0260934_consumption, 75_LVBus0260934_production, 75_LVBus0260935_production, 75_LVBus0260937_production, 75_LVBus0260938_production, 75_LVBus0260939_production, 75_LVBus0260940_consumption, 75_LVBus0260940_production, 75_LVBus0260941_production, 75_LVBus0260942_production, 75_LVBus0260943_production, 75_LVBus0260944_production, 75_LVBus0260945_production, 75_LVBus0260947_production, 75_LVBus0260948_production, 75_LVBus0260950_consumption, 75_LVBus0260950_production, 75_LVBus0260951_production, 75_LVBus0260952_production, 75_LVBus0260953_production, 75_LVBus0260954_consumption, 75_LVBus0260954_production, 75_LVBus0260956_consumption, 75_LVBus0260956_production, 75_LVBus0260957_production, 75_LVBus0260959_production, 75_LVBus0260961_production, 75_LVBus0260962_production, 75_LVBus0260963_consumption, 75_LVBus0260963_production, 75_LVBus0260965_production, 75_LVBus0260966_production, 75_LVBus0260967_production, 75_LVBus0260968_production, 75_LVBus0260969_production, 75_LVBus0260970_production, 75_LVBus0260971_production, 75_LVBus0260972_production, 75_LVBus0260973_production, 75_LVBus0260974_production, 75_LVBus0260975_production, 75_LVBus0260976_production, 75_LVBus0260977_production, 75_LVBus0260979_consumption, 75_LVBus0260979_production, 75_LVBus0260981_production, 75_LVBus0260983_production, 75_LVBus0260984_consumption, 75_LVBus0260984_production, 75_LVBus0260985_consumption, 75_LVBus0260985_production, 75_LVBus0260987_consumption, 75_LVBus0260987_production, 75_LVBus0260988_consumption, 75_LVBus0260988_production, 75_LVBus0260989_consumption, 75_LVBus0260989_production, 75_LVBus0260990_consumption, 75_LVBus0260990_production, 75_LVBus0260991_production, 75_LVBus0260992_production, 75_LVBus0260993_production, 75_LVBus0260994_consumption, 75_LVBus0260994_production, 75_LVBus0260995_consumption, 75_LVBus0260995_production, 75_LVBus0260996_production, 75_LVBus0260997_production, 75_LVBus0260998_consumption, 75_LVBus0260998_production, 75_LVBus0260999_production, 75_LVBus0261001_consumption, 75_LVBus0261001_production, 75_LVBus0261002_production, 75_LVBus0261004_production, 75_LVBus0261006_production, 75_LVBus0261008_consumption, 75_LVBus0261008_production, 75_LVBus0261009_production, 75_LVBus0261011_production, 75_LVBus0261012_production, 75_LVBus0261013_production, 75_LVBus0261014_production, 75_LVBus0261015_consumption, 75_LVBus0261015_production, 75_LVBus0261016_production, 75_LVBus0261017_production, 75_LVBus0261018_production, 75_LVBus0261020_production, 75_LVBus0261021_production, 75_LVBus0261023_production, 75_LVBus0261025_consumption, 75_LVBus0261025_production, 75_LVBus0261026_production, 75_LVBus0261027_production, 75_LVBus0261028_production, 75_LVBus0261029_production, 75_LVBus0261031_consumption, 75_LVBus0261031_production, 75_LVBus0261032_production, 75_LVBus0261033_production, 75_LVBus0261035_production, 75_LVBus0261036_consumption, 75_LVBus0261036_production, 75_LVBus0261037_production, 75_LVBus0261038_production, 75_LVBus0261039_production, 75_LVBus0261040_consumption, 75_LVBus0261040_production, 75_LVBus0261041_production, 75_LVBus0261042_production, 75_LVBus0261044_consumption, 75_LVBus0261044_production, 75_LVBus0261045_production, 75_LVBus0261046_production, 75_LVBus0261047_production, 75_LVBus0261049_production, 75_LVBus0261050_production, 75_LVBus0261052_consumption, 75_LVBus0261052_production, 75_LVBus0261053_consumption, 75_LVBus0261053_production, 75_LVBus0261054_production, 75_LVBus0261055_consumption, 75_LVBus0261055_production, 75_LVBus0261056_production, 75_LVBus0261058_consumption, 75_LVBus0261058_production, 75_LVBus0261059_production, 75_LVBus0261060_production, 75_LVBus0261062_consumption, 75_LVBus0261062_production, 75_LVBus0261063_consumption, 75_LVBus0261063_production, 75_LVBus0261065_production, 75_LVBus0261066_consumption, 75_LVBus0261066_production, 75_LVBus0261067_production, 75_LVBus0261069_consumption, 75_LVBus0261069_production, 75_LVBus0261070_production, 75_LVBus0261072_production, 75_LVBus0261073_production, 75_LVBus0261074_production, 75_LVBus0261075_production, 75_LVBus0261076_consumption, 75_LVBus0261076_production, 75_LVBus0261077_production, 75_LVBus0261078_production, 75_LVBus0261079_production, 75_LVBus0261080_production, 75_LVBus0261081_production, 75_LVBus0261082_production, 75_LVBus0261083_production, 75_LVBus0261084_consumption, 75_LVBus0261084_production, 75_LVBus0261086_production, 75_LVBus0261088_consumption, 75_LVBus0261088_production, 75_LVBus0261089_production, 75_LVBus0261090_production, 75_LVBus0261092_production, 75_LVBus0261093_consumption, 75_LVBus0261093_production, 75_LVBus0261094_production, 75_LVBus0261095_consumption, 75_LVBus0261095_production, 75_LVBus0261097_production, 75_LVBus0261098_production, 75_LVBus0261099_production, 75_LVBus0261100_production, 75_LVBus0261101_production, 75_LVBus0261102_production, 75_LVBus0261103_production, 75_LVBus0261104_production, 75_LVBus0261105_production, 75_LVBus0261106_production, 75_LVBus0261107_production, 75_LVBus0261108_consumption, 75_LVBus0261108_production, 75_LVBus0261109_production, 75_LVBus0261110_production, 75_LVBus0261112_production, 75_LVBus0261114_production, 75_LVBus0261115_production, 75_LVBus0261116_consumption, 75_LVBus0261116_production, 75_LVBus0261117_consumption, 75_LVBus0261117_production, 75_LVBus0261118_production, 75_LVBus0261119_production, 75_LVBus0261120_production, 75_LVBus0261121_production, 75_LVBus0261122_production, 75_LVBus0261124_production, 75_LVBus0261125_production, 75_LVBus0261127_production, 75_LVBus0261128_consumption, 75_LVBus0261128_production, 75_LVBus0261129_production, 75_LVBus0261130_production, 75_LVBus0261131_production, 75_LVBus0261132_production, 75_LVBus0261133_production, 75_LVBus0261134_production, 75_LVBus0261135_production, 75_LVBus0261136_production, 75_LVBus0261137_production, 75_LVBus0261138_production, 75_LVBus0261139_production, 75_LVBus0261141_production, 75_LVBus0261142_production, 75_LVBus0261143_production, 75_LVBus0261144_production, 75_LVBus0261146_production, 75_LVBus0261148_consumption, 75_LVBus0261148_production, 75_LVBus0261149_production, 75_LVBus0261150_production, 75_LVBus0261151_production, 75_LVBus0261152_production, 75_LVBus0261153_production, 75_LVBus0261154_production, 75_LVBus0261155_production, 75_LVBus0261156_production, 75_LVBus0261157_production, 75_LVBus0261158_production, 75_LVBus0261159_production, 75_LVBus0261160_production, 75_LVBus0261170_production, 75_LVBus0261172_consumption, 75_LVBus0261172_production, 75_LVBus0261173_consumption, 75_LVBus0261173_production, 75_LVBus0261174_consumption, 75_LVBus0261174_production, 75_LVBus0261175_production, 75_LVBus0261176_production, 75_LVBus0261177_production, 75_LVBus0261178_production, 75_LVBus0261179_production, 75_LVBus0261180_production, 75_LVBus0261181_production, 75_LVBus0261182_production, 75_LVBus0261184_consumption, 75_LVBus0261184_production, 75_LVBus0261187_production, 75_LVBus0261188_production, 75_LVBus0261189_production, 75_LVBus0261190_consumption, 75_LVBus0261190_production, 75_LVBus0261191_production, 75_LVBus0261192_production, 75_LVBus0261193_production, 75_LVBus0261194_production, 75_LVBus0261195_production, 75_LVBus0261197_consumption, 75_LVBus0261197_production, 75_LVBus0261198_production, 75_LVBus0261199_production, 75_LVBus0261201_consumption, 75_LVBus0261201_production, 75_LVBus0261202_production, 75_LVBus0261203_production, 75_LVBus0261204_production, 75_LVBus0261205_production, 75_LVBus0261206_production, 75_LVBus0261207_consumption, 75_LVBus0261207_production, 75_LVBus0261208_production, 75_LVBus0261209_production, 75_LVBus0261210_production, 75_LVBus0261212_consumption, 75_LVBus0261212_production, 75_LVBus0261213_consumption, 75_LVBus0261213_production, 75_LVBus0261214_production, 75_LVBus0261216_production, 75_LVBus0261218_production, 75_LVBus0261222_production, 75_LVBus0261224_consumption, 75_LVBus0261224_production, 75_LVBus0261226_consumption, 75_LVBus0261226_production, 75_LVBus0261228_consumption, 75_LVBus0261228_production, 75_LVBus0261230_production, 75_LVBus0261231_production, 75_LVBus0261232_production, 75_LVBus0261233_production, 75_LVBus0261234_production, 75_LVBus0261235_consumption, 75_LVBus0261235_production, 75_LVBus0261236_production, 75_LVBus0261237_consumption, 75_LVBus0261237_production, 75_LVBus0261239_consumption, 75_LVBus0261239_production, 75_LVBus0261241_production, 75_LVBus0261242_production, 75_LVBus0261244_production, 75_LVBus0261246_production, 75_LVBus0261247_production, 75_LVBus0261248_consumption, 75_LVBus0261248_production, 75_LVBus0261249_consumption, 75_LVBus0261249_production, 75_LVBus0261251_production, 75_LVBus0261253_production, 75_LVBus0261254_consumption, 75_LVBus0261254_production, 75_LVBus0261255_consumption, 75_LVBus0261255_production, 75_LVBus0261256_production, 75_LVBus0261257_production, 75_LVBus0261258_production, 75_LVBus0261261_production, 75_LVBus0261263_production, 75_LVBus0261267_consumption, 75_LVBus0261267_production, 75_LVBus0261269_production, 75_LVBus1934312_consumption, 75_LVBus1934312_production, 75_LVBus1934313_production, 75_LVBus1934314_production, 75_LVBus1934315_production, 75_LVBus1934316_production, 75_LVBus1934317_production, 75_LVBus1934318_consumption, 75_LVBus1934318_production, 75_LVBus1934319_production, 75_LVBus1946357_production, 75_LVBus1946358_production, 75_LVBus1946359_consumption, 75_LVBus1946359_production, 75_LVBus1951676_production, 75_LVBus1951677_production, 75_LVBus1951678_production, 75_LVBus1952927_production, 75_LVBus1952928_consumption, 75_LVBus1952928_production, 75_LVBus1952929_production, 75_LVBus1952930_production, 75_LVBus1960488_production, 75_LVBus1960489_consumption, 75_LVBus1960489_production, 75_LVBus1960490_consumption, 75_LVBus1960490_production, 75_LVBus1962030_consumption, 75_LVBus1962030_production, 75_LVBus1962031_production, 75_LVBus1962032_consumption, 75_LVBus1962032_production, 75_LVBus1962033_production, 75_LVBus1962034_consumption, 75_LVBus1962034_production, 75_LVBus1963701_production, 75_MVLV107233_consumption, 75_MVLV107233_production, 75_MVLV143218_consumption, 75_MVLV143218_production.

## 9. Data Quality Summary

**Total findings:** 250 (0 errors, 5 warnings, 245 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  568 of 848 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.45 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  569 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261191_consumption`  
  Load '75_LVBus0261191_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260900_consumption`  
  Load '75_LVBus0260900_consumption' has phase imbalance of 57.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260923_consumption`  
  Load '75_LVBus0260923_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260973_consumption`  
  Load '75_LVBus0260973_consumption' has phase imbalance of 238.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261133_consumption`  
  Load '75_LVBus0261133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261026_consumption`  
  Load '75_LVBus0261026_consumption' has phase imbalance of 162.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261234_consumption`  
  Load '75_LVBus0261234_consumption' has phase imbalance of 23.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261204_consumption`  
  Load '75_LVBus0261204_consumption' has phase imbalance of 58.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260824_consumption`  
  Load '75_LVBus0260824_consumption' has phase imbalance of 50.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260922_consumption`  
  Load '75_LVBus0260922_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261041_consumption`  
  Load '75_LVBus0261041_consumption' has phase imbalance of 30.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261230_consumption`  
  Load '75_LVBus0261230_consumption' has phase imbalance of 96.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261033_consumption`  
  Load '75_LVBus0261033_consumption' has phase imbalance of 33.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261199_consumption`  
  Load '75_LVBus0261199_consumption' has phase imbalance of 74.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260972_consumption`  
  Load '75_LVBus0260972_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260952_consumption`  
  Load '75_LVBus0260952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260827_consumption`  
  Load '75_LVBus0260827_consumption' has phase imbalance of 63.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260957_consumption`  
  Load '75_LVBus0260957_consumption' has phase imbalance of 67.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261182_consumption`  
  Load '75_LVBus0261182_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261179_consumption`  
  Load '75_LVBus0261179_consumption' has phase imbalance of 24.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261073_consumption`  
  Load '75_LVBus0261073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260826_consumption`  
  Load '75_LVBus0260826_consumption' has phase imbalance of 42.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261236_consumption`  
  Load '75_LVBus0261236_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261039_consumption`  
  Load '75_LVBus0261039_consumption' has phase imbalance of 67.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260846_consumption`  
  Load '75_LVBus0260846_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261263_consumption`  
  Load '75_LVBus0261263_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261081_consumption`  
  Load '75_LVBus0261081_consumption' has phase imbalance of 215.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261158_consumption`  
  Load '75_LVBus0261158_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260976_consumption`  
  Load '75_LVBus0260976_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260939_consumption`  
  Load '75_LVBus0260939_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260910_consumption`  
  Load '75_LVBus0260910_consumption' has phase imbalance of 39.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261118_consumption`  
  Load '75_LVBus0261118_consumption' has phase imbalance of 98.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261181_consumption`  
  Load '75_LVBus0261181_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261077_consumption`  
  Load '75_LVBus0261077_consumption' has phase imbalance of 57.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1952929_consumption`  
  Load '75_LVBus1952929_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261127_consumption`  
  Load '75_LVBus0261127_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1946357_consumption`  
  Load '75_LVBus1946357_consumption' has phase imbalance of 85.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260784_consumption`  
  Load '75_LVBus0260784_consumption' has phase imbalance of 76.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260967_consumption`  
  Load '75_LVBus0260967_consumption' has phase imbalance of 58.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261090_consumption`  
  Load '75_LVBus0261090_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261011_consumption`  
  Load '75_LVBus0261011_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260891_consumption`  
  Load '75_LVBus0260891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260931_consumption`  
  Load '75_LVBus0260931_consumption' has phase imbalance of 76.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261139_consumption`  
  Load '75_LVBus0261139_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261115_consumption`  
  Load '75_LVBus0261115_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261082_consumption`  
  Load '75_LVBus0261082_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261079_consumption`  
  Load '75_LVBus0261079_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261192_consumption`  
  Load '75_LVBus0261192_consumption' has phase imbalance of 49.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260895_consumption`  
  Load '75_LVBus0260895_consumption' has phase imbalance of 29.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261102_consumption`  
  Load '75_LVBus0261102_consumption' has phase imbalance of 142.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261086_consumption`  
  Load '75_LVBus0261086_consumption' has phase imbalance of 40.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260942_consumption`  
  Load '75_LVBus0260942_consumption' has phase imbalance of 35.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260921_consumption`  
  Load '75_LVBus0260921_consumption' has phase imbalance of 35.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261157_consumption`  
  Load '75_LVBus0261157_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261104_consumption`  
  Load '75_LVBus0261104_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260812_consumption`  
  Load '75_LVBus0260812_consumption' has phase imbalance of 42.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1951677_consumption`  
  Load '75_LVBus1951677_consumption' has phase imbalance of 73.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261142_consumption`  
  Load '75_LVBus0261142_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261242_consumption`  
  Load '75_LVBus0261242_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261208_consumption`  
  Load '75_LVBus0261208_consumption' has phase imbalance of 55.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261177_consumption`  
  Load '75_LVBus0261177_consumption' has phase imbalance of 143.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260894_consumption`  
  Load '75_LVBus0260894_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261187_consumption`  
  Load '75_LVBus0261187_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260951_consumption`  
  Load '75_LVBus0260951_consumption' has phase imbalance of 61.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260974_consumption`  
  Load '75_LVBus0260974_consumption' has phase imbalance of 249.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261151_consumption`  
  Load '75_LVBus0261151_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260947_consumption`  
  Load '75_LVBus0260947_consumption' has phase imbalance of 104.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261120_consumption`  
  Load '75_LVBus0261120_consumption' has phase imbalance of 103.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261109_consumption`  
  Load '75_LVBus0261109_consumption' has phase imbalance of 43.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260790_consumption`  
  Load '75_LVBus0260790_consumption' has phase imbalance of 37.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261099_consumption`  
  Load '75_LVBus0261099_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260983_consumption`  
  Load '75_LVBus0260983_consumption' has phase imbalance of 22.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261080_consumption`  
  Load '75_LVBus0261080_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261023_consumption`  
  Load '75_LVBus0261023_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261028_consumption`  
  Load '75_LVBus0261028_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260948_consumption`  
  Load '75_LVBus0260948_consumption' has phase imbalance of 105.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260786_consumption`  
  Load '75_LVBus0260786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261154_consumption`  
  Load '75_LVBus0261154_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261257_consumption`  
  Load '75_LVBus0261257_consumption' has phase imbalance of 177.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260997_consumption`  
  Load '75_LVBus0260997_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261138_consumption`  
  Load '75_LVBus0261138_consumption' has phase imbalance of 100.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261017_consumption`  
  Load '75_LVBus0261017_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261014_consumption`  
  Load '75_LVBus0261014_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261119_consumption`  
  Load '75_LVBus0261119_consumption' has phase imbalance of 77.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261141_consumption`  
  Load '75_LVBus0261141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261045_consumption`  
  Load '75_LVBus0261045_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261013_consumption`  
  Load '75_LVBus0261013_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261159_consumption`  
  Load '75_LVBus0261159_consumption' has phase imbalance of 37.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261233_consumption`  
  Load '75_LVBus0261233_consumption' has phase imbalance of 21.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261152_consumption`  
  Load '75_LVBus0261152_consumption' has phase imbalance of 66.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1962031_consumption`  
  Load '75_LVBus1962031_consumption' has phase imbalance of 63.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261206_consumption`  
  Load '75_LVBus0261206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260953_consumption`  
  Load '75_LVBus0260953_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261135_consumption`  
  Load '75_LVBus0261135_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261006_consumption`  
  Load '75_LVBus0261006_consumption' has phase imbalance of 86.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260991_consumption`  
  Load '75_LVBus0260991_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261122_consumption`  
  Load '75_LVBus0261122_consumption' has phase imbalance of 100.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260981_consumption`  
  Load '75_LVBus0260981_consumption' has phase imbalance of 69.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260823_consumption`  
  Load '75_LVBus0260823_consumption' has phase imbalance of 31.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261146_consumption`  
  Load '75_LVBus0261146_consumption' has phase imbalance of 96.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260774_consumption`  
  Load '75_LVBus0260774_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261150_consumption`  
  Load '75_LVBus0261150_consumption' has phase imbalance of 200.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261131_consumption`  
  Load '75_LVBus0261131_consumption' has phase imbalance of 49.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260851_consumption`  
  Load '75_LVBus0260851_consumption' has phase imbalance of 62.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261176_consumption`  
  Load '75_LVBus0261176_consumption' has phase imbalance of 79.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261203_consumption`  
  Load '75_LVBus0261203_consumption' has phase imbalance of 43.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261214_consumption`  
  Load '75_LVBus0261214_consumption' has phase imbalance of 129.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260791_consumption`  
  Load '75_LVBus0260791_consumption' has phase imbalance of 65.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261002_consumption`  
  Load '75_LVBus0261002_consumption' has phase imbalance of 142.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261170_consumption`  
  Load '75_LVBus0261170_consumption' has phase imbalance of 41.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261100_consumption`  
  Load '75_LVBus0261100_consumption' has phase imbalance of 110.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1934313_consumption`  
  Load '75_LVBus1934313_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1934319_consumption`  
  Load '75_LVBus1934319_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261136_consumption`  
  Load '75_LVBus0261136_consumption' has phase imbalance of 112.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260848_consumption`  
  Load '75_LVBus0260848_consumption' has phase imbalance of 34.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261132_consumption`  
  Load '75_LVBus0261132_consumption' has phase imbalance of 73.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261149_consumption`  
  Load '75_LVBus0261149_consumption' has phase imbalance of 81.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261009_consumption`  
  Load '75_LVBus0261009_consumption' has phase imbalance of 86.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260838_consumption`  
  Load '75_LVBus0260838_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261232_consumption`  
  Load '75_LVBus0261232_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261195_consumption`  
  Load '75_LVBus0261195_consumption' has phase imbalance of 48.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260793_consumption`  
  Load '75_LVBus0260793_consumption' has phase imbalance of 93.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260803_consumption`  
  Load '75_LVBus0260803_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1952930_consumption`  
  Load '75_LVBus1952930_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261056_consumption`  
  Load '75_LVBus0261056_consumption' has phase imbalance of 93.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260892_consumption`  
  Load '75_LVBus0260892_consumption' has phase imbalance of 196.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1934316_consumption`  
  Load '75_LVBus1934316_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261075_consumption`  
  Load '75_LVBus0261075_consumption' has phase imbalance of 40.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1934317_consumption`  
  Load '75_LVBus1934317_consumption' has phase imbalance of 94.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261143_consumption`  
  Load '75_LVBus0261143_consumption' has phase imbalance of 232.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260920_consumption`  
  Load '75_LVBus0260920_consumption' has phase imbalance of 124.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261101_consumption`  
  Load '75_LVBus0261101_consumption' has phase imbalance of 99.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261065_consumption`  
  Load '75_LVBus0261065_consumption' has phase imbalance of 94.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260935_consumption`  
  Load '75_LVBus0260935_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261004_consumption`  
  Load '75_LVBus0261004_consumption' has phase imbalance of 101.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260883_consumption`  
  Load '75_LVBus0260883_consumption' has phase imbalance of 39.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260788_consumption`  
  Load '75_LVBus0260788_consumption' has phase imbalance of 40.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261210_consumption`  
  Load '75_LVBus0261210_consumption' has phase imbalance of 43.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261129_consumption`  
  Load '75_LVBus0261129_consumption' has phase imbalance of 248.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260966_consumption`  
  Load '75_LVBus0260966_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261070_consumption`  
  Load '75_LVBus0261070_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261244_consumption`  
  Load '75_LVBus0261244_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260993_consumption`  
  Load '75_LVBus0260993_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260914_consumption`  
  Load '75_LVBus0260914_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261193_consumption`  
  Load '75_LVBus0261193_consumption' has phase imbalance of 131.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261046_consumption`  
  Load '75_LVBus0261046_consumption' has phase imbalance of 120.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260919_consumption`  
  Load '75_LVBus0260919_consumption' has phase imbalance of 92.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261178_consumption`  
  Load '75_LVBus0261178_consumption' has phase imbalance of 79.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261107_consumption`  
  Load '75_LVBus0261107_consumption' has phase imbalance of 61.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1963701_consumption`  
  Load '75_LVBus1963701_consumption' has phase imbalance of 250.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261180_consumption`  
  Load '75_LVBus0261180_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260778_consumption`  
  Load '75_LVBus0260778_consumption' has phase imbalance of 39.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260906_consumption`  
  Load '75_LVBus0260906_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260825_consumption`  
  Load '75_LVBus0260825_consumption' has phase imbalance of 275.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260907_consumption`  
  Load '75_LVBus0260907_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260969_consumption`  
  Load '75_LVBus0260969_consumption' has phase imbalance of 55.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260970_consumption`  
  Load '75_LVBus0260970_consumption' has phase imbalance of 42.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261246_consumption`  
  Load '75_LVBus0261246_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261059_consumption`  
  Load '75_LVBus0261059_consumption' has phase imbalance of 60.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260834_consumption`  
  Load '75_LVBus0260834_consumption' has phase imbalance of 34.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261198_consumption`  
  Load '75_LVBus0261198_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260904_consumption`  
  Load '75_LVBus0260904_consumption' has phase imbalance of 112.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261202_consumption`  
  Load '75_LVBus0261202_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261098_consumption`  
  Load '75_LVBus0261098_consumption' has phase imbalance of 108.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261083_consumption`  
  Load '75_LVBus0261083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260996_consumption`  
  Load '75_LVBus0260996_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261038_consumption`  
  Load '75_LVBus0261038_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261114_consumption`  
  Load '75_LVBus0261114_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260941_consumption`  
  Load '75_LVBus0260941_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261054_consumption`  
  Load '75_LVBus0261054_consumption' has phase imbalance of 46.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261144_consumption`  
  Load '75_LVBus0261144_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261049_consumption`  
  Load '75_LVBus0261049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261016_consumption`  
  Load '75_LVBus0261016_consumption' has phase imbalance of 53.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260880_consumption`  
  Load '75_LVBus0260880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261012_consumption`  
  Load '75_LVBus0261012_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261218_consumption`  
  Load '75_LVBus0261218_consumption' has phase imbalance of 31.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261060_consumption`  
  Load '75_LVBus0261060_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260937_consumption`  
  Load '75_LVBus0260937_consumption' has phase imbalance of 93.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1952927_consumption`  
  Load '75_LVBus1952927_consumption' has phase imbalance of 23.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261130_consumption`  
  Load '75_LVBus0261130_consumption' has phase imbalance of 30.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261125_consumption`  
  Load '75_LVBus0261125_consumption' has phase imbalance of 37.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261072_consumption`  
  Load '75_LVBus0261072_consumption' has phase imbalance of 266.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261153_consumption`  
  Load '75_LVBus0261153_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260828_consumption`  
  Load '75_LVBus0260828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260968_consumption`  
  Load '75_LVBus0260968_consumption' has phase imbalance of 38.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1934315_consumption`  
  Load '75_LVBus1934315_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261137_consumption`  
  Load '75_LVBus0261137_consumption' has phase imbalance of 54.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261035_consumption`  
  Load '75_LVBus0261035_consumption' has phase imbalance of 121.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260965_consumption`  
  Load '75_LVBus0260965_consumption' has phase imbalance of 149.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260943_consumption`  
  Load '75_LVBus0260943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261112_consumption`  
  Load '75_LVBus0261112_consumption' has phase imbalance of 257.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261205_consumption`  
  Load '75_LVBus0261205_consumption' has phase imbalance of 202.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261103_consumption`  
  Load '75_LVBus0261103_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260971_consumption`  
  Load '75_LVBus0260971_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261110_consumption`  
  Load '75_LVBus0261110_consumption' has phase imbalance of 110.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261018_consumption`  
  Load '75_LVBus0261018_consumption' has phase imbalance of 75.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260829_consumption`  
  Load '75_LVBus0260829_consumption' has phase imbalance of 35.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260884_consumption`  
  Load '75_LVBus0260884_consumption' has phase imbalance of 146.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261078_consumption`  
  Load '75_LVBus0261078_consumption' has phase imbalance of 143.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261124_consumption`  
  Load '75_LVBus0261124_consumption' has phase imbalance of 86.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261037_consumption`  
  Load '75_LVBus0261037_consumption' has phase imbalance of 96.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260817_consumption`  
  Load '75_LVBus0260817_consumption' has phase imbalance of 53.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261231_consumption`  
  Load '75_LVBus0261231_consumption' has phase imbalance of 38.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260849_consumption`  
  Load '75_LVBus0260849_consumption' has phase imbalance of 215.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261106_consumption`  
  Load '75_LVBus0261106_consumption' has phase imbalance of 189.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261029_consumption`  
  Load '75_LVBus0261029_consumption' has phase imbalance of 40.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260898_consumption`  
  Load '75_LVBus0260898_consumption' has phase imbalance of 61.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1934314_consumption`  
  Load '75_LVBus1934314_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261209_consumption`  
  Load '75_LVBus0261209_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260938_consumption`  
  Load '75_LVBus0260938_consumption' has phase imbalance of 89.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260944_consumption`  
  Load '75_LVBus0260944_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261156_consumption`  
  Load '75_LVBus0261156_consumption' has phase imbalance of 73.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261074_consumption`  
  Load '75_LVBus0261074_consumption' has phase imbalance of 112.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260992_consumption`  
  Load '75_LVBus0260992_consumption' has phase imbalance of 103.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260893_consumption`  
  Load '75_LVBus0260893_consumption' has phase imbalance of 31.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260912_consumption`  
  Load '75_LVBus0260912_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260961_consumption`  
  Load '75_LVBus0260961_consumption' has phase imbalance of 57.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1951676_consumption`  
  Load '75_LVBus1951676_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261105_consumption`  
  Load '75_LVBus0261105_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261155_consumption`  
  Load '75_LVBus0261155_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261121_consumption`  
  Load '75_LVBus0261121_consumption' has phase imbalance of 49.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261042_consumption`  
  Load '75_LVBus0261042_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261247_consumption`  
  Load '75_LVBus0261247_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261094_consumption`  
  Load '75_LVBus0261094_consumption' has phase imbalance of 217.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261253_consumption`  
  Load '75_LVBus0261253_consumption' has phase imbalance of 139.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260977_consumption`  
  Load '75_LVBus0260977_consumption' has phase imbalance of 25.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260869_consumption`  
  Load '75_LVBus0260869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260830_consumption`  
  Load '75_LVBus0260830_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0260975_consumption`  
  Load '75_LVBus0260975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0261251_consumption`  
  Load '75_LVBus0261251_consumption' has phase imbalance of 87.7%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 848 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0260910' has balanced aggregate load across 3 phase(s) (max spread 1.93%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  456 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  53 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0260786_consumption, 75_LVBus0260825_consumption, 75_LVBus0260828_consumption, 75_LVBus0260830_consumption, 75_LVBus0260869_consumption, 75_LVBus0260880_consumption, 75_LVBus0260891_consumption, 75_LVBus0260894_consumption, 75_LVBus0260912_consumption, 75_LVBus0260922_consumption, 75_LVBus0260939_consumption, 75_LVBus0260943_consumption, 75_LVBus0260952_consumption, 75_LVBus0260953_consumption, 75_LVBus0260972_consumption, 75_LVBus0260973_consumption, 75_LVBus0260974_consumption, 75_LVBus0260975_consumption, 75_LVBus0260991_consumption, 75_LVBus0260993_consumption, 75_LVBus0261014_consumption, 75_LVBus0261049_consumption, 75_LVBus0261070_consumption, 75_LVBus0261072_consumption, 75_LVBus0261073_consumption, 75_LVBus0261081_consumption, 75_LVBus0261082_consumption, 75_LVBus0261083_consumption, 75_LVBus0261090_consumption, 75_LVBus0261094_consumption, 75_LVBus0261103_consumption, 75_LVBus0261106_consumption, 75_LVBus0261112_consumption, 75_LVBus0261114_consumption, 75_LVBus0261127_consumption, 75_LVBus0261133_consumption, 75_LVBus0261141_consumption, 75_LVBus0261142_consumption, 75_LVBus0261143_consumption, 75_LVBus0261150_consumption, 75_LVBus0261157_consumption, 75_LVBus0261180_consumption, 75_LVBus0261191_consumption, 75_LVBus0261198_consumption, 75_LVBus0261202_consumption, 75_LVBus0261205_consumption, 75_LVBus0261206_consumption, 75_LVBus0261232_consumption, 75_LVBus0261257_consumption, 75_LVBus1934314_consumption, 75_LVBus1934319_consumption, 75_LVBus1951676_consumption, 75_LVBus1963701_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  424 group(s) of loads (848 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  569 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0260764_consumption, 75_LVBus0260764_production, 75_LVBus0260766_consumption, 75_LVBus0260766_production, 75_LVBus0260767_consumption, 75_LVBus0260767_production, 75_LVBus0260768_consumption, 75_LVBus0260768_production, 75_LVBus0260769_consumption, 75_LVBus0260769_production, 75_LVBus0260770_consumption, 75_LVBus0260770_production, 75_LVBus0260771_consumption, 75_LVBus0260771_production, 75_LVBus0260772_consumption, 75_LVBus0260772_production, 75_LVBus0260773_consumption, 75_LVBus0260773_production, 75_LVBus0260774_production, 75_LVBus0260775_consumption, 75_LVBus0260775_production, 75_LVBus0260777_consumption, 75_LVBus0260777_production, 75_LVBus0260778_production, 75_LVBus0260779_consumption, 75_LVBus0260779_production, 75_LVBus0260780_consumption, 75_LVBus0260780_production, 75_LVBus0260781_consumption, 75_LVBus0260781_production, 75_LVBus0260782_consumption, 75_LVBus0260782_production, 75_LVBus0260783_consumption, 75_LVBus0260783_production, 75_LVBus0260784_production, 75_LVBus0260785_consumption, 75_LVBus0260785_production, 75_LVBus0260786_production, 75_LVBus0260788_production, 75_LVBus0260790_production, 75_LVBus0260791_production, 75_LVBus0260793_production, 75_LVBus0260795_consumption, 75_LVBus0260795_production, 75_LVBus0260796_consumption, 75_LVBus0260796_production, 75_LVBus0260797_consumption, 75_LVBus0260797_production, 75_LVBus0260798_consumption, 75_LVBus0260798_production, 75_LVBus0260799_consumption, 75_LVBus0260799_production, 75_LVBus0260800_consumption, 75_LVBus0260800_production, 75_LVBus0260801_consumption, 75_LVBus0260801_production, 75_LVBus0260802_production, 75_LVBus0260803_production, 75_LVBus0260804_consumption, 75_LVBus0260804_production, 75_LVBus0260805_consumption, 75_LVBus0260805_production, 75_LVBus0260807_consumption, 75_LVBus0260807_production, 75_LVBus0260808_consumption, 75_LVBus0260808_production, 75_LVBus0260809_consumption, 75_LVBus0260809_production, 75_LVBus0260810_consumption, 75_LVBus0260810_production, 75_LVBus0260811_consumption, 75_LVBus0260811_production, 75_LVBus0260812_production, 75_LVBus0260813_consumption, 75_LVBus0260813_production, 75_LVBus0260815_consumption, 75_LVBus0260815_production, 75_LVBus0260817_production, 75_LVBus0260819_production, 75_LVBus0260821_production, 75_LVBus0260823_production, 75_LVBus0260824_production, 75_LVBus0260825_production, 75_LVBus0260826_production, 75_LVBus0260827_production, 75_LVBus0260828_production, 75_LVBus0260829_production, 75_LVBus0260830_production, 75_LVBus0260831_consumption, 75_LVBus0260831_production, 75_LVBus0260832_production, 75_LVBus0260834_production, 75_LVBus0260836_consumption, 75_LVBus0260836_production, 75_LVBus0260838_production, 75_LVBus0260840_consumption, 75_LVBus0260840_production, 75_LVBus0260842_production, 75_LVBus0260844_consumption, 75_LVBus0260844_production, 75_LVBus0260846_production, 75_LVBus0260847_consumption, 75_LVBus0260847_production, 75_LVBus0260848_production, 75_LVBus0260849_production, 75_LVBus0260850_production, 75_LVBus0260851_production, 75_LVBus0260852_production, 75_LVBus0260853_consumption, 75_LVBus0260853_production, 75_LVBus0260854_production, 75_LVBus0260855_consumption, 75_LVBus0260855_production, 75_LVBus0260856_consumption, 75_LVBus0260856_production, 75_LVBus0260857_consumption, 75_LVBus0260857_production, 75_LVBus0260858_consumption, 75_LVBus0260858_production, 75_LVBus0260859_consumption, 75_LVBus0260859_production, 75_LVBus0260860_consumption, 75_LVBus0260860_production, 75_LVBus0260861_production, 75_LVBus0260862_consumption, 75_LVBus0260862_production, 75_LVBus0260863_production, 75_LVBus0260864_consumption, 75_LVBus0260864_production, 75_LVBus0260865_consumption, 75_LVBus0260865_production, 75_LVBus0260866_consumption, 75_LVBus0260866_production, 75_LVBus0260867_consumption, 75_LVBus0260867_production, 75_LVBus0260869_production, 75_LVBus0260870_production, 75_LVBus0260871_consumption, 75_LVBus0260871_production, 75_LVBus0260873_consumption, 75_LVBus0260873_production, 75_LVBus0260874_consumption, 75_LVBus0260874_production, 75_LVBus0260875_production, 75_LVBus0260876_consumption, 75_LVBus0260876_production, 75_LVBus0260878_consumption, 75_LVBus0260878_production, 75_LVBus0260879_consumption, 75_LVBus0260879_production, 75_LVBus0260880_production, 75_LVBus0260882_consumption, 75_LVBus0260882_production, 75_LVBus0260883_production, 75_LVBus0260884_production, 75_LVBus0260885_production, 75_LVBus0260887_consumption, 75_LVBus0260887_production, 75_LVBus0260888_consumption, 75_LVBus0260888_production, 75_LVBus0260889_consumption, 75_LVBus0260889_production, 75_LVBus0260890_production, 75_LVBus0260891_production, 75_LVBus0260892_production, 75_LVBus0260893_production, 75_LVBus0260894_production, 75_LVBus0260895_production, 75_LVBus0260896_production, 75_LVBus0260897_consumption, 75_LVBus0260897_production, 75_LVBus0260898_production, 75_LVBus0260900_production, 75_LVBus0260902_consumption, 75_LVBus0260902_production, 75_LVBus0260904_production, 75_LVBus0260905_consumption, 75_LVBus0260905_production, 75_LVBus0260906_production, 75_LVBus0260907_production, 75_LVBus0260910_production, 75_LVBus0260912_production, 75_LVBus0260914_production, 75_LVBus0260915_consumption, 75_LVBus0260915_production, 75_LVBus0260916_production, 75_LVBus0260917_production, 75_LVBus0260919_production, 75_LVBus0260920_production, 75_LVBus0260921_production, 75_LVBus0260922_production, 75_LVBus0260923_production, 75_LVBus0260925_consumption, 75_LVBus0260925_production, 75_LVBus0260926_production, 75_LVBus0260927_consumption, 75_LVBus0260927_production, 75_LVBus0260928_consumption, 75_LVBus0260928_production, 75_LVBus0260929_consumption, 75_LVBus0260929_production, 75_LVBus0260930_consumption, 75_LVBus0260930_production, 75_LVBus0260931_production, 75_LVBus0260932_consumption, 75_LVBus0260932_production, 75_LVBus0260933_consumption, 75_LVBus0260933_production, 75_LVBus0260934_consumption, 75_LVBus0260934_production, 75_LVBus0260935_production, 75_LVBus0260937_production, 75_LVBus0260938_production, 75_LVBus0260939_production, 75_LVBus0260940_consumption, 75_LVBus0260940_production, 75_LVBus0260941_production, 75_LVBus0260942_production, 75_LVBus0260943_production, 75_LVBus0260944_production, 75_LVBus0260945_production, 75_LVBus0260947_production, 75_LVBus0260948_production, 75_LVBus0260950_consumption, 75_LVBus0260950_production, 75_LVBus0260951_production, 75_LVBus0260952_production, 75_LVBus0260953_production, 75_LVBus0260954_consumption, 75_LVBus0260954_production, 75_LVBus0260956_consumption, 75_LVBus0260956_production, 75_LVBus0260957_production, 75_LVBus0260959_production, 75_LVBus0260961_production, 75_LVBus0260962_production, 75_LVBus0260963_consumption, 75_LVBus0260963_production, 75_LVBus0260965_production, 75_LVBus0260966_production, 75_LVBus0260967_production, 75_LVBus0260968_production, 75_LVBus0260969_production, 75_LVBus0260970_production, 75_LVBus0260971_production, 75_LVBus0260972_production, 75_LVBus0260973_production, 75_LVBus0260974_production, 75_LVBus0260975_production, 75_LVBus0260976_production, 75_LVBus0260977_production, 75_LVBus0260979_consumption, 75_LVBus0260979_production, 75_LVBus0260981_production, 75_LVBus0260983_production, 75_LVBus0260984_consumption, 75_LVBus0260984_production, 75_LVBus0260985_consumption, 75_LVBus0260985_production, 75_LVBus0260987_consumption, 75_LVBus0260987_production, 75_LVBus0260988_consumption, 75_LVBus0260988_production, 75_LVBus0260989_consumption, 75_LVBus0260989_production, 75_LVBus0260990_consumption, 75_LVBus0260990_production, 75_LVBus0260991_production, 75_LVBus0260992_production, 75_LVBus0260993_production, 75_LVBus0260994_consumption, 75_LVBus0260994_production, 75_LVBus0260995_consumption, 75_LVBus0260995_production, 75_LVBus0260996_production, 75_LVBus0260997_production, 75_LVBus0260998_consumption, 75_LVBus0260998_production, 75_LVBus0260999_production, 75_LVBus0261001_consumption, 75_LVBus0261001_production, 75_LVBus0261002_production, 75_LVBus0261004_production, 75_LVBus0261006_production, 75_LVBus0261008_consumption, 75_LVBus0261008_production, 75_LVBus0261009_production, 75_LVBus0261011_production, 75_LVBus0261012_production, 75_LVBus0261013_production, 75_LVBus0261014_production, 75_LVBus0261015_consumption, 75_LVBus0261015_production, 75_LVBus0261016_production, 75_LVBus0261017_production, 75_LVBus0261018_production, 75_LVBus0261020_production, 75_LVBus0261021_production, 75_LVBus0261023_production, 75_LVBus0261025_consumption, 75_LVBus0261025_production, 75_LVBus0261026_production, 75_LVBus0261027_production, 75_LVBus0261028_production, 75_LVBus0261029_production, 75_LVBus0261031_consumption, 75_LVBus0261031_production, 75_LVBus0261032_production, 75_LVBus0261033_production, 75_LVBus0261035_production, 75_LVBus0261036_consumption, 75_LVBus0261036_production, 75_LVBus0261037_production, 75_LVBus0261038_production, 75_LVBus0261039_production, 75_LVBus0261040_consumption, 75_LVBus0261040_production, 75_LVBus0261041_production, 75_LVBus0261042_production, 75_LVBus0261044_consumption, 75_LVBus0261044_production, 75_LVBus0261045_production, 75_LVBus0261046_production, 75_LVBus0261047_production, 75_LVBus0261049_production, 75_LVBus0261050_production, 75_LVBus0261052_consumption, 75_LVBus0261052_production, 75_LVBus0261053_consumption, 75_LVBus0261053_production, 75_LVBus0261054_production, 75_LVBus0261055_consumption, 75_LVBus0261055_production, 75_LVBus0261056_production, 75_LVBus0261058_consumption, 75_LVBus0261058_production, 75_LVBus0261059_production, 75_LVBus0261060_production, 75_LVBus0261062_consumption, 75_LVBus0261062_production, 75_LVBus0261063_consumption, 75_LVBus0261063_production, 75_LVBus0261065_production, 75_LVBus0261066_consumption, 75_LVBus0261066_production, 75_LVBus0261067_production, 75_LVBus0261069_consumption, 75_LVBus0261069_production, 75_LVBus0261070_production, 75_LVBus0261072_production, 75_LVBus0261073_production, 75_LVBus0261074_production, 75_LVBus0261075_production, 75_LVBus0261076_consumption, 75_LVBus0261076_production, 75_LVBus0261077_production, 75_LVBus0261078_production, 75_LVBus0261079_production, 75_LVBus0261080_production, 75_LVBus0261081_production, 75_LVBus0261082_production, 75_LVBus0261083_production, 75_LVBus0261084_consumption, 75_LVBus0261084_production, 75_LVBus0261086_production, 75_LVBus0261088_consumption, 75_LVBus0261088_production, 75_LVBus0261089_production, 75_LVBus0261090_production, 75_LVBus0261092_production, 75_LVBus0261093_consumption, 75_LVBus0261093_production, 75_LVBus0261094_production, 75_LVBus0261095_consumption, 75_LVBus0261095_production, 75_LVBus0261097_production, 75_LVBus0261098_production, 75_LVBus0261099_production, 75_LVBus0261100_production, 75_LVBus0261101_production, 75_LVBus0261102_production, 75_LVBus0261103_production, 75_LVBus0261104_production, 75_LVBus0261105_production, 75_LVBus0261106_production, 75_LVBus0261107_production, 75_LVBus0261108_consumption, 75_LVBus0261108_production, 75_LVBus0261109_production, 75_LVBus0261110_production, 75_LVBus0261112_production, 75_LVBus0261114_production, 75_LVBus0261115_production, 75_LVBus0261116_consumption, 75_LVBus0261116_production, 75_LVBus0261117_consumption, 75_LVBus0261117_production, 75_LVBus0261118_production, 75_LVBus0261119_production, 75_LVBus0261120_production, 75_LVBus0261121_production, 75_LVBus0261122_production, 75_LVBus0261124_production, 75_LVBus0261125_production, 75_LVBus0261127_production, 75_LVBus0261128_consumption, 75_LVBus0261128_production, 75_LVBus0261129_production, 75_LVBus0261130_production, 75_LVBus0261131_production, 75_LVBus0261132_production, 75_LVBus0261133_production, 75_LVBus0261134_production, 75_LVBus0261135_production, 75_LVBus0261136_production, 75_LVBus0261137_production, 75_LVBus0261138_production, 75_LVBus0261139_production, 75_LVBus0261141_production, 75_LVBus0261142_production, 75_LVBus0261143_production, 75_LVBus0261144_production, 75_LVBus0261146_production, 75_LVBus0261148_consumption, 75_LVBus0261148_production, 75_LVBus0261149_production, 75_LVBus0261150_production, 75_LVBus0261151_production, 75_LVBus0261152_production, 75_LVBus0261153_production, 75_LVBus0261154_production, 75_LVBus0261155_production, 75_LVBus0261156_production, 75_LVBus0261157_production, 75_LVBus0261158_production, 75_LVBus0261159_production, 75_LVBus0261160_production, 75_LVBus0261170_production, 75_LVBus0261172_consumption, 75_LVBus0261172_production, 75_LVBus0261173_consumption, 75_LVBus0261173_production, 75_LVBus0261174_consumption, 75_LVBus0261174_production, 75_LVBus0261175_production, 75_LVBus0261176_production, 75_LVBus0261177_production, 75_LVBus0261178_production, 75_LVBus0261179_production, 75_LVBus0261180_production, 75_LVBus0261181_production, 75_LVBus0261182_production, 75_LVBus0261184_consumption, 75_LVBus0261184_production, 75_LVBus0261187_production, 75_LVBus0261188_production, 75_LVBus0261189_production, 75_LVBus0261190_consumption, 75_LVBus0261190_production, 75_LVBus0261191_production, 75_LVBus0261192_production, 75_LVBus0261193_production, 75_LVBus0261194_production, 75_LVBus0261195_production, 75_LVBus0261197_consumption, 75_LVBus0261197_production, 75_LVBus0261198_production, 75_LVBus0261199_production, 75_LVBus0261201_consumption, 75_LVBus0261201_production, 75_LVBus0261202_production, 75_LVBus0261203_production, 75_LVBus0261204_production, 75_LVBus0261205_production, 75_LVBus0261206_production, 75_LVBus0261207_consumption, 75_LVBus0261207_production, 75_LVBus0261208_production, 75_LVBus0261209_production, 75_LVBus0261210_production, 75_LVBus0261212_consumption, 75_LVBus0261212_production, 75_LVBus0261213_consumption, 75_LVBus0261213_production, 75_LVBus0261214_production, 75_LVBus0261216_production, 75_LVBus0261218_production, 75_LVBus0261222_production, 75_LVBus0261224_consumption, 75_LVBus0261224_production, 75_LVBus0261226_consumption, 75_LVBus0261226_production, 75_LVBus0261228_consumption, 75_LVBus0261228_production, 75_LVBus0261230_production, 75_LVBus0261231_production, 75_LVBus0261232_production, 75_LVBus0261233_production, 75_LVBus0261234_production, 75_LVBus0261235_consumption, 75_LVBus0261235_production, 75_LVBus0261236_production, 75_LVBus0261237_consumption, 75_LVBus0261237_production, 75_LVBus0261239_consumption, 75_LVBus0261239_production, 75_LVBus0261241_production, 75_LVBus0261242_production, 75_LVBus0261244_production, 75_LVBus0261246_production, 75_LVBus0261247_production, 75_LVBus0261248_consumption, 75_LVBus0261248_production, 75_LVBus0261249_consumption, 75_LVBus0261249_production, 75_LVBus0261251_production, 75_LVBus0261253_production, 75_LVBus0261254_consumption, 75_LVBus0261254_production, 75_LVBus0261255_consumption, 75_LVBus0261255_production, 75_LVBus0261256_production, 75_LVBus0261257_production, 75_LVBus0261258_production, 75_LVBus0261261_production, 75_LVBus0261263_production, 75_LVBus0261267_consumption, 75_LVBus0261267_production, 75_LVBus0261269_production, 75_LVBus1934312_consumption, 75_LVBus1934312_production, 75_LVBus1934313_production, 75_LVBus1934314_production, 75_LVBus1934315_production, 75_LVBus1934316_production, 75_LVBus1934317_production, 75_LVBus1934318_consumption, 75_LVBus1934318_production, 75_LVBus1934319_production, 75_LVBus1946357_production, 75_LVBus1946358_production, 75_LVBus1946359_consumption, 75_LVBus1946359_production, 75_LVBus1951676_production, 75_LVBus1951677_production, 75_LVBus1951678_production, 75_LVBus1952927_production, 75_LVBus1952928_consumption, 75_LVBus1952928_production, 75_LVBus1952929_production, 75_LVBus1952930_production, 75_LVBus1960488_production, 75_LVBus1960489_consumption, 75_LVBus1960489_production, 75_LVBus1960490_consumption, 75_LVBus1960490_production, 75_LVBus1962030_consumption, 75_LVBus1962030_production, 75_LVBus1962031_production, 75_LVBus1962032_consumption, 75_LVBus1962032_production, 75_LVBus1962033_production, 75_LVBus1962034_consumption, 75_LVBus1962034_production, 75_LVBus1963701_production, 75_MVLV107233_consumption, 75_MVLV107233_production, 75_MVLV143218_consumption, 75_MVLV143218_production.

