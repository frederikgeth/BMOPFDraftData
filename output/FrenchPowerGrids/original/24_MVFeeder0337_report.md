# BMOPF Network Summary: 24_MVFeeder0337

**Generated:** 2026-10-01 23:33:58  
**Findings:** 0 errors · 5 warnings · 203 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 68 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 541 |  |
| line | 472 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 624 | 1.241 MW, 372.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 68 |  |
| switch | 0 |  |
| transformer | 68 | Dyn11×68 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 166 | 165 | 10 | 0 |
| LV_236V | 236.0 V | 375 | 307 | 614 | 0 |

**Transformer transitions:**

- `24_MVLV56235_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69947_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV70262_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV86768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV83286_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV67136_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV58223_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV86697_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV88451_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV90860_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV90522_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV04431_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV67137_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV67735_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV04927_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV12579_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV72916_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV04759_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV67728_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV88985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV09210_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV41034_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV72394_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV23940_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV80683_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV29259_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV45837_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV46271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69186_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV75035_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV23915_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV86713_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV07132_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV86054_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV90559_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV40814_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV04372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV21376_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV87406_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV51530_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV90651_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV70668_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV12207_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV23913_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV31264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV26056_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV78348_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV53138_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV83069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV46293_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV66064_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV89258_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV90197_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV09420_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV56879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36253_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV31280_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV67192_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV37665_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV56575_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV56541_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV24635_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV21731_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV48124_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV44594_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV76976_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV24900_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV19522_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 4 |
| Degree-1 buses | 160 |
| Tree depth (max hops) | 35 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 541 | 1 | 540 | 0 | 0 | 0 |
| Tier LV_236V | 375 | 68 | 307 | 0 | 0 | 0 |
| Tier MV_11.8kV | 166 | 1 | 165 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 68; skipped invalid branches: 0.

Galvanic zones: 69; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 24_C.LO5 | MV_11.8kV | 166 | 0 | 0 | 68 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1998 declared bus terminals; 1723 mapped line/closed-switch conductor edges; 275 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 19900.0 | 2.898 | 1872 |
| q_nom | 0.0 | 5980.0 | 2.898 | 1872 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.461 | 5240.0 | 1.942 | 472 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.407 | 68 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 423 of 624 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288353_consumption' has phase imbalance of 102.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288055_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843573_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288030_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288109_consumption' has phase imbalance of 203.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288091_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288173_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288378_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288237_consumption' has phase imbalance of 275.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288103_consumption' has phase imbalance of 182.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288417_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288308_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288278_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288391_consumption' has phase imbalance of 55.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288416_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288033_consumption' has phase imbalance of 23.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288073_consumption' has phase imbalance of 264.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288211_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288202_consumption' has phase imbalance of 121.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288396_consumption' has phase imbalance of 241.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288423_consumption' has phase imbalance of 211.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288243_consumption' has phase imbalance of 111.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288310_consumption' has phase imbalance of 283.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288159_consumption' has phase imbalance of 54.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288080_consumption' has phase imbalance of 237.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288075_consumption' has phase imbalance of 160.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843374_consumption' has phase imbalance of 224.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288437_consumption' has phase imbalance of 116.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288072_consumption' has phase imbalance of 258.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288379_consumption' has phase imbalance of 278.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288438_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288364_consumption' has phase imbalance of 205.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288066_consumption' has phase imbalance of 249.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288171_consumption' has phase imbalance of 79.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288441_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288394_consumption' has phase imbalance of 264.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288249_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843049_consumption' has phase imbalance of 256.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288077_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288368_consumption' has phase imbalance of 148.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288102_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288101_consumption' has phase imbalance of 281.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288232_consumption' has phase imbalance of 250.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288122_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288116_consumption' has phase imbalance of 150.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288366_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288309_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288392_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288311_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288389_consumption' has phase imbalance of 108.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288384_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288053_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288216_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288032_consumption' has phase imbalance of 289.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288299_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288119_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288126_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288229_consumption' has phase imbalance of 30.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288044_consumption' has phase imbalance of 213.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288402_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288084_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288264_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288287_consumption' has phase imbalance of 235.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288069_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288226_consumption' has phase imbalance of 243.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288415_consumption' has phase imbalance of 250.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288210_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843050_consumption' has phase imbalance of 220.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288194_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288035_consumption' has phase imbalance of 96.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288387_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288154_consumption' has phase imbalance of 269.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288057_consumption' has phase imbalance of 41.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288382_consumption' has phase imbalance of 233.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288361_consumption' has phase imbalance of 93.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288298_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288218_consumption' has phase imbalance of 286.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288190_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288172_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288076_consumption' has phase imbalance of 291.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288367_consumption' has phase imbalance of 216.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288219_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288137_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288124_consumption' has phase imbalance of 243.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288123_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843571_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288082_consumption' has phase imbalance of 26.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288435_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288105_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843574_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288339_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288393_consumption' has phase imbalance of 225.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288362_consumption' has phase imbalance of 266.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288381_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288388_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288316_consumption' has phase imbalance of 141.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288371_consumption' has phase imbalance of 198.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288117_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288142_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288322_consumption' has phase imbalance of 86.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288253_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288121_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288230_consumption' has phase imbalance of 242.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus288125_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 624 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus288341' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus288176' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus288163' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus288022' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus288430' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.241 MW |
| Total load Q | 372.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 24_MVLV56235_Transformer | 110.0 kVA | 6.6% |
| 24_MVLV69947_Transformer | 110.0 kVA | 9.6% |
| 24_MVLV70262_Transformer | 176.0 kVA | 8.1% |
| 24_MVLV86768_Transformer | 440.0 kVA | 31.5% |
| 24_MVLV83286_Transformer | 110.0 kVA | 1.3% |
| 24_MVLV67136_Transformer | 176.0 kVA | 7.4% |
| 24_MVLV58223_Transformer | 110.0 kVA | 11.1% |
| 24_MVLV86697_Transformer | 110.0 kVA | 10.2% |
| 24_MVLV88451_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV90860_Transformer | 176.0 kVA | 15.6% |
| 24_MVLV90522_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV04431_Transformer | 110.0 kVA | 12.0% |
| 24_MVLV67137_Transformer | 176.0 kVA | 4.9% |
| 24_MVLV67735_Transformer | 110.0 kVA | 2.1% |
| 24_MVLV04927_Transformer | 275.0 kVA | 7.6% |
| 24_MVLV12579_Transformer | 110.0 kVA | 0.0% |
| 24_MVLV72916_Transformer | 110.0 kVA | 9.9% |
| 24_MVLV04759_Transformer | 110.0 kVA | 2.4% |
| 24_MVLV67728_Transformer | 110.0 kVA | 10.6% |
| 24_MVLV88985_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV09210_Transformer | 110.0 kVA | 16.0% |
| 24_MVLV41034_Transformer | 176.0 kVA | 12.7% |
| 24_MVLV72394_Transformer | 176.0 kVA | 6.5% |
| 24_MVLV23940_Transformer | 275.0 kVA | 16.8% |
| 24_MVLV80683_Transformer | 110.0 kVA | 7.6% |
| 24_MVLV29259_Transformer | 110.0 kVA | 5.9% |
| 24_MVLV45837_Transformer | 275.0 kVA | 9.3% |
| 24_MVLV46271_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV69186_Transformer | 110.0 kVA | 9.4% |
| 24_MVLV75035_Transformer | 110.0 kVA | 2.1% |
| 24_MVLV23915_Transformer | 110.0 kVA | 8.3% |
| 24_MVLV86713_Transformer | 176.0 kVA | 29.9% |
| 24_MVLV07132_Transformer | 110.0 kVA | 6.1% |
| 24_MVLV86054_Transformer | 110.0 kVA | 5.6% |
| 24_MVLV90559_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV40814_Transformer | 110.0 kVA | 4.2% |
| 24_MVLV04372_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV21376_Transformer | 275.0 kVA | 30.9% |
| 24_MVLV87406_Transformer | 110.0 kVA | 14.7% |
| 24_MVLV51530_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV90651_Transformer | 110.0 kVA | 1.7% |
| 24_MVLV70668_Transformer | 176.0 kVA | 10.8% |
| 24_MVLV12207_Transformer | 176.0 kVA | 10.1% |
| 24_MVLV23913_Transformer | 176.0 kVA | 2.3% |
| 24_MVLV31264_Transformer | 176.0 kVA | 11.8% |
| 24_MVLV26056_Transformer | 110.0 kVA | 6.0% |
| 24_MVLV78348_Transformer | 275.0 kVA | 14.2% |
| 24_MVLV53138_Transformer | 176.0 kVA | 9.3% |
| 24_MVLV83069_Transformer | 110.0 kVA | 2.5% |
| 24_MVLV46293_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV66064_Transformer | 110.0 kVA | 0.8% |
| 24_MVLV89258_Transformer | 176.0 kVA | 15.7% |
| 24_MVLV90197_Transformer | 110.0 kVA | 15.8% |
| 24_MVLV09420_Transformer | 110.0 kVA | 2.1% |
| 24_MVLV56879_Transformer | 275.0 kVA | 21.6% |
| 24_MVLV36253_Transformer | 275.0 kVA | 33.5% |
| 24_MVLV31280_Transformer | 110.0 kVA | 8.2% |
| 24_MVLV67192_Transformer | 176.0 kVA | 13.1% |
| 24_MVLV37665_Transformer | 110.0 kVA | 9.7% |
| 24_MVLV56575_Transformer | 110.0 kVA | 12.2% |
| 24_MVLV56541_Transformer | 176.0 kVA | 14.2% |
| 24_MVLV24635_Transformer | 176.0 kVA | 8.7% |
| 24_MVLV21731_Transformer | 275.0 kVA | 19.3% |
| 24_MVLV48124_Transformer | 176.0 kVA | 14.2% |
| 24_MVLV44594_Transformer | 275.0 kVA | 16.6% |
| 24_MVLV76976_Transformer | 110.0 kVA | 8.5% |
| 24_MVLV24900_Transformer | 275.0 kVA | 33.6% |
| 24_MVLV19522_Transformer | 110.0 kVA | 7.1% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.24 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '24_C.LO5' (MV, 11.78 kV) has an electrical reach of 22.64 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus288412' (LV, 0.24 kV) has an electrical reach of 8.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus288176' (LV, 0.24 kV) has an electrical reach of 27.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus288426' (LV, 0.24 kV) has an electrical reach of 2.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus288182' (LV, 0.24 kV) has an electrical reach of 9.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus288428' (LV, 0.24 kV) has an electrical reach of 6.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus288430' (LV, 0.24 kV) has an electrical reach of 2.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 541 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 541 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 68 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 166 |
| LV_236V | 4-wire | 375 / 375 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 375 |
| Neutral branches | 307 |
| Grounding points | 68 |
| Neutral sections | 68 |
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
| 11.78 kV | 166 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 69 |
| Islands without voltage reference | 0 |
| Line impedance spread | 5830.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 375 / 166 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 424 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 424 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus288019_consumption, 24_LVBus288019_production, 24_LVBus288020_consumption, 24_LVBus288020_production, 24_LVBus288022_production, 24_LVBus288030_production, 24_LVBus288032_production, 24_LVBus288033_production, 24_LVBus288035_production, 24_LVBus288037_consumption, 24_LVBus288037_production, 24_LVBus288039_consumption, 24_LVBus288039_production, 24_LVBus288040_consumption, 24_LVBus288040_production, 24_LVBus288041_consumption, 24_LVBus288041_production, 24_LVBus288042_production, 24_LVBus288043_consumption, 24_LVBus288043_production, 24_LVBus288044_production, 24_LVBus288046_consumption, 24_LVBus288046_production, 24_LVBus288047_consumption, 24_LVBus288047_production, 24_LVBus288048_consumption, 24_LVBus288048_production, 24_LVBus288049_consumption, 24_LVBus288049_production, 24_LVBus288050_consumption, 24_LVBus288050_production, 24_LVBus288052_production, 24_LVBus288053_production, 24_LVBus288054_consumption, 24_LVBus288054_production, 24_LVBus288055_production, 24_LVBus288057_production, 24_LVBus288059_production, 24_LVBus288061_consumption, 24_LVBus288061_production, 24_LVBus288063_production, 24_LVBus288065_production, 24_LVBus288066_production, 24_LVBus288067_consumption, 24_LVBus288067_production, 24_LVBus288068_production, 24_LVBus288069_production, 24_LVBus288070_production, 24_LVBus288072_production, 24_LVBus288073_production, 24_LVBus288074_production, 24_LVBus288075_production, 24_LVBus288076_production, 24_LVBus288077_production, 24_LVBus288078_production, 24_LVBus288080_production, 24_LVBus288081_production, 24_LVBus288082_production, 24_LVBus288083_production, 24_LVBus288084_production, 24_LVBus288086_consumption, 24_LVBus288086_production, 24_LVBus288088_production, 24_LVBus288089_consumption, 24_LVBus288089_production, 24_LVBus288090_production, 24_LVBus288091_production, 24_LVBus288093_consumption, 24_LVBus288093_production, 24_LVBus288094_production, 24_LVBus288095_production, 24_LVBus288097_production, 24_LVBus288099_consumption, 24_LVBus288099_production, 24_LVBus288100_production, 24_LVBus288101_production, 24_LVBus288102_production, 24_LVBus288103_production, 24_LVBus288104_production, 24_LVBus288105_production, 24_LVBus288107_consumption, 24_LVBus288107_production, 24_LVBus288108_production, 24_LVBus288109_production, 24_LVBus288110_consumption, 24_LVBus288110_production, 24_LVBus288112_production, 24_LVBus288115_production, 24_LVBus288116_production, 24_LVBus288117_production, 24_LVBus288118_production, 24_LVBus288119_production, 24_LVBus288121_production, 24_LVBus288122_production, 24_LVBus288123_production, 24_LVBus288124_production, 24_LVBus288125_production, 24_LVBus288126_production, 24_LVBus288127_production, 24_LVBus288129_production, 24_LVBus288130_production, 24_LVBus288131_production, 24_LVBus288133_production, 24_LVBus288134_consumption, 24_LVBus288134_production, 24_LVBus288135_production, 24_LVBus288137_production, 24_LVBus288138_production, 24_LVBus288139_production, 24_LVBus288140_production, 24_LVBus288142_production, 24_LVBus288143_production, 24_LVBus288145_consumption, 24_LVBus288145_production, 24_LVBus288148_production, 24_LVBus288150_consumption, 24_LVBus288150_production, 24_LVBus288152_consumption, 24_LVBus288152_production, 24_LVBus288153_consumption, 24_LVBus288153_production, 24_LVBus288154_production, 24_LVBus288158_production, 24_LVBus288159_production, 24_LVBus288160_consumption, 24_LVBus288160_production, 24_LVBus288161_production, 24_LVBus288163_production, 24_LVBus288165_production, 24_LVBus288166_production, 24_LVBus288167_consumption, 24_LVBus288167_production, 24_LVBus288169_consumption, 24_LVBus288169_production, 24_LVBus288170_consumption, 24_LVBus288170_production, 24_LVBus288171_production, 24_LVBus288172_production, 24_LVBus288173_production, 24_LVBus288174_consumption, 24_LVBus288174_production, 24_LVBus288176_production, 24_LVBus288178_consumption, 24_LVBus288178_production, 24_LVBus288180_consumption, 24_LVBus288180_production, 24_LVBus288182_consumption, 24_LVBus288182_production, 24_LVBus288184_consumption, 24_LVBus288184_production, 24_LVBus288186_consumption, 24_LVBus288186_production, 24_LVBus288187_consumption, 24_LVBus288187_production, 24_LVBus288189_consumption, 24_LVBus288189_production, 24_LVBus288190_production, 24_LVBus288191_consumption, 24_LVBus288191_production, 24_LVBus288192_consumption, 24_LVBus288192_production, 24_LVBus288193_consumption, 24_LVBus288193_production, 24_LVBus288194_production, 24_LVBus288195_consumption, 24_LVBus288195_production, 24_LVBus288197_consumption, 24_LVBus288197_production, 24_LVBus288198_consumption, 24_LVBus288198_production, 24_LVBus288199_consumption, 24_LVBus288199_production, 24_LVBus288201_consumption, 24_LVBus288201_production, 24_LVBus288202_production, 24_LVBus288203_consumption, 24_LVBus288203_production, 24_LVBus288204_production, 24_LVBus288205_production, 24_LVBus288209_consumption, 24_LVBus288209_production, 24_LVBus288210_production, 24_LVBus288211_production, 24_LVBus288215_production, 24_LVBus288216_production, 24_LVBus288217_production, 24_LVBus288218_production, 24_LVBus288219_production, 24_LVBus288221_production, 24_LVBus288222_consumption, 24_LVBus288222_production, 24_LVBus288223_production, 24_LVBus288224_production, 24_LVBus288226_production, 24_LVBus288228_production, 24_LVBus288229_production, 24_LVBus288230_production, 24_LVBus288232_production, 24_LVBus288233_consumption, 24_LVBus288233_production, 24_LVBus288234_production, 24_LVBus288236_consumption, 24_LVBus288236_production, 24_LVBus288237_production, 24_LVBus288238_production, 24_LVBus288240_production, 24_LVBus288242_production, 24_LVBus288243_production, 24_LVBus288244_consumption, 24_LVBus288244_production, 24_LVBus288246_production, 24_LVBus288247_consumption, 24_LVBus288247_production, 24_LVBus288248_production, 24_LVBus288249_production, 24_LVBus288251_consumption, 24_LVBus288251_production, 24_LVBus288252_production, 24_LVBus288253_production, 24_LVBus288254_consumption, 24_LVBus288254_production, 24_LVBus288255_consumption, 24_LVBus288255_production, 24_LVBus288256_production, 24_LVBus288257_production, 24_LVBus288258_production, 24_LVBus288260_consumption, 24_LVBus288260_production, 24_LVBus288261_consumption, 24_LVBus288261_production, 24_LVBus288262_production, 24_LVBus288263_production, 24_LVBus288264_production, 24_LVBus288265_consumption, 24_LVBus288265_production, 24_LVBus288266_production, 24_LVBus288271_production, 24_LVBus288272_consumption, 24_LVBus288272_production, 24_LVBus288273_consumption, 24_LVBus288273_production, 24_LVBus288274_consumption, 24_LVBus288274_production, 24_LVBus288276_production, 24_LVBus288277_consumption, 24_LVBus288277_production, 24_LVBus288278_production, 24_LVBus288279_consumption, 24_LVBus288279_production, 24_LVBus288281_consumption, 24_LVBus288281_production, 24_LVBus288283_consumption, 24_LVBus288283_production, 24_LVBus288284_consumption, 24_LVBus288284_production, 24_LVBus288285_production, 24_LVBus288286_consumption, 24_LVBus288286_production, 24_LVBus288287_production, 24_LVBus288291_consumption, 24_LVBus288291_production, 24_LVBus288292_production, 24_LVBus288293_consumption, 24_LVBus288293_production, 24_LVBus288294_consumption, 24_LVBus288294_production, 24_LVBus288295_consumption, 24_LVBus288295_production, 24_LVBus288296_production, 24_LVBus288297_production, 24_LVBus288298_production, 24_LVBus288299_production, 24_LVBus288305_production, 24_LVBus288307_consumption, 24_LVBus288307_production, 24_LVBus288308_production, 24_LVBus288309_production, 24_LVBus288310_production, 24_LVBus288311_production, 24_LVBus288315_production, 24_LVBus288316_production, 24_LVBus288317_consumption, 24_LVBus288317_production, 24_LVBus288318_production, 24_LVBus288320_consumption, 24_LVBus288320_production, 24_LVBus288322_production, 24_LVBus288324_production, 24_LVBus288325_consumption, 24_LVBus288325_production, 24_LVBus288326_production, 24_LVBus288327_consumption, 24_LVBus288327_production, 24_LVBus288328_consumption, 24_LVBus288328_production, 24_LVBus288329_consumption, 24_LVBus288329_production, 24_LVBus288330_production, 24_LVBus288331_production, 24_LVBus288333_production, 24_LVBus288334_production, 24_LVBus288336_consumption, 24_LVBus288336_production, 24_LVBus288337_consumption, 24_LVBus288337_production, 24_LVBus288338_production, 24_LVBus288339_production, 24_LVBus288341_production, 24_LVBus288343_production, 24_LVBus288351_consumption, 24_LVBus288351_production, 24_LVBus288352_production, 24_LVBus288353_production, 24_LVBus288355_production, 24_LVBus288357_consumption, 24_LVBus288357_production, 24_LVBus288358_production, 24_LVBus288360_consumption, 24_LVBus288360_production, 24_LVBus288361_production, 24_LVBus288362_production, 24_LVBus288364_production, 24_LVBus288365_consumption, 24_LVBus288365_production, 24_LVBus288366_production, 24_LVBus288367_production, 24_LVBus288368_production, 24_LVBus288369_consumption, 24_LVBus288369_production, 24_LVBus288370_consumption, 24_LVBus288370_production, 24_LVBus288371_production, 24_LVBus288372_production, 24_LVBus288377_consumption, 24_LVBus288377_production, 24_LVBus288378_production, 24_LVBus288379_production, 24_LVBus288380_consumption, 24_LVBus288380_production, 24_LVBus288381_production, 24_LVBus288382_production, 24_LVBus288384_production, 24_LVBus288385_consumption, 24_LVBus288385_production, 24_LVBus288386_production, 24_LVBus288387_production, 24_LVBus288388_production, 24_LVBus288389_production, 24_LVBus288390_production, 24_LVBus288391_production, 24_LVBus288392_production, 24_LVBus288393_production, 24_LVBus288394_production, 24_LVBus288395_production, 24_LVBus288396_production, 24_LVBus288401_production, 24_LVBus288402_production, 24_LVBus288403_production, 24_LVBus288404_production, 24_LVBus288408_consumption, 24_LVBus288408_production, 24_LVBus288410_consumption, 24_LVBus288410_production, 24_LVBus288412_consumption, 24_LVBus288412_production, 24_LVBus288414_consumption, 24_LVBus288414_production, 24_LVBus288415_production, 24_LVBus288416_production, 24_LVBus288417_production, 24_LVBus288418_consumption, 24_LVBus288418_production, 24_LVBus288422_consumption, 24_LVBus288422_production, 24_LVBus288423_production, 24_LVBus288424_production, 24_LVBus288426_consumption, 24_LVBus288426_production, 24_LVBus288428_consumption, 24_LVBus288428_production, 24_LVBus288430_production, 24_LVBus288432_consumption, 24_LVBus288432_production, 24_LVBus288433_consumption, 24_LVBus288433_production, 24_LVBus288434_consumption, 24_LVBus288434_production, 24_LVBus288435_production, 24_LVBus288436_production, 24_LVBus288437_production, 24_LVBus288438_production, 24_LVBus288439_consumption, 24_LVBus288439_production, 24_LVBus288440_consumption, 24_LVBus288440_production, 24_LVBus288441_production, 24_LVBus288442_consumption, 24_LVBus288442_production, 24_LVBus288443_consumption, 24_LVBus288443_production, 24_LVBus843049_production, 24_LVBus843050_production, 24_LVBus843051_production, 24_LVBus843177_consumption, 24_LVBus843177_production, 24_LVBus843178_production, 24_LVBus843179_production, 24_LVBus843180_consumption, 24_LVBus843180_production, 24_LVBus843374_production, 24_LVBus843571_production, 24_LVBus843572_production, 24_LVBus843573_production, 24_LVBus843574_production, 24_MVLV03062_consumption, 24_MVLV03062_production, 24_MVLV10543_consumption, 24_MVLV10543_production, 24_MVLV53515_consumption, 24_MVLV53515_production, 24_MVLV61115_consumption, 24_MVLV61115_production, 24_MVLV86066_consumption, 24_MVLV86066_production.

## 9. Data Quality Summary

**Total findings:** 208 (0 errors, 5 warnings, 203 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  423 of 624 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.24 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  424 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288353_consumption`  
  Load '24_LVBus288353_consumption' has phase imbalance of 102.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288055_consumption`  
  Load '24_LVBus288055_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288074_consumption`  
  Load '24_LVBus288074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843573_consumption`  
  Load '24_LVBus843573_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288030_consumption`  
  Load '24_LVBus288030_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288109_consumption`  
  Load '24_LVBus288109_consumption' has phase imbalance of 203.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288130_consumption`  
  Load '24_LVBus288130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288324_consumption`  
  Load '24_LVBus288324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288065_consumption`  
  Load '24_LVBus288065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288091_consumption`  
  Load '24_LVBus288091_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288240_consumption`  
  Load '24_LVBus288240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288318_consumption`  
  Load '24_LVBus288318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288276_consumption`  
  Load '24_LVBus288276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288173_consumption`  
  Load '24_LVBus288173_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288223_consumption`  
  Load '24_LVBus288223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288148_consumption`  
  Load '24_LVBus288148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288378_consumption`  
  Load '24_LVBus288378_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288237_consumption`  
  Load '24_LVBus288237_consumption' has phase imbalance of 275.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288228_consumption`  
  Load '24_LVBus288228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288103_consumption`  
  Load '24_LVBus288103_consumption' has phase imbalance of 182.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288417_consumption`  
  Load '24_LVBus288417_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288308_consumption`  
  Load '24_LVBus288308_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288278_consumption`  
  Load '24_LVBus288278_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288391_consumption`  
  Load '24_LVBus288391_consumption' has phase imbalance of 55.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288416_consumption`  
  Load '24_LVBus288416_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288033_consumption`  
  Load '24_LVBus288033_consumption' has phase imbalance of 23.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288073_consumption`  
  Load '24_LVBus288073_consumption' has phase imbalance of 264.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288042_consumption`  
  Load '24_LVBus288042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288165_consumption`  
  Load '24_LVBus288165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288257_consumption`  
  Load '24_LVBus288257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288211_consumption`  
  Load '24_LVBus288211_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288202_consumption`  
  Load '24_LVBus288202_consumption' has phase imbalance of 121.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288118_consumption`  
  Load '24_LVBus288118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288052_consumption`  
  Load '24_LVBus288052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288252_consumption`  
  Load '24_LVBus288252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288396_consumption`  
  Load '24_LVBus288396_consumption' has phase imbalance of 241.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288423_consumption`  
  Load '24_LVBus288423_consumption' has phase imbalance of 211.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288424_consumption`  
  Load '24_LVBus288424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288436_consumption`  
  Load '24_LVBus288436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288243_consumption`  
  Load '24_LVBus288243_consumption' has phase imbalance of 111.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288297_consumption`  
  Load '24_LVBus288297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288090_consumption`  
  Load '24_LVBus288090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288310_consumption`  
  Load '24_LVBus288310_consumption' has phase imbalance of 283.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288331_consumption`  
  Load '24_LVBus288331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288159_consumption`  
  Load '24_LVBus288159_consumption' has phase imbalance of 54.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288080_consumption`  
  Load '24_LVBus288080_consumption' has phase imbalance of 237.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288075_consumption`  
  Load '24_LVBus288075_consumption' has phase imbalance of 160.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843374_consumption`  
  Load '24_LVBus843374_consumption' has phase imbalance of 224.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288131_consumption`  
  Load '24_LVBus288131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288395_consumption`  
  Load '24_LVBus288395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288437_consumption`  
  Load '24_LVBus288437_consumption' has phase imbalance of 116.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288129_consumption`  
  Load '24_LVBus288129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288072_consumption`  
  Load '24_LVBus288072_consumption' has phase imbalance of 258.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288143_consumption`  
  Load '24_LVBus288143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288266_consumption`  
  Load '24_LVBus288266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288379_consumption`  
  Load '24_LVBus288379_consumption' has phase imbalance of 278.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288438_consumption`  
  Load '24_LVBus288438_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288364_consumption`  
  Load '24_LVBus288364_consumption' has phase imbalance of 205.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288066_consumption`  
  Load '24_LVBus288066_consumption' has phase imbalance of 249.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288171_consumption`  
  Load '24_LVBus288171_consumption' has phase imbalance of 79.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288140_consumption`  
  Load '24_LVBus288140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288441_consumption`  
  Load '24_LVBus288441_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288390_consumption`  
  Load '24_LVBus288390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288394_consumption`  
  Load '24_LVBus288394_consumption' has phase imbalance of 264.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843572_consumption`  
  Load '24_LVBus843572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288249_consumption`  
  Load '24_LVBus288249_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843049_consumption`  
  Load '24_LVBus843049_consumption' has phase imbalance of 256.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288077_consumption`  
  Load '24_LVBus288077_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288285_consumption`  
  Load '24_LVBus288285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288205_consumption`  
  Load '24_LVBus288205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288368_consumption`  
  Load '24_LVBus288368_consumption' has phase imbalance of 148.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288102_consumption`  
  Load '24_LVBus288102_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288101_consumption`  
  Load '24_LVBus288101_consumption' has phase imbalance of 281.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288232_consumption`  
  Load '24_LVBus288232_consumption' has phase imbalance of 250.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288122_consumption`  
  Load '24_LVBus288122_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288116_consumption`  
  Load '24_LVBus288116_consumption' has phase imbalance of 150.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288204_consumption`  
  Load '24_LVBus288204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288161_consumption`  
  Load '24_LVBus288161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288271_consumption`  
  Load '24_LVBus288271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288292_consumption`  
  Load '24_LVBus288292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288330_consumption`  
  Load '24_LVBus288330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288366_consumption`  
  Load '24_LVBus288366_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288309_consumption`  
  Load '24_LVBus288309_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288392_consumption`  
  Load '24_LVBus288392_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288224_consumption`  
  Load '24_LVBus288224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843051_consumption`  
  Load '24_LVBus843051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288311_consumption`  
  Load '24_LVBus288311_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288389_consumption`  
  Load '24_LVBus288389_consumption' has phase imbalance of 108.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288384_consumption`  
  Load '24_LVBus288384_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288334_consumption`  
  Load '24_LVBus288334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288053_consumption`  
  Load '24_LVBus288053_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288139_consumption`  
  Load '24_LVBus288139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288216_consumption`  
  Load '24_LVBus288216_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288032_consumption`  
  Load '24_LVBus288032_consumption' has phase imbalance of 289.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288299_consumption`  
  Load '24_LVBus288299_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288119_consumption`  
  Load '24_LVBus288119_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288404_consumption`  
  Load '24_LVBus288404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288126_consumption`  
  Load '24_LVBus288126_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288229_consumption`  
  Load '24_LVBus288229_consumption' has phase imbalance of 30.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288248_consumption`  
  Load '24_LVBus288248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288044_consumption`  
  Load '24_LVBus288044_consumption' has phase imbalance of 213.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288094_consumption`  
  Load '24_LVBus288094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288234_consumption`  
  Load '24_LVBus288234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288068_consumption`  
  Load '24_LVBus288068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288097_consumption`  
  Load '24_LVBus288097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288402_consumption`  
  Load '24_LVBus288402_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288138_consumption`  
  Load '24_LVBus288138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288084_consumption`  
  Load '24_LVBus288084_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288104_consumption`  
  Load '24_LVBus288104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288258_consumption`  
  Load '24_LVBus288258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288264_consumption`  
  Load '24_LVBus288264_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288287_consumption`  
  Load '24_LVBus288287_consumption' has phase imbalance of 235.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288088_consumption`  
  Load '24_LVBus288088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288069_consumption`  
  Load '24_LVBus288069_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288226_consumption`  
  Load '24_LVBus288226_consumption' has phase imbalance of 243.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288415_consumption`  
  Load '24_LVBus288415_consumption' has phase imbalance of 250.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288135_consumption`  
  Load '24_LVBus288135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288210_consumption`  
  Load '24_LVBus288210_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288263_consumption`  
  Load '24_LVBus288263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843050_consumption`  
  Load '24_LVBus843050_consumption' has phase imbalance of 220.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288386_consumption`  
  Load '24_LVBus288386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288194_consumption`  
  Load '24_LVBus288194_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288403_consumption`  
  Load '24_LVBus288403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288133_consumption`  
  Load '24_LVBus288133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288035_consumption`  
  Load '24_LVBus288035_consumption' has phase imbalance of 96.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288387_consumption`  
  Load '24_LVBus288387_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288154_consumption`  
  Load '24_LVBus288154_consumption' has phase imbalance of 269.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288057_consumption`  
  Load '24_LVBus288057_consumption' has phase imbalance of 41.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288221_consumption`  
  Load '24_LVBus288221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288326_consumption`  
  Load '24_LVBus288326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288246_consumption`  
  Load '24_LVBus288246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288382_consumption`  
  Load '24_LVBus288382_consumption' has phase imbalance of 233.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288361_consumption`  
  Load '24_LVBus288361_consumption' has phase imbalance of 93.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288298_consumption`  
  Load '24_LVBus288298_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843179_consumption`  
  Load '24_LVBus843179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288256_consumption`  
  Load '24_LVBus288256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288355_consumption`  
  Load '24_LVBus288355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288218_consumption`  
  Load '24_LVBus288218_consumption' has phase imbalance of 286.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288262_consumption`  
  Load '24_LVBus288262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288190_consumption`  
  Load '24_LVBus288190_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288172_consumption`  
  Load '24_LVBus288172_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288076_consumption`  
  Load '24_LVBus288076_consumption' has phase imbalance of 291.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288367_consumption`  
  Load '24_LVBus288367_consumption' has phase imbalance of 216.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288219_consumption`  
  Load '24_LVBus288219_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288137_consumption`  
  Load '24_LVBus288137_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288124_consumption`  
  Load '24_LVBus288124_consumption' has phase imbalance of 243.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288123_consumption`  
  Load '24_LVBus288123_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288127_consumption`  
  Load '24_LVBus288127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843571_consumption`  
  Load '24_LVBus843571_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288082_consumption`  
  Load '24_LVBus288082_consumption' has phase imbalance of 26.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288435_consumption`  
  Load '24_LVBus288435_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288081_consumption`  
  Load '24_LVBus288081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288358_consumption`  
  Load '24_LVBus288358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288105_consumption`  
  Load '24_LVBus288105_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843574_consumption`  
  Load '24_LVBus843574_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843178_consumption`  
  Load '24_LVBus843178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288095_consumption`  
  Load '24_LVBus288095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288296_consumption`  
  Load '24_LVBus288296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288339_consumption`  
  Load '24_LVBus288339_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288393_consumption`  
  Load '24_LVBus288393_consumption' has phase imbalance of 225.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288372_consumption`  
  Load '24_LVBus288372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288362_consumption`  
  Load '24_LVBus288362_consumption' has phase imbalance of 266.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288381_consumption`  
  Load '24_LVBus288381_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288401_consumption`  
  Load '24_LVBus288401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288388_consumption`  
  Load '24_LVBus288388_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288316_consumption`  
  Load '24_LVBus288316_consumption' has phase imbalance of 141.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288371_consumption`  
  Load '24_LVBus288371_consumption' has phase imbalance of 198.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288117_consumption`  
  Load '24_LVBus288117_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288142_consumption`  
  Load '24_LVBus288142_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288322_consumption`  
  Load '24_LVBus288322_consumption' has phase imbalance of 86.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288063_consumption`  
  Load '24_LVBus288063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288253_consumption`  
  Load '24_LVBus288253_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288121_consumption`  
  Load '24_LVBus288121_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288230_consumption`  
  Load '24_LVBus288230_consumption' has phase imbalance of 242.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus288125_consumption`  
  Load '24_LVBus288125_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 624 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus288341' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus288176' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus288163' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus288022' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus288430' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '24_C.LO5' (MV, 11.78 kV) has an electrical reach of 22.64 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus288412' (LV, 0.24 kV) has an electrical reach of 8.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus288176' (LV, 0.24 kV) has an electrical reach of 27.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus288426' (LV, 0.24 kV) has an electrical reach of 2.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus288182' (LV, 0.24 kV) has an electrical reach of 9.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus288428' (LV, 0.24 kV) has an electrical reach of 6.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus288430' (LV, 0.24 kV) has an electrical reach of 2.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  541 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '24_26439' and '24_8006' at bus '24_MVBus10936' have ||Z||_F ratio 1330.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  135 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 24_LVBus288032_consumption, 24_LVBus288042_consumption, 24_LVBus288052_consumption, 24_LVBus288053_consumption, 24_LVBus288055_consumption, 24_LVBus288063_consumption, 24_LVBus288065_consumption, 24_LVBus288068_consumption, 24_LVBus288069_consumption, 24_LVBus288072_consumption, 24_LVBus288073_consumption, 24_LVBus288074_consumption, 24_LVBus288076_consumption, 24_LVBus288077_consumption, 24_LVBus288080_consumption, 24_LVBus288081_consumption, 24_LVBus288088_consumption, 24_LVBus288090_consumption, 24_LVBus288094_consumption, 24_LVBus288095_consumption, 24_LVBus288097_consumption, 24_LVBus288104_consumption, 24_LVBus288105_consumption, 24_LVBus288117_consumption, 24_LVBus288118_consumption, 24_LVBus288119_consumption, 24_LVBus288121_consumption, 24_LVBus288122_consumption, 24_LVBus288124_consumption, 24_LVBus288125_consumption, 24_LVBus288126_consumption, 24_LVBus288127_consumption, 24_LVBus288129_consumption, 24_LVBus288130_consumption, 24_LVBus288131_consumption, 24_LVBus288133_consumption, 24_LVBus288135_consumption, 24_LVBus288138_consumption, 24_LVBus288139_consumption, 24_LVBus288140_consumption, 24_LVBus288142_consumption, 24_LVBus288143_consumption, 24_LVBus288148_consumption, 24_LVBus288161_consumption, 24_LVBus288165_consumption, 24_LVBus288172_consumption, 24_LVBus288194_consumption, 24_LVBus288204_consumption, 24_LVBus288205_consumption, 24_LVBus288210_consumption, 24_LVBus288216_consumption, 24_LVBus288218_consumption, 24_LVBus288221_consumption, 24_LVBus288223_consumption, 24_LVBus288224_consumption, 24_LVBus288226_consumption, 24_LVBus288228_consumption, 24_LVBus288230_consumption, 24_LVBus288232_consumption, 24_LVBus288234_consumption, 24_LVBus288237_consumption, 24_LVBus288240_consumption, 24_LVBus288246_consumption, 24_LVBus288248_consumption, 24_LVBus288249_consumption, 24_LVBus288252_consumption, 24_LVBus288253_consumption, 24_LVBus288256_consumption, 24_LVBus288257_consumption, 24_LVBus288258_consumption, 24_LVBus288262_consumption, 24_LVBus288263_consumption, 24_LVBus288264_consumption, 24_LVBus288266_consumption, 24_LVBus288271_consumption, 24_LVBus288276_consumption, 24_LVBus288278_consumption, 24_LVBus288285_consumption, 24_LVBus288287_consumption, 24_LVBus288292_consumption, 24_LVBus288296_consumption, 24_LVBus288297_consumption, 24_LVBus288299_consumption, 24_LVBus288308_consumption, 24_LVBus288309_consumption, 24_LVBus288310_consumption, 24_LVBus288311_consumption, 24_LVBus288318_consumption, 24_LVBus288324_consumption, 24_LVBus288326_consumption, 24_LVBus288330_consumption, 24_LVBus288331_consumption, 24_LVBus288334_consumption, 24_LVBus288339_consumption, 24_LVBus288355_consumption, 24_LVBus288358_consumption, 24_LVBus288362_consumption, 24_LVBus288364_consumption, 24_LVBus288366_consumption, 24_LVBus288367_consumption, 24_LVBus288371_consumption, 24_LVBus288372_consumption, 24_LVBus288378_consumption, 24_LVBus288379_consumption, 24_LVBus288381_consumption, 24_LVBus288382_consumption, 24_LVBus288384_consumption, 24_LVBus288386_consumption, 24_LVBus288390_consumption, 24_LVBus288392_consumption, 24_LVBus288393_consumption, 24_LVBus288394_consumption, 24_LVBus288395_consumption, 24_LVBus288396_consumption, 24_LVBus288401_consumption, 24_LVBus288402_consumption, 24_LVBus288403_consumption, 24_LVBus288404_consumption, 24_LVBus288415_consumption, 24_LVBus288416_consumption, 24_LVBus288417_consumption, 24_LVBus288423_consumption, 24_LVBus288424_consumption, 24_LVBus288435_consumption, 24_LVBus288436_consumption, 24_LVBus288438_consumption, 24_LVBus288441_consumption, 24_LVBus843049_consumption, 24_LVBus843050_consumption, 24_LVBus843051_consumption, 24_LVBus843178_consumption, 24_LVBus843179_consumption, 24_LVBus843374_consumption, 24_LVBus843572_consumption, 24_LVBus843573_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  312 group(s) of loads (624 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  21 group(s) of series lines (45 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  424 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus288019_consumption, 24_LVBus288019_production, 24_LVBus288020_consumption, 24_LVBus288020_production, 24_LVBus288022_production, 24_LVBus288030_production, 24_LVBus288032_production, 24_LVBus288033_production, 24_LVBus288035_production, 24_LVBus288037_consumption, 24_LVBus288037_production, 24_LVBus288039_consumption, 24_LVBus288039_production, 24_LVBus288040_consumption, 24_LVBus288040_production, 24_LVBus288041_consumption, 24_LVBus288041_production, 24_LVBus288042_production, 24_LVBus288043_consumption, 24_LVBus288043_production, 24_LVBus288044_production, 24_LVBus288046_consumption, 24_LVBus288046_production, 24_LVBus288047_consumption, 24_LVBus288047_production, 24_LVBus288048_consumption, 24_LVBus288048_production, 24_LVBus288049_consumption, 24_LVBus288049_production, 24_LVBus288050_consumption, 24_LVBus288050_production, 24_LVBus288052_production, 24_LVBus288053_production, 24_LVBus288054_consumption, 24_LVBus288054_production, 24_LVBus288055_production, 24_LVBus288057_production, 24_LVBus288059_production, 24_LVBus288061_consumption, 24_LVBus288061_production, 24_LVBus288063_production, 24_LVBus288065_production, 24_LVBus288066_production, 24_LVBus288067_consumption, 24_LVBus288067_production, 24_LVBus288068_production, 24_LVBus288069_production, 24_LVBus288070_production, 24_LVBus288072_production, 24_LVBus288073_production, 24_LVBus288074_production, 24_LVBus288075_production, 24_LVBus288076_production, 24_LVBus288077_production, 24_LVBus288078_production, 24_LVBus288080_production, 24_LVBus288081_production, 24_LVBus288082_production, 24_LVBus288083_production, 24_LVBus288084_production, 24_LVBus288086_consumption, 24_LVBus288086_production, 24_LVBus288088_production, 24_LVBus288089_consumption, 24_LVBus288089_production, 24_LVBus288090_production, 24_LVBus288091_production, 24_LVBus288093_consumption, 24_LVBus288093_production, 24_LVBus288094_production, 24_LVBus288095_production, 24_LVBus288097_production, 24_LVBus288099_consumption, 24_LVBus288099_production, 24_LVBus288100_production, 24_LVBus288101_production, 24_LVBus288102_production, 24_LVBus288103_production, 24_LVBus288104_production, 24_LVBus288105_production, 24_LVBus288107_consumption, 24_LVBus288107_production, 24_LVBus288108_production, 24_LVBus288109_production, 24_LVBus288110_consumption, 24_LVBus288110_production, 24_LVBus288112_production, 24_LVBus288115_production, 24_LVBus288116_production, 24_LVBus288117_production, 24_LVBus288118_production, 24_LVBus288119_production, 24_LVBus288121_production, 24_LVBus288122_production, 24_LVBus288123_production, 24_LVBus288124_production, 24_LVBus288125_production, 24_LVBus288126_production, 24_LVBus288127_production, 24_LVBus288129_production, 24_LVBus288130_production, 24_LVBus288131_production, 24_LVBus288133_production, 24_LVBus288134_consumption, 24_LVBus288134_production, 24_LVBus288135_production, 24_LVBus288137_production, 24_LVBus288138_production, 24_LVBus288139_production, 24_LVBus288140_production, 24_LVBus288142_production, 24_LVBus288143_production, 24_LVBus288145_consumption, 24_LVBus288145_production, 24_LVBus288148_production, 24_LVBus288150_consumption, 24_LVBus288150_production, 24_LVBus288152_consumption, 24_LVBus288152_production, 24_LVBus288153_consumption, 24_LVBus288153_production, 24_LVBus288154_production, 24_LVBus288158_production, 24_LVBus288159_production, 24_LVBus288160_consumption, 24_LVBus288160_production, 24_LVBus288161_production, 24_LVBus288163_production, 24_LVBus288165_production, 24_LVBus288166_production, 24_LVBus288167_consumption, 24_LVBus288167_production, 24_LVBus288169_consumption, 24_LVBus288169_production, 24_LVBus288170_consumption, 24_LVBus288170_production, 24_LVBus288171_production, 24_LVBus288172_production, 24_LVBus288173_production, 24_LVBus288174_consumption, 24_LVBus288174_production, 24_LVBus288176_production, 24_LVBus288178_consumption, 24_LVBus288178_production, 24_LVBus288180_consumption, 24_LVBus288180_production, 24_LVBus288182_consumption, 24_LVBus288182_production, 24_LVBus288184_consumption, 24_LVBus288184_production, 24_LVBus288186_consumption, 24_LVBus288186_production, 24_LVBus288187_consumption, 24_LVBus288187_production, 24_LVBus288189_consumption, 24_LVBus288189_production, 24_LVBus288190_production, 24_LVBus288191_consumption, 24_LVBus288191_production, 24_LVBus288192_consumption, 24_LVBus288192_production, 24_LVBus288193_consumption, 24_LVBus288193_production, 24_LVBus288194_production, 24_LVBus288195_consumption, 24_LVBus288195_production, 24_LVBus288197_consumption, 24_LVBus288197_production, 24_LVBus288198_consumption, 24_LVBus288198_production, 24_LVBus288199_consumption, 24_LVBus288199_production, 24_LVBus288201_consumption, 24_LVBus288201_production, 24_LVBus288202_production, 24_LVBus288203_consumption, 24_LVBus288203_production, 24_LVBus288204_production, 24_LVBus288205_production, 24_LVBus288209_consumption, 24_LVBus288209_production, 24_LVBus288210_production, 24_LVBus288211_production, 24_LVBus288215_production, 24_LVBus288216_production, 24_LVBus288217_production, 24_LVBus288218_production, 24_LVBus288219_production, 24_LVBus288221_production, 24_LVBus288222_consumption, 24_LVBus288222_production, 24_LVBus288223_production, 24_LVBus288224_production, 24_LVBus288226_production, 24_LVBus288228_production, 24_LVBus288229_production, 24_LVBus288230_production, 24_LVBus288232_production, 24_LVBus288233_consumption, 24_LVBus288233_production, 24_LVBus288234_production, 24_LVBus288236_consumption, 24_LVBus288236_production, 24_LVBus288237_production, 24_LVBus288238_production, 24_LVBus288240_production, 24_LVBus288242_production, 24_LVBus288243_production, 24_LVBus288244_consumption, 24_LVBus288244_production, 24_LVBus288246_production, 24_LVBus288247_consumption, 24_LVBus288247_production, 24_LVBus288248_production, 24_LVBus288249_production, 24_LVBus288251_consumption, 24_LVBus288251_production, 24_LVBus288252_production, 24_LVBus288253_production, 24_LVBus288254_consumption, 24_LVBus288254_production, 24_LVBus288255_consumption, 24_LVBus288255_production, 24_LVBus288256_production, 24_LVBus288257_production, 24_LVBus288258_production, 24_LVBus288260_consumption, 24_LVBus288260_production, 24_LVBus288261_consumption, 24_LVBus288261_production, 24_LVBus288262_production, 24_LVBus288263_production, 24_LVBus288264_production, 24_LVBus288265_consumption, 24_LVBus288265_production, 24_LVBus288266_production, 24_LVBus288271_production, 24_LVBus288272_consumption, 24_LVBus288272_production, 24_LVBus288273_consumption, 24_LVBus288273_production, 24_LVBus288274_consumption, 24_LVBus288274_production, 24_LVBus288276_production, 24_LVBus288277_consumption, 24_LVBus288277_production, 24_LVBus288278_production, 24_LVBus288279_consumption, 24_LVBus288279_production, 24_LVBus288281_consumption, 24_LVBus288281_production, 24_LVBus288283_consumption, 24_LVBus288283_production, 24_LVBus288284_consumption, 24_LVBus288284_production, 24_LVBus288285_production, 24_LVBus288286_consumption, 24_LVBus288286_production, 24_LVBus288287_production, 24_LVBus288291_consumption, 24_LVBus288291_production, 24_LVBus288292_production, 24_LVBus288293_consumption, 24_LVBus288293_production, 24_LVBus288294_consumption, 24_LVBus288294_production, 24_LVBus288295_consumption, 24_LVBus288295_production, 24_LVBus288296_production, 24_LVBus288297_production, 24_LVBus288298_production, 24_LVBus288299_production, 24_LVBus288305_production, 24_LVBus288307_consumption, 24_LVBus288307_production, 24_LVBus288308_production, 24_LVBus288309_production, 24_LVBus288310_production, 24_LVBus288311_production, 24_LVBus288315_production, 24_LVBus288316_production, 24_LVBus288317_consumption, 24_LVBus288317_production, 24_LVBus288318_production, 24_LVBus288320_consumption, 24_LVBus288320_production, 24_LVBus288322_production, 24_LVBus288324_production, 24_LVBus288325_consumption, 24_LVBus288325_production, 24_LVBus288326_production, 24_LVBus288327_consumption, 24_LVBus288327_production, 24_LVBus288328_consumption, 24_LVBus288328_production, 24_LVBus288329_consumption, 24_LVBus288329_production, 24_LVBus288330_production, 24_LVBus288331_production, 24_LVBus288333_production, 24_LVBus288334_production, 24_LVBus288336_consumption, 24_LVBus288336_production, 24_LVBus288337_consumption, 24_LVBus288337_production, 24_LVBus288338_production, 24_LVBus288339_production, 24_LVBus288341_production, 24_LVBus288343_production, 24_LVBus288351_consumption, 24_LVBus288351_production, 24_LVBus288352_production, 24_LVBus288353_production, 24_LVBus288355_production, 24_LVBus288357_consumption, 24_LVBus288357_production, 24_LVBus288358_production, 24_LVBus288360_consumption, 24_LVBus288360_production, 24_LVBus288361_production, 24_LVBus288362_production, 24_LVBus288364_production, 24_LVBus288365_consumption, 24_LVBus288365_production, 24_LVBus288366_production, 24_LVBus288367_production, 24_LVBus288368_production, 24_LVBus288369_consumption, 24_LVBus288369_production, 24_LVBus288370_consumption, 24_LVBus288370_production, 24_LVBus288371_production, 24_LVBus288372_production, 24_LVBus288377_consumption, 24_LVBus288377_production, 24_LVBus288378_production, 24_LVBus288379_production, 24_LVBus288380_consumption, 24_LVBus288380_production, 24_LVBus288381_production, 24_LVBus288382_production, 24_LVBus288384_production, 24_LVBus288385_consumption, 24_LVBus288385_production, 24_LVBus288386_production, 24_LVBus288387_production, 24_LVBus288388_production, 24_LVBus288389_production, 24_LVBus288390_production, 24_LVBus288391_production, 24_LVBus288392_production, 24_LVBus288393_production, 24_LVBus288394_production, 24_LVBus288395_production, 24_LVBus288396_production, 24_LVBus288401_production, 24_LVBus288402_production, 24_LVBus288403_production, 24_LVBus288404_production, 24_LVBus288408_consumption, 24_LVBus288408_production, 24_LVBus288410_consumption, 24_LVBus288410_production, 24_LVBus288412_consumption, 24_LVBus288412_production, 24_LVBus288414_consumption, 24_LVBus288414_production, 24_LVBus288415_production, 24_LVBus288416_production, 24_LVBus288417_production, 24_LVBus288418_consumption, 24_LVBus288418_production, 24_LVBus288422_consumption, 24_LVBus288422_production, 24_LVBus288423_production, 24_LVBus288424_production, 24_LVBus288426_consumption, 24_LVBus288426_production, 24_LVBus288428_consumption, 24_LVBus288428_production, 24_LVBus288430_production, 24_LVBus288432_consumption, 24_LVBus288432_production, 24_LVBus288433_consumption, 24_LVBus288433_production, 24_LVBus288434_consumption, 24_LVBus288434_production, 24_LVBus288435_production, 24_LVBus288436_production, 24_LVBus288437_production, 24_LVBus288438_production, 24_LVBus288439_consumption, 24_LVBus288439_production, 24_LVBus288440_consumption, 24_LVBus288440_production, 24_LVBus288441_production, 24_LVBus288442_consumption, 24_LVBus288442_production, 24_LVBus288443_consumption, 24_LVBus288443_production, 24_LVBus843049_production, 24_LVBus843050_production, 24_LVBus843051_production, 24_LVBus843177_consumption, 24_LVBus843177_production, 24_LVBus843178_production, 24_LVBus843179_production, 24_LVBus843180_consumption, 24_LVBus843180_production, 24_LVBus843374_production, 24_LVBus843571_production, 24_LVBus843572_production, 24_LVBus843573_production, 24_LVBus843574_production, 24_MVLV03062_consumption, 24_MVLV03062_production, 24_MVLV10543_consumption, 24_MVLV10543_production, 24_MVLV53515_consumption, 24_MVLV53515_production, 24_MVLV61115_consumption, 24_MVLV61115_production, 24_MVLV86066_consumption, 24_MVLV86066_production.

