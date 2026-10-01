# BMOPF Network Summary: 32_MVFeeder1627

**Generated:** 2026-10-01 23:34:07  
**Findings:** 0 errors · 5 warnings · 338 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 498 |  |
| line | 484 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 940 | 1.825 MW, 547.4 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 13 |  |
| switch | 0 |  |
| transformer | 13 | Dyn11×13 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 17 | 16 | 4 | 0 |
| LV_236V | 236.0 V | 481 | 468 | 936 | 0 |

**Transformer transitions:**

- `32_MVLV29403_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV35466_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV36953_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV53066_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV27112_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV36149_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV38953_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV75023_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV12446_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV66271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV22035_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV23977_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV62915_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 10 |
| Degree-1 buses | 174 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 498 | 1 | 497 | 0 | 0 | 0 |
| Tier LV_236V | 481 | 13 | 468 | 0 | 0 | 0 |
| Tier MV_11.8kV | 17 | 1 | 16 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 13; skipped invalid branches: 0.

Galvanic zones: 14; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_HANNA | MV_11.8kV | 17 | 0 | 0 | 13 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1975 declared bus terminals; 1920 mapped line/closed-switch conductor edges; 55 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 26400.0 | 2.937 | 2820 |
| q_nom | 0.0 | 7920.0 | 2.937 | 2820 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.06 | 1270.0 | 1.592 | 484 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.607 | 13 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 593 of 940 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373592_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373850_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373772_consumption' has phase imbalance of 135.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373622_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1166133_consumption' has phase imbalance of 83.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373676_consumption' has phase imbalance of 269.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373520_consumption' has phase imbalance of 86.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373812_consumption' has phase imbalance of 131.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373505_consumption' has phase imbalance of 176.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373618_consumption' has phase imbalance of 61.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373661_consumption' has phase imbalance of 135.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373420_consumption' has phase imbalance of 203.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110903_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373641_consumption' has phase imbalance of 241.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373607_consumption' has phase imbalance of 51.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1166129_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373412_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373401_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373574_consumption' has phase imbalance of 140.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373851_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373730_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373391_consumption' has phase imbalance of 223.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373698_consumption' has phase imbalance of 63.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373454_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373696_consumption' has phase imbalance of 204.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373808_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373613_consumption' has phase imbalance of 221.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373410_consumption' has phase imbalance of 74.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373616_consumption' has phase imbalance of 92.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373827_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373738_consumption' has phase imbalance of 201.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373385_consumption' has phase imbalance of 191.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373621_consumption' has phase imbalance of 93.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373848_consumption' has phase imbalance of 120.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373724_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373416_consumption' has phase imbalance of 187.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1166130_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1176221_consumption' has phase imbalance of 173.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373678_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373790_consumption' has phase imbalance of 126.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373488_consumption' has phase imbalance of 94.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373593_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373640_consumption' has phase imbalance of 27.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373819_consumption' has phase imbalance of 104.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373700_consumption' has phase imbalance of 118.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373490_consumption' has phase imbalance of 100.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373620_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373585_consumption' has phase imbalance of 194.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373394_consumption' has phase imbalance of 134.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373940_consumption' has phase imbalance of 98.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373393_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373529_consumption' has phase imbalance of 37.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373578_consumption' has phase imbalance of 171.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373606_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373491_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373729_consumption' has phase imbalance of 104.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373609_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373658_consumption' has phase imbalance of 137.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373519_consumption' has phase imbalance of 104.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1159484_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373798_consumption' has phase imbalance of 69.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1176223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373941_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373513_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373766_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373477_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373926_consumption' has phase imbalance of 227.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373688_consumption' has phase imbalance of 201.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373697_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373619_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373573_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373644_consumption' has phase imbalance of 172.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373496_consumption' has phase imbalance of 207.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373747_consumption' has phase imbalance of 258.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373605_consumption' has phase imbalance of 131.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373682_consumption' has phase imbalance of 104.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373422_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373936_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373647_consumption' has phase imbalance of 174.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373833_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373567_consumption' has phase imbalance of 42.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373517_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373579_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373913_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373825_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373430_consumption' has phase imbalance of 135.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373818_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373668_consumption' has phase imbalance of 267.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373414_consumption' has phase imbalance of 246.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373594_consumption' has phase imbalance of 78.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373846_consumption' has phase imbalance of 68.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373831_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373934_consumption' has phase imbalance of 24.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373637_consumption' has phase imbalance of 220.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1142555_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373836_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373832_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373824_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373489_consumption' has phase imbalance of 88.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373583_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373945_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1180552_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373656_consumption' has phase imbalance of 294.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373814_consumption' has phase imbalance of 40.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373596_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373558_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373922_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1128681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373780_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373472_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373645_consumption' has phase imbalance of 42.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373917_consumption' has phase imbalance of 264.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373745_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373770_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1159485_consumption' has phase imbalance of 165.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373581_consumption' has phase imbalance of 33.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373800_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373675_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373815_consumption' has phase imbalance of 176.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373544_consumption' has phase imbalance of 42.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373534_consumption' has phase imbalance of 54.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373672_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373746_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373743_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373643_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373813_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1180553_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373920_consumption' has phase imbalance of 276.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1176224_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373522_consumption' has phase imbalance of 210.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373382_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373576_consumption' has phase imbalance of 142.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373796_consumption' has phase imbalance of 248.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373671_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373509_consumption' has phase imbalance of 112.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373392_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373650_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373810_consumption' has phase imbalance of 206.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373638_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373501_consumption' has phase imbalance of 179.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1128680_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373510_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373475_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110907_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373801_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373837_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373797_consumption' has phase imbalance of 89.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373679_consumption' has phase imbalance of 67.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373767_consumption' has phase imbalance of 170.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373794_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373533_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373478_consumption' has phase imbalance of 113.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373702_consumption' has phase imbalance of 67.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373692_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373739_consumption' has phase imbalance of 240.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373429_consumption' has phase imbalance of 49.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110905_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373474_consumption' has phase imbalance of 108.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373785_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373406_consumption' has phase imbalance of 29.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373553_consumption' has phase imbalance of 45.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373737_consumption' has phase imbalance of 137.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373802_consumption' has phase imbalance of 257.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373646_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373631_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373396_consumption' has phase imbalance of 121.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373628_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1142554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373636_consumption' has phase imbalance of 36.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373610_consumption' has phase imbalance of 109.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373944_consumption' has phase imbalance of 215.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373536_consumption' has phase imbalance of 71.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373524_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373669_consumption' has phase imbalance of 264.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373704_consumption' has phase imbalance of 65.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373543_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373587_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373736_consumption' has phase imbalance of 243.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373580_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373847_consumption' has phase imbalance of 82.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373829_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373778_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373705_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373663_consumption' has phase imbalance of 86.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373855_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373508_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373817_consumption' has phase imbalance of 159.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373717_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373757_consumption' has phase imbalance of 52.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373648_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373795_consumption' has phase imbalance of 155.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373624_consumption' has phase imbalance of 68.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373559_consumption' has phase imbalance of 68.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373612_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1128683_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373407_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373602_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373942_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373838_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373783_consumption' has phase imbalance of 187.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373400_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373532_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373843_consumption' has phase imbalance of 228.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373635_consumption' has phase imbalance of 230.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373765_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373674_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373390_consumption' has phase imbalance of 182.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373575_consumption' has phase imbalance of 247.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373653_consumption' has phase imbalance of 194.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373473_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373601_consumption' has phase imbalance of 23.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373415_consumption' has phase imbalance of 234.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373502_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373946_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373673_consumption' has phase imbalance of 43.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373614_consumption' has phase imbalance of 75.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373823_consumption' has phase imbalance of 200.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373844_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373598_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373512_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1142552_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1184320_consumption' has phase imbalance of 76.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373424_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373516_consumption' has phase imbalance of 91.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373486_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373651_consumption' has phase imbalance of 55.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1125442_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110906_consumption' has phase imbalance of 130.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373597_consumption' has phase imbalance of 39.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373803_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373604_consumption' has phase imbalance of 158.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373591_consumption' has phase imbalance of 152.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373497_consumption' has phase imbalance of 172.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373639_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373423_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373839_consumption' has phase imbalance of 20.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373514_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373405_consumption' has phase imbalance of 86.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373744_consumption' has phase imbalance of 85.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373518_consumption' has phase imbalance of 228.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373840_consumption' has phase imbalance of 143.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373921_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373384_consumption' has phase imbalance of 59.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373784_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373535_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373649_consumption' has phase imbalance of 89.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373408_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373588_consumption' has phase imbalance of 251.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373938_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373854_consumption' has phase imbalance of 81.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373821_consumption' has phase imbalance of 88.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1166132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110904_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373680_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus373805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 940 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.825 MW |
| Total load Q | 547.4 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV29403_Transformer | 176.0 kVA | 88.4% |
| 32_MVLV35466_Transformer | 693.0 kVA | 33.6% |
| 32_MVLV36953_Transformer | 275.0 kVA | 23.4% |
| 32_MVLV53066_Transformer | 110.0 kVA | 10.2% |
| 32_MVLV27112_Transformer | 440.0 kVA | 27.0% |
| 32_MVLV36149_Transformer | 440.0 kVA | 34.9% |
| 32_MVLV38953_Transformer | 1.1 MVA | 24.9% |
| 32_MVLV75023_Transformer | 440.0 kVA | 33.2% |
| 32_MVLV12446_Transformer | 693.0 kVA | 19.3% |
| 32_MVLV66271_Transformer | 440.0 kVA | 52.2% |
| 32_MVLV22035_Transformer | 176.0 kVA | 16.1% |
| 32_MVLV23977_Transformer | 275.0 kVA | 44.5% |
| 32_MVLV62915_Transformer | 693.0 kVA | 33.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.82 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '32_LVBus1128679' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 498 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 498 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 17 |
| LV_236V | 4-wire | 481 / 481 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 481 |
| Neutral branches | 468 |
| Grounding points | 13 |
| Neutral sections | 13 |
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
| 11.78 kV | 17 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 53 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 73 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 66 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 45 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 45 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 14 |
| Islands without voltage reference | 0 |
| Line impedance spread | 263.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 481 / 17 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 594 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 594 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1110903_production, 32_LVBus1110904_production, 32_LVBus1110905_production, 32_LVBus1110906_production, 32_LVBus1110907_production, 32_LVBus1110908_production, 32_LVBus1110909_production, 32_LVBus1125442_production, 32_LVBus1128679_consumption, 32_LVBus1128679_production, 32_LVBus1128680_production, 32_LVBus1128681_production, 32_LVBus1128682_production, 32_LVBus1128683_production, 32_LVBus1142549_consumption, 32_LVBus1142549_production, 32_LVBus1142550_consumption, 32_LVBus1142550_production, 32_LVBus1142551_consumption, 32_LVBus1142551_production, 32_LVBus1142552_production, 32_LVBus1142553_consumption, 32_LVBus1142553_production, 32_LVBus1142554_production, 32_LVBus1142555_production, 32_LVBus1159484_production, 32_LVBus1159485_production, 32_LVBus1166129_production, 32_LVBus1166130_production, 32_LVBus1166131_consumption, 32_LVBus1166131_production, 32_LVBus1166132_production, 32_LVBus1166133_production, 32_LVBus1176221_production, 32_LVBus1176222_production, 32_LVBus1176223_production, 32_LVBus1176224_production, 32_LVBus1180552_production, 32_LVBus1180553_production, 32_LVBus1184320_production, 32_LVBus373382_production, 32_LVBus373384_production, 32_LVBus373385_production, 32_LVBus373386_production, 32_LVBus373387_production, 32_LVBus373388_consumption, 32_LVBus373388_production, 32_LVBus373390_production, 32_LVBus373391_production, 32_LVBus373392_production, 32_LVBus373393_production, 32_LVBus373394_production, 32_LVBus373396_production, 32_LVBus373397_production, 32_LVBus373398_consumption, 32_LVBus373398_production, 32_LVBus373400_production, 32_LVBus373401_production, 32_LVBus373402_consumption, 32_LVBus373402_production, 32_LVBus373403_production, 32_LVBus373404_consumption, 32_LVBus373404_production, 32_LVBus373405_production, 32_LVBus373406_production, 32_LVBus373407_production, 32_LVBus373408_production, 32_LVBus373409_production, 32_LVBus373410_production, 32_LVBus373411_consumption, 32_LVBus373411_production, 32_LVBus373412_production, 32_LVBus373413_consumption, 32_LVBus373413_production, 32_LVBus373414_production, 32_LVBus373415_production, 32_LVBus373416_production, 32_LVBus373418_consumption, 32_LVBus373418_production, 32_LVBus373419_production, 32_LVBus373420_production, 32_LVBus373421_consumption, 32_LVBus373421_production, 32_LVBus373422_production, 32_LVBus373423_production, 32_LVBus373424_production, 32_LVBus373425_production, 32_LVBus373427_consumption, 32_LVBus373427_production, 32_LVBus373428_production, 32_LVBus373429_production, 32_LVBus373430_production, 32_LVBus373432_production, 32_LVBus373434_consumption, 32_LVBus373434_production, 32_LVBus373435_consumption, 32_LVBus373435_production, 32_LVBus373437_consumption, 32_LVBus373437_production, 32_LVBus373438_consumption, 32_LVBus373438_production, 32_LVBus373439_consumption, 32_LVBus373439_production, 32_LVBus373441_consumption, 32_LVBus373441_production, 32_LVBus373442_consumption, 32_LVBus373442_production, 32_LVBus373443_production, 32_LVBus373445_consumption, 32_LVBus373445_production, 32_LVBus373446_consumption, 32_LVBus373446_production, 32_LVBus373447_consumption, 32_LVBus373447_production, 32_LVBus373448_consumption, 32_LVBus373448_production, 32_LVBus373450_consumption, 32_LVBus373450_production, 32_LVBus373451_consumption, 32_LVBus373451_production, 32_LVBus373452_consumption, 32_LVBus373452_production, 32_LVBus373454_production, 32_LVBus373455_consumption, 32_LVBus373455_production, 32_LVBus373456_consumption, 32_LVBus373456_production, 32_LVBus373457_production, 32_LVBus373459_consumption, 32_LVBus373459_production, 32_LVBus373460_consumption, 32_LVBus373460_production, 32_LVBus373462_consumption, 32_LVBus373462_production, 32_LVBus373463_consumption, 32_LVBus373463_production, 32_LVBus373465_consumption, 32_LVBus373465_production, 32_LVBus373466_consumption, 32_LVBus373466_production, 32_LVBus373467_consumption, 32_LVBus373467_production, 32_LVBus373472_production, 32_LVBus373473_production, 32_LVBus373474_production, 32_LVBus373475_production, 32_LVBus373476_production, 32_LVBus373477_production, 32_LVBus373478_production, 32_LVBus373479_consumption, 32_LVBus373479_production, 32_LVBus373480_consumption, 32_LVBus373480_production, 32_LVBus373481_consumption, 32_LVBus373481_production, 32_LVBus373482_consumption, 32_LVBus373482_production, 32_LVBus373483_consumption, 32_LVBus373483_production, 32_LVBus373484_consumption, 32_LVBus373484_production, 32_LVBus373485_production, 32_LVBus373486_production, 32_LVBus373487_production, 32_LVBus373488_production, 32_LVBus373489_production, 32_LVBus373490_production, 32_LVBus373491_production, 32_LVBus373493_production, 32_LVBus373495_consumption, 32_LVBus373495_production, 32_LVBus373496_production, 32_LVBus373497_production, 32_LVBus373498_production, 32_LVBus373499_production, 32_LVBus373500_production, 32_LVBus373501_production, 32_LVBus373502_production, 32_LVBus373503_consumption, 32_LVBus373503_production, 32_LVBus373504_consumption, 32_LVBus373504_production, 32_LVBus373505_production, 32_LVBus373506_consumption, 32_LVBus373506_production, 32_LVBus373507_consumption, 32_LVBus373507_production, 32_LVBus373508_production, 32_LVBus373509_production, 32_LVBus373510_production, 32_LVBus373512_production, 32_LVBus373513_production, 32_LVBus373514_production, 32_LVBus373515_production, 32_LVBus373516_production, 32_LVBus373517_production, 32_LVBus373518_production, 32_LVBus373519_production, 32_LVBus373520_production, 32_LVBus373521_production, 32_LVBus373522_production, 32_LVBus373523_consumption, 32_LVBus373523_production, 32_LVBus373524_production, 32_LVBus373525_production, 32_LVBus373527_consumption, 32_LVBus373527_production, 32_LVBus373528_consumption, 32_LVBus373528_production, 32_LVBus373529_production, 32_LVBus373530_production, 32_LVBus373531_production, 32_LVBus373532_production, 32_LVBus373533_production, 32_LVBus373534_production, 32_LVBus373535_production, 32_LVBus373536_production, 32_LVBus373537_production, 32_LVBus373538_consumption, 32_LVBus373538_production, 32_LVBus373539_consumption, 32_LVBus373539_production, 32_LVBus373540_consumption, 32_LVBus373540_production, 32_LVBus373542_consumption, 32_LVBus373542_production, 32_LVBus373543_production, 32_LVBus373544_production, 32_LVBus373546_consumption, 32_LVBus373546_production, 32_LVBus373547_consumption, 32_LVBus373547_production, 32_LVBus373548_consumption, 32_LVBus373548_production, 32_LVBus373549_production, 32_LVBus373551_consumption, 32_LVBus373551_production, 32_LVBus373552_consumption, 32_LVBus373552_production, 32_LVBus373553_production, 32_LVBus373554_consumption, 32_LVBus373554_production, 32_LVBus373555_consumption, 32_LVBus373555_production, 32_LVBus373556_production, 32_LVBus373557_production, 32_LVBus373558_production, 32_LVBus373559_production, 32_LVBus373561_consumption, 32_LVBus373561_production, 32_LVBus373563_production, 32_LVBus373565_production, 32_LVBus373567_production, 32_LVBus373569_production, 32_LVBus373571_consumption, 32_LVBus373571_production, 32_LVBus373573_production, 32_LVBus373574_production, 32_LVBus373575_production, 32_LVBus373576_production, 32_LVBus373577_production, 32_LVBus373578_production, 32_LVBus373579_production, 32_LVBus373580_production, 32_LVBus373581_production, 32_LVBus373583_production, 32_LVBus373584_production, 32_LVBus373585_production, 32_LVBus373586_production, 32_LVBus373587_production, 32_LVBus373588_production, 32_LVBus373590_production, 32_LVBus373591_production, 32_LVBus373592_production, 32_LVBus373593_production, 32_LVBus373594_production, 32_LVBus373596_production, 32_LVBus373597_production, 32_LVBus373598_production, 32_LVBus373599_consumption, 32_LVBus373599_production, 32_LVBus373600_production, 32_LVBus373601_production, 32_LVBus373602_production, 32_LVBus373604_production, 32_LVBus373605_production, 32_LVBus373606_production, 32_LVBus373607_production, 32_LVBus373609_production, 32_LVBus373610_production, 32_LVBus373611_production, 32_LVBus373612_production, 32_LVBus373613_production, 32_LVBus373614_production, 32_LVBus373615_production, 32_LVBus373616_production, 32_LVBus373618_production, 32_LVBus373619_production, 32_LVBus373620_production, 32_LVBus373621_production, 32_LVBus373622_production, 32_LVBus373624_production, 32_LVBus373625_production, 32_LVBus373626_consumption, 32_LVBus373626_production, 32_LVBus373627_consumption, 32_LVBus373627_production, 32_LVBus373628_production, 32_LVBus373629_production, 32_LVBus373630_consumption, 32_LVBus373630_production, 32_LVBus373631_production, 32_LVBus373632_production, 32_LVBus373633_production, 32_LVBus373635_production, 32_LVBus373636_production, 32_LVBus373637_production, 32_LVBus373638_production, 32_LVBus373639_production, 32_LVBus373640_production, 32_LVBus373641_production, 32_LVBus373643_production, 32_LVBus373644_production, 32_LVBus373645_production, 32_LVBus373646_production, 32_LVBus373647_production, 32_LVBus373648_production, 32_LVBus373649_production, 32_LVBus373650_production, 32_LVBus373651_production, 32_LVBus373653_production, 32_LVBus373654_consumption, 32_LVBus373654_production, 32_LVBus373656_production, 32_LVBus373657_production, 32_LVBus373658_production, 32_LVBus373660_production, 32_LVBus373661_production, 32_LVBus373663_production, 32_LVBus373664_production, 32_LVBus373665_consumption, 32_LVBus373665_production, 32_LVBus373666_consumption, 32_LVBus373666_production, 32_LVBus373667_consumption, 32_LVBus373667_production, 32_LVBus373668_production, 32_LVBus373669_production, 32_LVBus373671_production, 32_LVBus373672_production, 32_LVBus373673_production, 32_LVBus373674_production, 32_LVBus373675_production, 32_LVBus373676_production, 32_LVBus373678_production, 32_LVBus373679_production, 32_LVBus373680_production, 32_LVBus373681_production, 32_LVBus373682_production, 32_LVBus373683_production, 32_LVBus373685_consumption, 32_LVBus373685_production, 32_LVBus373687_production, 32_LVBus373688_production, 32_LVBus373690_production, 32_LVBus373692_production, 32_LVBus373693_consumption, 32_LVBus373693_production, 32_LVBus373694_production, 32_LVBus373695_consumption, 32_LVBus373695_production, 32_LVBus373696_production, 32_LVBus373697_production, 32_LVBus373698_production, 32_LVBus373700_production, 32_LVBus373701_production, 32_LVBus373702_production, 32_LVBus373703_consumption, 32_LVBus373703_production, 32_LVBus373704_production, 32_LVBus373705_production, 32_LVBus373706_consumption, 32_LVBus373706_production, 32_LVBus373707_consumption, 32_LVBus373707_production, 32_LVBus373708_production, 32_LVBus373709_production, 32_LVBus373710_consumption, 32_LVBus373710_production, 32_LVBus373712_consumption, 32_LVBus373712_production, 32_LVBus373714_consumption, 32_LVBus373714_production, 32_LVBus373715_consumption, 32_LVBus373715_production, 32_LVBus373717_production, 32_LVBus373719_consumption, 32_LVBus373719_production, 32_LVBus373721_consumption, 32_LVBus373721_production, 32_LVBus373722_consumption, 32_LVBus373722_production, 32_LVBus373724_production, 32_LVBus373726_production, 32_LVBus373727_production, 32_LVBus373728_production, 32_LVBus373729_production, 32_LVBus373730_production, 32_LVBus373731_production, 32_LVBus373732_consumption, 32_LVBus373732_production, 32_LVBus373733_consumption, 32_LVBus373733_production, 32_LVBus373735_production, 32_LVBus373736_production, 32_LVBus373737_production, 32_LVBus373738_production, 32_LVBus373739_production, 32_LVBus373741_production, 32_LVBus373742_consumption, 32_LVBus373742_production, 32_LVBus373743_production, 32_LVBus373744_production, 32_LVBus373745_production, 32_LVBus373746_production, 32_LVBus373747_production, 32_LVBus373748_production, 32_LVBus373749_production, 32_LVBus373750_production, 32_LVBus373751_production, 32_LVBus373752_consumption, 32_LVBus373752_production, 32_LVBus373753_consumption, 32_LVBus373753_production, 32_LVBus373754_production, 32_LVBus373755_production, 32_LVBus373756_consumption, 32_LVBus373756_production, 32_LVBus373757_production, 32_LVBus373759_production, 32_LVBus373761_consumption, 32_LVBus373761_production, 32_LVBus373762_consumption, 32_LVBus373762_production, 32_LVBus373763_consumption, 32_LVBus373763_production, 32_LVBus373764_production, 32_LVBus373765_production, 32_LVBus373766_production, 32_LVBus373767_production, 32_LVBus373768_production, 32_LVBus373769_production, 32_LVBus373770_production, 32_LVBus373771_production, 32_LVBus373772_production, 32_LVBus373773_production, 32_LVBus373774_production, 32_LVBus373776_consumption, 32_LVBus373776_production, 32_LVBus373777_production, 32_LVBus373778_production, 32_LVBus373779_consumption, 32_LVBus373779_production, 32_LVBus373780_production, 32_LVBus373781_consumption, 32_LVBus373781_production, 32_LVBus373783_production, 32_LVBus373784_production, 32_LVBus373785_production, 32_LVBus373786_production, 32_LVBus373787_consumption, 32_LVBus373787_production, 32_LVBus373788_production, 32_LVBus373789_production, 32_LVBus373790_production, 32_LVBus373791_consumption, 32_LVBus373791_production, 32_LVBus373794_production, 32_LVBus373795_production, 32_LVBus373796_production, 32_LVBus373797_production, 32_LVBus373798_production, 32_LVBus373799_consumption, 32_LVBus373799_production, 32_LVBus373800_production, 32_LVBus373801_production, 32_LVBus373802_production, 32_LVBus373803_production, 32_LVBus373805_production, 32_LVBus373807_production, 32_LVBus373808_production, 32_LVBus373809_consumption, 32_LVBus373809_production, 32_LVBus373810_production, 32_LVBus373811_consumption, 32_LVBus373811_production, 32_LVBus373812_production, 32_LVBus373813_production, 32_LVBus373814_production, 32_LVBus373815_production, 32_LVBus373816_consumption, 32_LVBus373816_production, 32_LVBus373817_production, 32_LVBus373818_production, 32_LVBus373819_production, 32_LVBus373820_consumption, 32_LVBus373820_production, 32_LVBus373821_production, 32_LVBus373822_production, 32_LVBus373823_production, 32_LVBus373824_production, 32_LVBus373825_production, 32_LVBus373827_production, 32_LVBus373828_production, 32_LVBus373829_production, 32_LVBus373830_production, 32_LVBus373831_production, 32_LVBus373832_production, 32_LVBus373833_production, 32_LVBus373834_consumption, 32_LVBus373834_production, 32_LVBus373836_production, 32_LVBus373837_production, 32_LVBus373838_production, 32_LVBus373839_production, 32_LVBus373840_production, 32_LVBus373841_production, 32_LVBus373842_production, 32_LVBus373843_production, 32_LVBus373844_production, 32_LVBus373846_production, 32_LVBus373847_production, 32_LVBus373848_production, 32_LVBus373849_consumption, 32_LVBus373849_production, 32_LVBus373850_production, 32_LVBus373851_production, 32_LVBus373852_consumption, 32_LVBus373852_production, 32_LVBus373853_production, 32_LVBus373854_production, 32_LVBus373855_production, 32_LVBus373856_production, 32_LVBus373911_consumption, 32_LVBus373911_production, 32_LVBus373912_production, 32_LVBus373913_production, 32_LVBus373915_consumption, 32_LVBus373915_production, 32_LVBus373916_consumption, 32_LVBus373916_production, 32_LVBus373917_production, 32_LVBus373918_production, 32_LVBus373919_consumption, 32_LVBus373919_production, 32_LVBus373920_production, 32_LVBus373921_production, 32_LVBus373922_production, 32_LVBus373924_production, 32_LVBus373926_production, 32_LVBus373927_consumption, 32_LVBus373927_production, 32_LVBus373928_consumption, 32_LVBus373928_production, 32_LVBus373929_consumption, 32_LVBus373929_production, 32_LVBus373930_consumption, 32_LVBus373930_production, 32_LVBus373931_consumption, 32_LVBus373931_production, 32_LVBus373932_consumption, 32_LVBus373932_production, 32_LVBus373933_consumption, 32_LVBus373933_production, 32_LVBus373934_production, 32_LVBus373935_consumption, 32_LVBus373935_production, 32_LVBus373936_production, 32_LVBus373937_consumption, 32_LVBus373937_production, 32_LVBus373938_production, 32_LVBus373939_consumption, 32_LVBus373939_production, 32_LVBus373940_production, 32_LVBus373941_production, 32_LVBus373942_production, 32_LVBus373943_production, 32_LVBus373944_production, 32_LVBus373945_production, 32_LVBus373946_production, 32_MVLV49496_consumption, 32_MVLV49496_production, 32_MVLV59272_consumption, 32_MVLV59272_production.

## 9. Data Quality Summary

**Total findings:** 343 (0 errors, 5 warnings, 338 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  593 of 940 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.82 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  594 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373592_consumption`  
  Load '32_LVBus373592_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373850_consumption`  
  Load '32_LVBus373850_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373772_consumption`  
  Load '32_LVBus373772_consumption' has phase imbalance of 135.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373622_consumption`  
  Load '32_LVBus373622_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1166133_consumption`  
  Load '32_LVBus1166133_consumption' has phase imbalance of 83.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373676_consumption`  
  Load '32_LVBus373676_consumption' has phase imbalance of 269.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373520_consumption`  
  Load '32_LVBus373520_consumption' has phase imbalance of 86.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373812_consumption`  
  Load '32_LVBus373812_consumption' has phase imbalance of 131.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373505_consumption`  
  Load '32_LVBus373505_consumption' has phase imbalance of 176.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373618_consumption`  
  Load '32_LVBus373618_consumption' has phase imbalance of 61.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373661_consumption`  
  Load '32_LVBus373661_consumption' has phase imbalance of 135.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373525_consumption`  
  Load '32_LVBus373525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373420_consumption`  
  Load '32_LVBus373420_consumption' has phase imbalance of 203.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110903_consumption`  
  Load '32_LVBus1110903_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373641_consumption`  
  Load '32_LVBus373641_consumption' has phase imbalance of 241.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373607_consumption`  
  Load '32_LVBus373607_consumption' has phase imbalance of 51.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1166129_consumption`  
  Load '32_LVBus1166129_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373412_consumption`  
  Load '32_LVBus373412_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373401_consumption`  
  Load '32_LVBus373401_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373574_consumption`  
  Load '32_LVBus373574_consumption' has phase imbalance of 140.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373515_consumption`  
  Load '32_LVBus373515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373500_consumption`  
  Load '32_LVBus373500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373851_consumption`  
  Load '32_LVBus373851_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373730_consumption`  
  Load '32_LVBus373730_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373391_consumption`  
  Load '32_LVBus373391_consumption' has phase imbalance of 223.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373698_consumption`  
  Load '32_LVBus373698_consumption' has phase imbalance of 63.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373454_consumption`  
  Load '32_LVBus373454_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373696_consumption`  
  Load '32_LVBus373696_consumption' has phase imbalance of 204.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373842_consumption`  
  Load '32_LVBus373842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373750_consumption`  
  Load '32_LVBus373750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373808_consumption`  
  Load '32_LVBus373808_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373613_consumption`  
  Load '32_LVBus373613_consumption' has phase imbalance of 221.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373410_consumption`  
  Load '32_LVBus373410_consumption' has phase imbalance of 74.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373616_consumption`  
  Load '32_LVBus373616_consumption' has phase imbalance of 92.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373827_consumption`  
  Load '32_LVBus373827_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373738_consumption`  
  Load '32_LVBus373738_consumption' has phase imbalance of 201.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373385_consumption`  
  Load '32_LVBus373385_consumption' has phase imbalance of 191.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373621_consumption`  
  Load '32_LVBus373621_consumption' has phase imbalance of 93.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373590_consumption`  
  Load '32_LVBus373590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373848_consumption`  
  Load '32_LVBus373848_consumption' has phase imbalance of 120.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373724_consumption`  
  Load '32_LVBus373724_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373409_consumption`  
  Load '32_LVBus373409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373853_consumption`  
  Load '32_LVBus373853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373416_consumption`  
  Load '32_LVBus373416_consumption' has phase imbalance of 187.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1166130_consumption`  
  Load '32_LVBus1166130_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1176221_consumption`  
  Load '32_LVBus1176221_consumption' has phase imbalance of 173.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373678_consumption`  
  Load '32_LVBus373678_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373790_consumption`  
  Load '32_LVBus373790_consumption' has phase imbalance of 126.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373789_consumption`  
  Load '32_LVBus373789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373625_consumption`  
  Load '32_LVBus373625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373488_consumption`  
  Load '32_LVBus373488_consumption' has phase imbalance of 94.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373593_consumption`  
  Load '32_LVBus373593_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373640_consumption`  
  Load '32_LVBus373640_consumption' has phase imbalance of 27.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373819_consumption`  
  Load '32_LVBus373819_consumption' has phase imbalance of 104.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373700_consumption`  
  Load '32_LVBus373700_consumption' has phase imbalance of 118.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373490_consumption`  
  Load '32_LVBus373490_consumption' has phase imbalance of 100.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373620_consumption`  
  Load '32_LVBus373620_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373585_consumption`  
  Load '32_LVBus373585_consumption' has phase imbalance of 194.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373394_consumption`  
  Load '32_LVBus373394_consumption' has phase imbalance of 134.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373940_consumption`  
  Load '32_LVBus373940_consumption' has phase imbalance of 98.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373393_consumption`  
  Load '32_LVBus373393_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373529_consumption`  
  Load '32_LVBus373529_consumption' has phase imbalance of 37.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373578_consumption`  
  Load '32_LVBus373578_consumption' has phase imbalance of 171.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373606_consumption`  
  Load '32_LVBus373606_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373690_consumption`  
  Load '32_LVBus373690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373491_consumption`  
  Load '32_LVBus373491_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373729_consumption`  
  Load '32_LVBus373729_consumption' has phase imbalance of 104.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373728_consumption`  
  Load '32_LVBus373728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373609_consumption`  
  Load '32_LVBus373609_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373493_consumption`  
  Load '32_LVBus373493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373777_consumption`  
  Load '32_LVBus373777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373658_consumption`  
  Load '32_LVBus373658_consumption' has phase imbalance of 137.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373519_consumption`  
  Load '32_LVBus373519_consumption' has phase imbalance of 104.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1159484_consumption`  
  Load '32_LVBus1159484_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373798_consumption`  
  Load '32_LVBus373798_consumption' has phase imbalance of 69.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1176223_consumption`  
  Load '32_LVBus1176223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373941_consumption`  
  Load '32_LVBus373941_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373513_consumption`  
  Load '32_LVBus373513_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373766_consumption`  
  Load '32_LVBus373766_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373600_consumption`  
  Load '32_LVBus373600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373477_consumption`  
  Load '32_LVBus373477_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373926_consumption`  
  Load '32_LVBus373926_consumption' has phase imbalance of 227.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373688_consumption`  
  Load '32_LVBus373688_consumption' has phase imbalance of 201.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373697_consumption`  
  Load '32_LVBus373697_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373619_consumption`  
  Load '32_LVBus373619_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373573_consumption`  
  Load '32_LVBus373573_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373644_consumption`  
  Load '32_LVBus373644_consumption' has phase imbalance of 172.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373496_consumption`  
  Load '32_LVBus373496_consumption' has phase imbalance of 207.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373747_consumption`  
  Load '32_LVBus373747_consumption' has phase imbalance of 258.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373605_consumption`  
  Load '32_LVBus373605_consumption' has phase imbalance of 131.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373682_consumption`  
  Load '32_LVBus373682_consumption' has phase imbalance of 104.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373632_consumption`  
  Load '32_LVBus373632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373422_consumption`  
  Load '32_LVBus373422_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373936_consumption`  
  Load '32_LVBus373936_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373647_consumption`  
  Load '32_LVBus373647_consumption' has phase imbalance of 174.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373660_consumption`  
  Load '32_LVBus373660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373833_consumption`  
  Load '32_LVBus373833_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373567_consumption`  
  Load '32_LVBus373567_consumption' has phase imbalance of 42.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373517_consumption`  
  Load '32_LVBus373517_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373579_consumption`  
  Load '32_LVBus373579_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373913_consumption`  
  Load '32_LVBus373913_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373825_consumption`  
  Load '32_LVBus373825_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373430_consumption`  
  Load '32_LVBus373430_consumption' has phase imbalance of 135.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373818_consumption`  
  Load '32_LVBus373818_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373668_consumption`  
  Load '32_LVBus373668_consumption' has phase imbalance of 267.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373414_consumption`  
  Load '32_LVBus373414_consumption' has phase imbalance of 246.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373594_consumption`  
  Load '32_LVBus373594_consumption' has phase imbalance of 78.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373846_consumption`  
  Load '32_LVBus373846_consumption' has phase imbalance of 68.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373831_consumption`  
  Load '32_LVBus373831_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373487_consumption`  
  Load '32_LVBus373487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373943_consumption`  
  Load '32_LVBus373943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373828_consumption`  
  Load '32_LVBus373828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373788_consumption`  
  Load '32_LVBus373788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373934_consumption`  
  Load '32_LVBus373934_consumption' has phase imbalance of 24.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373637_consumption`  
  Load '32_LVBus373637_consumption' has phase imbalance of 220.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1142555_consumption`  
  Load '32_LVBus1142555_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373836_consumption`  
  Load '32_LVBus373836_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373832_consumption`  
  Load '32_LVBus373832_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373824_consumption`  
  Load '32_LVBus373824_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373499_consumption`  
  Load '32_LVBus373499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373489_consumption`  
  Load '32_LVBus373489_consumption' has phase imbalance of 88.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373583_consumption`  
  Load '32_LVBus373583_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373945_consumption`  
  Load '32_LVBus373945_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1180552_consumption`  
  Load '32_LVBus1180552_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373656_consumption`  
  Load '32_LVBus373656_consumption' has phase imbalance of 294.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373814_consumption`  
  Load '32_LVBus373814_consumption' has phase imbalance of 40.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110908_consumption`  
  Load '32_LVBus1110908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373596_consumption`  
  Load '32_LVBus373596_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373558_consumption`  
  Load '32_LVBus373558_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373922_consumption`  
  Load '32_LVBus373922_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373807_consumption`  
  Load '32_LVBus373807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373386_consumption`  
  Load '32_LVBus373386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1128681_consumption`  
  Load '32_LVBus1128681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373664_consumption`  
  Load '32_LVBus373664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373780_consumption`  
  Load '32_LVBus373780_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373472_consumption`  
  Load '32_LVBus373472_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373645_consumption`  
  Load '32_LVBus373645_consumption' has phase imbalance of 42.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373917_consumption`  
  Load '32_LVBus373917_consumption' has phase imbalance of 264.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373745_consumption`  
  Load '32_LVBus373745_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373770_consumption`  
  Load '32_LVBus373770_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1159485_consumption`  
  Load '32_LVBus1159485_consumption' has phase imbalance of 165.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373581_consumption`  
  Load '32_LVBus373581_consumption' has phase imbalance of 33.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373800_consumption`  
  Load '32_LVBus373800_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373675_consumption`  
  Load '32_LVBus373675_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373815_consumption`  
  Load '32_LVBus373815_consumption' has phase imbalance of 176.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373544_consumption`  
  Load '32_LVBus373544_consumption' has phase imbalance of 42.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373534_consumption`  
  Load '32_LVBus373534_consumption' has phase imbalance of 54.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373672_consumption`  
  Load '32_LVBus373672_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373746_consumption`  
  Load '32_LVBus373746_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373743_consumption`  
  Load '32_LVBus373743_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373577_consumption`  
  Load '32_LVBus373577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373643_consumption`  
  Load '32_LVBus373643_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373813_consumption`  
  Load '32_LVBus373813_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1180553_consumption`  
  Load '32_LVBus1180553_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373920_consumption`  
  Load '32_LVBus373920_consumption' has phase imbalance of 276.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1176224_consumption`  
  Load '32_LVBus1176224_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373522_consumption`  
  Load '32_LVBus373522_consumption' has phase imbalance of 210.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373382_consumption`  
  Load '32_LVBus373382_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373576_consumption`  
  Load '32_LVBus373576_consumption' has phase imbalance of 142.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373796_consumption`  
  Load '32_LVBus373796_consumption' has phase imbalance of 248.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373671_consumption`  
  Load '32_LVBus373671_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373509_consumption`  
  Load '32_LVBus373509_consumption' has phase imbalance of 112.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373741_consumption`  
  Load '32_LVBus373741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373392_consumption`  
  Load '32_LVBus373392_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373521_consumption`  
  Load '32_LVBus373521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373749_consumption`  
  Load '32_LVBus373749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373650_consumption`  
  Load '32_LVBus373650_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373810_consumption`  
  Load '32_LVBus373810_consumption' has phase imbalance of 206.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373638_consumption`  
  Load '32_LVBus373638_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373501_consumption`  
  Load '32_LVBus373501_consumption' has phase imbalance of 179.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1128680_consumption`  
  Load '32_LVBus1128680_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373633_consumption`  
  Load '32_LVBus373633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373510_consumption`  
  Load '32_LVBus373510_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373475_consumption`  
  Load '32_LVBus373475_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110907_consumption`  
  Load '32_LVBus1110907_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373801_consumption`  
  Load '32_LVBus373801_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373837_consumption`  
  Load '32_LVBus373837_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373797_consumption`  
  Load '32_LVBus373797_consumption' has phase imbalance of 89.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373679_consumption`  
  Load '32_LVBus373679_consumption' has phase imbalance of 67.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373767_consumption`  
  Load '32_LVBus373767_consumption' has phase imbalance of 170.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373794_consumption`  
  Load '32_LVBus373794_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373586_consumption`  
  Load '32_LVBus373586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373533_consumption`  
  Load '32_LVBus373533_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373726_consumption`  
  Load '32_LVBus373726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373478_consumption`  
  Load '32_LVBus373478_consumption' has phase imbalance of 113.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373702_consumption`  
  Load '32_LVBus373702_consumption' has phase imbalance of 67.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373692_consumption`  
  Load '32_LVBus373692_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373774_consumption`  
  Load '32_LVBus373774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373739_consumption`  
  Load '32_LVBus373739_consumption' has phase imbalance of 240.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373429_consumption`  
  Load '32_LVBus373429_consumption' has phase imbalance of 49.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110905_consumption`  
  Load '32_LVBus1110905_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373474_consumption`  
  Load '32_LVBus373474_consumption' has phase imbalance of 108.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373785_consumption`  
  Load '32_LVBus373785_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373406_consumption`  
  Load '32_LVBus373406_consumption' has phase imbalance of 29.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373553_consumption`  
  Load '32_LVBus373553_consumption' has phase imbalance of 45.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373737_consumption`  
  Load '32_LVBus373737_consumption' has phase imbalance of 137.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373856_consumption`  
  Load '32_LVBus373856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373802_consumption`  
  Load '32_LVBus373802_consumption' has phase imbalance of 257.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373646_consumption`  
  Load '32_LVBus373646_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373755_consumption`  
  Load '32_LVBus373755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373631_consumption`  
  Load '32_LVBus373631_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373428_consumption`  
  Load '32_LVBus373428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373396_consumption`  
  Load '32_LVBus373396_consumption' has phase imbalance of 121.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373924_consumption`  
  Load '32_LVBus373924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373530_consumption`  
  Load '32_LVBus373530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373628_consumption`  
  Load '32_LVBus373628_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1142554_consumption`  
  Load '32_LVBus1142554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373636_consumption`  
  Load '32_LVBus373636_consumption' has phase imbalance of 36.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373610_consumption`  
  Load '32_LVBus373610_consumption' has phase imbalance of 109.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373841_consumption`  
  Load '32_LVBus373841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373944_consumption`  
  Load '32_LVBus373944_consumption' has phase imbalance of 215.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373536_consumption`  
  Load '32_LVBus373536_consumption' has phase imbalance of 71.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373524_consumption`  
  Load '32_LVBus373524_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373669_consumption`  
  Load '32_LVBus373669_consumption' has phase imbalance of 264.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373704_consumption`  
  Load '32_LVBus373704_consumption' has phase imbalance of 65.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373543_consumption`  
  Load '32_LVBus373543_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373587_consumption`  
  Load '32_LVBus373587_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373736_consumption`  
  Load '32_LVBus373736_consumption' has phase imbalance of 243.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373580_consumption`  
  Load '32_LVBus373580_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373847_consumption`  
  Load '32_LVBus373847_consumption' has phase imbalance of 82.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373829_consumption`  
  Load '32_LVBus373829_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373778_consumption`  
  Load '32_LVBus373778_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373705_consumption`  
  Load '32_LVBus373705_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373663_consumption`  
  Load '32_LVBus373663_consumption' has phase imbalance of 86.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373855_consumption`  
  Load '32_LVBus373855_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373508_consumption`  
  Load '32_LVBus373508_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373764_consumption`  
  Load '32_LVBus373764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373531_consumption`  
  Load '32_LVBus373531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373817_consumption`  
  Load '32_LVBus373817_consumption' has phase imbalance of 159.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373717_consumption`  
  Load '32_LVBus373717_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373757_consumption`  
  Load '32_LVBus373757_consumption' has phase imbalance of 52.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373648_consumption`  
  Load '32_LVBus373648_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373795_consumption`  
  Load '32_LVBus373795_consumption' has phase imbalance of 155.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373624_consumption`  
  Load '32_LVBus373624_consumption' has phase imbalance of 68.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373559_consumption`  
  Load '32_LVBus373559_consumption' has phase imbalance of 68.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373612_consumption`  
  Load '32_LVBus373612_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1128683_consumption`  
  Load '32_LVBus1128683_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373407_consumption`  
  Load '32_LVBus373407_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373602_consumption`  
  Load '32_LVBus373602_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373918_consumption`  
  Load '32_LVBus373918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373629_consumption`  
  Load '32_LVBus373629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373942_consumption`  
  Load '32_LVBus373942_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373838_consumption`  
  Load '32_LVBus373838_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373783_consumption`  
  Load '32_LVBus373783_consumption' has phase imbalance of 187.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373400_consumption`  
  Load '32_LVBus373400_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373532_consumption`  
  Load '32_LVBus373532_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373843_consumption`  
  Load '32_LVBus373843_consumption' has phase imbalance of 228.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373635_consumption`  
  Load '32_LVBus373635_consumption' has phase imbalance of 230.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373765_consumption`  
  Load '32_LVBus373765_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373397_consumption`  
  Load '32_LVBus373397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373751_consumption`  
  Load '32_LVBus373751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373674_consumption`  
  Load '32_LVBus373674_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373498_consumption`  
  Load '32_LVBus373498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373390_consumption`  
  Load '32_LVBus373390_consumption' has phase imbalance of 182.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373575_consumption`  
  Load '32_LVBus373575_consumption' has phase imbalance of 247.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373419_consumption`  
  Load '32_LVBus373419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373537_consumption`  
  Load '32_LVBus373537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373653_consumption`  
  Load '32_LVBus373653_consumption' has phase imbalance of 194.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373735_consumption`  
  Load '32_LVBus373735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373473_consumption`  
  Load '32_LVBus373473_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373601_consumption`  
  Load '32_LVBus373601_consumption' has phase imbalance of 23.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373415_consumption`  
  Load '32_LVBus373415_consumption' has phase imbalance of 234.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373502_consumption`  
  Load '32_LVBus373502_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373946_consumption`  
  Load '32_LVBus373946_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373769_consumption`  
  Load '32_LVBus373769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373657_consumption`  
  Load '32_LVBus373657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373673_consumption`  
  Load '32_LVBus373673_consumption' has phase imbalance of 43.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373614_consumption`  
  Load '32_LVBus373614_consumption' has phase imbalance of 75.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373823_consumption`  
  Load '32_LVBus373823_consumption' has phase imbalance of 200.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373844_consumption`  
  Load '32_LVBus373844_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373786_consumption`  
  Load '32_LVBus373786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373598_consumption`  
  Load '32_LVBus373598_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373512_consumption`  
  Load '32_LVBus373512_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1142552_consumption`  
  Load '32_LVBus1142552_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373611_consumption`  
  Load '32_LVBus373611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1184320_consumption`  
  Load '32_LVBus1184320_consumption' has phase imbalance of 76.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373424_consumption`  
  Load '32_LVBus373424_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373516_consumption`  
  Load '32_LVBus373516_consumption' has phase imbalance of 91.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373387_consumption`  
  Load '32_LVBus373387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373486_consumption`  
  Load '32_LVBus373486_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373727_consumption`  
  Load '32_LVBus373727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373403_consumption`  
  Load '32_LVBus373403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373651_consumption`  
  Load '32_LVBus373651_consumption' has phase imbalance of 55.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1125442_consumption`  
  Load '32_LVBus1125442_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373768_consumption`  
  Load '32_LVBus373768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110906_consumption`  
  Load '32_LVBus1110906_consumption' has phase imbalance of 130.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373597_consumption`  
  Load '32_LVBus373597_consumption' has phase imbalance of 39.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373759_consumption`  
  Load '32_LVBus373759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373803_consumption`  
  Load '32_LVBus373803_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373731_consumption`  
  Load '32_LVBus373731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373604_consumption`  
  Load '32_LVBus373604_consumption' has phase imbalance of 158.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373591_consumption`  
  Load '32_LVBus373591_consumption' has phase imbalance of 152.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373773_consumption`  
  Load '32_LVBus373773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373497_consumption`  
  Load '32_LVBus373497_consumption' has phase imbalance of 172.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373639_consumption`  
  Load '32_LVBus373639_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373423_consumption`  
  Load '32_LVBus373423_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373584_consumption`  
  Load '32_LVBus373584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373839_consumption`  
  Load '32_LVBus373839_consumption' has phase imbalance of 20.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373514_consumption`  
  Load '32_LVBus373514_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373405_consumption`  
  Load '32_LVBus373405_consumption' has phase imbalance of 86.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373744_consumption`  
  Load '32_LVBus373744_consumption' has phase imbalance of 85.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373518_consumption`  
  Load '32_LVBus373518_consumption' has phase imbalance of 228.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373840_consumption`  
  Load '32_LVBus373840_consumption' has phase imbalance of 143.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373921_consumption`  
  Load '32_LVBus373921_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110909_consumption`  
  Load '32_LVBus1110909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373432_consumption`  
  Load '32_LVBus373432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373384_consumption`  
  Load '32_LVBus373384_consumption' has phase imbalance of 59.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373549_consumption`  
  Load '32_LVBus373549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373784_consumption`  
  Load '32_LVBus373784_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373476_consumption`  
  Load '32_LVBus373476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373535_consumption`  
  Load '32_LVBus373535_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373771_consumption`  
  Load '32_LVBus373771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373649_consumption`  
  Load '32_LVBus373649_consumption' has phase imbalance of 89.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373408_consumption`  
  Load '32_LVBus373408_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373588_consumption`  
  Load '32_LVBus373588_consumption' has phase imbalance of 251.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373938_consumption`  
  Load '32_LVBus373938_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373854_consumption`  
  Load '32_LVBus373854_consumption' has phase imbalance of 81.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373821_consumption`  
  Load '32_LVBus373821_consumption' has phase imbalance of 88.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373748_consumption`  
  Load '32_LVBus373748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1166132_consumption`  
  Load '32_LVBus1166132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110904_consumption`  
  Load '32_LVBus1110904_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373680_consumption`  
  Load '32_LVBus373680_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus373805_consumption`  
  Load '32_LVBus373805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 940 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '32_LVBus1128679' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  498 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  195 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus1110903_consumption, 32_LVBus1110907_consumption, 32_LVBus1110908_consumption, 32_LVBus1110909_consumption, 32_LVBus1125442_consumption, 32_LVBus1128680_consumption, 32_LVBus1128681_consumption, 32_LVBus1142554_consumption, 32_LVBus1142555_consumption, 32_LVBus1159484_consumption, 32_LVBus1159485_consumption, 32_LVBus1166129_consumption, 32_LVBus1166130_consumption, 32_LVBus1166132_consumption, 32_LVBus1176221_consumption, 32_LVBus1176223_consumption, 32_LVBus1180553_consumption, 32_LVBus373382_consumption, 32_LVBus373385_consumption, 32_LVBus373386_consumption, 32_LVBus373387_consumption, 32_LVBus373390_consumption, 32_LVBus373391_consumption, 32_LVBus373393_consumption, 32_LVBus373397_consumption, 32_LVBus373403_consumption, 32_LVBus373407_consumption, 32_LVBus373408_consumption, 32_LVBus373409_consumption, 32_LVBus373412_consumption, 32_LVBus373414_consumption, 32_LVBus373415_consumption, 32_LVBus373419_consumption, 32_LVBus373420_consumption, 32_LVBus373422_consumption, 32_LVBus373423_consumption, 32_LVBus373424_consumption, 32_LVBus373428_consumption, 32_LVBus373432_consumption, 32_LVBus373472_consumption, 32_LVBus373473_consumption, 32_LVBus373475_consumption, 32_LVBus373476_consumption, 32_LVBus373477_consumption, 32_LVBus373486_consumption, 32_LVBus373487_consumption, 32_LVBus373491_consumption, 32_LVBus373493_consumption, 32_LVBus373496_consumption, 32_LVBus373498_consumption, 32_LVBus373499_consumption, 32_LVBus373500_consumption, 32_LVBus373501_consumption, 32_LVBus373502_consumption, 32_LVBus373510_consumption, 32_LVBus373512_consumption, 32_LVBus373514_consumption, 32_LVBus373515_consumption, 32_LVBus373517_consumption, 32_LVBus373518_consumption, 32_LVBus373521_consumption, 32_LVBus373522_consumption, 32_LVBus373524_consumption, 32_LVBus373525_consumption, 32_LVBus373530_consumption, 32_LVBus373531_consumption, 32_LVBus373532_consumption, 32_LVBus373535_consumption, 32_LVBus373537_consumption, 32_LVBus373549_consumption, 32_LVBus373573_consumption, 32_LVBus373575_consumption, 32_LVBus373577_consumption, 32_LVBus373578_consumption, 32_LVBus373580_consumption, 32_LVBus373583_consumption, 32_LVBus373584_consumption, 32_LVBus373585_consumption, 32_LVBus373586_consumption, 32_LVBus373587_consumption, 32_LVBus373590_consumption, 32_LVBus373593_consumption, 32_LVBus373598_consumption, 32_LVBus373600_consumption, 32_LVBus373602_consumption, 32_LVBus373606_consumption, 32_LVBus373609_consumption, 32_LVBus373611_consumption, 32_LVBus373612_consumption, 32_LVBus373613_consumption, 32_LVBus373622_consumption, 32_LVBus373625_consumption, 32_LVBus373629_consumption, 32_LVBus373632_consumption, 32_LVBus373633_consumption, 32_LVBus373635_consumption, 32_LVBus373637_consumption, 32_LVBus373638_consumption, 32_LVBus373639_consumption, 32_LVBus373641_consumption, 32_LVBus373644_consumption, 32_LVBus373646_consumption, 32_LVBus373647_consumption, 32_LVBus373653_consumption, 32_LVBus373656_consumption, 32_LVBus373657_consumption, 32_LVBus373660_consumption, 32_LVBus373664_consumption, 32_LVBus373668_consumption, 32_LVBus373669_consumption, 32_LVBus373671_consumption, 32_LVBus373672_consumption, 32_LVBus373674_consumption, 32_LVBus373675_consumption, 32_LVBus373676_consumption, 32_LVBus373688_consumption, 32_LVBus373690_consumption, 32_LVBus373696_consumption, 32_LVBus373724_consumption, 32_LVBus373726_consumption, 32_LVBus373727_consumption, 32_LVBus373728_consumption, 32_LVBus373731_consumption, 32_LVBus373735_consumption, 32_LVBus373736_consumption, 32_LVBus373738_consumption, 32_LVBus373739_consumption, 32_LVBus373741_consumption, 32_LVBus373743_consumption, 32_LVBus373745_consumption, 32_LVBus373747_consumption, 32_LVBus373748_consumption, 32_LVBus373749_consumption, 32_LVBus373750_consumption, 32_LVBus373751_consumption, 32_LVBus373755_consumption, 32_LVBus373759_consumption, 32_LVBus373764_consumption, 32_LVBus373765_consumption, 32_LVBus373766_consumption, 32_LVBus373767_consumption, 32_LVBus373768_consumption, 32_LVBus373769_consumption, 32_LVBus373770_consumption, 32_LVBus373771_consumption, 32_LVBus373773_consumption, 32_LVBus373774_consumption, 32_LVBus373777_consumption, 32_LVBus373778_consumption, 32_LVBus373783_consumption, 32_LVBus373785_consumption, 32_LVBus373786_consumption, 32_LVBus373788_consumption, 32_LVBus373789_consumption, 32_LVBus373794_consumption, 32_LVBus373795_consumption, 32_LVBus373796_consumption, 32_LVBus373802_consumption, 32_LVBus373803_consumption, 32_LVBus373805_consumption, 32_LVBus373807_consumption, 32_LVBus373808_consumption, 32_LVBus373810_consumption, 32_LVBus373815_consumption, 32_LVBus373817_consumption, 32_LVBus373823_consumption, 32_LVBus373825_consumption, 32_LVBus373827_consumption, 32_LVBus373828_consumption, 32_LVBus373829_consumption, 32_LVBus373832_consumption, 32_LVBus373837_consumption, 32_LVBus373841_consumption, 32_LVBus373842_consumption, 32_LVBus373843_consumption, 32_LVBus373844_consumption, 32_LVBus373851_consumption, 32_LVBus373853_consumption, 32_LVBus373855_consumption, 32_LVBus373856_consumption, 32_LVBus373917_consumption, 32_LVBus373918_consumption, 32_LVBus373920_consumption, 32_LVBus373921_consumption, 32_LVBus373922_consumption, 32_LVBus373924_consumption, 32_LVBus373926_consumption, 32_LVBus373936_consumption, 32_LVBus373938_consumption, 32_LVBus373941_consumption, 32_LVBus373942_consumption, 32_LVBus373943_consumption, 32_LVBus373944_consumption, 32_LVBus373945_consumption, 32_LVBus373946_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  470 group(s) of loads (940 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  594 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1110903_production, 32_LVBus1110904_production, 32_LVBus1110905_production, 32_LVBus1110906_production, 32_LVBus1110907_production, 32_LVBus1110908_production, 32_LVBus1110909_production, 32_LVBus1125442_production, 32_LVBus1128679_consumption, 32_LVBus1128679_production, 32_LVBus1128680_production, 32_LVBus1128681_production, 32_LVBus1128682_production, 32_LVBus1128683_production, 32_LVBus1142549_consumption, 32_LVBus1142549_production, 32_LVBus1142550_consumption, 32_LVBus1142550_production, 32_LVBus1142551_consumption, 32_LVBus1142551_production, 32_LVBus1142552_production, 32_LVBus1142553_consumption, 32_LVBus1142553_production, 32_LVBus1142554_production, 32_LVBus1142555_production, 32_LVBus1159484_production, 32_LVBus1159485_production, 32_LVBus1166129_production, 32_LVBus1166130_production, 32_LVBus1166131_consumption, 32_LVBus1166131_production, 32_LVBus1166132_production, 32_LVBus1166133_production, 32_LVBus1176221_production, 32_LVBus1176222_production, 32_LVBus1176223_production, 32_LVBus1176224_production, 32_LVBus1180552_production, 32_LVBus1180553_production, 32_LVBus1184320_production, 32_LVBus373382_production, 32_LVBus373384_production, 32_LVBus373385_production, 32_LVBus373386_production, 32_LVBus373387_production, 32_LVBus373388_consumption, 32_LVBus373388_production, 32_LVBus373390_production, 32_LVBus373391_production, 32_LVBus373392_production, 32_LVBus373393_production, 32_LVBus373394_production, 32_LVBus373396_production, 32_LVBus373397_production, 32_LVBus373398_consumption, 32_LVBus373398_production, 32_LVBus373400_production, 32_LVBus373401_production, 32_LVBus373402_consumption, 32_LVBus373402_production, 32_LVBus373403_production, 32_LVBus373404_consumption, 32_LVBus373404_production, 32_LVBus373405_production, 32_LVBus373406_production, 32_LVBus373407_production, 32_LVBus373408_production, 32_LVBus373409_production, 32_LVBus373410_production, 32_LVBus373411_consumption, 32_LVBus373411_production, 32_LVBus373412_production, 32_LVBus373413_consumption, 32_LVBus373413_production, 32_LVBus373414_production, 32_LVBus373415_production, 32_LVBus373416_production, 32_LVBus373418_consumption, 32_LVBus373418_production, 32_LVBus373419_production, 32_LVBus373420_production, 32_LVBus373421_consumption, 32_LVBus373421_production, 32_LVBus373422_production, 32_LVBus373423_production, 32_LVBus373424_production, 32_LVBus373425_production, 32_LVBus373427_consumption, 32_LVBus373427_production, 32_LVBus373428_production, 32_LVBus373429_production, 32_LVBus373430_production, 32_LVBus373432_production, 32_LVBus373434_consumption, 32_LVBus373434_production, 32_LVBus373435_consumption, 32_LVBus373435_production, 32_LVBus373437_consumption, 32_LVBus373437_production, 32_LVBus373438_consumption, 32_LVBus373438_production, 32_LVBus373439_consumption, 32_LVBus373439_production, 32_LVBus373441_consumption, 32_LVBus373441_production, 32_LVBus373442_consumption, 32_LVBus373442_production, 32_LVBus373443_production, 32_LVBus373445_consumption, 32_LVBus373445_production, 32_LVBus373446_consumption, 32_LVBus373446_production, 32_LVBus373447_consumption, 32_LVBus373447_production, 32_LVBus373448_consumption, 32_LVBus373448_production, 32_LVBus373450_consumption, 32_LVBus373450_production, 32_LVBus373451_consumption, 32_LVBus373451_production, 32_LVBus373452_consumption, 32_LVBus373452_production, 32_LVBus373454_production, 32_LVBus373455_consumption, 32_LVBus373455_production, 32_LVBus373456_consumption, 32_LVBus373456_production, 32_LVBus373457_production, 32_LVBus373459_consumption, 32_LVBus373459_production, 32_LVBus373460_consumption, 32_LVBus373460_production, 32_LVBus373462_consumption, 32_LVBus373462_production, 32_LVBus373463_consumption, 32_LVBus373463_production, 32_LVBus373465_consumption, 32_LVBus373465_production, 32_LVBus373466_consumption, 32_LVBus373466_production, 32_LVBus373467_consumption, 32_LVBus373467_production, 32_LVBus373472_production, 32_LVBus373473_production, 32_LVBus373474_production, 32_LVBus373475_production, 32_LVBus373476_production, 32_LVBus373477_production, 32_LVBus373478_production, 32_LVBus373479_consumption, 32_LVBus373479_production, 32_LVBus373480_consumption, 32_LVBus373480_production, 32_LVBus373481_consumption, 32_LVBus373481_production, 32_LVBus373482_consumption, 32_LVBus373482_production, 32_LVBus373483_consumption, 32_LVBus373483_production, 32_LVBus373484_consumption, 32_LVBus373484_production, 32_LVBus373485_production, 32_LVBus373486_production, 32_LVBus373487_production, 32_LVBus373488_production, 32_LVBus373489_production, 32_LVBus373490_production, 32_LVBus373491_production, 32_LVBus373493_production, 32_LVBus373495_consumption, 32_LVBus373495_production, 32_LVBus373496_production, 32_LVBus373497_production, 32_LVBus373498_production, 32_LVBus373499_production, 32_LVBus373500_production, 32_LVBus373501_production, 32_LVBus373502_production, 32_LVBus373503_consumption, 32_LVBus373503_production, 32_LVBus373504_consumption, 32_LVBus373504_production, 32_LVBus373505_production, 32_LVBus373506_consumption, 32_LVBus373506_production, 32_LVBus373507_consumption, 32_LVBus373507_production, 32_LVBus373508_production, 32_LVBus373509_production, 32_LVBus373510_production, 32_LVBus373512_production, 32_LVBus373513_production, 32_LVBus373514_production, 32_LVBus373515_production, 32_LVBus373516_production, 32_LVBus373517_production, 32_LVBus373518_production, 32_LVBus373519_production, 32_LVBus373520_production, 32_LVBus373521_production, 32_LVBus373522_production, 32_LVBus373523_consumption, 32_LVBus373523_production, 32_LVBus373524_production, 32_LVBus373525_production, 32_LVBus373527_consumption, 32_LVBus373527_production, 32_LVBus373528_consumption, 32_LVBus373528_production, 32_LVBus373529_production, 32_LVBus373530_production, 32_LVBus373531_production, 32_LVBus373532_production, 32_LVBus373533_production, 32_LVBus373534_production, 32_LVBus373535_production, 32_LVBus373536_production, 32_LVBus373537_production, 32_LVBus373538_consumption, 32_LVBus373538_production, 32_LVBus373539_consumption, 32_LVBus373539_production, 32_LVBus373540_consumption, 32_LVBus373540_production, 32_LVBus373542_consumption, 32_LVBus373542_production, 32_LVBus373543_production, 32_LVBus373544_production, 32_LVBus373546_consumption, 32_LVBus373546_production, 32_LVBus373547_consumption, 32_LVBus373547_production, 32_LVBus373548_consumption, 32_LVBus373548_production, 32_LVBus373549_production, 32_LVBus373551_consumption, 32_LVBus373551_production, 32_LVBus373552_consumption, 32_LVBus373552_production, 32_LVBus373553_production, 32_LVBus373554_consumption, 32_LVBus373554_production, 32_LVBus373555_consumption, 32_LVBus373555_production, 32_LVBus373556_production, 32_LVBus373557_production, 32_LVBus373558_production, 32_LVBus373559_production, 32_LVBus373561_consumption, 32_LVBus373561_production, 32_LVBus373563_production, 32_LVBus373565_production, 32_LVBus373567_production, 32_LVBus373569_production, 32_LVBus373571_consumption, 32_LVBus373571_production, 32_LVBus373573_production, 32_LVBus373574_production, 32_LVBus373575_production, 32_LVBus373576_production, 32_LVBus373577_production, 32_LVBus373578_production, 32_LVBus373579_production, 32_LVBus373580_production, 32_LVBus373581_production, 32_LVBus373583_production, 32_LVBus373584_production, 32_LVBus373585_production, 32_LVBus373586_production, 32_LVBus373587_production, 32_LVBus373588_production, 32_LVBus373590_production, 32_LVBus373591_production, 32_LVBus373592_production, 32_LVBus373593_production, 32_LVBus373594_production, 32_LVBus373596_production, 32_LVBus373597_production, 32_LVBus373598_production, 32_LVBus373599_consumption, 32_LVBus373599_production, 32_LVBus373600_production, 32_LVBus373601_production, 32_LVBus373602_production, 32_LVBus373604_production, 32_LVBus373605_production, 32_LVBus373606_production, 32_LVBus373607_production, 32_LVBus373609_production, 32_LVBus373610_production, 32_LVBus373611_production, 32_LVBus373612_production, 32_LVBus373613_production, 32_LVBus373614_production, 32_LVBus373615_production, 32_LVBus373616_production, 32_LVBus373618_production, 32_LVBus373619_production, 32_LVBus373620_production, 32_LVBus373621_production, 32_LVBus373622_production, 32_LVBus373624_production, 32_LVBus373625_production, 32_LVBus373626_consumption, 32_LVBus373626_production, 32_LVBus373627_consumption, 32_LVBus373627_production, 32_LVBus373628_production, 32_LVBus373629_production, 32_LVBus373630_consumption, 32_LVBus373630_production, 32_LVBus373631_production, 32_LVBus373632_production, 32_LVBus373633_production, 32_LVBus373635_production, 32_LVBus373636_production, 32_LVBus373637_production, 32_LVBus373638_production, 32_LVBus373639_production, 32_LVBus373640_production, 32_LVBus373641_production, 32_LVBus373643_production, 32_LVBus373644_production, 32_LVBus373645_production, 32_LVBus373646_production, 32_LVBus373647_production, 32_LVBus373648_production, 32_LVBus373649_production, 32_LVBus373650_production, 32_LVBus373651_production, 32_LVBus373653_production, 32_LVBus373654_consumption, 32_LVBus373654_production, 32_LVBus373656_production, 32_LVBus373657_production, 32_LVBus373658_production, 32_LVBus373660_production, 32_LVBus373661_production, 32_LVBus373663_production, 32_LVBus373664_production, 32_LVBus373665_consumption, 32_LVBus373665_production, 32_LVBus373666_consumption, 32_LVBus373666_production, 32_LVBus373667_consumption, 32_LVBus373667_production, 32_LVBus373668_production, 32_LVBus373669_production, 32_LVBus373671_production, 32_LVBus373672_production, 32_LVBus373673_production, 32_LVBus373674_production, 32_LVBus373675_production, 32_LVBus373676_production, 32_LVBus373678_production, 32_LVBus373679_production, 32_LVBus373680_production, 32_LVBus373681_production, 32_LVBus373682_production, 32_LVBus373683_production, 32_LVBus373685_consumption, 32_LVBus373685_production, 32_LVBus373687_production, 32_LVBus373688_production, 32_LVBus373690_production, 32_LVBus373692_production, 32_LVBus373693_consumption, 32_LVBus373693_production, 32_LVBus373694_production, 32_LVBus373695_consumption, 32_LVBus373695_production, 32_LVBus373696_production, 32_LVBus373697_production, 32_LVBus373698_production, 32_LVBus373700_production, 32_LVBus373701_production, 32_LVBus373702_production, 32_LVBus373703_consumption, 32_LVBus373703_production, 32_LVBus373704_production, 32_LVBus373705_production, 32_LVBus373706_consumption, 32_LVBus373706_production, 32_LVBus373707_consumption, 32_LVBus373707_production, 32_LVBus373708_production, 32_LVBus373709_production, 32_LVBus373710_consumption, 32_LVBus373710_production, 32_LVBus373712_consumption, 32_LVBus373712_production, 32_LVBus373714_consumption, 32_LVBus373714_production, 32_LVBus373715_consumption, 32_LVBus373715_production, 32_LVBus373717_production, 32_LVBus373719_consumption, 32_LVBus373719_production, 32_LVBus373721_consumption, 32_LVBus373721_production, 32_LVBus373722_consumption, 32_LVBus373722_production, 32_LVBus373724_production, 32_LVBus373726_production, 32_LVBus373727_production, 32_LVBus373728_production, 32_LVBus373729_production, 32_LVBus373730_production, 32_LVBus373731_production, 32_LVBus373732_consumption, 32_LVBus373732_production, 32_LVBus373733_consumption, 32_LVBus373733_production, 32_LVBus373735_production, 32_LVBus373736_production, 32_LVBus373737_production, 32_LVBus373738_production, 32_LVBus373739_production, 32_LVBus373741_production, 32_LVBus373742_consumption, 32_LVBus373742_production, 32_LVBus373743_production, 32_LVBus373744_production, 32_LVBus373745_production, 32_LVBus373746_production, 32_LVBus373747_production, 32_LVBus373748_production, 32_LVBus373749_production, 32_LVBus373750_production, 32_LVBus373751_production, 32_LVBus373752_consumption, 32_LVBus373752_production, 32_LVBus373753_consumption, 32_LVBus373753_production, 32_LVBus373754_production, 32_LVBus373755_production, 32_LVBus373756_consumption, 32_LVBus373756_production, 32_LVBus373757_production, 32_LVBus373759_production, 32_LVBus373761_consumption, 32_LVBus373761_production, 32_LVBus373762_consumption, 32_LVBus373762_production, 32_LVBus373763_consumption, 32_LVBus373763_production, 32_LVBus373764_production, 32_LVBus373765_production, 32_LVBus373766_production, 32_LVBus373767_production, 32_LVBus373768_production, 32_LVBus373769_production, 32_LVBus373770_production, 32_LVBus373771_production, 32_LVBus373772_production, 32_LVBus373773_production, 32_LVBus373774_production, 32_LVBus373776_consumption, 32_LVBus373776_production, 32_LVBus373777_production, 32_LVBus373778_production, 32_LVBus373779_consumption, 32_LVBus373779_production, 32_LVBus373780_production, 32_LVBus373781_consumption, 32_LVBus373781_production, 32_LVBus373783_production, 32_LVBus373784_production, 32_LVBus373785_production, 32_LVBus373786_production, 32_LVBus373787_consumption, 32_LVBus373787_production, 32_LVBus373788_production, 32_LVBus373789_production, 32_LVBus373790_production, 32_LVBus373791_consumption, 32_LVBus373791_production, 32_LVBus373794_production, 32_LVBus373795_production, 32_LVBus373796_production, 32_LVBus373797_production, 32_LVBus373798_production, 32_LVBus373799_consumption, 32_LVBus373799_production, 32_LVBus373800_production, 32_LVBus373801_production, 32_LVBus373802_production, 32_LVBus373803_production, 32_LVBus373805_production, 32_LVBus373807_production, 32_LVBus373808_production, 32_LVBus373809_consumption, 32_LVBus373809_production, 32_LVBus373810_production, 32_LVBus373811_consumption, 32_LVBus373811_production, 32_LVBus373812_production, 32_LVBus373813_production, 32_LVBus373814_production, 32_LVBus373815_production, 32_LVBus373816_consumption, 32_LVBus373816_production, 32_LVBus373817_production, 32_LVBus373818_production, 32_LVBus373819_production, 32_LVBus373820_consumption, 32_LVBus373820_production, 32_LVBus373821_production, 32_LVBus373822_production, 32_LVBus373823_production, 32_LVBus373824_production, 32_LVBus373825_production, 32_LVBus373827_production, 32_LVBus373828_production, 32_LVBus373829_production, 32_LVBus373830_production, 32_LVBus373831_production, 32_LVBus373832_production, 32_LVBus373833_production, 32_LVBus373834_consumption, 32_LVBus373834_production, 32_LVBus373836_production, 32_LVBus373837_production, 32_LVBus373838_production, 32_LVBus373839_production, 32_LVBus373840_production, 32_LVBus373841_production, 32_LVBus373842_production, 32_LVBus373843_production, 32_LVBus373844_production, 32_LVBus373846_production, 32_LVBus373847_production, 32_LVBus373848_production, 32_LVBus373849_consumption, 32_LVBus373849_production, 32_LVBus373850_production, 32_LVBus373851_production, 32_LVBus373852_consumption, 32_LVBus373852_production, 32_LVBus373853_production, 32_LVBus373854_production, 32_LVBus373855_production, 32_LVBus373856_production, 32_LVBus373911_consumption, 32_LVBus373911_production, 32_LVBus373912_production, 32_LVBus373913_production, 32_LVBus373915_consumption, 32_LVBus373915_production, 32_LVBus373916_consumption, 32_LVBus373916_production, 32_LVBus373917_production, 32_LVBus373918_production, 32_LVBus373919_consumption, 32_LVBus373919_production, 32_LVBus373920_production, 32_LVBus373921_production, 32_LVBus373922_production, 32_LVBus373924_production, 32_LVBus373926_production, 32_LVBus373927_consumption, 32_LVBus373927_production, 32_LVBus373928_consumption, 32_LVBus373928_production, 32_LVBus373929_consumption, 32_LVBus373929_production, 32_LVBus373930_consumption, 32_LVBus373930_production, 32_LVBus373931_consumption, 32_LVBus373931_production, 32_LVBus373932_consumption, 32_LVBus373932_production, 32_LVBus373933_consumption, 32_LVBus373933_production, 32_LVBus373934_production, 32_LVBus373935_consumption, 32_LVBus373935_production, 32_LVBus373936_production, 32_LVBus373937_consumption, 32_LVBus373937_production, 32_LVBus373938_production, 32_LVBus373939_consumption, 32_LVBus373939_production, 32_LVBus373940_production, 32_LVBus373941_production, 32_LVBus373942_production, 32_LVBus373943_production, 32_LVBus373944_production, 32_LVBus373945_production, 32_LVBus373946_production, 32_MVLV49496_consumption, 32_MVLV49496_production, 32_MVLV59272_consumption, 32_MVLV59272_production.

