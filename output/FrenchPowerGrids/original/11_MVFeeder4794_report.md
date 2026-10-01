# BMOPF Network Summary: 11_MVFeeder4794

**Generated:** 2026-10-01 23:33:57  
**Findings:** 0 errors · 5 warnings · 414 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 668 |  |
| line | 657 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 1290 | 1.022 MW, 306.5 kvar |
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
| MV_11.8kV | 11.78 kV | 16 | 15 | 6 | 0 |
| LV_236V | 236.0 V | 652 | 642 | 1284 | 0 |

**Transformer transitions:**

- `11_MVLV27505_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV44560_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV44608_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV46894_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV06438_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV46898_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV09763_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV23105_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV23109_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV52403_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 15 |
| Degree-1 buses | 212 |
| Tree depth (max hops) | 45 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 668 | 1 | 667 | 0 | 0 | 0 |
| Tier LV_236V | 652 | 10 | 642 | 0 | 0 | 0 |
| Tier MV_11.8kV | 16 | 1 | 15 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 10; skipped invalid branches: 0.

Galvanic zones: 11; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_MVBus81137 | MV_11.8kV | 16 | 0 | 0 | 10 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2656 declared bus terminals; 2613 mapped line/closed-switch conductor edges; 43 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 11000.0 | 2.717 | 3870 |
| q_nom | 0.0 | 3300.0 | 2.717 | 3870 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.47 | 766.0 | 1.233 | 657 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 3.47e6 | 1.294 | 10 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 834 of 1290 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369242_consumption' has phase imbalance of 63.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369200_consumption' has phase imbalance of 102.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891819_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370357_consumption' has phase imbalance of 37.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891875_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891734_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1297804_consumption' has phase imbalance of 240.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891729_consumption' has phase imbalance of 173.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891452_consumption' has phase imbalance of 67.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891363_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891349_consumption' has phase imbalance of 20.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369206_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891550_consumption' has phase imbalance of 195.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369180_consumption' has phase imbalance of 203.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891792_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891575_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891539_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891628_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891576_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891560_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369172_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286520_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286523_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370354_consumption' has phase imbalance of 99.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369275_consumption' has phase imbalance of 41.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891514_consumption' has phase imbalance of 84.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891812_consumption' has phase imbalance of 31.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891728_consumption' has phase imbalance of 168.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891753_consumption' has phase imbalance of 76.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891766_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891369_consumption' has phase imbalance of 142.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891700_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891456_consumption' has phase imbalance of 98.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891540_consumption' has phase imbalance of 112.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1303382_consumption' has phase imbalance of 270.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891339_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891854_consumption' has phase imbalance of 159.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891569_consumption' has phase imbalance of 62.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891621_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891654_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891706_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891666_consumption' has phase imbalance of 122.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891746_consumption' has phase imbalance of 72.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891537_consumption' has phase imbalance of 110.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891778_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891570_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891472_consumption' has phase imbalance of 106.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369230_consumption' has phase imbalance of 117.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891594_consumption' has phase imbalance of 68.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370359_consumption' has phase imbalance of 96.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891744_consumption' has phase imbalance of 214.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286521_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891458_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370352_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891750_consumption' has phase imbalance of 83.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891822_consumption' has phase imbalance of 48.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369183_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891554_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891786_consumption' has phase imbalance of 209.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891776_consumption' has phase imbalance of 74.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370348_consumption' has phase imbalance of 244.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1284260_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369201_consumption' has phase imbalance of 123.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891616_consumption' has phase imbalance of 79.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891850_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891663_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369173_consumption' has phase imbalance of 262.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891800_consumption' has phase imbalance of 200.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891572_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891615_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891632_consumption' has phase imbalance of 194.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891507_consumption' has phase imbalance of 44.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891668_consumption' has phase imbalance of 278.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891782_consumption' has phase imbalance of 24.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891688_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891667_consumption' has phase imbalance of 57.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370351_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369165_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891592_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891556_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891755_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891697_consumption' has phase imbalance of 198.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891874_consumption' has phase imbalance of 24.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891588_consumption' has phase imbalance of 130.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369182_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891358_consumption' has phase imbalance of 47.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891791_consumption' has phase imbalance of 80.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891824_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891855_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1303379_consumption' has phase imbalance of 31.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891361_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891727_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891574_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369273_consumption' has phase imbalance of 121.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369196_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891846_consumption' has phase imbalance of 131.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891382_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891783_consumption' has phase imbalance of 136.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369241_consumption' has phase imbalance of 67.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891831_consumption' has phase imbalance of 53.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891633_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891780_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891429_consumption' has phase imbalance of 29.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891857_consumption' has phase imbalance of 84.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891348_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891491_consumption' has phase imbalance of 142.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891802_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891866_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369175_consumption' has phase imbalance of 79.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891676_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891852_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891557_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369228_consumption' has phase imbalance of 46.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891530_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891360_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891328_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891528_consumption' has phase imbalance of 116.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891597_consumption' has phase imbalance of 257.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369208_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369272_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891559_consumption' has phase imbalance of 142.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891441_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891671_consumption' has phase imbalance of 51.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891536_consumption' has phase imbalance of 78.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369204_consumption' has phase imbalance of 23.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891475_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891606_consumption' has phase imbalance of 95.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370358_consumption' has phase imbalance of 53.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369186_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891455_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891862_consumption' has phase imbalance of 75.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891721_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891620_consumption' has phase imbalance of 90.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891726_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1282566_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891571_consumption' has phase imbalance of 130.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891542_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891761_consumption' has phase imbalance of 40.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891631_consumption' has phase imbalance of 89.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369234_consumption' has phase imbalance of 71.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891499_consumption' has phase imbalance of 78.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1297801_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891830_consumption' has phase imbalance of 101.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891357_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369199_consumption' has phase imbalance of 74.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891674_consumption' has phase imbalance of 58.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891828_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891419_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891531_consumption' has phase imbalance of 42.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369185_consumption' has phase imbalance of 65.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891549_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891695_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891543_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1284908_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891679_consumption' has phase imbalance of 193.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891347_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891437_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1297803_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891362_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891748_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891818_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1297799_consumption' has phase imbalance of 148.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369249_consumption' has phase imbalance of 124.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891430_consumption' has phase imbalance of 121.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891587_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891567_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369247_consumption' has phase imbalance of 140.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891779_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891578_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369216_consumption' has phase imbalance of 153.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1282567_consumption' has phase imbalance of 117.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891563_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891738_consumption' has phase imbalance of 70.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891813_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891839_consumption' has phase imbalance of 225.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891492_consumption' has phase imbalance of 244.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891773_consumption' has phase imbalance of 103.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1297800_consumption' has phase imbalance of 143.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891477_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891636_consumption' has phase imbalance of 107.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891710_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891661_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369223_consumption' has phase imbalance of 112.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891842_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891466_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369169_consumption' has phase imbalance of 112.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891664_consumption' has phase imbalance of 83.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891823_consumption' has phase imbalance of 53.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891551_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891747_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891337_consumption' has phase imbalance of 259.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891836_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891740_consumption' has phase imbalance of 97.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891829_consumption' has phase imbalance of 37.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891489_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891487_consumption' has phase imbalance of 220.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891817_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369267_consumption' has phase imbalance of 30.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891825_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370345_consumption' has phase imbalance of 47.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369178_consumption' has phase imbalance of 131.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891546_consumption' has phase imbalance of 229.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891767_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891617_consumption' has phase imbalance of 93.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891763_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891408_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891604_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370347_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891806_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891639_consumption' has phase imbalance of 76.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369166_consumption' has phase imbalance of 114.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286516_consumption' has phase imbalance of 80.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891708_consumption' has phase imbalance of 79.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891789_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891428_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891796_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891788_consumption' has phase imbalance of 146.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891838_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286522_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1282565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891799_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1303380_consumption' has phase imbalance of 46.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891696_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891670_consumption' has phase imbalance of 119.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891691_consumption' has phase imbalance of 238.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891677_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891643_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891548_consumption' has phase imbalance of 246.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369236_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891859_consumption' has phase imbalance of 73.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891598_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286519_consumption' has phase imbalance of 33.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891856_consumption' has phase imbalance of 29.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891718_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891601_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891534_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891338_consumption' has phase imbalance of 107.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891787_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891547_consumption' has phase imbalance of 106.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891439_consumption' has phase imbalance of 125.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369209_consumption' has phase imbalance of 85.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891646_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369214_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891832_consumption' has phase imbalance of 268.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369255_consumption' has phase imbalance of 58.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891467_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369235_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891457_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1297802_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369257_consumption' has phase imbalance of 57.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891864_consumption' has phase imbalance of 98.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891454_consumption' has phase imbalance of 91.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891581_consumption' has phase imbalance of 226.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891619_consumption' has phase imbalance of 28.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370356_consumption' has phase imbalance of 59.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891545_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891877_consumption' has phase imbalance of 48.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891801_consumption' has phase imbalance of 255.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891768_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891731_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891835_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891552_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891793_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369211_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891630_consumption' has phase imbalance of 121.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891476_consumption' has phase imbalance of 118.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1284910_consumption' has phase imbalance of 156.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891568_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1284913_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891656_consumption' has phase imbalance of 133.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891703_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891589_consumption' has phase imbalance of 47.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891585_consumption' has phase imbalance of 38.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369238_consumption' has phase imbalance of 102.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891678_consumption' has phase imbalance of 91.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891709_consumption' has phase imbalance of 162.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891686_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891741_consumption' has phase imbalance of 41.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891754_consumption' has phase imbalance of 129.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891694_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369276_consumption' has phase imbalance of 79.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1303381_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369210_consumption' has phase imbalance of 25.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891561_consumption' has phase imbalance of 104.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891765_consumption' has phase imbalance of 78.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891359_consumption' has phase imbalance of 110.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891416_consumption' has phase imbalance of 28.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891715_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891863_consumption' has phase imbalance of 107.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891680_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891665_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369239_consumption' has phase imbalance of 66.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286517_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369167_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891635_consumption' has phase imbalance of 200.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891662_consumption' has phase imbalance of 214.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891840_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369198_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891707_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891693_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370343_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369250_consumption' has phase imbalance of 40.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891648_consumption' has phase imbalance of 286.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891449_consumption' has phase imbalance of 111.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891600_consumption' has phase imbalance of 233.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1286524_consumption' has phase imbalance of 41.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369207_consumption' has phase imbalance of 58.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891595_consumption' has phase imbalance of 74.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891634_consumption' has phase imbalance of 221.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891535_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891774_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369245_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891804_consumption' has phase imbalance of 232.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369197_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891533_consumption' has phase imbalance of 299.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891413_consumption' has phase imbalance of 64.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369277_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369220_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891775_consumption' has phase imbalance of 74.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891566_consumption' has phase imbalance of 139.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891558_consumption' has phase imbalance of 85.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891453_consumption' has phase imbalance of 120.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891827_consumption' has phase imbalance of 175.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891431_consumption' has phase imbalance of 263.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369227_consumption' has phase imbalance of 68.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891553_consumption' has phase imbalance of 101.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369271_consumption' has phase imbalance of 89.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891865_consumption' has phase imbalance of 69.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891544_consumption' has phase imbalance of 295.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891724_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891732_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369254_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891564_consumption' has phase imbalance of 136.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369243_consumption' has phase imbalance of 132.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891565_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891760_consumption' has phase imbalance of 167.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891596_consumption' has phase imbalance of 86.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891464_consumption' has phase imbalance of 78.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891809_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369221_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369177_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891751_consumption' has phase imbalance of 47.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891465_consumption' has phase imbalance of 50.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891736_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891772_consumption' has phase imbalance of 94.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891653_consumption' has phase imbalance of 105.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1370344_consumption' has phase imbalance of 97.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1369229_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891488_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0891644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1284909_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1290 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_V.GEO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.022 MW |
| Total load Q | 306.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV27505_Transformer | 693.0 kVA | 24.4% |
| 11_MVLV44560_Transformer | 3.47 MVA | 7.3% |
| 11_MVLV44608_Transformer | 440.0 kVA | 21.6% |
| 11_MVLV46894_Transformer | 693.0 kVA | 19.4% |
| 11_MVLV06438_Transformer | 440.0 kVA | 13.2% |
| 11_MVLV46898_Transformer | 440.0 kVA | 19.7% |
| 11_MVLV09763_Transformer | 275.0 kVA | 15.0% |
| 11_MVLV23105_Transformer | 110.0 kVA | 12.4% |
| 11_MVLV23109_Transformer | 693.0 kVA | 19.8% |
| 11_MVLV52403_Transformer | 275.0 kVA | 16.6% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.02 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '11_LVBus0891587' (LV, 0.24 kV) has an electrical reach of 1.2 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 668 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 668 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 16 |
| LV_236V | 4-wire | 652 / 652 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 652 |
| Neutral branches | 642 |
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
| 11.78 kV | 16 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 46 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 83 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 59 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 203 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 59 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 80 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 41 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 221.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 652 / 16 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 835 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 835 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0891328_production, 11_LVBus0891330_production, 11_LVBus0891332_consumption, 11_LVBus0891332_production, 11_LVBus0891333_production, 11_LVBus0891334_consumption, 11_LVBus0891334_production, 11_LVBus0891335_consumption, 11_LVBus0891335_production, 11_LVBus0891336_consumption, 11_LVBus0891336_production, 11_LVBus0891337_production, 11_LVBus0891338_production, 11_LVBus0891339_production, 11_LVBus0891340_production, 11_LVBus0891341_production, 11_LVBus0891342_production, 11_LVBus0891344_consumption, 11_LVBus0891344_production, 11_LVBus0891346_consumption, 11_LVBus0891346_production, 11_LVBus0891347_production, 11_LVBus0891348_production, 11_LVBus0891349_production, 11_LVBus0891351_consumption, 11_LVBus0891351_production, 11_LVBus0891352_consumption, 11_LVBus0891352_production, 11_LVBus0891354_consumption, 11_LVBus0891354_production, 11_LVBus0891355_production, 11_LVBus0891356_production, 11_LVBus0891357_production, 11_LVBus0891358_production, 11_LVBus0891359_production, 11_LVBus0891360_production, 11_LVBus0891361_production, 11_LVBus0891362_production, 11_LVBus0891363_production, 11_LVBus0891365_consumption, 11_LVBus0891365_production, 11_LVBus0891367_consumption, 11_LVBus0891367_production, 11_LVBus0891368_consumption, 11_LVBus0891368_production, 11_LVBus0891369_production, 11_LVBus0891370_consumption, 11_LVBus0891370_production, 11_LVBus0891371_consumption, 11_LVBus0891371_production, 11_LVBus0891373_production, 11_LVBus0891375_consumption, 11_LVBus0891375_production, 11_LVBus0891376_consumption, 11_LVBus0891376_production, 11_LVBus0891378_consumption, 11_LVBus0891378_production, 11_LVBus0891379_consumption, 11_LVBus0891379_production, 11_LVBus0891380_consumption, 11_LVBus0891380_production, 11_LVBus0891381_consumption, 11_LVBus0891381_production, 11_LVBus0891382_production, 11_LVBus0891383_consumption, 11_LVBus0891383_production, 11_LVBus0891385_consumption, 11_LVBus0891385_production, 11_LVBus0891386_consumption, 11_LVBus0891386_production, 11_LVBus0891387_consumption, 11_LVBus0891387_production, 11_LVBus0891388_consumption, 11_LVBus0891388_production, 11_LVBus0891389_consumption, 11_LVBus0891389_production, 11_LVBus0891390_consumption, 11_LVBus0891390_production, 11_LVBus0891391_consumption, 11_LVBus0891391_production, 11_LVBus0891392_consumption, 11_LVBus0891392_production, 11_LVBus0891393_consumption, 11_LVBus0891393_production, 11_LVBus0891394_consumption, 11_LVBus0891394_production, 11_LVBus0891395_production, 11_LVBus0891396_production, 11_LVBus0891397_consumption, 11_LVBus0891397_production, 11_LVBus0891399_consumption, 11_LVBus0891399_production, 11_LVBus0891400_consumption, 11_LVBus0891400_production, 11_LVBus0891401_consumption, 11_LVBus0891401_production, 11_LVBus0891402_consumption, 11_LVBus0891402_production, 11_LVBus0891403_consumption, 11_LVBus0891403_production, 11_LVBus0891404_consumption, 11_LVBus0891404_production, 11_LVBus0891405_consumption, 11_LVBus0891405_production, 11_LVBus0891406_consumption, 11_LVBus0891406_production, 11_LVBus0891408_production, 11_LVBus0891410_consumption, 11_LVBus0891410_production, 11_LVBus0891411_consumption, 11_LVBus0891411_production, 11_LVBus0891412_consumption, 11_LVBus0891412_production, 11_LVBus0891413_production, 11_LVBus0891414_consumption, 11_LVBus0891414_production, 11_LVBus0891415_consumption, 11_LVBus0891415_production, 11_LVBus0891416_production, 11_LVBus0891417_consumption, 11_LVBus0891417_production, 11_LVBus0891419_production, 11_LVBus0891421_consumption, 11_LVBus0891421_production, 11_LVBus0891422_consumption, 11_LVBus0891422_production, 11_LVBus0891423_consumption, 11_LVBus0891423_production, 11_LVBus0891424_production, 11_LVBus0891425_consumption, 11_LVBus0891425_production, 11_LVBus0891426_consumption, 11_LVBus0891426_production, 11_LVBus0891427_production, 11_LVBus0891428_production, 11_LVBus0891429_production, 11_LVBus0891430_production, 11_LVBus0891431_production, 11_LVBus0891433_consumption, 11_LVBus0891433_production, 11_LVBus0891434_consumption, 11_LVBus0891434_production, 11_LVBus0891435_consumption, 11_LVBus0891435_production, 11_LVBus0891436_consumption, 11_LVBus0891436_production, 11_LVBus0891437_production, 11_LVBus0891439_production, 11_LVBus0891441_production, 11_LVBus0891443_consumption, 11_LVBus0891443_production, 11_LVBus0891444_consumption, 11_LVBus0891444_production, 11_LVBus0891445_consumption, 11_LVBus0891445_production, 11_LVBus0891447_consumption, 11_LVBus0891447_production, 11_LVBus0891448_consumption, 11_LVBus0891448_production, 11_LVBus0891449_production, 11_LVBus0891450_production, 11_LVBus0891451_production, 11_LVBus0891452_production, 11_LVBus0891453_production, 11_LVBus0891454_production, 11_LVBus0891455_production, 11_LVBus0891456_production, 11_LVBus0891457_production, 11_LVBus0891458_production, 11_LVBus0891459_consumption, 11_LVBus0891459_production, 11_LVBus0891460_consumption, 11_LVBus0891460_production, 11_LVBus0891462_consumption, 11_LVBus0891462_production, 11_LVBus0891463_consumption, 11_LVBus0891463_production, 11_LVBus0891464_production, 11_LVBus0891465_production, 11_LVBus0891466_production, 11_LVBus0891467_production, 11_LVBus0891469_consumption, 11_LVBus0891469_production, 11_LVBus0891470_consumption, 11_LVBus0891470_production, 11_LVBus0891471_production, 11_LVBus0891472_production, 11_LVBus0891473_production, 11_LVBus0891474_consumption, 11_LVBus0891474_production, 11_LVBus0891475_production, 11_LVBus0891476_production, 11_LVBus0891477_production, 11_LVBus0891478_consumption, 11_LVBus0891478_production, 11_LVBus0891479_consumption, 11_LVBus0891479_production, 11_LVBus0891480_production, 11_LVBus0891482_consumption, 11_LVBus0891482_production, 11_LVBus0891483_consumption, 11_LVBus0891483_production, 11_LVBus0891484_consumption, 11_LVBus0891484_production, 11_LVBus0891485_consumption, 11_LVBus0891485_production, 11_LVBus0891486_production, 11_LVBus0891487_production, 11_LVBus0891488_production, 11_LVBus0891489_production, 11_LVBus0891490_production, 11_LVBus0891491_production, 11_LVBus0891492_production, 11_LVBus0891493_production, 11_LVBus0891495_consumption, 11_LVBus0891495_production, 11_LVBus0891496_production, 11_LVBus0891497_production, 11_LVBus0891499_production, 11_LVBus0891500_consumption, 11_LVBus0891500_production, 11_LVBus0891501_consumption, 11_LVBus0891501_production, 11_LVBus0891502_consumption, 11_LVBus0891502_production, 11_LVBus0891503_consumption, 11_LVBus0891503_production, 11_LVBus0891504_consumption, 11_LVBus0891504_production, 11_LVBus0891505_production, 11_LVBus0891506_consumption, 11_LVBus0891506_production, 11_LVBus0891507_production, 11_LVBus0891508_consumption, 11_LVBus0891508_production, 11_LVBus0891509_consumption, 11_LVBus0891509_production, 11_LVBus0891511_consumption, 11_LVBus0891511_production, 11_LVBus0891512_consumption, 11_LVBus0891512_production, 11_LVBus0891513_consumption, 11_LVBus0891513_production, 11_LVBus0891514_production, 11_LVBus0891515_consumption, 11_LVBus0891515_production, 11_LVBus0891516_production, 11_LVBus0891518_consumption, 11_LVBus0891518_production, 11_LVBus0891519_consumption, 11_LVBus0891519_production, 11_LVBus0891520_consumption, 11_LVBus0891520_production, 11_LVBus0891521_production, 11_LVBus0891523_consumption, 11_LVBus0891523_production, 11_LVBus0891524_consumption, 11_LVBus0891524_production, 11_LVBus0891525_consumption, 11_LVBus0891525_production, 11_LVBus0891526_consumption, 11_LVBus0891526_production, 11_LVBus0891527_consumption, 11_LVBus0891527_production, 11_LVBus0891528_production, 11_LVBus0891529_consumption, 11_LVBus0891529_production, 11_LVBus0891530_production, 11_LVBus0891531_production, 11_LVBus0891533_production, 11_LVBus0891534_production, 11_LVBus0891535_production, 11_LVBus0891536_production, 11_LVBus0891537_production, 11_LVBus0891538_production, 11_LVBus0891539_production, 11_LVBus0891540_production, 11_LVBus0891542_production, 11_LVBus0891543_production, 11_LVBus0891544_production, 11_LVBus0891545_production, 11_LVBus0891546_production, 11_LVBus0891547_production, 11_LVBus0891548_production, 11_LVBus0891549_production, 11_LVBus0891550_production, 11_LVBus0891551_production, 11_LVBus0891552_production, 11_LVBus0891553_production, 11_LVBus0891554_production, 11_LVBus0891556_production, 11_LVBus0891557_production, 11_LVBus0891558_production, 11_LVBus0891559_production, 11_LVBus0891560_production, 11_LVBus0891561_production, 11_LVBus0891563_production, 11_LVBus0891564_production, 11_LVBus0891565_production, 11_LVBus0891566_production, 11_LVBus0891567_production, 11_LVBus0891568_production, 11_LVBus0891569_production, 11_LVBus0891570_production, 11_LVBus0891571_production, 11_LVBus0891572_production, 11_LVBus0891574_production, 11_LVBus0891575_production, 11_LVBus0891576_production, 11_LVBus0891577_consumption, 11_LVBus0891577_production, 11_LVBus0891578_production, 11_LVBus0891579_production, 11_LVBus0891581_production, 11_LVBus0891582_consumption, 11_LVBus0891582_production, 11_LVBus0891583_production, 11_LVBus0891585_production, 11_LVBus0891587_production, 11_LVBus0891588_production, 11_LVBus0891589_production, 11_LVBus0891591_consumption, 11_LVBus0891591_production, 11_LVBus0891592_production, 11_LVBus0891593_consumption, 11_LVBus0891593_production, 11_LVBus0891594_production, 11_LVBus0891595_production, 11_LVBus0891596_production, 11_LVBus0891597_production, 11_LVBus0891598_production, 11_LVBus0891599_production, 11_LVBus0891600_production, 11_LVBus0891601_production, 11_LVBus0891602_production, 11_LVBus0891603_consumption, 11_LVBus0891603_production, 11_LVBus0891604_production, 11_LVBus0891605_consumption, 11_LVBus0891605_production, 11_LVBus0891606_production, 11_LVBus0891608_production, 11_LVBus0891609_consumption, 11_LVBus0891609_production, 11_LVBus0891611_consumption, 11_LVBus0891611_production, 11_LVBus0891612_production, 11_LVBus0891613_consumption, 11_LVBus0891613_production, 11_LVBus0891614_production, 11_LVBus0891615_production, 11_LVBus0891616_production, 11_LVBus0891617_production, 11_LVBus0891618_production, 11_LVBus0891619_production, 11_LVBus0891620_production, 11_LVBus0891621_production, 11_LVBus0891623_consumption, 11_LVBus0891623_production, 11_LVBus0891624_consumption, 11_LVBus0891624_production, 11_LVBus0891625_production, 11_LVBus0891627_consumption, 11_LVBus0891627_production, 11_LVBus0891628_production, 11_LVBus0891629_production, 11_LVBus0891630_production, 11_LVBus0891631_production, 11_LVBus0891632_production, 11_LVBus0891633_production, 11_LVBus0891634_production, 11_LVBus0891635_production, 11_LVBus0891636_production, 11_LVBus0891638_production, 11_LVBus0891639_production, 11_LVBus0891640_production, 11_LVBus0891642_consumption, 11_LVBus0891642_production, 11_LVBus0891643_production, 11_LVBus0891644_production, 11_LVBus0891645_consumption, 11_LVBus0891645_production, 11_LVBus0891646_production, 11_LVBus0891648_production, 11_LVBus0891650_consumption, 11_LVBus0891650_production, 11_LVBus0891651_production, 11_LVBus0891652_production, 11_LVBus0891653_production, 11_LVBus0891654_production, 11_LVBus0891656_production, 11_LVBus0891658_production, 11_LVBus0891659_production, 11_LVBus0891660_consumption, 11_LVBus0891660_production, 11_LVBus0891661_production, 11_LVBus0891662_production, 11_LVBus0891663_production, 11_LVBus0891664_production, 11_LVBus0891665_production, 11_LVBus0891666_production, 11_LVBus0891667_production, 11_LVBus0891668_production, 11_LVBus0891669_consumption, 11_LVBus0891669_production, 11_LVBus0891670_production, 11_LVBus0891671_production, 11_LVBus0891672_production, 11_LVBus0891673_consumption, 11_LVBus0891673_production, 11_LVBus0891674_production, 11_LVBus0891675_production, 11_LVBus0891676_production, 11_LVBus0891677_production, 11_LVBus0891678_production, 11_LVBus0891679_production, 11_LVBus0891680_production, 11_LVBus0891682_consumption, 11_LVBus0891682_production, 11_LVBus0891683_consumption, 11_LVBus0891683_production, 11_LVBus0891684_consumption, 11_LVBus0891684_production, 11_LVBus0891685_production, 11_LVBus0891686_production, 11_LVBus0891687_production, 11_LVBus0891688_production, 11_LVBus0891689_consumption, 11_LVBus0891689_production, 11_LVBus0891690_production, 11_LVBus0891691_production, 11_LVBus0891692_production, 11_LVBus0891693_production, 11_LVBus0891694_production, 11_LVBus0891695_production, 11_LVBus0891696_production, 11_LVBus0891697_production, 11_LVBus0891698_production, 11_LVBus0891699_production, 11_LVBus0891700_production, 11_LVBus0891701_consumption, 11_LVBus0891701_production, 11_LVBus0891702_production, 11_LVBus0891703_production, 11_LVBus0891704_production, 11_LVBus0891705_production, 11_LVBus0891706_production, 11_LVBus0891707_production, 11_LVBus0891708_production, 11_LVBus0891709_production, 11_LVBus0891710_production, 11_LVBus0891712_consumption, 11_LVBus0891712_production, 11_LVBus0891713_consumption, 11_LVBus0891713_production, 11_LVBus0891714_consumption, 11_LVBus0891714_production, 11_LVBus0891715_production, 11_LVBus0891716_consumption, 11_LVBus0891716_production, 11_LVBus0891717_production, 11_LVBus0891718_production, 11_LVBus0891719_consumption, 11_LVBus0891719_production, 11_LVBus0891721_production, 11_LVBus0891722_consumption, 11_LVBus0891722_production, 11_LVBus0891723_consumption, 11_LVBus0891723_production, 11_LVBus0891724_production, 11_LVBus0891725_production, 11_LVBus0891726_production, 11_LVBus0891727_production, 11_LVBus0891728_production, 11_LVBus0891729_production, 11_LVBus0891730_production, 11_LVBus0891731_production, 11_LVBus0891732_production, 11_LVBus0891733_consumption, 11_LVBus0891733_production, 11_LVBus0891734_production, 11_LVBus0891735_production, 11_LVBus0891736_production, 11_LVBus0891737_production, 11_LVBus0891738_production, 11_LVBus0891739_consumption, 11_LVBus0891739_production, 11_LVBus0891740_production, 11_LVBus0891741_production, 11_LVBus0891743_consumption, 11_LVBus0891743_production, 11_LVBus0891744_production, 11_LVBus0891745_production, 11_LVBus0891746_production, 11_LVBus0891747_production, 11_LVBus0891748_production, 11_LVBus0891749_production, 11_LVBus0891750_production, 11_LVBus0891751_production, 11_LVBus0891752_consumption, 11_LVBus0891752_production, 11_LVBus0891753_production, 11_LVBus0891754_production, 11_LVBus0891755_production, 11_LVBus0891756_consumption, 11_LVBus0891756_production, 11_LVBus0891758_consumption, 11_LVBus0891758_production, 11_LVBus0891759_consumption, 11_LVBus0891759_production, 11_LVBus0891760_production, 11_LVBus0891761_production, 11_LVBus0891762_consumption, 11_LVBus0891762_production, 11_LVBus0891763_production, 11_LVBus0891765_production, 11_LVBus0891766_production, 11_LVBus0891767_production, 11_LVBus0891768_production, 11_LVBus0891769_production, 11_LVBus0891771_consumption, 11_LVBus0891771_production, 11_LVBus0891772_production, 11_LVBus0891773_production, 11_LVBus0891774_production, 11_LVBus0891775_production, 11_LVBus0891776_production, 11_LVBus0891777_consumption, 11_LVBus0891777_production, 11_LVBus0891778_production, 11_LVBus0891779_production, 11_LVBus0891780_production, 11_LVBus0891781_production, 11_LVBus0891782_production, 11_LVBus0891783_production, 11_LVBus0891785_consumption, 11_LVBus0891785_production, 11_LVBus0891786_production, 11_LVBus0891787_production, 11_LVBus0891788_production, 11_LVBus0891789_production, 11_LVBus0891790_production, 11_LVBus0891791_production, 11_LVBus0891792_production, 11_LVBus0891793_production, 11_LVBus0891794_production, 11_LVBus0891795_consumption, 11_LVBus0891795_production, 11_LVBus0891796_production, 11_LVBus0891798_production, 11_LVBus0891799_production, 11_LVBus0891800_production, 11_LVBus0891801_production, 11_LVBus0891802_production, 11_LVBus0891803_production, 11_LVBus0891804_production, 11_LVBus0891806_production, 11_LVBus0891808_consumption, 11_LVBus0891808_production, 11_LVBus0891809_production, 11_LVBus0891811_consumption, 11_LVBus0891811_production, 11_LVBus0891812_production, 11_LVBus0891813_production, 11_LVBus0891815_production, 11_LVBus0891817_production, 11_LVBus0891818_production, 11_LVBus0891819_production, 11_LVBus0891821_consumption, 11_LVBus0891821_production, 11_LVBus0891822_production, 11_LVBus0891823_production, 11_LVBus0891824_production, 11_LVBus0891825_production, 11_LVBus0891826_production, 11_LVBus0891827_production, 11_LVBus0891828_production, 11_LVBus0891829_production, 11_LVBus0891830_production, 11_LVBus0891831_production, 11_LVBus0891832_production, 11_LVBus0891833_consumption, 11_LVBus0891833_production, 11_LVBus0891835_production, 11_LVBus0891836_production, 11_LVBus0891837_production, 11_LVBus0891838_production, 11_LVBus0891839_production, 11_LVBus0891840_production, 11_LVBus0891841_consumption, 11_LVBus0891841_production, 11_LVBus0891842_production, 11_LVBus0891843_production, 11_LVBus0891844_production, 11_LVBus0891846_production, 11_LVBus0891848_consumption, 11_LVBus0891848_production, 11_LVBus0891849_production, 11_LVBus0891850_production, 11_LVBus0891851_production, 11_LVBus0891852_production, 11_LVBus0891853_consumption, 11_LVBus0891853_production, 11_LVBus0891854_production, 11_LVBus0891855_production, 11_LVBus0891856_production, 11_LVBus0891857_production, 11_LVBus0891859_production, 11_LVBus0891861_consumption, 11_LVBus0891861_production, 11_LVBus0891862_production, 11_LVBus0891863_production, 11_LVBus0891864_production, 11_LVBus0891865_production, 11_LVBus0891866_production, 11_LVBus0891867_production, 11_LVBus0891868_consumption, 11_LVBus0891868_production, 11_LVBus0891869_consumption, 11_LVBus0891869_production, 11_LVBus0891870_consumption, 11_LVBus0891870_production, 11_LVBus0891871_consumption, 11_LVBus0891871_production, 11_LVBus0891873_production, 11_LVBus0891874_production, 11_LVBus0891875_production, 11_LVBus0891877_production, 11_LVBus1282564_consumption, 11_LVBus1282564_production, 11_LVBus1282565_production, 11_LVBus1282566_production, 11_LVBus1282567_production, 11_LVBus1284260_production, 11_LVBus1284908_production, 11_LVBus1284909_production, 11_LVBus1284910_production, 11_LVBus1284911_consumption, 11_LVBus1284911_production, 11_LVBus1284912_consumption, 11_LVBus1284912_production, 11_LVBus1284913_production, 11_LVBus1286516_production, 11_LVBus1286517_production, 11_LVBus1286518_production, 11_LVBus1286519_production, 11_LVBus1286520_production, 11_LVBus1286521_production, 11_LVBus1286522_production, 11_LVBus1286523_production, 11_LVBus1286524_production, 11_LVBus1297799_production, 11_LVBus1297800_production, 11_LVBus1297801_production, 11_LVBus1297802_production, 11_LVBus1297803_production, 11_LVBus1297804_production, 11_LVBus1303379_production, 11_LVBus1303380_production, 11_LVBus1303381_production, 11_LVBus1303382_production, 11_LVBus1369164_consumption, 11_LVBus1369164_production, 11_LVBus1369165_production, 11_LVBus1369166_production, 11_LVBus1369167_production, 11_LVBus1369168_consumption, 11_LVBus1369168_production, 11_LVBus1369169_production, 11_LVBus1369170_production, 11_LVBus1369171_production, 11_LVBus1369172_production, 11_LVBus1369173_production, 11_LVBus1369174_consumption, 11_LVBus1369174_production, 11_LVBus1369175_production, 11_LVBus1369176_production, 11_LVBus1369177_production, 11_LVBus1369178_production, 11_LVBus1369179_consumption, 11_LVBus1369179_production, 11_LVBus1369180_production, 11_LVBus1369181_production, 11_LVBus1369182_production, 11_LVBus1369183_production, 11_LVBus1369184_consumption, 11_LVBus1369184_production, 11_LVBus1369185_production, 11_LVBus1369186_production, 11_LVBus1369187_consumption, 11_LVBus1369187_production, 11_LVBus1369188_consumption, 11_LVBus1369188_production, 11_LVBus1369189_consumption, 11_LVBus1369189_production, 11_LVBus1369190_consumption, 11_LVBus1369190_production, 11_LVBus1369191_consumption, 11_LVBus1369191_production, 11_LVBus1369192_consumption, 11_LVBus1369192_production, 11_LVBus1369193_consumption, 11_LVBus1369193_production, 11_LVBus1369194_production, 11_LVBus1369195_consumption, 11_LVBus1369195_production, 11_LVBus1369196_production, 11_LVBus1369197_production, 11_LVBus1369198_production, 11_LVBus1369199_production, 11_LVBus1369200_production, 11_LVBus1369201_production, 11_LVBus1369202_consumption, 11_LVBus1369202_production, 11_LVBus1369203_consumption, 11_LVBus1369203_production, 11_LVBus1369204_production, 11_LVBus1369205_production, 11_LVBus1369206_production, 11_LVBus1369207_production, 11_LVBus1369208_production, 11_LVBus1369209_production, 11_LVBus1369210_production, 11_LVBus1369211_production, 11_LVBus1369212_consumption, 11_LVBus1369212_production, 11_LVBus1369213_production, 11_LVBus1369214_production, 11_LVBus1369215_consumption, 11_LVBus1369215_production, 11_LVBus1369216_production, 11_LVBus1369217_production, 11_LVBus1369218_production, 11_LVBus1369219_consumption, 11_LVBus1369219_production, 11_LVBus1369220_production, 11_LVBus1369221_production, 11_LVBus1369222_production, 11_LVBus1369223_production, 11_LVBus1369224_production, 11_LVBus1369225_consumption, 11_LVBus1369225_production, 11_LVBus1369226_consumption, 11_LVBus1369226_production, 11_LVBus1369227_production, 11_LVBus1369228_production, 11_LVBus1369229_production, 11_LVBus1369230_production, 11_LVBus1369231_production, 11_LVBus1369232_production, 11_LVBus1369233_consumption, 11_LVBus1369233_production, 11_LVBus1369234_production, 11_LVBus1369235_production, 11_LVBus1369236_production, 11_LVBus1369237_production, 11_LVBus1369238_production, 11_LVBus1369239_production, 11_LVBus1369240_production, 11_LVBus1369241_production, 11_LVBus1369242_production, 11_LVBus1369243_production, 11_LVBus1369244_consumption, 11_LVBus1369244_production, 11_LVBus1369245_production, 11_LVBus1369246_production, 11_LVBus1369247_production, 11_LVBus1369248_production, 11_LVBus1369249_production, 11_LVBus1369250_production, 11_LVBus1369251_consumption, 11_LVBus1369251_production, 11_LVBus1369252_consumption, 11_LVBus1369252_production, 11_LVBus1369253_consumption, 11_LVBus1369253_production, 11_LVBus1369254_production, 11_LVBus1369255_production, 11_LVBus1369256_consumption, 11_LVBus1369256_production, 11_LVBus1369257_production, 11_LVBus1369258_consumption, 11_LVBus1369258_production, 11_LVBus1369259_production, 11_LVBus1369260_production, 11_LVBus1369261_consumption, 11_LVBus1369261_production, 11_LVBus1369262_production, 11_LVBus1369263_production, 11_LVBus1369264_consumption, 11_LVBus1369264_production, 11_LVBus1369265_consumption, 11_LVBus1369265_production, 11_LVBus1369266_consumption, 11_LVBus1369266_production, 11_LVBus1369267_production, 11_LVBus1369268_consumption, 11_LVBus1369268_production, 11_LVBus1369269_consumption, 11_LVBus1369269_production, 11_LVBus1369270_consumption, 11_LVBus1369270_production, 11_LVBus1369271_production, 11_LVBus1369272_production, 11_LVBus1369273_production, 11_LVBus1369274_production, 11_LVBus1369275_production, 11_LVBus1369276_production, 11_LVBus1369277_production, 11_LVBus1369278_consumption, 11_LVBus1369278_production, 11_LVBus1370343_production, 11_LVBus1370344_production, 11_LVBus1370345_production, 11_LVBus1370346_production, 11_LVBus1370347_production, 11_LVBus1370348_production, 11_LVBus1370349_production, 11_LVBus1370350_production, 11_LVBus1370351_production, 11_LVBus1370352_production, 11_LVBus1370353_production, 11_LVBus1370354_production, 11_LVBus1370355_production, 11_LVBus1370356_production, 11_LVBus1370357_production, 11_LVBus1370358_production, 11_LVBus1370359_production, 11_LVBus1370360_consumption, 11_LVBus1370360_production, 11_MVLV35758_consumption, 11_MVLV35758_production, 11_MVLV46971_production, 11_MVLV73641_consumption, 11_MVLV73641_production.

## 9. Data Quality Summary

**Total findings:** 419 (0 errors, 5 warnings, 414 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  834 of 1290 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.02 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  835 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369242_consumption`  
  Load '11_LVBus1369242_consumption' has phase imbalance of 63.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891516_consumption`  
  Load '11_LVBus0891516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369200_consumption`  
  Load '11_LVBus1369200_consumption' has phase imbalance of 102.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891690_consumption`  
  Load '11_LVBus0891690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891819_consumption`  
  Load '11_LVBus0891819_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370357_consumption`  
  Load '11_LVBus1370357_consumption' has phase imbalance of 37.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891875_consumption`  
  Load '11_LVBus0891875_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369181_consumption`  
  Load '11_LVBus1369181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891734_consumption`  
  Load '11_LVBus0891734_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1297804_consumption`  
  Load '11_LVBus1297804_consumption' has phase imbalance of 240.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891851_consumption`  
  Load '11_LVBus0891851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891737_consumption`  
  Load '11_LVBus0891737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891729_consumption`  
  Load '11_LVBus0891729_consumption' has phase imbalance of 173.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891452_consumption`  
  Load '11_LVBus0891452_consumption' has phase imbalance of 67.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891363_consumption`  
  Load '11_LVBus0891363_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891349_consumption`  
  Load '11_LVBus0891349_consumption' has phase imbalance of 20.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369206_consumption`  
  Load '11_LVBus1369206_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891550_consumption`  
  Load '11_LVBus0891550_consumption' has phase imbalance of 195.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891608_consumption`  
  Load '11_LVBus0891608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369180_consumption`  
  Load '11_LVBus1369180_consumption' has phase imbalance of 203.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891792_consumption`  
  Load '11_LVBus0891792_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891575_consumption`  
  Load '11_LVBus0891575_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891539_consumption`  
  Load '11_LVBus0891539_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891628_consumption`  
  Load '11_LVBus0891628_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891576_consumption`  
  Load '11_LVBus0891576_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891849_consumption`  
  Load '11_LVBus0891849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891560_consumption`  
  Load '11_LVBus0891560_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891705_consumption`  
  Load '11_LVBus0891705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369172_consumption`  
  Load '11_LVBus1369172_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286520_consumption`  
  Load '11_LVBus1286520_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286523_consumption`  
  Load '11_LVBus1286523_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370354_consumption`  
  Load '11_LVBus1370354_consumption' has phase imbalance of 99.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369275_consumption`  
  Load '11_LVBus1369275_consumption' has phase imbalance of 41.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891514_consumption`  
  Load '11_LVBus0891514_consumption' has phase imbalance of 84.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891812_consumption`  
  Load '11_LVBus0891812_consumption' has phase imbalance of 31.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891728_consumption`  
  Load '11_LVBus0891728_consumption' has phase imbalance of 168.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891753_consumption`  
  Load '11_LVBus0891753_consumption' has phase imbalance of 76.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891766_consumption`  
  Load '11_LVBus0891766_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891369_consumption`  
  Load '11_LVBus0891369_consumption' has phase imbalance of 142.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891700_consumption`  
  Load '11_LVBus0891700_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891456_consumption`  
  Load '11_LVBus0891456_consumption' has phase imbalance of 98.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891540_consumption`  
  Load '11_LVBus0891540_consumption' has phase imbalance of 112.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891497_consumption`  
  Load '11_LVBus0891497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1303382_consumption`  
  Load '11_LVBus1303382_consumption' has phase imbalance of 270.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891339_consumption`  
  Load '11_LVBus0891339_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891854_consumption`  
  Load '11_LVBus0891854_consumption' has phase imbalance of 159.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891569_consumption`  
  Load '11_LVBus0891569_consumption' has phase imbalance of 62.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891621_consumption`  
  Load '11_LVBus0891621_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891654_consumption`  
  Load '11_LVBus0891654_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891706_consumption`  
  Load '11_LVBus0891706_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891666_consumption`  
  Load '11_LVBus0891666_consumption' has phase imbalance of 122.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891746_consumption`  
  Load '11_LVBus0891746_consumption' has phase imbalance of 72.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369246_consumption`  
  Load '11_LVBus1369246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891537_consumption`  
  Load '11_LVBus0891537_consumption' has phase imbalance of 110.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891704_consumption`  
  Load '11_LVBus0891704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891699_consumption`  
  Load '11_LVBus0891699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891778_consumption`  
  Load '11_LVBus0891778_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891570_consumption`  
  Load '11_LVBus0891570_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891472_consumption`  
  Load '11_LVBus0891472_consumption' has phase imbalance of 106.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369230_consumption`  
  Load '11_LVBus1369230_consumption' has phase imbalance of 117.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891815_consumption`  
  Load '11_LVBus0891815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891594_consumption`  
  Load '11_LVBus0891594_consumption' has phase imbalance of 68.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891473_consumption`  
  Load '11_LVBus0891473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370359_consumption`  
  Load '11_LVBus1370359_consumption' has phase imbalance of 96.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891744_consumption`  
  Load '11_LVBus0891744_consumption' has phase imbalance of 214.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286521_consumption`  
  Load '11_LVBus1286521_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891458_consumption`  
  Load '11_LVBus0891458_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370352_consumption`  
  Load '11_LVBus1370352_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891750_consumption`  
  Load '11_LVBus0891750_consumption' has phase imbalance of 83.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891822_consumption`  
  Load '11_LVBus0891822_consumption' has phase imbalance of 48.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369183_consumption`  
  Load '11_LVBus1369183_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891554_consumption`  
  Load '11_LVBus0891554_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891735_consumption`  
  Load '11_LVBus0891735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891786_consumption`  
  Load '11_LVBus0891786_consumption' has phase imbalance of 209.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891776_consumption`  
  Load '11_LVBus0891776_consumption' has phase imbalance of 74.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370348_consumption`  
  Load '11_LVBus1370348_consumption' has phase imbalance of 244.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1284260_consumption`  
  Load '11_LVBus1284260_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369201_consumption`  
  Load '11_LVBus1369201_consumption' has phase imbalance of 123.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891616_consumption`  
  Load '11_LVBus0891616_consumption' has phase imbalance of 79.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891798_consumption`  
  Load '11_LVBus0891798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891850_consumption`  
  Load '11_LVBus0891850_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891663_consumption`  
  Load '11_LVBus0891663_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369173_consumption`  
  Load '11_LVBus1369173_consumption' has phase imbalance of 262.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891800_consumption`  
  Load '11_LVBus0891800_consumption' has phase imbalance of 200.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891572_consumption`  
  Load '11_LVBus0891572_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891615_consumption`  
  Load '11_LVBus0891615_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891632_consumption`  
  Load '11_LVBus0891632_consumption' has phase imbalance of 194.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891507_consumption`  
  Load '11_LVBus0891507_consumption' has phase imbalance of 44.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891668_consumption`  
  Load '11_LVBus0891668_consumption' has phase imbalance of 278.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891782_consumption`  
  Load '11_LVBus0891782_consumption' has phase imbalance of 24.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891688_consumption`  
  Load '11_LVBus0891688_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891667_consumption`  
  Load '11_LVBus0891667_consumption' has phase imbalance of 57.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370351_consumption`  
  Load '11_LVBus1370351_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369165_consumption`  
  Load '11_LVBus1369165_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891702_consumption`  
  Load '11_LVBus0891702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891592_consumption`  
  Load '11_LVBus0891592_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891556_consumption`  
  Load '11_LVBus0891556_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891755_consumption`  
  Load '11_LVBus0891755_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891697_consumption`  
  Load '11_LVBus0891697_consumption' has phase imbalance of 198.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891826_consumption`  
  Load '11_LVBus0891826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891874_consumption`  
  Load '11_LVBus0891874_consumption' has phase imbalance of 24.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891588_consumption`  
  Load '11_LVBus0891588_consumption' has phase imbalance of 130.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369182_consumption`  
  Load '11_LVBus1369182_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891358_consumption`  
  Load '11_LVBus0891358_consumption' has phase imbalance of 47.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891791_consumption`  
  Load '11_LVBus0891791_consumption' has phase imbalance of 80.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891824_consumption`  
  Load '11_LVBus0891824_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891855_consumption`  
  Load '11_LVBus0891855_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1303379_consumption`  
  Load '11_LVBus1303379_consumption' has phase imbalance of 31.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891361_consumption`  
  Load '11_LVBus0891361_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891727_consumption`  
  Load '11_LVBus0891727_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891574_consumption`  
  Load '11_LVBus0891574_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369273_consumption`  
  Load '11_LVBus1369273_consumption' has phase imbalance of 121.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369196_consumption`  
  Load '11_LVBus1369196_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891846_consumption`  
  Load '11_LVBus0891846_consumption' has phase imbalance of 131.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891382_consumption`  
  Load '11_LVBus0891382_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891783_consumption`  
  Load '11_LVBus0891783_consumption' has phase imbalance of 136.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369241_consumption`  
  Load '11_LVBus1369241_consumption' has phase imbalance of 67.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891831_consumption`  
  Load '11_LVBus0891831_consumption' has phase imbalance of 53.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891633_consumption`  
  Load '11_LVBus0891633_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891780_consumption`  
  Load '11_LVBus0891780_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891429_consumption`  
  Load '11_LVBus0891429_consumption' has phase imbalance of 29.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891857_consumption`  
  Load '11_LVBus0891857_consumption' has phase imbalance of 84.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891348_consumption`  
  Load '11_LVBus0891348_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891491_consumption`  
  Load '11_LVBus0891491_consumption' has phase imbalance of 142.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891769_consumption`  
  Load '11_LVBus0891769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891802_consumption`  
  Load '11_LVBus0891802_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891866_consumption`  
  Load '11_LVBus0891866_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369175_consumption`  
  Load '11_LVBus1369175_consumption' has phase imbalance of 79.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891676_consumption`  
  Load '11_LVBus0891676_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891852_consumption`  
  Load '11_LVBus0891852_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891557_consumption`  
  Load '11_LVBus0891557_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369228_consumption`  
  Load '11_LVBus1369228_consumption' has phase imbalance of 46.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891530_consumption`  
  Load '11_LVBus0891530_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891360_consumption`  
  Load '11_LVBus0891360_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891328_consumption`  
  Load '11_LVBus0891328_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891528_consumption`  
  Load '11_LVBus0891528_consumption' has phase imbalance of 116.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891597_consumption`  
  Load '11_LVBus0891597_consumption' has phase imbalance of 257.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369208_consumption`  
  Load '11_LVBus1369208_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369272_consumption`  
  Load '11_LVBus1369272_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891559_consumption`  
  Load '11_LVBus0891559_consumption' has phase imbalance of 142.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891441_consumption`  
  Load '11_LVBus0891441_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891671_consumption`  
  Load '11_LVBus0891671_consumption' has phase imbalance of 51.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891536_consumption`  
  Load '11_LVBus0891536_consumption' has phase imbalance of 78.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369204_consumption`  
  Load '11_LVBus1369204_consumption' has phase imbalance of 23.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891475_consumption`  
  Load '11_LVBus0891475_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891606_consumption`  
  Load '11_LVBus0891606_consumption' has phase imbalance of 95.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891659_consumption`  
  Load '11_LVBus0891659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370358_consumption`  
  Load '11_LVBus1370358_consumption' has phase imbalance of 53.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891749_consumption`  
  Load '11_LVBus0891749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369186_consumption`  
  Load '11_LVBus1369186_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891455_consumption`  
  Load '11_LVBus0891455_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891862_consumption`  
  Load '11_LVBus0891862_consumption' has phase imbalance of 75.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369222_consumption`  
  Load '11_LVBus1369222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891721_consumption`  
  Load '11_LVBus0891721_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891652_consumption`  
  Load '11_LVBus0891652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891620_consumption`  
  Load '11_LVBus0891620_consumption' has phase imbalance of 90.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891726_consumption`  
  Load '11_LVBus0891726_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1282566_consumption`  
  Load '11_LVBus1282566_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891571_consumption`  
  Load '11_LVBus0891571_consumption' has phase imbalance of 130.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891542_consumption`  
  Load '11_LVBus0891542_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891761_consumption`  
  Load '11_LVBus0891761_consumption' has phase imbalance of 40.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891631_consumption`  
  Load '11_LVBus0891631_consumption' has phase imbalance of 89.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369234_consumption`  
  Load '11_LVBus1369234_consumption' has phase imbalance of 71.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891499_consumption`  
  Load '11_LVBus0891499_consumption' has phase imbalance of 78.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1297801_consumption`  
  Load '11_LVBus1297801_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891830_consumption`  
  Load '11_LVBus0891830_consumption' has phase imbalance of 101.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891451_consumption`  
  Load '11_LVBus0891451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891357_consumption`  
  Load '11_LVBus0891357_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369199_consumption`  
  Load '11_LVBus1369199_consumption' has phase imbalance of 74.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891674_consumption`  
  Load '11_LVBus0891674_consumption' has phase imbalance of 58.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891828_consumption`  
  Load '11_LVBus0891828_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891419_consumption`  
  Load '11_LVBus0891419_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891531_consumption`  
  Load '11_LVBus0891531_consumption' has phase imbalance of 42.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369185_consumption`  
  Load '11_LVBus1369185_consumption' has phase imbalance of 65.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891549_consumption`  
  Load '11_LVBus0891549_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891695_consumption`  
  Load '11_LVBus0891695_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891543_consumption`  
  Load '11_LVBus0891543_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1284908_consumption`  
  Load '11_LVBus1284908_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891873_consumption`  
  Load '11_LVBus0891873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891618_consumption`  
  Load '11_LVBus0891618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891679_consumption`  
  Load '11_LVBus0891679_consumption' has phase imbalance of 193.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891347_consumption`  
  Load '11_LVBus0891347_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891437_consumption`  
  Load '11_LVBus0891437_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1297803_consumption`  
  Load '11_LVBus1297803_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891362_consumption`  
  Load '11_LVBus0891362_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891748_consumption`  
  Load '11_LVBus0891748_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891818_consumption`  
  Load '11_LVBus0891818_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1297799_consumption`  
  Load '11_LVBus1297799_consumption' has phase imbalance of 148.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369249_consumption`  
  Load '11_LVBus1369249_consumption' has phase imbalance of 124.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891430_consumption`  
  Load '11_LVBus0891430_consumption' has phase imbalance of 121.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891587_consumption`  
  Load '11_LVBus0891587_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891450_consumption`  
  Load '11_LVBus0891450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891567_consumption`  
  Load '11_LVBus0891567_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369247_consumption`  
  Load '11_LVBus1369247_consumption' has phase imbalance of 140.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891779_consumption`  
  Load '11_LVBus0891779_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891578_consumption`  
  Load '11_LVBus0891578_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891837_consumption`  
  Load '11_LVBus0891837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369216_consumption`  
  Load '11_LVBus1369216_consumption' has phase imbalance of 153.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891745_consumption`  
  Load '11_LVBus0891745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1282567_consumption`  
  Load '11_LVBus1282567_consumption' has phase imbalance of 117.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891563_consumption`  
  Load '11_LVBus0891563_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891738_consumption`  
  Load '11_LVBus0891738_consumption' has phase imbalance of 70.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891813_consumption`  
  Load '11_LVBus0891813_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891839_consumption`  
  Load '11_LVBus0891839_consumption' has phase imbalance of 225.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891492_consumption`  
  Load '11_LVBus0891492_consumption' has phase imbalance of 244.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891773_consumption`  
  Load '11_LVBus0891773_consumption' has phase imbalance of 103.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1297800_consumption`  
  Load '11_LVBus1297800_consumption' has phase imbalance of 143.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891477_consumption`  
  Load '11_LVBus0891477_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891636_consumption`  
  Load '11_LVBus0891636_consumption' has phase imbalance of 107.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891710_consumption`  
  Load '11_LVBus0891710_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891661_consumption`  
  Load '11_LVBus0891661_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369223_consumption`  
  Load '11_LVBus1369223_consumption' has phase imbalance of 112.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891842_consumption`  
  Load '11_LVBus0891842_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891466_consumption`  
  Load '11_LVBus0891466_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369169_consumption`  
  Load '11_LVBus1369169_consumption' has phase imbalance of 112.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891664_consumption`  
  Load '11_LVBus0891664_consumption' has phase imbalance of 83.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891480_consumption`  
  Load '11_LVBus0891480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891823_consumption`  
  Load '11_LVBus0891823_consumption' has phase imbalance of 53.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891551_consumption`  
  Load '11_LVBus0891551_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891747_consumption`  
  Load '11_LVBus0891747_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891337_consumption`  
  Load '11_LVBus0891337_consumption' has phase imbalance of 259.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891725_consumption`  
  Load '11_LVBus0891725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891836_consumption`  
  Load '11_LVBus0891836_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891740_consumption`  
  Load '11_LVBus0891740_consumption' has phase imbalance of 97.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891829_consumption`  
  Load '11_LVBus0891829_consumption' has phase imbalance of 37.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891489_consumption`  
  Load '11_LVBus0891489_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891333_consumption`  
  Load '11_LVBus0891333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891651_consumption`  
  Load '11_LVBus0891651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891487_consumption`  
  Load '11_LVBus0891487_consumption' has phase imbalance of 220.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891817_consumption`  
  Load '11_LVBus0891817_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369267_consumption`  
  Load '11_LVBus1369267_consumption' has phase imbalance of 30.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891825_consumption`  
  Load '11_LVBus0891825_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891687_consumption`  
  Load '11_LVBus0891687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370345_consumption`  
  Load '11_LVBus1370345_consumption' has phase imbalance of 47.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891612_consumption`  
  Load '11_LVBus0891612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369178_consumption`  
  Load '11_LVBus1369178_consumption' has phase imbalance of 131.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891546_consumption`  
  Load '11_LVBus0891546_consumption' has phase imbalance of 229.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891767_consumption`  
  Load '11_LVBus0891767_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891617_consumption`  
  Load '11_LVBus0891617_consumption' has phase imbalance of 93.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891763_consumption`  
  Load '11_LVBus0891763_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891408_consumption`  
  Load '11_LVBus0891408_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891604_consumption`  
  Load '11_LVBus0891604_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370347_consumption`  
  Load '11_LVBus1370347_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891806_consumption`  
  Load '11_LVBus0891806_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891639_consumption`  
  Load '11_LVBus0891639_consumption' has phase imbalance of 76.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369166_consumption`  
  Load '11_LVBus1369166_consumption' has phase imbalance of 114.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891471_consumption`  
  Load '11_LVBus0891471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286516_consumption`  
  Load '11_LVBus1286516_consumption' has phase imbalance of 80.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891708_consumption`  
  Load '11_LVBus0891708_consumption' has phase imbalance of 79.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891789_consumption`  
  Load '11_LVBus0891789_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891428_consumption`  
  Load '11_LVBus0891428_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891796_consumption`  
  Load '11_LVBus0891796_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891788_consumption`  
  Load '11_LVBus0891788_consumption' has phase imbalance of 146.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891838_consumption`  
  Load '11_LVBus0891838_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286522_consumption`  
  Load '11_LVBus1286522_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1282565_consumption`  
  Load '11_LVBus1282565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891799_consumption`  
  Load '11_LVBus0891799_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1303380_consumption`  
  Load '11_LVBus1303380_consumption' has phase imbalance of 46.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891696_consumption`  
  Load '11_LVBus0891696_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891670_consumption`  
  Load '11_LVBus0891670_consumption' has phase imbalance of 119.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891691_consumption`  
  Load '11_LVBus0891691_consumption' has phase imbalance of 238.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891677_consumption`  
  Load '11_LVBus0891677_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891643_consumption`  
  Load '11_LVBus0891643_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891548_consumption`  
  Load '11_LVBus0891548_consumption' has phase imbalance of 246.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369236_consumption`  
  Load '11_LVBus1369236_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891859_consumption`  
  Load '11_LVBus0891859_consumption' has phase imbalance of 73.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891598_consumption`  
  Load '11_LVBus0891598_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286519_consumption`  
  Load '11_LVBus1286519_consumption' has phase imbalance of 33.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891856_consumption`  
  Load '11_LVBus0891856_consumption' has phase imbalance of 29.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891718_consumption`  
  Load '11_LVBus0891718_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891601_consumption`  
  Load '11_LVBus0891601_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891534_consumption`  
  Load '11_LVBus0891534_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891338_consumption`  
  Load '11_LVBus0891338_consumption' has phase imbalance of 107.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891787_consumption`  
  Load '11_LVBus0891787_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891340_consumption`  
  Load '11_LVBus0891340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891547_consumption`  
  Load '11_LVBus0891547_consumption' has phase imbalance of 106.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891439_consumption`  
  Load '11_LVBus0891439_consumption' has phase imbalance of 125.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369209_consumption`  
  Load '11_LVBus1369209_consumption' has phase imbalance of 85.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891646_consumption`  
  Load '11_LVBus0891646_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369214_consumption`  
  Load '11_LVBus1369214_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891832_consumption`  
  Load '11_LVBus0891832_consumption' has phase imbalance of 268.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891602_consumption`  
  Load '11_LVBus0891602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369255_consumption`  
  Load '11_LVBus1369255_consumption' has phase imbalance of 58.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891467_consumption`  
  Load '11_LVBus0891467_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369235_consumption`  
  Load '11_LVBus1369235_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891457_consumption`  
  Load '11_LVBus0891457_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1297802_consumption`  
  Load '11_LVBus1297802_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369257_consumption`  
  Load '11_LVBus1369257_consumption' has phase imbalance of 57.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891864_consumption`  
  Load '11_LVBus0891864_consumption' has phase imbalance of 98.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891454_consumption`  
  Load '11_LVBus0891454_consumption' has phase imbalance of 91.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891581_consumption`  
  Load '11_LVBus0891581_consumption' has phase imbalance of 226.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891619_consumption`  
  Load '11_LVBus0891619_consumption' has phase imbalance of 28.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370356_consumption`  
  Load '11_LVBus1370356_consumption' has phase imbalance of 59.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891545_consumption`  
  Load '11_LVBus0891545_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891877_consumption`  
  Load '11_LVBus0891877_consumption' has phase imbalance of 48.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891801_consumption`  
  Load '11_LVBus0891801_consumption' has phase imbalance of 255.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891768_consumption`  
  Load '11_LVBus0891768_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891731_consumption`  
  Load '11_LVBus0891731_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891835_consumption`  
  Load '11_LVBus0891835_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891552_consumption`  
  Load '11_LVBus0891552_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891793_consumption`  
  Load '11_LVBus0891793_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369211_consumption`  
  Load '11_LVBus1369211_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891630_consumption`  
  Load '11_LVBus0891630_consumption' has phase imbalance of 121.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891476_consumption`  
  Load '11_LVBus0891476_consumption' has phase imbalance of 118.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891330_consumption`  
  Load '11_LVBus0891330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1284910_consumption`  
  Load '11_LVBus1284910_consumption' has phase imbalance of 156.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891568_consumption`  
  Load '11_LVBus0891568_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1284913_consumption`  
  Load '11_LVBus1284913_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891656_consumption`  
  Load '11_LVBus0891656_consumption' has phase imbalance of 133.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891703_consumption`  
  Load '11_LVBus0891703_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891589_consumption`  
  Load '11_LVBus0891589_consumption' has phase imbalance of 47.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891698_consumption`  
  Load '11_LVBus0891698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891585_consumption`  
  Load '11_LVBus0891585_consumption' has phase imbalance of 38.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369238_consumption`  
  Load '11_LVBus1369238_consumption' has phase imbalance of 102.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891678_consumption`  
  Load '11_LVBus0891678_consumption' has phase imbalance of 91.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891496_consumption`  
  Load '11_LVBus0891496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891709_consumption`  
  Load '11_LVBus0891709_consumption' has phase imbalance of 162.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891686_consumption`  
  Load '11_LVBus0891686_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891741_consumption`  
  Load '11_LVBus0891741_consumption' has phase imbalance of 41.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891754_consumption`  
  Load '11_LVBus0891754_consumption' has phase imbalance of 129.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891694_consumption`  
  Load '11_LVBus0891694_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891658_consumption`  
  Load '11_LVBus0891658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369276_consumption`  
  Load '11_LVBus1369276_consumption' has phase imbalance of 79.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1303381_consumption`  
  Load '11_LVBus1303381_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369210_consumption`  
  Load '11_LVBus1369210_consumption' has phase imbalance of 25.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891781_consumption`  
  Load '11_LVBus0891781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891561_consumption`  
  Load '11_LVBus0891561_consumption' has phase imbalance of 104.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891765_consumption`  
  Load '11_LVBus0891765_consumption' has phase imbalance of 78.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891359_consumption`  
  Load '11_LVBus0891359_consumption' has phase imbalance of 110.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891416_consumption`  
  Load '11_LVBus0891416_consumption' has phase imbalance of 28.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891715_consumption`  
  Load '11_LVBus0891715_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891863_consumption`  
  Load '11_LVBus0891863_consumption' has phase imbalance of 107.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891680_consumption`  
  Load '11_LVBus0891680_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891665_consumption`  
  Load '11_LVBus0891665_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369239_consumption`  
  Load '11_LVBus1369239_consumption' has phase imbalance of 66.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286517_consumption`  
  Load '11_LVBus1286517_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891867_consumption`  
  Load '11_LVBus0891867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369167_consumption`  
  Load '11_LVBus1369167_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891635_consumption`  
  Load '11_LVBus0891635_consumption' has phase imbalance of 200.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891662_consumption`  
  Load '11_LVBus0891662_consumption' has phase imbalance of 214.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891840_consumption`  
  Load '11_LVBus0891840_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369198_consumption`  
  Load '11_LVBus1369198_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891707_consumption`  
  Load '11_LVBus0891707_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891693_consumption`  
  Load '11_LVBus0891693_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370343_consumption`  
  Load '11_LVBus1370343_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369250_consumption`  
  Load '11_LVBus1369250_consumption' has phase imbalance of 40.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891675_consumption`  
  Load '11_LVBus0891675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891648_consumption`  
  Load '11_LVBus0891648_consumption' has phase imbalance of 286.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891449_consumption`  
  Load '11_LVBus0891449_consumption' has phase imbalance of 111.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891600_consumption`  
  Load '11_LVBus0891600_consumption' has phase imbalance of 233.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1286524_consumption`  
  Load '11_LVBus1286524_consumption' has phase imbalance of 41.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369207_consumption`  
  Load '11_LVBus1369207_consumption' has phase imbalance of 58.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891595_consumption`  
  Load '11_LVBus0891595_consumption' has phase imbalance of 74.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891634_consumption`  
  Load '11_LVBus0891634_consumption' has phase imbalance of 221.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891535_consumption`  
  Load '11_LVBus0891535_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891774_consumption`  
  Load '11_LVBus0891774_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369245_consumption`  
  Load '11_LVBus1369245_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891804_consumption`  
  Load '11_LVBus0891804_consumption' has phase imbalance of 232.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369197_consumption`  
  Load '11_LVBus1369197_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891533_consumption`  
  Load '11_LVBus0891533_consumption' has phase imbalance of 299.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891413_consumption`  
  Load '11_LVBus0891413_consumption' has phase imbalance of 64.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369277_consumption`  
  Load '11_LVBus1369277_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369220_consumption`  
  Load '11_LVBus1369220_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891775_consumption`  
  Load '11_LVBus0891775_consumption' has phase imbalance of 74.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891566_consumption`  
  Load '11_LVBus0891566_consumption' has phase imbalance of 139.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891558_consumption`  
  Load '11_LVBus0891558_consumption' has phase imbalance of 85.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891453_consumption`  
  Load '11_LVBus0891453_consumption' has phase imbalance of 120.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891827_consumption`  
  Load '11_LVBus0891827_consumption' has phase imbalance of 175.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891431_consumption`  
  Load '11_LVBus0891431_consumption' has phase imbalance of 263.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369227_consumption`  
  Load '11_LVBus1369227_consumption' has phase imbalance of 68.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891553_consumption`  
  Load '11_LVBus0891553_consumption' has phase imbalance of 101.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369271_consumption`  
  Load '11_LVBus1369271_consumption' has phase imbalance of 89.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891865_consumption`  
  Load '11_LVBus0891865_consumption' has phase imbalance of 69.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891544_consumption`  
  Load '11_LVBus0891544_consumption' has phase imbalance of 295.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891724_consumption`  
  Load '11_LVBus0891724_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891732_consumption`  
  Load '11_LVBus0891732_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369254_consumption`  
  Load '11_LVBus1369254_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891564_consumption`  
  Load '11_LVBus0891564_consumption' has phase imbalance of 136.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369243_consumption`  
  Load '11_LVBus1369243_consumption' has phase imbalance of 132.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891565_consumption`  
  Load '11_LVBus0891565_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891760_consumption`  
  Load '11_LVBus0891760_consumption' has phase imbalance of 167.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891596_consumption`  
  Load '11_LVBus0891596_consumption' has phase imbalance of 86.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891464_consumption`  
  Load '11_LVBus0891464_consumption' has phase imbalance of 78.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891490_consumption`  
  Load '11_LVBus0891490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891809_consumption`  
  Load '11_LVBus0891809_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369221_consumption`  
  Load '11_LVBus1369221_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369177_consumption`  
  Load '11_LVBus1369177_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891751_consumption`  
  Load '11_LVBus0891751_consumption' has phase imbalance of 47.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891465_consumption`  
  Load '11_LVBus0891465_consumption' has phase imbalance of 50.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891736_consumption`  
  Load '11_LVBus0891736_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891772_consumption`  
  Load '11_LVBus0891772_consumption' has phase imbalance of 94.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891653_consumption`  
  Load '11_LVBus0891653_consumption' has phase imbalance of 105.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1370344_consumption`  
  Load '11_LVBus1370344_consumption' has phase imbalance of 97.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891685_consumption`  
  Load '11_LVBus0891685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1369229_consumption`  
  Load '11_LVBus1369229_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891488_consumption`  
  Load '11_LVBus0891488_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0891644_consumption`  
  Load '11_LVBus0891644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1284909_consumption`  
  Load '11_LVBus1284909_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1290 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_V.GEO' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '11_LVBus0891587' (LV, 0.24 kV) has an electrical reach of 1.2 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  668 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  135 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus0891330_consumption, 11_LVBus0891333_consumption, 11_LVBus0891337_consumption, 11_LVBus0891340_consumption, 11_LVBus0891348_consumption, 11_LVBus0891360_consumption, 11_LVBus0891361_consumption, 11_LVBus0891362_consumption, 11_LVBus0891363_consumption, 11_LVBus0891431_consumption, 11_LVBus0891450_consumption, 11_LVBus0891451_consumption, 11_LVBus0891458_consumption, 11_LVBus0891471_consumption, 11_LVBus0891473_consumption, 11_LVBus0891475_consumption, 11_LVBus0891480_consumption, 11_LVBus0891487_consumption, 11_LVBus0891489_consumption, 11_LVBus0891490_consumption, 11_LVBus0891492_consumption, 11_LVBus0891496_consumption, 11_LVBus0891497_consumption, 11_LVBus0891516_consumption, 11_LVBus0891534_consumption, 11_LVBus0891543_consumption, 11_LVBus0891544_consumption, 11_LVBus0891546_consumption, 11_LVBus0891548_consumption, 11_LVBus0891552_consumption, 11_LVBus0891563_consumption, 11_LVBus0891567_consumption, 11_LVBus0891576_consumption, 11_LVBus0891578_consumption, 11_LVBus0891581_consumption, 11_LVBus0891600_consumption, 11_LVBus0891602_consumption, 11_LVBus0891608_consumption, 11_LVBus0891612_consumption, 11_LVBus0891618_consumption, 11_LVBus0891632_consumption, 11_LVBus0891634_consumption, 11_LVBus0891643_consumption, 11_LVBus0891644_consumption, 11_LVBus0891651_consumption, 11_LVBus0891652_consumption, 11_LVBus0891658_consumption, 11_LVBus0891659_consumption, 11_LVBus0891662_consumption, 11_LVBus0891675_consumption, 11_LVBus0891676_consumption, 11_LVBus0891685_consumption, 11_LVBus0891686_consumption, 11_LVBus0891687_consumption, 11_LVBus0891688_consumption, 11_LVBus0891690_consumption, 11_LVBus0891691_consumption, 11_LVBus0891698_consumption, 11_LVBus0891699_consumption, 11_LVBus0891700_consumption, 11_LVBus0891702_consumption, 11_LVBus0891703_consumption, 11_LVBus0891704_consumption, 11_LVBus0891705_consumption, 11_LVBus0891706_consumption, 11_LVBus0891710_consumption, 11_LVBus0891715_consumption, 11_LVBus0891725_consumption, 11_LVBus0891726_consumption, 11_LVBus0891727_consumption, 11_LVBus0891728_consumption, 11_LVBus0891729_consumption, 11_LVBus0891731_consumption, 11_LVBus0891732_consumption, 11_LVBus0891734_consumption, 11_LVBus0891735_consumption, 11_LVBus0891737_consumption, 11_LVBus0891744_consumption, 11_LVBus0891745_consumption, 11_LVBus0891749_consumption, 11_LVBus0891760_consumption, 11_LVBus0891763_consumption, 11_LVBus0891766_consumption, 11_LVBus0891768_consumption, 11_LVBus0891769_consumption, 11_LVBus0891774_consumption, 11_LVBus0891781_consumption, 11_LVBus0891786_consumption, 11_LVBus0891792_consumption, 11_LVBus0891798_consumption, 11_LVBus0891800_consumption, 11_LVBus0891801_consumption, 11_LVBus0891804_consumption, 11_LVBus0891815_consumption, 11_LVBus0891819_consumption, 11_LVBus0891825_consumption, 11_LVBus0891826_consumption, 11_LVBus0891827_consumption, 11_LVBus0891828_consumption, 11_LVBus0891832_consumption, 11_LVBus0891835_consumption, 11_LVBus0891836_consumption, 11_LVBus0891837_consumption, 11_LVBus0891849_consumption, 11_LVBus0891851_consumption, 11_LVBus0891852_consumption, 11_LVBus0891854_consumption, 11_LVBus0891855_consumption, 11_LVBus0891867_consumption, 11_LVBus0891873_consumption, 11_LVBus1282565_consumption, 11_LVBus1282566_consumption, 11_LVBus1284260_consumption, 11_LVBus1284908_consumption, 11_LVBus1284909_consumption, 11_LVBus1284913_consumption, 11_LVBus1286521_consumption, 11_LVBus1297801_consumption, 11_LVBus1297804_consumption, 11_LVBus1303381_consumption, 11_LVBus1303382_consumption, 11_LVBus1369172_consumption, 11_LVBus1369173_consumption, 11_LVBus1369180_consumption, 11_LVBus1369181_consumption, 11_LVBus1369183_consumption, 11_LVBus1369196_consumption, 11_LVBus1369197_consumption, 11_LVBus1369198_consumption, 11_LVBus1369220_consumption, 11_LVBus1369221_consumption, 11_LVBus1369222_consumption, 11_LVBus1369229_consumption, 11_LVBus1369246_consumption, 11_LVBus1370348_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  645 group(s) of loads (1290 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  835 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0891328_production, 11_LVBus0891330_production, 11_LVBus0891332_consumption, 11_LVBus0891332_production, 11_LVBus0891333_production, 11_LVBus0891334_consumption, 11_LVBus0891334_production, 11_LVBus0891335_consumption, 11_LVBus0891335_production, 11_LVBus0891336_consumption, 11_LVBus0891336_production, 11_LVBus0891337_production, 11_LVBus0891338_production, 11_LVBus0891339_production, 11_LVBus0891340_production, 11_LVBus0891341_production, 11_LVBus0891342_production, 11_LVBus0891344_consumption, 11_LVBus0891344_production, 11_LVBus0891346_consumption, 11_LVBus0891346_production, 11_LVBus0891347_production, 11_LVBus0891348_production, 11_LVBus0891349_production, 11_LVBus0891351_consumption, 11_LVBus0891351_production, 11_LVBus0891352_consumption, 11_LVBus0891352_production, 11_LVBus0891354_consumption, 11_LVBus0891354_production, 11_LVBus0891355_production, 11_LVBus0891356_production, 11_LVBus0891357_production, 11_LVBus0891358_production, 11_LVBus0891359_production, 11_LVBus0891360_production, 11_LVBus0891361_production, 11_LVBus0891362_production, 11_LVBus0891363_production, 11_LVBus0891365_consumption, 11_LVBus0891365_production, 11_LVBus0891367_consumption, 11_LVBus0891367_production, 11_LVBus0891368_consumption, 11_LVBus0891368_production, 11_LVBus0891369_production, 11_LVBus0891370_consumption, 11_LVBus0891370_production, 11_LVBus0891371_consumption, 11_LVBus0891371_production, 11_LVBus0891373_production, 11_LVBus0891375_consumption, 11_LVBus0891375_production, 11_LVBus0891376_consumption, 11_LVBus0891376_production, 11_LVBus0891378_consumption, 11_LVBus0891378_production, 11_LVBus0891379_consumption, 11_LVBus0891379_production, 11_LVBus0891380_consumption, 11_LVBus0891380_production, 11_LVBus0891381_consumption, 11_LVBus0891381_production, 11_LVBus0891382_production, 11_LVBus0891383_consumption, 11_LVBus0891383_production, 11_LVBus0891385_consumption, 11_LVBus0891385_production, 11_LVBus0891386_consumption, 11_LVBus0891386_production, 11_LVBus0891387_consumption, 11_LVBus0891387_production, 11_LVBus0891388_consumption, 11_LVBus0891388_production, 11_LVBus0891389_consumption, 11_LVBus0891389_production, 11_LVBus0891390_consumption, 11_LVBus0891390_production, 11_LVBus0891391_consumption, 11_LVBus0891391_production, 11_LVBus0891392_consumption, 11_LVBus0891392_production, 11_LVBus0891393_consumption, 11_LVBus0891393_production, 11_LVBus0891394_consumption, 11_LVBus0891394_production, 11_LVBus0891395_production, 11_LVBus0891396_production, 11_LVBus0891397_consumption, 11_LVBus0891397_production, 11_LVBus0891399_consumption, 11_LVBus0891399_production, 11_LVBus0891400_consumption, 11_LVBus0891400_production, 11_LVBus0891401_consumption, 11_LVBus0891401_production, 11_LVBus0891402_consumption, 11_LVBus0891402_production, 11_LVBus0891403_consumption, 11_LVBus0891403_production, 11_LVBus0891404_consumption, 11_LVBus0891404_production, 11_LVBus0891405_consumption, 11_LVBus0891405_production, 11_LVBus0891406_consumption, 11_LVBus0891406_production, 11_LVBus0891408_production, 11_LVBus0891410_consumption, 11_LVBus0891410_production, 11_LVBus0891411_consumption, 11_LVBus0891411_production, 11_LVBus0891412_consumption, 11_LVBus0891412_production, 11_LVBus0891413_production, 11_LVBus0891414_consumption, 11_LVBus0891414_production, 11_LVBus0891415_consumption, 11_LVBus0891415_production, 11_LVBus0891416_production, 11_LVBus0891417_consumption, 11_LVBus0891417_production, 11_LVBus0891419_production, 11_LVBus0891421_consumption, 11_LVBus0891421_production, 11_LVBus0891422_consumption, 11_LVBus0891422_production, 11_LVBus0891423_consumption, 11_LVBus0891423_production, 11_LVBus0891424_production, 11_LVBus0891425_consumption, 11_LVBus0891425_production, 11_LVBus0891426_consumption, 11_LVBus0891426_production, 11_LVBus0891427_production, 11_LVBus0891428_production, 11_LVBus0891429_production, 11_LVBus0891430_production, 11_LVBus0891431_production, 11_LVBus0891433_consumption, 11_LVBus0891433_production, 11_LVBus0891434_consumption, 11_LVBus0891434_production, 11_LVBus0891435_consumption, 11_LVBus0891435_production, 11_LVBus0891436_consumption, 11_LVBus0891436_production, 11_LVBus0891437_production, 11_LVBus0891439_production, 11_LVBus0891441_production, 11_LVBus0891443_consumption, 11_LVBus0891443_production, 11_LVBus0891444_consumption, 11_LVBus0891444_production, 11_LVBus0891445_consumption, 11_LVBus0891445_production, 11_LVBus0891447_consumption, 11_LVBus0891447_production, 11_LVBus0891448_consumption, 11_LVBus0891448_production, 11_LVBus0891449_production, 11_LVBus0891450_production, 11_LVBus0891451_production, 11_LVBus0891452_production, 11_LVBus0891453_production, 11_LVBus0891454_production, 11_LVBus0891455_production, 11_LVBus0891456_production, 11_LVBus0891457_production, 11_LVBus0891458_production, 11_LVBus0891459_consumption, 11_LVBus0891459_production, 11_LVBus0891460_consumption, 11_LVBus0891460_production, 11_LVBus0891462_consumption, 11_LVBus0891462_production, 11_LVBus0891463_consumption, 11_LVBus0891463_production, 11_LVBus0891464_production, 11_LVBus0891465_production, 11_LVBus0891466_production, 11_LVBus0891467_production, 11_LVBus0891469_consumption, 11_LVBus0891469_production, 11_LVBus0891470_consumption, 11_LVBus0891470_production, 11_LVBus0891471_production, 11_LVBus0891472_production, 11_LVBus0891473_production, 11_LVBus0891474_consumption, 11_LVBus0891474_production, 11_LVBus0891475_production, 11_LVBus0891476_production, 11_LVBus0891477_production, 11_LVBus0891478_consumption, 11_LVBus0891478_production, 11_LVBus0891479_consumption, 11_LVBus0891479_production, 11_LVBus0891480_production, 11_LVBus0891482_consumption, 11_LVBus0891482_production, 11_LVBus0891483_consumption, 11_LVBus0891483_production, 11_LVBus0891484_consumption, 11_LVBus0891484_production, 11_LVBus0891485_consumption, 11_LVBus0891485_production, 11_LVBus0891486_production, 11_LVBus0891487_production, 11_LVBus0891488_production, 11_LVBus0891489_production, 11_LVBus0891490_production, 11_LVBus0891491_production, 11_LVBus0891492_production, 11_LVBus0891493_production, 11_LVBus0891495_consumption, 11_LVBus0891495_production, 11_LVBus0891496_production, 11_LVBus0891497_production, 11_LVBus0891499_production, 11_LVBus0891500_consumption, 11_LVBus0891500_production, 11_LVBus0891501_consumption, 11_LVBus0891501_production, 11_LVBus0891502_consumption, 11_LVBus0891502_production, 11_LVBus0891503_consumption, 11_LVBus0891503_production, 11_LVBus0891504_consumption, 11_LVBus0891504_production, 11_LVBus0891505_production, 11_LVBus0891506_consumption, 11_LVBus0891506_production, 11_LVBus0891507_production, 11_LVBus0891508_consumption, 11_LVBus0891508_production, 11_LVBus0891509_consumption, 11_LVBus0891509_production, 11_LVBus0891511_consumption, 11_LVBus0891511_production, 11_LVBus0891512_consumption, 11_LVBus0891512_production, 11_LVBus0891513_consumption, 11_LVBus0891513_production, 11_LVBus0891514_production, 11_LVBus0891515_consumption, 11_LVBus0891515_production, 11_LVBus0891516_production, 11_LVBus0891518_consumption, 11_LVBus0891518_production, 11_LVBus0891519_consumption, 11_LVBus0891519_production, 11_LVBus0891520_consumption, 11_LVBus0891520_production, 11_LVBus0891521_production, 11_LVBus0891523_consumption, 11_LVBus0891523_production, 11_LVBus0891524_consumption, 11_LVBus0891524_production, 11_LVBus0891525_consumption, 11_LVBus0891525_production, 11_LVBus0891526_consumption, 11_LVBus0891526_production, 11_LVBus0891527_consumption, 11_LVBus0891527_production, 11_LVBus0891528_production, 11_LVBus0891529_consumption, 11_LVBus0891529_production, 11_LVBus0891530_production, 11_LVBus0891531_production, 11_LVBus0891533_production, 11_LVBus0891534_production, 11_LVBus0891535_production, 11_LVBus0891536_production, 11_LVBus0891537_production, 11_LVBus0891538_production, 11_LVBus0891539_production, 11_LVBus0891540_production, 11_LVBus0891542_production, 11_LVBus0891543_production, 11_LVBus0891544_production, 11_LVBus0891545_production, 11_LVBus0891546_production, 11_LVBus0891547_production, 11_LVBus0891548_production, 11_LVBus0891549_production, 11_LVBus0891550_production, 11_LVBus0891551_production, 11_LVBus0891552_production, 11_LVBus0891553_production, 11_LVBus0891554_production, 11_LVBus0891556_production, 11_LVBus0891557_production, 11_LVBus0891558_production, 11_LVBus0891559_production, 11_LVBus0891560_production, 11_LVBus0891561_production, 11_LVBus0891563_production, 11_LVBus0891564_production, 11_LVBus0891565_production, 11_LVBus0891566_production, 11_LVBus0891567_production, 11_LVBus0891568_production, 11_LVBus0891569_production, 11_LVBus0891570_production, 11_LVBus0891571_production, 11_LVBus0891572_production, 11_LVBus0891574_production, 11_LVBus0891575_production, 11_LVBus0891576_production, 11_LVBus0891577_consumption, 11_LVBus0891577_production, 11_LVBus0891578_production, 11_LVBus0891579_production, 11_LVBus0891581_production, 11_LVBus0891582_consumption, 11_LVBus0891582_production, 11_LVBus0891583_production, 11_LVBus0891585_production, 11_LVBus0891587_production, 11_LVBus0891588_production, 11_LVBus0891589_production, 11_LVBus0891591_consumption, 11_LVBus0891591_production, 11_LVBus0891592_production, 11_LVBus0891593_consumption, 11_LVBus0891593_production, 11_LVBus0891594_production, 11_LVBus0891595_production, 11_LVBus0891596_production, 11_LVBus0891597_production, 11_LVBus0891598_production, 11_LVBus0891599_production, 11_LVBus0891600_production, 11_LVBus0891601_production, 11_LVBus0891602_production, 11_LVBus0891603_consumption, 11_LVBus0891603_production, 11_LVBus0891604_production, 11_LVBus0891605_consumption, 11_LVBus0891605_production, 11_LVBus0891606_production, 11_LVBus0891608_production, 11_LVBus0891609_consumption, 11_LVBus0891609_production, 11_LVBus0891611_consumption, 11_LVBus0891611_production, 11_LVBus0891612_production, 11_LVBus0891613_consumption, 11_LVBus0891613_production, 11_LVBus0891614_production, 11_LVBus0891615_production, 11_LVBus0891616_production, 11_LVBus0891617_production, 11_LVBus0891618_production, 11_LVBus0891619_production, 11_LVBus0891620_production, 11_LVBus0891621_production, 11_LVBus0891623_consumption, 11_LVBus0891623_production, 11_LVBus0891624_consumption, 11_LVBus0891624_production, 11_LVBus0891625_production, 11_LVBus0891627_consumption, 11_LVBus0891627_production, 11_LVBus0891628_production, 11_LVBus0891629_production, 11_LVBus0891630_production, 11_LVBus0891631_production, 11_LVBus0891632_production, 11_LVBus0891633_production, 11_LVBus0891634_production, 11_LVBus0891635_production, 11_LVBus0891636_production, 11_LVBus0891638_production, 11_LVBus0891639_production, 11_LVBus0891640_production, 11_LVBus0891642_consumption, 11_LVBus0891642_production, 11_LVBus0891643_production, 11_LVBus0891644_production, 11_LVBus0891645_consumption, 11_LVBus0891645_production, 11_LVBus0891646_production, 11_LVBus0891648_production, 11_LVBus0891650_consumption, 11_LVBus0891650_production, 11_LVBus0891651_production, 11_LVBus0891652_production, 11_LVBus0891653_production, 11_LVBus0891654_production, 11_LVBus0891656_production, 11_LVBus0891658_production, 11_LVBus0891659_production, 11_LVBus0891660_consumption, 11_LVBus0891660_production, 11_LVBus0891661_production, 11_LVBus0891662_production, 11_LVBus0891663_production, 11_LVBus0891664_production, 11_LVBus0891665_production, 11_LVBus0891666_production, 11_LVBus0891667_production, 11_LVBus0891668_production, 11_LVBus0891669_consumption, 11_LVBus0891669_production, 11_LVBus0891670_production, 11_LVBus0891671_production, 11_LVBus0891672_production, 11_LVBus0891673_consumption, 11_LVBus0891673_production, 11_LVBus0891674_production, 11_LVBus0891675_production, 11_LVBus0891676_production, 11_LVBus0891677_production, 11_LVBus0891678_production, 11_LVBus0891679_production, 11_LVBus0891680_production, 11_LVBus0891682_consumption, 11_LVBus0891682_production, 11_LVBus0891683_consumption, 11_LVBus0891683_production, 11_LVBus0891684_consumption, 11_LVBus0891684_production, 11_LVBus0891685_production, 11_LVBus0891686_production, 11_LVBus0891687_production, 11_LVBus0891688_production, 11_LVBus0891689_consumption, 11_LVBus0891689_production, 11_LVBus0891690_production, 11_LVBus0891691_production, 11_LVBus0891692_production, 11_LVBus0891693_production, 11_LVBus0891694_production, 11_LVBus0891695_production, 11_LVBus0891696_production, 11_LVBus0891697_production, 11_LVBus0891698_production, 11_LVBus0891699_production, 11_LVBus0891700_production, 11_LVBus0891701_consumption, 11_LVBus0891701_production, 11_LVBus0891702_production, 11_LVBus0891703_production, 11_LVBus0891704_production, 11_LVBus0891705_production, 11_LVBus0891706_production, 11_LVBus0891707_production, 11_LVBus0891708_production, 11_LVBus0891709_production, 11_LVBus0891710_production, 11_LVBus0891712_consumption, 11_LVBus0891712_production, 11_LVBus0891713_consumption, 11_LVBus0891713_production, 11_LVBus0891714_consumption, 11_LVBus0891714_production, 11_LVBus0891715_production, 11_LVBus0891716_consumption, 11_LVBus0891716_production, 11_LVBus0891717_production, 11_LVBus0891718_production, 11_LVBus0891719_consumption, 11_LVBus0891719_production, 11_LVBus0891721_production, 11_LVBus0891722_consumption, 11_LVBus0891722_production, 11_LVBus0891723_consumption, 11_LVBus0891723_production, 11_LVBus0891724_production, 11_LVBus0891725_production, 11_LVBus0891726_production, 11_LVBus0891727_production, 11_LVBus0891728_production, 11_LVBus0891729_production, 11_LVBus0891730_production, 11_LVBus0891731_production, 11_LVBus0891732_production, 11_LVBus0891733_consumption, 11_LVBus0891733_production, 11_LVBus0891734_production, 11_LVBus0891735_production, 11_LVBus0891736_production, 11_LVBus0891737_production, 11_LVBus0891738_production, 11_LVBus0891739_consumption, 11_LVBus0891739_production, 11_LVBus0891740_production, 11_LVBus0891741_production, 11_LVBus0891743_consumption, 11_LVBus0891743_production, 11_LVBus0891744_production, 11_LVBus0891745_production, 11_LVBus0891746_production, 11_LVBus0891747_production, 11_LVBus0891748_production, 11_LVBus0891749_production, 11_LVBus0891750_production, 11_LVBus0891751_production, 11_LVBus0891752_consumption, 11_LVBus0891752_production, 11_LVBus0891753_production, 11_LVBus0891754_production, 11_LVBus0891755_production, 11_LVBus0891756_consumption, 11_LVBus0891756_production, 11_LVBus0891758_consumption, 11_LVBus0891758_production, 11_LVBus0891759_consumption, 11_LVBus0891759_production, 11_LVBus0891760_production, 11_LVBus0891761_production, 11_LVBus0891762_consumption, 11_LVBus0891762_production, 11_LVBus0891763_production, 11_LVBus0891765_production, 11_LVBus0891766_production, 11_LVBus0891767_production, 11_LVBus0891768_production, 11_LVBus0891769_production, 11_LVBus0891771_consumption, 11_LVBus0891771_production, 11_LVBus0891772_production, 11_LVBus0891773_production, 11_LVBus0891774_production, 11_LVBus0891775_production, 11_LVBus0891776_production, 11_LVBus0891777_consumption, 11_LVBus0891777_production, 11_LVBus0891778_production, 11_LVBus0891779_production, 11_LVBus0891780_production, 11_LVBus0891781_production, 11_LVBus0891782_production, 11_LVBus0891783_production, 11_LVBus0891785_consumption, 11_LVBus0891785_production, 11_LVBus0891786_production, 11_LVBus0891787_production, 11_LVBus0891788_production, 11_LVBus0891789_production, 11_LVBus0891790_production, 11_LVBus0891791_production, 11_LVBus0891792_production, 11_LVBus0891793_production, 11_LVBus0891794_production, 11_LVBus0891795_consumption, 11_LVBus0891795_production, 11_LVBus0891796_production, 11_LVBus0891798_production, 11_LVBus0891799_production, 11_LVBus0891800_production, 11_LVBus0891801_production, 11_LVBus0891802_production, 11_LVBus0891803_production, 11_LVBus0891804_production, 11_LVBus0891806_production, 11_LVBus0891808_consumption, 11_LVBus0891808_production, 11_LVBus0891809_production, 11_LVBus0891811_consumption, 11_LVBus0891811_production, 11_LVBus0891812_production, 11_LVBus0891813_production, 11_LVBus0891815_production, 11_LVBus0891817_production, 11_LVBus0891818_production, 11_LVBus0891819_production, 11_LVBus0891821_consumption, 11_LVBus0891821_production, 11_LVBus0891822_production, 11_LVBus0891823_production, 11_LVBus0891824_production, 11_LVBus0891825_production, 11_LVBus0891826_production, 11_LVBus0891827_production, 11_LVBus0891828_production, 11_LVBus0891829_production, 11_LVBus0891830_production, 11_LVBus0891831_production, 11_LVBus0891832_production, 11_LVBus0891833_consumption, 11_LVBus0891833_production, 11_LVBus0891835_production, 11_LVBus0891836_production, 11_LVBus0891837_production, 11_LVBus0891838_production, 11_LVBus0891839_production, 11_LVBus0891840_production, 11_LVBus0891841_consumption, 11_LVBus0891841_production, 11_LVBus0891842_production, 11_LVBus0891843_production, 11_LVBus0891844_production, 11_LVBus0891846_production, 11_LVBus0891848_consumption, 11_LVBus0891848_production, 11_LVBus0891849_production, 11_LVBus0891850_production, 11_LVBus0891851_production, 11_LVBus0891852_production, 11_LVBus0891853_consumption, 11_LVBus0891853_production, 11_LVBus0891854_production, 11_LVBus0891855_production, 11_LVBus0891856_production, 11_LVBus0891857_production, 11_LVBus0891859_production, 11_LVBus0891861_consumption, 11_LVBus0891861_production, 11_LVBus0891862_production, 11_LVBus0891863_production, 11_LVBus0891864_production, 11_LVBus0891865_production, 11_LVBus0891866_production, 11_LVBus0891867_production, 11_LVBus0891868_consumption, 11_LVBus0891868_production, 11_LVBus0891869_consumption, 11_LVBus0891869_production, 11_LVBus0891870_consumption, 11_LVBus0891870_production, 11_LVBus0891871_consumption, 11_LVBus0891871_production, 11_LVBus0891873_production, 11_LVBus0891874_production, 11_LVBus0891875_production, 11_LVBus0891877_production, 11_LVBus1282564_consumption, 11_LVBus1282564_production, 11_LVBus1282565_production, 11_LVBus1282566_production, 11_LVBus1282567_production, 11_LVBus1284260_production, 11_LVBus1284908_production, 11_LVBus1284909_production, 11_LVBus1284910_production, 11_LVBus1284911_consumption, 11_LVBus1284911_production, 11_LVBus1284912_consumption, 11_LVBus1284912_production, 11_LVBus1284913_production, 11_LVBus1286516_production, 11_LVBus1286517_production, 11_LVBus1286518_production, 11_LVBus1286519_production, 11_LVBus1286520_production, 11_LVBus1286521_production, 11_LVBus1286522_production, 11_LVBus1286523_production, 11_LVBus1286524_production, 11_LVBus1297799_production, 11_LVBus1297800_production, 11_LVBus1297801_production, 11_LVBus1297802_production, 11_LVBus1297803_production, 11_LVBus1297804_production, 11_LVBus1303379_production, 11_LVBus1303380_production, 11_LVBus1303381_production, 11_LVBus1303382_production, 11_LVBus1369164_consumption, 11_LVBus1369164_production, 11_LVBus1369165_production, 11_LVBus1369166_production, 11_LVBus1369167_production, 11_LVBus1369168_consumption, 11_LVBus1369168_production, 11_LVBus1369169_production, 11_LVBus1369170_production, 11_LVBus1369171_production, 11_LVBus1369172_production, 11_LVBus1369173_production, 11_LVBus1369174_consumption, 11_LVBus1369174_production, 11_LVBus1369175_production, 11_LVBus1369176_production, 11_LVBus1369177_production, 11_LVBus1369178_production, 11_LVBus1369179_consumption, 11_LVBus1369179_production, 11_LVBus1369180_production, 11_LVBus1369181_production, 11_LVBus1369182_production, 11_LVBus1369183_production, 11_LVBus1369184_consumption, 11_LVBus1369184_production, 11_LVBus1369185_production, 11_LVBus1369186_production, 11_LVBus1369187_consumption, 11_LVBus1369187_production, 11_LVBus1369188_consumption, 11_LVBus1369188_production, 11_LVBus1369189_consumption, 11_LVBus1369189_production, 11_LVBus1369190_consumption, 11_LVBus1369190_production, 11_LVBus1369191_consumption, 11_LVBus1369191_production, 11_LVBus1369192_consumption, 11_LVBus1369192_production, 11_LVBus1369193_consumption, 11_LVBus1369193_production, 11_LVBus1369194_production, 11_LVBus1369195_consumption, 11_LVBus1369195_production, 11_LVBus1369196_production, 11_LVBus1369197_production, 11_LVBus1369198_production, 11_LVBus1369199_production, 11_LVBus1369200_production, 11_LVBus1369201_production, 11_LVBus1369202_consumption, 11_LVBus1369202_production, 11_LVBus1369203_consumption, 11_LVBus1369203_production, 11_LVBus1369204_production, 11_LVBus1369205_production, 11_LVBus1369206_production, 11_LVBus1369207_production, 11_LVBus1369208_production, 11_LVBus1369209_production, 11_LVBus1369210_production, 11_LVBus1369211_production, 11_LVBus1369212_consumption, 11_LVBus1369212_production, 11_LVBus1369213_production, 11_LVBus1369214_production, 11_LVBus1369215_consumption, 11_LVBus1369215_production, 11_LVBus1369216_production, 11_LVBus1369217_production, 11_LVBus1369218_production, 11_LVBus1369219_consumption, 11_LVBus1369219_production, 11_LVBus1369220_production, 11_LVBus1369221_production, 11_LVBus1369222_production, 11_LVBus1369223_production, 11_LVBus1369224_production, 11_LVBus1369225_consumption, 11_LVBus1369225_production, 11_LVBus1369226_consumption, 11_LVBus1369226_production, 11_LVBus1369227_production, 11_LVBus1369228_production, 11_LVBus1369229_production, 11_LVBus1369230_production, 11_LVBus1369231_production, 11_LVBus1369232_production, 11_LVBus1369233_consumption, 11_LVBus1369233_production, 11_LVBus1369234_production, 11_LVBus1369235_production, 11_LVBus1369236_production, 11_LVBus1369237_production, 11_LVBus1369238_production, 11_LVBus1369239_production, 11_LVBus1369240_production, 11_LVBus1369241_production, 11_LVBus1369242_production, 11_LVBus1369243_production, 11_LVBus1369244_consumption, 11_LVBus1369244_production, 11_LVBus1369245_production, 11_LVBus1369246_production, 11_LVBus1369247_production, 11_LVBus1369248_production, 11_LVBus1369249_production, 11_LVBus1369250_production, 11_LVBus1369251_consumption, 11_LVBus1369251_production, 11_LVBus1369252_consumption, 11_LVBus1369252_production, 11_LVBus1369253_consumption, 11_LVBus1369253_production, 11_LVBus1369254_production, 11_LVBus1369255_production, 11_LVBus1369256_consumption, 11_LVBus1369256_production, 11_LVBus1369257_production, 11_LVBus1369258_consumption, 11_LVBus1369258_production, 11_LVBus1369259_production, 11_LVBus1369260_production, 11_LVBus1369261_consumption, 11_LVBus1369261_production, 11_LVBus1369262_production, 11_LVBus1369263_production, 11_LVBus1369264_consumption, 11_LVBus1369264_production, 11_LVBus1369265_consumption, 11_LVBus1369265_production, 11_LVBus1369266_consumption, 11_LVBus1369266_production, 11_LVBus1369267_production, 11_LVBus1369268_consumption, 11_LVBus1369268_production, 11_LVBus1369269_consumption, 11_LVBus1369269_production, 11_LVBus1369270_consumption, 11_LVBus1369270_production, 11_LVBus1369271_production, 11_LVBus1369272_production, 11_LVBus1369273_production, 11_LVBus1369274_production, 11_LVBus1369275_production, 11_LVBus1369276_production, 11_LVBus1369277_production, 11_LVBus1369278_consumption, 11_LVBus1369278_production, 11_LVBus1370343_production, 11_LVBus1370344_production, 11_LVBus1370345_production, 11_LVBus1370346_production, 11_LVBus1370347_production, 11_LVBus1370348_production, 11_LVBus1370349_production, 11_LVBus1370350_production, 11_LVBus1370351_production, 11_LVBus1370352_production, 11_LVBus1370353_production, 11_LVBus1370354_production, 11_LVBus1370355_production, 11_LVBus1370356_production, 11_LVBus1370357_production, 11_LVBus1370358_production, 11_LVBus1370359_production, 11_LVBus1370360_consumption, 11_LVBus1370360_production, 11_MVLV35758_consumption, 11_MVLV35758_production, 11_MVLV46971_production, 11_MVLV73641_consumption, 11_MVLV73641_production.

