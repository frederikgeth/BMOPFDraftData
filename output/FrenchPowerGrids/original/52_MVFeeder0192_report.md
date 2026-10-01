# BMOPF Network Summary: 52_MVFeeder0192

**Generated:** 2026-10-01 23:34:11  
**Findings:** 0 errors · 5 warnings · 204 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 331 |  |
| line | 310 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 572 | 4.117 MW, 1.24 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 20 |  |
| switch | 0 |  |
| transformer | 20 | Dyn11×20 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 29 | 28 | 8 | 0 |
| LV_236V | 236.0 V | 302 | 282 | 564 | 0 |

**Transformer transitions:**

- `52_MVLV045737_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104253_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV045745_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV062085_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009404_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV045825_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV032491_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV067820_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV020762_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV087109_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV064284_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV074054_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV102875_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV086584_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV032866_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV022619_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV105283_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV000738_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV021769_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV045822_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 7 |
| Degree-1 buses | 126 |
| Tree depth (max hops) | 17 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 331 | 1 | 330 | 0 | 0 | 0 |
| Tier LV_236V | 302 | 20 | 282 | 0 | 0 | 0 |
| Tier MV_11.8kV | 29 | 1 | 28 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 20; skipped invalid branches: 0.

Galvanic zones: 21; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_BENE5 | MV_11.8kV | 29 | 0 | 0 | 20 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1295 declared bus terminals; 1212 mapped line/closed-switch conductor edges; 83 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 461000.0 | 8.227 | 1716 |
| q_nom | 0.0 | 138000.0 | 8.227 | 1716 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.29 | 2870.0 | 1.882 | 310 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.551 | 20 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 348 of 572 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267796_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267727_consumption' has phase imbalance of 277.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267687_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267722_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267803_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267855_consumption' has phase imbalance of 43.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267685_consumption' has phase imbalance of 271.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267829_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267890_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267967_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267873_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267667_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267688_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267813_consumption' has phase imbalance of 113.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267686_consumption' has phase imbalance of 278.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267740_consumption' has phase imbalance of 73.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267772_consumption' has phase imbalance of 165.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267854_consumption' has phase imbalance of 44.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267673_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267842_consumption' has phase imbalance of 130.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267719_consumption' has phase imbalance of 149.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267960_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267750_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267821_consumption' has phase imbalance of 227.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267784_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267824_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267710_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267848_consumption' has phase imbalance of 125.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267816_consumption' has phase imbalance of 114.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267871_consumption' has phase imbalance of 264.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267817_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267811_consumption' has phase imbalance of 34.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267966_consumption' has phase imbalance of 114.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267760_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267874_consumption' has phase imbalance of 248.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267704_consumption' has phase imbalance of 37.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267761_consumption' has phase imbalance of 58.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267681_consumption' has phase imbalance of 100.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267882_consumption' has phase imbalance of 144.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267892_consumption' has phase imbalance of 253.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267826_consumption' has phase imbalance of 104.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267759_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267654_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267837_consumption' has phase imbalance of 112.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267690_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267743_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267662_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267718_consumption' has phase imbalance of 59.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267844_consumption' has phase imbalance of 145.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267976_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267663_consumption' has phase imbalance of 211.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267752_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267700_consumption' has phase imbalance of 87.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267818_consumption' has phase imbalance of 121.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267839_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267767_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267852_consumption' has phase imbalance of 105.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267745_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267793_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267787_consumption' has phase imbalance of 72.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267800_consumption' has phase imbalance of 128.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267819_consumption' has phase imbalance of 84.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267971_consumption' has phase imbalance of 224.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267708_consumption' has phase imbalance of 209.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267758_consumption' has phase imbalance of 112.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267714_consumption' has phase imbalance of 34.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267812_consumption' has phase imbalance of 86.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267792_consumption' has phase imbalance of 269.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267790_consumption' has phase imbalance of 66.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267744_consumption' has phase imbalance of 102.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267834_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267757_consumption' has phase imbalance of 270.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267693_consumption' has phase imbalance of 96.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267668_consumption' has phase imbalance of 148.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267827_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267684_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267856_consumption' has phase imbalance of 46.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267765_consumption' has phase imbalance of 56.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267731_consumption' has phase imbalance of 172.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267868_consumption' has phase imbalance of 198.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267795_consumption' has phase imbalance of 118.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267713_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267963_consumption' has phase imbalance of 246.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267751_consumption' has phase imbalance of 176.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267859_consumption' has phase imbalance of 129.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267773_consumption' has phase imbalance of 269.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267705_consumption' has phase imbalance of 207.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267830_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267799_consumption' has phase imbalance of 39.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267929_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267838_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267857_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267866_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267893_consumption' has phase imbalance of 187.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267970_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267823_consumption' has phase imbalance of 156.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267846_consumption' has phase imbalance of 94.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267766_consumption' has phase imbalance of 172.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267965_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267870_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267701_consumption' has phase imbalance of 193.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267849_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267845_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267655_consumption' has phase imbalance of 80.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267716_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267872_consumption' has phase imbalance of 62.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267862_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267678_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267746_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267864_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267768_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267702_consumption' has phase imbalance of 258.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267669_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267695_consumption' has phase imbalance of 206.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267665_consumption' has phase imbalance of 90.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267697_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267822_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267809_consumption' has phase imbalance of 256.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267721_consumption' has phase imbalance of 143.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267828_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267682_consumption' has phase imbalance of 131.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267754_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267720_consumption' has phase imbalance of 54.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267962_consumption' has phase imbalance of 30.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267741_consumption' has phase imbalance of 266.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267656_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267756_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267886_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267794_consumption' has phase imbalance of 128.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267664_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267969_consumption' has phase imbalance of 36.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267786_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267798_consumption' has phase imbalance of 156.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267707_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267850_consumption' has phase imbalance of 91.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267853_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267733_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267797_consumption' has phase imbalance of 121.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267677_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267748_consumption' has phase imbalance of 158.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267694_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267879_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267683_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267674_consumption' has phase imbalance of 118.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267771_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267657_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1181076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267703_consumption' has phase imbalance of 31.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267835_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267763_consumption' has phase imbalance of 74.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267676_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267749_consumption' has phase imbalance of 146.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267715_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267885_consumption' has phase imbalance of 54.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267831_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus267884_consumption' has phase imbalance of 134.8%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 572 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_BENE5' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus1178832' has balanced aggregate load across 3 phase(s) (max spread 0.07%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus267932' has balanced aggregate load across 3 phase(s) (max spread 1.48%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus267650' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus267922' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.117 MW |
| Total load Q | 1.24 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV045737_Transformer | 275.0 kVA | 11.9% |
| 52_MVLV104253_Transformer | 275.0 kVA | 25.5% |
| 52_MVLV045745_Transformer | 693.0 kVA | 20.6% |
| 52_MVLV062085_Transformer | 440.0 kVA | 26.3% |
| 52_MVLV009404_Transformer | 176.0 kVA | 13.2% |
| 52_MVLV045825_Transformer | 693.0 kVA | 43.8% |
| 52_MVLV032491_Transformer | 176.0 kVA | 7.7% |
| 52_MVLV067820_Transformer | 440.0 kVA | 46.7% |
| 52_MVLV020762_Transformer | 440.0 kVA | 24.9% |
| 52_MVLV087109_Transformer | 110.0 kVA | 12.7% |
| 52_MVLV064284_Transformer | 693.0 kVA | 29.6% |
| 52_MVLV074054_Transformer | 1.1 MVA | 38.3% |
| 52_MVLV102875_Transformer | 693.0 kVA | 24.7% |
| 52_MVLV086584_Transformer | 693.0 kVA | 16.7% |
| 52_MVLV032866_Transformer | 440.0 kVA | 25.2% |
| 52_MVLV022619_Transformer | 440.0 kVA | 16.6% |
| 52_MVLV105283_Transformer | 275.0 kVA | 9.2% |
| 52_MVLV000738_Transformer | 110.0 kVA | 3.2% |
| 52_MVLV021769_Transformer | 693.0 kVA | 45.1% |
| 52_MVLV045822_Transformer | 440.0 kVA | 41.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.12 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus267650' (LV, 0.24 kV) has an electrical reach of 8.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 331 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 331 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 29 |
| LV_236V | 4-wire | 302 / 302 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 302 |
| Neutral branches | 282 |
| Grounding points | 20 |
| Neutral sections | 20 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| exactly_balanced | 1 |
| decoupled | 2 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 4 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 29 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 21 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1160.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 302 / 29 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 349 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 349 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1153094_consumption, 52_LVBus1153094_production, 52_LVBus1153095_consumption, 52_LVBus1153095_production, 52_LVBus1155391_consumption, 52_LVBus1155391_production, 52_LVBus1155392_consumption, 52_LVBus1155392_production, 52_LVBus1156149_consumption, 52_LVBus1156149_production, 52_LVBus1156659_consumption, 52_LVBus1156659_production, 52_LVBus1161141_consumption, 52_LVBus1161141_production, 52_LVBus1162803_consumption, 52_LVBus1162803_production, 52_LVBus1178832_consumption, 52_LVBus1178832_production, 52_LVBus1180281_consumption, 52_LVBus1180281_production, 52_LVBus1181075_consumption, 52_LVBus1181075_production, 52_LVBus1181076_production, 52_LVBus1182374_consumption, 52_LVBus1182374_production, 52_LVBus1183080_production, 52_LVBus1185395_consumption, 52_LVBus1185395_production, 52_LVBus1188640_consumption, 52_LVBus1188640_production, 52_LVBus267642_consumption, 52_LVBus267642_production, 52_LVBus267644_consumption, 52_LVBus267644_production, 52_LVBus267646_consumption, 52_LVBus267646_production, 52_LVBus267648_consumption, 52_LVBus267648_production, 52_LVBus267650_production, 52_LVBus267651_consumption, 52_LVBus267651_production, 52_LVBus267654_production, 52_LVBus267655_production, 52_LVBus267656_production, 52_LVBus267657_production, 52_LVBus267658_production, 52_LVBus267659_production, 52_LVBus267660_production, 52_LVBus267662_production, 52_LVBus267663_production, 52_LVBus267664_production, 52_LVBus267665_production, 52_LVBus267667_production, 52_LVBus267668_production, 52_LVBus267669_production, 52_LVBus267671_consumption, 52_LVBus267671_production, 52_LVBus267672_consumption, 52_LVBus267672_production, 52_LVBus267673_production, 52_LVBus267674_production, 52_LVBus267676_production, 52_LVBus267677_production, 52_LVBus267678_production, 52_LVBus267679_consumption, 52_LVBus267679_production, 52_LVBus267680_consumption, 52_LVBus267680_production, 52_LVBus267681_production, 52_LVBus267682_production, 52_LVBus267683_production, 52_LVBus267684_production, 52_LVBus267685_production, 52_LVBus267686_production, 52_LVBus267687_production, 52_LVBus267688_production, 52_LVBus267690_production, 52_LVBus267691_production, 52_LVBus267693_production, 52_LVBus267694_production, 52_LVBus267695_production, 52_LVBus267696_production, 52_LVBus267697_production, 52_LVBus267699_consumption, 52_LVBus267699_production, 52_LVBus267700_production, 52_LVBus267701_production, 52_LVBus267702_production, 52_LVBus267703_production, 52_LVBus267704_production, 52_LVBus267705_production, 52_LVBus267706_production, 52_LVBus267707_production, 52_LVBus267708_production, 52_LVBus267709_production, 52_LVBus267710_production, 52_LVBus267713_production, 52_LVBus267714_production, 52_LVBus267715_production, 52_LVBus267716_production, 52_LVBus267718_production, 52_LVBus267719_production, 52_LVBus267720_production, 52_LVBus267721_production, 52_LVBus267722_production, 52_LVBus267724_consumption, 52_LVBus267724_production, 52_LVBus267725_consumption, 52_LVBus267725_production, 52_LVBus267726_consumption, 52_LVBus267726_production, 52_LVBus267727_production, 52_LVBus267728_production, 52_LVBus267729_consumption, 52_LVBus267729_production, 52_LVBus267730_consumption, 52_LVBus267730_production, 52_LVBus267731_production, 52_LVBus267732_production, 52_LVBus267733_production, 52_LVBus267734_consumption, 52_LVBus267734_production, 52_LVBus267735_consumption, 52_LVBus267735_production, 52_LVBus267736_consumption, 52_LVBus267736_production, 52_LVBus267738_consumption, 52_LVBus267738_production, 52_LVBus267740_production, 52_LVBus267741_production, 52_LVBus267743_production, 52_LVBus267744_production, 52_LVBus267745_production, 52_LVBus267746_production, 52_LVBus267748_production, 52_LVBus267749_production, 52_LVBus267750_production, 52_LVBus267751_production, 52_LVBus267752_production, 52_LVBus267754_production, 52_LVBus267756_production, 52_LVBus267757_production, 52_LVBus267758_production, 52_LVBus267759_production, 52_LVBus267760_production, 52_LVBus267761_production, 52_LVBus267763_production, 52_LVBus267765_production, 52_LVBus267766_production, 52_LVBus267767_production, 52_LVBus267768_production, 52_LVBus267770_production, 52_LVBus267771_production, 52_LVBus267772_production, 52_LVBus267773_production, 52_LVBus267775_production, 52_LVBus267776_production, 52_LVBus267777_production, 52_LVBus267778_production, 52_LVBus267779_production, 52_LVBus267781_consumption, 52_LVBus267781_production, 52_LVBus267783_consumption, 52_LVBus267783_production, 52_LVBus267784_production, 52_LVBus267786_production, 52_LVBus267787_production, 52_LVBus267789_production, 52_LVBus267790_production, 52_LVBus267792_production, 52_LVBus267793_production, 52_LVBus267794_production, 52_LVBus267795_production, 52_LVBus267796_production, 52_LVBus267797_production, 52_LVBus267798_production, 52_LVBus267799_production, 52_LVBus267800_production, 52_LVBus267801_production, 52_LVBus267803_production, 52_LVBus267804_consumption, 52_LVBus267804_production, 52_LVBus267805_consumption, 52_LVBus267805_production, 52_LVBus267806_consumption, 52_LVBus267806_production, 52_LVBus267807_consumption, 52_LVBus267807_production, 52_LVBus267808_production, 52_LVBus267809_production, 52_LVBus267810_production, 52_LVBus267811_production, 52_LVBus267812_production, 52_LVBus267813_production, 52_LVBus267815_production, 52_LVBus267816_production, 52_LVBus267817_production, 52_LVBus267818_production, 52_LVBus267819_production, 52_LVBus267821_production, 52_LVBus267822_production, 52_LVBus267823_production, 52_LVBus267824_production, 52_LVBus267826_production, 52_LVBus267827_production, 52_LVBus267828_production, 52_LVBus267829_production, 52_LVBus267830_production, 52_LVBus267831_production, 52_LVBus267834_production, 52_LVBus267835_production, 52_LVBus267837_production, 52_LVBus267838_production, 52_LVBus267839_production, 52_LVBus267840_production, 52_LVBus267841_production, 52_LVBus267842_production, 52_LVBus267844_production, 52_LVBus267845_production, 52_LVBus267846_production, 52_LVBus267848_production, 52_LVBus267849_production, 52_LVBus267850_production, 52_LVBus267852_production, 52_LVBus267853_production, 52_LVBus267854_production, 52_LVBus267855_production, 52_LVBus267856_production, 52_LVBus267857_production, 52_LVBus267859_production, 52_LVBus267861_production, 52_LVBus267862_production, 52_LVBus267863_production, 52_LVBus267864_production, 52_LVBus267865_production, 52_LVBus267866_production, 52_LVBus267868_production, 52_LVBus267869_production, 52_LVBus267870_production, 52_LVBus267871_production, 52_LVBus267872_production, 52_LVBus267873_production, 52_LVBus267874_production, 52_LVBus267876_production, 52_LVBus267878_consumption, 52_LVBus267878_production, 52_LVBus267879_production, 52_LVBus267880_production, 52_LVBus267881_consumption, 52_LVBus267881_production, 52_LVBus267882_production, 52_LVBus267883_production, 52_LVBus267884_production, 52_LVBus267885_production, 52_LVBus267886_production, 52_LVBus267888_consumption, 52_LVBus267888_production, 52_LVBus267889_consumption, 52_LVBus267889_production, 52_LVBus267890_production, 52_LVBus267891_production, 52_LVBus267892_production, 52_LVBus267893_production, 52_LVBus267894_production, 52_LVBus267895_production, 52_LVBus267897_production, 52_LVBus267898_production, 52_LVBus267899_production, 52_LVBus267900_production, 52_LVBus267901_production, 52_LVBus267903_production, 52_LVBus267904_production, 52_LVBus267905_production, 52_LVBus267906_consumption, 52_LVBus267906_production, 52_LVBus267907_production, 52_LVBus267909_production, 52_LVBus267910_production, 52_LVBus267912_production, 52_LVBus267913_consumption, 52_LVBus267913_production, 52_LVBus267914_production, 52_LVBus267916_production, 52_LVBus267917_consumption, 52_LVBus267917_production, 52_LVBus267918_production, 52_LVBus267920_consumption, 52_LVBus267920_production, 52_LVBus267922_consumption, 52_LVBus267922_production, 52_LVBus267924_production, 52_LVBus267926_production, 52_LVBus267928_production, 52_LVBus267929_production, 52_LVBus267932_production, 52_LVBus267933_consumption, 52_LVBus267933_production, 52_LVBus267935_consumption, 52_LVBus267935_production, 52_LVBus267936_production, 52_LVBus267937_consumption, 52_LVBus267937_production, 52_LVBus267938_production, 52_LVBus267940_consumption, 52_LVBus267940_production, 52_LVBus267941_consumption, 52_LVBus267941_production, 52_LVBus267942_production, 52_LVBus267943_consumption, 52_LVBus267943_production, 52_LVBus267944_consumption, 52_LVBus267944_production, 52_LVBus267945_production, 52_LVBus267946_consumption, 52_LVBus267946_production, 52_LVBus267947_production, 52_LVBus267949_consumption, 52_LVBus267949_production, 52_LVBus267950_production, 52_LVBus267951_production, 52_LVBus267952_consumption, 52_LVBus267952_production, 52_LVBus267953_consumption, 52_LVBus267953_production, 52_LVBus267954_production, 52_LVBus267955_production, 52_LVBus267957_production, 52_LVBus267960_production, 52_LVBus267962_production, 52_LVBus267963_production, 52_LVBus267965_production, 52_LVBus267966_production, 52_LVBus267967_production, 52_LVBus267969_production, 52_LVBus267970_production, 52_LVBus267971_production, 52_LVBus267973_production, 52_LVBus267974_consumption, 52_LVBus267974_production, 52_LVBus267975_production, 52_LVBus267976_production, 52_LVBus267977_consumption, 52_LVBus267977_production, 52_MVLV000332_consumption, 52_MVLV000332_production, 52_MVLV000458_production, 52_MVLV062038_consumption, 52_MVLV062038_production, 52_MVLV102220_production.

## 9. Data Quality Summary

**Total findings:** 209 (0 errors, 5 warnings, 204 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  348 of 572 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.12 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  349 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267796_consumption`  
  Load '52_LVBus267796_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267727_consumption`  
  Load '52_LVBus267727_consumption' has phase imbalance of 277.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267687_consumption`  
  Load '52_LVBus267687_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267722_consumption`  
  Load '52_LVBus267722_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267803_consumption`  
  Load '52_LVBus267803_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267855_consumption`  
  Load '52_LVBus267855_consumption' has phase imbalance of 43.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267685_consumption`  
  Load '52_LVBus267685_consumption' has phase imbalance of 271.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267829_consumption`  
  Load '52_LVBus267829_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267890_consumption`  
  Load '52_LVBus267890_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267973_consumption`  
  Load '52_LVBus267973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267967_consumption`  
  Load '52_LVBus267967_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267873_consumption`  
  Load '52_LVBus267873_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267667_consumption`  
  Load '52_LVBus267667_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267688_consumption`  
  Load '52_LVBus267688_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267813_consumption`  
  Load '52_LVBus267813_consumption' has phase imbalance of 113.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267686_consumption`  
  Load '52_LVBus267686_consumption' has phase imbalance of 278.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267740_consumption`  
  Load '52_LVBus267740_consumption' has phase imbalance of 73.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267772_consumption`  
  Load '52_LVBus267772_consumption' has phase imbalance of 165.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267854_consumption`  
  Load '52_LVBus267854_consumption' has phase imbalance of 44.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267673_consumption`  
  Load '52_LVBus267673_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267842_consumption`  
  Load '52_LVBus267842_consumption' has phase imbalance of 130.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267808_consumption`  
  Load '52_LVBus267808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267719_consumption`  
  Load '52_LVBus267719_consumption' has phase imbalance of 149.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267960_consumption`  
  Load '52_LVBus267960_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267750_consumption`  
  Load '52_LVBus267750_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267821_consumption`  
  Load '52_LVBus267821_consumption' has phase imbalance of 227.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267658_consumption`  
  Load '52_LVBus267658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267784_consumption`  
  Load '52_LVBus267784_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267824_consumption`  
  Load '52_LVBus267824_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267710_consumption`  
  Load '52_LVBus267710_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267848_consumption`  
  Load '52_LVBus267848_consumption' has phase imbalance of 125.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267880_consumption`  
  Load '52_LVBus267880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267816_consumption`  
  Load '52_LVBus267816_consumption' has phase imbalance of 114.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267871_consumption`  
  Load '52_LVBus267871_consumption' has phase imbalance of 264.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267801_consumption`  
  Load '52_LVBus267801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267728_consumption`  
  Load '52_LVBus267728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267770_consumption`  
  Load '52_LVBus267770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267817_consumption`  
  Load '52_LVBus267817_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267863_consumption`  
  Load '52_LVBus267863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267811_consumption`  
  Load '52_LVBus267811_consumption' has phase imbalance of 34.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267966_consumption`  
  Load '52_LVBus267966_consumption' has phase imbalance of 114.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267760_consumption`  
  Load '52_LVBus267760_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267660_consumption`  
  Load '52_LVBus267660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267874_consumption`  
  Load '52_LVBus267874_consumption' has phase imbalance of 248.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267704_consumption`  
  Load '52_LVBus267704_consumption' has phase imbalance of 37.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267761_consumption`  
  Load '52_LVBus267761_consumption' has phase imbalance of 58.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267681_consumption`  
  Load '52_LVBus267681_consumption' has phase imbalance of 100.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267869_consumption`  
  Load '52_LVBus267869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267882_consumption`  
  Load '52_LVBus267882_consumption' has phase imbalance of 144.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267892_consumption`  
  Load '52_LVBus267892_consumption' has phase imbalance of 253.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267826_consumption`  
  Load '52_LVBus267826_consumption' has phase imbalance of 104.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267883_consumption`  
  Load '52_LVBus267883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267759_consumption`  
  Load '52_LVBus267759_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267654_consumption`  
  Load '52_LVBus267654_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267732_consumption`  
  Load '52_LVBus267732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267837_consumption`  
  Load '52_LVBus267837_consumption' has phase imbalance of 112.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267690_consumption`  
  Load '52_LVBus267690_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267743_consumption`  
  Load '52_LVBus267743_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267662_consumption`  
  Load '52_LVBus267662_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267696_consumption`  
  Load '52_LVBus267696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267718_consumption`  
  Load '52_LVBus267718_consumption' has phase imbalance of 59.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267815_consumption`  
  Load '52_LVBus267815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267844_consumption`  
  Load '52_LVBus267844_consumption' has phase imbalance of 145.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267840_consumption`  
  Load '52_LVBus267840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267976_consumption`  
  Load '52_LVBus267976_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267663_consumption`  
  Load '52_LVBus267663_consumption' has phase imbalance of 211.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267752_consumption`  
  Load '52_LVBus267752_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267700_consumption`  
  Load '52_LVBus267700_consumption' has phase imbalance of 87.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267818_consumption`  
  Load '52_LVBus267818_consumption' has phase imbalance of 121.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267839_consumption`  
  Load '52_LVBus267839_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267767_consumption`  
  Load '52_LVBus267767_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267852_consumption`  
  Load '52_LVBus267852_consumption' has phase imbalance of 105.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267745_consumption`  
  Load '52_LVBus267745_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267793_consumption`  
  Load '52_LVBus267793_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267787_consumption`  
  Load '52_LVBus267787_consumption' has phase imbalance of 72.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267800_consumption`  
  Load '52_LVBus267800_consumption' has phase imbalance of 128.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267819_consumption`  
  Load '52_LVBus267819_consumption' has phase imbalance of 84.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267659_consumption`  
  Load '52_LVBus267659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267971_consumption`  
  Load '52_LVBus267971_consumption' has phase imbalance of 224.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267708_consumption`  
  Load '52_LVBus267708_consumption' has phase imbalance of 209.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267758_consumption`  
  Load '52_LVBus267758_consumption' has phase imbalance of 112.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267714_consumption`  
  Load '52_LVBus267714_consumption' has phase imbalance of 34.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267812_consumption`  
  Load '52_LVBus267812_consumption' has phase imbalance of 86.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267792_consumption`  
  Load '52_LVBus267792_consumption' has phase imbalance of 269.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267790_consumption`  
  Load '52_LVBus267790_consumption' has phase imbalance of 66.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267744_consumption`  
  Load '52_LVBus267744_consumption' has phase imbalance of 102.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267834_consumption`  
  Load '52_LVBus267834_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267757_consumption`  
  Load '52_LVBus267757_consumption' has phase imbalance of 270.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267693_consumption`  
  Load '52_LVBus267693_consumption' has phase imbalance of 96.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267668_consumption`  
  Load '52_LVBus267668_consumption' has phase imbalance of 148.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267827_consumption`  
  Load '52_LVBus267827_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267684_consumption`  
  Load '52_LVBus267684_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267856_consumption`  
  Load '52_LVBus267856_consumption' has phase imbalance of 46.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267765_consumption`  
  Load '52_LVBus267765_consumption' has phase imbalance of 56.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267731_consumption`  
  Load '52_LVBus267731_consumption' has phase imbalance of 172.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267868_consumption`  
  Load '52_LVBus267868_consumption' has phase imbalance of 198.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267795_consumption`  
  Load '52_LVBus267795_consumption' has phase imbalance of 118.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267713_consumption`  
  Load '52_LVBus267713_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267963_consumption`  
  Load '52_LVBus267963_consumption' has phase imbalance of 246.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267751_consumption`  
  Load '52_LVBus267751_consumption' has phase imbalance of 176.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267859_consumption`  
  Load '52_LVBus267859_consumption' has phase imbalance of 129.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267975_consumption`  
  Load '52_LVBus267975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267773_consumption`  
  Load '52_LVBus267773_consumption' has phase imbalance of 269.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267706_consumption`  
  Load '52_LVBus267706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267705_consumption`  
  Load '52_LVBus267705_consumption' has phase imbalance of 207.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267830_consumption`  
  Load '52_LVBus267830_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267799_consumption`  
  Load '52_LVBus267799_consumption' has phase imbalance of 39.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267929_consumption`  
  Load '52_LVBus267929_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267838_consumption`  
  Load '52_LVBus267838_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267857_consumption`  
  Load '52_LVBus267857_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267866_consumption`  
  Load '52_LVBus267866_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267893_consumption`  
  Load '52_LVBus267893_consumption' has phase imbalance of 187.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267970_consumption`  
  Load '52_LVBus267970_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267823_consumption`  
  Load '52_LVBus267823_consumption' has phase imbalance of 156.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267846_consumption`  
  Load '52_LVBus267846_consumption' has phase imbalance of 94.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267766_consumption`  
  Load '52_LVBus267766_consumption' has phase imbalance of 172.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267965_consumption`  
  Load '52_LVBus267965_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267870_consumption`  
  Load '52_LVBus267870_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267841_consumption`  
  Load '52_LVBus267841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267701_consumption`  
  Load '52_LVBus267701_consumption' has phase imbalance of 193.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267849_consumption`  
  Load '52_LVBus267849_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267845_consumption`  
  Load '52_LVBus267845_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267928_consumption`  
  Load '52_LVBus267928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267655_consumption`  
  Load '52_LVBus267655_consumption' has phase imbalance of 80.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267716_consumption`  
  Load '52_LVBus267716_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267872_consumption`  
  Load '52_LVBus267872_consumption' has phase imbalance of 62.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267862_consumption`  
  Load '52_LVBus267862_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267678_consumption`  
  Load '52_LVBus267678_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267746_consumption`  
  Load '52_LVBus267746_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267864_consumption`  
  Load '52_LVBus267864_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267768_consumption`  
  Load '52_LVBus267768_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267776_consumption`  
  Load '52_LVBus267776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267702_consumption`  
  Load '52_LVBus267702_consumption' has phase imbalance of 258.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267669_consumption`  
  Load '52_LVBus267669_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267695_consumption`  
  Load '52_LVBus267695_consumption' has phase imbalance of 206.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267665_consumption`  
  Load '52_LVBus267665_consumption' has phase imbalance of 90.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267697_consumption`  
  Load '52_LVBus267697_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267822_consumption`  
  Load '52_LVBus267822_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267809_consumption`  
  Load '52_LVBus267809_consumption' has phase imbalance of 256.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267721_consumption`  
  Load '52_LVBus267721_consumption' has phase imbalance of 143.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267828_consumption`  
  Load '52_LVBus267828_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267682_consumption`  
  Load '52_LVBus267682_consumption' has phase imbalance of 131.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267754_consumption`  
  Load '52_LVBus267754_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267720_consumption`  
  Load '52_LVBus267720_consumption' has phase imbalance of 54.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267775_consumption`  
  Load '52_LVBus267775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267891_consumption`  
  Load '52_LVBus267891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267962_consumption`  
  Load '52_LVBus267962_consumption' has phase imbalance of 30.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267741_consumption`  
  Load '52_LVBus267741_consumption' has phase imbalance of 266.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267656_consumption`  
  Load '52_LVBus267656_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267756_consumption`  
  Load '52_LVBus267756_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267886_consumption`  
  Load '52_LVBus267886_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267794_consumption`  
  Load '52_LVBus267794_consumption' has phase imbalance of 128.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267664_consumption`  
  Load '52_LVBus267664_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267969_consumption`  
  Load '52_LVBus267969_consumption' has phase imbalance of 36.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267786_consumption`  
  Load '52_LVBus267786_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267798_consumption`  
  Load '52_LVBus267798_consumption' has phase imbalance of 156.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267707_consumption`  
  Load '52_LVBus267707_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267777_consumption`  
  Load '52_LVBus267777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267850_consumption`  
  Load '52_LVBus267850_consumption' has phase imbalance of 91.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267789_consumption`  
  Load '52_LVBus267789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267853_consumption`  
  Load '52_LVBus267853_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267733_consumption`  
  Load '52_LVBus267733_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267797_consumption`  
  Load '52_LVBus267797_consumption' has phase imbalance of 121.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267861_consumption`  
  Load '52_LVBus267861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267677_consumption`  
  Load '52_LVBus267677_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267709_consumption`  
  Load '52_LVBus267709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267748_consumption`  
  Load '52_LVBus267748_consumption' has phase imbalance of 158.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267694_consumption`  
  Load '52_LVBus267694_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267879_consumption`  
  Load '52_LVBus267879_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267683_consumption`  
  Load '52_LVBus267683_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267674_consumption`  
  Load '52_LVBus267674_consumption' has phase imbalance of 118.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267771_consumption`  
  Load '52_LVBus267771_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267657_consumption`  
  Load '52_LVBus267657_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1181076_consumption`  
  Load '52_LVBus1181076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267703_consumption`  
  Load '52_LVBus267703_consumption' has phase imbalance of 31.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267835_consumption`  
  Load '52_LVBus267835_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267763_consumption`  
  Load '52_LVBus267763_consumption' has phase imbalance of 74.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267676_consumption`  
  Load '52_LVBus267676_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267749_consumption`  
  Load '52_LVBus267749_consumption' has phase imbalance of 146.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267715_consumption`  
  Load '52_LVBus267715_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267885_consumption`  
  Load '52_LVBus267885_consumption' has phase imbalance of 54.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267831_consumption`  
  Load '52_LVBus267831_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus267884_consumption`  
  Load '52_LVBus267884_consumption' has phase imbalance of 134.8%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 572 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_BENE5' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus1178832' has balanced aggregate load across 3 phase(s) (max spread 0.07%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus267932' has balanced aggregate load across 3 phase(s) (max spread 1.48%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus267650' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus267922' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus267650' (LV, 0.24 kV) has an electrical reach of 8.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  331 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  87 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 52_LVBus1181076_consumption, 52_LVBus267654_consumption, 52_LVBus267656_consumption, 52_LVBus267657_consumption, 52_LVBus267658_consumption, 52_LVBus267659_consumption, 52_LVBus267660_consumption, 52_LVBus267663_consumption, 52_LVBus267664_consumption, 52_LVBus267683_consumption, 52_LVBus267685_consumption, 52_LVBus267686_consumption, 52_LVBus267687_consumption, 52_LVBus267688_consumption, 52_LVBus267694_consumption, 52_LVBus267695_consumption, 52_LVBus267696_consumption, 52_LVBus267701_consumption, 52_LVBus267706_consumption, 52_LVBus267708_consumption, 52_LVBus267709_consumption, 52_LVBus267713_consumption, 52_LVBus267715_consumption, 52_LVBus267716_consumption, 52_LVBus267727_consumption, 52_LVBus267728_consumption, 52_LVBus267731_consumption, 52_LVBus267732_consumption, 52_LVBus267733_consumption, 52_LVBus267741_consumption, 52_LVBus267743_consumption, 52_LVBus267748_consumption, 52_LVBus267751_consumption, 52_LVBus267752_consumption, 52_LVBus267756_consumption, 52_LVBus267757_consumption, 52_LVBus267760_consumption, 52_LVBus267766_consumption, 52_LVBus267767_consumption, 52_LVBus267768_consumption, 52_LVBus267770_consumption, 52_LVBus267771_consumption, 52_LVBus267773_consumption, 52_LVBus267775_consumption, 52_LVBus267776_consumption, 52_LVBus267777_consumption, 52_LVBus267789_consumption, 52_LVBus267792_consumption, 52_LVBus267796_consumption, 52_LVBus267798_consumption, 52_LVBus267801_consumption, 52_LVBus267808_consumption, 52_LVBus267809_consumption, 52_LVBus267815_consumption, 52_LVBus267821_consumption, 52_LVBus267822_consumption, 52_LVBus267829_consumption, 52_LVBus267830_consumption, 52_LVBus267838_consumption, 52_LVBus267839_consumption, 52_LVBus267840_consumption, 52_LVBus267841_consumption, 52_LVBus267853_consumption, 52_LVBus267861_consumption, 52_LVBus267863_consumption, 52_LVBus267864_consumption, 52_LVBus267866_consumption, 52_LVBus267868_consumption, 52_LVBus267869_consumption, 52_LVBus267870_consumption, 52_LVBus267871_consumption, 52_LVBus267874_consumption, 52_LVBus267880_consumption, 52_LVBus267883_consumption, 52_LVBus267886_consumption, 52_LVBus267890_consumption, 52_LVBus267891_consumption, 52_LVBus267892_consumption, 52_LVBus267928_consumption, 52_LVBus267963_consumption, 52_LVBus267965_consumption, 52_LVBus267967_consumption, 52_LVBus267970_consumption, 52_LVBus267971_consumption, 52_LVBus267973_consumption, 52_LVBus267975_consumption, 52_LVBus267976_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  286 group(s) of loads (572 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (3 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  349 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1153094_consumption, 52_LVBus1153094_production, 52_LVBus1153095_consumption, 52_LVBus1153095_production, 52_LVBus1155391_consumption, 52_LVBus1155391_production, 52_LVBus1155392_consumption, 52_LVBus1155392_production, 52_LVBus1156149_consumption, 52_LVBus1156149_production, 52_LVBus1156659_consumption, 52_LVBus1156659_production, 52_LVBus1161141_consumption, 52_LVBus1161141_production, 52_LVBus1162803_consumption, 52_LVBus1162803_production, 52_LVBus1178832_consumption, 52_LVBus1178832_production, 52_LVBus1180281_consumption, 52_LVBus1180281_production, 52_LVBus1181075_consumption, 52_LVBus1181075_production, 52_LVBus1181076_production, 52_LVBus1182374_consumption, 52_LVBus1182374_production, 52_LVBus1183080_production, 52_LVBus1185395_consumption, 52_LVBus1185395_production, 52_LVBus1188640_consumption, 52_LVBus1188640_production, 52_LVBus267642_consumption, 52_LVBus267642_production, 52_LVBus267644_consumption, 52_LVBus267644_production, 52_LVBus267646_consumption, 52_LVBus267646_production, 52_LVBus267648_consumption, 52_LVBus267648_production, 52_LVBus267650_production, 52_LVBus267651_consumption, 52_LVBus267651_production, 52_LVBus267654_production, 52_LVBus267655_production, 52_LVBus267656_production, 52_LVBus267657_production, 52_LVBus267658_production, 52_LVBus267659_production, 52_LVBus267660_production, 52_LVBus267662_production, 52_LVBus267663_production, 52_LVBus267664_production, 52_LVBus267665_production, 52_LVBus267667_production, 52_LVBus267668_production, 52_LVBus267669_production, 52_LVBus267671_consumption, 52_LVBus267671_production, 52_LVBus267672_consumption, 52_LVBus267672_production, 52_LVBus267673_production, 52_LVBus267674_production, 52_LVBus267676_production, 52_LVBus267677_production, 52_LVBus267678_production, 52_LVBus267679_consumption, 52_LVBus267679_production, 52_LVBus267680_consumption, 52_LVBus267680_production, 52_LVBus267681_production, 52_LVBus267682_production, 52_LVBus267683_production, 52_LVBus267684_production, 52_LVBus267685_production, 52_LVBus267686_production, 52_LVBus267687_production, 52_LVBus267688_production, 52_LVBus267690_production, 52_LVBus267691_production, 52_LVBus267693_production, 52_LVBus267694_production, 52_LVBus267695_production, 52_LVBus267696_production, 52_LVBus267697_production, 52_LVBus267699_consumption, 52_LVBus267699_production, 52_LVBus267700_production, 52_LVBus267701_production, 52_LVBus267702_production, 52_LVBus267703_production, 52_LVBus267704_production, 52_LVBus267705_production, 52_LVBus267706_production, 52_LVBus267707_production, 52_LVBus267708_production, 52_LVBus267709_production, 52_LVBus267710_production, 52_LVBus267713_production, 52_LVBus267714_production, 52_LVBus267715_production, 52_LVBus267716_production, 52_LVBus267718_production, 52_LVBus267719_production, 52_LVBus267720_production, 52_LVBus267721_production, 52_LVBus267722_production, 52_LVBus267724_consumption, 52_LVBus267724_production, 52_LVBus267725_consumption, 52_LVBus267725_production, 52_LVBus267726_consumption, 52_LVBus267726_production, 52_LVBus267727_production, 52_LVBus267728_production, 52_LVBus267729_consumption, 52_LVBus267729_production, 52_LVBus267730_consumption, 52_LVBus267730_production, 52_LVBus267731_production, 52_LVBus267732_production, 52_LVBus267733_production, 52_LVBus267734_consumption, 52_LVBus267734_production, 52_LVBus267735_consumption, 52_LVBus267735_production, 52_LVBus267736_consumption, 52_LVBus267736_production, 52_LVBus267738_consumption, 52_LVBus267738_production, 52_LVBus267740_production, 52_LVBus267741_production, 52_LVBus267743_production, 52_LVBus267744_production, 52_LVBus267745_production, 52_LVBus267746_production, 52_LVBus267748_production, 52_LVBus267749_production, 52_LVBus267750_production, 52_LVBus267751_production, 52_LVBus267752_production, 52_LVBus267754_production, 52_LVBus267756_production, 52_LVBus267757_production, 52_LVBus267758_production, 52_LVBus267759_production, 52_LVBus267760_production, 52_LVBus267761_production, 52_LVBus267763_production, 52_LVBus267765_production, 52_LVBus267766_production, 52_LVBus267767_production, 52_LVBus267768_production, 52_LVBus267770_production, 52_LVBus267771_production, 52_LVBus267772_production, 52_LVBus267773_production, 52_LVBus267775_production, 52_LVBus267776_production, 52_LVBus267777_production, 52_LVBus267778_production, 52_LVBus267779_production, 52_LVBus267781_consumption, 52_LVBus267781_production, 52_LVBus267783_consumption, 52_LVBus267783_production, 52_LVBus267784_production, 52_LVBus267786_production, 52_LVBus267787_production, 52_LVBus267789_production, 52_LVBus267790_production, 52_LVBus267792_production, 52_LVBus267793_production, 52_LVBus267794_production, 52_LVBus267795_production, 52_LVBus267796_production, 52_LVBus267797_production, 52_LVBus267798_production, 52_LVBus267799_production, 52_LVBus267800_production, 52_LVBus267801_production, 52_LVBus267803_production, 52_LVBus267804_consumption, 52_LVBus267804_production, 52_LVBus267805_consumption, 52_LVBus267805_production, 52_LVBus267806_consumption, 52_LVBus267806_production, 52_LVBus267807_consumption, 52_LVBus267807_production, 52_LVBus267808_production, 52_LVBus267809_production, 52_LVBus267810_production, 52_LVBus267811_production, 52_LVBus267812_production, 52_LVBus267813_production, 52_LVBus267815_production, 52_LVBus267816_production, 52_LVBus267817_production, 52_LVBus267818_production, 52_LVBus267819_production, 52_LVBus267821_production, 52_LVBus267822_production, 52_LVBus267823_production, 52_LVBus267824_production, 52_LVBus267826_production, 52_LVBus267827_production, 52_LVBus267828_production, 52_LVBus267829_production, 52_LVBus267830_production, 52_LVBus267831_production, 52_LVBus267834_production, 52_LVBus267835_production, 52_LVBus267837_production, 52_LVBus267838_production, 52_LVBus267839_production, 52_LVBus267840_production, 52_LVBus267841_production, 52_LVBus267842_production, 52_LVBus267844_production, 52_LVBus267845_production, 52_LVBus267846_production, 52_LVBus267848_production, 52_LVBus267849_production, 52_LVBus267850_production, 52_LVBus267852_production, 52_LVBus267853_production, 52_LVBus267854_production, 52_LVBus267855_production, 52_LVBus267856_production, 52_LVBus267857_production, 52_LVBus267859_production, 52_LVBus267861_production, 52_LVBus267862_production, 52_LVBus267863_production, 52_LVBus267864_production, 52_LVBus267865_production, 52_LVBus267866_production, 52_LVBus267868_production, 52_LVBus267869_production, 52_LVBus267870_production, 52_LVBus267871_production, 52_LVBus267872_production, 52_LVBus267873_production, 52_LVBus267874_production, 52_LVBus267876_production, 52_LVBus267878_consumption, 52_LVBus267878_production, 52_LVBus267879_production, 52_LVBus267880_production, 52_LVBus267881_consumption, 52_LVBus267881_production, 52_LVBus267882_production, 52_LVBus267883_production, 52_LVBus267884_production, 52_LVBus267885_production, 52_LVBus267886_production, 52_LVBus267888_consumption, 52_LVBus267888_production, 52_LVBus267889_consumption, 52_LVBus267889_production, 52_LVBus267890_production, 52_LVBus267891_production, 52_LVBus267892_production, 52_LVBus267893_production, 52_LVBus267894_production, 52_LVBus267895_production, 52_LVBus267897_production, 52_LVBus267898_production, 52_LVBus267899_production, 52_LVBus267900_production, 52_LVBus267901_production, 52_LVBus267903_production, 52_LVBus267904_production, 52_LVBus267905_production, 52_LVBus267906_consumption, 52_LVBus267906_production, 52_LVBus267907_production, 52_LVBus267909_production, 52_LVBus267910_production, 52_LVBus267912_production, 52_LVBus267913_consumption, 52_LVBus267913_production, 52_LVBus267914_production, 52_LVBus267916_production, 52_LVBus267917_consumption, 52_LVBus267917_production, 52_LVBus267918_production, 52_LVBus267920_consumption, 52_LVBus267920_production, 52_LVBus267922_consumption, 52_LVBus267922_production, 52_LVBus267924_production, 52_LVBus267926_production, 52_LVBus267928_production, 52_LVBus267929_production, 52_LVBus267932_production, 52_LVBus267933_consumption, 52_LVBus267933_production, 52_LVBus267935_consumption, 52_LVBus267935_production, 52_LVBus267936_production, 52_LVBus267937_consumption, 52_LVBus267937_production, 52_LVBus267938_production, 52_LVBus267940_consumption, 52_LVBus267940_production, 52_LVBus267941_consumption, 52_LVBus267941_production, 52_LVBus267942_production, 52_LVBus267943_consumption, 52_LVBus267943_production, 52_LVBus267944_consumption, 52_LVBus267944_production, 52_LVBus267945_production, 52_LVBus267946_consumption, 52_LVBus267946_production, 52_LVBus267947_production, 52_LVBus267949_consumption, 52_LVBus267949_production, 52_LVBus267950_production, 52_LVBus267951_production, 52_LVBus267952_consumption, 52_LVBus267952_production, 52_LVBus267953_consumption, 52_LVBus267953_production, 52_LVBus267954_production, 52_LVBus267955_production, 52_LVBus267957_production, 52_LVBus267960_production, 52_LVBus267962_production, 52_LVBus267963_production, 52_LVBus267965_production, 52_LVBus267966_production, 52_LVBus267967_production, 52_LVBus267969_production, 52_LVBus267970_production, 52_LVBus267971_production, 52_LVBus267973_production, 52_LVBus267974_consumption, 52_LVBus267974_production, 52_LVBus267975_production, 52_LVBus267976_production, 52_LVBus267977_consumption, 52_LVBus267977_production, 52_MVLV000332_consumption, 52_MVLV000332_production, 52_MVLV000458_production, 52_MVLV062038_consumption, 52_MVLV062038_production, 52_MVLV102220_production.

