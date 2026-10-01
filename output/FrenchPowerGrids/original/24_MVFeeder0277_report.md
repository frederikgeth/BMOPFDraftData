# BMOPF Network Summary: 24_MVFeeder0277

**Generated:** 2026-10-01 23:33:57  
**Findings:** 0 errors · 5 warnings · 186 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 31 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 350 |  |
| line | 318 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 498 | 1.376 MW, 412.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 31 |  |
| switch | 0 |  |
| transformer | 31 | Dyn11×31 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 72 | 71 | 4 | 0 |
| LV_236V | 236.0 V | 278 | 247 | 494 | 0 |

**Transformer transitions:**

- `24_MVLV09013_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV52386_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV46696_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV19241_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV33375_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV09005_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV84105_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69552_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV83399_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV71746_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV38944_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV02790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV30368_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV24497_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV78897_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV33371_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV19693_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV46702_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV63972_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV59971_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV31438_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV33372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV05393_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV24496_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV06681_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV19240_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV19692_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV73148_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV52158_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV13806_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV13808_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 7 |
| Degree-1 buses | 108 |
| Tree depth (max hops) | 32 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 350 | 1 | 349 | 0 | 0 | 0 |
| Tier LV_236V | 278 | 31 | 247 | 0 | 0 | 0 |
| Tier MV_11.8kV | 72 | 1 | 71 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 31; skipped invalid branches: 0.

Galvanic zones: 32; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 24_BUIS | MV_11.8kV | 72 | 0 | 0 | 31 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1328 declared bus terminals; 1201 mapped line/closed-switch conductor edges; 127 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 27800.0 | 2.955 | 1494 |
| q_nom | 0.0 | 8350.0 | 2.955 | 1494 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.898 | 2410.0 | 1.787 | 318 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.757 | 31 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 321 of 498 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216858_consumption' has phase imbalance of 145.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216942_consumption' has phase imbalance of 249.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216792_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216984_consumption' has phase imbalance of 109.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216846_consumption' has phase imbalance of 240.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216813_consumption' has phase imbalance of 246.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217015_consumption' has phase imbalance of 212.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216905_consumption' has phase imbalance of 243.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216974_consumption' has phase imbalance of 119.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216995_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216894_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216747_consumption' has phase imbalance of 124.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217002_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216797_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216843_consumption' has phase imbalance of 127.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216837_consumption' has phase imbalance of 116.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216938_consumption' has phase imbalance of 97.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216904_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216783_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216932_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216929_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216849_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216931_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216996_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216760_consumption' has phase imbalance of 237.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216922_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216917_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216903_consumption' has phase imbalance of 142.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216948_consumption' has phase imbalance of 221.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216944_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216924_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216777_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216822_consumption' has phase imbalance of 287.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216993_consumption' has phase imbalance of 277.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216855_consumption' has phase imbalance of 234.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216821_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216771_consumption' has phase imbalance of 258.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216928_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216951_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216940_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216724_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216873_consumption' has phase imbalance of 36.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216871_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216836_consumption' has phase imbalance of 115.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216923_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216749_consumption' has phase imbalance of 216.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216842_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216916_consumption' has phase imbalance of 175.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216850_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216781_consumption' has phase imbalance of 255.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216764_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216838_consumption' has phase imbalance of 143.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216973_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216800_consumption' has phase imbalance of 283.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216812_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217001_consumption' has phase imbalance of 209.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216901_consumption' has phase imbalance of 140.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216835_consumption' has phase imbalance of 113.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216895_consumption' has phase imbalance of 286.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216740_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216972_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216753_consumption' has phase imbalance of 228.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216927_consumption' has phase imbalance of 284.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216761_consumption' has phase imbalance of 208.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216950_consumption' has phase imbalance of 97.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216782_consumption' has phase imbalance of 230.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216815_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216912_consumption' has phase imbalance of 122.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216906_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216994_consumption' has phase imbalance of 36.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216976_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216921_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216857_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216860_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216856_consumption' has phase imbalance of 158.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216819_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216791_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216907_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216739_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216852_consumption' has phase imbalance of 201.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216867_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216758_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216780_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216874_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216816_consumption' has phase imbalance of 35.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216785_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216746_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216841_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216880_consumption' has phase imbalance of 147.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216769_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216933_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216925_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus217014_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216911_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216914_consumption' has phase imbalance of 224.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216975_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216902_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216941_consumption' has phase imbalance of 247.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216745_consumption' has phase imbalance of 136.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216802_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216834_consumption' has phase imbalance of 112.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216762_consumption' has phase imbalance of 229.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216808_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216789_consumption' has phase imbalance of 241.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216887_consumption' has phase imbalance of 36.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216949_consumption' has phase imbalance of 167.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216810_consumption' has phase imbalance of 231.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216839_consumption' has phase imbalance of 193.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216864_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216939_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus216755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 498 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus216829' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.376 MW |
| Total load Q | 412.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 24_MVLV09013_Transformer | 693.0 kVA | 43.6% |
| 24_MVLV52386_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV46696_Transformer | 110.0 kVA | 5.2% |
| 24_MVLV19241_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV33375_Transformer | 176.0 kVA | 4.9% |
| 24_MVLV09005_Transformer | 176.0 kVA | 5.8% |
| 24_MVLV84105_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV69552_Transformer | 440.0 kVA | 35.2% |
| 24_MVLV83399_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV71746_Transformer | 110.0 kVA | 9.6% |
| 24_MVLV38944_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV02790_Transformer | 275.0 kVA | 9.4% |
| 24_MVLV30368_Transformer | 176.0 kVA | 17.2% |
| 24_MVLV24497_Transformer | 110.0 kVA | 13.6% |
| 24_MVLV78897_Transformer | 110.0 kVA | 3.4% |
| 24_MVLV33371_Transformer | 110.0 kVA | 0.7% |
| 24_MVLV19693_Transformer | 110.0 kVA | 0.6% |
| 24_MVLV46702_Transformer | 176.0 kVA | 11.6% |
| 24_MVLV63972_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV59971_Transformer | 693.0 kVA | 33.3% |
| 24_MVLV31438_Transformer | 176.0 kVA | 7.4% |
| 24_MVLV33372_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV05393_Transformer | 110.0 kVA | 2.4% |
| 24_MVLV24496_Transformer | 440.0 kVA | 43.2% |
| 24_MVLV06681_Transformer | 110.0 kVA | 4.4% |
| 24_MVLV19240_Transformer | 275.0 kVA | 24.7% |
| 24_MVLV19692_Transformer | 110.0 kVA | 6.6% |
| 24_MVLV73148_Transformer | 110.0 kVA | 0.6% |
| 24_MVLV52158_Transformer | 693.0 kVA | 36.1% |
| 24_MVLV13806_Transformer | 176.0 kVA | 13.0% |
| 24_MVLV13808_Transformer | 275.0 kVA | 21.1% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.38 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus216724' (LV, 0.24 kV) has an electrical reach of 13.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus216935' (LV, 0.24 kV) has an electrical reach of 9.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus217035' (LV, 0.24 kV) has an electrical reach of 10.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus216824' (LV, 0.24 kV) has an electrical reach of 28.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus216889' (LV, 0.24 kV) has an electrical reach of 20.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 350 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 350 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 31 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 72 |
| LV_236V | 4-wire | 278 / 278 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 278 |
| Neutral branches | 247 |
| Grounding points | 31 |
| Neutral sections | 31 |
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
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 53 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 32 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1710.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 278 / 72 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 322 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 322 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus216724_production, 24_LVBus216726_production, 24_LVBus216728_production, 24_LVBus216729_consumption, 24_LVBus216729_production, 24_LVBus216732_production, 24_LVBus216733_consumption, 24_LVBus216733_production, 24_LVBus216735_consumption, 24_LVBus216735_production, 24_LVBus216736_consumption, 24_LVBus216736_production, 24_LVBus216737_production, 24_LVBus216738_consumption, 24_LVBus216738_production, 24_LVBus216739_production, 24_LVBus216740_production, 24_LVBus216744_production, 24_LVBus216745_production, 24_LVBus216746_production, 24_LVBus216747_production, 24_LVBus216748_production, 24_LVBus216749_production, 24_LVBus216750_consumption, 24_LVBus216750_production, 24_LVBus216751_production, 24_LVBus216752_production, 24_LVBus216753_production, 24_LVBus216754_production, 24_LVBus216755_production, 24_LVBus216756_consumption, 24_LVBus216756_production, 24_LVBus216757_consumption, 24_LVBus216757_production, 24_LVBus216758_production, 24_LVBus216760_production, 24_LVBus216761_production, 24_LVBus216762_production, 24_LVBus216763_production, 24_LVBus216764_production, 24_LVBus216765_production, 24_LVBus216766_consumption, 24_LVBus216766_production, 24_LVBus216767_production, 24_LVBus216768_production, 24_LVBus216769_production, 24_LVBus216770_production, 24_LVBus216771_production, 24_LVBus216772_production, 24_LVBus216773_production, 24_LVBus216774_production, 24_LVBus216775_consumption, 24_LVBus216775_production, 24_LVBus216777_production, 24_LVBus216778_production, 24_LVBus216779_production, 24_LVBus216780_production, 24_LVBus216781_production, 24_LVBus216782_production, 24_LVBus216783_production, 24_LVBus216784_production, 24_LVBus216785_production, 24_LVBus216786_production, 24_LVBus216788_production, 24_LVBus216789_production, 24_LVBus216790_consumption, 24_LVBus216790_production, 24_LVBus216791_production, 24_LVBus216792_production, 24_LVBus216793_production, 24_LVBus216794_consumption, 24_LVBus216794_production, 24_LVBus216795_production, 24_LVBus216796_consumption, 24_LVBus216796_production, 24_LVBus216797_production, 24_LVBus216799_consumption, 24_LVBus216799_production, 24_LVBus216800_production, 24_LVBus216801_consumption, 24_LVBus216801_production, 24_LVBus216802_production, 24_LVBus216803_production, 24_LVBus216804_production, 24_LVBus216805_production, 24_LVBus216806_production, 24_LVBus216808_production, 24_LVBus216809_production, 24_LVBus216810_production, 24_LVBus216811_production, 24_LVBus216812_production, 24_LVBus216813_production, 24_LVBus216815_production, 24_LVBus216816_production, 24_LVBus216817_production, 24_LVBus216818_consumption, 24_LVBus216818_production, 24_LVBus216819_production, 24_LVBus216820_production, 24_LVBus216821_production, 24_LVBus216822_production, 24_LVBus216824_consumption, 24_LVBus216824_production, 24_LVBus216826_consumption, 24_LVBus216826_production, 24_LVBus216827_production, 24_LVBus216829_production, 24_LVBus216830_consumption, 24_LVBus216830_production, 24_LVBus216831_production, 24_LVBus216832_consumption, 24_LVBus216832_production, 24_LVBus216834_production, 24_LVBus216835_production, 24_LVBus216836_production, 24_LVBus216837_production, 24_LVBus216838_production, 24_LVBus216839_production, 24_LVBus216840_consumption, 24_LVBus216840_production, 24_LVBus216841_production, 24_LVBus216842_production, 24_LVBus216843_production, 24_LVBus216844_consumption, 24_LVBus216844_production, 24_LVBus216845_consumption, 24_LVBus216845_production, 24_LVBus216846_production, 24_LVBus216848_consumption, 24_LVBus216848_production, 24_LVBus216849_production, 24_LVBus216850_production, 24_LVBus216851_production, 24_LVBus216852_production, 24_LVBus216853_production, 24_LVBus216854_production, 24_LVBus216855_production, 24_LVBus216856_production, 24_LVBus216857_production, 24_LVBus216858_production, 24_LVBus216859_production, 24_LVBus216860_production, 24_LVBus216862_production, 24_LVBus216864_production, 24_LVBus216865_consumption, 24_LVBus216865_production, 24_LVBus216866_consumption, 24_LVBus216866_production, 24_LVBus216867_production, 24_LVBus216868_production, 24_LVBus216869_production, 24_LVBus216871_production, 24_LVBus216872_consumption, 24_LVBus216872_production, 24_LVBus216873_production, 24_LVBus216874_production, 24_LVBus216875_consumption, 24_LVBus216875_production, 24_LVBus216877_consumption, 24_LVBus216877_production, 24_LVBus216879_production, 24_LVBus216880_production, 24_LVBus216882_consumption, 24_LVBus216882_production, 24_LVBus216883_consumption, 24_LVBus216883_production, 24_LVBus216885_consumption, 24_LVBus216885_production, 24_LVBus216886_consumption, 24_LVBus216886_production, 24_LVBus216887_production, 24_LVBus216889_consumption, 24_LVBus216889_production, 24_LVBus216891_production, 24_LVBus216892_production, 24_LVBus216894_production, 24_LVBus216895_production, 24_LVBus216896_production, 24_LVBus216897_consumption, 24_LVBus216897_production, 24_LVBus216898_production, 24_LVBus216900_consumption, 24_LVBus216900_production, 24_LVBus216901_production, 24_LVBus216902_production, 24_LVBus216903_production, 24_LVBus216904_production, 24_LVBus216905_production, 24_LVBus216906_production, 24_LVBus216907_production, 24_LVBus216909_consumption, 24_LVBus216909_production, 24_LVBus216910_consumption, 24_LVBus216910_production, 24_LVBus216911_production, 24_LVBus216912_production, 24_LVBus216913_production, 24_LVBus216914_production, 24_LVBus216915_production, 24_LVBus216916_production, 24_LVBus216917_production, 24_LVBus216918_production, 24_LVBus216920_production, 24_LVBus216921_production, 24_LVBus216922_production, 24_LVBus216923_production, 24_LVBus216924_production, 24_LVBus216925_production, 24_LVBus216927_production, 24_LVBus216928_production, 24_LVBus216929_production, 24_LVBus216930_production, 24_LVBus216931_production, 24_LVBus216932_production, 24_LVBus216933_production, 24_LVBus216935_consumption, 24_LVBus216935_production, 24_LVBus216937_consumption, 24_LVBus216937_production, 24_LVBus216938_production, 24_LVBus216939_production, 24_LVBus216940_production, 24_LVBus216941_production, 24_LVBus216942_production, 24_LVBus216943_production, 24_LVBus216944_production, 24_LVBus216945_production, 24_LVBus216947_consumption, 24_LVBus216947_production, 24_LVBus216948_production, 24_LVBus216949_production, 24_LVBus216950_production, 24_LVBus216951_production, 24_LVBus216953_consumption, 24_LVBus216953_production, 24_LVBus216954_production, 24_LVBus216956_consumption, 24_LVBus216956_production, 24_LVBus216957_consumption, 24_LVBus216957_production, 24_LVBus216959_consumption, 24_LVBus216959_production, 24_LVBus216960_production, 24_LVBus216962_consumption, 24_LVBus216962_production, 24_LVBus216963_consumption, 24_LVBus216963_production, 24_LVBus216968_consumption, 24_LVBus216968_production, 24_LVBus216969_consumption, 24_LVBus216969_production, 24_LVBus216970_consumption, 24_LVBus216970_production, 24_LVBus216972_production, 24_LVBus216973_production, 24_LVBus216974_production, 24_LVBus216975_production, 24_LVBus216976_production, 24_LVBus216978_consumption, 24_LVBus216978_production, 24_LVBus216979_consumption, 24_LVBus216979_production, 24_LVBus216980_consumption, 24_LVBus216980_production, 24_LVBus216982_consumption, 24_LVBus216982_production, 24_LVBus216983_production, 24_LVBus216984_production, 24_LVBus216985_production, 24_LVBus216987_consumption, 24_LVBus216987_production, 24_LVBus216988_production, 24_LVBus216990_consumption, 24_LVBus216990_production, 24_LVBus216991_consumption, 24_LVBus216991_production, 24_LVBus216992_consumption, 24_LVBus216992_production, 24_LVBus216993_production, 24_LVBus216994_production, 24_LVBus216995_production, 24_LVBus216996_production, 24_LVBus216998_production, 24_LVBus216999_production, 24_LVBus217000_consumption, 24_LVBus217000_production, 24_LVBus217001_production, 24_LVBus217002_production, 24_LVBus217003_production, 24_LVBus217004_production, 24_LVBus217014_production, 24_LVBus217015_production, 24_LVBus217016_consumption, 24_LVBus217016_production, 24_LVBus217020_consumption, 24_LVBus217020_production, 24_LVBus217021_consumption, 24_LVBus217021_production, 24_LVBus217022_production, 24_LVBus217025_consumption, 24_LVBus217025_production, 24_LVBus217026_consumption, 24_LVBus217026_production, 24_LVBus217027_consumption, 24_LVBus217027_production, 24_LVBus217028_production, 24_LVBus217029_consumption, 24_LVBus217029_production, 24_LVBus217030_consumption, 24_LVBus217030_production, 24_LVBus217032_consumption, 24_LVBus217032_production, 24_LVBus217033_consumption, 24_LVBus217033_production, 24_LVBus217035_consumption, 24_LVBus217035_production, 24_LVBus835069_consumption, 24_LVBus835069_production, 24_MVLV78990_consumption, 24_MVLV78990_production, 24_MVLV82213_consumption, 24_MVLV82213_production.

## 9. Data Quality Summary

**Total findings:** 191 (0 errors, 5 warnings, 186 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  321 of 498 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.38 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  322 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216858_consumption`  
  Load '24_LVBus216858_consumption' has phase imbalance of 145.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216942_consumption`  
  Load '24_LVBus216942_consumption' has phase imbalance of 249.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216792_consumption`  
  Load '24_LVBus216792_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216984_consumption`  
  Load '24_LVBus216984_consumption' has phase imbalance of 109.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216752_consumption`  
  Load '24_LVBus216752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216846_consumption`  
  Load '24_LVBus216846_consumption' has phase imbalance of 240.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216813_consumption`  
  Load '24_LVBus216813_consumption' has phase imbalance of 246.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217015_consumption`  
  Load '24_LVBus217015_consumption' has phase imbalance of 212.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216795_consumption`  
  Load '24_LVBus216795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216905_consumption`  
  Load '24_LVBus216905_consumption' has phase imbalance of 243.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216974_consumption`  
  Load '24_LVBus216974_consumption' has phase imbalance of 119.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216748_consumption`  
  Load '24_LVBus216748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216995_consumption`  
  Load '24_LVBus216995_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216894_consumption`  
  Load '24_LVBus216894_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216773_consumption`  
  Load '24_LVBus216773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216747_consumption`  
  Load '24_LVBus216747_consumption' has phase imbalance of 124.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217002_consumption`  
  Load '24_LVBus217002_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217003_consumption`  
  Load '24_LVBus217003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216797_consumption`  
  Load '24_LVBus216797_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216843_consumption`  
  Load '24_LVBus216843_consumption' has phase imbalance of 127.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216837_consumption`  
  Load '24_LVBus216837_consumption' has phase imbalance of 116.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216938_consumption`  
  Load '24_LVBus216938_consumption' has phase imbalance of 97.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216904_consumption`  
  Load '24_LVBus216904_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216811_consumption`  
  Load '24_LVBus216811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216783_consumption`  
  Load '24_LVBus216783_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216932_consumption`  
  Load '24_LVBus216932_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216929_consumption`  
  Load '24_LVBus216929_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216754_consumption`  
  Load '24_LVBus216754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216767_consumption`  
  Load '24_LVBus216767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216849_consumption`  
  Load '24_LVBus216849_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216931_consumption`  
  Load '24_LVBus216931_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216751_consumption`  
  Load '24_LVBus216751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216817_consumption`  
  Load '24_LVBus216817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216996_consumption`  
  Load '24_LVBus216996_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216806_consumption`  
  Load '24_LVBus216806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216809_consumption`  
  Load '24_LVBus216809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216892_consumption`  
  Load '24_LVBus216892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216760_consumption`  
  Load '24_LVBus216760_consumption' has phase imbalance of 237.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216772_consumption`  
  Load '24_LVBus216772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216922_consumption`  
  Load '24_LVBus216922_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216917_consumption`  
  Load '24_LVBus216917_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217004_consumption`  
  Load '24_LVBus217004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216903_consumption`  
  Load '24_LVBus216903_consumption' has phase imbalance of 142.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216948_consumption`  
  Load '24_LVBus216948_consumption' has phase imbalance of 221.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216944_consumption`  
  Load '24_LVBus216944_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216924_consumption`  
  Load '24_LVBus216924_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216777_consumption`  
  Load '24_LVBus216777_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217022_consumption`  
  Load '24_LVBus217022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216999_consumption`  
  Load '24_LVBus216999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216822_consumption`  
  Load '24_LVBus216822_consumption' has phase imbalance of 287.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216993_consumption`  
  Load '24_LVBus216993_consumption' has phase imbalance of 277.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216855_consumption`  
  Load '24_LVBus216855_consumption' has phase imbalance of 234.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216821_consumption`  
  Load '24_LVBus216821_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216771_consumption`  
  Load '24_LVBus216771_consumption' has phase imbalance of 258.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216928_consumption`  
  Load '24_LVBus216928_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216788_consumption`  
  Load '24_LVBus216788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216951_consumption`  
  Load '24_LVBus216951_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216940_consumption`  
  Load '24_LVBus216940_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216920_consumption`  
  Load '24_LVBus216920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216851_consumption`  
  Load '24_LVBus216851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217028_consumption`  
  Load '24_LVBus217028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216724_consumption`  
  Load '24_LVBus216724_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216918_consumption`  
  Load '24_LVBus216918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216873_consumption`  
  Load '24_LVBus216873_consumption' has phase imbalance of 36.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216871_consumption`  
  Load '24_LVBus216871_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216803_consumption`  
  Load '24_LVBus216803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216859_consumption`  
  Load '24_LVBus216859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216836_consumption`  
  Load '24_LVBus216836_consumption' has phase imbalance of 115.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216923_consumption`  
  Load '24_LVBus216923_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216770_consumption`  
  Load '24_LVBus216770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216749_consumption`  
  Load '24_LVBus216749_consumption' has phase imbalance of 216.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216774_consumption`  
  Load '24_LVBus216774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216842_consumption`  
  Load '24_LVBus216842_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216916_consumption`  
  Load '24_LVBus216916_consumption' has phase imbalance of 175.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216784_consumption`  
  Load '24_LVBus216784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216943_consumption`  
  Load '24_LVBus216943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216850_consumption`  
  Load '24_LVBus216850_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216781_consumption`  
  Load '24_LVBus216781_consumption' has phase imbalance of 255.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216764_consumption`  
  Load '24_LVBus216764_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216786_consumption`  
  Load '24_LVBus216786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216838_consumption`  
  Load '24_LVBus216838_consumption' has phase imbalance of 143.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216973_consumption`  
  Load '24_LVBus216973_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216800_consumption`  
  Load '24_LVBus216800_consumption' has phase imbalance of 283.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216868_consumption`  
  Load '24_LVBus216868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216812_consumption`  
  Load '24_LVBus216812_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216854_consumption`  
  Load '24_LVBus216854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217001_consumption`  
  Load '24_LVBus217001_consumption' has phase imbalance of 209.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216901_consumption`  
  Load '24_LVBus216901_consumption' has phase imbalance of 140.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216835_consumption`  
  Load '24_LVBus216835_consumption' has phase imbalance of 113.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216895_consumption`  
  Load '24_LVBus216895_consumption' has phase imbalance of 286.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216740_consumption`  
  Load '24_LVBus216740_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216972_consumption`  
  Load '24_LVBus216972_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216983_consumption`  
  Load '24_LVBus216983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216753_consumption`  
  Load '24_LVBus216753_consumption' has phase imbalance of 228.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216927_consumption`  
  Load '24_LVBus216927_consumption' has phase imbalance of 284.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216761_consumption`  
  Load '24_LVBus216761_consumption' has phase imbalance of 208.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216950_consumption`  
  Load '24_LVBus216950_consumption' has phase imbalance of 97.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216782_consumption`  
  Load '24_LVBus216782_consumption' has phase imbalance of 230.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216930_consumption`  
  Load '24_LVBus216930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216815_consumption`  
  Load '24_LVBus216815_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216912_consumption`  
  Load '24_LVBus216912_consumption' has phase imbalance of 122.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216985_consumption`  
  Load '24_LVBus216985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216906_consumption`  
  Load '24_LVBus216906_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216994_consumption`  
  Load '24_LVBus216994_consumption' has phase imbalance of 36.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216976_consumption`  
  Load '24_LVBus216976_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216778_consumption`  
  Load '24_LVBus216778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216805_consumption`  
  Load '24_LVBus216805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216921_consumption`  
  Load '24_LVBus216921_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216857_consumption`  
  Load '24_LVBus216857_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216860_consumption`  
  Load '24_LVBus216860_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216856_consumption`  
  Load '24_LVBus216856_consumption' has phase imbalance of 158.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216819_consumption`  
  Load '24_LVBus216819_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216791_consumption`  
  Load '24_LVBus216791_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216896_consumption`  
  Load '24_LVBus216896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216907_consumption`  
  Load '24_LVBus216907_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216945_consumption`  
  Load '24_LVBus216945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216739_consumption`  
  Load '24_LVBus216739_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216852_consumption`  
  Load '24_LVBus216852_consumption' has phase imbalance of 201.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216768_consumption`  
  Load '24_LVBus216768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216867_consumption`  
  Load '24_LVBus216867_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216758_consumption`  
  Load '24_LVBus216758_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216780_consumption`  
  Load '24_LVBus216780_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216874_consumption`  
  Load '24_LVBus216874_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216816_consumption`  
  Load '24_LVBus216816_consumption' has phase imbalance of 35.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216820_consumption`  
  Load '24_LVBus216820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216779_consumption`  
  Load '24_LVBus216779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216763_consumption`  
  Load '24_LVBus216763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216785_consumption`  
  Load '24_LVBus216785_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216746_consumption`  
  Load '24_LVBus216746_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216841_consumption`  
  Load '24_LVBus216841_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216880_consumption`  
  Load '24_LVBus216880_consumption' has phase imbalance of 147.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216891_consumption`  
  Load '24_LVBus216891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216732_consumption`  
  Load '24_LVBus216732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216913_consumption`  
  Load '24_LVBus216913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216804_consumption`  
  Load '24_LVBus216804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216769_consumption`  
  Load '24_LVBus216769_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216933_consumption`  
  Load '24_LVBus216933_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216925_consumption`  
  Load '24_LVBus216925_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus217014_consumption`  
  Load '24_LVBus217014_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216911_consumption`  
  Load '24_LVBus216911_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216914_consumption`  
  Load '24_LVBus216914_consumption' has phase imbalance of 224.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216975_consumption`  
  Load '24_LVBus216975_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216737_consumption`  
  Load '24_LVBus216737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216853_consumption`  
  Load '24_LVBus216853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216765_consumption`  
  Load '24_LVBus216765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216902_consumption`  
  Load '24_LVBus216902_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216941_consumption`  
  Load '24_LVBus216941_consumption' has phase imbalance of 247.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216745_consumption`  
  Load '24_LVBus216745_consumption' has phase imbalance of 136.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216728_consumption`  
  Load '24_LVBus216728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216802_consumption`  
  Load '24_LVBus216802_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216869_consumption`  
  Load '24_LVBus216869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216834_consumption`  
  Load '24_LVBus216834_consumption' has phase imbalance of 112.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216762_consumption`  
  Load '24_LVBus216762_consumption' has phase imbalance of 229.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216827_consumption`  
  Load '24_LVBus216827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216808_consumption`  
  Load '24_LVBus216808_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216793_consumption`  
  Load '24_LVBus216793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216789_consumption`  
  Load '24_LVBus216789_consumption' has phase imbalance of 241.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216887_consumption`  
  Load '24_LVBus216887_consumption' has phase imbalance of 36.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216949_consumption`  
  Load '24_LVBus216949_consumption' has phase imbalance of 167.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216810_consumption`  
  Load '24_LVBus216810_consumption' has phase imbalance of 231.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216839_consumption`  
  Load '24_LVBus216839_consumption' has phase imbalance of 193.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216864_consumption`  
  Load '24_LVBus216864_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216998_consumption`  
  Load '24_LVBus216998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216939_consumption`  
  Load '24_LVBus216939_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus216755_consumption`  
  Load '24_LVBus216755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 498 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus216829' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus216724' (LV, 0.24 kV) has an electrical reach of 13.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus216935' (LV, 0.24 kV) has an electrical reach of 9.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus217035' (LV, 0.24 kV) has an electrical reach of 10.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus216824' (LV, 0.24 kV) has an electrical reach of 28.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus216889' (LV, 0.24 kV) has an electrical reach of 20.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  350 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  120 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 24_LVBus216724_consumption, 24_LVBus216728_consumption, 24_LVBus216732_consumption, 24_LVBus216737_consumption, 24_LVBus216739_consumption, 24_LVBus216740_consumption, 24_LVBus216748_consumption, 24_LVBus216749_consumption, 24_LVBus216751_consumption, 24_LVBus216752_consumption, 24_LVBus216753_consumption, 24_LVBus216754_consumption, 24_LVBus216755_consumption, 24_LVBus216758_consumption, 24_LVBus216760_consumption, 24_LVBus216761_consumption, 24_LVBus216762_consumption, 24_LVBus216763_consumption, 24_LVBus216764_consumption, 24_LVBus216765_consumption, 24_LVBus216767_consumption, 24_LVBus216768_consumption, 24_LVBus216769_consumption, 24_LVBus216770_consumption, 24_LVBus216771_consumption, 24_LVBus216772_consumption, 24_LVBus216773_consumption, 24_LVBus216774_consumption, 24_LVBus216777_consumption, 24_LVBus216778_consumption, 24_LVBus216779_consumption, 24_LVBus216780_consumption, 24_LVBus216781_consumption, 24_LVBus216782_consumption, 24_LVBus216784_consumption, 24_LVBus216785_consumption, 24_LVBus216786_consumption, 24_LVBus216788_consumption, 24_LVBus216789_consumption, 24_LVBus216791_consumption, 24_LVBus216792_consumption, 24_LVBus216793_consumption, 24_LVBus216795_consumption, 24_LVBus216797_consumption, 24_LVBus216800_consumption, 24_LVBus216802_consumption, 24_LVBus216803_consumption, 24_LVBus216804_consumption, 24_LVBus216805_consumption, 24_LVBus216806_consumption, 24_LVBus216808_consumption, 24_LVBus216809_consumption, 24_LVBus216810_consumption, 24_LVBus216811_consumption, 24_LVBus216813_consumption, 24_LVBus216815_consumption, 24_LVBus216817_consumption, 24_LVBus216820_consumption, 24_LVBus216827_consumption, 24_LVBus216839_consumption, 24_LVBus216841_consumption, 24_LVBus216842_consumption, 24_LVBus216849_consumption, 24_LVBus216850_consumption, 24_LVBus216851_consumption, 24_LVBus216852_consumption, 24_LVBus216853_consumption, 24_LVBus216854_consumption, 24_LVBus216855_consumption, 24_LVBus216856_consumption, 24_LVBus216857_consumption, 24_LVBus216859_consumption, 24_LVBus216864_consumption, 24_LVBus216868_consumption, 24_LVBus216869_consumption, 24_LVBus216871_consumption, 24_LVBus216874_consumption, 24_LVBus216891_consumption, 24_LVBus216892_consumption, 24_LVBus216894_consumption, 24_LVBus216896_consumption, 24_LVBus216902_consumption, 24_LVBus216904_consumption, 24_LVBus216905_consumption, 24_LVBus216906_consumption, 24_LVBus216913_consumption, 24_LVBus216914_consumption, 24_LVBus216916_consumption, 24_LVBus216918_consumption, 24_LVBus216920_consumption, 24_LVBus216922_consumption, 24_LVBus216924_consumption, 24_LVBus216927_consumption, 24_LVBus216929_consumption, 24_LVBus216930_consumption, 24_LVBus216932_consumption, 24_LVBus216933_consumption, 24_LVBus216941_consumption, 24_LVBus216942_consumption, 24_LVBus216943_consumption, 24_LVBus216944_consumption, 24_LVBus216945_consumption, 24_LVBus216948_consumption, 24_LVBus216949_consumption, 24_LVBus216972_consumption, 24_LVBus216975_consumption, 24_LVBus216976_consumption, 24_LVBus216983_consumption, 24_LVBus216985_consumption, 24_LVBus216993_consumption, 24_LVBus216996_consumption, 24_LVBus216998_consumption, 24_LVBus216999_consumption, 24_LVBus217001_consumption, 24_LVBus217003_consumption, 24_LVBus217004_consumption, 24_LVBus217014_consumption, 24_LVBus217015_consumption, 24_LVBus217022_consumption, 24_LVBus217028_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  249 group(s) of loads (498 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  12 group(s) of series lines (26 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  322 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus216724_production, 24_LVBus216726_production, 24_LVBus216728_production, 24_LVBus216729_consumption, 24_LVBus216729_production, 24_LVBus216732_production, 24_LVBus216733_consumption, 24_LVBus216733_production, 24_LVBus216735_consumption, 24_LVBus216735_production, 24_LVBus216736_consumption, 24_LVBus216736_production, 24_LVBus216737_production, 24_LVBus216738_consumption, 24_LVBus216738_production, 24_LVBus216739_production, 24_LVBus216740_production, 24_LVBus216744_production, 24_LVBus216745_production, 24_LVBus216746_production, 24_LVBus216747_production, 24_LVBus216748_production, 24_LVBus216749_production, 24_LVBus216750_consumption, 24_LVBus216750_production, 24_LVBus216751_production, 24_LVBus216752_production, 24_LVBus216753_production, 24_LVBus216754_production, 24_LVBus216755_production, 24_LVBus216756_consumption, 24_LVBus216756_production, 24_LVBus216757_consumption, 24_LVBus216757_production, 24_LVBus216758_production, 24_LVBus216760_production, 24_LVBus216761_production, 24_LVBus216762_production, 24_LVBus216763_production, 24_LVBus216764_production, 24_LVBus216765_production, 24_LVBus216766_consumption, 24_LVBus216766_production, 24_LVBus216767_production, 24_LVBus216768_production, 24_LVBus216769_production, 24_LVBus216770_production, 24_LVBus216771_production, 24_LVBus216772_production, 24_LVBus216773_production, 24_LVBus216774_production, 24_LVBus216775_consumption, 24_LVBus216775_production, 24_LVBus216777_production, 24_LVBus216778_production, 24_LVBus216779_production, 24_LVBus216780_production, 24_LVBus216781_production, 24_LVBus216782_production, 24_LVBus216783_production, 24_LVBus216784_production, 24_LVBus216785_production, 24_LVBus216786_production, 24_LVBus216788_production, 24_LVBus216789_production, 24_LVBus216790_consumption, 24_LVBus216790_production, 24_LVBus216791_production, 24_LVBus216792_production, 24_LVBus216793_production, 24_LVBus216794_consumption, 24_LVBus216794_production, 24_LVBus216795_production, 24_LVBus216796_consumption, 24_LVBus216796_production, 24_LVBus216797_production, 24_LVBus216799_consumption, 24_LVBus216799_production, 24_LVBus216800_production, 24_LVBus216801_consumption, 24_LVBus216801_production, 24_LVBus216802_production, 24_LVBus216803_production, 24_LVBus216804_production, 24_LVBus216805_production, 24_LVBus216806_production, 24_LVBus216808_production, 24_LVBus216809_production, 24_LVBus216810_production, 24_LVBus216811_production, 24_LVBus216812_production, 24_LVBus216813_production, 24_LVBus216815_production, 24_LVBus216816_production, 24_LVBus216817_production, 24_LVBus216818_consumption, 24_LVBus216818_production, 24_LVBus216819_production, 24_LVBus216820_production, 24_LVBus216821_production, 24_LVBus216822_production, 24_LVBus216824_consumption, 24_LVBus216824_production, 24_LVBus216826_consumption, 24_LVBus216826_production, 24_LVBus216827_production, 24_LVBus216829_production, 24_LVBus216830_consumption, 24_LVBus216830_production, 24_LVBus216831_production, 24_LVBus216832_consumption, 24_LVBus216832_production, 24_LVBus216834_production, 24_LVBus216835_production, 24_LVBus216836_production, 24_LVBus216837_production, 24_LVBus216838_production, 24_LVBus216839_production, 24_LVBus216840_consumption, 24_LVBus216840_production, 24_LVBus216841_production, 24_LVBus216842_production, 24_LVBus216843_production, 24_LVBus216844_consumption, 24_LVBus216844_production, 24_LVBus216845_consumption, 24_LVBus216845_production, 24_LVBus216846_production, 24_LVBus216848_consumption, 24_LVBus216848_production, 24_LVBus216849_production, 24_LVBus216850_production, 24_LVBus216851_production, 24_LVBus216852_production, 24_LVBus216853_production, 24_LVBus216854_production, 24_LVBus216855_production, 24_LVBus216856_production, 24_LVBus216857_production, 24_LVBus216858_production, 24_LVBus216859_production, 24_LVBus216860_production, 24_LVBus216862_production, 24_LVBus216864_production, 24_LVBus216865_consumption, 24_LVBus216865_production, 24_LVBus216866_consumption, 24_LVBus216866_production, 24_LVBus216867_production, 24_LVBus216868_production, 24_LVBus216869_production, 24_LVBus216871_production, 24_LVBus216872_consumption, 24_LVBus216872_production, 24_LVBus216873_production, 24_LVBus216874_production, 24_LVBus216875_consumption, 24_LVBus216875_production, 24_LVBus216877_consumption, 24_LVBus216877_production, 24_LVBus216879_production, 24_LVBus216880_production, 24_LVBus216882_consumption, 24_LVBus216882_production, 24_LVBus216883_consumption, 24_LVBus216883_production, 24_LVBus216885_consumption, 24_LVBus216885_production, 24_LVBus216886_consumption, 24_LVBus216886_production, 24_LVBus216887_production, 24_LVBus216889_consumption, 24_LVBus216889_production, 24_LVBus216891_production, 24_LVBus216892_production, 24_LVBus216894_production, 24_LVBus216895_production, 24_LVBus216896_production, 24_LVBus216897_consumption, 24_LVBus216897_production, 24_LVBus216898_production, 24_LVBus216900_consumption, 24_LVBus216900_production, 24_LVBus216901_production, 24_LVBus216902_production, 24_LVBus216903_production, 24_LVBus216904_production, 24_LVBus216905_production, 24_LVBus216906_production, 24_LVBus216907_production, 24_LVBus216909_consumption, 24_LVBus216909_production, 24_LVBus216910_consumption, 24_LVBus216910_production, 24_LVBus216911_production, 24_LVBus216912_production, 24_LVBus216913_production, 24_LVBus216914_production, 24_LVBus216915_production, 24_LVBus216916_production, 24_LVBus216917_production, 24_LVBus216918_production, 24_LVBus216920_production, 24_LVBus216921_production, 24_LVBus216922_production, 24_LVBus216923_production, 24_LVBus216924_production, 24_LVBus216925_production, 24_LVBus216927_production, 24_LVBus216928_production, 24_LVBus216929_production, 24_LVBus216930_production, 24_LVBus216931_production, 24_LVBus216932_production, 24_LVBus216933_production, 24_LVBus216935_consumption, 24_LVBus216935_production, 24_LVBus216937_consumption, 24_LVBus216937_production, 24_LVBus216938_production, 24_LVBus216939_production, 24_LVBus216940_production, 24_LVBus216941_production, 24_LVBus216942_production, 24_LVBus216943_production, 24_LVBus216944_production, 24_LVBus216945_production, 24_LVBus216947_consumption, 24_LVBus216947_production, 24_LVBus216948_production, 24_LVBus216949_production, 24_LVBus216950_production, 24_LVBus216951_production, 24_LVBus216953_consumption, 24_LVBus216953_production, 24_LVBus216954_production, 24_LVBus216956_consumption, 24_LVBus216956_production, 24_LVBus216957_consumption, 24_LVBus216957_production, 24_LVBus216959_consumption, 24_LVBus216959_production, 24_LVBus216960_production, 24_LVBus216962_consumption, 24_LVBus216962_production, 24_LVBus216963_consumption, 24_LVBus216963_production, 24_LVBus216968_consumption, 24_LVBus216968_production, 24_LVBus216969_consumption, 24_LVBus216969_production, 24_LVBus216970_consumption, 24_LVBus216970_production, 24_LVBus216972_production, 24_LVBus216973_production, 24_LVBus216974_production, 24_LVBus216975_production, 24_LVBus216976_production, 24_LVBus216978_consumption, 24_LVBus216978_production, 24_LVBus216979_consumption, 24_LVBus216979_production, 24_LVBus216980_consumption, 24_LVBus216980_production, 24_LVBus216982_consumption, 24_LVBus216982_production, 24_LVBus216983_production, 24_LVBus216984_production, 24_LVBus216985_production, 24_LVBus216987_consumption, 24_LVBus216987_production, 24_LVBus216988_production, 24_LVBus216990_consumption, 24_LVBus216990_production, 24_LVBus216991_consumption, 24_LVBus216991_production, 24_LVBus216992_consumption, 24_LVBus216992_production, 24_LVBus216993_production, 24_LVBus216994_production, 24_LVBus216995_production, 24_LVBus216996_production, 24_LVBus216998_production, 24_LVBus216999_production, 24_LVBus217000_consumption, 24_LVBus217000_production, 24_LVBus217001_production, 24_LVBus217002_production, 24_LVBus217003_production, 24_LVBus217004_production, 24_LVBus217014_production, 24_LVBus217015_production, 24_LVBus217016_consumption, 24_LVBus217016_production, 24_LVBus217020_consumption, 24_LVBus217020_production, 24_LVBus217021_consumption, 24_LVBus217021_production, 24_LVBus217022_production, 24_LVBus217025_consumption, 24_LVBus217025_production, 24_LVBus217026_consumption, 24_LVBus217026_production, 24_LVBus217027_consumption, 24_LVBus217027_production, 24_LVBus217028_production, 24_LVBus217029_consumption, 24_LVBus217029_production, 24_LVBus217030_consumption, 24_LVBus217030_production, 24_LVBus217032_consumption, 24_LVBus217032_production, 24_LVBus217033_consumption, 24_LVBus217033_production, 24_LVBus217035_consumption, 24_LVBus217035_production, 24_LVBus835069_consumption, 24_LVBus835069_production, 24_MVLV78990_consumption, 24_MVLV78990_production, 24_MVLV82213_consumption, 24_MVLV82213_production.

