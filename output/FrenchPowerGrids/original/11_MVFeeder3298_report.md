# BMOPF Network Summary: 11_MVFeeder3298

**Generated:** 2026-10-01 23:33:56  
**Findings:** 0 errors · 5 warnings · 288 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 29 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 432 |  |
| line | 402 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 738 | 5.063 MW, 1.52 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 29 |  |
| switch | 0 |  |
| transformer | 29 | Dyn11×29 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 40 | 39 | 12 | 0 |
| LV_236V | 236.0 V | 392 | 363 | 726 | 0 |

**Transformer transitions:**

- `11_MVLV64969_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV35108_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV04454_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV50966_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV37038_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV50945_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV35114_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV35083_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV47772_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV23745_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV45768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV35105_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV48373_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV64987_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV38789_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV21287_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV20989_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV16017_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV23956_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV47718_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV16039_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV74193_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV64952_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV51159_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV18488_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV18535_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV64971_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV37066_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV64948_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 11 |
| Degree-1 buses | 232 |
| Tree depth (max hops) | 31 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 432 | 1 | 431 | 0 | 0 | 0 |
| Tier LV_236V | 392 | 29 | 363 | 0 | 0 | 0 |
| Tier MV_11.8kV | 40 | 1 | 39 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 29; skipped invalid branches: 0.

Galvanic zones: 30; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_MVBus57414 | MV_11.8kV | 40 | 0 | 0 | 29 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1688 declared bus terminals; 1569 mapped line/closed-switch conductor edges; 119 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 59900.0 | 2.37 | 2214 |
| q_nom | 0.0 | 18000.0 | 2.37 | 2214 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.71 | 3630.0 | 2.185 | 402 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.519 | 29 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 433 of 738 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964168_consumption' has phase imbalance of 131.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964050_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963718_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964130_consumption' has phase imbalance of 98.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963984_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963750_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964032_consumption' has phase imbalance of 73.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963694_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963747_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964038_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963774_consumption' has phase imbalance of 132.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964156_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963976_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964131_consumption' has phase imbalance of 119.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963709_consumption' has phase imbalance of 116.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963711_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964183_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964016_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964009_consumption' has phase imbalance of 28.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964134_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963931_consumption' has phase imbalance of 105.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1363873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964170_consumption' has phase imbalance of 281.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963970_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963899_consumption' has phase imbalance of 90.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964169_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963740_consumption' has phase imbalance of 47.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963802_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370729_consumption' has phase imbalance of 50.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963921_consumption' has phase imbalance of 33.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963869_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963945_consumption' has phase imbalance of 72.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963751_consumption' has phase imbalance of 166.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963975_consumption' has phase imbalance of 228.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963702_consumption' has phase imbalance of 145.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964135_consumption' has phase imbalance of 71.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963858_consumption' has phase imbalance of 100.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963961_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963723_consumption' has phase imbalance of 258.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963986_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963985_consumption' has phase imbalance of 26.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963909_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963911_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964137_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964155_consumption' has phase imbalance of 84.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964115_consumption' has phase imbalance of 110.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963874_consumption' has phase imbalance of 23.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963919_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964007_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963865_consumption' has phase imbalance of 180.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963809_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963843_consumption' has phase imbalance of 92.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964177_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963724_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963735_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963828_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964139_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964018_consumption' has phase imbalance of 59.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963883_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963965_consumption' has phase imbalance of 53.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964125_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963846_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963749_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963897_consumption' has phase imbalance of 64.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963958_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964035_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964073_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964165_consumption' has phase imbalance of 234.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964095_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964097_consumption' has phase imbalance of 58.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964164_consumption' has phase imbalance of 39.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963852_consumption' has phase imbalance of 264.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963960_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963898_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964149_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963973_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964094_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964045_consumption' has phase imbalance of 183.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964127_consumption' has phase imbalance of 46.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963892_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963927_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963720_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964078_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963974_consumption' has phase imbalance of 37.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964033_consumption' has phase imbalance of 113.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964041_consumption' has phase imbalance of 145.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964092_consumption' has phase imbalance of 131.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963887_consumption' has phase imbalance of 273.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963982_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964184_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963888_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964039_consumption' has phase imbalance of 55.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963822_consumption' has phase imbalance of 220.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963739_consumption' has phase imbalance of 265.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964002_consumption' has phase imbalance of 84.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964054_consumption' has phase imbalance of 75.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963725_consumption' has phase imbalance of 68.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963978_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964019_consumption' has phase imbalance of 24.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1363878_consumption' has phase imbalance of 47.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963772_consumption' has phase imbalance of 78.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963695_consumption' has phase imbalance of 103.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964152_consumption' has phase imbalance of 30.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964147_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963769_consumption' has phase imbalance of 125.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964001_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963845_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964043_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963755_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963889_consumption' has phase imbalance of 241.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963840_consumption' has phase imbalance of 124.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963851_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964141_consumption' has phase imbalance of 56.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963744_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963940_consumption' has phase imbalance of 68.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963867_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963727_consumption' has phase imbalance of 89.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964158_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964179_consumption' has phase imbalance of 65.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964173_consumption' has phase imbalance of 169.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963859_consumption' has phase imbalance of 36.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964180_consumption' has phase imbalance of 84.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963882_consumption' has phase imbalance of 90.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964153_consumption' has phase imbalance of 46.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963903_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963736_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963781_consumption' has phase imbalance of 88.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963814_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963743_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963818_consumption' has phase imbalance of 54.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963866_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963907_consumption' has phase imbalance of 52.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963894_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964175_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964129_consumption' has phase imbalance of 114.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963957_consumption' has phase imbalance of 232.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963763_consumption' has phase imbalance of 53.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964178_consumption' has phase imbalance of 30.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963876_consumption' has phase imbalance of 27.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963762_consumption' has phase imbalance of 102.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963924_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964166_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963726_consumption' has phase imbalance of 47.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963933_consumption' has phase imbalance of 72.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963904_consumption' has phase imbalance of 167.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963900_consumption' has phase imbalance of 228.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963761_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963979_consumption' has phase imbalance of 231.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964111_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964126_consumption' has phase imbalance of 202.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964098_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963833_consumption' has phase imbalance of 119.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964048_consumption' has phase imbalance of 176.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964116_consumption' has phase imbalance of 144.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964036_consumption' has phase imbalance of 205.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964103_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963947_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964089_consumption' has phase imbalance of 93.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963790_consumption' has phase imbalance of 28.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963905_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963916_consumption' has phase imbalance of 96.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1365471_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370731_consumption' has phase imbalance of 214.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963929_consumption' has phase imbalance of 128.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964087_consumption' has phase imbalance of 36.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963881_consumption' has phase imbalance of 147.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964066_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963835_consumption' has phase imbalance of 45.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963879_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964023_consumption' has phase imbalance of 27.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963918_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963799_consumption' has phase imbalance of 69.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963759_consumption' has phase imbalance of 206.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963855_consumption' has phase imbalance of 41.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963841_consumption' has phase imbalance of 71.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963854_consumption' has phase imbalance of 57.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964079_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963837_consumption' has phase imbalance of 60.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964101_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963699_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963753_consumption' has phase imbalance of 187.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964030_consumption' has phase imbalance of 81.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963956_consumption' has phase imbalance of 107.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1363881_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963856_consumption' has phase imbalance of 116.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964171_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964145_consumption' has phase imbalance of 120.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964027_consumption' has phase imbalance of 68.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963830_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963719_consumption' has phase imbalance of 55.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963808_consumption' has phase imbalance of 78.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1363880_consumption' has phase imbalance of 283.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963994_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963962_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964142_consumption' has phase imbalance of 54.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963896_consumption' has phase imbalance of 124.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963972_consumption' has phase imbalance of 230.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963797_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963942_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964075_consumption' has phase imbalance of 250.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963935_consumption' has phase imbalance of 27.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963902_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963698_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963925_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963934_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963847_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964040_consumption' has phase imbalance of 131.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963731_consumption' has phase imbalance of 123.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963992_consumption' has phase imbalance of 36.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964109_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963779_consumption' has phase imbalance of 125.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963767_consumption' has phase imbalance of 32.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964029_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963738_consumption' has phase imbalance of 188.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963980_consumption' has phase imbalance of 223.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964123_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964084_consumption' has phase imbalance of 27.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963712_consumption' has phase imbalance of 59.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963890_consumption' has phase imbalance of 85.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963990_consumption' has phase imbalance of 43.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964100_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963773_consumption' has phase imbalance of 35.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964077_consumption' has phase imbalance of 184.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963697_consumption' has phase imbalance of 207.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964133_consumption' has phase imbalance of 83.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963722_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0964162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0963953_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 738 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0964056' has balanced aggregate load across 3 phase(s) (max spread 0.84%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_NOURO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0963785' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0963861' has balanced aggregate load across 3 phase(s) (max spread 1.94%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus0963691' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 5.063 MW |
| Total load Q | 1.52 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV64969_Transformer | 176.0 kVA | 83.2% |
| 11_MVLV35108_Transformer | 346.5 kVA | 86.7% |
| 11_MVLV04454_Transformer | 110.0 kVA | 11.2% |
| 11_MVLV50966_Transformer | 440.0 kVA | 63.7% |
| 11_MVLV37038_Transformer | 110.0 kVA | 26.8% |
| 11_MVLV50945_Transformer | 275.0 kVA | 43.9% |
| 11_MVLV35114_Transformer | 440.0 kVA | 37.7% |
| 11_MVLV35083_Transformer | 440.0 kVA | 60.9% |
| 11_MVLV47772_Transformer | 176.0 kVA | 54.1% |
| 11_MVLV23745_Transformer | 110.0 kVA | 8.0% |
| 11_MVLV45768_Transformer | 275.0 kVA | 26.4% |
| 11_MVLV35105_Transformer | 440.0 kVA | 53.6% |
| 11_MVLV48373_Transformer | 176.0 kVA | 25.7% |
| 11_MVLV64987_Transformer | 550.0 kVA | 85.1% |
| 11_MVLV38789_Transformer | 440.0 kVA | 82.1% |
| 11_MVLV21287_Transformer | 440.0 kVA | 52.1% |
| 11_MVLV20989_Transformer | 110.0 kVA | 8.2% |
| 11_MVLV16017_Transformer | 275.0 kVA | 67.7% |
| 11_MVLV23956_Transformer | 176.0 kVA | 62.2% |
| 11_MVLV47718_Transformer | 440.0 kVA | 41.9% |
| 11_MVLV16039_Transformer | 110.0 kVA | 41.6% |
| 11_MVLV74193_Transformer | 176.0 kVA | 79.4% |
| 11_MVLV64952_Transformer | 275.0 kVA | 85.9% |
| 11_MVLV51159_Transformer | 440.0 kVA | 56.0% |
| 11_MVLV18488_Transformer | 440.0 kVA | 84.7% |
| 11_MVLV18535_Transformer | 693.0 kVA | 46.1% |
| 11_MVLV64971_Transformer | 440.0 kVA | 56.6% |
| 11_MVLV37066_Transformer | 176.0 kVA | 59.7% |
| 11_MVLV64948_Transformer | 176.0 kVA | 46.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.06 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '11_LVBus0963820' (LV, 0.24 kV) has an electrical reach of 10.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 432 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 432 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 29 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 40 |
| LV_236V | 4-wire | 392 / 392 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 392 |
| Neutral branches | 363 |
| Grounding points | 29 |
| Neutral sections | 29 |
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
| 11.78 kV | 40 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 30 |
| Islands without voltage reference | 0 |
| Line impedance spread | 900.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 392 / 40 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 434 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 434 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0963691_consumption, 11_LVBus0963691_production, 11_LVBus0963694_production, 11_LVBus0963695_production, 11_LVBus0963696_production, 11_LVBus0963697_production, 11_LVBus0963698_production, 11_LVBus0963699_production, 11_LVBus0963701_production, 11_LVBus0963702_production, 11_LVBus0963703_consumption, 11_LVBus0963703_production, 11_LVBus0963704_production, 11_LVBus0963705_production, 11_LVBus0963707_production, 11_LVBus0963708_production, 11_LVBus0963709_production, 11_LVBus0963710_production, 11_LVBus0963711_production, 11_LVBus0963712_production, 11_LVBus0963713_production, 11_LVBus0963715_consumption, 11_LVBus0963715_production, 11_LVBus0963716_consumption, 11_LVBus0963716_production, 11_LVBus0963717_consumption, 11_LVBus0963717_production, 11_LVBus0963718_production, 11_LVBus0963719_production, 11_LVBus0963720_production, 11_LVBus0963721_consumption, 11_LVBus0963721_production, 11_LVBus0963722_production, 11_LVBus0963723_production, 11_LVBus0963724_production, 11_LVBus0963725_production, 11_LVBus0963726_production, 11_LVBus0963727_production, 11_LVBus0963731_production, 11_LVBus0963733_production, 11_LVBus0963735_production, 11_LVBus0963736_production, 11_LVBus0963737_production, 11_LVBus0963738_production, 11_LVBus0963739_production, 11_LVBus0963740_production, 11_LVBus0963742_production, 11_LVBus0963743_production, 11_LVBus0963744_production, 11_LVBus0963745_production, 11_LVBus0963747_production, 11_LVBus0963748_consumption, 11_LVBus0963748_production, 11_LVBus0963749_production, 11_LVBus0963750_production, 11_LVBus0963751_production, 11_LVBus0963752_production, 11_LVBus0963753_production, 11_LVBus0963754_production, 11_LVBus0963755_production, 11_LVBus0963757_production, 11_LVBus0963759_production, 11_LVBus0963761_production, 11_LVBus0963762_production, 11_LVBus0963763_production, 11_LVBus0963765_production, 11_LVBus0963767_production, 11_LVBus0963769_production, 11_LVBus0963771_production, 11_LVBus0963772_production, 11_LVBus0963773_production, 11_LVBus0963774_production, 11_LVBus0963775_production, 11_LVBus0963776_production, 11_LVBus0963777_production, 11_LVBus0963778_production, 11_LVBus0963779_production, 11_LVBus0963781_production, 11_LVBus0963783_consumption, 11_LVBus0963783_production, 11_LVBus0963785_production, 11_LVBus0963786_production, 11_LVBus0963788_consumption, 11_LVBus0963788_production, 11_LVBus0963790_production, 11_LVBus0963792_consumption, 11_LVBus0963792_production, 11_LVBus0963793_production, 11_LVBus0963795_consumption, 11_LVBus0963795_production, 11_LVBus0963797_production, 11_LVBus0963798_production, 11_LVBus0963799_production, 11_LVBus0963801_production, 11_LVBus0963802_production, 11_LVBus0963803_consumption, 11_LVBus0963803_production, 11_LVBus0963805_production, 11_LVBus0963806_production, 11_LVBus0963807_production, 11_LVBus0963808_production, 11_LVBus0963809_production, 11_LVBus0963811_consumption, 11_LVBus0963811_production, 11_LVBus0963812_production, 11_LVBus0963814_production, 11_LVBus0963816_consumption, 11_LVBus0963816_production, 11_LVBus0963818_production, 11_LVBus0963820_consumption, 11_LVBus0963820_production, 11_LVBus0963822_production, 11_LVBus0963824_consumption, 11_LVBus0963824_production, 11_LVBus0963826_production, 11_LVBus0963828_production, 11_LVBus0963830_production, 11_LVBus0963831_consumption, 11_LVBus0963831_production, 11_LVBus0963833_production, 11_LVBus0963835_production, 11_LVBus0963837_production, 11_LVBus0963839_consumption, 11_LVBus0963839_production, 11_LVBus0963840_production, 11_LVBus0963841_production, 11_LVBus0963843_production, 11_LVBus0963845_production, 11_LVBus0963846_production, 11_LVBus0963847_production, 11_LVBus0963848_production, 11_LVBus0963850_production, 11_LVBus0963851_production, 11_LVBus0963852_production, 11_LVBus0963854_production, 11_LVBus0963855_production, 11_LVBus0963856_production, 11_LVBus0963858_production, 11_LVBus0963859_production, 11_LVBus0963861_production, 11_LVBus0963863_consumption, 11_LVBus0963863_production, 11_LVBus0963865_production, 11_LVBus0963866_production, 11_LVBus0963867_production, 11_LVBus0963869_production, 11_LVBus0963870_consumption, 11_LVBus0963870_production, 11_LVBus0963871_production, 11_LVBus0963872_consumption, 11_LVBus0963872_production, 11_LVBus0963874_production, 11_LVBus0963875_production, 11_LVBus0963876_production, 11_LVBus0963879_production, 11_LVBus0963881_production, 11_LVBus0963882_production, 11_LVBus0963883_production, 11_LVBus0963885_production, 11_LVBus0963887_production, 11_LVBus0963888_production, 11_LVBus0963889_production, 11_LVBus0963890_production, 11_LVBus0963891_consumption, 11_LVBus0963891_production, 11_LVBus0963892_production, 11_LVBus0963894_production, 11_LVBus0963895_production, 11_LVBus0963896_production, 11_LVBus0963897_production, 11_LVBus0963898_production, 11_LVBus0963899_production, 11_LVBus0963900_production, 11_LVBus0963902_production, 11_LVBus0963903_production, 11_LVBus0963904_production, 11_LVBus0963905_production, 11_LVBus0963907_production, 11_LVBus0963909_production, 11_LVBus0963911_production, 11_LVBus0963913_consumption, 11_LVBus0963913_production, 11_LVBus0963914_consumption, 11_LVBus0963914_production, 11_LVBus0963915_production, 11_LVBus0963916_production, 11_LVBus0963917_consumption, 11_LVBus0963917_production, 11_LVBus0963918_production, 11_LVBus0963919_production, 11_LVBus0963921_production, 11_LVBus0963922_consumption, 11_LVBus0963922_production, 11_LVBus0963923_consumption, 11_LVBus0963923_production, 11_LVBus0963924_production, 11_LVBus0963925_production, 11_LVBus0963926_production, 11_LVBus0963927_production, 11_LVBus0963929_production, 11_LVBus0963930_production, 11_LVBus0963931_production, 11_LVBus0963933_production, 11_LVBus0963934_production, 11_LVBus0963935_production, 11_LVBus0963936_consumption, 11_LVBus0963936_production, 11_LVBus0963938_consumption, 11_LVBus0963938_production, 11_LVBus0963940_production, 11_LVBus0963942_production, 11_LVBus0963943_production, 11_LVBus0963945_production, 11_LVBus0963947_production, 11_LVBus0963949_consumption, 11_LVBus0963949_production, 11_LVBus0963951_production, 11_LVBus0963953_production, 11_LVBus0963954_production, 11_LVBus0963956_production, 11_LVBus0963957_production, 11_LVBus0963958_production, 11_LVBus0963960_production, 11_LVBus0963961_production, 11_LVBus0963962_production, 11_LVBus0963964_consumption, 11_LVBus0963964_production, 11_LVBus0963965_production, 11_LVBus0963966_production, 11_LVBus0963968_production, 11_LVBus0963969_production, 11_LVBus0963970_production, 11_LVBus0963972_production, 11_LVBus0963973_production, 11_LVBus0963974_production, 11_LVBus0963975_production, 11_LVBus0963976_production, 11_LVBus0963978_production, 11_LVBus0963979_production, 11_LVBus0963980_production, 11_LVBus0963982_production, 11_LVBus0963984_production, 11_LVBus0963985_production, 11_LVBus0963986_production, 11_LVBus0963988_production, 11_LVBus0963989_consumption, 11_LVBus0963989_production, 11_LVBus0963990_production, 11_LVBus0963992_production, 11_LVBus0963994_production, 11_LVBus0963996_production, 11_LVBus0963999_production, 11_LVBus0964001_production, 11_LVBus0964002_production, 11_LVBus0964003_consumption, 11_LVBus0964003_production, 11_LVBus0964005_consumption, 11_LVBus0964005_production, 11_LVBus0964007_production, 11_LVBus0964009_production, 11_LVBus0964011_consumption, 11_LVBus0964011_production, 11_LVBus0964013_consumption, 11_LVBus0964013_production, 11_LVBus0964014_production, 11_LVBus0964016_production, 11_LVBus0964017_production, 11_LVBus0964018_production, 11_LVBus0964019_production, 11_LVBus0964021_production, 11_LVBus0964023_production, 11_LVBus0964025_consumption, 11_LVBus0964025_production, 11_LVBus0964027_production, 11_LVBus0964029_production, 11_LVBus0964030_production, 11_LVBus0964032_production, 11_LVBus0964033_production, 11_LVBus0964035_production, 11_LVBus0964036_production, 11_LVBus0964038_production, 11_LVBus0964039_production, 11_LVBus0964040_production, 11_LVBus0964041_production, 11_LVBus0964042_production, 11_LVBus0964043_production, 11_LVBus0964045_production, 11_LVBus0964047_production, 11_LVBus0964048_production, 11_LVBus0964050_production, 11_LVBus0964052_consumption, 11_LVBus0964052_production, 11_LVBus0964053_consumption, 11_LVBus0964053_production, 11_LVBus0964054_production, 11_LVBus0964056_production, 11_LVBus0964058_production, 11_LVBus0964060_production, 11_LVBus0964062_production, 11_LVBus0964064_production, 11_LVBus0964066_production, 11_LVBus0964067_production, 11_LVBus0964069_consumption, 11_LVBus0964069_production, 11_LVBus0964071_production, 11_LVBus0964073_production, 11_LVBus0964075_production, 11_LVBus0964077_production, 11_LVBus0964078_production, 11_LVBus0964079_production, 11_LVBus0964081_consumption, 11_LVBus0964081_production, 11_LVBus0964084_production, 11_LVBus0964086_production, 11_LVBus0964087_production, 11_LVBus0964089_production, 11_LVBus0964091_production, 11_LVBus0964092_production, 11_LVBus0964094_production, 11_LVBus0964095_production, 11_LVBus0964097_production, 11_LVBus0964098_production, 11_LVBus0964100_production, 11_LVBus0964101_production, 11_LVBus0964103_production, 11_LVBus0964104_production, 11_LVBus0964106_consumption, 11_LVBus0964106_production, 11_LVBus0964108_consumption, 11_LVBus0964108_production, 11_LVBus0964109_production, 11_LVBus0964111_production, 11_LVBus0964113_consumption, 11_LVBus0964113_production, 11_LVBus0964115_production, 11_LVBus0964116_production, 11_LVBus0964117_production, 11_LVBus0964119_production, 11_LVBus0964121_production, 11_LVBus0964123_production, 11_LVBus0964125_production, 11_LVBus0964126_production, 11_LVBus0964127_production, 11_LVBus0964129_production, 11_LVBus0964130_production, 11_LVBus0964131_production, 11_LVBus0964133_production, 11_LVBus0964134_production, 11_LVBus0964135_production, 11_LVBus0964137_production, 11_LVBus0964138_consumption, 11_LVBus0964138_production, 11_LVBus0964139_production, 11_LVBus0964141_production, 11_LVBus0964142_production, 11_LVBus0964143_production, 11_LVBus0964145_production, 11_LVBus0964147_production, 11_LVBus0964149_production, 11_LVBus0964151_consumption, 11_LVBus0964151_production, 11_LVBus0964152_production, 11_LVBus0964153_production, 11_LVBus0964155_production, 11_LVBus0964156_production, 11_LVBus0964158_production, 11_LVBus0964160_consumption, 11_LVBus0964160_production, 11_LVBus0964161_production, 11_LVBus0964162_production, 11_LVBus0964163_production, 11_LVBus0964164_production, 11_LVBus0964165_production, 11_LVBus0964166_production, 11_LVBus0964167_consumption, 11_LVBus0964167_production, 11_LVBus0964168_production, 11_LVBus0964169_production, 11_LVBus0964170_production, 11_LVBus0964171_production, 11_LVBus0964172_consumption, 11_LVBus0964172_production, 11_LVBus0964173_production, 11_LVBus0964175_production, 11_LVBus0964177_production, 11_LVBus0964178_production, 11_LVBus0964179_production, 11_LVBus0964180_production, 11_LVBus0964182_consumption, 11_LVBus0964182_production, 11_LVBus0964183_production, 11_LVBus0964184_production, 11_LVBus0964185_consumption, 11_LVBus0964185_production, 11_LVBus0964186_consumption, 11_LVBus0964186_production, 11_LVBus1281429_production, 11_LVBus1299998_production, 11_LVBus1300037_consumption, 11_LVBus1300037_production, 11_LVBus1330040_consumption, 11_LVBus1330040_production, 11_LVBus1330041_consumption, 11_LVBus1330041_production, 11_LVBus1363873_production, 11_LVBus1363874_consumption, 11_LVBus1363874_production, 11_LVBus1363875_consumption, 11_LVBus1363875_production, 11_LVBus1363876_consumption, 11_LVBus1363876_production, 11_LVBus1363877_production, 11_LVBus1363878_production, 11_LVBus1363879_consumption, 11_LVBus1363879_production, 11_LVBus1363880_production, 11_LVBus1363881_production, 11_LVBus1365471_production, 11_LVBus1370728_production, 11_LVBus1370729_production, 11_LVBus1370730_consumption, 11_LVBus1370730_production, 11_LVBus1370731_production, 11_MVLV24155_consumption, 11_MVLV24155_production, 11_MVLV39012_consumption, 11_MVLV39012_production, 11_MVLV45746_production, 11_MVLV56067_consumption, 11_MVLV56067_production, 11_MVLV73142_consumption, 11_MVLV73142_production, 11_MVLV74170_consumption, 11_MVLV74170_production.

## 9. Data Quality Summary

**Total findings:** 293 (0 errors, 5 warnings, 288 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  433 of 738 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.06 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  434 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964168_consumption`  
  Load '11_LVBus0964168_consumption' has phase imbalance of 131.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963778_consumption`  
  Load '11_LVBus0963778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964050_consumption`  
  Load '11_LVBus0964050_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963718_consumption`  
  Load '11_LVBus0963718_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964163_consumption`  
  Load '11_LVBus0964163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964130_consumption`  
  Load '11_LVBus0964130_consumption' has phase imbalance of 98.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963984_consumption`  
  Load '11_LVBus0963984_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963750_consumption`  
  Load '11_LVBus0963750_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964032_consumption`  
  Load '11_LVBus0964032_consumption' has phase imbalance of 73.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963694_consumption`  
  Load '11_LVBus0963694_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963747_consumption`  
  Load '11_LVBus0963747_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964038_consumption`  
  Load '11_LVBus0964038_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964143_consumption`  
  Load '11_LVBus0964143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963806_consumption`  
  Load '11_LVBus0963806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963915_consumption`  
  Load '11_LVBus0963915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963774_consumption`  
  Load '11_LVBus0963774_consumption' has phase imbalance of 132.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964156_consumption`  
  Load '11_LVBus0964156_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963976_consumption`  
  Load '11_LVBus0963976_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964131_consumption`  
  Load '11_LVBus0964131_consumption' has phase imbalance of 119.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963709_consumption`  
  Load '11_LVBus0963709_consumption' has phase imbalance of 116.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963711_consumption`  
  Load '11_LVBus0963711_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964183_consumption`  
  Load '11_LVBus0964183_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964016_consumption`  
  Load '11_LVBus0964016_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964009_consumption`  
  Load '11_LVBus0964009_consumption' has phase imbalance of 28.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964134_consumption`  
  Load '11_LVBus0964134_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963931_consumption`  
  Load '11_LVBus0963931_consumption' has phase imbalance of 105.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1363873_consumption`  
  Load '11_LVBus1363873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964170_consumption`  
  Load '11_LVBus0964170_consumption' has phase imbalance of 281.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963826_consumption`  
  Load '11_LVBus0963826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963970_consumption`  
  Load '11_LVBus0963970_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963899_consumption`  
  Load '11_LVBus0963899_consumption' has phase imbalance of 90.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964169_consumption`  
  Load '11_LVBus0964169_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963740_consumption`  
  Load '11_LVBus0963740_consumption' has phase imbalance of 47.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963802_consumption`  
  Load '11_LVBus0963802_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370729_consumption`  
  Load '11_LVBus1370729_consumption' has phase imbalance of 50.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963921_consumption`  
  Load '11_LVBus0963921_consumption' has phase imbalance of 33.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963869_consumption`  
  Load '11_LVBus0963869_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963945_consumption`  
  Load '11_LVBus0963945_consumption' has phase imbalance of 72.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963751_consumption`  
  Load '11_LVBus0963751_consumption' has phase imbalance of 166.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963975_consumption`  
  Load '11_LVBus0963975_consumption' has phase imbalance of 228.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963702_consumption`  
  Load '11_LVBus0963702_consumption' has phase imbalance of 145.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963805_consumption`  
  Load '11_LVBus0963805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964104_consumption`  
  Load '11_LVBus0964104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964135_consumption`  
  Load '11_LVBus0964135_consumption' has phase imbalance of 71.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963858_consumption`  
  Load '11_LVBus0963858_consumption' has phase imbalance of 100.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963926_consumption`  
  Load '11_LVBus0963926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963710_consumption`  
  Load '11_LVBus0963710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963775_consumption`  
  Load '11_LVBus0963775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963961_consumption`  
  Load '11_LVBus0963961_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963723_consumption`  
  Load '11_LVBus0963723_consumption' has phase imbalance of 258.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963986_consumption`  
  Load '11_LVBus0963986_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963985_consumption`  
  Load '11_LVBus0963985_consumption' has phase imbalance of 26.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963909_consumption`  
  Load '11_LVBus0963909_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964021_consumption`  
  Load '11_LVBus0964021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963911_consumption`  
  Load '11_LVBus0963911_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963742_consumption`  
  Load '11_LVBus0963742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964137_consumption`  
  Load '11_LVBus0964137_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964155_consumption`  
  Load '11_LVBus0964155_consumption' has phase imbalance of 84.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964115_consumption`  
  Load '11_LVBus0964115_consumption' has phase imbalance of 110.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963874_consumption`  
  Load '11_LVBus0963874_consumption' has phase imbalance of 23.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963919_consumption`  
  Load '11_LVBus0963919_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964007_consumption`  
  Load '11_LVBus0964007_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963865_consumption`  
  Load '11_LVBus0963865_consumption' has phase imbalance of 180.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963809_consumption`  
  Load '11_LVBus0963809_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963843_consumption`  
  Load '11_LVBus0963843_consumption' has phase imbalance of 92.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964177_consumption`  
  Load '11_LVBus0964177_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963724_consumption`  
  Load '11_LVBus0963724_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963735_consumption`  
  Load '11_LVBus0963735_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963828_consumption`  
  Load '11_LVBus0963828_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964139_consumption`  
  Load '11_LVBus0964139_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964018_consumption`  
  Load '11_LVBus0964018_consumption' has phase imbalance of 59.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963883_consumption`  
  Load '11_LVBus0963883_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963965_consumption`  
  Load '11_LVBus0963965_consumption' has phase imbalance of 53.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964125_consumption`  
  Load '11_LVBus0964125_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963846_consumption`  
  Load '11_LVBus0963846_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963749_consumption`  
  Load '11_LVBus0963749_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963897_consumption`  
  Load '11_LVBus0963897_consumption' has phase imbalance of 64.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963958_consumption`  
  Load '11_LVBus0963958_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964035_consumption`  
  Load '11_LVBus0964035_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964073_consumption`  
  Load '11_LVBus0964073_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964165_consumption`  
  Load '11_LVBus0964165_consumption' has phase imbalance of 234.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964095_consumption`  
  Load '11_LVBus0964095_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963969_consumption`  
  Load '11_LVBus0963969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963988_consumption`  
  Load '11_LVBus0963988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964097_consumption`  
  Load '11_LVBus0964097_consumption' has phase imbalance of 58.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964164_consumption`  
  Load '11_LVBus0964164_consumption' has phase imbalance of 39.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963852_consumption`  
  Load '11_LVBus0963852_consumption' has phase imbalance of 264.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963960_consumption`  
  Load '11_LVBus0963960_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963705_consumption`  
  Load '11_LVBus0963705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963713_consumption`  
  Load '11_LVBus0963713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963898_consumption`  
  Load '11_LVBus0963898_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963895_consumption`  
  Load '11_LVBus0963895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964149_consumption`  
  Load '11_LVBus0964149_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963973_consumption`  
  Load '11_LVBus0963973_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964094_consumption`  
  Load '11_LVBus0964094_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964045_consumption`  
  Load '11_LVBus0964045_consumption' has phase imbalance of 183.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964127_consumption`  
  Load '11_LVBus0964127_consumption' has phase imbalance of 46.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963771_consumption`  
  Load '11_LVBus0963771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963892_consumption`  
  Load '11_LVBus0963892_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963927_consumption`  
  Load '11_LVBus0963927_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964047_consumption`  
  Load '11_LVBus0964047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963707_consumption`  
  Load '11_LVBus0963707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963776_consumption`  
  Load '11_LVBus0963776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963720_consumption`  
  Load '11_LVBus0963720_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964078_consumption`  
  Load '11_LVBus0964078_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963974_consumption`  
  Load '11_LVBus0963974_consumption' has phase imbalance of 37.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964033_consumption`  
  Load '11_LVBus0964033_consumption' has phase imbalance of 113.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964041_consumption`  
  Load '11_LVBus0964041_consumption' has phase imbalance of 145.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963798_consumption`  
  Load '11_LVBus0963798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964092_consumption`  
  Load '11_LVBus0964092_consumption' has phase imbalance of 131.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963887_consumption`  
  Load '11_LVBus0963887_consumption' has phase imbalance of 273.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963982_consumption`  
  Load '11_LVBus0963982_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964184_consumption`  
  Load '11_LVBus0964184_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963888_consumption`  
  Load '11_LVBus0963888_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964039_consumption`  
  Load '11_LVBus0964039_consumption' has phase imbalance of 55.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963801_consumption`  
  Load '11_LVBus0963801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963822_consumption`  
  Load '11_LVBus0963822_consumption' has phase imbalance of 220.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963739_consumption`  
  Load '11_LVBus0963739_consumption' has phase imbalance of 265.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963754_consumption`  
  Load '11_LVBus0963754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964002_consumption`  
  Load '11_LVBus0964002_consumption' has phase imbalance of 84.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964054_consumption`  
  Load '11_LVBus0964054_consumption' has phase imbalance of 75.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963725_consumption`  
  Load '11_LVBus0963725_consumption' has phase imbalance of 68.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963696_consumption`  
  Load '11_LVBus0963696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963708_consumption`  
  Load '11_LVBus0963708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963978_consumption`  
  Load '11_LVBus0963978_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964019_consumption`  
  Load '11_LVBus0964019_consumption' has phase imbalance of 24.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1363878_consumption`  
  Load '11_LVBus1363878_consumption' has phase imbalance of 47.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963772_consumption`  
  Load '11_LVBus0963772_consumption' has phase imbalance of 78.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963695_consumption`  
  Load '11_LVBus0963695_consumption' has phase imbalance of 103.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964152_consumption`  
  Load '11_LVBus0964152_consumption' has phase imbalance of 30.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964147_consumption`  
  Load '11_LVBus0964147_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963769_consumption`  
  Load '11_LVBus0963769_consumption' has phase imbalance of 125.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964001_consumption`  
  Load '11_LVBus0964001_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963845_consumption`  
  Load '11_LVBus0963845_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963793_consumption`  
  Load '11_LVBus0963793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964043_consumption`  
  Load '11_LVBus0964043_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963755_consumption`  
  Load '11_LVBus0963755_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963889_consumption`  
  Load '11_LVBus0963889_consumption' has phase imbalance of 241.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963840_consumption`  
  Load '11_LVBus0963840_consumption' has phase imbalance of 124.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963851_consumption`  
  Load '11_LVBus0963851_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964141_consumption`  
  Load '11_LVBus0964141_consumption' has phase imbalance of 56.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964161_consumption`  
  Load '11_LVBus0964161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963744_consumption`  
  Load '11_LVBus0963744_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963940_consumption`  
  Load '11_LVBus0963940_consumption' has phase imbalance of 68.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963867_consumption`  
  Load '11_LVBus0963867_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963727_consumption`  
  Load '11_LVBus0963727_consumption' has phase imbalance of 89.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964158_consumption`  
  Load '11_LVBus0964158_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964179_consumption`  
  Load '11_LVBus0964179_consumption' has phase imbalance of 65.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964173_consumption`  
  Load '11_LVBus0964173_consumption' has phase imbalance of 169.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963859_consumption`  
  Load '11_LVBus0963859_consumption' has phase imbalance of 36.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964180_consumption`  
  Load '11_LVBus0964180_consumption' has phase imbalance of 84.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963882_consumption`  
  Load '11_LVBus0963882_consumption' has phase imbalance of 90.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964153_consumption`  
  Load '11_LVBus0964153_consumption' has phase imbalance of 46.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963903_consumption`  
  Load '11_LVBus0963903_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963736_consumption`  
  Load '11_LVBus0963736_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963781_consumption`  
  Load '11_LVBus0963781_consumption' has phase imbalance of 88.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963814_consumption`  
  Load '11_LVBus0963814_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963743_consumption`  
  Load '11_LVBus0963743_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963818_consumption`  
  Load '11_LVBus0963818_consumption' has phase imbalance of 54.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963866_consumption`  
  Load '11_LVBus0963866_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963907_consumption`  
  Load '11_LVBus0963907_consumption' has phase imbalance of 52.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963894_consumption`  
  Load '11_LVBus0963894_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964175_consumption`  
  Load '11_LVBus0964175_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964129_consumption`  
  Load '11_LVBus0964129_consumption' has phase imbalance of 114.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963957_consumption`  
  Load '11_LVBus0963957_consumption' has phase imbalance of 232.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370728_consumption`  
  Load '11_LVBus1370728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963763_consumption`  
  Load '11_LVBus0963763_consumption' has phase imbalance of 53.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964178_consumption`  
  Load '11_LVBus0964178_consumption' has phase imbalance of 30.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963745_consumption`  
  Load '11_LVBus0963745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963876_consumption`  
  Load '11_LVBus0963876_consumption' has phase imbalance of 27.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963762_consumption`  
  Load '11_LVBus0963762_consumption' has phase imbalance of 102.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963924_consumption`  
  Load '11_LVBus0963924_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964166_consumption`  
  Load '11_LVBus0964166_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963726_consumption`  
  Load '11_LVBus0963726_consumption' has phase imbalance of 47.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964017_consumption`  
  Load '11_LVBus0964017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963737_consumption`  
  Load '11_LVBus0963737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963933_consumption`  
  Load '11_LVBus0963933_consumption' has phase imbalance of 72.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963904_consumption`  
  Load '11_LVBus0963904_consumption' has phase imbalance of 167.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963900_consumption`  
  Load '11_LVBus0963900_consumption' has phase imbalance of 228.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963761_consumption`  
  Load '11_LVBus0963761_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963979_consumption`  
  Load '11_LVBus0963979_consumption' has phase imbalance of 231.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964111_consumption`  
  Load '11_LVBus0964111_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964126_consumption`  
  Load '11_LVBus0964126_consumption' has phase imbalance of 202.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964098_consumption`  
  Load '11_LVBus0964098_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963833_consumption`  
  Load '11_LVBus0963833_consumption' has phase imbalance of 119.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964048_consumption`  
  Load '11_LVBus0964048_consumption' has phase imbalance of 176.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964116_consumption`  
  Load '11_LVBus0964116_consumption' has phase imbalance of 144.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964036_consumption`  
  Load '11_LVBus0964036_consumption' has phase imbalance of 205.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964103_consumption`  
  Load '11_LVBus0964103_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963947_consumption`  
  Load '11_LVBus0963947_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964089_consumption`  
  Load '11_LVBus0964089_consumption' has phase imbalance of 93.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963790_consumption`  
  Load '11_LVBus0963790_consumption' has phase imbalance of 28.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963905_consumption`  
  Load '11_LVBus0963905_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963916_consumption`  
  Load '11_LVBus0963916_consumption' has phase imbalance of 96.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1365471_consumption`  
  Load '11_LVBus1365471_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370731_consumption`  
  Load '11_LVBus1370731_consumption' has phase imbalance of 214.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963929_consumption`  
  Load '11_LVBus0963929_consumption' has phase imbalance of 128.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964087_consumption`  
  Load '11_LVBus0964087_consumption' has phase imbalance of 36.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963881_consumption`  
  Load '11_LVBus0963881_consumption' has phase imbalance of 147.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964066_consumption`  
  Load '11_LVBus0964066_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963835_consumption`  
  Load '11_LVBus0963835_consumption' has phase imbalance of 45.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963879_consumption`  
  Load '11_LVBus0963879_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964023_consumption`  
  Load '11_LVBus0964023_consumption' has phase imbalance of 27.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963918_consumption`  
  Load '11_LVBus0963918_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963799_consumption`  
  Load '11_LVBus0963799_consumption' has phase imbalance of 69.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963759_consumption`  
  Load '11_LVBus0963759_consumption' has phase imbalance of 206.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963701_consumption`  
  Load '11_LVBus0963701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963855_consumption`  
  Load '11_LVBus0963855_consumption' has phase imbalance of 41.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963841_consumption`  
  Load '11_LVBus0963841_consumption' has phase imbalance of 71.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963854_consumption`  
  Load '11_LVBus0963854_consumption' has phase imbalance of 57.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964079_consumption`  
  Load '11_LVBus0964079_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963837_consumption`  
  Load '11_LVBus0963837_consumption' has phase imbalance of 60.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964101_consumption`  
  Load '11_LVBus0964101_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963699_consumption`  
  Load '11_LVBus0963699_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963753_consumption`  
  Load '11_LVBus0963753_consumption' has phase imbalance of 187.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964086_consumption`  
  Load '11_LVBus0964086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964030_consumption`  
  Load '11_LVBus0964030_consumption' has phase imbalance of 81.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963956_consumption`  
  Load '11_LVBus0963956_consumption' has phase imbalance of 107.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1363881_consumption`  
  Load '11_LVBus1363881_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963856_consumption`  
  Load '11_LVBus0963856_consumption' has phase imbalance of 116.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964171_consumption`  
  Load '11_LVBus0964171_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964145_consumption`  
  Load '11_LVBus0964145_consumption' has phase imbalance of 120.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964027_consumption`  
  Load '11_LVBus0964027_consumption' has phase imbalance of 68.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963830_consumption`  
  Load '11_LVBus0963830_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963719_consumption`  
  Load '11_LVBus0963719_consumption' has phase imbalance of 55.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963808_consumption`  
  Load '11_LVBus0963808_consumption' has phase imbalance of 78.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1363880_consumption`  
  Load '11_LVBus1363880_consumption' has phase imbalance of 283.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963994_consumption`  
  Load '11_LVBus0963994_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963962_consumption`  
  Load '11_LVBus0963962_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964142_consumption`  
  Load '11_LVBus0964142_consumption' has phase imbalance of 54.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963896_consumption`  
  Load '11_LVBus0963896_consumption' has phase imbalance of 124.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963972_consumption`  
  Load '11_LVBus0963972_consumption' has phase imbalance of 230.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963797_consumption`  
  Load '11_LVBus0963797_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963942_consumption`  
  Load '11_LVBus0963942_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964075_consumption`  
  Load '11_LVBus0964075_consumption' has phase imbalance of 250.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963935_consumption`  
  Load '11_LVBus0963935_consumption' has phase imbalance of 27.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963752_consumption`  
  Load '11_LVBus0963752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963902_consumption`  
  Load '11_LVBus0963902_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963698_consumption`  
  Load '11_LVBus0963698_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963925_consumption`  
  Load '11_LVBus0963925_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963934_consumption`  
  Load '11_LVBus0963934_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963847_consumption`  
  Load '11_LVBus0963847_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964040_consumption`  
  Load '11_LVBus0964040_consumption' has phase imbalance of 131.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963731_consumption`  
  Load '11_LVBus0963731_consumption' has phase imbalance of 123.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963992_consumption`  
  Load '11_LVBus0963992_consumption' has phase imbalance of 36.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964109_consumption`  
  Load '11_LVBus0964109_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963777_consumption`  
  Load '11_LVBus0963777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963779_consumption`  
  Load '11_LVBus0963779_consumption' has phase imbalance of 125.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963767_consumption`  
  Load '11_LVBus0963767_consumption' has phase imbalance of 32.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964029_consumption`  
  Load '11_LVBus0964029_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963738_consumption`  
  Load '11_LVBus0963738_consumption' has phase imbalance of 188.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963980_consumption`  
  Load '11_LVBus0963980_consumption' has phase imbalance of 223.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964123_consumption`  
  Load '11_LVBus0964123_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964084_consumption`  
  Load '11_LVBus0964084_consumption' has phase imbalance of 27.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963712_consumption`  
  Load '11_LVBus0963712_consumption' has phase imbalance of 59.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963875_consumption`  
  Load '11_LVBus0963875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963890_consumption`  
  Load '11_LVBus0963890_consumption' has phase imbalance of 85.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963990_consumption`  
  Load '11_LVBus0963990_consumption' has phase imbalance of 43.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964100_consumption`  
  Load '11_LVBus0964100_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963704_consumption`  
  Load '11_LVBus0963704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963773_consumption`  
  Load '11_LVBus0963773_consumption' has phase imbalance of 35.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964077_consumption`  
  Load '11_LVBus0964077_consumption' has phase imbalance of 184.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963697_consumption`  
  Load '11_LVBus0963697_consumption' has phase imbalance of 207.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964133_consumption`  
  Load '11_LVBus0964133_consumption' has phase imbalance of 83.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963722_consumption`  
  Load '11_LVBus0963722_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0964162_consumption`  
  Load '11_LVBus0964162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0963953_consumption`  
  Load '11_LVBus0963953_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 738 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0964056' has balanced aggregate load across 3 phase(s) (max spread 0.84%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_NOURO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0963785' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0963861' has balanced aggregate load across 3 phase(s) (max spread 1.94%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus0963691' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '11_LVBus0963820' (LV, 0.24 kV) has an electrical reach of 10.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  432 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  104 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus0963694_consumption, 11_LVBus0963696_consumption, 11_LVBus0963697_consumption, 11_LVBus0963701_consumption, 11_LVBus0963704_consumption, 11_LVBus0963705_consumption, 11_LVBus0963707_consumption, 11_LVBus0963708_consumption, 11_LVBus0963710_consumption, 11_LVBus0963713_consumption, 11_LVBus0963718_consumption, 11_LVBus0963722_consumption, 11_LVBus0963723_consumption, 11_LVBus0963724_consumption, 11_LVBus0963735_consumption, 11_LVBus0963737_consumption, 11_LVBus0963738_consumption, 11_LVBus0963739_consumption, 11_LVBus0963742_consumption, 11_LVBus0963745_consumption, 11_LVBus0963747_consumption, 11_LVBus0963749_consumption, 11_LVBus0963751_consumption, 11_LVBus0963752_consumption, 11_LVBus0963753_consumption, 11_LVBus0963754_consumption, 11_LVBus0963759_consumption, 11_LVBus0963771_consumption, 11_LVBus0963775_consumption, 11_LVBus0963776_consumption, 11_LVBus0963777_consumption, 11_LVBus0963778_consumption, 11_LVBus0963793_consumption, 11_LVBus0963797_consumption, 11_LVBus0963798_consumption, 11_LVBus0963801_consumption, 11_LVBus0963805_consumption, 11_LVBus0963806_consumption, 11_LVBus0963822_consumption, 11_LVBus0963826_consumption, 11_LVBus0963851_consumption, 11_LVBus0963852_consumption, 11_LVBus0963865_consumption, 11_LVBus0963866_consumption, 11_LVBus0963875_consumption, 11_LVBus0963879_consumption, 11_LVBus0963883_consumption, 11_LVBus0963887_consumption, 11_LVBus0963888_consumption, 11_LVBus0963889_consumption, 11_LVBus0963892_consumption, 11_LVBus0963894_consumption, 11_LVBus0963895_consumption, 11_LVBus0963898_consumption, 11_LVBus0963900_consumption, 11_LVBus0963902_consumption, 11_LVBus0963904_consumption, 11_LVBus0963915_consumption, 11_LVBus0963919_consumption, 11_LVBus0963926_consumption, 11_LVBus0963927_consumption, 11_LVBus0963934_consumption, 11_LVBus0963947_consumption, 11_LVBus0963957_consumption, 11_LVBus0963958_consumption, 11_LVBus0963961_consumption, 11_LVBus0963962_consumption, 11_LVBus0963969_consumption, 11_LVBus0963970_consumption, 11_LVBus0963972_consumption, 11_LVBus0963975_consumption, 11_LVBus0963976_consumption, 11_LVBus0963984_consumption, 11_LVBus0963988_consumption, 11_LVBus0964017_consumption, 11_LVBus0964021_consumption, 11_LVBus0964036_consumption, 11_LVBus0964045_consumption, 11_LVBus0964047_consumption, 11_LVBus0964050_consumption, 11_LVBus0964066_consumption, 11_LVBus0964075_consumption, 11_LVBus0964079_consumption, 11_LVBus0964086_consumption, 11_LVBus0964094_consumption, 11_LVBus0964098_consumption, 11_LVBus0964103_consumption, 11_LVBus0964104_consumption, 11_LVBus0964109_consumption, 11_LVBus0964126_consumption, 11_LVBus0964137_consumption, 11_LVBus0964143_consumption, 11_LVBus0964147_consumption, 11_LVBus0964161_consumption, 11_LVBus0964162_consumption, 11_LVBus0964163_consumption, 11_LVBus0964165_consumption, 11_LVBus0964170_consumption, 11_LVBus0964175_consumption, 11_LVBus1363873_consumption, 11_LVBus1363880_consumption, 11_LVBus1365471_consumption, 11_LVBus1370728_consumption, 11_LVBus1370731_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  369 group(s) of loads (738 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  2 group(s) of series lines (4 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  434 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0963691_consumption, 11_LVBus0963691_production, 11_LVBus0963694_production, 11_LVBus0963695_production, 11_LVBus0963696_production, 11_LVBus0963697_production, 11_LVBus0963698_production, 11_LVBus0963699_production, 11_LVBus0963701_production, 11_LVBus0963702_production, 11_LVBus0963703_consumption, 11_LVBus0963703_production, 11_LVBus0963704_production, 11_LVBus0963705_production, 11_LVBus0963707_production, 11_LVBus0963708_production, 11_LVBus0963709_production, 11_LVBus0963710_production, 11_LVBus0963711_production, 11_LVBus0963712_production, 11_LVBus0963713_production, 11_LVBus0963715_consumption, 11_LVBus0963715_production, 11_LVBus0963716_consumption, 11_LVBus0963716_production, 11_LVBus0963717_consumption, 11_LVBus0963717_production, 11_LVBus0963718_production, 11_LVBus0963719_production, 11_LVBus0963720_production, 11_LVBus0963721_consumption, 11_LVBus0963721_production, 11_LVBus0963722_production, 11_LVBus0963723_production, 11_LVBus0963724_production, 11_LVBus0963725_production, 11_LVBus0963726_production, 11_LVBus0963727_production, 11_LVBus0963731_production, 11_LVBus0963733_production, 11_LVBus0963735_production, 11_LVBus0963736_production, 11_LVBus0963737_production, 11_LVBus0963738_production, 11_LVBus0963739_production, 11_LVBus0963740_production, 11_LVBus0963742_production, 11_LVBus0963743_production, 11_LVBus0963744_production, 11_LVBus0963745_production, 11_LVBus0963747_production, 11_LVBus0963748_consumption, 11_LVBus0963748_production, 11_LVBus0963749_production, 11_LVBus0963750_production, 11_LVBus0963751_production, 11_LVBus0963752_production, 11_LVBus0963753_production, 11_LVBus0963754_production, 11_LVBus0963755_production, 11_LVBus0963757_production, 11_LVBus0963759_production, 11_LVBus0963761_production, 11_LVBus0963762_production, 11_LVBus0963763_production, 11_LVBus0963765_production, 11_LVBus0963767_production, 11_LVBus0963769_production, 11_LVBus0963771_production, 11_LVBus0963772_production, 11_LVBus0963773_production, 11_LVBus0963774_production, 11_LVBus0963775_production, 11_LVBus0963776_production, 11_LVBus0963777_production, 11_LVBus0963778_production, 11_LVBus0963779_production, 11_LVBus0963781_production, 11_LVBus0963783_consumption, 11_LVBus0963783_production, 11_LVBus0963785_production, 11_LVBus0963786_production, 11_LVBus0963788_consumption, 11_LVBus0963788_production, 11_LVBus0963790_production, 11_LVBus0963792_consumption, 11_LVBus0963792_production, 11_LVBus0963793_production, 11_LVBus0963795_consumption, 11_LVBus0963795_production, 11_LVBus0963797_production, 11_LVBus0963798_production, 11_LVBus0963799_production, 11_LVBus0963801_production, 11_LVBus0963802_production, 11_LVBus0963803_consumption, 11_LVBus0963803_production, 11_LVBus0963805_production, 11_LVBus0963806_production, 11_LVBus0963807_production, 11_LVBus0963808_production, 11_LVBus0963809_production, 11_LVBus0963811_consumption, 11_LVBus0963811_production, 11_LVBus0963812_production, 11_LVBus0963814_production, 11_LVBus0963816_consumption, 11_LVBus0963816_production, 11_LVBus0963818_production, 11_LVBus0963820_consumption, 11_LVBus0963820_production, 11_LVBus0963822_production, 11_LVBus0963824_consumption, 11_LVBus0963824_production, 11_LVBus0963826_production, 11_LVBus0963828_production, 11_LVBus0963830_production, 11_LVBus0963831_consumption, 11_LVBus0963831_production, 11_LVBus0963833_production, 11_LVBus0963835_production, 11_LVBus0963837_production, 11_LVBus0963839_consumption, 11_LVBus0963839_production, 11_LVBus0963840_production, 11_LVBus0963841_production, 11_LVBus0963843_production, 11_LVBus0963845_production, 11_LVBus0963846_production, 11_LVBus0963847_production, 11_LVBus0963848_production, 11_LVBus0963850_production, 11_LVBus0963851_production, 11_LVBus0963852_production, 11_LVBus0963854_production, 11_LVBus0963855_production, 11_LVBus0963856_production, 11_LVBus0963858_production, 11_LVBus0963859_production, 11_LVBus0963861_production, 11_LVBus0963863_consumption, 11_LVBus0963863_production, 11_LVBus0963865_production, 11_LVBus0963866_production, 11_LVBus0963867_production, 11_LVBus0963869_production, 11_LVBus0963870_consumption, 11_LVBus0963870_production, 11_LVBus0963871_production, 11_LVBus0963872_consumption, 11_LVBus0963872_production, 11_LVBus0963874_production, 11_LVBus0963875_production, 11_LVBus0963876_production, 11_LVBus0963879_production, 11_LVBus0963881_production, 11_LVBus0963882_production, 11_LVBus0963883_production, 11_LVBus0963885_production, 11_LVBus0963887_production, 11_LVBus0963888_production, 11_LVBus0963889_production, 11_LVBus0963890_production, 11_LVBus0963891_consumption, 11_LVBus0963891_production, 11_LVBus0963892_production, 11_LVBus0963894_production, 11_LVBus0963895_production, 11_LVBus0963896_production, 11_LVBus0963897_production, 11_LVBus0963898_production, 11_LVBus0963899_production, 11_LVBus0963900_production, 11_LVBus0963902_production, 11_LVBus0963903_production, 11_LVBus0963904_production, 11_LVBus0963905_production, 11_LVBus0963907_production, 11_LVBus0963909_production, 11_LVBus0963911_production, 11_LVBus0963913_consumption, 11_LVBus0963913_production, 11_LVBus0963914_consumption, 11_LVBus0963914_production, 11_LVBus0963915_production, 11_LVBus0963916_production, 11_LVBus0963917_consumption, 11_LVBus0963917_production, 11_LVBus0963918_production, 11_LVBus0963919_production, 11_LVBus0963921_production, 11_LVBus0963922_consumption, 11_LVBus0963922_production, 11_LVBus0963923_consumption, 11_LVBus0963923_production, 11_LVBus0963924_production, 11_LVBus0963925_production, 11_LVBus0963926_production, 11_LVBus0963927_production, 11_LVBus0963929_production, 11_LVBus0963930_production, 11_LVBus0963931_production, 11_LVBus0963933_production, 11_LVBus0963934_production, 11_LVBus0963935_production, 11_LVBus0963936_consumption, 11_LVBus0963936_production, 11_LVBus0963938_consumption, 11_LVBus0963938_production, 11_LVBus0963940_production, 11_LVBus0963942_production, 11_LVBus0963943_production, 11_LVBus0963945_production, 11_LVBus0963947_production, 11_LVBus0963949_consumption, 11_LVBus0963949_production, 11_LVBus0963951_production, 11_LVBus0963953_production, 11_LVBus0963954_production, 11_LVBus0963956_production, 11_LVBus0963957_production, 11_LVBus0963958_production, 11_LVBus0963960_production, 11_LVBus0963961_production, 11_LVBus0963962_production, 11_LVBus0963964_consumption, 11_LVBus0963964_production, 11_LVBus0963965_production, 11_LVBus0963966_production, 11_LVBus0963968_production, 11_LVBus0963969_production, 11_LVBus0963970_production, 11_LVBus0963972_production, 11_LVBus0963973_production, 11_LVBus0963974_production, 11_LVBus0963975_production, 11_LVBus0963976_production, 11_LVBus0963978_production, 11_LVBus0963979_production, 11_LVBus0963980_production, 11_LVBus0963982_production, 11_LVBus0963984_production, 11_LVBus0963985_production, 11_LVBus0963986_production, 11_LVBus0963988_production, 11_LVBus0963989_consumption, 11_LVBus0963989_production, 11_LVBus0963990_production, 11_LVBus0963992_production, 11_LVBus0963994_production, 11_LVBus0963996_production, 11_LVBus0963999_production, 11_LVBus0964001_production, 11_LVBus0964002_production, 11_LVBus0964003_consumption, 11_LVBus0964003_production, 11_LVBus0964005_consumption, 11_LVBus0964005_production, 11_LVBus0964007_production, 11_LVBus0964009_production, 11_LVBus0964011_consumption, 11_LVBus0964011_production, 11_LVBus0964013_consumption, 11_LVBus0964013_production, 11_LVBus0964014_production, 11_LVBus0964016_production, 11_LVBus0964017_production, 11_LVBus0964018_production, 11_LVBus0964019_production, 11_LVBus0964021_production, 11_LVBus0964023_production, 11_LVBus0964025_consumption, 11_LVBus0964025_production, 11_LVBus0964027_production, 11_LVBus0964029_production, 11_LVBus0964030_production, 11_LVBus0964032_production, 11_LVBus0964033_production, 11_LVBus0964035_production, 11_LVBus0964036_production, 11_LVBus0964038_production, 11_LVBus0964039_production, 11_LVBus0964040_production, 11_LVBus0964041_production, 11_LVBus0964042_production, 11_LVBus0964043_production, 11_LVBus0964045_production, 11_LVBus0964047_production, 11_LVBus0964048_production, 11_LVBus0964050_production, 11_LVBus0964052_consumption, 11_LVBus0964052_production, 11_LVBus0964053_consumption, 11_LVBus0964053_production, 11_LVBus0964054_production, 11_LVBus0964056_production, 11_LVBus0964058_production, 11_LVBus0964060_production, 11_LVBus0964062_production, 11_LVBus0964064_production, 11_LVBus0964066_production, 11_LVBus0964067_production, 11_LVBus0964069_consumption, 11_LVBus0964069_production, 11_LVBus0964071_production, 11_LVBus0964073_production, 11_LVBus0964075_production, 11_LVBus0964077_production, 11_LVBus0964078_production, 11_LVBus0964079_production, 11_LVBus0964081_consumption, 11_LVBus0964081_production, 11_LVBus0964084_production, 11_LVBus0964086_production, 11_LVBus0964087_production, 11_LVBus0964089_production, 11_LVBus0964091_production, 11_LVBus0964092_production, 11_LVBus0964094_production, 11_LVBus0964095_production, 11_LVBus0964097_production, 11_LVBus0964098_production, 11_LVBus0964100_production, 11_LVBus0964101_production, 11_LVBus0964103_production, 11_LVBus0964104_production, 11_LVBus0964106_consumption, 11_LVBus0964106_production, 11_LVBus0964108_consumption, 11_LVBus0964108_production, 11_LVBus0964109_production, 11_LVBus0964111_production, 11_LVBus0964113_consumption, 11_LVBus0964113_production, 11_LVBus0964115_production, 11_LVBus0964116_production, 11_LVBus0964117_production, 11_LVBus0964119_production, 11_LVBus0964121_production, 11_LVBus0964123_production, 11_LVBus0964125_production, 11_LVBus0964126_production, 11_LVBus0964127_production, 11_LVBus0964129_production, 11_LVBus0964130_production, 11_LVBus0964131_production, 11_LVBus0964133_production, 11_LVBus0964134_production, 11_LVBus0964135_production, 11_LVBus0964137_production, 11_LVBus0964138_consumption, 11_LVBus0964138_production, 11_LVBus0964139_production, 11_LVBus0964141_production, 11_LVBus0964142_production, 11_LVBus0964143_production, 11_LVBus0964145_production, 11_LVBus0964147_production, 11_LVBus0964149_production, 11_LVBus0964151_consumption, 11_LVBus0964151_production, 11_LVBus0964152_production, 11_LVBus0964153_production, 11_LVBus0964155_production, 11_LVBus0964156_production, 11_LVBus0964158_production, 11_LVBus0964160_consumption, 11_LVBus0964160_production, 11_LVBus0964161_production, 11_LVBus0964162_production, 11_LVBus0964163_production, 11_LVBus0964164_production, 11_LVBus0964165_production, 11_LVBus0964166_production, 11_LVBus0964167_consumption, 11_LVBus0964167_production, 11_LVBus0964168_production, 11_LVBus0964169_production, 11_LVBus0964170_production, 11_LVBus0964171_production, 11_LVBus0964172_consumption, 11_LVBus0964172_production, 11_LVBus0964173_production, 11_LVBus0964175_production, 11_LVBus0964177_production, 11_LVBus0964178_production, 11_LVBus0964179_production, 11_LVBus0964180_production, 11_LVBus0964182_consumption, 11_LVBus0964182_production, 11_LVBus0964183_production, 11_LVBus0964184_production, 11_LVBus0964185_consumption, 11_LVBus0964185_production, 11_LVBus0964186_consumption, 11_LVBus0964186_production, 11_LVBus1281429_production, 11_LVBus1299998_production, 11_LVBus1300037_consumption, 11_LVBus1300037_production, 11_LVBus1330040_consumption, 11_LVBus1330040_production, 11_LVBus1330041_consumption, 11_LVBus1330041_production, 11_LVBus1363873_production, 11_LVBus1363874_consumption, 11_LVBus1363874_production, 11_LVBus1363875_consumption, 11_LVBus1363875_production, 11_LVBus1363876_consumption, 11_LVBus1363876_production, 11_LVBus1363877_production, 11_LVBus1363878_production, 11_LVBus1363879_consumption, 11_LVBus1363879_production, 11_LVBus1363880_production, 11_LVBus1363881_production, 11_LVBus1365471_production, 11_LVBus1370728_production, 11_LVBus1370729_production, 11_LVBus1370730_consumption, 11_LVBus1370730_production, 11_LVBus1370731_production, 11_MVLV24155_consumption, 11_MVLV24155_production, 11_MVLV39012_consumption, 11_MVLV39012_production, 11_MVLV45746_production, 11_MVLV56067_consumption, 11_MVLV56067_production, 11_MVLV73142_consumption, 11_MVLV73142_production, 11_MVLV74170_consumption, 11_MVLV74170_production.

