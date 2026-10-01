# BMOPF Network Summary: 11_MVFeeder4885

**Generated:** 2026-10-01 23:33:57  
**Findings:** 0 errors · 6 warnings · 221 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 379 |  |
| line | 358 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 652 | 2.982 MW, 894.5 kvar |
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
| MV_11.8kV | 11.78 kV | 42 | 41 | 18 | 0 |
| LV_236V | 236.0 V | 337 | 317 | 634 | 0 |

**Transformer transitions:**

- `11_MVLV22850_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV15826_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV18494_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV32114_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV24160_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV44958_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV73147_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV56427_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV06112_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV14879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV12493_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV55276_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV55277_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV73146_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV61744_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV35064_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV04468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV32144_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV14876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV73693_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 11 |
| Degree-1 buses | 151 |
| Tree depth (max hops) | 25 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 379 | 1 | 378 | 0 | 0 | 0 |
| Tier LV_236V | 337 | 20 | 317 | 0 | 0 | 0 |
| Tier MV_11.8kV | 42 | 1 | 41 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 20; skipped invalid branches: 0.

Galvanic zones: 21; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_MVBus81803 | MV_11.8kV | 42 | 0 | 0 | 20 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1474 declared bus terminals; 1391 mapped line/closed-switch conductor edges; 83 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 66700.0 | 3.653 | 1956 |
| q_nom | 0.0 | 20000.0 | 3.653 | 1956 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.19 | 1600.0 | 1.539 | 358 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.74 | 20 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 404 of 652 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909839_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910041_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909892_consumption' has phase imbalance of 107.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910016_consumption' has phase imbalance of 89.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321507_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1296094_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1332608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1301049_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909777_consumption' has phase imbalance of 153.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909896_consumption' has phase imbalance of 196.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909937_consumption' has phase imbalance of 173.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1288942_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1325554_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910029_consumption' has phase imbalance of 243.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1304920_consumption' has phase imbalance of 93.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910023_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910019_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909918_consumption' has phase imbalance of 82.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909782_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909836_consumption' has phase imbalance of 229.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909812_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308096_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910073_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909766_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909947_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1326079_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909763_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1301000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909906_consumption' has phase imbalance of 86.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1347775_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910055_consumption' has phase imbalance of 236.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909809_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321506_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909826_consumption' has phase imbalance of 70.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1347777_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909948_consumption' has phase imbalance of 214.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910064_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909877_consumption' has phase imbalance of 228.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909878_consumption' has phase imbalance of 204.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909852_consumption' has phase imbalance of 49.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909951_consumption' has phase imbalance of 155.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321504_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910025_consumption' has phase imbalance of 125.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1290185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308097_consumption' has phase imbalance of 213.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1326077_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909783_consumption' has phase imbalance of 189.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1296536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308686_consumption' has phase imbalance of 36.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308683_consumption' has phase imbalance of 76.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909943_consumption' has phase imbalance of 205.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909891_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910083_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1312385_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321510_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308160_consumption' has phase imbalance of 77.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1303765_consumption' has phase imbalance of 200.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909771_consumption' has phase imbalance of 66.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1303766_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909996_consumption' has phase imbalance of 104.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909931_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909825_consumption' has phase imbalance of 21.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909953_consumption' has phase imbalance of 232.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909871_consumption' has phase imbalance of 142.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1325555_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910003_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909904_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909925_consumption' has phase imbalance of 260.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910001_consumption' has phase imbalance of 58.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910009_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1309230_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909787_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909919_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910066_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909757_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1301050_consumption' has phase imbalance of 87.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1347774_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1336436_consumption' has phase imbalance of 73.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909764_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909854_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909845_consumption' has phase imbalance of 38.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910080_consumption' has phase imbalance of 73.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909769_consumption' has phase imbalance of 104.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910077_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308687_consumption' has phase imbalance of 124.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909874_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909932_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909775_consumption' has phase imbalance of 129.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910040_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909888_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909954_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1336437_consumption' has phase imbalance of 64.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909835_consumption' has phase imbalance of 254.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910008_consumption' has phase imbalance of 288.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909924_consumption' has phase imbalance of 214.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909998_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308688_consumption' has phase imbalance of 234.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308159_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910007_consumption' has phase imbalance of 96.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909989_consumption' has phase imbalance of 279.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1296535_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1347776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910017_consumption' has phase imbalance of 209.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909917_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909780_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910026_consumption' has phase imbalance of 131.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909756_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909824_consumption' has phase imbalance of 108.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1309233_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909761_consumption' has phase imbalance of 256.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909867_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1296537_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909936_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909857_consumption' has phase imbalance of 58.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910076_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909935_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909955_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910034_consumption' has phase imbalance of 52.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909986_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909921_consumption' has phase imbalance of 235.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909907_consumption' has phase imbalance of 117.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909786_consumption' has phase imbalance of 86.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909795_consumption' has phase imbalance of 89.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909997_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909999_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321499_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909908_consumption' has phase imbalance of 110.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910065_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909768_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308684_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910005_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909853_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1301048_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909773_consumption' has phase imbalance of 101.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909811_consumption' has phase imbalance of 54.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1309232_consumption' has phase imbalance of 209.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910047_consumption' has phase imbalance of 206.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909760_consumption' has phase imbalance of 141.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910043_consumption' has phase imbalance of 238.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909922_consumption' has phase imbalance of 138.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321500_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1309231_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909882_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1316704_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909959_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909914_consumption' has phase imbalance of 97.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909781_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1301001_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909772_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909807_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909884_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909840_consumption' has phase imbalance of 250.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909767_consumption' has phase imbalance of 139.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910013_consumption' has phase imbalance of 67.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909960_consumption' has phase imbalance of 112.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910022_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909987_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1296095_consumption' has phase imbalance of 141.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909945_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909949_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1332609_consumption' has phase imbalance of 234.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1301002_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0909913_consumption' has phase imbalance of 257.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0910030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 652 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_VERSA' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0909965' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0909805' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0909828' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.982 MW |
| Total load Q | 894.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV22850_Transformer | 110.0 kVA | 29.0% |
| 11_MVLV15826_Transformer | 110.0 kVA | 14.4% |
| 11_MVLV18494_Transformer | 693.0 kVA | 78.6% |
| 11_MVLV32114_Transformer | 440.0 kVA | 42.6% |
| 11_MVLV24160_Transformer | 440.0 kVA | 45.0% |
| 11_MVLV44958_Transformer | 110.0 kVA | 26.7% |
| 11_MVLV73147_Transformer | 176.0 kVA | 61.1% |
| 11_MVLV56427_Transformer | 110.0 kVA | 7.2% |
| 11_MVLV06112_Transformer | 110.0 kVA | 26.8% |
| 11_MVLV14879_Transformer | 110.0 kVA | 8.2% |
| 11_MVLV12493_Transformer | 110.0 kVA | 2.5% |
| 11_MVLV55276_Transformer | 693.0 kVA | 28.6% |
| 11_MVLV55277_Transformer | 440.0 kVA | 51.6% |
| 11_MVLV73146_Transformer | 110.0 kVA | 24.5% |
| 11_MVLV61744_Transformer | 275.0 kVA | 47.3% |
| 11_MVLV35064_Transformer | 275.0 kVA | 37.2% |
| 11_MVLV04468_Transformer | 275.0 kVA | 91.3% ⚠ |
| 11_MVLV32144_Transformer | 110.0 kVA | 35.7% |
| 11_MVLV14876_Transformer | 176.0 kVA | 85.1% |
| 11_MVLV73693_Transformer | 275.0 kVA | 52.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.98 MW).
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '11_MVLV04468_Transformer' is at 91.3% utilisation at nominal load — little OPF headroom.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '11_LVBus0909805' (LV, 0.24 kV) has an electrical reach of 8.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 379 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 379 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 42 |
| LV_236V | 4-wire | 337 / 337 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 337 |
| Neutral branches | 317 |
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
| 11.78 kV | 42 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 45 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 865.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 337 / 42 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 405 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 405 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0909756_production, 11_LVBus0909757_production, 11_LVBus0909758_production, 11_LVBus0909759_production, 11_LVBus0909760_production, 11_LVBus0909761_production, 11_LVBus0909763_production, 11_LVBus0909764_production, 11_LVBus0909766_production, 11_LVBus0909767_production, 11_LVBus0909768_production, 11_LVBus0909769_production, 11_LVBus0909771_production, 11_LVBus0909772_production, 11_LVBus0909773_production, 11_LVBus0909775_production, 11_LVBus0909777_production, 11_LVBus0909778_consumption, 11_LVBus0909778_production, 11_LVBus0909780_production, 11_LVBus0909781_production, 11_LVBus0909782_production, 11_LVBus0909783_production, 11_LVBus0909784_production, 11_LVBus0909786_production, 11_LVBus0909787_production, 11_LVBus0909789_production, 11_LVBus0909791_production, 11_LVBus0909793_production, 11_LVBus0909795_production, 11_LVBus0909797_consumption, 11_LVBus0909797_production, 11_LVBus0909799_consumption, 11_LVBus0909799_production, 11_LVBus0909801_production, 11_LVBus0909803_production, 11_LVBus0909805_production, 11_LVBus0909807_production, 11_LVBus0909809_production, 11_LVBus0909811_production, 11_LVBus0909812_production, 11_LVBus0909813_consumption, 11_LVBus0909813_production, 11_LVBus0909814_production, 11_LVBus0909816_production, 11_LVBus0909817_consumption, 11_LVBus0909817_production, 11_LVBus0909818_consumption, 11_LVBus0909818_production, 11_LVBus0909819_consumption, 11_LVBus0909819_production, 11_LVBus0909820_consumption, 11_LVBus0909820_production, 11_LVBus0909822_consumption, 11_LVBus0909822_production, 11_LVBus0909823_consumption, 11_LVBus0909823_production, 11_LVBus0909824_production, 11_LVBus0909825_production, 11_LVBus0909826_production, 11_LVBus0909828_production, 11_LVBus0909830_production, 11_LVBus0909832_production, 11_LVBus0909834_production, 11_LVBus0909835_production, 11_LVBus0909836_production, 11_LVBus0909838_production, 11_LVBus0909839_production, 11_LVBus0909840_production, 11_LVBus0909842_consumption, 11_LVBus0909842_production, 11_LVBus0909843_consumption, 11_LVBus0909843_production, 11_LVBus0909844_consumption, 11_LVBus0909844_production, 11_LVBus0909845_production, 11_LVBus0909846_consumption, 11_LVBus0909846_production, 11_LVBus0909848_consumption, 11_LVBus0909848_production, 11_LVBus0909849_consumption, 11_LVBus0909849_production, 11_LVBus0909850_consumption, 11_LVBus0909850_production, 11_LVBus0909851_consumption, 11_LVBus0909851_production, 11_LVBus0909852_production, 11_LVBus0909853_production, 11_LVBus0909854_production, 11_LVBus0909856_consumption, 11_LVBus0909856_production, 11_LVBus0909857_production, 11_LVBus0909859_production, 11_LVBus0909860_production, 11_LVBus0909861_consumption, 11_LVBus0909861_production, 11_LVBus0909862_consumption, 11_LVBus0909862_production, 11_LVBus0909863_production, 11_LVBus0909864_production, 11_LVBus0909865_consumption, 11_LVBus0909865_production, 11_LVBus0909867_production, 11_LVBus0909868_consumption, 11_LVBus0909868_production, 11_LVBus0909869_production, 11_LVBus0909871_production, 11_LVBus0909872_consumption, 11_LVBus0909872_production, 11_LVBus0909874_production, 11_LVBus0909875_consumption, 11_LVBus0909875_production, 11_LVBus0909877_production, 11_LVBus0909878_production, 11_LVBus0909880_production, 11_LVBus0909882_production, 11_LVBus0909883_production, 11_LVBus0909884_production, 11_LVBus0909886_consumption, 11_LVBus0909886_production, 11_LVBus0909888_production, 11_LVBus0909889_consumption, 11_LVBus0909889_production, 11_LVBus0909891_production, 11_LVBus0909892_production, 11_LVBus0909894_consumption, 11_LVBus0909894_production, 11_LVBus0909896_production, 11_LVBus0909897_production, 11_LVBus0909899_consumption, 11_LVBus0909899_production, 11_LVBus0909900_consumption, 11_LVBus0909900_production, 11_LVBus0909902_production, 11_LVBus0909904_production, 11_LVBus0909905_consumption, 11_LVBus0909905_production, 11_LVBus0909906_production, 11_LVBus0909907_production, 11_LVBus0909908_production, 11_LVBus0909909_consumption, 11_LVBus0909909_production, 11_LVBus0909911_production, 11_LVBus0909913_production, 11_LVBus0909914_production, 11_LVBus0909915_production, 11_LVBus0909917_production, 11_LVBus0909918_production, 11_LVBus0909919_production, 11_LVBus0909921_production, 11_LVBus0909922_production, 11_LVBus0909923_consumption, 11_LVBus0909923_production, 11_LVBus0909924_production, 11_LVBus0909925_production, 11_LVBus0909926_production, 11_LVBus0909927_production, 11_LVBus0909928_consumption, 11_LVBus0909928_production, 11_LVBus0909930_production, 11_LVBus0909931_production, 11_LVBus0909932_production, 11_LVBus0909933_consumption, 11_LVBus0909933_production, 11_LVBus0909934_consumption, 11_LVBus0909934_production, 11_LVBus0909935_production, 11_LVBus0909936_production, 11_LVBus0909937_production, 11_LVBus0909938_production, 11_LVBus0909939_production, 11_LVBus0909940_production, 11_LVBus0909941_production, 11_LVBus0909943_production, 11_LVBus0909944_production, 11_LVBus0909945_production, 11_LVBus0909947_production, 11_LVBus0909948_production, 11_LVBus0909949_production, 11_LVBus0909951_production, 11_LVBus0909953_production, 11_LVBus0909954_production, 11_LVBus0909955_production, 11_LVBus0909957_consumption, 11_LVBus0909957_production, 11_LVBus0909959_production, 11_LVBus0909960_production, 11_LVBus0909961_production, 11_LVBus0909962_production, 11_LVBus0909965_consumption, 11_LVBus0909965_production, 11_LVBus0909967_production, 11_LVBus0909969_consumption, 11_LVBus0909969_production, 11_LVBus0909971_production, 11_LVBus0909973_consumption, 11_LVBus0909973_production, 11_LVBus0909974_production, 11_LVBus0909975_consumption, 11_LVBus0909975_production, 11_LVBus0909976_production, 11_LVBus0909978_production, 11_LVBus0909979_production, 11_LVBus0909981_production, 11_LVBus0909986_production, 11_LVBus0909987_production, 11_LVBus0909989_production, 11_LVBus0909990_consumption, 11_LVBus0909990_production, 11_LVBus0909991_production, 11_LVBus0909992_consumption, 11_LVBus0909992_production, 11_LVBus0909993_consumption, 11_LVBus0909993_production, 11_LVBus0909994_consumption, 11_LVBus0909994_production, 11_LVBus0909995_consumption, 11_LVBus0909995_production, 11_LVBus0909996_production, 11_LVBus0909997_production, 11_LVBus0909998_production, 11_LVBus0909999_production, 11_LVBus0910001_production, 11_LVBus0910002_production, 11_LVBus0910003_production, 11_LVBus0910005_production, 11_LVBus0910006_production, 11_LVBus0910007_production, 11_LVBus0910008_production, 11_LVBus0910009_production, 11_LVBus0910010_production, 11_LVBus0910011_production, 11_LVBus0910013_production, 11_LVBus0910014_consumption, 11_LVBus0910014_production, 11_LVBus0910015_consumption, 11_LVBus0910015_production, 11_LVBus0910016_production, 11_LVBus0910017_production, 11_LVBus0910018_production, 11_LVBus0910019_production, 11_LVBus0910020_production, 11_LVBus0910021_production, 11_LVBus0910022_production, 11_LVBus0910023_production, 11_LVBus0910025_production, 11_LVBus0910026_production, 11_LVBus0910028_consumption, 11_LVBus0910028_production, 11_LVBus0910029_production, 11_LVBus0910030_production, 11_LVBus0910031_production, 11_LVBus0910032_production, 11_LVBus0910034_production, 11_LVBus0910036_consumption, 11_LVBus0910036_production, 11_LVBus0910038_production, 11_LVBus0910039_production, 11_LVBus0910040_production, 11_LVBus0910041_production, 11_LVBus0910043_production, 11_LVBus0910045_consumption, 11_LVBus0910045_production, 11_LVBus0910047_production, 11_LVBus0910049_production, 11_LVBus0910051_production, 11_LVBus0910052_production, 11_LVBus0910053_consumption, 11_LVBus0910053_production, 11_LVBus0910055_production, 11_LVBus0910056_consumption, 11_LVBus0910056_production, 11_LVBus0910057_production, 11_LVBus0910059_production, 11_LVBus0910061_consumption, 11_LVBus0910061_production, 11_LVBus0910062_consumption, 11_LVBus0910062_production, 11_LVBus0910063_consumption, 11_LVBus0910063_production, 11_LVBus0910064_production, 11_LVBus0910065_production, 11_LVBus0910066_production, 11_LVBus0910068_production, 11_LVBus0910069_production, 11_LVBus0910070_production, 11_LVBus0910071_production, 11_LVBus0910073_production, 11_LVBus0910074_production, 11_LVBus0910076_production, 11_LVBus0910077_production, 11_LVBus0910078_consumption, 11_LVBus0910078_production, 11_LVBus0910080_production, 11_LVBus0910081_production, 11_LVBus0910083_production, 11_LVBus0910085_production, 11_LVBus0910086_consumption, 11_LVBus0910086_production, 11_LVBus0910087_consumption, 11_LVBus0910087_production, 11_LVBus0910089_consumption, 11_LVBus0910089_production, 11_LVBus0910090_production, 11_LVBus0910092_production, 11_LVBus1284669_consumption, 11_LVBus1284669_production, 11_LVBus1284670_consumption, 11_LVBus1284670_production, 11_LVBus1288941_consumption, 11_LVBus1288941_production, 11_LVBus1288942_production, 11_LVBus1290184_consumption, 11_LVBus1290184_production, 11_LVBus1290185_production, 11_LVBus1290186_consumption, 11_LVBus1290186_production, 11_LVBus1294818_consumption, 11_LVBus1294818_production, 11_LVBus1296094_production, 11_LVBus1296095_production, 11_LVBus1296535_production, 11_LVBus1296536_production, 11_LVBus1296537_production, 11_LVBus1301000_production, 11_LVBus1301001_production, 11_LVBus1301002_production, 11_LVBus1301047_consumption, 11_LVBus1301047_production, 11_LVBus1301048_production, 11_LVBus1301049_production, 11_LVBus1301050_production, 11_LVBus1303765_production, 11_LVBus1303766_production, 11_LVBus1304920_production, 11_LVBus1308096_production, 11_LVBus1308097_production, 11_LVBus1308159_production, 11_LVBus1308160_production, 11_LVBus1308682_consumption, 11_LVBus1308682_production, 11_LVBus1308683_production, 11_LVBus1308684_production, 11_LVBus1308685_consumption, 11_LVBus1308685_production, 11_LVBus1308686_production, 11_LVBus1308687_production, 11_LVBus1308688_production, 11_LVBus1308689_consumption, 11_LVBus1308689_production, 11_LVBus1308690_production, 11_LVBus1309230_production, 11_LVBus1309231_production, 11_LVBus1309232_production, 11_LVBus1309233_production, 11_LVBus1312384_production, 11_LVBus1312385_production, 11_LVBus1316704_production, 11_LVBus1318107_production, 11_LVBus1321499_production, 11_LVBus1321500_production, 11_LVBus1321501_production, 11_LVBus1321502_consumption, 11_LVBus1321502_production, 11_LVBus1321503_production, 11_LVBus1321504_production, 11_LVBus1321505_production, 11_LVBus1321506_production, 11_LVBus1321507_production, 11_LVBus1321508_production, 11_LVBus1321509_production, 11_LVBus1321510_production, 11_LVBus1325554_production, 11_LVBus1325555_production, 11_LVBus1326077_production, 11_LVBus1326078_consumption, 11_LVBus1326078_production, 11_LVBus1326079_production, 11_LVBus1332608_production, 11_LVBus1332609_production, 11_LVBus1336436_production, 11_LVBus1336437_production, 11_LVBus1338984_consumption, 11_LVBus1338984_production, 11_LVBus1338985_consumption, 11_LVBus1338985_production, 11_LVBus1342255_production, 11_LVBus1347774_production, 11_LVBus1347775_production, 11_LVBus1347776_production, 11_LVBus1347777_production, 11_MVLV03967_production, 11_MVLV04460_consumption, 11_MVLV04460_production, 11_MVLV18993_consumption, 11_MVLV18993_production, 11_MVLV32444_production, 11_MVLV42429_consumption, 11_MVLV42429_production, 11_MVLV45743_consumption, 11_MVLV45743_production, 11_MVLV47113_production, 11_MVLV63172_production, 11_MVLV74366_consumption, 11_MVLV74366_production.

## 9. Data Quality Summary

**Total findings:** 227 (0 errors, 6 warnings, 221 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  404 of 652 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.98 MW).
- **[W.OPS.XFMR_OVERLOADED]** `11_MVLV04468_Transformer`  
  Transformer '11_MVLV04468_Transformer' is at 91.3% utilisation at nominal load — little OPF headroom.
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  405 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909839_consumption`  
  Load '11_LVBus0909839_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910041_consumption`  
  Load '11_LVBus0910041_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909897_consumption`  
  Load '11_LVBus0909897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909892_consumption`  
  Load '11_LVBus0909892_consumption' has phase imbalance of 107.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910016_consumption`  
  Load '11_LVBus0910016_consumption' has phase imbalance of 89.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321507_consumption`  
  Load '11_LVBus1321507_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1296094_consumption`  
  Load '11_LVBus1296094_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1332608_consumption`  
  Load '11_LVBus1332608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1301049_consumption`  
  Load '11_LVBus1301049_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909961_consumption`  
  Load '11_LVBus0909961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909911_consumption`  
  Load '11_LVBus0909911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909777_consumption`  
  Load '11_LVBus0909777_consumption' has phase imbalance of 153.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910068_consumption`  
  Load '11_LVBus0910068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909991_consumption`  
  Load '11_LVBus0909991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909896_consumption`  
  Load '11_LVBus0909896_consumption' has phase imbalance of 196.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910071_consumption`  
  Load '11_LVBus0910071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321505_consumption`  
  Load '11_LVBus1321505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909937_consumption`  
  Load '11_LVBus0909937_consumption' has phase imbalance of 173.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909859_consumption`  
  Load '11_LVBus0909859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1288942_consumption`  
  Load '11_LVBus1288942_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910020_consumption`  
  Load '11_LVBus0910020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1325554_consumption`  
  Load '11_LVBus1325554_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910029_consumption`  
  Load '11_LVBus0910029_consumption' has phase imbalance of 243.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1304920_consumption`  
  Load '11_LVBus1304920_consumption' has phase imbalance of 93.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910023_consumption`  
  Load '11_LVBus0910023_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910019_consumption`  
  Load '11_LVBus0910019_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909918_consumption`  
  Load '11_LVBus0909918_consumption' has phase imbalance of 82.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909782_consumption`  
  Load '11_LVBus0909782_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909836_consumption`  
  Load '11_LVBus0909836_consumption' has phase imbalance of 229.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909812_consumption`  
  Load '11_LVBus0909812_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308096_consumption`  
  Load '11_LVBus1308096_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910073_consumption`  
  Load '11_LVBus0910073_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909766_consumption`  
  Load '11_LVBus0909766_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909947_consumption`  
  Load '11_LVBus0909947_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1326079_consumption`  
  Load '11_LVBus1326079_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910039_consumption`  
  Load '11_LVBus0910039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909763_consumption`  
  Load '11_LVBus0909763_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909759_consumption`  
  Load '11_LVBus0909759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1301000_consumption`  
  Load '11_LVBus1301000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910052_consumption`  
  Load '11_LVBus0910052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910032_consumption`  
  Load '11_LVBus0910032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909906_consumption`  
  Load '11_LVBus0909906_consumption' has phase imbalance of 86.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1347775_consumption`  
  Load '11_LVBus1347775_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910055_consumption`  
  Load '11_LVBus0910055_consumption' has phase imbalance of 236.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909809_consumption`  
  Load '11_LVBus0909809_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321506_consumption`  
  Load '11_LVBus1321506_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909826_consumption`  
  Load '11_LVBus0909826_consumption' has phase imbalance of 70.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1347777_consumption`  
  Load '11_LVBus1347777_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909948_consumption`  
  Load '11_LVBus0909948_consumption' has phase imbalance of 214.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910064_consumption`  
  Load '11_LVBus0910064_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909877_consumption`  
  Load '11_LVBus0909877_consumption' has phase imbalance of 228.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909758_consumption`  
  Load '11_LVBus0909758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909878_consumption`  
  Load '11_LVBus0909878_consumption' has phase imbalance of 204.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909852_consumption`  
  Load '11_LVBus0909852_consumption' has phase imbalance of 49.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909915_consumption`  
  Load '11_LVBus0909915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909951_consumption`  
  Load '11_LVBus0909951_consumption' has phase imbalance of 155.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910081_consumption`  
  Load '11_LVBus0910081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321504_consumption`  
  Load '11_LVBus1321504_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910025_consumption`  
  Load '11_LVBus0910025_consumption' has phase imbalance of 125.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1290185_consumption`  
  Load '11_LVBus1290185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308097_consumption`  
  Load '11_LVBus1308097_consumption' has phase imbalance of 213.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1326077_consumption`  
  Load '11_LVBus1326077_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909783_consumption`  
  Load '11_LVBus0909783_consumption' has phase imbalance of 189.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1296536_consumption`  
  Load '11_LVBus1296536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910090_consumption`  
  Load '11_LVBus0910090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308686_consumption`  
  Load '11_LVBus1308686_consumption' has phase imbalance of 36.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308683_consumption`  
  Load '11_LVBus1308683_consumption' has phase imbalance of 76.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909943_consumption`  
  Load '11_LVBus0909943_consumption' has phase imbalance of 205.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909891_consumption`  
  Load '11_LVBus0909891_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910083_consumption`  
  Load '11_LVBus0910083_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1312385_consumption`  
  Load '11_LVBus1312385_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321510_consumption`  
  Load '11_LVBus1321510_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909926_consumption`  
  Load '11_LVBus0909926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308160_consumption`  
  Load '11_LVBus1308160_consumption' has phase imbalance of 77.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1303765_consumption`  
  Load '11_LVBus1303765_consumption' has phase imbalance of 200.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321509_consumption`  
  Load '11_LVBus1321509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909771_consumption`  
  Load '11_LVBus0909771_consumption' has phase imbalance of 66.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1303766_consumption`  
  Load '11_LVBus1303766_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909996_consumption`  
  Load '11_LVBus0909996_consumption' has phase imbalance of 104.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909931_consumption`  
  Load '11_LVBus0909931_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321503_consumption`  
  Load '11_LVBus1321503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909825_consumption`  
  Load '11_LVBus0909825_consumption' has phase imbalance of 21.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909953_consumption`  
  Load '11_LVBus0909953_consumption' has phase imbalance of 232.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909871_consumption`  
  Load '11_LVBus0909871_consumption' has phase imbalance of 142.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1325555_consumption`  
  Load '11_LVBus1325555_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910003_consumption`  
  Load '11_LVBus0910003_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909904_consumption`  
  Load '11_LVBus0909904_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909925_consumption`  
  Load '11_LVBus0909925_consumption' has phase imbalance of 260.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910001_consumption`  
  Load '11_LVBus0910001_consumption' has phase imbalance of 58.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910009_consumption`  
  Load '11_LVBus0910009_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1309230_consumption`  
  Load '11_LVBus1309230_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909787_consumption`  
  Load '11_LVBus0909787_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909919_consumption`  
  Load '11_LVBus0909919_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910066_consumption`  
  Load '11_LVBus0910066_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909757_consumption`  
  Load '11_LVBus0909757_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1301050_consumption`  
  Load '11_LVBus1301050_consumption' has phase imbalance of 87.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910006_consumption`  
  Load '11_LVBus0910006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1347774_consumption`  
  Load '11_LVBus1347774_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909784_consumption`  
  Load '11_LVBus0909784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1336436_consumption`  
  Load '11_LVBus1336436_consumption' has phase imbalance of 73.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909764_consumption`  
  Load '11_LVBus0909764_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909854_consumption`  
  Load '11_LVBus0909854_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909845_consumption`  
  Load '11_LVBus0909845_consumption' has phase imbalance of 38.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910080_consumption`  
  Load '11_LVBus0910080_consumption' has phase imbalance of 73.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909769_consumption`  
  Load '11_LVBus0909769_consumption' has phase imbalance of 104.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910077_consumption`  
  Load '11_LVBus0910077_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308687_consumption`  
  Load '11_LVBus1308687_consumption' has phase imbalance of 124.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909874_consumption`  
  Load '11_LVBus0909874_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909932_consumption`  
  Load '11_LVBus0909932_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909775_consumption`  
  Load '11_LVBus0909775_consumption' has phase imbalance of 129.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909939_consumption`  
  Load '11_LVBus0909939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910040_consumption`  
  Load '11_LVBus0910040_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909888_consumption`  
  Load '11_LVBus0909888_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909954_consumption`  
  Load '11_LVBus0909954_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1336437_consumption`  
  Load '11_LVBus1336437_consumption' has phase imbalance of 64.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909835_consumption`  
  Load '11_LVBus0909835_consumption' has phase imbalance of 254.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910008_consumption`  
  Load '11_LVBus0910008_consumption' has phase imbalance of 288.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909924_consumption`  
  Load '11_LVBus0909924_consumption' has phase imbalance of 214.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909998_consumption`  
  Load '11_LVBus0909998_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308688_consumption`  
  Load '11_LVBus1308688_consumption' has phase imbalance of 234.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308159_consumption`  
  Load '11_LVBus1308159_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910007_consumption`  
  Load '11_LVBus0910007_consumption' has phase imbalance of 96.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909989_consumption`  
  Load '11_LVBus0909989_consumption' has phase imbalance of 279.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1296535_consumption`  
  Load '11_LVBus1296535_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909883_consumption`  
  Load '11_LVBus0909883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1347776_consumption`  
  Load '11_LVBus1347776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910069_consumption`  
  Load '11_LVBus0910069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910011_consumption`  
  Load '11_LVBus0910011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910017_consumption`  
  Load '11_LVBus0910017_consumption' has phase imbalance of 209.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909917_consumption`  
  Load '11_LVBus0909917_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909780_consumption`  
  Load '11_LVBus0909780_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910026_consumption`  
  Load '11_LVBus0910026_consumption' has phase imbalance of 131.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909756_consumption`  
  Load '11_LVBus0909756_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910010_consumption`  
  Load '11_LVBus0910010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909824_consumption`  
  Load '11_LVBus0909824_consumption' has phase imbalance of 108.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1309233_consumption`  
  Load '11_LVBus1309233_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909761_consumption`  
  Load '11_LVBus0909761_consumption' has phase imbalance of 256.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909838_consumption`  
  Load '11_LVBus0909838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909867_consumption`  
  Load '11_LVBus0909867_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1296537_consumption`  
  Load '11_LVBus1296537_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909936_consumption`  
  Load '11_LVBus0909936_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909857_consumption`  
  Load '11_LVBus0909857_consumption' has phase imbalance of 58.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910076_consumption`  
  Load '11_LVBus0910076_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909935_consumption`  
  Load '11_LVBus0909935_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909955_consumption`  
  Load '11_LVBus0909955_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910034_consumption`  
  Load '11_LVBus0910034_consumption' has phase imbalance of 52.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909986_consumption`  
  Load '11_LVBus0909986_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909921_consumption`  
  Load '11_LVBus0909921_consumption' has phase imbalance of 235.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909907_consumption`  
  Load '11_LVBus0909907_consumption' has phase imbalance of 117.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909786_consumption`  
  Load '11_LVBus0909786_consumption' has phase imbalance of 86.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909795_consumption`  
  Load '11_LVBus0909795_consumption' has phase imbalance of 89.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909997_consumption`  
  Load '11_LVBus0909997_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909999_consumption`  
  Load '11_LVBus0909999_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321499_consumption`  
  Load '11_LVBus1321499_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909908_consumption`  
  Load '11_LVBus0909908_consumption' has phase imbalance of 110.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910065_consumption`  
  Load '11_LVBus0910065_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909768_consumption`  
  Load '11_LVBus0909768_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910031_consumption`  
  Load '11_LVBus0910031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909930_consumption`  
  Load '11_LVBus0909930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308684_consumption`  
  Load '11_LVBus1308684_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910005_consumption`  
  Load '11_LVBus0910005_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910070_consumption`  
  Load '11_LVBus0910070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909853_consumption`  
  Load '11_LVBus0909853_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1301048_consumption`  
  Load '11_LVBus1301048_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909773_consumption`  
  Load '11_LVBus0909773_consumption' has phase imbalance of 101.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909811_consumption`  
  Load '11_LVBus0909811_consumption' has phase imbalance of 54.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1309232_consumption`  
  Load '11_LVBus1309232_consumption' has phase imbalance of 209.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910047_consumption`  
  Load '11_LVBus0910047_consumption' has phase imbalance of 206.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909760_consumption`  
  Load '11_LVBus0909760_consumption' has phase imbalance of 141.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910043_consumption`  
  Load '11_LVBus0910043_consumption' has phase imbalance of 238.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909922_consumption`  
  Load '11_LVBus0909922_consumption' has phase imbalance of 138.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321500_consumption`  
  Load '11_LVBus1321500_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910038_consumption`  
  Load '11_LVBus0910038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1309231_consumption`  
  Load '11_LVBus1309231_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909882_consumption`  
  Load '11_LVBus0909882_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1316704_consumption`  
  Load '11_LVBus1316704_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909959_consumption`  
  Load '11_LVBus0909959_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909914_consumption`  
  Load '11_LVBus0909914_consumption' has phase imbalance of 97.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909781_consumption`  
  Load '11_LVBus0909781_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1301001_consumption`  
  Load '11_LVBus1301001_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909772_consumption`  
  Load '11_LVBus0909772_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909807_consumption`  
  Load '11_LVBus0909807_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909884_consumption`  
  Load '11_LVBus0909884_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909840_consumption`  
  Load '11_LVBus0909840_consumption' has phase imbalance of 250.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909767_consumption`  
  Load '11_LVBus0909767_consumption' has phase imbalance of 139.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910013_consumption`  
  Load '11_LVBus0910013_consumption' has phase imbalance of 67.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909960_consumption`  
  Load '11_LVBus0909960_consumption' has phase imbalance of 112.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321501_consumption`  
  Load '11_LVBus1321501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910022_consumption`  
  Load '11_LVBus0910022_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910021_consumption`  
  Load '11_LVBus0910021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909987_consumption`  
  Load '11_LVBus0909987_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1296095_consumption`  
  Load '11_LVBus1296095_consumption' has phase imbalance of 141.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909945_consumption`  
  Load '11_LVBus0909945_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909949_consumption`  
  Load '11_LVBus0909949_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321508_consumption`  
  Load '11_LVBus1321508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1332609_consumption`  
  Load '11_LVBus1332609_consumption' has phase imbalance of 234.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910018_consumption`  
  Load '11_LVBus0910018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910074_consumption`  
  Load '11_LVBus0910074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1301002_consumption`  
  Load '11_LVBus1301002_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0909913_consumption`  
  Load '11_LVBus0909913_consumption' has phase imbalance of 257.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0910030_consumption`  
  Load '11_LVBus0910030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 652 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_VERSA' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0909965' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0909805' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0909828' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '11_LVBus0909805' (LV, 0.24 kV) has an electrical reach of 8.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  379 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  115 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus0909756_consumption, 11_LVBus0909758_consumption, 11_LVBus0909759_consumption, 11_LVBus0909761_consumption, 11_LVBus0909764_consumption, 11_LVBus0909768_consumption, 11_LVBus0909772_consumption, 11_LVBus0909777_consumption, 11_LVBus0909780_consumption, 11_LVBus0909781_consumption, 11_LVBus0909784_consumption, 11_LVBus0909807_consumption, 11_LVBus0909809_consumption, 11_LVBus0909835_consumption, 11_LVBus0909836_consumption, 11_LVBus0909838_consumption, 11_LVBus0909839_consumption, 11_LVBus0909840_consumption, 11_LVBus0909854_consumption, 11_LVBus0909859_consumption, 11_LVBus0909867_consumption, 11_LVBus0909877_consumption, 11_LVBus0909878_consumption, 11_LVBus0909883_consumption, 11_LVBus0909891_consumption, 11_LVBus0909897_consumption, 11_LVBus0909911_consumption, 11_LVBus0909913_consumption, 11_LVBus0909915_consumption, 11_LVBus0909919_consumption, 11_LVBus0909921_consumption, 11_LVBus0909924_consumption, 11_LVBus0909925_consumption, 11_LVBus0909926_consumption, 11_LVBus0909930_consumption, 11_LVBus0909931_consumption, 11_LVBus0909932_consumption, 11_LVBus0909936_consumption, 11_LVBus0909937_consumption, 11_LVBus0909939_consumption, 11_LVBus0909943_consumption, 11_LVBus0909945_consumption, 11_LVBus0909948_consumption, 11_LVBus0909949_consumption, 11_LVBus0909951_consumption, 11_LVBus0909954_consumption, 11_LVBus0909955_consumption, 11_LVBus0909959_consumption, 11_LVBus0909961_consumption, 11_LVBus0909986_consumption, 11_LVBus0909989_consumption, 11_LVBus0909991_consumption, 11_LVBus0909997_consumption, 11_LVBus0909998_consumption, 11_LVBus0909999_consumption, 11_LVBus0910006_consumption, 11_LVBus0910008_consumption, 11_LVBus0910010_consumption, 11_LVBus0910011_consumption, 11_LVBus0910018_consumption, 11_LVBus0910019_consumption, 11_LVBus0910020_consumption, 11_LVBus0910021_consumption, 11_LVBus0910023_consumption, 11_LVBus0910029_consumption, 11_LVBus0910030_consumption, 11_LVBus0910031_consumption, 11_LVBus0910032_consumption, 11_LVBus0910038_consumption, 11_LVBus0910039_consumption, 11_LVBus0910040_consumption, 11_LVBus0910041_consumption, 11_LVBus0910043_consumption, 11_LVBus0910052_consumption, 11_LVBus0910055_consumption, 11_LVBus0910064_consumption, 11_LVBus0910066_consumption, 11_LVBus0910068_consumption, 11_LVBus0910069_consumption, 11_LVBus0910070_consumption, 11_LVBus0910071_consumption, 11_LVBus0910074_consumption, 11_LVBus0910076_consumption, 11_LVBus0910081_consumption, 11_LVBus0910090_consumption, 11_LVBus1288942_consumption, 11_LVBus1290185_consumption, 11_LVBus1296094_consumption, 11_LVBus1296535_consumption, 11_LVBus1296536_consumption, 11_LVBus1296537_consumption, 11_LVBus1301000_consumption, 11_LVBus1301048_consumption, 11_LVBus1303765_consumption, 11_LVBus1308096_consumption, 11_LVBus1308097_consumption, 11_LVBus1308688_consumption, 11_LVBus1309230_consumption, 11_LVBus1309232_consumption, 11_LVBus1316704_consumption, 11_LVBus1321499_consumption, 11_LVBus1321500_consumption, 11_LVBus1321501_consumption, 11_LVBus1321503_consumption, 11_LVBus1321504_consumption, 11_LVBus1321505_consumption, 11_LVBus1321508_consumption, 11_LVBus1321509_consumption, 11_LVBus1321510_consumption, 11_LVBus1325554_consumption, 11_LVBus1325555_consumption, 11_LVBus1326077_consumption, 11_LVBus1332608_consumption, 11_LVBus1332609_consumption, 11_LVBus1347776_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  326 group(s) of loads (652 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  3 group(s) of series lines (6 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  405 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0909756_production, 11_LVBus0909757_production, 11_LVBus0909758_production, 11_LVBus0909759_production, 11_LVBus0909760_production, 11_LVBus0909761_production, 11_LVBus0909763_production, 11_LVBus0909764_production, 11_LVBus0909766_production, 11_LVBus0909767_production, 11_LVBus0909768_production, 11_LVBus0909769_production, 11_LVBus0909771_production, 11_LVBus0909772_production, 11_LVBus0909773_production, 11_LVBus0909775_production, 11_LVBus0909777_production, 11_LVBus0909778_consumption, 11_LVBus0909778_production, 11_LVBus0909780_production, 11_LVBus0909781_production, 11_LVBus0909782_production, 11_LVBus0909783_production, 11_LVBus0909784_production, 11_LVBus0909786_production, 11_LVBus0909787_production, 11_LVBus0909789_production, 11_LVBus0909791_production, 11_LVBus0909793_production, 11_LVBus0909795_production, 11_LVBus0909797_consumption, 11_LVBus0909797_production, 11_LVBus0909799_consumption, 11_LVBus0909799_production, 11_LVBus0909801_production, 11_LVBus0909803_production, 11_LVBus0909805_production, 11_LVBus0909807_production, 11_LVBus0909809_production, 11_LVBus0909811_production, 11_LVBus0909812_production, 11_LVBus0909813_consumption, 11_LVBus0909813_production, 11_LVBus0909814_production, 11_LVBus0909816_production, 11_LVBus0909817_consumption, 11_LVBus0909817_production, 11_LVBus0909818_consumption, 11_LVBus0909818_production, 11_LVBus0909819_consumption, 11_LVBus0909819_production, 11_LVBus0909820_consumption, 11_LVBus0909820_production, 11_LVBus0909822_consumption, 11_LVBus0909822_production, 11_LVBus0909823_consumption, 11_LVBus0909823_production, 11_LVBus0909824_production, 11_LVBus0909825_production, 11_LVBus0909826_production, 11_LVBus0909828_production, 11_LVBus0909830_production, 11_LVBus0909832_production, 11_LVBus0909834_production, 11_LVBus0909835_production, 11_LVBus0909836_production, 11_LVBus0909838_production, 11_LVBus0909839_production, 11_LVBus0909840_production, 11_LVBus0909842_consumption, 11_LVBus0909842_production, 11_LVBus0909843_consumption, 11_LVBus0909843_production, 11_LVBus0909844_consumption, 11_LVBus0909844_production, 11_LVBus0909845_production, 11_LVBus0909846_consumption, 11_LVBus0909846_production, 11_LVBus0909848_consumption, 11_LVBus0909848_production, 11_LVBus0909849_consumption, 11_LVBus0909849_production, 11_LVBus0909850_consumption, 11_LVBus0909850_production, 11_LVBus0909851_consumption, 11_LVBus0909851_production, 11_LVBus0909852_production, 11_LVBus0909853_production, 11_LVBus0909854_production, 11_LVBus0909856_consumption, 11_LVBus0909856_production, 11_LVBus0909857_production, 11_LVBus0909859_production, 11_LVBus0909860_production, 11_LVBus0909861_consumption, 11_LVBus0909861_production, 11_LVBus0909862_consumption, 11_LVBus0909862_production, 11_LVBus0909863_production, 11_LVBus0909864_production, 11_LVBus0909865_consumption, 11_LVBus0909865_production, 11_LVBus0909867_production, 11_LVBus0909868_consumption, 11_LVBus0909868_production, 11_LVBus0909869_production, 11_LVBus0909871_production, 11_LVBus0909872_consumption, 11_LVBus0909872_production, 11_LVBus0909874_production, 11_LVBus0909875_consumption, 11_LVBus0909875_production, 11_LVBus0909877_production, 11_LVBus0909878_production, 11_LVBus0909880_production, 11_LVBus0909882_production, 11_LVBus0909883_production, 11_LVBus0909884_production, 11_LVBus0909886_consumption, 11_LVBus0909886_production, 11_LVBus0909888_production, 11_LVBus0909889_consumption, 11_LVBus0909889_production, 11_LVBus0909891_production, 11_LVBus0909892_production, 11_LVBus0909894_consumption, 11_LVBus0909894_production, 11_LVBus0909896_production, 11_LVBus0909897_production, 11_LVBus0909899_consumption, 11_LVBus0909899_production, 11_LVBus0909900_consumption, 11_LVBus0909900_production, 11_LVBus0909902_production, 11_LVBus0909904_production, 11_LVBus0909905_consumption, 11_LVBus0909905_production, 11_LVBus0909906_production, 11_LVBus0909907_production, 11_LVBus0909908_production, 11_LVBus0909909_consumption, 11_LVBus0909909_production, 11_LVBus0909911_production, 11_LVBus0909913_production, 11_LVBus0909914_production, 11_LVBus0909915_production, 11_LVBus0909917_production, 11_LVBus0909918_production, 11_LVBus0909919_production, 11_LVBus0909921_production, 11_LVBus0909922_production, 11_LVBus0909923_consumption, 11_LVBus0909923_production, 11_LVBus0909924_production, 11_LVBus0909925_production, 11_LVBus0909926_production, 11_LVBus0909927_production, 11_LVBus0909928_consumption, 11_LVBus0909928_production, 11_LVBus0909930_production, 11_LVBus0909931_production, 11_LVBus0909932_production, 11_LVBus0909933_consumption, 11_LVBus0909933_production, 11_LVBus0909934_consumption, 11_LVBus0909934_production, 11_LVBus0909935_production, 11_LVBus0909936_production, 11_LVBus0909937_production, 11_LVBus0909938_production, 11_LVBus0909939_production, 11_LVBus0909940_production, 11_LVBus0909941_production, 11_LVBus0909943_production, 11_LVBus0909944_production, 11_LVBus0909945_production, 11_LVBus0909947_production, 11_LVBus0909948_production, 11_LVBus0909949_production, 11_LVBus0909951_production, 11_LVBus0909953_production, 11_LVBus0909954_production, 11_LVBus0909955_production, 11_LVBus0909957_consumption, 11_LVBus0909957_production, 11_LVBus0909959_production, 11_LVBus0909960_production, 11_LVBus0909961_production, 11_LVBus0909962_production, 11_LVBus0909965_consumption, 11_LVBus0909965_production, 11_LVBus0909967_production, 11_LVBus0909969_consumption, 11_LVBus0909969_production, 11_LVBus0909971_production, 11_LVBus0909973_consumption, 11_LVBus0909973_production, 11_LVBus0909974_production, 11_LVBus0909975_consumption, 11_LVBus0909975_production, 11_LVBus0909976_production, 11_LVBus0909978_production, 11_LVBus0909979_production, 11_LVBus0909981_production, 11_LVBus0909986_production, 11_LVBus0909987_production, 11_LVBus0909989_production, 11_LVBus0909990_consumption, 11_LVBus0909990_production, 11_LVBus0909991_production, 11_LVBus0909992_consumption, 11_LVBus0909992_production, 11_LVBus0909993_consumption, 11_LVBus0909993_production, 11_LVBus0909994_consumption, 11_LVBus0909994_production, 11_LVBus0909995_consumption, 11_LVBus0909995_production, 11_LVBus0909996_production, 11_LVBus0909997_production, 11_LVBus0909998_production, 11_LVBus0909999_production, 11_LVBus0910001_production, 11_LVBus0910002_production, 11_LVBus0910003_production, 11_LVBus0910005_production, 11_LVBus0910006_production, 11_LVBus0910007_production, 11_LVBus0910008_production, 11_LVBus0910009_production, 11_LVBus0910010_production, 11_LVBus0910011_production, 11_LVBus0910013_production, 11_LVBus0910014_consumption, 11_LVBus0910014_production, 11_LVBus0910015_consumption, 11_LVBus0910015_production, 11_LVBus0910016_production, 11_LVBus0910017_production, 11_LVBus0910018_production, 11_LVBus0910019_production, 11_LVBus0910020_production, 11_LVBus0910021_production, 11_LVBus0910022_production, 11_LVBus0910023_production, 11_LVBus0910025_production, 11_LVBus0910026_production, 11_LVBus0910028_consumption, 11_LVBus0910028_production, 11_LVBus0910029_production, 11_LVBus0910030_production, 11_LVBus0910031_production, 11_LVBus0910032_production, 11_LVBus0910034_production, 11_LVBus0910036_consumption, 11_LVBus0910036_production, 11_LVBus0910038_production, 11_LVBus0910039_production, 11_LVBus0910040_production, 11_LVBus0910041_production, 11_LVBus0910043_production, 11_LVBus0910045_consumption, 11_LVBus0910045_production, 11_LVBus0910047_production, 11_LVBus0910049_production, 11_LVBus0910051_production, 11_LVBus0910052_production, 11_LVBus0910053_consumption, 11_LVBus0910053_production, 11_LVBus0910055_production, 11_LVBus0910056_consumption, 11_LVBus0910056_production, 11_LVBus0910057_production, 11_LVBus0910059_production, 11_LVBus0910061_consumption, 11_LVBus0910061_production, 11_LVBus0910062_consumption, 11_LVBus0910062_production, 11_LVBus0910063_consumption, 11_LVBus0910063_production, 11_LVBus0910064_production, 11_LVBus0910065_production, 11_LVBus0910066_production, 11_LVBus0910068_production, 11_LVBus0910069_production, 11_LVBus0910070_production, 11_LVBus0910071_production, 11_LVBus0910073_production, 11_LVBus0910074_production, 11_LVBus0910076_production, 11_LVBus0910077_production, 11_LVBus0910078_consumption, 11_LVBus0910078_production, 11_LVBus0910080_production, 11_LVBus0910081_production, 11_LVBus0910083_production, 11_LVBus0910085_production, 11_LVBus0910086_consumption, 11_LVBus0910086_production, 11_LVBus0910087_consumption, 11_LVBus0910087_production, 11_LVBus0910089_consumption, 11_LVBus0910089_production, 11_LVBus0910090_production, 11_LVBus0910092_production, 11_LVBus1284669_consumption, 11_LVBus1284669_production, 11_LVBus1284670_consumption, 11_LVBus1284670_production, 11_LVBus1288941_consumption, 11_LVBus1288941_production, 11_LVBus1288942_production, 11_LVBus1290184_consumption, 11_LVBus1290184_production, 11_LVBus1290185_production, 11_LVBus1290186_consumption, 11_LVBus1290186_production, 11_LVBus1294818_consumption, 11_LVBus1294818_production, 11_LVBus1296094_production, 11_LVBus1296095_production, 11_LVBus1296535_production, 11_LVBus1296536_production, 11_LVBus1296537_production, 11_LVBus1301000_production, 11_LVBus1301001_production, 11_LVBus1301002_production, 11_LVBus1301047_consumption, 11_LVBus1301047_production, 11_LVBus1301048_production, 11_LVBus1301049_production, 11_LVBus1301050_production, 11_LVBus1303765_production, 11_LVBus1303766_production, 11_LVBus1304920_production, 11_LVBus1308096_production, 11_LVBus1308097_production, 11_LVBus1308159_production, 11_LVBus1308160_production, 11_LVBus1308682_consumption, 11_LVBus1308682_production, 11_LVBus1308683_production, 11_LVBus1308684_production, 11_LVBus1308685_consumption, 11_LVBus1308685_production, 11_LVBus1308686_production, 11_LVBus1308687_production, 11_LVBus1308688_production, 11_LVBus1308689_consumption, 11_LVBus1308689_production, 11_LVBus1308690_production, 11_LVBus1309230_production, 11_LVBus1309231_production, 11_LVBus1309232_production, 11_LVBus1309233_production, 11_LVBus1312384_production, 11_LVBus1312385_production, 11_LVBus1316704_production, 11_LVBus1318107_production, 11_LVBus1321499_production, 11_LVBus1321500_production, 11_LVBus1321501_production, 11_LVBus1321502_consumption, 11_LVBus1321502_production, 11_LVBus1321503_production, 11_LVBus1321504_production, 11_LVBus1321505_production, 11_LVBus1321506_production, 11_LVBus1321507_production, 11_LVBus1321508_production, 11_LVBus1321509_production, 11_LVBus1321510_production, 11_LVBus1325554_production, 11_LVBus1325555_production, 11_LVBus1326077_production, 11_LVBus1326078_consumption, 11_LVBus1326078_production, 11_LVBus1326079_production, 11_LVBus1332608_production, 11_LVBus1332609_production, 11_LVBus1336436_production, 11_LVBus1336437_production, 11_LVBus1338984_consumption, 11_LVBus1338984_production, 11_LVBus1338985_consumption, 11_LVBus1338985_production, 11_LVBus1342255_production, 11_LVBus1347774_production, 11_LVBus1347775_production, 11_LVBus1347776_production, 11_LVBus1347777_production, 11_MVLV03967_production, 11_MVLV04460_consumption, 11_MVLV04460_production, 11_MVLV18993_consumption, 11_MVLV18993_production, 11_MVLV32444_production, 11_MVLV42429_consumption, 11_MVLV42429_production, 11_MVLV45743_consumption, 11_MVLV45743_production, 11_MVLV47113_production, 11_MVLV63172_production, 11_MVLV74366_consumption, 11_MVLV74366_production.

