# BMOPF Network Summary: 93_MVFeeder1230

**Generated:** 2026-10-01 23:34:49  
**Findings:** 0 errors · 5 warnings · 228 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 38 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 491 |  |
| line | 452 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 764 | 1.812 MW, 543.5 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 38 |  |
| switch | 0 |  |
| transformer | 38 | Dyn11×38 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 78 | 77 | 14 | 0 |
| LV_236V | 236.0 V | 413 | 375 | 750 | 0 |

**Transformer transitions:**

- `93_MVLV13060_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV15812_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV42744_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV56831_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV25483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV49220_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV51493_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV35482_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV64866_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV57286_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV66296_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV63037_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV71861_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV10208_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV55320_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV12836_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV56998_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV15583_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV10234_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV10271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV60718_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV42039_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV58424_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV27291_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV63985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV25478_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV25536_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV73568_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV01419_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV63988_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV58420_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV16364_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV66516_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV15818_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV20333_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV21218_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV64233_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV10254_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 11 |
| Degree-1 buses | 173 |
| Tree depth (max hops) | 36 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 491 | 1 | 490 | 0 | 0 | 0 |
| Tier LV_236V | 413 | 38 | 375 | 0 | 0 | 0 |
| Tier MV_11.8kV | 78 | 1 | 77 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 38; skipped invalid branches: 0.

Galvanic zones: 39; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 93_GRIM5 | MV_11.8kV | 78 | 0 | 0 | 38 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1886 declared bus terminals; 1731 mapped line/closed-switch conductor edges; 155 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 35300.0 | 3.694 | 2292 |
| q_nom | 0.0 | 10600.0 | 3.694 | 2292 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.126 | 2980.0 | 1.769 | 452 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 2.2e6 | 1.507 | 38 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 528 of 764 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869959_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870087_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869846_consumption' has phase imbalance of 253.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869680_consumption' has phase imbalance of 217.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869963_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869806_consumption' has phase imbalance of 232.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870037_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869917_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870134_consumption' has phase imbalance of 275.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869911_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869742_consumption' has phase imbalance of 258.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869921_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870093_consumption' has phase imbalance of 39.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869896_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869964_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870077_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869998_consumption' has phase imbalance of 263.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1393153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869949_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869970_consumption' has phase imbalance of 140.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869829_consumption' has phase imbalance of 276.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869914_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870044_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869843_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869938_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870072_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869913_consumption' has phase imbalance of 267.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869972_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870046_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869941_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870010_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869832_consumption' has phase imbalance of 240.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869981_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870042_consumption' has phase imbalance of 91.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869954_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869976_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869738_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869885_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869990_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869920_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1392505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869958_consumption' has phase imbalance of 50.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869897_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869988_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869986_consumption' has phase imbalance of 274.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870038_consumption' has phase imbalance of 251.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869870_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869943_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869937_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870001_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870135_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869834_consumption' has phase imbalance of 148.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870068_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869740_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870102_consumption' has phase imbalance of 98.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870050_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870047_consumption' has phase imbalance of 67.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869974_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869894_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869889_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869681_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869910_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869951_consumption' has phase imbalance of 85.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870101_consumption' has phase imbalance of 267.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869955_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869845_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869906_consumption' has phase imbalance of 42.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869947_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870098_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869944_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869912_consumption' has phase imbalance of 66.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1374127_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869727_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870034_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869957_consumption' has phase imbalance of 164.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869739_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869891_consumption' has phase imbalance of 139.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1393151_consumption' has phase imbalance of 175.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869836_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870132_consumption' has phase imbalance of 221.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870089_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869844_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869761_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869989_consumption' has phase imbalance of 207.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869960_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870075_consumption' has phase imbalance of 132.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870015_consumption' has phase imbalance of 107.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869697_consumption' has phase imbalance of 185.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869925_consumption' has phase imbalance of 67.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869801_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870005_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869971_consumption' has phase imbalance of 207.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869946_consumption' has phase imbalance of 251.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870036_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870096_consumption' has phase imbalance of 288.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869719_consumption' has phase imbalance of 227.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869982_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869685_consumption' has phase imbalance of 114.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869930_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869720_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870009_consumption' has phase imbalance of 76.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870058_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1418957_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1372213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869931_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870099_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870069_consumption' has phase imbalance of 167.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869717_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869997_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869928_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869919_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1414054_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869915_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870076_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869858_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870003_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869728_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1393152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869747_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869729_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870090_consumption' has phase imbalance of 283.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869755_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870092_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869864_consumption' has phase imbalance of 242.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0869983_consumption' has phase imbalance of 210.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0870029_consumption' has phase imbalance of 266.9%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 764 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0869700' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0869811' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0869776' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0870027' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.812 MW |
| Total load Q | 543.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 93_MVLV13060_Transformer | 176.0 kVA | 22.0% |
| 93_MVLV15812_Transformer | 110.0 kVA | 16.3% |
| 93_MVLV42744_Transformer | 110.0 kVA | 7.4% |
| 93_MVLV56831_Transformer | 110.0 kVA | 9.2% |
| 93_MVLV25483_Transformer | 110.0 kVA | 11.1% |
| 93_MVLV49220_Transformer | 176.0 kVA | 29.0% |
| 93_MVLV51493_Transformer | 110.0 kVA | 44.1% |
| 93_MVLV35482_Transformer | 110.0 kVA | 0.0% |
| 93_MVLV64866_Transformer | 110.0 kVA | 0.7% |
| 93_MVLV57286_Transformer | 275.0 kVA | 45.0% |
| 93_MVLV66296_Transformer | 176.0 kVA | 20.4% |
| 93_MVLV63037_Transformer | 176.0 kVA | 0.0% |
| 93_MVLV71861_Transformer | 275.0 kVA | 26.2% |
| 93_MVLV10208_Transformer | 176.0 kVA | 0.0% |
| 93_MVLV55320_Transformer | 275.0 kVA | 41.8% |
| 93_MVLV12836_Transformer | 110.0 kVA | 21.9% |
| 93_MVLV56998_Transformer | 110.0 kVA | 10.1% |
| 93_MVLV15583_Transformer | 110.0 kVA | 12.6% |
| 93_MVLV10234_Transformer | 110.0 kVA | 29.6% |
| 93_MVLV10271_Transformer | 110.0 kVA | 26.5% |
| 93_MVLV60718_Transformer | 110.0 kVA | 41.2% |
| 93_MVLV42039_Transformer | 176.0 kVA | 44.5% |
| 93_MVLV58424_Transformer | 275.0 kVA | 36.9% |
| 93_MVLV27291_Transformer | 110.0 kVA | 3.0% |
| 93_MVLV63985_Transformer | 110.0 kVA | 13.7% |
| 93_MVLV25478_Transformer | 110.0 kVA | 4.1% |
| 93_MVLV25536_Transformer | 176.0 kVA | 41.0% |
| 93_MVLV73568_Transformer | 2.2 MVA | 19.2% |
| 93_MVLV01419_Transformer | 176.0 kVA | 19.2% |
| 93_MVLV63988_Transformer | 110.0 kVA | 2.3% |
| 93_MVLV58420_Transformer | 275.0 kVA | 7.5% |
| 93_MVLV16364_Transformer | 440.0 kVA | 21.3% |
| 93_MVLV66516_Transformer | 176.0 kVA | 47.9% |
| 93_MVLV15818_Transformer | 110.0 kVA | 20.5% |
| 93_MVLV20333_Transformer | 275.0 kVA | 15.1% |
| 93_MVLV21218_Transformer | 110.0 kVA | 0.8% |
| 93_MVLV64233_Transformer | 176.0 kVA | 47.9% |
| 93_MVLV10254_Transformer | 440.0 kVA | 27.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.81 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '93_GRIM5' (MV, 11.78 kV) has an electrical reach of 24.66 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '93_LVBus0869967' (LV, 0.24 kV) has an electrical reach of 1.19 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '93_LVBus0870029' (LV, 0.24 kV) has an electrical reach of 6.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '93_LVBus0870062' (LV, 0.24 kV) has an electrical reach of 1.36 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '93_LVBus0869727' (LV, 0.24 kV) has an electrical reach of 1.16 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '93_LVBus0870025' (LV, 0.24 kV) has an electrical reach of 14.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '93_LVBus0870027' (LV, 0.24 kV) has an electrical reach of 9.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 491 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 491 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 38 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 78 |
| LV_236V | 4-wire | 413 / 413 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 413 |
| Neutral branches | 375 |
| Grounding points | 38 |
| Neutral sections | 38 |
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
| 11.78 kV | 78 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 3 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, O_AM_54, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 5 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 3 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, O_AM_54, U_AL_150.
> 🔵 **[I.PROV.LINE_SWITCH_LIKE]** Line '93_LVBranch1216351' has near-zero series impedance and may be modelled more accurately as a switch: effective impedance (Z·length) < 0.0001 Ω on all diagonals.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 39 |
| Islands without voltage reference | 0 |
| Line impedance spread | 34800.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 413 / 78 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 529 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 529 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0869679_production, 93_LVBus0869680_production, 93_LVBus0869681_production, 93_LVBus0869682_production, 93_LVBus0869683_production, 93_LVBus0869685_production, 93_LVBus0869686_production, 93_LVBus0869688_consumption, 93_LVBus0869688_production, 93_LVBus0869690_consumption, 93_LVBus0869690_production, 93_LVBus0869692_production, 93_LVBus0869694_consumption, 93_LVBus0869694_production, 93_LVBus0869695_production, 93_LVBus0869696_production, 93_LVBus0869697_production, 93_LVBus0869698_production, 93_LVBus0869700_consumption, 93_LVBus0869700_production, 93_LVBus0869701_production, 93_LVBus0869703_consumption, 93_LVBus0869703_production, 93_LVBus0869704_consumption, 93_LVBus0869704_production, 93_LVBus0869705_consumption, 93_LVBus0869705_production, 93_LVBus0869707_consumption, 93_LVBus0869707_production, 93_LVBus0869709_consumption, 93_LVBus0869709_production, 93_LVBus0869710_production, 93_LVBus0869712_production, 93_LVBus0869716_consumption, 93_LVBus0869716_production, 93_LVBus0869717_production, 93_LVBus0869718_consumption, 93_LVBus0869718_production, 93_LVBus0869719_production, 93_LVBus0869720_production, 93_LVBus0869721_production, 93_LVBus0869722_consumption, 93_LVBus0869722_production, 93_LVBus0869723_production, 93_LVBus0869727_production, 93_LVBus0869728_production, 93_LVBus0869729_production, 93_LVBus0869730_production, 93_LVBus0869731_production, 93_LVBus0869732_production, 93_LVBus0869734_production, 93_LVBus0869735_production, 93_LVBus0869736_production, 93_LVBus0869737_production, 93_LVBus0869738_production, 93_LVBus0869739_production, 93_LVBus0869740_production, 93_LVBus0869741_consumption, 93_LVBus0869741_production, 93_LVBus0869742_production, 93_LVBus0869744_production, 93_LVBus0869746_consumption, 93_LVBus0869746_production, 93_LVBus0869747_production, 93_LVBus0869748_consumption, 93_LVBus0869748_production, 93_LVBus0869749_production, 93_LVBus0869750_consumption, 93_LVBus0869750_production, 93_LVBus0869751_consumption, 93_LVBus0869751_production, 93_LVBus0869753_consumption, 93_LVBus0869753_production, 93_LVBus0869754_consumption, 93_LVBus0869754_production, 93_LVBus0869755_production, 93_LVBus0869760_production, 93_LVBus0869761_production, 93_LVBus0869762_consumption, 93_LVBus0869762_production, 93_LVBus0869766_production, 93_LVBus0869767_production, 93_LVBus0869768_consumption, 93_LVBus0869768_production, 93_LVBus0869769_production, 93_LVBus0869770_consumption, 93_LVBus0869770_production, 93_LVBus0869771_production, 93_LVBus0869772_production, 93_LVBus0869776_consumption, 93_LVBus0869776_production, 93_LVBus0869777_consumption, 93_LVBus0869777_production, 93_LVBus0869778_consumption, 93_LVBus0869778_production, 93_LVBus0869779_production, 93_LVBus0869780_consumption, 93_LVBus0869780_production, 93_LVBus0869782_consumption, 93_LVBus0869782_production, 93_LVBus0869783_production, 93_LVBus0869785_consumption, 93_LVBus0869785_production, 93_LVBus0869786_consumption, 93_LVBus0869786_production, 93_LVBus0869787_consumption, 93_LVBus0869787_production, 93_LVBus0869789_consumption, 93_LVBus0869789_production, 93_LVBus0869790_consumption, 93_LVBus0869790_production, 93_LVBus0869791_consumption, 93_LVBus0869791_production, 93_LVBus0869792_consumption, 93_LVBus0869792_production, 93_LVBus0869793_consumption, 93_LVBus0869793_production, 93_LVBus0869795_consumption, 93_LVBus0869795_production, 93_LVBus0869796_production, 93_LVBus0869797_production, 93_LVBus0869798_consumption, 93_LVBus0869798_production, 93_LVBus0869799_consumption, 93_LVBus0869799_production, 93_LVBus0869800_consumption, 93_LVBus0869800_production, 93_LVBus0869801_production, 93_LVBus0869802_production, 93_LVBus0869803_consumption, 93_LVBus0869803_production, 93_LVBus0869804_consumption, 93_LVBus0869804_production, 93_LVBus0869805_production, 93_LVBus0869806_production, 93_LVBus0869807_production, 93_LVBus0869811_production, 93_LVBus0869813_production, 93_LVBus0869814_consumption, 93_LVBus0869814_production, 93_LVBus0869815_consumption, 93_LVBus0869815_production, 93_LVBus0869816_production, 93_LVBus0869817_production, 93_LVBus0869818_consumption, 93_LVBus0869818_production, 93_LVBus0869819_consumption, 93_LVBus0869819_production, 93_LVBus0869821_consumption, 93_LVBus0869821_production, 93_LVBus0869822_production, 93_LVBus0869823_consumption, 93_LVBus0869823_production, 93_LVBus0869824_production, 93_LVBus0869825_consumption, 93_LVBus0869825_production, 93_LVBus0869826_consumption, 93_LVBus0869826_production, 93_LVBus0869827_production, 93_LVBus0869828_consumption, 93_LVBus0869828_production, 93_LVBus0869829_production, 93_LVBus0869831_production, 93_LVBus0869832_production, 93_LVBus0869833_consumption, 93_LVBus0869833_production, 93_LVBus0869834_production, 93_LVBus0869835_consumption, 93_LVBus0869835_production, 93_LVBus0869836_production, 93_LVBus0869837_production, 93_LVBus0869838_production, 93_LVBus0869839_production, 93_LVBus0869840_production, 93_LVBus0869842_production, 93_LVBus0869843_production, 93_LVBus0869844_production, 93_LVBus0869845_production, 93_LVBus0869846_production, 93_LVBus0869848_production, 93_LVBus0869849_production, 93_LVBus0869850_consumption, 93_LVBus0869850_production, 93_LVBus0869852_consumption, 93_LVBus0869852_production, 93_LVBus0869857_consumption, 93_LVBus0869857_production, 93_LVBus0869858_production, 93_LVBus0869859_production, 93_LVBus0869861_consumption, 93_LVBus0869861_production, 93_LVBus0869862_production, 93_LVBus0869863_consumption, 93_LVBus0869863_production, 93_LVBus0869864_production, 93_LVBus0869866_consumption, 93_LVBus0869866_production, 93_LVBus0869867_consumption, 93_LVBus0869867_production, 93_LVBus0869868_consumption, 93_LVBus0869868_production, 93_LVBus0869869_production, 93_LVBus0869870_production, 93_LVBus0869872_consumption, 93_LVBus0869872_production, 93_LVBus0869873_consumption, 93_LVBus0869873_production, 93_LVBus0869874_consumption, 93_LVBus0869874_production, 93_LVBus0869875_production, 93_LVBus0869876_consumption, 93_LVBus0869876_production, 93_LVBus0869877_production, 93_LVBus0869878_consumption, 93_LVBus0869878_production, 93_LVBus0869879_consumption, 93_LVBus0869879_production, 93_LVBus0869880_production, 93_LVBus0869884_production, 93_LVBus0869885_production, 93_LVBus0869886_consumption, 93_LVBus0869886_production, 93_LVBus0869888_consumption, 93_LVBus0869888_production, 93_LVBus0869889_production, 93_LVBus0869890_production, 93_LVBus0869891_production, 93_LVBus0869892_production, 93_LVBus0869893_consumption, 93_LVBus0869893_production, 93_LVBus0869894_production, 93_LVBus0869896_production, 93_LVBus0869897_production, 93_LVBus0869901_consumption, 93_LVBus0869901_production, 93_LVBus0869902_production, 93_LVBus0869904_consumption, 93_LVBus0869904_production, 93_LVBus0869905_consumption, 93_LVBus0869905_production, 93_LVBus0869906_production, 93_LVBus0869907_production, 93_LVBus0869909_consumption, 93_LVBus0869909_production, 93_LVBus0869910_production, 93_LVBus0869911_production, 93_LVBus0869912_production, 93_LVBus0869913_production, 93_LVBus0869914_production, 93_LVBus0869915_production, 93_LVBus0869916_consumption, 93_LVBus0869916_production, 93_LVBus0869917_production, 93_LVBus0869919_production, 93_LVBus0869920_production, 93_LVBus0869921_production, 93_LVBus0869923_production, 93_LVBus0869924_production, 93_LVBus0869925_production, 93_LVBus0869927_production, 93_LVBus0869928_production, 93_LVBus0869930_production, 93_LVBus0869931_production, 93_LVBus0869932_consumption, 93_LVBus0869932_production, 93_LVBus0869936_consumption, 93_LVBus0869936_production, 93_LVBus0869937_production, 93_LVBus0869938_production, 93_LVBus0869940_consumption, 93_LVBus0869940_production, 93_LVBus0869941_production, 93_LVBus0869943_production, 93_LVBus0869944_production, 93_LVBus0869945_production, 93_LVBus0869946_production, 93_LVBus0869947_production, 93_LVBus0869949_production, 93_LVBus0869950_consumption, 93_LVBus0869950_production, 93_LVBus0869951_production, 93_LVBus0869952_consumption, 93_LVBus0869952_production, 93_LVBus0869953_consumption, 93_LVBus0869953_production, 93_LVBus0869954_production, 93_LVBus0869955_production, 93_LVBus0869956_consumption, 93_LVBus0869956_production, 93_LVBus0869957_production, 93_LVBus0869958_production, 93_LVBus0869959_production, 93_LVBus0869960_production, 93_LVBus0869961_consumption, 93_LVBus0869961_production, 93_LVBus0869962_production, 93_LVBus0869963_production, 93_LVBus0869964_production, 93_LVBus0869965_production, 93_LVBus0869967_consumption, 93_LVBus0869967_production, 93_LVBus0869968_consumption, 93_LVBus0869968_production, 93_LVBus0869969_consumption, 93_LVBus0869969_production, 93_LVBus0869970_production, 93_LVBus0869971_production, 93_LVBus0869972_production, 93_LVBus0869973_production, 93_LVBus0869974_production, 93_LVBus0869975_production, 93_LVBus0869976_production, 93_LVBus0869977_production, 93_LVBus0869978_production, 93_LVBus0869979_production, 93_LVBus0869980_consumption, 93_LVBus0869980_production, 93_LVBus0869981_production, 93_LVBus0869982_production, 93_LVBus0869983_production, 93_LVBus0869985_consumption, 93_LVBus0869985_production, 93_LVBus0869986_production, 93_LVBus0869988_production, 93_LVBus0869989_production, 93_LVBus0869990_production, 93_LVBus0869991_production, 93_LVBus0869993_consumption, 93_LVBus0869993_production, 93_LVBus0869994_consumption, 93_LVBus0869994_production, 93_LVBus0869995_consumption, 93_LVBus0869995_production, 93_LVBus0869996_production, 93_LVBus0869997_production, 93_LVBus0869998_production, 93_LVBus0869999_consumption, 93_LVBus0869999_production, 93_LVBus0870000_production, 93_LVBus0870001_production, 93_LVBus0870002_consumption, 93_LVBus0870002_production, 93_LVBus0870003_production, 93_LVBus0870004_production, 93_LVBus0870005_production, 93_LVBus0870007_production, 93_LVBus0870008_production, 93_LVBus0870009_production, 93_LVBus0870010_production, 93_LVBus0870013_production, 93_LVBus0870014_consumption, 93_LVBus0870014_production, 93_LVBus0870015_production, 93_LVBus0870016_production, 93_LVBus0870017_consumption, 93_LVBus0870017_production, 93_LVBus0870018_consumption, 93_LVBus0870018_production, 93_LVBus0870019_consumption, 93_LVBus0870019_production, 93_LVBus0870020_production, 93_LVBus0870021_production, 93_LVBus0870025_consumption, 93_LVBus0870025_production, 93_LVBus0870027_production, 93_LVBus0870029_production, 93_LVBus0870031_production, 93_LVBus0870033_production, 93_LVBus0870034_production, 93_LVBus0870036_production, 93_LVBus0870037_production, 93_LVBus0870038_production, 93_LVBus0870040_consumption, 93_LVBus0870040_production, 93_LVBus0870042_production, 93_LVBus0870043_production, 93_LVBus0870044_production, 93_LVBus0870045_production, 93_LVBus0870046_production, 93_LVBus0870047_production, 93_LVBus0870049_production, 93_LVBus0870050_production, 93_LVBus0870052_consumption, 93_LVBus0870052_production, 93_LVBus0870053_consumption, 93_LVBus0870053_production, 93_LVBus0870054_consumption, 93_LVBus0870054_production, 93_LVBus0870055_consumption, 93_LVBus0870055_production, 93_LVBus0870056_consumption, 93_LVBus0870056_production, 93_LVBus0870057_consumption, 93_LVBus0870057_production, 93_LVBus0870058_production, 93_LVBus0870062_consumption, 93_LVBus0870062_production, 93_LVBus0870063_production, 93_LVBus0870064_consumption, 93_LVBus0870064_production, 93_LVBus0870065_production, 93_LVBus0870066_production, 93_LVBus0870067_production, 93_LVBus0870068_production, 93_LVBus0870069_production, 93_LVBus0870070_consumption, 93_LVBus0870070_production, 93_LVBus0870071_consumption, 93_LVBus0870071_production, 93_LVBus0870072_production, 93_LVBus0870073_production, 93_LVBus0870074_consumption, 93_LVBus0870074_production, 93_LVBus0870075_production, 93_LVBus0870076_production, 93_LVBus0870077_production, 93_LVBus0870078_consumption, 93_LVBus0870078_production, 93_LVBus0870080_consumption, 93_LVBus0870080_production, 93_LVBus0870081_production, 93_LVBus0870085_consumption, 93_LVBus0870085_production, 93_LVBus0870086_consumption, 93_LVBus0870086_production, 93_LVBus0870087_production, 93_LVBus0870088_consumption, 93_LVBus0870088_production, 93_LVBus0870089_production, 93_LVBus0870090_production, 93_LVBus0870091_production, 93_LVBus0870092_production, 93_LVBus0870093_production, 93_LVBus0870095_production, 93_LVBus0870096_production, 93_LVBus0870097_production, 93_LVBus0870098_production, 93_LVBus0870099_production, 93_LVBus0870100_consumption, 93_LVBus0870100_production, 93_LVBus0870101_production, 93_LVBus0870102_production, 93_LVBus0870103_production, 93_LVBus0870104_production, 93_LVBus0870106_consumption, 93_LVBus0870106_production, 93_LVBus0870107_consumption, 93_LVBus0870107_production, 93_LVBus0870109_consumption, 93_LVBus0870109_production, 93_LVBus0870111_consumption, 93_LVBus0870111_production, 93_LVBus0870112_consumption, 93_LVBus0870112_production, 93_LVBus0870114_production, 93_LVBus0870116_consumption, 93_LVBus0870116_production, 93_LVBus0870117_consumption, 93_LVBus0870117_production, 93_LVBus0870119_production, 93_LVBus0870121_production, 93_LVBus0870122_consumption, 93_LVBus0870122_production, 93_LVBus0870123_production, 93_LVBus0870124_consumption, 93_LVBus0870124_production, 93_LVBus0870126_production, 93_LVBus0870127_production, 93_LVBus0870128_consumption, 93_LVBus0870128_production, 93_LVBus0870129_production, 93_LVBus0870131_consumption, 93_LVBus0870131_production, 93_LVBus0870132_production, 93_LVBus0870133_production, 93_LVBus0870134_production, 93_LVBus0870135_production, 93_LVBus0870137_production, 93_LVBus0870139_production, 93_LVBus1359130_consumption, 93_LVBus1359130_production, 93_LVBus1359131_consumption, 93_LVBus1359131_production, 93_LVBus1359132_consumption, 93_LVBus1359132_production, 93_LVBus1359133_consumption, 93_LVBus1359133_production, 93_LVBus1359134_consumption, 93_LVBus1359134_production, 93_LVBus1359135_consumption, 93_LVBus1359135_production, 93_LVBus1365869_consumption, 93_LVBus1365869_production, 93_LVBus1372212_consumption, 93_LVBus1372212_production, 93_LVBus1372213_production, 93_LVBus1374127_production, 93_LVBus1385110_consumption, 93_LVBus1385110_production, 93_LVBus1385111_consumption, 93_LVBus1385111_production, 93_LVBus1392505_production, 93_LVBus1392506_consumption, 93_LVBus1392506_production, 93_LVBus1393151_production, 93_LVBus1393152_production, 93_LVBus1393153_production, 93_LVBus1414053_consumption, 93_LVBus1414053_production, 93_LVBus1414054_production, 93_LVBus1418957_production, 93_LVBus1418958_consumption, 93_LVBus1418958_production, 93_LVBus1427304_consumption, 93_LVBus1427304_production, 93_MVLV11036_consumption, 93_MVLV11036_production, 93_MVLV16626_consumption, 93_MVLV16626_production, 93_MVLV20339_consumption, 93_MVLV20339_production, 93_MVLV21981_consumption, 93_MVLV21981_production, 93_MVLV35709_consumption, 93_MVLV35709_production, 93_MVLV46943_consumption, 93_MVLV46943_production, 93_MVLV73764_consumption, 93_MVLV73764_production.

## 9. Data Quality Summary

**Total findings:** 233 (0 errors, 5 warnings, 228 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  528 of 764 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.81 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  529 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869959_consumption`  
  Load '93_LVBus0869959_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870087_consumption`  
  Load '93_LVBus0870087_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869846_consumption`  
  Load '93_LVBus0869846_consumption' has phase imbalance of 253.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869890_consumption`  
  Load '93_LVBus0869890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869840_consumption`  
  Load '93_LVBus0869840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869680_consumption`  
  Load '93_LVBus0869680_consumption' has phase imbalance of 217.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869963_consumption`  
  Load '93_LVBus0869963_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869806_consumption`  
  Load '93_LVBus0869806_consumption' has phase imbalance of 232.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870037_consumption`  
  Load '93_LVBus0870037_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869917_consumption`  
  Load '93_LVBus0869917_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870134_consumption`  
  Load '93_LVBus0870134_consumption' has phase imbalance of 275.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869911_consumption`  
  Load '93_LVBus0869911_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869742_consumption`  
  Load '93_LVBus0869742_consumption' has phase imbalance of 258.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869921_consumption`  
  Load '93_LVBus0869921_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869772_consumption`  
  Load '93_LVBus0869772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869686_consumption`  
  Load '93_LVBus0869686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870093_consumption`  
  Load '93_LVBus0870093_consumption' has phase imbalance of 39.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869848_consumption`  
  Load '93_LVBus0869848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869896_consumption`  
  Load '93_LVBus0869896_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869683_consumption`  
  Load '93_LVBus0869683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869964_consumption`  
  Load '93_LVBus0869964_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870077_consumption`  
  Load '93_LVBus0870077_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869902_consumption`  
  Load '93_LVBus0869902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869998_consumption`  
  Load '93_LVBus0869998_consumption' has phase imbalance of 263.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1393153_consumption`  
  Load '93_LVBus1393153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869949_consumption`  
  Load '93_LVBus0869949_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870000_consumption`  
  Load '93_LVBus0870000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869838_consumption`  
  Load '93_LVBus0869838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869970_consumption`  
  Load '93_LVBus0869970_consumption' has phase imbalance of 140.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869735_consumption`  
  Load '93_LVBus0869735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869945_consumption`  
  Load '93_LVBus0869945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869749_consumption`  
  Load '93_LVBus0869749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869829_consumption`  
  Load '93_LVBus0869829_consumption' has phase imbalance of 276.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869914_consumption`  
  Load '93_LVBus0869914_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870044_consumption`  
  Load '93_LVBus0870044_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869736_consumption`  
  Load '93_LVBus0869736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869843_consumption`  
  Load '93_LVBus0869843_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869938_consumption`  
  Load '93_LVBus0869938_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870072_consumption`  
  Load '93_LVBus0870072_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869913_consumption`  
  Load '93_LVBus0869913_consumption' has phase imbalance of 267.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869972_consumption`  
  Load '93_LVBus0869972_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870046_consumption`  
  Load '93_LVBus0870046_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870016_consumption`  
  Load '93_LVBus0870016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870043_consumption`  
  Load '93_LVBus0870043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869941_consumption`  
  Load '93_LVBus0869941_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869822_consumption`  
  Load '93_LVBus0869822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870010_consumption`  
  Load '93_LVBus0870010_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869832_consumption`  
  Load '93_LVBus0869832_consumption' has phase imbalance of 240.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869816_consumption`  
  Load '93_LVBus0869816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869849_consumption`  
  Load '93_LVBus0869849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869875_consumption`  
  Load '93_LVBus0869875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869813_consumption`  
  Load '93_LVBus0869813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869981_consumption`  
  Load '93_LVBus0869981_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869805_consumption`  
  Load '93_LVBus0869805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869692_consumption`  
  Load '93_LVBus0869692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870042_consumption`  
  Load '93_LVBus0870042_consumption' has phase imbalance of 91.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869796_consumption`  
  Load '93_LVBus0869796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869954_consumption`  
  Load '93_LVBus0869954_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869976_consumption`  
  Load '93_LVBus0869976_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869738_consumption`  
  Load '93_LVBus0869738_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869885_consumption`  
  Load '93_LVBus0869885_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869990_consumption`  
  Load '93_LVBus0869990_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869920_consumption`  
  Load '93_LVBus0869920_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870007_consumption`  
  Load '93_LVBus0870007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1392505_consumption`  
  Load '93_LVBus1392505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869958_consumption`  
  Load '93_LVBus0869958_consumption' has phase imbalance of 50.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870066_consumption`  
  Load '93_LVBus0870066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869897_consumption`  
  Load '93_LVBus0869897_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869731_consumption`  
  Load '93_LVBus0869731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869988_consumption`  
  Load '93_LVBus0869988_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869827_consumption`  
  Load '93_LVBus0869827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869986_consumption`  
  Load '93_LVBus0869986_consumption' has phase imbalance of 274.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870038_consumption`  
  Load '93_LVBus0870038_consumption' has phase imbalance of 251.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869870_consumption`  
  Load '93_LVBus0869870_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869943_consumption`  
  Load '93_LVBus0869943_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869937_consumption`  
  Load '93_LVBus0869937_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870001_consumption`  
  Load '93_LVBus0870001_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870135_consumption`  
  Load '93_LVBus0870135_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869834_consumption`  
  Load '93_LVBus0869834_consumption' has phase imbalance of 148.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869831_consumption`  
  Load '93_LVBus0869831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870068_consumption`  
  Load '93_LVBus0870068_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869740_consumption`  
  Load '93_LVBus0869740_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869767_consumption`  
  Load '93_LVBus0869767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870102_consumption`  
  Load '93_LVBus0870102_consumption' has phase imbalance of 98.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870021_consumption`  
  Load '93_LVBus0870021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870050_consumption`  
  Load '93_LVBus0870050_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870047_consumption`  
  Load '93_LVBus0870047_consumption' has phase imbalance of 67.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869974_consumption`  
  Load '93_LVBus0869974_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869839_consumption`  
  Load '93_LVBus0869839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869894_consumption`  
  Load '93_LVBus0869894_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869962_consumption`  
  Load '93_LVBus0869962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869889_consumption`  
  Load '93_LVBus0869889_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869681_consumption`  
  Load '93_LVBus0869681_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869910_consumption`  
  Load '93_LVBus0869910_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869951_consumption`  
  Load '93_LVBus0869951_consumption' has phase imbalance of 85.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870101_consumption`  
  Load '93_LVBus0870101_consumption' has phase imbalance of 267.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870013_consumption`  
  Load '93_LVBus0870013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869955_consumption`  
  Load '93_LVBus0869955_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869845_consumption`  
  Load '93_LVBus0869845_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869679_consumption`  
  Load '93_LVBus0869679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869906_consumption`  
  Load '93_LVBus0869906_consumption' has phase imbalance of 42.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869947_consumption`  
  Load '93_LVBus0869947_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870098_consumption`  
  Load '93_LVBus0870098_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869977_consumption`  
  Load '93_LVBus0869977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869892_consumption`  
  Load '93_LVBus0869892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869944_consumption`  
  Load '93_LVBus0869944_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869842_consumption`  
  Load '93_LVBus0869842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869837_consumption`  
  Load '93_LVBus0869837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869817_consumption`  
  Load '93_LVBus0869817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869912_consumption`  
  Load '93_LVBus0869912_consumption' has phase imbalance of 66.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869996_consumption`  
  Load '93_LVBus0869996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869721_consumption`  
  Load '93_LVBus0869721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1374127_consumption`  
  Load '93_LVBus1374127_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869727_consumption`  
  Load '93_LVBus0869727_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869807_consumption`  
  Load '93_LVBus0869807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869682_consumption`  
  Load '93_LVBus0869682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869734_consumption`  
  Load '93_LVBus0869734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870034_consumption`  
  Load '93_LVBus0870034_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869957_consumption`  
  Load '93_LVBus0869957_consumption' has phase imbalance of 164.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869907_consumption`  
  Load '93_LVBus0869907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869739_consumption`  
  Load '93_LVBus0869739_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870045_consumption`  
  Load '93_LVBus0870045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869891_consumption`  
  Load '93_LVBus0869891_consumption' has phase imbalance of 139.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870008_consumption`  
  Load '93_LVBus0870008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1393151_consumption`  
  Load '93_LVBus1393151_consumption' has phase imbalance of 175.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869836_consumption`  
  Load '93_LVBus0869836_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870132_consumption`  
  Load '93_LVBus0870132_consumption' has phase imbalance of 221.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869771_consumption`  
  Load '93_LVBus0869771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870089_consumption`  
  Load '93_LVBus0870089_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869927_consumption`  
  Load '93_LVBus0869927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869844_consumption`  
  Load '93_LVBus0869844_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869761_consumption`  
  Load '93_LVBus0869761_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869880_consumption`  
  Load '93_LVBus0869880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869824_consumption`  
  Load '93_LVBus0869824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870103_consumption`  
  Load '93_LVBus0870103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869973_consumption`  
  Load '93_LVBus0869973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870091_consumption`  
  Load '93_LVBus0870091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870104_consumption`  
  Load '93_LVBus0870104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869989_consumption`  
  Load '93_LVBus0869989_consumption' has phase imbalance of 207.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869960_consumption`  
  Load '93_LVBus0869960_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870065_consumption`  
  Load '93_LVBus0870065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870075_consumption`  
  Load '93_LVBus0870075_consumption' has phase imbalance of 132.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870015_consumption`  
  Load '93_LVBus0870015_consumption' has phase imbalance of 107.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869697_consumption`  
  Load '93_LVBus0869697_consumption' has phase imbalance of 185.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869925_consumption`  
  Load '93_LVBus0869925_consumption' has phase imbalance of 67.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869801_consumption`  
  Load '93_LVBus0869801_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869730_consumption`  
  Load '93_LVBus0869730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869732_consumption`  
  Load '93_LVBus0869732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869766_consumption`  
  Load '93_LVBus0869766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870005_consumption`  
  Load '93_LVBus0870005_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869971_consumption`  
  Load '93_LVBus0869971_consumption' has phase imbalance of 207.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869946_consumption`  
  Load '93_LVBus0869946_consumption' has phase imbalance of 251.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869769_consumption`  
  Load '93_LVBus0869769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870033_consumption`  
  Load '93_LVBus0870033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870036_consumption`  
  Load '93_LVBus0870036_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870096_consumption`  
  Load '93_LVBus0870096_consumption' has phase imbalance of 288.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869719_consumption`  
  Load '93_LVBus0869719_consumption' has phase imbalance of 227.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870063_consumption`  
  Load '93_LVBus0870063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869982_consumption`  
  Load '93_LVBus0869982_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869923_consumption`  
  Load '93_LVBus0869923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869685_consumption`  
  Load '93_LVBus0869685_consumption' has phase imbalance of 114.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869930_consumption`  
  Load '93_LVBus0869930_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869720_consumption`  
  Load '93_LVBus0869720_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869744_consumption`  
  Load '93_LVBus0869744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869884_consumption`  
  Load '93_LVBus0869884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869698_consumption`  
  Load '93_LVBus0869698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870009_consumption`  
  Load '93_LVBus0870009_consumption' has phase imbalance of 76.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869978_consumption`  
  Load '93_LVBus0869978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869869_consumption`  
  Load '93_LVBus0869869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870058_consumption`  
  Load '93_LVBus0870058_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1418957_consumption`  
  Load '93_LVBus1418957_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1372213_consumption`  
  Load '93_LVBus1372213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869931_consumption`  
  Load '93_LVBus0869931_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870099_consumption`  
  Load '93_LVBus0870099_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870069_consumption`  
  Load '93_LVBus0870069_consumption' has phase imbalance of 167.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869717_consumption`  
  Load '93_LVBus0869717_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869997_consumption`  
  Load '93_LVBus0869997_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869928_consumption`  
  Load '93_LVBus0869928_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869737_consumption`  
  Load '93_LVBus0869737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869919_consumption`  
  Load '93_LVBus0869919_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1414054_consumption`  
  Load '93_LVBus1414054_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869915_consumption`  
  Load '93_LVBus0869915_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870139_consumption`  
  Load '93_LVBus0870139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870049_consumption`  
  Load '93_LVBus0870049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870076_consumption`  
  Load '93_LVBus0870076_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869696_consumption`  
  Load '93_LVBus0869696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870031_consumption`  
  Load '93_LVBus0870031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869858_consumption`  
  Load '93_LVBus0869858_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870003_consumption`  
  Load '93_LVBus0870003_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869728_consumption`  
  Load '93_LVBus0869728_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1393152_consumption`  
  Load '93_LVBus1393152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869747_consumption`  
  Load '93_LVBus0869747_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870073_consumption`  
  Load '93_LVBus0870073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869729_consumption`  
  Load '93_LVBus0869729_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870090_consumption`  
  Load '93_LVBus0870090_consumption' has phase imbalance of 283.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869755_consumption`  
  Load '93_LVBus0869755_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870092_consumption`  
  Load '93_LVBus0870092_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869864_consumption`  
  Load '93_LVBus0869864_consumption' has phase imbalance of 242.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0869983_consumption`  
  Load '93_LVBus0869983_consumption' has phase imbalance of 210.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0870029_consumption`  
  Load '93_LVBus0870029_consumption' has phase imbalance of 266.9%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 764 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0869700' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0869811' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0869776' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0870027' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '93_GRIM5' (MV, 11.78 kV) has an electrical reach of 24.66 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '93_LVBus0869967' (LV, 0.24 kV) has an electrical reach of 1.19 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '93_LVBus0870029' (LV, 0.24 kV) has an electrical reach of 6.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '93_LVBus0870062' (LV, 0.24 kV) has an electrical reach of 1.36 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '93_LVBus0869727' (LV, 0.24 kV) has an electrical reach of 1.16 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '93_LVBus0870025' (LV, 0.24 kV) has an electrical reach of 14.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '93_LVBus0870027' (LV, 0.24 kV) has an electrical reach of 9.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
- **[I.PROV.LINE_SWITCH_LIKE]** `93_LVBranch1216351`  
  Line '93_LVBranch1216351' has near-zero series impedance and may be modelled more accurately as a switch: effective impedance (Z·length) < 0.0001 Ω on all diagonals.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  491 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '93_LVBranch0065846' and '93_LVBranch0144555' at bus '93_LVBus0870013' have ||Z||_F ratio 3110.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  165 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 93_LVBus0869679_consumption, 93_LVBus0869682_consumption, 93_LVBus0869683_consumption, 93_LVBus0869686_consumption, 93_LVBus0869692_consumption, 93_LVBus0869696_consumption, 93_LVBus0869697_consumption, 93_LVBus0869698_consumption, 93_LVBus0869717_consumption, 93_LVBus0869719_consumption, 93_LVBus0869720_consumption, 93_LVBus0869721_consumption, 93_LVBus0869727_consumption, 93_LVBus0869728_consumption, 93_LVBus0869729_consumption, 93_LVBus0869730_consumption, 93_LVBus0869731_consumption, 93_LVBus0869732_consumption, 93_LVBus0869734_consumption, 93_LVBus0869735_consumption, 93_LVBus0869736_consumption, 93_LVBus0869737_consumption, 93_LVBus0869738_consumption, 93_LVBus0869739_consumption, 93_LVBus0869744_consumption, 93_LVBus0869747_consumption, 93_LVBus0869749_consumption, 93_LVBus0869755_consumption, 93_LVBus0869761_consumption, 93_LVBus0869766_consumption, 93_LVBus0869767_consumption, 93_LVBus0869769_consumption, 93_LVBus0869771_consumption, 93_LVBus0869772_consumption, 93_LVBus0869796_consumption, 93_LVBus0869801_consumption, 93_LVBus0869805_consumption, 93_LVBus0869806_consumption, 93_LVBus0869807_consumption, 93_LVBus0869813_consumption, 93_LVBus0869816_consumption, 93_LVBus0869817_consumption, 93_LVBus0869822_consumption, 93_LVBus0869824_consumption, 93_LVBus0869827_consumption, 93_LVBus0869829_consumption, 93_LVBus0869831_consumption, 93_LVBus0869832_consumption, 93_LVBus0869836_consumption, 93_LVBus0869837_consumption, 93_LVBus0869838_consumption, 93_LVBus0869839_consumption, 93_LVBus0869840_consumption, 93_LVBus0869842_consumption, 93_LVBus0869843_consumption, 93_LVBus0869845_consumption, 93_LVBus0869846_consumption, 93_LVBus0869848_consumption, 93_LVBus0869849_consumption, 93_LVBus0869858_consumption, 93_LVBus0869864_consumption, 93_LVBus0869869_consumption, 93_LVBus0869870_consumption, 93_LVBus0869875_consumption, 93_LVBus0869880_consumption, 93_LVBus0869884_consumption, 93_LVBus0869885_consumption, 93_LVBus0869890_consumption, 93_LVBus0869892_consumption, 93_LVBus0869896_consumption, 93_LVBus0869897_consumption, 93_LVBus0869902_consumption, 93_LVBus0869907_consumption, 93_LVBus0869910_consumption, 93_LVBus0869911_consumption, 93_LVBus0869913_consumption, 93_LVBus0869914_consumption, 93_LVBus0869915_consumption, 93_LVBus0869917_consumption, 93_LVBus0869919_consumption, 93_LVBus0869920_consumption, 93_LVBus0869923_consumption, 93_LVBus0869927_consumption, 93_LVBus0869928_consumption, 93_LVBus0869930_consumption, 93_LVBus0869931_consumption, 93_LVBus0869937_consumption, 93_LVBus0869941_consumption, 93_LVBus0869943_consumption, 93_LVBus0869944_consumption, 93_LVBus0869945_consumption, 93_LVBus0869946_consumption, 93_LVBus0869947_consumption, 93_LVBus0869949_consumption, 93_LVBus0869954_consumption, 93_LVBus0869955_consumption, 93_LVBus0869959_consumption, 93_LVBus0869960_consumption, 93_LVBus0869962_consumption, 93_LVBus0869964_consumption, 93_LVBus0869971_consumption, 93_LVBus0869972_consumption, 93_LVBus0869973_consumption, 93_LVBus0869976_consumption, 93_LVBus0869977_consumption, 93_LVBus0869978_consumption, 93_LVBus0869982_consumption, 93_LVBus0869986_consumption, 93_LVBus0869988_consumption, 93_LVBus0869989_consumption, 93_LVBus0869990_consumption, 93_LVBus0869996_consumption, 93_LVBus0869997_consumption, 93_LVBus0869998_consumption, 93_LVBus0870000_consumption, 93_LVBus0870001_consumption, 93_LVBus0870005_consumption, 93_LVBus0870007_consumption, 93_LVBus0870008_consumption, 93_LVBus0870010_consumption, 93_LVBus0870013_consumption, 93_LVBus0870016_consumption, 93_LVBus0870021_consumption, 93_LVBus0870029_consumption, 93_LVBus0870031_consumption, 93_LVBus0870033_consumption, 93_LVBus0870034_consumption, 93_LVBus0870036_consumption, 93_LVBus0870038_consumption, 93_LVBus0870043_consumption, 93_LVBus0870044_consumption, 93_LVBus0870045_consumption, 93_LVBus0870046_consumption, 93_LVBus0870049_consumption, 93_LVBus0870050_consumption, 93_LVBus0870063_consumption, 93_LVBus0870065_consumption, 93_LVBus0870066_consumption, 93_LVBus0870068_consumption, 93_LVBus0870069_consumption, 93_LVBus0870073_consumption, 93_LVBus0870076_consumption, 93_LVBus0870077_consumption, 93_LVBus0870087_consumption, 93_LVBus0870089_consumption, 93_LVBus0870090_consumption, 93_LVBus0870091_consumption, 93_LVBus0870096_consumption, 93_LVBus0870098_consumption, 93_LVBus0870099_consumption, 93_LVBus0870101_consumption, 93_LVBus0870103_consumption, 93_LVBus0870104_consumption, 93_LVBus0870132_consumption, 93_LVBus0870134_consumption, 93_LVBus0870135_consumption, 93_LVBus0870139_consumption, 93_LVBus1372213_consumption, 93_LVBus1374127_consumption, 93_LVBus1392505_consumption, 93_LVBus1393151_consumption, 93_LVBus1393152_consumption, 93_LVBus1393153_consumption, 93_LVBus1414054_consumption, 93_LVBus1418957_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  382 group(s) of loads (764 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  7 group(s) of series lines (15 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  529 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0869679_production, 93_LVBus0869680_production, 93_LVBus0869681_production, 93_LVBus0869682_production, 93_LVBus0869683_production, 93_LVBus0869685_production, 93_LVBus0869686_production, 93_LVBus0869688_consumption, 93_LVBus0869688_production, 93_LVBus0869690_consumption, 93_LVBus0869690_production, 93_LVBus0869692_production, 93_LVBus0869694_consumption, 93_LVBus0869694_production, 93_LVBus0869695_production, 93_LVBus0869696_production, 93_LVBus0869697_production, 93_LVBus0869698_production, 93_LVBus0869700_consumption, 93_LVBus0869700_production, 93_LVBus0869701_production, 93_LVBus0869703_consumption, 93_LVBus0869703_production, 93_LVBus0869704_consumption, 93_LVBus0869704_production, 93_LVBus0869705_consumption, 93_LVBus0869705_production, 93_LVBus0869707_consumption, 93_LVBus0869707_production, 93_LVBus0869709_consumption, 93_LVBus0869709_production, 93_LVBus0869710_production, 93_LVBus0869712_production, 93_LVBus0869716_consumption, 93_LVBus0869716_production, 93_LVBus0869717_production, 93_LVBus0869718_consumption, 93_LVBus0869718_production, 93_LVBus0869719_production, 93_LVBus0869720_production, 93_LVBus0869721_production, 93_LVBus0869722_consumption, 93_LVBus0869722_production, 93_LVBus0869723_production, 93_LVBus0869727_production, 93_LVBus0869728_production, 93_LVBus0869729_production, 93_LVBus0869730_production, 93_LVBus0869731_production, 93_LVBus0869732_production, 93_LVBus0869734_production, 93_LVBus0869735_production, 93_LVBus0869736_production, 93_LVBus0869737_production, 93_LVBus0869738_production, 93_LVBus0869739_production, 93_LVBus0869740_production, 93_LVBus0869741_consumption, 93_LVBus0869741_production, 93_LVBus0869742_production, 93_LVBus0869744_production, 93_LVBus0869746_consumption, 93_LVBus0869746_production, 93_LVBus0869747_production, 93_LVBus0869748_consumption, 93_LVBus0869748_production, 93_LVBus0869749_production, 93_LVBus0869750_consumption, 93_LVBus0869750_production, 93_LVBus0869751_consumption, 93_LVBus0869751_production, 93_LVBus0869753_consumption, 93_LVBus0869753_production, 93_LVBus0869754_consumption, 93_LVBus0869754_production, 93_LVBus0869755_production, 93_LVBus0869760_production, 93_LVBus0869761_production, 93_LVBus0869762_consumption, 93_LVBus0869762_production, 93_LVBus0869766_production, 93_LVBus0869767_production, 93_LVBus0869768_consumption, 93_LVBus0869768_production, 93_LVBus0869769_production, 93_LVBus0869770_consumption, 93_LVBus0869770_production, 93_LVBus0869771_production, 93_LVBus0869772_production, 93_LVBus0869776_consumption, 93_LVBus0869776_production, 93_LVBus0869777_consumption, 93_LVBus0869777_production, 93_LVBus0869778_consumption, 93_LVBus0869778_production, 93_LVBus0869779_production, 93_LVBus0869780_consumption, 93_LVBus0869780_production, 93_LVBus0869782_consumption, 93_LVBus0869782_production, 93_LVBus0869783_production, 93_LVBus0869785_consumption, 93_LVBus0869785_production, 93_LVBus0869786_consumption, 93_LVBus0869786_production, 93_LVBus0869787_consumption, 93_LVBus0869787_production, 93_LVBus0869789_consumption, 93_LVBus0869789_production, 93_LVBus0869790_consumption, 93_LVBus0869790_production, 93_LVBus0869791_consumption, 93_LVBus0869791_production, 93_LVBus0869792_consumption, 93_LVBus0869792_production, 93_LVBus0869793_consumption, 93_LVBus0869793_production, 93_LVBus0869795_consumption, 93_LVBus0869795_production, 93_LVBus0869796_production, 93_LVBus0869797_production, 93_LVBus0869798_consumption, 93_LVBus0869798_production, 93_LVBus0869799_consumption, 93_LVBus0869799_production, 93_LVBus0869800_consumption, 93_LVBus0869800_production, 93_LVBus0869801_production, 93_LVBus0869802_production, 93_LVBus0869803_consumption, 93_LVBus0869803_production, 93_LVBus0869804_consumption, 93_LVBus0869804_production, 93_LVBus0869805_production, 93_LVBus0869806_production, 93_LVBus0869807_production, 93_LVBus0869811_production, 93_LVBus0869813_production, 93_LVBus0869814_consumption, 93_LVBus0869814_production, 93_LVBus0869815_consumption, 93_LVBus0869815_production, 93_LVBus0869816_production, 93_LVBus0869817_production, 93_LVBus0869818_consumption, 93_LVBus0869818_production, 93_LVBus0869819_consumption, 93_LVBus0869819_production, 93_LVBus0869821_consumption, 93_LVBus0869821_production, 93_LVBus0869822_production, 93_LVBus0869823_consumption, 93_LVBus0869823_production, 93_LVBus0869824_production, 93_LVBus0869825_consumption, 93_LVBus0869825_production, 93_LVBus0869826_consumption, 93_LVBus0869826_production, 93_LVBus0869827_production, 93_LVBus0869828_consumption, 93_LVBus0869828_production, 93_LVBus0869829_production, 93_LVBus0869831_production, 93_LVBus0869832_production, 93_LVBus0869833_consumption, 93_LVBus0869833_production, 93_LVBus0869834_production, 93_LVBus0869835_consumption, 93_LVBus0869835_production, 93_LVBus0869836_production, 93_LVBus0869837_production, 93_LVBus0869838_production, 93_LVBus0869839_production, 93_LVBus0869840_production, 93_LVBus0869842_production, 93_LVBus0869843_production, 93_LVBus0869844_production, 93_LVBus0869845_production, 93_LVBus0869846_production, 93_LVBus0869848_production, 93_LVBus0869849_production, 93_LVBus0869850_consumption, 93_LVBus0869850_production, 93_LVBus0869852_consumption, 93_LVBus0869852_production, 93_LVBus0869857_consumption, 93_LVBus0869857_production, 93_LVBus0869858_production, 93_LVBus0869859_production, 93_LVBus0869861_consumption, 93_LVBus0869861_production, 93_LVBus0869862_production, 93_LVBus0869863_consumption, 93_LVBus0869863_production, 93_LVBus0869864_production, 93_LVBus0869866_consumption, 93_LVBus0869866_production, 93_LVBus0869867_consumption, 93_LVBus0869867_production, 93_LVBus0869868_consumption, 93_LVBus0869868_production, 93_LVBus0869869_production, 93_LVBus0869870_production, 93_LVBus0869872_consumption, 93_LVBus0869872_production, 93_LVBus0869873_consumption, 93_LVBus0869873_production, 93_LVBus0869874_consumption, 93_LVBus0869874_production, 93_LVBus0869875_production, 93_LVBus0869876_consumption, 93_LVBus0869876_production, 93_LVBus0869877_production, 93_LVBus0869878_consumption, 93_LVBus0869878_production, 93_LVBus0869879_consumption, 93_LVBus0869879_production, 93_LVBus0869880_production, 93_LVBus0869884_production, 93_LVBus0869885_production, 93_LVBus0869886_consumption, 93_LVBus0869886_production, 93_LVBus0869888_consumption, 93_LVBus0869888_production, 93_LVBus0869889_production, 93_LVBus0869890_production, 93_LVBus0869891_production, 93_LVBus0869892_production, 93_LVBus0869893_consumption, 93_LVBus0869893_production, 93_LVBus0869894_production, 93_LVBus0869896_production, 93_LVBus0869897_production, 93_LVBus0869901_consumption, 93_LVBus0869901_production, 93_LVBus0869902_production, 93_LVBus0869904_consumption, 93_LVBus0869904_production, 93_LVBus0869905_consumption, 93_LVBus0869905_production, 93_LVBus0869906_production, 93_LVBus0869907_production, 93_LVBus0869909_consumption, 93_LVBus0869909_production, 93_LVBus0869910_production, 93_LVBus0869911_production, 93_LVBus0869912_production, 93_LVBus0869913_production, 93_LVBus0869914_production, 93_LVBus0869915_production, 93_LVBus0869916_consumption, 93_LVBus0869916_production, 93_LVBus0869917_production, 93_LVBus0869919_production, 93_LVBus0869920_production, 93_LVBus0869921_production, 93_LVBus0869923_production, 93_LVBus0869924_production, 93_LVBus0869925_production, 93_LVBus0869927_production, 93_LVBus0869928_production, 93_LVBus0869930_production, 93_LVBus0869931_production, 93_LVBus0869932_consumption, 93_LVBus0869932_production, 93_LVBus0869936_consumption, 93_LVBus0869936_production, 93_LVBus0869937_production, 93_LVBus0869938_production, 93_LVBus0869940_consumption, 93_LVBus0869940_production, 93_LVBus0869941_production, 93_LVBus0869943_production, 93_LVBus0869944_production, 93_LVBus0869945_production, 93_LVBus0869946_production, 93_LVBus0869947_production, 93_LVBus0869949_production, 93_LVBus0869950_consumption, 93_LVBus0869950_production, 93_LVBus0869951_production, 93_LVBus0869952_consumption, 93_LVBus0869952_production, 93_LVBus0869953_consumption, 93_LVBus0869953_production, 93_LVBus0869954_production, 93_LVBus0869955_production, 93_LVBus0869956_consumption, 93_LVBus0869956_production, 93_LVBus0869957_production, 93_LVBus0869958_production, 93_LVBus0869959_production, 93_LVBus0869960_production, 93_LVBus0869961_consumption, 93_LVBus0869961_production, 93_LVBus0869962_production, 93_LVBus0869963_production, 93_LVBus0869964_production, 93_LVBus0869965_production, 93_LVBus0869967_consumption, 93_LVBus0869967_production, 93_LVBus0869968_consumption, 93_LVBus0869968_production, 93_LVBus0869969_consumption, 93_LVBus0869969_production, 93_LVBus0869970_production, 93_LVBus0869971_production, 93_LVBus0869972_production, 93_LVBus0869973_production, 93_LVBus0869974_production, 93_LVBus0869975_production, 93_LVBus0869976_production, 93_LVBus0869977_production, 93_LVBus0869978_production, 93_LVBus0869979_production, 93_LVBus0869980_consumption, 93_LVBus0869980_production, 93_LVBus0869981_production, 93_LVBus0869982_production, 93_LVBus0869983_production, 93_LVBus0869985_consumption, 93_LVBus0869985_production, 93_LVBus0869986_production, 93_LVBus0869988_production, 93_LVBus0869989_production, 93_LVBus0869990_production, 93_LVBus0869991_production, 93_LVBus0869993_consumption, 93_LVBus0869993_production, 93_LVBus0869994_consumption, 93_LVBus0869994_production, 93_LVBus0869995_consumption, 93_LVBus0869995_production, 93_LVBus0869996_production, 93_LVBus0869997_production, 93_LVBus0869998_production, 93_LVBus0869999_consumption, 93_LVBus0869999_production, 93_LVBus0870000_production, 93_LVBus0870001_production, 93_LVBus0870002_consumption, 93_LVBus0870002_production, 93_LVBus0870003_production, 93_LVBus0870004_production, 93_LVBus0870005_production, 93_LVBus0870007_production, 93_LVBus0870008_production, 93_LVBus0870009_production, 93_LVBus0870010_production, 93_LVBus0870013_production, 93_LVBus0870014_consumption, 93_LVBus0870014_production, 93_LVBus0870015_production, 93_LVBus0870016_production, 93_LVBus0870017_consumption, 93_LVBus0870017_production, 93_LVBus0870018_consumption, 93_LVBus0870018_production, 93_LVBus0870019_consumption, 93_LVBus0870019_production, 93_LVBus0870020_production, 93_LVBus0870021_production, 93_LVBus0870025_consumption, 93_LVBus0870025_production, 93_LVBus0870027_production, 93_LVBus0870029_production, 93_LVBus0870031_production, 93_LVBus0870033_production, 93_LVBus0870034_production, 93_LVBus0870036_production, 93_LVBus0870037_production, 93_LVBus0870038_production, 93_LVBus0870040_consumption, 93_LVBus0870040_production, 93_LVBus0870042_production, 93_LVBus0870043_production, 93_LVBus0870044_production, 93_LVBus0870045_production, 93_LVBus0870046_production, 93_LVBus0870047_production, 93_LVBus0870049_production, 93_LVBus0870050_production, 93_LVBus0870052_consumption, 93_LVBus0870052_production, 93_LVBus0870053_consumption, 93_LVBus0870053_production, 93_LVBus0870054_consumption, 93_LVBus0870054_production, 93_LVBus0870055_consumption, 93_LVBus0870055_production, 93_LVBus0870056_consumption, 93_LVBus0870056_production, 93_LVBus0870057_consumption, 93_LVBus0870057_production, 93_LVBus0870058_production, 93_LVBus0870062_consumption, 93_LVBus0870062_production, 93_LVBus0870063_production, 93_LVBus0870064_consumption, 93_LVBus0870064_production, 93_LVBus0870065_production, 93_LVBus0870066_production, 93_LVBus0870067_production, 93_LVBus0870068_production, 93_LVBus0870069_production, 93_LVBus0870070_consumption, 93_LVBus0870070_production, 93_LVBus0870071_consumption, 93_LVBus0870071_production, 93_LVBus0870072_production, 93_LVBus0870073_production, 93_LVBus0870074_consumption, 93_LVBus0870074_production, 93_LVBus0870075_production, 93_LVBus0870076_production, 93_LVBus0870077_production, 93_LVBus0870078_consumption, 93_LVBus0870078_production, 93_LVBus0870080_consumption, 93_LVBus0870080_production, 93_LVBus0870081_production, 93_LVBus0870085_consumption, 93_LVBus0870085_production, 93_LVBus0870086_consumption, 93_LVBus0870086_production, 93_LVBus0870087_production, 93_LVBus0870088_consumption, 93_LVBus0870088_production, 93_LVBus0870089_production, 93_LVBus0870090_production, 93_LVBus0870091_production, 93_LVBus0870092_production, 93_LVBus0870093_production, 93_LVBus0870095_production, 93_LVBus0870096_production, 93_LVBus0870097_production, 93_LVBus0870098_production, 93_LVBus0870099_production, 93_LVBus0870100_consumption, 93_LVBus0870100_production, 93_LVBus0870101_production, 93_LVBus0870102_production, 93_LVBus0870103_production, 93_LVBus0870104_production, 93_LVBus0870106_consumption, 93_LVBus0870106_production, 93_LVBus0870107_consumption, 93_LVBus0870107_production, 93_LVBus0870109_consumption, 93_LVBus0870109_production, 93_LVBus0870111_consumption, 93_LVBus0870111_production, 93_LVBus0870112_consumption, 93_LVBus0870112_production, 93_LVBus0870114_production, 93_LVBus0870116_consumption, 93_LVBus0870116_production, 93_LVBus0870117_consumption, 93_LVBus0870117_production, 93_LVBus0870119_production, 93_LVBus0870121_production, 93_LVBus0870122_consumption, 93_LVBus0870122_production, 93_LVBus0870123_production, 93_LVBus0870124_consumption, 93_LVBus0870124_production, 93_LVBus0870126_production, 93_LVBus0870127_production, 93_LVBus0870128_consumption, 93_LVBus0870128_production, 93_LVBus0870129_production, 93_LVBus0870131_consumption, 93_LVBus0870131_production, 93_LVBus0870132_production, 93_LVBus0870133_production, 93_LVBus0870134_production, 93_LVBus0870135_production, 93_LVBus0870137_production, 93_LVBus0870139_production, 93_LVBus1359130_consumption, 93_LVBus1359130_production, 93_LVBus1359131_consumption, 93_LVBus1359131_production, 93_LVBus1359132_consumption, 93_LVBus1359132_production, 93_LVBus1359133_consumption, 93_LVBus1359133_production, 93_LVBus1359134_consumption, 93_LVBus1359134_production, 93_LVBus1359135_consumption, 93_LVBus1359135_production, 93_LVBus1365869_consumption, 93_LVBus1365869_production, 93_LVBus1372212_consumption, 93_LVBus1372212_production, 93_LVBus1372213_production, 93_LVBus1374127_production, 93_LVBus1385110_consumption, 93_LVBus1385110_production, 93_LVBus1385111_consumption, 93_LVBus1385111_production, 93_LVBus1392505_production, 93_LVBus1392506_consumption, 93_LVBus1392506_production, 93_LVBus1393151_production, 93_LVBus1393152_production, 93_LVBus1393153_production, 93_LVBus1414053_consumption, 93_LVBus1414053_production, 93_LVBus1414054_production, 93_LVBus1418957_production, 93_LVBus1418958_consumption, 93_LVBus1418958_production, 93_LVBus1427304_consumption, 93_LVBus1427304_production, 93_MVLV11036_consumption, 93_MVLV11036_production, 93_MVLV16626_consumption, 93_MVLV16626_production, 93_MVLV20339_consumption, 93_MVLV20339_production, 93_MVLV21981_consumption, 93_MVLV21981_production, 93_MVLV35709_consumption, 93_MVLV35709_production, 93_MVLV46943_consumption, 93_MVLV46943_production, 93_MVLV73764_consumption, 93_MVLV73764_production.

