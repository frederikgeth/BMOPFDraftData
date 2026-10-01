# BMOPF Network Summary: 53_MVFeeder0762

**Generated:** 2026-10-01 23:34:18  
**Findings:** 0 errors · 4 warnings · 194 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 11 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 351 |  |
| line | 339 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 656 | 3.344 MW, 1.0 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 11 |  |
| switch | 0 |  |
| transformer | 11 | Dyn11×11 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 17 | 16 | 10 | 0 |
| LV_236V | 236.0 V | 334 | 323 | 646 | 0 |

**Transformer transitions:**

- `53_MVLV10552_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV43168_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV74671_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV18648_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV40380_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV32735_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV10570_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV55468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV44003_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV43069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV71970_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 15 |
| Degree-1 buses | 131 |
| Tree depth (max hops) | 24 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 351 | 1 | 350 | 0 | 0 | 0 |
| Tier LV_236V | 334 | 11 | 323 | 0 | 0 | 0 |
| Tier MV_11.8kV | 17 | 1 | 16 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 11; skipped invalid branches: 0.

Galvanic zones: 12; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 53_KEROL | MV_11.8kV | 17 | 0 | 0 | 11 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1387 declared bus terminals; 1340 mapped line/closed-switch conductor edges; 47 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 115000.0 | 3.644 | 1968 |
| q_nom | 0.0 | 34400.0 | 3.644 | 1968 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.34 | 1460.0 | 1.692 | 339 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 1.1e6 | 0.358 | 11 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 446 of 656 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900480_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900515_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900711_consumption' has phase imbalance of 66.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900529_consumption' has phase imbalance of 87.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900530_consumption' has phase imbalance of 129.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900438_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900572_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900652_consumption' has phase imbalance of 97.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900441_consumption' has phase imbalance of 43.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900570_consumption' has phase imbalance of 27.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900413_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900558_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900620_consumption' has phase imbalance of 113.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900534_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900497_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900693_consumption' has phase imbalance of 113.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900511_consumption' has phase imbalance of 149.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900751_consumption' has phase imbalance of 52.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900489_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900384_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900666_consumption' has phase imbalance of 143.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900626_consumption' has phase imbalance of 68.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900678_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900702_consumption' has phase imbalance of 214.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900618_consumption' has phase imbalance of 39.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900552_consumption' has phase imbalance of 38.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900451_consumption' has phase imbalance of 72.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900705_consumption' has phase imbalance of 33.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900464_consumption' has phase imbalance of 119.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900703_consumption' has phase imbalance of 200.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900691_consumption' has phase imbalance of 113.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900481_consumption' has phase imbalance of 40.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900493_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900700_consumption' has phase imbalance of 107.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900469_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900540_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900673_consumption' has phase imbalance of 33.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900501_consumption' has phase imbalance of 70.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900698_consumption' has phase imbalance of 127.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900689_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900521_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900468_consumption' has phase imbalance of 113.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900663_consumption' has phase imbalance of 76.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900557_consumption' has phase imbalance of 64.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900470_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900605_consumption' has phase imbalance of 35.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900659_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900422_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900450_consumption' has phase imbalance of 226.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900560_consumption' has phase imbalance of 42.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900431_consumption' has phase imbalance of 27.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900516_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900657_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900565_consumption' has phase imbalance of 93.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900567_consumption' has phase imbalance of 129.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900532_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900363_consumption' has phase imbalance of 100.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900740_consumption' has phase imbalance of 127.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900687_consumption' has phase imbalance of 204.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900697_consumption' has phase imbalance of 47.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900707_consumption' has phase imbalance of 67.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900684_consumption' has phase imbalance of 93.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900535_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900646_consumption' has phase imbalance of 70.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900394_consumption' has phase imbalance of 83.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900462_consumption' has phase imbalance of 32.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900472_consumption' has phase imbalance of 57.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900508_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900491_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900568_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900561_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900662_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900647_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900611_consumption' has phase imbalance of 133.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900417_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900527_consumption' has phase imbalance of 76.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900421_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900661_consumption' has phase imbalance of 33.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900465_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900437_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900440_consumption' has phase imbalance of 97.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900603_consumption' has phase imbalance of 100.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900708_consumption' has phase imbalance of 46.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900460_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900539_consumption' has phase imbalance of 50.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900513_consumption' has phase imbalance of 21.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900651_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900674_consumption' has phase imbalance of 98.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus981094_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900690_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900742_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900564_consumption' has phase imbalance of 148.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900692_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus974593_consumption' has phase imbalance of 68.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900485_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900478_consumption' has phase imbalance of 41.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900531_consumption' has phase imbalance of 82.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900741_consumption' has phase imbalance of 112.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900566_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900452_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900517_consumption' has phase imbalance of 28.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900648_consumption' has phase imbalance of 86.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900563_consumption' has phase imbalance of 137.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900364_consumption' has phase imbalance of 91.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus985421_consumption' has phase imbalance of 41.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900672_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900617_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900680_consumption' has phase imbalance of 184.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900664_consumption' has phase imbalance of 101.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900660_consumption' has phase imbalance of 92.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900653_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900750_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900446_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900429_consumption' has phase imbalance of 21.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900433_consumption' has phase imbalance of 23.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900712_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900685_consumption' has phase imbalance of 257.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900500_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900668_consumption' has phase imbalance of 122.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900679_consumption' has phase imbalance of 57.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900424_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900553_consumption' has phase imbalance of 51.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900522_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900423_consumption' has phase imbalance of 106.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900459_consumption' has phase imbalance of 61.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900658_consumption' has phase imbalance of 108.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900559_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900542_consumption' has phase imbalance of 103.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900710_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900747_consumption' has phase imbalance of 73.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900425_consumption' has phase imbalance of 194.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900533_consumption' has phase imbalance of 147.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900436_consumption' has phase imbalance of 28.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900713_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900699_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900738_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900752_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900667_consumption' has phase imbalance of 71.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900388_consumption' has phase imbalance of 42.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900688_consumption' has phase imbalance of 48.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900696_consumption' has phase imbalance of 59.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900670_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900609_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900461_consumption' has phase imbalance of 118.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900655_consumption' has phase imbalance of 22.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900528_consumption' has phase imbalance of 23.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900475_consumption' has phase imbalance of 28.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900543_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900677_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900409_consumption' has phase imbalance of 106.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900392_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900512_consumption' has phase imbalance of 85.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900523_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus985426_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900487_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900704_consumption' has phase imbalance of 77.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900507_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900743_consumption' has phase imbalance of 123.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900467_consumption' has phase imbalance of 242.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900536_consumption' has phase imbalance of 75.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900665_consumption' has phase imbalance of 55.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus980987_consumption' has phase imbalance of 32.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900701_consumption' has phase imbalance of 191.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900676_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus900650_consumption' has phase imbalance of 71.9%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 656 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_KEROL' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus900731' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.344 MW |
| Total load Q | 1.0 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 53_MVLV10552_Transformer | 693.0 kVA | 34.1% |
| 53_MVLV43168_Transformer | 1.1 MVA | 22.7% |
| 53_MVLV74671_Transformer | 693.0 kVA | 32.5% |
| 53_MVLV18648_Transformer | 275.0 kVA | 8.5% |
| 53_MVLV40380_Transformer | 693.0 kVA | 39.4% |
| 53_MVLV32735_Transformer | 693.0 kVA | 41.6% |
| 53_MVLV10570_Transformer | 1.1 MVA | 41.1% |
| 53_MVLV55468_Transformer | 1.1 MVA | 56.8% |
| 53_MVLV44003_Transformer | 693.0 kVA | 23.0% |
| 53_MVLV43069_Transformer | 693.0 kVA | 53.8% |
| 53_MVLV71970_Transformer | 440.0 kVA | 8.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.34 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 351 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 351 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 11 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 17 |
| LV_236V | 4-wire | 334 / 334 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 334 |
| Neutral branches | 323 |
| Grounding points | 11 |
| Neutral sections | 11 |
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
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 47 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 54 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 66 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 12 |
| Islands without voltage reference | 0 |
| Line impedance spread | 462.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 334 / 17 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 447 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 447 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus900363_production, 53_LVBus900364_production, 53_LVBus900366_consumption, 53_LVBus900366_production, 53_LVBus900367_consumption, 53_LVBus900367_production, 53_LVBus900369_consumption, 53_LVBus900369_production, 53_LVBus900371_consumption, 53_LVBus900371_production, 53_LVBus900372_consumption, 53_LVBus900372_production, 53_LVBus900373_consumption, 53_LVBus900373_production, 53_LVBus900374_consumption, 53_LVBus900374_production, 53_LVBus900375_consumption, 53_LVBus900375_production, 53_LVBus900376_consumption, 53_LVBus900376_production, 53_LVBus900377_production, 53_LVBus900378_consumption, 53_LVBus900378_production, 53_LVBus900379_consumption, 53_LVBus900379_production, 53_LVBus900381_consumption, 53_LVBus900381_production, 53_LVBus900383_consumption, 53_LVBus900383_production, 53_LVBus900384_production, 53_LVBus900385_consumption, 53_LVBus900385_production, 53_LVBus900386_consumption, 53_LVBus900386_production, 53_LVBus900388_production, 53_LVBus900390_consumption, 53_LVBus900390_production, 53_LVBus900392_production, 53_LVBus900394_production, 53_LVBus900395_consumption, 53_LVBus900395_production, 53_LVBus900396_consumption, 53_LVBus900396_production, 53_LVBus900397_consumption, 53_LVBus900397_production, 53_LVBus900398_production, 53_LVBus900399_production, 53_LVBus900400_consumption, 53_LVBus900400_production, 53_LVBus900401_consumption, 53_LVBus900401_production, 53_LVBus900403_consumption, 53_LVBus900403_production, 53_LVBus900405_production, 53_LVBus900407_production, 53_LVBus900408_consumption, 53_LVBus900408_production, 53_LVBus900409_production, 53_LVBus900410_consumption, 53_LVBus900410_production, 53_LVBus900412_consumption, 53_LVBus900412_production, 53_LVBus900413_production, 53_LVBus900414_production, 53_LVBus900415_consumption, 53_LVBus900415_production, 53_LVBus900417_production, 53_LVBus900418_consumption, 53_LVBus900418_production, 53_LVBus900420_production, 53_LVBus900421_production, 53_LVBus900422_production, 53_LVBus900423_production, 53_LVBus900424_production, 53_LVBus900425_production, 53_LVBus900426_production, 53_LVBus900428_consumption, 53_LVBus900428_production, 53_LVBus900429_production, 53_LVBus900431_production, 53_LVBus900433_production, 53_LVBus900435_consumption, 53_LVBus900435_production, 53_LVBus900436_production, 53_LVBus900437_production, 53_LVBus900438_production, 53_LVBus900439_production, 53_LVBus900440_production, 53_LVBus900441_production, 53_LVBus900443_consumption, 53_LVBus900443_production, 53_LVBus900444_consumption, 53_LVBus900444_production, 53_LVBus900446_production, 53_LVBus900447_consumption, 53_LVBus900447_production, 53_LVBus900449_consumption, 53_LVBus900449_production, 53_LVBus900450_production, 53_LVBus900451_production, 53_LVBus900452_production, 53_LVBus900453_production, 53_LVBus900454_production, 53_LVBus900455_consumption, 53_LVBus900455_production, 53_LVBus900456_consumption, 53_LVBus900456_production, 53_LVBus900457_production, 53_LVBus900459_production, 53_LVBus900460_production, 53_LVBus900461_production, 53_LVBus900462_production, 53_LVBus900464_production, 53_LVBus900465_production, 53_LVBus900467_production, 53_LVBus900468_production, 53_LVBus900469_production, 53_LVBus900470_production, 53_LVBus900471_production, 53_LVBus900472_production, 53_LVBus900475_production, 53_LVBus900476_consumption, 53_LVBus900476_production, 53_LVBus900478_production, 53_LVBus900479_consumption, 53_LVBus900479_production, 53_LVBus900480_production, 53_LVBus900481_production, 53_LVBus900482_production, 53_LVBus900484_consumption, 53_LVBus900484_production, 53_LVBus900485_production, 53_LVBus900486_consumption, 53_LVBus900486_production, 53_LVBus900487_production, 53_LVBus900488_consumption, 53_LVBus900488_production, 53_LVBus900489_production, 53_LVBus900490_consumption, 53_LVBus900490_production, 53_LVBus900491_production, 53_LVBus900493_production, 53_LVBus900494_production, 53_LVBus900496_production, 53_LVBus900497_production, 53_LVBus900498_production, 53_LVBus900500_production, 53_LVBus900501_production, 53_LVBus900502_production, 53_LVBus900503_consumption, 53_LVBus900503_production, 53_LVBus900506_production, 53_LVBus900507_production, 53_LVBus900508_production, 53_LVBus900509_production, 53_LVBus900510_consumption, 53_LVBus900510_production, 53_LVBus900511_production, 53_LVBus900512_production, 53_LVBus900513_production, 53_LVBus900515_production, 53_LVBus900516_production, 53_LVBus900517_production, 53_LVBus900518_production, 53_LVBus900520_production, 53_LVBus900521_production, 53_LVBus900522_production, 53_LVBus900523_production, 53_LVBus900524_production, 53_LVBus900526_production, 53_LVBus900527_production, 53_LVBus900528_production, 53_LVBus900529_production, 53_LVBus900530_production, 53_LVBus900531_production, 53_LVBus900532_production, 53_LVBus900533_production, 53_LVBus900534_production, 53_LVBus900535_production, 53_LVBus900536_production, 53_LVBus900539_production, 53_LVBus900540_production, 53_LVBus900542_production, 53_LVBus900543_production, 53_LVBus900545_consumption, 53_LVBus900545_production, 53_LVBus900546_consumption, 53_LVBus900546_production, 53_LVBus900548_consumption, 53_LVBus900548_production, 53_LVBus900550_consumption, 53_LVBus900550_production, 53_LVBus900552_production, 53_LVBus900553_production, 53_LVBus900554_production, 53_LVBus900556_consumption, 53_LVBus900556_production, 53_LVBus900557_production, 53_LVBus900558_production, 53_LVBus900559_production, 53_LVBus900560_production, 53_LVBus900561_production, 53_LVBus900562_consumption, 53_LVBus900562_production, 53_LVBus900563_production, 53_LVBus900564_production, 53_LVBus900565_production, 53_LVBus900566_production, 53_LVBus900567_production, 53_LVBus900568_production, 53_LVBus900569_production, 53_LVBus900570_production, 53_LVBus900571_production, 53_LVBus900572_production, 53_LVBus900573_production, 53_LVBus900575_consumption, 53_LVBus900575_production, 53_LVBus900577_consumption, 53_LVBus900577_production, 53_LVBus900579_consumption, 53_LVBus900579_production, 53_LVBus900581_consumption, 53_LVBus900581_production, 53_LVBus900583_consumption, 53_LVBus900583_production, 53_LVBus900585_consumption, 53_LVBus900585_production, 53_LVBus900587_consumption, 53_LVBus900587_production, 53_LVBus900588_consumption, 53_LVBus900588_production, 53_LVBus900589_consumption, 53_LVBus900589_production, 53_LVBus900590_consumption, 53_LVBus900590_production, 53_LVBus900591_consumption, 53_LVBus900591_production, 53_LVBus900592_consumption, 53_LVBus900592_production, 53_LVBus900593_consumption, 53_LVBus900593_production, 53_LVBus900594_consumption, 53_LVBus900594_production, 53_LVBus900596_consumption, 53_LVBus900596_production, 53_LVBus900598_consumption, 53_LVBus900598_production, 53_LVBus900600_consumption, 53_LVBus900600_production, 53_LVBus900601_consumption, 53_LVBus900601_production, 53_LVBus900602_consumption, 53_LVBus900602_production, 53_LVBus900603_production, 53_LVBus900604_consumption, 53_LVBus900604_production, 53_LVBus900605_production, 53_LVBus900606_consumption, 53_LVBus900606_production, 53_LVBus900608_consumption, 53_LVBus900608_production, 53_LVBus900609_production, 53_LVBus900610_consumption, 53_LVBus900610_production, 53_LVBus900611_production, 53_LVBus900612_consumption, 53_LVBus900612_production, 53_LVBus900613_consumption, 53_LVBus900613_production, 53_LVBus900616_consumption, 53_LVBus900616_production, 53_LVBus900617_production, 53_LVBus900618_production, 53_LVBus900619_consumption, 53_LVBus900619_production, 53_LVBus900620_production, 53_LVBus900621_consumption, 53_LVBus900621_production, 53_LVBus900622_production, 53_LVBus900623_consumption, 53_LVBus900623_production, 53_LVBus900624_production, 53_LVBus900625_production, 53_LVBus900626_production, 53_LVBus900627_consumption, 53_LVBus900627_production, 53_LVBus900629_consumption, 53_LVBus900629_production, 53_LVBus900630_consumption, 53_LVBus900630_production, 53_LVBus900631_consumption, 53_LVBus900631_production, 53_LVBus900632_consumption, 53_LVBus900632_production, 53_LVBus900633_consumption, 53_LVBus900633_production, 53_LVBus900634_consumption, 53_LVBus900634_production, 53_LVBus900637_consumption, 53_LVBus900637_production, 53_LVBus900638_consumption, 53_LVBus900638_production, 53_LVBus900639_consumption, 53_LVBus900639_production, 53_LVBus900640_consumption, 53_LVBus900640_production, 53_LVBus900641_consumption, 53_LVBus900641_production, 53_LVBus900643_consumption, 53_LVBus900643_production, 53_LVBus900644_consumption, 53_LVBus900644_production, 53_LVBus900646_production, 53_LVBus900647_production, 53_LVBus900648_production, 53_LVBus900649_production, 53_LVBus900650_production, 53_LVBus900651_production, 53_LVBus900652_production, 53_LVBus900653_production, 53_LVBus900655_production, 53_LVBus900656_production, 53_LVBus900657_production, 53_LVBus900658_production, 53_LVBus900659_production, 53_LVBus900660_production, 53_LVBus900661_production, 53_LVBus900662_production, 53_LVBus900663_production, 53_LVBus900664_production, 53_LVBus900665_production, 53_LVBus900666_production, 53_LVBus900667_production, 53_LVBus900668_production, 53_LVBus900669_consumption, 53_LVBus900669_production, 53_LVBus900670_production, 53_LVBus900672_production, 53_LVBus900673_production, 53_LVBus900674_production, 53_LVBus900675_production, 53_LVBus900676_production, 53_LVBus900677_production, 53_LVBus900678_production, 53_LVBus900679_production, 53_LVBus900680_production, 53_LVBus900681_production, 53_LVBus900682_production, 53_LVBus900683_consumption, 53_LVBus900683_production, 53_LVBus900684_production, 53_LVBus900685_production, 53_LVBus900687_production, 53_LVBus900688_production, 53_LVBus900689_production, 53_LVBus900690_production, 53_LVBus900691_production, 53_LVBus900692_production, 53_LVBus900693_production, 53_LVBus900694_consumption, 53_LVBus900694_production, 53_LVBus900696_production, 53_LVBus900697_production, 53_LVBus900698_production, 53_LVBus900699_production, 53_LVBus900700_production, 53_LVBus900701_production, 53_LVBus900702_production, 53_LVBus900703_production, 53_LVBus900704_production, 53_LVBus900705_production, 53_LVBus900707_production, 53_LVBus900708_production, 53_LVBus900709_production, 53_LVBus900710_production, 53_LVBus900711_production, 53_LVBus900712_production, 53_LVBus900713_production, 53_LVBus900714_consumption, 53_LVBus900714_production, 53_LVBus900715_consumption, 53_LVBus900715_production, 53_LVBus900731_consumption, 53_LVBus900731_production, 53_LVBus900733_production, 53_LVBus900735_consumption, 53_LVBus900735_production, 53_LVBus900736_consumption, 53_LVBus900736_production, 53_LVBus900738_production, 53_LVBus900740_production, 53_LVBus900741_production, 53_LVBus900742_production, 53_LVBus900743_production, 53_LVBus900744_production, 53_LVBus900745_production, 53_LVBus900747_production, 53_LVBus900749_consumption, 53_LVBus900749_production, 53_LVBus900750_production, 53_LVBus900751_production, 53_LVBus900752_production, 53_LVBus974592_consumption, 53_LVBus974592_production, 53_LVBus974593_production, 53_LVBus980830_consumption, 53_LVBus980830_production, 53_LVBus980974_production, 53_LVBus980984_consumption, 53_LVBus980984_production, 53_LVBus980985_consumption, 53_LVBus980985_production, 53_LVBus980986_consumption, 53_LVBus980986_production, 53_LVBus980987_production, 53_LVBus980988_consumption, 53_LVBus980988_production, 53_LVBus980989_consumption, 53_LVBus980989_production, 53_LVBus981094_production, 53_LVBus981671_consumption, 53_LVBus981671_production, 53_LVBus981672_consumption, 53_LVBus981672_production, 53_LVBus981673_production, 53_LVBus985420_consumption, 53_LVBus985420_production, 53_LVBus985421_production, 53_LVBus985422_consumption, 53_LVBus985422_production, 53_LVBus985423_consumption, 53_LVBus985423_production, 53_LVBus985424_consumption, 53_LVBus985424_production, 53_LVBus985425_consumption, 53_LVBus985425_production, 53_LVBus985426_production, 53_LVBus985427_consumption, 53_LVBus985427_production, 53_MVLV03958_production, 53_MVLV18103_consumption, 53_MVLV18103_production, 53_MVLV18466_consumption, 53_MVLV18466_production, 53_MVLV32362_consumption, 53_MVLV32362_production, 53_MVLV62280_production.

## 9. Data Quality Summary

**Total findings:** 198 (0 errors, 4 warnings, 194 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  446 of 656 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.34 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  447 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900480_consumption`  
  Load '53_LVBus900480_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900515_consumption`  
  Load '53_LVBus900515_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900711_consumption`  
  Load '53_LVBus900711_consumption' has phase imbalance of 66.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900529_consumption`  
  Load '53_LVBus900529_consumption' has phase imbalance of 87.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900530_consumption`  
  Load '53_LVBus900530_consumption' has phase imbalance of 129.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900438_consumption`  
  Load '53_LVBus900438_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900572_consumption`  
  Load '53_LVBus900572_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900652_consumption`  
  Load '53_LVBus900652_consumption' has phase imbalance of 97.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900441_consumption`  
  Load '53_LVBus900441_consumption' has phase imbalance of 43.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900570_consumption`  
  Load '53_LVBus900570_consumption' has phase imbalance of 27.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900413_consumption`  
  Load '53_LVBus900413_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900558_consumption`  
  Load '53_LVBus900558_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900620_consumption`  
  Load '53_LVBus900620_consumption' has phase imbalance of 113.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900534_consumption`  
  Load '53_LVBus900534_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900497_consumption`  
  Load '53_LVBus900497_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900693_consumption`  
  Load '53_LVBus900693_consumption' has phase imbalance of 113.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900511_consumption`  
  Load '53_LVBus900511_consumption' has phase imbalance of 149.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900751_consumption`  
  Load '53_LVBus900751_consumption' has phase imbalance of 52.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900489_consumption`  
  Load '53_LVBus900489_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900384_consumption`  
  Load '53_LVBus900384_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900666_consumption`  
  Load '53_LVBus900666_consumption' has phase imbalance of 143.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900626_consumption`  
  Load '53_LVBus900626_consumption' has phase imbalance of 68.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900678_consumption`  
  Load '53_LVBus900678_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900702_consumption`  
  Load '53_LVBus900702_consumption' has phase imbalance of 214.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900618_consumption`  
  Load '53_LVBus900618_consumption' has phase imbalance of 39.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900552_consumption`  
  Load '53_LVBus900552_consumption' has phase imbalance of 38.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900451_consumption`  
  Load '53_LVBus900451_consumption' has phase imbalance of 72.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900705_consumption`  
  Load '53_LVBus900705_consumption' has phase imbalance of 33.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900464_consumption`  
  Load '53_LVBus900464_consumption' has phase imbalance of 119.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900703_consumption`  
  Load '53_LVBus900703_consumption' has phase imbalance of 200.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900691_consumption`  
  Load '53_LVBus900691_consumption' has phase imbalance of 113.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900481_consumption`  
  Load '53_LVBus900481_consumption' has phase imbalance of 40.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900493_consumption`  
  Load '53_LVBus900493_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900700_consumption`  
  Load '53_LVBus900700_consumption' has phase imbalance of 107.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900682_consumption`  
  Load '53_LVBus900682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900469_consumption`  
  Load '53_LVBus900469_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900540_consumption`  
  Load '53_LVBus900540_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900673_consumption`  
  Load '53_LVBus900673_consumption' has phase imbalance of 33.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900420_consumption`  
  Load '53_LVBus900420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900501_consumption`  
  Load '53_LVBus900501_consumption' has phase imbalance of 70.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900698_consumption`  
  Load '53_LVBus900698_consumption' has phase imbalance of 127.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900689_consumption`  
  Load '53_LVBus900689_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900526_consumption`  
  Load '53_LVBus900526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900521_consumption`  
  Load '53_LVBus900521_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900468_consumption`  
  Load '53_LVBus900468_consumption' has phase imbalance of 113.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900663_consumption`  
  Load '53_LVBus900663_consumption' has phase imbalance of 76.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900557_consumption`  
  Load '53_LVBus900557_consumption' has phase imbalance of 64.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900470_consumption`  
  Load '53_LVBus900470_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900605_consumption`  
  Load '53_LVBus900605_consumption' has phase imbalance of 35.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900659_consumption`  
  Load '53_LVBus900659_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900422_consumption`  
  Load '53_LVBus900422_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900450_consumption`  
  Load '53_LVBus900450_consumption' has phase imbalance of 226.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900560_consumption`  
  Load '53_LVBus900560_consumption' has phase imbalance of 42.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900431_consumption`  
  Load '53_LVBus900431_consumption' has phase imbalance of 27.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900516_consumption`  
  Load '53_LVBus900516_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900554_consumption`  
  Load '53_LVBus900554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900657_consumption`  
  Load '53_LVBus900657_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900565_consumption`  
  Load '53_LVBus900565_consumption' has phase imbalance of 93.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900567_consumption`  
  Load '53_LVBus900567_consumption' has phase imbalance of 129.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900532_consumption`  
  Load '53_LVBus900532_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900363_consumption`  
  Load '53_LVBus900363_consumption' has phase imbalance of 100.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900740_consumption`  
  Load '53_LVBus900740_consumption' has phase imbalance of 127.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900687_consumption`  
  Load '53_LVBus900687_consumption' has phase imbalance of 204.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900697_consumption`  
  Load '53_LVBus900697_consumption' has phase imbalance of 47.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900707_consumption`  
  Load '53_LVBus900707_consumption' has phase imbalance of 67.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900684_consumption`  
  Load '53_LVBus900684_consumption' has phase imbalance of 93.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900535_consumption`  
  Load '53_LVBus900535_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900646_consumption`  
  Load '53_LVBus900646_consumption' has phase imbalance of 70.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900394_consumption`  
  Load '53_LVBus900394_consumption' has phase imbalance of 83.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900462_consumption`  
  Load '53_LVBus900462_consumption' has phase imbalance of 32.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900472_consumption`  
  Load '53_LVBus900472_consumption' has phase imbalance of 57.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900508_consumption`  
  Load '53_LVBus900508_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900491_consumption`  
  Load '53_LVBus900491_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900568_consumption`  
  Load '53_LVBus900568_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900561_consumption`  
  Load '53_LVBus900561_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900662_consumption`  
  Load '53_LVBus900662_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900647_consumption`  
  Load '53_LVBus900647_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900611_consumption`  
  Load '53_LVBus900611_consumption' has phase imbalance of 133.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900417_consumption`  
  Load '53_LVBus900417_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900527_consumption`  
  Load '53_LVBus900527_consumption' has phase imbalance of 76.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900421_consumption`  
  Load '53_LVBus900421_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900661_consumption`  
  Load '53_LVBus900661_consumption' has phase imbalance of 33.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900465_consumption`  
  Load '53_LVBus900465_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900437_consumption`  
  Load '53_LVBus900437_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900440_consumption`  
  Load '53_LVBus900440_consumption' has phase imbalance of 97.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900603_consumption`  
  Load '53_LVBus900603_consumption' has phase imbalance of 100.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900708_consumption`  
  Load '53_LVBus900708_consumption' has phase imbalance of 46.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900460_consumption`  
  Load '53_LVBus900460_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900539_consumption`  
  Load '53_LVBus900539_consumption' has phase imbalance of 50.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900513_consumption`  
  Load '53_LVBus900513_consumption' has phase imbalance of 21.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900651_consumption`  
  Load '53_LVBus900651_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900674_consumption`  
  Load '53_LVBus900674_consumption' has phase imbalance of 98.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus981094_consumption`  
  Load '53_LVBus981094_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900690_consumption`  
  Load '53_LVBus900690_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900742_consumption`  
  Load '53_LVBus900742_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900564_consumption`  
  Load '53_LVBus900564_consumption' has phase imbalance of 148.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900692_consumption`  
  Load '53_LVBus900692_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus974593_consumption`  
  Load '53_LVBus974593_consumption' has phase imbalance of 68.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900485_consumption`  
  Load '53_LVBus900485_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900478_consumption`  
  Load '53_LVBus900478_consumption' has phase imbalance of 41.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900531_consumption`  
  Load '53_LVBus900531_consumption' has phase imbalance of 82.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900741_consumption`  
  Load '53_LVBus900741_consumption' has phase imbalance of 112.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900566_consumption`  
  Load '53_LVBus900566_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900452_consumption`  
  Load '53_LVBus900452_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900517_consumption`  
  Load '53_LVBus900517_consumption' has phase imbalance of 28.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900648_consumption`  
  Load '53_LVBus900648_consumption' has phase imbalance of 86.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900563_consumption`  
  Load '53_LVBus900563_consumption' has phase imbalance of 137.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900364_consumption`  
  Load '53_LVBus900364_consumption' has phase imbalance of 91.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus985421_consumption`  
  Load '53_LVBus985421_consumption' has phase imbalance of 41.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900672_consumption`  
  Load '53_LVBus900672_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900617_consumption`  
  Load '53_LVBus900617_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900680_consumption`  
  Load '53_LVBus900680_consumption' has phase imbalance of 184.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900664_consumption`  
  Load '53_LVBus900664_consumption' has phase imbalance of 101.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900660_consumption`  
  Load '53_LVBus900660_consumption' has phase imbalance of 92.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900653_consumption`  
  Load '53_LVBus900653_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900750_consumption`  
  Load '53_LVBus900750_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900681_consumption`  
  Load '53_LVBus900681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900446_consumption`  
  Load '53_LVBus900446_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900429_consumption`  
  Load '53_LVBus900429_consumption' has phase imbalance of 21.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900433_consumption`  
  Load '53_LVBus900433_consumption' has phase imbalance of 23.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900712_consumption`  
  Load '53_LVBus900712_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900509_consumption`  
  Load '53_LVBus900509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900685_consumption`  
  Load '53_LVBus900685_consumption' has phase imbalance of 257.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900500_consumption`  
  Load '53_LVBus900500_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900668_consumption`  
  Load '53_LVBus900668_consumption' has phase imbalance of 122.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900679_consumption`  
  Load '53_LVBus900679_consumption' has phase imbalance of 57.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900518_consumption`  
  Load '53_LVBus900518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900424_consumption`  
  Load '53_LVBus900424_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900553_consumption`  
  Load '53_LVBus900553_consumption' has phase imbalance of 51.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900522_consumption`  
  Load '53_LVBus900522_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900423_consumption`  
  Load '53_LVBus900423_consumption' has phase imbalance of 106.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900459_consumption`  
  Load '53_LVBus900459_consumption' has phase imbalance of 61.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900506_consumption`  
  Load '53_LVBus900506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900658_consumption`  
  Load '53_LVBus900658_consumption' has phase imbalance of 108.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900559_consumption`  
  Load '53_LVBus900559_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900542_consumption`  
  Load '53_LVBus900542_consumption' has phase imbalance of 103.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900675_consumption`  
  Load '53_LVBus900675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900471_consumption`  
  Load '53_LVBus900471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900710_consumption`  
  Load '53_LVBus900710_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900747_consumption`  
  Load '53_LVBus900747_consumption' has phase imbalance of 73.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900425_consumption`  
  Load '53_LVBus900425_consumption' has phase imbalance of 194.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900533_consumption`  
  Load '53_LVBus900533_consumption' has phase imbalance of 147.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900436_consumption`  
  Load '53_LVBus900436_consumption' has phase imbalance of 28.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900713_consumption`  
  Load '53_LVBus900713_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900699_consumption`  
  Load '53_LVBus900699_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900738_consumption`  
  Load '53_LVBus900738_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900752_consumption`  
  Load '53_LVBus900752_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900667_consumption`  
  Load '53_LVBus900667_consumption' has phase imbalance of 71.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900388_consumption`  
  Load '53_LVBus900388_consumption' has phase imbalance of 42.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900688_consumption`  
  Load '53_LVBus900688_consumption' has phase imbalance of 48.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900696_consumption`  
  Load '53_LVBus900696_consumption' has phase imbalance of 59.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900399_consumption`  
  Load '53_LVBus900399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900670_consumption`  
  Load '53_LVBus900670_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900609_consumption`  
  Load '53_LVBus900609_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900461_consumption`  
  Load '53_LVBus900461_consumption' has phase imbalance of 118.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900655_consumption`  
  Load '53_LVBus900655_consumption' has phase imbalance of 22.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900528_consumption`  
  Load '53_LVBus900528_consumption' has phase imbalance of 23.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900475_consumption`  
  Load '53_LVBus900475_consumption' has phase imbalance of 28.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900543_consumption`  
  Load '53_LVBus900543_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900677_consumption`  
  Load '53_LVBus900677_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900409_consumption`  
  Load '53_LVBus900409_consumption' has phase imbalance of 106.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900392_consumption`  
  Load '53_LVBus900392_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900454_consumption`  
  Load '53_LVBus900454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900512_consumption`  
  Load '53_LVBus900512_consumption' has phase imbalance of 85.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900523_consumption`  
  Load '53_LVBus900523_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus985426_consumption`  
  Load '53_LVBus985426_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900487_consumption`  
  Load '53_LVBus900487_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900649_consumption`  
  Load '53_LVBus900649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900704_consumption`  
  Load '53_LVBus900704_consumption' has phase imbalance of 77.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900507_consumption`  
  Load '53_LVBus900507_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900743_consumption`  
  Load '53_LVBus900743_consumption' has phase imbalance of 123.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900467_consumption`  
  Load '53_LVBus900467_consumption' has phase imbalance of 242.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900536_consumption`  
  Load '53_LVBus900536_consumption' has phase imbalance of 75.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900665_consumption`  
  Load '53_LVBus900665_consumption' has phase imbalance of 55.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus980987_consumption`  
  Load '53_LVBus980987_consumption' has phase imbalance of 32.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900701_consumption`  
  Load '53_LVBus900701_consumption' has phase imbalance of 191.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900676_consumption`  
  Load '53_LVBus900676_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus900650_consumption`  
  Load '53_LVBus900650_consumption' has phase imbalance of 71.9%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 656 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_KEROL' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus900731' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  351 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  39 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 53_LVBus900399_consumption, 53_LVBus900417_consumption, 53_LVBus900420_consumption, 53_LVBus900421_consumption, 53_LVBus900422_consumption, 53_LVBus900424_consumption, 53_LVBus900425_consumption, 53_LVBus900438_consumption, 53_LVBus900450_consumption, 53_LVBus900454_consumption, 53_LVBus900465_consumption, 53_LVBus900470_consumption, 53_LVBus900471_consumption, 53_LVBus900491_consumption, 53_LVBus900500_consumption, 53_LVBus900506_consumption, 53_LVBus900507_consumption, 53_LVBus900508_consumption, 53_LVBus900509_consumption, 53_LVBus900518_consumption, 53_LVBus900523_consumption, 53_LVBus900526_consumption, 53_LVBus900532_consumption, 53_LVBus900535_consumption, 53_LVBus900554_consumption, 53_LVBus900559_consumption, 53_LVBus900617_consumption, 53_LVBus900649_consumption, 53_LVBus900662_consumption, 53_LVBus900672_consumption, 53_LVBus900675_consumption, 53_LVBus900681_consumption, 53_LVBus900682_consumption, 53_LVBus900685_consumption, 53_LVBus900690_consumption, 53_LVBus900701_consumption, 53_LVBus900712_consumption, 53_LVBus900738_consumption, 53_LVBus900752_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  328 group(s) of loads (656 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  447 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus900363_production, 53_LVBus900364_production, 53_LVBus900366_consumption, 53_LVBus900366_production, 53_LVBus900367_consumption, 53_LVBus900367_production, 53_LVBus900369_consumption, 53_LVBus900369_production, 53_LVBus900371_consumption, 53_LVBus900371_production, 53_LVBus900372_consumption, 53_LVBus900372_production, 53_LVBus900373_consumption, 53_LVBus900373_production, 53_LVBus900374_consumption, 53_LVBus900374_production, 53_LVBus900375_consumption, 53_LVBus900375_production, 53_LVBus900376_consumption, 53_LVBus900376_production, 53_LVBus900377_production, 53_LVBus900378_consumption, 53_LVBus900378_production, 53_LVBus900379_consumption, 53_LVBus900379_production, 53_LVBus900381_consumption, 53_LVBus900381_production, 53_LVBus900383_consumption, 53_LVBus900383_production, 53_LVBus900384_production, 53_LVBus900385_consumption, 53_LVBus900385_production, 53_LVBus900386_consumption, 53_LVBus900386_production, 53_LVBus900388_production, 53_LVBus900390_consumption, 53_LVBus900390_production, 53_LVBus900392_production, 53_LVBus900394_production, 53_LVBus900395_consumption, 53_LVBus900395_production, 53_LVBus900396_consumption, 53_LVBus900396_production, 53_LVBus900397_consumption, 53_LVBus900397_production, 53_LVBus900398_production, 53_LVBus900399_production, 53_LVBus900400_consumption, 53_LVBus900400_production, 53_LVBus900401_consumption, 53_LVBus900401_production, 53_LVBus900403_consumption, 53_LVBus900403_production, 53_LVBus900405_production, 53_LVBus900407_production, 53_LVBus900408_consumption, 53_LVBus900408_production, 53_LVBus900409_production, 53_LVBus900410_consumption, 53_LVBus900410_production, 53_LVBus900412_consumption, 53_LVBus900412_production, 53_LVBus900413_production, 53_LVBus900414_production, 53_LVBus900415_consumption, 53_LVBus900415_production, 53_LVBus900417_production, 53_LVBus900418_consumption, 53_LVBus900418_production, 53_LVBus900420_production, 53_LVBus900421_production, 53_LVBus900422_production, 53_LVBus900423_production, 53_LVBus900424_production, 53_LVBus900425_production, 53_LVBus900426_production, 53_LVBus900428_consumption, 53_LVBus900428_production, 53_LVBus900429_production, 53_LVBus900431_production, 53_LVBus900433_production, 53_LVBus900435_consumption, 53_LVBus900435_production, 53_LVBus900436_production, 53_LVBus900437_production, 53_LVBus900438_production, 53_LVBus900439_production, 53_LVBus900440_production, 53_LVBus900441_production, 53_LVBus900443_consumption, 53_LVBus900443_production, 53_LVBus900444_consumption, 53_LVBus900444_production, 53_LVBus900446_production, 53_LVBus900447_consumption, 53_LVBus900447_production, 53_LVBus900449_consumption, 53_LVBus900449_production, 53_LVBus900450_production, 53_LVBus900451_production, 53_LVBus900452_production, 53_LVBus900453_production, 53_LVBus900454_production, 53_LVBus900455_consumption, 53_LVBus900455_production, 53_LVBus900456_consumption, 53_LVBus900456_production, 53_LVBus900457_production, 53_LVBus900459_production, 53_LVBus900460_production, 53_LVBus900461_production, 53_LVBus900462_production, 53_LVBus900464_production, 53_LVBus900465_production, 53_LVBus900467_production, 53_LVBus900468_production, 53_LVBus900469_production, 53_LVBus900470_production, 53_LVBus900471_production, 53_LVBus900472_production, 53_LVBus900475_production, 53_LVBus900476_consumption, 53_LVBus900476_production, 53_LVBus900478_production, 53_LVBus900479_consumption, 53_LVBus900479_production, 53_LVBus900480_production, 53_LVBus900481_production, 53_LVBus900482_production, 53_LVBus900484_consumption, 53_LVBus900484_production, 53_LVBus900485_production, 53_LVBus900486_consumption, 53_LVBus900486_production, 53_LVBus900487_production, 53_LVBus900488_consumption, 53_LVBus900488_production, 53_LVBus900489_production, 53_LVBus900490_consumption, 53_LVBus900490_production, 53_LVBus900491_production, 53_LVBus900493_production, 53_LVBus900494_production, 53_LVBus900496_production, 53_LVBus900497_production, 53_LVBus900498_production, 53_LVBus900500_production, 53_LVBus900501_production, 53_LVBus900502_production, 53_LVBus900503_consumption, 53_LVBus900503_production, 53_LVBus900506_production, 53_LVBus900507_production, 53_LVBus900508_production, 53_LVBus900509_production, 53_LVBus900510_consumption, 53_LVBus900510_production, 53_LVBus900511_production, 53_LVBus900512_production, 53_LVBus900513_production, 53_LVBus900515_production, 53_LVBus900516_production, 53_LVBus900517_production, 53_LVBus900518_production, 53_LVBus900520_production, 53_LVBus900521_production, 53_LVBus900522_production, 53_LVBus900523_production, 53_LVBus900524_production, 53_LVBus900526_production, 53_LVBus900527_production, 53_LVBus900528_production, 53_LVBus900529_production, 53_LVBus900530_production, 53_LVBus900531_production, 53_LVBus900532_production, 53_LVBus900533_production, 53_LVBus900534_production, 53_LVBus900535_production, 53_LVBus900536_production, 53_LVBus900539_production, 53_LVBus900540_production, 53_LVBus900542_production, 53_LVBus900543_production, 53_LVBus900545_consumption, 53_LVBus900545_production, 53_LVBus900546_consumption, 53_LVBus900546_production, 53_LVBus900548_consumption, 53_LVBus900548_production, 53_LVBus900550_consumption, 53_LVBus900550_production, 53_LVBus900552_production, 53_LVBus900553_production, 53_LVBus900554_production, 53_LVBus900556_consumption, 53_LVBus900556_production, 53_LVBus900557_production, 53_LVBus900558_production, 53_LVBus900559_production, 53_LVBus900560_production, 53_LVBus900561_production, 53_LVBus900562_consumption, 53_LVBus900562_production, 53_LVBus900563_production, 53_LVBus900564_production, 53_LVBus900565_production, 53_LVBus900566_production, 53_LVBus900567_production, 53_LVBus900568_production, 53_LVBus900569_production, 53_LVBus900570_production, 53_LVBus900571_production, 53_LVBus900572_production, 53_LVBus900573_production, 53_LVBus900575_consumption, 53_LVBus900575_production, 53_LVBus900577_consumption, 53_LVBus900577_production, 53_LVBus900579_consumption, 53_LVBus900579_production, 53_LVBus900581_consumption, 53_LVBus900581_production, 53_LVBus900583_consumption, 53_LVBus900583_production, 53_LVBus900585_consumption, 53_LVBus900585_production, 53_LVBus900587_consumption, 53_LVBus900587_production, 53_LVBus900588_consumption, 53_LVBus900588_production, 53_LVBus900589_consumption, 53_LVBus900589_production, 53_LVBus900590_consumption, 53_LVBus900590_production, 53_LVBus900591_consumption, 53_LVBus900591_production, 53_LVBus900592_consumption, 53_LVBus900592_production, 53_LVBus900593_consumption, 53_LVBus900593_production, 53_LVBus900594_consumption, 53_LVBus900594_production, 53_LVBus900596_consumption, 53_LVBus900596_production, 53_LVBus900598_consumption, 53_LVBus900598_production, 53_LVBus900600_consumption, 53_LVBus900600_production, 53_LVBus900601_consumption, 53_LVBus900601_production, 53_LVBus900602_consumption, 53_LVBus900602_production, 53_LVBus900603_production, 53_LVBus900604_consumption, 53_LVBus900604_production, 53_LVBus900605_production, 53_LVBus900606_consumption, 53_LVBus900606_production, 53_LVBus900608_consumption, 53_LVBus900608_production, 53_LVBus900609_production, 53_LVBus900610_consumption, 53_LVBus900610_production, 53_LVBus900611_production, 53_LVBus900612_consumption, 53_LVBus900612_production, 53_LVBus900613_consumption, 53_LVBus900613_production, 53_LVBus900616_consumption, 53_LVBus900616_production, 53_LVBus900617_production, 53_LVBus900618_production, 53_LVBus900619_consumption, 53_LVBus900619_production, 53_LVBus900620_production, 53_LVBus900621_consumption, 53_LVBus900621_production, 53_LVBus900622_production, 53_LVBus900623_consumption, 53_LVBus900623_production, 53_LVBus900624_production, 53_LVBus900625_production, 53_LVBus900626_production, 53_LVBus900627_consumption, 53_LVBus900627_production, 53_LVBus900629_consumption, 53_LVBus900629_production, 53_LVBus900630_consumption, 53_LVBus900630_production, 53_LVBus900631_consumption, 53_LVBus900631_production, 53_LVBus900632_consumption, 53_LVBus900632_production, 53_LVBus900633_consumption, 53_LVBus900633_production, 53_LVBus900634_consumption, 53_LVBus900634_production, 53_LVBus900637_consumption, 53_LVBus900637_production, 53_LVBus900638_consumption, 53_LVBus900638_production, 53_LVBus900639_consumption, 53_LVBus900639_production, 53_LVBus900640_consumption, 53_LVBus900640_production, 53_LVBus900641_consumption, 53_LVBus900641_production, 53_LVBus900643_consumption, 53_LVBus900643_production, 53_LVBus900644_consumption, 53_LVBus900644_production, 53_LVBus900646_production, 53_LVBus900647_production, 53_LVBus900648_production, 53_LVBus900649_production, 53_LVBus900650_production, 53_LVBus900651_production, 53_LVBus900652_production, 53_LVBus900653_production, 53_LVBus900655_production, 53_LVBus900656_production, 53_LVBus900657_production, 53_LVBus900658_production, 53_LVBus900659_production, 53_LVBus900660_production, 53_LVBus900661_production, 53_LVBus900662_production, 53_LVBus900663_production, 53_LVBus900664_production, 53_LVBus900665_production, 53_LVBus900666_production, 53_LVBus900667_production, 53_LVBus900668_production, 53_LVBus900669_consumption, 53_LVBus900669_production, 53_LVBus900670_production, 53_LVBus900672_production, 53_LVBus900673_production, 53_LVBus900674_production, 53_LVBus900675_production, 53_LVBus900676_production, 53_LVBus900677_production, 53_LVBus900678_production, 53_LVBus900679_production, 53_LVBus900680_production, 53_LVBus900681_production, 53_LVBus900682_production, 53_LVBus900683_consumption, 53_LVBus900683_production, 53_LVBus900684_production, 53_LVBus900685_production, 53_LVBus900687_production, 53_LVBus900688_production, 53_LVBus900689_production, 53_LVBus900690_production, 53_LVBus900691_production, 53_LVBus900692_production, 53_LVBus900693_production, 53_LVBus900694_consumption, 53_LVBus900694_production, 53_LVBus900696_production, 53_LVBus900697_production, 53_LVBus900698_production, 53_LVBus900699_production, 53_LVBus900700_production, 53_LVBus900701_production, 53_LVBus900702_production, 53_LVBus900703_production, 53_LVBus900704_production, 53_LVBus900705_production, 53_LVBus900707_production, 53_LVBus900708_production, 53_LVBus900709_production, 53_LVBus900710_production, 53_LVBus900711_production, 53_LVBus900712_production, 53_LVBus900713_production, 53_LVBus900714_consumption, 53_LVBus900714_production, 53_LVBus900715_consumption, 53_LVBus900715_production, 53_LVBus900731_consumption, 53_LVBus900731_production, 53_LVBus900733_production, 53_LVBus900735_consumption, 53_LVBus900735_production, 53_LVBus900736_consumption, 53_LVBus900736_production, 53_LVBus900738_production, 53_LVBus900740_production, 53_LVBus900741_production, 53_LVBus900742_production, 53_LVBus900743_production, 53_LVBus900744_production, 53_LVBus900745_production, 53_LVBus900747_production, 53_LVBus900749_consumption, 53_LVBus900749_production, 53_LVBus900750_production, 53_LVBus900751_production, 53_LVBus900752_production, 53_LVBus974592_consumption, 53_LVBus974592_production, 53_LVBus974593_production, 53_LVBus980830_consumption, 53_LVBus980830_production, 53_LVBus980974_production, 53_LVBus980984_consumption, 53_LVBus980984_production, 53_LVBus980985_consumption, 53_LVBus980985_production, 53_LVBus980986_consumption, 53_LVBus980986_production, 53_LVBus980987_production, 53_LVBus980988_consumption, 53_LVBus980988_production, 53_LVBus980989_consumption, 53_LVBus980989_production, 53_LVBus981094_production, 53_LVBus981671_consumption, 53_LVBus981671_production, 53_LVBus981672_consumption, 53_LVBus981672_production, 53_LVBus981673_production, 53_LVBus985420_consumption, 53_LVBus985420_production, 53_LVBus985421_production, 53_LVBus985422_consumption, 53_LVBus985422_production, 53_LVBus985423_consumption, 53_LVBus985423_production, 53_LVBus985424_consumption, 53_LVBus985424_production, 53_LVBus985425_consumption, 53_LVBus985425_production, 53_LVBus985426_production, 53_LVBus985427_consumption, 53_LVBus985427_production, 53_MVLV03958_production, 53_MVLV18103_consumption, 53_MVLV18103_production, 53_MVLV18466_consumption, 53_MVLV18466_production, 53_MVLV32362_consumption, 53_MVLV32362_production, 53_MVLV62280_production.

