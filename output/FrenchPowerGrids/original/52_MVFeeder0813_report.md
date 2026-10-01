# BMOPF Network Summary: 52_MVFeeder0813

**Generated:** 2026-10-01 23:34:13  
**Findings:** 0 errors · 5 warnings · 189 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 325 |  |
| line | 308 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 580 | 3.514 MW, 1.05 Mvar |
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
| MV_11.8kV | 11.78 kV | 22 | 21 | 6 | 0 |
| LV_236V | 236.0 V | 303 | 287 | 574 | 0 |

**Transformer transitions:**

- `52_MVLV002623_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV107184_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV079217_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV078833_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV043270_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV030808_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV044592_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV069367_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV054228_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV013876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV034783_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV091182_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV077467_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV056219_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV059773_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV024611_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 14 |
| Degree-1 buses | 169 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 325 | 1 | 324 | 0 | 0 | 0 |
| Tier LV_236V | 303 | 16 | 287 | 0 | 0 | 0 |
| Tier MV_11.8kV | 22 | 1 | 21 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 16; skipped invalid branches: 0.

Galvanic zones: 17; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_DOULO | MV_11.8kV | 22 | 0 | 0 | 16 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1278 declared bus terminals; 1211 mapped line/closed-switch conductor edges; 67 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 79500.0 | 3.241 | 1740 |
| q_nom | 0.0 | 23800.0 | 3.241 | 1740 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.852 | 2790.0 | 2.337 | 308 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.517 | 16 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 387 of 580 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194798_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195045_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194890_consumption' has phase imbalance of 224.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194842_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195038_consumption' has phase imbalance of 196.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194875_consumption' has phase imbalance of 60.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195003_consumption' has phase imbalance of 175.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194830_consumption' has phase imbalance of 223.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195103_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194790_consumption' has phase imbalance of 28.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195061_consumption' has phase imbalance of 64.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194818_consumption' has phase imbalance of 265.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194878_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194911_consumption' has phase imbalance of 48.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194775_consumption' has phase imbalance of 209.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195098_consumption' has phase imbalance of 31.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195024_consumption' has phase imbalance of 223.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195097_consumption' has phase imbalance of 198.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194908_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195014_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194916_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195040_consumption' has phase imbalance of 115.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194823_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194788_consumption' has phase imbalance of 225.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194809_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195049_consumption' has phase imbalance of 114.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194858_consumption' has phase imbalance of 124.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194893_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195096_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195012_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194836_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194761_consumption' has phase imbalance of 43.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194931_consumption' has phase imbalance of 103.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194791_consumption' has phase imbalance of 87.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194783_consumption' has phase imbalance of 31.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194759_consumption' has phase imbalance of 41.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194918_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194851_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195048_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195010_consumption' has phase imbalance of 57.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194817_consumption' has phase imbalance of 129.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194824_consumption' has phase imbalance of 38.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194846_consumption' has phase imbalance of 138.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194794_consumption' has phase imbalance of 89.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195068_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195107_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194829_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194819_consumption' has phase imbalance of 139.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195056_consumption' has phase imbalance of 117.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194872_consumption' has phase imbalance of 130.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195085_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194902_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194839_consumption' has phase imbalance of 82.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194965_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195021_consumption' has phase imbalance of 247.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195050_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194808_consumption' has phase imbalance of 81.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194871_consumption' has phase imbalance of 229.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194827_consumption' has phase imbalance of 32.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195132_consumption' has phase imbalance of 93.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194922_consumption' has phase imbalance of 103.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195017_consumption' has phase imbalance of 144.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195006_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194876_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195055_consumption' has phase imbalance of 24.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194929_consumption' has phase imbalance of 23.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194887_consumption' has phase imbalance of 188.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195005_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194913_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195117_consumption' has phase imbalance of 64.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194822_consumption' has phase imbalance of 31.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195075_consumption' has phase imbalance of 66.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195033_consumption' has phase imbalance of 226.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195046_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194870_consumption' has phase imbalance of 189.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195042_consumption' has phase imbalance of 131.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195063_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194917_consumption' has phase imbalance of 88.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194881_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194927_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195000_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194844_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194891_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194904_consumption' has phase imbalance of 39.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195123_consumption' has phase imbalance of 47.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194838_consumption' has phase imbalance of 185.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194924_consumption' has phase imbalance of 47.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194889_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194845_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194857_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194820_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194852_consumption' has phase imbalance of 32.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195128_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195104_consumption' has phase imbalance of 31.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195029_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194835_consumption' has phase imbalance of 176.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194781_consumption' has phase imbalance of 50.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194994_consumption' has phase imbalance of 52.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194970_consumption' has phase imbalance of 22.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195108_consumption' has phase imbalance of 35.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195053_consumption' has phase imbalance of 94.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194833_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195032_consumption' has phase imbalance of 91.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195022_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194919_consumption' has phase imbalance of 102.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195037_consumption' has phase imbalance of 62.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194895_consumption' has phase imbalance of 210.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195092_consumption' has phase imbalance of 104.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194915_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194866_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194837_consumption' has phase imbalance of 109.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194863_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194971_consumption' has phase imbalance of 20.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194832_consumption' has phase imbalance of 182.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194864_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194854_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195036_consumption' has phase imbalance of 51.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194834_consumption' has phase imbalance of 112.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195004_consumption' has phase imbalance of 131.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194920_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194910_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194992_consumption' has phase imbalance of 90.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195060_consumption' has phase imbalance of 109.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194886_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195086_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194873_consumption' has phase imbalance of 26.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195011_consumption' has phase imbalance of 187.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194779_consumption' has phase imbalance of 20.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195018_consumption' has phase imbalance of 37.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195009_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194903_consumption' has phase imbalance of 170.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194892_consumption' has phase imbalance of 125.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194792_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194797_consumption' has phase imbalance of 49.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194776_consumption' has phase imbalance of 50.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194803_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195013_consumption' has phase imbalance of 58.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194787_consumption' has phase imbalance of 105.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195020_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195019_consumption' has phase imbalance of 234.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194905_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195124_consumption' has phase imbalance of 70.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus195030_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194879_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus194850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 580 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_DOULO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus194943' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.514 MW |
| Total load Q | 1.05 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV002623_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV107184_Transformer | 1.1 MVA | 52.1% |
| 52_MVLV079217_Transformer | 440.0 kVA | 43.9% |
| 52_MVLV078833_Transformer | 693.0 kVA | 59.3% |
| 52_MVLV043270_Transformer | 693.0 kVA | 31.6% |
| 52_MVLV030808_Transformer | 275.0 kVA | 19.3% |
| 52_MVLV044592_Transformer | 275.0 kVA | 29.9% |
| 52_MVLV069367_Transformer | 440.0 kVA | 15.2% |
| 52_MVLV054228_Transformer | 440.0 kVA | 24.1% |
| 52_MVLV013876_Transformer | 275.0 kVA | 48.8% |
| 52_MVLV034783_Transformer | 693.0 kVA | 33.3% |
| 52_MVLV091182_Transformer | 440.0 kVA | 38.4% |
| 52_MVLV077467_Transformer | 693.0 kVA | 34.7% |
| 52_MVLV056219_Transformer | 693.0 kVA | 41.5% |
| 52_MVLV059773_Transformer | 440.0 kVA | 60.3% |
| 52_MVLV024611_Transformer | 110.0 kVA | 4.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.51 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus194733' (LV, 0.24 kV) has an electrical reach of 7.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus194763' (LV, 0.24 kV) has an electrical reach of 6.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 325 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 325 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 16 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 22 |
| LV_236V | 4-wire | 303 / 303 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 303 |
| Neutral branches | 287 |
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
| 11.78 kV | 22 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 1390.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 303 / 22 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 388 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 388 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus194733_consumption, 52_LVBus194733_production, 52_LVBus194735_consumption, 52_LVBus194735_production, 52_LVBus194737_consumption, 52_LVBus194737_production, 52_LVBus194739_consumption, 52_LVBus194739_production, 52_LVBus194741_consumption, 52_LVBus194741_production, 52_LVBus194743_consumption, 52_LVBus194743_production, 52_LVBus194745_consumption, 52_LVBus194745_production, 52_LVBus194747_consumption, 52_LVBus194747_production, 52_LVBus194751_consumption, 52_LVBus194751_production, 52_LVBus194753_consumption, 52_LVBus194753_production, 52_LVBus194755_production, 52_LVBus194757_consumption, 52_LVBus194757_production, 52_LVBus194759_production, 52_LVBus194761_production, 52_LVBus194763_consumption, 52_LVBus194763_production, 52_LVBus194765_consumption, 52_LVBus194765_production, 52_LVBus194767_production, 52_LVBus194769_consumption, 52_LVBus194769_production, 52_LVBus194771_consumption, 52_LVBus194771_production, 52_LVBus194773_consumption, 52_LVBus194773_production, 52_LVBus194774_consumption, 52_LVBus194774_production, 52_LVBus194775_production, 52_LVBus194776_production, 52_LVBus194777_production, 52_LVBus194779_production, 52_LVBus194781_production, 52_LVBus194783_production, 52_LVBus194785_consumption, 52_LVBus194785_production, 52_LVBus194787_production, 52_LVBus194788_production, 52_LVBus194789_consumption, 52_LVBus194789_production, 52_LVBus194790_production, 52_LVBus194791_production, 52_LVBus194792_production, 52_LVBus194793_production, 52_LVBus194794_production, 52_LVBus194796_consumption, 52_LVBus194796_production, 52_LVBus194797_production, 52_LVBus194798_production, 52_LVBus194800_consumption, 52_LVBus194800_production, 52_LVBus194801_production, 52_LVBus194803_production, 52_LVBus194805_consumption, 52_LVBus194805_production, 52_LVBus194806_consumption, 52_LVBus194806_production, 52_LVBus194807_consumption, 52_LVBus194807_production, 52_LVBus194808_production, 52_LVBus194809_production, 52_LVBus194810_production, 52_LVBus194811_production, 52_LVBus194812_production, 52_LVBus194813_consumption, 52_LVBus194813_production, 52_LVBus194814_consumption, 52_LVBus194814_production, 52_LVBus194815_production, 52_LVBus194816_consumption, 52_LVBus194816_production, 52_LVBus194817_production, 52_LVBus194818_production, 52_LVBus194819_production, 52_LVBus194820_production, 52_LVBus194822_production, 52_LVBus194823_production, 52_LVBus194824_production, 52_LVBus194826_production, 52_LVBus194827_production, 52_LVBus194829_production, 52_LVBus194830_production, 52_LVBus194831_production, 52_LVBus194832_production, 52_LVBus194833_production, 52_LVBus194834_production, 52_LVBus194835_production, 52_LVBus194836_production, 52_LVBus194837_production, 52_LVBus194838_production, 52_LVBus194839_production, 52_LVBus194840_production, 52_LVBus194841_production, 52_LVBus194842_production, 52_LVBus194844_production, 52_LVBus194845_production, 52_LVBus194846_production, 52_LVBus194848_consumption, 52_LVBus194848_production, 52_LVBus194850_production, 52_LVBus194851_production, 52_LVBus194852_production, 52_LVBus194854_production, 52_LVBus194856_consumption, 52_LVBus194856_production, 52_LVBus194857_production, 52_LVBus194858_production, 52_LVBus194860_consumption, 52_LVBus194860_production, 52_LVBus194861_consumption, 52_LVBus194861_production, 52_LVBus194862_consumption, 52_LVBus194862_production, 52_LVBus194863_production, 52_LVBus194864_production, 52_LVBus194865_consumption, 52_LVBus194865_production, 52_LVBus194866_production, 52_LVBus194867_consumption, 52_LVBus194867_production, 52_LVBus194868_consumption, 52_LVBus194868_production, 52_LVBus194870_production, 52_LVBus194871_production, 52_LVBus194872_production, 52_LVBus194873_production, 52_LVBus194875_production, 52_LVBus194876_production, 52_LVBus194878_production, 52_LVBus194879_production, 52_LVBus194881_production, 52_LVBus194883_production, 52_LVBus194885_production, 52_LVBus194886_production, 52_LVBus194887_production, 52_LVBus194889_production, 52_LVBus194890_production, 52_LVBus194891_production, 52_LVBus194892_production, 52_LVBus194893_production, 52_LVBus194894_consumption, 52_LVBus194894_production, 52_LVBus194895_production, 52_LVBus194896_production, 52_LVBus194897_production, 52_LVBus194898_production, 52_LVBus194900_production, 52_LVBus194902_production, 52_LVBus194903_production, 52_LVBus194904_production, 52_LVBus194905_production, 52_LVBus194906_consumption, 52_LVBus194906_production, 52_LVBus194907_production, 52_LVBus194908_production, 52_LVBus194909_production, 52_LVBus194910_production, 52_LVBus194911_production, 52_LVBus194913_production, 52_LVBus194914_production, 52_LVBus194915_production, 52_LVBus194916_production, 52_LVBus194917_production, 52_LVBus194918_production, 52_LVBus194919_production, 52_LVBus194920_production, 52_LVBus194922_production, 52_LVBus194924_production, 52_LVBus194926_consumption, 52_LVBus194926_production, 52_LVBus194927_production, 52_LVBus194928_production, 52_LVBus194929_production, 52_LVBus194931_production, 52_LVBus194933_production, 52_LVBus194943_consumption, 52_LVBus194943_production, 52_LVBus194945_consumption, 52_LVBus194945_production, 52_LVBus194946_consumption, 52_LVBus194946_production, 52_LVBus194947_consumption, 52_LVBus194947_production, 52_LVBus194949_production, 52_LVBus194951_consumption, 52_LVBus194951_production, 52_LVBus194952_consumption, 52_LVBus194952_production, 52_LVBus194953_production, 52_LVBus194955_consumption, 52_LVBus194955_production, 52_LVBus194957_consumption, 52_LVBus194957_production, 52_LVBus194959_consumption, 52_LVBus194959_production, 52_LVBus194961_consumption, 52_LVBus194961_production, 52_LVBus194962_consumption, 52_LVBus194962_production, 52_LVBus194963_consumption, 52_LVBus194963_production, 52_LVBus194965_production, 52_LVBus194967_consumption, 52_LVBus194967_production, 52_LVBus194969_consumption, 52_LVBus194969_production, 52_LVBus194970_production, 52_LVBus194971_production, 52_LVBus194973_consumption, 52_LVBus194973_production, 52_LVBus194975_consumption, 52_LVBus194975_production, 52_LVBus194976_consumption, 52_LVBus194976_production, 52_LVBus194977_consumption, 52_LVBus194977_production, 52_LVBus194979_consumption, 52_LVBus194979_production, 52_LVBus194980_consumption, 52_LVBus194980_production, 52_LVBus194981_production, 52_LVBus194983_consumption, 52_LVBus194983_production, 52_LVBus194984_consumption, 52_LVBus194984_production, 52_LVBus194985_consumption, 52_LVBus194985_production, 52_LVBus194987_consumption, 52_LVBus194987_production, 52_LVBus194989_consumption, 52_LVBus194989_production, 52_LVBus194990_production, 52_LVBus194991_production, 52_LVBus194992_production, 52_LVBus194993_consumption, 52_LVBus194993_production, 52_LVBus194994_production, 52_LVBus194996_consumption, 52_LVBus194996_production, 52_LVBus194998_consumption, 52_LVBus194998_production, 52_LVBus195000_production, 52_LVBus195002_production, 52_LVBus195003_production, 52_LVBus195004_production, 52_LVBus195005_production, 52_LVBus195006_production, 52_LVBus195007_production, 52_LVBus195009_production, 52_LVBus195010_production, 52_LVBus195011_production, 52_LVBus195012_production, 52_LVBus195013_production, 52_LVBus195014_production, 52_LVBus195016_production, 52_LVBus195017_production, 52_LVBus195018_production, 52_LVBus195019_production, 52_LVBus195020_production, 52_LVBus195021_production, 52_LVBus195022_production, 52_LVBus195023_consumption, 52_LVBus195023_production, 52_LVBus195024_production, 52_LVBus195025_production, 52_LVBus195026_consumption, 52_LVBus195026_production, 52_LVBus195028_consumption, 52_LVBus195028_production, 52_LVBus195029_production, 52_LVBus195030_production, 52_LVBus195032_production, 52_LVBus195033_production, 52_LVBus195034_production, 52_LVBus195035_production, 52_LVBus195036_production, 52_LVBus195037_production, 52_LVBus195038_production, 52_LVBus195040_production, 52_LVBus195041_production, 52_LVBus195042_production, 52_LVBus195043_production, 52_LVBus195045_production, 52_LVBus195046_production, 52_LVBus195047_consumption, 52_LVBus195047_production, 52_LVBus195048_production, 52_LVBus195049_production, 52_LVBus195050_production, 52_LVBus195052_consumption, 52_LVBus195052_production, 52_LVBus195053_production, 52_LVBus195055_production, 52_LVBus195056_production, 52_LVBus195058_production, 52_LVBus195060_production, 52_LVBus195061_production, 52_LVBus195062_production, 52_LVBus195063_production, 52_LVBus195065_consumption, 52_LVBus195065_production, 52_LVBus195067_consumption, 52_LVBus195067_production, 52_LVBus195068_production, 52_LVBus195069_consumption, 52_LVBus195069_production, 52_LVBus195071_consumption, 52_LVBus195071_production, 52_LVBus195072_consumption, 52_LVBus195072_production, 52_LVBus195073_consumption, 52_LVBus195073_production, 52_LVBus195075_production, 52_LVBus195077_production, 52_LVBus195078_consumption, 52_LVBus195078_production, 52_LVBus195079_consumption, 52_LVBus195079_production, 52_LVBus195081_consumption, 52_LVBus195081_production, 52_LVBus195083_consumption, 52_LVBus195083_production, 52_LVBus195084_consumption, 52_LVBus195084_production, 52_LVBus195085_production, 52_LVBus195086_production, 52_LVBus195090_consumption, 52_LVBus195090_production, 52_LVBus195092_production, 52_LVBus195094_consumption, 52_LVBus195094_production, 52_LVBus195095_consumption, 52_LVBus195095_production, 52_LVBus195096_production, 52_LVBus195097_production, 52_LVBus195098_production, 52_LVBus195100_consumption, 52_LVBus195100_production, 52_LVBus195102_consumption, 52_LVBus195102_production, 52_LVBus195103_production, 52_LVBus195104_production, 52_LVBus195106_production, 52_LVBus195107_production, 52_LVBus195108_production, 52_LVBus195110_consumption, 52_LVBus195110_production, 52_LVBus195111_consumption, 52_LVBus195111_production, 52_LVBus195112_consumption, 52_LVBus195112_production, 52_LVBus195113_consumption, 52_LVBus195113_production, 52_LVBus195114_production, 52_LVBus195115_production, 52_LVBus195116_consumption, 52_LVBus195116_production, 52_LVBus195117_production, 52_LVBus195118_consumption, 52_LVBus195118_production, 52_LVBus195120_consumption, 52_LVBus195120_production, 52_LVBus195122_consumption, 52_LVBus195122_production, 52_LVBus195123_production, 52_LVBus195124_production, 52_LVBus195126_consumption, 52_LVBus195126_production, 52_LVBus195127_consumption, 52_LVBus195127_production, 52_LVBus195128_production, 52_LVBus195130_production, 52_LVBus195132_production, 52_LVBus195134_consumption, 52_LVBus195134_production, 52_MVLV002624_production, 52_MVLV023883_production, 52_MVLV064473_production.

## 9. Data Quality Summary

**Total findings:** 194 (0 errors, 5 warnings, 189 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  387 of 580 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.51 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  388 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194798_consumption`  
  Load '52_LVBus194798_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195045_consumption`  
  Load '52_LVBus195045_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194890_consumption`  
  Load '52_LVBus194890_consumption' has phase imbalance of 224.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194842_consumption`  
  Load '52_LVBus194842_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195038_consumption`  
  Load '52_LVBus195038_consumption' has phase imbalance of 196.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194875_consumption`  
  Load '52_LVBus194875_consumption' has phase imbalance of 60.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195003_consumption`  
  Load '52_LVBus195003_consumption' has phase imbalance of 175.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194830_consumption`  
  Load '52_LVBus194830_consumption' has phase imbalance of 223.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194896_consumption`  
  Load '52_LVBus194896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195103_consumption`  
  Load '52_LVBus195103_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194777_consumption`  
  Load '52_LVBus194777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194790_consumption`  
  Load '52_LVBus194790_consumption' has phase imbalance of 28.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195061_consumption`  
  Load '52_LVBus195061_consumption' has phase imbalance of 64.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194818_consumption`  
  Load '52_LVBus194818_consumption' has phase imbalance of 265.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194909_consumption`  
  Load '52_LVBus194909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194878_consumption`  
  Load '52_LVBus194878_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195016_consumption`  
  Load '52_LVBus195016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194911_consumption`  
  Load '52_LVBus194911_consumption' has phase imbalance of 48.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194775_consumption`  
  Load '52_LVBus194775_consumption' has phase imbalance of 209.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195098_consumption`  
  Load '52_LVBus195098_consumption' has phase imbalance of 31.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194907_consumption`  
  Load '52_LVBus194907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195024_consumption`  
  Load '52_LVBus195024_consumption' has phase imbalance of 223.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194840_consumption`  
  Load '52_LVBus194840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195097_consumption`  
  Load '52_LVBus195097_consumption' has phase imbalance of 198.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194908_consumption`  
  Load '52_LVBus194908_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195014_consumption`  
  Load '52_LVBus195014_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194916_consumption`  
  Load '52_LVBus194916_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195040_consumption`  
  Load '52_LVBus195040_consumption' has phase imbalance of 115.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194823_consumption`  
  Load '52_LVBus194823_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194788_consumption`  
  Load '52_LVBus194788_consumption' has phase imbalance of 225.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194809_consumption`  
  Load '52_LVBus194809_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195049_consumption`  
  Load '52_LVBus195049_consumption' has phase imbalance of 114.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194858_consumption`  
  Load '52_LVBus194858_consumption' has phase imbalance of 124.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194893_consumption`  
  Load '52_LVBus194893_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195096_consumption`  
  Load '52_LVBus195096_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195012_consumption`  
  Load '52_LVBus195012_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194836_consumption`  
  Load '52_LVBus194836_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194761_consumption`  
  Load '52_LVBus194761_consumption' has phase imbalance of 43.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194931_consumption`  
  Load '52_LVBus194931_consumption' has phase imbalance of 103.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194791_consumption`  
  Load '52_LVBus194791_consumption' has phase imbalance of 87.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194783_consumption`  
  Load '52_LVBus194783_consumption' has phase imbalance of 31.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194759_consumption`  
  Load '52_LVBus194759_consumption' has phase imbalance of 41.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195025_consumption`  
  Load '52_LVBus195025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194918_consumption`  
  Load '52_LVBus194918_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194851_consumption`  
  Load '52_LVBus194851_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195048_consumption`  
  Load '52_LVBus195048_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195010_consumption`  
  Load '52_LVBus195010_consumption' has phase imbalance of 57.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194817_consumption`  
  Load '52_LVBus194817_consumption' has phase imbalance of 129.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194824_consumption`  
  Load '52_LVBus194824_consumption' has phase imbalance of 38.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194846_consumption`  
  Load '52_LVBus194846_consumption' has phase imbalance of 138.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194794_consumption`  
  Load '52_LVBus194794_consumption' has phase imbalance of 89.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195068_consumption`  
  Load '52_LVBus195068_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195107_consumption`  
  Load '52_LVBus195107_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194829_consumption`  
  Load '52_LVBus194829_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194819_consumption`  
  Load '52_LVBus194819_consumption' has phase imbalance of 139.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195056_consumption`  
  Load '52_LVBus195056_consumption' has phase imbalance of 117.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195007_consumption`  
  Load '52_LVBus195007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194872_consumption`  
  Load '52_LVBus194872_consumption' has phase imbalance of 130.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195085_consumption`  
  Load '52_LVBus195085_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194841_consumption`  
  Load '52_LVBus194841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194902_consumption`  
  Load '52_LVBus194902_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194839_consumption`  
  Load '52_LVBus194839_consumption' has phase imbalance of 82.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194965_consumption`  
  Load '52_LVBus194965_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195021_consumption`  
  Load '52_LVBus195021_consumption' has phase imbalance of 247.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195050_consumption`  
  Load '52_LVBus195050_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195035_consumption`  
  Load '52_LVBus195035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194808_consumption`  
  Load '52_LVBus194808_consumption' has phase imbalance of 81.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194871_consumption`  
  Load '52_LVBus194871_consumption' has phase imbalance of 229.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194827_consumption`  
  Load '52_LVBus194827_consumption' has phase imbalance of 32.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195132_consumption`  
  Load '52_LVBus195132_consumption' has phase imbalance of 93.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194922_consumption`  
  Load '52_LVBus194922_consumption' has phase imbalance of 103.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195017_consumption`  
  Load '52_LVBus195017_consumption' has phase imbalance of 144.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195006_consumption`  
  Load '52_LVBus195006_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194876_consumption`  
  Load '52_LVBus194876_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195055_consumption`  
  Load '52_LVBus195055_consumption' has phase imbalance of 24.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194929_consumption`  
  Load '52_LVBus194929_consumption' has phase imbalance of 23.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194887_consumption`  
  Load '52_LVBus194887_consumption' has phase imbalance of 188.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195005_consumption`  
  Load '52_LVBus195005_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194913_consumption`  
  Load '52_LVBus194913_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195117_consumption`  
  Load '52_LVBus195117_consumption' has phase imbalance of 64.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194822_consumption`  
  Load '52_LVBus194822_consumption' has phase imbalance of 31.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195075_consumption`  
  Load '52_LVBus195075_consumption' has phase imbalance of 66.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195033_consumption`  
  Load '52_LVBus195033_consumption' has phase imbalance of 226.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195046_consumption`  
  Load '52_LVBus195046_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194870_consumption`  
  Load '52_LVBus194870_consumption' has phase imbalance of 189.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195042_consumption`  
  Load '52_LVBus195042_consumption' has phase imbalance of 131.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195063_consumption`  
  Load '52_LVBus195063_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194917_consumption`  
  Load '52_LVBus194917_consumption' has phase imbalance of 88.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194881_consumption`  
  Load '52_LVBus194881_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194927_consumption`  
  Load '52_LVBus194927_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195000_consumption`  
  Load '52_LVBus195000_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194844_consumption`  
  Load '52_LVBus194844_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194891_consumption`  
  Load '52_LVBus194891_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194811_consumption`  
  Load '52_LVBus194811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194904_consumption`  
  Load '52_LVBus194904_consumption' has phase imbalance of 39.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194914_consumption`  
  Load '52_LVBus194914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195123_consumption`  
  Load '52_LVBus195123_consumption' has phase imbalance of 47.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194838_consumption`  
  Load '52_LVBus194838_consumption' has phase imbalance of 185.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194924_consumption`  
  Load '52_LVBus194924_consumption' has phase imbalance of 47.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194826_consumption`  
  Load '52_LVBus194826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195002_consumption`  
  Load '52_LVBus195002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194889_consumption`  
  Load '52_LVBus194889_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194831_consumption`  
  Load '52_LVBus194831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194845_consumption`  
  Load '52_LVBus194845_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194857_consumption`  
  Load '52_LVBus194857_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194812_consumption`  
  Load '52_LVBus194812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194820_consumption`  
  Load '52_LVBus194820_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194991_consumption`  
  Load '52_LVBus194991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194852_consumption`  
  Load '52_LVBus194852_consumption' has phase imbalance of 32.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195128_consumption`  
  Load '52_LVBus195128_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194767_consumption`  
  Load '52_LVBus194767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195104_consumption`  
  Load '52_LVBus195104_consumption' has phase imbalance of 31.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195029_consumption`  
  Load '52_LVBus195029_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194835_consumption`  
  Load '52_LVBus194835_consumption' has phase imbalance of 176.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194781_consumption`  
  Load '52_LVBus194781_consumption' has phase imbalance of 50.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194994_consumption`  
  Load '52_LVBus194994_consumption' has phase imbalance of 52.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194970_consumption`  
  Load '52_LVBus194970_consumption' has phase imbalance of 22.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195108_consumption`  
  Load '52_LVBus195108_consumption' has phase imbalance of 35.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195041_consumption`  
  Load '52_LVBus195041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195053_consumption`  
  Load '52_LVBus195053_consumption' has phase imbalance of 94.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194833_consumption`  
  Load '52_LVBus194833_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195032_consumption`  
  Load '52_LVBus195032_consumption' has phase imbalance of 91.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195022_consumption`  
  Load '52_LVBus195022_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194897_consumption`  
  Load '52_LVBus194897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194883_consumption`  
  Load '52_LVBus194883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194919_consumption`  
  Load '52_LVBus194919_consumption' has phase imbalance of 102.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195037_consumption`  
  Load '52_LVBus195037_consumption' has phase imbalance of 62.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194895_consumption`  
  Load '52_LVBus194895_consumption' has phase imbalance of 210.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195092_consumption`  
  Load '52_LVBus195092_consumption' has phase imbalance of 104.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194915_consumption`  
  Load '52_LVBus194915_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194866_consumption`  
  Load '52_LVBus194866_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194837_consumption`  
  Load '52_LVBus194837_consumption' has phase imbalance of 109.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194863_consumption`  
  Load '52_LVBus194863_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194971_consumption`  
  Load '52_LVBus194971_consumption' has phase imbalance of 20.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194832_consumption`  
  Load '52_LVBus194832_consumption' has phase imbalance of 182.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194864_consumption`  
  Load '52_LVBus194864_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194854_consumption`  
  Load '52_LVBus194854_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195036_consumption`  
  Load '52_LVBus195036_consumption' has phase imbalance of 51.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194834_consumption`  
  Load '52_LVBus194834_consumption' has phase imbalance of 112.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195004_consumption`  
  Load '52_LVBus195004_consumption' has phase imbalance of 131.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194920_consumption`  
  Load '52_LVBus194920_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195062_consumption`  
  Load '52_LVBus195062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194928_consumption`  
  Load '52_LVBus194928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194910_consumption`  
  Load '52_LVBus194910_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194992_consumption`  
  Load '52_LVBus194992_consumption' has phase imbalance of 90.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195060_consumption`  
  Load '52_LVBus195060_consumption' has phase imbalance of 109.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194886_consumption`  
  Load '52_LVBus194886_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195034_consumption`  
  Load '52_LVBus195034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195086_consumption`  
  Load '52_LVBus195086_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194873_consumption`  
  Load '52_LVBus194873_consumption' has phase imbalance of 26.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194810_consumption`  
  Load '52_LVBus194810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195011_consumption`  
  Load '52_LVBus195011_consumption' has phase imbalance of 187.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194779_consumption`  
  Load '52_LVBus194779_consumption' has phase imbalance of 20.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195018_consumption`  
  Load '52_LVBus195018_consumption' has phase imbalance of 37.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195009_consumption`  
  Load '52_LVBus195009_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194793_consumption`  
  Load '52_LVBus194793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194903_consumption`  
  Load '52_LVBus194903_consumption' has phase imbalance of 170.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194892_consumption`  
  Load '52_LVBus194892_consumption' has phase imbalance of 125.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194792_consumption`  
  Load '52_LVBus194792_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194797_consumption`  
  Load '52_LVBus194797_consumption' has phase imbalance of 49.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194776_consumption`  
  Load '52_LVBus194776_consumption' has phase imbalance of 50.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194803_consumption`  
  Load '52_LVBus194803_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195013_consumption`  
  Load '52_LVBus195013_consumption' has phase imbalance of 58.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194787_consumption`  
  Load '52_LVBus194787_consumption' has phase imbalance of 105.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195020_consumption`  
  Load '52_LVBus195020_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195019_consumption`  
  Load '52_LVBus195019_consumption' has phase imbalance of 234.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194905_consumption`  
  Load '52_LVBus194905_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195124_consumption`  
  Load '52_LVBus195124_consumption' has phase imbalance of 70.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus195030_consumption`  
  Load '52_LVBus195030_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194879_consumption`  
  Load '52_LVBus194879_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus194850_consumption`  
  Load '52_LVBus194850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 580 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_DOULO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus194943' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus194733' (LV, 0.24 kV) has an electrical reach of 7.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus194763' (LV, 0.24 kV) has an electrical reach of 6.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  325 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  67 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 52_LVBus194767_consumption, 52_LVBus194775_consumption, 52_LVBus194777_consumption, 52_LVBus194792_consumption, 52_LVBus194793_consumption, 52_LVBus194798_consumption, 52_LVBus194809_consumption, 52_LVBus194810_consumption, 52_LVBus194811_consumption, 52_LVBus194812_consumption, 52_LVBus194818_consumption, 52_LVBus194826_consumption, 52_LVBus194830_consumption, 52_LVBus194831_consumption, 52_LVBus194840_consumption, 52_LVBus194841_consumption, 52_LVBus194842_consumption, 52_LVBus194850_consumption, 52_LVBus194857_consumption, 52_LVBus194863_consumption, 52_LVBus194864_consumption, 52_LVBus194871_consumption, 52_LVBus194876_consumption, 52_LVBus194879_consumption, 52_LVBus194881_consumption, 52_LVBus194883_consumption, 52_LVBus194887_consumption, 52_LVBus194890_consumption, 52_LVBus194893_consumption, 52_LVBus194895_consumption, 52_LVBus194896_consumption, 52_LVBus194897_consumption, 52_LVBus194902_consumption, 52_LVBus194905_consumption, 52_LVBus194907_consumption, 52_LVBus194908_consumption, 52_LVBus194909_consumption, 52_LVBus194914_consumption, 52_LVBus194916_consumption, 52_LVBus194918_consumption, 52_LVBus194920_consumption, 52_LVBus194928_consumption, 52_LVBus194991_consumption, 52_LVBus195002_consumption, 52_LVBus195003_consumption, 52_LVBus195007_consumption, 52_LVBus195012_consumption, 52_LVBus195014_consumption, 52_LVBus195016_consumption, 52_LVBus195019_consumption, 52_LVBus195020_consumption, 52_LVBus195021_consumption, 52_LVBus195024_consumption, 52_LVBus195025_consumption, 52_LVBus195033_consumption, 52_LVBus195034_consumption, 52_LVBus195035_consumption, 52_LVBus195038_consumption, 52_LVBus195041_consumption, 52_LVBus195045_consumption, 52_LVBus195046_consumption, 52_LVBus195048_consumption, 52_LVBus195062_consumption, 52_LVBus195063_consumption, 52_LVBus195086_consumption, 52_LVBus195096_consumption, 52_LVBus195097_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  290 group(s) of loads (580 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  388 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus194733_consumption, 52_LVBus194733_production, 52_LVBus194735_consumption, 52_LVBus194735_production, 52_LVBus194737_consumption, 52_LVBus194737_production, 52_LVBus194739_consumption, 52_LVBus194739_production, 52_LVBus194741_consumption, 52_LVBus194741_production, 52_LVBus194743_consumption, 52_LVBus194743_production, 52_LVBus194745_consumption, 52_LVBus194745_production, 52_LVBus194747_consumption, 52_LVBus194747_production, 52_LVBus194751_consumption, 52_LVBus194751_production, 52_LVBus194753_consumption, 52_LVBus194753_production, 52_LVBus194755_production, 52_LVBus194757_consumption, 52_LVBus194757_production, 52_LVBus194759_production, 52_LVBus194761_production, 52_LVBus194763_consumption, 52_LVBus194763_production, 52_LVBus194765_consumption, 52_LVBus194765_production, 52_LVBus194767_production, 52_LVBus194769_consumption, 52_LVBus194769_production, 52_LVBus194771_consumption, 52_LVBus194771_production, 52_LVBus194773_consumption, 52_LVBus194773_production, 52_LVBus194774_consumption, 52_LVBus194774_production, 52_LVBus194775_production, 52_LVBus194776_production, 52_LVBus194777_production, 52_LVBus194779_production, 52_LVBus194781_production, 52_LVBus194783_production, 52_LVBus194785_consumption, 52_LVBus194785_production, 52_LVBus194787_production, 52_LVBus194788_production, 52_LVBus194789_consumption, 52_LVBus194789_production, 52_LVBus194790_production, 52_LVBus194791_production, 52_LVBus194792_production, 52_LVBus194793_production, 52_LVBus194794_production, 52_LVBus194796_consumption, 52_LVBus194796_production, 52_LVBus194797_production, 52_LVBus194798_production, 52_LVBus194800_consumption, 52_LVBus194800_production, 52_LVBus194801_production, 52_LVBus194803_production, 52_LVBus194805_consumption, 52_LVBus194805_production, 52_LVBus194806_consumption, 52_LVBus194806_production, 52_LVBus194807_consumption, 52_LVBus194807_production, 52_LVBus194808_production, 52_LVBus194809_production, 52_LVBus194810_production, 52_LVBus194811_production, 52_LVBus194812_production, 52_LVBus194813_consumption, 52_LVBus194813_production, 52_LVBus194814_consumption, 52_LVBus194814_production, 52_LVBus194815_production, 52_LVBus194816_consumption, 52_LVBus194816_production, 52_LVBus194817_production, 52_LVBus194818_production, 52_LVBus194819_production, 52_LVBus194820_production, 52_LVBus194822_production, 52_LVBus194823_production, 52_LVBus194824_production, 52_LVBus194826_production, 52_LVBus194827_production, 52_LVBus194829_production, 52_LVBus194830_production, 52_LVBus194831_production, 52_LVBus194832_production, 52_LVBus194833_production, 52_LVBus194834_production, 52_LVBus194835_production, 52_LVBus194836_production, 52_LVBus194837_production, 52_LVBus194838_production, 52_LVBus194839_production, 52_LVBus194840_production, 52_LVBus194841_production, 52_LVBus194842_production, 52_LVBus194844_production, 52_LVBus194845_production, 52_LVBus194846_production, 52_LVBus194848_consumption, 52_LVBus194848_production, 52_LVBus194850_production, 52_LVBus194851_production, 52_LVBus194852_production, 52_LVBus194854_production, 52_LVBus194856_consumption, 52_LVBus194856_production, 52_LVBus194857_production, 52_LVBus194858_production, 52_LVBus194860_consumption, 52_LVBus194860_production, 52_LVBus194861_consumption, 52_LVBus194861_production, 52_LVBus194862_consumption, 52_LVBus194862_production, 52_LVBus194863_production, 52_LVBus194864_production, 52_LVBus194865_consumption, 52_LVBus194865_production, 52_LVBus194866_production, 52_LVBus194867_consumption, 52_LVBus194867_production, 52_LVBus194868_consumption, 52_LVBus194868_production, 52_LVBus194870_production, 52_LVBus194871_production, 52_LVBus194872_production, 52_LVBus194873_production, 52_LVBus194875_production, 52_LVBus194876_production, 52_LVBus194878_production, 52_LVBus194879_production, 52_LVBus194881_production, 52_LVBus194883_production, 52_LVBus194885_production, 52_LVBus194886_production, 52_LVBus194887_production, 52_LVBus194889_production, 52_LVBus194890_production, 52_LVBus194891_production, 52_LVBus194892_production, 52_LVBus194893_production, 52_LVBus194894_consumption, 52_LVBus194894_production, 52_LVBus194895_production, 52_LVBus194896_production, 52_LVBus194897_production, 52_LVBus194898_production, 52_LVBus194900_production, 52_LVBus194902_production, 52_LVBus194903_production, 52_LVBus194904_production, 52_LVBus194905_production, 52_LVBus194906_consumption, 52_LVBus194906_production, 52_LVBus194907_production, 52_LVBus194908_production, 52_LVBus194909_production, 52_LVBus194910_production, 52_LVBus194911_production, 52_LVBus194913_production, 52_LVBus194914_production, 52_LVBus194915_production, 52_LVBus194916_production, 52_LVBus194917_production, 52_LVBus194918_production, 52_LVBus194919_production, 52_LVBus194920_production, 52_LVBus194922_production, 52_LVBus194924_production, 52_LVBus194926_consumption, 52_LVBus194926_production, 52_LVBus194927_production, 52_LVBus194928_production, 52_LVBus194929_production, 52_LVBus194931_production, 52_LVBus194933_production, 52_LVBus194943_consumption, 52_LVBus194943_production, 52_LVBus194945_consumption, 52_LVBus194945_production, 52_LVBus194946_consumption, 52_LVBus194946_production, 52_LVBus194947_consumption, 52_LVBus194947_production, 52_LVBus194949_production, 52_LVBus194951_consumption, 52_LVBus194951_production, 52_LVBus194952_consumption, 52_LVBus194952_production, 52_LVBus194953_production, 52_LVBus194955_consumption, 52_LVBus194955_production, 52_LVBus194957_consumption, 52_LVBus194957_production, 52_LVBus194959_consumption, 52_LVBus194959_production, 52_LVBus194961_consumption, 52_LVBus194961_production, 52_LVBus194962_consumption, 52_LVBus194962_production, 52_LVBus194963_consumption, 52_LVBus194963_production, 52_LVBus194965_production, 52_LVBus194967_consumption, 52_LVBus194967_production, 52_LVBus194969_consumption, 52_LVBus194969_production, 52_LVBus194970_production, 52_LVBus194971_production, 52_LVBus194973_consumption, 52_LVBus194973_production, 52_LVBus194975_consumption, 52_LVBus194975_production, 52_LVBus194976_consumption, 52_LVBus194976_production, 52_LVBus194977_consumption, 52_LVBus194977_production, 52_LVBus194979_consumption, 52_LVBus194979_production, 52_LVBus194980_consumption, 52_LVBus194980_production, 52_LVBus194981_production, 52_LVBus194983_consumption, 52_LVBus194983_production, 52_LVBus194984_consumption, 52_LVBus194984_production, 52_LVBus194985_consumption, 52_LVBus194985_production, 52_LVBus194987_consumption, 52_LVBus194987_production, 52_LVBus194989_consumption, 52_LVBus194989_production, 52_LVBus194990_production, 52_LVBus194991_production, 52_LVBus194992_production, 52_LVBus194993_consumption, 52_LVBus194993_production, 52_LVBus194994_production, 52_LVBus194996_consumption, 52_LVBus194996_production, 52_LVBus194998_consumption, 52_LVBus194998_production, 52_LVBus195000_production, 52_LVBus195002_production, 52_LVBus195003_production, 52_LVBus195004_production, 52_LVBus195005_production, 52_LVBus195006_production, 52_LVBus195007_production, 52_LVBus195009_production, 52_LVBus195010_production, 52_LVBus195011_production, 52_LVBus195012_production, 52_LVBus195013_production, 52_LVBus195014_production, 52_LVBus195016_production, 52_LVBus195017_production, 52_LVBus195018_production, 52_LVBus195019_production, 52_LVBus195020_production, 52_LVBus195021_production, 52_LVBus195022_production, 52_LVBus195023_consumption, 52_LVBus195023_production, 52_LVBus195024_production, 52_LVBus195025_production, 52_LVBus195026_consumption, 52_LVBus195026_production, 52_LVBus195028_consumption, 52_LVBus195028_production, 52_LVBus195029_production, 52_LVBus195030_production, 52_LVBus195032_production, 52_LVBus195033_production, 52_LVBus195034_production, 52_LVBus195035_production, 52_LVBus195036_production, 52_LVBus195037_production, 52_LVBus195038_production, 52_LVBus195040_production, 52_LVBus195041_production, 52_LVBus195042_production, 52_LVBus195043_production, 52_LVBus195045_production, 52_LVBus195046_production, 52_LVBus195047_consumption, 52_LVBus195047_production, 52_LVBus195048_production, 52_LVBus195049_production, 52_LVBus195050_production, 52_LVBus195052_consumption, 52_LVBus195052_production, 52_LVBus195053_production, 52_LVBus195055_production, 52_LVBus195056_production, 52_LVBus195058_production, 52_LVBus195060_production, 52_LVBus195061_production, 52_LVBus195062_production, 52_LVBus195063_production, 52_LVBus195065_consumption, 52_LVBus195065_production, 52_LVBus195067_consumption, 52_LVBus195067_production, 52_LVBus195068_production, 52_LVBus195069_consumption, 52_LVBus195069_production, 52_LVBus195071_consumption, 52_LVBus195071_production, 52_LVBus195072_consumption, 52_LVBus195072_production, 52_LVBus195073_consumption, 52_LVBus195073_production, 52_LVBus195075_production, 52_LVBus195077_production, 52_LVBus195078_consumption, 52_LVBus195078_production, 52_LVBus195079_consumption, 52_LVBus195079_production, 52_LVBus195081_consumption, 52_LVBus195081_production, 52_LVBus195083_consumption, 52_LVBus195083_production, 52_LVBus195084_consumption, 52_LVBus195084_production, 52_LVBus195085_production, 52_LVBus195086_production, 52_LVBus195090_consumption, 52_LVBus195090_production, 52_LVBus195092_production, 52_LVBus195094_consumption, 52_LVBus195094_production, 52_LVBus195095_consumption, 52_LVBus195095_production, 52_LVBus195096_production, 52_LVBus195097_production, 52_LVBus195098_production, 52_LVBus195100_consumption, 52_LVBus195100_production, 52_LVBus195102_consumption, 52_LVBus195102_production, 52_LVBus195103_production, 52_LVBus195104_production, 52_LVBus195106_production, 52_LVBus195107_production, 52_LVBus195108_production, 52_LVBus195110_consumption, 52_LVBus195110_production, 52_LVBus195111_consumption, 52_LVBus195111_production, 52_LVBus195112_consumption, 52_LVBus195112_production, 52_LVBus195113_consumption, 52_LVBus195113_production, 52_LVBus195114_production, 52_LVBus195115_production, 52_LVBus195116_consumption, 52_LVBus195116_production, 52_LVBus195117_production, 52_LVBus195118_consumption, 52_LVBus195118_production, 52_LVBus195120_consumption, 52_LVBus195120_production, 52_LVBus195122_consumption, 52_LVBus195122_production, 52_LVBus195123_production, 52_LVBus195124_production, 52_LVBus195126_consumption, 52_LVBus195126_production, 52_LVBus195127_consumption, 52_LVBus195127_production, 52_LVBus195128_production, 52_LVBus195130_production, 52_LVBus195132_production, 52_LVBus195134_consumption, 52_LVBus195134_production, 52_MVLV002624_production, 52_MVLV023883_production, 52_MVLV064473_production.

