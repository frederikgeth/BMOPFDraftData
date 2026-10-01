# BMOPF Network Summary: 52_MVFeeder0054

**Generated:** 2026-10-01 23:34:11  
**Findings:** 0 errors · 5 warnings · 244 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 36 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 412 |  |
| line | 375 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 614 | 1.776 MW, 532.7 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 36 |  |
| switch | 0 |  |
| transformer | 36 | Dyn11×36 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 72 | 71 | 6 | 0 |
| LV_236V | 236.0 V | 340 | 304 | 608 | 0 |

**Transformer transitions:**

- `52_MVLV088401_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV014241_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV040141_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV014242_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV040827_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV001043_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV008599_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV015426_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV000964_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV029273_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV089854_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV045010_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV040150_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV071606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV064012_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV058816_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV033701_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104577_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV080908_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV042493_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV064057_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV083405_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV028965_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV092694_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV001615_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV083404_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009306_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV014295_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV046526_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV040162_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV083383_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV097524_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV028631_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV059309_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV003697_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV069614_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 146 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 412 | 1 | 411 | 0 | 0 | 0 |
| Tier LV_236V | 340 | 36 | 304 | 0 | 0 | 0 |
| Tier MV_11.8kV | 72 | 1 | 71 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 36; skipped invalid branches: 0.

Galvanic zones: 37; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_ANCEN | MV_11.8kV | 72 | 0 | 0 | 36 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1576 declared bus terminals; 1429 mapped line/closed-switch conductor edges; 147 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 18100.0 | 2.361 | 1842 |
| q_nom | 0.0 | 5440.0 | 2.361 | 1842 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.819 | 5320.0 | 2.09 | 375 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.527 | 36 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 369 of 614 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646946_consumption' has phase imbalance of 292.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646678_consumption' has phase imbalance of 176.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646747_consumption' has phase imbalance of 146.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646602_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646647_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646759_consumption' has phase imbalance of 236.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646712_consumption' has phase imbalance of 69.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646643_consumption' has phase imbalance of 295.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646785_consumption' has phase imbalance of 103.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646705_consumption' has phase imbalance of 121.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646681_consumption' has phase imbalance of 289.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646916_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646834_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646898_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646691_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646673_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646881_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646729_consumption' has phase imbalance of 248.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646784_consumption' has phase imbalance of 216.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646695_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646761_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646780_consumption' has phase imbalance of 245.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646755_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646758_consumption' has phase imbalance of 209.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646723_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646921_consumption' has phase imbalance of 228.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646823_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646654_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1156779_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646794_consumption' has phase imbalance of 284.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646690_consumption' has phase imbalance of 140.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646722_consumption' has phase imbalance of 239.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646593_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646732_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646912_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646928_consumption' has phase imbalance of 198.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646922_consumption' has phase imbalance of 52.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646754_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646867_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646893_consumption' has phase imbalance of 120.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646943_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646689_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646861_consumption' has phase imbalance of 74.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646832_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646622_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646863_consumption' has phase imbalance of 204.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646693_consumption' has phase imbalance of 101.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646788_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646715_consumption' has phase imbalance of 139.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646697_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646901_consumption' has phase imbalance of 105.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646615_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646809_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646934_consumption' has phase imbalance of 135.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646792_consumption' has phase imbalance of 255.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646728_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646698_consumption' has phase imbalance of 150.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646879_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646949_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646699_consumption' has phase imbalance of 120.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646675_consumption' has phase imbalance of 209.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646656_consumption' has phase imbalance of 189.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646740_consumption' has phase imbalance of 125.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646899_consumption' has phase imbalance of 187.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646878_consumption' has phase imbalance of 282.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646812_consumption' has phase imbalance of 139.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1156782_consumption' has phase imbalance of 104.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646736_consumption' has phase imbalance of 288.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646608_consumption' has phase imbalance of 241.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646630_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646741_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646841_consumption' has phase imbalance of 120.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646671_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646804_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646821_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646629_consumption' has phase imbalance of 176.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646931_consumption' has phase imbalance of 122.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646676_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646820_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646877_consumption' has phase imbalance of 192.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646802_consumption' has phase imbalance of 147.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646864_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646617_consumption' has phase imbalance of 153.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646930_consumption' has phase imbalance of 131.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646616_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646680_consumption' has phase imbalance of 214.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1140759_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646835_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646744_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646777_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646601_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646734_consumption' has phase imbalance of 85.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646765_consumption' has phase imbalance of 249.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646927_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646760_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646650_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646917_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646942_consumption' has phase imbalance of 282.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646795_consumption' has phase imbalance of 261.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646614_consumption' has phase imbalance of 210.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646595_consumption' has phase imbalance of 31.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646692_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646597_consumption' has phase imbalance of 125.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646831_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646781_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646787_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646932_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646865_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646626_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646672_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646858_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646855_consumption' has phase imbalance of 235.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646791_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1156781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646660_consumption' has phase imbalance of 264.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646735_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646661_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646891_consumption' has phase imbalance of 236.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646737_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646874_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646621_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646746_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646600_consumption' has phase imbalance of 122.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646646_consumption' has phase imbalance of 119.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646598_consumption' has phase imbalance of 87.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646649_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646704_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646908_consumption' has phase imbalance of 266.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1140758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646846_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646900_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646828_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646612_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646885_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646727_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646620_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646607_consumption' has phase imbalance of 154.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646918_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646870_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646711_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646822_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646611_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646721_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646862_consumption' has phase imbalance of 230.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646609_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646604_consumption' has phase imbalance of 279.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646890_consumption' has phase imbalance of 294.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646819_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646803_consumption' has phase imbalance of 242.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646796_consumption' has phase imbalance of 283.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646664_consumption' has phase imbalance of 297.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646726_consumption' has phase imbalance of 273.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1156778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646856_consumption' has phase imbalance of 40.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646618_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646944_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646591_consumption' has phase imbalance of 158.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646623_consumption' has phase imbalance of 231.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646594_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646742_consumption' has phase imbalance of 107.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646670_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646887_consumption' has phase imbalance of 205.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646914_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646596_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646677_consumption' has phase imbalance of 78.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus646880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 614 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus1154433' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus646750' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus646701' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.776 MW |
| Total load Q | 532.7 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV088401_Transformer | 275.0 kVA | 18.0% |
| 52_MVLV014241_Transformer | 176.0 kVA | 18.7% |
| 52_MVLV040141_Transformer | 693.0 kVA | 30.9% |
| 52_MVLV014242_Transformer | 176.0 kVA | 17.7% |
| 52_MVLV040827_Transformer | 275.0 kVA | 27.4% |
| 52_MVLV001043_Transformer | 440.0 kVA | 31.0% |
| 52_MVLV008599_Transformer | 110.0 kVA | 7.1% |
| 52_MVLV015426_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV000964_Transformer | 440.0 kVA | 23.1% |
| 52_MVLV029273_Transformer | 275.0 kVA | 8.7% |
| 52_MVLV089854_Transformer | 275.0 kVA | 36.3% |
| 52_MVLV045010_Transformer | 110.0 kVA | 7.2% |
| 52_MVLV040150_Transformer | 440.0 kVA | 41.1% |
| 52_MVLV071606_Transformer | 176.0 kVA | 7.7% |
| 52_MVLV064012_Transformer | 110.0 kVA | 21.8% |
| 52_MVLV058816_Transformer | 176.0 kVA | 13.9% |
| 52_MVLV033701_Transformer | 110.0 kVA | 10.6% |
| 52_MVLV104577_Transformer | 176.0 kVA | 18.9% |
| 52_MVLV080908_Transformer | 176.0 kVA | 9.3% |
| 52_MVLV042493_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV064057_Transformer | 110.0 kVA | 25.4% |
| 52_MVLV083405_Transformer | 440.0 kVA | 27.1% |
| 52_MVLV028965_Transformer | 275.0 kVA | 9.9% |
| 52_MVLV092694_Transformer | 110.0 kVA | 2.3% |
| 52_MVLV001615_Transformer | 176.0 kVA | 10.2% |
| 52_MVLV083404_Transformer | 176.0 kVA | 16.2% |
| 52_MVLV009306_Transformer | 275.0 kVA | 16.7% |
| 52_MVLV014295_Transformer | 275.0 kVA | 28.2% |
| 52_MVLV046526_Transformer | 275.0 kVA | 24.0% |
| 52_MVLV040162_Transformer | 110.0 kVA | 3.9% |
| 52_MVLV083383_Transformer | 440.0 kVA | 24.9% |
| 52_MVLV097524_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV028631_Transformer | 275.0 kVA | 20.8% |
| 52_MVLV059309_Transformer | 275.0 kVA | 13.1% |
| 52_MVLV003697_Transformer | 275.0 kVA | 13.5% |
| 52_MVLV069614_Transformer | 440.0 kVA | 25.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.78 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus646750' (LV, 0.24 kV) has an electrical reach of 16.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus646642' (LV, 0.24 kV) has an electrical reach of 21.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus646701' (LV, 0.24 kV) has an electrical reach of 18.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 412 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 412 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 36 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 72 |
| LV_236V | 4-wire | 340 / 340 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 340 |
| Neutral branches | 304 |
| Grounding points | 36 |
| Neutral sections | 36 |
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
| 11.78 kV | 72 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 37 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1880.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 340 / 72 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 370 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 370 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1140758_production, 52_LVBus1140759_production, 52_LVBus1149113_consumption, 52_LVBus1149113_production, 52_LVBus1149132_consumption, 52_LVBus1149132_production, 52_LVBus1149137_consumption, 52_LVBus1149137_production, 52_LVBus1149158_consumption, 52_LVBus1149158_production, 52_LVBus1149178_consumption, 52_LVBus1149178_production, 52_LVBus1149196_consumption, 52_LVBus1149196_production, 52_LVBus1154433_consumption, 52_LVBus1154433_production, 52_LVBus1156537_consumption, 52_LVBus1156537_production, 52_LVBus1156778_production, 52_LVBus1156779_production, 52_LVBus1156780_consumption, 52_LVBus1156780_production, 52_LVBus1156781_production, 52_LVBus1156782_production, 52_LVBus1162272_consumption, 52_LVBus1162272_production, 52_LVBus646591_production, 52_LVBus646592_production, 52_LVBus646593_production, 52_LVBus646594_production, 52_LVBus646595_production, 52_LVBus646596_production, 52_LVBus646597_production, 52_LVBus646598_production, 52_LVBus646600_production, 52_LVBus646601_production, 52_LVBus646602_production, 52_LVBus646604_production, 52_LVBus646605_production, 52_LVBus646607_production, 52_LVBus646608_production, 52_LVBus646609_production, 52_LVBus646611_production, 52_LVBus646612_production, 52_LVBus646613_production, 52_LVBus646614_production, 52_LVBus646615_production, 52_LVBus646616_production, 52_LVBus646617_production, 52_LVBus646618_production, 52_LVBus646619_consumption, 52_LVBus646619_production, 52_LVBus646620_production, 52_LVBus646621_production, 52_LVBus646622_production, 52_LVBus646623_production, 52_LVBus646624_production, 52_LVBus646625_production, 52_LVBus646626_production, 52_LVBus646628_production, 52_LVBus646629_production, 52_LVBus646630_production, 52_LVBus646632_consumption, 52_LVBus646632_production, 52_LVBus646634_production, 52_LVBus646636_consumption, 52_LVBus646636_production, 52_LVBus646638_consumption, 52_LVBus646638_production, 52_LVBus646640_consumption, 52_LVBus646640_production, 52_LVBus646642_consumption, 52_LVBus646642_production, 52_LVBus646643_production, 52_LVBus646646_production, 52_LVBus646647_production, 52_LVBus646648_consumption, 52_LVBus646648_production, 52_LVBus646649_production, 52_LVBus646650_production, 52_LVBus646651_consumption, 52_LVBus646651_production, 52_LVBus646653_production, 52_LVBus646654_production, 52_LVBus646655_production, 52_LVBus646656_production, 52_LVBus646657_production, 52_LVBus646658_production, 52_LVBus646660_production, 52_LVBus646661_production, 52_LVBus646662_consumption, 52_LVBus646662_production, 52_LVBus646663_consumption, 52_LVBus646663_production, 52_LVBus646664_production, 52_LVBus646665_production, 52_LVBus646666_production, 52_LVBus646668_production, 52_LVBus646670_production, 52_LVBus646671_production, 52_LVBus646672_production, 52_LVBus646673_production, 52_LVBus646674_production, 52_LVBus646675_production, 52_LVBus646676_production, 52_LVBus646677_production, 52_LVBus646678_production, 52_LVBus646680_production, 52_LVBus646681_production, 52_LVBus646683_consumption, 52_LVBus646683_production, 52_LVBus646685_consumption, 52_LVBus646685_production, 52_LVBus646687_consumption, 52_LVBus646687_production, 52_LVBus646689_production, 52_LVBus646690_production, 52_LVBus646691_production, 52_LVBus646692_production, 52_LVBus646693_production, 52_LVBus646695_production, 52_LVBus646697_production, 52_LVBus646698_production, 52_LVBus646699_production, 52_LVBus646701_production, 52_LVBus646703_production, 52_LVBus646704_production, 52_LVBus646705_production, 52_LVBus646707_consumption, 52_LVBus646707_production, 52_LVBus646708_consumption, 52_LVBus646708_production, 52_LVBus646709_consumption, 52_LVBus646709_production, 52_LVBus646711_production, 52_LVBus646712_production, 52_LVBus646713_production, 52_LVBus646714_production, 52_LVBus646715_production, 52_LVBus646717_production, 52_LVBus646718_production, 52_LVBus646719_production, 52_LVBus646721_production, 52_LVBus646722_production, 52_LVBus646723_production, 52_LVBus646724_production, 52_LVBus646725_production, 52_LVBus646726_production, 52_LVBus646727_production, 52_LVBus646728_production, 52_LVBus646729_production, 52_LVBus646730_consumption, 52_LVBus646730_production, 52_LVBus646732_production, 52_LVBus646733_consumption, 52_LVBus646733_production, 52_LVBus646734_production, 52_LVBus646735_production, 52_LVBus646736_production, 52_LVBus646737_production, 52_LVBus646739_production, 52_LVBus646740_production, 52_LVBus646741_production, 52_LVBus646742_production, 52_LVBus646743_production, 52_LVBus646744_production, 52_LVBus646745_production, 52_LVBus646746_production, 52_LVBus646747_production, 52_LVBus646750_production, 52_LVBus646752_consumption, 52_LVBus646752_production, 52_LVBus646754_production, 52_LVBus646755_production, 52_LVBus646756_production, 52_LVBus646757_production, 52_LVBus646758_production, 52_LVBus646759_production, 52_LVBus646760_production, 52_LVBus646761_production, 52_LVBus646762_consumption, 52_LVBus646762_production, 52_LVBus646763_production, 52_LVBus646765_production, 52_LVBus646767_consumption, 52_LVBus646767_production, 52_LVBus646769_consumption, 52_LVBus646769_production, 52_LVBus646771_consumption, 52_LVBus646771_production, 52_LVBus646773_consumption, 52_LVBus646773_production, 52_LVBus646775_production, 52_LVBus646776_production, 52_LVBus646777_production, 52_LVBus646780_production, 52_LVBus646781_production, 52_LVBus646782_production, 52_LVBus646783_production, 52_LVBus646784_production, 52_LVBus646785_production, 52_LVBus646786_consumption, 52_LVBus646786_production, 52_LVBus646787_production, 52_LVBus646788_production, 52_LVBus646790_production, 52_LVBus646791_production, 52_LVBus646792_production, 52_LVBus646794_production, 52_LVBus646795_production, 52_LVBus646796_production, 52_LVBus646797_production, 52_LVBus646798_production, 52_LVBus646799_consumption, 52_LVBus646799_production, 52_LVBus646801_production, 52_LVBus646802_production, 52_LVBus646803_production, 52_LVBus646804_production, 52_LVBus646805_consumption, 52_LVBus646805_production, 52_LVBus646806_production, 52_LVBus646808_consumption, 52_LVBus646808_production, 52_LVBus646809_production, 52_LVBus646810_production, 52_LVBus646812_production, 52_LVBus646813_production, 52_LVBus646814_consumption, 52_LVBus646814_production, 52_LVBus646815_production, 52_LVBus646817_consumption, 52_LVBus646817_production, 52_LVBus646818_production, 52_LVBus646819_production, 52_LVBus646820_production, 52_LVBus646821_production, 52_LVBus646822_production, 52_LVBus646823_production, 52_LVBus646824_production, 52_LVBus646825_consumption, 52_LVBus646825_production, 52_LVBus646826_production, 52_LVBus646828_production, 52_LVBus646829_production, 52_LVBus646831_production, 52_LVBus646832_production, 52_LVBus646833_production, 52_LVBus646834_production, 52_LVBus646835_production, 52_LVBus646837_consumption, 52_LVBus646837_production, 52_LVBus646838_consumption, 52_LVBus646838_production, 52_LVBus646839_consumption, 52_LVBus646839_production, 52_LVBus646840_production, 52_LVBus646841_production, 52_LVBus646842_production, 52_LVBus646844_consumption, 52_LVBus646844_production, 52_LVBus646845_production, 52_LVBus646846_production, 52_LVBus646847_production, 52_LVBus646848_production, 52_LVBus646849_production, 52_LVBus646850_production, 52_LVBus646851_production, 52_LVBus646853_consumption, 52_LVBus646853_production, 52_LVBus646854_production, 52_LVBus646855_production, 52_LVBus646856_production, 52_LVBus646858_production, 52_LVBus646859_production, 52_LVBus646861_production, 52_LVBus646862_production, 52_LVBus646863_production, 52_LVBus646864_production, 52_LVBus646865_production, 52_LVBus646866_consumption, 52_LVBus646866_production, 52_LVBus646867_production, 52_LVBus646868_production, 52_LVBus646869_production, 52_LVBus646870_production, 52_LVBus646872_production, 52_LVBus646873_production, 52_LVBus646874_production, 52_LVBus646875_production, 52_LVBus646876_production, 52_LVBus646877_production, 52_LVBus646878_production, 52_LVBus646879_production, 52_LVBus646880_production, 52_LVBus646881_production, 52_LVBus646883_production, 52_LVBus646884_production, 52_LVBus646885_production, 52_LVBus646886_consumption, 52_LVBus646886_production, 52_LVBus646887_production, 52_LVBus646888_production, 52_LVBus646890_production, 52_LVBus646891_production, 52_LVBus646892_production, 52_LVBus646893_production, 52_LVBus646895_production, 52_LVBus646896_production, 52_LVBus646897_production, 52_LVBus646898_production, 52_LVBus646899_production, 52_LVBus646900_production, 52_LVBus646901_production, 52_LVBus646904_consumption, 52_LVBus646904_production, 52_LVBus646905_consumption, 52_LVBus646905_production, 52_LVBus646906_consumption, 52_LVBus646906_production, 52_LVBus646907_production, 52_LVBus646908_production, 52_LVBus646909_production, 52_LVBus646910_production, 52_LVBus646911_production, 52_LVBus646912_production, 52_LVBus646913_production, 52_LVBus646914_production, 52_LVBus646915_consumption, 52_LVBus646915_production, 52_LVBus646916_production, 52_LVBus646917_production, 52_LVBus646918_production, 52_LVBus646920_consumption, 52_LVBus646920_production, 52_LVBus646921_production, 52_LVBus646922_production, 52_LVBus646923_consumption, 52_LVBus646923_production, 52_LVBus646924_consumption, 52_LVBus646924_production, 52_LVBus646925_consumption, 52_LVBus646925_production, 52_LVBus646926_production, 52_LVBus646927_production, 52_LVBus646928_production, 52_LVBus646930_production, 52_LVBus646931_production, 52_LVBus646932_production, 52_LVBus646934_production, 52_LVBus646936_consumption, 52_LVBus646936_production, 52_LVBus646938_consumption, 52_LVBus646938_production, 52_LVBus646940_consumption, 52_LVBus646940_production, 52_LVBus646942_production, 52_LVBus646943_production, 52_LVBus646944_production, 52_LVBus646945_production, 52_LVBus646946_production, 52_LVBus646948_consumption, 52_LVBus646948_production, 52_LVBus646949_production, 52_MVLV040415_consumption, 52_MVLV040415_production, 52_MVLV092789_consumption, 52_MVLV092789_production, 52_MVLV105904_consumption, 52_MVLV105904_production.

## 9. Data Quality Summary

**Total findings:** 249 (0 errors, 5 warnings, 244 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  369 of 614 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.78 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  370 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646946_consumption`  
  Load '52_LVBus646946_consumption' has phase imbalance of 292.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646678_consumption`  
  Load '52_LVBus646678_consumption' has phase imbalance of 176.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646747_consumption`  
  Load '52_LVBus646747_consumption' has phase imbalance of 146.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646602_consumption`  
  Load '52_LVBus646602_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646624_consumption`  
  Load '52_LVBus646624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646647_consumption`  
  Load '52_LVBus646647_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646759_consumption`  
  Load '52_LVBus646759_consumption' has phase imbalance of 236.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646824_consumption`  
  Load '52_LVBus646824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646712_consumption`  
  Load '52_LVBus646712_consumption' has phase imbalance of 69.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646643_consumption`  
  Load '52_LVBus646643_consumption' has phase imbalance of 295.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646883_consumption`  
  Load '52_LVBus646883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646785_consumption`  
  Load '52_LVBus646785_consumption' has phase imbalance of 103.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646705_consumption`  
  Load '52_LVBus646705_consumption' has phase imbalance of 121.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646681_consumption`  
  Load '52_LVBus646681_consumption' has phase imbalance of 289.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646872_consumption`  
  Load '52_LVBus646872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646916_consumption`  
  Load '52_LVBus646916_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646834_consumption`  
  Load '52_LVBus646834_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646898_consumption`  
  Load '52_LVBus646898_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646691_consumption`  
  Load '52_LVBus646691_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646673_consumption`  
  Load '52_LVBus646673_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646881_consumption`  
  Load '52_LVBus646881_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646729_consumption`  
  Load '52_LVBus646729_consumption' has phase imbalance of 248.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646784_consumption`  
  Load '52_LVBus646784_consumption' has phase imbalance of 216.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646695_consumption`  
  Load '52_LVBus646695_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646761_consumption`  
  Load '52_LVBus646761_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646815_consumption`  
  Load '52_LVBus646815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646780_consumption`  
  Load '52_LVBus646780_consumption' has phase imbalance of 245.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646755_consumption`  
  Load '52_LVBus646755_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646758_consumption`  
  Load '52_LVBus646758_consumption' has phase imbalance of 209.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646756_consumption`  
  Load '52_LVBus646756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646723_consumption`  
  Load '52_LVBus646723_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646921_consumption`  
  Load '52_LVBus646921_consumption' has phase imbalance of 228.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646823_consumption`  
  Load '52_LVBus646823_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646654_consumption`  
  Load '52_LVBus646654_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1156779_consumption`  
  Load '52_LVBus1156779_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646794_consumption`  
  Load '52_LVBus646794_consumption' has phase imbalance of 284.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646775_consumption`  
  Load '52_LVBus646775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646690_consumption`  
  Load '52_LVBus646690_consumption' has phase imbalance of 140.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646722_consumption`  
  Load '52_LVBus646722_consumption' has phase imbalance of 239.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646593_consumption`  
  Load '52_LVBus646593_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646732_consumption`  
  Load '52_LVBus646732_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646713_consumption`  
  Load '52_LVBus646713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646665_consumption`  
  Load '52_LVBus646665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646912_consumption`  
  Load '52_LVBus646912_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646897_consumption`  
  Load '52_LVBus646897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646928_consumption`  
  Load '52_LVBus646928_consumption' has phase imbalance of 198.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646797_consumption`  
  Load '52_LVBus646797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646798_consumption`  
  Load '52_LVBus646798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646763_consumption`  
  Load '52_LVBus646763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646719_consumption`  
  Load '52_LVBus646719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646592_consumption`  
  Load '52_LVBus646592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646668_consumption`  
  Load '52_LVBus646668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646922_consumption`  
  Load '52_LVBus646922_consumption' has phase imbalance of 52.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646754_consumption`  
  Load '52_LVBus646754_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646867_consumption`  
  Load '52_LVBus646867_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646893_consumption`  
  Load '52_LVBus646893_consumption' has phase imbalance of 120.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646907_consumption`  
  Load '52_LVBus646907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646840_consumption`  
  Load '52_LVBus646840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646943_consumption`  
  Load '52_LVBus646943_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646689_consumption`  
  Load '52_LVBus646689_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646861_consumption`  
  Load '52_LVBus646861_consumption' has phase imbalance of 74.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646832_consumption`  
  Load '52_LVBus646832_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646622_consumption`  
  Load '52_LVBus646622_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646863_consumption`  
  Load '52_LVBus646863_consumption' has phase imbalance of 204.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646693_consumption`  
  Load '52_LVBus646693_consumption' has phase imbalance of 101.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646788_consumption`  
  Load '52_LVBus646788_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646715_consumption`  
  Load '52_LVBus646715_consumption' has phase imbalance of 139.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646697_consumption`  
  Load '52_LVBus646697_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646901_consumption`  
  Load '52_LVBus646901_consumption' has phase imbalance of 105.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646615_consumption`  
  Load '52_LVBus646615_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646809_consumption`  
  Load '52_LVBus646809_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646934_consumption`  
  Load '52_LVBus646934_consumption' has phase imbalance of 135.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646792_consumption`  
  Load '52_LVBus646792_consumption' has phase imbalance of 255.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646728_consumption`  
  Load '52_LVBus646728_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646698_consumption`  
  Load '52_LVBus646698_consumption' has phase imbalance of 150.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646879_consumption`  
  Load '52_LVBus646879_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646613_consumption`  
  Load '52_LVBus646613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646873_consumption`  
  Load '52_LVBus646873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646949_consumption`  
  Load '52_LVBus646949_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646699_consumption`  
  Load '52_LVBus646699_consumption' has phase imbalance of 120.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646657_consumption`  
  Load '52_LVBus646657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646675_consumption`  
  Load '52_LVBus646675_consumption' has phase imbalance of 209.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646884_consumption`  
  Load '52_LVBus646884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646656_consumption`  
  Load '52_LVBus646656_consumption' has phase imbalance of 189.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646740_consumption`  
  Load '52_LVBus646740_consumption' has phase imbalance of 125.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646899_consumption`  
  Load '52_LVBus646899_consumption' has phase imbalance of 187.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646666_consumption`  
  Load '52_LVBus646666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646878_consumption`  
  Load '52_LVBus646878_consumption' has phase imbalance of 282.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646812_consumption`  
  Load '52_LVBus646812_consumption' has phase imbalance of 139.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646850_consumption`  
  Load '52_LVBus646850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1156782_consumption`  
  Load '52_LVBus1156782_consumption' has phase imbalance of 104.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646736_consumption`  
  Load '52_LVBus646736_consumption' has phase imbalance of 288.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646608_consumption`  
  Load '52_LVBus646608_consumption' has phase imbalance of 241.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646630_consumption`  
  Load '52_LVBus646630_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646741_consumption`  
  Load '52_LVBus646741_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646841_consumption`  
  Load '52_LVBus646841_consumption' has phase imbalance of 120.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646896_consumption`  
  Load '52_LVBus646896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646671_consumption`  
  Load '52_LVBus646671_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646804_consumption`  
  Load '52_LVBus646804_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646821_consumption`  
  Load '52_LVBus646821_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646625_consumption`  
  Load '52_LVBus646625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646629_consumption`  
  Load '52_LVBus646629_consumption' has phase imbalance of 176.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646931_consumption`  
  Load '52_LVBus646931_consumption' has phase imbalance of 122.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646833_consumption`  
  Load '52_LVBus646833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646676_consumption`  
  Load '52_LVBus646676_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646820_consumption`  
  Load '52_LVBus646820_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646877_consumption`  
  Load '52_LVBus646877_consumption' has phase imbalance of 192.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646802_consumption`  
  Load '52_LVBus646802_consumption' has phase imbalance of 147.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646864_consumption`  
  Load '52_LVBus646864_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646617_consumption`  
  Load '52_LVBus646617_consumption' has phase imbalance of 153.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646930_consumption`  
  Load '52_LVBus646930_consumption' has phase imbalance of 131.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646616_consumption`  
  Load '52_LVBus646616_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646680_consumption`  
  Load '52_LVBus646680_consumption' has phase imbalance of 214.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1140759_consumption`  
  Load '52_LVBus1140759_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646842_consumption`  
  Load '52_LVBus646842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646909_consumption`  
  Load '52_LVBus646909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646835_consumption`  
  Load '52_LVBus646835_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646744_consumption`  
  Load '52_LVBus646744_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646777_consumption`  
  Load '52_LVBus646777_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646601_consumption`  
  Load '52_LVBus646601_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646734_consumption`  
  Load '52_LVBus646734_consumption' has phase imbalance of 85.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646765_consumption`  
  Load '52_LVBus646765_consumption' has phase imbalance of 249.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646927_consumption`  
  Load '52_LVBus646927_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646760_consumption`  
  Load '52_LVBus646760_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646650_consumption`  
  Load '52_LVBus646650_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646917_consumption`  
  Load '52_LVBus646917_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646942_consumption`  
  Load '52_LVBus646942_consumption' has phase imbalance of 282.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646795_consumption`  
  Load '52_LVBus646795_consumption' has phase imbalance of 261.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646614_consumption`  
  Load '52_LVBus646614_consumption' has phase imbalance of 210.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646595_consumption`  
  Load '52_LVBus646595_consumption' has phase imbalance of 31.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646692_consumption`  
  Load '52_LVBus646692_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646845_consumption`  
  Load '52_LVBus646845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646597_consumption`  
  Load '52_LVBus646597_consumption' has phase imbalance of 125.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646831_consumption`  
  Load '52_LVBus646831_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646658_consumption`  
  Load '52_LVBus646658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646781_consumption`  
  Load '52_LVBus646781_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646787_consumption`  
  Load '52_LVBus646787_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646932_consumption`  
  Load '52_LVBus646932_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646865_consumption`  
  Load '52_LVBus646865_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646626_consumption`  
  Load '52_LVBus646626_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646790_consumption`  
  Load '52_LVBus646790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646739_consumption`  
  Load '52_LVBus646739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646945_consumption`  
  Load '52_LVBus646945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646672_consumption`  
  Load '52_LVBus646672_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646858_consumption`  
  Load '52_LVBus646858_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646776_consumption`  
  Load '52_LVBus646776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646826_consumption`  
  Load '52_LVBus646826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646855_consumption`  
  Load '52_LVBus646855_consumption' has phase imbalance of 235.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646791_consumption`  
  Load '52_LVBus646791_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1156781_consumption`  
  Load '52_LVBus1156781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646660_consumption`  
  Load '52_LVBus646660_consumption' has phase imbalance of 264.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646735_consumption`  
  Load '52_LVBus646735_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646869_consumption`  
  Load '52_LVBus646869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646661_consumption`  
  Load '52_LVBus646661_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646891_consumption`  
  Load '52_LVBus646891_consumption' has phase imbalance of 236.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646737_consumption`  
  Load '52_LVBus646737_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646874_consumption`  
  Load '52_LVBus646874_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646621_consumption`  
  Load '52_LVBus646621_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646746_consumption`  
  Load '52_LVBus646746_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646600_consumption`  
  Load '52_LVBus646600_consumption' has phase imbalance of 122.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646646_consumption`  
  Load '52_LVBus646646_consumption' has phase imbalance of 119.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646598_consumption`  
  Load '52_LVBus646598_consumption' has phase imbalance of 87.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646649_consumption`  
  Load '52_LVBus646649_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646892_consumption`  
  Load '52_LVBus646892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646704_consumption`  
  Load '52_LVBus646704_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646908_consumption`  
  Load '52_LVBus646908_consumption' has phase imbalance of 266.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646605_consumption`  
  Load '52_LVBus646605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1140758_consumption`  
  Load '52_LVBus1140758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646846_consumption`  
  Load '52_LVBus646846_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646900_consumption`  
  Load '52_LVBus646900_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646828_consumption`  
  Load '52_LVBus646828_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646895_consumption`  
  Load '52_LVBus646895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646757_consumption`  
  Load '52_LVBus646757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646612_consumption`  
  Load '52_LVBus646612_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646849_consumption`  
  Load '52_LVBus646849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646885_consumption`  
  Load '52_LVBus646885_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646727_consumption`  
  Load '52_LVBus646727_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646801_consumption`  
  Load '52_LVBus646801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646620_consumption`  
  Load '52_LVBus646620_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646607_consumption`  
  Load '52_LVBus646607_consumption' has phase imbalance of 154.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646918_consumption`  
  Load '52_LVBus646918_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646870_consumption`  
  Load '52_LVBus646870_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646711_consumption`  
  Load '52_LVBus646711_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646822_consumption`  
  Load '52_LVBus646822_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646611_consumption`  
  Load '52_LVBus646611_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646721_consumption`  
  Load '52_LVBus646721_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646862_consumption`  
  Load '52_LVBus646862_consumption' has phase imbalance of 230.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646609_consumption`  
  Load '52_LVBus646609_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646604_consumption`  
  Load '52_LVBus646604_consumption' has phase imbalance of 279.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646890_consumption`  
  Load '52_LVBus646890_consumption' has phase imbalance of 294.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646888_consumption`  
  Load '52_LVBus646888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646819_consumption`  
  Load '52_LVBus646819_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646803_consumption`  
  Load '52_LVBus646803_consumption' has phase imbalance of 242.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646859_consumption`  
  Load '52_LVBus646859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646718_consumption`  
  Load '52_LVBus646718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646714_consumption`  
  Load '52_LVBus646714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646628_consumption`  
  Load '52_LVBus646628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646745_consumption`  
  Load '52_LVBus646745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646653_consumption`  
  Load '52_LVBus646653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646717_consumption`  
  Load '52_LVBus646717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646796_consumption`  
  Load '52_LVBus646796_consumption' has phase imbalance of 283.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646910_consumption`  
  Load '52_LVBus646910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646875_consumption`  
  Load '52_LVBus646875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646664_consumption`  
  Load '52_LVBus646664_consumption' has phase imbalance of 297.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646726_consumption`  
  Load '52_LVBus646726_consumption' has phase imbalance of 273.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1156778_consumption`  
  Load '52_LVBus1156778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646856_consumption`  
  Load '52_LVBus646856_consumption' has phase imbalance of 40.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646854_consumption`  
  Load '52_LVBus646854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646618_consumption`  
  Load '52_LVBus646618_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646944_consumption`  
  Load '52_LVBus646944_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646591_consumption`  
  Load '52_LVBus646591_consumption' has phase imbalance of 158.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646851_consumption`  
  Load '52_LVBus646851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646623_consumption`  
  Load '52_LVBus646623_consumption' has phase imbalance of 231.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646594_consumption`  
  Load '52_LVBus646594_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646742_consumption`  
  Load '52_LVBus646742_consumption' has phase imbalance of 107.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646670_consumption`  
  Load '52_LVBus646670_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646876_consumption`  
  Load '52_LVBus646876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646887_consumption`  
  Load '52_LVBus646887_consumption' has phase imbalance of 205.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646914_consumption`  
  Load '52_LVBus646914_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646596_consumption`  
  Load '52_LVBus646596_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646677_consumption`  
  Load '52_LVBus646677_consumption' has phase imbalance of 78.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646926_consumption`  
  Load '52_LVBus646926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus646880_consumption`  
  Load '52_LVBus646880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 614 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus1154433' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus646750' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus646701' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus646750' (LV, 0.24 kV) has an electrical reach of 16.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus646642' (LV, 0.24 kV) has an electrical reach of 21.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus646701' (LV, 0.24 kV) has an electrical reach of 18.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  412 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  136 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 52_LVBus1140758_consumption, 52_LVBus1140759_consumption, 52_LVBus1156778_consumption, 52_LVBus1156779_consumption, 52_LVBus1156781_consumption, 52_LVBus646592_consumption, 52_LVBus646593_consumption, 52_LVBus646594_consumption, 52_LVBus646601_consumption, 52_LVBus646602_consumption, 52_LVBus646604_consumption, 52_LVBus646605_consumption, 52_LVBus646608_consumption, 52_LVBus646611_consumption, 52_LVBus646612_consumption, 52_LVBus646613_consumption, 52_LVBus646614_consumption, 52_LVBus646615_consumption, 52_LVBus646616_consumption, 52_LVBus646617_consumption, 52_LVBus646618_consumption, 52_LVBus646620_consumption, 52_LVBus646622_consumption, 52_LVBus646623_consumption, 52_LVBus646624_consumption, 52_LVBus646625_consumption, 52_LVBus646628_consumption, 52_LVBus646647_consumption, 52_LVBus646649_consumption, 52_LVBus646653_consumption, 52_LVBus646657_consumption, 52_LVBus646658_consumption, 52_LVBus646660_consumption, 52_LVBus646665_consumption, 52_LVBus646666_consumption, 52_LVBus646668_consumption, 52_LVBus646670_consumption, 52_LVBus646672_consumption, 52_LVBus646673_consumption, 52_LVBus646678_consumption, 52_LVBus646680_consumption, 52_LVBus646689_consumption, 52_LVBus646695_consumption, 52_LVBus646713_consumption, 52_LVBus646714_consumption, 52_LVBus646717_consumption, 52_LVBus646718_consumption, 52_LVBus646719_consumption, 52_LVBus646722_consumption, 52_LVBus646723_consumption, 52_LVBus646726_consumption, 52_LVBus646727_consumption, 52_LVBus646729_consumption, 52_LVBus646732_consumption, 52_LVBus646735_consumption, 52_LVBus646739_consumption, 52_LVBus646741_consumption, 52_LVBus646745_consumption, 52_LVBus646746_consumption, 52_LVBus646754_consumption, 52_LVBus646755_consumption, 52_LVBus646756_consumption, 52_LVBus646757_consumption, 52_LVBus646758_consumption, 52_LVBus646759_consumption, 52_LVBus646760_consumption, 52_LVBus646763_consumption, 52_LVBus646775_consumption, 52_LVBus646776_consumption, 52_LVBus646784_consumption, 52_LVBus646790_consumption, 52_LVBus646797_consumption, 52_LVBus646798_consumption, 52_LVBus646801_consumption, 52_LVBus646803_consumption, 52_LVBus646804_consumption, 52_LVBus646815_consumption, 52_LVBus646821_consumption, 52_LVBus646824_consumption, 52_LVBus646826_consumption, 52_LVBus646828_consumption, 52_LVBus646831_consumption, 52_LVBus646832_consumption, 52_LVBus646833_consumption, 52_LVBus646834_consumption, 52_LVBus646835_consumption, 52_LVBus646840_consumption, 52_LVBus646842_consumption, 52_LVBus646845_consumption, 52_LVBus646846_consumption, 52_LVBus646849_consumption, 52_LVBus646850_consumption, 52_LVBus646851_consumption, 52_LVBus646854_consumption, 52_LVBus646859_consumption, 52_LVBus646865_consumption, 52_LVBus646867_consumption, 52_LVBus646869_consumption, 52_LVBus646872_consumption, 52_LVBus646873_consumption, 52_LVBus646874_consumption, 52_LVBus646875_consumption, 52_LVBus646876_consumption, 52_LVBus646879_consumption, 52_LVBus646880_consumption, 52_LVBus646881_consumption, 52_LVBus646883_consumption, 52_LVBus646884_consumption, 52_LVBus646885_consumption, 52_LVBus646887_consumption, 52_LVBus646888_consumption, 52_LVBus646890_consumption, 52_LVBus646891_consumption, 52_LVBus646892_consumption, 52_LVBus646895_consumption, 52_LVBus646896_consumption, 52_LVBus646897_consumption, 52_LVBus646899_consumption, 52_LVBus646907_consumption, 52_LVBus646908_consumption, 52_LVBus646909_consumption, 52_LVBus646910_consumption, 52_LVBus646914_consumption, 52_LVBus646916_consumption, 52_LVBus646917_consumption, 52_LVBus646918_consumption, 52_LVBus646921_consumption, 52_LVBus646926_consumption, 52_LVBus646927_consumption, 52_LVBus646928_consumption, 52_LVBus646932_consumption, 52_LVBus646942_consumption, 52_LVBus646943_consumption, 52_LVBus646944_consumption, 52_LVBus646945_consumption, 52_LVBus646949_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  307 group(s) of loads (614 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  5 group(s) of series lines (10 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  370 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1140758_production, 52_LVBus1140759_production, 52_LVBus1149113_consumption, 52_LVBus1149113_production, 52_LVBus1149132_consumption, 52_LVBus1149132_production, 52_LVBus1149137_consumption, 52_LVBus1149137_production, 52_LVBus1149158_consumption, 52_LVBus1149158_production, 52_LVBus1149178_consumption, 52_LVBus1149178_production, 52_LVBus1149196_consumption, 52_LVBus1149196_production, 52_LVBus1154433_consumption, 52_LVBus1154433_production, 52_LVBus1156537_consumption, 52_LVBus1156537_production, 52_LVBus1156778_production, 52_LVBus1156779_production, 52_LVBus1156780_consumption, 52_LVBus1156780_production, 52_LVBus1156781_production, 52_LVBus1156782_production, 52_LVBus1162272_consumption, 52_LVBus1162272_production, 52_LVBus646591_production, 52_LVBus646592_production, 52_LVBus646593_production, 52_LVBus646594_production, 52_LVBus646595_production, 52_LVBus646596_production, 52_LVBus646597_production, 52_LVBus646598_production, 52_LVBus646600_production, 52_LVBus646601_production, 52_LVBus646602_production, 52_LVBus646604_production, 52_LVBus646605_production, 52_LVBus646607_production, 52_LVBus646608_production, 52_LVBus646609_production, 52_LVBus646611_production, 52_LVBus646612_production, 52_LVBus646613_production, 52_LVBus646614_production, 52_LVBus646615_production, 52_LVBus646616_production, 52_LVBus646617_production, 52_LVBus646618_production, 52_LVBus646619_consumption, 52_LVBus646619_production, 52_LVBus646620_production, 52_LVBus646621_production, 52_LVBus646622_production, 52_LVBus646623_production, 52_LVBus646624_production, 52_LVBus646625_production, 52_LVBus646626_production, 52_LVBus646628_production, 52_LVBus646629_production, 52_LVBus646630_production, 52_LVBus646632_consumption, 52_LVBus646632_production, 52_LVBus646634_production, 52_LVBus646636_consumption, 52_LVBus646636_production, 52_LVBus646638_consumption, 52_LVBus646638_production, 52_LVBus646640_consumption, 52_LVBus646640_production, 52_LVBus646642_consumption, 52_LVBus646642_production, 52_LVBus646643_production, 52_LVBus646646_production, 52_LVBus646647_production, 52_LVBus646648_consumption, 52_LVBus646648_production, 52_LVBus646649_production, 52_LVBus646650_production, 52_LVBus646651_consumption, 52_LVBus646651_production, 52_LVBus646653_production, 52_LVBus646654_production, 52_LVBus646655_production, 52_LVBus646656_production, 52_LVBus646657_production, 52_LVBus646658_production, 52_LVBus646660_production, 52_LVBus646661_production, 52_LVBus646662_consumption, 52_LVBus646662_production, 52_LVBus646663_consumption, 52_LVBus646663_production, 52_LVBus646664_production, 52_LVBus646665_production, 52_LVBus646666_production, 52_LVBus646668_production, 52_LVBus646670_production, 52_LVBus646671_production, 52_LVBus646672_production, 52_LVBus646673_production, 52_LVBus646674_production, 52_LVBus646675_production, 52_LVBus646676_production, 52_LVBus646677_production, 52_LVBus646678_production, 52_LVBus646680_production, 52_LVBus646681_production, 52_LVBus646683_consumption, 52_LVBus646683_production, 52_LVBus646685_consumption, 52_LVBus646685_production, 52_LVBus646687_consumption, 52_LVBus646687_production, 52_LVBus646689_production, 52_LVBus646690_production, 52_LVBus646691_production, 52_LVBus646692_production, 52_LVBus646693_production, 52_LVBus646695_production, 52_LVBus646697_production, 52_LVBus646698_production, 52_LVBus646699_production, 52_LVBus646701_production, 52_LVBus646703_production, 52_LVBus646704_production, 52_LVBus646705_production, 52_LVBus646707_consumption, 52_LVBus646707_production, 52_LVBus646708_consumption, 52_LVBus646708_production, 52_LVBus646709_consumption, 52_LVBus646709_production, 52_LVBus646711_production, 52_LVBus646712_production, 52_LVBus646713_production, 52_LVBus646714_production, 52_LVBus646715_production, 52_LVBus646717_production, 52_LVBus646718_production, 52_LVBus646719_production, 52_LVBus646721_production, 52_LVBus646722_production, 52_LVBus646723_production, 52_LVBus646724_production, 52_LVBus646725_production, 52_LVBus646726_production, 52_LVBus646727_production, 52_LVBus646728_production, 52_LVBus646729_production, 52_LVBus646730_consumption, 52_LVBus646730_production, 52_LVBus646732_production, 52_LVBus646733_consumption, 52_LVBus646733_production, 52_LVBus646734_production, 52_LVBus646735_production, 52_LVBus646736_production, 52_LVBus646737_production, 52_LVBus646739_production, 52_LVBus646740_production, 52_LVBus646741_production, 52_LVBus646742_production, 52_LVBus646743_production, 52_LVBus646744_production, 52_LVBus646745_production, 52_LVBus646746_production, 52_LVBus646747_production, 52_LVBus646750_production, 52_LVBus646752_consumption, 52_LVBus646752_production, 52_LVBus646754_production, 52_LVBus646755_production, 52_LVBus646756_production, 52_LVBus646757_production, 52_LVBus646758_production, 52_LVBus646759_production, 52_LVBus646760_production, 52_LVBus646761_production, 52_LVBus646762_consumption, 52_LVBus646762_production, 52_LVBus646763_production, 52_LVBus646765_production, 52_LVBus646767_consumption, 52_LVBus646767_production, 52_LVBus646769_consumption, 52_LVBus646769_production, 52_LVBus646771_consumption, 52_LVBus646771_production, 52_LVBus646773_consumption, 52_LVBus646773_production, 52_LVBus646775_production, 52_LVBus646776_production, 52_LVBus646777_production, 52_LVBus646780_production, 52_LVBus646781_production, 52_LVBus646782_production, 52_LVBus646783_production, 52_LVBus646784_production, 52_LVBus646785_production, 52_LVBus646786_consumption, 52_LVBus646786_production, 52_LVBus646787_production, 52_LVBus646788_production, 52_LVBus646790_production, 52_LVBus646791_production, 52_LVBus646792_production, 52_LVBus646794_production, 52_LVBus646795_production, 52_LVBus646796_production, 52_LVBus646797_production, 52_LVBus646798_production, 52_LVBus646799_consumption, 52_LVBus646799_production, 52_LVBus646801_production, 52_LVBus646802_production, 52_LVBus646803_production, 52_LVBus646804_production, 52_LVBus646805_consumption, 52_LVBus646805_production, 52_LVBus646806_production, 52_LVBus646808_consumption, 52_LVBus646808_production, 52_LVBus646809_production, 52_LVBus646810_production, 52_LVBus646812_production, 52_LVBus646813_production, 52_LVBus646814_consumption, 52_LVBus646814_production, 52_LVBus646815_production, 52_LVBus646817_consumption, 52_LVBus646817_production, 52_LVBus646818_production, 52_LVBus646819_production, 52_LVBus646820_production, 52_LVBus646821_production, 52_LVBus646822_production, 52_LVBus646823_production, 52_LVBus646824_production, 52_LVBus646825_consumption, 52_LVBus646825_production, 52_LVBus646826_production, 52_LVBus646828_production, 52_LVBus646829_production, 52_LVBus646831_production, 52_LVBus646832_production, 52_LVBus646833_production, 52_LVBus646834_production, 52_LVBus646835_production, 52_LVBus646837_consumption, 52_LVBus646837_production, 52_LVBus646838_consumption, 52_LVBus646838_production, 52_LVBus646839_consumption, 52_LVBus646839_production, 52_LVBus646840_production, 52_LVBus646841_production, 52_LVBus646842_production, 52_LVBus646844_consumption, 52_LVBus646844_production, 52_LVBus646845_production, 52_LVBus646846_production, 52_LVBus646847_production, 52_LVBus646848_production, 52_LVBus646849_production, 52_LVBus646850_production, 52_LVBus646851_production, 52_LVBus646853_consumption, 52_LVBus646853_production, 52_LVBus646854_production, 52_LVBus646855_production, 52_LVBus646856_production, 52_LVBus646858_production, 52_LVBus646859_production, 52_LVBus646861_production, 52_LVBus646862_production, 52_LVBus646863_production, 52_LVBus646864_production, 52_LVBus646865_production, 52_LVBus646866_consumption, 52_LVBus646866_production, 52_LVBus646867_production, 52_LVBus646868_production, 52_LVBus646869_production, 52_LVBus646870_production, 52_LVBus646872_production, 52_LVBus646873_production, 52_LVBus646874_production, 52_LVBus646875_production, 52_LVBus646876_production, 52_LVBus646877_production, 52_LVBus646878_production, 52_LVBus646879_production, 52_LVBus646880_production, 52_LVBus646881_production, 52_LVBus646883_production, 52_LVBus646884_production, 52_LVBus646885_production, 52_LVBus646886_consumption, 52_LVBus646886_production, 52_LVBus646887_production, 52_LVBus646888_production, 52_LVBus646890_production, 52_LVBus646891_production, 52_LVBus646892_production, 52_LVBus646893_production, 52_LVBus646895_production, 52_LVBus646896_production, 52_LVBus646897_production, 52_LVBus646898_production, 52_LVBus646899_production, 52_LVBus646900_production, 52_LVBus646901_production, 52_LVBus646904_consumption, 52_LVBus646904_production, 52_LVBus646905_consumption, 52_LVBus646905_production, 52_LVBus646906_consumption, 52_LVBus646906_production, 52_LVBus646907_production, 52_LVBus646908_production, 52_LVBus646909_production, 52_LVBus646910_production, 52_LVBus646911_production, 52_LVBus646912_production, 52_LVBus646913_production, 52_LVBus646914_production, 52_LVBus646915_consumption, 52_LVBus646915_production, 52_LVBus646916_production, 52_LVBus646917_production, 52_LVBus646918_production, 52_LVBus646920_consumption, 52_LVBus646920_production, 52_LVBus646921_production, 52_LVBus646922_production, 52_LVBus646923_consumption, 52_LVBus646923_production, 52_LVBus646924_consumption, 52_LVBus646924_production, 52_LVBus646925_consumption, 52_LVBus646925_production, 52_LVBus646926_production, 52_LVBus646927_production, 52_LVBus646928_production, 52_LVBus646930_production, 52_LVBus646931_production, 52_LVBus646932_production, 52_LVBus646934_production, 52_LVBus646936_consumption, 52_LVBus646936_production, 52_LVBus646938_consumption, 52_LVBus646938_production, 52_LVBus646940_consumption, 52_LVBus646940_production, 52_LVBus646942_production, 52_LVBus646943_production, 52_LVBus646944_production, 52_LVBus646945_production, 52_LVBus646946_production, 52_LVBus646948_consumption, 52_LVBus646948_production, 52_LVBus646949_production, 52_MVLV040415_consumption, 52_MVLV040415_production, 52_MVLV092789_consumption, 52_MVLV092789_production, 52_MVLV105904_consumption, 52_MVLV105904_production.

