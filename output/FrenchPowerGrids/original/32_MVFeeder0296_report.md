# BMOPF Network Summary: 32_MVFeeder0296

**Generated:** 2026-10-01 23:34:05  
**Findings:** 0 errors · 5 warnings · 171 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 22 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 320 |  |
| line | 297 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 522 | 2.674 MW, 802.2 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 22 |  |
| switch | 0 |  |
| transformer | 22 | Dyn11×22 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 44 | 43 | 14 | 0 |
| LV_236V | 236.0 V | 276 | 254 | 508 | 0 |

**Transformer transitions:**

- `32_MVLV27946_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV33586_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV19423_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV59078_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV29207_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV53017_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV13224_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV67058_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV24380_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV30364_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV10184_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV20120_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV15409_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV67350_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV49858_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV19422_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV07905_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV56936_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV63489_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV19462_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV46232_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV50805_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 11 |
| Degree-1 buses | 115 |
| Tree depth (max hops) | 34 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 320 | 1 | 319 | 0 | 0 | 0 |
| Tier LV_236V | 276 | 22 | 254 | 0 | 0 | 0 |
| Tier MV_11.8kV | 44 | 1 | 43 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 22; skipped invalid branches: 0.

Galvanic zones: 23; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_ARRAS | MV_11.8kV | 44 | 0 | 0 | 22 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1236 declared bus terminals; 1145 mapped line/closed-switch conductor edges; 91 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 277000.0 | 7.423 | 1566 |
| q_nom | 0.0 | 83200.0 | 7.423 | 1566 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.33 | 4490.0 | 2.56 | 297 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.699 | 22 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 331 of 522 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696941_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696896_consumption' has phase imbalance of 244.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696959_consumption' has phase imbalance of 284.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696999_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697098_consumption' has phase imbalance of 122.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696809_consumption' has phase imbalance of 31.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696953_consumption' has phase imbalance of 214.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697093_consumption' has phase imbalance of 57.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696859_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696875_consumption' has phase imbalance of 96.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696877_consumption' has phase imbalance of 30.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696923_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697001_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696886_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696802_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696813_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696978_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697007_consumption' has phase imbalance of 82.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696902_consumption' has phase imbalance of 74.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696996_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696891_consumption' has phase imbalance of 186.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696948_consumption' has phase imbalance of 96.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696835_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697041_consumption' has phase imbalance of 70.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696880_consumption' has phase imbalance of 122.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697057_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696981_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696940_consumption' has phase imbalance of 121.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696869_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696889_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696979_consumption' has phase imbalance of 142.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696878_consumption' has phase imbalance of 68.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696935_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696816_consumption' has phase imbalance of 99.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697068_consumption' has phase imbalance of 273.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696885_consumption' has phase imbalance of 57.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696924_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696899_consumption' has phase imbalance of 233.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696939_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697079_consumption' has phase imbalance of 163.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696976_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696977_consumption' has phase imbalance of 169.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696994_consumption' has phase imbalance of 133.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696950_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696898_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696968_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697080_consumption' has phase imbalance of 259.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696967_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696832_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697077_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697075_consumption' has phase imbalance of 233.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696934_consumption' has phase imbalance of 264.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696928_consumption' has phase imbalance of 196.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697005_consumption' has phase imbalance of 54.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696958_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697053_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696963_consumption' has phase imbalance of 190.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697004_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696964_consumption' has phase imbalance of 283.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696965_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697074_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696998_consumption' has phase imbalance of 199.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696966_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696932_consumption' has phase imbalance of 225.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696980_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696814_consumption' has phase imbalance of 277.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696874_consumption' has phase imbalance of 93.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697055_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697072_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696985_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696937_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696807_consumption' has phase imbalance of 39.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696938_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696990_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697056_consumption' has phase imbalance of 82.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696883_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696893_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696818_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696984_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697006_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696879_consumption' has phase imbalance of 64.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696866_consumption' has phase imbalance of 129.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697067_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696882_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696931_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696881_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696960_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696989_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697071_consumption' has phase imbalance of 146.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697045_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696817_consumption' has phase imbalance of 51.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696863_consumption' has phase imbalance of 91.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696949_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696870_consumption' has phase imbalance of 60.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696821_consumption' has phase imbalance of 255.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697054_consumption' has phase imbalance of 95.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696901_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697070_consumption' has phase imbalance of 254.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696971_consumption' has phase imbalance of 206.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696808_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696829_consumption' has phase imbalance of 278.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696933_consumption' has phase imbalance of 46.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus697073_consumption' has phase imbalance of 239.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696884_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus696862_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 522 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_ARRAS' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus696781' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus696838' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus697039' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus696793' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus697061' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.674 MW |
| Total load Q | 802.2 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV27946_Transformer | 693.0 kVA | 37.6% |
| 32_MVLV33586_Transformer | 275.0 kVA | 78.8% |
| 32_MVLV19423_Transformer | 176.0 kVA | 32.9% |
| 32_MVLV59078_Transformer | 110.0 kVA | 0.9% |
| 32_MVLV29207_Transformer | 176.0 kVA | 42.9% |
| 32_MVLV53017_Transformer | 176.0 kVA | 2.4% |
| 32_MVLV13224_Transformer | 110.0 kVA | 12.5% |
| 32_MVLV67058_Transformer | 440.0 kVA | 24.1% |
| 32_MVLV24380_Transformer | 176.0 kVA | 31.5% |
| 32_MVLV30364_Transformer | 693.0 kVA | 30.1% |
| 32_MVLV10184_Transformer | 176.0 kVA | 22.9% |
| 32_MVLV20120_Transformer | 110.0 kVA | 29.2% |
| 32_MVLV15409_Transformer | 110.0 kVA | 10.4% |
| 32_MVLV67350_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV49858_Transformer | 275.0 kVA | 46.7% |
| 32_MVLV19422_Transformer | 275.0 kVA | 38.2% |
| 32_MVLV07905_Transformer | 110.0 kVA | 26.0% |
| 32_MVLV56936_Transformer | 176.0 kVA | 65.0% |
| 32_MVLV63489_Transformer | 176.0 kVA | 63.2% |
| 32_MVLV19462_Transformer | 176.0 kVA | 30.6% |
| 32_MVLV46232_Transformer | 275.0 kVA | 45.3% |
| 32_MVLV50805_Transformer | 176.0 kVA | 0.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.67 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '32_ARRAS' (MV, 11.78 kV) has an electrical reach of 21.91 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus697039' (LV, 0.24 kV) has an electrical reach of 3.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus1128351' (LV, 0.24 kV) has an electrical reach of 16.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 320 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 320 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 22 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 44 |
| LV_236V | 4-wire | 276 / 276 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 276 |
| Neutral branches | 254 |
| Grounding points | 22 |
| Neutral sections | 22 |
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
| 11.78 kV | 44 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 23 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2570.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 276 / 44 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 332 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 332 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1128351_consumption, 32_LVBus1128351_production, 32_LVBus696774_consumption, 32_LVBus696774_production, 32_LVBus696776_production, 32_LVBus696777_consumption, 32_LVBus696777_production, 32_LVBus696778_production, 32_LVBus696781_consumption, 32_LVBus696781_production, 32_LVBus696782_production, 32_LVBus696784_consumption, 32_LVBus696784_production, 32_LVBus696785_production, 32_LVBus696787_consumption, 32_LVBus696787_production, 32_LVBus696788_production, 32_LVBus696790_production, 32_LVBus696791_production, 32_LVBus696793_consumption, 32_LVBus696793_production, 32_LVBus696795_consumption, 32_LVBus696795_production, 32_LVBus696797_production, 32_LVBus696799_consumption, 32_LVBus696799_production, 32_LVBus696801_production, 32_LVBus696802_production, 32_LVBus696805_production, 32_LVBus696806_production, 32_LVBus696807_production, 32_LVBus696808_production, 32_LVBus696809_production, 32_LVBus696810_consumption, 32_LVBus696810_production, 32_LVBus696811_production, 32_LVBus696812_production, 32_LVBus696813_production, 32_LVBus696814_production, 32_LVBus696816_production, 32_LVBus696817_production, 32_LVBus696818_production, 32_LVBus696819_production, 32_LVBus696820_consumption, 32_LVBus696820_production, 32_LVBus696821_production, 32_LVBus696823_production, 32_LVBus696824_production, 32_LVBus696826_consumption, 32_LVBus696826_production, 32_LVBus696827_consumption, 32_LVBus696827_production, 32_LVBus696828_consumption, 32_LVBus696828_production, 32_LVBus696829_production, 32_LVBus696830_consumption, 32_LVBus696830_production, 32_LVBus696831_production, 32_LVBus696832_production, 32_LVBus696833_consumption, 32_LVBus696833_production, 32_LVBus696834_consumption, 32_LVBus696834_production, 32_LVBus696835_production, 32_LVBus696836_production, 32_LVBus696838_consumption, 32_LVBus696838_production, 32_LVBus696839_consumption, 32_LVBus696839_production, 32_LVBus696840_consumption, 32_LVBus696840_production, 32_LVBus696842_consumption, 32_LVBus696842_production, 32_LVBus696843_consumption, 32_LVBus696843_production, 32_LVBus696844_production, 32_LVBus696846_production, 32_LVBus696848_production, 32_LVBus696850_production, 32_LVBus696852_consumption, 32_LVBus696852_production, 32_LVBus696853_consumption, 32_LVBus696853_production, 32_LVBus696855_consumption, 32_LVBus696855_production, 32_LVBus696857_consumption, 32_LVBus696857_production, 32_LVBus696858_consumption, 32_LVBus696858_production, 32_LVBus696859_production, 32_LVBus696860_production, 32_LVBus696862_production, 32_LVBus696863_production, 32_LVBus696866_production, 32_LVBus696867_production, 32_LVBus696869_production, 32_LVBus696870_production, 32_LVBus696871_consumption, 32_LVBus696871_production, 32_LVBus696872_production, 32_LVBus696873_production, 32_LVBus696874_production, 32_LVBus696875_production, 32_LVBus696877_production, 32_LVBus696878_production, 32_LVBus696879_production, 32_LVBus696880_production, 32_LVBus696881_production, 32_LVBus696882_production, 32_LVBus696883_production, 32_LVBus696884_production, 32_LVBus696885_production, 32_LVBus696886_production, 32_LVBus696888_production, 32_LVBus696889_production, 32_LVBus696890_production, 32_LVBus696891_production, 32_LVBus696892_production, 32_LVBus696893_production, 32_LVBus696895_consumption, 32_LVBus696895_production, 32_LVBus696896_production, 32_LVBus696897_production, 32_LVBus696898_production, 32_LVBus696899_production, 32_LVBus696900_consumption, 32_LVBus696900_production, 32_LVBus696901_production, 32_LVBus696902_production, 32_LVBus696904_production, 32_LVBus696906_production, 32_LVBus696908_production, 32_LVBus696910_production, 32_LVBus696911_consumption, 32_LVBus696911_production, 32_LVBus696913_production, 32_LVBus696915_consumption, 32_LVBus696915_production, 32_LVBus696917_production, 32_LVBus696919_production, 32_LVBus696921_production, 32_LVBus696923_production, 32_LVBus696924_production, 32_LVBus696925_production, 32_LVBus696926_production, 32_LVBus696927_production, 32_LVBus696928_production, 32_LVBus696929_production, 32_LVBus696930_production, 32_LVBus696931_production, 32_LVBus696932_production, 32_LVBus696933_production, 32_LVBus696934_production, 32_LVBus696935_production, 32_LVBus696937_production, 32_LVBus696938_production, 32_LVBus696939_production, 32_LVBus696940_production, 32_LVBus696941_production, 32_LVBus696943_production, 32_LVBus696945_production, 32_LVBus696946_production, 32_LVBus696947_production, 32_LVBus696948_production, 32_LVBus696949_production, 32_LVBus696950_production, 32_LVBus696951_consumption, 32_LVBus696951_production, 32_LVBus696952_production, 32_LVBus696953_production, 32_LVBus696957_consumption, 32_LVBus696957_production, 32_LVBus696958_production, 32_LVBus696959_production, 32_LVBus696960_production, 32_LVBus696962_consumption, 32_LVBus696962_production, 32_LVBus696963_production, 32_LVBus696964_production, 32_LVBus696965_production, 32_LVBus696966_production, 32_LVBus696967_production, 32_LVBus696968_production, 32_LVBus696969_production, 32_LVBus696971_production, 32_LVBus696973_production, 32_LVBus696974_consumption, 32_LVBus696974_production, 32_LVBus696975_production, 32_LVBus696976_production, 32_LVBus696977_production, 32_LVBus696978_production, 32_LVBus696979_production, 32_LVBus696980_production, 32_LVBus696981_production, 32_LVBus696983_production, 32_LVBus696984_production, 32_LVBus696985_production, 32_LVBus696986_production, 32_LVBus696987_production, 32_LVBus696988_consumption, 32_LVBus696988_production, 32_LVBus696989_production, 32_LVBus696990_production, 32_LVBus696991_production, 32_LVBus696993_production, 32_LVBus696994_production, 32_LVBus696995_production, 32_LVBus696996_production, 32_LVBus696998_production, 32_LVBus696999_production, 32_LVBus697000_production, 32_LVBus697001_production, 32_LVBus697002_production, 32_LVBus697003_production, 32_LVBus697004_production, 32_LVBus697005_production, 32_LVBus697006_production, 32_LVBus697007_production, 32_LVBus697009_production, 32_LVBus697013_consumption, 32_LVBus697013_production, 32_LVBus697015_consumption, 32_LVBus697015_production, 32_LVBus697016_consumption, 32_LVBus697016_production, 32_LVBus697017_consumption, 32_LVBus697017_production, 32_LVBus697019_consumption, 32_LVBus697019_production, 32_LVBus697020_consumption, 32_LVBus697020_production, 32_LVBus697021_consumption, 32_LVBus697021_production, 32_LVBus697023_consumption, 32_LVBus697023_production, 32_LVBus697024_consumption, 32_LVBus697024_production, 32_LVBus697025_consumption, 32_LVBus697025_production, 32_LVBus697027_consumption, 32_LVBus697027_production, 32_LVBus697029_consumption, 32_LVBus697029_production, 32_LVBus697031_consumption, 32_LVBus697031_production, 32_LVBus697033_consumption, 32_LVBus697033_production, 32_LVBus697035_consumption, 32_LVBus697035_production, 32_LVBus697037_consumption, 32_LVBus697037_production, 32_LVBus697039_production, 32_LVBus697041_production, 32_LVBus697042_production, 32_LVBus697043_production, 32_LVBus697044_consumption, 32_LVBus697044_production, 32_LVBus697045_production, 32_LVBus697046_consumption, 32_LVBus697046_production, 32_LVBus697047_production, 32_LVBus697048_production, 32_LVBus697049_consumption, 32_LVBus697049_production, 32_LVBus697050_production, 32_LVBus697051_production, 32_LVBus697052_production, 32_LVBus697053_production, 32_LVBus697054_production, 32_LVBus697055_production, 32_LVBus697056_production, 32_LVBus697057_production, 32_LVBus697061_production, 32_LVBus697063_production, 32_LVBus697064_consumption, 32_LVBus697064_production, 32_LVBus697065_production, 32_LVBus697066_production, 32_LVBus697067_production, 32_LVBus697068_production, 32_LVBus697069_consumption, 32_LVBus697069_production, 32_LVBus697070_production, 32_LVBus697071_production, 32_LVBus697072_production, 32_LVBus697073_production, 32_LVBus697074_production, 32_LVBus697075_production, 32_LVBus697076_production, 32_LVBus697077_production, 32_LVBus697078_production, 32_LVBus697079_production, 32_LVBus697080_production, 32_LVBus697081_production, 32_LVBus697082_consumption, 32_LVBus697082_production, 32_LVBus697084_consumption, 32_LVBus697084_production, 32_LVBus697086_consumption, 32_LVBus697086_production, 32_LVBus697087_production, 32_LVBus697088_production, 32_LVBus697090_consumption, 32_LVBus697090_production, 32_LVBus697091_production, 32_LVBus697092_consumption, 32_LVBus697092_production, 32_LVBus697093_production, 32_LVBus697095_production, 32_LVBus697097_consumption, 32_LVBus697097_production, 32_LVBus697098_production, 32_LVBus697099_production, 32_LVBus697101_production, 32_LVBus697103_consumption, 32_LVBus697103_production, 32_LVBus697105_production, 32_LVBus697109_consumption, 32_LVBus697109_production, 32_MVLV05364_consumption, 32_MVLV05364_production, 32_MVLV13372_consumption, 32_MVLV13372_production, 32_MVLV15315_consumption, 32_MVLV15315_production, 32_MVLV25093_consumption, 32_MVLV25093_production, 32_MVLV46624_production, 32_MVLV61153_production, 32_MVLV64448_consumption, 32_MVLV64448_production.

## 9. Data Quality Summary

**Total findings:** 176 (0 errors, 5 warnings, 171 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  331 of 522 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.67 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  332 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696892_consumption`  
  Load '32_LVBus696892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696941_consumption`  
  Load '32_LVBus696941_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696995_consumption`  
  Load '32_LVBus696995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696991_consumption`  
  Load '32_LVBus696991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696896_consumption`  
  Load '32_LVBus696896_consumption' has phase imbalance of 244.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696959_consumption`  
  Load '32_LVBus696959_consumption' has phase imbalance of 284.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696999_consumption`  
  Load '32_LVBus696999_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697098_consumption`  
  Load '32_LVBus697098_consumption' has phase imbalance of 122.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696809_consumption`  
  Load '32_LVBus696809_consumption' has phase imbalance of 31.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696953_consumption`  
  Load '32_LVBus696953_consumption' has phase imbalance of 214.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696872_consumption`  
  Load '32_LVBus696872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697093_consumption`  
  Load '32_LVBus697093_consumption' has phase imbalance of 57.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696888_consumption`  
  Load '32_LVBus696888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696859_consumption`  
  Load '32_LVBus696859_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696875_consumption`  
  Load '32_LVBus696875_consumption' has phase imbalance of 96.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696831_consumption`  
  Load '32_LVBus696831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696877_consumption`  
  Load '32_LVBus696877_consumption' has phase imbalance of 30.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697051_consumption`  
  Load '32_LVBus697051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696923_consumption`  
  Load '32_LVBus696923_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697001_consumption`  
  Load '32_LVBus697001_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696886_consumption`  
  Load '32_LVBus696886_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696945_consumption`  
  Load '32_LVBus696945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696802_consumption`  
  Load '32_LVBus696802_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696813_consumption`  
  Load '32_LVBus696813_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696873_consumption`  
  Load '32_LVBus696873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697063_consumption`  
  Load '32_LVBus697063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696978_consumption`  
  Load '32_LVBus696978_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697007_consumption`  
  Load '32_LVBus697007_consumption' has phase imbalance of 82.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696902_consumption`  
  Load '32_LVBus696902_consumption' has phase imbalance of 74.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696996_consumption`  
  Load '32_LVBus696996_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696891_consumption`  
  Load '32_LVBus696891_consumption' has phase imbalance of 186.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696948_consumption`  
  Load '32_LVBus696948_consumption' has phase imbalance of 96.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696835_consumption`  
  Load '32_LVBus696835_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697047_consumption`  
  Load '32_LVBus697047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697041_consumption`  
  Load '32_LVBus697041_consumption' has phase imbalance of 70.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697066_consumption`  
  Load '32_LVBus697066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697002_consumption`  
  Load '32_LVBus697002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696880_consumption`  
  Load '32_LVBus696880_consumption' has phase imbalance of 122.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697057_consumption`  
  Load '32_LVBus697057_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696981_consumption`  
  Load '32_LVBus696981_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696940_consumption`  
  Load '32_LVBus696940_consumption' has phase imbalance of 121.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697052_consumption`  
  Load '32_LVBus697052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696986_consumption`  
  Load '32_LVBus696986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696927_consumption`  
  Load '32_LVBus696927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696869_consumption`  
  Load '32_LVBus696869_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696889_consumption`  
  Load '32_LVBus696889_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696943_consumption`  
  Load '32_LVBus696943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696979_consumption`  
  Load '32_LVBus696979_consumption' has phase imbalance of 142.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696878_consumption`  
  Load '32_LVBus696878_consumption' has phase imbalance of 68.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696935_consumption`  
  Load '32_LVBus696935_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696816_consumption`  
  Load '32_LVBus696816_consumption' has phase imbalance of 99.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697068_consumption`  
  Load '32_LVBus697068_consumption' has phase imbalance of 273.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696885_consumption`  
  Load '32_LVBus696885_consumption' has phase imbalance of 57.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696924_consumption`  
  Load '32_LVBus696924_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696899_consumption`  
  Load '32_LVBus696899_consumption' has phase imbalance of 233.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696939_consumption`  
  Load '32_LVBus696939_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696993_consumption`  
  Load '32_LVBus696993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696969_consumption`  
  Load '32_LVBus696969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697079_consumption`  
  Load '32_LVBus697079_consumption' has phase imbalance of 163.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696946_consumption`  
  Load '32_LVBus696946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696976_consumption`  
  Load '32_LVBus696976_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696977_consumption`  
  Load '32_LVBus696977_consumption' has phase imbalance of 169.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696994_consumption`  
  Load '32_LVBus696994_consumption' has phase imbalance of 133.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697078_consumption`  
  Load '32_LVBus697078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696950_consumption`  
  Load '32_LVBus696950_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697009_consumption`  
  Load '32_LVBus697009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696898_consumption`  
  Load '32_LVBus696898_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696968_consumption`  
  Load '32_LVBus696968_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697080_consumption`  
  Load '32_LVBus697080_consumption' has phase imbalance of 259.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696967_consumption`  
  Load '32_LVBus696967_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696832_consumption`  
  Load '32_LVBus696832_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696973_consumption`  
  Load '32_LVBus696973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697077_consumption`  
  Load '32_LVBus697077_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697075_consumption`  
  Load '32_LVBus697075_consumption' has phase imbalance of 233.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697003_consumption`  
  Load '32_LVBus697003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696897_consumption`  
  Load '32_LVBus696897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696934_consumption`  
  Load '32_LVBus696934_consumption' has phase imbalance of 264.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696778_consumption`  
  Load '32_LVBus696778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696928_consumption`  
  Load '32_LVBus696928_consumption' has phase imbalance of 196.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697005_consumption`  
  Load '32_LVBus697005_consumption' has phase imbalance of 54.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696958_consumption`  
  Load '32_LVBus696958_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697053_consumption`  
  Load '32_LVBus697053_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696805_consumption`  
  Load '32_LVBus696805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696963_consumption`  
  Load '32_LVBus696963_consumption' has phase imbalance of 190.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696890_consumption`  
  Load '32_LVBus696890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697004_consumption`  
  Load '32_LVBus697004_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696964_consumption`  
  Load '32_LVBus696964_consumption' has phase imbalance of 283.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696965_consumption`  
  Load '32_LVBus696965_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697074_consumption`  
  Load '32_LVBus697074_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696998_consumption`  
  Load '32_LVBus696998_consumption' has phase imbalance of 199.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696966_consumption`  
  Load '32_LVBus696966_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697048_consumption`  
  Load '32_LVBus697048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697065_consumption`  
  Load '32_LVBus697065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696932_consumption`  
  Load '32_LVBus696932_consumption' has phase imbalance of 225.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696980_consumption`  
  Load '32_LVBus696980_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696814_consumption`  
  Load '32_LVBus696814_consumption' has phase imbalance of 277.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696975_consumption`  
  Load '32_LVBus696975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696874_consumption`  
  Load '32_LVBus696874_consumption' has phase imbalance of 93.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697055_consumption`  
  Load '32_LVBus697055_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697000_consumption`  
  Load '32_LVBus697000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696812_consumption`  
  Load '32_LVBus696812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697042_consumption`  
  Load '32_LVBus697042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697072_consumption`  
  Load '32_LVBus697072_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696985_consumption`  
  Load '32_LVBus696985_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696937_consumption`  
  Load '32_LVBus696937_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696807_consumption`  
  Load '32_LVBus696807_consumption' has phase imbalance of 39.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696938_consumption`  
  Load '32_LVBus696938_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696990_consumption`  
  Load '32_LVBus696990_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697056_consumption`  
  Load '32_LVBus697056_consumption' has phase imbalance of 82.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697043_consumption`  
  Load '32_LVBus697043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696860_consumption`  
  Load '32_LVBus696860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696883_consumption`  
  Load '32_LVBus696883_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696893_consumption`  
  Load '32_LVBus696893_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696818_consumption`  
  Load '32_LVBus696818_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696984_consumption`  
  Load '32_LVBus696984_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697006_consumption`  
  Load '32_LVBus697006_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696879_consumption`  
  Load '32_LVBus696879_consumption' has phase imbalance of 64.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696866_consumption`  
  Load '32_LVBus696866_consumption' has phase imbalance of 129.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697067_consumption`  
  Load '32_LVBus697067_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696882_consumption`  
  Load '32_LVBus696882_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696931_consumption`  
  Load '32_LVBus696931_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696881_consumption`  
  Load '32_LVBus696881_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696930_consumption`  
  Load '32_LVBus696930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697076_consumption`  
  Load '32_LVBus697076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696960_consumption`  
  Load '32_LVBus696960_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696989_consumption`  
  Load '32_LVBus696989_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697071_consumption`  
  Load '32_LVBus697071_consumption' has phase imbalance of 146.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696867_consumption`  
  Load '32_LVBus696867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697045_consumption`  
  Load '32_LVBus697045_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696817_consumption`  
  Load '32_LVBus696817_consumption' has phase imbalance of 51.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696863_consumption`  
  Load '32_LVBus696863_consumption' has phase imbalance of 91.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696949_consumption`  
  Load '32_LVBus696949_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696870_consumption`  
  Load '32_LVBus696870_consumption' has phase imbalance of 60.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696821_consumption`  
  Load '32_LVBus696821_consumption' has phase imbalance of 255.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697054_consumption`  
  Load '32_LVBus697054_consumption' has phase imbalance of 95.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696929_consumption`  
  Load '32_LVBus696929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696811_consumption`  
  Load '32_LVBus696811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696901_consumption`  
  Load '32_LVBus696901_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697070_consumption`  
  Load '32_LVBus697070_consumption' has phase imbalance of 254.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696971_consumption`  
  Load '32_LVBus696971_consumption' has phase imbalance of 206.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696808_consumption`  
  Load '32_LVBus696808_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696829_consumption`  
  Load '32_LVBus696829_consumption' has phase imbalance of 278.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696933_consumption`  
  Load '32_LVBus696933_consumption' has phase imbalance of 46.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus697073_consumption`  
  Load '32_LVBus697073_consumption' has phase imbalance of 239.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696952_consumption`  
  Load '32_LVBus696952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696884_consumption`  
  Load '32_LVBus696884_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus696862_consumption`  
  Load '32_LVBus696862_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 522 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_ARRAS' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus696781' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus696838' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus697039' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus696793' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus697061' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '32_ARRAS' (MV, 11.78 kV) has an electrical reach of 21.91 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus697039' (LV, 0.24 kV) has an electrical reach of 3.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus1128351' (LV, 0.24 kV) has an electrical reach of 16.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  320 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  99 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus696778_consumption, 32_LVBus696805_consumption, 32_LVBus696811_consumption, 32_LVBus696812_consumption, 32_LVBus696813_consumption, 32_LVBus696814_consumption, 32_LVBus696818_consumption, 32_LVBus696821_consumption, 32_LVBus696829_consumption, 32_LVBus696831_consumption, 32_LVBus696835_consumption, 32_LVBus696859_consumption, 32_LVBus696860_consumption, 32_LVBus696862_consumption, 32_LVBus696867_consumption, 32_LVBus696869_consumption, 32_LVBus696872_consumption, 32_LVBus696873_consumption, 32_LVBus696888_consumption, 32_LVBus696889_consumption, 32_LVBus696890_consumption, 32_LVBus696891_consumption, 32_LVBus696892_consumption, 32_LVBus696893_consumption, 32_LVBus696896_consumption, 32_LVBus696897_consumption, 32_LVBus696899_consumption, 32_LVBus696923_consumption, 32_LVBus696924_consumption, 32_LVBus696927_consumption, 32_LVBus696928_consumption, 32_LVBus696929_consumption, 32_LVBus696930_consumption, 32_LVBus696931_consumption, 32_LVBus696932_consumption, 32_LVBus696934_consumption, 32_LVBus696935_consumption, 32_LVBus696937_consumption, 32_LVBus696938_consumption, 32_LVBus696939_consumption, 32_LVBus696941_consumption, 32_LVBus696943_consumption, 32_LVBus696945_consumption, 32_LVBus696946_consumption, 32_LVBus696949_consumption, 32_LVBus696952_consumption, 32_LVBus696953_consumption, 32_LVBus696958_consumption, 32_LVBus696959_consumption, 32_LVBus696963_consumption, 32_LVBus696965_consumption, 32_LVBus696967_consumption, 32_LVBus696968_consumption, 32_LVBus696969_consumption, 32_LVBus696971_consumption, 32_LVBus696973_consumption, 32_LVBus696975_consumption, 32_LVBus696976_consumption, 32_LVBus696977_consumption, 32_LVBus696978_consumption, 32_LVBus696980_consumption, 32_LVBus696984_consumption, 32_LVBus696985_consumption, 32_LVBus696986_consumption, 32_LVBus696990_consumption, 32_LVBus696991_consumption, 32_LVBus696993_consumption, 32_LVBus696995_consumption, 32_LVBus696996_consumption, 32_LVBus696998_consumption, 32_LVBus696999_consumption, 32_LVBus697000_consumption, 32_LVBus697001_consumption, 32_LVBus697002_consumption, 32_LVBus697003_consumption, 32_LVBus697004_consumption, 32_LVBus697009_consumption, 32_LVBus697042_consumption, 32_LVBus697043_consumption, 32_LVBus697047_consumption, 32_LVBus697048_consumption, 32_LVBus697051_consumption, 32_LVBus697052_consumption, 32_LVBus697053_consumption, 32_LVBus697055_consumption, 32_LVBus697057_consumption, 32_LVBus697063_consumption, 32_LVBus697065_consumption, 32_LVBus697066_consumption, 32_LVBus697067_consumption, 32_LVBus697068_consumption, 32_LVBus697070_consumption, 32_LVBus697073_consumption, 32_LVBus697074_consumption, 32_LVBus697075_consumption, 32_LVBus697076_consumption, 32_LVBus697078_consumption, 32_LVBus697079_consumption, 32_LVBus697080_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  261 group(s) of loads (522 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  4 group(s) of series lines (8 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  332 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1128351_consumption, 32_LVBus1128351_production, 32_LVBus696774_consumption, 32_LVBus696774_production, 32_LVBus696776_production, 32_LVBus696777_consumption, 32_LVBus696777_production, 32_LVBus696778_production, 32_LVBus696781_consumption, 32_LVBus696781_production, 32_LVBus696782_production, 32_LVBus696784_consumption, 32_LVBus696784_production, 32_LVBus696785_production, 32_LVBus696787_consumption, 32_LVBus696787_production, 32_LVBus696788_production, 32_LVBus696790_production, 32_LVBus696791_production, 32_LVBus696793_consumption, 32_LVBus696793_production, 32_LVBus696795_consumption, 32_LVBus696795_production, 32_LVBus696797_production, 32_LVBus696799_consumption, 32_LVBus696799_production, 32_LVBus696801_production, 32_LVBus696802_production, 32_LVBus696805_production, 32_LVBus696806_production, 32_LVBus696807_production, 32_LVBus696808_production, 32_LVBus696809_production, 32_LVBus696810_consumption, 32_LVBus696810_production, 32_LVBus696811_production, 32_LVBus696812_production, 32_LVBus696813_production, 32_LVBus696814_production, 32_LVBus696816_production, 32_LVBus696817_production, 32_LVBus696818_production, 32_LVBus696819_production, 32_LVBus696820_consumption, 32_LVBus696820_production, 32_LVBus696821_production, 32_LVBus696823_production, 32_LVBus696824_production, 32_LVBus696826_consumption, 32_LVBus696826_production, 32_LVBus696827_consumption, 32_LVBus696827_production, 32_LVBus696828_consumption, 32_LVBus696828_production, 32_LVBus696829_production, 32_LVBus696830_consumption, 32_LVBus696830_production, 32_LVBus696831_production, 32_LVBus696832_production, 32_LVBus696833_consumption, 32_LVBus696833_production, 32_LVBus696834_consumption, 32_LVBus696834_production, 32_LVBus696835_production, 32_LVBus696836_production, 32_LVBus696838_consumption, 32_LVBus696838_production, 32_LVBus696839_consumption, 32_LVBus696839_production, 32_LVBus696840_consumption, 32_LVBus696840_production, 32_LVBus696842_consumption, 32_LVBus696842_production, 32_LVBus696843_consumption, 32_LVBus696843_production, 32_LVBus696844_production, 32_LVBus696846_production, 32_LVBus696848_production, 32_LVBus696850_production, 32_LVBus696852_consumption, 32_LVBus696852_production, 32_LVBus696853_consumption, 32_LVBus696853_production, 32_LVBus696855_consumption, 32_LVBus696855_production, 32_LVBus696857_consumption, 32_LVBus696857_production, 32_LVBus696858_consumption, 32_LVBus696858_production, 32_LVBus696859_production, 32_LVBus696860_production, 32_LVBus696862_production, 32_LVBus696863_production, 32_LVBus696866_production, 32_LVBus696867_production, 32_LVBus696869_production, 32_LVBus696870_production, 32_LVBus696871_consumption, 32_LVBus696871_production, 32_LVBus696872_production, 32_LVBus696873_production, 32_LVBus696874_production, 32_LVBus696875_production, 32_LVBus696877_production, 32_LVBus696878_production, 32_LVBus696879_production, 32_LVBus696880_production, 32_LVBus696881_production, 32_LVBus696882_production, 32_LVBus696883_production, 32_LVBus696884_production, 32_LVBus696885_production, 32_LVBus696886_production, 32_LVBus696888_production, 32_LVBus696889_production, 32_LVBus696890_production, 32_LVBus696891_production, 32_LVBus696892_production, 32_LVBus696893_production, 32_LVBus696895_consumption, 32_LVBus696895_production, 32_LVBus696896_production, 32_LVBus696897_production, 32_LVBus696898_production, 32_LVBus696899_production, 32_LVBus696900_consumption, 32_LVBus696900_production, 32_LVBus696901_production, 32_LVBus696902_production, 32_LVBus696904_production, 32_LVBus696906_production, 32_LVBus696908_production, 32_LVBus696910_production, 32_LVBus696911_consumption, 32_LVBus696911_production, 32_LVBus696913_production, 32_LVBus696915_consumption, 32_LVBus696915_production, 32_LVBus696917_production, 32_LVBus696919_production, 32_LVBus696921_production, 32_LVBus696923_production, 32_LVBus696924_production, 32_LVBus696925_production, 32_LVBus696926_production, 32_LVBus696927_production, 32_LVBus696928_production, 32_LVBus696929_production, 32_LVBus696930_production, 32_LVBus696931_production, 32_LVBus696932_production, 32_LVBus696933_production, 32_LVBus696934_production, 32_LVBus696935_production, 32_LVBus696937_production, 32_LVBus696938_production, 32_LVBus696939_production, 32_LVBus696940_production, 32_LVBus696941_production, 32_LVBus696943_production, 32_LVBus696945_production, 32_LVBus696946_production, 32_LVBus696947_production, 32_LVBus696948_production, 32_LVBus696949_production, 32_LVBus696950_production, 32_LVBus696951_consumption, 32_LVBus696951_production, 32_LVBus696952_production, 32_LVBus696953_production, 32_LVBus696957_consumption, 32_LVBus696957_production, 32_LVBus696958_production, 32_LVBus696959_production, 32_LVBus696960_production, 32_LVBus696962_consumption, 32_LVBus696962_production, 32_LVBus696963_production, 32_LVBus696964_production, 32_LVBus696965_production, 32_LVBus696966_production, 32_LVBus696967_production, 32_LVBus696968_production, 32_LVBus696969_production, 32_LVBus696971_production, 32_LVBus696973_production, 32_LVBus696974_consumption, 32_LVBus696974_production, 32_LVBus696975_production, 32_LVBus696976_production, 32_LVBus696977_production, 32_LVBus696978_production, 32_LVBus696979_production, 32_LVBus696980_production, 32_LVBus696981_production, 32_LVBus696983_production, 32_LVBus696984_production, 32_LVBus696985_production, 32_LVBus696986_production, 32_LVBus696987_production, 32_LVBus696988_consumption, 32_LVBus696988_production, 32_LVBus696989_production, 32_LVBus696990_production, 32_LVBus696991_production, 32_LVBus696993_production, 32_LVBus696994_production, 32_LVBus696995_production, 32_LVBus696996_production, 32_LVBus696998_production, 32_LVBus696999_production, 32_LVBus697000_production, 32_LVBus697001_production, 32_LVBus697002_production, 32_LVBus697003_production, 32_LVBus697004_production, 32_LVBus697005_production, 32_LVBus697006_production, 32_LVBus697007_production, 32_LVBus697009_production, 32_LVBus697013_consumption, 32_LVBus697013_production, 32_LVBus697015_consumption, 32_LVBus697015_production, 32_LVBus697016_consumption, 32_LVBus697016_production, 32_LVBus697017_consumption, 32_LVBus697017_production, 32_LVBus697019_consumption, 32_LVBus697019_production, 32_LVBus697020_consumption, 32_LVBus697020_production, 32_LVBus697021_consumption, 32_LVBus697021_production, 32_LVBus697023_consumption, 32_LVBus697023_production, 32_LVBus697024_consumption, 32_LVBus697024_production, 32_LVBus697025_consumption, 32_LVBus697025_production, 32_LVBus697027_consumption, 32_LVBus697027_production, 32_LVBus697029_consumption, 32_LVBus697029_production, 32_LVBus697031_consumption, 32_LVBus697031_production, 32_LVBus697033_consumption, 32_LVBus697033_production, 32_LVBus697035_consumption, 32_LVBus697035_production, 32_LVBus697037_consumption, 32_LVBus697037_production, 32_LVBus697039_production, 32_LVBus697041_production, 32_LVBus697042_production, 32_LVBus697043_production, 32_LVBus697044_consumption, 32_LVBus697044_production, 32_LVBus697045_production, 32_LVBus697046_consumption, 32_LVBus697046_production, 32_LVBus697047_production, 32_LVBus697048_production, 32_LVBus697049_consumption, 32_LVBus697049_production, 32_LVBus697050_production, 32_LVBus697051_production, 32_LVBus697052_production, 32_LVBus697053_production, 32_LVBus697054_production, 32_LVBus697055_production, 32_LVBus697056_production, 32_LVBus697057_production, 32_LVBus697061_production, 32_LVBus697063_production, 32_LVBus697064_consumption, 32_LVBus697064_production, 32_LVBus697065_production, 32_LVBus697066_production, 32_LVBus697067_production, 32_LVBus697068_production, 32_LVBus697069_consumption, 32_LVBus697069_production, 32_LVBus697070_production, 32_LVBus697071_production, 32_LVBus697072_production, 32_LVBus697073_production, 32_LVBus697074_production, 32_LVBus697075_production, 32_LVBus697076_production, 32_LVBus697077_production, 32_LVBus697078_production, 32_LVBus697079_production, 32_LVBus697080_production, 32_LVBus697081_production, 32_LVBus697082_consumption, 32_LVBus697082_production, 32_LVBus697084_consumption, 32_LVBus697084_production, 32_LVBus697086_consumption, 32_LVBus697086_production, 32_LVBus697087_production, 32_LVBus697088_production, 32_LVBus697090_consumption, 32_LVBus697090_production, 32_LVBus697091_production, 32_LVBus697092_consumption, 32_LVBus697092_production, 32_LVBus697093_production, 32_LVBus697095_production, 32_LVBus697097_consumption, 32_LVBus697097_production, 32_LVBus697098_production, 32_LVBus697099_production, 32_LVBus697101_production, 32_LVBus697103_consumption, 32_LVBus697103_production, 32_LVBus697105_production, 32_LVBus697109_consumption, 32_LVBus697109_production, 32_MVLV05364_consumption, 32_MVLV05364_production, 32_MVLV13372_consumption, 32_MVLV13372_production, 32_MVLV15315_consumption, 32_MVLV15315_production, 32_MVLV25093_consumption, 32_MVLV25093_production, 32_MVLV46624_production, 32_MVLV61153_production, 32_MVLV64448_consumption, 32_MVLV64448_production.

