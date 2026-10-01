# BMOPF Network Summary: 44_MVFeeder2376

**Generated:** 2026-10-01 23:34:11  
**Findings:** 0 errors · 5 warnings · 244 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 17 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 380 |  |
| line | 362 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 644 | 3.26 MW, 978.0 kvar |
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
| MV_11.8kV | 11.78 kV | 49 | 48 | 16 | 0 |
| LV_236V | 236.0 V | 331 | 314 | 628 | 0 |

**Transformer transitions:**

- `44_MVLV49555_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV52243_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV62715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV43656_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV19850_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV60571_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV04853_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV19851_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV46682_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV38135_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV32801_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV11960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV20069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV56169_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV50561_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV15568_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV08789_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 7 |
| Degree-1 buses | 121 |
| Tree depth (max hops) | 29 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 380 | 1 | 379 | 0 | 0 | 0 |
| Tier LV_236V | 331 | 17 | 314 | 0 | 0 | 0 |
| Tier MV_11.8kV | 49 | 1 | 48 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 17; skipped invalid branches: 0.

Galvanic zones: 18; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 44_MVBus42600 | MV_11.8kV | 49 | 0 | 0 | 17 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1471 declared bus terminals; 1400 mapped line/closed-switch conductor edges; 71 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 300000.0 | 7.171 | 1932 |
| q_nom | 0.0 | 89900.0 | 7.171 | 1932 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.501 | 1440.0 | 1.67 | 362 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.605 | 17 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 392 of 644 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014013_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus885815_consumption' has phase imbalance of 86.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014048_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014104_consumption' has phase imbalance of 230.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus857106_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014027_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013937_consumption' has phase imbalance of 114.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013923_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014014_consumption' has phase imbalance of 71.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014135_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014183_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014055_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884871_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014084_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014087_consumption' has phase imbalance of 142.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014125_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014111_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014112_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014080_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014049_consumption' has phase imbalance of 173.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014090_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014008_consumption' has phase imbalance of 122.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013982_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus852926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886259_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013995_consumption' has phase imbalance of 91.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014032_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014128_consumption' has phase imbalance of 282.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014136_consumption' has phase imbalance of 102.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013915_consumption' has phase imbalance of 82.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858579_consumption' has phase imbalance of 86.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus856577_consumption' has phase imbalance of 79.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014053_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014151_consumption' has phase imbalance of 73.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus859442_consumption' has phase imbalance of 54.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013903_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013979_consumption' has phase imbalance of 211.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014064_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013977_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013895_consumption' has phase imbalance of 41.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858628_consumption' has phase imbalance of 47.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014107_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013954_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014093_consumption' has phase imbalance of 137.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013908_consumption' has phase imbalance of 245.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014142_consumption' has phase imbalance of 111.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013968_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013967_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013939_consumption' has phase imbalance of 62.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014118_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013943_consumption' has phase imbalance of 84.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014069_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013981_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858580_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013960_consumption' has phase imbalance of 120.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013945_consumption' has phase imbalance of 258.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014089_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013999_consumption' has phase imbalance of 234.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus857314_consumption' has phase imbalance of 114.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014028_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus853817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884872_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014036_consumption' has phase imbalance of 90.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013994_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014029_consumption' has phase imbalance of 90.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013964_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886256_consumption' has phase imbalance of 88.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014085_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013989_consumption' has phase imbalance of 246.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014110_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858626_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013980_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014058_consumption' has phase imbalance of 179.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014122_consumption' has phase imbalance of 98.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014156_consumption' has phase imbalance of 181.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014082_consumption' has phase imbalance of 252.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013996_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus860936_consumption' has phase imbalance of 191.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013916_consumption' has phase imbalance of 116.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013998_consumption' has phase imbalance of 158.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013934_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus860955_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013904_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013970_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014133_consumption' has phase imbalance of 96.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus853815_consumption' has phase imbalance of 203.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884870_consumption' has phase imbalance of 113.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014059_consumption' has phase imbalance of 235.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014169_consumption' has phase imbalance of 204.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014072_consumption' has phase imbalance of 136.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014162_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014054_consumption' has phase imbalance of 40.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886255_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013912_consumption' has phase imbalance of 118.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014143_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884874_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014119_consumption' has phase imbalance of 203.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013911_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013917_consumption' has phase imbalance of 32.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus853819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014168_consumption' has phase imbalance of 252.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013901_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus856576_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014158_consumption' has phase imbalance of 64.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014117_consumption' has phase imbalance of 86.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013959_consumption' has phase imbalance of 62.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013925_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014163_consumption' has phase imbalance of 24.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014115_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus875766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014067_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014035_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014088_consumption' has phase imbalance of 61.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014042_consumption' has phase imbalance of 264.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014031_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013899_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013952_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014109_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus860439_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014121_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014051_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus885816_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014100_consumption' has phase imbalance of 258.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013906_consumption' has phase imbalance of 239.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013902_consumption' has phase imbalance of 28.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014177_consumption' has phase imbalance of 123.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013955_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013909_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014094_consumption' has phase imbalance of 207.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858627_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014130_consumption' has phase imbalance of 265.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013918_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014024_consumption' has phase imbalance of 58.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014092_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014076_consumption' has phase imbalance of 255.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014009_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014017_consumption' has phase imbalance of 97.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus869562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014144_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014018_consumption' has phase imbalance of 95.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013976_consumption' has phase imbalance of 122.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014178_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013905_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus859440_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014001_consumption' has phase imbalance of 40.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014086_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014083_consumption' has phase imbalance of 97.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884282_consumption' has phase imbalance of 38.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus859443_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014114_consumption' has phase imbalance of 273.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus859438_consumption' has phase imbalance of 225.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014037_consumption' has phase imbalance of 97.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014047_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013896_consumption' has phase imbalance of 121.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013894_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013988_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014022_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013926_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013953_consumption' has phase imbalance of 54.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014056_consumption' has phase imbalance of 147.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013922_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013991_consumption' has phase imbalance of 51.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013935_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014015_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013961_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus854060_consumption' has phase imbalance of 125.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886253_consumption' has phase imbalance of 156.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014116_consumption' has phase imbalance of 209.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus857104_consumption' has phase imbalance of 200.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014000_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013949_consumption' has phase imbalance of 57.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014012_consumption' has phase imbalance of 26.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus855176_consumption' has phase imbalance of 76.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014050_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014033_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014134_consumption' has phase imbalance of 79.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014003_consumption' has phase imbalance of 53.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014171_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884879_consumption' has phase imbalance of 260.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014164_consumption' has phase imbalance of 112.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014026_consumption' has phase imbalance of 118.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014124_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013987_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014176_consumption' has phase imbalance of 82.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus853975_consumption' has phase imbalance of 238.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886254_consumption' has phase imbalance of 81.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus859276_consumption' has phase imbalance of 61.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013920_consumption' has phase imbalance of 23.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus884875_consumption' has phase imbalance of 75.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014045_consumption' has phase imbalance of 86.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014167_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus852805_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014108_consumption' has phase imbalance of 77.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus886257_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014155_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus014007_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus853816_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus857105_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus013990_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 644 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_SSHUB' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.26 MW |
| Total load Q | 978.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 44_MVLV49555_Transformer | 110.0 kVA | 0.7% |
| 44_MVLV52243_Transformer | 176.0 kVA | 0.0% |
| 44_MVLV62715_Transformer | 176.0 kVA | 7.9% |
| 44_MVLV43656_Transformer | 275.0 kVA | 42.1% |
| 44_MVLV19850_Transformer | 275.0 kVA | 56.0% |
| 44_MVLV60571_Transformer | 693.0 kVA | 41.6% |
| 44_MVLV04853_Transformer | 693.0 kVA | 39.0% |
| 44_MVLV19851_Transformer | 176.0 kVA | 41.0% |
| 44_MVLV46682_Transformer | 275.0 kVA | 37.7% |
| 44_MVLV38135_Transformer | 110.0 kVA | 6.8% |
| 44_MVLV32801_Transformer | 693.0 kVA | 39.2% |
| 44_MVLV11960_Transformer | 176.0 kVA | 30.6% |
| 44_MVLV20069_Transformer | 440.0 kVA | 57.3% |
| 44_MVLV56169_Transformer | 693.0 kVA | 44.7% |
| 44_MVLV50561_Transformer | 440.0 kVA | 38.9% |
| 44_MVLV15568_Transformer | 693.0 kVA | 41.2% |
| 44_MVLV08789_Transformer | 693.0 kVA | 13.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.26 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus014039' (LV, 0.24 kV) has an electrical reach of 4.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus014074' (LV, 0.24 kV) has an electrical reach of 16.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 380 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 380 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 17 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 49 |
| LV_236V | 4-wire | 331 / 331 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 331 |
| Neutral branches | 314 |
| Grounding points | 17 |
| Neutral sections | 17 |
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
| 11.78 kV | 49 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 48 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 46 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 18 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2200.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 331 / 49 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 393 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 393 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus013894_production, 44_LVBus013895_production, 44_LVBus013896_production, 44_LVBus013897_production, 44_LVBus013899_production, 44_LVBus013901_production, 44_LVBus013902_production, 44_LVBus013903_production, 44_LVBus013904_production, 44_LVBus013905_production, 44_LVBus013906_production, 44_LVBus013908_production, 44_LVBus013909_production, 44_LVBus013911_production, 44_LVBus013912_production, 44_LVBus013913_consumption, 44_LVBus013913_production, 44_LVBus013915_production, 44_LVBus013916_production, 44_LVBus013917_production, 44_LVBus013918_production, 44_LVBus013919_consumption, 44_LVBus013919_production, 44_LVBus013920_production, 44_LVBus013921_production, 44_LVBus013922_production, 44_LVBus013923_production, 44_LVBus013925_production, 44_LVBus013926_production, 44_LVBus013927_consumption, 44_LVBus013927_production, 44_LVBus013928_consumption, 44_LVBus013928_production, 44_LVBus013929_production, 44_LVBus013930_consumption, 44_LVBus013930_production, 44_LVBus013931_consumption, 44_LVBus013931_production, 44_LVBus013932_production, 44_LVBus013933_consumption, 44_LVBus013933_production, 44_LVBus013934_production, 44_LVBus013935_production, 44_LVBus013937_production, 44_LVBus013939_production, 44_LVBus013941_consumption, 44_LVBus013941_production, 44_LVBus013943_production, 44_LVBus013945_production, 44_LVBus013947_production, 44_LVBus013949_production, 44_LVBus013951_consumption, 44_LVBus013951_production, 44_LVBus013952_production, 44_LVBus013953_production, 44_LVBus013954_production, 44_LVBus013955_production, 44_LVBus013956_consumption, 44_LVBus013956_production, 44_LVBus013958_consumption, 44_LVBus013958_production, 44_LVBus013959_production, 44_LVBus013960_production, 44_LVBus013961_production, 44_LVBus013963_consumption, 44_LVBus013963_production, 44_LVBus013964_production, 44_LVBus013966_production, 44_LVBus013967_production, 44_LVBus013968_production, 44_LVBus013970_production, 44_LVBus013972_consumption, 44_LVBus013972_production, 44_LVBus013973_production, 44_LVBus013975_production, 44_LVBus013976_production, 44_LVBus013977_production, 44_LVBus013978_consumption, 44_LVBus013978_production, 44_LVBus013979_production, 44_LVBus013980_production, 44_LVBus013981_production, 44_LVBus013982_production, 44_LVBus013983_production, 44_LVBus013984_consumption, 44_LVBus013984_production, 44_LVBus013986_production, 44_LVBus013987_production, 44_LVBus013988_production, 44_LVBus013989_production, 44_LVBus013990_production, 44_LVBus013991_production, 44_LVBus013993_production, 44_LVBus013994_production, 44_LVBus013995_production, 44_LVBus013996_production, 44_LVBus013997_consumption, 44_LVBus013997_production, 44_LVBus013998_production, 44_LVBus013999_production, 44_LVBus014000_production, 44_LVBus014001_production, 44_LVBus014002_consumption, 44_LVBus014002_production, 44_LVBus014003_production, 44_LVBus014004_consumption, 44_LVBus014004_production, 44_LVBus014005_production, 44_LVBus014006_production, 44_LVBus014007_production, 44_LVBus014008_production, 44_LVBus014009_production, 44_LVBus014011_consumption, 44_LVBus014011_production, 44_LVBus014012_production, 44_LVBus014013_production, 44_LVBus014014_production, 44_LVBus014015_production, 44_LVBus014017_production, 44_LVBus014018_production, 44_LVBus014019_production, 44_LVBus014020_production, 44_LVBus014022_production, 44_LVBus014023_production, 44_LVBus014024_production, 44_LVBus014026_production, 44_LVBus014027_production, 44_LVBus014028_production, 44_LVBus014029_production, 44_LVBus014031_production, 44_LVBus014032_production, 44_LVBus014033_production, 44_LVBus014035_production, 44_LVBus014036_production, 44_LVBus014037_production, 44_LVBus014039_production, 44_LVBus014041_production, 44_LVBus014042_production, 44_LVBus014044_production, 44_LVBus014045_production, 44_LVBus014046_production, 44_LVBus014047_production, 44_LVBus014048_production, 44_LVBus014049_production, 44_LVBus014050_production, 44_LVBus014051_production, 44_LVBus014053_production, 44_LVBus014054_production, 44_LVBus014055_production, 44_LVBus014056_production, 44_LVBus014058_production, 44_LVBus014059_production, 44_LVBus014060_production, 44_LVBus014061_consumption, 44_LVBus014061_production, 44_LVBus014063_consumption, 44_LVBus014063_production, 44_LVBus014064_production, 44_LVBus014065_consumption, 44_LVBus014065_production, 44_LVBus014066_production, 44_LVBus014067_production, 44_LVBus014068_production, 44_LVBus014069_production, 44_LVBus014071_production, 44_LVBus014072_production, 44_LVBus014074_production, 44_LVBus014076_production, 44_LVBus014077_consumption, 44_LVBus014077_production, 44_LVBus014078_production, 44_LVBus014080_production, 44_LVBus014081_production, 44_LVBus014082_production, 44_LVBus014083_production, 44_LVBus014084_production, 44_LVBus014085_production, 44_LVBus014086_production, 44_LVBus014087_production, 44_LVBus014088_production, 44_LVBus014089_production, 44_LVBus014090_production, 44_LVBus014092_production, 44_LVBus014093_production, 44_LVBus014094_production, 44_LVBus014096_production, 44_LVBus014098_consumption, 44_LVBus014098_production, 44_LVBus014100_production, 44_LVBus014101_production, 44_LVBus014102_production, 44_LVBus014103_production, 44_LVBus014104_production, 44_LVBus014106_consumption, 44_LVBus014106_production, 44_LVBus014107_production, 44_LVBus014108_production, 44_LVBus014109_production, 44_LVBus014110_production, 44_LVBus014111_production, 44_LVBus014112_production, 44_LVBus014113_production, 44_LVBus014114_production, 44_LVBus014115_production, 44_LVBus014116_production, 44_LVBus014117_production, 44_LVBus014118_production, 44_LVBus014119_production, 44_LVBus014120_production, 44_LVBus014121_production, 44_LVBus014122_production, 44_LVBus014123_consumption, 44_LVBus014123_production, 44_LVBus014124_production, 44_LVBus014125_production, 44_LVBus014127_consumption, 44_LVBus014127_production, 44_LVBus014128_production, 44_LVBus014129_production, 44_LVBus014130_production, 44_LVBus014131_consumption, 44_LVBus014131_production, 44_LVBus014132_consumption, 44_LVBus014132_production, 44_LVBus014133_production, 44_LVBus014134_production, 44_LVBus014135_production, 44_LVBus014136_production, 44_LVBus014138_consumption, 44_LVBus014138_production, 44_LVBus014139_production, 44_LVBus014140_consumption, 44_LVBus014140_production, 44_LVBus014141_consumption, 44_LVBus014141_production, 44_LVBus014142_production, 44_LVBus014143_production, 44_LVBus014144_production, 44_LVBus014145_consumption, 44_LVBus014145_production, 44_LVBus014146_production, 44_LVBus014147_production, 44_LVBus014149_consumption, 44_LVBus014149_production, 44_LVBus014150_consumption, 44_LVBus014150_production, 44_LVBus014151_production, 44_LVBus014153_production, 44_LVBus014155_production, 44_LVBus014156_production, 44_LVBus014157_consumption, 44_LVBus014157_production, 44_LVBus014158_production, 44_LVBus014160_consumption, 44_LVBus014160_production, 44_LVBus014161_consumption, 44_LVBus014161_production, 44_LVBus014162_production, 44_LVBus014163_production, 44_LVBus014164_production, 44_LVBus014165_consumption, 44_LVBus014165_production, 44_LVBus014166_production, 44_LVBus014167_production, 44_LVBus014168_production, 44_LVBus014169_production, 44_LVBus014170_production, 44_LVBus014171_production, 44_LVBus014173_consumption, 44_LVBus014173_production, 44_LVBus014175_consumption, 44_LVBus014175_production, 44_LVBus014176_production, 44_LVBus014177_production, 44_LVBus014178_production, 44_LVBus014180_consumption, 44_LVBus014180_production, 44_LVBus014181_consumption, 44_LVBus014181_production, 44_LVBus014182_consumption, 44_LVBus014182_production, 44_LVBus014183_production, 44_LVBus014184_consumption, 44_LVBus014184_production, 44_LVBus014185_consumption, 44_LVBus014185_production, 44_LVBus014187_consumption, 44_LVBus014187_production, 44_LVBus014188_consumption, 44_LVBus014188_production, 44_LVBus014189_consumption, 44_LVBus014189_production, 44_LVBus014190_consumption, 44_LVBus014190_production, 44_LVBus014191_consumption, 44_LVBus014191_production, 44_LVBus014193_consumption, 44_LVBus014193_production, 44_LVBus852805_production, 44_LVBus852926_production, 44_LVBus853815_production, 44_LVBus853816_production, 44_LVBus853817_production, 44_LVBus853818_production, 44_LVBus853819_production, 44_LVBus853975_production, 44_LVBus854060_production, 44_LVBus855176_production, 44_LVBus856576_production, 44_LVBus856577_production, 44_LVBus857104_production, 44_LVBus857105_production, 44_LVBus857106_production, 44_LVBus857314_production, 44_LVBus858579_production, 44_LVBus858580_production, 44_LVBus858626_production, 44_LVBus858627_production, 44_LVBus858628_production, 44_LVBus858629_consumption, 44_LVBus858629_production, 44_LVBus858630_consumption, 44_LVBus858630_production, 44_LVBus859276_production, 44_LVBus859437_consumption, 44_LVBus859437_production, 44_LVBus859438_production, 44_LVBus859439_production, 44_LVBus859440_production, 44_LVBus859441_production, 44_LVBus859442_production, 44_LVBus859443_production, 44_LVBus860439_production, 44_LVBus860936_production, 44_LVBus860955_production, 44_LVBus863227_consumption, 44_LVBus863227_production, 44_LVBus863228_consumption, 44_LVBus863228_production, 44_LVBus863229_consumption, 44_LVBus863229_production, 44_LVBus863230_consumption, 44_LVBus863230_production, 44_LVBus866557_consumption, 44_LVBus866557_production, 44_LVBus868417_production, 44_LVBus868418_production, 44_LVBus869561_consumption, 44_LVBus869561_production, 44_LVBus869562_production, 44_LVBus875764_consumption, 44_LVBus875764_production, 44_LVBus875765_consumption, 44_LVBus875765_production, 44_LVBus875766_production, 44_LVBus882006_consumption, 44_LVBus882006_production, 44_LVBus884282_production, 44_LVBus884870_production, 44_LVBus884871_production, 44_LVBus884872_production, 44_LVBus884873_production, 44_LVBus884874_production, 44_LVBus884875_production, 44_LVBus884876_production, 44_LVBus884877_production, 44_LVBus884878_production, 44_LVBus884879_production, 44_LVBus885815_production, 44_LVBus885816_production, 44_LVBus886252_production, 44_LVBus886253_production, 44_LVBus886254_production, 44_LVBus886255_production, 44_LVBus886256_production, 44_LVBus886257_production, 44_LVBus886258_production, 44_LVBus886259_production, 44_MVLV04851_consumption, 44_MVLV04851_production, 44_MVLV11824_production, 44_MVLV18898_consumption, 44_MVLV18898_production, 44_MVLV27041_consumption, 44_MVLV27041_production, 44_MVLV29370_consumption, 44_MVLV29370_production, 44_MVLV39460_consumption, 44_MVLV39460_production, 44_MVLV57351_consumption, 44_MVLV57351_production, 44_MVLV64443_consumption, 44_MVLV64443_production.

## 9. Data Quality Summary

**Total findings:** 249 (0 errors, 5 warnings, 244 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  392 of 644 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.26 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  393 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884876_consumption`  
  Load '44_LVBus884876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014013_consumption`  
  Load '44_LVBus014013_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus885815_consumption`  
  Load '44_LVBus885815_consumption' has phase imbalance of 86.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014048_consumption`  
  Load '44_LVBus014048_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014104_consumption`  
  Load '44_LVBus014104_consumption' has phase imbalance of 230.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus857106_consumption`  
  Load '44_LVBus857106_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014071_consumption`  
  Load '44_LVBus014071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013929_consumption`  
  Load '44_LVBus013929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014027_consumption`  
  Load '44_LVBus014027_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013937_consumption`  
  Load '44_LVBus013937_consumption' has phase imbalance of 114.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013923_consumption`  
  Load '44_LVBus013923_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014014_consumption`  
  Load '44_LVBus014014_consumption' has phase imbalance of 71.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014135_consumption`  
  Load '44_LVBus014135_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014183_consumption`  
  Load '44_LVBus014183_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014055_consumption`  
  Load '44_LVBus014055_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014068_consumption`  
  Load '44_LVBus014068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886258_consumption`  
  Load '44_LVBus886258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884878_consumption`  
  Load '44_LVBus884878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884871_consumption`  
  Load '44_LVBus884871_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014084_consumption`  
  Load '44_LVBus014084_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014087_consumption`  
  Load '44_LVBus014087_consumption' has phase imbalance of 142.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014125_consumption`  
  Load '44_LVBus014125_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014111_consumption`  
  Load '44_LVBus014111_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014112_consumption`  
  Load '44_LVBus014112_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014080_consumption`  
  Load '44_LVBus014080_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014049_consumption`  
  Load '44_LVBus014049_consumption' has phase imbalance of 173.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014090_consumption`  
  Load '44_LVBus014090_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014008_consumption`  
  Load '44_LVBus014008_consumption' has phase imbalance of 122.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013982_consumption`  
  Load '44_LVBus013982_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus852926_consumption`  
  Load '44_LVBus852926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886259_consumption`  
  Load '44_LVBus886259_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013995_consumption`  
  Load '44_LVBus013995_consumption' has phase imbalance of 91.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014032_consumption`  
  Load '44_LVBus014032_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014128_consumption`  
  Load '44_LVBus014128_consumption' has phase imbalance of 282.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014136_consumption`  
  Load '44_LVBus014136_consumption' has phase imbalance of 102.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013915_consumption`  
  Load '44_LVBus013915_consumption' has phase imbalance of 82.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858579_consumption`  
  Load '44_LVBus858579_consumption' has phase imbalance of 86.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus856577_consumption`  
  Load '44_LVBus856577_consumption' has phase imbalance of 79.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014053_consumption`  
  Load '44_LVBus014053_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014151_consumption`  
  Load '44_LVBus014151_consumption' has phase imbalance of 73.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus859442_consumption`  
  Load '44_LVBus859442_consumption' has phase imbalance of 54.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013903_consumption`  
  Load '44_LVBus013903_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886252_consumption`  
  Load '44_LVBus886252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013979_consumption`  
  Load '44_LVBus013979_consumption' has phase imbalance of 211.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014064_consumption`  
  Load '44_LVBus014064_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013977_consumption`  
  Load '44_LVBus013977_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013895_consumption`  
  Load '44_LVBus013895_consumption' has phase imbalance of 41.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858628_consumption`  
  Load '44_LVBus858628_consumption' has phase imbalance of 47.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014107_consumption`  
  Load '44_LVBus014107_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013954_consumption`  
  Load '44_LVBus013954_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014093_consumption`  
  Load '44_LVBus014093_consumption' has phase imbalance of 137.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013908_consumption`  
  Load '44_LVBus013908_consumption' has phase imbalance of 245.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014142_consumption`  
  Load '44_LVBus014142_consumption' has phase imbalance of 111.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013968_consumption`  
  Load '44_LVBus013968_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013967_consumption`  
  Load '44_LVBus013967_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013939_consumption`  
  Load '44_LVBus013939_consumption' has phase imbalance of 62.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014118_consumption`  
  Load '44_LVBus014118_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013943_consumption`  
  Load '44_LVBus013943_consumption' has phase imbalance of 84.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014069_consumption`  
  Load '44_LVBus014069_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013981_consumption`  
  Load '44_LVBus013981_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014044_consumption`  
  Load '44_LVBus014044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884873_consumption`  
  Load '44_LVBus884873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858580_consumption`  
  Load '44_LVBus858580_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013960_consumption`  
  Load '44_LVBus013960_consumption' has phase imbalance of 120.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013945_consumption`  
  Load '44_LVBus013945_consumption' has phase imbalance of 258.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014089_consumption`  
  Load '44_LVBus014089_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013999_consumption`  
  Load '44_LVBus013999_consumption' has phase imbalance of 234.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus857314_consumption`  
  Load '44_LVBus857314_consumption' has phase imbalance of 114.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014028_consumption`  
  Load '44_LVBus014028_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013993_consumption`  
  Load '44_LVBus013993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus853817_consumption`  
  Load '44_LVBus853817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884872_consumption`  
  Load '44_LVBus884872_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014153_consumption`  
  Load '44_LVBus014153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014036_consumption`  
  Load '44_LVBus014036_consumption' has phase imbalance of 90.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013994_consumption`  
  Load '44_LVBus013994_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014029_consumption`  
  Load '44_LVBus014029_consumption' has phase imbalance of 90.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013964_consumption`  
  Load '44_LVBus013964_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886256_consumption`  
  Load '44_LVBus886256_consumption' has phase imbalance of 88.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014085_consumption`  
  Load '44_LVBus014085_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013989_consumption`  
  Load '44_LVBus013989_consumption' has phase imbalance of 246.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014110_consumption`  
  Load '44_LVBus014110_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858626_consumption`  
  Load '44_LVBus858626_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013980_consumption`  
  Load '44_LVBus013980_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014058_consumption`  
  Load '44_LVBus014058_consumption' has phase imbalance of 179.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014122_consumption`  
  Load '44_LVBus014122_consumption' has phase imbalance of 98.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014156_consumption`  
  Load '44_LVBus014156_consumption' has phase imbalance of 181.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014082_consumption`  
  Load '44_LVBus014082_consumption' has phase imbalance of 252.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013996_consumption`  
  Load '44_LVBus013996_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013983_consumption`  
  Load '44_LVBus013983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus860936_consumption`  
  Load '44_LVBus860936_consumption' has phase imbalance of 191.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013916_consumption`  
  Load '44_LVBus013916_consumption' has phase imbalance of 116.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013998_consumption`  
  Load '44_LVBus013998_consumption' has phase imbalance of 158.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013934_consumption`  
  Load '44_LVBus013934_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014120_consumption`  
  Load '44_LVBus014120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus860955_consumption`  
  Load '44_LVBus860955_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013904_consumption`  
  Load '44_LVBus013904_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013973_consumption`  
  Load '44_LVBus013973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013970_consumption`  
  Load '44_LVBus013970_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014133_consumption`  
  Load '44_LVBus014133_consumption' has phase imbalance of 96.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus853815_consumption`  
  Load '44_LVBus853815_consumption' has phase imbalance of 203.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884870_consumption`  
  Load '44_LVBus884870_consumption' has phase imbalance of 113.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014113_consumption`  
  Load '44_LVBus014113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014059_consumption`  
  Load '44_LVBus014059_consumption' has phase imbalance of 235.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014039_consumption`  
  Load '44_LVBus014039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014169_consumption`  
  Load '44_LVBus014169_consumption' has phase imbalance of 204.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014072_consumption`  
  Load '44_LVBus014072_consumption' has phase imbalance of 136.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014162_consumption`  
  Load '44_LVBus014162_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014054_consumption`  
  Load '44_LVBus014054_consumption' has phase imbalance of 40.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886255_consumption`  
  Load '44_LVBus886255_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013912_consumption`  
  Load '44_LVBus013912_consumption' has phase imbalance of 118.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014143_consumption`  
  Load '44_LVBus014143_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884874_consumption`  
  Load '44_LVBus884874_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014119_consumption`  
  Load '44_LVBus014119_consumption' has phase imbalance of 203.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013911_consumption`  
  Load '44_LVBus013911_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014081_consumption`  
  Load '44_LVBus014081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013917_consumption`  
  Load '44_LVBus013917_consumption' has phase imbalance of 32.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus853819_consumption`  
  Load '44_LVBus853819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014139_consumption`  
  Load '44_LVBus014139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014168_consumption`  
  Load '44_LVBus014168_consumption' has phase imbalance of 252.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013901_consumption`  
  Load '44_LVBus013901_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus856576_consumption`  
  Load '44_LVBus856576_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014158_consumption`  
  Load '44_LVBus014158_consumption' has phase imbalance of 64.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014117_consumption`  
  Load '44_LVBus014117_consumption' has phase imbalance of 86.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013959_consumption`  
  Load '44_LVBus013959_consumption' has phase imbalance of 62.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013925_consumption`  
  Load '44_LVBus013925_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014163_consumption`  
  Load '44_LVBus014163_consumption' has phase imbalance of 24.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014115_consumption`  
  Load '44_LVBus014115_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus875766_consumption`  
  Load '44_LVBus875766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014067_consumption`  
  Load '44_LVBus014067_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014035_consumption`  
  Load '44_LVBus014035_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014088_consumption`  
  Load '44_LVBus014088_consumption' has phase imbalance of 61.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884877_consumption`  
  Load '44_LVBus884877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014074_consumption`  
  Load '44_LVBus014074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014042_consumption`  
  Load '44_LVBus014042_consumption' has phase imbalance of 264.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014031_consumption`  
  Load '44_LVBus014031_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013899_consumption`  
  Load '44_LVBus013899_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013952_consumption`  
  Load '44_LVBus013952_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013975_consumption`  
  Load '44_LVBus013975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014109_consumption`  
  Load '44_LVBus014109_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus860439_consumption`  
  Load '44_LVBus860439_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014121_consumption`  
  Load '44_LVBus014121_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014051_consumption`  
  Load '44_LVBus014051_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus885816_consumption`  
  Load '44_LVBus885816_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014100_consumption`  
  Load '44_LVBus014100_consumption' has phase imbalance of 258.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014147_consumption`  
  Load '44_LVBus014147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013906_consumption`  
  Load '44_LVBus013906_consumption' has phase imbalance of 239.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013902_consumption`  
  Load '44_LVBus013902_consumption' has phase imbalance of 28.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014177_consumption`  
  Load '44_LVBus014177_consumption' has phase imbalance of 123.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013955_consumption`  
  Load '44_LVBus013955_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013909_consumption`  
  Load '44_LVBus013909_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014094_consumption`  
  Load '44_LVBus014094_consumption' has phase imbalance of 207.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858627_consumption`  
  Load '44_LVBus858627_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014130_consumption`  
  Load '44_LVBus014130_consumption' has phase imbalance of 265.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013918_consumption`  
  Load '44_LVBus013918_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014024_consumption`  
  Load '44_LVBus014024_consumption' has phase imbalance of 58.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014092_consumption`  
  Load '44_LVBus014092_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014076_consumption`  
  Load '44_LVBus014076_consumption' has phase imbalance of 255.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014009_consumption`  
  Load '44_LVBus014009_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014017_consumption`  
  Load '44_LVBus014017_consumption' has phase imbalance of 97.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus869562_consumption`  
  Load '44_LVBus869562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014144_consumption`  
  Load '44_LVBus014144_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014041_consumption`  
  Load '44_LVBus014041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014018_consumption`  
  Load '44_LVBus014018_consumption' has phase imbalance of 95.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013976_consumption`  
  Load '44_LVBus013976_consumption' has phase imbalance of 122.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014178_consumption`  
  Load '44_LVBus014178_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013905_consumption`  
  Load '44_LVBus013905_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus859440_consumption`  
  Load '44_LVBus859440_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014001_consumption`  
  Load '44_LVBus014001_consumption' has phase imbalance of 40.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014086_consumption`  
  Load '44_LVBus014086_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014083_consumption`  
  Load '44_LVBus014083_consumption' has phase imbalance of 97.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884282_consumption`  
  Load '44_LVBus884282_consumption' has phase imbalance of 38.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus859443_consumption`  
  Load '44_LVBus859443_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014114_consumption`  
  Load '44_LVBus014114_consumption' has phase imbalance of 273.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus859438_consumption`  
  Load '44_LVBus859438_consumption' has phase imbalance of 225.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014037_consumption`  
  Load '44_LVBus014037_consumption' has phase imbalance of 97.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014047_consumption`  
  Load '44_LVBus014047_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013896_consumption`  
  Load '44_LVBus013896_consumption' has phase imbalance of 121.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013894_consumption`  
  Load '44_LVBus013894_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013988_consumption`  
  Load '44_LVBus013988_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014022_consumption`  
  Load '44_LVBus014022_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014103_consumption`  
  Load '44_LVBus014103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013926_consumption`  
  Load '44_LVBus013926_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013953_consumption`  
  Load '44_LVBus013953_consumption' has phase imbalance of 54.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014056_consumption`  
  Load '44_LVBus014056_consumption' has phase imbalance of 147.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013922_consumption`  
  Load '44_LVBus013922_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013991_consumption`  
  Load '44_LVBus013991_consumption' has phase imbalance of 51.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013935_consumption`  
  Load '44_LVBus013935_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014015_consumption`  
  Load '44_LVBus014015_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014060_consumption`  
  Load '44_LVBus014060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013961_consumption`  
  Load '44_LVBus013961_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus854060_consumption`  
  Load '44_LVBus854060_consumption' has phase imbalance of 125.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886253_consumption`  
  Load '44_LVBus886253_consumption' has phase imbalance of 156.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014116_consumption`  
  Load '44_LVBus014116_consumption' has phase imbalance of 209.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013966_consumption`  
  Load '44_LVBus013966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus857104_consumption`  
  Load '44_LVBus857104_consumption' has phase imbalance of 200.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014000_consumption`  
  Load '44_LVBus014000_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013949_consumption`  
  Load '44_LVBus013949_consumption' has phase imbalance of 57.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014012_consumption`  
  Load '44_LVBus014012_consumption' has phase imbalance of 26.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus855176_consumption`  
  Load '44_LVBus855176_consumption' has phase imbalance of 76.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014050_consumption`  
  Load '44_LVBus014050_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014033_consumption`  
  Load '44_LVBus014033_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014134_consumption`  
  Load '44_LVBus014134_consumption' has phase imbalance of 79.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014003_consumption`  
  Load '44_LVBus014003_consumption' has phase imbalance of 53.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014171_consumption`  
  Load '44_LVBus014171_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884879_consumption`  
  Load '44_LVBus884879_consumption' has phase imbalance of 260.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014164_consumption`  
  Load '44_LVBus014164_consumption' has phase imbalance of 112.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014026_consumption`  
  Load '44_LVBus014026_consumption' has phase imbalance of 118.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014124_consumption`  
  Load '44_LVBus014124_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013987_consumption`  
  Load '44_LVBus013987_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014176_consumption`  
  Load '44_LVBus014176_consumption' has phase imbalance of 82.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus853975_consumption`  
  Load '44_LVBus853975_consumption' has phase imbalance of 238.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886254_consumption`  
  Load '44_LVBus886254_consumption' has phase imbalance of 81.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus859276_consumption`  
  Load '44_LVBus859276_consumption' has phase imbalance of 61.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013920_consumption`  
  Load '44_LVBus013920_consumption' has phase imbalance of 23.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus884875_consumption`  
  Load '44_LVBus884875_consumption' has phase imbalance of 75.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014045_consumption`  
  Load '44_LVBus014045_consumption' has phase imbalance of 86.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014167_consumption`  
  Load '44_LVBus014167_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus852805_consumption`  
  Load '44_LVBus852805_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014108_consumption`  
  Load '44_LVBus014108_consumption' has phase imbalance of 77.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013932_consumption`  
  Load '44_LVBus013932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus886257_consumption`  
  Load '44_LVBus886257_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014155_consumption`  
  Load '44_LVBus014155_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus014007_consumption`  
  Load '44_LVBus014007_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus853816_consumption`  
  Load '44_LVBus853816_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus857105_consumption`  
  Load '44_LVBus857105_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus013990_consumption`  
  Load '44_LVBus013990_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 644 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_SSHUB' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus014039' (LV, 0.24 kV) has an electrical reach of 4.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus014074' (LV, 0.24 kV) has an electrical reach of 16.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  380 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  107 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 44_LVBus013903_consumption, 44_LVBus013905_consumption, 44_LVBus013906_consumption, 44_LVBus013908_consumption, 44_LVBus013926_consumption, 44_LVBus013929_consumption, 44_LVBus013932_consumption, 44_LVBus013935_consumption, 44_LVBus013945_consumption, 44_LVBus013952_consumption, 44_LVBus013955_consumption, 44_LVBus013961_consumption, 44_LVBus013964_consumption, 44_LVBus013966_consumption, 44_LVBus013968_consumption, 44_LVBus013973_consumption, 44_LVBus013975_consumption, 44_LVBus013977_consumption, 44_LVBus013979_consumption, 44_LVBus013980_consumption, 44_LVBus013981_consumption, 44_LVBus013982_consumption, 44_LVBus013983_consumption, 44_LVBus013989_consumption, 44_LVBus013990_consumption, 44_LVBus013993_consumption, 44_LVBus013994_consumption, 44_LVBus013996_consumption, 44_LVBus013998_consumption, 44_LVBus013999_consumption, 44_LVBus014007_consumption, 44_LVBus014013_consumption, 44_LVBus014015_consumption, 44_LVBus014027_consumption, 44_LVBus014028_consumption, 44_LVBus014032_consumption, 44_LVBus014033_consumption, 44_LVBus014035_consumption, 44_LVBus014039_consumption, 44_LVBus014041_consumption, 44_LVBus014042_consumption, 44_LVBus014044_consumption, 44_LVBus014048_consumption, 44_LVBus014053_consumption, 44_LVBus014059_consumption, 44_LVBus014060_consumption, 44_LVBus014064_consumption, 44_LVBus014068_consumption, 44_LVBus014071_consumption, 44_LVBus014074_consumption, 44_LVBus014076_consumption, 44_LVBus014080_consumption, 44_LVBus014081_consumption, 44_LVBus014082_consumption, 44_LVBus014084_consumption, 44_LVBus014089_consumption, 44_LVBus014100_consumption, 44_LVBus014103_consumption, 44_LVBus014104_consumption, 44_LVBus014107_consumption, 44_LVBus014109_consumption, 44_LVBus014110_consumption, 44_LVBus014111_consumption, 44_LVBus014113_consumption, 44_LVBus014114_consumption, 44_LVBus014115_consumption, 44_LVBus014116_consumption, 44_LVBus014118_consumption, 44_LVBus014119_consumption, 44_LVBus014120_consumption, 44_LVBus014121_consumption, 44_LVBus014128_consumption, 44_LVBus014130_consumption, 44_LVBus014139_consumption, 44_LVBus014147_consumption, 44_LVBus014153_consumption, 44_LVBus014155_consumption, 44_LVBus014156_consumption, 44_LVBus014168_consumption, 44_LVBus014171_consumption, 44_LVBus852926_consumption, 44_LVBus853815_consumption, 44_LVBus853817_consumption, 44_LVBus853819_consumption, 44_LVBus856576_consumption, 44_LVBus857104_consumption, 44_LVBus857106_consumption, 44_LVBus858626_consumption, 44_LVBus858627_consumption, 44_LVBus859438_consumption, 44_LVBus859440_consumption, 44_LVBus859443_consumption, 44_LVBus860936_consumption, 44_LVBus860955_consumption, 44_LVBus869562_consumption, 44_LVBus875766_consumption, 44_LVBus884872_consumption, 44_LVBus884873_consumption, 44_LVBus884876_consumption, 44_LVBus884877_consumption, 44_LVBus884878_consumption, 44_LVBus884879_consumption, 44_LVBus885816_consumption, 44_LVBus886252_consumption, 44_LVBus886253_consumption, 44_LVBus886257_consumption, 44_LVBus886258_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  322 group(s) of loads (644 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  7 group(s) of series lines (14 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  393 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus013894_production, 44_LVBus013895_production, 44_LVBus013896_production, 44_LVBus013897_production, 44_LVBus013899_production, 44_LVBus013901_production, 44_LVBus013902_production, 44_LVBus013903_production, 44_LVBus013904_production, 44_LVBus013905_production, 44_LVBus013906_production, 44_LVBus013908_production, 44_LVBus013909_production, 44_LVBus013911_production, 44_LVBus013912_production, 44_LVBus013913_consumption, 44_LVBus013913_production, 44_LVBus013915_production, 44_LVBus013916_production, 44_LVBus013917_production, 44_LVBus013918_production, 44_LVBus013919_consumption, 44_LVBus013919_production, 44_LVBus013920_production, 44_LVBus013921_production, 44_LVBus013922_production, 44_LVBus013923_production, 44_LVBus013925_production, 44_LVBus013926_production, 44_LVBus013927_consumption, 44_LVBus013927_production, 44_LVBus013928_consumption, 44_LVBus013928_production, 44_LVBus013929_production, 44_LVBus013930_consumption, 44_LVBus013930_production, 44_LVBus013931_consumption, 44_LVBus013931_production, 44_LVBus013932_production, 44_LVBus013933_consumption, 44_LVBus013933_production, 44_LVBus013934_production, 44_LVBus013935_production, 44_LVBus013937_production, 44_LVBus013939_production, 44_LVBus013941_consumption, 44_LVBus013941_production, 44_LVBus013943_production, 44_LVBus013945_production, 44_LVBus013947_production, 44_LVBus013949_production, 44_LVBus013951_consumption, 44_LVBus013951_production, 44_LVBus013952_production, 44_LVBus013953_production, 44_LVBus013954_production, 44_LVBus013955_production, 44_LVBus013956_consumption, 44_LVBus013956_production, 44_LVBus013958_consumption, 44_LVBus013958_production, 44_LVBus013959_production, 44_LVBus013960_production, 44_LVBus013961_production, 44_LVBus013963_consumption, 44_LVBus013963_production, 44_LVBus013964_production, 44_LVBus013966_production, 44_LVBus013967_production, 44_LVBus013968_production, 44_LVBus013970_production, 44_LVBus013972_consumption, 44_LVBus013972_production, 44_LVBus013973_production, 44_LVBus013975_production, 44_LVBus013976_production, 44_LVBus013977_production, 44_LVBus013978_consumption, 44_LVBus013978_production, 44_LVBus013979_production, 44_LVBus013980_production, 44_LVBus013981_production, 44_LVBus013982_production, 44_LVBus013983_production, 44_LVBus013984_consumption, 44_LVBus013984_production, 44_LVBus013986_production, 44_LVBus013987_production, 44_LVBus013988_production, 44_LVBus013989_production, 44_LVBus013990_production, 44_LVBus013991_production, 44_LVBus013993_production, 44_LVBus013994_production, 44_LVBus013995_production, 44_LVBus013996_production, 44_LVBus013997_consumption, 44_LVBus013997_production, 44_LVBus013998_production, 44_LVBus013999_production, 44_LVBus014000_production, 44_LVBus014001_production, 44_LVBus014002_consumption, 44_LVBus014002_production, 44_LVBus014003_production, 44_LVBus014004_consumption, 44_LVBus014004_production, 44_LVBus014005_production, 44_LVBus014006_production, 44_LVBus014007_production, 44_LVBus014008_production, 44_LVBus014009_production, 44_LVBus014011_consumption, 44_LVBus014011_production, 44_LVBus014012_production, 44_LVBus014013_production, 44_LVBus014014_production, 44_LVBus014015_production, 44_LVBus014017_production, 44_LVBus014018_production, 44_LVBus014019_production, 44_LVBus014020_production, 44_LVBus014022_production, 44_LVBus014023_production, 44_LVBus014024_production, 44_LVBus014026_production, 44_LVBus014027_production, 44_LVBus014028_production, 44_LVBus014029_production, 44_LVBus014031_production, 44_LVBus014032_production, 44_LVBus014033_production, 44_LVBus014035_production, 44_LVBus014036_production, 44_LVBus014037_production, 44_LVBus014039_production, 44_LVBus014041_production, 44_LVBus014042_production, 44_LVBus014044_production, 44_LVBus014045_production, 44_LVBus014046_production, 44_LVBus014047_production, 44_LVBus014048_production, 44_LVBus014049_production, 44_LVBus014050_production, 44_LVBus014051_production, 44_LVBus014053_production, 44_LVBus014054_production, 44_LVBus014055_production, 44_LVBus014056_production, 44_LVBus014058_production, 44_LVBus014059_production, 44_LVBus014060_production, 44_LVBus014061_consumption, 44_LVBus014061_production, 44_LVBus014063_consumption, 44_LVBus014063_production, 44_LVBus014064_production, 44_LVBus014065_consumption, 44_LVBus014065_production, 44_LVBus014066_production, 44_LVBus014067_production, 44_LVBus014068_production, 44_LVBus014069_production, 44_LVBus014071_production, 44_LVBus014072_production, 44_LVBus014074_production, 44_LVBus014076_production, 44_LVBus014077_consumption, 44_LVBus014077_production, 44_LVBus014078_production, 44_LVBus014080_production, 44_LVBus014081_production, 44_LVBus014082_production, 44_LVBus014083_production, 44_LVBus014084_production, 44_LVBus014085_production, 44_LVBus014086_production, 44_LVBus014087_production, 44_LVBus014088_production, 44_LVBus014089_production, 44_LVBus014090_production, 44_LVBus014092_production, 44_LVBus014093_production, 44_LVBus014094_production, 44_LVBus014096_production, 44_LVBus014098_consumption, 44_LVBus014098_production, 44_LVBus014100_production, 44_LVBus014101_production, 44_LVBus014102_production, 44_LVBus014103_production, 44_LVBus014104_production, 44_LVBus014106_consumption, 44_LVBus014106_production, 44_LVBus014107_production, 44_LVBus014108_production, 44_LVBus014109_production, 44_LVBus014110_production, 44_LVBus014111_production, 44_LVBus014112_production, 44_LVBus014113_production, 44_LVBus014114_production, 44_LVBus014115_production, 44_LVBus014116_production, 44_LVBus014117_production, 44_LVBus014118_production, 44_LVBus014119_production, 44_LVBus014120_production, 44_LVBus014121_production, 44_LVBus014122_production, 44_LVBus014123_consumption, 44_LVBus014123_production, 44_LVBus014124_production, 44_LVBus014125_production, 44_LVBus014127_consumption, 44_LVBus014127_production, 44_LVBus014128_production, 44_LVBus014129_production, 44_LVBus014130_production, 44_LVBus014131_consumption, 44_LVBus014131_production, 44_LVBus014132_consumption, 44_LVBus014132_production, 44_LVBus014133_production, 44_LVBus014134_production, 44_LVBus014135_production, 44_LVBus014136_production, 44_LVBus014138_consumption, 44_LVBus014138_production, 44_LVBus014139_production, 44_LVBus014140_consumption, 44_LVBus014140_production, 44_LVBus014141_consumption, 44_LVBus014141_production, 44_LVBus014142_production, 44_LVBus014143_production, 44_LVBus014144_production, 44_LVBus014145_consumption, 44_LVBus014145_production, 44_LVBus014146_production, 44_LVBus014147_production, 44_LVBus014149_consumption, 44_LVBus014149_production, 44_LVBus014150_consumption, 44_LVBus014150_production, 44_LVBus014151_production, 44_LVBus014153_production, 44_LVBus014155_production, 44_LVBus014156_production, 44_LVBus014157_consumption, 44_LVBus014157_production, 44_LVBus014158_production, 44_LVBus014160_consumption, 44_LVBus014160_production, 44_LVBus014161_consumption, 44_LVBus014161_production, 44_LVBus014162_production, 44_LVBus014163_production, 44_LVBus014164_production, 44_LVBus014165_consumption, 44_LVBus014165_production, 44_LVBus014166_production, 44_LVBus014167_production, 44_LVBus014168_production, 44_LVBus014169_production, 44_LVBus014170_production, 44_LVBus014171_production, 44_LVBus014173_consumption, 44_LVBus014173_production, 44_LVBus014175_consumption, 44_LVBus014175_production, 44_LVBus014176_production, 44_LVBus014177_production, 44_LVBus014178_production, 44_LVBus014180_consumption, 44_LVBus014180_production, 44_LVBus014181_consumption, 44_LVBus014181_production, 44_LVBus014182_consumption, 44_LVBus014182_production, 44_LVBus014183_production, 44_LVBus014184_consumption, 44_LVBus014184_production, 44_LVBus014185_consumption, 44_LVBus014185_production, 44_LVBus014187_consumption, 44_LVBus014187_production, 44_LVBus014188_consumption, 44_LVBus014188_production, 44_LVBus014189_consumption, 44_LVBus014189_production, 44_LVBus014190_consumption, 44_LVBus014190_production, 44_LVBus014191_consumption, 44_LVBus014191_production, 44_LVBus014193_consumption, 44_LVBus014193_production, 44_LVBus852805_production, 44_LVBus852926_production, 44_LVBus853815_production, 44_LVBus853816_production, 44_LVBus853817_production, 44_LVBus853818_production, 44_LVBus853819_production, 44_LVBus853975_production, 44_LVBus854060_production, 44_LVBus855176_production, 44_LVBus856576_production, 44_LVBus856577_production, 44_LVBus857104_production, 44_LVBus857105_production, 44_LVBus857106_production, 44_LVBus857314_production, 44_LVBus858579_production, 44_LVBus858580_production, 44_LVBus858626_production, 44_LVBus858627_production, 44_LVBus858628_production, 44_LVBus858629_consumption, 44_LVBus858629_production, 44_LVBus858630_consumption, 44_LVBus858630_production, 44_LVBus859276_production, 44_LVBus859437_consumption, 44_LVBus859437_production, 44_LVBus859438_production, 44_LVBus859439_production, 44_LVBus859440_production, 44_LVBus859441_production, 44_LVBus859442_production, 44_LVBus859443_production, 44_LVBus860439_production, 44_LVBus860936_production, 44_LVBus860955_production, 44_LVBus863227_consumption, 44_LVBus863227_production, 44_LVBus863228_consumption, 44_LVBus863228_production, 44_LVBus863229_consumption, 44_LVBus863229_production, 44_LVBus863230_consumption, 44_LVBus863230_production, 44_LVBus866557_consumption, 44_LVBus866557_production, 44_LVBus868417_production, 44_LVBus868418_production, 44_LVBus869561_consumption, 44_LVBus869561_production, 44_LVBus869562_production, 44_LVBus875764_consumption, 44_LVBus875764_production, 44_LVBus875765_consumption, 44_LVBus875765_production, 44_LVBus875766_production, 44_LVBus882006_consumption, 44_LVBus882006_production, 44_LVBus884282_production, 44_LVBus884870_production, 44_LVBus884871_production, 44_LVBus884872_production, 44_LVBus884873_production, 44_LVBus884874_production, 44_LVBus884875_production, 44_LVBus884876_production, 44_LVBus884877_production, 44_LVBus884878_production, 44_LVBus884879_production, 44_LVBus885815_production, 44_LVBus885816_production, 44_LVBus886252_production, 44_LVBus886253_production, 44_LVBus886254_production, 44_LVBus886255_production, 44_LVBus886256_production, 44_LVBus886257_production, 44_LVBus886258_production, 44_LVBus886259_production, 44_MVLV04851_consumption, 44_MVLV04851_production, 44_MVLV11824_production, 44_MVLV18898_consumption, 44_MVLV18898_production, 44_MVLV27041_consumption, 44_MVLV27041_production, 44_MVLV29370_consumption, 44_MVLV29370_production, 44_MVLV39460_consumption, 44_MVLV39460_production, 44_MVLV57351_consumption, 44_MVLV57351_production, 44_MVLV64443_consumption, 44_MVLV64443_production.

