# BMOPF Network Summary: 75_MVFeeder2731

**Generated:** 2026-10-01 23:34:24  
**Findings:** 0 errors · 5 warnings · 354 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 23 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 509 |  |
| line | 485 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 920 | 3.492 MW, 1.05 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 23 |  |
| switch | 0 |  |
| transformer | 23 | Dyn11×23 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 27 | 26 | 2 | 0 |
| LV_236V | 236.0 V | 482 | 459 | 918 | 0 |

**Transformer transitions:**

- `75_MVLV130167_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV072881_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV141953_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV050120_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV007219_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV111714_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV072905_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV006933_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV136069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV006931_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV168948_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV157804_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV131534_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV029961_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV094712_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV169078_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV111328_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV044893_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV152797_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067556_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV039491_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV133238_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066380_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 180 |
| Tree depth (max hops) | 31 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 509 | 1 | 508 | 0 | 0 | 0 |
| Tier LV_236V | 482 | 23 | 459 | 0 | 0 | 0 |
| Tier MV_11.8kV | 27 | 1 | 26 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 23; skipped invalid branches: 0.

Galvanic zones: 24; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MTEND | MV_11.8kV | 27 | 0 | 0 | 23 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2009 declared bus terminals; 1914 mapped line/closed-switch conductor edges; 95 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 31300.0 | 2.371 | 2760 |
| q_nom | 0.0 | 9380.0 | 2.371 | 2760 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.26 | 1060.0 | 1.517 | 485 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.531 | 23 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 539 of 920 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261488_consumption' has phase imbalance of 226.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261680_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261817_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261355_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261797_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261472_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261615_consumption' has phase imbalance of 256.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261642_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261738_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261600_consumption' has phase imbalance of 296.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261653_consumption' has phase imbalance of 289.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261693_consumption' has phase imbalance of 38.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261412_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261606_consumption' has phase imbalance of 227.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261793_consumption' has phase imbalance of 60.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261629_consumption' has phase imbalance of 92.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261370_consumption' has phase imbalance of 221.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261716_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2011918_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261673_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261338_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261613_consumption' has phase imbalance of 291.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261795_consumption' has phase imbalance of 54.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261607_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261828_consumption' has phase imbalance of 61.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261373_consumption' has phase imbalance of 40.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261644_consumption' has phase imbalance of 255.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261454_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261740_consumption' has phase imbalance of 265.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2009451_consumption' has phase imbalance of 123.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261729_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261805_consumption' has phase imbalance of 173.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1938201_consumption' has phase imbalance of 165.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261437_consumption' has phase imbalance of 20.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261611_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261524_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261844_consumption' has phase imbalance of 92.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261382_consumption' has phase imbalance of 201.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261369_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261460_consumption' has phase imbalance of 46.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261855_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261377_consumption' has phase imbalance of 265.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261444_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261596_consumption' has phase imbalance of 214.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261741_consumption' has phase imbalance of 212.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261420_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261422_consumption' has phase imbalance of 63.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261806_consumption' has phase imbalance of 163.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261826_consumption' has phase imbalance of 122.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261557_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261396_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261562_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261480_consumption' has phase imbalance of 85.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261780_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261707_consumption' has phase imbalance of 111.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261401_consumption' has phase imbalance of 48.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261648_consumption' has phase imbalance of 119.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261486_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261469_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261523_consumption' has phase imbalance of 65.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261516_consumption' has phase imbalance of 117.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261411_consumption' has phase imbalance of 130.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261587_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261778_consumption' has phase imbalance of 128.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261576_consumption' has phase imbalance of 162.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261718_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261491_consumption' has phase imbalance of 206.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261510_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261625_consumption' has phase imbalance of 57.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261402_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261829_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261706_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261409_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261609_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261368_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261802_consumption' has phase imbalance of 224.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261614_consumption' has phase imbalance of 187.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261342_consumption' has phase imbalance of 155.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261457_consumption' has phase imbalance of 114.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261622_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261476_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261352_consumption' has phase imbalance of 90.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261731_consumption' has phase imbalance of 167.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261783_consumption' has phase imbalance of 22.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261808_consumption' has phase imbalance of 98.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1938200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261423_consumption' has phase imbalance of 180.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261592_consumption' has phase imbalance of 41.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261458_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261442_consumption' has phase imbalance of 40.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261391_consumption' has phase imbalance of 143.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261558_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261347_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261633_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261418_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261834_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261703_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261383_consumption' has phase imbalance of 96.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261408_consumption' has phase imbalance of 261.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261630_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261452_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261598_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261435_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261588_consumption' has phase imbalance of 215.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261434_consumption' has phase imbalance of 234.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261667_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261626_consumption' has phase imbalance of 280.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261470_consumption' has phase imbalance of 37.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261597_consumption' has phase imbalance of 158.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261676_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261438_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261583_consumption' has phase imbalance of 180.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261556_consumption' has phase imbalance of 132.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261669_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261564_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261344_consumption' has phase imbalance of 208.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261569_consumption' has phase imbalance of 78.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261543_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261579_consumption' has phase imbalance of 148.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261475_consumption' has phase imbalance of 41.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261865_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261357_consumption' has phase imbalance of 165.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261658_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261535_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261520_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261634_consumption' has phase imbalance of 172.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261832_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261620_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261455_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261830_consumption' has phase imbalance of 131.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261734_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261358_consumption' has phase imbalance of 120.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261801_consumption' has phase imbalance of 278.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261477_consumption' has phase imbalance of 131.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261447_consumption' has phase imbalance of 80.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261792_consumption' has phase imbalance of 38.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261593_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261761_consumption' has phase imbalance of 46.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261359_consumption' has phase imbalance of 53.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261490_consumption' has phase imbalance of 276.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261665_consumption' has phase imbalance of 253.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261691_consumption' has phase imbalance of 256.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261666_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261479_consumption' has phase imbalance of 122.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261585_consumption' has phase imbalance of 139.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261812_consumption' has phase imbalance of 86.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261854_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261419_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261789_consumption' has phase imbalance of 118.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261511_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261514_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261771_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261387_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261664_consumption' has phase imbalance of 262.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261380_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261692_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261550_consumption' has phase imbalance of 247.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261513_consumption' has phase imbalance of 226.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261532_consumption' has phase imbalance of 273.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261345_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261660_consumption' has phase imbalance of 247.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261485_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261536_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261677_consumption' has phase imbalance of 132.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261528_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261459_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261617_consumption' has phase imbalance of 217.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261570_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261742_consumption' has phase imbalance of 213.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261578_consumption' has phase imbalance of 85.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261804_consumption' has phase imbalance of 127.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261407_consumption' has phase imbalance of 293.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261608_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261353_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261811_consumption' has phase imbalance of 133.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261821_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261700_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261605_consumption' has phase imbalance of 218.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261449_consumption' has phase imbalance of 27.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261366_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261809_consumption' has phase imbalance of 134.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261541_consumption' has phase imbalance of 271.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261799_consumption' has phase imbalance of 28.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261687_consumption' has phase imbalance of 65.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261356_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261712_consumption' has phase imbalance of 221.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261833_consumption' has phase imbalance of 40.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261573_consumption' has phase imbalance of 82.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261492_consumption' has phase imbalance of 207.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261354_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261580_consumption' has phase imbalance of 168.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261483_consumption' has phase imbalance of 255.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261722_consumption' has phase imbalance of 89.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261542_consumption' has phase imbalance of 143.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261638_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261728_consumption' has phase imbalance of 76.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261604_consumption' has phase imbalance of 281.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261336_consumption' has phase imbalance of 36.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261862_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261443_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261603_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261702_consumption' has phase imbalance of 276.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261777_consumption' has phase imbalance of 221.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261856_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261416_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261853_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261647_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261465_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261671_consumption' has phase imbalance of 144.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261360_consumption' has phase imbalance of 110.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261772_consumption' has phase imbalance of 292.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261675_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261610_consumption' has phase imbalance of 284.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261747_consumption' has phase imbalance of 124.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261512_consumption' has phase imbalance of 44.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261640_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261539_consumption' has phase imbalance of 231.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261635_consumption' has phase imbalance of 187.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261522_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261413_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261645_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261482_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261842_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261810_consumption' has phase imbalance of 23.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261567_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261538_consumption' has phase imbalance of 51.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261750_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261484_consumption' has phase imbalance of 275.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261748_consumption' has phase imbalance of 106.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261803_consumption' has phase imbalance of 138.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261637_consumption' has phase imbalance of 144.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261436_consumption' has phase imbalance of 121.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261775_consumption' has phase imbalance of 63.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261654_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261448_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261739_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261767_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261831_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261737_consumption' has phase imbalance of 214.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261584_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261389_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261545_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261746_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261781_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261818_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261582_consumption' has phase imbalance of 227.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261619_consumption' has phase imbalance of 222.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261768_consumption' has phase imbalance of 281.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261819_consumption' has phase imbalance of 288.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261672_consumption' has phase imbalance of 139.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261774_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261421_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261659_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261663_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261788_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261745_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261374_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261836_consumption' has phase imbalance of 20.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261530_consumption' has phase imbalance of 98.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261838_consumption' has phase imbalance of 71.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261527_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261870_consumption' has phase imbalance of 268.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261493_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261871_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261670_consumption' has phase imbalance of 232.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261581_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1261646_consumption' has phase imbalance of 276.3%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 920 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_MTEND' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.492 MW |
| Total load Q | 1.05 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV130167_Transformer | 176.0 kVA | 8.0% |
| 75_MVLV072881_Transformer | 440.0 kVA | 23.4% |
| 75_MVLV141953_Transformer | 440.0 kVA | 20.6% |
| 75_MVLV050120_Transformer | 440.0 kVA | 29.7% |
| 75_MVLV007219_Transformer | 440.0 kVA | 26.6% |
| 75_MVLV111714_Transformer | 693.0 kVA | 38.2% |
| 75_MVLV072905_Transformer | 1.1 MVA | 33.9% |
| 75_MVLV006933_Transformer | 693.0 kVA | 44.6% |
| 75_MVLV136069_Transformer | 440.0 kVA | 35.8% |
| 75_MVLV006931_Transformer | 693.0 kVA | 55.9% |
| 75_MVLV168948_Transformer | 275.0 kVA | 15.0% |
| 75_MVLV157804_Transformer | 1.1 MVA | 36.4% |
| 75_MVLV131534_Transformer | 275.0 kVA | 21.2% |
| 75_MVLV029961_Transformer | 693.0 kVA | 38.1% |
| 75_MVLV094712_Transformer | 275.0 kVA | 16.1% |
| 75_MVLV169078_Transformer | 440.0 kVA | 26.7% |
| 75_MVLV111328_Transformer | 440.0 kVA | 24.8% |
| 75_MVLV044893_Transformer | 693.0 kVA | 26.2% |
| 75_MVLV152797_Transformer | 440.0 kVA | 23.6% |
| 75_MVLV067556_Transformer | 275.0 kVA | 45.5% |
| 75_MVLV039491_Transformer | 110.0 kVA | 5.6% |
| 75_MVLV133238_Transformer | 176.0 kVA | 20.1% |
| 75_MVLV066380_Transformer | 693.0 kVA | 16.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.49 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_LVBus1261640' (LV, 0.24 kV) has an electrical reach of 1.2 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 509 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 509 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 23 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 27 |
| LV_236V | 4-wire | 482 / 482 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 482 |
| Neutral branches | 459 |
| Grounding points | 23 |
| Neutral sections | 23 |
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
| 11.78 kV | 27 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 64 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 43 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 53 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 49 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 24 |
| Islands without voltage reference | 0 |
| Line impedance spread | 385.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 482 / 27 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 540 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 540 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1261336_production, 75_LVBus1261337_consumption, 75_LVBus1261337_production, 75_LVBus1261338_production, 75_LVBus1261340_consumption, 75_LVBus1261340_production, 75_LVBus1261341_production, 75_LVBus1261342_production, 75_LVBus1261343_consumption, 75_LVBus1261343_production, 75_LVBus1261344_production, 75_LVBus1261345_production, 75_LVBus1261346_production, 75_LVBus1261347_production, 75_LVBus1261348_consumption, 75_LVBus1261348_production, 75_LVBus1261349_production, 75_LVBus1261351_consumption, 75_LVBus1261351_production, 75_LVBus1261352_production, 75_LVBus1261353_production, 75_LVBus1261354_production, 75_LVBus1261355_production, 75_LVBus1261356_production, 75_LVBus1261357_production, 75_LVBus1261358_production, 75_LVBus1261359_production, 75_LVBus1261360_production, 75_LVBus1261362_consumption, 75_LVBus1261362_production, 75_LVBus1261363_production, 75_LVBus1261364_production, 75_LVBus1261365_production, 75_LVBus1261366_production, 75_LVBus1261367_consumption, 75_LVBus1261367_production, 75_LVBus1261368_production, 75_LVBus1261369_production, 75_LVBus1261370_production, 75_LVBus1261371_consumption, 75_LVBus1261371_production, 75_LVBus1261372_production, 75_LVBus1261373_production, 75_LVBus1261374_production, 75_LVBus1261375_production, 75_LVBus1261376_production, 75_LVBus1261377_production, 75_LVBus1261379_consumption, 75_LVBus1261379_production, 75_LVBus1261380_production, 75_LVBus1261381_consumption, 75_LVBus1261381_production, 75_LVBus1261382_production, 75_LVBus1261383_production, 75_LVBus1261384_consumption, 75_LVBus1261384_production, 75_LVBus1261385_production, 75_LVBus1261386_production, 75_LVBus1261387_production, 75_LVBus1261388_production, 75_LVBus1261389_production, 75_LVBus1261390_production, 75_LVBus1261391_production, 75_LVBus1261392_consumption, 75_LVBus1261392_production, 75_LVBus1261393_production, 75_LVBus1261394_production, 75_LVBus1261395_production, 75_LVBus1261396_production, 75_LVBus1261398_consumption, 75_LVBus1261398_production, 75_LVBus1261399_consumption, 75_LVBus1261399_production, 75_LVBus1261400_production, 75_LVBus1261401_production, 75_LVBus1261402_production, 75_LVBus1261403_production, 75_LVBus1261405_production, 75_LVBus1261406_consumption, 75_LVBus1261406_production, 75_LVBus1261407_production, 75_LVBus1261408_production, 75_LVBus1261409_production, 75_LVBus1261410_consumption, 75_LVBus1261410_production, 75_LVBus1261411_production, 75_LVBus1261412_production, 75_LVBus1261413_production, 75_LVBus1261414_consumption, 75_LVBus1261414_production, 75_LVBus1261416_production, 75_LVBus1261417_consumption, 75_LVBus1261417_production, 75_LVBus1261418_production, 75_LVBus1261419_production, 75_LVBus1261420_production, 75_LVBus1261421_production, 75_LVBus1261422_production, 75_LVBus1261423_production, 75_LVBus1261424_production, 75_LVBus1261425_production, 75_LVBus1261427_production, 75_LVBus1261428_production, 75_LVBus1261430_consumption, 75_LVBus1261430_production, 75_LVBus1261432_consumption, 75_LVBus1261432_production, 75_LVBus1261433_consumption, 75_LVBus1261433_production, 75_LVBus1261434_production, 75_LVBus1261435_production, 75_LVBus1261436_production, 75_LVBus1261437_production, 75_LVBus1261438_production, 75_LVBus1261439_consumption, 75_LVBus1261439_production, 75_LVBus1261440_consumption, 75_LVBus1261440_production, 75_LVBus1261441_consumption, 75_LVBus1261441_production, 75_LVBus1261442_production, 75_LVBus1261443_production, 75_LVBus1261444_production, 75_LVBus1261445_consumption, 75_LVBus1261445_production, 75_LVBus1261446_production, 75_LVBus1261447_production, 75_LVBus1261448_production, 75_LVBus1261449_production, 75_LVBus1261450_production, 75_LVBus1261452_production, 75_LVBus1261454_production, 75_LVBus1261455_production, 75_LVBus1261456_production, 75_LVBus1261457_production, 75_LVBus1261458_production, 75_LVBus1261459_production, 75_LVBus1261460_production, 75_LVBus1261461_production, 75_LVBus1261462_production, 75_LVBus1261464_production, 75_LVBus1261465_production, 75_LVBus1261466_production, 75_LVBus1261468_consumption, 75_LVBus1261468_production, 75_LVBus1261469_production, 75_LVBus1261470_production, 75_LVBus1261471_production, 75_LVBus1261472_production, 75_LVBus1261474_consumption, 75_LVBus1261474_production, 75_LVBus1261475_production, 75_LVBus1261476_production, 75_LVBus1261477_production, 75_LVBus1261478_consumption, 75_LVBus1261478_production, 75_LVBus1261479_production, 75_LVBus1261480_production, 75_LVBus1261482_production, 75_LVBus1261483_production, 75_LVBus1261484_production, 75_LVBus1261485_production, 75_LVBus1261486_production, 75_LVBus1261487_production, 75_LVBus1261488_production, 75_LVBus1261489_consumption, 75_LVBus1261489_production, 75_LVBus1261490_production, 75_LVBus1261491_production, 75_LVBus1261492_production, 75_LVBus1261493_production, 75_LVBus1261495_consumption, 75_LVBus1261495_production, 75_LVBus1261497_consumption, 75_LVBus1261497_production, 75_LVBus1261498_consumption, 75_LVBus1261498_production, 75_LVBus1261499_production, 75_LVBus1261501_consumption, 75_LVBus1261501_production, 75_LVBus1261502_consumption, 75_LVBus1261502_production, 75_LVBus1261503_consumption, 75_LVBus1261503_production, 75_LVBus1261505_consumption, 75_LVBus1261505_production, 75_LVBus1261507_consumption, 75_LVBus1261507_production, 75_LVBus1261508_consumption, 75_LVBus1261508_production, 75_LVBus1261510_production, 75_LVBus1261511_production, 75_LVBus1261512_production, 75_LVBus1261513_production, 75_LVBus1261514_production, 75_LVBus1261516_production, 75_LVBus1261517_production, 75_LVBus1261518_consumption, 75_LVBus1261518_production, 75_LVBus1261520_production, 75_LVBus1261521_production, 75_LVBus1261522_production, 75_LVBus1261523_production, 75_LVBus1261524_production, 75_LVBus1261525_production, 75_LVBus1261526_production, 75_LVBus1261527_production, 75_LVBus1261528_production, 75_LVBus1261530_production, 75_LVBus1261532_production, 75_LVBus1261533_consumption, 75_LVBus1261533_production, 75_LVBus1261534_production, 75_LVBus1261535_production, 75_LVBus1261536_production, 75_LVBus1261538_production, 75_LVBus1261539_production, 75_LVBus1261541_production, 75_LVBus1261542_production, 75_LVBus1261543_production, 75_LVBus1261545_production, 75_LVBus1261546_production, 75_LVBus1261547_production, 75_LVBus1261548_production, 75_LVBus1261550_production, 75_LVBus1261551_consumption, 75_LVBus1261551_production, 75_LVBus1261552_production, 75_LVBus1261554_production, 75_LVBus1261556_production, 75_LVBus1261557_production, 75_LVBus1261558_production, 75_LVBus1261559_production, 75_LVBus1261561_consumption, 75_LVBus1261561_production, 75_LVBus1261562_production, 75_LVBus1261563_consumption, 75_LVBus1261563_production, 75_LVBus1261564_production, 75_LVBus1261566_consumption, 75_LVBus1261566_production, 75_LVBus1261567_production, 75_LVBus1261569_production, 75_LVBus1261570_production, 75_LVBus1261572_consumption, 75_LVBus1261572_production, 75_LVBus1261573_production, 75_LVBus1261574_production, 75_LVBus1261575_production, 75_LVBus1261576_production, 75_LVBus1261578_production, 75_LVBus1261579_production, 75_LVBus1261580_production, 75_LVBus1261581_production, 75_LVBus1261582_production, 75_LVBus1261583_production, 75_LVBus1261584_production, 75_LVBus1261585_production, 75_LVBus1261587_production, 75_LVBus1261588_production, 75_LVBus1261589_production, 75_LVBus1261590_production, 75_LVBus1261591_production, 75_LVBus1261592_production, 75_LVBus1261593_production, 75_LVBus1261594_production, 75_LVBus1261595_production, 75_LVBus1261596_production, 75_LVBus1261597_production, 75_LVBus1261598_production, 75_LVBus1261600_production, 75_LVBus1261601_production, 75_LVBus1261602_production, 75_LVBus1261603_production, 75_LVBus1261604_production, 75_LVBus1261605_production, 75_LVBus1261606_production, 75_LVBus1261607_production, 75_LVBus1261608_production, 75_LVBus1261609_production, 75_LVBus1261610_production, 75_LVBus1261611_production, 75_LVBus1261612_production, 75_LVBus1261613_production, 75_LVBus1261614_production, 75_LVBus1261615_production, 75_LVBus1261616_production, 75_LVBus1261617_production, 75_LVBus1261618_production, 75_LVBus1261619_production, 75_LVBus1261620_production, 75_LVBus1261622_production, 75_LVBus1261623_consumption, 75_LVBus1261623_production, 75_LVBus1261624_consumption, 75_LVBus1261624_production, 75_LVBus1261625_production, 75_LVBus1261626_production, 75_LVBus1261627_production, 75_LVBus1261628_consumption, 75_LVBus1261628_production, 75_LVBus1261629_production, 75_LVBus1261630_production, 75_LVBus1261631_consumption, 75_LVBus1261631_production, 75_LVBus1261633_production, 75_LVBus1261634_production, 75_LVBus1261635_production, 75_LVBus1261637_production, 75_LVBus1261638_production, 75_LVBus1261640_production, 75_LVBus1261641_production, 75_LVBus1261642_production, 75_LVBus1261644_production, 75_LVBus1261645_production, 75_LVBus1261646_production, 75_LVBus1261647_production, 75_LVBus1261648_production, 75_LVBus1261649_consumption, 75_LVBus1261649_production, 75_LVBus1261650_production, 75_LVBus1261651_production, 75_LVBus1261653_production, 75_LVBus1261654_production, 75_LVBus1261656_consumption, 75_LVBus1261656_production, 75_LVBus1261657_consumption, 75_LVBus1261657_production, 75_LVBus1261658_production, 75_LVBus1261659_production, 75_LVBus1261660_production, 75_LVBus1261661_production, 75_LVBus1261663_production, 75_LVBus1261664_production, 75_LVBus1261665_production, 75_LVBus1261666_production, 75_LVBus1261667_production, 75_LVBus1261668_production, 75_LVBus1261669_production, 75_LVBus1261670_production, 75_LVBus1261671_production, 75_LVBus1261672_production, 75_LVBus1261673_production, 75_LVBus1261675_production, 75_LVBus1261676_production, 75_LVBus1261677_production, 75_LVBus1261679_production, 75_LVBus1261680_production, 75_LVBus1261681_production, 75_LVBus1261683_production, 75_LVBus1261685_production, 75_LVBus1261686_production, 75_LVBus1261687_production, 75_LVBus1261689_production, 75_LVBus1261690_production, 75_LVBus1261691_production, 75_LVBus1261692_production, 75_LVBus1261693_production, 75_LVBus1261695_consumption, 75_LVBus1261695_production, 75_LVBus1261696_production, 75_LVBus1261698_production, 75_LVBus1261700_production, 75_LVBus1261701_consumption, 75_LVBus1261701_production, 75_LVBus1261702_production, 75_LVBus1261703_production, 75_LVBus1261705_consumption, 75_LVBus1261705_production, 75_LVBus1261706_production, 75_LVBus1261707_production, 75_LVBus1261709_consumption, 75_LVBus1261709_production, 75_LVBus1261710_production, 75_LVBus1261711_production, 75_LVBus1261712_production, 75_LVBus1261714_production, 75_LVBus1261716_production, 75_LVBus1261717_production, 75_LVBus1261718_production, 75_LVBus1261720_consumption, 75_LVBus1261720_production, 75_LVBus1261722_production, 75_LVBus1261724_consumption, 75_LVBus1261724_production, 75_LVBus1261726_production, 75_LVBus1261727_production, 75_LVBus1261728_production, 75_LVBus1261729_production, 75_LVBus1261730_consumption, 75_LVBus1261730_production, 75_LVBus1261731_production, 75_LVBus1261732_consumption, 75_LVBus1261732_production, 75_LVBus1261734_production, 75_LVBus1261735_production, 75_LVBus1261736_production, 75_LVBus1261737_production, 75_LVBus1261738_production, 75_LVBus1261739_production, 75_LVBus1261740_production, 75_LVBus1261741_production, 75_LVBus1261742_production, 75_LVBus1261744_consumption, 75_LVBus1261744_production, 75_LVBus1261745_production, 75_LVBus1261746_production, 75_LVBus1261747_production, 75_LVBus1261748_production, 75_LVBus1261750_production, 75_LVBus1261752_consumption, 75_LVBus1261752_production, 75_LVBus1261753_production, 75_LVBus1261755_production, 75_LVBus1261756_consumption, 75_LVBus1261756_production, 75_LVBus1261757_consumption, 75_LVBus1261757_production, 75_LVBus1261759_consumption, 75_LVBus1261759_production, 75_LVBus1261760_consumption, 75_LVBus1261760_production, 75_LVBus1261761_production, 75_LVBus1261763_consumption, 75_LVBus1261763_production, 75_LVBus1261764_consumption, 75_LVBus1261764_production, 75_LVBus1261767_production, 75_LVBus1261768_production, 75_LVBus1261769_production, 75_LVBus1261770_production, 75_LVBus1261771_production, 75_LVBus1261772_production, 75_LVBus1261774_production, 75_LVBus1261775_production, 75_LVBus1261777_production, 75_LVBus1261778_production, 75_LVBus1261780_production, 75_LVBus1261781_production, 75_LVBus1261782_production, 75_LVBus1261783_production, 75_LVBus1261784_production, 75_LVBus1261785_consumption, 75_LVBus1261785_production, 75_LVBus1261787_production, 75_LVBus1261788_production, 75_LVBus1261789_production, 75_LVBus1261790_consumption, 75_LVBus1261790_production, 75_LVBus1261791_production, 75_LVBus1261792_production, 75_LVBus1261793_production, 75_LVBus1261794_production, 75_LVBus1261795_production, 75_LVBus1261797_production, 75_LVBus1261798_consumption, 75_LVBus1261798_production, 75_LVBus1261799_production, 75_LVBus1261800_production, 75_LVBus1261801_production, 75_LVBus1261802_production, 75_LVBus1261803_production, 75_LVBus1261804_production, 75_LVBus1261805_production, 75_LVBus1261806_production, 75_LVBus1261808_production, 75_LVBus1261809_production, 75_LVBus1261810_production, 75_LVBus1261811_production, 75_LVBus1261812_production, 75_LVBus1261813_production, 75_LVBus1261815_production, 75_LVBus1261816_production, 75_LVBus1261817_production, 75_LVBus1261818_production, 75_LVBus1261819_production, 75_LVBus1261820_production, 75_LVBus1261821_production, 75_LVBus1261823_production, 75_LVBus1261824_consumption, 75_LVBus1261824_production, 75_LVBus1261825_production, 75_LVBus1261826_production, 75_LVBus1261827_production, 75_LVBus1261828_production, 75_LVBus1261829_production, 75_LVBus1261830_production, 75_LVBus1261831_production, 75_LVBus1261832_production, 75_LVBus1261833_production, 75_LVBus1261834_production, 75_LVBus1261836_production, 75_LVBus1261837_consumption, 75_LVBus1261837_production, 75_LVBus1261838_production, 75_LVBus1261839_production, 75_LVBus1261841_consumption, 75_LVBus1261841_production, 75_LVBus1261842_production, 75_LVBus1261844_production, 75_LVBus1261846_consumption, 75_LVBus1261846_production, 75_LVBus1261847_production, 75_LVBus1261849_production, 75_LVBus1261850_production, 75_LVBus1261851_production, 75_LVBus1261852_production, 75_LVBus1261853_production, 75_LVBus1261854_production, 75_LVBus1261855_production, 75_LVBus1261856_production, 75_LVBus1261857_consumption, 75_LVBus1261857_production, 75_LVBus1261859_production, 75_LVBus1261860_production, 75_LVBus1261861_production, 75_LVBus1261862_production, 75_LVBus1261863_production, 75_LVBus1261864_consumption, 75_LVBus1261864_production, 75_LVBus1261865_production, 75_LVBus1261867_production, 75_LVBus1261868_production, 75_LVBus1261869_production, 75_LVBus1261870_production, 75_LVBus1261871_production, 75_LVBus1261872_consumption, 75_LVBus1261872_production, 75_LVBus1261873_consumption, 75_LVBus1261873_production, 75_LVBus1938199_production, 75_LVBus1938200_production, 75_LVBus1938201_production, 75_LVBus1938202_production, 75_LVBus2009451_production, 75_LVBus2009767_production, 75_LVBus2011918_production, 75_LVBus2011919_consumption, 75_LVBus2011919_production, 75_MVLV011947_production.

## 9. Data Quality Summary

**Total findings:** 359 (0 errors, 5 warnings, 354 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  539 of 920 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.49 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  540 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261488_consumption`  
  Load '75_LVBus1261488_consumption' has phase imbalance of 226.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261680_consumption`  
  Load '75_LVBus1261680_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261817_consumption`  
  Load '75_LVBus1261817_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261355_consumption`  
  Load '75_LVBus1261355_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261797_consumption`  
  Load '75_LVBus1261797_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261472_consumption`  
  Load '75_LVBus1261472_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261615_consumption`  
  Load '75_LVBus1261615_consumption' has phase imbalance of 256.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261602_consumption`  
  Load '75_LVBus1261602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261642_consumption`  
  Load '75_LVBus1261642_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261839_consumption`  
  Load '75_LVBus1261839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261738_consumption`  
  Load '75_LVBus1261738_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261600_consumption`  
  Load '75_LVBus1261600_consumption' has phase imbalance of 296.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261653_consumption`  
  Load '75_LVBus1261653_consumption' has phase imbalance of 289.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261860_consumption`  
  Load '75_LVBus1261860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261693_consumption`  
  Load '75_LVBus1261693_consumption' has phase imbalance of 38.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261412_consumption`  
  Load '75_LVBus1261412_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261606_consumption`  
  Load '75_LVBus1261606_consumption' has phase imbalance of 227.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261793_consumption`  
  Load '75_LVBus1261793_consumption' has phase imbalance of 60.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261690_consumption`  
  Load '75_LVBus1261690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261525_consumption`  
  Load '75_LVBus1261525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261629_consumption`  
  Load '75_LVBus1261629_consumption' has phase imbalance of 92.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261370_consumption`  
  Load '75_LVBus1261370_consumption' has phase imbalance of 221.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261716_consumption`  
  Load '75_LVBus1261716_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2011918_consumption`  
  Load '75_LVBus2011918_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261673_consumption`  
  Load '75_LVBus1261673_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261338_consumption`  
  Load '75_LVBus1261338_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261868_consumption`  
  Load '75_LVBus1261868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261613_consumption`  
  Load '75_LVBus1261613_consumption' has phase imbalance of 291.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261795_consumption`  
  Load '75_LVBus1261795_consumption' has phase imbalance of 54.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261607_consumption`  
  Load '75_LVBus1261607_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261828_consumption`  
  Load '75_LVBus1261828_consumption' has phase imbalance of 61.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261373_consumption`  
  Load '75_LVBus1261373_consumption' has phase imbalance of 40.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261644_consumption`  
  Load '75_LVBus1261644_consumption' has phase imbalance of 255.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261454_consumption`  
  Load '75_LVBus1261454_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261740_consumption`  
  Load '75_LVBus1261740_consumption' has phase imbalance of 265.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2009451_consumption`  
  Load '75_LVBus2009451_consumption' has phase imbalance of 123.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261729_consumption`  
  Load '75_LVBus1261729_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261805_consumption`  
  Load '75_LVBus1261805_consumption' has phase imbalance of 173.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1938201_consumption`  
  Load '75_LVBus1938201_consumption' has phase imbalance of 165.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261437_consumption`  
  Load '75_LVBus1261437_consumption' has phase imbalance of 20.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261612_consumption`  
  Load '75_LVBus1261612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261611_consumption`  
  Load '75_LVBus1261611_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261524_consumption`  
  Load '75_LVBus1261524_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261844_consumption`  
  Load '75_LVBus1261844_consumption' has phase imbalance of 92.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261382_consumption`  
  Load '75_LVBus1261382_consumption' has phase imbalance of 201.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261369_consumption`  
  Load '75_LVBus1261369_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261460_consumption`  
  Load '75_LVBus1261460_consumption' has phase imbalance of 46.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261855_consumption`  
  Load '75_LVBus1261855_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261377_consumption`  
  Load '75_LVBus1261377_consumption' has phase imbalance of 265.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261444_consumption`  
  Load '75_LVBus1261444_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261596_consumption`  
  Load '75_LVBus1261596_consumption' has phase imbalance of 214.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261741_consumption`  
  Load '75_LVBus1261741_consumption' has phase imbalance of 212.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261420_consumption`  
  Load '75_LVBus1261420_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261422_consumption`  
  Load '75_LVBus1261422_consumption' has phase imbalance of 63.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261806_consumption`  
  Load '75_LVBus1261806_consumption' has phase imbalance of 163.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261859_consumption`  
  Load '75_LVBus1261859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261826_consumption`  
  Load '75_LVBus1261826_consumption' has phase imbalance of 122.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261557_consumption`  
  Load '75_LVBus1261557_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261396_consumption`  
  Load '75_LVBus1261396_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261562_consumption`  
  Load '75_LVBus1261562_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261480_consumption`  
  Load '75_LVBus1261480_consumption' has phase imbalance of 85.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261461_consumption`  
  Load '75_LVBus1261461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261780_consumption`  
  Load '75_LVBus1261780_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261707_consumption`  
  Load '75_LVBus1261707_consumption' has phase imbalance of 111.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261401_consumption`  
  Load '75_LVBus1261401_consumption' has phase imbalance of 48.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261648_consumption`  
  Load '75_LVBus1261648_consumption' has phase imbalance of 119.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261486_consumption`  
  Load '75_LVBus1261486_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261469_consumption`  
  Load '75_LVBus1261469_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261523_consumption`  
  Load '75_LVBus1261523_consumption' has phase imbalance of 65.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261516_consumption`  
  Load '75_LVBus1261516_consumption' has phase imbalance of 117.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261487_consumption`  
  Load '75_LVBus1261487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261847_consumption`  
  Load '75_LVBus1261847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261411_consumption`  
  Load '75_LVBus1261411_consumption' has phase imbalance of 130.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261587_consumption`  
  Load '75_LVBus1261587_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261778_consumption`  
  Load '75_LVBus1261778_consumption' has phase imbalance of 128.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261650_consumption`  
  Load '75_LVBus1261650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261576_consumption`  
  Load '75_LVBus1261576_consumption' has phase imbalance of 162.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261446_consumption`  
  Load '75_LVBus1261446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261718_consumption`  
  Load '75_LVBus1261718_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261491_consumption`  
  Load '75_LVBus1261491_consumption' has phase imbalance of 206.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261510_consumption`  
  Load '75_LVBus1261510_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261683_consumption`  
  Load '75_LVBus1261683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261625_consumption`  
  Load '75_LVBus1261625_consumption' has phase imbalance of 57.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261402_consumption`  
  Load '75_LVBus1261402_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261869_consumption`  
  Load '75_LVBus1261869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261829_consumption`  
  Load '75_LVBus1261829_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261706_consumption`  
  Load '75_LVBus1261706_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261409_consumption`  
  Load '75_LVBus1261409_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261609_consumption`  
  Load '75_LVBus1261609_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261368_consumption`  
  Load '75_LVBus1261368_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261802_consumption`  
  Load '75_LVBus1261802_consumption' has phase imbalance of 224.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261614_consumption`  
  Load '75_LVBus1261614_consumption' has phase imbalance of 187.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261342_consumption`  
  Load '75_LVBus1261342_consumption' has phase imbalance of 155.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261457_consumption`  
  Load '75_LVBus1261457_consumption' has phase imbalance of 114.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261800_consumption`  
  Load '75_LVBus1261800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261622_consumption`  
  Load '75_LVBus1261622_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261476_consumption`  
  Load '75_LVBus1261476_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261867_consumption`  
  Load '75_LVBus1261867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261352_consumption`  
  Load '75_LVBus1261352_consumption' has phase imbalance of 90.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261731_consumption`  
  Load '75_LVBus1261731_consumption' has phase imbalance of 167.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261783_consumption`  
  Load '75_LVBus1261783_consumption' has phase imbalance of 22.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261808_consumption`  
  Load '75_LVBus1261808_consumption' has phase imbalance of 98.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1938200_consumption`  
  Load '75_LVBus1938200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261423_consumption`  
  Load '75_LVBus1261423_consumption' has phase imbalance of 180.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261592_consumption`  
  Load '75_LVBus1261592_consumption' has phase imbalance of 41.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261458_consumption`  
  Load '75_LVBus1261458_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261499_consumption`  
  Load '75_LVBus1261499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261442_consumption`  
  Load '75_LVBus1261442_consumption' has phase imbalance of 40.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261391_consumption`  
  Load '75_LVBus1261391_consumption' has phase imbalance of 143.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261558_consumption`  
  Load '75_LVBus1261558_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261347_consumption`  
  Load '75_LVBus1261347_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261633_consumption`  
  Load '75_LVBus1261633_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261418_consumption`  
  Load '75_LVBus1261418_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261521_consumption`  
  Load '75_LVBus1261521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261834_consumption`  
  Load '75_LVBus1261834_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261703_consumption`  
  Load '75_LVBus1261703_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261668_consumption`  
  Load '75_LVBus1261668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261616_consumption`  
  Load '75_LVBus1261616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261383_consumption`  
  Load '75_LVBus1261383_consumption' has phase imbalance of 96.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261852_consumption`  
  Load '75_LVBus1261852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261408_consumption`  
  Load '75_LVBus1261408_consumption' has phase imbalance of 261.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261863_consumption`  
  Load '75_LVBus1261863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261630_consumption`  
  Load '75_LVBus1261630_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261452_consumption`  
  Load '75_LVBus1261452_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261372_consumption`  
  Load '75_LVBus1261372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261727_consumption`  
  Load '75_LVBus1261727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261598_consumption`  
  Load '75_LVBus1261598_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261435_consumption`  
  Load '75_LVBus1261435_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261588_consumption`  
  Load '75_LVBus1261588_consumption' has phase imbalance of 215.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261434_consumption`  
  Load '75_LVBus1261434_consumption' has phase imbalance of 234.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261667_consumption`  
  Load '75_LVBus1261667_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261349_consumption`  
  Load '75_LVBus1261349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261626_consumption`  
  Load '75_LVBus1261626_consumption' has phase imbalance of 280.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261470_consumption`  
  Load '75_LVBus1261470_consumption' has phase imbalance of 37.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261597_consumption`  
  Load '75_LVBus1261597_consumption' has phase imbalance of 158.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261676_consumption`  
  Load '75_LVBus1261676_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261641_consumption`  
  Load '75_LVBus1261641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261438_consumption`  
  Load '75_LVBus1261438_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261583_consumption`  
  Load '75_LVBus1261583_consumption' has phase imbalance of 180.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261556_consumption`  
  Load '75_LVBus1261556_consumption' has phase imbalance of 132.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261669_consumption`  
  Load '75_LVBus1261669_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261564_consumption`  
  Load '75_LVBus1261564_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261344_consumption`  
  Load '75_LVBus1261344_consumption' has phase imbalance of 208.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261471_consumption`  
  Load '75_LVBus1261471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261569_consumption`  
  Load '75_LVBus1261569_consumption' has phase imbalance of 78.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261543_consumption`  
  Load '75_LVBus1261543_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261696_consumption`  
  Load '75_LVBus1261696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261579_consumption`  
  Load '75_LVBus1261579_consumption' has phase imbalance of 148.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261475_consumption`  
  Load '75_LVBus1261475_consumption' has phase imbalance of 41.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261865_consumption`  
  Load '75_LVBus1261865_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261357_consumption`  
  Load '75_LVBus1261357_consumption' has phase imbalance of 165.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261658_consumption`  
  Load '75_LVBus1261658_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261535_consumption`  
  Load '75_LVBus1261535_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261520_consumption`  
  Load '75_LVBus1261520_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261634_consumption`  
  Load '75_LVBus1261634_consumption' has phase imbalance of 172.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261832_consumption`  
  Load '75_LVBus1261832_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261620_consumption`  
  Load '75_LVBus1261620_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261455_consumption`  
  Load '75_LVBus1261455_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261830_consumption`  
  Load '75_LVBus1261830_consumption' has phase imbalance of 131.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261726_consumption`  
  Load '75_LVBus1261726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261734_consumption`  
  Load '75_LVBus1261734_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261358_consumption`  
  Load '75_LVBus1261358_consumption' has phase imbalance of 120.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261801_consumption`  
  Load '75_LVBus1261801_consumption' has phase imbalance of 278.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261477_consumption`  
  Load '75_LVBus1261477_consumption' has phase imbalance of 131.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261400_consumption`  
  Load '75_LVBus1261400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261447_consumption`  
  Load '75_LVBus1261447_consumption' has phase imbalance of 80.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261820_consumption`  
  Load '75_LVBus1261820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261792_consumption`  
  Load '75_LVBus1261792_consumption' has phase imbalance of 38.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261736_consumption`  
  Load '75_LVBus1261736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261593_consumption`  
  Load '75_LVBus1261593_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261761_consumption`  
  Load '75_LVBus1261761_consumption' has phase imbalance of 46.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261359_consumption`  
  Load '75_LVBus1261359_consumption' has phase imbalance of 53.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261698_consumption`  
  Load '75_LVBus1261698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261490_consumption`  
  Load '75_LVBus1261490_consumption' has phase imbalance of 276.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261665_consumption`  
  Load '75_LVBus1261665_consumption' has phase imbalance of 253.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261691_consumption`  
  Load '75_LVBus1261691_consumption' has phase imbalance of 256.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261666_consumption`  
  Load '75_LVBus1261666_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261479_consumption`  
  Load '75_LVBus1261479_consumption' has phase imbalance of 122.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261585_consumption`  
  Load '75_LVBus1261585_consumption' has phase imbalance of 139.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261812_consumption`  
  Load '75_LVBus1261812_consumption' has phase imbalance of 86.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261546_consumption`  
  Load '75_LVBus1261546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261854_consumption`  
  Load '75_LVBus1261854_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261419_consumption`  
  Load '75_LVBus1261419_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261789_consumption`  
  Load '75_LVBus1261789_consumption' has phase imbalance of 118.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261375_consumption`  
  Load '75_LVBus1261375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261511_consumption`  
  Load '75_LVBus1261511_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261514_consumption`  
  Load '75_LVBus1261514_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261771_consumption`  
  Load '75_LVBus1261771_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261387_consumption`  
  Load '75_LVBus1261387_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261664_consumption`  
  Load '75_LVBus1261664_consumption' has phase imbalance of 262.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261380_consumption`  
  Load '75_LVBus1261380_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261692_consumption`  
  Load '75_LVBus1261692_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261364_consumption`  
  Load '75_LVBus1261364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261550_consumption`  
  Load '75_LVBus1261550_consumption' has phase imbalance of 247.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261513_consumption`  
  Load '75_LVBus1261513_consumption' has phase imbalance of 226.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261532_consumption`  
  Load '75_LVBus1261532_consumption' has phase imbalance of 273.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261345_consumption`  
  Load '75_LVBus1261345_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261660_consumption`  
  Load '75_LVBus1261660_consumption' has phase imbalance of 247.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261485_consumption`  
  Load '75_LVBus1261485_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261536_consumption`  
  Load '75_LVBus1261536_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261677_consumption`  
  Load '75_LVBus1261677_consumption' has phase imbalance of 132.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261456_consumption`  
  Load '75_LVBus1261456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261813_consumption`  
  Load '75_LVBus1261813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261528_consumption`  
  Load '75_LVBus1261528_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261459_consumption`  
  Load '75_LVBus1261459_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261617_consumption`  
  Load '75_LVBus1261617_consumption' has phase imbalance of 217.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261570_consumption`  
  Load '75_LVBus1261570_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261428_consumption`  
  Load '75_LVBus1261428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261685_consumption`  
  Load '75_LVBus1261685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261742_consumption`  
  Load '75_LVBus1261742_consumption' has phase imbalance of 213.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261578_consumption`  
  Load '75_LVBus1261578_consumption' has phase imbalance of 85.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261575_consumption`  
  Load '75_LVBus1261575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261804_consumption`  
  Load '75_LVBus1261804_consumption' has phase imbalance of 127.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261407_consumption`  
  Load '75_LVBus1261407_consumption' has phase imbalance of 293.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261849_consumption`  
  Load '75_LVBus1261849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261782_consumption`  
  Load '75_LVBus1261782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261608_consumption`  
  Load '75_LVBus1261608_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261353_consumption`  
  Load '75_LVBus1261353_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261601_consumption`  
  Load '75_LVBus1261601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261811_consumption`  
  Load '75_LVBus1261811_consumption' has phase imbalance of 133.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261821_consumption`  
  Load '75_LVBus1261821_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261700_consumption`  
  Load '75_LVBus1261700_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261376_consumption`  
  Load '75_LVBus1261376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261605_consumption`  
  Load '75_LVBus1261605_consumption' has phase imbalance of 218.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261449_consumption`  
  Load '75_LVBus1261449_consumption' has phase imbalance of 27.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261366_consumption`  
  Load '75_LVBus1261366_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261679_consumption`  
  Load '75_LVBus1261679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261809_consumption`  
  Load '75_LVBus1261809_consumption' has phase imbalance of 134.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261541_consumption`  
  Load '75_LVBus1261541_consumption' has phase imbalance of 271.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261799_consumption`  
  Load '75_LVBus1261799_consumption' has phase imbalance of 28.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261687_consumption`  
  Load '75_LVBus1261687_consumption' has phase imbalance of 65.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261388_consumption`  
  Load '75_LVBus1261388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261356_consumption`  
  Load '75_LVBus1261356_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261717_consumption`  
  Load '75_LVBus1261717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261787_consumption`  
  Load '75_LVBus1261787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261712_consumption`  
  Load '75_LVBus1261712_consumption' has phase imbalance of 221.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261833_consumption`  
  Load '75_LVBus1261833_consumption' has phase imbalance of 40.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261573_consumption`  
  Load '75_LVBus1261573_consumption' has phase imbalance of 82.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261462_consumption`  
  Load '75_LVBus1261462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261492_consumption`  
  Load '75_LVBus1261492_consumption' has phase imbalance of 207.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261354_consumption`  
  Load '75_LVBus1261354_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261580_consumption`  
  Load '75_LVBus1261580_consumption' has phase imbalance of 168.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261590_consumption`  
  Load '75_LVBus1261590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261483_consumption`  
  Load '75_LVBus1261483_consumption' has phase imbalance of 255.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261722_consumption`  
  Load '75_LVBus1261722_consumption' has phase imbalance of 89.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261542_consumption`  
  Load '75_LVBus1261542_consumption' has phase imbalance of 143.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261638_consumption`  
  Load '75_LVBus1261638_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261728_consumption`  
  Load '75_LVBus1261728_consumption' has phase imbalance of 76.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261604_consumption`  
  Load '75_LVBus1261604_consumption' has phase imbalance of 281.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261336_consumption`  
  Load '75_LVBus1261336_consumption' has phase imbalance of 36.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261862_consumption`  
  Load '75_LVBus1261862_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261443_consumption`  
  Load '75_LVBus1261443_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261603_consumption`  
  Load '75_LVBus1261603_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261702_consumption`  
  Load '75_LVBus1261702_consumption' has phase imbalance of 276.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261403_consumption`  
  Load '75_LVBus1261403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261777_consumption`  
  Load '75_LVBus1261777_consumption' has phase imbalance of 221.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261856_consumption`  
  Load '75_LVBus1261856_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261416_consumption`  
  Load '75_LVBus1261416_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261853_consumption`  
  Load '75_LVBus1261853_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261647_consumption`  
  Load '75_LVBus1261647_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261465_consumption`  
  Load '75_LVBus1261465_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261671_consumption`  
  Load '75_LVBus1261671_consumption' has phase imbalance of 144.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261360_consumption`  
  Load '75_LVBus1261360_consumption' has phase imbalance of 110.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261772_consumption`  
  Load '75_LVBus1261772_consumption' has phase imbalance of 292.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261464_consumption`  
  Load '75_LVBus1261464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261675_consumption`  
  Load '75_LVBus1261675_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261861_consumption`  
  Load '75_LVBus1261861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261610_consumption`  
  Load '75_LVBus1261610_consumption' has phase imbalance of 284.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261747_consumption`  
  Load '75_LVBus1261747_consumption' has phase imbalance of 124.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261618_consumption`  
  Load '75_LVBus1261618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261512_consumption`  
  Load '75_LVBus1261512_consumption' has phase imbalance of 44.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261640_consumption`  
  Load '75_LVBus1261640_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261539_consumption`  
  Load '75_LVBus1261539_consumption' has phase imbalance of 231.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261635_consumption`  
  Load '75_LVBus1261635_consumption' has phase imbalance of 187.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261823_consumption`  
  Load '75_LVBus1261823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261710_consumption`  
  Load '75_LVBus1261710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261466_consumption`  
  Load '75_LVBus1261466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261522_consumption`  
  Load '75_LVBus1261522_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261413_consumption`  
  Load '75_LVBus1261413_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261645_consumption`  
  Load '75_LVBus1261645_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261851_consumption`  
  Load '75_LVBus1261851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261482_consumption`  
  Load '75_LVBus1261482_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261594_consumption`  
  Load '75_LVBus1261594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261827_consumption`  
  Load '75_LVBus1261827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261842_consumption`  
  Load '75_LVBus1261842_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261810_consumption`  
  Load '75_LVBus1261810_consumption' has phase imbalance of 23.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261567_consumption`  
  Load '75_LVBus1261567_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261538_consumption`  
  Load '75_LVBus1261538_consumption' has phase imbalance of 51.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261750_consumption`  
  Load '75_LVBus1261750_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261484_consumption`  
  Load '75_LVBus1261484_consumption' has phase imbalance of 275.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261748_consumption`  
  Load '75_LVBus1261748_consumption' has phase imbalance of 106.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261803_consumption`  
  Load '75_LVBus1261803_consumption' has phase imbalance of 138.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261637_consumption`  
  Load '75_LVBus1261637_consumption' has phase imbalance of 144.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261794_consumption`  
  Load '75_LVBus1261794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261436_consumption`  
  Load '75_LVBus1261436_consumption' has phase imbalance of 121.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261775_consumption`  
  Load '75_LVBus1261775_consumption' has phase imbalance of 63.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261654_consumption`  
  Load '75_LVBus1261654_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261448_consumption`  
  Load '75_LVBus1261448_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261739_consumption`  
  Load '75_LVBus1261739_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261767_consumption`  
  Load '75_LVBus1261767_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261831_consumption`  
  Load '75_LVBus1261831_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261711_consumption`  
  Load '75_LVBus1261711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261737_consumption`  
  Load '75_LVBus1261737_consumption' has phase imbalance of 214.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261584_consumption`  
  Load '75_LVBus1261584_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261389_consumption`  
  Load '75_LVBus1261389_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261545_consumption`  
  Load '75_LVBus1261545_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261746_consumption`  
  Load '75_LVBus1261746_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261781_consumption`  
  Load '75_LVBus1261781_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261818_consumption`  
  Load '75_LVBus1261818_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261651_consumption`  
  Load '75_LVBus1261651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261582_consumption`  
  Load '75_LVBus1261582_consumption' has phase imbalance of 227.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261619_consumption`  
  Load '75_LVBus1261619_consumption' has phase imbalance of 222.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261768_consumption`  
  Load '75_LVBus1261768_consumption' has phase imbalance of 281.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261819_consumption`  
  Load '75_LVBus1261819_consumption' has phase imbalance of 288.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261386_consumption`  
  Load '75_LVBus1261386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261672_consumption`  
  Load '75_LVBus1261672_consumption' has phase imbalance of 139.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261774_consumption`  
  Load '75_LVBus1261774_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261421_consumption`  
  Load '75_LVBus1261421_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261390_consumption`  
  Load '75_LVBus1261390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261659_consumption`  
  Load '75_LVBus1261659_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261663_consumption`  
  Load '75_LVBus1261663_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261788_consumption`  
  Load '75_LVBus1261788_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261745_consumption`  
  Load '75_LVBus1261745_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261374_consumption`  
  Load '75_LVBus1261374_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261836_consumption`  
  Load '75_LVBus1261836_consumption' has phase imbalance of 20.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261530_consumption`  
  Load '75_LVBus1261530_consumption' has phase imbalance of 98.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261425_consumption`  
  Load '75_LVBus1261425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261838_consumption`  
  Load '75_LVBus1261838_consumption' has phase imbalance of 71.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261424_consumption`  
  Load '75_LVBus1261424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261527_consumption`  
  Load '75_LVBus1261527_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261870_consumption`  
  Load '75_LVBus1261870_consumption' has phase imbalance of 268.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261661_consumption`  
  Load '75_LVBus1261661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261493_consumption`  
  Load '75_LVBus1261493_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261735_consumption`  
  Load '75_LVBus1261735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261871_consumption`  
  Load '75_LVBus1261871_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261670_consumption`  
  Load '75_LVBus1261670_consumption' has phase imbalance of 232.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261581_consumption`  
  Load '75_LVBus1261581_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1261646_consumption`  
  Load '75_LVBus1261646_consumption' has phase imbalance of 276.3%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 920 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_MTEND' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_LVBus1261640' (LV, 0.24 kV) has an electrical reach of 1.2 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  509 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  210 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1261338_consumption, 75_LVBus1261342_consumption, 75_LVBus1261345_consumption, 75_LVBus1261347_consumption, 75_LVBus1261349_consumption, 75_LVBus1261353_consumption, 75_LVBus1261354_consumption, 75_LVBus1261364_consumption, 75_LVBus1261366_consumption, 75_LVBus1261368_consumption, 75_LVBus1261369_consumption, 75_LVBus1261370_consumption, 75_LVBus1261372_consumption, 75_LVBus1261375_consumption, 75_LVBus1261376_consumption, 75_LVBus1261377_consumption, 75_LVBus1261380_consumption, 75_LVBus1261382_consumption, 75_LVBus1261386_consumption, 75_LVBus1261387_consumption, 75_LVBus1261388_consumption, 75_LVBus1261390_consumption, 75_LVBus1261396_consumption, 75_LVBus1261400_consumption, 75_LVBus1261403_consumption, 75_LVBus1261407_consumption, 75_LVBus1261408_consumption, 75_LVBus1261413_consumption, 75_LVBus1261416_consumption, 75_LVBus1261419_consumption, 75_LVBus1261421_consumption, 75_LVBus1261424_consumption, 75_LVBus1261425_consumption, 75_LVBus1261428_consumption, 75_LVBus1261438_consumption, 75_LVBus1261443_consumption, 75_LVBus1261446_consumption, 75_LVBus1261456_consumption, 75_LVBus1261459_consumption, 75_LVBus1261461_consumption, 75_LVBus1261462_consumption, 75_LVBus1261464_consumption, 75_LVBus1261466_consumption, 75_LVBus1261469_consumption, 75_LVBus1261471_consumption, 75_LVBus1261476_consumption, 75_LVBus1261482_consumption, 75_LVBus1261483_consumption, 75_LVBus1261484_consumption, 75_LVBus1261485_consumption, 75_LVBus1261486_consumption, 75_LVBus1261487_consumption, 75_LVBus1261488_consumption, 75_LVBus1261490_consumption, 75_LVBus1261491_consumption, 75_LVBus1261492_consumption, 75_LVBus1261499_consumption, 75_LVBus1261513_consumption, 75_LVBus1261514_consumption, 75_LVBus1261520_consumption, 75_LVBus1261521_consumption, 75_LVBus1261524_consumption, 75_LVBus1261525_consumption, 75_LVBus1261527_consumption, 75_LVBus1261528_consumption, 75_LVBus1261532_consumption, 75_LVBus1261535_consumption, 75_LVBus1261539_consumption, 75_LVBus1261541_consumption, 75_LVBus1261546_consumption, 75_LVBus1261562_consumption, 75_LVBus1261564_consumption, 75_LVBus1261570_consumption, 75_LVBus1261575_consumption, 75_LVBus1261580_consumption, 75_LVBus1261581_consumption, 75_LVBus1261582_consumption, 75_LVBus1261584_consumption, 75_LVBus1261587_consumption, 75_LVBus1261588_consumption, 75_LVBus1261590_consumption, 75_LVBus1261593_consumption, 75_LVBus1261594_consumption, 75_LVBus1261596_consumption, 75_LVBus1261598_consumption, 75_LVBus1261600_consumption, 75_LVBus1261601_consumption, 75_LVBus1261602_consumption, 75_LVBus1261603_consumption, 75_LVBus1261604_consumption, 75_LVBus1261605_consumption, 75_LVBus1261606_consumption, 75_LVBus1261607_consumption, 75_LVBus1261608_consumption, 75_LVBus1261609_consumption, 75_LVBus1261610_consumption, 75_LVBus1261612_consumption, 75_LVBus1261613_consumption, 75_LVBus1261614_consumption, 75_LVBus1261615_consumption, 75_LVBus1261616_consumption, 75_LVBus1261617_consumption, 75_LVBus1261618_consumption, 75_LVBus1261619_consumption, 75_LVBus1261620_consumption, 75_LVBus1261626_consumption, 75_LVBus1261630_consumption, 75_LVBus1261633_consumption, 75_LVBus1261635_consumption, 75_LVBus1261640_consumption, 75_LVBus1261641_consumption, 75_LVBus1261642_consumption, 75_LVBus1261644_consumption, 75_LVBus1261645_consumption, 75_LVBus1261646_consumption, 75_LVBus1261650_consumption, 75_LVBus1261651_consumption, 75_LVBus1261653_consumption, 75_LVBus1261654_consumption, 75_LVBus1261658_consumption, 75_LVBus1261659_consumption, 75_LVBus1261660_consumption, 75_LVBus1261661_consumption, 75_LVBus1261663_consumption, 75_LVBus1261664_consumption, 75_LVBus1261665_consumption, 75_LVBus1261666_consumption, 75_LVBus1261668_consumption, 75_LVBus1261669_consumption, 75_LVBus1261670_consumption, 75_LVBus1261673_consumption, 75_LVBus1261675_consumption, 75_LVBus1261676_consumption, 75_LVBus1261679_consumption, 75_LVBus1261680_consumption, 75_LVBus1261683_consumption, 75_LVBus1261685_consumption, 75_LVBus1261690_consumption, 75_LVBus1261691_consumption, 75_LVBus1261692_consumption, 75_LVBus1261696_consumption, 75_LVBus1261698_consumption, 75_LVBus1261700_consumption, 75_LVBus1261702_consumption, 75_LVBus1261703_consumption, 75_LVBus1261710_consumption, 75_LVBus1261711_consumption, 75_LVBus1261712_consumption, 75_LVBus1261716_consumption, 75_LVBus1261717_consumption, 75_LVBus1261718_consumption, 75_LVBus1261726_consumption, 75_LVBus1261727_consumption, 75_LVBus1261729_consumption, 75_LVBus1261731_consumption, 75_LVBus1261734_consumption, 75_LVBus1261735_consumption, 75_LVBus1261736_consumption, 75_LVBus1261737_consumption, 75_LVBus1261738_consumption, 75_LVBus1261740_consumption, 75_LVBus1261742_consumption, 75_LVBus1261745_consumption, 75_LVBus1261746_consumption, 75_LVBus1261768_consumption, 75_LVBus1261771_consumption, 75_LVBus1261772_consumption, 75_LVBus1261774_consumption, 75_LVBus1261777_consumption, 75_LVBus1261781_consumption, 75_LVBus1261782_consumption, 75_LVBus1261787_consumption, 75_LVBus1261788_consumption, 75_LVBus1261794_consumption, 75_LVBus1261797_consumption, 75_LVBus1261800_consumption, 75_LVBus1261801_consumption, 75_LVBus1261805_consumption, 75_LVBus1261806_consumption, 75_LVBus1261813_consumption, 75_LVBus1261818_consumption, 75_LVBus1261819_consumption, 75_LVBus1261820_consumption, 75_LVBus1261821_consumption, 75_LVBus1261823_consumption, 75_LVBus1261827_consumption, 75_LVBus1261829_consumption, 75_LVBus1261832_consumption, 75_LVBus1261834_consumption, 75_LVBus1261839_consumption, 75_LVBus1261847_consumption, 75_LVBus1261849_consumption, 75_LVBus1261851_consumption, 75_LVBus1261852_consumption, 75_LVBus1261854_consumption, 75_LVBus1261855_consumption, 75_LVBus1261856_consumption, 75_LVBus1261859_consumption, 75_LVBus1261860_consumption, 75_LVBus1261861_consumption, 75_LVBus1261862_consumption, 75_LVBus1261863_consumption, 75_LVBus1261865_consumption, 75_LVBus1261867_consumption, 75_LVBus1261868_consumption, 75_LVBus1261869_consumption, 75_LVBus1261870_consumption, 75_LVBus1261871_consumption, 75_LVBus1938200_consumption, 75_LVBus1938201_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  460 group(s) of loads (920 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  540 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1261336_production, 75_LVBus1261337_consumption, 75_LVBus1261337_production, 75_LVBus1261338_production, 75_LVBus1261340_consumption, 75_LVBus1261340_production, 75_LVBus1261341_production, 75_LVBus1261342_production, 75_LVBus1261343_consumption, 75_LVBus1261343_production, 75_LVBus1261344_production, 75_LVBus1261345_production, 75_LVBus1261346_production, 75_LVBus1261347_production, 75_LVBus1261348_consumption, 75_LVBus1261348_production, 75_LVBus1261349_production, 75_LVBus1261351_consumption, 75_LVBus1261351_production, 75_LVBus1261352_production, 75_LVBus1261353_production, 75_LVBus1261354_production, 75_LVBus1261355_production, 75_LVBus1261356_production, 75_LVBus1261357_production, 75_LVBus1261358_production, 75_LVBus1261359_production, 75_LVBus1261360_production, 75_LVBus1261362_consumption, 75_LVBus1261362_production, 75_LVBus1261363_production, 75_LVBus1261364_production, 75_LVBus1261365_production, 75_LVBus1261366_production, 75_LVBus1261367_consumption, 75_LVBus1261367_production, 75_LVBus1261368_production, 75_LVBus1261369_production, 75_LVBus1261370_production, 75_LVBus1261371_consumption, 75_LVBus1261371_production, 75_LVBus1261372_production, 75_LVBus1261373_production, 75_LVBus1261374_production, 75_LVBus1261375_production, 75_LVBus1261376_production, 75_LVBus1261377_production, 75_LVBus1261379_consumption, 75_LVBus1261379_production, 75_LVBus1261380_production, 75_LVBus1261381_consumption, 75_LVBus1261381_production, 75_LVBus1261382_production, 75_LVBus1261383_production, 75_LVBus1261384_consumption, 75_LVBus1261384_production, 75_LVBus1261385_production, 75_LVBus1261386_production, 75_LVBus1261387_production, 75_LVBus1261388_production, 75_LVBus1261389_production, 75_LVBus1261390_production, 75_LVBus1261391_production, 75_LVBus1261392_consumption, 75_LVBus1261392_production, 75_LVBus1261393_production, 75_LVBus1261394_production, 75_LVBus1261395_production, 75_LVBus1261396_production, 75_LVBus1261398_consumption, 75_LVBus1261398_production, 75_LVBus1261399_consumption, 75_LVBus1261399_production, 75_LVBus1261400_production, 75_LVBus1261401_production, 75_LVBus1261402_production, 75_LVBus1261403_production, 75_LVBus1261405_production, 75_LVBus1261406_consumption, 75_LVBus1261406_production, 75_LVBus1261407_production, 75_LVBus1261408_production, 75_LVBus1261409_production, 75_LVBus1261410_consumption, 75_LVBus1261410_production, 75_LVBus1261411_production, 75_LVBus1261412_production, 75_LVBus1261413_production, 75_LVBus1261414_consumption, 75_LVBus1261414_production, 75_LVBus1261416_production, 75_LVBus1261417_consumption, 75_LVBus1261417_production, 75_LVBus1261418_production, 75_LVBus1261419_production, 75_LVBus1261420_production, 75_LVBus1261421_production, 75_LVBus1261422_production, 75_LVBus1261423_production, 75_LVBus1261424_production, 75_LVBus1261425_production, 75_LVBus1261427_production, 75_LVBus1261428_production, 75_LVBus1261430_consumption, 75_LVBus1261430_production, 75_LVBus1261432_consumption, 75_LVBus1261432_production, 75_LVBus1261433_consumption, 75_LVBus1261433_production, 75_LVBus1261434_production, 75_LVBus1261435_production, 75_LVBus1261436_production, 75_LVBus1261437_production, 75_LVBus1261438_production, 75_LVBus1261439_consumption, 75_LVBus1261439_production, 75_LVBus1261440_consumption, 75_LVBus1261440_production, 75_LVBus1261441_consumption, 75_LVBus1261441_production, 75_LVBus1261442_production, 75_LVBus1261443_production, 75_LVBus1261444_production, 75_LVBus1261445_consumption, 75_LVBus1261445_production, 75_LVBus1261446_production, 75_LVBus1261447_production, 75_LVBus1261448_production, 75_LVBus1261449_production, 75_LVBus1261450_production, 75_LVBus1261452_production, 75_LVBus1261454_production, 75_LVBus1261455_production, 75_LVBus1261456_production, 75_LVBus1261457_production, 75_LVBus1261458_production, 75_LVBus1261459_production, 75_LVBus1261460_production, 75_LVBus1261461_production, 75_LVBus1261462_production, 75_LVBus1261464_production, 75_LVBus1261465_production, 75_LVBus1261466_production, 75_LVBus1261468_consumption, 75_LVBus1261468_production, 75_LVBus1261469_production, 75_LVBus1261470_production, 75_LVBus1261471_production, 75_LVBus1261472_production, 75_LVBus1261474_consumption, 75_LVBus1261474_production, 75_LVBus1261475_production, 75_LVBus1261476_production, 75_LVBus1261477_production, 75_LVBus1261478_consumption, 75_LVBus1261478_production, 75_LVBus1261479_production, 75_LVBus1261480_production, 75_LVBus1261482_production, 75_LVBus1261483_production, 75_LVBus1261484_production, 75_LVBus1261485_production, 75_LVBus1261486_production, 75_LVBus1261487_production, 75_LVBus1261488_production, 75_LVBus1261489_consumption, 75_LVBus1261489_production, 75_LVBus1261490_production, 75_LVBus1261491_production, 75_LVBus1261492_production, 75_LVBus1261493_production, 75_LVBus1261495_consumption, 75_LVBus1261495_production, 75_LVBus1261497_consumption, 75_LVBus1261497_production, 75_LVBus1261498_consumption, 75_LVBus1261498_production, 75_LVBus1261499_production, 75_LVBus1261501_consumption, 75_LVBus1261501_production, 75_LVBus1261502_consumption, 75_LVBus1261502_production, 75_LVBus1261503_consumption, 75_LVBus1261503_production, 75_LVBus1261505_consumption, 75_LVBus1261505_production, 75_LVBus1261507_consumption, 75_LVBus1261507_production, 75_LVBus1261508_consumption, 75_LVBus1261508_production, 75_LVBus1261510_production, 75_LVBus1261511_production, 75_LVBus1261512_production, 75_LVBus1261513_production, 75_LVBus1261514_production, 75_LVBus1261516_production, 75_LVBus1261517_production, 75_LVBus1261518_consumption, 75_LVBus1261518_production, 75_LVBus1261520_production, 75_LVBus1261521_production, 75_LVBus1261522_production, 75_LVBus1261523_production, 75_LVBus1261524_production, 75_LVBus1261525_production, 75_LVBus1261526_production, 75_LVBus1261527_production, 75_LVBus1261528_production, 75_LVBus1261530_production, 75_LVBus1261532_production, 75_LVBus1261533_consumption, 75_LVBus1261533_production, 75_LVBus1261534_production, 75_LVBus1261535_production, 75_LVBus1261536_production, 75_LVBus1261538_production, 75_LVBus1261539_production, 75_LVBus1261541_production, 75_LVBus1261542_production, 75_LVBus1261543_production, 75_LVBus1261545_production, 75_LVBus1261546_production, 75_LVBus1261547_production, 75_LVBus1261548_production, 75_LVBus1261550_production, 75_LVBus1261551_consumption, 75_LVBus1261551_production, 75_LVBus1261552_production, 75_LVBus1261554_production, 75_LVBus1261556_production, 75_LVBus1261557_production, 75_LVBus1261558_production, 75_LVBus1261559_production, 75_LVBus1261561_consumption, 75_LVBus1261561_production, 75_LVBus1261562_production, 75_LVBus1261563_consumption, 75_LVBus1261563_production, 75_LVBus1261564_production, 75_LVBus1261566_consumption, 75_LVBus1261566_production, 75_LVBus1261567_production, 75_LVBus1261569_production, 75_LVBus1261570_production, 75_LVBus1261572_consumption, 75_LVBus1261572_production, 75_LVBus1261573_production, 75_LVBus1261574_production, 75_LVBus1261575_production, 75_LVBus1261576_production, 75_LVBus1261578_production, 75_LVBus1261579_production, 75_LVBus1261580_production, 75_LVBus1261581_production, 75_LVBus1261582_production, 75_LVBus1261583_production, 75_LVBus1261584_production, 75_LVBus1261585_production, 75_LVBus1261587_production, 75_LVBus1261588_production, 75_LVBus1261589_production, 75_LVBus1261590_production, 75_LVBus1261591_production, 75_LVBus1261592_production, 75_LVBus1261593_production, 75_LVBus1261594_production, 75_LVBus1261595_production, 75_LVBus1261596_production, 75_LVBus1261597_production, 75_LVBus1261598_production, 75_LVBus1261600_production, 75_LVBus1261601_production, 75_LVBus1261602_production, 75_LVBus1261603_production, 75_LVBus1261604_production, 75_LVBus1261605_production, 75_LVBus1261606_production, 75_LVBus1261607_production, 75_LVBus1261608_production, 75_LVBus1261609_production, 75_LVBus1261610_production, 75_LVBus1261611_production, 75_LVBus1261612_production, 75_LVBus1261613_production, 75_LVBus1261614_production, 75_LVBus1261615_production, 75_LVBus1261616_production, 75_LVBus1261617_production, 75_LVBus1261618_production, 75_LVBus1261619_production, 75_LVBus1261620_production, 75_LVBus1261622_production, 75_LVBus1261623_consumption, 75_LVBus1261623_production, 75_LVBus1261624_consumption, 75_LVBus1261624_production, 75_LVBus1261625_production, 75_LVBus1261626_production, 75_LVBus1261627_production, 75_LVBus1261628_consumption, 75_LVBus1261628_production, 75_LVBus1261629_production, 75_LVBus1261630_production, 75_LVBus1261631_consumption, 75_LVBus1261631_production, 75_LVBus1261633_production, 75_LVBus1261634_production, 75_LVBus1261635_production, 75_LVBus1261637_production, 75_LVBus1261638_production, 75_LVBus1261640_production, 75_LVBus1261641_production, 75_LVBus1261642_production, 75_LVBus1261644_production, 75_LVBus1261645_production, 75_LVBus1261646_production, 75_LVBus1261647_production, 75_LVBus1261648_production, 75_LVBus1261649_consumption, 75_LVBus1261649_production, 75_LVBus1261650_production, 75_LVBus1261651_production, 75_LVBus1261653_production, 75_LVBus1261654_production, 75_LVBus1261656_consumption, 75_LVBus1261656_production, 75_LVBus1261657_consumption, 75_LVBus1261657_production, 75_LVBus1261658_production, 75_LVBus1261659_production, 75_LVBus1261660_production, 75_LVBus1261661_production, 75_LVBus1261663_production, 75_LVBus1261664_production, 75_LVBus1261665_production, 75_LVBus1261666_production, 75_LVBus1261667_production, 75_LVBus1261668_production, 75_LVBus1261669_production, 75_LVBus1261670_production, 75_LVBus1261671_production, 75_LVBus1261672_production, 75_LVBus1261673_production, 75_LVBus1261675_production, 75_LVBus1261676_production, 75_LVBus1261677_production, 75_LVBus1261679_production, 75_LVBus1261680_production, 75_LVBus1261681_production, 75_LVBus1261683_production, 75_LVBus1261685_production, 75_LVBus1261686_production, 75_LVBus1261687_production, 75_LVBus1261689_production, 75_LVBus1261690_production, 75_LVBus1261691_production, 75_LVBus1261692_production, 75_LVBus1261693_production, 75_LVBus1261695_consumption, 75_LVBus1261695_production, 75_LVBus1261696_production, 75_LVBus1261698_production, 75_LVBus1261700_production, 75_LVBus1261701_consumption, 75_LVBus1261701_production, 75_LVBus1261702_production, 75_LVBus1261703_production, 75_LVBus1261705_consumption, 75_LVBus1261705_production, 75_LVBus1261706_production, 75_LVBus1261707_production, 75_LVBus1261709_consumption, 75_LVBus1261709_production, 75_LVBus1261710_production, 75_LVBus1261711_production, 75_LVBus1261712_production, 75_LVBus1261714_production, 75_LVBus1261716_production, 75_LVBus1261717_production, 75_LVBus1261718_production, 75_LVBus1261720_consumption, 75_LVBus1261720_production, 75_LVBus1261722_production, 75_LVBus1261724_consumption, 75_LVBus1261724_production, 75_LVBus1261726_production, 75_LVBus1261727_production, 75_LVBus1261728_production, 75_LVBus1261729_production, 75_LVBus1261730_consumption, 75_LVBus1261730_production, 75_LVBus1261731_production, 75_LVBus1261732_consumption, 75_LVBus1261732_production, 75_LVBus1261734_production, 75_LVBus1261735_production, 75_LVBus1261736_production, 75_LVBus1261737_production, 75_LVBus1261738_production, 75_LVBus1261739_production, 75_LVBus1261740_production, 75_LVBus1261741_production, 75_LVBus1261742_production, 75_LVBus1261744_consumption, 75_LVBus1261744_production, 75_LVBus1261745_production, 75_LVBus1261746_production, 75_LVBus1261747_production, 75_LVBus1261748_production, 75_LVBus1261750_production, 75_LVBus1261752_consumption, 75_LVBus1261752_production, 75_LVBus1261753_production, 75_LVBus1261755_production, 75_LVBus1261756_consumption, 75_LVBus1261756_production, 75_LVBus1261757_consumption, 75_LVBus1261757_production, 75_LVBus1261759_consumption, 75_LVBus1261759_production, 75_LVBus1261760_consumption, 75_LVBus1261760_production, 75_LVBus1261761_production, 75_LVBus1261763_consumption, 75_LVBus1261763_production, 75_LVBus1261764_consumption, 75_LVBus1261764_production, 75_LVBus1261767_production, 75_LVBus1261768_production, 75_LVBus1261769_production, 75_LVBus1261770_production, 75_LVBus1261771_production, 75_LVBus1261772_production, 75_LVBus1261774_production, 75_LVBus1261775_production, 75_LVBus1261777_production, 75_LVBus1261778_production, 75_LVBus1261780_production, 75_LVBus1261781_production, 75_LVBus1261782_production, 75_LVBus1261783_production, 75_LVBus1261784_production, 75_LVBus1261785_consumption, 75_LVBus1261785_production, 75_LVBus1261787_production, 75_LVBus1261788_production, 75_LVBus1261789_production, 75_LVBus1261790_consumption, 75_LVBus1261790_production, 75_LVBus1261791_production, 75_LVBus1261792_production, 75_LVBus1261793_production, 75_LVBus1261794_production, 75_LVBus1261795_production, 75_LVBus1261797_production, 75_LVBus1261798_consumption, 75_LVBus1261798_production, 75_LVBus1261799_production, 75_LVBus1261800_production, 75_LVBus1261801_production, 75_LVBus1261802_production, 75_LVBus1261803_production, 75_LVBus1261804_production, 75_LVBus1261805_production, 75_LVBus1261806_production, 75_LVBus1261808_production, 75_LVBus1261809_production, 75_LVBus1261810_production, 75_LVBus1261811_production, 75_LVBus1261812_production, 75_LVBus1261813_production, 75_LVBus1261815_production, 75_LVBus1261816_production, 75_LVBus1261817_production, 75_LVBus1261818_production, 75_LVBus1261819_production, 75_LVBus1261820_production, 75_LVBus1261821_production, 75_LVBus1261823_production, 75_LVBus1261824_consumption, 75_LVBus1261824_production, 75_LVBus1261825_production, 75_LVBus1261826_production, 75_LVBus1261827_production, 75_LVBus1261828_production, 75_LVBus1261829_production, 75_LVBus1261830_production, 75_LVBus1261831_production, 75_LVBus1261832_production, 75_LVBus1261833_production, 75_LVBus1261834_production, 75_LVBus1261836_production, 75_LVBus1261837_consumption, 75_LVBus1261837_production, 75_LVBus1261838_production, 75_LVBus1261839_production, 75_LVBus1261841_consumption, 75_LVBus1261841_production, 75_LVBus1261842_production, 75_LVBus1261844_production, 75_LVBus1261846_consumption, 75_LVBus1261846_production, 75_LVBus1261847_production, 75_LVBus1261849_production, 75_LVBus1261850_production, 75_LVBus1261851_production, 75_LVBus1261852_production, 75_LVBus1261853_production, 75_LVBus1261854_production, 75_LVBus1261855_production, 75_LVBus1261856_production, 75_LVBus1261857_consumption, 75_LVBus1261857_production, 75_LVBus1261859_production, 75_LVBus1261860_production, 75_LVBus1261861_production, 75_LVBus1261862_production, 75_LVBus1261863_production, 75_LVBus1261864_consumption, 75_LVBus1261864_production, 75_LVBus1261865_production, 75_LVBus1261867_production, 75_LVBus1261868_production, 75_LVBus1261869_production, 75_LVBus1261870_production, 75_LVBus1261871_production, 75_LVBus1261872_consumption, 75_LVBus1261872_production, 75_LVBus1261873_consumption, 75_LVBus1261873_production, 75_LVBus1938199_production, 75_LVBus1938200_production, 75_LVBus1938201_production, 75_LVBus1938202_production, 75_LVBus2009451_production, 75_LVBus2009767_production, 75_LVBus2011918_production, 75_LVBus2011919_consumption, 75_LVBus2011919_production, 75_MVLV011947_production.

