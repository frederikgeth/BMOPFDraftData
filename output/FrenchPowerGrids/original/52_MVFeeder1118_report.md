# BMOPF Network Summary: 52_MVFeeder1118

**Generated:** 2026-10-01 23:34:13  
**Findings:** 0 errors · 4 warnings · 249 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 390 |  |
| line | 379 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 738 | 4.726 MW, 1.42 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 10 |  |
| switch | 0 |  |
| transformer | 10 | Dyn11×10 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 13 | 12 | 4 | 0 |
| LV_236V | 236.0 V | 377 | 367 | 734 | 0 |

**Transformer transitions:**

- `52_MVLV033012_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV090024_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV041324_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV003020_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV017154_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV001575_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV003023_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV081577_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV049395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV039354_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 16 |
| Degree-1 buses | 166 |
| Tree depth (max hops) | 20 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 390 | 1 | 389 | 0 | 0 | 0 |
| Tier LV_236V | 377 | 10 | 367 | 0 | 0 | 0 |
| Tier MV_11.8kV | 13 | 1 | 12 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 10; skipped invalid branches: 0.

Galvanic zones: 11; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_HEINL | MV_11.8kV | 13 | 0 | 0 | 10 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1547 declared bus terminals; 1504 mapped line/closed-switch conductor edges; 43 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 885000.0 | 15.283 | 2214 |
| q_nom | 0.0 | 266000.0 | 15.283 | 2214 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.409 | 1100.0 | 1.371 | 379 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 693000.0 | 0.366 | 10 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 484 of 738 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058529_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058498_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058531_consumption' has phase imbalance of 232.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058734_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058765_consumption' has phase imbalance of 77.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058660_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058781_consumption' has phase imbalance of 41.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058666_consumption' has phase imbalance of 256.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058587_consumption' has phase imbalance of 140.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058657_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058862_consumption' has phase imbalance of 188.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058537_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058687_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1133477_consumption' has phase imbalance of 181.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058696_consumption' has phase imbalance of 39.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058895_consumption' has phase imbalance of 49.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058525_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058619_consumption' has phase imbalance of 63.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058559_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058905_consumption' has phase imbalance of 31.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058526_consumption' has phase imbalance of 54.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058566_consumption' has phase imbalance of 57.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058591_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058503_consumption' has phase imbalance of 23.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058704_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058661_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058850_consumption' has phase imbalance of 83.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058538_consumption' has phase imbalance of 224.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058888_consumption' has phase imbalance of 120.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058845_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058896_consumption' has phase imbalance of 153.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1145272_consumption' has phase imbalance of 291.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058884_consumption' has phase imbalance of 64.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058847_consumption' has phase imbalance of 108.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058893_consumption' has phase imbalance of 97.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058588_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058534_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058737_consumption' has phase imbalance of 103.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1191649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058762_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058688_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058551_consumption' has phase imbalance of 220.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058668_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058530_consumption' has phase imbalance of 132.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058528_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058780_consumption' has phase imbalance of 33.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058510_consumption' has phase imbalance of 38.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058879_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058694_consumption' has phase imbalance of 105.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058791_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058771_consumption' has phase imbalance of 293.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058500_consumption' has phase imbalance of 88.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058740_consumption' has phase imbalance of 221.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058564_consumption' has phase imbalance of 106.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058697_consumption' has phase imbalance of 206.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058569_consumption' has phase imbalance of 89.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058523_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058624_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058776_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058553_consumption' has phase imbalance of 29.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058759_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058729_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058667_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058671_consumption' has phase imbalance of 43.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058756_consumption' has phase imbalance of 73.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058907_consumption' has phase imbalance of 147.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058636_consumption' has phase imbalance of 96.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058711_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058626_consumption' has phase imbalance of 110.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058570_consumption' has phase imbalance of 262.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058599_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058543_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058648_consumption' has phase imbalance of 93.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058790_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058576_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058760_consumption' has phase imbalance of 147.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058764_consumption' has phase imbalance of 103.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058739_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058766_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058733_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058881_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058653_consumption' has phase imbalance of 137.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058715_consumption' has phase imbalance of 146.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058692_consumption' has phase imbalance of 69.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058513_consumption' has phase imbalance of 61.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1133478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058726_consumption' has phase imbalance of 175.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058571_consumption' has phase imbalance of 258.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058851_consumption' has phase imbalance of 91.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058777_consumption' has phase imbalance of 135.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058557_consumption' has phase imbalance of 130.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1192310_consumption' has phase imbalance of 23.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058548_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058573_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058502_consumption' has phase imbalance of 163.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058860_consumption' has phase imbalance of 90.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058568_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058700_consumption' has phase imbalance of 116.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058842_consumption' has phase imbalance of 85.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058720_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058768_consumption' has phase imbalance of 78.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058866_consumption' has phase imbalance of 232.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058774_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058590_consumption' has phase imbalance of 106.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058899_consumption' has phase imbalance of 111.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058532_consumption' has phase imbalance of 95.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058690_consumption' has phase imbalance of 127.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058846_consumption' has phase imbalance of 128.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058707_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058533_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058658_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058527_consumption' has phase imbalance of 141.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058892_consumption' has phase imbalance of 188.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058625_consumption' has phase imbalance of 104.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058673_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058758_consumption' has phase imbalance of 43.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058662_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058757_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058550_consumption' has phase imbalance of 59.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058689_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058723_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058755_consumption' has phase imbalance of 105.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1191648_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058580_consumption' has phase imbalance of 47.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058867_consumption' has phase imbalance of 238.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058900_consumption' has phase imbalance of 39.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058536_consumption' has phase imbalance of 77.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058675_consumption' has phase imbalance of 198.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058556_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1191647_consumption' has phase imbalance of 107.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058852_consumption' has phase imbalance of 98.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058824_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058555_consumption' has phase imbalance of 110.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058849_consumption' has phase imbalance of 107.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058732_consumption' has phase imbalance of 54.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1145270_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058864_consumption' has phase imbalance of 268.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058719_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058725_consumption' has phase imbalance of 140.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058586_consumption' has phase imbalance of 48.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058871_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058894_consumption' has phase imbalance of 67.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1191644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058708_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058656_consumption' has phase imbalance of 78.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058736_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058891_consumption' has phase imbalance of 93.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058722_consumption' has phase imbalance of 142.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058826_consumption' has phase imbalance of 90.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058565_consumption' has phase imbalance of 111.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058585_consumption' has phase imbalance of 42.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058750_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058562_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058674_consumption' has phase imbalance of 146.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058589_consumption' has phase imbalance of 27.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058561_consumption' has phase imbalance of 37.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058855_consumption' has phase imbalance of 89.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058686_consumption' has phase imbalance of 225.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058684_consumption' has phase imbalance of 278.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058676_consumption' has phase imbalance of 116.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058578_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058785_consumption' has phase imbalance of 136.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058699_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058854_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058908_consumption' has phase imbalance of 38.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1191645_consumption' has phase imbalance of 51.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058698_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058735_consumption' has phase imbalance of 265.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058731_consumption' has phase imbalance of 282.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058775_consumption' has phase imbalance of 209.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058695_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058747_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058853_consumption' has phase imbalance of 176.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1145271_consumption' has phase imbalance of 229.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058738_consumption' has phase imbalance of 125.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058897_consumption' has phase imbalance of 107.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058709_consumption' has phase imbalance of 244.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058651_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058558_consumption' has phase imbalance of 240.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058655_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058763_consumption' has phase imbalance of 128.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058572_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1133475_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058623_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058906_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058769_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058642_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058516_consumption' has phase imbalance of 23.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058863_consumption' has phase imbalance of 112.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058672_consumption' has phase imbalance of 26.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058522_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058649_consumption' has phase imbalance of 128.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058575_consumption' has phase imbalance of 83.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058724_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058542_consumption' has phase imbalance of 172.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058861_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058524_consumption' has phase imbalance of 25.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058632_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058890_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus058560_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1133476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 738 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_HEINL' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus058794' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.726 MW |
| Total load Q | 1.42 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV033012_Transformer | 693.0 kVA | 69.8% |
| 52_MVLV090024_Transformer | 693.0 kVA | 68.0% |
| 52_MVLV041324_Transformer | 693.0 kVA | 57.9% |
| 52_MVLV003020_Transformer | 693.0 kVA | 38.9% |
| 52_MVLV017154_Transformer | 440.0 kVA | 25.0% |
| 52_MVLV001575_Transformer | 440.0 kVA | 20.3% |
| 52_MVLV003023_Transformer | 693.0 kVA | 25.4% |
| 52_MVLV081577_Transformer | 693.0 kVA | 19.2% |
| 52_MVLV049395_Transformer | 176.0 kVA | 4.9% |
| 52_MVLV039354_Transformer | 275.0 kVA | 6.6% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.73 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 390 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 390 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 13 |
| LV_236V | 4-wire | 377 / 377 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 377 |
| Neutral branches | 367 |
| Grounding points | 10 |
| Neutral sections | 10 |
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
| 11.78 kV | 13 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 41 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 87 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 73 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 11 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1140.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 377 / 13 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 485 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 485 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus058497_consumption, 52_LVBus058497_production, 52_LVBus058498_production, 52_LVBus058499_consumption, 52_LVBus058499_production, 52_LVBus058500_production, 52_LVBus058502_production, 52_LVBus058503_production, 52_LVBus058505_consumption, 52_LVBus058505_production, 52_LVBus058506_consumption, 52_LVBus058506_production, 52_LVBus058508_consumption, 52_LVBus058508_production, 52_LVBus058509_consumption, 52_LVBus058509_production, 52_LVBus058510_production, 52_LVBus058511_consumption, 52_LVBus058511_production, 52_LVBus058512_consumption, 52_LVBus058512_production, 52_LVBus058513_production, 52_LVBus058515_consumption, 52_LVBus058515_production, 52_LVBus058516_production, 52_LVBus058518_consumption, 52_LVBus058518_production, 52_LVBus058519_consumption, 52_LVBus058519_production, 52_LVBus058520_consumption, 52_LVBus058520_production, 52_LVBus058522_production, 52_LVBus058523_production, 52_LVBus058524_production, 52_LVBus058525_production, 52_LVBus058526_production, 52_LVBus058527_production, 52_LVBus058528_production, 52_LVBus058529_production, 52_LVBus058530_production, 52_LVBus058531_production, 52_LVBus058532_production, 52_LVBus058533_production, 52_LVBus058534_production, 52_LVBus058536_production, 52_LVBus058537_production, 52_LVBus058538_production, 52_LVBus058539_consumption, 52_LVBus058539_production, 52_LVBus058540_consumption, 52_LVBus058540_production, 52_LVBus058541_production, 52_LVBus058542_production, 52_LVBus058543_production, 52_LVBus058544_production, 52_LVBus058545_production, 52_LVBus058546_production, 52_LVBus058548_production, 52_LVBus058549_production, 52_LVBus058550_production, 52_LVBus058551_production, 52_LVBus058553_production, 52_LVBus058555_production, 52_LVBus058556_production, 52_LVBus058557_production, 52_LVBus058558_production, 52_LVBus058559_production, 52_LVBus058560_production, 52_LVBus058561_production, 52_LVBus058562_production, 52_LVBus058564_production, 52_LVBus058565_production, 52_LVBus058566_production, 52_LVBus058568_production, 52_LVBus058569_production, 52_LVBus058570_production, 52_LVBus058571_production, 52_LVBus058572_production, 52_LVBus058573_production, 52_LVBus058574_consumption, 52_LVBus058574_production, 52_LVBus058575_production, 52_LVBus058576_production, 52_LVBus058577_production, 52_LVBus058578_production, 52_LVBus058579_consumption, 52_LVBus058579_production, 52_LVBus058580_production, 52_LVBus058582_consumption, 52_LVBus058582_production, 52_LVBus058583_consumption, 52_LVBus058583_production, 52_LVBus058584_consumption, 52_LVBus058584_production, 52_LVBus058585_production, 52_LVBus058586_production, 52_LVBus058587_production, 52_LVBus058588_production, 52_LVBus058589_production, 52_LVBus058590_production, 52_LVBus058591_production, 52_LVBus058593_consumption, 52_LVBus058593_production, 52_LVBus058595_consumption, 52_LVBus058595_production, 52_LVBus058596_consumption, 52_LVBus058596_production, 52_LVBus058597_consumption, 52_LVBus058597_production, 52_LVBus058599_production, 52_LVBus058600_consumption, 52_LVBus058600_production, 52_LVBus058602_consumption, 52_LVBus058602_production, 52_LVBus058604_consumption, 52_LVBus058604_production, 52_LVBus058605_consumption, 52_LVBus058605_production, 52_LVBus058606_consumption, 52_LVBus058606_production, 52_LVBus058608_consumption, 52_LVBus058608_production, 52_LVBus058609_consumption, 52_LVBus058609_production, 52_LVBus058610_production, 52_LVBus058612_consumption, 52_LVBus058612_production, 52_LVBus058613_consumption, 52_LVBus058613_production, 52_LVBus058615_consumption, 52_LVBus058615_production, 52_LVBus058616_consumption, 52_LVBus058616_production, 52_LVBus058618_consumption, 52_LVBus058618_production, 52_LVBus058619_production, 52_LVBus058620_consumption, 52_LVBus058620_production, 52_LVBus058622_consumption, 52_LVBus058622_production, 52_LVBus058623_production, 52_LVBus058624_production, 52_LVBus058625_production, 52_LVBus058626_production, 52_LVBus058628_consumption, 52_LVBus058628_production, 52_LVBus058629_consumption, 52_LVBus058629_production, 52_LVBus058631_consumption, 52_LVBus058631_production, 52_LVBus058632_production, 52_LVBus058633_consumption, 52_LVBus058633_production, 52_LVBus058635_consumption, 52_LVBus058635_production, 52_LVBus058636_production, 52_LVBus058637_consumption, 52_LVBus058637_production, 52_LVBus058638_consumption, 52_LVBus058638_production, 52_LVBus058639_consumption, 52_LVBus058639_production, 52_LVBus058641_consumption, 52_LVBus058641_production, 52_LVBus058642_production, 52_LVBus058643_consumption, 52_LVBus058643_production, 52_LVBus058644_production, 52_LVBus058645_consumption, 52_LVBus058645_production, 52_LVBus058648_production, 52_LVBus058649_production, 52_LVBus058650_production, 52_LVBus058651_production, 52_LVBus058652_consumption, 52_LVBus058652_production, 52_LVBus058653_production, 52_LVBus058654_production, 52_LVBus058655_production, 52_LVBus058656_production, 52_LVBus058657_production, 52_LVBus058658_production, 52_LVBus058659_consumption, 52_LVBus058659_production, 52_LVBus058660_production, 52_LVBus058661_production, 52_LVBus058662_production, 52_LVBus058663_production, 52_LVBus058664_production, 52_LVBus058665_production, 52_LVBus058666_production, 52_LVBus058667_production, 52_LVBus058668_production, 52_LVBus058670_production, 52_LVBus058671_production, 52_LVBus058672_production, 52_LVBus058673_production, 52_LVBus058674_production, 52_LVBus058675_production, 52_LVBus058676_production, 52_LVBus058677_consumption, 52_LVBus058677_production, 52_LVBus058678_consumption, 52_LVBus058678_production, 52_LVBus058679_production, 52_LVBus058680_production, 52_LVBus058681_production, 52_LVBus058682_consumption, 52_LVBus058682_production, 52_LVBus058683_production, 52_LVBus058684_production, 52_LVBus058685_production, 52_LVBus058686_production, 52_LVBus058687_production, 52_LVBus058688_production, 52_LVBus058689_production, 52_LVBus058690_production, 52_LVBus058691_production, 52_LVBus058692_production, 52_LVBus058693_production, 52_LVBus058694_production, 52_LVBus058695_production, 52_LVBus058696_production, 52_LVBus058697_production, 52_LVBus058698_production, 52_LVBus058699_production, 52_LVBus058700_production, 52_LVBus058702_production, 52_LVBus058703_consumption, 52_LVBus058703_production, 52_LVBus058704_production, 52_LVBus058705_consumption, 52_LVBus058705_production, 52_LVBus058706_consumption, 52_LVBus058706_production, 52_LVBus058707_production, 52_LVBus058708_production, 52_LVBus058709_production, 52_LVBus058710_production, 52_LVBus058711_production, 52_LVBus058712_consumption, 52_LVBus058712_production, 52_LVBus058713_consumption, 52_LVBus058713_production, 52_LVBus058715_production, 52_LVBus058717_production, 52_LVBus058719_production, 52_LVBus058720_production, 52_LVBus058722_production, 52_LVBus058723_production, 52_LVBus058724_production, 52_LVBus058725_production, 52_LVBus058726_production, 52_LVBus058728_production, 52_LVBus058729_production, 52_LVBus058730_consumption, 52_LVBus058730_production, 52_LVBus058731_production, 52_LVBus058732_production, 52_LVBus058733_production, 52_LVBus058734_production, 52_LVBus058735_production, 52_LVBus058736_production, 52_LVBus058737_production, 52_LVBus058738_production, 52_LVBus058739_production, 52_LVBus058740_production, 52_LVBus058742_production, 52_LVBus058744_consumption, 52_LVBus058744_production, 52_LVBus058747_production, 52_LVBus058748_consumption, 52_LVBus058748_production, 52_LVBus058749_production, 52_LVBus058750_production, 52_LVBus058751_consumption, 52_LVBus058751_production, 52_LVBus058752_consumption, 52_LVBus058752_production, 52_LVBus058753_consumption, 52_LVBus058753_production, 52_LVBus058755_production, 52_LVBus058756_production, 52_LVBus058757_production, 52_LVBus058758_production, 52_LVBus058759_production, 52_LVBus058760_production, 52_LVBus058762_production, 52_LVBus058763_production, 52_LVBus058764_production, 52_LVBus058765_production, 52_LVBus058766_production, 52_LVBus058767_consumption, 52_LVBus058767_production, 52_LVBus058768_production, 52_LVBus058769_production, 52_LVBus058771_production, 52_LVBus058773_production, 52_LVBus058774_production, 52_LVBus058775_production, 52_LVBus058776_production, 52_LVBus058777_production, 52_LVBus058778_consumption, 52_LVBus058778_production, 52_LVBus058779_consumption, 52_LVBus058779_production, 52_LVBus058780_production, 52_LVBus058781_production, 52_LVBus058783_production, 52_LVBus058784_production, 52_LVBus058785_production, 52_LVBus058786_production, 52_LVBus058787_production, 52_LVBus058788_production, 52_LVBus058790_production, 52_LVBus058791_production, 52_LVBus058792_consumption, 52_LVBus058792_production, 52_LVBus058794_consumption, 52_LVBus058794_production, 52_LVBus058796_consumption, 52_LVBus058796_production, 52_LVBus058798_consumption, 52_LVBus058798_production, 52_LVBus058800_consumption, 52_LVBus058800_production, 52_LVBus058801_consumption, 52_LVBus058801_production, 52_LVBus058803_consumption, 52_LVBus058803_production, 52_LVBus058805_consumption, 52_LVBus058805_production, 52_LVBus058806_consumption, 52_LVBus058806_production, 52_LVBus058808_production, 52_LVBus058810_consumption, 52_LVBus058810_production, 52_LVBus058811_consumption, 52_LVBus058811_production, 52_LVBus058813_consumption, 52_LVBus058813_production, 52_LVBus058815_consumption, 52_LVBus058815_production, 52_LVBus058817_consumption, 52_LVBus058817_production, 52_LVBus058818_production, 52_LVBus058820_consumption, 52_LVBus058820_production, 52_LVBus058822_consumption, 52_LVBus058822_production, 52_LVBus058824_production, 52_LVBus058826_production, 52_LVBus058828_consumption, 52_LVBus058828_production, 52_LVBus058829_consumption, 52_LVBus058829_production, 52_LVBus058830_consumption, 52_LVBus058830_production, 52_LVBus058831_consumption, 52_LVBus058831_production, 52_LVBus058832_production, 52_LVBus058834_consumption, 52_LVBus058834_production, 52_LVBus058835_consumption, 52_LVBus058835_production, 52_LVBus058836_consumption, 52_LVBus058836_production, 52_LVBus058838_consumption, 52_LVBus058838_production, 52_LVBus058839_consumption, 52_LVBus058839_production, 52_LVBus058840_consumption, 52_LVBus058840_production, 52_LVBus058842_production, 52_LVBus058844_production, 52_LVBus058845_production, 52_LVBus058846_production, 52_LVBus058847_production, 52_LVBus058848_production, 52_LVBus058849_production, 52_LVBus058850_production, 52_LVBus058851_production, 52_LVBus058852_production, 52_LVBus058853_production, 52_LVBus058854_production, 52_LVBus058855_production, 52_LVBus058856_production, 52_LVBus058858_consumption, 52_LVBus058858_production, 52_LVBus058859_consumption, 52_LVBus058859_production, 52_LVBus058860_production, 52_LVBus058861_production, 52_LVBus058862_production, 52_LVBus058863_production, 52_LVBus058864_production, 52_LVBus058865_consumption, 52_LVBus058865_production, 52_LVBus058866_production, 52_LVBus058867_production, 52_LVBus058868_consumption, 52_LVBus058868_production, 52_LVBus058869_consumption, 52_LVBus058869_production, 52_LVBus058870_production, 52_LVBus058871_production, 52_LVBus058872_production, 52_LVBus058873_production, 52_LVBus058875_production, 52_LVBus058877_production, 52_LVBus058878_consumption, 52_LVBus058878_production, 52_LVBus058879_production, 52_LVBus058880_consumption, 52_LVBus058880_production, 52_LVBus058881_production, 52_LVBus058882_consumption, 52_LVBus058882_production, 52_LVBus058884_production, 52_LVBus058885_production, 52_LVBus058887_consumption, 52_LVBus058887_production, 52_LVBus058888_production, 52_LVBus058889_consumption, 52_LVBus058889_production, 52_LVBus058890_production, 52_LVBus058891_production, 52_LVBus058892_production, 52_LVBus058893_production, 52_LVBus058894_production, 52_LVBus058895_production, 52_LVBus058896_production, 52_LVBus058897_production, 52_LVBus058899_production, 52_LVBus058900_production, 52_LVBus058901_consumption, 52_LVBus058901_production, 52_LVBus058902_consumption, 52_LVBus058902_production, 52_LVBus058903_consumption, 52_LVBus058903_production, 52_LVBus058904_production, 52_LVBus058905_production, 52_LVBus058906_production, 52_LVBus058907_production, 52_LVBus058908_production, 52_LVBus058909_production, 52_LVBus058910_production, 52_LVBus1133475_production, 52_LVBus1133476_production, 52_LVBus1133477_production, 52_LVBus1133478_production, 52_LVBus1136989_consumption, 52_LVBus1136989_production, 52_LVBus1137303_consumption, 52_LVBus1137303_production, 52_LVBus1137304_consumption, 52_LVBus1137304_production, 52_LVBus1137305_consumption, 52_LVBus1137305_production, 52_LVBus1138116_consumption, 52_LVBus1138116_production, 52_LVBus1140288_consumption, 52_LVBus1140288_production, 52_LVBus1140289_production, 52_LVBus1145270_production, 52_LVBus1145271_production, 52_LVBus1145272_production, 52_LVBus1173183_consumption, 52_LVBus1173183_production, 52_LVBus1191642_production, 52_LVBus1191643_consumption, 52_LVBus1191643_production, 52_LVBus1191644_production, 52_LVBus1191645_production, 52_LVBus1191646_consumption, 52_LVBus1191646_production, 52_LVBus1191647_production, 52_LVBus1191648_production, 52_LVBus1191649_production, 52_LVBus1192309_production, 52_LVBus1192310_production, 52_MVLV014160_production, 52_MVLV021153_consumption, 52_MVLV021153_production.

## 9. Data Quality Summary

**Total findings:** 253 (0 errors, 4 warnings, 249 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  484 of 738 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.73 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  485 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058529_consumption`  
  Load '52_LVBus058529_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058541_consumption`  
  Load '52_LVBus058541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058498_consumption`  
  Load '52_LVBus058498_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058531_consumption`  
  Load '52_LVBus058531_consumption' has phase imbalance of 232.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058693_consumption`  
  Load '52_LVBus058693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058734_consumption`  
  Load '52_LVBus058734_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058873_consumption`  
  Load '52_LVBus058873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058765_consumption`  
  Load '52_LVBus058765_consumption' has phase imbalance of 77.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058660_consumption`  
  Load '52_LVBus058660_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058691_consumption`  
  Load '52_LVBus058691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058781_consumption`  
  Load '52_LVBus058781_consumption' has phase imbalance of 41.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058666_consumption`  
  Load '52_LVBus058666_consumption' has phase imbalance of 256.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058587_consumption`  
  Load '52_LVBus058587_consumption' has phase imbalance of 140.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058657_consumption`  
  Load '52_LVBus058657_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058862_consumption`  
  Load '52_LVBus058862_consumption' has phase imbalance of 188.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058664_consumption`  
  Load '52_LVBus058664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058537_consumption`  
  Load '52_LVBus058537_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058654_consumption`  
  Load '52_LVBus058654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058687_consumption`  
  Load '52_LVBus058687_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1133477_consumption`  
  Load '52_LVBus1133477_consumption' has phase imbalance of 181.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058696_consumption`  
  Load '52_LVBus058696_consumption' has phase imbalance of 39.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058895_consumption`  
  Load '52_LVBus058895_consumption' has phase imbalance of 49.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058717_consumption`  
  Load '52_LVBus058717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058525_consumption`  
  Load '52_LVBus058525_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058619_consumption`  
  Load '52_LVBus058619_consumption' has phase imbalance of 63.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058559_consumption`  
  Load '52_LVBus058559_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058905_consumption`  
  Load '52_LVBus058905_consumption' has phase imbalance of 31.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058526_consumption`  
  Load '52_LVBus058526_consumption' has phase imbalance of 54.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058566_consumption`  
  Load '52_LVBus058566_consumption' has phase imbalance of 57.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058591_consumption`  
  Load '52_LVBus058591_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058503_consumption`  
  Load '52_LVBus058503_consumption' has phase imbalance of 23.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058704_consumption`  
  Load '52_LVBus058704_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058661_consumption`  
  Load '52_LVBus058661_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058710_consumption`  
  Load '52_LVBus058710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058850_consumption`  
  Load '52_LVBus058850_consumption' has phase imbalance of 83.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058784_consumption`  
  Load '52_LVBus058784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058538_consumption`  
  Load '52_LVBus058538_consumption' has phase imbalance of 224.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058888_consumption`  
  Load '52_LVBus058888_consumption' has phase imbalance of 120.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058845_consumption`  
  Load '52_LVBus058845_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058896_consumption`  
  Load '52_LVBus058896_consumption' has phase imbalance of 153.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1145272_consumption`  
  Load '52_LVBus1145272_consumption' has phase imbalance of 291.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058884_consumption`  
  Load '52_LVBus058884_consumption' has phase imbalance of 64.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058847_consumption`  
  Load '52_LVBus058847_consumption' has phase imbalance of 108.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058893_consumption`  
  Load '52_LVBus058893_consumption' has phase imbalance of 97.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058588_consumption`  
  Load '52_LVBus058588_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058534_consumption`  
  Load '52_LVBus058534_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058875_consumption`  
  Load '52_LVBus058875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058737_consumption`  
  Load '52_LVBus058737_consumption' has phase imbalance of 103.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1191649_consumption`  
  Load '52_LVBus1191649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058762_consumption`  
  Load '52_LVBus058762_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058688_consumption`  
  Load '52_LVBus058688_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058551_consumption`  
  Load '52_LVBus058551_consumption' has phase imbalance of 220.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058668_consumption`  
  Load '52_LVBus058668_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058665_consumption`  
  Load '52_LVBus058665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058530_consumption`  
  Load '52_LVBus058530_consumption' has phase imbalance of 132.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058528_consumption`  
  Load '52_LVBus058528_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058780_consumption`  
  Load '52_LVBus058780_consumption' has phase imbalance of 33.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058510_consumption`  
  Load '52_LVBus058510_consumption' has phase imbalance of 38.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058879_consumption`  
  Load '52_LVBus058879_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058694_consumption`  
  Load '52_LVBus058694_consumption' has phase imbalance of 105.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058791_consumption`  
  Load '52_LVBus058791_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058771_consumption`  
  Load '52_LVBus058771_consumption' has phase imbalance of 293.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058500_consumption`  
  Load '52_LVBus058500_consumption' has phase imbalance of 88.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058740_consumption`  
  Load '52_LVBus058740_consumption' has phase imbalance of 221.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058564_consumption`  
  Load '52_LVBus058564_consumption' has phase imbalance of 106.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058697_consumption`  
  Load '52_LVBus058697_consumption' has phase imbalance of 206.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058681_consumption`  
  Load '52_LVBus058681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058569_consumption`  
  Load '52_LVBus058569_consumption' has phase imbalance of 89.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058523_consumption`  
  Load '52_LVBus058523_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058624_consumption`  
  Load '52_LVBus058624_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058702_consumption`  
  Load '52_LVBus058702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058776_consumption`  
  Load '52_LVBus058776_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058553_consumption`  
  Load '52_LVBus058553_consumption' has phase imbalance of 29.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058759_consumption`  
  Load '52_LVBus058759_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058728_consumption`  
  Load '52_LVBus058728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058729_consumption`  
  Load '52_LVBus058729_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058667_consumption`  
  Load '52_LVBus058667_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058671_consumption`  
  Load '52_LVBus058671_consumption' has phase imbalance of 43.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058756_consumption`  
  Load '52_LVBus058756_consumption' has phase imbalance of 73.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058907_consumption`  
  Load '52_LVBus058907_consumption' has phase imbalance of 147.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058636_consumption`  
  Load '52_LVBus058636_consumption' has phase imbalance of 96.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058577_consumption`  
  Load '52_LVBus058577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058711_consumption`  
  Load '52_LVBus058711_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058626_consumption`  
  Load '52_LVBus058626_consumption' has phase imbalance of 110.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058570_consumption`  
  Load '52_LVBus058570_consumption' has phase imbalance of 262.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058783_consumption`  
  Load '52_LVBus058783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058599_consumption`  
  Load '52_LVBus058599_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058543_consumption`  
  Load '52_LVBus058543_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058648_consumption`  
  Load '52_LVBus058648_consumption' has phase imbalance of 93.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058650_consumption`  
  Load '52_LVBus058650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058790_consumption`  
  Load '52_LVBus058790_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058576_consumption`  
  Load '52_LVBus058576_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058760_consumption`  
  Load '52_LVBus058760_consumption' has phase imbalance of 147.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058764_consumption`  
  Load '52_LVBus058764_consumption' has phase imbalance of 103.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058739_consumption`  
  Load '52_LVBus058739_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058679_consumption`  
  Load '52_LVBus058679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058766_consumption`  
  Load '52_LVBus058766_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058733_consumption`  
  Load '52_LVBus058733_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058881_consumption`  
  Load '52_LVBus058881_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058653_consumption`  
  Load '52_LVBus058653_consumption' has phase imbalance of 137.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058715_consumption`  
  Load '52_LVBus058715_consumption' has phase imbalance of 146.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058692_consumption`  
  Load '52_LVBus058692_consumption' has phase imbalance of 69.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058773_consumption`  
  Load '52_LVBus058773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058513_consumption`  
  Load '52_LVBus058513_consumption' has phase imbalance of 61.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1133478_consumption`  
  Load '52_LVBus1133478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058726_consumption`  
  Load '52_LVBus058726_consumption' has phase imbalance of 175.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058571_consumption`  
  Load '52_LVBus058571_consumption' has phase imbalance of 258.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058851_consumption`  
  Load '52_LVBus058851_consumption' has phase imbalance of 91.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058777_consumption`  
  Load '52_LVBus058777_consumption' has phase imbalance of 135.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058557_consumption`  
  Load '52_LVBus058557_consumption' has phase imbalance of 130.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1192310_consumption`  
  Load '52_LVBus1192310_consumption' has phase imbalance of 23.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058548_consumption`  
  Load '52_LVBus058548_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058573_consumption`  
  Load '52_LVBus058573_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058502_consumption`  
  Load '52_LVBus058502_consumption' has phase imbalance of 163.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058860_consumption`  
  Load '52_LVBus058860_consumption' has phase imbalance of 90.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058568_consumption`  
  Load '52_LVBus058568_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058848_consumption`  
  Load '52_LVBus058848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058786_consumption`  
  Load '52_LVBus058786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058700_consumption`  
  Load '52_LVBus058700_consumption' has phase imbalance of 116.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058842_consumption`  
  Load '52_LVBus058842_consumption' has phase imbalance of 85.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058720_consumption`  
  Load '52_LVBus058720_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058768_consumption`  
  Load '52_LVBus058768_consumption' has phase imbalance of 78.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058866_consumption`  
  Load '52_LVBus058866_consumption' has phase imbalance of 232.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058774_consumption`  
  Load '52_LVBus058774_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058590_consumption`  
  Load '52_LVBus058590_consumption' has phase imbalance of 106.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058899_consumption`  
  Load '52_LVBus058899_consumption' has phase imbalance of 111.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058546_consumption`  
  Load '52_LVBus058546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058532_consumption`  
  Load '52_LVBus058532_consumption' has phase imbalance of 95.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058690_consumption`  
  Load '52_LVBus058690_consumption' has phase imbalance of 127.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058846_consumption`  
  Load '52_LVBus058846_consumption' has phase imbalance of 128.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058707_consumption`  
  Load '52_LVBus058707_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058533_consumption`  
  Load '52_LVBus058533_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058658_consumption`  
  Load '52_LVBus058658_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058527_consumption`  
  Load '52_LVBus058527_consumption' has phase imbalance of 141.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058892_consumption`  
  Load '52_LVBus058892_consumption' has phase imbalance of 188.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058625_consumption`  
  Load '52_LVBus058625_consumption' has phase imbalance of 104.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058904_consumption`  
  Load '52_LVBus058904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058673_consumption`  
  Load '52_LVBus058673_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058758_consumption`  
  Load '52_LVBus058758_consumption' has phase imbalance of 43.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058662_consumption`  
  Load '52_LVBus058662_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058757_consumption`  
  Load '52_LVBus058757_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058550_consumption`  
  Load '52_LVBus058550_consumption' has phase imbalance of 59.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058689_consumption`  
  Load '52_LVBus058689_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058723_consumption`  
  Load '52_LVBus058723_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058755_consumption`  
  Load '52_LVBus058755_consumption' has phase imbalance of 105.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058856_consumption`  
  Load '52_LVBus058856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1191648_consumption`  
  Load '52_LVBus1191648_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058580_consumption`  
  Load '52_LVBus058580_consumption' has phase imbalance of 47.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058867_consumption`  
  Load '52_LVBus058867_consumption' has phase imbalance of 238.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058872_consumption`  
  Load '52_LVBus058872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058900_consumption`  
  Load '52_LVBus058900_consumption' has phase imbalance of 39.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058536_consumption`  
  Load '52_LVBus058536_consumption' has phase imbalance of 77.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058675_consumption`  
  Load '52_LVBus058675_consumption' has phase imbalance of 198.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058556_consumption`  
  Load '52_LVBus058556_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1191647_consumption`  
  Load '52_LVBus1191647_consumption' has phase imbalance of 107.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058852_consumption`  
  Load '52_LVBus058852_consumption' has phase imbalance of 98.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058824_consumption`  
  Load '52_LVBus058824_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058555_consumption`  
  Load '52_LVBus058555_consumption' has phase imbalance of 110.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058849_consumption`  
  Load '52_LVBus058849_consumption' has phase imbalance of 107.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058732_consumption`  
  Load '52_LVBus058732_consumption' has phase imbalance of 54.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1145270_consumption`  
  Load '52_LVBus1145270_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058864_consumption`  
  Load '52_LVBus058864_consumption' has phase imbalance of 268.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058719_consumption`  
  Load '52_LVBus058719_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058725_consumption`  
  Load '52_LVBus058725_consumption' has phase imbalance of 140.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058586_consumption`  
  Load '52_LVBus058586_consumption' has phase imbalance of 48.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058871_consumption`  
  Load '52_LVBus058871_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058894_consumption`  
  Load '52_LVBus058894_consumption' has phase imbalance of 67.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1191644_consumption`  
  Load '52_LVBus1191644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058708_consumption`  
  Load '52_LVBus058708_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058656_consumption`  
  Load '52_LVBus058656_consumption' has phase imbalance of 78.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058736_consumption`  
  Load '52_LVBus058736_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058787_consumption`  
  Load '52_LVBus058787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058910_consumption`  
  Load '52_LVBus058910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058877_consumption`  
  Load '52_LVBus058877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058891_consumption`  
  Load '52_LVBus058891_consumption' has phase imbalance of 93.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058722_consumption`  
  Load '52_LVBus058722_consumption' has phase imbalance of 142.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058826_consumption`  
  Load '52_LVBus058826_consumption' has phase imbalance of 90.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058565_consumption`  
  Load '52_LVBus058565_consumption' has phase imbalance of 111.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058585_consumption`  
  Load '52_LVBus058585_consumption' has phase imbalance of 42.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058750_consumption`  
  Load '52_LVBus058750_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058562_consumption`  
  Load '52_LVBus058562_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058674_consumption`  
  Load '52_LVBus058674_consumption' has phase imbalance of 146.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058683_consumption`  
  Load '52_LVBus058683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058610_consumption`  
  Load '52_LVBus058610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058589_consumption`  
  Load '52_LVBus058589_consumption' has phase imbalance of 27.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058561_consumption`  
  Load '52_LVBus058561_consumption' has phase imbalance of 37.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058855_consumption`  
  Load '52_LVBus058855_consumption' has phase imbalance of 89.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058686_consumption`  
  Load '52_LVBus058686_consumption' has phase imbalance of 225.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058684_consumption`  
  Load '52_LVBus058684_consumption' has phase imbalance of 278.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058676_consumption`  
  Load '52_LVBus058676_consumption' has phase imbalance of 116.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058578_consumption`  
  Load '52_LVBus058578_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058785_consumption`  
  Load '52_LVBus058785_consumption' has phase imbalance of 136.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058699_consumption`  
  Load '52_LVBus058699_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058854_consumption`  
  Load '52_LVBus058854_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058908_consumption`  
  Load '52_LVBus058908_consumption' has phase imbalance of 38.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1191645_consumption`  
  Load '52_LVBus1191645_consumption' has phase imbalance of 51.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058698_consumption`  
  Load '52_LVBus058698_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058735_consumption`  
  Load '52_LVBus058735_consumption' has phase imbalance of 265.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058731_consumption`  
  Load '52_LVBus058731_consumption' has phase imbalance of 282.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058909_consumption`  
  Load '52_LVBus058909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058775_consumption`  
  Load '52_LVBus058775_consumption' has phase imbalance of 209.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058695_consumption`  
  Load '52_LVBus058695_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058747_consumption`  
  Load '52_LVBus058747_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058853_consumption`  
  Load '52_LVBus058853_consumption' has phase imbalance of 176.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1145271_consumption`  
  Load '52_LVBus1145271_consumption' has phase imbalance of 229.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058738_consumption`  
  Load '52_LVBus058738_consumption' has phase imbalance of 125.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058897_consumption`  
  Load '52_LVBus058897_consumption' has phase imbalance of 107.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058709_consumption`  
  Load '52_LVBus058709_consumption' has phase imbalance of 244.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058651_consumption`  
  Load '52_LVBus058651_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058558_consumption`  
  Load '52_LVBus058558_consumption' has phase imbalance of 240.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058655_consumption`  
  Load '52_LVBus058655_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058545_consumption`  
  Load '52_LVBus058545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058763_consumption`  
  Load '52_LVBus058763_consumption' has phase imbalance of 128.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058572_consumption`  
  Load '52_LVBus058572_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1133475_consumption`  
  Load '52_LVBus1133475_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058623_consumption`  
  Load '52_LVBus058623_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058906_consumption`  
  Load '52_LVBus058906_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058769_consumption`  
  Load '52_LVBus058769_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058642_consumption`  
  Load '52_LVBus058642_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058516_consumption`  
  Load '52_LVBus058516_consumption' has phase imbalance of 23.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058863_consumption`  
  Load '52_LVBus058863_consumption' has phase imbalance of 112.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058672_consumption`  
  Load '52_LVBus058672_consumption' has phase imbalance of 26.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058522_consumption`  
  Load '52_LVBus058522_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058649_consumption`  
  Load '52_LVBus058649_consumption' has phase imbalance of 128.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058575_consumption`  
  Load '52_LVBus058575_consumption' has phase imbalance of 83.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058724_consumption`  
  Load '52_LVBus058724_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058542_consumption`  
  Load '52_LVBus058542_consumption' has phase imbalance of 172.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058861_consumption`  
  Load '52_LVBus058861_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058524_consumption`  
  Load '52_LVBus058524_consumption' has phase imbalance of 25.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058632_consumption`  
  Load '52_LVBus058632_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058890_consumption`  
  Load '52_LVBus058890_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus058560_consumption`  
  Load '52_LVBus058560_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1133476_consumption`  
  Load '52_LVBus1133476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 738 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_HEINL' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus058794' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  390 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  99 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 52_LVBus058522_consumption, 52_LVBus058528_consumption, 52_LVBus058529_consumption, 52_LVBus058531_consumption, 52_LVBus058533_consumption, 52_LVBus058537_consumption, 52_LVBus058538_consumption, 52_LVBus058541_consumption, 52_LVBus058542_consumption, 52_LVBus058543_consumption, 52_LVBus058545_consumption, 52_LVBus058546_consumption, 52_LVBus058551_consumption, 52_LVBus058556_consumption, 52_LVBus058558_consumption, 52_LVBus058560_consumption, 52_LVBus058562_consumption, 52_LVBus058570_consumption, 52_LVBus058571_consumption, 52_LVBus058573_consumption, 52_LVBus058577_consumption, 52_LVBus058578_consumption, 52_LVBus058591_consumption, 52_LVBus058610_consumption, 52_LVBus058623_consumption, 52_LVBus058624_consumption, 52_LVBus058650_consumption, 52_LVBus058654_consumption, 52_LVBus058655_consumption, 52_LVBus058662_consumption, 52_LVBus058664_consumption, 52_LVBus058665_consumption, 52_LVBus058666_consumption, 52_LVBus058667_consumption, 52_LVBus058679_consumption, 52_LVBus058681_consumption, 52_LVBus058683_consumption, 52_LVBus058684_consumption, 52_LVBus058686_consumption, 52_LVBus058689_consumption, 52_LVBus058691_consumption, 52_LVBus058693_consumption, 52_LVBus058695_consumption, 52_LVBus058697_consumption, 52_LVBus058698_consumption, 52_LVBus058699_consumption, 52_LVBus058702_consumption, 52_LVBus058704_consumption, 52_LVBus058707_consumption, 52_LVBus058708_consumption, 52_LVBus058709_consumption, 52_LVBus058710_consumption, 52_LVBus058711_consumption, 52_LVBus058717_consumption, 52_LVBus058724_consumption, 52_LVBus058726_consumption, 52_LVBus058728_consumption, 52_LVBus058731_consumption, 52_LVBus058733_consumption, 52_LVBus058734_consumption, 52_LVBus058735_consumption, 52_LVBus058736_consumption, 52_LVBus058739_consumption, 52_LVBus058740_consumption, 52_LVBus058766_consumption, 52_LVBus058771_consumption, 52_LVBus058773_consumption, 52_LVBus058774_consumption, 52_LVBus058775_consumption, 52_LVBus058783_consumption, 52_LVBus058784_consumption, 52_LVBus058786_consumption, 52_LVBus058787_consumption, 52_LVBus058848_consumption, 52_LVBus058853_consumption, 52_LVBus058856_consumption, 52_LVBus058861_consumption, 52_LVBus058864_consumption, 52_LVBus058866_consumption, 52_LVBus058867_consumption, 52_LVBus058872_consumption, 52_LVBus058873_consumption, 52_LVBus058875_consumption, 52_LVBus058877_consumption, 52_LVBus058879_consumption, 52_LVBus058890_consumption, 52_LVBus058896_consumption, 52_LVBus058904_consumption, 52_LVBus058906_consumption, 52_LVBus058909_consumption, 52_LVBus058910_consumption, 52_LVBus1133475_consumption, 52_LVBus1133476_consumption, 52_LVBus1133477_consumption, 52_LVBus1133478_consumption, 52_LVBus1145271_consumption, 52_LVBus1145272_consumption, 52_LVBus1191644_consumption, 52_LVBus1191649_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  369 group(s) of loads (738 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  485 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus058497_consumption, 52_LVBus058497_production, 52_LVBus058498_production, 52_LVBus058499_consumption, 52_LVBus058499_production, 52_LVBus058500_production, 52_LVBus058502_production, 52_LVBus058503_production, 52_LVBus058505_consumption, 52_LVBus058505_production, 52_LVBus058506_consumption, 52_LVBus058506_production, 52_LVBus058508_consumption, 52_LVBus058508_production, 52_LVBus058509_consumption, 52_LVBus058509_production, 52_LVBus058510_production, 52_LVBus058511_consumption, 52_LVBus058511_production, 52_LVBus058512_consumption, 52_LVBus058512_production, 52_LVBus058513_production, 52_LVBus058515_consumption, 52_LVBus058515_production, 52_LVBus058516_production, 52_LVBus058518_consumption, 52_LVBus058518_production, 52_LVBus058519_consumption, 52_LVBus058519_production, 52_LVBus058520_consumption, 52_LVBus058520_production, 52_LVBus058522_production, 52_LVBus058523_production, 52_LVBus058524_production, 52_LVBus058525_production, 52_LVBus058526_production, 52_LVBus058527_production, 52_LVBus058528_production, 52_LVBus058529_production, 52_LVBus058530_production, 52_LVBus058531_production, 52_LVBus058532_production, 52_LVBus058533_production, 52_LVBus058534_production, 52_LVBus058536_production, 52_LVBus058537_production, 52_LVBus058538_production, 52_LVBus058539_consumption, 52_LVBus058539_production, 52_LVBus058540_consumption, 52_LVBus058540_production, 52_LVBus058541_production, 52_LVBus058542_production, 52_LVBus058543_production, 52_LVBus058544_production, 52_LVBus058545_production, 52_LVBus058546_production, 52_LVBus058548_production, 52_LVBus058549_production, 52_LVBus058550_production, 52_LVBus058551_production, 52_LVBus058553_production, 52_LVBus058555_production, 52_LVBus058556_production, 52_LVBus058557_production, 52_LVBus058558_production, 52_LVBus058559_production, 52_LVBus058560_production, 52_LVBus058561_production, 52_LVBus058562_production, 52_LVBus058564_production, 52_LVBus058565_production, 52_LVBus058566_production, 52_LVBus058568_production, 52_LVBus058569_production, 52_LVBus058570_production, 52_LVBus058571_production, 52_LVBus058572_production, 52_LVBus058573_production, 52_LVBus058574_consumption, 52_LVBus058574_production, 52_LVBus058575_production, 52_LVBus058576_production, 52_LVBus058577_production, 52_LVBus058578_production, 52_LVBus058579_consumption, 52_LVBus058579_production, 52_LVBus058580_production, 52_LVBus058582_consumption, 52_LVBus058582_production, 52_LVBus058583_consumption, 52_LVBus058583_production, 52_LVBus058584_consumption, 52_LVBus058584_production, 52_LVBus058585_production, 52_LVBus058586_production, 52_LVBus058587_production, 52_LVBus058588_production, 52_LVBus058589_production, 52_LVBus058590_production, 52_LVBus058591_production, 52_LVBus058593_consumption, 52_LVBus058593_production, 52_LVBus058595_consumption, 52_LVBus058595_production, 52_LVBus058596_consumption, 52_LVBus058596_production, 52_LVBus058597_consumption, 52_LVBus058597_production, 52_LVBus058599_production, 52_LVBus058600_consumption, 52_LVBus058600_production, 52_LVBus058602_consumption, 52_LVBus058602_production, 52_LVBus058604_consumption, 52_LVBus058604_production, 52_LVBus058605_consumption, 52_LVBus058605_production, 52_LVBus058606_consumption, 52_LVBus058606_production, 52_LVBus058608_consumption, 52_LVBus058608_production, 52_LVBus058609_consumption, 52_LVBus058609_production, 52_LVBus058610_production, 52_LVBus058612_consumption, 52_LVBus058612_production, 52_LVBus058613_consumption, 52_LVBus058613_production, 52_LVBus058615_consumption, 52_LVBus058615_production, 52_LVBus058616_consumption, 52_LVBus058616_production, 52_LVBus058618_consumption, 52_LVBus058618_production, 52_LVBus058619_production, 52_LVBus058620_consumption, 52_LVBus058620_production, 52_LVBus058622_consumption, 52_LVBus058622_production, 52_LVBus058623_production, 52_LVBus058624_production, 52_LVBus058625_production, 52_LVBus058626_production, 52_LVBus058628_consumption, 52_LVBus058628_production, 52_LVBus058629_consumption, 52_LVBus058629_production, 52_LVBus058631_consumption, 52_LVBus058631_production, 52_LVBus058632_production, 52_LVBus058633_consumption, 52_LVBus058633_production, 52_LVBus058635_consumption, 52_LVBus058635_production, 52_LVBus058636_production, 52_LVBus058637_consumption, 52_LVBus058637_production, 52_LVBus058638_consumption, 52_LVBus058638_production, 52_LVBus058639_consumption, 52_LVBus058639_production, 52_LVBus058641_consumption, 52_LVBus058641_production, 52_LVBus058642_production, 52_LVBus058643_consumption, 52_LVBus058643_production, 52_LVBus058644_production, 52_LVBus058645_consumption, 52_LVBus058645_production, 52_LVBus058648_production, 52_LVBus058649_production, 52_LVBus058650_production, 52_LVBus058651_production, 52_LVBus058652_consumption, 52_LVBus058652_production, 52_LVBus058653_production, 52_LVBus058654_production, 52_LVBus058655_production, 52_LVBus058656_production, 52_LVBus058657_production, 52_LVBus058658_production, 52_LVBus058659_consumption, 52_LVBus058659_production, 52_LVBus058660_production, 52_LVBus058661_production, 52_LVBus058662_production, 52_LVBus058663_production, 52_LVBus058664_production, 52_LVBus058665_production, 52_LVBus058666_production, 52_LVBus058667_production, 52_LVBus058668_production, 52_LVBus058670_production, 52_LVBus058671_production, 52_LVBus058672_production, 52_LVBus058673_production, 52_LVBus058674_production, 52_LVBus058675_production, 52_LVBus058676_production, 52_LVBus058677_consumption, 52_LVBus058677_production, 52_LVBus058678_consumption, 52_LVBus058678_production, 52_LVBus058679_production, 52_LVBus058680_production, 52_LVBus058681_production, 52_LVBus058682_consumption, 52_LVBus058682_production, 52_LVBus058683_production, 52_LVBus058684_production, 52_LVBus058685_production, 52_LVBus058686_production, 52_LVBus058687_production, 52_LVBus058688_production, 52_LVBus058689_production, 52_LVBus058690_production, 52_LVBus058691_production, 52_LVBus058692_production, 52_LVBus058693_production, 52_LVBus058694_production, 52_LVBus058695_production, 52_LVBus058696_production, 52_LVBus058697_production, 52_LVBus058698_production, 52_LVBus058699_production, 52_LVBus058700_production, 52_LVBus058702_production, 52_LVBus058703_consumption, 52_LVBus058703_production, 52_LVBus058704_production, 52_LVBus058705_consumption, 52_LVBus058705_production, 52_LVBus058706_consumption, 52_LVBus058706_production, 52_LVBus058707_production, 52_LVBus058708_production, 52_LVBus058709_production, 52_LVBus058710_production, 52_LVBus058711_production, 52_LVBus058712_consumption, 52_LVBus058712_production, 52_LVBus058713_consumption, 52_LVBus058713_production, 52_LVBus058715_production, 52_LVBus058717_production, 52_LVBus058719_production, 52_LVBus058720_production, 52_LVBus058722_production, 52_LVBus058723_production, 52_LVBus058724_production, 52_LVBus058725_production, 52_LVBus058726_production, 52_LVBus058728_production, 52_LVBus058729_production, 52_LVBus058730_consumption, 52_LVBus058730_production, 52_LVBus058731_production, 52_LVBus058732_production, 52_LVBus058733_production, 52_LVBus058734_production, 52_LVBus058735_production, 52_LVBus058736_production, 52_LVBus058737_production, 52_LVBus058738_production, 52_LVBus058739_production, 52_LVBus058740_production, 52_LVBus058742_production, 52_LVBus058744_consumption, 52_LVBus058744_production, 52_LVBus058747_production, 52_LVBus058748_consumption, 52_LVBus058748_production, 52_LVBus058749_production, 52_LVBus058750_production, 52_LVBus058751_consumption, 52_LVBus058751_production, 52_LVBus058752_consumption, 52_LVBus058752_production, 52_LVBus058753_consumption, 52_LVBus058753_production, 52_LVBus058755_production, 52_LVBus058756_production, 52_LVBus058757_production, 52_LVBus058758_production, 52_LVBus058759_production, 52_LVBus058760_production, 52_LVBus058762_production, 52_LVBus058763_production, 52_LVBus058764_production, 52_LVBus058765_production, 52_LVBus058766_production, 52_LVBus058767_consumption, 52_LVBus058767_production, 52_LVBus058768_production, 52_LVBus058769_production, 52_LVBus058771_production, 52_LVBus058773_production, 52_LVBus058774_production, 52_LVBus058775_production, 52_LVBus058776_production, 52_LVBus058777_production, 52_LVBus058778_consumption, 52_LVBus058778_production, 52_LVBus058779_consumption, 52_LVBus058779_production, 52_LVBus058780_production, 52_LVBus058781_production, 52_LVBus058783_production, 52_LVBus058784_production, 52_LVBus058785_production, 52_LVBus058786_production, 52_LVBus058787_production, 52_LVBus058788_production, 52_LVBus058790_production, 52_LVBus058791_production, 52_LVBus058792_consumption, 52_LVBus058792_production, 52_LVBus058794_consumption, 52_LVBus058794_production, 52_LVBus058796_consumption, 52_LVBus058796_production, 52_LVBus058798_consumption, 52_LVBus058798_production, 52_LVBus058800_consumption, 52_LVBus058800_production, 52_LVBus058801_consumption, 52_LVBus058801_production, 52_LVBus058803_consumption, 52_LVBus058803_production, 52_LVBus058805_consumption, 52_LVBus058805_production, 52_LVBus058806_consumption, 52_LVBus058806_production, 52_LVBus058808_production, 52_LVBus058810_consumption, 52_LVBus058810_production, 52_LVBus058811_consumption, 52_LVBus058811_production, 52_LVBus058813_consumption, 52_LVBus058813_production, 52_LVBus058815_consumption, 52_LVBus058815_production, 52_LVBus058817_consumption, 52_LVBus058817_production, 52_LVBus058818_production, 52_LVBus058820_consumption, 52_LVBus058820_production, 52_LVBus058822_consumption, 52_LVBus058822_production, 52_LVBus058824_production, 52_LVBus058826_production, 52_LVBus058828_consumption, 52_LVBus058828_production, 52_LVBus058829_consumption, 52_LVBus058829_production, 52_LVBus058830_consumption, 52_LVBus058830_production, 52_LVBus058831_consumption, 52_LVBus058831_production, 52_LVBus058832_production, 52_LVBus058834_consumption, 52_LVBus058834_production, 52_LVBus058835_consumption, 52_LVBus058835_production, 52_LVBus058836_consumption, 52_LVBus058836_production, 52_LVBus058838_consumption, 52_LVBus058838_production, 52_LVBus058839_consumption, 52_LVBus058839_production, 52_LVBus058840_consumption, 52_LVBus058840_production, 52_LVBus058842_production, 52_LVBus058844_production, 52_LVBus058845_production, 52_LVBus058846_production, 52_LVBus058847_production, 52_LVBus058848_production, 52_LVBus058849_production, 52_LVBus058850_production, 52_LVBus058851_production, 52_LVBus058852_production, 52_LVBus058853_production, 52_LVBus058854_production, 52_LVBus058855_production, 52_LVBus058856_production, 52_LVBus058858_consumption, 52_LVBus058858_production, 52_LVBus058859_consumption, 52_LVBus058859_production, 52_LVBus058860_production, 52_LVBus058861_production, 52_LVBus058862_production, 52_LVBus058863_production, 52_LVBus058864_production, 52_LVBus058865_consumption, 52_LVBus058865_production, 52_LVBus058866_production, 52_LVBus058867_production, 52_LVBus058868_consumption, 52_LVBus058868_production, 52_LVBus058869_consumption, 52_LVBus058869_production, 52_LVBus058870_production, 52_LVBus058871_production, 52_LVBus058872_production, 52_LVBus058873_production, 52_LVBus058875_production, 52_LVBus058877_production, 52_LVBus058878_consumption, 52_LVBus058878_production, 52_LVBus058879_production, 52_LVBus058880_consumption, 52_LVBus058880_production, 52_LVBus058881_production, 52_LVBus058882_consumption, 52_LVBus058882_production, 52_LVBus058884_production, 52_LVBus058885_production, 52_LVBus058887_consumption, 52_LVBus058887_production, 52_LVBus058888_production, 52_LVBus058889_consumption, 52_LVBus058889_production, 52_LVBus058890_production, 52_LVBus058891_production, 52_LVBus058892_production, 52_LVBus058893_production, 52_LVBus058894_production, 52_LVBus058895_production, 52_LVBus058896_production, 52_LVBus058897_production, 52_LVBus058899_production, 52_LVBus058900_production, 52_LVBus058901_consumption, 52_LVBus058901_production, 52_LVBus058902_consumption, 52_LVBus058902_production, 52_LVBus058903_consumption, 52_LVBus058903_production, 52_LVBus058904_production, 52_LVBus058905_production, 52_LVBus058906_production, 52_LVBus058907_production, 52_LVBus058908_production, 52_LVBus058909_production, 52_LVBus058910_production, 52_LVBus1133475_production, 52_LVBus1133476_production, 52_LVBus1133477_production, 52_LVBus1133478_production, 52_LVBus1136989_consumption, 52_LVBus1136989_production, 52_LVBus1137303_consumption, 52_LVBus1137303_production, 52_LVBus1137304_consumption, 52_LVBus1137304_production, 52_LVBus1137305_consumption, 52_LVBus1137305_production, 52_LVBus1138116_consumption, 52_LVBus1138116_production, 52_LVBus1140288_consumption, 52_LVBus1140288_production, 52_LVBus1140289_production, 52_LVBus1145270_production, 52_LVBus1145271_production, 52_LVBus1145272_production, 52_LVBus1173183_consumption, 52_LVBus1173183_production, 52_LVBus1191642_production, 52_LVBus1191643_consumption, 52_LVBus1191643_production, 52_LVBus1191644_production, 52_LVBus1191645_production, 52_LVBus1191646_consumption, 52_LVBus1191646_production, 52_LVBus1191647_production, 52_LVBus1191648_production, 52_LVBus1191649_production, 52_LVBus1192309_production, 52_LVBus1192310_production, 52_MVLV014160_production, 52_MVLV021153_consumption, 52_MVLV021153_production.

