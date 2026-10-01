# BMOPF Network Summary: 28_MVFeeder2047

**Generated:** 2026-10-01 23:34:04  
**Findings:** 0 errors · 4 warnings · 301 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 34 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 516 |  |
| line | 481 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 854 | 3.347 MW, 1.0 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 34 |  |
| switch | 0 |  |
| transformer | 34 | Dyn11×34 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 60 | 59 | 10 | 0 |
| LV_236V | 236.0 V | 456 | 422 | 844 | 0 |

**Transformer transitions:**

- `28_MVLV41525_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55213_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV58411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV81483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV81226_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47184_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV29872_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55165_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV82024_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV81418_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV07864_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55212_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV61912_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41435_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41794_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV81985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84959_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20389_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV58802_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV00201_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55204_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26586_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV07814_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80646_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV72690_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV61873_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV05208_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV65502_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV29876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42770_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV64272_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20274_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV11615_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42216_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 208 |
| Tree depth (max hops) | 47 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 516 | 1 | 515 | 0 | 0 | 0 |
| Tier LV_236V | 456 | 34 | 422 | 0 | 0 | 0 |
| Tier MV_11.8kV | 60 | 1 | 59 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 34; skipped invalid branches: 0.

Galvanic zones: 35; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_MVBus59485 | MV_11.8kV | 60 | 0 | 0 | 34 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2004 declared bus terminals; 1865 mapped line/closed-switch conductor edges; 139 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 47700.0 | 3.276 | 2562 |
| q_nom | 0.0 | 14300.0 | 3.276 | 2562 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.773 | 1030.0 | 1.27 | 481 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.736 | 34 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 545 of 854 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759538_consumption' has phase imbalance of 32.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759690_consumption' has phase imbalance of 234.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759694_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759846_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890269_consumption' has phase imbalance of 189.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759798_consumption' has phase imbalance of 90.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759550_consumption' has phase imbalance of 228.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759716_consumption' has phase imbalance of 45.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853800_consumption' has phase imbalance of 198.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759493_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759821_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759835_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759495_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759837_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916254_consumption' has phase imbalance of 258.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759582_consumption' has phase imbalance of 20.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759898_consumption' has phase imbalance of 266.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759832_consumption' has phase imbalance of 121.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759528_consumption' has phase imbalance of 21.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759516_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759869_consumption' has phase imbalance of 40.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759561_consumption' has phase imbalance of 180.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759505_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759763_consumption' has phase imbalance of 173.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759862_consumption' has phase imbalance of 43.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759777_consumption' has phase imbalance of 103.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759518_consumption' has phase imbalance of 240.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759903_consumption' has phase imbalance of 149.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus899818_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759881_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759774_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759688_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759793_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759853_consumption' has phase imbalance of 287.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759667_consumption' has phase imbalance of 224.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759873_consumption' has phase imbalance of 91.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853799_consumption' has phase imbalance of 258.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759586_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759785_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759519_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus928329_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759826_consumption' has phase imbalance of 128.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759587_consumption' has phase imbalance of 285.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759544_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759815_consumption' has phase imbalance of 108.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759712_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886405_consumption' has phase imbalance of 22.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759530_consumption' has phase imbalance of 73.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759831_consumption' has phase imbalance of 254.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759659_consumption' has phase imbalance of 44.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759742_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759710_consumption' has phase imbalance of 28.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus956277_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus928328_consumption' has phase imbalance of 111.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759642_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759626_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759485_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759863_consumption' has phase imbalance of 119.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759877_consumption' has phase imbalance of 68.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916244_consumption' has phase imbalance of 125.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886408_consumption' has phase imbalance of 198.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759692_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759801_consumption' has phase imbalance of 83.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759590_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus859879_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916251_consumption' has phase imbalance of 291.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759459_consumption' has phase imbalance of 232.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759563_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759906_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759915_consumption' has phase imbalance of 248.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759647_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759914_consumption' has phase imbalance of 24.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759872_consumption' has phase imbalance of 180.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759664_consumption' has phase imbalance of 118.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759522_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759574_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759573_consumption' has phase imbalance of 52.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916246_consumption' has phase imbalance of 176.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759905_consumption' has phase imbalance of 148.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759641_consumption' has phase imbalance of 32.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759649_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759652_consumption' has phase imbalance of 64.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759699_consumption' has phase imbalance of 212.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916245_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759624_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759599_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759856_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759865_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759497_consumption' has phase imbalance of 281.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759572_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759618_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759654_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759802_consumption' has phase imbalance of 251.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus956276_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759532_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759560_consumption' has phase imbalance of 145.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759639_consumption' has phase imbalance of 250.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886402_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759568_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759827_consumption' has phase imbalance of 243.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759907_consumption' has phase imbalance of 140.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus859880_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916253_consumption' has phase imbalance of 170.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759900_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759691_consumption' has phase imbalance of 94.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759665_consumption' has phase imbalance of 106.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759548_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759857_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759779_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759735_consumption' has phase imbalance of 142.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759578_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759653_consumption' has phase imbalance of 85.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759795_consumption' has phase imbalance of 144.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759546_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759819_consumption' has phase imbalance of 47.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759807_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759491_consumption' has phase imbalance of 274.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759902_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759840_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886411_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759612_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759803_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus956275_consumption' has phase imbalance of 290.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759488_consumption' has phase imbalance of 286.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759669_consumption' has phase imbalance of 288.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759646_consumption' has phase imbalance of 107.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759767_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus887155_consumption' has phase imbalance of 281.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759455_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759734_consumption' has phase imbalance of 109.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus956278_consumption' has phase imbalance of 47.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759484_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759923_consumption' has phase imbalance of 238.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759569_consumption' has phase imbalance of 233.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759828_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus908535_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759614_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759547_consumption' has phase imbalance of 156.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus887584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759536_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759926_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759876_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759896_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759874_consumption' has phase imbalance of 78.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759885_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus873115_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759589_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759844_consumption' has phase imbalance of 261.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759656_consumption' has phase imbalance of 186.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759697_consumption' has phase imbalance of 230.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759780_consumption' has phase imbalance of 153.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759651_consumption' has phase imbalance of 242.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759571_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759760_consumption' has phase imbalance of 199.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759575_consumption' has phase imbalance of 45.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759605_consumption' has phase imbalance of 241.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759483_consumption' has phase imbalance of 244.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759921_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759631_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759577_consumption' has phase imbalance of 38.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759830_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759529_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759617_consumption' has phase imbalance of 196.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759510_consumption' has phase imbalance of 292.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759810_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759565_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759899_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759526_consumption' has phase imbalance of 275.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759668_consumption' has phase imbalance of 84.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759794_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759686_consumption' has phase imbalance of 70.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759689_consumption' has phase imbalance of 119.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759621_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus928330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759494_consumption' has phase imbalance of 295.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759498_consumption' has phase imbalance of 247.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759829_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759566_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759796_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759824_consumption' has phase imbalance of 212.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759525_consumption' has phase imbalance of 234.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759727_consumption' has phase imbalance of 80.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759644_consumption' has phase imbalance of 156.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759636_consumption' has phase imbalance of 20.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759791_consumption' has phase imbalance of 215.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759534_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759925_consumption' has phase imbalance of 245.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759540_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759787_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759570_consumption' has phase imbalance of 165.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus859877_consumption' has phase imbalance of 183.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759725_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759553_consumption' has phase imbalance of 105.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759562_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759521_consumption' has phase imbalance of 88.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus887156_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759622_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759492_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759882_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853401_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759715_consumption' has phase imbalance of 105.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus916243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759558_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759580_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus759504_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 854 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_TOUQU' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus759465' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus759461' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus759673' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.347 MW |
| Total load Q | 1.0 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV41525_Transformer | 176.0 kVA | 16.3% |
| 28_MVLV55213_Transformer | 176.0 kVA | 12.4% |
| 28_MVLV58411_Transformer | 176.0 kVA | 15.8% |
| 28_MVLV81483_Transformer | 275.0 kVA | 36.2% |
| 28_MVLV81226_Transformer | 440.0 kVA | 46.1% |
| 28_MVLV47184_Transformer | 110.0 kVA | 12.6% |
| 28_MVLV29872_Transformer | 176.0 kVA | 32.8% |
| 28_MVLV55165_Transformer | 440.0 kVA | 69.6% |
| 28_MVLV82024_Transformer | 110.0 kVA | 2.8% |
| 28_MVLV81418_Transformer | 176.0 kVA | 20.2% |
| 28_MVLV07864_Transformer | 440.0 kVA | 17.3% |
| 28_MVLV55212_Transformer | 693.0 kVA | 45.2% |
| 28_MVLV61912_Transformer | 275.0 kVA | 9.5% |
| 28_MVLV41435_Transformer | 275.0 kVA | 21.5% |
| 28_MVLV41794_Transformer | 110.0 kVA | 22.1% |
| 28_MVLV81985_Transformer | 176.0 kVA | 5.0% |
| 28_MVLV84959_Transformer | 176.0 kVA | 25.0% |
| 28_MVLV20389_Transformer | 440.0 kVA | 41.0% |
| 28_MVLV58802_Transformer | 110.0 kVA | 6.3% |
| 28_MVLV00201_Transformer | 110.0 kVA | 7.2% |
| 28_MVLV55204_Transformer | 693.0 kVA | 38.5% |
| 28_MVLV26586_Transformer | 275.0 kVA | 17.7% |
| 28_MVLV07814_Transformer | 1.1 MVA | 41.8% |
| 28_MVLV80646_Transformer | 440.0 kVA | 20.9% |
| 28_MVLV72690_Transformer | 275.0 kVA | 6.1% |
| 28_MVLV61873_Transformer | 176.0 kVA | 23.8% |
| 28_MVLV05208_Transformer | 275.0 kVA | 12.5% |
| 28_MVLV65502_Transformer | 110.0 kVA | 7.6% |
| 28_MVLV29876_Transformer | 693.0 kVA | 31.2% |
| 28_MVLV42770_Transformer | 110.0 kVA | 14.8% |
| 28_MVLV64272_Transformer | 693.0 kVA | 57.8% |
| 28_MVLV20274_Transformer | 176.0 kVA | 23.8% |
| 28_MVLV11615_Transformer | 275.0 kVA | 13.1% |
| 28_MVLV42216_Transformer | 275.0 kVA | 45.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.35 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 516 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 516 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 34 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 60 |
| LV_236V | 4-wire | 456 / 456 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 456 |
| Neutral branches | 422 |
| Grounding points | 34 |
| Neutral sections | 34 |
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
| 11.78 kV | 60 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 56 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 55 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 35 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1100.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 456 / 60 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 546 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 546 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus759454_consumption, 28_LVBus759454_production, 28_LVBus759455_production, 28_LVBus759457_consumption, 28_LVBus759457_production, 28_LVBus759458_consumption, 28_LVBus759458_production, 28_LVBus759459_production, 28_LVBus759461_consumption, 28_LVBus759461_production, 28_LVBus759463_production, 28_LVBus759465_production, 28_LVBus759467_consumption, 28_LVBus759467_production, 28_LVBus759468_consumption, 28_LVBus759468_production, 28_LVBus759469_consumption, 28_LVBus759469_production, 28_LVBus759470_consumption, 28_LVBus759470_production, 28_LVBus759471_production, 28_LVBus759472_production, 28_LVBus759473_production, 28_LVBus759475_production, 28_LVBus759477_production, 28_LVBus759479_consumption, 28_LVBus759479_production, 28_LVBus759480_production, 28_LVBus759481_consumption, 28_LVBus759481_production, 28_LVBus759482_consumption, 28_LVBus759482_production, 28_LVBus759483_production, 28_LVBus759484_production, 28_LVBus759485_production, 28_LVBus759487_production, 28_LVBus759488_production, 28_LVBus759490_consumption, 28_LVBus759490_production, 28_LVBus759491_production, 28_LVBus759492_production, 28_LVBus759493_production, 28_LVBus759494_production, 28_LVBus759495_production, 28_LVBus759496_production, 28_LVBus759497_production, 28_LVBus759498_production, 28_LVBus759500_consumption, 28_LVBus759500_production, 28_LVBus759502_production, 28_LVBus759504_production, 28_LVBus759505_production, 28_LVBus759506_production, 28_LVBus759507_consumption, 28_LVBus759507_production, 28_LVBus759508_consumption, 28_LVBus759508_production, 28_LVBus759509_consumption, 28_LVBus759509_production, 28_LVBus759510_production, 28_LVBus759511_consumption, 28_LVBus759511_production, 28_LVBus759512_production, 28_LVBus759514_consumption, 28_LVBus759514_production, 28_LVBus759515_consumption, 28_LVBus759515_production, 28_LVBus759516_production, 28_LVBus759518_production, 28_LVBus759519_production, 28_LVBus759521_production, 28_LVBus759522_production, 28_LVBus759523_production, 28_LVBus759525_production, 28_LVBus759526_production, 28_LVBus759528_production, 28_LVBus759529_production, 28_LVBus759530_production, 28_LVBus759532_production, 28_LVBus759534_production, 28_LVBus759536_production, 28_LVBus759538_production, 28_LVBus759540_production, 28_LVBus759542_consumption, 28_LVBus759542_production, 28_LVBus759544_production, 28_LVBus759546_production, 28_LVBus759547_production, 28_LVBus759548_production, 28_LVBus759549_consumption, 28_LVBus759549_production, 28_LVBus759550_production, 28_LVBus759551_production, 28_LVBus759553_production, 28_LVBus759555_consumption, 28_LVBus759555_production, 28_LVBus759556_production, 28_LVBus759558_production, 28_LVBus759559_production, 28_LVBus759560_production, 28_LVBus759561_production, 28_LVBus759562_production, 28_LVBus759563_production, 28_LVBus759565_production, 28_LVBus759566_production, 28_LVBus759568_production, 28_LVBus759569_production, 28_LVBus759570_production, 28_LVBus759571_production, 28_LVBus759572_production, 28_LVBus759573_production, 28_LVBus759574_production, 28_LVBus759575_production, 28_LVBus759577_production, 28_LVBus759578_production, 28_LVBus759579_consumption, 28_LVBus759579_production, 28_LVBus759580_production, 28_LVBus759581_production, 28_LVBus759582_production, 28_LVBus759586_production, 28_LVBus759587_production, 28_LVBus759588_consumption, 28_LVBus759588_production, 28_LVBus759589_production, 28_LVBus759590_production, 28_LVBus759591_consumption, 28_LVBus759591_production, 28_LVBus759592_consumption, 28_LVBus759592_production, 28_LVBus759593_production, 28_LVBus759594_production, 28_LVBus759596_consumption, 28_LVBus759596_production, 28_LVBus759597_production, 28_LVBus759598_consumption, 28_LVBus759598_production, 28_LVBus759599_production, 28_LVBus759604_production, 28_LVBus759605_production, 28_LVBus759606_production, 28_LVBus759607_production, 28_LVBus759609_consumption, 28_LVBus759609_production, 28_LVBus759610_consumption, 28_LVBus759610_production, 28_LVBus759612_production, 28_LVBus759614_production, 28_LVBus759615_consumption, 28_LVBus759615_production, 28_LVBus759617_production, 28_LVBus759618_production, 28_LVBus759619_production, 28_LVBus759621_production, 28_LVBus759622_production, 28_LVBus759623_production, 28_LVBus759624_production, 28_LVBus759626_production, 28_LVBus759628_consumption, 28_LVBus759628_production, 28_LVBus759629_consumption, 28_LVBus759629_production, 28_LVBus759630_production, 28_LVBus759631_production, 28_LVBus759635_consumption, 28_LVBus759635_production, 28_LVBus759636_production, 28_LVBus759637_consumption, 28_LVBus759637_production, 28_LVBus759639_production, 28_LVBus759640_production, 28_LVBus759641_production, 28_LVBus759642_production, 28_LVBus759643_consumption, 28_LVBus759643_production, 28_LVBus759644_production, 28_LVBus759646_production, 28_LVBus759647_production, 28_LVBus759648_consumption, 28_LVBus759648_production, 28_LVBus759649_production, 28_LVBus759650_consumption, 28_LVBus759650_production, 28_LVBus759651_production, 28_LVBus759652_production, 28_LVBus759653_production, 28_LVBus759654_production, 28_LVBus759655_production, 28_LVBus759656_production, 28_LVBus759658_consumption, 28_LVBus759658_production, 28_LVBus759659_production, 28_LVBus759661_consumption, 28_LVBus759661_production, 28_LVBus759663_consumption, 28_LVBus759663_production, 28_LVBus759664_production, 28_LVBus759665_production, 28_LVBus759667_production, 28_LVBus759668_production, 28_LVBus759669_production, 28_LVBus759673_production, 28_LVBus759675_production, 28_LVBus759677_production, 28_LVBus759679_production, 28_LVBus759681_consumption, 28_LVBus759681_production, 28_LVBus759683_production, 28_LVBus759685_production, 28_LVBus759686_production, 28_LVBus759687_consumption, 28_LVBus759687_production, 28_LVBus759688_production, 28_LVBus759689_production, 28_LVBus759690_production, 28_LVBus759691_production, 28_LVBus759692_production, 28_LVBus759693_production, 28_LVBus759694_production, 28_LVBus759695_consumption, 28_LVBus759695_production, 28_LVBus759696_production, 28_LVBus759697_production, 28_LVBus759699_production, 28_LVBus759701_production, 28_LVBus759702_production, 28_LVBus759703_consumption, 28_LVBus759703_production, 28_LVBus759704_production, 28_LVBus759705_consumption, 28_LVBus759705_production, 28_LVBus759707_production, 28_LVBus759708_production, 28_LVBus759709_production, 28_LVBus759710_production, 28_LVBus759711_consumption, 28_LVBus759711_production, 28_LVBus759712_production, 28_LVBus759713_production, 28_LVBus759714_consumption, 28_LVBus759714_production, 28_LVBus759715_production, 28_LVBus759716_production, 28_LVBus759717_consumption, 28_LVBus759717_production, 28_LVBus759718_consumption, 28_LVBus759718_production, 28_LVBus759719_production, 28_LVBus759721_consumption, 28_LVBus759721_production, 28_LVBus759722_consumption, 28_LVBus759722_production, 28_LVBus759723_consumption, 28_LVBus759723_production, 28_LVBus759724_consumption, 28_LVBus759724_production, 28_LVBus759725_production, 28_LVBus759727_production, 28_LVBus759728_consumption, 28_LVBus759728_production, 28_LVBus759730_consumption, 28_LVBus759730_production, 28_LVBus759731_consumption, 28_LVBus759731_production, 28_LVBus759732_consumption, 28_LVBus759732_production, 28_LVBus759734_production, 28_LVBus759735_production, 28_LVBus759736_production, 28_LVBus759737_production, 28_LVBus759741_consumption, 28_LVBus759741_production, 28_LVBus759742_production, 28_LVBus759744_consumption, 28_LVBus759744_production, 28_LVBus759745_production, 28_LVBus759748_production, 28_LVBus759749_consumption, 28_LVBus759749_production, 28_LVBus759750_production, 28_LVBus759751_consumption, 28_LVBus759751_production, 28_LVBus759752_production, 28_LVBus759753_production, 28_LVBus759755_production, 28_LVBus759756_consumption, 28_LVBus759756_production, 28_LVBus759758_production, 28_LVBus759759_consumption, 28_LVBus759759_production, 28_LVBus759760_production, 28_LVBus759761_consumption, 28_LVBus759761_production, 28_LVBus759763_production, 28_LVBus759765_consumption, 28_LVBus759765_production, 28_LVBus759767_production, 28_LVBus759771_production, 28_LVBus759773_consumption, 28_LVBus759773_production, 28_LVBus759774_production, 28_LVBus759776_production, 28_LVBus759777_production, 28_LVBus759778_production, 28_LVBus759779_production, 28_LVBus759780_production, 28_LVBus759781_production, 28_LVBus759783_production, 28_LVBus759784_production, 28_LVBus759785_production, 28_LVBus759786_production, 28_LVBus759787_production, 28_LVBus759788_production, 28_LVBus759789_production, 28_LVBus759790_production, 28_LVBus759791_production, 28_LVBus759793_production, 28_LVBus759794_production, 28_LVBus759795_production, 28_LVBus759796_production, 28_LVBus759798_production, 28_LVBus759799_consumption, 28_LVBus759799_production, 28_LVBus759801_production, 28_LVBus759802_production, 28_LVBus759803_production, 28_LVBus759804_consumption, 28_LVBus759804_production, 28_LVBus759805_consumption, 28_LVBus759805_production, 28_LVBus759806_production, 28_LVBus759807_production, 28_LVBus759809_consumption, 28_LVBus759809_production, 28_LVBus759810_production, 28_LVBus759811_consumption, 28_LVBus759811_production, 28_LVBus759812_consumption, 28_LVBus759812_production, 28_LVBus759813_consumption, 28_LVBus759813_production, 28_LVBus759814_consumption, 28_LVBus759814_production, 28_LVBus759815_production, 28_LVBus759816_consumption, 28_LVBus759816_production, 28_LVBus759817_consumption, 28_LVBus759817_production, 28_LVBus759818_consumption, 28_LVBus759818_production, 28_LVBus759819_production, 28_LVBus759820_consumption, 28_LVBus759820_production, 28_LVBus759821_production, 28_LVBus759822_production, 28_LVBus759823_consumption, 28_LVBus759823_production, 28_LVBus759824_production, 28_LVBus759826_production, 28_LVBus759827_production, 28_LVBus759828_production, 28_LVBus759829_production, 28_LVBus759830_production, 28_LVBus759831_production, 28_LVBus759832_production, 28_LVBus759833_production, 28_LVBus759835_production, 28_LVBus759836_production, 28_LVBus759837_production, 28_LVBus759838_consumption, 28_LVBus759838_production, 28_LVBus759840_production, 28_LVBus759842_consumption, 28_LVBus759842_production, 28_LVBus759844_production, 28_LVBus759845_consumption, 28_LVBus759845_production, 28_LVBus759846_production, 28_LVBus759847_production, 28_LVBus759849_consumption, 28_LVBus759849_production, 28_LVBus759851_production, 28_LVBus759853_production, 28_LVBus759854_production, 28_LVBus759856_production, 28_LVBus759857_production, 28_LVBus759858_production, 28_LVBus759859_consumption, 28_LVBus759859_production, 28_LVBus759861_production, 28_LVBus759862_production, 28_LVBus759863_production, 28_LVBus759865_production, 28_LVBus759866_consumption, 28_LVBus759866_production, 28_LVBus759868_production, 28_LVBus759869_production, 28_LVBus759871_consumption, 28_LVBus759871_production, 28_LVBus759872_production, 28_LVBus759873_production, 28_LVBus759874_production, 28_LVBus759876_production, 28_LVBus759877_production, 28_LVBus759879_consumption, 28_LVBus759879_production, 28_LVBus759880_consumption, 28_LVBus759880_production, 28_LVBus759881_production, 28_LVBus759882_production, 28_LVBus759883_production, 28_LVBus759884_consumption, 28_LVBus759884_production, 28_LVBus759885_production, 28_LVBus759886_production, 28_LVBus759887_consumption, 28_LVBus759887_production, 28_LVBus759888_consumption, 28_LVBus759888_production, 28_LVBus759889_production, 28_LVBus759890_production, 28_LVBus759891_consumption, 28_LVBus759891_production, 28_LVBus759892_production, 28_LVBus759896_production, 28_LVBus759898_production, 28_LVBus759899_production, 28_LVBus759900_production, 28_LVBus759902_production, 28_LVBus759903_production, 28_LVBus759905_production, 28_LVBus759906_production, 28_LVBus759907_production, 28_LVBus759909_production, 28_LVBus759910_consumption, 28_LVBus759910_production, 28_LVBus759911_production, 28_LVBus759913_consumption, 28_LVBus759913_production, 28_LVBus759914_production, 28_LVBus759915_production, 28_LVBus759917_consumption, 28_LVBus759917_production, 28_LVBus759918_production, 28_LVBus759920_consumption, 28_LVBus759920_production, 28_LVBus759921_production, 28_LVBus759923_production, 28_LVBus759924_consumption, 28_LVBus759924_production, 28_LVBus759925_production, 28_LVBus759926_production, 28_LVBus759927_production, 28_LVBus759928_production, 28_LVBus853401_production, 28_LVBus853402_consumption, 28_LVBus853402_production, 28_LVBus853403_production, 28_LVBus853799_production, 28_LVBus853800_production, 28_LVBus859877_production, 28_LVBus859878_consumption, 28_LVBus859878_production, 28_LVBus859879_production, 28_LVBus859880_production, 28_LVBus873113_consumption, 28_LVBus873113_production, 28_LVBus873114_production, 28_LVBus873115_production, 28_LVBus880913_consumption, 28_LVBus880913_production, 28_LVBus882185_consumption, 28_LVBus882185_production, 28_LVBus886401_consumption, 28_LVBus886401_production, 28_LVBus886402_production, 28_LVBus886403_production, 28_LVBus886404_production, 28_LVBus886405_production, 28_LVBus886406_production, 28_LVBus886407_production, 28_LVBus886408_production, 28_LVBus886409_consumption, 28_LVBus886409_production, 28_LVBus886410_production, 28_LVBus886411_production, 28_LVBus886412_consumption, 28_LVBus886412_production, 28_LVBus887155_production, 28_LVBus887156_production, 28_LVBus887157_consumption, 28_LVBus887157_production, 28_LVBus887584_production, 28_LVBus890266_production, 28_LVBus890267_production, 28_LVBus890268_production, 28_LVBus890269_production, 28_LVBus890270_production, 28_LVBus899818_production, 28_LVBus908535_production, 28_LVBus912379_production, 28_LVBus914265_consumption, 28_LVBus914265_production, 28_LVBus914266_consumption, 28_LVBus914266_production, 28_LVBus916240_consumption, 28_LVBus916240_production, 28_LVBus916241_consumption, 28_LVBus916241_production, 28_LVBus916242_consumption, 28_LVBus916242_production, 28_LVBus916243_production, 28_LVBus916244_production, 28_LVBus916245_production, 28_LVBus916246_production, 28_LVBus916247_production, 28_LVBus916248_production, 28_LVBus916249_production, 28_LVBus916250_production, 28_LVBus916251_production, 28_LVBus916252_production, 28_LVBus916253_production, 28_LVBus916254_production, 28_LVBus922180_production, 28_LVBus928328_production, 28_LVBus928329_production, 28_LVBus928330_production, 28_LVBus931597_consumption, 28_LVBus931597_production, 28_LVBus936956_consumption, 28_LVBus936956_production, 28_LVBus956275_production, 28_LVBus956276_production, 28_LVBus956277_production, 28_LVBus956278_production, 28_LVBus956888_consumption, 28_LVBus956888_production, 28_MVLV24182_consumption, 28_MVLV24182_production, 28_MVLV26163_production, 28_MVLV43992_consumption, 28_MVLV43992_production, 28_MVLV58423_consumption, 28_MVLV58423_production, 28_MVLV82232_consumption, 28_MVLV82232_production.

## 9. Data Quality Summary

**Total findings:** 305 (0 errors, 4 warnings, 301 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  545 of 854 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.35 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  546 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759538_consumption`  
  Load '28_LVBus759538_consumption' has phase imbalance of 32.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759690_consumption`  
  Load '28_LVBus759690_consumption' has phase imbalance of 234.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759694_consumption`  
  Load '28_LVBus759694_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759846_consumption`  
  Load '28_LVBus759846_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890269_consumption`  
  Load '28_LVBus890269_consumption' has phase imbalance of 189.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759798_consumption`  
  Load '28_LVBus759798_consumption' has phase imbalance of 90.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759550_consumption`  
  Load '28_LVBus759550_consumption' has phase imbalance of 228.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759716_consumption`  
  Load '28_LVBus759716_consumption' has phase imbalance of 45.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853800_consumption`  
  Load '28_LVBus853800_consumption' has phase imbalance of 198.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759833_consumption`  
  Load '28_LVBus759833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759493_consumption`  
  Load '28_LVBus759493_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759821_consumption`  
  Load '28_LVBus759821_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759835_consumption`  
  Load '28_LVBus759835_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759495_consumption`  
  Load '28_LVBus759495_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759837_consumption`  
  Load '28_LVBus759837_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916254_consumption`  
  Load '28_LVBus916254_consumption' has phase imbalance of 258.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759582_consumption`  
  Load '28_LVBus759582_consumption' has phase imbalance of 20.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759898_consumption`  
  Load '28_LVBus759898_consumption' has phase imbalance of 266.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759551_consumption`  
  Load '28_LVBus759551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759832_consumption`  
  Load '28_LVBus759832_consumption' has phase imbalance of 121.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759528_consumption`  
  Load '28_LVBus759528_consumption' has phase imbalance of 21.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759516_consumption`  
  Load '28_LVBus759516_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759869_consumption`  
  Load '28_LVBus759869_consumption' has phase imbalance of 40.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759561_consumption`  
  Load '28_LVBus759561_consumption' has phase imbalance of 180.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759496_consumption`  
  Load '28_LVBus759496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759505_consumption`  
  Load '28_LVBus759505_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759763_consumption`  
  Load '28_LVBus759763_consumption' has phase imbalance of 173.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759862_consumption`  
  Load '28_LVBus759862_consumption' has phase imbalance of 43.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759750_consumption`  
  Load '28_LVBus759750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759890_consumption`  
  Load '28_LVBus759890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759784_consumption`  
  Load '28_LVBus759784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759918_consumption`  
  Load '28_LVBus759918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759777_consumption`  
  Load '28_LVBus759777_consumption' has phase imbalance of 103.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916247_consumption`  
  Load '28_LVBus916247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759518_consumption`  
  Load '28_LVBus759518_consumption' has phase imbalance of 240.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759903_consumption`  
  Load '28_LVBus759903_consumption' has phase imbalance of 149.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus899818_consumption`  
  Load '28_LVBus899818_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759881_consumption`  
  Load '28_LVBus759881_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759774_consumption`  
  Load '28_LVBus759774_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759688_consumption`  
  Load '28_LVBus759688_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759487_consumption`  
  Load '28_LVBus759487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759701_consumption`  
  Load '28_LVBus759701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759793_consumption`  
  Load '28_LVBus759793_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759853_consumption`  
  Load '28_LVBus759853_consumption' has phase imbalance of 287.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759667_consumption`  
  Load '28_LVBus759667_consumption' has phase imbalance of 224.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916250_consumption`  
  Load '28_LVBus916250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759873_consumption`  
  Load '28_LVBus759873_consumption' has phase imbalance of 91.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853799_consumption`  
  Load '28_LVBus853799_consumption' has phase imbalance of 258.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759586_consumption`  
  Load '28_LVBus759586_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759785_consumption`  
  Load '28_LVBus759785_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759736_consumption`  
  Load '28_LVBus759736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759519_consumption`  
  Load '28_LVBus759519_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus928329_consumption`  
  Load '28_LVBus928329_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759826_consumption`  
  Load '28_LVBus759826_consumption' has phase imbalance of 128.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759587_consumption`  
  Load '28_LVBus759587_consumption' has phase imbalance of 285.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759822_consumption`  
  Load '28_LVBus759822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759693_consumption`  
  Load '28_LVBus759693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759544_consumption`  
  Load '28_LVBus759544_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759815_consumption`  
  Load '28_LVBus759815_consumption' has phase imbalance of 108.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759712_consumption`  
  Load '28_LVBus759712_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759619_consumption`  
  Load '28_LVBus759619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886405_consumption`  
  Load '28_LVBus886405_consumption' has phase imbalance of 22.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759530_consumption`  
  Load '28_LVBus759530_consumption' has phase imbalance of 73.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759831_consumption`  
  Load '28_LVBus759831_consumption' has phase imbalance of 254.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759758_consumption`  
  Load '28_LVBus759758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759659_consumption`  
  Load '28_LVBus759659_consumption' has phase imbalance of 44.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759752_consumption`  
  Load '28_LVBus759752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759742_consumption`  
  Load '28_LVBus759742_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759480_consumption`  
  Load '28_LVBus759480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759710_consumption`  
  Load '28_LVBus759710_consumption' has phase imbalance of 28.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus956277_consumption`  
  Load '28_LVBus956277_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus928328_consumption`  
  Load '28_LVBus928328_consumption' has phase imbalance of 111.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759702_consumption`  
  Load '28_LVBus759702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759642_consumption`  
  Load '28_LVBus759642_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759626_consumption`  
  Load '28_LVBus759626_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759485_consumption`  
  Load '28_LVBus759485_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759889_consumption`  
  Load '28_LVBus759889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759863_consumption`  
  Load '28_LVBus759863_consumption' has phase imbalance of 119.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759877_consumption`  
  Load '28_LVBus759877_consumption' has phase imbalance of 68.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916244_consumption`  
  Load '28_LVBus916244_consumption' has phase imbalance of 125.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886408_consumption`  
  Load '28_LVBus886408_consumption' has phase imbalance of 198.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759692_consumption`  
  Load '28_LVBus759692_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890270_consumption`  
  Load '28_LVBus890270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853403_consumption`  
  Load '28_LVBus853403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759801_consumption`  
  Load '28_LVBus759801_consumption' has phase imbalance of 83.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759590_consumption`  
  Load '28_LVBus759590_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759778_consumption`  
  Load '28_LVBus759778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759655_consumption`  
  Load '28_LVBus759655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759786_consumption`  
  Load '28_LVBus759786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus859879_consumption`  
  Load '28_LVBus859879_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759753_consumption`  
  Load '28_LVBus759753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916251_consumption`  
  Load '28_LVBus916251_consumption' has phase imbalance of 291.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759459_consumption`  
  Load '28_LVBus759459_consumption' has phase imbalance of 232.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759563_consumption`  
  Load '28_LVBus759563_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759906_consumption`  
  Load '28_LVBus759906_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759607_consumption`  
  Load '28_LVBus759607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759915_consumption`  
  Load '28_LVBus759915_consumption' has phase imbalance of 248.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759789_consumption`  
  Load '28_LVBus759789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759647_consumption`  
  Load '28_LVBus759647_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759708_consumption`  
  Load '28_LVBus759708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759911_consumption`  
  Load '28_LVBus759911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759914_consumption`  
  Load '28_LVBus759914_consumption' has phase imbalance of 24.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759872_consumption`  
  Load '28_LVBus759872_consumption' has phase imbalance of 180.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759664_consumption`  
  Load '28_LVBus759664_consumption' has phase imbalance of 118.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759755_consumption`  
  Load '28_LVBus759755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759522_consumption`  
  Load '28_LVBus759522_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759574_consumption`  
  Load '28_LVBus759574_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759581_consumption`  
  Load '28_LVBus759581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759573_consumption`  
  Load '28_LVBus759573_consumption' has phase imbalance of 52.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916246_consumption`  
  Load '28_LVBus916246_consumption' has phase imbalance of 176.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759781_consumption`  
  Load '28_LVBus759781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759905_consumption`  
  Load '28_LVBus759905_consumption' has phase imbalance of 148.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759641_consumption`  
  Load '28_LVBus759641_consumption' has phase imbalance of 32.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759649_consumption`  
  Load '28_LVBus759649_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759652_consumption`  
  Load '28_LVBus759652_consumption' has phase imbalance of 64.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759699_consumption`  
  Load '28_LVBus759699_consumption' has phase imbalance of 212.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916245_consumption`  
  Load '28_LVBus916245_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759624_consumption`  
  Load '28_LVBus759624_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759604_consumption`  
  Load '28_LVBus759604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759788_consumption`  
  Load '28_LVBus759788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759748_consumption`  
  Load '28_LVBus759748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759599_consumption`  
  Load '28_LVBus759599_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759856_consumption`  
  Load '28_LVBus759856_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759776_consumption`  
  Load '28_LVBus759776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759707_consumption`  
  Load '28_LVBus759707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759851_consumption`  
  Load '28_LVBus759851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759745_consumption`  
  Load '28_LVBus759745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759865_consumption`  
  Load '28_LVBus759865_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759497_consumption`  
  Load '28_LVBus759497_consumption' has phase imbalance of 281.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759572_consumption`  
  Load '28_LVBus759572_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759909_consumption`  
  Load '28_LVBus759909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759737_consumption`  
  Load '28_LVBus759737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759618_consumption`  
  Load '28_LVBus759618_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759654_consumption`  
  Load '28_LVBus759654_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759802_consumption`  
  Load '28_LVBus759802_consumption' has phase imbalance of 251.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus956276_consumption`  
  Load '28_LVBus956276_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759532_consumption`  
  Load '28_LVBus759532_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759560_consumption`  
  Load '28_LVBus759560_consumption' has phase imbalance of 145.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759639_consumption`  
  Load '28_LVBus759639_consumption' has phase imbalance of 250.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886402_consumption`  
  Load '28_LVBus886402_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759568_consumption`  
  Load '28_LVBus759568_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759827_consumption`  
  Load '28_LVBus759827_consumption' has phase imbalance of 243.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759523_consumption`  
  Load '28_LVBus759523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759847_consumption`  
  Load '28_LVBus759847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759907_consumption`  
  Load '28_LVBus759907_consumption' has phase imbalance of 140.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus859880_consumption`  
  Load '28_LVBus859880_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916253_consumption`  
  Load '28_LVBus916253_consumption' has phase imbalance of 170.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759900_consumption`  
  Load '28_LVBus759900_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759691_consumption`  
  Load '28_LVBus759691_consumption' has phase imbalance of 94.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759665_consumption`  
  Load '28_LVBus759665_consumption' has phase imbalance of 106.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759548_consumption`  
  Load '28_LVBus759548_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759696_consumption`  
  Load '28_LVBus759696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759857_consumption`  
  Load '28_LVBus759857_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759779_consumption`  
  Load '28_LVBus759779_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759886_consumption`  
  Load '28_LVBus759886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759735_consumption`  
  Load '28_LVBus759735_consumption' has phase imbalance of 142.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759578_consumption`  
  Load '28_LVBus759578_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759653_consumption`  
  Load '28_LVBus759653_consumption' has phase imbalance of 85.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759795_consumption`  
  Load '28_LVBus759795_consumption' has phase imbalance of 144.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759623_consumption`  
  Load '28_LVBus759623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759546_consumption`  
  Load '28_LVBus759546_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759819_consumption`  
  Load '28_LVBus759819_consumption' has phase imbalance of 47.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759806_consumption`  
  Load '28_LVBus759806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886406_consumption`  
  Load '28_LVBus886406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759807_consumption`  
  Load '28_LVBus759807_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759491_consumption`  
  Load '28_LVBus759491_consumption' has phase imbalance of 274.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759902_consumption`  
  Load '28_LVBus759902_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759840_consumption`  
  Load '28_LVBus759840_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886411_consumption`  
  Load '28_LVBus886411_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759612_consumption`  
  Load '28_LVBus759612_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759803_consumption`  
  Load '28_LVBus759803_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus956275_consumption`  
  Load '28_LVBus956275_consumption' has phase imbalance of 290.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759488_consumption`  
  Load '28_LVBus759488_consumption' has phase imbalance of 286.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759669_consumption`  
  Load '28_LVBus759669_consumption' has phase imbalance of 288.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759646_consumption`  
  Load '28_LVBus759646_consumption' has phase imbalance of 107.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759767_consumption`  
  Load '28_LVBus759767_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus887155_consumption`  
  Load '28_LVBus887155_consumption' has phase imbalance of 281.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759928_consumption`  
  Load '28_LVBus759928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759512_consumption`  
  Load '28_LVBus759512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759455_consumption`  
  Load '28_LVBus759455_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759734_consumption`  
  Load '28_LVBus759734_consumption' has phase imbalance of 109.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759506_consumption`  
  Load '28_LVBus759506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus956278_consumption`  
  Load '28_LVBus956278_consumption' has phase imbalance of 47.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916252_consumption`  
  Load '28_LVBus916252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890267_consumption`  
  Load '28_LVBus890267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759484_consumption`  
  Load '28_LVBus759484_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759923_consumption`  
  Load '28_LVBus759923_consumption' has phase imbalance of 238.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890266_consumption`  
  Load '28_LVBus890266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759569_consumption`  
  Load '28_LVBus759569_consumption' has phase imbalance of 233.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759828_consumption`  
  Load '28_LVBus759828_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916248_consumption`  
  Load '28_LVBus916248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759502_consumption`  
  Load '28_LVBus759502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus908535_consumption`  
  Load '28_LVBus908535_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759614_consumption`  
  Load '28_LVBus759614_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759547_consumption`  
  Load '28_LVBus759547_consumption' has phase imbalance of 156.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus887584_consumption`  
  Load '28_LVBus887584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759536_consumption`  
  Load '28_LVBus759536_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759926_consumption`  
  Load '28_LVBus759926_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759876_consumption`  
  Load '28_LVBus759876_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759593_consumption`  
  Load '28_LVBus759593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890268_consumption`  
  Load '28_LVBus890268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759896_consumption`  
  Load '28_LVBus759896_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759874_consumption`  
  Load '28_LVBus759874_consumption' has phase imbalance of 78.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759885_consumption`  
  Load '28_LVBus759885_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus873115_consumption`  
  Load '28_LVBus873115_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759783_consumption`  
  Load '28_LVBus759783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759589_consumption`  
  Load '28_LVBus759589_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759844_consumption`  
  Load '28_LVBus759844_consumption' has phase imbalance of 261.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759656_consumption`  
  Load '28_LVBus759656_consumption' has phase imbalance of 186.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759697_consumption`  
  Load '28_LVBus759697_consumption' has phase imbalance of 230.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759780_consumption`  
  Load '28_LVBus759780_consumption' has phase imbalance of 153.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759861_consumption`  
  Load '28_LVBus759861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759704_consumption`  
  Load '28_LVBus759704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759651_consumption`  
  Load '28_LVBus759651_consumption' has phase imbalance of 242.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759571_consumption`  
  Load '28_LVBus759571_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759927_consumption`  
  Load '28_LVBus759927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759760_consumption`  
  Load '28_LVBus759760_consumption' has phase imbalance of 199.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759575_consumption`  
  Load '28_LVBus759575_consumption' has phase imbalance of 45.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759605_consumption`  
  Load '28_LVBus759605_consumption' has phase imbalance of 241.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759483_consumption`  
  Load '28_LVBus759483_consumption' has phase imbalance of 244.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759921_consumption`  
  Load '28_LVBus759921_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759631_consumption`  
  Load '28_LVBus759631_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886404_consumption`  
  Load '28_LVBus886404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759577_consumption`  
  Load '28_LVBus759577_consumption' has phase imbalance of 38.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759709_consumption`  
  Load '28_LVBus759709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759830_consumption`  
  Load '28_LVBus759830_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759713_consumption`  
  Load '28_LVBus759713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759529_consumption`  
  Load '28_LVBus759529_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759617_consumption`  
  Load '28_LVBus759617_consumption' has phase imbalance of 196.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759510_consumption`  
  Load '28_LVBus759510_consumption' has phase imbalance of 292.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759810_consumption`  
  Load '28_LVBus759810_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759565_consumption`  
  Load '28_LVBus759565_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759899_consumption`  
  Load '28_LVBus759899_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759771_consumption`  
  Load '28_LVBus759771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759594_consumption`  
  Load '28_LVBus759594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759526_consumption`  
  Load '28_LVBus759526_consumption' has phase imbalance of 275.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759668_consumption`  
  Load '28_LVBus759668_consumption' has phase imbalance of 84.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759794_consumption`  
  Load '28_LVBus759794_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759606_consumption`  
  Load '28_LVBus759606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759686_consumption`  
  Load '28_LVBus759686_consumption' has phase imbalance of 70.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759689_consumption`  
  Load '28_LVBus759689_consumption' has phase imbalance of 119.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759621_consumption`  
  Load '28_LVBus759621_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759892_consumption`  
  Load '28_LVBus759892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759854_consumption`  
  Load '28_LVBus759854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus928330_consumption`  
  Load '28_LVBus928330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759494_consumption`  
  Load '28_LVBus759494_consumption' has phase imbalance of 295.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759498_consumption`  
  Load '28_LVBus759498_consumption' has phase imbalance of 247.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759829_consumption`  
  Load '28_LVBus759829_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759566_consumption`  
  Load '28_LVBus759566_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759796_consumption`  
  Load '28_LVBus759796_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759824_consumption`  
  Load '28_LVBus759824_consumption' has phase imbalance of 212.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759525_consumption`  
  Load '28_LVBus759525_consumption' has phase imbalance of 234.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759727_consumption`  
  Load '28_LVBus759727_consumption' has phase imbalance of 80.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759597_consumption`  
  Load '28_LVBus759597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759644_consumption`  
  Load '28_LVBus759644_consumption' has phase imbalance of 156.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759636_consumption`  
  Load '28_LVBus759636_consumption' has phase imbalance of 20.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759791_consumption`  
  Load '28_LVBus759791_consumption' has phase imbalance of 215.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759534_consumption`  
  Load '28_LVBus759534_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759640_consumption`  
  Load '28_LVBus759640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759685_consumption`  
  Load '28_LVBus759685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759925_consumption`  
  Load '28_LVBus759925_consumption' has phase imbalance of 245.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759540_consumption`  
  Load '28_LVBus759540_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759787_consumption`  
  Load '28_LVBus759787_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759570_consumption`  
  Load '28_LVBus759570_consumption' has phase imbalance of 165.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus859877_consumption`  
  Load '28_LVBus859877_consumption' has phase imbalance of 183.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759725_consumption`  
  Load '28_LVBus759725_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759868_consumption`  
  Load '28_LVBus759868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759553_consumption`  
  Load '28_LVBus759553_consumption' has phase imbalance of 105.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759562_consumption`  
  Load '28_LVBus759562_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759521_consumption`  
  Load '28_LVBus759521_consumption' has phase imbalance of 88.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus887156_consumption`  
  Load '28_LVBus887156_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759622_consumption`  
  Load '28_LVBus759622_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759492_consumption`  
  Load '28_LVBus759492_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759882_consumption`  
  Load '28_LVBus759882_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853401_consumption`  
  Load '28_LVBus853401_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759715_consumption`  
  Load '28_LVBus759715_consumption' has phase imbalance of 105.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759790_consumption`  
  Load '28_LVBus759790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759836_consumption`  
  Load '28_LVBus759836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus916243_consumption`  
  Load '28_LVBus916243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759558_consumption`  
  Load '28_LVBus759558_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759580_consumption`  
  Load '28_LVBus759580_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus759504_consumption`  
  Load '28_LVBus759504_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 854 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_TOUQU' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus759465' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus759461' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus759673' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  516 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  186 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus759455_consumption, 28_LVBus759459_consumption, 28_LVBus759480_consumption, 28_LVBus759487_consumption, 28_LVBus759491_consumption, 28_LVBus759494_consumption, 28_LVBus759496_consumption, 28_LVBus759497_consumption, 28_LVBus759498_consumption, 28_LVBus759502_consumption, 28_LVBus759504_consumption, 28_LVBus759505_consumption, 28_LVBus759506_consumption, 28_LVBus759510_consumption, 28_LVBus759512_consumption, 28_LVBus759516_consumption, 28_LVBus759518_consumption, 28_LVBus759519_consumption, 28_LVBus759522_consumption, 28_LVBus759523_consumption, 28_LVBus759525_consumption, 28_LVBus759526_consumption, 28_LVBus759529_consumption, 28_LVBus759532_consumption, 28_LVBus759536_consumption, 28_LVBus759547_consumption, 28_LVBus759548_consumption, 28_LVBus759550_consumption, 28_LVBus759551_consumption, 28_LVBus759558_consumption, 28_LVBus759562_consumption, 28_LVBus759565_consumption, 28_LVBus759568_consumption, 28_LVBus759569_consumption, 28_LVBus759571_consumption, 28_LVBus759572_consumption, 28_LVBus759578_consumption, 28_LVBus759580_consumption, 28_LVBus759581_consumption, 28_LVBus759586_consumption, 28_LVBus759587_consumption, 28_LVBus759590_consumption, 28_LVBus759593_consumption, 28_LVBus759594_consumption, 28_LVBus759597_consumption, 28_LVBus759604_consumption, 28_LVBus759605_consumption, 28_LVBus759606_consumption, 28_LVBus759607_consumption, 28_LVBus759617_consumption, 28_LVBus759618_consumption, 28_LVBus759619_consumption, 28_LVBus759622_consumption, 28_LVBus759623_consumption, 28_LVBus759624_consumption, 28_LVBus759626_consumption, 28_LVBus759631_consumption, 28_LVBus759639_consumption, 28_LVBus759640_consumption, 28_LVBus759644_consumption, 28_LVBus759647_consumption, 28_LVBus759651_consumption, 28_LVBus759655_consumption, 28_LVBus759656_consumption, 28_LVBus759669_consumption, 28_LVBus759685_consumption, 28_LVBus759690_consumption, 28_LVBus759692_consumption, 28_LVBus759693_consumption, 28_LVBus759696_consumption, 28_LVBus759697_consumption, 28_LVBus759699_consumption, 28_LVBus759701_consumption, 28_LVBus759702_consumption, 28_LVBus759704_consumption, 28_LVBus759707_consumption, 28_LVBus759708_consumption, 28_LVBus759709_consumption, 28_LVBus759712_consumption, 28_LVBus759713_consumption, 28_LVBus759736_consumption, 28_LVBus759737_consumption, 28_LVBus759742_consumption, 28_LVBus759745_consumption, 28_LVBus759748_consumption, 28_LVBus759750_consumption, 28_LVBus759752_consumption, 28_LVBus759753_consumption, 28_LVBus759755_consumption, 28_LVBus759758_consumption, 28_LVBus759760_consumption, 28_LVBus759763_consumption, 28_LVBus759771_consumption, 28_LVBus759774_consumption, 28_LVBus759776_consumption, 28_LVBus759778_consumption, 28_LVBus759779_consumption, 28_LVBus759780_consumption, 28_LVBus759781_consumption, 28_LVBus759783_consumption, 28_LVBus759784_consumption, 28_LVBus759785_consumption, 28_LVBus759786_consumption, 28_LVBus759787_consumption, 28_LVBus759788_consumption, 28_LVBus759789_consumption, 28_LVBus759790_consumption, 28_LVBus759794_consumption, 28_LVBus759796_consumption, 28_LVBus759802_consumption, 28_LVBus759803_consumption, 28_LVBus759806_consumption, 28_LVBus759810_consumption, 28_LVBus759822_consumption, 28_LVBus759824_consumption, 28_LVBus759827_consumption, 28_LVBus759830_consumption, 28_LVBus759831_consumption, 28_LVBus759833_consumption, 28_LVBus759835_consumption, 28_LVBus759836_consumption, 28_LVBus759837_consumption, 28_LVBus759840_consumption, 28_LVBus759844_consumption, 28_LVBus759846_consumption, 28_LVBus759847_consumption, 28_LVBus759851_consumption, 28_LVBus759853_consumption, 28_LVBus759854_consumption, 28_LVBus759856_consumption, 28_LVBus759857_consumption, 28_LVBus759861_consumption, 28_LVBus759868_consumption, 28_LVBus759876_consumption, 28_LVBus759882_consumption, 28_LVBus759885_consumption, 28_LVBus759886_consumption, 28_LVBus759889_consumption, 28_LVBus759890_consumption, 28_LVBus759892_consumption, 28_LVBus759898_consumption, 28_LVBus759899_consumption, 28_LVBus759900_consumption, 28_LVBus759902_consumption, 28_LVBus759906_consumption, 28_LVBus759909_consumption, 28_LVBus759911_consumption, 28_LVBus759915_consumption, 28_LVBus759918_consumption, 28_LVBus759923_consumption, 28_LVBus759925_consumption, 28_LVBus759927_consumption, 28_LVBus759928_consumption, 28_LVBus853401_consumption, 28_LVBus853403_consumption, 28_LVBus853800_consumption, 28_LVBus859877_consumption, 28_LVBus859879_consumption, 28_LVBus859880_consumption, 28_LVBus873115_consumption, 28_LVBus886402_consumption, 28_LVBus886404_consumption, 28_LVBus886406_consumption, 28_LVBus886408_consumption, 28_LVBus886411_consumption, 28_LVBus887155_consumption, 28_LVBus887584_consumption, 28_LVBus890266_consumption, 28_LVBus890267_consumption, 28_LVBus890268_consumption, 28_LVBus890269_consumption, 28_LVBus890270_consumption, 28_LVBus899818_consumption, 28_LVBus908535_consumption, 28_LVBus916243_consumption, 28_LVBus916245_consumption, 28_LVBus916246_consumption, 28_LVBus916247_consumption, 28_LVBus916248_consumption, 28_LVBus916250_consumption, 28_LVBus916251_consumption, 28_LVBus916252_consumption, 28_LVBus916253_consumption, 28_LVBus916254_consumption, 28_LVBus928330_consumption, 28_LVBus956275_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  427 group(s) of loads (854 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  4 group(s) of series lines (8 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  546 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus759454_consumption, 28_LVBus759454_production, 28_LVBus759455_production, 28_LVBus759457_consumption, 28_LVBus759457_production, 28_LVBus759458_consumption, 28_LVBus759458_production, 28_LVBus759459_production, 28_LVBus759461_consumption, 28_LVBus759461_production, 28_LVBus759463_production, 28_LVBus759465_production, 28_LVBus759467_consumption, 28_LVBus759467_production, 28_LVBus759468_consumption, 28_LVBus759468_production, 28_LVBus759469_consumption, 28_LVBus759469_production, 28_LVBus759470_consumption, 28_LVBus759470_production, 28_LVBus759471_production, 28_LVBus759472_production, 28_LVBus759473_production, 28_LVBus759475_production, 28_LVBus759477_production, 28_LVBus759479_consumption, 28_LVBus759479_production, 28_LVBus759480_production, 28_LVBus759481_consumption, 28_LVBus759481_production, 28_LVBus759482_consumption, 28_LVBus759482_production, 28_LVBus759483_production, 28_LVBus759484_production, 28_LVBus759485_production, 28_LVBus759487_production, 28_LVBus759488_production, 28_LVBus759490_consumption, 28_LVBus759490_production, 28_LVBus759491_production, 28_LVBus759492_production, 28_LVBus759493_production, 28_LVBus759494_production, 28_LVBus759495_production, 28_LVBus759496_production, 28_LVBus759497_production, 28_LVBus759498_production, 28_LVBus759500_consumption, 28_LVBus759500_production, 28_LVBus759502_production, 28_LVBus759504_production, 28_LVBus759505_production, 28_LVBus759506_production, 28_LVBus759507_consumption, 28_LVBus759507_production, 28_LVBus759508_consumption, 28_LVBus759508_production, 28_LVBus759509_consumption, 28_LVBus759509_production, 28_LVBus759510_production, 28_LVBus759511_consumption, 28_LVBus759511_production, 28_LVBus759512_production, 28_LVBus759514_consumption, 28_LVBus759514_production, 28_LVBus759515_consumption, 28_LVBus759515_production, 28_LVBus759516_production, 28_LVBus759518_production, 28_LVBus759519_production, 28_LVBus759521_production, 28_LVBus759522_production, 28_LVBus759523_production, 28_LVBus759525_production, 28_LVBus759526_production, 28_LVBus759528_production, 28_LVBus759529_production, 28_LVBus759530_production, 28_LVBus759532_production, 28_LVBus759534_production, 28_LVBus759536_production, 28_LVBus759538_production, 28_LVBus759540_production, 28_LVBus759542_consumption, 28_LVBus759542_production, 28_LVBus759544_production, 28_LVBus759546_production, 28_LVBus759547_production, 28_LVBus759548_production, 28_LVBus759549_consumption, 28_LVBus759549_production, 28_LVBus759550_production, 28_LVBus759551_production, 28_LVBus759553_production, 28_LVBus759555_consumption, 28_LVBus759555_production, 28_LVBus759556_production, 28_LVBus759558_production, 28_LVBus759559_production, 28_LVBus759560_production, 28_LVBus759561_production, 28_LVBus759562_production, 28_LVBus759563_production, 28_LVBus759565_production, 28_LVBus759566_production, 28_LVBus759568_production, 28_LVBus759569_production, 28_LVBus759570_production, 28_LVBus759571_production, 28_LVBus759572_production, 28_LVBus759573_production, 28_LVBus759574_production, 28_LVBus759575_production, 28_LVBus759577_production, 28_LVBus759578_production, 28_LVBus759579_consumption, 28_LVBus759579_production, 28_LVBus759580_production, 28_LVBus759581_production, 28_LVBus759582_production, 28_LVBus759586_production, 28_LVBus759587_production, 28_LVBus759588_consumption, 28_LVBus759588_production, 28_LVBus759589_production, 28_LVBus759590_production, 28_LVBus759591_consumption, 28_LVBus759591_production, 28_LVBus759592_consumption, 28_LVBus759592_production, 28_LVBus759593_production, 28_LVBus759594_production, 28_LVBus759596_consumption, 28_LVBus759596_production, 28_LVBus759597_production, 28_LVBus759598_consumption, 28_LVBus759598_production, 28_LVBus759599_production, 28_LVBus759604_production, 28_LVBus759605_production, 28_LVBus759606_production, 28_LVBus759607_production, 28_LVBus759609_consumption, 28_LVBus759609_production, 28_LVBus759610_consumption, 28_LVBus759610_production, 28_LVBus759612_production, 28_LVBus759614_production, 28_LVBus759615_consumption, 28_LVBus759615_production, 28_LVBus759617_production, 28_LVBus759618_production, 28_LVBus759619_production, 28_LVBus759621_production, 28_LVBus759622_production, 28_LVBus759623_production, 28_LVBus759624_production, 28_LVBus759626_production, 28_LVBus759628_consumption, 28_LVBus759628_production, 28_LVBus759629_consumption, 28_LVBus759629_production, 28_LVBus759630_production, 28_LVBus759631_production, 28_LVBus759635_consumption, 28_LVBus759635_production, 28_LVBus759636_production, 28_LVBus759637_consumption, 28_LVBus759637_production, 28_LVBus759639_production, 28_LVBus759640_production, 28_LVBus759641_production, 28_LVBus759642_production, 28_LVBus759643_consumption, 28_LVBus759643_production, 28_LVBus759644_production, 28_LVBus759646_production, 28_LVBus759647_production, 28_LVBus759648_consumption, 28_LVBus759648_production, 28_LVBus759649_production, 28_LVBus759650_consumption, 28_LVBus759650_production, 28_LVBus759651_production, 28_LVBus759652_production, 28_LVBus759653_production, 28_LVBus759654_production, 28_LVBus759655_production, 28_LVBus759656_production, 28_LVBus759658_consumption, 28_LVBus759658_production, 28_LVBus759659_production, 28_LVBus759661_consumption, 28_LVBus759661_production, 28_LVBus759663_consumption, 28_LVBus759663_production, 28_LVBus759664_production, 28_LVBus759665_production, 28_LVBus759667_production, 28_LVBus759668_production, 28_LVBus759669_production, 28_LVBus759673_production, 28_LVBus759675_production, 28_LVBus759677_production, 28_LVBus759679_production, 28_LVBus759681_consumption, 28_LVBus759681_production, 28_LVBus759683_production, 28_LVBus759685_production, 28_LVBus759686_production, 28_LVBus759687_consumption, 28_LVBus759687_production, 28_LVBus759688_production, 28_LVBus759689_production, 28_LVBus759690_production, 28_LVBus759691_production, 28_LVBus759692_production, 28_LVBus759693_production, 28_LVBus759694_production, 28_LVBus759695_consumption, 28_LVBus759695_production, 28_LVBus759696_production, 28_LVBus759697_production, 28_LVBus759699_production, 28_LVBus759701_production, 28_LVBus759702_production, 28_LVBus759703_consumption, 28_LVBus759703_production, 28_LVBus759704_production, 28_LVBus759705_consumption, 28_LVBus759705_production, 28_LVBus759707_production, 28_LVBus759708_production, 28_LVBus759709_production, 28_LVBus759710_production, 28_LVBus759711_consumption, 28_LVBus759711_production, 28_LVBus759712_production, 28_LVBus759713_production, 28_LVBus759714_consumption, 28_LVBus759714_production, 28_LVBus759715_production, 28_LVBus759716_production, 28_LVBus759717_consumption, 28_LVBus759717_production, 28_LVBus759718_consumption, 28_LVBus759718_production, 28_LVBus759719_production, 28_LVBus759721_consumption, 28_LVBus759721_production, 28_LVBus759722_consumption, 28_LVBus759722_production, 28_LVBus759723_consumption, 28_LVBus759723_production, 28_LVBus759724_consumption, 28_LVBus759724_production, 28_LVBus759725_production, 28_LVBus759727_production, 28_LVBus759728_consumption, 28_LVBus759728_production, 28_LVBus759730_consumption, 28_LVBus759730_production, 28_LVBus759731_consumption, 28_LVBus759731_production, 28_LVBus759732_consumption, 28_LVBus759732_production, 28_LVBus759734_production, 28_LVBus759735_production, 28_LVBus759736_production, 28_LVBus759737_production, 28_LVBus759741_consumption, 28_LVBus759741_production, 28_LVBus759742_production, 28_LVBus759744_consumption, 28_LVBus759744_production, 28_LVBus759745_production, 28_LVBus759748_production, 28_LVBus759749_consumption, 28_LVBus759749_production, 28_LVBus759750_production, 28_LVBus759751_consumption, 28_LVBus759751_production, 28_LVBus759752_production, 28_LVBus759753_production, 28_LVBus759755_production, 28_LVBus759756_consumption, 28_LVBus759756_production, 28_LVBus759758_production, 28_LVBus759759_consumption, 28_LVBus759759_production, 28_LVBus759760_production, 28_LVBus759761_consumption, 28_LVBus759761_production, 28_LVBus759763_production, 28_LVBus759765_consumption, 28_LVBus759765_production, 28_LVBus759767_production, 28_LVBus759771_production, 28_LVBus759773_consumption, 28_LVBus759773_production, 28_LVBus759774_production, 28_LVBus759776_production, 28_LVBus759777_production, 28_LVBus759778_production, 28_LVBus759779_production, 28_LVBus759780_production, 28_LVBus759781_production, 28_LVBus759783_production, 28_LVBus759784_production, 28_LVBus759785_production, 28_LVBus759786_production, 28_LVBus759787_production, 28_LVBus759788_production, 28_LVBus759789_production, 28_LVBus759790_production, 28_LVBus759791_production, 28_LVBus759793_production, 28_LVBus759794_production, 28_LVBus759795_production, 28_LVBus759796_production, 28_LVBus759798_production, 28_LVBus759799_consumption, 28_LVBus759799_production, 28_LVBus759801_production, 28_LVBus759802_production, 28_LVBus759803_production, 28_LVBus759804_consumption, 28_LVBus759804_production, 28_LVBus759805_consumption, 28_LVBus759805_production, 28_LVBus759806_production, 28_LVBus759807_production, 28_LVBus759809_consumption, 28_LVBus759809_production, 28_LVBus759810_production, 28_LVBus759811_consumption, 28_LVBus759811_production, 28_LVBus759812_consumption, 28_LVBus759812_production, 28_LVBus759813_consumption, 28_LVBus759813_production, 28_LVBus759814_consumption, 28_LVBus759814_production, 28_LVBus759815_production, 28_LVBus759816_consumption, 28_LVBus759816_production, 28_LVBus759817_consumption, 28_LVBus759817_production, 28_LVBus759818_consumption, 28_LVBus759818_production, 28_LVBus759819_production, 28_LVBus759820_consumption, 28_LVBus759820_production, 28_LVBus759821_production, 28_LVBus759822_production, 28_LVBus759823_consumption, 28_LVBus759823_production, 28_LVBus759824_production, 28_LVBus759826_production, 28_LVBus759827_production, 28_LVBus759828_production, 28_LVBus759829_production, 28_LVBus759830_production, 28_LVBus759831_production, 28_LVBus759832_production, 28_LVBus759833_production, 28_LVBus759835_production, 28_LVBus759836_production, 28_LVBus759837_production, 28_LVBus759838_consumption, 28_LVBus759838_production, 28_LVBus759840_production, 28_LVBus759842_consumption, 28_LVBus759842_production, 28_LVBus759844_production, 28_LVBus759845_consumption, 28_LVBus759845_production, 28_LVBus759846_production, 28_LVBus759847_production, 28_LVBus759849_consumption, 28_LVBus759849_production, 28_LVBus759851_production, 28_LVBus759853_production, 28_LVBus759854_production, 28_LVBus759856_production, 28_LVBus759857_production, 28_LVBus759858_production, 28_LVBus759859_consumption, 28_LVBus759859_production, 28_LVBus759861_production, 28_LVBus759862_production, 28_LVBus759863_production, 28_LVBus759865_production, 28_LVBus759866_consumption, 28_LVBus759866_production, 28_LVBus759868_production, 28_LVBus759869_production, 28_LVBus759871_consumption, 28_LVBus759871_production, 28_LVBus759872_production, 28_LVBus759873_production, 28_LVBus759874_production, 28_LVBus759876_production, 28_LVBus759877_production, 28_LVBus759879_consumption, 28_LVBus759879_production, 28_LVBus759880_consumption, 28_LVBus759880_production, 28_LVBus759881_production, 28_LVBus759882_production, 28_LVBus759883_production, 28_LVBus759884_consumption, 28_LVBus759884_production, 28_LVBus759885_production, 28_LVBus759886_production, 28_LVBus759887_consumption, 28_LVBus759887_production, 28_LVBus759888_consumption, 28_LVBus759888_production, 28_LVBus759889_production, 28_LVBus759890_production, 28_LVBus759891_consumption, 28_LVBus759891_production, 28_LVBus759892_production, 28_LVBus759896_production, 28_LVBus759898_production, 28_LVBus759899_production, 28_LVBus759900_production, 28_LVBus759902_production, 28_LVBus759903_production, 28_LVBus759905_production, 28_LVBus759906_production, 28_LVBus759907_production, 28_LVBus759909_production, 28_LVBus759910_consumption, 28_LVBus759910_production, 28_LVBus759911_production, 28_LVBus759913_consumption, 28_LVBus759913_production, 28_LVBus759914_production, 28_LVBus759915_production, 28_LVBus759917_consumption, 28_LVBus759917_production, 28_LVBus759918_production, 28_LVBus759920_consumption, 28_LVBus759920_production, 28_LVBus759921_production, 28_LVBus759923_production, 28_LVBus759924_consumption, 28_LVBus759924_production, 28_LVBus759925_production, 28_LVBus759926_production, 28_LVBus759927_production, 28_LVBus759928_production, 28_LVBus853401_production, 28_LVBus853402_consumption, 28_LVBus853402_production, 28_LVBus853403_production, 28_LVBus853799_production, 28_LVBus853800_production, 28_LVBus859877_production, 28_LVBus859878_consumption, 28_LVBus859878_production, 28_LVBus859879_production, 28_LVBus859880_production, 28_LVBus873113_consumption, 28_LVBus873113_production, 28_LVBus873114_production, 28_LVBus873115_production, 28_LVBus880913_consumption, 28_LVBus880913_production, 28_LVBus882185_consumption, 28_LVBus882185_production, 28_LVBus886401_consumption, 28_LVBus886401_production, 28_LVBus886402_production, 28_LVBus886403_production, 28_LVBus886404_production, 28_LVBus886405_production, 28_LVBus886406_production, 28_LVBus886407_production, 28_LVBus886408_production, 28_LVBus886409_consumption, 28_LVBus886409_production, 28_LVBus886410_production, 28_LVBus886411_production, 28_LVBus886412_consumption, 28_LVBus886412_production, 28_LVBus887155_production, 28_LVBus887156_production, 28_LVBus887157_consumption, 28_LVBus887157_production, 28_LVBus887584_production, 28_LVBus890266_production, 28_LVBus890267_production, 28_LVBus890268_production, 28_LVBus890269_production, 28_LVBus890270_production, 28_LVBus899818_production, 28_LVBus908535_production, 28_LVBus912379_production, 28_LVBus914265_consumption, 28_LVBus914265_production, 28_LVBus914266_consumption, 28_LVBus914266_production, 28_LVBus916240_consumption, 28_LVBus916240_production, 28_LVBus916241_consumption, 28_LVBus916241_production, 28_LVBus916242_consumption, 28_LVBus916242_production, 28_LVBus916243_production, 28_LVBus916244_production, 28_LVBus916245_production, 28_LVBus916246_production, 28_LVBus916247_production, 28_LVBus916248_production, 28_LVBus916249_production, 28_LVBus916250_production, 28_LVBus916251_production, 28_LVBus916252_production, 28_LVBus916253_production, 28_LVBus916254_production, 28_LVBus922180_production, 28_LVBus928328_production, 28_LVBus928329_production, 28_LVBus928330_production, 28_LVBus931597_consumption, 28_LVBus931597_production, 28_LVBus936956_consumption, 28_LVBus936956_production, 28_LVBus956275_production, 28_LVBus956276_production, 28_LVBus956277_production, 28_LVBus956278_production, 28_LVBus956888_consumption, 28_LVBus956888_production, 28_MVLV24182_consumption, 28_MVLV24182_production, 28_MVLV26163_production, 28_MVLV43992_consumption, 28_MVLV43992_production, 28_MVLV58423_consumption, 28_MVLV58423_production, 28_MVLV82232_consumption, 28_MVLV82232_production.

