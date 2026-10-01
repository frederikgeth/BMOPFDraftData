# BMOPF Network Summary: 52_MVFeeder0837

**Generated:** 2026-10-01 23:34:13  
**Findings:** 0 errors · 5 warnings · 324 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 54 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 649 |  |
| line | 594 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 958 | 1.595 MW, 478.4 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 54 |  |
| switch | 0 |  |
| transformer | 54 | Dyn11×54 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 127 | 126 | 22 | 0 |
| LV_236V | 236.0 V | 522 | 468 | 936 | 0 |

**Transformer transitions:**

- `52_MVLV039413_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV085012_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV088977_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV042715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV011684_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV007384_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV056877_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104513_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV003718_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV008610_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009858_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV077489_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV045131_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV006817_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV085960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV107089_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV055882_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV010193_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV100957_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV070738_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV097457_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV044764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV065068_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV107121_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV010021_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV038170_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV096930_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV035851_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV097455_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV088966_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV065370_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV034161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV079553_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV035469_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV048761_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV091563_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV015220_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV094126_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV062593_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV070951_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV093362_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV076960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV070729_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV088981_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV079536_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV036837_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV029495_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV030911_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV040481_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV107120_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV069464_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV076258_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV015318_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV012816_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 8 |
| Degree-1 buses | 229 |
| Tree depth (max hops) | 54 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 649 | 1 | 648 | 0 | 0 | 0 |
| Tier LV_236V | 522 | 54 | 468 | 0 | 0 | 0 |
| Tier MV_11.8kV | 127 | 1 | 126 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 54; skipped invalid branches: 0.

Galvanic zones: 55; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_DROUG | MV_11.8kV | 127 | 0 | 0 | 54 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2469 declared bus terminals; 2250 mapped line/closed-switch conductor edges; 219 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 20900.0 | 2.852 | 2874 |
| q_nom | 0.0 | 6280.0 | 2.852 | 2874 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.5 | 4490.0 | 1.758 | 594 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.656 | 54 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 615 of 958 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920678_consumption' has phase imbalance of 288.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920937_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920628_consumption' has phase imbalance of 201.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920888_consumption' has phase imbalance of 201.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920890_consumption' has phase imbalance of 149.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920931_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920846_consumption' has phase imbalance of 262.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921041_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921114_consumption' has phase imbalance of 258.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920901_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920621_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920616_consumption' has phase imbalance of 210.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920822_consumption' has phase imbalance of 59.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921134_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921083_consumption' has phase imbalance of 107.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921093_consumption' has phase imbalance of 122.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921060_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920818_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920847_consumption' has phase imbalance of 145.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921019_consumption' has phase imbalance of 145.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920998_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921005_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920595_consumption' has phase imbalance of 29.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921056_consumption' has phase imbalance of 278.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920699_consumption' has phase imbalance of 43.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920800_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921072_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920912_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921062_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1180650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920842_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920829_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921046_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920648_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920841_consumption' has phase imbalance of 113.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921092_consumption' has phase imbalance of 98.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921004_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920629_consumption' has phase imbalance of 270.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921113_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920768_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920583_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921143_consumption' has phase imbalance of 52.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1179403_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920669_consumption' has phase imbalance of 239.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920834_consumption' has phase imbalance of 84.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920957_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920619_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920831_consumption' has phase imbalance of 126.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920734_consumption' has phase imbalance of 140.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920608_consumption' has phase imbalance of 36.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920677_consumption' has phase imbalance of 72.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920706_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921006_consumption' has phase imbalance of 144.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921008_consumption' has phase imbalance of 40.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920971_consumption' has phase imbalance of 258.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921069_consumption' has phase imbalance of 85.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920715_consumption' has phase imbalance of 42.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920843_consumption' has phase imbalance of 278.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920676_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920654_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920738_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920618_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920913_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920830_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920948_consumption' has phase imbalance of 120.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920849_consumption' has phase imbalance of 88.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920896_consumption' has phase imbalance of 225.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921128_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921055_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920679_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921094_consumption' has phase imbalance of 135.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920838_consumption' has phase imbalance of 171.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920698_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921047_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921091_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921081_consumption' has phase imbalance of 94.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920805_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921020_consumption' has phase imbalance of 202.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920880_consumption' has phase imbalance of 63.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920652_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920557_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920825_consumption' has phase imbalance of 149.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921002_consumption' has phase imbalance of 23.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920850_consumption' has phase imbalance of 93.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920902_consumption' has phase imbalance of 268.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920610_consumption' has phase imbalance of 238.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921017_consumption' has phase imbalance of 254.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920944_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920705_consumption' has phase imbalance of 68.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920799_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920716_consumption' has phase imbalance of 125.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921102_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920827_consumption' has phase imbalance of 132.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920857_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920670_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921025_consumption' has phase imbalance of 292.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921089_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921074_consumption' has phase imbalance of 77.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1180647_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921080_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921066_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920653_consumption' has phase imbalance of 93.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1180649_consumption' has phase imbalance of 202.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920938_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920870_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920823_consumption' has phase imbalance of 134.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920953_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1179400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1179399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920892_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920821_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921109_consumption' has phase imbalance of 124.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920582_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920680_consumption' has phase imbalance of 221.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920722_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920620_consumption' has phase imbalance of 284.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921132_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920879_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920897_consumption' has phase imbalance of 119.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920625_consumption' has phase imbalance of 293.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920839_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920627_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1180648_consumption' has phase imbalance of 255.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920826_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920898_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921043_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921067_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920891_consumption' has phase imbalance of 108.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920885_consumption' has phase imbalance of 239.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920777_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920844_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921099_consumption' has phase imbalance of 52.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920820_consumption' has phase imbalance of 201.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920947_consumption' has phase imbalance of 58.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920765_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920813_consumption' has phase imbalance of 103.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920989_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921026_consumption' has phase imbalance of 185.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920837_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920603_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920854_consumption' has phase imbalance of 48.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920695_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920996_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920851_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920763_consumption' has phase imbalance of 83.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921001_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920711_consumption' has phase imbalance of 142.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921075_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921016_consumption' has phase imbalance of 33.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1180652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920945_consumption' has phase imbalance of 209.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920752_consumption' has phase imbalance of 28.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920790_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920702_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921030_consumption' has phase imbalance of 216.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921073_consumption' has phase imbalance of 89.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920990_consumption' has phase imbalance of 222.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921022_consumption' has phase imbalance of 83.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921009_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920617_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920714_consumption' has phase imbalance of 263.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920819_consumption' has phase imbalance of 35.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920992_consumption' has phase imbalance of 140.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921007_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921021_consumption' has phase imbalance of 83.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920609_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920721_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920744_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920836_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920672_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920688_consumption' has phase imbalance of 61.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920769_consumption' has phase imbalance of 273.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921054_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920814_consumption' has phase imbalance of 51.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920853_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920899_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920894_consumption' has phase imbalance of 105.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920740_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920991_consumption' has phase imbalance of 148.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920720_consumption' has phase imbalance of 234.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920597_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920955_consumption' has phase imbalance of 148.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920884_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920631_consumption' has phase imbalance of 200.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921123_consumption' has phase imbalance of 138.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920718_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920845_consumption' has phase imbalance of 232.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920682_consumption' has phase imbalance of 85.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920626_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920681_consumption' has phase imbalance of 147.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920949_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920808_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920564_consumption' has phase imbalance of 215.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920893_consumption' has phase imbalance of 131.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920835_consumption' has phase imbalance of 172.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920696_consumption' has phase imbalance of 34.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1179404_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921140_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920791_consumption' has phase imbalance of 190.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920632_consumption' has phase imbalance of 223.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920858_consumption' has phase imbalance of 197.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920704_consumption' has phase imbalance of 113.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921096_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus920903_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus921138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 958 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus921146' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus921116' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus920572' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus920918' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus920874' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.595 MW |
| Total load Q | 478.4 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV039413_Transformer | 176.0 kVA | 7.3% |
| 52_MVLV085012_Transformer | 176.0 kVA | 4.9% |
| 52_MVLV088977_Transformer | 440.0 kVA | 4.6% |
| 52_MVLV042715_Transformer | 275.0 kVA | 5.1% |
| 52_MVLV011684_Transformer | 440.0 kVA | 11.9% |
| 52_MVLV007384_Transformer | 176.0 kVA | 5.4% |
| 52_MVLV056877_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV104513_Transformer | 110.0 kVA | 0.6% |
| 52_MVLV003718_Transformer | 110.0 kVA | 0.3% |
| 52_MVLV008610_Transformer | 110.0 kVA | 4.9% |
| 52_MVLV009858_Transformer | 693.0 kVA | 21.0% |
| 52_MVLV077489_Transformer | 440.0 kVA | 14.9% |
| 52_MVLV045131_Transformer | 110.0 kVA | 3.2% |
| 52_MVLV006817_Transformer | 176.0 kVA | 4.4% |
| 52_MVLV085960_Transformer | 275.0 kVA | 18.4% |
| 52_MVLV107089_Transformer | 176.0 kVA | 9.2% |
| 52_MVLV055882_Transformer | 110.0 kVA | 2.0% |
| 52_MVLV010193_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV100957_Transformer | 110.0 kVA | 1.8% |
| 52_MVLV070738_Transformer | 110.0 kVA | 5.2% |
| 52_MVLV097457_Transformer | 693.0 kVA | 29.7% |
| 52_MVLV044764_Transformer | 176.0 kVA | 2.9% |
| 52_MVLV065068_Transformer | 110.0 kVA | 7.0% |
| 52_MVLV107121_Transformer | 275.0 kVA | 4.6% |
| 52_MVLV010021_Transformer | 176.0 kVA | 4.1% |
| 52_MVLV038170_Transformer | 176.0 kVA | 4.4% |
| 52_MVLV096930_Transformer | 275.0 kVA | 8.6% |
| 52_MVLV035851_Transformer | 693.0 kVA | 28.4% |
| 52_MVLV097455_Transformer | 176.0 kVA | 5.7% |
| 52_MVLV088966_Transformer | 110.0 kVA | 3.5% |
| 52_MVLV065370_Transformer | 110.0 kVA | 2.3% |
| 52_MVLV034161_Transformer | 440.0 kVA | 12.3% |
| 52_MVLV079553_Transformer | 275.0 kVA | 5.1% |
| 52_MVLV035469_Transformer | 275.0 kVA | 5.0% |
| 52_MVLV048761_Transformer | 110.0 kVA | 3.0% |
| 52_MVLV091563_Transformer | 275.0 kVA | 9.9% |
| 52_MVLV015220_Transformer | 275.0 kVA | 4.6% |
| 52_MVLV094126_Transformer | 440.0 kVA | 16.3% |
| 52_MVLV062593_Transformer | 176.0 kVA | 5.0% |
| 52_MVLV070951_Transformer | 176.0 kVA | 3.4% |
| 52_MVLV093362_Transformer | 440.0 kVA | 14.8% |
| 52_MVLV076960_Transformer | 176.0 kVA | 9.3% |
| 52_MVLV070729_Transformer | 176.0 kVA | 4.3% |
| 52_MVLV088981_Transformer | 275.0 kVA | 8.6% |
| 52_MVLV079536_Transformer | 110.0 kVA | 4.3% |
| 52_MVLV036837_Transformer | 176.0 kVA | 6.1% |
| 52_MVLV029495_Transformer | 275.0 kVA | 20.4% |
| 52_MVLV030911_Transformer | 110.0 kVA | 2.0% |
| 52_MVLV040481_Transformer | 176.0 kVA | 3.2% |
| 52_MVLV107120_Transformer | 110.0 kVA | 6.1% |
| 52_MVLV069464_Transformer | 693.0 kVA | 22.8% |
| 52_MVLV076258_Transformer | 440.0 kVA | 28.2% |
| 52_MVLV015318_Transformer | 440.0 kVA | 14.9% |
| 52_MVLV012816_Transformer | 110.0 kVA | 0.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.59 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '52_LVBus920755' (LV, 0.24 kV) has an electrical reach of 1.03 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus920959' (LV, 0.24 kV) has an electrical reach of 9.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus921146' (LV, 0.24 kV) has an electrical reach of 15.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus920547' (LV, 0.24 kV) has an electrical reach of 19.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 649 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 649 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 54 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 127 |
| LV_236V | 4-wire | 522 / 522 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 522 |
| Neutral branches | 468 |
| Grounding points | 54 |
| Neutral sections | 54 |
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
| 11.78 kV | 127 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 59 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 55 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2560.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 522 / 127 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 616 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 616 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1179399_production, 52_LVBus1179400_production, 52_LVBus1179401_consumption, 52_LVBus1179401_production, 52_LVBus1179402_consumption, 52_LVBus1179402_production, 52_LVBus1179403_production, 52_LVBus1179404_production, 52_LVBus1179405_consumption, 52_LVBus1179405_production, 52_LVBus1180644_production, 52_LVBus1180647_production, 52_LVBus1180648_production, 52_LVBus1180649_production, 52_LVBus1180650_production, 52_LVBus1180651_consumption, 52_LVBus1180651_production, 52_LVBus1180652_production, 52_LVBus1180653_consumption, 52_LVBus1180653_production, 52_LVBus1189203_consumption, 52_LVBus1189203_production, 52_LVBus920547_production, 52_LVBus920549_production, 52_LVBus920551_production, 52_LVBus920553_consumption, 52_LVBus920553_production, 52_LVBus920554_production, 52_LVBus920556_consumption, 52_LVBus920556_production, 52_LVBus920557_production, 52_LVBus920558_consumption, 52_LVBus920558_production, 52_LVBus920559_production, 52_LVBus920560_production, 52_LVBus920561_consumption, 52_LVBus920561_production, 52_LVBus920562_consumption, 52_LVBus920562_production, 52_LVBus920563_consumption, 52_LVBus920563_production, 52_LVBus920564_production, 52_LVBus920565_production, 52_LVBus920569_production, 52_LVBus920570_production, 52_LVBus920572_production, 52_LVBus920573_production, 52_LVBus920574_consumption, 52_LVBus920574_production, 52_LVBus920575_production, 52_LVBus920577_production, 52_LVBus920579_consumption, 52_LVBus920579_production, 52_LVBus920581_consumption, 52_LVBus920581_production, 52_LVBus920582_production, 52_LVBus920583_production, 52_LVBus920587_consumption, 52_LVBus920587_production, 52_LVBus920588_consumption, 52_LVBus920588_production, 52_LVBus920590_consumption, 52_LVBus920590_production, 52_LVBus920593_consumption, 52_LVBus920593_production, 52_LVBus920595_production, 52_LVBus920596_production, 52_LVBus920597_production, 52_LVBus920600_production, 52_LVBus920602_consumption, 52_LVBus920602_production, 52_LVBus920603_production, 52_LVBus920604_production, 52_LVBus920605_production, 52_LVBus920606_consumption, 52_LVBus920606_production, 52_LVBus920607_production, 52_LVBus920608_production, 52_LVBus920609_production, 52_LVBus920610_production, 52_LVBus920611_production, 52_LVBus920615_consumption, 52_LVBus920615_production, 52_LVBus920616_production, 52_LVBus920617_production, 52_LVBus920618_production, 52_LVBus920619_production, 52_LVBus920620_production, 52_LVBus920621_production, 52_LVBus920623_consumption, 52_LVBus920623_production, 52_LVBus920625_production, 52_LVBus920626_production, 52_LVBus920627_production, 52_LVBus920628_production, 52_LVBus920629_production, 52_LVBus920631_production, 52_LVBus920632_production, 52_LVBus920633_production, 52_LVBus920648_production, 52_LVBus920649_production, 52_LVBus920650_consumption, 52_LVBus920650_production, 52_LVBus920652_production, 52_LVBus920653_production, 52_LVBus920654_production, 52_LVBus920655_production, 52_LVBus920656_production, 52_LVBus920658_consumption, 52_LVBus920658_production, 52_LVBus920659_consumption, 52_LVBus920659_production, 52_LVBus920660_consumption, 52_LVBus920660_production, 52_LVBus920661_consumption, 52_LVBus920661_production, 52_LVBus920662_production, 52_LVBus920663_consumption, 52_LVBus920663_production, 52_LVBus920665_production, 52_LVBus920666_consumption, 52_LVBus920666_production, 52_LVBus920668_production, 52_LVBus920669_production, 52_LVBus920670_production, 52_LVBus920672_production, 52_LVBus920673_consumption, 52_LVBus920673_production, 52_LVBus920676_production, 52_LVBus920677_production, 52_LVBus920678_production, 52_LVBus920679_production, 52_LVBus920680_production, 52_LVBus920681_production, 52_LVBus920682_production, 52_LVBus920684_production, 52_LVBus920686_consumption, 52_LVBus920686_production, 52_LVBus920688_production, 52_LVBus920690_consumption, 52_LVBus920690_production, 52_LVBus920691_production, 52_LVBus920693_production, 52_LVBus920695_production, 52_LVBus920696_production, 52_LVBus920697_consumption, 52_LVBus920697_production, 52_LVBus920698_production, 52_LVBus920699_production, 52_LVBus920700_production, 52_LVBus920701_production, 52_LVBus920702_production, 52_LVBus920704_production, 52_LVBus920705_production, 52_LVBus920706_production, 52_LVBus920707_production, 52_LVBus920709_consumption, 52_LVBus920709_production, 52_LVBus920710_production, 52_LVBus920711_production, 52_LVBus920712_production, 52_LVBus920714_production, 52_LVBus920715_production, 52_LVBus920716_production, 52_LVBus920718_production, 52_LVBus920719_production, 52_LVBus920720_production, 52_LVBus920721_production, 52_LVBus920722_production, 52_LVBus920724_production, 52_LVBus920725_consumption, 52_LVBus920725_production, 52_LVBus920726_consumption, 52_LVBus920726_production, 52_LVBus920727_production, 52_LVBus920728_consumption, 52_LVBus920728_production, 52_LVBus920729_production, 52_LVBus920731_consumption, 52_LVBus920731_production, 52_LVBus920733_consumption, 52_LVBus920733_production, 52_LVBus920734_production, 52_LVBus920735_consumption, 52_LVBus920735_production, 52_LVBus920736_production, 52_LVBus920738_production, 52_LVBus920739_consumption, 52_LVBus920739_production, 52_LVBus920740_production, 52_LVBus920741_production, 52_LVBus920742_consumption, 52_LVBus920742_production, 52_LVBus920743_consumption, 52_LVBus920743_production, 52_LVBus920744_production, 52_LVBus920746_consumption, 52_LVBus920746_production, 52_LVBus920747_consumption, 52_LVBus920747_production, 52_LVBus920748_production, 52_LVBus920749_production, 52_LVBus920750_consumption, 52_LVBus920750_production, 52_LVBus920751_consumption, 52_LVBus920751_production, 52_LVBus920752_production, 52_LVBus920753_production, 52_LVBus920755_consumption, 52_LVBus920755_production, 52_LVBus920756_consumption, 52_LVBus920756_production, 52_LVBus920757_consumption, 52_LVBus920757_production, 52_LVBus920758_consumption, 52_LVBus920758_production, 52_LVBus920759_production, 52_LVBus920760_consumption, 52_LVBus920760_production, 52_LVBus920761_production, 52_LVBus920763_production, 52_LVBus920765_production, 52_LVBus920766_consumption, 52_LVBus920766_production, 52_LVBus920768_production, 52_LVBus920769_production, 52_LVBus920775_production, 52_LVBus920776_consumption, 52_LVBus920776_production, 52_LVBus920777_production, 52_LVBus920778_production, 52_LVBus920780_consumption, 52_LVBus920780_production, 52_LVBus920781_production, 52_LVBus920782_production, 52_LVBus920783_consumption, 52_LVBus920783_production, 52_LVBus920784_production, 52_LVBus920789_consumption, 52_LVBus920789_production, 52_LVBus920790_production, 52_LVBus920791_production, 52_LVBus920793_consumption, 52_LVBus920793_production, 52_LVBus920794_consumption, 52_LVBus920794_production, 52_LVBus920795_consumption, 52_LVBus920795_production, 52_LVBus920796_consumption, 52_LVBus920796_production, 52_LVBus920798_production, 52_LVBus920799_production, 52_LVBus920800_production, 52_LVBus920802_consumption, 52_LVBus920802_production, 52_LVBus920803_production, 52_LVBus920805_production, 52_LVBus920807_consumption, 52_LVBus920807_production, 52_LVBus920808_production, 52_LVBus920809_production, 52_LVBus920813_production, 52_LVBus920814_production, 52_LVBus920815_consumption, 52_LVBus920815_production, 52_LVBus920816_production, 52_LVBus920818_production, 52_LVBus920819_production, 52_LVBus920820_production, 52_LVBus920821_production, 52_LVBus920822_production, 52_LVBus920823_production, 52_LVBus920824_consumption, 52_LVBus920824_production, 52_LVBus920825_production, 52_LVBus920826_production, 52_LVBus920827_production, 52_LVBus920829_production, 52_LVBus920830_production, 52_LVBus920831_production, 52_LVBus920833_consumption, 52_LVBus920833_production, 52_LVBus920834_production, 52_LVBus920835_production, 52_LVBus920836_production, 52_LVBus920837_production, 52_LVBus920838_production, 52_LVBus920839_production, 52_LVBus920841_production, 52_LVBus920842_production, 52_LVBus920843_production, 52_LVBus920844_production, 52_LVBus920845_production, 52_LVBus920846_production, 52_LVBus920847_production, 52_LVBus920849_production, 52_LVBus920850_production, 52_LVBus920851_production, 52_LVBus920852_production, 52_LVBus920853_production, 52_LVBus920854_production, 52_LVBus920856_consumption, 52_LVBus920856_production, 52_LVBus920857_production, 52_LVBus920858_production, 52_LVBus920859_production, 52_LVBus920860_production, 52_LVBus920864_consumption, 52_LVBus920864_production, 52_LVBus920865_production, 52_LVBus920866_production, 52_LVBus920867_consumption, 52_LVBus920867_production, 52_LVBus920868_production, 52_LVBus920869_production, 52_LVBus920870_production, 52_LVBus920874_production, 52_LVBus920876_consumption, 52_LVBus920876_production, 52_LVBus920878_consumption, 52_LVBus920878_production, 52_LVBus920879_production, 52_LVBus920880_production, 52_LVBus920882_consumption, 52_LVBus920882_production, 52_LVBus920883_production, 52_LVBus920884_production, 52_LVBus920885_production, 52_LVBus920886_production, 52_LVBus920887_production, 52_LVBus920888_production, 52_LVBus920889_production, 52_LVBus920890_production, 52_LVBus920891_production, 52_LVBus920892_production, 52_LVBus920893_production, 52_LVBus920894_production, 52_LVBus920896_production, 52_LVBus920897_production, 52_LVBus920898_production, 52_LVBus920899_production, 52_LVBus920901_production, 52_LVBus920902_production, 52_LVBus920903_production, 52_LVBus920905_consumption, 52_LVBus920905_production, 52_LVBus920907_consumption, 52_LVBus920907_production, 52_LVBus920908_consumption, 52_LVBus920908_production, 52_LVBus920909_production, 52_LVBus920910_production, 52_LVBus920911_consumption, 52_LVBus920911_production, 52_LVBus920912_production, 52_LVBus920913_production, 52_LVBus920914_production, 52_LVBus920918_consumption, 52_LVBus920918_production, 52_LVBus920920_production, 52_LVBus920922_consumption, 52_LVBus920922_production, 52_LVBus920923_production, 52_LVBus920924_production, 52_LVBus920928_production, 52_LVBus920930_consumption, 52_LVBus920930_production, 52_LVBus920931_production, 52_LVBus920932_consumption, 52_LVBus920932_production, 52_LVBus920934_consumption, 52_LVBus920934_production, 52_LVBus920935_production, 52_LVBus920936_consumption, 52_LVBus920936_production, 52_LVBus920937_production, 52_LVBus920938_production, 52_LVBus920939_production, 52_LVBus920940_consumption, 52_LVBus920940_production, 52_LVBus920942_production, 52_LVBus920943_production, 52_LVBus920944_production, 52_LVBus920945_production, 52_LVBus920946_production, 52_LVBus920947_production, 52_LVBus920948_production, 52_LVBus920949_production, 52_LVBus920951_production, 52_LVBus920952_production, 52_LVBus920953_production, 52_LVBus920955_production, 52_LVBus920956_consumption, 52_LVBus920956_production, 52_LVBus920957_production, 52_LVBus920959_production, 52_LVBus920960_production, 52_LVBus920963_consumption, 52_LVBus920963_production, 52_LVBus920965_consumption, 52_LVBus920965_production, 52_LVBus920967_production, 52_LVBus920968_production, 52_LVBus920969_consumption, 52_LVBus920969_production, 52_LVBus920970_consumption, 52_LVBus920970_production, 52_LVBus920971_production, 52_LVBus920972_consumption, 52_LVBus920972_production, 52_LVBus920973_consumption, 52_LVBus920973_production, 52_LVBus920974_production, 52_LVBus920975_consumption, 52_LVBus920975_production, 52_LVBus920976_production, 52_LVBus920978_consumption, 52_LVBus920978_production, 52_LVBus920979_production, 52_LVBus920980_consumption, 52_LVBus920980_production, 52_LVBus920981_consumption, 52_LVBus920981_production, 52_LVBus920983_consumption, 52_LVBus920983_production, 52_LVBus920984_production, 52_LVBus920986_production, 52_LVBus920988_production, 52_LVBus920989_production, 52_LVBus920990_production, 52_LVBus920991_production, 52_LVBus920992_production, 52_LVBus920993_production, 52_LVBus920995_production, 52_LVBus920996_production, 52_LVBus920997_consumption, 52_LVBus920997_production, 52_LVBus920998_production, 52_LVBus921000_consumption, 52_LVBus921000_production, 52_LVBus921001_production, 52_LVBus921002_production, 52_LVBus921004_production, 52_LVBus921005_production, 52_LVBus921006_production, 52_LVBus921007_production, 52_LVBus921008_production, 52_LVBus921009_production, 52_LVBus921010_production, 52_LVBus921011_production, 52_LVBus921012_consumption, 52_LVBus921012_production, 52_LVBus921013_consumption, 52_LVBus921013_production, 52_LVBus921014_consumption, 52_LVBus921014_production, 52_LVBus921016_production, 52_LVBus921017_production, 52_LVBus921019_production, 52_LVBus921020_production, 52_LVBus921021_production, 52_LVBus921022_production, 52_LVBus921024_production, 52_LVBus921025_production, 52_LVBus921026_production, 52_LVBus921027_consumption, 52_LVBus921027_production, 52_LVBus921028_production, 52_LVBus921029_production, 52_LVBus921030_production, 52_LVBus921031_production, 52_LVBus921032_production, 52_LVBus921033_production, 52_LVBus921034_production, 52_LVBus921036_consumption, 52_LVBus921036_production, 52_LVBus921037_consumption, 52_LVBus921037_production, 52_LVBus921038_production, 52_LVBus921039_production, 52_LVBus921040_consumption, 52_LVBus921040_production, 52_LVBus921041_production, 52_LVBus921042_production, 52_LVBus921043_production, 52_LVBus921044_production, 52_LVBus921046_production, 52_LVBus921047_production, 52_LVBus921048_production, 52_LVBus921049_production, 52_LVBus921051_production, 52_LVBus921052_production, 52_LVBus921053_consumption, 52_LVBus921053_production, 52_LVBus921054_production, 52_LVBus921055_production, 52_LVBus921056_production, 52_LVBus921058_consumption, 52_LVBus921058_production, 52_LVBus921059_production, 52_LVBus921060_production, 52_LVBus921061_production, 52_LVBus921062_production, 52_LVBus921063_production, 52_LVBus921065_consumption, 52_LVBus921065_production, 52_LVBus921066_production, 52_LVBus921067_production, 52_LVBus921068_production, 52_LVBus921069_production, 52_LVBus921070_production, 52_LVBus921072_production, 52_LVBus921073_production, 52_LVBus921074_production, 52_LVBus921075_production, 52_LVBus921076_consumption, 52_LVBus921076_production, 52_LVBus921077_production, 52_LVBus921079_production, 52_LVBus921080_production, 52_LVBus921081_production, 52_LVBus921082_production, 52_LVBus921083_production, 52_LVBus921084_production, 52_LVBus921086_production, 52_LVBus921087_production, 52_LVBus921088_consumption, 52_LVBus921088_production, 52_LVBus921089_production, 52_LVBus921090_production, 52_LVBus921091_production, 52_LVBus921092_production, 52_LVBus921093_production, 52_LVBus921094_production, 52_LVBus921095_production, 52_LVBus921096_production, 52_LVBus921097_consumption, 52_LVBus921097_production, 52_LVBus921099_production, 52_LVBus921100_production, 52_LVBus921101_production, 52_LVBus921102_production, 52_LVBus921103_production, 52_LVBus921104_production, 52_LVBus921105_consumption, 52_LVBus921105_production, 52_LVBus921106_consumption, 52_LVBus921106_production, 52_LVBus921107_consumption, 52_LVBus921107_production, 52_LVBus921108_production, 52_LVBus921109_production, 52_LVBus921110_consumption, 52_LVBus921110_production, 52_LVBus921111_consumption, 52_LVBus921111_production, 52_LVBus921112_production, 52_LVBus921113_production, 52_LVBus921114_production, 52_LVBus921116_production, 52_LVBus921118_consumption, 52_LVBus921118_production, 52_LVBus921119_consumption, 52_LVBus921119_production, 52_LVBus921120_consumption, 52_LVBus921120_production, 52_LVBus921122_consumption, 52_LVBus921122_production, 52_LVBus921123_production, 52_LVBus921124_consumption, 52_LVBus921124_production, 52_LVBus921126_consumption, 52_LVBus921126_production, 52_LVBus921127_production, 52_LVBus921128_production, 52_LVBus921129_consumption, 52_LVBus921129_production, 52_LVBus921130_consumption, 52_LVBus921130_production, 52_LVBus921131_consumption, 52_LVBus921131_production, 52_LVBus921132_production, 52_LVBus921133_production, 52_LVBus921134_production, 52_LVBus921135_consumption, 52_LVBus921135_production, 52_LVBus921136_production, 52_LVBus921137_production, 52_LVBus921138_production, 52_LVBus921140_production, 52_LVBus921141_production, 52_LVBus921143_production, 52_LVBus921144_production, 52_LVBus921146_production, 52_MVLV005214_consumption, 52_MVLV005214_production, 52_MVLV011325_consumption, 52_MVLV011325_production, 52_MVLV020300_consumption, 52_MVLV020300_production, 52_MVLV041618_consumption, 52_MVLV041618_production, 52_MVLV044793_consumption, 52_MVLV044793_production, 52_MVLV045130_consumption, 52_MVLV045130_production, 52_MVLV064945_consumption, 52_MVLV064945_production, 52_MVLV067068_consumption, 52_MVLV067068_production, 52_MVLV072977_consumption, 52_MVLV072977_production, 52_MVLV100172_consumption, 52_MVLV100172_production, 52_MVLV105210_consumption, 52_MVLV105210_production.

## 9. Data Quality Summary

**Total findings:** 329 (0 errors, 5 warnings, 324 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  615 of 958 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.59 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  616 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920866_consumption`  
  Load '52_LVBus920866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920551_consumption`  
  Load '52_LVBus920551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920678_consumption`  
  Load '52_LVBus920678_consumption' has phase imbalance of 288.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920937_consumption`  
  Load '52_LVBus920937_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920628_consumption`  
  Load '52_LVBus920628_consumption' has phase imbalance of 201.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920662_consumption`  
  Load '52_LVBus920662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920888_consumption`  
  Load '52_LVBus920888_consumption' has phase imbalance of 201.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920890_consumption`  
  Load '52_LVBus920890_consumption' has phase imbalance of 149.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920886_consumption`  
  Load '52_LVBus920886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920611_consumption`  
  Load '52_LVBus920611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920931_consumption`  
  Load '52_LVBus920931_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920846_consumption`  
  Load '52_LVBus920846_consumption' has phase imbalance of 262.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921041_consumption`  
  Load '52_LVBus921041_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921114_consumption`  
  Load '52_LVBus921114_consumption' has phase imbalance of 258.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920901_consumption`  
  Load '52_LVBus920901_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920621_consumption`  
  Load '52_LVBus920621_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920616_consumption`  
  Load '52_LVBus920616_consumption' has phase imbalance of 210.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920822_consumption`  
  Load '52_LVBus920822_consumption' has phase imbalance of 59.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921134_consumption`  
  Load '52_LVBus921134_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921083_consumption`  
  Load '52_LVBus921083_consumption' has phase imbalance of 107.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921093_consumption`  
  Load '52_LVBus921093_consumption' has phase imbalance of 122.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921060_consumption`  
  Load '52_LVBus921060_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920818_consumption`  
  Load '52_LVBus920818_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920665_consumption`  
  Load '52_LVBus920665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920560_consumption`  
  Load '52_LVBus920560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921133_consumption`  
  Load '52_LVBus921133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920847_consumption`  
  Load '52_LVBus920847_consumption' has phase imbalance of 145.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921019_consumption`  
  Load '52_LVBus921019_consumption' has phase imbalance of 145.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921100_consumption`  
  Load '52_LVBus921100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920998_consumption`  
  Load '52_LVBus920998_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921005_consumption`  
  Load '52_LVBus921005_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920749_consumption`  
  Load '52_LVBus920749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920595_consumption`  
  Load '52_LVBus920595_consumption' has phase imbalance of 29.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921056_consumption`  
  Load '52_LVBus921056_consumption' has phase imbalance of 278.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921141_consumption`  
  Load '52_LVBus921141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920699_consumption`  
  Load '52_LVBus920699_consumption' has phase imbalance of 43.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920800_consumption`  
  Load '52_LVBus920800_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921072_consumption`  
  Load '52_LVBus921072_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921137_consumption`  
  Load '52_LVBus921137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920912_consumption`  
  Load '52_LVBus920912_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921144_consumption`  
  Load '52_LVBus921144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921062_consumption`  
  Load '52_LVBus921062_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920554_consumption`  
  Load '52_LVBus920554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1180650_consumption`  
  Load '52_LVBus1180650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920842_consumption`  
  Load '52_LVBus920842_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920829_consumption`  
  Load '52_LVBus920829_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921046_consumption`  
  Load '52_LVBus921046_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920648_consumption`  
  Load '52_LVBus920648_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920841_consumption`  
  Load '52_LVBus920841_consumption' has phase imbalance of 113.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921092_consumption`  
  Load '52_LVBus921092_consumption' has phase imbalance of 98.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921004_consumption`  
  Load '52_LVBus921004_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920629_consumption`  
  Load '52_LVBus920629_consumption' has phase imbalance of 270.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921113_consumption`  
  Load '52_LVBus921113_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920768_consumption`  
  Load '52_LVBus920768_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920988_consumption`  
  Load '52_LVBus920988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921028_consumption`  
  Load '52_LVBus921028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920707_consumption`  
  Load '52_LVBus920707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920570_consumption`  
  Load '52_LVBus920570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920952_consumption`  
  Load '52_LVBus920952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920583_consumption`  
  Load '52_LVBus920583_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921084_consumption`  
  Load '52_LVBus921084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920809_consumption`  
  Load '52_LVBus920809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921143_consumption`  
  Load '52_LVBus921143_consumption' has phase imbalance of 52.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920865_consumption`  
  Load '52_LVBus920865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1179403_consumption`  
  Load '52_LVBus1179403_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920887_consumption`  
  Load '52_LVBus920887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920669_consumption`  
  Load '52_LVBus920669_consumption' has phase imbalance of 239.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920834_consumption`  
  Load '52_LVBus920834_consumption' has phase imbalance of 84.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920935_consumption`  
  Load '52_LVBus920935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920957_consumption`  
  Load '52_LVBus920957_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920619_consumption`  
  Load '52_LVBus920619_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920727_consumption`  
  Load '52_LVBus920727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920831_consumption`  
  Load '52_LVBus920831_consumption' has phase imbalance of 126.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920734_consumption`  
  Load '52_LVBus920734_consumption' has phase imbalance of 140.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920608_consumption`  
  Load '52_LVBus920608_consumption' has phase imbalance of 36.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920677_consumption`  
  Load '52_LVBus920677_consumption' has phase imbalance of 72.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920883_consumption`  
  Load '52_LVBus920883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920706_consumption`  
  Load '52_LVBus920706_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921044_consumption`  
  Load '52_LVBus921044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920943_consumption`  
  Load '52_LVBus920943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921034_consumption`  
  Load '52_LVBus921034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921006_consumption`  
  Load '52_LVBus921006_consumption' has phase imbalance of 144.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920565_consumption`  
  Load '52_LVBus920565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921008_consumption`  
  Load '52_LVBus921008_consumption' has phase imbalance of 40.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920701_consumption`  
  Load '52_LVBus920701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920971_consumption`  
  Load '52_LVBus920971_consumption' has phase imbalance of 258.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921069_consumption`  
  Load '52_LVBus921069_consumption' has phase imbalance of 85.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920715_consumption`  
  Load '52_LVBus920715_consumption' has phase imbalance of 42.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920843_consumption`  
  Load '52_LVBus920843_consumption' has phase imbalance of 278.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920676_consumption`  
  Load '52_LVBus920676_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921082_consumption`  
  Load '52_LVBus921082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920923_consumption`  
  Load '52_LVBus920923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920654_consumption`  
  Load '52_LVBus920654_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921029_consumption`  
  Load '52_LVBus921029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920738_consumption`  
  Load '52_LVBus920738_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920618_consumption`  
  Load '52_LVBus920618_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920913_consumption`  
  Load '52_LVBus920913_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920830_consumption`  
  Load '52_LVBus920830_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920948_consumption`  
  Load '52_LVBus920948_consumption' has phase imbalance of 120.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920849_consumption`  
  Load '52_LVBus920849_consumption' has phase imbalance of 88.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920896_consumption`  
  Load '52_LVBus920896_consumption' has phase imbalance of 225.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921128_consumption`  
  Load '52_LVBus921128_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921055_consumption`  
  Load '52_LVBus921055_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920633_consumption`  
  Load '52_LVBus920633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920649_consumption`  
  Load '52_LVBus920649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920679_consumption`  
  Load '52_LVBus920679_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920668_consumption`  
  Load '52_LVBus920668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921094_consumption`  
  Load '52_LVBus921094_consumption' has phase imbalance of 135.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920838_consumption`  
  Load '52_LVBus920838_consumption' has phase imbalance of 171.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920698_consumption`  
  Load '52_LVBus920698_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921047_consumption`  
  Load '52_LVBus921047_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921091_consumption`  
  Load '52_LVBus921091_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921081_consumption`  
  Load '52_LVBus921081_consumption' has phase imbalance of 94.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921101_consumption`  
  Load '52_LVBus921101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920805_consumption`  
  Load '52_LVBus920805_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920753_consumption`  
  Load '52_LVBus920753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921086_consumption`  
  Load '52_LVBus921086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921020_consumption`  
  Load '52_LVBus921020_consumption' has phase imbalance of 202.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920880_consumption`  
  Load '52_LVBus920880_consumption' has phase imbalance of 63.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920652_consumption`  
  Load '52_LVBus920652_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920557_consumption`  
  Load '52_LVBus920557_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920825_consumption`  
  Load '52_LVBus920825_consumption' has phase imbalance of 149.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921002_consumption`  
  Load '52_LVBus921002_consumption' has phase imbalance of 23.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920850_consumption`  
  Load '52_LVBus920850_consumption' has phase imbalance of 93.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920902_consumption`  
  Load '52_LVBus920902_consumption' has phase imbalance of 268.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920610_consumption`  
  Load '52_LVBus920610_consumption' has phase imbalance of 238.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920910_consumption`  
  Load '52_LVBus920910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921017_consumption`  
  Load '52_LVBus921017_consumption' has phase imbalance of 254.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920944_consumption`  
  Load '52_LVBus920944_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920705_consumption`  
  Load '52_LVBus920705_consumption' has phase imbalance of 68.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920799_consumption`  
  Load '52_LVBus920799_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920716_consumption`  
  Load '52_LVBus920716_consumption' has phase imbalance of 125.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921102_consumption`  
  Load '52_LVBus921102_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920781_consumption`  
  Load '52_LVBus920781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920827_consumption`  
  Load '52_LVBus920827_consumption' has phase imbalance of 132.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920857_consumption`  
  Load '52_LVBus920857_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920670_consumption`  
  Load '52_LVBus920670_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921025_consumption`  
  Load '52_LVBus921025_consumption' has phase imbalance of 292.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921089_consumption`  
  Load '52_LVBus921089_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921074_consumption`  
  Load '52_LVBus921074_consumption' has phase imbalance of 77.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1180647_consumption`  
  Load '52_LVBus1180647_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920860_consumption`  
  Load '52_LVBus920860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921080_consumption`  
  Load '52_LVBus921080_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921066_consumption`  
  Load '52_LVBus921066_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920656_consumption`  
  Load '52_LVBus920656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921031_consumption`  
  Load '52_LVBus921031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920653_consumption`  
  Load '52_LVBus920653_consumption' has phase imbalance of 93.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920914_consumption`  
  Load '52_LVBus920914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1180649_consumption`  
  Load '52_LVBus1180649_consumption' has phase imbalance of 202.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920938_consumption`  
  Load '52_LVBus920938_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920870_consumption`  
  Load '52_LVBus920870_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920823_consumption`  
  Load '52_LVBus920823_consumption' has phase imbalance of 134.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920924_consumption`  
  Load '52_LVBus920924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920953_consumption`  
  Load '52_LVBus920953_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921048_consumption`  
  Load '52_LVBus921048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1179400_consumption`  
  Load '52_LVBus1179400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1179399_consumption`  
  Load '52_LVBus1179399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920892_consumption`  
  Load '52_LVBus920892_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920821_consumption`  
  Load '52_LVBus920821_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920993_consumption`  
  Load '52_LVBus920993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920655_consumption`  
  Load '52_LVBus920655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921109_consumption`  
  Load '52_LVBus921109_consumption' has phase imbalance of 124.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920582_consumption`  
  Load '52_LVBus920582_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921011_consumption`  
  Load '52_LVBus921011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921127_consumption`  
  Load '52_LVBus921127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920607_consumption`  
  Load '52_LVBus920607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920680_consumption`  
  Load '52_LVBus920680_consumption' has phase imbalance of 221.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920722_consumption`  
  Load '52_LVBus920722_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920620_consumption`  
  Load '52_LVBus920620_consumption' has phase imbalance of 284.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921132_consumption`  
  Load '52_LVBus921132_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920879_consumption`  
  Load '52_LVBus920879_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920897_consumption`  
  Load '52_LVBus920897_consumption' has phase imbalance of 119.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920889_consumption`  
  Load '52_LVBus920889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920625_consumption`  
  Load '52_LVBus920625_consumption' has phase imbalance of 293.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920719_consumption`  
  Load '52_LVBus920719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920839_consumption`  
  Load '52_LVBus920839_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921103_consumption`  
  Load '52_LVBus921103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920939_consumption`  
  Load '52_LVBus920939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920627_consumption`  
  Load '52_LVBus920627_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920782_consumption`  
  Load '52_LVBus920782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920798_consumption`  
  Load '52_LVBus920798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921049_consumption`  
  Load '52_LVBus921049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920605_consumption`  
  Load '52_LVBus920605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921042_consumption`  
  Load '52_LVBus921042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1180648_consumption`  
  Load '52_LVBus1180648_consumption' has phase imbalance of 255.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920826_consumption`  
  Load '52_LVBus920826_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920898_consumption`  
  Load '52_LVBus920898_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921043_consumption`  
  Load '52_LVBus921043_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921067_consumption`  
  Load '52_LVBus921067_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920891_consumption`  
  Load '52_LVBus920891_consumption' has phase imbalance of 108.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920885_consumption`  
  Load '52_LVBus920885_consumption' has phase imbalance of 239.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920777_consumption`  
  Load '52_LVBus920777_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920844_consumption`  
  Load '52_LVBus920844_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920604_consumption`  
  Load '52_LVBus920604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921099_consumption`  
  Load '52_LVBus921099_consumption' has phase imbalance of 52.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920820_consumption`  
  Load '52_LVBus920820_consumption' has phase imbalance of 201.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920547_consumption`  
  Load '52_LVBus920547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920947_consumption`  
  Load '52_LVBus920947_consumption' has phase imbalance of 58.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920765_consumption`  
  Load '52_LVBus920765_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920816_consumption`  
  Load '52_LVBus920816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920775_consumption`  
  Load '52_LVBus920775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920813_consumption`  
  Load '52_LVBus920813_consumption' has phase imbalance of 103.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920989_consumption`  
  Load '52_LVBus920989_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921026_consumption`  
  Load '52_LVBus921026_consumption' has phase imbalance of 185.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920837_consumption`  
  Load '52_LVBus920837_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921090_consumption`  
  Load '52_LVBus921090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920603_consumption`  
  Load '52_LVBus920603_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920854_consumption`  
  Load '52_LVBus920854_consumption' has phase imbalance of 48.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920695_consumption`  
  Load '52_LVBus920695_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920996_consumption`  
  Load '52_LVBus920996_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920851_consumption`  
  Load '52_LVBus920851_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920763_consumption`  
  Load '52_LVBus920763_consumption' has phase imbalance of 83.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920942_consumption`  
  Load '52_LVBus920942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921001_consumption`  
  Load '52_LVBus921001_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920711_consumption`  
  Load '52_LVBus920711_consumption' has phase imbalance of 142.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921075_consumption`  
  Load '52_LVBus921075_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921016_consumption`  
  Load '52_LVBus921016_consumption' has phase imbalance of 33.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1180652_consumption`  
  Load '52_LVBus1180652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920945_consumption`  
  Load '52_LVBus920945_consumption' has phase imbalance of 209.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920752_consumption`  
  Load '52_LVBus920752_consumption' has phase imbalance of 28.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920790_consumption`  
  Load '52_LVBus920790_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920702_consumption`  
  Load '52_LVBus920702_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921030_consumption`  
  Load '52_LVBus921030_consumption' has phase imbalance of 216.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920600_consumption`  
  Load '52_LVBus920600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921073_consumption`  
  Load '52_LVBus921073_consumption' has phase imbalance of 89.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920951_consumption`  
  Load '52_LVBus920951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921063_consumption`  
  Load '52_LVBus921063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920990_consumption`  
  Load '52_LVBus920990_consumption' has phase imbalance of 222.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921022_consumption`  
  Load '52_LVBus921022_consumption' has phase imbalance of 83.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921009_consumption`  
  Load '52_LVBus921009_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920617_consumption`  
  Load '52_LVBus920617_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920714_consumption`  
  Load '52_LVBus920714_consumption' has phase imbalance of 263.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920596_consumption`  
  Load '52_LVBus920596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920819_consumption`  
  Load '52_LVBus920819_consumption' has phase imbalance of 35.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920992_consumption`  
  Load '52_LVBus920992_consumption' has phase imbalance of 140.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921007_consumption`  
  Load '52_LVBus921007_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920859_consumption`  
  Load '52_LVBus920859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921021_consumption`  
  Load '52_LVBus921021_consumption' has phase imbalance of 83.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920609_consumption`  
  Load '52_LVBus920609_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920721_consumption`  
  Load '52_LVBus920721_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921024_consumption`  
  Load '52_LVBus921024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920744_consumption`  
  Load '52_LVBus920744_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920836_consumption`  
  Load '52_LVBus920836_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921061_consumption`  
  Load '52_LVBus921061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920672_consumption`  
  Load '52_LVBus920672_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920688_consumption`  
  Load '52_LVBus920688_consumption' has phase imbalance of 61.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920712_consumption`  
  Load '52_LVBus920712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920769_consumption`  
  Load '52_LVBus920769_consumption' has phase imbalance of 273.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921054_consumption`  
  Load '52_LVBus921054_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920814_consumption`  
  Load '52_LVBus920814_consumption' has phase imbalance of 51.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920853_consumption`  
  Load '52_LVBus920853_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920899_consumption`  
  Load '52_LVBus920899_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920894_consumption`  
  Load '52_LVBus920894_consumption' has phase imbalance of 105.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920868_consumption`  
  Load '52_LVBus920868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920740_consumption`  
  Load '52_LVBus920740_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920991_consumption`  
  Load '52_LVBus920991_consumption' has phase imbalance of 148.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920778_consumption`  
  Load '52_LVBus920778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920720_consumption`  
  Load '52_LVBus920720_consumption' has phase imbalance of 234.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920597_consumption`  
  Load '52_LVBus920597_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921095_consumption`  
  Load '52_LVBus921095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921136_consumption`  
  Load '52_LVBus921136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920955_consumption`  
  Load '52_LVBus920955_consumption' has phase imbalance of 148.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920741_consumption`  
  Load '52_LVBus920741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920869_consumption`  
  Load '52_LVBus920869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920884_consumption`  
  Load '52_LVBus920884_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920631_consumption`  
  Load '52_LVBus920631_consumption' has phase imbalance of 200.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921059_consumption`  
  Load '52_LVBus921059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921123_consumption`  
  Load '52_LVBus921123_consumption' has phase imbalance of 138.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921032_consumption`  
  Load '52_LVBus921032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920718_consumption`  
  Load '52_LVBus920718_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920845_consumption`  
  Load '52_LVBus920845_consumption' has phase imbalance of 232.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920569_consumption`  
  Load '52_LVBus920569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920682_consumption`  
  Load '52_LVBus920682_consumption' has phase imbalance of 85.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920626_consumption`  
  Load '52_LVBus920626_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920681_consumption`  
  Load '52_LVBus920681_consumption' has phase imbalance of 147.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920949_consumption`  
  Load '52_LVBus920949_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920808_consumption`  
  Load '52_LVBus920808_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920559_consumption`  
  Load '52_LVBus920559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920564_consumption`  
  Load '52_LVBus920564_consumption' has phase imbalance of 215.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921052_consumption`  
  Load '52_LVBus921052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920761_consumption`  
  Load '52_LVBus920761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920893_consumption`  
  Load '52_LVBus920893_consumption' has phase imbalance of 131.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920835_consumption`  
  Load '52_LVBus920835_consumption' has phase imbalance of 172.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920696_consumption`  
  Load '52_LVBus920696_consumption' has phase imbalance of 34.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1179404_consumption`  
  Load '52_LVBus1179404_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921140_consumption`  
  Load '52_LVBus921140_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920784_consumption`  
  Load '52_LVBus920784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920852_consumption`  
  Load '52_LVBus920852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920946_consumption`  
  Load '52_LVBus920946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920791_consumption`  
  Load '52_LVBus920791_consumption' has phase imbalance of 190.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920632_consumption`  
  Load '52_LVBus920632_consumption' has phase imbalance of 223.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920858_consumption`  
  Load '52_LVBus920858_consumption' has phase imbalance of 197.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920803_consumption`  
  Load '52_LVBus920803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920684_consumption`  
  Load '52_LVBus920684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920704_consumption`  
  Load '52_LVBus920704_consumption' has phase imbalance of 113.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921077_consumption`  
  Load '52_LVBus921077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921096_consumption`  
  Load '52_LVBus921096_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921010_consumption`  
  Load '52_LVBus921010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus920903_consumption`  
  Load '52_LVBus920903_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus921138_consumption`  
  Load '52_LVBus921138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 958 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus921146' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus921116' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus920572' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus920918' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus920874' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '52_LVBus920755' (LV, 0.24 kV) has an electrical reach of 1.03 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus920959' (LV, 0.24 kV) has an electrical reach of 9.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus921146' (LV, 0.24 kV) has an electrical reach of 15.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus920547' (LV, 0.24 kV) has an electrical reach of 19.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  649 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  191 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 52_LVBus1179399_consumption, 52_LVBus1179400_consumption, 52_LVBus1179404_consumption, 52_LVBus1180647_consumption, 52_LVBus1180648_consumption, 52_LVBus1180649_consumption, 52_LVBus1180650_consumption, 52_LVBus1180652_consumption, 52_LVBus920547_consumption, 52_LVBus920551_consumption, 52_LVBus920554_consumption, 52_LVBus920557_consumption, 52_LVBus920559_consumption, 52_LVBus920560_consumption, 52_LVBus920564_consumption, 52_LVBus920565_consumption, 52_LVBus920569_consumption, 52_LVBus920570_consumption, 52_LVBus920582_consumption, 52_LVBus920596_consumption, 52_LVBus920600_consumption, 52_LVBus920603_consumption, 52_LVBus920604_consumption, 52_LVBus920605_consumption, 52_LVBus920607_consumption, 52_LVBus920609_consumption, 52_LVBus920610_consumption, 52_LVBus920611_consumption, 52_LVBus920616_consumption, 52_LVBus920620_consumption, 52_LVBus920625_consumption, 52_LVBus920626_consumption, 52_LVBus920627_consumption, 52_LVBus920628_consumption, 52_LVBus920629_consumption, 52_LVBus920632_consumption, 52_LVBus920633_consumption, 52_LVBus920648_consumption, 52_LVBus920649_consumption, 52_LVBus920654_consumption, 52_LVBus920655_consumption, 52_LVBus920656_consumption, 52_LVBus920662_consumption, 52_LVBus920665_consumption, 52_LVBus920668_consumption, 52_LVBus920672_consumption, 52_LVBus920678_consumption, 52_LVBus920684_consumption, 52_LVBus920701_consumption, 52_LVBus920706_consumption, 52_LVBus920707_consumption, 52_LVBus920712_consumption, 52_LVBus920714_consumption, 52_LVBus920719_consumption, 52_LVBus920720_consumption, 52_LVBus920722_consumption, 52_LVBus920727_consumption, 52_LVBus920738_consumption, 52_LVBus920740_consumption, 52_LVBus920741_consumption, 52_LVBus920749_consumption, 52_LVBus920753_consumption, 52_LVBus920761_consumption, 52_LVBus920765_consumption, 52_LVBus920768_consumption, 52_LVBus920769_consumption, 52_LVBus920775_consumption, 52_LVBus920778_consumption, 52_LVBus920781_consumption, 52_LVBus920782_consumption, 52_LVBus920784_consumption, 52_LVBus920790_consumption, 52_LVBus920791_consumption, 52_LVBus920798_consumption, 52_LVBus920799_consumption, 52_LVBus920803_consumption, 52_LVBus920808_consumption, 52_LVBus920809_consumption, 52_LVBus920816_consumption, 52_LVBus920818_consumption, 52_LVBus920820_consumption, 52_LVBus920826_consumption, 52_LVBus920829_consumption, 52_LVBus920830_consumption, 52_LVBus920838_consumption, 52_LVBus920839_consumption, 52_LVBus920842_consumption, 52_LVBus920843_consumption, 52_LVBus920844_consumption, 52_LVBus920845_consumption, 52_LVBus920846_consumption, 52_LVBus920851_consumption, 52_LVBus920852_consumption, 52_LVBus920853_consumption, 52_LVBus920857_consumption, 52_LVBus920858_consumption, 52_LVBus920859_consumption, 52_LVBus920860_consumption, 52_LVBus920865_consumption, 52_LVBus920866_consumption, 52_LVBus920868_consumption, 52_LVBus920869_consumption, 52_LVBus920870_consumption, 52_LVBus920879_consumption, 52_LVBus920883_consumption, 52_LVBus920885_consumption, 52_LVBus920886_consumption, 52_LVBus920887_consumption, 52_LVBus920888_consumption, 52_LVBus920889_consumption, 52_LVBus920892_consumption, 52_LVBus920896_consumption, 52_LVBus920899_consumption, 52_LVBus920901_consumption, 52_LVBus920902_consumption, 52_LVBus920903_consumption, 52_LVBus920910_consumption, 52_LVBus920912_consumption, 52_LVBus920914_consumption, 52_LVBus920923_consumption, 52_LVBus920924_consumption, 52_LVBus920935_consumption, 52_LVBus920937_consumption, 52_LVBus920938_consumption, 52_LVBus920939_consumption, 52_LVBus920942_consumption, 52_LVBus920943_consumption, 52_LVBus920944_consumption, 52_LVBus920945_consumption, 52_LVBus920946_consumption, 52_LVBus920949_consumption, 52_LVBus920951_consumption, 52_LVBus920952_consumption, 52_LVBus920953_consumption, 52_LVBus920957_consumption, 52_LVBus920971_consumption, 52_LVBus920988_consumption, 52_LVBus920990_consumption, 52_LVBus920993_consumption, 52_LVBus921004_consumption, 52_LVBus921005_consumption, 52_LVBus921010_consumption, 52_LVBus921011_consumption, 52_LVBus921017_consumption, 52_LVBus921020_consumption, 52_LVBus921024_consumption, 52_LVBus921025_consumption, 52_LVBus921026_consumption, 52_LVBus921028_consumption, 52_LVBus921029_consumption, 52_LVBus921030_consumption, 52_LVBus921031_consumption, 52_LVBus921032_consumption, 52_LVBus921034_consumption, 52_LVBus921042_consumption, 52_LVBus921043_consumption, 52_LVBus921044_consumption, 52_LVBus921048_consumption, 52_LVBus921049_consumption, 52_LVBus921052_consumption, 52_LVBus921054_consumption, 52_LVBus921055_consumption, 52_LVBus921056_consumption, 52_LVBus921059_consumption, 52_LVBus921061_consumption, 52_LVBus921063_consumption, 52_LVBus921067_consumption, 52_LVBus921072_consumption, 52_LVBus921077_consumption, 52_LVBus921080_consumption, 52_LVBus921082_consumption, 52_LVBus921084_consumption, 52_LVBus921086_consumption, 52_LVBus921089_consumption, 52_LVBus921090_consumption, 52_LVBus921091_consumption, 52_LVBus921095_consumption, 52_LVBus921100_consumption, 52_LVBus921101_consumption, 52_LVBus921103_consumption, 52_LVBus921114_consumption, 52_LVBus921127_consumption, 52_LVBus921128_consumption, 52_LVBus921132_consumption, 52_LVBus921133_consumption, 52_LVBus921134_consumption, 52_LVBus921136_consumption, 52_LVBus921137_consumption, 52_LVBus921138_consumption, 52_LVBus921141_consumption, 52_LVBus921144_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  479 group(s) of loads (958 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  15 group(s) of series lines (30 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  616 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1179399_production, 52_LVBus1179400_production, 52_LVBus1179401_consumption, 52_LVBus1179401_production, 52_LVBus1179402_consumption, 52_LVBus1179402_production, 52_LVBus1179403_production, 52_LVBus1179404_production, 52_LVBus1179405_consumption, 52_LVBus1179405_production, 52_LVBus1180644_production, 52_LVBus1180647_production, 52_LVBus1180648_production, 52_LVBus1180649_production, 52_LVBus1180650_production, 52_LVBus1180651_consumption, 52_LVBus1180651_production, 52_LVBus1180652_production, 52_LVBus1180653_consumption, 52_LVBus1180653_production, 52_LVBus1189203_consumption, 52_LVBus1189203_production, 52_LVBus920547_production, 52_LVBus920549_production, 52_LVBus920551_production, 52_LVBus920553_consumption, 52_LVBus920553_production, 52_LVBus920554_production, 52_LVBus920556_consumption, 52_LVBus920556_production, 52_LVBus920557_production, 52_LVBus920558_consumption, 52_LVBus920558_production, 52_LVBus920559_production, 52_LVBus920560_production, 52_LVBus920561_consumption, 52_LVBus920561_production, 52_LVBus920562_consumption, 52_LVBus920562_production, 52_LVBus920563_consumption, 52_LVBus920563_production, 52_LVBus920564_production, 52_LVBus920565_production, 52_LVBus920569_production, 52_LVBus920570_production, 52_LVBus920572_production, 52_LVBus920573_production, 52_LVBus920574_consumption, 52_LVBus920574_production, 52_LVBus920575_production, 52_LVBus920577_production, 52_LVBus920579_consumption, 52_LVBus920579_production, 52_LVBus920581_consumption, 52_LVBus920581_production, 52_LVBus920582_production, 52_LVBus920583_production, 52_LVBus920587_consumption, 52_LVBus920587_production, 52_LVBus920588_consumption, 52_LVBus920588_production, 52_LVBus920590_consumption, 52_LVBus920590_production, 52_LVBus920593_consumption, 52_LVBus920593_production, 52_LVBus920595_production, 52_LVBus920596_production, 52_LVBus920597_production, 52_LVBus920600_production, 52_LVBus920602_consumption, 52_LVBus920602_production, 52_LVBus920603_production, 52_LVBus920604_production, 52_LVBus920605_production, 52_LVBus920606_consumption, 52_LVBus920606_production, 52_LVBus920607_production, 52_LVBus920608_production, 52_LVBus920609_production, 52_LVBus920610_production, 52_LVBus920611_production, 52_LVBus920615_consumption, 52_LVBus920615_production, 52_LVBus920616_production, 52_LVBus920617_production, 52_LVBus920618_production, 52_LVBus920619_production, 52_LVBus920620_production, 52_LVBus920621_production, 52_LVBus920623_consumption, 52_LVBus920623_production, 52_LVBus920625_production, 52_LVBus920626_production, 52_LVBus920627_production, 52_LVBus920628_production, 52_LVBus920629_production, 52_LVBus920631_production, 52_LVBus920632_production, 52_LVBus920633_production, 52_LVBus920648_production, 52_LVBus920649_production, 52_LVBus920650_consumption, 52_LVBus920650_production, 52_LVBus920652_production, 52_LVBus920653_production, 52_LVBus920654_production, 52_LVBus920655_production, 52_LVBus920656_production, 52_LVBus920658_consumption, 52_LVBus920658_production, 52_LVBus920659_consumption, 52_LVBus920659_production, 52_LVBus920660_consumption, 52_LVBus920660_production, 52_LVBus920661_consumption, 52_LVBus920661_production, 52_LVBus920662_production, 52_LVBus920663_consumption, 52_LVBus920663_production, 52_LVBus920665_production, 52_LVBus920666_consumption, 52_LVBus920666_production, 52_LVBus920668_production, 52_LVBus920669_production, 52_LVBus920670_production, 52_LVBus920672_production, 52_LVBus920673_consumption, 52_LVBus920673_production, 52_LVBus920676_production, 52_LVBus920677_production, 52_LVBus920678_production, 52_LVBus920679_production, 52_LVBus920680_production, 52_LVBus920681_production, 52_LVBus920682_production, 52_LVBus920684_production, 52_LVBus920686_consumption, 52_LVBus920686_production, 52_LVBus920688_production, 52_LVBus920690_consumption, 52_LVBus920690_production, 52_LVBus920691_production, 52_LVBus920693_production, 52_LVBus920695_production, 52_LVBus920696_production, 52_LVBus920697_consumption, 52_LVBus920697_production, 52_LVBus920698_production, 52_LVBus920699_production, 52_LVBus920700_production, 52_LVBus920701_production, 52_LVBus920702_production, 52_LVBus920704_production, 52_LVBus920705_production, 52_LVBus920706_production, 52_LVBus920707_production, 52_LVBus920709_consumption, 52_LVBus920709_production, 52_LVBus920710_production, 52_LVBus920711_production, 52_LVBus920712_production, 52_LVBus920714_production, 52_LVBus920715_production, 52_LVBus920716_production, 52_LVBus920718_production, 52_LVBus920719_production, 52_LVBus920720_production, 52_LVBus920721_production, 52_LVBus920722_production, 52_LVBus920724_production, 52_LVBus920725_consumption, 52_LVBus920725_production, 52_LVBus920726_consumption, 52_LVBus920726_production, 52_LVBus920727_production, 52_LVBus920728_consumption, 52_LVBus920728_production, 52_LVBus920729_production, 52_LVBus920731_consumption, 52_LVBus920731_production, 52_LVBus920733_consumption, 52_LVBus920733_production, 52_LVBus920734_production, 52_LVBus920735_consumption, 52_LVBus920735_production, 52_LVBus920736_production, 52_LVBus920738_production, 52_LVBus920739_consumption, 52_LVBus920739_production, 52_LVBus920740_production, 52_LVBus920741_production, 52_LVBus920742_consumption, 52_LVBus920742_production, 52_LVBus920743_consumption, 52_LVBus920743_production, 52_LVBus920744_production, 52_LVBus920746_consumption, 52_LVBus920746_production, 52_LVBus920747_consumption, 52_LVBus920747_production, 52_LVBus920748_production, 52_LVBus920749_production, 52_LVBus920750_consumption, 52_LVBus920750_production, 52_LVBus920751_consumption, 52_LVBus920751_production, 52_LVBus920752_production, 52_LVBus920753_production, 52_LVBus920755_consumption, 52_LVBus920755_production, 52_LVBus920756_consumption, 52_LVBus920756_production, 52_LVBus920757_consumption, 52_LVBus920757_production, 52_LVBus920758_consumption, 52_LVBus920758_production, 52_LVBus920759_production, 52_LVBus920760_consumption, 52_LVBus920760_production, 52_LVBus920761_production, 52_LVBus920763_production, 52_LVBus920765_production, 52_LVBus920766_consumption, 52_LVBus920766_production, 52_LVBus920768_production, 52_LVBus920769_production, 52_LVBus920775_production, 52_LVBus920776_consumption, 52_LVBus920776_production, 52_LVBus920777_production, 52_LVBus920778_production, 52_LVBus920780_consumption, 52_LVBus920780_production, 52_LVBus920781_production, 52_LVBus920782_production, 52_LVBus920783_consumption, 52_LVBus920783_production, 52_LVBus920784_production, 52_LVBus920789_consumption, 52_LVBus920789_production, 52_LVBus920790_production, 52_LVBus920791_production, 52_LVBus920793_consumption, 52_LVBus920793_production, 52_LVBus920794_consumption, 52_LVBus920794_production, 52_LVBus920795_consumption, 52_LVBus920795_production, 52_LVBus920796_consumption, 52_LVBus920796_production, 52_LVBus920798_production, 52_LVBus920799_production, 52_LVBus920800_production, 52_LVBus920802_consumption, 52_LVBus920802_production, 52_LVBus920803_production, 52_LVBus920805_production, 52_LVBus920807_consumption, 52_LVBus920807_production, 52_LVBus920808_production, 52_LVBus920809_production, 52_LVBus920813_production, 52_LVBus920814_production, 52_LVBus920815_consumption, 52_LVBus920815_production, 52_LVBus920816_production, 52_LVBus920818_production, 52_LVBus920819_production, 52_LVBus920820_production, 52_LVBus920821_production, 52_LVBus920822_production, 52_LVBus920823_production, 52_LVBus920824_consumption, 52_LVBus920824_production, 52_LVBus920825_production, 52_LVBus920826_production, 52_LVBus920827_production, 52_LVBus920829_production, 52_LVBus920830_production, 52_LVBus920831_production, 52_LVBus920833_consumption, 52_LVBus920833_production, 52_LVBus920834_production, 52_LVBus920835_production, 52_LVBus920836_production, 52_LVBus920837_production, 52_LVBus920838_production, 52_LVBus920839_production, 52_LVBus920841_production, 52_LVBus920842_production, 52_LVBus920843_production, 52_LVBus920844_production, 52_LVBus920845_production, 52_LVBus920846_production, 52_LVBus920847_production, 52_LVBus920849_production, 52_LVBus920850_production, 52_LVBus920851_production, 52_LVBus920852_production, 52_LVBus920853_production, 52_LVBus920854_production, 52_LVBus920856_consumption, 52_LVBus920856_production, 52_LVBus920857_production, 52_LVBus920858_production, 52_LVBus920859_production, 52_LVBus920860_production, 52_LVBus920864_consumption, 52_LVBus920864_production, 52_LVBus920865_production, 52_LVBus920866_production, 52_LVBus920867_consumption, 52_LVBus920867_production, 52_LVBus920868_production, 52_LVBus920869_production, 52_LVBus920870_production, 52_LVBus920874_production, 52_LVBus920876_consumption, 52_LVBus920876_production, 52_LVBus920878_consumption, 52_LVBus920878_production, 52_LVBus920879_production, 52_LVBus920880_production, 52_LVBus920882_consumption, 52_LVBus920882_production, 52_LVBus920883_production, 52_LVBus920884_production, 52_LVBus920885_production, 52_LVBus920886_production, 52_LVBus920887_production, 52_LVBus920888_production, 52_LVBus920889_production, 52_LVBus920890_production, 52_LVBus920891_production, 52_LVBus920892_production, 52_LVBus920893_production, 52_LVBus920894_production, 52_LVBus920896_production, 52_LVBus920897_production, 52_LVBus920898_production, 52_LVBus920899_production, 52_LVBus920901_production, 52_LVBus920902_production, 52_LVBus920903_production, 52_LVBus920905_consumption, 52_LVBus920905_production, 52_LVBus920907_consumption, 52_LVBus920907_production, 52_LVBus920908_consumption, 52_LVBus920908_production, 52_LVBus920909_production, 52_LVBus920910_production, 52_LVBus920911_consumption, 52_LVBus920911_production, 52_LVBus920912_production, 52_LVBus920913_production, 52_LVBus920914_production, 52_LVBus920918_consumption, 52_LVBus920918_production, 52_LVBus920920_production, 52_LVBus920922_consumption, 52_LVBus920922_production, 52_LVBus920923_production, 52_LVBus920924_production, 52_LVBus920928_production, 52_LVBus920930_consumption, 52_LVBus920930_production, 52_LVBus920931_production, 52_LVBus920932_consumption, 52_LVBus920932_production, 52_LVBus920934_consumption, 52_LVBus920934_production, 52_LVBus920935_production, 52_LVBus920936_consumption, 52_LVBus920936_production, 52_LVBus920937_production, 52_LVBus920938_production, 52_LVBus920939_production, 52_LVBus920940_consumption, 52_LVBus920940_production, 52_LVBus920942_production, 52_LVBus920943_production, 52_LVBus920944_production, 52_LVBus920945_production, 52_LVBus920946_production, 52_LVBus920947_production, 52_LVBus920948_production, 52_LVBus920949_production, 52_LVBus920951_production, 52_LVBus920952_production, 52_LVBus920953_production, 52_LVBus920955_production, 52_LVBus920956_consumption, 52_LVBus920956_production, 52_LVBus920957_production, 52_LVBus920959_production, 52_LVBus920960_production, 52_LVBus920963_consumption, 52_LVBus920963_production, 52_LVBus920965_consumption, 52_LVBus920965_production, 52_LVBus920967_production, 52_LVBus920968_production, 52_LVBus920969_consumption, 52_LVBus920969_production, 52_LVBus920970_consumption, 52_LVBus920970_production, 52_LVBus920971_production, 52_LVBus920972_consumption, 52_LVBus920972_production, 52_LVBus920973_consumption, 52_LVBus920973_production, 52_LVBus920974_production, 52_LVBus920975_consumption, 52_LVBus920975_production, 52_LVBus920976_production, 52_LVBus920978_consumption, 52_LVBus920978_production, 52_LVBus920979_production, 52_LVBus920980_consumption, 52_LVBus920980_production, 52_LVBus920981_consumption, 52_LVBus920981_production, 52_LVBus920983_consumption, 52_LVBus920983_production, 52_LVBus920984_production, 52_LVBus920986_production, 52_LVBus920988_production, 52_LVBus920989_production, 52_LVBus920990_production, 52_LVBus920991_production, 52_LVBus920992_production, 52_LVBus920993_production, 52_LVBus920995_production, 52_LVBus920996_production, 52_LVBus920997_consumption, 52_LVBus920997_production, 52_LVBus920998_production, 52_LVBus921000_consumption, 52_LVBus921000_production, 52_LVBus921001_production, 52_LVBus921002_production, 52_LVBus921004_production, 52_LVBus921005_production, 52_LVBus921006_production, 52_LVBus921007_production, 52_LVBus921008_production, 52_LVBus921009_production, 52_LVBus921010_production, 52_LVBus921011_production, 52_LVBus921012_consumption, 52_LVBus921012_production, 52_LVBus921013_consumption, 52_LVBus921013_production, 52_LVBus921014_consumption, 52_LVBus921014_production, 52_LVBus921016_production, 52_LVBus921017_production, 52_LVBus921019_production, 52_LVBus921020_production, 52_LVBus921021_production, 52_LVBus921022_production, 52_LVBus921024_production, 52_LVBus921025_production, 52_LVBus921026_production, 52_LVBus921027_consumption, 52_LVBus921027_production, 52_LVBus921028_production, 52_LVBus921029_production, 52_LVBus921030_production, 52_LVBus921031_production, 52_LVBus921032_production, 52_LVBus921033_production, 52_LVBus921034_production, 52_LVBus921036_consumption, 52_LVBus921036_production, 52_LVBus921037_consumption, 52_LVBus921037_production, 52_LVBus921038_production, 52_LVBus921039_production, 52_LVBus921040_consumption, 52_LVBus921040_production, 52_LVBus921041_production, 52_LVBus921042_production, 52_LVBus921043_production, 52_LVBus921044_production, 52_LVBus921046_production, 52_LVBus921047_production, 52_LVBus921048_production, 52_LVBus921049_production, 52_LVBus921051_production, 52_LVBus921052_production, 52_LVBus921053_consumption, 52_LVBus921053_production, 52_LVBus921054_production, 52_LVBus921055_production, 52_LVBus921056_production, 52_LVBus921058_consumption, 52_LVBus921058_production, 52_LVBus921059_production, 52_LVBus921060_production, 52_LVBus921061_production, 52_LVBus921062_production, 52_LVBus921063_production, 52_LVBus921065_consumption, 52_LVBus921065_production, 52_LVBus921066_production, 52_LVBus921067_production, 52_LVBus921068_production, 52_LVBus921069_production, 52_LVBus921070_production, 52_LVBus921072_production, 52_LVBus921073_production, 52_LVBus921074_production, 52_LVBus921075_production, 52_LVBus921076_consumption, 52_LVBus921076_production, 52_LVBus921077_production, 52_LVBus921079_production, 52_LVBus921080_production, 52_LVBus921081_production, 52_LVBus921082_production, 52_LVBus921083_production, 52_LVBus921084_production, 52_LVBus921086_production, 52_LVBus921087_production, 52_LVBus921088_consumption, 52_LVBus921088_production, 52_LVBus921089_production, 52_LVBus921090_production, 52_LVBus921091_production, 52_LVBus921092_production, 52_LVBus921093_production, 52_LVBus921094_production, 52_LVBus921095_production, 52_LVBus921096_production, 52_LVBus921097_consumption, 52_LVBus921097_production, 52_LVBus921099_production, 52_LVBus921100_production, 52_LVBus921101_production, 52_LVBus921102_production, 52_LVBus921103_production, 52_LVBus921104_production, 52_LVBus921105_consumption, 52_LVBus921105_production, 52_LVBus921106_consumption, 52_LVBus921106_production, 52_LVBus921107_consumption, 52_LVBus921107_production, 52_LVBus921108_production, 52_LVBus921109_production, 52_LVBus921110_consumption, 52_LVBus921110_production, 52_LVBus921111_consumption, 52_LVBus921111_production, 52_LVBus921112_production, 52_LVBus921113_production, 52_LVBus921114_production, 52_LVBus921116_production, 52_LVBus921118_consumption, 52_LVBus921118_production, 52_LVBus921119_consumption, 52_LVBus921119_production, 52_LVBus921120_consumption, 52_LVBus921120_production, 52_LVBus921122_consumption, 52_LVBus921122_production, 52_LVBus921123_production, 52_LVBus921124_consumption, 52_LVBus921124_production, 52_LVBus921126_consumption, 52_LVBus921126_production, 52_LVBus921127_production, 52_LVBus921128_production, 52_LVBus921129_consumption, 52_LVBus921129_production, 52_LVBus921130_consumption, 52_LVBus921130_production, 52_LVBus921131_consumption, 52_LVBus921131_production, 52_LVBus921132_production, 52_LVBus921133_production, 52_LVBus921134_production, 52_LVBus921135_consumption, 52_LVBus921135_production, 52_LVBus921136_production, 52_LVBus921137_production, 52_LVBus921138_production, 52_LVBus921140_production, 52_LVBus921141_production, 52_LVBus921143_production, 52_LVBus921144_production, 52_LVBus921146_production, 52_MVLV005214_consumption, 52_MVLV005214_production, 52_MVLV011325_consumption, 52_MVLV011325_production, 52_MVLV020300_consumption, 52_MVLV020300_production, 52_MVLV041618_consumption, 52_MVLV041618_production, 52_MVLV044793_consumption, 52_MVLV044793_production, 52_MVLV045130_consumption, 52_MVLV045130_production, 52_MVLV064945_consumption, 52_MVLV064945_production, 52_MVLV067068_consumption, 52_MVLV067068_production, 52_MVLV072977_consumption, 52_MVLV072977_production, 52_MVLV100172_consumption, 52_MVLV100172_production, 52_MVLV105210_consumption, 52_MVLV105210_production.

