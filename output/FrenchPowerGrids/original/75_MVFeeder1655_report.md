# BMOPF Network Summary: 75_MVFeeder1655

**Generated:** 2026-10-01 23:34:23  
**Findings:** 0 errors · 5 warnings · 414 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 17 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 604 |  |
| line | 586 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 1136 | 5.266 MW, 1.58 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 17 |  |
| switch | 0 |  |
| transformer | 17 | Dyn11×17 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 21 | 20 | 4 | 0 |
| LV_236V | 236.0 V | 583 | 566 | 1132 | 0 |

**Transformer transitions:**

- `75_MVLV096212_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV025856_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV091583_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV084850_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121476_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV122581_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV125617_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV041659_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV041725_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV112219_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV126973_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV164336_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV122571_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV014150_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV025868_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV055606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV023617_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 236 |
| Tree depth (max hops) | 24 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 604 | 1 | 603 | 0 | 0 | 0 |
| Tier LV_236V | 583 | 17 | 566 | 0 | 0 | 0 |
| Tier MV_11.8kV | 21 | 1 | 20 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 17; skipped invalid branches: 0.

Galvanic zones: 18; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_FTPIN | MV_11.8kV | 21 | 0 | 0 | 17 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2395 declared bus terminals; 2324 mapped line/closed-switch conductor edges; 71 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 295000.0 | 6.929 | 3408 |
| q_nom | 0.0 | 88500.0 | 6.929 | 3408 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.922 | 2510.0 | 2.522 | 586 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 2.2e6 | 0.652 | 17 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 681 of 1136 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1920293_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857277_consumption' has phase imbalance of 212.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857542_consumption' has phase imbalance of 47.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857173_consumption' has phase imbalance of 138.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857205_consumption' has phase imbalance of 214.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857640_consumption' has phase imbalance of 64.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857654_consumption' has phase imbalance of 90.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857397_consumption' has phase imbalance of 71.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857382_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857209_consumption' has phase imbalance of 136.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857502_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857211_consumption' has phase imbalance of 99.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857227_consumption' has phase imbalance of 236.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857170_consumption' has phase imbalance of 29.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857580_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857252_consumption' has phase imbalance of 44.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857513_consumption' has phase imbalance of 261.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857303_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857516_consumption' has phase imbalance of 85.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857302_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857418_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857632_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857611_consumption' has phase imbalance of 41.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857515_consumption' has phase imbalance of 189.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857456_consumption' has phase imbalance of 40.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857295_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857679_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857373_consumption' has phase imbalance of 64.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857614_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857299_consumption' has phase imbalance of 94.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857196_consumption' has phase imbalance of 50.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857059_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857375_consumption' has phase imbalance of 59.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857221_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857097_consumption' has phase imbalance of 245.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857096_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857647_consumption' has phase imbalance of 250.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857367_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857266_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857153_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857151_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857212_consumption' has phase imbalance of 286.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857318_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857636_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857459_consumption' has phase imbalance of 82.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857148_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857087_consumption' has phase imbalance of 104.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857162_consumption' has phase imbalance of 141.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857368_consumption' has phase imbalance of 104.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857256_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857484_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857370_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857348_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857127_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857187_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857566_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857404_consumption' has phase imbalance of 111.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857159_consumption' has phase imbalance of 192.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857449_consumption' has phase imbalance of 69.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857402_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857457_consumption' has phase imbalance of 113.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857379_consumption' has phase imbalance of 27.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857355_consumption' has phase imbalance of 119.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857553_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857426_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857578_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857165_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857535_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857420_consumption' has phase imbalance of 40.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857680_consumption' has phase imbalance of 56.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857627_consumption' has phase imbalance of 51.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857098_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857093_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857200_consumption' has phase imbalance of 63.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857226_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857143_consumption' has phase imbalance of 62.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857575_consumption' has phase imbalance of 93.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857287_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857157_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857596_consumption' has phase imbalance of 53.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857152_consumption' has phase imbalance of 220.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857563_consumption' has phase imbalance of 35.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857570_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1920295_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857197_consumption' has phase imbalance of 138.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857546_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857665_consumption' has phase imbalance of 76.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857319_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857223_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857462_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857380_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857082_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1984041_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857343_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857106_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857101_consumption' has phase imbalance of 276.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857338_consumption' has phase imbalance of 23.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857548_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857641_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857362_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857210_consumption' has phase imbalance of 173.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857284_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857495_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857248_consumption' has phase imbalance of 119.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857396_consumption' has phase imbalance of 228.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857455_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857585_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857060_consumption' has phase imbalance of 215.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857156_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857469_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857177_consumption' has phase imbalance of 107.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857071_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857415_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857490_consumption' has phase imbalance of 45.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857058_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857423_consumption' has phase imbalance of 46.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857341_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857389_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857568_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857184_consumption' has phase imbalance of 219.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857160_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857158_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857360_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857430_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857315_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857131_consumption' has phase imbalance of 60.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857653_consumption' has phase imbalance of 61.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857512_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857089_consumption' has phase imbalance of 120.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857508_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857280_consumption' has phase imbalance of 88.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857112_consumption' has phase imbalance of 85.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857447_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1920296_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857419_consumption' has phase imbalance of 134.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857561_consumption' has phase imbalance of 49.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857225_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857424_consumption' has phase imbalance of 238.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857061_consumption' has phase imbalance of 271.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857354_consumption' has phase imbalance of 85.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1990527_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857574_consumption' has phase imbalance of 220.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857401_consumption' has phase imbalance of 82.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857604_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857505_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857503_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857511_consumption' has phase imbalance of 126.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857311_consumption' has phase imbalance of 141.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857301_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857668_consumption' has phase imbalance of 112.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857432_consumption' has phase imbalance of 97.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857458_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857437_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857344_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857366_consumption' has phase imbalance of 146.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857556_consumption' has phase imbalance of 48.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857359_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857446_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857673_consumption' has phase imbalance of 211.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857218_consumption' has phase imbalance of 223.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857492_consumption' has phase imbalance of 200.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857473_consumption' has phase imbalance of 33.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857592_consumption' has phase imbalance of 46.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857099_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857325_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857587_consumption' has phase imbalance of 39.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857080_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857448_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857440_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857452_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857075_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857425_consumption' has phase imbalance of 125.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857467_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857439_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857507_consumption' has phase imbalance of 58.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857135_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857265_consumption' has phase imbalance of 233.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857163_consumption' has phase imbalance of 98.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857475_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857618_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857339_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857594_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1920292_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857185_consumption' has phase imbalance of 200.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857077_consumption' has phase imbalance of 224.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857189_consumption' has phase imbalance of 106.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857181_consumption' has phase imbalance of 129.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857154_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857554_consumption' has phase imbalance of 129.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857682_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857558_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857519_consumption' has phase imbalance of 247.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857681_consumption' has phase imbalance of 124.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857088_consumption' has phase imbalance of 61.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857182_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857572_consumption' has phase imbalance of 141.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857268_consumption' has phase imbalance of 26.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857257_consumption' has phase imbalance of 97.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857202_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857346_consumption' has phase imbalance of 45.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857527_consumption' has phase imbalance of 22.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857222_consumption' has phase imbalance of 217.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857358_consumption' has phase imbalance of 139.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857569_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857347_consumption' has phase imbalance of 102.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857329_consumption' has phase imbalance of 257.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857305_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857532_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857207_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857480_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857667_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857307_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857429_consumption' has phase imbalance of 45.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857677_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857481_consumption' has phase imbalance of 104.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857581_consumption' has phase imbalance of 23.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857124_consumption' has phase imbalance of 114.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857573_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857084_consumption' has phase imbalance of 194.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857663_consumption' has phase imbalance of 56.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857444_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857193_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857656_consumption' has phase imbalance of 120.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857434_consumption' has phase imbalance of 132.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857247_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857245_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857092_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857175_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857292_consumption' has phase imbalance of 20.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857602_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857588_consumption' has phase imbalance of 106.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857645_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857304_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857476_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857324_consumption' has phase imbalance of 73.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857579_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857066_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857136_consumption' has phase imbalance of 129.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857433_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1990526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857216_consumption' has phase imbalance of 216.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857518_consumption' has phase imbalance of 206.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857214_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857486_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857624_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857529_consumption' has phase imbalance of 187.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857528_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857521_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857552_consumption' has phase imbalance of 38.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857063_consumption' has phase imbalance of 26.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857422_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857113_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857364_consumption' has phase imbalance of 59.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857171_consumption' has phase imbalance of 242.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857056_consumption' has phase imbalance of 20.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857509_consumption' has phase imbalance of 100.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857669_consumption' has phase imbalance of 20.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857345_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857083_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857179_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857398_consumption' has phase imbalance of 215.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857137_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857111_consumption' has phase imbalance of 246.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857068_consumption' has phase imbalance of 144.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857431_consumption' has phase imbalance of 73.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857264_consumption' has phase imbalance of 60.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857483_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857169_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1990529_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857541_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857231_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857584_consumption' has phase imbalance of 52.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857388_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857371_consumption' has phase imbalance of 104.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857474_consumption' has phase imbalance of 48.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857314_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857598_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857489_consumption' has phase imbalance of 109.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857194_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857290_consumption' has phase imbalance of 211.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857443_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857161_consumption' has phase imbalance of 249.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857638_consumption' has phase imbalance of 24.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857323_consumption' has phase imbalance of 93.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857635_consumption' has phase imbalance of 47.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857372_consumption' has phase imbalance of 33.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857496_consumption' has phase imbalance of 127.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857100_consumption' has phase imbalance of 249.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857340_consumption' has phase imbalance of 29.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857126_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857155_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1920287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857258_consumption' has phase imbalance of 94.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857309_consumption' has phase imbalance of 86.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857463_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857534_consumption' has phase imbalance of 85.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857146_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857683_consumption' has phase imbalance of 124.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857545_consumption' has phase imbalance of 64.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857298_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857590_consumption' has phase imbalance of 50.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1920289_consumption' has phase imbalance of 133.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857328_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857416_consumption' has phase imbalance of 174.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857174_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857365_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857460_consumption' has phase imbalance of 47.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857504_consumption' has phase imbalance of 267.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857493_consumption' has phase imbalance of 93.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857510_consumption' has phase imbalance of 246.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857125_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857164_consumption' has phase imbalance of 89.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857147_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857095_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857069_consumption' has phase imbalance of 105.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857281_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857244_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857660_consumption' has phase imbalance of 60.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857288_consumption' has phase imbalance of 21.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857176_consumption' has phase imbalance of 254.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857672_consumption' has phase imbalance of 120.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857220_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857263_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857549_consumption' has phase imbalance of 36.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857091_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857576_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857259_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857655_consumption' has phase imbalance of 205.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857178_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1920290_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857491_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857249_consumption' has phase imbalance of 66.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857320_consumption' has phase imbalance of 90.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857628_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857517_consumption' has phase imbalance of 88.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857658_consumption' has phase imbalance of 65.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857405_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857381_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857180_consumption' has phase imbalance of 248.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857464_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857094_consumption' has phase imbalance of 243.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857407_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1857286_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1136 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_FTPIN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1857538' has balanced aggregate load across 3 phase(s) (max spread 1.11%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 5.266 MW |
| Total load Q | 1.58 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV096212_Transformer | 1.1 MVA | 31.4% |
| 75_MVLV025856_Transformer | 693.0 kVA | 41.0% |
| 75_MVLV091583_Transformer | 693.0 kVA | 24.0% |
| 75_MVLV084850_Transformer | 693.0 kVA | 29.5% |
| 75_MVLV121476_Transformer | 693.0 kVA | 26.3% |
| 75_MVLV122581_Transformer | 1.1 MVA | 33.1% |
| 75_MVLV125617_Transformer | 440.0 kVA | 37.9% |
| 75_MVLV041659_Transformer | 693.0 kVA | 44.8% |
| 75_MVLV041725_Transformer | 440.0 kVA | 23.3% |
| 75_MVLV112219_Transformer | 1.1 MVA | 25.8% |
| 75_MVLV126973_Transformer | 2.2 MVA | 6.3% |
| 75_MVLV164336_Transformer | 440.0 kVA | 36.7% |
| 75_MVLV122571_Transformer | 2.2 MVA | 18.4% |
| 75_MVLV014150_Transformer | 440.0 kVA | 30.5% |
| 75_MVLV025868_Transformer | 693.0 kVA | 72.6% |
| 75_MVLV055606_Transformer | 275.0 kVA | 23.0% |
| 75_MVLV023617_Transformer | 693.0 kVA | 31.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.27 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 604 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 604 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 17 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 21 |
| LV_236V | 4-wire | 583 / 583 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 583 |
| Neutral branches | 566 |
| Grounding points | 17 |
| Neutral sections | 17 |
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
| 11.78 kV | 21 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 81 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 58 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 107 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 43 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 18 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1160.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 583 / 21 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 682 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 682 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1857050_production, 75_LVBus1857051_consumption, 75_LVBus1857051_production, 75_LVBus1857053_consumption, 75_LVBus1857053_production, 75_LVBus1857055_consumption, 75_LVBus1857055_production, 75_LVBus1857056_production, 75_LVBus1857058_production, 75_LVBus1857059_production, 75_LVBus1857060_production, 75_LVBus1857061_production, 75_LVBus1857062_production, 75_LVBus1857063_production, 75_LVBus1857064_production, 75_LVBus1857065_production, 75_LVBus1857066_production, 75_LVBus1857068_production, 75_LVBus1857069_production, 75_LVBus1857070_production, 75_LVBus1857071_production, 75_LVBus1857072_consumption, 75_LVBus1857072_production, 75_LVBus1857073_consumption, 75_LVBus1857073_production, 75_LVBus1857074_consumption, 75_LVBus1857074_production, 75_LVBus1857075_production, 75_LVBus1857077_production, 75_LVBus1857078_production, 75_LVBus1857079_production, 75_LVBus1857080_production, 75_LVBus1857081_production, 75_LVBus1857082_production, 75_LVBus1857083_production, 75_LVBus1857084_production, 75_LVBus1857086_consumption, 75_LVBus1857086_production, 75_LVBus1857087_production, 75_LVBus1857088_production, 75_LVBus1857089_production, 75_LVBus1857091_production, 75_LVBus1857092_production, 75_LVBus1857093_production, 75_LVBus1857094_production, 75_LVBus1857095_production, 75_LVBus1857096_production, 75_LVBus1857097_production, 75_LVBus1857098_production, 75_LVBus1857099_production, 75_LVBus1857100_production, 75_LVBus1857101_production, 75_LVBus1857103_consumption, 75_LVBus1857103_production, 75_LVBus1857104_production, 75_LVBus1857105_production, 75_LVBus1857106_production, 75_LVBus1857109_production, 75_LVBus1857110_production, 75_LVBus1857111_production, 75_LVBus1857112_production, 75_LVBus1857113_production, 75_LVBus1857114_consumption, 75_LVBus1857114_production, 75_LVBus1857116_consumption, 75_LVBus1857116_production, 75_LVBus1857118_consumption, 75_LVBus1857118_production, 75_LVBus1857119_consumption, 75_LVBus1857119_production, 75_LVBus1857121_consumption, 75_LVBus1857121_production, 75_LVBus1857122_consumption, 75_LVBus1857122_production, 75_LVBus1857123_consumption, 75_LVBus1857123_production, 75_LVBus1857124_production, 75_LVBus1857125_production, 75_LVBus1857126_production, 75_LVBus1857127_production, 75_LVBus1857128_consumption, 75_LVBus1857128_production, 75_LVBus1857130_consumption, 75_LVBus1857130_production, 75_LVBus1857131_production, 75_LVBus1857133_consumption, 75_LVBus1857133_production, 75_LVBus1857134_production, 75_LVBus1857135_production, 75_LVBus1857136_production, 75_LVBus1857137_production, 75_LVBus1857139_production, 75_LVBus1857140_production, 75_LVBus1857142_consumption, 75_LVBus1857142_production, 75_LVBus1857143_production, 75_LVBus1857145_production, 75_LVBus1857146_production, 75_LVBus1857147_production, 75_LVBus1857148_production, 75_LVBus1857149_consumption, 75_LVBus1857149_production, 75_LVBus1857150_consumption, 75_LVBus1857150_production, 75_LVBus1857151_production, 75_LVBus1857152_production, 75_LVBus1857153_production, 75_LVBus1857154_production, 75_LVBus1857155_production, 75_LVBus1857156_production, 75_LVBus1857157_production, 75_LVBus1857158_production, 75_LVBus1857159_production, 75_LVBus1857160_production, 75_LVBus1857161_production, 75_LVBus1857162_production, 75_LVBus1857163_production, 75_LVBus1857164_production, 75_LVBus1857165_production, 75_LVBus1857166_consumption, 75_LVBus1857166_production, 75_LVBus1857167_production, 75_LVBus1857168_production, 75_LVBus1857169_production, 75_LVBus1857170_production, 75_LVBus1857171_production, 75_LVBus1857173_production, 75_LVBus1857174_production, 75_LVBus1857175_production, 75_LVBus1857176_production, 75_LVBus1857177_production, 75_LVBus1857178_production, 75_LVBus1857179_production, 75_LVBus1857180_production, 75_LVBus1857181_production, 75_LVBus1857182_production, 75_LVBus1857184_production, 75_LVBus1857185_production, 75_LVBus1857186_consumption, 75_LVBus1857186_production, 75_LVBus1857187_production, 75_LVBus1857188_production, 75_LVBus1857189_production, 75_LVBus1857191_production, 75_LVBus1857193_production, 75_LVBus1857194_production, 75_LVBus1857195_consumption, 75_LVBus1857195_production, 75_LVBus1857196_production, 75_LVBus1857197_production, 75_LVBus1857198_production, 75_LVBus1857199_consumption, 75_LVBus1857199_production, 75_LVBus1857200_production, 75_LVBus1857201_production, 75_LVBus1857202_production, 75_LVBus1857203_consumption, 75_LVBus1857203_production, 75_LVBus1857204_production, 75_LVBus1857205_production, 75_LVBus1857206_production, 75_LVBus1857207_production, 75_LVBus1857208_production, 75_LVBus1857209_production, 75_LVBus1857210_production, 75_LVBus1857211_production, 75_LVBus1857212_production, 75_LVBus1857214_production, 75_LVBus1857216_production, 75_LVBus1857218_production, 75_LVBus1857219_consumption, 75_LVBus1857219_production, 75_LVBus1857220_production, 75_LVBus1857221_production, 75_LVBus1857222_production, 75_LVBus1857223_production, 75_LVBus1857224_production, 75_LVBus1857225_production, 75_LVBus1857226_production, 75_LVBus1857227_production, 75_LVBus1857228_production, 75_LVBus1857229_production, 75_LVBus1857230_production, 75_LVBus1857231_production, 75_LVBus1857233_production, 75_LVBus1857235_production, 75_LVBus1857236_consumption, 75_LVBus1857236_production, 75_LVBus1857238_consumption, 75_LVBus1857238_production, 75_LVBus1857239_consumption, 75_LVBus1857239_production, 75_LVBus1857240_consumption, 75_LVBus1857240_production, 75_LVBus1857241_consumption, 75_LVBus1857241_production, 75_LVBus1857242_production, 75_LVBus1857243_consumption, 75_LVBus1857243_production, 75_LVBus1857244_production, 75_LVBus1857245_production, 75_LVBus1857246_consumption, 75_LVBus1857246_production, 75_LVBus1857247_production, 75_LVBus1857248_production, 75_LVBus1857249_production, 75_LVBus1857250_consumption, 75_LVBus1857250_production, 75_LVBus1857251_production, 75_LVBus1857252_production, 75_LVBus1857254_consumption, 75_LVBus1857254_production, 75_LVBus1857255_consumption, 75_LVBus1857255_production, 75_LVBus1857256_production, 75_LVBus1857257_production, 75_LVBus1857258_production, 75_LVBus1857259_production, 75_LVBus1857260_production, 75_LVBus1857262_consumption, 75_LVBus1857262_production, 75_LVBus1857263_production, 75_LVBus1857264_production, 75_LVBus1857265_production, 75_LVBus1857266_production, 75_LVBus1857267_production, 75_LVBus1857268_production, 75_LVBus1857270_consumption, 75_LVBus1857270_production, 75_LVBus1857271_consumption, 75_LVBus1857271_production, 75_LVBus1857272_production, 75_LVBus1857273_production, 75_LVBus1857274_consumption, 75_LVBus1857274_production, 75_LVBus1857275_consumption, 75_LVBus1857275_production, 75_LVBus1857276_consumption, 75_LVBus1857276_production, 75_LVBus1857277_production, 75_LVBus1857278_production, 75_LVBus1857279_consumption, 75_LVBus1857279_production, 75_LVBus1857280_production, 75_LVBus1857281_production, 75_LVBus1857282_production, 75_LVBus1857283_production, 75_LVBus1857284_production, 75_LVBus1857285_production, 75_LVBus1857286_production, 75_LVBus1857287_production, 75_LVBus1857288_production, 75_LVBus1857289_consumption, 75_LVBus1857289_production, 75_LVBus1857290_production, 75_LVBus1857291_production, 75_LVBus1857292_production, 75_LVBus1857294_production, 75_LVBus1857295_production, 75_LVBus1857297_consumption, 75_LVBus1857297_production, 75_LVBus1857298_production, 75_LVBus1857299_production, 75_LVBus1857300_consumption, 75_LVBus1857300_production, 75_LVBus1857301_production, 75_LVBus1857302_production, 75_LVBus1857303_production, 75_LVBus1857304_production, 75_LVBus1857305_production, 75_LVBus1857307_production, 75_LVBus1857309_production, 75_LVBus1857311_production, 75_LVBus1857312_production, 75_LVBus1857313_consumption, 75_LVBus1857313_production, 75_LVBus1857314_production, 75_LVBus1857315_production, 75_LVBus1857316_production, 75_LVBus1857318_production, 75_LVBus1857319_production, 75_LVBus1857320_production, 75_LVBus1857322_production, 75_LVBus1857323_production, 75_LVBus1857324_production, 75_LVBus1857325_production, 75_LVBus1857328_production, 75_LVBus1857329_production, 75_LVBus1857330_production, 75_LVBus1857331_consumption, 75_LVBus1857331_production, 75_LVBus1857332_consumption, 75_LVBus1857332_production, 75_LVBus1857335_consumption, 75_LVBus1857335_production, 75_LVBus1857336_consumption, 75_LVBus1857336_production, 75_LVBus1857337_consumption, 75_LVBus1857337_production, 75_LVBus1857338_production, 75_LVBus1857339_production, 75_LVBus1857340_production, 75_LVBus1857341_production, 75_LVBus1857343_production, 75_LVBus1857344_production, 75_LVBus1857345_production, 75_LVBus1857346_production, 75_LVBus1857347_production, 75_LVBus1857348_production, 75_LVBus1857349_production, 75_LVBus1857350_production, 75_LVBus1857352_consumption, 75_LVBus1857352_production, 75_LVBus1857353_consumption, 75_LVBus1857353_production, 75_LVBus1857354_production, 75_LVBus1857355_production, 75_LVBus1857356_consumption, 75_LVBus1857356_production, 75_LVBus1857357_consumption, 75_LVBus1857357_production, 75_LVBus1857358_production, 75_LVBus1857359_production, 75_LVBus1857360_production, 75_LVBus1857362_production, 75_LVBus1857363_consumption, 75_LVBus1857363_production, 75_LVBus1857364_production, 75_LVBus1857365_production, 75_LVBus1857366_production, 75_LVBus1857367_production, 75_LVBus1857368_production, 75_LVBus1857369_consumption, 75_LVBus1857369_production, 75_LVBus1857370_production, 75_LVBus1857371_production, 75_LVBus1857372_production, 75_LVBus1857373_production, 75_LVBus1857375_production, 75_LVBus1857376_consumption, 75_LVBus1857376_production, 75_LVBus1857377_consumption, 75_LVBus1857377_production, 75_LVBus1857378_consumption, 75_LVBus1857378_production, 75_LVBus1857379_production, 75_LVBus1857380_production, 75_LVBus1857381_production, 75_LVBus1857382_production, 75_LVBus1857385_consumption, 75_LVBus1857385_production, 75_LVBus1857386_consumption, 75_LVBus1857386_production, 75_LVBus1857388_production, 75_LVBus1857389_production, 75_LVBus1857391_consumption, 75_LVBus1857391_production, 75_LVBus1857392_consumption, 75_LVBus1857392_production, 75_LVBus1857393_consumption, 75_LVBus1857393_production, 75_LVBus1857394_production, 75_LVBus1857395_production, 75_LVBus1857396_production, 75_LVBus1857397_production, 75_LVBus1857398_production, 75_LVBus1857400_consumption, 75_LVBus1857400_production, 75_LVBus1857401_production, 75_LVBus1857402_production, 75_LVBus1857403_production, 75_LVBus1857404_production, 75_LVBus1857405_production, 75_LVBus1857407_production, 75_LVBus1857408_consumption, 75_LVBus1857408_production, 75_LVBus1857409_consumption, 75_LVBus1857409_production, 75_LVBus1857410_consumption, 75_LVBus1857410_production, 75_LVBus1857411_consumption, 75_LVBus1857411_production, 75_LVBus1857412_production, 75_LVBus1857413_production, 75_LVBus1857414_production, 75_LVBus1857415_production, 75_LVBus1857416_production, 75_LVBus1857417_consumption, 75_LVBus1857417_production, 75_LVBus1857418_production, 75_LVBus1857419_production, 75_LVBus1857420_production, 75_LVBus1857421_production, 75_LVBus1857422_production, 75_LVBus1857423_production, 75_LVBus1857424_production, 75_LVBus1857425_production, 75_LVBus1857426_production, 75_LVBus1857427_production, 75_LVBus1857428_production, 75_LVBus1857429_production, 75_LVBus1857430_production, 75_LVBus1857431_production, 75_LVBus1857432_production, 75_LVBus1857433_production, 75_LVBus1857434_production, 75_LVBus1857435_consumption, 75_LVBus1857435_production, 75_LVBus1857436_production, 75_LVBus1857437_production, 75_LVBus1857438_production, 75_LVBus1857439_production, 75_LVBus1857440_production, 75_LVBus1857441_consumption, 75_LVBus1857441_production, 75_LVBus1857442_consumption, 75_LVBus1857442_production, 75_LVBus1857443_production, 75_LVBus1857444_production, 75_LVBus1857445_production, 75_LVBus1857446_production, 75_LVBus1857447_production, 75_LVBus1857448_production, 75_LVBus1857449_production, 75_LVBus1857451_consumption, 75_LVBus1857451_production, 75_LVBus1857452_production, 75_LVBus1857453_consumption, 75_LVBus1857453_production, 75_LVBus1857454_production, 75_LVBus1857455_production, 75_LVBus1857456_production, 75_LVBus1857457_production, 75_LVBus1857458_production, 75_LVBus1857459_production, 75_LVBus1857460_production, 75_LVBus1857461_consumption, 75_LVBus1857461_production, 75_LVBus1857462_production, 75_LVBus1857463_production, 75_LVBus1857464_production, 75_LVBus1857465_consumption, 75_LVBus1857465_production, 75_LVBus1857466_production, 75_LVBus1857467_production, 75_LVBus1857468_production, 75_LVBus1857469_production, 75_LVBus1857470_consumption, 75_LVBus1857470_production, 75_LVBus1857471_production, 75_LVBus1857472_consumption, 75_LVBus1857472_production, 75_LVBus1857473_production, 75_LVBus1857474_production, 75_LVBus1857475_production, 75_LVBus1857476_production, 75_LVBus1857478_consumption, 75_LVBus1857478_production, 75_LVBus1857479_production, 75_LVBus1857480_production, 75_LVBus1857481_production, 75_LVBus1857482_consumption, 75_LVBus1857482_production, 75_LVBus1857483_production, 75_LVBus1857484_production, 75_LVBus1857485_consumption, 75_LVBus1857485_production, 75_LVBus1857486_production, 75_LVBus1857487_production, 75_LVBus1857488_production, 75_LVBus1857489_production, 75_LVBus1857490_production, 75_LVBus1857491_production, 75_LVBus1857492_production, 75_LVBus1857493_production, 75_LVBus1857494_production, 75_LVBus1857495_production, 75_LVBus1857496_production, 75_LVBus1857502_production, 75_LVBus1857503_production, 75_LVBus1857504_production, 75_LVBus1857505_production, 75_LVBus1857506_production, 75_LVBus1857507_production, 75_LVBus1857508_production, 75_LVBus1857509_production, 75_LVBus1857510_production, 75_LVBus1857511_production, 75_LVBus1857512_production, 75_LVBus1857513_production, 75_LVBus1857514_production, 75_LVBus1857515_production, 75_LVBus1857516_production, 75_LVBus1857517_production, 75_LVBus1857518_production, 75_LVBus1857519_production, 75_LVBus1857520_production, 75_LVBus1857521_production, 75_LVBus1857523_consumption, 75_LVBus1857523_production, 75_LVBus1857524_consumption, 75_LVBus1857524_production, 75_LVBus1857525_production, 75_LVBus1857526_production, 75_LVBus1857527_production, 75_LVBus1857528_production, 75_LVBus1857529_production, 75_LVBus1857531_consumption, 75_LVBus1857531_production, 75_LVBus1857532_production, 75_LVBus1857533_production, 75_LVBus1857534_production, 75_LVBus1857535_production, 75_LVBus1857538_production, 75_LVBus1857540_consumption, 75_LVBus1857540_production, 75_LVBus1857541_production, 75_LVBus1857542_production, 75_LVBus1857544_production, 75_LVBus1857545_production, 75_LVBus1857546_production, 75_LVBus1857547_production, 75_LVBus1857548_production, 75_LVBus1857549_production, 75_LVBus1857550_production, 75_LVBus1857551_consumption, 75_LVBus1857551_production, 75_LVBus1857552_production, 75_LVBus1857553_production, 75_LVBus1857554_production, 75_LVBus1857556_production, 75_LVBus1857558_production, 75_LVBus1857560_consumption, 75_LVBus1857560_production, 75_LVBus1857561_production, 75_LVBus1857563_production, 75_LVBus1857564_production, 75_LVBus1857565_consumption, 75_LVBus1857565_production, 75_LVBus1857566_production, 75_LVBus1857567_consumption, 75_LVBus1857567_production, 75_LVBus1857568_production, 75_LVBus1857569_production, 75_LVBus1857570_production, 75_LVBus1857571_production, 75_LVBus1857572_production, 75_LVBus1857573_production, 75_LVBus1857574_production, 75_LVBus1857575_production, 75_LVBus1857576_production, 75_LVBus1857577_production, 75_LVBus1857578_production, 75_LVBus1857579_production, 75_LVBus1857580_production, 75_LVBus1857581_production, 75_LVBus1857582_production, 75_LVBus1857583_consumption, 75_LVBus1857583_production, 75_LVBus1857584_production, 75_LVBus1857585_production, 75_LVBus1857587_production, 75_LVBus1857588_production, 75_LVBus1857590_production, 75_LVBus1857591_production, 75_LVBus1857592_production, 75_LVBus1857594_production, 75_LVBus1857595_production, 75_LVBus1857596_production, 75_LVBus1857597_production, 75_LVBus1857598_production, 75_LVBus1857599_production, 75_LVBus1857600_consumption, 75_LVBus1857600_production, 75_LVBus1857602_production, 75_LVBus1857603_consumption, 75_LVBus1857603_production, 75_LVBus1857604_production, 75_LVBus1857605_production, 75_LVBus1857606_consumption, 75_LVBus1857606_production, 75_LVBus1857607_production, 75_LVBus1857608_consumption, 75_LVBus1857608_production, 75_LVBus1857609_production, 75_LVBus1857611_production, 75_LVBus1857613_consumption, 75_LVBus1857613_production, 75_LVBus1857614_production, 75_LVBus1857615_consumption, 75_LVBus1857615_production, 75_LVBus1857617_production, 75_LVBus1857618_production, 75_LVBus1857619_production, 75_LVBus1857620_consumption, 75_LVBus1857620_production, 75_LVBus1857621_production, 75_LVBus1857622_production, 75_LVBus1857623_production, 75_LVBus1857624_production, 75_LVBus1857625_consumption, 75_LVBus1857625_production, 75_LVBus1857626_production, 75_LVBus1857627_production, 75_LVBus1857628_production, 75_LVBus1857630_consumption, 75_LVBus1857630_production, 75_LVBus1857631_production, 75_LVBus1857632_production, 75_LVBus1857633_consumption, 75_LVBus1857633_production, 75_LVBus1857635_production, 75_LVBus1857636_production, 75_LVBus1857638_production, 75_LVBus1857639_production, 75_LVBus1857640_production, 75_LVBus1857641_production, 75_LVBus1857642_production, 75_LVBus1857643_production, 75_LVBus1857644_consumption, 75_LVBus1857644_production, 75_LVBus1857645_production, 75_LVBus1857646_production, 75_LVBus1857647_production, 75_LVBus1857648_consumption, 75_LVBus1857648_production, 75_LVBus1857649_production, 75_LVBus1857651_production, 75_LVBus1857653_production, 75_LVBus1857654_production, 75_LVBus1857655_production, 75_LVBus1857656_production, 75_LVBus1857657_production, 75_LVBus1857658_production, 75_LVBus1857660_production, 75_LVBus1857661_consumption, 75_LVBus1857661_production, 75_LVBus1857663_production, 75_LVBus1857665_production, 75_LVBus1857667_production, 75_LVBus1857668_production, 75_LVBus1857669_production, 75_LVBus1857670_production, 75_LVBus1857672_production, 75_LVBus1857673_production, 75_LVBus1857674_consumption, 75_LVBus1857674_production, 75_LVBus1857676_consumption, 75_LVBus1857676_production, 75_LVBus1857677_production, 75_LVBus1857678_production, 75_LVBus1857679_production, 75_LVBus1857680_production, 75_LVBus1857681_production, 75_LVBus1857682_production, 75_LVBus1857683_production, 75_LVBus1920286_consumption, 75_LVBus1920286_production, 75_LVBus1920287_production, 75_LVBus1920288_production, 75_LVBus1920289_production, 75_LVBus1920290_production, 75_LVBus1920291_consumption, 75_LVBus1920291_production, 75_LVBus1920292_production, 75_LVBus1920293_production, 75_LVBus1920294_consumption, 75_LVBus1920294_production, 75_LVBus1920295_production, 75_LVBus1920296_production, 75_LVBus1920297_production, 75_LVBus1984040_consumption, 75_LVBus1984040_production, 75_LVBus1984041_production, 75_LVBus1990526_production, 75_LVBus1990527_production, 75_LVBus1990528_production, 75_LVBus1990529_production, 75_LVBus1990530_consumption, 75_LVBus1990530_production, 75_MVLV067938_production, 75_MVLV121510_production.

## 9. Data Quality Summary

**Total findings:** 419 (0 errors, 5 warnings, 414 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  681 of 1136 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.27 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  682 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1920293_consumption`  
  Load '75_LVBus1920293_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857277_consumption`  
  Load '75_LVBus1857277_consumption' has phase imbalance of 212.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857542_consumption`  
  Load '75_LVBus1857542_consumption' has phase imbalance of 47.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857395_consumption`  
  Load '75_LVBus1857395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857349_consumption`  
  Load '75_LVBus1857349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857173_consumption`  
  Load '75_LVBus1857173_consumption' has phase imbalance of 138.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857205_consumption`  
  Load '75_LVBus1857205_consumption' has phase imbalance of 214.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857640_consumption`  
  Load '75_LVBus1857640_consumption' has phase imbalance of 64.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857654_consumption`  
  Load '75_LVBus1857654_consumption' has phase imbalance of 90.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857397_consumption`  
  Load '75_LVBus1857397_consumption' has phase imbalance of 71.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857382_consumption`  
  Load '75_LVBus1857382_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857209_consumption`  
  Load '75_LVBus1857209_consumption' has phase imbalance of 136.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857502_consumption`  
  Load '75_LVBus1857502_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857211_consumption`  
  Load '75_LVBus1857211_consumption' has phase imbalance of 99.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857050_consumption`  
  Load '75_LVBus1857050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857227_consumption`  
  Load '75_LVBus1857227_consumption' has phase imbalance of 236.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857170_consumption`  
  Load '75_LVBus1857170_consumption' has phase imbalance of 29.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857580_consumption`  
  Load '75_LVBus1857580_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857252_consumption`  
  Load '75_LVBus1857252_consumption' has phase imbalance of 44.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857513_consumption`  
  Load '75_LVBus1857513_consumption' has phase imbalance of 261.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857303_consumption`  
  Load '75_LVBus1857303_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857516_consumption`  
  Load '75_LVBus1857516_consumption' has phase imbalance of 85.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857302_consumption`  
  Load '75_LVBus1857302_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857418_consumption`  
  Load '75_LVBus1857418_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857204_consumption`  
  Load '75_LVBus1857204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857632_consumption`  
  Load '75_LVBus1857632_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857611_consumption`  
  Load '75_LVBus1857611_consumption' has phase imbalance of 41.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857445_consumption`  
  Load '75_LVBus1857445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857515_consumption`  
  Load '75_LVBus1857515_consumption' has phase imbalance of 189.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857456_consumption`  
  Load '75_LVBus1857456_consumption' has phase imbalance of 40.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857295_consumption`  
  Load '75_LVBus1857295_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857312_consumption`  
  Load '75_LVBus1857312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857679_consumption`  
  Load '75_LVBus1857679_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857373_consumption`  
  Load '75_LVBus1857373_consumption' has phase imbalance of 64.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857614_consumption`  
  Load '75_LVBus1857614_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857299_consumption`  
  Load '75_LVBus1857299_consumption' has phase imbalance of 94.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857196_consumption`  
  Load '75_LVBus1857196_consumption' has phase imbalance of 50.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857059_consumption`  
  Load '75_LVBus1857059_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857375_consumption`  
  Load '75_LVBus1857375_consumption' has phase imbalance of 59.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857221_consumption`  
  Load '75_LVBus1857221_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857097_consumption`  
  Load '75_LVBus1857097_consumption' has phase imbalance of 245.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857096_consumption`  
  Load '75_LVBus1857096_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857647_consumption`  
  Load '75_LVBus1857647_consumption' has phase imbalance of 250.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857145_consumption`  
  Load '75_LVBus1857145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857367_consumption`  
  Load '75_LVBus1857367_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857266_consumption`  
  Load '75_LVBus1857266_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857153_consumption`  
  Load '75_LVBus1857153_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857414_consumption`  
  Load '75_LVBus1857414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857151_consumption`  
  Load '75_LVBus1857151_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857212_consumption`  
  Load '75_LVBus1857212_consumption' has phase imbalance of 286.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857318_consumption`  
  Load '75_LVBus1857318_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857636_consumption`  
  Load '75_LVBus1857636_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857459_consumption`  
  Load '75_LVBus1857459_consumption' has phase imbalance of 82.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857278_consumption`  
  Load '75_LVBus1857278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857148_consumption`  
  Load '75_LVBus1857148_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857087_consumption`  
  Load '75_LVBus1857087_consumption' has phase imbalance of 104.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857162_consumption`  
  Load '75_LVBus1857162_consumption' has phase imbalance of 141.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857368_consumption`  
  Load '75_LVBus1857368_consumption' has phase imbalance of 104.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857134_consumption`  
  Load '75_LVBus1857134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857256_consumption`  
  Load '75_LVBus1857256_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857484_consumption`  
  Load '75_LVBus1857484_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857370_consumption`  
  Load '75_LVBus1857370_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857348_consumption`  
  Load '75_LVBus1857348_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857127_consumption`  
  Load '75_LVBus1857127_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857187_consumption`  
  Load '75_LVBus1857187_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857566_consumption`  
  Load '75_LVBus1857566_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857404_consumption`  
  Load '75_LVBus1857404_consumption' has phase imbalance of 111.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857514_consumption`  
  Load '75_LVBus1857514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857159_consumption`  
  Load '75_LVBus1857159_consumption' has phase imbalance of 192.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857449_consumption`  
  Load '75_LVBus1857449_consumption' has phase imbalance of 69.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857402_consumption`  
  Load '75_LVBus1857402_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857457_consumption`  
  Load '75_LVBus1857457_consumption' has phase imbalance of 113.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857379_consumption`  
  Load '75_LVBus1857379_consumption' has phase imbalance of 27.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857619_consumption`  
  Load '75_LVBus1857619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857355_consumption`  
  Load '75_LVBus1857355_consumption' has phase imbalance of 119.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857553_consumption`  
  Load '75_LVBus1857553_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857224_consumption`  
  Load '75_LVBus1857224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857426_consumption`  
  Load '75_LVBus1857426_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857578_consumption`  
  Load '75_LVBus1857578_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857165_consumption`  
  Load '75_LVBus1857165_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857535_consumption`  
  Load '75_LVBus1857535_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857420_consumption`  
  Load '75_LVBus1857420_consumption' has phase imbalance of 40.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857680_consumption`  
  Load '75_LVBus1857680_consumption' has phase imbalance of 56.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857079_consumption`  
  Load '75_LVBus1857079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857526_consumption`  
  Load '75_LVBus1857526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857627_consumption`  
  Load '75_LVBus1857627_consumption' has phase imbalance of 51.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857098_consumption`  
  Load '75_LVBus1857098_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857093_consumption`  
  Load '75_LVBus1857093_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857200_consumption`  
  Load '75_LVBus1857200_consumption' has phase imbalance of 63.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857226_consumption`  
  Load '75_LVBus1857226_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857143_consumption`  
  Load '75_LVBus1857143_consumption' has phase imbalance of 62.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857575_consumption`  
  Load '75_LVBus1857575_consumption' has phase imbalance of 93.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857287_consumption`  
  Load '75_LVBus1857287_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857157_consumption`  
  Load '75_LVBus1857157_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857596_consumption`  
  Load '75_LVBus1857596_consumption' has phase imbalance of 53.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857152_consumption`  
  Load '75_LVBus1857152_consumption' has phase imbalance of 220.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857563_consumption`  
  Load '75_LVBus1857563_consumption' has phase imbalance of 35.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857570_consumption`  
  Load '75_LVBus1857570_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1920295_consumption`  
  Load '75_LVBus1920295_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857168_consumption`  
  Load '75_LVBus1857168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857197_consumption`  
  Load '75_LVBus1857197_consumption' has phase imbalance of 138.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857546_consumption`  
  Load '75_LVBus1857546_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857665_consumption`  
  Load '75_LVBus1857665_consumption' has phase imbalance of 76.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857319_consumption`  
  Load '75_LVBus1857319_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857223_consumption`  
  Load '75_LVBus1857223_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857462_consumption`  
  Load '75_LVBus1857462_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857380_consumption`  
  Load '75_LVBus1857380_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857191_consumption`  
  Load '75_LVBus1857191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857082_consumption`  
  Load '75_LVBus1857082_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1984041_consumption`  
  Load '75_LVBus1984041_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857343_consumption`  
  Load '75_LVBus1857343_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857106_consumption`  
  Load '75_LVBus1857106_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857101_consumption`  
  Load '75_LVBus1857101_consumption' has phase imbalance of 276.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857338_consumption`  
  Load '75_LVBus1857338_consumption' has phase imbalance of 23.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857548_consumption`  
  Load '75_LVBus1857548_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857641_consumption`  
  Load '75_LVBus1857641_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857362_consumption`  
  Load '75_LVBus1857362_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857210_consumption`  
  Load '75_LVBus1857210_consumption' has phase imbalance of 173.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857267_consumption`  
  Load '75_LVBus1857267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857284_consumption`  
  Load '75_LVBus1857284_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857495_consumption`  
  Load '75_LVBus1857495_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857248_consumption`  
  Load '75_LVBus1857248_consumption' has phase imbalance of 119.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857396_consumption`  
  Load '75_LVBus1857396_consumption' has phase imbalance of 228.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857455_consumption`  
  Load '75_LVBus1857455_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857585_consumption`  
  Load '75_LVBus1857585_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857060_consumption`  
  Load '75_LVBus1857060_consumption' has phase imbalance of 215.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857156_consumption`  
  Load '75_LVBus1857156_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857469_consumption`  
  Load '75_LVBus1857469_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857177_consumption`  
  Load '75_LVBus1857177_consumption' has phase imbalance of 107.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857071_consumption`  
  Load '75_LVBus1857071_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857415_consumption`  
  Load '75_LVBus1857415_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857490_consumption`  
  Load '75_LVBus1857490_consumption' has phase imbalance of 45.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857403_consumption`  
  Load '75_LVBus1857403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857058_consumption`  
  Load '75_LVBus1857058_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857423_consumption`  
  Load '75_LVBus1857423_consumption' has phase imbalance of 46.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857341_consumption`  
  Load '75_LVBus1857341_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857623_consumption`  
  Load '75_LVBus1857623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857525_consumption`  
  Load '75_LVBus1857525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857389_consumption`  
  Load '75_LVBus1857389_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857568_consumption`  
  Load '75_LVBus1857568_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857282_consumption`  
  Load '75_LVBus1857282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857184_consumption`  
  Load '75_LVBus1857184_consumption' has phase imbalance of 219.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857160_consumption`  
  Load '75_LVBus1857160_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857158_consumption`  
  Load '75_LVBus1857158_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857360_consumption`  
  Load '75_LVBus1857360_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857430_consumption`  
  Load '75_LVBus1857430_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857315_consumption`  
  Load '75_LVBus1857315_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857131_consumption`  
  Load '75_LVBus1857131_consumption' has phase imbalance of 60.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857653_consumption`  
  Load '75_LVBus1857653_consumption' has phase imbalance of 61.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857512_consumption`  
  Load '75_LVBus1857512_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857089_consumption`  
  Load '75_LVBus1857089_consumption' has phase imbalance of 120.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857508_consumption`  
  Load '75_LVBus1857508_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857280_consumption`  
  Load '75_LVBus1857280_consumption' has phase imbalance of 88.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857112_consumption`  
  Load '75_LVBus1857112_consumption' has phase imbalance of 85.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857447_consumption`  
  Load '75_LVBus1857447_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1920296_consumption`  
  Load '75_LVBus1920296_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857419_consumption`  
  Load '75_LVBus1857419_consumption' has phase imbalance of 134.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857561_consumption`  
  Load '75_LVBus1857561_consumption' has phase imbalance of 49.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857228_consumption`  
  Load '75_LVBus1857228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857225_consumption`  
  Load '75_LVBus1857225_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857424_consumption`  
  Load '75_LVBus1857424_consumption' has phase imbalance of 238.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857061_consumption`  
  Load '75_LVBus1857061_consumption' has phase imbalance of 271.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857354_consumption`  
  Load '75_LVBus1857354_consumption' has phase imbalance of 85.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1990527_consumption`  
  Load '75_LVBus1990527_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857574_consumption`  
  Load '75_LVBus1857574_consumption' has phase imbalance of 220.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857401_consumption`  
  Load '75_LVBus1857401_consumption' has phase imbalance of 82.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857604_consumption`  
  Load '75_LVBus1857604_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857505_consumption`  
  Load '75_LVBus1857505_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857503_consumption`  
  Load '75_LVBus1857503_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857511_consumption`  
  Load '75_LVBus1857511_consumption' has phase imbalance of 126.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857311_consumption`  
  Load '75_LVBus1857311_consumption' has phase imbalance of 141.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857301_consumption`  
  Load '75_LVBus1857301_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857668_consumption`  
  Load '75_LVBus1857668_consumption' has phase imbalance of 112.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857432_consumption`  
  Load '75_LVBus1857432_consumption' has phase imbalance of 97.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857458_consumption`  
  Load '75_LVBus1857458_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857437_consumption`  
  Load '75_LVBus1857437_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857344_consumption`  
  Load '75_LVBus1857344_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857366_consumption`  
  Load '75_LVBus1857366_consumption' has phase imbalance of 146.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857556_consumption`  
  Load '75_LVBus1857556_consumption' has phase imbalance of 48.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857359_consumption`  
  Load '75_LVBus1857359_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857230_consumption`  
  Load '75_LVBus1857230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857446_consumption`  
  Load '75_LVBus1857446_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857494_consumption`  
  Load '75_LVBus1857494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857673_consumption`  
  Load '75_LVBus1857673_consumption' has phase imbalance of 211.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857218_consumption`  
  Load '75_LVBus1857218_consumption' has phase imbalance of 223.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857492_consumption`  
  Load '75_LVBus1857492_consumption' has phase imbalance of 200.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857473_consumption`  
  Load '75_LVBus1857473_consumption' has phase imbalance of 33.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857592_consumption`  
  Load '75_LVBus1857592_consumption' has phase imbalance of 46.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857099_consumption`  
  Load '75_LVBus1857099_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857325_consumption`  
  Load '75_LVBus1857325_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857587_consumption`  
  Load '75_LVBus1857587_consumption' has phase imbalance of 39.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857080_consumption`  
  Load '75_LVBus1857080_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857448_consumption`  
  Load '75_LVBus1857448_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857440_consumption`  
  Load '75_LVBus1857440_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857452_consumption`  
  Load '75_LVBus1857452_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857075_consumption`  
  Load '75_LVBus1857075_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857425_consumption`  
  Load '75_LVBus1857425_consumption' has phase imbalance of 125.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857467_consumption`  
  Load '75_LVBus1857467_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857439_consumption`  
  Load '75_LVBus1857439_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857507_consumption`  
  Load '75_LVBus1857507_consumption' has phase imbalance of 58.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857251_consumption`  
  Load '75_LVBus1857251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857412_consumption`  
  Load '75_LVBus1857412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857135_consumption`  
  Load '75_LVBus1857135_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857265_consumption`  
  Load '75_LVBus1857265_consumption' has phase imbalance of 233.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857163_consumption`  
  Load '75_LVBus1857163_consumption' has phase imbalance of 98.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857475_consumption`  
  Load '75_LVBus1857475_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857618_consumption`  
  Load '75_LVBus1857618_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857339_consumption`  
  Load '75_LVBus1857339_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857594_consumption`  
  Load '75_LVBus1857594_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857109_consumption`  
  Load '75_LVBus1857109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1920292_consumption`  
  Load '75_LVBus1920292_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857167_consumption`  
  Load '75_LVBus1857167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857617_consumption`  
  Load '75_LVBus1857617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857577_consumption`  
  Load '75_LVBus1857577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857185_consumption`  
  Load '75_LVBus1857185_consumption' has phase imbalance of 200.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857077_consumption`  
  Load '75_LVBus1857077_consumption' has phase imbalance of 224.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857189_consumption`  
  Load '75_LVBus1857189_consumption' has phase imbalance of 106.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857181_consumption`  
  Load '75_LVBus1857181_consumption' has phase imbalance of 129.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857154_consumption`  
  Load '75_LVBus1857154_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857554_consumption`  
  Load '75_LVBus1857554_consumption' has phase imbalance of 129.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857682_consumption`  
  Load '75_LVBus1857682_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857428_consumption`  
  Load '75_LVBus1857428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857558_consumption`  
  Load '75_LVBus1857558_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857078_consumption`  
  Load '75_LVBus1857078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857519_consumption`  
  Load '75_LVBus1857519_consumption' has phase imbalance of 247.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857681_consumption`  
  Load '75_LVBus1857681_consumption' has phase imbalance of 124.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857088_consumption`  
  Load '75_LVBus1857088_consumption' has phase imbalance of 61.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857182_consumption`  
  Load '75_LVBus1857182_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857572_consumption`  
  Load '75_LVBus1857572_consumption' has phase imbalance of 141.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857268_consumption`  
  Load '75_LVBus1857268_consumption' has phase imbalance of 26.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857257_consumption`  
  Load '75_LVBus1857257_consumption' has phase imbalance of 97.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857202_consumption`  
  Load '75_LVBus1857202_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857346_consumption`  
  Load '75_LVBus1857346_consumption' has phase imbalance of 45.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857527_consumption`  
  Load '75_LVBus1857527_consumption' has phase imbalance of 22.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857421_consumption`  
  Load '75_LVBus1857421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857222_consumption`  
  Load '75_LVBus1857222_consumption' has phase imbalance of 217.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857358_consumption`  
  Load '75_LVBus1857358_consumption' has phase imbalance of 139.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857569_consumption`  
  Load '75_LVBus1857569_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857347_consumption`  
  Load '75_LVBus1857347_consumption' has phase imbalance of 102.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857329_consumption`  
  Load '75_LVBus1857329_consumption' has phase imbalance of 257.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857305_consumption`  
  Load '75_LVBus1857305_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857316_consumption`  
  Load '75_LVBus1857316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857532_consumption`  
  Load '75_LVBus1857532_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857207_consumption`  
  Load '75_LVBus1857207_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857480_consumption`  
  Load '75_LVBus1857480_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857667_consumption`  
  Load '75_LVBus1857667_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857307_consumption`  
  Load '75_LVBus1857307_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857429_consumption`  
  Load '75_LVBus1857429_consumption' has phase imbalance of 45.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857677_consumption`  
  Load '75_LVBus1857677_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857481_consumption`  
  Load '75_LVBus1857481_consumption' has phase imbalance of 104.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857581_consumption`  
  Load '75_LVBus1857581_consumption' has phase imbalance of 23.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857124_consumption`  
  Load '75_LVBus1857124_consumption' has phase imbalance of 114.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857573_consumption`  
  Load '75_LVBus1857573_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857084_consumption`  
  Load '75_LVBus1857084_consumption' has phase imbalance of 194.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857663_consumption`  
  Load '75_LVBus1857663_consumption' has phase imbalance of 56.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857070_consumption`  
  Load '75_LVBus1857070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857444_consumption`  
  Load '75_LVBus1857444_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857193_consumption`  
  Load '75_LVBus1857193_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857656_consumption`  
  Load '75_LVBus1857656_consumption' has phase imbalance of 120.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857434_consumption`  
  Load '75_LVBus1857434_consumption' has phase imbalance of 132.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857247_consumption`  
  Load '75_LVBus1857247_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857245_consumption`  
  Load '75_LVBus1857245_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857092_consumption`  
  Load '75_LVBus1857092_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857175_consumption`  
  Load '75_LVBus1857175_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857292_consumption`  
  Load '75_LVBus1857292_consumption' has phase imbalance of 20.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857104_consumption`  
  Load '75_LVBus1857104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857602_consumption`  
  Load '75_LVBus1857602_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857487_consumption`  
  Load '75_LVBus1857487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857588_consumption`  
  Load '75_LVBus1857588_consumption' has phase imbalance of 106.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857645_consumption`  
  Load '75_LVBus1857645_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857304_consumption`  
  Load '75_LVBus1857304_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857476_consumption`  
  Load '75_LVBus1857476_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857324_consumption`  
  Load '75_LVBus1857324_consumption' has phase imbalance of 73.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857579_consumption`  
  Load '75_LVBus1857579_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857066_consumption`  
  Load '75_LVBus1857066_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857136_consumption`  
  Load '75_LVBus1857136_consumption' has phase imbalance of 129.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857433_consumption`  
  Load '75_LVBus1857433_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857110_consumption`  
  Load '75_LVBus1857110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1990526_consumption`  
  Load '75_LVBus1990526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857216_consumption`  
  Load '75_LVBus1857216_consumption' has phase imbalance of 216.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857518_consumption`  
  Load '75_LVBus1857518_consumption' has phase imbalance of 206.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857214_consumption`  
  Load '75_LVBus1857214_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857486_consumption`  
  Load '75_LVBus1857486_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857624_consumption`  
  Load '75_LVBus1857624_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857529_consumption`  
  Load '75_LVBus1857529_consumption' has phase imbalance of 187.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857528_consumption`  
  Load '75_LVBus1857528_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857521_consumption`  
  Load '75_LVBus1857521_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857552_consumption`  
  Load '75_LVBus1857552_consumption' has phase imbalance of 38.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857322_consumption`  
  Load '75_LVBus1857322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857063_consumption`  
  Load '75_LVBus1857063_consumption' has phase imbalance of 26.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857422_consumption`  
  Load '75_LVBus1857422_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857113_consumption`  
  Load '75_LVBus1857113_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857062_consumption`  
  Load '75_LVBus1857062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857364_consumption`  
  Load '75_LVBus1857364_consumption' has phase imbalance of 59.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857657_consumption`  
  Load '75_LVBus1857657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857171_consumption`  
  Load '75_LVBus1857171_consumption' has phase imbalance of 242.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857056_consumption`  
  Load '75_LVBus1857056_consumption' has phase imbalance of 20.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857509_consumption`  
  Load '75_LVBus1857509_consumption' has phase imbalance of 100.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857669_consumption`  
  Load '75_LVBus1857669_consumption' has phase imbalance of 20.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857229_consumption`  
  Load '75_LVBus1857229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857345_consumption`  
  Load '75_LVBus1857345_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857083_consumption`  
  Load '75_LVBus1857083_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857081_consumption`  
  Load '75_LVBus1857081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857179_consumption`  
  Load '75_LVBus1857179_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857398_consumption`  
  Load '75_LVBus1857398_consumption' has phase imbalance of 215.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857137_consumption`  
  Load '75_LVBus1857137_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857471_consumption`  
  Load '75_LVBus1857471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857111_consumption`  
  Load '75_LVBus1857111_consumption' has phase imbalance of 246.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857068_consumption`  
  Load '75_LVBus1857068_consumption' has phase imbalance of 144.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857431_consumption`  
  Load '75_LVBus1857431_consumption' has phase imbalance of 73.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857264_consumption`  
  Load '75_LVBus1857264_consumption' has phase imbalance of 60.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857483_consumption`  
  Load '75_LVBus1857483_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857169_consumption`  
  Load '75_LVBus1857169_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1990529_consumption`  
  Load '75_LVBus1990529_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857541_consumption`  
  Load '75_LVBus1857541_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857231_consumption`  
  Load '75_LVBus1857231_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857584_consumption`  
  Load '75_LVBus1857584_consumption' has phase imbalance of 52.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857388_consumption`  
  Load '75_LVBus1857388_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857371_consumption`  
  Load '75_LVBus1857371_consumption' has phase imbalance of 104.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857474_consumption`  
  Load '75_LVBus1857474_consumption' has phase imbalance of 48.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857314_consumption`  
  Load '75_LVBus1857314_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857598_consumption`  
  Load '75_LVBus1857598_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857489_consumption`  
  Load '75_LVBus1857489_consumption' has phase imbalance of 109.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857194_consumption`  
  Load '75_LVBus1857194_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857290_consumption`  
  Load '75_LVBus1857290_consumption' has phase imbalance of 211.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857443_consumption`  
  Load '75_LVBus1857443_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857427_consumption`  
  Load '75_LVBus1857427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857161_consumption`  
  Load '75_LVBus1857161_consumption' has phase imbalance of 249.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857638_consumption`  
  Load '75_LVBus1857638_consumption' has phase imbalance of 24.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857323_consumption`  
  Load '75_LVBus1857323_consumption' has phase imbalance of 93.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857635_consumption`  
  Load '75_LVBus1857635_consumption' has phase imbalance of 47.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857372_consumption`  
  Load '75_LVBus1857372_consumption' has phase imbalance of 33.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857496_consumption`  
  Load '75_LVBus1857496_consumption' has phase imbalance of 127.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857100_consumption`  
  Load '75_LVBus1857100_consumption' has phase imbalance of 249.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857340_consumption`  
  Load '75_LVBus1857340_consumption' has phase imbalance of 29.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857126_consumption`  
  Load '75_LVBus1857126_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857155_consumption`  
  Load '75_LVBus1857155_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1920287_consumption`  
  Load '75_LVBus1920287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857258_consumption`  
  Load '75_LVBus1857258_consumption' has phase imbalance of 94.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857309_consumption`  
  Load '75_LVBus1857309_consumption' has phase imbalance of 86.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857463_consumption`  
  Load '75_LVBus1857463_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857534_consumption`  
  Load '75_LVBus1857534_consumption' has phase imbalance of 85.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857146_consumption`  
  Load '75_LVBus1857146_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857683_consumption`  
  Load '75_LVBus1857683_consumption' has phase imbalance of 124.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857545_consumption`  
  Load '75_LVBus1857545_consumption' has phase imbalance of 64.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857298_consumption`  
  Load '75_LVBus1857298_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857291_consumption`  
  Load '75_LVBus1857291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857670_consumption`  
  Load '75_LVBus1857670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857590_consumption`  
  Load '75_LVBus1857590_consumption' has phase imbalance of 50.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1920289_consumption`  
  Load '75_LVBus1920289_consumption' has phase imbalance of 133.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857328_consumption`  
  Load '75_LVBus1857328_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857208_consumption`  
  Load '75_LVBus1857208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857416_consumption`  
  Load '75_LVBus1857416_consumption' has phase imbalance of 174.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857506_consumption`  
  Load '75_LVBus1857506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857174_consumption`  
  Load '75_LVBus1857174_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857365_consumption`  
  Load '75_LVBus1857365_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857460_consumption`  
  Load '75_LVBus1857460_consumption' has phase imbalance of 47.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857504_consumption`  
  Load '75_LVBus1857504_consumption' has phase imbalance of 267.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857493_consumption`  
  Load '75_LVBus1857493_consumption' has phase imbalance of 93.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857510_consumption`  
  Load '75_LVBus1857510_consumption' has phase imbalance of 246.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857125_consumption`  
  Load '75_LVBus1857125_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857164_consumption`  
  Load '75_LVBus1857164_consumption' has phase imbalance of 89.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857147_consumption`  
  Load '75_LVBus1857147_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857095_consumption`  
  Load '75_LVBus1857095_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857069_consumption`  
  Load '75_LVBus1857069_consumption' has phase imbalance of 105.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857281_consumption`  
  Load '75_LVBus1857281_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857244_consumption`  
  Load '75_LVBus1857244_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857660_consumption`  
  Load '75_LVBus1857660_consumption' has phase imbalance of 60.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857285_consumption`  
  Load '75_LVBus1857285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857288_consumption`  
  Load '75_LVBus1857288_consumption' has phase imbalance of 21.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857176_consumption`  
  Load '75_LVBus1857176_consumption' has phase imbalance of 254.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857436_consumption`  
  Load '75_LVBus1857436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857672_consumption`  
  Load '75_LVBus1857672_consumption' has phase imbalance of 120.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857220_consumption`  
  Load '75_LVBus1857220_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857064_consumption`  
  Load '75_LVBus1857064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857263_consumption`  
  Load '75_LVBus1857263_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857065_consumption`  
  Load '75_LVBus1857065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857549_consumption`  
  Load '75_LVBus1857549_consumption' has phase imbalance of 36.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857091_consumption`  
  Load '75_LVBus1857091_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857576_consumption`  
  Load '75_LVBus1857576_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857259_consumption`  
  Load '75_LVBus1857259_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857655_consumption`  
  Load '75_LVBus1857655_consumption' has phase imbalance of 205.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857178_consumption`  
  Load '75_LVBus1857178_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1920290_consumption`  
  Load '75_LVBus1920290_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857491_consumption`  
  Load '75_LVBus1857491_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857249_consumption`  
  Load '75_LVBus1857249_consumption' has phase imbalance of 66.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857320_consumption`  
  Load '75_LVBus1857320_consumption' has phase imbalance of 90.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857628_consumption`  
  Load '75_LVBus1857628_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857517_consumption`  
  Load '75_LVBus1857517_consumption' has phase imbalance of 88.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857438_consumption`  
  Load '75_LVBus1857438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857658_consumption`  
  Load '75_LVBus1857658_consumption' has phase imbalance of 65.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857405_consumption`  
  Load '75_LVBus1857405_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857381_consumption`  
  Load '75_LVBus1857381_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857180_consumption`  
  Load '75_LVBus1857180_consumption' has phase imbalance of 248.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857464_consumption`  
  Load '75_LVBus1857464_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857094_consumption`  
  Load '75_LVBus1857094_consumption' has phase imbalance of 243.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857407_consumption`  
  Load '75_LVBus1857407_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1857286_consumption`  
  Load '75_LVBus1857286_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1136 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_FTPIN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1857538' has balanced aggregate load across 3 phase(s) (max spread 1.11%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  604 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  185 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1857050_consumption, 75_LVBus1857058_consumption, 75_LVBus1857059_consumption, 75_LVBus1857060_consumption, 75_LVBus1857061_consumption, 75_LVBus1857062_consumption, 75_LVBus1857064_consumption, 75_LVBus1857065_consumption, 75_LVBus1857066_consumption, 75_LVBus1857070_consumption, 75_LVBus1857075_consumption, 75_LVBus1857077_consumption, 75_LVBus1857078_consumption, 75_LVBus1857079_consumption, 75_LVBus1857080_consumption, 75_LVBus1857081_consumption, 75_LVBus1857082_consumption, 75_LVBus1857083_consumption, 75_LVBus1857084_consumption, 75_LVBus1857092_consumption, 75_LVBus1857094_consumption, 75_LVBus1857095_consumption, 75_LVBus1857097_consumption, 75_LVBus1857098_consumption, 75_LVBus1857099_consumption, 75_LVBus1857100_consumption, 75_LVBus1857101_consumption, 75_LVBus1857104_consumption, 75_LVBus1857109_consumption, 75_LVBus1857110_consumption, 75_LVBus1857111_consumption, 75_LVBus1857113_consumption, 75_LVBus1857126_consumption, 75_LVBus1857134_consumption, 75_LVBus1857135_consumption, 75_LVBus1857145_consumption, 75_LVBus1857146_consumption, 75_LVBus1857147_consumption, 75_LVBus1857148_consumption, 75_LVBus1857152_consumption, 75_LVBus1857153_consumption, 75_LVBus1857155_consumption, 75_LVBus1857156_consumption, 75_LVBus1857159_consumption, 75_LVBus1857167_consumption, 75_LVBus1857168_consumption, 75_LVBus1857171_consumption, 75_LVBus1857174_consumption, 75_LVBus1857176_consumption, 75_LVBus1857179_consumption, 75_LVBus1857180_consumption, 75_LVBus1857184_consumption, 75_LVBus1857185_consumption, 75_LVBus1857191_consumption, 75_LVBus1857202_consumption, 75_LVBus1857204_consumption, 75_LVBus1857205_consumption, 75_LVBus1857207_consumption, 75_LVBus1857208_consumption, 75_LVBus1857210_consumption, 75_LVBus1857212_consumption, 75_LVBus1857214_consumption, 75_LVBus1857216_consumption, 75_LVBus1857218_consumption, 75_LVBus1857222_consumption, 75_LVBus1857224_consumption, 75_LVBus1857226_consumption, 75_LVBus1857227_consumption, 75_LVBus1857228_consumption, 75_LVBus1857229_consumption, 75_LVBus1857230_consumption, 75_LVBus1857245_consumption, 75_LVBus1857251_consumption, 75_LVBus1857267_consumption, 75_LVBus1857277_consumption, 75_LVBus1857278_consumption, 75_LVBus1857281_consumption, 75_LVBus1857282_consumption, 75_LVBus1857285_consumption, 75_LVBus1857290_consumption, 75_LVBus1857291_consumption, 75_LVBus1857298_consumption, 75_LVBus1857301_consumption, 75_LVBus1857312_consumption, 75_LVBus1857315_consumption, 75_LVBus1857316_consumption, 75_LVBus1857322_consumption, 75_LVBus1857325_consumption, 75_LVBus1857329_consumption, 75_LVBus1857341_consumption, 75_LVBus1857343_consumption, 75_LVBus1857344_consumption, 75_LVBus1857348_consumption, 75_LVBus1857349_consumption, 75_LVBus1857359_consumption, 75_LVBus1857362_consumption, 75_LVBus1857388_consumption, 75_LVBus1857389_consumption, 75_LVBus1857395_consumption, 75_LVBus1857396_consumption, 75_LVBus1857398_consumption, 75_LVBus1857402_consumption, 75_LVBus1857403_consumption, 75_LVBus1857405_consumption, 75_LVBus1857407_consumption, 75_LVBus1857412_consumption, 75_LVBus1857414_consumption, 75_LVBus1857416_consumption, 75_LVBus1857418_consumption, 75_LVBus1857421_consumption, 75_LVBus1857424_consumption, 75_LVBus1857426_consumption, 75_LVBus1857427_consumption, 75_LVBus1857428_consumption, 75_LVBus1857430_consumption, 75_LVBus1857433_consumption, 75_LVBus1857436_consumption, 75_LVBus1857438_consumption, 75_LVBus1857439_consumption, 75_LVBus1857440_consumption, 75_LVBus1857443_consumption, 75_LVBus1857444_consumption, 75_LVBus1857445_consumption, 75_LVBus1857447_consumption, 75_LVBus1857452_consumption, 75_LVBus1857458_consumption, 75_LVBus1857464_consumption, 75_LVBus1857471_consumption, 75_LVBus1857476_consumption, 75_LVBus1857480_consumption, 75_LVBus1857483_consumption, 75_LVBus1857487_consumption, 75_LVBus1857492_consumption, 75_LVBus1857494_consumption, 75_LVBus1857502_consumption, 75_LVBus1857503_consumption, 75_LVBus1857504_consumption, 75_LVBus1857505_consumption, 75_LVBus1857506_consumption, 75_LVBus1857510_consumption, 75_LVBus1857512_consumption, 75_LVBus1857513_consumption, 75_LVBus1857514_consumption, 75_LVBus1857518_consumption, 75_LVBus1857519_consumption, 75_LVBus1857521_consumption, 75_LVBus1857525_consumption, 75_LVBus1857526_consumption, 75_LVBus1857529_consumption, 75_LVBus1857541_consumption, 75_LVBus1857548_consumption, 75_LVBus1857553_consumption, 75_LVBus1857558_consumption, 75_LVBus1857568_consumption, 75_LVBus1857570_consumption, 75_LVBus1857573_consumption, 75_LVBus1857574_consumption, 75_LVBus1857577_consumption, 75_LVBus1857578_consumption, 75_LVBus1857580_consumption, 75_LVBus1857585_consumption, 75_LVBus1857602_consumption, 75_LVBus1857604_consumption, 75_LVBus1857617_consumption, 75_LVBus1857619_consumption, 75_LVBus1857623_consumption, 75_LVBus1857624_consumption, 75_LVBus1857632_consumption, 75_LVBus1857636_consumption, 75_LVBus1857645_consumption, 75_LVBus1857647_consumption, 75_LVBus1857655_consumption, 75_LVBus1857657_consumption, 75_LVBus1857667_consumption, 75_LVBus1857670_consumption, 75_LVBus1857673_consumption, 75_LVBus1857677_consumption, 75_LVBus1857679_consumption, 75_LVBus1857682_consumption, 75_LVBus1920287_consumption, 75_LVBus1920290_consumption, 75_LVBus1920292_consumption, 75_LVBus1920293_consumption, 75_LVBus1990526_consumption, 75_LVBus1990529_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  568 group(s) of loads (1136 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  682 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1857050_production, 75_LVBus1857051_consumption, 75_LVBus1857051_production, 75_LVBus1857053_consumption, 75_LVBus1857053_production, 75_LVBus1857055_consumption, 75_LVBus1857055_production, 75_LVBus1857056_production, 75_LVBus1857058_production, 75_LVBus1857059_production, 75_LVBus1857060_production, 75_LVBus1857061_production, 75_LVBus1857062_production, 75_LVBus1857063_production, 75_LVBus1857064_production, 75_LVBus1857065_production, 75_LVBus1857066_production, 75_LVBus1857068_production, 75_LVBus1857069_production, 75_LVBus1857070_production, 75_LVBus1857071_production, 75_LVBus1857072_consumption, 75_LVBus1857072_production, 75_LVBus1857073_consumption, 75_LVBus1857073_production, 75_LVBus1857074_consumption, 75_LVBus1857074_production, 75_LVBus1857075_production, 75_LVBus1857077_production, 75_LVBus1857078_production, 75_LVBus1857079_production, 75_LVBus1857080_production, 75_LVBus1857081_production, 75_LVBus1857082_production, 75_LVBus1857083_production, 75_LVBus1857084_production, 75_LVBus1857086_consumption, 75_LVBus1857086_production, 75_LVBus1857087_production, 75_LVBus1857088_production, 75_LVBus1857089_production, 75_LVBus1857091_production, 75_LVBus1857092_production, 75_LVBus1857093_production, 75_LVBus1857094_production, 75_LVBus1857095_production, 75_LVBus1857096_production, 75_LVBus1857097_production, 75_LVBus1857098_production, 75_LVBus1857099_production, 75_LVBus1857100_production, 75_LVBus1857101_production, 75_LVBus1857103_consumption, 75_LVBus1857103_production, 75_LVBus1857104_production, 75_LVBus1857105_production, 75_LVBus1857106_production, 75_LVBus1857109_production, 75_LVBus1857110_production, 75_LVBus1857111_production, 75_LVBus1857112_production, 75_LVBus1857113_production, 75_LVBus1857114_consumption, 75_LVBus1857114_production, 75_LVBus1857116_consumption, 75_LVBus1857116_production, 75_LVBus1857118_consumption, 75_LVBus1857118_production, 75_LVBus1857119_consumption, 75_LVBus1857119_production, 75_LVBus1857121_consumption, 75_LVBus1857121_production, 75_LVBus1857122_consumption, 75_LVBus1857122_production, 75_LVBus1857123_consumption, 75_LVBus1857123_production, 75_LVBus1857124_production, 75_LVBus1857125_production, 75_LVBus1857126_production, 75_LVBus1857127_production, 75_LVBus1857128_consumption, 75_LVBus1857128_production, 75_LVBus1857130_consumption, 75_LVBus1857130_production, 75_LVBus1857131_production, 75_LVBus1857133_consumption, 75_LVBus1857133_production, 75_LVBus1857134_production, 75_LVBus1857135_production, 75_LVBus1857136_production, 75_LVBus1857137_production, 75_LVBus1857139_production, 75_LVBus1857140_production, 75_LVBus1857142_consumption, 75_LVBus1857142_production, 75_LVBus1857143_production, 75_LVBus1857145_production, 75_LVBus1857146_production, 75_LVBus1857147_production, 75_LVBus1857148_production, 75_LVBus1857149_consumption, 75_LVBus1857149_production, 75_LVBus1857150_consumption, 75_LVBus1857150_production, 75_LVBus1857151_production, 75_LVBus1857152_production, 75_LVBus1857153_production, 75_LVBus1857154_production, 75_LVBus1857155_production, 75_LVBus1857156_production, 75_LVBus1857157_production, 75_LVBus1857158_production, 75_LVBus1857159_production, 75_LVBus1857160_production, 75_LVBus1857161_production, 75_LVBus1857162_production, 75_LVBus1857163_production, 75_LVBus1857164_production, 75_LVBus1857165_production, 75_LVBus1857166_consumption, 75_LVBus1857166_production, 75_LVBus1857167_production, 75_LVBus1857168_production, 75_LVBus1857169_production, 75_LVBus1857170_production, 75_LVBus1857171_production, 75_LVBus1857173_production, 75_LVBus1857174_production, 75_LVBus1857175_production, 75_LVBus1857176_production, 75_LVBus1857177_production, 75_LVBus1857178_production, 75_LVBus1857179_production, 75_LVBus1857180_production, 75_LVBus1857181_production, 75_LVBus1857182_production, 75_LVBus1857184_production, 75_LVBus1857185_production, 75_LVBus1857186_consumption, 75_LVBus1857186_production, 75_LVBus1857187_production, 75_LVBus1857188_production, 75_LVBus1857189_production, 75_LVBus1857191_production, 75_LVBus1857193_production, 75_LVBus1857194_production, 75_LVBus1857195_consumption, 75_LVBus1857195_production, 75_LVBus1857196_production, 75_LVBus1857197_production, 75_LVBus1857198_production, 75_LVBus1857199_consumption, 75_LVBus1857199_production, 75_LVBus1857200_production, 75_LVBus1857201_production, 75_LVBus1857202_production, 75_LVBus1857203_consumption, 75_LVBus1857203_production, 75_LVBus1857204_production, 75_LVBus1857205_production, 75_LVBus1857206_production, 75_LVBus1857207_production, 75_LVBus1857208_production, 75_LVBus1857209_production, 75_LVBus1857210_production, 75_LVBus1857211_production, 75_LVBus1857212_production, 75_LVBus1857214_production, 75_LVBus1857216_production, 75_LVBus1857218_production, 75_LVBus1857219_consumption, 75_LVBus1857219_production, 75_LVBus1857220_production, 75_LVBus1857221_production, 75_LVBus1857222_production, 75_LVBus1857223_production, 75_LVBus1857224_production, 75_LVBus1857225_production, 75_LVBus1857226_production, 75_LVBus1857227_production, 75_LVBus1857228_production, 75_LVBus1857229_production, 75_LVBus1857230_production, 75_LVBus1857231_production, 75_LVBus1857233_production, 75_LVBus1857235_production, 75_LVBus1857236_consumption, 75_LVBus1857236_production, 75_LVBus1857238_consumption, 75_LVBus1857238_production, 75_LVBus1857239_consumption, 75_LVBus1857239_production, 75_LVBus1857240_consumption, 75_LVBus1857240_production, 75_LVBus1857241_consumption, 75_LVBus1857241_production, 75_LVBus1857242_production, 75_LVBus1857243_consumption, 75_LVBus1857243_production, 75_LVBus1857244_production, 75_LVBus1857245_production, 75_LVBus1857246_consumption, 75_LVBus1857246_production, 75_LVBus1857247_production, 75_LVBus1857248_production, 75_LVBus1857249_production, 75_LVBus1857250_consumption, 75_LVBus1857250_production, 75_LVBus1857251_production, 75_LVBus1857252_production, 75_LVBus1857254_consumption, 75_LVBus1857254_production, 75_LVBus1857255_consumption, 75_LVBus1857255_production, 75_LVBus1857256_production, 75_LVBus1857257_production, 75_LVBus1857258_production, 75_LVBus1857259_production, 75_LVBus1857260_production, 75_LVBus1857262_consumption, 75_LVBus1857262_production, 75_LVBus1857263_production, 75_LVBus1857264_production, 75_LVBus1857265_production, 75_LVBus1857266_production, 75_LVBus1857267_production, 75_LVBus1857268_production, 75_LVBus1857270_consumption, 75_LVBus1857270_production, 75_LVBus1857271_consumption, 75_LVBus1857271_production, 75_LVBus1857272_production, 75_LVBus1857273_production, 75_LVBus1857274_consumption, 75_LVBus1857274_production, 75_LVBus1857275_consumption, 75_LVBus1857275_production, 75_LVBus1857276_consumption, 75_LVBus1857276_production, 75_LVBus1857277_production, 75_LVBus1857278_production, 75_LVBus1857279_consumption, 75_LVBus1857279_production, 75_LVBus1857280_production, 75_LVBus1857281_production, 75_LVBus1857282_production, 75_LVBus1857283_production, 75_LVBus1857284_production, 75_LVBus1857285_production, 75_LVBus1857286_production, 75_LVBus1857287_production, 75_LVBus1857288_production, 75_LVBus1857289_consumption, 75_LVBus1857289_production, 75_LVBus1857290_production, 75_LVBus1857291_production, 75_LVBus1857292_production, 75_LVBus1857294_production, 75_LVBus1857295_production, 75_LVBus1857297_consumption, 75_LVBus1857297_production, 75_LVBus1857298_production, 75_LVBus1857299_production, 75_LVBus1857300_consumption, 75_LVBus1857300_production, 75_LVBus1857301_production, 75_LVBus1857302_production, 75_LVBus1857303_production, 75_LVBus1857304_production, 75_LVBus1857305_production, 75_LVBus1857307_production, 75_LVBus1857309_production, 75_LVBus1857311_production, 75_LVBus1857312_production, 75_LVBus1857313_consumption, 75_LVBus1857313_production, 75_LVBus1857314_production, 75_LVBus1857315_production, 75_LVBus1857316_production, 75_LVBus1857318_production, 75_LVBus1857319_production, 75_LVBus1857320_production, 75_LVBus1857322_production, 75_LVBus1857323_production, 75_LVBus1857324_production, 75_LVBus1857325_production, 75_LVBus1857328_production, 75_LVBus1857329_production, 75_LVBus1857330_production, 75_LVBus1857331_consumption, 75_LVBus1857331_production, 75_LVBus1857332_consumption, 75_LVBus1857332_production, 75_LVBus1857335_consumption, 75_LVBus1857335_production, 75_LVBus1857336_consumption, 75_LVBus1857336_production, 75_LVBus1857337_consumption, 75_LVBus1857337_production, 75_LVBus1857338_production, 75_LVBus1857339_production, 75_LVBus1857340_production, 75_LVBus1857341_production, 75_LVBus1857343_production, 75_LVBus1857344_production, 75_LVBus1857345_production, 75_LVBus1857346_production, 75_LVBus1857347_production, 75_LVBus1857348_production, 75_LVBus1857349_production, 75_LVBus1857350_production, 75_LVBus1857352_consumption, 75_LVBus1857352_production, 75_LVBus1857353_consumption, 75_LVBus1857353_production, 75_LVBus1857354_production, 75_LVBus1857355_production, 75_LVBus1857356_consumption, 75_LVBus1857356_production, 75_LVBus1857357_consumption, 75_LVBus1857357_production, 75_LVBus1857358_production, 75_LVBus1857359_production, 75_LVBus1857360_production, 75_LVBus1857362_production, 75_LVBus1857363_consumption, 75_LVBus1857363_production, 75_LVBus1857364_production, 75_LVBus1857365_production, 75_LVBus1857366_production, 75_LVBus1857367_production, 75_LVBus1857368_production, 75_LVBus1857369_consumption, 75_LVBus1857369_production, 75_LVBus1857370_production, 75_LVBus1857371_production, 75_LVBus1857372_production, 75_LVBus1857373_production, 75_LVBus1857375_production, 75_LVBus1857376_consumption, 75_LVBus1857376_production, 75_LVBus1857377_consumption, 75_LVBus1857377_production, 75_LVBus1857378_consumption, 75_LVBus1857378_production, 75_LVBus1857379_production, 75_LVBus1857380_production, 75_LVBus1857381_production, 75_LVBus1857382_production, 75_LVBus1857385_consumption, 75_LVBus1857385_production, 75_LVBus1857386_consumption, 75_LVBus1857386_production, 75_LVBus1857388_production, 75_LVBus1857389_production, 75_LVBus1857391_consumption, 75_LVBus1857391_production, 75_LVBus1857392_consumption, 75_LVBus1857392_production, 75_LVBus1857393_consumption, 75_LVBus1857393_production, 75_LVBus1857394_production, 75_LVBus1857395_production, 75_LVBus1857396_production, 75_LVBus1857397_production, 75_LVBus1857398_production, 75_LVBus1857400_consumption, 75_LVBus1857400_production, 75_LVBus1857401_production, 75_LVBus1857402_production, 75_LVBus1857403_production, 75_LVBus1857404_production, 75_LVBus1857405_production, 75_LVBus1857407_production, 75_LVBus1857408_consumption, 75_LVBus1857408_production, 75_LVBus1857409_consumption, 75_LVBus1857409_production, 75_LVBus1857410_consumption, 75_LVBus1857410_production, 75_LVBus1857411_consumption, 75_LVBus1857411_production, 75_LVBus1857412_production, 75_LVBus1857413_production, 75_LVBus1857414_production, 75_LVBus1857415_production, 75_LVBus1857416_production, 75_LVBus1857417_consumption, 75_LVBus1857417_production, 75_LVBus1857418_production, 75_LVBus1857419_production, 75_LVBus1857420_production, 75_LVBus1857421_production, 75_LVBus1857422_production, 75_LVBus1857423_production, 75_LVBus1857424_production, 75_LVBus1857425_production, 75_LVBus1857426_production, 75_LVBus1857427_production, 75_LVBus1857428_production, 75_LVBus1857429_production, 75_LVBus1857430_production, 75_LVBus1857431_production, 75_LVBus1857432_production, 75_LVBus1857433_production, 75_LVBus1857434_production, 75_LVBus1857435_consumption, 75_LVBus1857435_production, 75_LVBus1857436_production, 75_LVBus1857437_production, 75_LVBus1857438_production, 75_LVBus1857439_production, 75_LVBus1857440_production, 75_LVBus1857441_consumption, 75_LVBus1857441_production, 75_LVBus1857442_consumption, 75_LVBus1857442_production, 75_LVBus1857443_production, 75_LVBus1857444_production, 75_LVBus1857445_production, 75_LVBus1857446_production, 75_LVBus1857447_production, 75_LVBus1857448_production, 75_LVBus1857449_production, 75_LVBus1857451_consumption, 75_LVBus1857451_production, 75_LVBus1857452_production, 75_LVBus1857453_consumption, 75_LVBus1857453_production, 75_LVBus1857454_production, 75_LVBus1857455_production, 75_LVBus1857456_production, 75_LVBus1857457_production, 75_LVBus1857458_production, 75_LVBus1857459_production, 75_LVBus1857460_production, 75_LVBus1857461_consumption, 75_LVBus1857461_production, 75_LVBus1857462_production, 75_LVBus1857463_production, 75_LVBus1857464_production, 75_LVBus1857465_consumption, 75_LVBus1857465_production, 75_LVBus1857466_production, 75_LVBus1857467_production, 75_LVBus1857468_production, 75_LVBus1857469_production, 75_LVBus1857470_consumption, 75_LVBus1857470_production, 75_LVBus1857471_production, 75_LVBus1857472_consumption, 75_LVBus1857472_production, 75_LVBus1857473_production, 75_LVBus1857474_production, 75_LVBus1857475_production, 75_LVBus1857476_production, 75_LVBus1857478_consumption, 75_LVBus1857478_production, 75_LVBus1857479_production, 75_LVBus1857480_production, 75_LVBus1857481_production, 75_LVBus1857482_consumption, 75_LVBus1857482_production, 75_LVBus1857483_production, 75_LVBus1857484_production, 75_LVBus1857485_consumption, 75_LVBus1857485_production, 75_LVBus1857486_production, 75_LVBus1857487_production, 75_LVBus1857488_production, 75_LVBus1857489_production, 75_LVBus1857490_production, 75_LVBus1857491_production, 75_LVBus1857492_production, 75_LVBus1857493_production, 75_LVBus1857494_production, 75_LVBus1857495_production, 75_LVBus1857496_production, 75_LVBus1857502_production, 75_LVBus1857503_production, 75_LVBus1857504_production, 75_LVBus1857505_production, 75_LVBus1857506_production, 75_LVBus1857507_production, 75_LVBus1857508_production, 75_LVBus1857509_production, 75_LVBus1857510_production, 75_LVBus1857511_production, 75_LVBus1857512_production, 75_LVBus1857513_production, 75_LVBus1857514_production, 75_LVBus1857515_production, 75_LVBus1857516_production, 75_LVBus1857517_production, 75_LVBus1857518_production, 75_LVBus1857519_production, 75_LVBus1857520_production, 75_LVBus1857521_production, 75_LVBus1857523_consumption, 75_LVBus1857523_production, 75_LVBus1857524_consumption, 75_LVBus1857524_production, 75_LVBus1857525_production, 75_LVBus1857526_production, 75_LVBus1857527_production, 75_LVBus1857528_production, 75_LVBus1857529_production, 75_LVBus1857531_consumption, 75_LVBus1857531_production, 75_LVBus1857532_production, 75_LVBus1857533_production, 75_LVBus1857534_production, 75_LVBus1857535_production, 75_LVBus1857538_production, 75_LVBus1857540_consumption, 75_LVBus1857540_production, 75_LVBus1857541_production, 75_LVBus1857542_production, 75_LVBus1857544_production, 75_LVBus1857545_production, 75_LVBus1857546_production, 75_LVBus1857547_production, 75_LVBus1857548_production, 75_LVBus1857549_production, 75_LVBus1857550_production, 75_LVBus1857551_consumption, 75_LVBus1857551_production, 75_LVBus1857552_production, 75_LVBus1857553_production, 75_LVBus1857554_production, 75_LVBus1857556_production, 75_LVBus1857558_production, 75_LVBus1857560_consumption, 75_LVBus1857560_production, 75_LVBus1857561_production, 75_LVBus1857563_production, 75_LVBus1857564_production, 75_LVBus1857565_consumption, 75_LVBus1857565_production, 75_LVBus1857566_production, 75_LVBus1857567_consumption, 75_LVBus1857567_production, 75_LVBus1857568_production, 75_LVBus1857569_production, 75_LVBus1857570_production, 75_LVBus1857571_production, 75_LVBus1857572_production, 75_LVBus1857573_production, 75_LVBus1857574_production, 75_LVBus1857575_production, 75_LVBus1857576_production, 75_LVBus1857577_production, 75_LVBus1857578_production, 75_LVBus1857579_production, 75_LVBus1857580_production, 75_LVBus1857581_production, 75_LVBus1857582_production, 75_LVBus1857583_consumption, 75_LVBus1857583_production, 75_LVBus1857584_production, 75_LVBus1857585_production, 75_LVBus1857587_production, 75_LVBus1857588_production, 75_LVBus1857590_production, 75_LVBus1857591_production, 75_LVBus1857592_production, 75_LVBus1857594_production, 75_LVBus1857595_production, 75_LVBus1857596_production, 75_LVBus1857597_production, 75_LVBus1857598_production, 75_LVBus1857599_production, 75_LVBus1857600_consumption, 75_LVBus1857600_production, 75_LVBus1857602_production, 75_LVBus1857603_consumption, 75_LVBus1857603_production, 75_LVBus1857604_production, 75_LVBus1857605_production, 75_LVBus1857606_consumption, 75_LVBus1857606_production, 75_LVBus1857607_production, 75_LVBus1857608_consumption, 75_LVBus1857608_production, 75_LVBus1857609_production, 75_LVBus1857611_production, 75_LVBus1857613_consumption, 75_LVBus1857613_production, 75_LVBus1857614_production, 75_LVBus1857615_consumption, 75_LVBus1857615_production, 75_LVBus1857617_production, 75_LVBus1857618_production, 75_LVBus1857619_production, 75_LVBus1857620_consumption, 75_LVBus1857620_production, 75_LVBus1857621_production, 75_LVBus1857622_production, 75_LVBus1857623_production, 75_LVBus1857624_production, 75_LVBus1857625_consumption, 75_LVBus1857625_production, 75_LVBus1857626_production, 75_LVBus1857627_production, 75_LVBus1857628_production, 75_LVBus1857630_consumption, 75_LVBus1857630_production, 75_LVBus1857631_production, 75_LVBus1857632_production, 75_LVBus1857633_consumption, 75_LVBus1857633_production, 75_LVBus1857635_production, 75_LVBus1857636_production, 75_LVBus1857638_production, 75_LVBus1857639_production, 75_LVBus1857640_production, 75_LVBus1857641_production, 75_LVBus1857642_production, 75_LVBus1857643_production, 75_LVBus1857644_consumption, 75_LVBus1857644_production, 75_LVBus1857645_production, 75_LVBus1857646_production, 75_LVBus1857647_production, 75_LVBus1857648_consumption, 75_LVBus1857648_production, 75_LVBus1857649_production, 75_LVBus1857651_production, 75_LVBus1857653_production, 75_LVBus1857654_production, 75_LVBus1857655_production, 75_LVBus1857656_production, 75_LVBus1857657_production, 75_LVBus1857658_production, 75_LVBus1857660_production, 75_LVBus1857661_consumption, 75_LVBus1857661_production, 75_LVBus1857663_production, 75_LVBus1857665_production, 75_LVBus1857667_production, 75_LVBus1857668_production, 75_LVBus1857669_production, 75_LVBus1857670_production, 75_LVBus1857672_production, 75_LVBus1857673_production, 75_LVBus1857674_consumption, 75_LVBus1857674_production, 75_LVBus1857676_consumption, 75_LVBus1857676_production, 75_LVBus1857677_production, 75_LVBus1857678_production, 75_LVBus1857679_production, 75_LVBus1857680_production, 75_LVBus1857681_production, 75_LVBus1857682_production, 75_LVBus1857683_production, 75_LVBus1920286_consumption, 75_LVBus1920286_production, 75_LVBus1920287_production, 75_LVBus1920288_production, 75_LVBus1920289_production, 75_LVBus1920290_production, 75_LVBus1920291_consumption, 75_LVBus1920291_production, 75_LVBus1920292_production, 75_LVBus1920293_production, 75_LVBus1920294_consumption, 75_LVBus1920294_production, 75_LVBus1920295_production, 75_LVBus1920296_production, 75_LVBus1920297_production, 75_LVBus1984040_consumption, 75_LVBus1984040_production, 75_LVBus1984041_production, 75_LVBus1990526_production, 75_LVBus1990527_production, 75_LVBus1990528_production, 75_LVBus1990529_production, 75_LVBus1990530_consumption, 75_LVBus1990530_production, 75_MVLV067938_production, 75_MVLV121510_production.

