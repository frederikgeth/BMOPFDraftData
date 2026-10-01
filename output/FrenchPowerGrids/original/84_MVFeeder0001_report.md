# BMOPF Network Summary: 84_MVFeeder0001

**Generated:** 2026-10-01 23:34:37  
**Findings:** 0 errors · 4 warnings · 400 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 18 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 562 |  |
| line | 543 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 1050 | 3.033 MW, 910.0 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 18 |  |
| switch | 0 |  |
| transformer | 18 | Dyn11×18 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 27 | 26 | 16 | 0 |
| LV_236V | 236.0 V | 535 | 517 | 1034 | 0 |

**Transformer transitions:**

- `84_MVLV025760_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV082836_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV024712_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV108164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV120020_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV063491_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV117616_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV102494_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV024713_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV054197_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV151212_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV104930_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV140203_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV125604_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV021209_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV063492_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV121479_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV151246_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 181 |
| Tree depth (max hops) | 34 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 562 | 1 | 561 | 0 | 0 | 0 |
| Tier LV_236V | 535 | 18 | 517 | 0 | 0 | 0 |
| Tier MV_11.8kV | 27 | 1 | 26 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 18; skipped invalid branches: 0.

Galvanic zones: 19; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_A.BAI | MV_11.8kV | 27 | 0 | 0 | 18 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2221 declared bus terminals; 2146 mapped line/closed-switch conductor edges; 75 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 34000.0 | 3.035 | 3150 |
| q_nom | 0.0 | 10200.0 | 3.035 | 3150 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.42 | 947.0 | 1.42 | 543 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 693000.0 | 0.294 | 18 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 632 of 1050 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2196707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594144_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593860_consumption' has phase imbalance of 127.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594153_consumption' has phase imbalance of 256.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593938_consumption' has phase imbalance of 224.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594035_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593831_consumption' has phase imbalance of 121.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593766_consumption' has phase imbalance of 195.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594105_consumption' has phase imbalance of 284.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593743_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594116_consumption' has phase imbalance of 148.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593993_consumption' has phase imbalance of 263.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594093_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593681_consumption' has phase imbalance of 89.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2205273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593837_consumption' has phase imbalance of 225.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593692_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593676_consumption' has phase imbalance of 189.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593821_consumption' has phase imbalance of 122.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2139774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594089_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2139771_consumption' has phase imbalance of 278.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593942_consumption' has phase imbalance of 232.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593922_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593982_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594117_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594115_consumption' has phase imbalance of 260.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2221674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593857_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593921_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593937_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2100851_consumption' has phase imbalance of 248.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593709_consumption' has phase imbalance of 245.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593943_consumption' has phase imbalance of 51.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594154_consumption' has phase imbalance of 229.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593875_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594006_consumption' has phase imbalance of 289.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594052_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593913_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593998_consumption' has phase imbalance of 129.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593994_consumption' has phase imbalance of 50.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593828_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2139773_consumption' has phase imbalance of 88.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594004_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593698_consumption' has phase imbalance of 52.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593838_consumption' has phase imbalance of 196.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593843_consumption' has phase imbalance of 203.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593745_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594119_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593651_consumption' has phase imbalance of 260.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593635_consumption' has phase imbalance of 246.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593877_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593716_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593644_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594128_consumption' has phase imbalance of 198.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2143769_consumption' has phase imbalance of 176.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593904_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593986_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593996_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594014_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593751_consumption' has phase imbalance of 117.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593827_consumption' has phase imbalance of 122.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593829_consumption' has phase imbalance of 213.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593835_consumption' has phase imbalance of 257.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593974_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594048_consumption' has phase imbalance of 252.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593859_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123383_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593803_consumption' has phase imbalance of 224.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593823_consumption' has phase imbalance of 124.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593855_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593945_consumption' has phase imbalance of 59.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594132_consumption' has phase imbalance of 143.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593686_consumption' has phase imbalance of 61.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593796_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593881_consumption' has phase imbalance of 277.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593907_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593968_consumption' has phase imbalance of 111.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593777_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594122_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594030_consumption' has phase imbalance of 207.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593756_consumption' has phase imbalance of 217.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593805_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593953_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593924_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593784_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593675_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593868_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593984_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593850_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593658_consumption' has phase imbalance of 270.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593708_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594007_consumption' has phase imbalance of 109.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593682_consumption' has phase imbalance of 80.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593862_consumption' has phase imbalance of 264.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594143_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593638_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593957_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593746_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594096_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123384_consumption' has phase imbalance of 283.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593802_consumption' has phase imbalance of 219.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594047_consumption' has phase imbalance of 225.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593670_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593933_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594109_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593815_consumption' has phase imbalance of 217.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594027_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593761_consumption' has phase imbalance of 243.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593987_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594051_consumption' has phase imbalance of 226.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593700_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593864_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593707_consumption' has phase imbalance of 251.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593925_consumption' has phase imbalance of 229.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593919_consumption' has phase imbalance of 94.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594010_consumption' has phase imbalance of 74.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594083_consumption' has phase imbalance of 118.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594016_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594017_consumption' has phase imbalance of 215.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593872_consumption' has phase imbalance of 33.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593885_consumption' has phase imbalance of 229.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593879_consumption' has phase imbalance of 271.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594129_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123382_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593706_consumption' has phase imbalance of 77.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593876_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593655_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593951_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593916_consumption' has phase imbalance of 26.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593858_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593785_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594058_consumption' has phase imbalance of 106.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593787_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593941_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594152_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594065_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594042_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594092_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593939_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593947_consumption' has phase imbalance of 246.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593822_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2253897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594023_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594099_consumption' has phase imbalance of 136.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594064_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593897_consumption' has phase imbalance of 263.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593782_consumption' has phase imbalance of 239.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593960_consumption' has phase imbalance of 254.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593685_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593894_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593775_consumption' has phase imbalance of 114.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593934_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593910_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594068_consumption' has phase imbalance of 146.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593664_consumption' has phase imbalance of 124.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593954_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593901_consumption' has phase imbalance of 149.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2235373_consumption' has phase imbalance of 281.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594135_consumption' has phase imbalance of 153.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593970_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593865_consumption' has phase imbalance of 262.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593985_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593826_consumption' has phase imbalance of 167.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593955_consumption' has phase imbalance of 233.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593781_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593927_consumption' has phase imbalance of 106.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593786_consumption' has phase imbalance of 97.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2139770_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594045_consumption' has phase imbalance of 246.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593929_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594139_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593834_consumption' has phase imbalance of 243.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593980_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593936_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593663_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593971_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594028_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594098_consumption' has phase imbalance of 260.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594066_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593728_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593952_consumption' has phase imbalance of 280.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593699_consumption' has phase imbalance of 85.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593931_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593991_consumption' has phase imbalance of 247.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594120_consumption' has phase imbalance of 101.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593678_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593979_consumption' has phase imbalance of 65.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593637_consumption' has phase imbalance of 37.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2071790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2253896_consumption' has phase imbalance of 179.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593693_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2196708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593912_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594013_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593833_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593726_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2127736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594060_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593891_consumption' has phase imbalance of 139.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594101_consumption' has phase imbalance of 256.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593762_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593754_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593874_consumption' has phase imbalance of 203.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594112_consumption' has phase imbalance of 282.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593669_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594146_consumption' has phase imbalance of 77.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593886_consumption' has phase imbalance of 64.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594043_consumption' has phase imbalance of 223.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593814_consumption' has phase imbalance of 130.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593995_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2139776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593920_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593694_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593967_consumption' has phase imbalance of 139.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593992_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593789_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594155_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593884_consumption' has phase imbalance of 256.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594022_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593818_consumption' has phase imbalance of 280.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593691_consumption' has phase imbalance of 204.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593846_consumption' has phase imbalance of 44.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593892_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594040_consumption' has phase imbalance of 44.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594091_consumption' has phase imbalance of 96.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593806_consumption' has phase imbalance of 125.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593741_consumption' has phase imbalance of 205.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594094_consumption' has phase imbalance of 175.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593780_consumption' has phase imbalance of 146.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593990_consumption' has phase imbalance of 232.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593926_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593737_consumption' has phase imbalance of 22.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593935_consumption' has phase imbalance of 226.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593949_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594080_consumption' has phase imbalance of 165.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593715_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593824_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594059_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593976_consumption' has phase imbalance of 110.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594050_consumption' has phase imbalance of 90.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594087_consumption' has phase imbalance of 255.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594005_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593900_consumption' has phase imbalance of 96.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593752_consumption' has phase imbalance of 85.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594123_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593673_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594086_consumption' has phase imbalance of 238.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594134_consumption' has phase imbalance of 163.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593989_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593772_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593853_consumption' has phase imbalance of 103.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593899_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594108_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594025_consumption' has phase imbalance of 78.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594151_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593866_consumption' has phase imbalance of 88.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593662_consumption' has phase imbalance of 39.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593667_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593983_consumption' has phase imbalance of 47.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594057_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593905_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594012_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594011_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593679_consumption' has phase imbalance of 201.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593684_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593962_consumption' has phase imbalance of 120.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2115723_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593981_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593914_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593820_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1594056_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593944_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593839_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593722_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593948_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1593883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1050 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.033 MW |
| Total load Q | 910.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV025760_Transformer | 440.0 kVA | 30.6% |
| 84_MVLV082836_Transformer | 275.0 kVA | 36.0% |
| 84_MVLV024712_Transformer | 440.0 kVA | 38.1% |
| 84_MVLV108164_Transformer | 440.0 kVA | 38.1% |
| 84_MVLV120020_Transformer | 693.0 kVA | 54.5% |
| 84_MVLV063491_Transformer | 440.0 kVA | 42.7% |
| 84_MVLV117616_Transformer | 440.0 kVA | 31.5% |
| 84_MVLV102494_Transformer | 275.0 kVA | 36.9% |
| 84_MVLV024713_Transformer | 440.0 kVA | 32.8% |
| 84_MVLV054197_Transformer | 275.0 kVA | 28.1% |
| 84_MVLV151212_Transformer | 440.0 kVA | 39.7% |
| 84_MVLV104930_Transformer | 693.0 kVA | 28.3% |
| 84_MVLV140203_Transformer | 440.0 kVA | 36.9% |
| 84_MVLV125604_Transformer | 440.0 kVA | 22.1% |
| 84_MVLV021209_Transformer | 693.0 kVA | 30.8% |
| 84_MVLV063492_Transformer | 440.0 kVA | 37.8% |
| 84_MVLV121479_Transformer | 440.0 kVA | 54.9% |
| 84_MVLV151246_Transformer | 693.0 kVA | 46.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.03 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 562 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 562 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 18 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 27 |
| LV_236V | 4-wire | 535 / 535 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 535 |
| Neutral branches | 517 |
| Grounding points | 18 |
| Neutral sections | 18 |
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
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 49 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 50 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 19 |
| Islands without voltage reference | 0 |
| Line impedance spread | 292.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 535 / 27 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 633 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 633 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1593633_production, 84_LVBus1593634_production, 84_LVBus1593635_production, 84_LVBus1593637_production, 84_LVBus1593638_production, 84_LVBus1593639_production, 84_LVBus1593640_consumption, 84_LVBus1593640_production, 84_LVBus1593641_production, 84_LVBus1593642_production, 84_LVBus1593644_production, 84_LVBus1593646_production, 84_LVBus1593648_consumption, 84_LVBus1593648_production, 84_LVBus1593649_production, 84_LVBus1593650_production, 84_LVBus1593651_production, 84_LVBus1593652_production, 84_LVBus1593653_production, 84_LVBus1593654_production, 84_LVBus1593655_production, 84_LVBus1593656_production, 84_LVBus1593657_production, 84_LVBus1593658_production, 84_LVBus1593659_consumption, 84_LVBus1593659_production, 84_LVBus1593660_production, 84_LVBus1593661_consumption, 84_LVBus1593661_production, 84_LVBus1593662_production, 84_LVBus1593663_production, 84_LVBus1593664_production, 84_LVBus1593665_production, 84_LVBus1593666_production, 84_LVBus1593667_production, 84_LVBus1593669_production, 84_LVBus1593670_production, 84_LVBus1593671_production, 84_LVBus1593672_consumption, 84_LVBus1593672_production, 84_LVBus1593673_production, 84_LVBus1593674_production, 84_LVBus1593675_production, 84_LVBus1593676_production, 84_LVBus1593678_production, 84_LVBus1593679_production, 84_LVBus1593680_consumption, 84_LVBus1593680_production, 84_LVBus1593681_production, 84_LVBus1593682_production, 84_LVBus1593683_production, 84_LVBus1593684_production, 84_LVBus1593685_production, 84_LVBus1593686_production, 84_LVBus1593688_consumption, 84_LVBus1593688_production, 84_LVBus1593690_consumption, 84_LVBus1593690_production, 84_LVBus1593691_production, 84_LVBus1593692_production, 84_LVBus1593693_production, 84_LVBus1593694_production, 84_LVBus1593696_consumption, 84_LVBus1593696_production, 84_LVBus1593697_consumption, 84_LVBus1593697_production, 84_LVBus1593698_production, 84_LVBus1593699_production, 84_LVBus1593700_production, 84_LVBus1593701_consumption, 84_LVBus1593701_production, 84_LVBus1593702_consumption, 84_LVBus1593702_production, 84_LVBus1593703_consumption, 84_LVBus1593703_production, 84_LVBus1593704_consumption, 84_LVBus1593704_production, 84_LVBus1593705_consumption, 84_LVBus1593705_production, 84_LVBus1593706_production, 84_LVBus1593707_production, 84_LVBus1593708_production, 84_LVBus1593709_production, 84_LVBus1593710_production, 84_LVBus1593711_production, 84_LVBus1593713_production, 84_LVBus1593714_production, 84_LVBus1593715_production, 84_LVBus1593716_production, 84_LVBus1593717_production, 84_LVBus1593718_production, 84_LVBus1593719_production, 84_LVBus1593721_production, 84_LVBus1593722_production, 84_LVBus1593723_production, 84_LVBus1593725_production, 84_LVBus1593726_production, 84_LVBus1593727_production, 84_LVBus1593728_production, 84_LVBus1593730_production, 84_LVBus1593731_production, 84_LVBus1593732_production, 84_LVBus1593733_consumption, 84_LVBus1593733_production, 84_LVBus1593735_consumption, 84_LVBus1593735_production, 84_LVBus1593736_consumption, 84_LVBus1593736_production, 84_LVBus1593737_production, 84_LVBus1593738_consumption, 84_LVBus1593738_production, 84_LVBus1593739_consumption, 84_LVBus1593739_production, 84_LVBus1593740_consumption, 84_LVBus1593740_production, 84_LVBus1593741_production, 84_LVBus1593742_production, 84_LVBus1593743_production, 84_LVBus1593745_production, 84_LVBus1593746_production, 84_LVBus1593748_consumption, 84_LVBus1593748_production, 84_LVBus1593749_production, 84_LVBus1593751_production, 84_LVBus1593752_production, 84_LVBus1593754_production, 84_LVBus1593755_production, 84_LVBus1593756_production, 84_LVBus1593757_production, 84_LVBus1593758_production, 84_LVBus1593759_production, 84_LVBus1593761_production, 84_LVBus1593762_production, 84_LVBus1593763_consumption, 84_LVBus1593763_production, 84_LVBus1593764_consumption, 84_LVBus1593764_production, 84_LVBus1593765_production, 84_LVBus1593766_production, 84_LVBus1593768_production, 84_LVBus1593769_consumption, 84_LVBus1593769_production, 84_LVBus1593770_production, 84_LVBus1593771_production, 84_LVBus1593772_production, 84_LVBus1593773_production, 84_LVBus1593774_production, 84_LVBus1593775_production, 84_LVBus1593776_production, 84_LVBus1593777_production, 84_LVBus1593778_production, 84_LVBus1593779_production, 84_LVBus1593780_production, 84_LVBus1593781_production, 84_LVBus1593782_production, 84_LVBus1593784_production, 84_LVBus1593785_production, 84_LVBus1593786_production, 84_LVBus1593787_production, 84_LVBus1593788_consumption, 84_LVBus1593788_production, 84_LVBus1593789_production, 84_LVBus1593790_consumption, 84_LVBus1593790_production, 84_LVBus1593792_consumption, 84_LVBus1593792_production, 84_LVBus1593793_production, 84_LVBus1593794_production, 84_LVBus1593795_production, 84_LVBus1593796_production, 84_LVBus1593797_production, 84_LVBus1593798_consumption, 84_LVBus1593798_production, 84_LVBus1593799_consumption, 84_LVBus1593799_production, 84_LVBus1593800_consumption, 84_LVBus1593800_production, 84_LVBus1593801_consumption, 84_LVBus1593801_production, 84_LVBus1593802_production, 84_LVBus1593803_production, 84_LVBus1593804_consumption, 84_LVBus1593804_production, 84_LVBus1593805_production, 84_LVBus1593806_production, 84_LVBus1593807_production, 84_LVBus1593808_production, 84_LVBus1593809_production, 84_LVBus1593810_production, 84_LVBus1593812_consumption, 84_LVBus1593812_production, 84_LVBus1593813_production, 84_LVBus1593814_production, 84_LVBus1593815_production, 84_LVBus1593817_production, 84_LVBus1593818_production, 84_LVBus1593819_production, 84_LVBus1593820_production, 84_LVBus1593821_production, 84_LVBus1593822_production, 84_LVBus1593823_production, 84_LVBus1593824_production, 84_LVBus1593826_production, 84_LVBus1593827_production, 84_LVBus1593828_production, 84_LVBus1593829_production, 84_LVBus1593831_production, 84_LVBus1593833_production, 84_LVBus1593834_production, 84_LVBus1593835_production, 84_LVBus1593836_production, 84_LVBus1593837_production, 84_LVBus1593838_production, 84_LVBus1593839_production, 84_LVBus1593840_production, 84_LVBus1593841_production, 84_LVBus1593842_production, 84_LVBus1593843_production, 84_LVBus1593845_production, 84_LVBus1593846_production, 84_LVBus1593848_consumption, 84_LVBus1593848_production, 84_LVBus1593849_consumption, 84_LVBus1593849_production, 84_LVBus1593850_production, 84_LVBus1593852_production, 84_LVBus1593853_production, 84_LVBus1593854_production, 84_LVBus1593855_production, 84_LVBus1593857_production, 84_LVBus1593858_production, 84_LVBus1593859_production, 84_LVBus1593860_production, 84_LVBus1593861_production, 84_LVBus1593862_production, 84_LVBus1593863_production, 84_LVBus1593864_production, 84_LVBus1593865_production, 84_LVBus1593866_production, 84_LVBus1593867_production, 84_LVBus1593868_production, 84_LVBus1593871_consumption, 84_LVBus1593871_production, 84_LVBus1593872_production, 84_LVBus1593873_production, 84_LVBus1593874_production, 84_LVBus1593875_production, 84_LVBus1593876_production, 84_LVBus1593877_production, 84_LVBus1593878_production, 84_LVBus1593879_production, 84_LVBus1593880_production, 84_LVBus1593881_production, 84_LVBus1593883_production, 84_LVBus1593884_production, 84_LVBus1593885_production, 84_LVBus1593886_production, 84_LVBus1593887_consumption, 84_LVBus1593887_production, 84_LVBus1593888_consumption, 84_LVBus1593888_production, 84_LVBus1593890_consumption, 84_LVBus1593890_production, 84_LVBus1593891_production, 84_LVBus1593892_production, 84_LVBus1593894_production, 84_LVBus1593895_consumption, 84_LVBus1593895_production, 84_LVBus1593896_production, 84_LVBus1593897_production, 84_LVBus1593898_consumption, 84_LVBus1593898_production, 84_LVBus1593899_production, 84_LVBus1593900_production, 84_LVBus1593901_production, 84_LVBus1593903_consumption, 84_LVBus1593903_production, 84_LVBus1593904_production, 84_LVBus1593905_production, 84_LVBus1593906_production, 84_LVBus1593907_production, 84_LVBus1593909_consumption, 84_LVBus1593909_production, 84_LVBus1593910_production, 84_LVBus1593911_consumption, 84_LVBus1593911_production, 84_LVBus1593912_production, 84_LVBus1593913_production, 84_LVBus1593914_production, 84_LVBus1593915_production, 84_LVBus1593916_production, 84_LVBus1593917_consumption, 84_LVBus1593917_production, 84_LVBus1593918_consumption, 84_LVBus1593918_production, 84_LVBus1593919_production, 84_LVBus1593920_production, 84_LVBus1593921_production, 84_LVBus1593922_production, 84_LVBus1593924_production, 84_LVBus1593925_production, 84_LVBus1593926_production, 84_LVBus1593927_production, 84_LVBus1593928_production, 84_LVBus1593929_production, 84_LVBus1593931_production, 84_LVBus1593932_production, 84_LVBus1593933_production, 84_LVBus1593934_production, 84_LVBus1593935_production, 84_LVBus1593936_production, 84_LVBus1593937_production, 84_LVBus1593938_production, 84_LVBus1593939_production, 84_LVBus1593941_production, 84_LVBus1593942_production, 84_LVBus1593943_production, 84_LVBus1593944_production, 84_LVBus1593945_production, 84_LVBus1593947_production, 84_LVBus1593948_production, 84_LVBus1593949_production, 84_LVBus1593951_production, 84_LVBus1593952_production, 84_LVBus1593953_production, 84_LVBus1593954_production, 84_LVBus1593955_production, 84_LVBus1593957_production, 84_LVBus1593959_consumption, 84_LVBus1593959_production, 84_LVBus1593960_production, 84_LVBus1593962_production, 84_LVBus1593963_consumption, 84_LVBus1593963_production, 84_LVBus1593964_consumption, 84_LVBus1593964_production, 84_LVBus1593965_consumption, 84_LVBus1593965_production, 84_LVBus1593966_production, 84_LVBus1593967_production, 84_LVBus1593968_production, 84_LVBus1593970_production, 84_LVBus1593971_production, 84_LVBus1593973_production, 84_LVBus1593974_production, 84_LVBus1593975_production, 84_LVBus1593976_production, 84_LVBus1593977_consumption, 84_LVBus1593977_production, 84_LVBus1593978_consumption, 84_LVBus1593978_production, 84_LVBus1593979_production, 84_LVBus1593980_production, 84_LVBus1593981_production, 84_LVBus1593982_production, 84_LVBus1593983_production, 84_LVBus1593984_production, 84_LVBus1593985_production, 84_LVBus1593986_production, 84_LVBus1593987_production, 84_LVBus1593989_production, 84_LVBus1593990_production, 84_LVBus1593991_production, 84_LVBus1593992_production, 84_LVBus1593993_production, 84_LVBus1593994_production, 84_LVBus1593995_production, 84_LVBus1593996_production, 84_LVBus1593998_production, 84_LVBus1593999_production, 84_LVBus1594000_consumption, 84_LVBus1594000_production, 84_LVBus1594001_consumption, 84_LVBus1594001_production, 84_LVBus1594003_production, 84_LVBus1594004_production, 84_LVBus1594005_production, 84_LVBus1594006_production, 84_LVBus1594007_production, 84_LVBus1594009_production, 84_LVBus1594010_production, 84_LVBus1594011_production, 84_LVBus1594012_production, 84_LVBus1594013_production, 84_LVBus1594014_production, 84_LVBus1594016_production, 84_LVBus1594017_production, 84_LVBus1594018_production, 84_LVBus1594020_consumption, 84_LVBus1594020_production, 84_LVBus1594021_consumption, 84_LVBus1594021_production, 84_LVBus1594022_production, 84_LVBus1594023_production, 84_LVBus1594024_production, 84_LVBus1594025_production, 84_LVBus1594026_consumption, 84_LVBus1594026_production, 84_LVBus1594027_production, 84_LVBus1594028_production, 84_LVBus1594029_consumption, 84_LVBus1594029_production, 84_LVBus1594030_production, 84_LVBus1594031_production, 84_LVBus1594032_production, 84_LVBus1594033_production, 84_LVBus1594034_production, 84_LVBus1594035_production, 84_LVBus1594037_consumption, 84_LVBus1594037_production, 84_LVBus1594038_production, 84_LVBus1594039_consumption, 84_LVBus1594039_production, 84_LVBus1594040_production, 84_LVBus1594042_production, 84_LVBus1594043_production, 84_LVBus1594045_production, 84_LVBus1594046_production, 84_LVBus1594047_production, 84_LVBus1594048_production, 84_LVBus1594049_production, 84_LVBus1594050_production, 84_LVBus1594051_production, 84_LVBus1594052_production, 84_LVBus1594053_consumption, 84_LVBus1594053_production, 84_LVBus1594054_consumption, 84_LVBus1594054_production, 84_LVBus1594056_production, 84_LVBus1594057_production, 84_LVBus1594058_production, 84_LVBus1594059_production, 84_LVBus1594060_production, 84_LVBus1594061_production, 84_LVBus1594062_consumption, 84_LVBus1594062_production, 84_LVBus1594063_production, 84_LVBus1594064_production, 84_LVBus1594065_production, 84_LVBus1594066_production, 84_LVBus1594068_production, 84_LVBus1594070_production, 84_LVBus1594072_consumption, 84_LVBus1594072_production, 84_LVBus1594074_production, 84_LVBus1594076_production, 84_LVBus1594077_production, 84_LVBus1594078_production, 84_LVBus1594079_consumption, 84_LVBus1594079_production, 84_LVBus1594080_production, 84_LVBus1594081_production, 84_LVBus1594082_production, 84_LVBus1594083_production, 84_LVBus1594084_production, 84_LVBus1594085_production, 84_LVBus1594086_production, 84_LVBus1594087_production, 84_LVBus1594089_production, 84_LVBus1594091_production, 84_LVBus1594092_production, 84_LVBus1594093_production, 84_LVBus1594094_production, 84_LVBus1594095_consumption, 84_LVBus1594095_production, 84_LVBus1594096_production, 84_LVBus1594097_production, 84_LVBus1594098_production, 84_LVBus1594099_production, 84_LVBus1594100_production, 84_LVBus1594101_production, 84_LVBus1594102_production, 84_LVBus1594104_consumption, 84_LVBus1594104_production, 84_LVBus1594105_production, 84_LVBus1594106_production, 84_LVBus1594107_production, 84_LVBus1594108_production, 84_LVBus1594109_production, 84_LVBus1594111_consumption, 84_LVBus1594111_production, 84_LVBus1594112_production, 84_LVBus1594113_production, 84_LVBus1594115_production, 84_LVBus1594116_production, 84_LVBus1594117_production, 84_LVBus1594119_production, 84_LVBus1594120_production, 84_LVBus1594121_production, 84_LVBus1594122_production, 84_LVBus1594123_production, 84_LVBus1594124_production, 84_LVBus1594126_consumption, 84_LVBus1594126_production, 84_LVBus1594127_production, 84_LVBus1594128_production, 84_LVBus1594129_production, 84_LVBus1594130_production, 84_LVBus1594131_production, 84_LVBus1594132_production, 84_LVBus1594133_production, 84_LVBus1594134_production, 84_LVBus1594135_production, 84_LVBus1594137_consumption, 84_LVBus1594137_production, 84_LVBus1594138_consumption, 84_LVBus1594138_production, 84_LVBus1594139_production, 84_LVBus1594140_production, 84_LVBus1594142_production, 84_LVBus1594143_production, 84_LVBus1594144_production, 84_LVBus1594145_production, 84_LVBus1594146_production, 84_LVBus1594148_consumption, 84_LVBus1594148_production, 84_LVBus1594149_production, 84_LVBus1594151_production, 84_LVBus1594152_production, 84_LVBus1594153_production, 84_LVBus1594154_production, 84_LVBus1594155_production, 84_LVBus1594156_production, 84_LVBus1594158_consumption, 84_LVBus1594158_production, 84_LVBus1594160_consumption, 84_LVBus1594160_production, 84_LVBus1594161_consumption, 84_LVBus1594161_production, 84_LVBus1594162_production, 84_LVBus1594164_consumption, 84_LVBus1594164_production, 84_LVBus1594165_production, 84_LVBus1594167_consumption, 84_LVBus1594167_production, 84_LVBus1594168_production, 84_LVBus1594169_production, 84_LVBus1594171_production, 84_LVBus1594173_consumption, 84_LVBus1594173_production, 84_LVBus1594174_consumption, 84_LVBus1594174_production, 84_LVBus1594176_production, 84_LVBus1594178_production, 84_LVBus2021878_consumption, 84_LVBus2021878_production, 84_LVBus2037715_consumption, 84_LVBus2037715_production, 84_LVBus2037716_consumption, 84_LVBus2037716_production, 84_LVBus2071790_production, 84_LVBus2078923_production, 84_LVBus2090293_consumption, 84_LVBus2090293_production, 84_LVBus2090294_production, 84_LVBus2093850_consumption, 84_LVBus2093850_production, 84_LVBus2093851_consumption, 84_LVBus2093851_production, 84_LVBus2100851_production, 84_LVBus2115723_production, 84_LVBus2122339_consumption, 84_LVBus2122339_production, 84_LVBus2122340_consumption, 84_LVBus2122340_production, 84_LVBus2123381_consumption, 84_LVBus2123381_production, 84_LVBus2123382_production, 84_LVBus2123383_production, 84_LVBus2123384_production, 84_LVBus2123385_production, 84_LVBus2123386_production, 84_LVBus2123387_production, 84_LVBus2123388_production, 84_LVBus2123389_production, 84_LVBus2127736_production, 84_LVBus2127737_consumption, 84_LVBus2127737_production, 84_LVBus2139768_production, 84_LVBus2139769_production, 84_LVBus2139770_production, 84_LVBus2139771_production, 84_LVBus2139772_consumption, 84_LVBus2139772_production, 84_LVBus2139773_production, 84_LVBus2139774_production, 84_LVBus2139775_consumption, 84_LVBus2139775_production, 84_LVBus2139776_production, 84_LVBus2139777_production, 84_LVBus2143769_production, 84_LVBus2162104_consumption, 84_LVBus2162104_production, 84_LVBus2196706_consumption, 84_LVBus2196706_production, 84_LVBus2196707_production, 84_LVBus2196708_production, 84_LVBus2205273_production, 84_LVBus2211803_consumption, 84_LVBus2211803_production, 84_LVBus2221673_production, 84_LVBus2221674_production, 84_LVBus2221675_production, 84_LVBus2235373_production, 84_LVBus2244605_consumption, 84_LVBus2244605_production, 84_LVBus2253895_consumption, 84_LVBus2253895_production, 84_LVBus2253896_production, 84_LVBus2253897_production, 84_LVBus2253898_consumption, 84_LVBus2253898_production, 84_LVBus2262545_consumption, 84_LVBus2262545_production, 84_LVBus2262546_production, 84_LVBus2262547_consumption, 84_LVBus2262547_production, 84_MVLV000240_consumption, 84_MVLV000240_production, 84_MVLV049724_consumption, 84_MVLV049724_production, 84_MVLV049750_consumption, 84_MVLV049750_production, 84_MVLV059885_consumption, 84_MVLV059885_production, 84_MVLV084113_consumption, 84_MVLV084113_production, 84_MVLV098132_consumption, 84_MVLV098132_production, 84_MVLV127696_consumption, 84_MVLV127696_production, 84_MVLV142140_consumption, 84_MVLV142140_production.

## 9. Data Quality Summary

**Total findings:** 404 (0 errors, 4 warnings, 400 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  632 of 1050 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.03 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  633 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2196707_consumption`  
  Load '84_LVBus2196707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594144_consumption`  
  Load '84_LVBus1594144_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593860_consumption`  
  Load '84_LVBus1593860_consumption' has phase imbalance of 127.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594153_consumption`  
  Load '84_LVBus1594153_consumption' has phase imbalance of 256.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593938_consumption`  
  Load '84_LVBus1593938_consumption' has phase imbalance of 224.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593654_consumption`  
  Load '84_LVBus1593654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594003_consumption`  
  Load '84_LVBus1594003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594035_consumption`  
  Load '84_LVBus1594035_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593831_consumption`  
  Load '84_LVBus1593831_consumption' has phase imbalance of 121.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593766_consumption`  
  Load '84_LVBus1593766_consumption' has phase imbalance of 195.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593634_consumption`  
  Load '84_LVBus1593634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123387_consumption`  
  Load '84_LVBus2123387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594105_consumption`  
  Load '84_LVBus1594105_consumption' has phase imbalance of 284.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593743_consumption`  
  Load '84_LVBus1593743_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594140_consumption`  
  Load '84_LVBus1594140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594116_consumption`  
  Load '84_LVBus1594116_consumption' has phase imbalance of 148.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593993_consumption`  
  Load '84_LVBus1593993_consumption' has phase imbalance of 263.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594093_consumption`  
  Load '84_LVBus1594093_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593681_consumption`  
  Load '84_LVBus1593681_consumption' has phase imbalance of 89.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2205273_consumption`  
  Load '84_LVBus2205273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593837_consumption`  
  Load '84_LVBus1593837_consumption' has phase imbalance of 225.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593692_consumption`  
  Load '84_LVBus1593692_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593676_consumption`  
  Load '84_LVBus1593676_consumption' has phase imbalance of 189.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593821_consumption`  
  Load '84_LVBus1593821_consumption' has phase imbalance of 122.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2139774_consumption`  
  Load '84_LVBus2139774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594089_consumption`  
  Load '84_LVBus1594089_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2139771_consumption`  
  Load '84_LVBus2139771_consumption' has phase imbalance of 278.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593942_consumption`  
  Load '84_LVBus1593942_consumption' has phase imbalance of 232.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593922_consumption`  
  Load '84_LVBus1593922_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593982_consumption`  
  Load '84_LVBus1593982_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593727_consumption`  
  Load '84_LVBus1593727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594117_consumption`  
  Load '84_LVBus1594117_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594115_consumption`  
  Load '84_LVBus1594115_consumption' has phase imbalance of 260.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593650_consumption`  
  Load '84_LVBus1593650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2221674_consumption`  
  Load '84_LVBus2221674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593794_consumption`  
  Load '84_LVBus1593794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593857_consumption`  
  Load '84_LVBus1593857_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593921_consumption`  
  Load '84_LVBus1593921_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593937_consumption`  
  Load '84_LVBus1593937_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2100851_consumption`  
  Load '84_LVBus2100851_consumption' has phase imbalance of 248.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593709_consumption`  
  Load '84_LVBus1593709_consumption' has phase imbalance of 245.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594133_consumption`  
  Load '84_LVBus1594133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593943_consumption`  
  Load '84_LVBus1593943_consumption' has phase imbalance of 51.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594154_consumption`  
  Load '84_LVBus1594154_consumption' has phase imbalance of 229.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593875_consumption`  
  Load '84_LVBus1593875_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594107_consumption`  
  Load '84_LVBus1594107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594006_consumption`  
  Load '84_LVBus1594006_consumption' has phase imbalance of 289.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594052_consumption`  
  Load '84_LVBus1594052_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593913_consumption`  
  Load '84_LVBus1593913_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593998_consumption`  
  Load '84_LVBus1593998_consumption' has phase imbalance of 129.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593994_consumption`  
  Load '84_LVBus1593994_consumption' has phase imbalance of 50.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593828_consumption`  
  Load '84_LVBus1593828_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593732_consumption`  
  Load '84_LVBus1593732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594032_consumption`  
  Load '84_LVBus1594032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2139773_consumption`  
  Load '84_LVBus2139773_consumption' has phase imbalance of 88.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594004_consumption`  
  Load '84_LVBus1594004_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593755_consumption`  
  Load '84_LVBus1593755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593810_consumption`  
  Load '84_LVBus1593810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593698_consumption`  
  Load '84_LVBus1593698_consumption' has phase imbalance of 52.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593813_consumption`  
  Load '84_LVBus1593813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593838_consumption`  
  Load '84_LVBus1593838_consumption' has phase imbalance of 196.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593843_consumption`  
  Load '84_LVBus1593843_consumption' has phase imbalance of 203.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593861_consumption`  
  Load '84_LVBus1593861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593745_consumption`  
  Load '84_LVBus1593745_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090294_consumption`  
  Load '84_LVBus2090294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594119_consumption`  
  Load '84_LVBus1594119_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594106_consumption`  
  Load '84_LVBus1594106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593651_consumption`  
  Load '84_LVBus1593651_consumption' has phase imbalance of 260.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593683_consumption`  
  Load '84_LVBus1593683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593635_consumption`  
  Load '84_LVBus1593635_consumption' has phase imbalance of 246.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593877_consumption`  
  Load '84_LVBus1593877_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593716_consumption`  
  Load '84_LVBus1593716_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593644_consumption`  
  Load '84_LVBus1593644_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593713_consumption`  
  Load '84_LVBus1593713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594128_consumption`  
  Load '84_LVBus1594128_consumption' has phase imbalance of 198.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2143769_consumption`  
  Load '84_LVBus2143769_consumption' has phase imbalance of 176.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593904_consumption`  
  Load '84_LVBus1593904_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593718_consumption`  
  Load '84_LVBus1593718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593986_consumption`  
  Load '84_LVBus1593986_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593996_consumption`  
  Load '84_LVBus1593996_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594014_consumption`  
  Load '84_LVBus1594014_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593793_consumption`  
  Load '84_LVBus1593793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593751_consumption`  
  Load '84_LVBus1593751_consumption' has phase imbalance of 117.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593730_consumption`  
  Load '84_LVBus1593730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593827_consumption`  
  Load '84_LVBus1593827_consumption' has phase imbalance of 122.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593973_consumption`  
  Load '84_LVBus1593973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593829_consumption`  
  Load '84_LVBus1593829_consumption' has phase imbalance of 213.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594168_consumption`  
  Load '84_LVBus1594168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593657_consumption`  
  Load '84_LVBus1593657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593835_consumption`  
  Load '84_LVBus1593835_consumption' has phase imbalance of 257.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593974_consumption`  
  Load '84_LVBus1593974_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594048_consumption`  
  Load '84_LVBus1594048_consumption' has phase imbalance of 252.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593859_consumption`  
  Load '84_LVBus1593859_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123383_consumption`  
  Load '84_LVBus2123383_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594078_consumption`  
  Load '84_LVBus1594078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593803_consumption`  
  Load '84_LVBus1593803_consumption' has phase imbalance of 224.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593823_consumption`  
  Load '84_LVBus1593823_consumption' has phase imbalance of 124.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593855_consumption`  
  Load '84_LVBus1593855_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593932_consumption`  
  Load '84_LVBus1593932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593945_consumption`  
  Load '84_LVBus1593945_consumption' has phase imbalance of 59.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594132_consumption`  
  Load '84_LVBus1594132_consumption' has phase imbalance of 143.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593686_consumption`  
  Load '84_LVBus1593686_consumption' has phase imbalance of 61.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593796_consumption`  
  Load '84_LVBus1593796_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593881_consumption`  
  Load '84_LVBus1593881_consumption' has phase imbalance of 277.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594130_consumption`  
  Load '84_LVBus1594130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593907_consumption`  
  Load '84_LVBus1593907_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593758_consumption`  
  Load '84_LVBus1593758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593968_consumption`  
  Load '84_LVBus1593968_consumption' has phase imbalance of 111.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593777_consumption`  
  Load '84_LVBus1593777_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594122_consumption`  
  Load '84_LVBus1594122_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594030_consumption`  
  Load '84_LVBus1594030_consumption' has phase imbalance of 207.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593867_consumption`  
  Load '84_LVBus1593867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593756_consumption`  
  Load '84_LVBus1593756_consumption' has phase imbalance of 217.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593805_consumption`  
  Load '84_LVBus1593805_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593953_consumption`  
  Load '84_LVBus1593953_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593770_consumption`  
  Load '84_LVBus1593770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593924_consumption`  
  Load '84_LVBus1593924_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593784_consumption`  
  Load '84_LVBus1593784_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593675_consumption`  
  Load '84_LVBus1593675_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593868_consumption`  
  Load '84_LVBus1593868_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593984_consumption`  
  Load '84_LVBus1593984_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593850_consumption`  
  Load '84_LVBus1593850_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593658_consumption`  
  Load '84_LVBus1593658_consumption' has phase imbalance of 270.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593840_consumption`  
  Load '84_LVBus1593840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594145_consumption`  
  Load '84_LVBus1594145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593708_consumption`  
  Load '84_LVBus1593708_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593852_consumption`  
  Load '84_LVBus1593852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594007_consumption`  
  Load '84_LVBus1594007_consumption' has phase imbalance of 109.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593682_consumption`  
  Load '84_LVBus1593682_consumption' has phase imbalance of 80.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123385_consumption`  
  Load '84_LVBus2123385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593966_consumption`  
  Load '84_LVBus1593966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593862_consumption`  
  Load '84_LVBus1593862_consumption' has phase imbalance of 264.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594143_consumption`  
  Load '84_LVBus1594143_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593638_consumption`  
  Load '84_LVBus1593638_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593957_consumption`  
  Load '84_LVBus1593957_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594024_consumption`  
  Load '84_LVBus1594024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593639_consumption`  
  Load '84_LVBus1593639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593746_consumption`  
  Load '84_LVBus1593746_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594096_consumption`  
  Load '84_LVBus1594096_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593671_consumption`  
  Load '84_LVBus1593671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593999_consumption`  
  Load '84_LVBus1593999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123384_consumption`  
  Load '84_LVBus2123384_consumption' has phase imbalance of 283.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593802_consumption`  
  Load '84_LVBus1593802_consumption' has phase imbalance of 219.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594142_consumption`  
  Load '84_LVBus1594142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593808_consumption`  
  Load '84_LVBus1593808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594047_consumption`  
  Load '84_LVBus1594047_consumption' has phase imbalance of 225.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593670_consumption`  
  Load '84_LVBus1593670_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593933_consumption`  
  Load '84_LVBus1593933_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594109_consumption`  
  Load '84_LVBus1594109_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593815_consumption`  
  Load '84_LVBus1593815_consumption' has phase imbalance of 217.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594027_consumption`  
  Load '84_LVBus1594027_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594084_consumption`  
  Load '84_LVBus1594084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594102_consumption`  
  Load '84_LVBus1594102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594046_consumption`  
  Load '84_LVBus1594046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593765_consumption`  
  Load '84_LVBus1593765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593761_consumption`  
  Load '84_LVBus1593761_consumption' has phase imbalance of 243.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593714_consumption`  
  Load '84_LVBus1593714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593987_consumption`  
  Load '84_LVBus1593987_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594051_consumption`  
  Load '84_LVBus1594051_consumption' has phase imbalance of 226.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593700_consumption`  
  Load '84_LVBus1593700_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594124_consumption`  
  Load '84_LVBus1594124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594061_consumption`  
  Load '84_LVBus1594061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593864_consumption`  
  Load '84_LVBus1593864_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593707_consumption`  
  Load '84_LVBus1593707_consumption' has phase imbalance of 251.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593925_consumption`  
  Load '84_LVBus1593925_consumption' has phase imbalance of 229.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594121_consumption`  
  Load '84_LVBus1594121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593919_consumption`  
  Load '84_LVBus1593919_consumption' has phase imbalance of 94.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593841_consumption`  
  Load '84_LVBus1593841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594010_consumption`  
  Load '84_LVBus1594010_consumption' has phase imbalance of 74.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593719_consumption`  
  Load '84_LVBus1593719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594083_consumption`  
  Load '84_LVBus1594083_consumption' has phase imbalance of 118.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594082_consumption`  
  Load '84_LVBus1594082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594016_consumption`  
  Load '84_LVBus1594016_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594017_consumption`  
  Load '84_LVBus1594017_consumption' has phase imbalance of 215.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593872_consumption`  
  Load '84_LVBus1593872_consumption' has phase imbalance of 33.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593885_consumption`  
  Load '84_LVBus1593885_consumption' has phase imbalance of 229.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593879_consumption`  
  Load '84_LVBus1593879_consumption' has phase imbalance of 271.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594129_consumption`  
  Load '84_LVBus1594129_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593928_consumption`  
  Load '84_LVBus1593928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123382_consumption`  
  Load '84_LVBus2123382_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593706_consumption`  
  Load '84_LVBus1593706_consumption' has phase imbalance of 77.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593876_consumption`  
  Load '84_LVBus1593876_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593655_consumption`  
  Load '84_LVBus1593655_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593951_consumption`  
  Load '84_LVBus1593951_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593916_consumption`  
  Load '84_LVBus1593916_consumption' has phase imbalance of 26.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593652_consumption`  
  Load '84_LVBus1593652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593858_consumption`  
  Load '84_LVBus1593858_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593785_consumption`  
  Load '84_LVBus1593785_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594058_consumption`  
  Load '84_LVBus1594058_consumption' has phase imbalance of 106.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593787_consumption`  
  Load '84_LVBus1593787_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593941_consumption`  
  Load '84_LVBus1593941_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594152_consumption`  
  Load '84_LVBus1594152_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594065_consumption`  
  Load '84_LVBus1594065_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594042_consumption`  
  Load '84_LVBus1594042_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594092_consumption`  
  Load '84_LVBus1594092_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593939_consumption`  
  Load '84_LVBus1593939_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593947_consumption`  
  Load '84_LVBus1593947_consumption' has phase imbalance of 246.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594156_consumption`  
  Load '84_LVBus1594156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593822_consumption`  
  Load '84_LVBus1593822_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2253897_consumption`  
  Load '84_LVBus2253897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594023_consumption`  
  Load '84_LVBus1594023_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594099_consumption`  
  Load '84_LVBus1594099_consumption' has phase imbalance of 136.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594064_consumption`  
  Load '84_LVBus1594064_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593897_consumption`  
  Load '84_LVBus1593897_consumption' has phase imbalance of 263.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593795_consumption`  
  Load '84_LVBus1593795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593782_consumption`  
  Load '84_LVBus1593782_consumption' has phase imbalance of 239.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593960_consumption`  
  Load '84_LVBus1593960_consumption' has phase imbalance of 254.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593685_consumption`  
  Load '84_LVBus1593685_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594034_consumption`  
  Load '84_LVBus1594034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593894_consumption`  
  Load '84_LVBus1593894_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593775_consumption`  
  Load '84_LVBus1593775_consumption' has phase imbalance of 114.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593934_consumption`  
  Load '84_LVBus1593934_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593711_consumption`  
  Load '84_LVBus1593711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593845_consumption`  
  Load '84_LVBus1593845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593819_consumption`  
  Load '84_LVBus1593819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593910_consumption`  
  Load '84_LVBus1593910_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594068_consumption`  
  Load '84_LVBus1594068_consumption' has phase imbalance of 146.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123386_consumption`  
  Load '84_LVBus2123386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593664_consumption`  
  Load '84_LVBus1593664_consumption' has phase imbalance of 124.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593759_consumption`  
  Load '84_LVBus1593759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593954_consumption`  
  Load '84_LVBus1593954_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593797_consumption`  
  Load '84_LVBus1593797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593901_consumption`  
  Load '84_LVBus1593901_consumption' has phase imbalance of 149.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2235373_consumption`  
  Load '84_LVBus2235373_consumption' has phase imbalance of 281.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594135_consumption`  
  Load '84_LVBus1594135_consumption' has phase imbalance of 153.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593970_consumption`  
  Load '84_LVBus1593970_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593768_consumption`  
  Load '84_LVBus1593768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593865_consumption`  
  Load '84_LVBus1593865_consumption' has phase imbalance of 262.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593985_consumption`  
  Load '84_LVBus1593985_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594085_consumption`  
  Load '84_LVBus1594085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593826_consumption`  
  Load '84_LVBus1593826_consumption' has phase imbalance of 167.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593955_consumption`  
  Load '84_LVBus1593955_consumption' has phase imbalance of 233.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593781_consumption`  
  Load '84_LVBus1593781_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593710_consumption`  
  Load '84_LVBus1593710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593927_consumption`  
  Load '84_LVBus1593927_consumption' has phase imbalance of 106.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593786_consumption`  
  Load '84_LVBus1593786_consumption' has phase imbalance of 97.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594076_consumption`  
  Load '84_LVBus1594076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593717_consumption`  
  Load '84_LVBus1593717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2139770_consumption`  
  Load '84_LVBus2139770_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594045_consumption`  
  Load '84_LVBus1594045_consumption' has phase imbalance of 246.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593929_consumption`  
  Load '84_LVBus1593929_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594139_consumption`  
  Load '84_LVBus1594139_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593834_consumption`  
  Load '84_LVBus1593834_consumption' has phase imbalance of 243.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593980_consumption`  
  Load '84_LVBus1593980_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593936_consumption`  
  Load '84_LVBus1593936_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593663_consumption`  
  Load '84_LVBus1593663_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593971_consumption`  
  Load '84_LVBus1593971_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594028_consumption`  
  Load '84_LVBus1594028_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593880_consumption`  
  Load '84_LVBus1593880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594098_consumption`  
  Load '84_LVBus1594098_consumption' has phase imbalance of 260.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594066_consumption`  
  Load '84_LVBus1594066_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593728_consumption`  
  Load '84_LVBus1593728_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593952_consumption`  
  Load '84_LVBus1593952_consumption' has phase imbalance of 280.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593699_consumption`  
  Load '84_LVBus1593699_consumption' has phase imbalance of 85.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593931_consumption`  
  Load '84_LVBus1593931_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594070_consumption`  
  Load '84_LVBus1594070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593991_consumption`  
  Load '84_LVBus1593991_consumption' has phase imbalance of 247.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594120_consumption`  
  Load '84_LVBus1594120_consumption' has phase imbalance of 101.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593678_consumption`  
  Load '84_LVBus1593678_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593656_consumption`  
  Load '84_LVBus1593656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593979_consumption`  
  Load '84_LVBus1593979_consumption' has phase imbalance of 65.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593637_consumption`  
  Load '84_LVBus1593637_consumption' has phase imbalance of 37.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2071790_consumption`  
  Load '84_LVBus2071790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2253896_consumption`  
  Load '84_LVBus2253896_consumption' has phase imbalance of 179.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593693_consumption`  
  Load '84_LVBus1593693_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593774_consumption`  
  Load '84_LVBus1593774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2196708_consumption`  
  Load '84_LVBus2196708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593912_consumption`  
  Load '84_LVBus1593912_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593807_consumption`  
  Load '84_LVBus1593807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593725_consumption`  
  Load '84_LVBus1593725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594013_consumption`  
  Load '84_LVBus1594013_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593749_consumption`  
  Load '84_LVBus1593749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593833_consumption`  
  Load '84_LVBus1593833_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593726_consumption`  
  Load '84_LVBus1593726_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2127736_consumption`  
  Load '84_LVBus2127736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594060_consumption`  
  Load '84_LVBus1594060_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593891_consumption`  
  Load '84_LVBus1593891_consumption' has phase imbalance of 139.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594101_consumption`  
  Load '84_LVBus1594101_consumption' has phase imbalance of 256.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594097_consumption`  
  Load '84_LVBus1594097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593762_consumption`  
  Load '84_LVBus1593762_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594074_consumption`  
  Load '84_LVBus1594074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593754_consumption`  
  Load '84_LVBus1593754_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593874_consumption`  
  Load '84_LVBus1593874_consumption' has phase imbalance of 203.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594112_consumption`  
  Load '84_LVBus1594112_consumption' has phase imbalance of 282.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593669_consumption`  
  Load '84_LVBus1593669_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594146_consumption`  
  Load '84_LVBus1594146_consumption' has phase imbalance of 77.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593886_consumption`  
  Load '84_LVBus1593886_consumption' has phase imbalance of 64.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594043_consumption`  
  Load '84_LVBus1594043_consumption' has phase imbalance of 223.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593814_consumption`  
  Load '84_LVBus1593814_consumption' has phase imbalance of 130.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593817_consumption`  
  Load '84_LVBus1593817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593995_consumption`  
  Load '84_LVBus1593995_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2139776_consumption`  
  Load '84_LVBus2139776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593920_consumption`  
  Load '84_LVBus1593920_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593742_consumption`  
  Load '84_LVBus1593742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593694_consumption`  
  Load '84_LVBus1593694_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593967_consumption`  
  Load '84_LVBus1593967_consumption' has phase imbalance of 139.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593992_consumption`  
  Load '84_LVBus1593992_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593789_consumption`  
  Load '84_LVBus1593789_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594063_consumption`  
  Load '84_LVBus1594063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594131_consumption`  
  Load '84_LVBus1594131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594155_consumption`  
  Load '84_LVBus1594155_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593884_consumption`  
  Load '84_LVBus1593884_consumption' has phase imbalance of 256.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593836_consumption`  
  Load '84_LVBus1593836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594022_consumption`  
  Load '84_LVBus1594022_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593818_consumption`  
  Load '84_LVBus1593818_consumption' has phase imbalance of 280.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593653_consumption`  
  Load '84_LVBus1593653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594127_consumption`  
  Load '84_LVBus1594127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593691_consumption`  
  Load '84_LVBus1593691_consumption' has phase imbalance of 204.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593846_consumption`  
  Load '84_LVBus1593846_consumption' has phase imbalance of 44.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593892_consumption`  
  Load '84_LVBus1593892_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593863_consumption`  
  Load '84_LVBus1593863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594113_consumption`  
  Load '84_LVBus1594113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594040_consumption`  
  Load '84_LVBus1594040_consumption' has phase imbalance of 44.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594091_consumption`  
  Load '84_LVBus1594091_consumption' has phase imbalance of 96.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593806_consumption`  
  Load '84_LVBus1593806_consumption' has phase imbalance of 125.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593741_consumption`  
  Load '84_LVBus1593741_consumption' has phase imbalance of 205.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594094_consumption`  
  Load '84_LVBus1594094_consumption' has phase imbalance of 175.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593780_consumption`  
  Load '84_LVBus1593780_consumption' has phase imbalance of 146.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593990_consumption`  
  Load '84_LVBus1593990_consumption' has phase imbalance of 232.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593926_consumption`  
  Load '84_LVBus1593926_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123388_consumption`  
  Load '84_LVBus2123388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593737_consumption`  
  Load '84_LVBus1593737_consumption' has phase imbalance of 22.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593935_consumption`  
  Load '84_LVBus1593935_consumption' has phase imbalance of 226.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594081_consumption`  
  Load '84_LVBus1594081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593949_consumption`  
  Load '84_LVBus1593949_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594080_consumption`  
  Load '84_LVBus1594080_consumption' has phase imbalance of 165.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593715_consumption`  
  Load '84_LVBus1593715_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593666_consumption`  
  Load '84_LVBus1593666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593824_consumption`  
  Load '84_LVBus1593824_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594059_consumption`  
  Load '84_LVBus1594059_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593976_consumption`  
  Load '84_LVBus1593976_consumption' has phase imbalance of 110.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593779_consumption`  
  Load '84_LVBus1593779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594050_consumption`  
  Load '84_LVBus1594050_consumption' has phase imbalance of 90.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594087_consumption`  
  Load '84_LVBus1594087_consumption' has phase imbalance of 255.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594005_consumption`  
  Load '84_LVBus1594005_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593900_consumption`  
  Load '84_LVBus1593900_consumption' has phase imbalance of 96.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593752_consumption`  
  Load '84_LVBus1593752_consumption' has phase imbalance of 85.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593633_consumption`  
  Load '84_LVBus1593633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594123_consumption`  
  Load '84_LVBus1594123_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593673_consumption`  
  Load '84_LVBus1593673_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594038_consumption`  
  Load '84_LVBus1594038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594086_consumption`  
  Load '84_LVBus1594086_consumption' has phase imbalance of 238.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593878_consumption`  
  Load '84_LVBus1593878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593771_consumption`  
  Load '84_LVBus1593771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593854_consumption`  
  Load '84_LVBus1593854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593975_consumption`  
  Load '84_LVBus1593975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594134_consumption`  
  Load '84_LVBus1594134_consumption' has phase imbalance of 163.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593989_consumption`  
  Load '84_LVBus1593989_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593772_consumption`  
  Load '84_LVBus1593772_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593853_consumption`  
  Load '84_LVBus1593853_consumption' has phase imbalance of 103.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593649_consumption`  
  Load '84_LVBus1593649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593899_consumption`  
  Load '84_LVBus1593899_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593776_consumption`  
  Load '84_LVBus1593776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594108_consumption`  
  Load '84_LVBus1594108_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594025_consumption`  
  Load '84_LVBus1594025_consumption' has phase imbalance of 78.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593674_consumption`  
  Load '84_LVBus1593674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594151_consumption`  
  Load '84_LVBus1594151_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593809_consumption`  
  Load '84_LVBus1593809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593866_consumption`  
  Load '84_LVBus1593866_consumption' has phase imbalance of 88.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593662_consumption`  
  Load '84_LVBus1593662_consumption' has phase imbalance of 39.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593842_consumption`  
  Load '84_LVBus1593842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593667_consumption`  
  Load '84_LVBus1593667_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593983_consumption`  
  Load '84_LVBus1593983_consumption' has phase imbalance of 47.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594100_consumption`  
  Load '84_LVBus1594100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594057_consumption`  
  Load '84_LVBus1594057_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593905_consumption`  
  Load '84_LVBus1593905_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594012_consumption`  
  Load '84_LVBus1594012_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594011_consumption`  
  Load '84_LVBus1594011_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593679_consumption`  
  Load '84_LVBus1593679_consumption' has phase imbalance of 201.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593684_consumption`  
  Load '84_LVBus1593684_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593660_consumption`  
  Load '84_LVBus1593660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593962_consumption`  
  Load '84_LVBus1593962_consumption' has phase imbalance of 120.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123389_consumption`  
  Load '84_LVBus2123389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594049_consumption`  
  Load '84_LVBus1594049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2115723_consumption`  
  Load '84_LVBus2115723_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594033_consumption`  
  Load '84_LVBus1594033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593778_consumption`  
  Load '84_LVBus1593778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593981_consumption`  
  Load '84_LVBus1593981_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593914_consumption`  
  Load '84_LVBus1593914_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593820_consumption`  
  Load '84_LVBus1593820_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1594056_consumption`  
  Load '84_LVBus1594056_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593944_consumption`  
  Load '84_LVBus1593944_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593839_consumption`  
  Load '84_LVBus1593839_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593722_consumption`  
  Load '84_LVBus1593722_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593948_consumption`  
  Load '84_LVBus1593948_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1593883_consumption`  
  Load '84_LVBus1593883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1050 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
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
  562 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  283 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus1593633_consumption, 84_LVBus1593634_consumption, 84_LVBus1593635_consumption, 84_LVBus1593638_consumption, 84_LVBus1593639_consumption, 84_LVBus1593644_consumption, 84_LVBus1593649_consumption, 84_LVBus1593650_consumption, 84_LVBus1593651_consumption, 84_LVBus1593652_consumption, 84_LVBus1593653_consumption, 84_LVBus1593654_consumption, 84_LVBus1593655_consumption, 84_LVBus1593656_consumption, 84_LVBus1593657_consumption, 84_LVBus1593658_consumption, 84_LVBus1593660_consumption, 84_LVBus1593663_consumption, 84_LVBus1593666_consumption, 84_LVBus1593667_consumption, 84_LVBus1593669_consumption, 84_LVBus1593670_consumption, 84_LVBus1593671_consumption, 84_LVBus1593674_consumption, 84_LVBus1593675_consumption, 84_LVBus1593676_consumption, 84_LVBus1593678_consumption, 84_LVBus1593679_consumption, 84_LVBus1593683_consumption, 84_LVBus1593684_consumption, 84_LVBus1593692_consumption, 84_LVBus1593707_consumption, 84_LVBus1593708_consumption, 84_LVBus1593709_consumption, 84_LVBus1593710_consumption, 84_LVBus1593711_consumption, 84_LVBus1593713_consumption, 84_LVBus1593714_consumption, 84_LVBus1593715_consumption, 84_LVBus1593716_consumption, 84_LVBus1593717_consumption, 84_LVBus1593718_consumption, 84_LVBus1593719_consumption, 84_LVBus1593722_consumption, 84_LVBus1593725_consumption, 84_LVBus1593726_consumption, 84_LVBus1593727_consumption, 84_LVBus1593730_consumption, 84_LVBus1593732_consumption, 84_LVBus1593741_consumption, 84_LVBus1593742_consumption, 84_LVBus1593743_consumption, 84_LVBus1593745_consumption, 84_LVBus1593749_consumption, 84_LVBus1593754_consumption, 84_LVBus1593755_consumption, 84_LVBus1593756_consumption, 84_LVBus1593758_consumption, 84_LVBus1593759_consumption, 84_LVBus1593761_consumption, 84_LVBus1593762_consumption, 84_LVBus1593765_consumption, 84_LVBus1593766_consumption, 84_LVBus1593768_consumption, 84_LVBus1593770_consumption, 84_LVBus1593771_consumption, 84_LVBus1593772_consumption, 84_LVBus1593774_consumption, 84_LVBus1593776_consumption, 84_LVBus1593778_consumption, 84_LVBus1593779_consumption, 84_LVBus1593781_consumption, 84_LVBus1593782_consumption, 84_LVBus1593785_consumption, 84_LVBus1593787_consumption, 84_LVBus1593789_consumption, 84_LVBus1593793_consumption, 84_LVBus1593794_consumption, 84_LVBus1593795_consumption, 84_LVBus1593796_consumption, 84_LVBus1593797_consumption, 84_LVBus1593802_consumption, 84_LVBus1593803_consumption, 84_LVBus1593805_consumption, 84_LVBus1593807_consumption, 84_LVBus1593808_consumption, 84_LVBus1593809_consumption, 84_LVBus1593810_consumption, 84_LVBus1593813_consumption, 84_LVBus1593815_consumption, 84_LVBus1593817_consumption, 84_LVBus1593818_consumption, 84_LVBus1593819_consumption, 84_LVBus1593820_consumption, 84_LVBus1593826_consumption, 84_LVBus1593829_consumption, 84_LVBus1593834_consumption, 84_LVBus1593835_consumption, 84_LVBus1593836_consumption, 84_LVBus1593837_consumption, 84_LVBus1593838_consumption, 84_LVBus1593839_consumption, 84_LVBus1593840_consumption, 84_LVBus1593841_consumption, 84_LVBus1593842_consumption, 84_LVBus1593843_consumption, 84_LVBus1593845_consumption, 84_LVBus1593850_consumption, 84_LVBus1593852_consumption, 84_LVBus1593854_consumption, 84_LVBus1593857_consumption, 84_LVBus1593858_consumption, 84_LVBus1593861_consumption, 84_LVBus1593862_consumption, 84_LVBus1593863_consumption, 84_LVBus1593864_consumption, 84_LVBus1593865_consumption, 84_LVBus1593867_consumption, 84_LVBus1593868_consumption, 84_LVBus1593874_consumption, 84_LVBus1593875_consumption, 84_LVBus1593876_consumption, 84_LVBus1593877_consumption, 84_LVBus1593878_consumption, 84_LVBus1593879_consumption, 84_LVBus1593880_consumption, 84_LVBus1593881_consumption, 84_LVBus1593883_consumption, 84_LVBus1593884_consumption, 84_LVBus1593885_consumption, 84_LVBus1593892_consumption, 84_LVBus1593894_consumption, 84_LVBus1593897_consumption, 84_LVBus1593899_consumption, 84_LVBus1593905_consumption, 84_LVBus1593910_consumption, 84_LVBus1593912_consumption, 84_LVBus1593913_consumption, 84_LVBus1593914_consumption, 84_LVBus1593921_consumption, 84_LVBus1593922_consumption, 84_LVBus1593924_consumption, 84_LVBus1593925_consumption, 84_LVBus1593928_consumption, 84_LVBus1593931_consumption, 84_LVBus1593932_consumption, 84_LVBus1593933_consumption, 84_LVBus1593935_consumption, 84_LVBus1593937_consumption, 84_LVBus1593938_consumption, 84_LVBus1593941_consumption, 84_LVBus1593942_consumption, 84_LVBus1593947_consumption, 84_LVBus1593952_consumption, 84_LVBus1593953_consumption, 84_LVBus1593954_consumption, 84_LVBus1593955_consumption, 84_LVBus1593957_consumption, 84_LVBus1593960_consumption, 84_LVBus1593966_consumption, 84_LVBus1593973_consumption, 84_LVBus1593974_consumption, 84_LVBus1593975_consumption, 84_LVBus1593980_consumption, 84_LVBus1593981_consumption, 84_LVBus1593982_consumption, 84_LVBus1593984_consumption, 84_LVBus1593985_consumption, 84_LVBus1593986_consumption, 84_LVBus1593987_consumption, 84_LVBus1593989_consumption, 84_LVBus1593990_consumption, 84_LVBus1593991_consumption, 84_LVBus1593992_consumption, 84_LVBus1593993_consumption, 84_LVBus1593995_consumption, 84_LVBus1593996_consumption, 84_LVBus1593999_consumption, 84_LVBus1594003_consumption, 84_LVBus1594004_consumption, 84_LVBus1594006_consumption, 84_LVBus1594011_consumption, 84_LVBus1594012_consumption, 84_LVBus1594013_consumption, 84_LVBus1594014_consumption, 84_LVBus1594016_consumption, 84_LVBus1594017_consumption, 84_LVBus1594024_consumption, 84_LVBus1594030_consumption, 84_LVBus1594032_consumption, 84_LVBus1594033_consumption, 84_LVBus1594034_consumption, 84_LVBus1594035_consumption, 84_LVBus1594038_consumption, 84_LVBus1594042_consumption, 84_LVBus1594043_consumption, 84_LVBus1594045_consumption, 84_LVBus1594046_consumption, 84_LVBus1594047_consumption, 84_LVBus1594048_consumption, 84_LVBus1594049_consumption, 84_LVBus1594052_consumption, 84_LVBus1594056_consumption, 84_LVBus1594059_consumption, 84_LVBus1594060_consumption, 84_LVBus1594061_consumption, 84_LVBus1594063_consumption, 84_LVBus1594064_consumption, 84_LVBus1594070_consumption, 84_LVBus1594074_consumption, 84_LVBus1594076_consumption, 84_LVBus1594078_consumption, 84_LVBus1594080_consumption, 84_LVBus1594081_consumption, 84_LVBus1594082_consumption, 84_LVBus1594084_consumption, 84_LVBus1594085_consumption, 84_LVBus1594086_consumption, 84_LVBus1594087_consumption, 84_LVBus1594089_consumption, 84_LVBus1594092_consumption, 84_LVBus1594093_consumption, 84_LVBus1594096_consumption, 84_LVBus1594097_consumption, 84_LVBus1594098_consumption, 84_LVBus1594100_consumption, 84_LVBus1594101_consumption, 84_LVBus1594102_consumption, 84_LVBus1594105_consumption, 84_LVBus1594106_consumption, 84_LVBus1594107_consumption, 84_LVBus1594108_consumption, 84_LVBus1594109_consumption, 84_LVBus1594112_consumption, 84_LVBus1594113_consumption, 84_LVBus1594115_consumption, 84_LVBus1594119_consumption, 84_LVBus1594121_consumption, 84_LVBus1594122_consumption, 84_LVBus1594123_consumption, 84_LVBus1594124_consumption, 84_LVBus1594127_consumption, 84_LVBus1594128_consumption, 84_LVBus1594129_consumption, 84_LVBus1594130_consumption, 84_LVBus1594131_consumption, 84_LVBus1594133_consumption, 84_LVBus1594134_consumption, 84_LVBus1594135_consumption, 84_LVBus1594139_consumption, 84_LVBus1594140_consumption, 84_LVBus1594142_consumption, 84_LVBus1594145_consumption, 84_LVBus1594151_consumption, 84_LVBus1594153_consumption, 84_LVBus1594154_consumption, 84_LVBus1594155_consumption, 84_LVBus1594156_consumption, 84_LVBus1594168_consumption, 84_LVBus2071790_consumption, 84_LVBus2090294_consumption, 84_LVBus2100851_consumption, 84_LVBus2115723_consumption, 84_LVBus2123383_consumption, 84_LVBus2123384_consumption, 84_LVBus2123385_consumption, 84_LVBus2123386_consumption, 84_LVBus2123387_consumption, 84_LVBus2123388_consumption, 84_LVBus2123389_consumption, 84_LVBus2127736_consumption, 84_LVBus2139770_consumption, 84_LVBus2139771_consumption, 84_LVBus2139774_consumption, 84_LVBus2139776_consumption, 84_LVBus2143769_consumption, 84_LVBus2196707_consumption, 84_LVBus2196708_consumption, 84_LVBus2205273_consumption, 84_LVBus2221674_consumption, 84_LVBus2235373_consumption, 84_LVBus2253896_consumption, 84_LVBus2253897_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  525 group(s) of loads (1050 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  633 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1593633_production, 84_LVBus1593634_production, 84_LVBus1593635_production, 84_LVBus1593637_production, 84_LVBus1593638_production, 84_LVBus1593639_production, 84_LVBus1593640_consumption, 84_LVBus1593640_production, 84_LVBus1593641_production, 84_LVBus1593642_production, 84_LVBus1593644_production, 84_LVBus1593646_production, 84_LVBus1593648_consumption, 84_LVBus1593648_production, 84_LVBus1593649_production, 84_LVBus1593650_production, 84_LVBus1593651_production, 84_LVBus1593652_production, 84_LVBus1593653_production, 84_LVBus1593654_production, 84_LVBus1593655_production, 84_LVBus1593656_production, 84_LVBus1593657_production, 84_LVBus1593658_production, 84_LVBus1593659_consumption, 84_LVBus1593659_production, 84_LVBus1593660_production, 84_LVBus1593661_consumption, 84_LVBus1593661_production, 84_LVBus1593662_production, 84_LVBus1593663_production, 84_LVBus1593664_production, 84_LVBus1593665_production, 84_LVBus1593666_production, 84_LVBus1593667_production, 84_LVBus1593669_production, 84_LVBus1593670_production, 84_LVBus1593671_production, 84_LVBus1593672_consumption, 84_LVBus1593672_production, 84_LVBus1593673_production, 84_LVBus1593674_production, 84_LVBus1593675_production, 84_LVBus1593676_production, 84_LVBus1593678_production, 84_LVBus1593679_production, 84_LVBus1593680_consumption, 84_LVBus1593680_production, 84_LVBus1593681_production, 84_LVBus1593682_production, 84_LVBus1593683_production, 84_LVBus1593684_production, 84_LVBus1593685_production, 84_LVBus1593686_production, 84_LVBus1593688_consumption, 84_LVBus1593688_production, 84_LVBus1593690_consumption, 84_LVBus1593690_production, 84_LVBus1593691_production, 84_LVBus1593692_production, 84_LVBus1593693_production, 84_LVBus1593694_production, 84_LVBus1593696_consumption, 84_LVBus1593696_production, 84_LVBus1593697_consumption, 84_LVBus1593697_production, 84_LVBus1593698_production, 84_LVBus1593699_production, 84_LVBus1593700_production, 84_LVBus1593701_consumption, 84_LVBus1593701_production, 84_LVBus1593702_consumption, 84_LVBus1593702_production, 84_LVBus1593703_consumption, 84_LVBus1593703_production, 84_LVBus1593704_consumption, 84_LVBus1593704_production, 84_LVBus1593705_consumption, 84_LVBus1593705_production, 84_LVBus1593706_production, 84_LVBus1593707_production, 84_LVBus1593708_production, 84_LVBus1593709_production, 84_LVBus1593710_production, 84_LVBus1593711_production, 84_LVBus1593713_production, 84_LVBus1593714_production, 84_LVBus1593715_production, 84_LVBus1593716_production, 84_LVBus1593717_production, 84_LVBus1593718_production, 84_LVBus1593719_production, 84_LVBus1593721_production, 84_LVBus1593722_production, 84_LVBus1593723_production, 84_LVBus1593725_production, 84_LVBus1593726_production, 84_LVBus1593727_production, 84_LVBus1593728_production, 84_LVBus1593730_production, 84_LVBus1593731_production, 84_LVBus1593732_production, 84_LVBus1593733_consumption, 84_LVBus1593733_production, 84_LVBus1593735_consumption, 84_LVBus1593735_production, 84_LVBus1593736_consumption, 84_LVBus1593736_production, 84_LVBus1593737_production, 84_LVBus1593738_consumption, 84_LVBus1593738_production, 84_LVBus1593739_consumption, 84_LVBus1593739_production, 84_LVBus1593740_consumption, 84_LVBus1593740_production, 84_LVBus1593741_production, 84_LVBus1593742_production, 84_LVBus1593743_production, 84_LVBus1593745_production, 84_LVBus1593746_production, 84_LVBus1593748_consumption, 84_LVBus1593748_production, 84_LVBus1593749_production, 84_LVBus1593751_production, 84_LVBus1593752_production, 84_LVBus1593754_production, 84_LVBus1593755_production, 84_LVBus1593756_production, 84_LVBus1593757_production, 84_LVBus1593758_production, 84_LVBus1593759_production, 84_LVBus1593761_production, 84_LVBus1593762_production, 84_LVBus1593763_consumption, 84_LVBus1593763_production, 84_LVBus1593764_consumption, 84_LVBus1593764_production, 84_LVBus1593765_production, 84_LVBus1593766_production, 84_LVBus1593768_production, 84_LVBus1593769_consumption, 84_LVBus1593769_production, 84_LVBus1593770_production, 84_LVBus1593771_production, 84_LVBus1593772_production, 84_LVBus1593773_production, 84_LVBus1593774_production, 84_LVBus1593775_production, 84_LVBus1593776_production, 84_LVBus1593777_production, 84_LVBus1593778_production, 84_LVBus1593779_production, 84_LVBus1593780_production, 84_LVBus1593781_production, 84_LVBus1593782_production, 84_LVBus1593784_production, 84_LVBus1593785_production, 84_LVBus1593786_production, 84_LVBus1593787_production, 84_LVBus1593788_consumption, 84_LVBus1593788_production, 84_LVBus1593789_production, 84_LVBus1593790_consumption, 84_LVBus1593790_production, 84_LVBus1593792_consumption, 84_LVBus1593792_production, 84_LVBus1593793_production, 84_LVBus1593794_production, 84_LVBus1593795_production, 84_LVBus1593796_production, 84_LVBus1593797_production, 84_LVBus1593798_consumption, 84_LVBus1593798_production, 84_LVBus1593799_consumption, 84_LVBus1593799_production, 84_LVBus1593800_consumption, 84_LVBus1593800_production, 84_LVBus1593801_consumption, 84_LVBus1593801_production, 84_LVBus1593802_production, 84_LVBus1593803_production, 84_LVBus1593804_consumption, 84_LVBus1593804_production, 84_LVBus1593805_production, 84_LVBus1593806_production, 84_LVBus1593807_production, 84_LVBus1593808_production, 84_LVBus1593809_production, 84_LVBus1593810_production, 84_LVBus1593812_consumption, 84_LVBus1593812_production, 84_LVBus1593813_production, 84_LVBus1593814_production, 84_LVBus1593815_production, 84_LVBus1593817_production, 84_LVBus1593818_production, 84_LVBus1593819_production, 84_LVBus1593820_production, 84_LVBus1593821_production, 84_LVBus1593822_production, 84_LVBus1593823_production, 84_LVBus1593824_production, 84_LVBus1593826_production, 84_LVBus1593827_production, 84_LVBus1593828_production, 84_LVBus1593829_production, 84_LVBus1593831_production, 84_LVBus1593833_production, 84_LVBus1593834_production, 84_LVBus1593835_production, 84_LVBus1593836_production, 84_LVBus1593837_production, 84_LVBus1593838_production, 84_LVBus1593839_production, 84_LVBus1593840_production, 84_LVBus1593841_production, 84_LVBus1593842_production, 84_LVBus1593843_production, 84_LVBus1593845_production, 84_LVBus1593846_production, 84_LVBus1593848_consumption, 84_LVBus1593848_production, 84_LVBus1593849_consumption, 84_LVBus1593849_production, 84_LVBus1593850_production, 84_LVBus1593852_production, 84_LVBus1593853_production, 84_LVBus1593854_production, 84_LVBus1593855_production, 84_LVBus1593857_production, 84_LVBus1593858_production, 84_LVBus1593859_production, 84_LVBus1593860_production, 84_LVBus1593861_production, 84_LVBus1593862_production, 84_LVBus1593863_production, 84_LVBus1593864_production, 84_LVBus1593865_production, 84_LVBus1593866_production, 84_LVBus1593867_production, 84_LVBus1593868_production, 84_LVBus1593871_consumption, 84_LVBus1593871_production, 84_LVBus1593872_production, 84_LVBus1593873_production, 84_LVBus1593874_production, 84_LVBus1593875_production, 84_LVBus1593876_production, 84_LVBus1593877_production, 84_LVBus1593878_production, 84_LVBus1593879_production, 84_LVBus1593880_production, 84_LVBus1593881_production, 84_LVBus1593883_production, 84_LVBus1593884_production, 84_LVBus1593885_production, 84_LVBus1593886_production, 84_LVBus1593887_consumption, 84_LVBus1593887_production, 84_LVBus1593888_consumption, 84_LVBus1593888_production, 84_LVBus1593890_consumption, 84_LVBus1593890_production, 84_LVBus1593891_production, 84_LVBus1593892_production, 84_LVBus1593894_production, 84_LVBus1593895_consumption, 84_LVBus1593895_production, 84_LVBus1593896_production, 84_LVBus1593897_production, 84_LVBus1593898_consumption, 84_LVBus1593898_production, 84_LVBus1593899_production, 84_LVBus1593900_production, 84_LVBus1593901_production, 84_LVBus1593903_consumption, 84_LVBus1593903_production, 84_LVBus1593904_production, 84_LVBus1593905_production, 84_LVBus1593906_production, 84_LVBus1593907_production, 84_LVBus1593909_consumption, 84_LVBus1593909_production, 84_LVBus1593910_production, 84_LVBus1593911_consumption, 84_LVBus1593911_production, 84_LVBus1593912_production, 84_LVBus1593913_production, 84_LVBus1593914_production, 84_LVBus1593915_production, 84_LVBus1593916_production, 84_LVBus1593917_consumption, 84_LVBus1593917_production, 84_LVBus1593918_consumption, 84_LVBus1593918_production, 84_LVBus1593919_production, 84_LVBus1593920_production, 84_LVBus1593921_production, 84_LVBus1593922_production, 84_LVBus1593924_production, 84_LVBus1593925_production, 84_LVBus1593926_production, 84_LVBus1593927_production, 84_LVBus1593928_production, 84_LVBus1593929_production, 84_LVBus1593931_production, 84_LVBus1593932_production, 84_LVBus1593933_production, 84_LVBus1593934_production, 84_LVBus1593935_production, 84_LVBus1593936_production, 84_LVBus1593937_production, 84_LVBus1593938_production, 84_LVBus1593939_production, 84_LVBus1593941_production, 84_LVBus1593942_production, 84_LVBus1593943_production, 84_LVBus1593944_production, 84_LVBus1593945_production, 84_LVBus1593947_production, 84_LVBus1593948_production, 84_LVBus1593949_production, 84_LVBus1593951_production, 84_LVBus1593952_production, 84_LVBus1593953_production, 84_LVBus1593954_production, 84_LVBus1593955_production, 84_LVBus1593957_production, 84_LVBus1593959_consumption, 84_LVBus1593959_production, 84_LVBus1593960_production, 84_LVBus1593962_production, 84_LVBus1593963_consumption, 84_LVBus1593963_production, 84_LVBus1593964_consumption, 84_LVBus1593964_production, 84_LVBus1593965_consumption, 84_LVBus1593965_production, 84_LVBus1593966_production, 84_LVBus1593967_production, 84_LVBus1593968_production, 84_LVBus1593970_production, 84_LVBus1593971_production, 84_LVBus1593973_production, 84_LVBus1593974_production, 84_LVBus1593975_production, 84_LVBus1593976_production, 84_LVBus1593977_consumption, 84_LVBus1593977_production, 84_LVBus1593978_consumption, 84_LVBus1593978_production, 84_LVBus1593979_production, 84_LVBus1593980_production, 84_LVBus1593981_production, 84_LVBus1593982_production, 84_LVBus1593983_production, 84_LVBus1593984_production, 84_LVBus1593985_production, 84_LVBus1593986_production, 84_LVBus1593987_production, 84_LVBus1593989_production, 84_LVBus1593990_production, 84_LVBus1593991_production, 84_LVBus1593992_production, 84_LVBus1593993_production, 84_LVBus1593994_production, 84_LVBus1593995_production, 84_LVBus1593996_production, 84_LVBus1593998_production, 84_LVBus1593999_production, 84_LVBus1594000_consumption, 84_LVBus1594000_production, 84_LVBus1594001_consumption, 84_LVBus1594001_production, 84_LVBus1594003_production, 84_LVBus1594004_production, 84_LVBus1594005_production, 84_LVBus1594006_production, 84_LVBus1594007_production, 84_LVBus1594009_production, 84_LVBus1594010_production, 84_LVBus1594011_production, 84_LVBus1594012_production, 84_LVBus1594013_production, 84_LVBus1594014_production, 84_LVBus1594016_production, 84_LVBus1594017_production, 84_LVBus1594018_production, 84_LVBus1594020_consumption, 84_LVBus1594020_production, 84_LVBus1594021_consumption, 84_LVBus1594021_production, 84_LVBus1594022_production, 84_LVBus1594023_production, 84_LVBus1594024_production, 84_LVBus1594025_production, 84_LVBus1594026_consumption, 84_LVBus1594026_production, 84_LVBus1594027_production, 84_LVBus1594028_production, 84_LVBus1594029_consumption, 84_LVBus1594029_production, 84_LVBus1594030_production, 84_LVBus1594031_production, 84_LVBus1594032_production, 84_LVBus1594033_production, 84_LVBus1594034_production, 84_LVBus1594035_production, 84_LVBus1594037_consumption, 84_LVBus1594037_production, 84_LVBus1594038_production, 84_LVBus1594039_consumption, 84_LVBus1594039_production, 84_LVBus1594040_production, 84_LVBus1594042_production, 84_LVBus1594043_production, 84_LVBus1594045_production, 84_LVBus1594046_production, 84_LVBus1594047_production, 84_LVBus1594048_production, 84_LVBus1594049_production, 84_LVBus1594050_production, 84_LVBus1594051_production, 84_LVBus1594052_production, 84_LVBus1594053_consumption, 84_LVBus1594053_production, 84_LVBus1594054_consumption, 84_LVBus1594054_production, 84_LVBus1594056_production, 84_LVBus1594057_production, 84_LVBus1594058_production, 84_LVBus1594059_production, 84_LVBus1594060_production, 84_LVBus1594061_production, 84_LVBus1594062_consumption, 84_LVBus1594062_production, 84_LVBus1594063_production, 84_LVBus1594064_production, 84_LVBus1594065_production, 84_LVBus1594066_production, 84_LVBus1594068_production, 84_LVBus1594070_production, 84_LVBus1594072_consumption, 84_LVBus1594072_production, 84_LVBus1594074_production, 84_LVBus1594076_production, 84_LVBus1594077_production, 84_LVBus1594078_production, 84_LVBus1594079_consumption, 84_LVBus1594079_production, 84_LVBus1594080_production, 84_LVBus1594081_production, 84_LVBus1594082_production, 84_LVBus1594083_production, 84_LVBus1594084_production, 84_LVBus1594085_production, 84_LVBus1594086_production, 84_LVBus1594087_production, 84_LVBus1594089_production, 84_LVBus1594091_production, 84_LVBus1594092_production, 84_LVBus1594093_production, 84_LVBus1594094_production, 84_LVBus1594095_consumption, 84_LVBus1594095_production, 84_LVBus1594096_production, 84_LVBus1594097_production, 84_LVBus1594098_production, 84_LVBus1594099_production, 84_LVBus1594100_production, 84_LVBus1594101_production, 84_LVBus1594102_production, 84_LVBus1594104_consumption, 84_LVBus1594104_production, 84_LVBus1594105_production, 84_LVBus1594106_production, 84_LVBus1594107_production, 84_LVBus1594108_production, 84_LVBus1594109_production, 84_LVBus1594111_consumption, 84_LVBus1594111_production, 84_LVBus1594112_production, 84_LVBus1594113_production, 84_LVBus1594115_production, 84_LVBus1594116_production, 84_LVBus1594117_production, 84_LVBus1594119_production, 84_LVBus1594120_production, 84_LVBus1594121_production, 84_LVBus1594122_production, 84_LVBus1594123_production, 84_LVBus1594124_production, 84_LVBus1594126_consumption, 84_LVBus1594126_production, 84_LVBus1594127_production, 84_LVBus1594128_production, 84_LVBus1594129_production, 84_LVBus1594130_production, 84_LVBus1594131_production, 84_LVBus1594132_production, 84_LVBus1594133_production, 84_LVBus1594134_production, 84_LVBus1594135_production, 84_LVBus1594137_consumption, 84_LVBus1594137_production, 84_LVBus1594138_consumption, 84_LVBus1594138_production, 84_LVBus1594139_production, 84_LVBus1594140_production, 84_LVBus1594142_production, 84_LVBus1594143_production, 84_LVBus1594144_production, 84_LVBus1594145_production, 84_LVBus1594146_production, 84_LVBus1594148_consumption, 84_LVBus1594148_production, 84_LVBus1594149_production, 84_LVBus1594151_production, 84_LVBus1594152_production, 84_LVBus1594153_production, 84_LVBus1594154_production, 84_LVBus1594155_production, 84_LVBus1594156_production, 84_LVBus1594158_consumption, 84_LVBus1594158_production, 84_LVBus1594160_consumption, 84_LVBus1594160_production, 84_LVBus1594161_consumption, 84_LVBus1594161_production, 84_LVBus1594162_production, 84_LVBus1594164_consumption, 84_LVBus1594164_production, 84_LVBus1594165_production, 84_LVBus1594167_consumption, 84_LVBus1594167_production, 84_LVBus1594168_production, 84_LVBus1594169_production, 84_LVBus1594171_production, 84_LVBus1594173_consumption, 84_LVBus1594173_production, 84_LVBus1594174_consumption, 84_LVBus1594174_production, 84_LVBus1594176_production, 84_LVBus1594178_production, 84_LVBus2021878_consumption, 84_LVBus2021878_production, 84_LVBus2037715_consumption, 84_LVBus2037715_production, 84_LVBus2037716_consumption, 84_LVBus2037716_production, 84_LVBus2071790_production, 84_LVBus2078923_production, 84_LVBus2090293_consumption, 84_LVBus2090293_production, 84_LVBus2090294_production, 84_LVBus2093850_consumption, 84_LVBus2093850_production, 84_LVBus2093851_consumption, 84_LVBus2093851_production, 84_LVBus2100851_production, 84_LVBus2115723_production, 84_LVBus2122339_consumption, 84_LVBus2122339_production, 84_LVBus2122340_consumption, 84_LVBus2122340_production, 84_LVBus2123381_consumption, 84_LVBus2123381_production, 84_LVBus2123382_production, 84_LVBus2123383_production, 84_LVBus2123384_production, 84_LVBus2123385_production, 84_LVBus2123386_production, 84_LVBus2123387_production, 84_LVBus2123388_production, 84_LVBus2123389_production, 84_LVBus2127736_production, 84_LVBus2127737_consumption, 84_LVBus2127737_production, 84_LVBus2139768_production, 84_LVBus2139769_production, 84_LVBus2139770_production, 84_LVBus2139771_production, 84_LVBus2139772_consumption, 84_LVBus2139772_production, 84_LVBus2139773_production, 84_LVBus2139774_production, 84_LVBus2139775_consumption, 84_LVBus2139775_production, 84_LVBus2139776_production, 84_LVBus2139777_production, 84_LVBus2143769_production, 84_LVBus2162104_consumption, 84_LVBus2162104_production, 84_LVBus2196706_consumption, 84_LVBus2196706_production, 84_LVBus2196707_production, 84_LVBus2196708_production, 84_LVBus2205273_production, 84_LVBus2211803_consumption, 84_LVBus2211803_production, 84_LVBus2221673_production, 84_LVBus2221674_production, 84_LVBus2221675_production, 84_LVBus2235373_production, 84_LVBus2244605_consumption, 84_LVBus2244605_production, 84_LVBus2253895_consumption, 84_LVBus2253895_production, 84_LVBus2253896_production, 84_LVBus2253897_production, 84_LVBus2253898_consumption, 84_LVBus2253898_production, 84_LVBus2262545_consumption, 84_LVBus2262545_production, 84_LVBus2262546_production, 84_LVBus2262547_consumption, 84_LVBus2262547_production, 84_MVLV000240_consumption, 84_MVLV000240_production, 84_MVLV049724_consumption, 84_MVLV049724_production, 84_MVLV049750_consumption, 84_MVLV049750_production, 84_MVLV059885_consumption, 84_MVLV059885_production, 84_MVLV084113_consumption, 84_MVLV084113_production, 84_MVLV098132_consumption, 84_MVLV098132_production, 84_MVLV127696_consumption, 84_MVLV127696_production, 84_MVLV142140_consumption, 84_MVLV142140_production.

