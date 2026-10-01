# BMOPF Network Summary: 93_MVFeeder2759

**Generated:** 2026-10-01 23:34:51  
**Findings:** 0 errors · 5 warnings · 259 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 492 |  |
| line | 475 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 916 | 2.977 MW, 893.2 kvar |
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
| MV_11.8kV | 11.78 kV | 28 | 27 | 20 | 0 |
| LV_236V | 236.0 V | 464 | 448 | 896 | 0 |

**Transformer transitions:**

- `93_MVLV67180_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV04945_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV48026_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV42111_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV55676_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV07266_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV49832_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV02937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV62128_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV28840_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV43128_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV29542_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV10622_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV25042_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV02202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV10081_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 217 |
| Tree depth (max hops) | 31 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 492 | 1 | 491 | 0 | 0 | 0 |
| Tier LV_236V | 464 | 16 | 448 | 0 | 0 | 0 |
| Tier MV_11.8kV | 28 | 1 | 27 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 16; skipped invalid branches: 0.

Galvanic zones: 17; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 93_MVBus38498 | MV_11.8kV | 28 | 0 | 0 | 16 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1940 declared bus terminals; 1873 mapped line/closed-switch conductor edges; 67 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 86500.0 | 3.865 | 2748 |
| q_nom | 0.0 | 25900.0 | 3.865 | 2748 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.31 | 1930.0 | 2.229 | 475 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.434 | 16 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 629 of 916 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107036_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106705_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106952_consumption' has phase imbalance of 96.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107051_consumption' has phase imbalance of 170.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106816_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106806_consumption' has phase imbalance of 114.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106914_consumption' has phase imbalance of 219.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107058_consumption' has phase imbalance of 207.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106889_consumption' has phase imbalance of 28.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106969_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106861_consumption' has phase imbalance of 170.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106735_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106679_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106738_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107029_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106800_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106822_consumption' has phase imbalance of 69.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106612_consumption' has phase imbalance of 238.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106690_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106702_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107065_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106874_consumption' has phase imbalance of 94.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106726_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106616_consumption' has phase imbalance of 114.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106843_consumption' has phase imbalance of 108.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106887_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106725_consumption' has phase imbalance of 181.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106818_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106836_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107061_consumption' has phase imbalance of 81.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106637_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106860_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106687_consumption' has phase imbalance of 64.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106631_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106871_consumption' has phase imbalance of 205.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106794_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106694_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106968_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106918_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106980_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106910_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106973_consumption' has phase imbalance of 125.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106620_consumption' has phase imbalance of 237.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106921_consumption' has phase imbalance of 216.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106875_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106615_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106688_consumption' has phase imbalance of 132.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106838_consumption' has phase imbalance of 218.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106807_consumption' has phase imbalance of 96.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106850_consumption' has phase imbalance of 280.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106844_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106811_consumption' has phase imbalance of 223.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106863_consumption' has phase imbalance of 222.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106894_consumption' has phase imbalance of 204.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106841_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106792_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106805_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107031_consumption' has phase imbalance of 27.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106898_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106907_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106658_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107035_consumption' has phase imbalance of 88.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106880_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106731_consumption' has phase imbalance of 275.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106808_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106846_consumption' has phase imbalance of 236.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106704_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106673_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106826_consumption' has phase imbalance of 92.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106963_consumption' has phase imbalance of 55.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106886_consumption' has phase imbalance of 206.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106972_consumption' has phase imbalance of 58.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106669_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106920_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106905_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106737_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106922_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107059_consumption' has phase imbalance of 263.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106902_consumption' has phase imbalance of 228.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106802_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107067_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106870_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107055_consumption' has phase imbalance of 278.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106740_consumption' has phase imbalance of 200.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106647_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106859_consumption' has phase imbalance of 257.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106862_consumption' has phase imbalance of 221.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106899_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106825_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106906_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107056_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106953_consumption' has phase imbalance of 46.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106821_consumption' has phase imbalance of 22.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106912_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106722_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106710_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106736_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106700_consumption' has phase imbalance of 137.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106845_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106695_consumption' has phase imbalance of 236.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106996_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106770_consumption' has phase imbalance of 47.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106987_consumption' has phase imbalance of 52.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106839_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106872_consumption' has phase imbalance of 72.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106854_consumption' has phase imbalance of 230.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106743_consumption' has phase imbalance of 87.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106801_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106932_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106917_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106733_consumption' has phase imbalance of 252.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106919_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106613_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106923_consumption' has phase imbalance of 60.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107034_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106885_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107053_consumption' has phase imbalance of 216.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106835_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106734_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106723_consumption' has phase imbalance of 75.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106677_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106798_consumption' has phase imbalance of 236.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107033_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106742_consumption' has phase imbalance of 59.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106950_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106876_consumption' has phase imbalance of 57.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106820_consumption' has phase imbalance of 275.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106713_consumption' has phase imbalance of 246.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106810_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106711_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106622_consumption' has phase imbalance of 289.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106903_consumption' has phase imbalance of 212.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106971_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106877_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106707_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106834_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107063_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106626_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106714_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106809_consumption' has phase imbalance of 266.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106892_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106685_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106951_consumption' has phase imbalance of 198.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106610_consumption' has phase imbalance of 137.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106691_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106636_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106986_consumption' has phase imbalance of 43.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106632_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106724_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106672_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106893_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106625_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106732_consumption' has phase imbalance of 215.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106799_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106994_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106727_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106891_consumption' has phase imbalance of 129.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106916_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106851_consumption' has phase imbalance of 211.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106712_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106678_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106814_consumption' has phase imbalance of 22.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106706_consumption' has phase imbalance of 239.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106878_consumption' has phase imbalance of 211.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106718_consumption' has phase imbalance of 114.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106873_consumption' has phase imbalance of 269.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106796_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106759_consumption' has phase imbalance of 256.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106676_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106852_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106881_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106819_consumption' has phase imbalance of 187.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106824_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107054_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106670_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106728_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106900_consumption' has phase imbalance of 245.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106982_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106668_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106671_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106715_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1107027_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1106962_consumption' has phase imbalance of 47.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 916 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus1107101' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus1107070' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_VITRO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus1106977' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.977 MW |
| Total load Q | 893.2 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 93_MVLV67180_Transformer | 440.0 kVA | 40.7% |
| 93_MVLV04945_Transformer | 275.0 kVA | 73.1% |
| 93_MVLV48026_Transformer | 110.0 kVA | 32.7% |
| 93_MVLV42111_Transformer | 275.0 kVA | 26.3% |
| 93_MVLV55676_Transformer | 176.0 kVA | 70.6% |
| 93_MVLV07266_Transformer | 440.0 kVA | 52.4% |
| 93_MVLV49832_Transformer | 176.0 kVA | 46.1% |
| 93_MVLV02937_Transformer | 440.0 kVA | 35.5% |
| 93_MVLV62128_Transformer | 275.0 kVA | 30.5% |
| 93_MVLV28840_Transformer | 275.0 kVA | 56.3% |
| 93_MVLV43128_Transformer | 275.0 kVA | 84.7% |
| 93_MVLV29542_Transformer | 693.0 kVA | 65.2% |
| 93_MVLV10622_Transformer | 440.0 kVA | 41.9% |
| 93_MVLV25042_Transformer | 346.5 kVA | 81.7% |
| 93_MVLV02202_Transformer | 275.0 kVA | 50.9% |
| 93_MVLV10081_Transformer | 275.0 kVA | 31.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.98 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '93_LVBus1106977' (LV, 0.24 kV) has an electrical reach of 9.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 492 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 492 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 28 |
| LV_236V | 4-wire | 464 / 464 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 464 |
| Neutral branches | 448 |
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
| 11.78 kV | 28 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 46 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 65 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 66 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 623.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 464 / 28 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 630 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 630 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus1106605_consumption, 93_LVBus1106605_production, 93_LVBus1106606_production, 93_LVBus1106607_production, 93_LVBus1106608_consumption, 93_LVBus1106608_production, 93_LVBus1106609_production, 93_LVBus1106610_production, 93_LVBus1106611_production, 93_LVBus1106612_production, 93_LVBus1106613_production, 93_LVBus1106615_production, 93_LVBus1106616_production, 93_LVBus1106617_consumption, 93_LVBus1106617_production, 93_LVBus1106619_production, 93_LVBus1106620_production, 93_LVBus1106621_consumption, 93_LVBus1106621_production, 93_LVBus1106622_production, 93_LVBus1106623_production, 93_LVBus1106625_production, 93_LVBus1106626_production, 93_LVBus1106628_consumption, 93_LVBus1106628_production, 93_LVBus1106630_consumption, 93_LVBus1106630_production, 93_LVBus1106631_production, 93_LVBus1106632_production, 93_LVBus1106633_consumption, 93_LVBus1106633_production, 93_LVBus1106634_production, 93_LVBus1106635_production, 93_LVBus1106636_production, 93_LVBus1106637_production, 93_LVBus1106639_consumption, 93_LVBus1106639_production, 93_LVBus1106641_production, 93_LVBus1106642_production, 93_LVBus1106643_consumption, 93_LVBus1106643_production, 93_LVBus1106644_production, 93_LVBus1106646_consumption, 93_LVBus1106646_production, 93_LVBus1106647_production, 93_LVBus1106648_consumption, 93_LVBus1106648_production, 93_LVBus1106649_consumption, 93_LVBus1106649_production, 93_LVBus1106651_production, 93_LVBus1106652_consumption, 93_LVBus1106652_production, 93_LVBus1106653_production, 93_LVBus1106655_consumption, 93_LVBus1106655_production, 93_LVBus1106656_consumption, 93_LVBus1106656_production, 93_LVBus1106658_production, 93_LVBus1106659_consumption, 93_LVBus1106659_production, 93_LVBus1106661_consumption, 93_LVBus1106661_production, 93_LVBus1106663_consumption, 93_LVBus1106663_production, 93_LVBus1106665_production, 93_LVBus1106666_production, 93_LVBus1106667_consumption, 93_LVBus1106667_production, 93_LVBus1106668_production, 93_LVBus1106669_production, 93_LVBus1106670_production, 93_LVBus1106671_production, 93_LVBus1106672_production, 93_LVBus1106673_production, 93_LVBus1106674_consumption, 93_LVBus1106674_production, 93_LVBus1106676_production, 93_LVBus1106677_production, 93_LVBus1106678_production, 93_LVBus1106679_production, 93_LVBus1106680_consumption, 93_LVBus1106680_production, 93_LVBus1106681_production, 93_LVBus1106682_consumption, 93_LVBus1106682_production, 93_LVBus1106683_production, 93_LVBus1106684_production, 93_LVBus1106685_production, 93_LVBus1106686_production, 93_LVBus1106687_production, 93_LVBus1106688_production, 93_LVBus1106689_consumption, 93_LVBus1106689_production, 93_LVBus1106690_production, 93_LVBus1106691_production, 93_LVBus1106693_production, 93_LVBus1106694_production, 93_LVBus1106695_production, 93_LVBus1106697_consumption, 93_LVBus1106697_production, 93_LVBus1106698_consumption, 93_LVBus1106698_production, 93_LVBus1106699_production, 93_LVBus1106700_production, 93_LVBus1106701_production, 93_LVBus1106702_production, 93_LVBus1106703_production, 93_LVBus1106704_production, 93_LVBus1106705_production, 93_LVBus1106706_production, 93_LVBus1106707_production, 93_LVBus1106708_production, 93_LVBus1106709_production, 93_LVBus1106710_production, 93_LVBus1106711_production, 93_LVBus1106712_production, 93_LVBus1106713_production, 93_LVBus1106714_production, 93_LVBus1106715_production, 93_LVBus1106717_production, 93_LVBus1106718_production, 93_LVBus1106720_consumption, 93_LVBus1106720_production, 93_LVBus1106721_production, 93_LVBus1106722_production, 93_LVBus1106723_production, 93_LVBus1106724_production, 93_LVBus1106725_production, 93_LVBus1106726_production, 93_LVBus1106727_production, 93_LVBus1106728_production, 93_LVBus1106729_consumption, 93_LVBus1106729_production, 93_LVBus1106730_production, 93_LVBus1106731_production, 93_LVBus1106732_production, 93_LVBus1106733_production, 93_LVBus1106734_production, 93_LVBus1106735_production, 93_LVBus1106736_production, 93_LVBus1106737_production, 93_LVBus1106738_production, 93_LVBus1106740_production, 93_LVBus1106741_production, 93_LVBus1106742_production, 93_LVBus1106743_production, 93_LVBus1106745_production, 93_LVBus1106747_consumption, 93_LVBus1106747_production, 93_LVBus1106749_consumption, 93_LVBus1106749_production, 93_LVBus1106750_production, 93_LVBus1106751_production, 93_LVBus1106752_consumption, 93_LVBus1106752_production, 93_LVBus1106753_consumption, 93_LVBus1106753_production, 93_LVBus1106754_production, 93_LVBus1106755_consumption, 93_LVBus1106755_production, 93_LVBus1106756_consumption, 93_LVBus1106756_production, 93_LVBus1106757_production, 93_LVBus1106758_production, 93_LVBus1106759_production, 93_LVBus1106761_consumption, 93_LVBus1106761_production, 93_LVBus1106762_production, 93_LVBus1106764_production, 93_LVBus1106766_production, 93_LVBus1106767_consumption, 93_LVBus1106767_production, 93_LVBus1106768_production, 93_LVBus1106769_consumption, 93_LVBus1106769_production, 93_LVBus1106770_production, 93_LVBus1106771_consumption, 93_LVBus1106771_production, 93_LVBus1106772_production, 93_LVBus1106773_consumption, 93_LVBus1106773_production, 93_LVBus1106774_production, 93_LVBus1106776_consumption, 93_LVBus1106776_production, 93_LVBus1106777_consumption, 93_LVBus1106777_production, 93_LVBus1106778_production, 93_LVBus1106779_production, 93_LVBus1106780_production, 93_LVBus1106781_consumption, 93_LVBus1106781_production, 93_LVBus1106783_consumption, 93_LVBus1106783_production, 93_LVBus1106784_consumption, 93_LVBus1106784_production, 93_LVBus1106785_production, 93_LVBus1106787_consumption, 93_LVBus1106787_production, 93_LVBus1106789_consumption, 93_LVBus1106789_production, 93_LVBus1106791_production, 93_LVBus1106792_production, 93_LVBus1106793_production, 93_LVBus1106794_production, 93_LVBus1106795_production, 93_LVBus1106796_production, 93_LVBus1106797_production, 93_LVBus1106798_production, 93_LVBus1106799_production, 93_LVBus1106800_production, 93_LVBus1106801_production, 93_LVBus1106802_production, 93_LVBus1106804_consumption, 93_LVBus1106804_production, 93_LVBus1106805_production, 93_LVBus1106806_production, 93_LVBus1106807_production, 93_LVBus1106808_production, 93_LVBus1106809_production, 93_LVBus1106810_production, 93_LVBus1106811_production, 93_LVBus1106813_production, 93_LVBus1106814_production, 93_LVBus1106815_consumption, 93_LVBus1106815_production, 93_LVBus1106816_production, 93_LVBus1106818_production, 93_LVBus1106819_production, 93_LVBus1106820_production, 93_LVBus1106821_production, 93_LVBus1106822_production, 93_LVBus1106824_production, 93_LVBus1106825_production, 93_LVBus1106826_production, 93_LVBus1106827_production, 93_LVBus1106828_production, 93_LVBus1106830_consumption, 93_LVBus1106830_production, 93_LVBus1106831_consumption, 93_LVBus1106831_production, 93_LVBus1106832_consumption, 93_LVBus1106832_production, 93_LVBus1106833_production, 93_LVBus1106834_production, 93_LVBus1106835_production, 93_LVBus1106836_production, 93_LVBus1106838_production, 93_LVBus1106839_production, 93_LVBus1106841_production, 93_LVBus1106842_production, 93_LVBus1106843_production, 93_LVBus1106844_production, 93_LVBus1106845_production, 93_LVBus1106846_production, 93_LVBus1106848_production, 93_LVBus1106849_consumption, 93_LVBus1106849_production, 93_LVBus1106850_production, 93_LVBus1106851_production, 93_LVBus1106852_production, 93_LVBus1106853_production, 93_LVBus1106854_production, 93_LVBus1106856_production, 93_LVBus1106857_consumption, 93_LVBus1106857_production, 93_LVBus1106858_consumption, 93_LVBus1106858_production, 93_LVBus1106859_production, 93_LVBus1106860_production, 93_LVBus1106861_production, 93_LVBus1106862_production, 93_LVBus1106863_production, 93_LVBus1106864_consumption, 93_LVBus1106864_production, 93_LVBus1106866_production, 93_LVBus1106867_production, 93_LVBus1106868_consumption, 93_LVBus1106868_production, 93_LVBus1106869_consumption, 93_LVBus1106869_production, 93_LVBus1106870_production, 93_LVBus1106871_production, 93_LVBus1106872_production, 93_LVBus1106873_production, 93_LVBus1106874_production, 93_LVBus1106875_production, 93_LVBus1106876_production, 93_LVBus1106877_production, 93_LVBus1106878_production, 93_LVBus1106880_production, 93_LVBus1106881_production, 93_LVBus1106882_consumption, 93_LVBus1106882_production, 93_LVBus1106883_consumption, 93_LVBus1106883_production, 93_LVBus1106884_production, 93_LVBus1106885_production, 93_LVBus1106886_production, 93_LVBus1106887_production, 93_LVBus1106888_production, 93_LVBus1106889_production, 93_LVBus1106891_production, 93_LVBus1106892_production, 93_LVBus1106893_production, 93_LVBus1106894_production, 93_LVBus1106895_production, 93_LVBus1106896_consumption, 93_LVBus1106896_production, 93_LVBus1106897_production, 93_LVBus1106898_production, 93_LVBus1106899_production, 93_LVBus1106900_production, 93_LVBus1106901_consumption, 93_LVBus1106901_production, 93_LVBus1106902_production, 93_LVBus1106903_production, 93_LVBus1106905_production, 93_LVBus1106906_production, 93_LVBus1106907_production, 93_LVBus1106908_production, 93_LVBus1106909_consumption, 93_LVBus1106909_production, 93_LVBus1106910_production, 93_LVBus1106911_consumption, 93_LVBus1106911_production, 93_LVBus1106912_production, 93_LVBus1106913_production, 93_LVBus1106914_production, 93_LVBus1106915_production, 93_LVBus1106916_production, 93_LVBus1106917_production, 93_LVBus1106918_production, 93_LVBus1106919_production, 93_LVBus1106920_production, 93_LVBus1106921_production, 93_LVBus1106922_production, 93_LVBus1106923_production, 93_LVBus1106927_consumption, 93_LVBus1106927_production, 93_LVBus1106928_production, 93_LVBus1106929_consumption, 93_LVBus1106929_production, 93_LVBus1106930_consumption, 93_LVBus1106930_production, 93_LVBus1106931_consumption, 93_LVBus1106931_production, 93_LVBus1106932_production, 93_LVBus1106934_consumption, 93_LVBus1106934_production, 93_LVBus1106935_production, 93_LVBus1106936_consumption, 93_LVBus1106936_production, 93_LVBus1106937_consumption, 93_LVBus1106937_production, 93_LVBus1106939_consumption, 93_LVBus1106939_production, 93_LVBus1106940_production, 93_LVBus1106942_consumption, 93_LVBus1106942_production, 93_LVBus1106945_production, 93_LVBus1106947_consumption, 93_LVBus1106947_production, 93_LVBus1106948_consumption, 93_LVBus1106948_production, 93_LVBus1106949_consumption, 93_LVBus1106949_production, 93_LVBus1106950_production, 93_LVBus1106951_production, 93_LVBus1106952_production, 93_LVBus1106953_production, 93_LVBus1106955_consumption, 93_LVBus1106955_production, 93_LVBus1106956_consumption, 93_LVBus1106956_production, 93_LVBus1106957_consumption, 93_LVBus1106957_production, 93_LVBus1106959_consumption, 93_LVBus1106959_production, 93_LVBus1106960_consumption, 93_LVBus1106960_production, 93_LVBus1106961_production, 93_LVBus1106962_production, 93_LVBus1106963_production, 93_LVBus1106965_consumption, 93_LVBus1106965_production, 93_LVBus1106966_consumption, 93_LVBus1106966_production, 93_LVBus1106967_consumption, 93_LVBus1106967_production, 93_LVBus1106968_production, 93_LVBus1106969_production, 93_LVBus1106970_consumption, 93_LVBus1106970_production, 93_LVBus1106971_production, 93_LVBus1106972_production, 93_LVBus1106973_production, 93_LVBus1106975_consumption, 93_LVBus1106975_production, 93_LVBus1106977_production, 93_LVBus1106979_consumption, 93_LVBus1106979_production, 93_LVBus1106980_production, 93_LVBus1106981_production, 93_LVBus1106982_production, 93_LVBus1106983_production, 93_LVBus1106984_consumption, 93_LVBus1106984_production, 93_LVBus1106985_consumption, 93_LVBus1106985_production, 93_LVBus1106986_production, 93_LVBus1106987_production, 93_LVBus1106989_consumption, 93_LVBus1106989_production, 93_LVBus1106990_consumption, 93_LVBus1106990_production, 93_LVBus1106992_consumption, 93_LVBus1106992_production, 93_LVBus1106993_consumption, 93_LVBus1106993_production, 93_LVBus1106994_production, 93_LVBus1106995_production, 93_LVBus1106996_production, 93_LVBus1106998_consumption, 93_LVBus1106998_production, 93_LVBus1106999_consumption, 93_LVBus1106999_production, 93_LVBus1107000_consumption, 93_LVBus1107000_production, 93_LVBus1107001_consumption, 93_LVBus1107001_production, 93_LVBus1107002_consumption, 93_LVBus1107002_production, 93_LVBus1107003_consumption, 93_LVBus1107003_production, 93_LVBus1107004_consumption, 93_LVBus1107004_production, 93_LVBus1107005_consumption, 93_LVBus1107005_production, 93_LVBus1107006_consumption, 93_LVBus1107006_production, 93_LVBus1107007_consumption, 93_LVBus1107007_production, 93_LVBus1107008_consumption, 93_LVBus1107008_production, 93_LVBus1107009_consumption, 93_LVBus1107009_production, 93_LVBus1107010_consumption, 93_LVBus1107010_production, 93_LVBus1107011_consumption, 93_LVBus1107011_production, 93_LVBus1107012_consumption, 93_LVBus1107012_production, 93_LVBus1107013_consumption, 93_LVBus1107013_production, 93_LVBus1107014_consumption, 93_LVBus1107014_production, 93_LVBus1107016_consumption, 93_LVBus1107016_production, 93_LVBus1107017_consumption, 93_LVBus1107017_production, 93_LVBus1107018_consumption, 93_LVBus1107018_production, 93_LVBus1107019_consumption, 93_LVBus1107019_production, 93_LVBus1107020_consumption, 93_LVBus1107020_production, 93_LVBus1107021_consumption, 93_LVBus1107021_production, 93_LVBus1107022_consumption, 93_LVBus1107022_production, 93_LVBus1107024_consumption, 93_LVBus1107024_production, 93_LVBus1107025_consumption, 93_LVBus1107025_production, 93_LVBus1107026_production, 93_LVBus1107027_production, 93_LVBus1107028_consumption, 93_LVBus1107028_production, 93_LVBus1107029_production, 93_LVBus1107030_production, 93_LVBus1107031_production, 93_LVBus1107032_production, 93_LVBus1107033_production, 93_LVBus1107034_production, 93_LVBus1107035_production, 93_LVBus1107036_production, 93_LVBus1107038_consumption, 93_LVBus1107038_production, 93_LVBus1107039_consumption, 93_LVBus1107039_production, 93_LVBus1107040_consumption, 93_LVBus1107040_production, 93_LVBus1107041_consumption, 93_LVBus1107041_production, 93_LVBus1107042_consumption, 93_LVBus1107042_production, 93_LVBus1107043_consumption, 93_LVBus1107043_production, 93_LVBus1107044_consumption, 93_LVBus1107044_production, 93_LVBus1107045_consumption, 93_LVBus1107045_production, 93_LVBus1107046_consumption, 93_LVBus1107046_production, 93_LVBus1107047_consumption, 93_LVBus1107047_production, 93_LVBus1107048_consumption, 93_LVBus1107048_production, 93_LVBus1107049_consumption, 93_LVBus1107049_production, 93_LVBus1107051_production, 93_LVBus1107052_production, 93_LVBus1107053_production, 93_LVBus1107054_production, 93_LVBus1107055_production, 93_LVBus1107056_production, 93_LVBus1107057_production, 93_LVBus1107058_production, 93_LVBus1107059_production, 93_LVBus1107061_production, 93_LVBus1107062_production, 93_LVBus1107063_production, 93_LVBus1107064_production, 93_LVBus1107065_production, 93_LVBus1107067_production, 93_LVBus1107068_production, 93_LVBus1107070_consumption, 93_LVBus1107070_production, 93_LVBus1107071_consumption, 93_LVBus1107071_production, 93_LVBus1107072_consumption, 93_LVBus1107072_production, 93_LVBus1107073_consumption, 93_LVBus1107073_production, 93_LVBus1107074_production, 93_LVBus1107075_consumption, 93_LVBus1107075_production, 93_LVBus1107076_production, 93_LVBus1107077_consumption, 93_LVBus1107077_production, 93_LVBus1107078_production, 93_LVBus1107080_consumption, 93_LVBus1107080_production, 93_LVBus1107081_consumption, 93_LVBus1107081_production, 93_LVBus1107082_production, 93_LVBus1107084_production, 93_LVBus1107085_production, 93_LVBus1107086_production, 93_LVBus1107087_consumption, 93_LVBus1107087_production, 93_LVBus1107088_production, 93_LVBus1107090_production, 93_LVBus1107091_consumption, 93_LVBus1107091_production, 93_LVBus1107092_consumption, 93_LVBus1107092_production, 93_LVBus1107093_consumption, 93_LVBus1107093_production, 93_LVBus1107094_production, 93_LVBus1107095_production, 93_LVBus1107096_consumption, 93_LVBus1107096_production, 93_LVBus1107097_consumption, 93_LVBus1107097_production, 93_LVBus1107098_production, 93_LVBus1107099_consumption, 93_LVBus1107099_production, 93_LVBus1107101_production, 93_LVBus1107102_production, 93_LVBus1107103_consumption, 93_LVBus1107103_production, 93_LVBus1107105_consumption, 93_LVBus1107105_production, 93_LVBus1107106_consumption, 93_LVBus1107106_production, 93_LVBus1107107_consumption, 93_LVBus1107107_production, 93_LVBus1107108_consumption, 93_LVBus1107108_production, 93_LVBus1107109_consumption, 93_LVBus1107109_production, 93_LVBus1107110_consumption, 93_LVBus1107110_production, 93_LVBus1107112_consumption, 93_LVBus1107112_production, 93_LVBus1107113_consumption, 93_LVBus1107113_production, 93_LVBus1107114_production, 93_LVBus1107115_production, 93_LVBus1107116_consumption, 93_LVBus1107116_production, 93_LVBus1107117_consumption, 93_LVBus1107117_production, 93_LVBus1107118_consumption, 93_LVBus1107118_production, 93_LVBus1107120_consumption, 93_LVBus1107120_production, 93_LVBus1107121_consumption, 93_LVBus1107121_production, 93_LVBus1107122_production, 93_LVBus1107123_consumption, 93_LVBus1107123_production, 93_LVBus1107124_consumption, 93_LVBus1107124_production, 93_LVBus1107125_consumption, 93_LVBus1107125_production, 93_LVBus1107126_consumption, 93_LVBus1107126_production, 93_LVBus1107127_production, 93_LVBus1107128_consumption, 93_LVBus1107128_production, 93_MVLV03342_consumption, 93_MVLV03342_production, 93_MVLV04942_consumption, 93_MVLV04942_production, 93_MVLV10075_production, 93_MVLV22791_consumption, 93_MVLV22791_production, 93_MVLV29819_consumption, 93_MVLV29819_production, 93_MVLV29839_consumption, 93_MVLV29839_production, 93_MVLV51159_consumption, 93_MVLV51159_production, 93_MVLV60941_consumption, 93_MVLV60941_production, 93_MVLV60955_consumption, 93_MVLV60955_production, 93_MVLV63342_production.

## 9. Data Quality Summary

**Total findings:** 264 (0 errors, 5 warnings, 259 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  629 of 916 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.98 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  630 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107036_consumption`  
  Load '93_LVBus1107036_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107032_consumption`  
  Load '93_LVBus1107032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106705_consumption`  
  Load '93_LVBus1106705_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106611_consumption`  
  Load '93_LVBus1106611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106952_consumption`  
  Load '93_LVBus1106952_consumption' has phase imbalance of 96.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107051_consumption`  
  Load '93_LVBus1107051_consumption' has phase imbalance of 170.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106816_consumption`  
  Load '93_LVBus1106816_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106806_consumption`  
  Load '93_LVBus1106806_consumption' has phase imbalance of 114.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106914_consumption`  
  Load '93_LVBus1106914_consumption' has phase imbalance of 219.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107058_consumption`  
  Load '93_LVBus1107058_consumption' has phase imbalance of 207.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106889_consumption`  
  Load '93_LVBus1106889_consumption' has phase imbalance of 28.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106969_consumption`  
  Load '93_LVBus1106969_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106861_consumption`  
  Load '93_LVBus1106861_consumption' has phase imbalance of 170.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106735_consumption`  
  Load '93_LVBus1106735_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106866_consumption`  
  Load '93_LVBus1106866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106833_consumption`  
  Load '93_LVBus1106833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106679_consumption`  
  Load '93_LVBus1106679_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106738_consumption`  
  Load '93_LVBus1106738_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107029_consumption`  
  Load '93_LVBus1107029_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106800_consumption`  
  Load '93_LVBus1106800_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106822_consumption`  
  Load '93_LVBus1106822_consumption' has phase imbalance of 69.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106612_consumption`  
  Load '93_LVBus1106612_consumption' has phase imbalance of 238.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106686_consumption`  
  Load '93_LVBus1106686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106690_consumption`  
  Load '93_LVBus1106690_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106702_consumption`  
  Load '93_LVBus1106702_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107065_consumption`  
  Load '93_LVBus1107065_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106874_consumption`  
  Load '93_LVBus1106874_consumption' has phase imbalance of 94.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106726_consumption`  
  Load '93_LVBus1106726_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106616_consumption`  
  Load '93_LVBus1106616_consumption' has phase imbalance of 114.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106843_consumption`  
  Load '93_LVBus1106843_consumption' has phase imbalance of 108.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106887_consumption`  
  Load '93_LVBus1106887_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106725_consumption`  
  Load '93_LVBus1106725_consumption' has phase imbalance of 181.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106818_consumption`  
  Load '93_LVBus1106818_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106836_consumption`  
  Load '93_LVBus1106836_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107061_consumption`  
  Load '93_LVBus1107061_consumption' has phase imbalance of 81.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106637_consumption`  
  Load '93_LVBus1106637_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106860_consumption`  
  Load '93_LVBus1106860_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106687_consumption`  
  Load '93_LVBus1106687_consumption' has phase imbalance of 64.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106631_consumption`  
  Load '93_LVBus1106631_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106871_consumption`  
  Load '93_LVBus1106871_consumption' has phase imbalance of 205.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106699_consumption`  
  Load '93_LVBus1106699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106794_consumption`  
  Load '93_LVBus1106794_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106606_consumption`  
  Load '93_LVBus1106606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106694_consumption`  
  Load '93_LVBus1106694_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106717_consumption`  
  Load '93_LVBus1106717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106968_consumption`  
  Load '93_LVBus1106968_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106918_consumption`  
  Load '93_LVBus1106918_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106980_consumption`  
  Load '93_LVBus1106980_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106910_consumption`  
  Load '93_LVBus1106910_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106973_consumption`  
  Load '93_LVBus1106973_consumption' has phase imbalance of 125.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106793_consumption`  
  Load '93_LVBus1106793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106758_consumption`  
  Load '93_LVBus1106758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106620_consumption`  
  Load '93_LVBus1106620_consumption' has phase imbalance of 237.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106921_consumption`  
  Load '93_LVBus1106921_consumption' has phase imbalance of 216.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106875_consumption`  
  Load '93_LVBus1106875_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106615_consumption`  
  Load '93_LVBus1106615_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106708_consumption`  
  Load '93_LVBus1106708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106688_consumption`  
  Load '93_LVBus1106688_consumption' has phase imbalance of 132.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106838_consumption`  
  Load '93_LVBus1106838_consumption' has phase imbalance of 218.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106807_consumption`  
  Load '93_LVBus1106807_consumption' has phase imbalance of 96.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106607_consumption`  
  Load '93_LVBus1106607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106850_consumption`  
  Load '93_LVBus1106850_consumption' has phase imbalance of 280.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106844_consumption`  
  Load '93_LVBus1106844_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106848_consumption`  
  Load '93_LVBus1106848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106811_consumption`  
  Load '93_LVBus1106811_consumption' has phase imbalance of 223.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106863_consumption`  
  Load '93_LVBus1106863_consumption' has phase imbalance of 222.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106894_consumption`  
  Load '93_LVBus1106894_consumption' has phase imbalance of 204.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106841_consumption`  
  Load '93_LVBus1106841_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106792_consumption`  
  Load '93_LVBus1106792_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106805_consumption`  
  Load '93_LVBus1106805_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107031_consumption`  
  Load '93_LVBus1107031_consumption' has phase imbalance of 27.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106898_consumption`  
  Load '93_LVBus1106898_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106907_consumption`  
  Load '93_LVBus1106907_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106730_consumption`  
  Load '93_LVBus1106730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106658_consumption`  
  Load '93_LVBus1106658_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107035_consumption`  
  Load '93_LVBus1107035_consumption' has phase imbalance of 88.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106791_consumption`  
  Load '93_LVBus1106791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106880_consumption`  
  Load '93_LVBus1106880_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106731_consumption`  
  Load '93_LVBus1106731_consumption' has phase imbalance of 275.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106808_consumption`  
  Load '93_LVBus1106808_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106915_consumption`  
  Load '93_LVBus1106915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106888_consumption`  
  Load '93_LVBus1106888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106846_consumption`  
  Load '93_LVBus1106846_consumption' has phase imbalance of 236.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106704_consumption`  
  Load '93_LVBus1106704_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106673_consumption`  
  Load '93_LVBus1106673_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106826_consumption`  
  Load '93_LVBus1106826_consumption' has phase imbalance of 92.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106963_consumption`  
  Load '93_LVBus1106963_consumption' has phase imbalance of 55.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106886_consumption`  
  Load '93_LVBus1106886_consumption' has phase imbalance of 206.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106972_consumption`  
  Load '93_LVBus1106972_consumption' has phase imbalance of 58.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106669_consumption`  
  Load '93_LVBus1106669_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106920_consumption`  
  Load '93_LVBus1106920_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106905_consumption`  
  Load '93_LVBus1106905_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106737_consumption`  
  Load '93_LVBus1106737_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106922_consumption`  
  Load '93_LVBus1106922_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107059_consumption`  
  Load '93_LVBus1107059_consumption' has phase imbalance of 263.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106902_consumption`  
  Load '93_LVBus1106902_consumption' has phase imbalance of 228.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106634_consumption`  
  Load '93_LVBus1106634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106802_consumption`  
  Load '93_LVBus1106802_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107067_consumption`  
  Load '93_LVBus1107067_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106870_consumption`  
  Load '93_LVBus1106870_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107055_consumption`  
  Load '93_LVBus1107055_consumption' has phase imbalance of 278.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106740_consumption`  
  Load '93_LVBus1106740_consumption' has phase imbalance of 200.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106619_consumption`  
  Load '93_LVBus1106619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106797_consumption`  
  Load '93_LVBus1106797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106647_consumption`  
  Load '93_LVBus1106647_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106859_consumption`  
  Load '93_LVBus1106859_consumption' has phase imbalance of 257.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106862_consumption`  
  Load '93_LVBus1106862_consumption' has phase imbalance of 221.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106623_consumption`  
  Load '93_LVBus1106623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106741_consumption`  
  Load '93_LVBus1106741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106842_consumption`  
  Load '93_LVBus1106842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106899_consumption`  
  Load '93_LVBus1106899_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106825_consumption`  
  Load '93_LVBus1106825_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106906_consumption`  
  Load '93_LVBus1106906_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106703_consumption`  
  Load '93_LVBus1106703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107056_consumption`  
  Load '93_LVBus1107056_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106766_consumption`  
  Load '93_LVBus1106766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106953_consumption`  
  Load '93_LVBus1106953_consumption' has phase imbalance of 46.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106821_consumption`  
  Load '93_LVBus1106821_consumption' has phase imbalance of 22.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106912_consumption`  
  Load '93_LVBus1106912_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106856_consumption`  
  Load '93_LVBus1106856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106722_consumption`  
  Load '93_LVBus1106722_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106701_consumption`  
  Load '93_LVBus1106701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106710_consumption`  
  Load '93_LVBus1106710_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106736_consumption`  
  Load '93_LVBus1106736_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106700_consumption`  
  Load '93_LVBus1106700_consumption' has phase imbalance of 137.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106845_consumption`  
  Load '93_LVBus1106845_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106609_consumption`  
  Load '93_LVBus1106609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106695_consumption`  
  Load '93_LVBus1106695_consumption' has phase imbalance of 236.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106996_consumption`  
  Load '93_LVBus1106996_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107052_consumption`  
  Load '93_LVBus1107052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106908_consumption`  
  Load '93_LVBus1106908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106770_consumption`  
  Load '93_LVBus1106770_consumption' has phase imbalance of 47.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106987_consumption`  
  Load '93_LVBus1106987_consumption' has phase imbalance of 52.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106839_consumption`  
  Load '93_LVBus1106839_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106872_consumption`  
  Load '93_LVBus1106872_consumption' has phase imbalance of 72.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106854_consumption`  
  Load '93_LVBus1106854_consumption' has phase imbalance of 230.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106743_consumption`  
  Load '93_LVBus1106743_consumption' has phase imbalance of 87.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106801_consumption`  
  Load '93_LVBus1106801_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106932_consumption`  
  Load '93_LVBus1106932_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106681_consumption`  
  Load '93_LVBus1106681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106917_consumption`  
  Load '93_LVBus1106917_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106733_consumption`  
  Load '93_LVBus1106733_consumption' has phase imbalance of 252.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106919_consumption`  
  Load '93_LVBus1106919_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106613_consumption`  
  Load '93_LVBus1106613_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106923_consumption`  
  Load '93_LVBus1106923_consumption' has phase imbalance of 60.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107034_consumption`  
  Load '93_LVBus1107034_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107026_consumption`  
  Load '93_LVBus1107026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106885_consumption`  
  Load '93_LVBus1106885_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107053_consumption`  
  Load '93_LVBus1107053_consumption' has phase imbalance of 216.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107062_consumption`  
  Load '93_LVBus1107062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106835_consumption`  
  Load '93_LVBus1106835_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106734_consumption`  
  Load '93_LVBus1106734_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107068_consumption`  
  Load '93_LVBus1107068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106723_consumption`  
  Load '93_LVBus1106723_consumption' has phase imbalance of 75.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106813_consumption`  
  Load '93_LVBus1106813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106895_consumption`  
  Load '93_LVBus1106895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106635_consumption`  
  Load '93_LVBus1106635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107057_consumption`  
  Load '93_LVBus1107057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106677_consumption`  
  Load '93_LVBus1106677_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106798_consumption`  
  Load '93_LVBus1106798_consumption' has phase imbalance of 236.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107033_consumption`  
  Load '93_LVBus1107033_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106742_consumption`  
  Load '93_LVBus1106742_consumption' has phase imbalance of 59.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106995_consumption`  
  Load '93_LVBus1106995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106983_consumption`  
  Load '93_LVBus1106983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106950_consumption`  
  Load '93_LVBus1106950_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106683_consumption`  
  Load '93_LVBus1106683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106876_consumption`  
  Load '93_LVBus1106876_consumption' has phase imbalance of 57.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106820_consumption`  
  Load '93_LVBus1106820_consumption' has phase imbalance of 275.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106713_consumption`  
  Load '93_LVBus1106713_consumption' has phase imbalance of 246.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106810_consumption`  
  Load '93_LVBus1106810_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106711_consumption`  
  Load '93_LVBus1106711_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106622_consumption`  
  Load '93_LVBus1106622_consumption' has phase imbalance of 289.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106903_consumption`  
  Load '93_LVBus1106903_consumption' has phase imbalance of 212.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106897_consumption`  
  Load '93_LVBus1106897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106971_consumption`  
  Load '93_LVBus1106971_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106877_consumption`  
  Load '93_LVBus1106877_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107064_consumption`  
  Load '93_LVBus1107064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106721_consumption`  
  Load '93_LVBus1106721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106707_consumption`  
  Load '93_LVBus1106707_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106834_consumption`  
  Load '93_LVBus1106834_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107063_consumption`  
  Load '93_LVBus1107063_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106626_consumption`  
  Load '93_LVBus1106626_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106714_consumption`  
  Load '93_LVBus1106714_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106809_consumption`  
  Load '93_LVBus1106809_consumption' has phase imbalance of 266.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106913_consumption`  
  Load '93_LVBus1106913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106892_consumption`  
  Load '93_LVBus1106892_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106685_consumption`  
  Load '93_LVBus1106685_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106951_consumption`  
  Load '93_LVBus1106951_consumption' has phase imbalance of 198.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106610_consumption`  
  Load '93_LVBus1106610_consumption' has phase imbalance of 137.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106691_consumption`  
  Load '93_LVBus1106691_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106636_consumption`  
  Load '93_LVBus1106636_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106986_consumption`  
  Load '93_LVBus1106986_consumption' has phase imbalance of 43.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106632_consumption`  
  Load '93_LVBus1106632_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106724_consumption`  
  Load '93_LVBus1106724_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106672_consumption`  
  Load '93_LVBus1106672_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106893_consumption`  
  Load '93_LVBus1106893_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106625_consumption`  
  Load '93_LVBus1106625_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106732_consumption`  
  Load '93_LVBus1106732_consumption' has phase imbalance of 215.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106799_consumption`  
  Load '93_LVBus1106799_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106994_consumption`  
  Load '93_LVBus1106994_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106727_consumption`  
  Load '93_LVBus1106727_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106891_consumption`  
  Load '93_LVBus1106891_consumption' has phase imbalance of 129.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106867_consumption`  
  Load '93_LVBus1106867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106916_consumption`  
  Load '93_LVBus1106916_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106768_consumption`  
  Load '93_LVBus1106768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106828_consumption`  
  Load '93_LVBus1106828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106851_consumption`  
  Load '93_LVBus1106851_consumption' has phase imbalance of 211.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106712_consumption`  
  Load '93_LVBus1106712_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106678_consumption`  
  Load '93_LVBus1106678_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106693_consumption`  
  Load '93_LVBus1106693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106709_consumption`  
  Load '93_LVBus1106709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106814_consumption`  
  Load '93_LVBus1106814_consumption' has phase imbalance of 22.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106706_consumption`  
  Load '93_LVBus1106706_consumption' has phase imbalance of 239.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106878_consumption`  
  Load '93_LVBus1106878_consumption' has phase imbalance of 211.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107030_consumption`  
  Load '93_LVBus1107030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106853_consumption`  
  Load '93_LVBus1106853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106827_consumption`  
  Load '93_LVBus1106827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106718_consumption`  
  Load '93_LVBus1106718_consumption' has phase imbalance of 114.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106873_consumption`  
  Load '93_LVBus1106873_consumption' has phase imbalance of 269.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106796_consumption`  
  Load '93_LVBus1106796_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106759_consumption`  
  Load '93_LVBus1106759_consumption' has phase imbalance of 256.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106665_consumption`  
  Load '93_LVBus1106665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106676_consumption`  
  Load '93_LVBus1106676_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106757_consumption`  
  Load '93_LVBus1106757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106852_consumption`  
  Load '93_LVBus1106852_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106745_consumption`  
  Load '93_LVBus1106745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106881_consumption`  
  Load '93_LVBus1106881_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106819_consumption`  
  Load '93_LVBus1106819_consumption' has phase imbalance of 187.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106824_consumption`  
  Load '93_LVBus1106824_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107054_consumption`  
  Load '93_LVBus1107054_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106670_consumption`  
  Load '93_LVBus1106670_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106884_consumption`  
  Load '93_LVBus1106884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106728_consumption`  
  Load '93_LVBus1106728_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106900_consumption`  
  Load '93_LVBus1106900_consumption' has phase imbalance of 245.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106666_consumption`  
  Load '93_LVBus1106666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106982_consumption`  
  Load '93_LVBus1106982_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106684_consumption`  
  Load '93_LVBus1106684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106668_consumption`  
  Load '93_LVBus1106668_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106671_consumption`  
  Load '93_LVBus1106671_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106715_consumption`  
  Load '93_LVBus1106715_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1107027_consumption`  
  Load '93_LVBus1107027_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1106962_consumption`  
  Load '93_LVBus1106962_consumption' has phase imbalance of 47.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 916 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus1107101' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus1107070' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_VITRO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus1106977' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '93_LVBus1106977' (LV, 0.24 kV) has an electrical reach of 9.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  492 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  173 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 93_LVBus1106606_consumption, 93_LVBus1106607_consumption, 93_LVBus1106609_consumption, 93_LVBus1106611_consumption, 93_LVBus1106612_consumption, 93_LVBus1106613_consumption, 93_LVBus1106615_consumption, 93_LVBus1106619_consumption, 93_LVBus1106620_consumption, 93_LVBus1106622_consumption, 93_LVBus1106623_consumption, 93_LVBus1106625_consumption, 93_LVBus1106626_consumption, 93_LVBus1106631_consumption, 93_LVBus1106632_consumption, 93_LVBus1106634_consumption, 93_LVBus1106635_consumption, 93_LVBus1106636_consumption, 93_LVBus1106637_consumption, 93_LVBus1106665_consumption, 93_LVBus1106666_consumption, 93_LVBus1106668_consumption, 93_LVBus1106669_consumption, 93_LVBus1106670_consumption, 93_LVBus1106671_consumption, 93_LVBus1106672_consumption, 93_LVBus1106673_consumption, 93_LVBus1106676_consumption, 93_LVBus1106677_consumption, 93_LVBus1106678_consumption, 93_LVBus1106681_consumption, 93_LVBus1106683_consumption, 93_LVBus1106684_consumption, 93_LVBus1106686_consumption, 93_LVBus1106690_consumption, 93_LVBus1106691_consumption, 93_LVBus1106693_consumption, 93_LVBus1106694_consumption, 93_LVBus1106699_consumption, 93_LVBus1106701_consumption, 93_LVBus1106702_consumption, 93_LVBus1106703_consumption, 93_LVBus1106705_consumption, 93_LVBus1106706_consumption, 93_LVBus1106708_consumption, 93_LVBus1106709_consumption, 93_LVBus1106711_consumption, 93_LVBus1106712_consumption, 93_LVBus1106713_consumption, 93_LVBus1106714_consumption, 93_LVBus1106717_consumption, 93_LVBus1106721_consumption, 93_LVBus1106722_consumption, 93_LVBus1106725_consumption, 93_LVBus1106726_consumption, 93_LVBus1106727_consumption, 93_LVBus1106728_consumption, 93_LVBus1106730_consumption, 93_LVBus1106731_consumption, 93_LVBus1106732_consumption, 93_LVBus1106733_consumption, 93_LVBus1106735_consumption, 93_LVBus1106736_consumption, 93_LVBus1106738_consumption, 93_LVBus1106740_consumption, 93_LVBus1106741_consumption, 93_LVBus1106745_consumption, 93_LVBus1106757_consumption, 93_LVBus1106758_consumption, 93_LVBus1106766_consumption, 93_LVBus1106768_consumption, 93_LVBus1106791_consumption, 93_LVBus1106792_consumption, 93_LVBus1106793_consumption, 93_LVBus1106794_consumption, 93_LVBus1106796_consumption, 93_LVBus1106797_consumption, 93_LVBus1106798_consumption, 93_LVBus1106800_consumption, 93_LVBus1106802_consumption, 93_LVBus1106808_consumption, 93_LVBus1106809_consumption, 93_LVBus1106811_consumption, 93_LVBus1106813_consumption, 93_LVBus1106818_consumption, 93_LVBus1106819_consumption, 93_LVBus1106820_consumption, 93_LVBus1106825_consumption, 93_LVBus1106827_consumption, 93_LVBus1106828_consumption, 93_LVBus1106833_consumption, 93_LVBus1106834_consumption, 93_LVBus1106835_consumption, 93_LVBus1106836_consumption, 93_LVBus1106838_consumption, 93_LVBus1106839_consumption, 93_LVBus1106841_consumption, 93_LVBus1106842_consumption, 93_LVBus1106844_consumption, 93_LVBus1106845_consumption, 93_LVBus1106846_consumption, 93_LVBus1106848_consumption, 93_LVBus1106850_consumption, 93_LVBus1106851_consumption, 93_LVBus1106852_consumption, 93_LVBus1106853_consumption, 93_LVBus1106854_consumption, 93_LVBus1106856_consumption, 93_LVBus1106859_consumption, 93_LVBus1106860_consumption, 93_LVBus1106862_consumption, 93_LVBus1106863_consumption, 93_LVBus1106866_consumption, 93_LVBus1106867_consumption, 93_LVBus1106870_consumption, 93_LVBus1106871_consumption, 93_LVBus1106873_consumption, 93_LVBus1106875_consumption, 93_LVBus1106878_consumption, 93_LVBus1106880_consumption, 93_LVBus1106884_consumption, 93_LVBus1106885_consumption, 93_LVBus1106886_consumption, 93_LVBus1106887_consumption, 93_LVBus1106888_consumption, 93_LVBus1106892_consumption, 93_LVBus1106893_consumption, 93_LVBus1106894_consumption, 93_LVBus1106895_consumption, 93_LVBus1106897_consumption, 93_LVBus1106898_consumption, 93_LVBus1106899_consumption, 93_LVBus1106900_consumption, 93_LVBus1106902_consumption, 93_LVBus1106903_consumption, 93_LVBus1106905_consumption, 93_LVBus1106906_consumption, 93_LVBus1106908_consumption, 93_LVBus1106910_consumption, 93_LVBus1106912_consumption, 93_LVBus1106913_consumption, 93_LVBus1106914_consumption, 93_LVBus1106915_consumption, 93_LVBus1106916_consumption, 93_LVBus1106917_consumption, 93_LVBus1106919_consumption, 93_LVBus1106920_consumption, 93_LVBus1106921_consumption, 93_LVBus1106922_consumption, 93_LVBus1106932_consumption, 93_LVBus1106980_consumption, 93_LVBus1106982_consumption, 93_LVBus1106983_consumption, 93_LVBus1106994_consumption, 93_LVBus1106995_consumption, 93_LVBus1107026_consumption, 93_LVBus1107027_consumption, 93_LVBus1107029_consumption, 93_LVBus1107030_consumption, 93_LVBus1107032_consumption, 93_LVBus1107033_consumption, 93_LVBus1107034_consumption, 93_LVBus1107051_consumption, 93_LVBus1107052_consumption, 93_LVBus1107053_consumption, 93_LVBus1107054_consumption, 93_LVBus1107055_consumption, 93_LVBus1107056_consumption, 93_LVBus1107057_consumption, 93_LVBus1107059_consumption, 93_LVBus1107062_consumption, 93_LVBus1107064_consumption, 93_LVBus1107068_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  458 group(s) of loads (916 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  630 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus1106605_consumption, 93_LVBus1106605_production, 93_LVBus1106606_production, 93_LVBus1106607_production, 93_LVBus1106608_consumption, 93_LVBus1106608_production, 93_LVBus1106609_production, 93_LVBus1106610_production, 93_LVBus1106611_production, 93_LVBus1106612_production, 93_LVBus1106613_production, 93_LVBus1106615_production, 93_LVBus1106616_production, 93_LVBus1106617_consumption, 93_LVBus1106617_production, 93_LVBus1106619_production, 93_LVBus1106620_production, 93_LVBus1106621_consumption, 93_LVBus1106621_production, 93_LVBus1106622_production, 93_LVBus1106623_production, 93_LVBus1106625_production, 93_LVBus1106626_production, 93_LVBus1106628_consumption, 93_LVBus1106628_production, 93_LVBus1106630_consumption, 93_LVBus1106630_production, 93_LVBus1106631_production, 93_LVBus1106632_production, 93_LVBus1106633_consumption, 93_LVBus1106633_production, 93_LVBus1106634_production, 93_LVBus1106635_production, 93_LVBus1106636_production, 93_LVBus1106637_production, 93_LVBus1106639_consumption, 93_LVBus1106639_production, 93_LVBus1106641_production, 93_LVBus1106642_production, 93_LVBus1106643_consumption, 93_LVBus1106643_production, 93_LVBus1106644_production, 93_LVBus1106646_consumption, 93_LVBus1106646_production, 93_LVBus1106647_production, 93_LVBus1106648_consumption, 93_LVBus1106648_production, 93_LVBus1106649_consumption, 93_LVBus1106649_production, 93_LVBus1106651_production, 93_LVBus1106652_consumption, 93_LVBus1106652_production, 93_LVBus1106653_production, 93_LVBus1106655_consumption, 93_LVBus1106655_production, 93_LVBus1106656_consumption, 93_LVBus1106656_production, 93_LVBus1106658_production, 93_LVBus1106659_consumption, 93_LVBus1106659_production, 93_LVBus1106661_consumption, 93_LVBus1106661_production, 93_LVBus1106663_consumption, 93_LVBus1106663_production, 93_LVBus1106665_production, 93_LVBus1106666_production, 93_LVBus1106667_consumption, 93_LVBus1106667_production, 93_LVBus1106668_production, 93_LVBus1106669_production, 93_LVBus1106670_production, 93_LVBus1106671_production, 93_LVBus1106672_production, 93_LVBus1106673_production, 93_LVBus1106674_consumption, 93_LVBus1106674_production, 93_LVBus1106676_production, 93_LVBus1106677_production, 93_LVBus1106678_production, 93_LVBus1106679_production, 93_LVBus1106680_consumption, 93_LVBus1106680_production, 93_LVBus1106681_production, 93_LVBus1106682_consumption, 93_LVBus1106682_production, 93_LVBus1106683_production, 93_LVBus1106684_production, 93_LVBus1106685_production, 93_LVBus1106686_production, 93_LVBus1106687_production, 93_LVBus1106688_production, 93_LVBus1106689_consumption, 93_LVBus1106689_production, 93_LVBus1106690_production, 93_LVBus1106691_production, 93_LVBus1106693_production, 93_LVBus1106694_production, 93_LVBus1106695_production, 93_LVBus1106697_consumption, 93_LVBus1106697_production, 93_LVBus1106698_consumption, 93_LVBus1106698_production, 93_LVBus1106699_production, 93_LVBus1106700_production, 93_LVBus1106701_production, 93_LVBus1106702_production, 93_LVBus1106703_production, 93_LVBus1106704_production, 93_LVBus1106705_production, 93_LVBus1106706_production, 93_LVBus1106707_production, 93_LVBus1106708_production, 93_LVBus1106709_production, 93_LVBus1106710_production, 93_LVBus1106711_production, 93_LVBus1106712_production, 93_LVBus1106713_production, 93_LVBus1106714_production, 93_LVBus1106715_production, 93_LVBus1106717_production, 93_LVBus1106718_production, 93_LVBus1106720_consumption, 93_LVBus1106720_production, 93_LVBus1106721_production, 93_LVBus1106722_production, 93_LVBus1106723_production, 93_LVBus1106724_production, 93_LVBus1106725_production, 93_LVBus1106726_production, 93_LVBus1106727_production, 93_LVBus1106728_production, 93_LVBus1106729_consumption, 93_LVBus1106729_production, 93_LVBus1106730_production, 93_LVBus1106731_production, 93_LVBus1106732_production, 93_LVBus1106733_production, 93_LVBus1106734_production, 93_LVBus1106735_production, 93_LVBus1106736_production, 93_LVBus1106737_production, 93_LVBus1106738_production, 93_LVBus1106740_production, 93_LVBus1106741_production, 93_LVBus1106742_production, 93_LVBus1106743_production, 93_LVBus1106745_production, 93_LVBus1106747_consumption, 93_LVBus1106747_production, 93_LVBus1106749_consumption, 93_LVBus1106749_production, 93_LVBus1106750_production, 93_LVBus1106751_production, 93_LVBus1106752_consumption, 93_LVBus1106752_production, 93_LVBus1106753_consumption, 93_LVBus1106753_production, 93_LVBus1106754_production, 93_LVBus1106755_consumption, 93_LVBus1106755_production, 93_LVBus1106756_consumption, 93_LVBus1106756_production, 93_LVBus1106757_production, 93_LVBus1106758_production, 93_LVBus1106759_production, 93_LVBus1106761_consumption, 93_LVBus1106761_production, 93_LVBus1106762_production, 93_LVBus1106764_production, 93_LVBus1106766_production, 93_LVBus1106767_consumption, 93_LVBus1106767_production, 93_LVBus1106768_production, 93_LVBus1106769_consumption, 93_LVBus1106769_production, 93_LVBus1106770_production, 93_LVBus1106771_consumption, 93_LVBus1106771_production, 93_LVBus1106772_production, 93_LVBus1106773_consumption, 93_LVBus1106773_production, 93_LVBus1106774_production, 93_LVBus1106776_consumption, 93_LVBus1106776_production, 93_LVBus1106777_consumption, 93_LVBus1106777_production, 93_LVBus1106778_production, 93_LVBus1106779_production, 93_LVBus1106780_production, 93_LVBus1106781_consumption, 93_LVBus1106781_production, 93_LVBus1106783_consumption, 93_LVBus1106783_production, 93_LVBus1106784_consumption, 93_LVBus1106784_production, 93_LVBus1106785_production, 93_LVBus1106787_consumption, 93_LVBus1106787_production, 93_LVBus1106789_consumption, 93_LVBus1106789_production, 93_LVBus1106791_production, 93_LVBus1106792_production, 93_LVBus1106793_production, 93_LVBus1106794_production, 93_LVBus1106795_production, 93_LVBus1106796_production, 93_LVBus1106797_production, 93_LVBus1106798_production, 93_LVBus1106799_production, 93_LVBus1106800_production, 93_LVBus1106801_production, 93_LVBus1106802_production, 93_LVBus1106804_consumption, 93_LVBus1106804_production, 93_LVBus1106805_production, 93_LVBus1106806_production, 93_LVBus1106807_production, 93_LVBus1106808_production, 93_LVBus1106809_production, 93_LVBus1106810_production, 93_LVBus1106811_production, 93_LVBus1106813_production, 93_LVBus1106814_production, 93_LVBus1106815_consumption, 93_LVBus1106815_production, 93_LVBus1106816_production, 93_LVBus1106818_production, 93_LVBus1106819_production, 93_LVBus1106820_production, 93_LVBus1106821_production, 93_LVBus1106822_production, 93_LVBus1106824_production, 93_LVBus1106825_production, 93_LVBus1106826_production, 93_LVBus1106827_production, 93_LVBus1106828_production, 93_LVBus1106830_consumption, 93_LVBus1106830_production, 93_LVBus1106831_consumption, 93_LVBus1106831_production, 93_LVBus1106832_consumption, 93_LVBus1106832_production, 93_LVBus1106833_production, 93_LVBus1106834_production, 93_LVBus1106835_production, 93_LVBus1106836_production, 93_LVBus1106838_production, 93_LVBus1106839_production, 93_LVBus1106841_production, 93_LVBus1106842_production, 93_LVBus1106843_production, 93_LVBus1106844_production, 93_LVBus1106845_production, 93_LVBus1106846_production, 93_LVBus1106848_production, 93_LVBus1106849_consumption, 93_LVBus1106849_production, 93_LVBus1106850_production, 93_LVBus1106851_production, 93_LVBus1106852_production, 93_LVBus1106853_production, 93_LVBus1106854_production, 93_LVBus1106856_production, 93_LVBus1106857_consumption, 93_LVBus1106857_production, 93_LVBus1106858_consumption, 93_LVBus1106858_production, 93_LVBus1106859_production, 93_LVBus1106860_production, 93_LVBus1106861_production, 93_LVBus1106862_production, 93_LVBus1106863_production, 93_LVBus1106864_consumption, 93_LVBus1106864_production, 93_LVBus1106866_production, 93_LVBus1106867_production, 93_LVBus1106868_consumption, 93_LVBus1106868_production, 93_LVBus1106869_consumption, 93_LVBus1106869_production, 93_LVBus1106870_production, 93_LVBus1106871_production, 93_LVBus1106872_production, 93_LVBus1106873_production, 93_LVBus1106874_production, 93_LVBus1106875_production, 93_LVBus1106876_production, 93_LVBus1106877_production, 93_LVBus1106878_production, 93_LVBus1106880_production, 93_LVBus1106881_production, 93_LVBus1106882_consumption, 93_LVBus1106882_production, 93_LVBus1106883_consumption, 93_LVBus1106883_production, 93_LVBus1106884_production, 93_LVBus1106885_production, 93_LVBus1106886_production, 93_LVBus1106887_production, 93_LVBus1106888_production, 93_LVBus1106889_production, 93_LVBus1106891_production, 93_LVBus1106892_production, 93_LVBus1106893_production, 93_LVBus1106894_production, 93_LVBus1106895_production, 93_LVBus1106896_consumption, 93_LVBus1106896_production, 93_LVBus1106897_production, 93_LVBus1106898_production, 93_LVBus1106899_production, 93_LVBus1106900_production, 93_LVBus1106901_consumption, 93_LVBus1106901_production, 93_LVBus1106902_production, 93_LVBus1106903_production, 93_LVBus1106905_production, 93_LVBus1106906_production, 93_LVBus1106907_production, 93_LVBus1106908_production, 93_LVBus1106909_consumption, 93_LVBus1106909_production, 93_LVBus1106910_production, 93_LVBus1106911_consumption, 93_LVBus1106911_production, 93_LVBus1106912_production, 93_LVBus1106913_production, 93_LVBus1106914_production, 93_LVBus1106915_production, 93_LVBus1106916_production, 93_LVBus1106917_production, 93_LVBus1106918_production, 93_LVBus1106919_production, 93_LVBus1106920_production, 93_LVBus1106921_production, 93_LVBus1106922_production, 93_LVBus1106923_production, 93_LVBus1106927_consumption, 93_LVBus1106927_production, 93_LVBus1106928_production, 93_LVBus1106929_consumption, 93_LVBus1106929_production, 93_LVBus1106930_consumption, 93_LVBus1106930_production, 93_LVBus1106931_consumption, 93_LVBus1106931_production, 93_LVBus1106932_production, 93_LVBus1106934_consumption, 93_LVBus1106934_production, 93_LVBus1106935_production, 93_LVBus1106936_consumption, 93_LVBus1106936_production, 93_LVBus1106937_consumption, 93_LVBus1106937_production, 93_LVBus1106939_consumption, 93_LVBus1106939_production, 93_LVBus1106940_production, 93_LVBus1106942_consumption, 93_LVBus1106942_production, 93_LVBus1106945_production, 93_LVBus1106947_consumption, 93_LVBus1106947_production, 93_LVBus1106948_consumption, 93_LVBus1106948_production, 93_LVBus1106949_consumption, 93_LVBus1106949_production, 93_LVBus1106950_production, 93_LVBus1106951_production, 93_LVBus1106952_production, 93_LVBus1106953_production, 93_LVBus1106955_consumption, 93_LVBus1106955_production, 93_LVBus1106956_consumption, 93_LVBus1106956_production, 93_LVBus1106957_consumption, 93_LVBus1106957_production, 93_LVBus1106959_consumption, 93_LVBus1106959_production, 93_LVBus1106960_consumption, 93_LVBus1106960_production, 93_LVBus1106961_production, 93_LVBus1106962_production, 93_LVBus1106963_production, 93_LVBus1106965_consumption, 93_LVBus1106965_production, 93_LVBus1106966_consumption, 93_LVBus1106966_production, 93_LVBus1106967_consumption, 93_LVBus1106967_production, 93_LVBus1106968_production, 93_LVBus1106969_production, 93_LVBus1106970_consumption, 93_LVBus1106970_production, 93_LVBus1106971_production, 93_LVBus1106972_production, 93_LVBus1106973_production, 93_LVBus1106975_consumption, 93_LVBus1106975_production, 93_LVBus1106977_production, 93_LVBus1106979_consumption, 93_LVBus1106979_production, 93_LVBus1106980_production, 93_LVBus1106981_production, 93_LVBus1106982_production, 93_LVBus1106983_production, 93_LVBus1106984_consumption, 93_LVBus1106984_production, 93_LVBus1106985_consumption, 93_LVBus1106985_production, 93_LVBus1106986_production, 93_LVBus1106987_production, 93_LVBus1106989_consumption, 93_LVBus1106989_production, 93_LVBus1106990_consumption, 93_LVBus1106990_production, 93_LVBus1106992_consumption, 93_LVBus1106992_production, 93_LVBus1106993_consumption, 93_LVBus1106993_production, 93_LVBus1106994_production, 93_LVBus1106995_production, 93_LVBus1106996_production, 93_LVBus1106998_consumption, 93_LVBus1106998_production, 93_LVBus1106999_consumption, 93_LVBus1106999_production, 93_LVBus1107000_consumption, 93_LVBus1107000_production, 93_LVBus1107001_consumption, 93_LVBus1107001_production, 93_LVBus1107002_consumption, 93_LVBus1107002_production, 93_LVBus1107003_consumption, 93_LVBus1107003_production, 93_LVBus1107004_consumption, 93_LVBus1107004_production, 93_LVBus1107005_consumption, 93_LVBus1107005_production, 93_LVBus1107006_consumption, 93_LVBus1107006_production, 93_LVBus1107007_consumption, 93_LVBus1107007_production, 93_LVBus1107008_consumption, 93_LVBus1107008_production, 93_LVBus1107009_consumption, 93_LVBus1107009_production, 93_LVBus1107010_consumption, 93_LVBus1107010_production, 93_LVBus1107011_consumption, 93_LVBus1107011_production, 93_LVBus1107012_consumption, 93_LVBus1107012_production, 93_LVBus1107013_consumption, 93_LVBus1107013_production, 93_LVBus1107014_consumption, 93_LVBus1107014_production, 93_LVBus1107016_consumption, 93_LVBus1107016_production, 93_LVBus1107017_consumption, 93_LVBus1107017_production, 93_LVBus1107018_consumption, 93_LVBus1107018_production, 93_LVBus1107019_consumption, 93_LVBus1107019_production, 93_LVBus1107020_consumption, 93_LVBus1107020_production, 93_LVBus1107021_consumption, 93_LVBus1107021_production, 93_LVBus1107022_consumption, 93_LVBus1107022_production, 93_LVBus1107024_consumption, 93_LVBus1107024_production, 93_LVBus1107025_consumption, 93_LVBus1107025_production, 93_LVBus1107026_production, 93_LVBus1107027_production, 93_LVBus1107028_consumption, 93_LVBus1107028_production, 93_LVBus1107029_production, 93_LVBus1107030_production, 93_LVBus1107031_production, 93_LVBus1107032_production, 93_LVBus1107033_production, 93_LVBus1107034_production, 93_LVBus1107035_production, 93_LVBus1107036_production, 93_LVBus1107038_consumption, 93_LVBus1107038_production, 93_LVBus1107039_consumption, 93_LVBus1107039_production, 93_LVBus1107040_consumption, 93_LVBus1107040_production, 93_LVBus1107041_consumption, 93_LVBus1107041_production, 93_LVBus1107042_consumption, 93_LVBus1107042_production, 93_LVBus1107043_consumption, 93_LVBus1107043_production, 93_LVBus1107044_consumption, 93_LVBus1107044_production, 93_LVBus1107045_consumption, 93_LVBus1107045_production, 93_LVBus1107046_consumption, 93_LVBus1107046_production, 93_LVBus1107047_consumption, 93_LVBus1107047_production, 93_LVBus1107048_consumption, 93_LVBus1107048_production, 93_LVBus1107049_consumption, 93_LVBus1107049_production, 93_LVBus1107051_production, 93_LVBus1107052_production, 93_LVBus1107053_production, 93_LVBus1107054_production, 93_LVBus1107055_production, 93_LVBus1107056_production, 93_LVBus1107057_production, 93_LVBus1107058_production, 93_LVBus1107059_production, 93_LVBus1107061_production, 93_LVBus1107062_production, 93_LVBus1107063_production, 93_LVBus1107064_production, 93_LVBus1107065_production, 93_LVBus1107067_production, 93_LVBus1107068_production, 93_LVBus1107070_consumption, 93_LVBus1107070_production, 93_LVBus1107071_consumption, 93_LVBus1107071_production, 93_LVBus1107072_consumption, 93_LVBus1107072_production, 93_LVBus1107073_consumption, 93_LVBus1107073_production, 93_LVBus1107074_production, 93_LVBus1107075_consumption, 93_LVBus1107075_production, 93_LVBus1107076_production, 93_LVBus1107077_consumption, 93_LVBus1107077_production, 93_LVBus1107078_production, 93_LVBus1107080_consumption, 93_LVBus1107080_production, 93_LVBus1107081_consumption, 93_LVBus1107081_production, 93_LVBus1107082_production, 93_LVBus1107084_production, 93_LVBus1107085_production, 93_LVBus1107086_production, 93_LVBus1107087_consumption, 93_LVBus1107087_production, 93_LVBus1107088_production, 93_LVBus1107090_production, 93_LVBus1107091_consumption, 93_LVBus1107091_production, 93_LVBus1107092_consumption, 93_LVBus1107092_production, 93_LVBus1107093_consumption, 93_LVBus1107093_production, 93_LVBus1107094_production, 93_LVBus1107095_production, 93_LVBus1107096_consumption, 93_LVBus1107096_production, 93_LVBus1107097_consumption, 93_LVBus1107097_production, 93_LVBus1107098_production, 93_LVBus1107099_consumption, 93_LVBus1107099_production, 93_LVBus1107101_production, 93_LVBus1107102_production, 93_LVBus1107103_consumption, 93_LVBus1107103_production, 93_LVBus1107105_consumption, 93_LVBus1107105_production, 93_LVBus1107106_consumption, 93_LVBus1107106_production, 93_LVBus1107107_consumption, 93_LVBus1107107_production, 93_LVBus1107108_consumption, 93_LVBus1107108_production, 93_LVBus1107109_consumption, 93_LVBus1107109_production, 93_LVBus1107110_consumption, 93_LVBus1107110_production, 93_LVBus1107112_consumption, 93_LVBus1107112_production, 93_LVBus1107113_consumption, 93_LVBus1107113_production, 93_LVBus1107114_production, 93_LVBus1107115_production, 93_LVBus1107116_consumption, 93_LVBus1107116_production, 93_LVBus1107117_consumption, 93_LVBus1107117_production, 93_LVBus1107118_consumption, 93_LVBus1107118_production, 93_LVBus1107120_consumption, 93_LVBus1107120_production, 93_LVBus1107121_consumption, 93_LVBus1107121_production, 93_LVBus1107122_production, 93_LVBus1107123_consumption, 93_LVBus1107123_production, 93_LVBus1107124_consumption, 93_LVBus1107124_production, 93_LVBus1107125_consumption, 93_LVBus1107125_production, 93_LVBus1107126_consumption, 93_LVBus1107126_production, 93_LVBus1107127_production, 93_LVBus1107128_consumption, 93_LVBus1107128_production, 93_MVLV03342_consumption, 93_MVLV03342_production, 93_MVLV04942_consumption, 93_MVLV04942_production, 93_MVLV10075_production, 93_MVLV22791_consumption, 93_MVLV22791_production, 93_MVLV29819_consumption, 93_MVLV29819_production, 93_MVLV29839_consumption, 93_MVLV29839_production, 93_MVLV51159_consumption, 93_MVLV51159_production, 93_MVLV60941_consumption, 93_MVLV60941_production, 93_MVLV60955_consumption, 93_MVLV60955_production, 93_MVLV63342_production.

