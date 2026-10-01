# BMOPF Network Summary: 28_MVFeeder1181

**Generated:** 2026-10-01 23:34:02  
**Findings:** 0 errors · 5 warnings · 262 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 41 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 445 |  |
| line | 403 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 620 | 820.851 kW, 246.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 41 |  |
| switch | 0 |  |
| transformer | 41 | Dyn11×41 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 97 | 96 | 6 | 0 |
| LV_236V | 236.0 V | 348 | 307 | 614 | 0 |

**Transformer transitions:**

- `28_MVLV56119_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV83335_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24389_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26975_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV01944_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV08942_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV64812_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV28667_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV51991_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV60467_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV50749_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV08550_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV65347_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV63853_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV79194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20632_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85244_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV04553_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV53526_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV48941_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26909_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV44730_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV08869_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13689_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV56123_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV65324_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV15420_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26910_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49036_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV65332_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84800_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV51990_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24390_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV05961_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV04612_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24843_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47335_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV48136_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV15421_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV11690_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 149 |
| Tree depth (max hops) | 36 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 445 | 1 | 444 | 0 | 0 | 0 |
| Tier LV_236V | 348 | 41 | 307 | 0 | 0 | 0 |
| Tier MV_11.8kV | 97 | 1 | 96 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 41; skipped invalid branches: 0.

Galvanic zones: 42; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_GOURN | MV_11.8kV | 97 | 0 | 0 | 41 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1683 declared bus terminals; 1516 mapped line/closed-switch conductor edges; 167 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 33800.0 | 3.569 | 1860 |
| q_nom | 0.0 | 10100.0 | 3.569 | 1860 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.82 | 2520.0 | 1.555 | 403 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.624 | 41 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 360 of 620 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373785_consumption' has phase imbalance of 270.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374048_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373959_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374132_consumption' has phase imbalance of 194.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374055_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373957_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374143_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373929_consumption' has phase imbalance of 82.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374030_consumption' has phase imbalance of 254.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374108_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374162_consumption' has phase imbalance of 174.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374163_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373857_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374152_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374062_consumption' has phase imbalance of 109.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374005_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374121_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373799_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373898_consumption' has phase imbalance of 96.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374024_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus975385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373955_consumption' has phase imbalance of 140.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373867_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373846_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373927_consumption' has phase imbalance of 90.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373818_consumption' has phase imbalance of 280.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373868_consumption' has phase imbalance of 131.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374058_consumption' has phase imbalance of 80.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374038_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373783_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373786_consumption' has phase imbalance of 126.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374012_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373864_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374158_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373962_consumption' has phase imbalance of 268.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373969_consumption' has phase imbalance of 195.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374142_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373807_consumption' has phase imbalance of 236.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374088_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373804_consumption' has phase imbalance of 142.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373904_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374085_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373964_consumption' has phase imbalance of 80.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373793_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374028_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374089_consumption' has phase imbalance of 285.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373813_consumption' has phase imbalance of 73.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373922_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374023_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373839_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373950_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373810_consumption' has phase imbalance of 53.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus975383_consumption' has phase imbalance of 212.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373996_consumption' has phase imbalance of 21.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374004_consumption' has phase imbalance of 128.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374006_consumption' has phase imbalance of 147.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373877_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374093_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373998_consumption' has phase imbalance of 136.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374105_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373899_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373893_consumption' has phase imbalance of 21.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373837_consumption' has phase imbalance of 187.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374116_consumption' has phase imbalance of 194.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374076_consumption' has phase imbalance of 99.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373960_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374115_consumption' has phase imbalance of 98.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373941_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374101_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374052_consumption' has phase imbalance of 24.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374036_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373869_consumption' has phase imbalance of 56.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374151_consumption' has phase imbalance of 279.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373789_consumption' has phase imbalance of 296.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373906_consumption' has phase imbalance of 54.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373935_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374138_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374002_consumption' has phase imbalance of 142.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374061_consumption' has phase imbalance of 236.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373979_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373956_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373917_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373923_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373940_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373909_consumption' has phase imbalance of 141.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373958_consumption' has phase imbalance of 30.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373920_consumption' has phase imbalance of 87.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374157_consumption' has phase imbalance of 268.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373945_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374113_consumption' has phase imbalance of 82.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374125_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374042_consumption' has phase imbalance of 32.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374082_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373803_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374010_consumption' has phase imbalance of 98.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373976_consumption' has phase imbalance of 133.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373883_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374107_consumption' has phase imbalance of 244.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897629_consumption' has phase imbalance of 79.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374016_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373965_consumption' has phase imbalance of 238.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373841_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373987_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373859_consumption' has phase imbalance of 135.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374137_consumption' has phase imbalance of 218.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373967_consumption' has phase imbalance of 97.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373948_consumption' has phase imbalance of 220.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374022_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374118_consumption' has phase imbalance of 127.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373871_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374134_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374131_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373912_consumption' has phase imbalance of 212.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373778_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374140_consumption' has phase imbalance of 24.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373886_consumption' has phase imbalance of 116.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373802_consumption' has phase imbalance of 148.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373949_consumption' has phase imbalance of 26.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373812_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373986_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374159_consumption' has phase imbalance of 43.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373978_consumption' has phase imbalance of 220.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373968_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373850_consumption' has phase imbalance of 142.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373777_consumption' has phase imbalance of 204.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373934_consumption' has phase imbalance of 128.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373811_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373971_consumption' has phase imbalance of 137.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373972_consumption' has phase imbalance of 58.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus975379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373944_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374037_consumption' has phase imbalance of 155.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373879_consumption' has phase imbalance of 234.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373994_consumption' has phase imbalance of 134.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374027_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373876_consumption' has phase imbalance of 233.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374059_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374032_consumption' has phase imbalance of 224.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374095_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373953_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373894_consumption' has phase imbalance of 244.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373901_consumption' has phase imbalance of 257.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373995_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373814_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374167_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373878_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373851_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373992_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374054_consumption' has phase imbalance of 282.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374065_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373939_consumption' has phase imbalance of 206.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374149_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373988_consumption' has phase imbalance of 232.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373858_consumption' has phase imbalance of 42.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373896_consumption' has phase imbalance of 189.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373900_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373862_consumption' has phase imbalance of 190.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374072_consumption' has phase imbalance of 269.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374104_consumption' has phase imbalance of 211.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374096_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374040_consumption' has phase imbalance of 98.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373784_consumption' has phase imbalance of 39.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373797_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373840_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373921_consumption' has phase imbalance of 273.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373828_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374044_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373852_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374098_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374031_consumption' has phase imbalance of 261.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374112_consumption' has phase imbalance of 87.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373870_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373790_consumption' has phase imbalance of 64.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374003_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374041_consumption' has phase imbalance of 254.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374057_consumption' has phase imbalance of 251.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374026_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373970_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373885_consumption' has phase imbalance of 239.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373908_consumption' has phase imbalance of 231.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374034_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373936_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373983_consumption' has phase imbalance of 185.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373938_consumption' has phase imbalance of 41.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373798_consumption' has phase imbalance of 21.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373830_consumption' has phase imbalance of 164.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373984_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374120_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374017_consumption' has phase imbalance of 278.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373821_consumption' has phase imbalance of 212.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373835_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374008_consumption' has phase imbalance of 28.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus373873_consumption' has phase imbalance of 181.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374084_consumption' has phase imbalance of 86.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374090_consumption' has phase imbalance of 118.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374064_consumption' has phase imbalance of 186.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus374166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 620 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 820.851 kW |
| Total load Q | 246.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV56119_Transformer | 440.0 kVA | 7.7% |
| 28_MVLV83335_Transformer | 275.0 kVA | 7.8% |
| 28_MVLV24389_Transformer | 176.0 kVA | 9.0% |
| 28_MVLV26975_Transformer | 275.0 kVA | 8.9% |
| 28_MVLV01944_Transformer | 110.0 kVA | 7.0% |
| 28_MVLV08942_Transformer | 176.0 kVA | 6.1% |
| 28_MVLV64812_Transformer | 275.0 kVA | 4.8% |
| 28_MVLV28667_Transformer | 440.0 kVA | 11.5% |
| 28_MVLV51991_Transformer | 275.0 kVA | 5.8% |
| 28_MVLV60467_Transformer | 440.0 kVA | 7.4% |
| 28_MVLV50749_Transformer | 275.0 kVA | 9.3% |
| 28_MVLV08550_Transformer | 275.0 kVA | 8.5% |
| 28_MVLV65347_Transformer | 275.0 kVA | 9.6% |
| 28_MVLV63853_Transformer | 275.0 kVA | 1.8% |
| 28_MVLV79194_Transformer | 1.1 MVA | 12.3% |
| 28_MVLV20632_Transformer | 440.0 kVA | 8.7% |
| 28_MVLV85244_Transformer | 110.0 kVA | 2.4% |
| 28_MVLV04553_Transformer | 440.0 kVA | 6.8% |
| 28_MVLV53526_Transformer | 440.0 kVA | 10.4% |
| 28_MVLV48941_Transformer | 275.0 kVA | 7.8% |
| 28_MVLV26909_Transformer | 176.0 kVA | 3.2% |
| 28_MVLV44730_Transformer | 176.0 kVA | 6.6% |
| 28_MVLV08869_Transformer | 110.0 kVA | 3.0% |
| 28_MVLV13689_Transformer | 440.0 kVA | 7.4% |
| 28_MVLV56123_Transformer | 275.0 kVA | 4.1% |
| 28_MVLV65324_Transformer | 110.0 kVA | 1.1% |
| 28_MVLV15420_Transformer | 110.0 kVA | 0.4% |
| 28_MVLV26910_Transformer | 176.0 kVA | 3.5% |
| 28_MVLV49036_Transformer | 176.0 kVA | 3.2% |
| 28_MVLV65332_Transformer | 110.0 kVA | 2.5% |
| 28_MVLV84800_Transformer | 275.0 kVA | 6.5% |
| 28_MVLV51990_Transformer | 440.0 kVA | 9.8% |
| 28_MVLV24390_Transformer | 176.0 kVA | 10.7% |
| 28_MVLV05961_Transformer | 275.0 kVA | 5.0% |
| 28_MVLV04612_Transformer | 275.0 kVA | 7.6% |
| 28_MVLV24843_Transformer | 440.0 kVA | 6.2% |
| 28_MVLV47335_Transformer | 275.0 kVA | 6.8% |
| 28_MVLV48136_Transformer | 110.0 kVA | 2.2% |
| 28_MVLV15421_Transformer | 176.0 kVA | 11.5% |
| 28_MVLV11690_Transformer | 110.0 kVA | 0.9% |
| 28_MVLV41606_Transformer | 275.0 kVA | 4.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.82 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '28_LVBus373783' (LV, 0.24 kV) has an electrical reach of 1.12 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus373854' (LV, 0.24 kV) has an electrical reach of 13.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 445 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 445 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 41 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 97 |
| LV_236V | 4-wire | 348 / 348 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 348 |
| Neutral branches | 307 |
| Grounding points | 41 |
| Neutral sections | 41 |
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
| 11.78 kV | 97 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 42 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2420.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 348 / 97 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 361 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 361 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus373774_consumption, 28_LVBus373774_production, 28_LVBus373775_production, 28_LVBus373776_production, 28_LVBus373777_production, 28_LVBus373778_production, 28_LVBus373779_consumption, 28_LVBus373779_production, 28_LVBus373783_production, 28_LVBus373784_production, 28_LVBus373785_production, 28_LVBus373786_production, 28_LVBus373788_consumption, 28_LVBus373788_production, 28_LVBus373789_production, 28_LVBus373790_production, 28_LVBus373791_production, 28_LVBus373793_production, 28_LVBus373794_consumption, 28_LVBus373794_production, 28_LVBus373795_consumption, 28_LVBus373795_production, 28_LVBus373796_consumption, 28_LVBus373796_production, 28_LVBus373797_production, 28_LVBus373798_production, 28_LVBus373799_production, 28_LVBus373800_production, 28_LVBus373802_production, 28_LVBus373803_production, 28_LVBus373804_production, 28_LVBus373806_consumption, 28_LVBus373806_production, 28_LVBus373807_production, 28_LVBus373809_consumption, 28_LVBus373809_production, 28_LVBus373810_production, 28_LVBus373811_production, 28_LVBus373812_production, 28_LVBus373813_production, 28_LVBus373814_production, 28_LVBus373816_consumption, 28_LVBus373816_production, 28_LVBus373817_consumption, 28_LVBus373817_production, 28_LVBus373818_production, 28_LVBus373820_production, 28_LVBus373821_production, 28_LVBus373822_consumption, 28_LVBus373822_production, 28_LVBus373826_consumption, 28_LVBus373826_production, 28_LVBus373827_production, 28_LVBus373828_production, 28_LVBus373829_consumption, 28_LVBus373829_production, 28_LVBus373830_production, 28_LVBus373831_production, 28_LVBus373833_production, 28_LVBus373835_production, 28_LVBus373837_production, 28_LVBus373839_production, 28_LVBus373840_production, 28_LVBus373841_production, 28_LVBus373842_production, 28_LVBus373843_production, 28_LVBus373844_consumption, 28_LVBus373844_production, 28_LVBus373845_production, 28_LVBus373846_production, 28_LVBus373847_production, 28_LVBus373848_production, 28_LVBus373850_production, 28_LVBus373851_production, 28_LVBus373852_production, 28_LVBus373854_production, 28_LVBus373856_production, 28_LVBus373857_production, 28_LVBus373858_production, 28_LVBus373859_production, 28_LVBus373861_consumption, 28_LVBus373861_production, 28_LVBus373862_production, 28_LVBus373863_consumption, 28_LVBus373863_production, 28_LVBus373864_production, 28_LVBus373866_production, 28_LVBus373867_production, 28_LVBus373868_production, 28_LVBus373869_production, 28_LVBus373870_production, 28_LVBus373871_production, 28_LVBus373872_consumption, 28_LVBus373872_production, 28_LVBus373873_production, 28_LVBus373875_consumption, 28_LVBus373875_production, 28_LVBus373876_production, 28_LVBus373877_production, 28_LVBus373878_production, 28_LVBus373879_production, 28_LVBus373880_production, 28_LVBus373883_production, 28_LVBus373884_production, 28_LVBus373885_production, 28_LVBus373886_production, 28_LVBus373887_consumption, 28_LVBus373887_production, 28_LVBus373892_production, 28_LVBus373893_production, 28_LVBus373894_production, 28_LVBus373895_production, 28_LVBus373896_production, 28_LVBus373898_production, 28_LVBus373899_production, 28_LVBus373900_production, 28_LVBus373901_production, 28_LVBus373902_production, 28_LVBus373904_production, 28_LVBus373906_production, 28_LVBus373908_production, 28_LVBus373909_production, 28_LVBus373910_production, 28_LVBus373911_production, 28_LVBus373912_production, 28_LVBus373914_production, 28_LVBus373916_consumption, 28_LVBus373916_production, 28_LVBus373917_production, 28_LVBus373919_consumption, 28_LVBus373919_production, 28_LVBus373920_production, 28_LVBus373921_production, 28_LVBus373922_production, 28_LVBus373923_production, 28_LVBus373924_consumption, 28_LVBus373924_production, 28_LVBus373925_consumption, 28_LVBus373925_production, 28_LVBus373926_production, 28_LVBus373927_production, 28_LVBus373929_production, 28_LVBus373933_consumption, 28_LVBus373933_production, 28_LVBus373934_production, 28_LVBus373935_production, 28_LVBus373936_production, 28_LVBus373938_production, 28_LVBus373939_production, 28_LVBus373940_production, 28_LVBus373941_production, 28_LVBus373942_consumption, 28_LVBus373942_production, 28_LVBus373944_production, 28_LVBus373945_production, 28_LVBus373947_consumption, 28_LVBus373947_production, 28_LVBus373948_production, 28_LVBus373949_production, 28_LVBus373950_production, 28_LVBus373951_consumption, 28_LVBus373951_production, 28_LVBus373952_production, 28_LVBus373953_production, 28_LVBus373955_production, 28_LVBus373956_production, 28_LVBus373957_production, 28_LVBus373958_production, 28_LVBus373959_production, 28_LVBus373960_production, 28_LVBus373962_production, 28_LVBus373963_consumption, 28_LVBus373963_production, 28_LVBus373964_production, 28_LVBus373965_production, 28_LVBus373967_production, 28_LVBus373968_production, 28_LVBus373969_production, 28_LVBus373970_production, 28_LVBus373971_production, 28_LVBus373972_production, 28_LVBus373976_production, 28_LVBus373977_consumption, 28_LVBus373977_production, 28_LVBus373978_production, 28_LVBus373979_production, 28_LVBus373980_production, 28_LVBus373982_production, 28_LVBus373983_production, 28_LVBus373984_production, 28_LVBus373986_production, 28_LVBus373987_production, 28_LVBus373988_production, 28_LVBus373989_production, 28_LVBus373990_consumption, 28_LVBus373990_production, 28_LVBus373991_production, 28_LVBus373992_production, 28_LVBus373994_production, 28_LVBus373995_production, 28_LVBus373996_production, 28_LVBus373997_production, 28_LVBus373998_production, 28_LVBus374002_production, 28_LVBus374003_production, 28_LVBus374004_production, 28_LVBus374005_production, 28_LVBus374006_production, 28_LVBus374007_production, 28_LVBus374008_production, 28_LVBus374009_production, 28_LVBus374010_production, 28_LVBus374012_production, 28_LVBus374013_consumption, 28_LVBus374013_production, 28_LVBus374014_production, 28_LVBus374015_production, 28_LVBus374016_production, 28_LVBus374017_production, 28_LVBus374018_production, 28_LVBus374020_production, 28_LVBus374021_production, 28_LVBus374022_production, 28_LVBus374023_production, 28_LVBus374024_production, 28_LVBus374026_production, 28_LVBus374027_production, 28_LVBus374028_production, 28_LVBus374030_production, 28_LVBus374031_production, 28_LVBus374032_production, 28_LVBus374033_consumption, 28_LVBus374033_production, 28_LVBus374034_production, 28_LVBus374036_production, 28_LVBus374037_production, 28_LVBus374038_production, 28_LVBus374040_production, 28_LVBus374041_production, 28_LVBus374042_production, 28_LVBus374043_production, 28_LVBus374044_production, 28_LVBus374045_consumption, 28_LVBus374045_production, 28_LVBus374046_production, 28_LVBus374048_production, 28_LVBus374050_production, 28_LVBus374052_production, 28_LVBus374054_production, 28_LVBus374055_production, 28_LVBus374057_production, 28_LVBus374058_production, 28_LVBus374059_production, 28_LVBus374061_production, 28_LVBus374062_production, 28_LVBus374063_production, 28_LVBus374064_production, 28_LVBus374065_production, 28_LVBus374066_production, 28_LVBus374067_production, 28_LVBus374069_production, 28_LVBus374071_production, 28_LVBus374072_production, 28_LVBus374073_production, 28_LVBus374074_production, 28_LVBus374076_production, 28_LVBus374080_consumption, 28_LVBus374080_production, 28_LVBus374081_consumption, 28_LVBus374081_production, 28_LVBus374082_production, 28_LVBus374083_production, 28_LVBus374084_production, 28_LVBus374085_production, 28_LVBus374086_production, 28_LVBus374088_production, 28_LVBus374089_production, 28_LVBus374090_production, 28_LVBus374091_production, 28_LVBus374092_consumption, 28_LVBus374092_production, 28_LVBus374093_production, 28_LVBus374094_production, 28_LVBus374095_production, 28_LVBus374096_production, 28_LVBus374097_consumption, 28_LVBus374097_production, 28_LVBus374098_production, 28_LVBus374100_consumption, 28_LVBus374100_production, 28_LVBus374101_production, 28_LVBus374102_production, 28_LVBus374104_production, 28_LVBus374105_production, 28_LVBus374107_production, 28_LVBus374108_production, 28_LVBus374110_production, 28_LVBus374112_production, 28_LVBus374113_production, 28_LVBus374115_production, 28_LVBus374116_production, 28_LVBus374117_consumption, 28_LVBus374117_production, 28_LVBus374118_production, 28_LVBus374120_production, 28_LVBus374121_production, 28_LVBus374122_production, 28_LVBus374124_consumption, 28_LVBus374124_production, 28_LVBus374125_production, 28_LVBus374131_production, 28_LVBus374132_production, 28_LVBus374133_consumption, 28_LVBus374133_production, 28_LVBus374134_production, 28_LVBus374135_production, 28_LVBus374136_production, 28_LVBus374137_production, 28_LVBus374138_production, 28_LVBus374140_production, 28_LVBus374142_production, 28_LVBus374143_production, 28_LVBus374144_production, 28_LVBus374146_consumption, 28_LVBus374146_production, 28_LVBus374147_production, 28_LVBus374148_consumption, 28_LVBus374148_production, 28_LVBus374149_production, 28_LVBus374150_consumption, 28_LVBus374150_production, 28_LVBus374151_production, 28_LVBus374152_production, 28_LVBus374153_production, 28_LVBus374157_production, 28_LVBus374158_production, 28_LVBus374159_production, 28_LVBus374160_production, 28_LVBus374162_production, 28_LVBus374163_production, 28_LVBus374165_consumption, 28_LVBus374165_production, 28_LVBus374166_production, 28_LVBus374167_production, 28_LVBus897629_production, 28_LVBus975379_production, 28_LVBus975380_consumption, 28_LVBus975380_production, 28_LVBus975381_consumption, 28_LVBus975381_production, 28_LVBus975382_consumption, 28_LVBus975382_production, 28_LVBus975383_production, 28_LVBus975384_production, 28_LVBus975385_production, 28_MVLV20246_consumption, 28_MVLV20246_production, 28_MVLV70731_consumption, 28_MVLV70731_production, 28_MVLV74352_consumption, 28_MVLV74352_production.

## 9. Data Quality Summary

**Total findings:** 267 (0 errors, 5 warnings, 262 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  360 of 620 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.82 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  361 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373776_consumption`  
  Load '28_LVBus373776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373785_consumption`  
  Load '28_LVBus373785_consumption' has phase imbalance of 270.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374048_consumption`  
  Load '28_LVBus374048_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373959_consumption`  
  Load '28_LVBus373959_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374160_consumption`  
  Load '28_LVBus374160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374132_consumption`  
  Load '28_LVBus374132_consumption' has phase imbalance of 194.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374046_consumption`  
  Load '28_LVBus374046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374055_consumption`  
  Load '28_LVBus374055_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373957_consumption`  
  Load '28_LVBus373957_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374143_consumption`  
  Load '28_LVBus374143_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374066_consumption`  
  Load '28_LVBus374066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373929_consumption`  
  Load '28_LVBus373929_consumption' has phase imbalance of 82.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374030_consumption`  
  Load '28_LVBus374030_consumption' has phase imbalance of 254.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374108_consumption`  
  Load '28_LVBus374108_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374162_consumption`  
  Load '28_LVBus374162_consumption' has phase imbalance of 174.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374009_consumption`  
  Load '28_LVBus374009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374163_consumption`  
  Load '28_LVBus374163_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373857_consumption`  
  Load '28_LVBus373857_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374152_consumption`  
  Load '28_LVBus374152_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373791_consumption`  
  Load '28_LVBus373791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374062_consumption`  
  Load '28_LVBus374062_consumption' has phase imbalance of 109.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374005_consumption`  
  Load '28_LVBus374005_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374121_consumption`  
  Load '28_LVBus374121_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373799_consumption`  
  Load '28_LVBus373799_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373898_consumption`  
  Load '28_LVBus373898_consumption' has phase imbalance of 96.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374024_consumption`  
  Load '28_LVBus374024_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus975385_consumption`  
  Load '28_LVBus975385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374153_consumption`  
  Load '28_LVBus374153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373955_consumption`  
  Load '28_LVBus373955_consumption' has phase imbalance of 140.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373867_consumption`  
  Load '28_LVBus373867_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373846_consumption`  
  Load '28_LVBus373846_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374073_consumption`  
  Load '28_LVBus374073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373927_consumption`  
  Load '28_LVBus373927_consumption' has phase imbalance of 90.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373818_consumption`  
  Load '28_LVBus373818_consumption' has phase imbalance of 280.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373868_consumption`  
  Load '28_LVBus373868_consumption' has phase imbalance of 131.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373854_consumption`  
  Load '28_LVBus373854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374058_consumption`  
  Load '28_LVBus374058_consumption' has phase imbalance of 80.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374038_consumption`  
  Load '28_LVBus374038_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373783_consumption`  
  Load '28_LVBus373783_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373786_consumption`  
  Load '28_LVBus373786_consumption' has phase imbalance of 126.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374012_consumption`  
  Load '28_LVBus374012_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373864_consumption`  
  Load '28_LVBus373864_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373842_consumption`  
  Load '28_LVBus373842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374158_consumption`  
  Load '28_LVBus374158_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373962_consumption`  
  Load '28_LVBus373962_consumption' has phase imbalance of 268.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373969_consumption`  
  Load '28_LVBus373969_consumption' has phase imbalance of 195.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374142_consumption`  
  Load '28_LVBus374142_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373843_consumption`  
  Load '28_LVBus373843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373807_consumption`  
  Load '28_LVBus373807_consumption' has phase imbalance of 236.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374088_consumption`  
  Load '28_LVBus374088_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373804_consumption`  
  Load '28_LVBus373804_consumption' has phase imbalance of 142.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373991_consumption`  
  Load '28_LVBus373991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374102_consumption`  
  Load '28_LVBus374102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373904_consumption`  
  Load '28_LVBus373904_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374085_consumption`  
  Load '28_LVBus374085_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373964_consumption`  
  Load '28_LVBus373964_consumption' has phase imbalance of 80.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373793_consumption`  
  Load '28_LVBus373793_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374028_consumption`  
  Load '28_LVBus374028_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374089_consumption`  
  Load '28_LVBus374089_consumption' has phase imbalance of 285.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373813_consumption`  
  Load '28_LVBus373813_consumption' has phase imbalance of 73.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373922_consumption`  
  Load '28_LVBus373922_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374023_consumption`  
  Load '28_LVBus374023_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374063_consumption`  
  Load '28_LVBus374063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373839_consumption`  
  Load '28_LVBus373839_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373950_consumption`  
  Load '28_LVBus373950_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373810_consumption`  
  Load '28_LVBus373810_consumption' has phase imbalance of 53.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus975383_consumption`  
  Load '28_LVBus975383_consumption' has phase imbalance of 212.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373996_consumption`  
  Load '28_LVBus373996_consumption' has phase imbalance of 21.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374004_consumption`  
  Load '28_LVBus374004_consumption' has phase imbalance of 128.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374006_consumption`  
  Load '28_LVBus374006_consumption' has phase imbalance of 147.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373877_consumption`  
  Load '28_LVBus373877_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374067_consumption`  
  Load '28_LVBus374067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374093_consumption`  
  Load '28_LVBus374093_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373831_consumption`  
  Load '28_LVBus373831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373998_consumption`  
  Load '28_LVBus373998_consumption' has phase imbalance of 136.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374105_consumption`  
  Load '28_LVBus374105_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373899_consumption`  
  Load '28_LVBus373899_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373893_consumption`  
  Load '28_LVBus373893_consumption' has phase imbalance of 21.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373837_consumption`  
  Load '28_LVBus373837_consumption' has phase imbalance of 187.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374116_consumption`  
  Load '28_LVBus374116_consumption' has phase imbalance of 194.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374076_consumption`  
  Load '28_LVBus374076_consumption' has phase imbalance of 99.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373960_consumption`  
  Load '28_LVBus373960_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373952_consumption`  
  Load '28_LVBus373952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374115_consumption`  
  Load '28_LVBus374115_consumption' has phase imbalance of 98.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374020_consumption`  
  Load '28_LVBus374020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373941_consumption`  
  Load '28_LVBus373941_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374101_consumption`  
  Load '28_LVBus374101_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374052_consumption`  
  Load '28_LVBus374052_consumption' has phase imbalance of 24.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374036_consumption`  
  Load '28_LVBus374036_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374147_consumption`  
  Load '28_LVBus374147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373866_consumption`  
  Load '28_LVBus373866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373869_consumption`  
  Load '28_LVBus373869_consumption' has phase imbalance of 56.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374151_consumption`  
  Load '28_LVBus374151_consumption' has phase imbalance of 279.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373800_consumption`  
  Load '28_LVBus373800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374083_consumption`  
  Load '28_LVBus374083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373789_consumption`  
  Load '28_LVBus373789_consumption' has phase imbalance of 296.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373906_consumption`  
  Load '28_LVBus373906_consumption' has phase imbalance of 54.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373848_consumption`  
  Load '28_LVBus373848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374094_consumption`  
  Load '28_LVBus374094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373884_consumption`  
  Load '28_LVBus373884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373935_consumption`  
  Load '28_LVBus373935_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374138_consumption`  
  Load '28_LVBus374138_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374002_consumption`  
  Load '28_LVBus374002_consumption' has phase imbalance of 142.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374061_consumption`  
  Load '28_LVBus374061_consumption' has phase imbalance of 236.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373979_consumption`  
  Load '28_LVBus373979_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373956_consumption`  
  Load '28_LVBus373956_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373917_consumption`  
  Load '28_LVBus373917_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374086_consumption`  
  Load '28_LVBus374086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373923_consumption`  
  Load '28_LVBus373923_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373940_consumption`  
  Load '28_LVBus373940_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373909_consumption`  
  Load '28_LVBus373909_consumption' has phase imbalance of 141.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373958_consumption`  
  Load '28_LVBus373958_consumption' has phase imbalance of 30.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374074_consumption`  
  Load '28_LVBus374074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373920_consumption`  
  Load '28_LVBus373920_consumption' has phase imbalance of 87.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374157_consumption`  
  Load '28_LVBus374157_consumption' has phase imbalance of 268.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374144_consumption`  
  Load '28_LVBus374144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373945_consumption`  
  Load '28_LVBus373945_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374113_consumption`  
  Load '28_LVBus374113_consumption' has phase imbalance of 82.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373845_consumption`  
  Load '28_LVBus373845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374125_consumption`  
  Load '28_LVBus374125_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374042_consumption`  
  Load '28_LVBus374042_consumption' has phase imbalance of 32.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374043_consumption`  
  Load '28_LVBus374043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373902_consumption`  
  Load '28_LVBus373902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374018_consumption`  
  Load '28_LVBus374018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374082_consumption`  
  Load '28_LVBus374082_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374007_consumption`  
  Load '28_LVBus374007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373803_consumption`  
  Load '28_LVBus373803_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374010_consumption`  
  Load '28_LVBus374010_consumption' has phase imbalance of 98.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373976_consumption`  
  Load '28_LVBus373976_consumption' has phase imbalance of 133.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373775_consumption`  
  Load '28_LVBus373775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374091_consumption`  
  Load '28_LVBus374091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373883_consumption`  
  Load '28_LVBus373883_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374107_consumption`  
  Load '28_LVBus374107_consumption' has phase imbalance of 244.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897629_consumption`  
  Load '28_LVBus897629_consumption' has phase imbalance of 79.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374016_consumption`  
  Load '28_LVBus374016_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373965_consumption`  
  Load '28_LVBus373965_consumption' has phase imbalance of 238.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373841_consumption`  
  Load '28_LVBus373841_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374136_consumption`  
  Load '28_LVBus374136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373987_consumption`  
  Load '28_LVBus373987_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373859_consumption`  
  Load '28_LVBus373859_consumption' has phase imbalance of 135.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374137_consumption`  
  Load '28_LVBus374137_consumption' has phase imbalance of 218.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373967_consumption`  
  Load '28_LVBus373967_consumption' has phase imbalance of 97.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374122_consumption`  
  Load '28_LVBus374122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373910_consumption`  
  Load '28_LVBus373910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373948_consumption`  
  Load '28_LVBus373948_consumption' has phase imbalance of 220.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374022_consumption`  
  Load '28_LVBus374022_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373911_consumption`  
  Load '28_LVBus373911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374118_consumption`  
  Load '28_LVBus374118_consumption' has phase imbalance of 127.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373871_consumption`  
  Load '28_LVBus373871_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374134_consumption`  
  Load '28_LVBus374134_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374131_consumption`  
  Load '28_LVBus374131_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373912_consumption`  
  Load '28_LVBus373912_consumption' has phase imbalance of 212.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373778_consumption`  
  Load '28_LVBus373778_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374140_consumption`  
  Load '28_LVBus374140_consumption' has phase imbalance of 24.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373886_consumption`  
  Load '28_LVBus373886_consumption' has phase imbalance of 116.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373802_consumption`  
  Load '28_LVBus373802_consumption' has phase imbalance of 148.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373949_consumption`  
  Load '28_LVBus373949_consumption' has phase imbalance of 26.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373812_consumption`  
  Load '28_LVBus373812_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373986_consumption`  
  Load '28_LVBus373986_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374159_consumption`  
  Load '28_LVBus374159_consumption' has phase imbalance of 43.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373978_consumption`  
  Load '28_LVBus373978_consumption' has phase imbalance of 220.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373968_consumption`  
  Load '28_LVBus373968_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373850_consumption`  
  Load '28_LVBus373850_consumption' has phase imbalance of 142.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373856_consumption`  
  Load '28_LVBus373856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373777_consumption`  
  Load '28_LVBus373777_consumption' has phase imbalance of 204.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373934_consumption`  
  Load '28_LVBus373934_consumption' has phase imbalance of 128.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374015_consumption`  
  Load '28_LVBus374015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373811_consumption`  
  Load '28_LVBus373811_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373971_consumption`  
  Load '28_LVBus373971_consumption' has phase imbalance of 137.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373972_consumption`  
  Load '28_LVBus373972_consumption' has phase imbalance of 58.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus975379_consumption`  
  Load '28_LVBus975379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373944_consumption`  
  Load '28_LVBus373944_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374037_consumption`  
  Load '28_LVBus374037_consumption' has phase imbalance of 155.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373879_consumption`  
  Load '28_LVBus373879_consumption' has phase imbalance of 234.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373994_consumption`  
  Load '28_LVBus373994_consumption' has phase imbalance of 134.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374027_consumption`  
  Load '28_LVBus374027_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373876_consumption`  
  Load '28_LVBus373876_consumption' has phase imbalance of 233.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374059_consumption`  
  Load '28_LVBus374059_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374032_consumption`  
  Load '28_LVBus374032_consumption' has phase imbalance of 224.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374095_consumption`  
  Load '28_LVBus374095_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373953_consumption`  
  Load '28_LVBus373953_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373894_consumption`  
  Load '28_LVBus373894_consumption' has phase imbalance of 244.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373901_consumption`  
  Load '28_LVBus373901_consumption' has phase imbalance of 257.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373995_consumption`  
  Load '28_LVBus373995_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373814_consumption`  
  Load '28_LVBus373814_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374167_consumption`  
  Load '28_LVBus374167_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373878_consumption`  
  Load '28_LVBus373878_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373851_consumption`  
  Load '28_LVBus373851_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373992_consumption`  
  Load '28_LVBus373992_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374054_consumption`  
  Load '28_LVBus374054_consumption' has phase imbalance of 282.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374065_consumption`  
  Load '28_LVBus374065_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373939_consumption`  
  Load '28_LVBus373939_consumption' has phase imbalance of 206.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374149_consumption`  
  Load '28_LVBus374149_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373988_consumption`  
  Load '28_LVBus373988_consumption' has phase imbalance of 232.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373858_consumption`  
  Load '28_LVBus373858_consumption' has phase imbalance of 42.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373896_consumption`  
  Load '28_LVBus373896_consumption' has phase imbalance of 189.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374110_consumption`  
  Load '28_LVBus374110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373900_consumption`  
  Load '28_LVBus373900_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373862_consumption`  
  Load '28_LVBus373862_consumption' has phase imbalance of 190.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374072_consumption`  
  Load '28_LVBus374072_consumption' has phase imbalance of 269.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374104_consumption`  
  Load '28_LVBus374104_consumption' has phase imbalance of 211.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374096_consumption`  
  Load '28_LVBus374096_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374071_consumption`  
  Load '28_LVBus374071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374040_consumption`  
  Load '28_LVBus374040_consumption' has phase imbalance of 98.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373784_consumption`  
  Load '28_LVBus373784_consumption' has phase imbalance of 39.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373797_consumption`  
  Load '28_LVBus373797_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373840_consumption`  
  Load '28_LVBus373840_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373921_consumption`  
  Load '28_LVBus373921_consumption' has phase imbalance of 273.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373828_consumption`  
  Load '28_LVBus373828_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374044_consumption`  
  Load '28_LVBus374044_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373852_consumption`  
  Load '28_LVBus373852_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374098_consumption`  
  Load '28_LVBus374098_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374031_consumption`  
  Load '28_LVBus374031_consumption' has phase imbalance of 261.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374112_consumption`  
  Load '28_LVBus374112_consumption' has phase imbalance of 87.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373870_consumption`  
  Load '28_LVBus373870_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373790_consumption`  
  Load '28_LVBus373790_consumption' has phase imbalance of 64.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374003_consumption`  
  Load '28_LVBus374003_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374041_consumption`  
  Load '28_LVBus374041_consumption' has phase imbalance of 254.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374057_consumption`  
  Load '28_LVBus374057_consumption' has phase imbalance of 251.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374026_consumption`  
  Load '28_LVBus374026_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373970_consumption`  
  Load '28_LVBus373970_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373885_consumption`  
  Load '28_LVBus373885_consumption' has phase imbalance of 239.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373908_consumption`  
  Load '28_LVBus373908_consumption' has phase imbalance of 231.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373926_consumption`  
  Load '28_LVBus373926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374034_consumption`  
  Load '28_LVBus374034_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373880_consumption`  
  Load '28_LVBus373880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373936_consumption`  
  Load '28_LVBus373936_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373983_consumption`  
  Load '28_LVBus373983_consumption' has phase imbalance of 185.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373938_consumption`  
  Load '28_LVBus373938_consumption' has phase imbalance of 41.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373798_consumption`  
  Load '28_LVBus373798_consumption' has phase imbalance of 21.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373830_consumption`  
  Load '28_LVBus373830_consumption' has phase imbalance of 164.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373984_consumption`  
  Load '28_LVBus373984_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374120_consumption`  
  Load '28_LVBus374120_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374017_consumption`  
  Load '28_LVBus374017_consumption' has phase imbalance of 278.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373821_consumption`  
  Load '28_LVBus373821_consumption' has phase imbalance of 212.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373989_consumption`  
  Load '28_LVBus373989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373835_consumption`  
  Load '28_LVBus373835_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374008_consumption`  
  Load '28_LVBus374008_consumption' has phase imbalance of 28.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus373873_consumption`  
  Load '28_LVBus373873_consumption' has phase imbalance of 181.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374084_consumption`  
  Load '28_LVBus374084_consumption' has phase imbalance of 86.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374090_consumption`  
  Load '28_LVBus374090_consumption' has phase imbalance of 118.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374064_consumption`  
  Load '28_LVBus374064_consumption' has phase imbalance of 186.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374050_consumption`  
  Load '28_LVBus374050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus374166_consumption`  
  Load '28_LVBus374166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 620 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '28_LVBus373783' (LV, 0.24 kV) has an electrical reach of 1.12 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus373854' (LV, 0.24 kV) has an electrical reach of 13.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  445 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '28_116382' and '28_122944' at bus '28_MVBus31224' have ||Z||_F ratio 1290.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  134 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus373775_consumption, 28_LVBus373776_consumption, 28_LVBus373777_consumption, 28_LVBus373783_consumption, 28_LVBus373785_consumption, 28_LVBus373789_consumption, 28_LVBus373791_consumption, 28_LVBus373800_consumption, 28_LVBus373803_consumption, 28_LVBus373807_consumption, 28_LVBus373812_consumption, 28_LVBus373814_consumption, 28_LVBus373818_consumption, 28_LVBus373830_consumption, 28_LVBus373831_consumption, 28_LVBus373835_consumption, 28_LVBus373839_consumption, 28_LVBus373840_consumption, 28_LVBus373841_consumption, 28_LVBus373842_consumption, 28_LVBus373843_consumption, 28_LVBus373845_consumption, 28_LVBus373846_consumption, 28_LVBus373848_consumption, 28_LVBus373851_consumption, 28_LVBus373854_consumption, 28_LVBus373856_consumption, 28_LVBus373857_consumption, 28_LVBus373862_consumption, 28_LVBus373864_consumption, 28_LVBus373866_consumption, 28_LVBus373870_consumption, 28_LVBus373876_consumption, 28_LVBus373877_consumption, 28_LVBus373878_consumption, 28_LVBus373879_consumption, 28_LVBus373880_consumption, 28_LVBus373883_consumption, 28_LVBus373884_consumption, 28_LVBus373894_consumption, 28_LVBus373896_consumption, 28_LVBus373899_consumption, 28_LVBus373901_consumption, 28_LVBus373902_consumption, 28_LVBus373908_consumption, 28_LVBus373910_consumption, 28_LVBus373911_consumption, 28_LVBus373912_consumption, 28_LVBus373921_consumption, 28_LVBus373922_consumption, 28_LVBus373926_consumption, 28_LVBus373936_consumption, 28_LVBus373939_consumption, 28_LVBus373940_consumption, 28_LVBus373944_consumption, 28_LVBus373948_consumption, 28_LVBus373950_consumption, 28_LVBus373952_consumption, 28_LVBus373953_consumption, 28_LVBus373957_consumption, 28_LVBus373959_consumption, 28_LVBus373962_consumption, 28_LVBus373968_consumption, 28_LVBus373969_consumption, 28_LVBus373970_consumption, 28_LVBus373978_consumption, 28_LVBus373983_consumption, 28_LVBus373986_consumption, 28_LVBus373987_consumption, 28_LVBus373988_consumption, 28_LVBus373989_consumption, 28_LVBus373991_consumption, 28_LVBus373992_consumption, 28_LVBus374005_consumption, 28_LVBus374007_consumption, 28_LVBus374009_consumption, 28_LVBus374012_consumption, 28_LVBus374015_consumption, 28_LVBus374017_consumption, 28_LVBus374018_consumption, 28_LVBus374020_consumption, 28_LVBus374023_consumption, 28_LVBus374030_consumption, 28_LVBus374037_consumption, 28_LVBus374041_consumption, 28_LVBus374043_consumption, 28_LVBus374046_consumption, 28_LVBus374050_consumption, 28_LVBus374054_consumption, 28_LVBus374055_consumption, 28_LVBus374057_consumption, 28_LVBus374059_consumption, 28_LVBus374061_consumption, 28_LVBus374063_consumption, 28_LVBus374064_consumption, 28_LVBus374065_consumption, 28_LVBus374066_consumption, 28_LVBus374067_consumption, 28_LVBus374071_consumption, 28_LVBus374072_consumption, 28_LVBus374073_consumption, 28_LVBus374074_consumption, 28_LVBus374083_consumption, 28_LVBus374085_consumption, 28_LVBus374086_consumption, 28_LVBus374088_consumption, 28_LVBus374089_consumption, 28_LVBus374091_consumption, 28_LVBus374093_consumption, 28_LVBus374094_consumption, 28_LVBus374095_consumption, 28_LVBus374096_consumption, 28_LVBus374098_consumption, 28_LVBus374101_consumption, 28_LVBus374102_consumption, 28_LVBus374105_consumption, 28_LVBus374110_consumption, 28_LVBus374116_consumption, 28_LVBus374120_consumption, 28_LVBus374122_consumption, 28_LVBus374134_consumption, 28_LVBus374136_consumption, 28_LVBus374144_consumption, 28_LVBus374147_consumption, 28_LVBus374151_consumption, 28_LVBus374153_consumption, 28_LVBus374157_consumption, 28_LVBus374160_consumption, 28_LVBus374163_consumption, 28_LVBus374166_consumption, 28_LVBus374167_consumption, 28_LVBus975379_consumption, 28_LVBus975383_consumption, 28_LVBus975385_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  310 group(s) of loads (620 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  15 group(s) of series lines (31 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  361 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus373774_consumption, 28_LVBus373774_production, 28_LVBus373775_production, 28_LVBus373776_production, 28_LVBus373777_production, 28_LVBus373778_production, 28_LVBus373779_consumption, 28_LVBus373779_production, 28_LVBus373783_production, 28_LVBus373784_production, 28_LVBus373785_production, 28_LVBus373786_production, 28_LVBus373788_consumption, 28_LVBus373788_production, 28_LVBus373789_production, 28_LVBus373790_production, 28_LVBus373791_production, 28_LVBus373793_production, 28_LVBus373794_consumption, 28_LVBus373794_production, 28_LVBus373795_consumption, 28_LVBus373795_production, 28_LVBus373796_consumption, 28_LVBus373796_production, 28_LVBus373797_production, 28_LVBus373798_production, 28_LVBus373799_production, 28_LVBus373800_production, 28_LVBus373802_production, 28_LVBus373803_production, 28_LVBus373804_production, 28_LVBus373806_consumption, 28_LVBus373806_production, 28_LVBus373807_production, 28_LVBus373809_consumption, 28_LVBus373809_production, 28_LVBus373810_production, 28_LVBus373811_production, 28_LVBus373812_production, 28_LVBus373813_production, 28_LVBus373814_production, 28_LVBus373816_consumption, 28_LVBus373816_production, 28_LVBus373817_consumption, 28_LVBus373817_production, 28_LVBus373818_production, 28_LVBus373820_production, 28_LVBus373821_production, 28_LVBus373822_consumption, 28_LVBus373822_production, 28_LVBus373826_consumption, 28_LVBus373826_production, 28_LVBus373827_production, 28_LVBus373828_production, 28_LVBus373829_consumption, 28_LVBus373829_production, 28_LVBus373830_production, 28_LVBus373831_production, 28_LVBus373833_production, 28_LVBus373835_production, 28_LVBus373837_production, 28_LVBus373839_production, 28_LVBus373840_production, 28_LVBus373841_production, 28_LVBus373842_production, 28_LVBus373843_production, 28_LVBus373844_consumption, 28_LVBus373844_production, 28_LVBus373845_production, 28_LVBus373846_production, 28_LVBus373847_production, 28_LVBus373848_production, 28_LVBus373850_production, 28_LVBus373851_production, 28_LVBus373852_production, 28_LVBus373854_production, 28_LVBus373856_production, 28_LVBus373857_production, 28_LVBus373858_production, 28_LVBus373859_production, 28_LVBus373861_consumption, 28_LVBus373861_production, 28_LVBus373862_production, 28_LVBus373863_consumption, 28_LVBus373863_production, 28_LVBus373864_production, 28_LVBus373866_production, 28_LVBus373867_production, 28_LVBus373868_production, 28_LVBus373869_production, 28_LVBus373870_production, 28_LVBus373871_production, 28_LVBus373872_consumption, 28_LVBus373872_production, 28_LVBus373873_production, 28_LVBus373875_consumption, 28_LVBus373875_production, 28_LVBus373876_production, 28_LVBus373877_production, 28_LVBus373878_production, 28_LVBus373879_production, 28_LVBus373880_production, 28_LVBus373883_production, 28_LVBus373884_production, 28_LVBus373885_production, 28_LVBus373886_production, 28_LVBus373887_consumption, 28_LVBus373887_production, 28_LVBus373892_production, 28_LVBus373893_production, 28_LVBus373894_production, 28_LVBus373895_production, 28_LVBus373896_production, 28_LVBus373898_production, 28_LVBus373899_production, 28_LVBus373900_production, 28_LVBus373901_production, 28_LVBus373902_production, 28_LVBus373904_production, 28_LVBus373906_production, 28_LVBus373908_production, 28_LVBus373909_production, 28_LVBus373910_production, 28_LVBus373911_production, 28_LVBus373912_production, 28_LVBus373914_production, 28_LVBus373916_consumption, 28_LVBus373916_production, 28_LVBus373917_production, 28_LVBus373919_consumption, 28_LVBus373919_production, 28_LVBus373920_production, 28_LVBus373921_production, 28_LVBus373922_production, 28_LVBus373923_production, 28_LVBus373924_consumption, 28_LVBus373924_production, 28_LVBus373925_consumption, 28_LVBus373925_production, 28_LVBus373926_production, 28_LVBus373927_production, 28_LVBus373929_production, 28_LVBus373933_consumption, 28_LVBus373933_production, 28_LVBus373934_production, 28_LVBus373935_production, 28_LVBus373936_production, 28_LVBus373938_production, 28_LVBus373939_production, 28_LVBus373940_production, 28_LVBus373941_production, 28_LVBus373942_consumption, 28_LVBus373942_production, 28_LVBus373944_production, 28_LVBus373945_production, 28_LVBus373947_consumption, 28_LVBus373947_production, 28_LVBus373948_production, 28_LVBus373949_production, 28_LVBus373950_production, 28_LVBus373951_consumption, 28_LVBus373951_production, 28_LVBus373952_production, 28_LVBus373953_production, 28_LVBus373955_production, 28_LVBus373956_production, 28_LVBus373957_production, 28_LVBus373958_production, 28_LVBus373959_production, 28_LVBus373960_production, 28_LVBus373962_production, 28_LVBus373963_consumption, 28_LVBus373963_production, 28_LVBus373964_production, 28_LVBus373965_production, 28_LVBus373967_production, 28_LVBus373968_production, 28_LVBus373969_production, 28_LVBus373970_production, 28_LVBus373971_production, 28_LVBus373972_production, 28_LVBus373976_production, 28_LVBus373977_consumption, 28_LVBus373977_production, 28_LVBus373978_production, 28_LVBus373979_production, 28_LVBus373980_production, 28_LVBus373982_production, 28_LVBus373983_production, 28_LVBus373984_production, 28_LVBus373986_production, 28_LVBus373987_production, 28_LVBus373988_production, 28_LVBus373989_production, 28_LVBus373990_consumption, 28_LVBus373990_production, 28_LVBus373991_production, 28_LVBus373992_production, 28_LVBus373994_production, 28_LVBus373995_production, 28_LVBus373996_production, 28_LVBus373997_production, 28_LVBus373998_production, 28_LVBus374002_production, 28_LVBus374003_production, 28_LVBus374004_production, 28_LVBus374005_production, 28_LVBus374006_production, 28_LVBus374007_production, 28_LVBus374008_production, 28_LVBus374009_production, 28_LVBus374010_production, 28_LVBus374012_production, 28_LVBus374013_consumption, 28_LVBus374013_production, 28_LVBus374014_production, 28_LVBus374015_production, 28_LVBus374016_production, 28_LVBus374017_production, 28_LVBus374018_production, 28_LVBus374020_production, 28_LVBus374021_production, 28_LVBus374022_production, 28_LVBus374023_production, 28_LVBus374024_production, 28_LVBus374026_production, 28_LVBus374027_production, 28_LVBus374028_production, 28_LVBus374030_production, 28_LVBus374031_production, 28_LVBus374032_production, 28_LVBus374033_consumption, 28_LVBus374033_production, 28_LVBus374034_production, 28_LVBus374036_production, 28_LVBus374037_production, 28_LVBus374038_production, 28_LVBus374040_production, 28_LVBus374041_production, 28_LVBus374042_production, 28_LVBus374043_production, 28_LVBus374044_production, 28_LVBus374045_consumption, 28_LVBus374045_production, 28_LVBus374046_production, 28_LVBus374048_production, 28_LVBus374050_production, 28_LVBus374052_production, 28_LVBus374054_production, 28_LVBus374055_production, 28_LVBus374057_production, 28_LVBus374058_production, 28_LVBus374059_production, 28_LVBus374061_production, 28_LVBus374062_production, 28_LVBus374063_production, 28_LVBus374064_production, 28_LVBus374065_production, 28_LVBus374066_production, 28_LVBus374067_production, 28_LVBus374069_production, 28_LVBus374071_production, 28_LVBus374072_production, 28_LVBus374073_production, 28_LVBus374074_production, 28_LVBus374076_production, 28_LVBus374080_consumption, 28_LVBus374080_production, 28_LVBus374081_consumption, 28_LVBus374081_production, 28_LVBus374082_production, 28_LVBus374083_production, 28_LVBus374084_production, 28_LVBus374085_production, 28_LVBus374086_production, 28_LVBus374088_production, 28_LVBus374089_production, 28_LVBus374090_production, 28_LVBus374091_production, 28_LVBus374092_consumption, 28_LVBus374092_production, 28_LVBus374093_production, 28_LVBus374094_production, 28_LVBus374095_production, 28_LVBus374096_production, 28_LVBus374097_consumption, 28_LVBus374097_production, 28_LVBus374098_production, 28_LVBus374100_consumption, 28_LVBus374100_production, 28_LVBus374101_production, 28_LVBus374102_production, 28_LVBus374104_production, 28_LVBus374105_production, 28_LVBus374107_production, 28_LVBus374108_production, 28_LVBus374110_production, 28_LVBus374112_production, 28_LVBus374113_production, 28_LVBus374115_production, 28_LVBus374116_production, 28_LVBus374117_consumption, 28_LVBus374117_production, 28_LVBus374118_production, 28_LVBus374120_production, 28_LVBus374121_production, 28_LVBus374122_production, 28_LVBus374124_consumption, 28_LVBus374124_production, 28_LVBus374125_production, 28_LVBus374131_production, 28_LVBus374132_production, 28_LVBus374133_consumption, 28_LVBus374133_production, 28_LVBus374134_production, 28_LVBus374135_production, 28_LVBus374136_production, 28_LVBus374137_production, 28_LVBus374138_production, 28_LVBus374140_production, 28_LVBus374142_production, 28_LVBus374143_production, 28_LVBus374144_production, 28_LVBus374146_consumption, 28_LVBus374146_production, 28_LVBus374147_production, 28_LVBus374148_consumption, 28_LVBus374148_production, 28_LVBus374149_production, 28_LVBus374150_consumption, 28_LVBus374150_production, 28_LVBus374151_production, 28_LVBus374152_production, 28_LVBus374153_production, 28_LVBus374157_production, 28_LVBus374158_production, 28_LVBus374159_production, 28_LVBus374160_production, 28_LVBus374162_production, 28_LVBus374163_production, 28_LVBus374165_consumption, 28_LVBus374165_production, 28_LVBus374166_production, 28_LVBus374167_production, 28_LVBus897629_production, 28_LVBus975379_production, 28_LVBus975380_consumption, 28_LVBus975380_production, 28_LVBus975381_consumption, 28_LVBus975381_production, 28_LVBus975382_consumption, 28_LVBus975382_production, 28_LVBus975383_production, 28_LVBus975384_production, 28_LVBus975385_production, 28_MVLV20246_consumption, 28_MVLV20246_production, 28_MVLV70731_consumption, 28_MVLV70731_production, 28_MVLV74352_consumption, 28_MVLV74352_production.

