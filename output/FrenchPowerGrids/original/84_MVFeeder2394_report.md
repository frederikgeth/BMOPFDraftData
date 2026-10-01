# BMOPF Network Summary: 84_MVFeeder2394

**Generated:** 2026-10-01 23:34:42  
**Findings:** 0 errors · 5 warnings · 377 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 43 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 688 |  |
| line | 644 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1116 | 1.72 MW, 515.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 43 |  |
| switch | 0 |  |
| transformer | 43 | Dyn11×43 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 89 | 88 | 4 | 0 |
| LV_236V | 236.0 V | 599 | 556 | 1112 | 0 |

**Transformer transitions:**

- `84_MVLV090301_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV036346_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV086535_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV099202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV025070_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV130282_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV022456_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV029790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094091_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV122468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV155607_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV032698_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094059_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV122460_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV129721_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV042210_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV047216_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV070146_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV038630_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV032702_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV070563_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV154530_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV013030_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV090395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV089412_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV012915_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV157051_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV107327_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV025069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV043755_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV108723_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV051857_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094042_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV154533_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV157560_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV027264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV084348_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV156163_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV142652_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV073035_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV041973_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128778_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV012988_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 230 |
| Tree depth (max hops) | 37 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 688 | 1 | 687 | 0 | 0 | 0 |
| Tier LV_236V | 599 | 43 | 556 | 0 | 0 | 0 |
| Tier MV_11.8kV | 89 | 1 | 88 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 43; skipped invalid branches: 0.

Galvanic zones: 44; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MESSI | MV_11.8kV | 89 | 0 | 0 | 43 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2663 declared bus terminals; 2488 mapped line/closed-switch conductor edges; 175 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 71600.0 | 4.837 | 3348 |
| q_nom | 0.0 | 21500.0 | 4.837 | 3348 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.12 | 2620.0 | 1.597 | 644 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.571 | 43 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 707 of 1116 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100672_consumption' has phase imbalance of 102.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100680_consumption' has phase imbalance of 213.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2148148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101007_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166447_consumption' has phase imbalance of 252.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2163420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100732_consumption' has phase imbalance of 242.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100558_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130207_consumption' has phase imbalance of 43.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100770_consumption' has phase imbalance of 216.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100657_consumption' has phase imbalance of 256.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100855_consumption' has phase imbalance of 122.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100933_consumption' has phase imbalance of 202.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100937_consumption' has phase imbalance of 188.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100942_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100967_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101023_consumption' has phase imbalance of 292.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101015_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2169894_consumption' has phase imbalance of 243.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2239741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101070_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100690_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100684_consumption' has phase imbalance of 293.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100825_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101035_consumption' has phase imbalance of 276.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100893_consumption' has phase imbalance of 138.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100913_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100576_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096038_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100660_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100580_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100682_consumption' has phase imbalance of 294.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101053_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100957_consumption' has phase imbalance of 297.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100647_consumption' has phase imbalance of 198.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100633_consumption' has phase imbalance of 293.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2063424_consumption' has phase imbalance of 180.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100848_consumption' has phase imbalance of 253.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100731_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100964_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2157774_consumption' has phase imbalance of 55.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100626_consumption' has phase imbalance of 204.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100559_consumption' has phase imbalance of 188.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100952_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100663_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100919_consumption' has phase imbalance of 206.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100876_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100921_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101014_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101055_consumption' has phase imbalance of 234.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100971_consumption' has phase imbalance of 119.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100807_consumption' has phase imbalance of 26.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100899_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100579_consumption' has phase imbalance of 224.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100603_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100826_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2211004_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100681_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100963_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100931_consumption' has phase imbalance of 298.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100985_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100816_consumption' has phase imbalance of 107.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100954_consumption' has phase imbalance of 275.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100543_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130205_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100988_consumption' has phase imbalance of 229.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100795_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100998_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2158473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100721_consumption' has phase imbalance of 59.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062023_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096040_consumption' has phase imbalance of 146.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100797_consumption' has phase imbalance of 31.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100785_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100840_consumption' has phase imbalance of 148.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100997_consumption' has phase imbalance of 280.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2032689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101041_consumption' has phase imbalance of 238.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100880_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100822_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100704_consumption' has phase imbalance of 232.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100596_consumption' has phase imbalance of 188.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100815_consumption' has phase imbalance of 92.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100889_consumption' has phase imbalance of 245.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100548_consumption' has phase imbalance of 244.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100583_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101019_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100868_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100894_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100645_consumption' has phase imbalance of 229.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100811_consumption' has phase imbalance of 83.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2179743_consumption' has phase imbalance of 140.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100620_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100857_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100780_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100960_consumption' has phase imbalance of 103.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101020_consumption' has phase imbalance of 220.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100915_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100670_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100979_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2163410_consumption' has phase imbalance of 107.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100724_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2148145_consumption' has phase imbalance of 285.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100759_consumption' has phase imbalance of 294.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100841_consumption' has phase imbalance of 232.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100788_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100703_consumption' has phase imbalance of 259.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100987_consumption' has phase imbalance of 188.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100572_consumption' has phase imbalance of 157.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166449_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100767_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100694_consumption' has phase imbalance of 271.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100671_consumption' has phase imbalance of 201.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100991_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100651_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100716_consumption' has phase imbalance of 203.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100658_consumption' has phase imbalance of 210.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100615_consumption' has phase imbalance of 205.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2148146_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100673_consumption' has phase imbalance of 44.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100892_consumption' has phase imbalance of 298.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101068_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100866_consumption' has phase imbalance of 206.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100765_consumption' has phase imbalance of 33.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100534_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100940_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100803_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100911_consumption' has phase imbalance of 86.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100928_consumption' has phase imbalance of 223.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2031085_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100699_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100762_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100948_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100665_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100853_consumption' has phase imbalance of 64.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100591_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101056_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101024_consumption' has phase imbalance of 230.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100968_consumption' has phase imbalance of 66.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100947_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100575_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100587_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100896_consumption' has phase imbalance of 165.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100740_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100654_consumption' has phase imbalance of 85.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100602_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100649_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100949_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096036_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100553_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100597_consumption' has phase imbalance of 215.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100833_consumption' has phase imbalance of 127.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100708_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100907_consumption' has phase imbalance of 293.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101072_consumption' has phase imbalance of 145.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100932_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100627_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100906_consumption' has phase imbalance of 134.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100632_consumption' has phase imbalance of 274.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100821_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100666_consumption' has phase imbalance of 209.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100544_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2179742_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100950_consumption' has phase imbalance of 239.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100990_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100944_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100717_consumption' has phase imbalance of 128.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100994_consumption' has phase imbalance of 168.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100664_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100959_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101037_consumption' has phase imbalance of 295.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100743_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100535_consumption' has phase imbalance of 264.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100656_consumption' has phase imbalance of 143.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100746_consumption' has phase imbalance of 90.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101027_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100925_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100881_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100832_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100733_consumption' has phase imbalance of 192.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2072645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100619_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100709_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100856_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100676_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100735_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2065571_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100827_consumption' has phase imbalance of 68.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100901_consumption' has phase imbalance of 225.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2096039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100667_consumption' has phase imbalance of 228.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100652_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100766_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100577_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2137917_consumption' has phase imbalance of 246.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100965_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100755_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100976_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2114845_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2177092_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100726_consumption' has phase imbalance of 104.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100612_consumption' has phase imbalance of 269.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2116560_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2169893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100659_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100882_consumption' has phase imbalance of 30.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101069_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100936_consumption' has phase imbalance of 101.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100885_consumption' has phase imbalance of 233.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100741_consumption' has phase imbalance of 267.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100648_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130199_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100977_consumption' has phase imbalance of 260.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100691_consumption' has phase imbalance of 237.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100830_consumption' has phase imbalance of 212.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100941_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100565_consumption' has phase imbalance of 277.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130202_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2114846_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118443_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100981_consumption' has phase imbalance of 62.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100984_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100692_consumption' has phase imbalance of 175.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100926_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101060_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100877_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100842_consumption' has phase imbalance of 24.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100914_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100939_consumption' has phase imbalance of 264.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100966_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100831_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0101036_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100787_consumption' has phase imbalance of 272.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100756_consumption' has phase imbalance of 141.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100951_consumption' has phase imbalance of 296.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100867_consumption' has phase imbalance of 279.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100634_consumption' has phase imbalance of 264.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130201_consumption' has phase imbalance of 190.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100697_consumption' has phase imbalance of 291.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100725_consumption' has phase imbalance of 157.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100800_consumption' has phase imbalance of 174.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100617_consumption' has phase imbalance of 259.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100554_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100783_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166448_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2087486_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100655_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100588_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100688_consumption' has phase imbalance of 274.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0100872_consumption' has phase imbalance of 90.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1116 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_MESSI' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0100639' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0100637' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0101012' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.72 MW |
| Total load Q | 515.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV090301_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV036346_Transformer | 440.0 kVA | 12.5% |
| 84_MVLV086535_Transformer | 693.0 kVA | 28.7% |
| 84_MVLV099202_Transformer | 110.0 kVA | 11.6% |
| 84_MVLV025070_Transformer | 110.0 kVA | 6.6% |
| 84_MVLV130282_Transformer | 275.0 kVA | 30.2% |
| 84_MVLV022456_Transformer | 275.0 kVA | 22.2% |
| 84_MVLV029790_Transformer | 440.0 kVA | 11.2% |
| 84_MVLV094091_Transformer | 176.0 kVA | 8.6% |
| 84_MVLV122468_Transformer | 275.0 kVA | 23.2% |
| 84_MVLV155607_Transformer | 176.0 kVA | 11.1% |
| 84_MVLV032698_Transformer | 275.0 kVA | 12.7% |
| 84_MVLV094059_Transformer | 693.0 kVA | 23.3% |
| 84_MVLV122460_Transformer | 176.0 kVA | 5.9% |
| 84_MVLV129721_Transformer | 176.0 kVA | 5.5% |
| 84_MVLV042210_Transformer | 275.0 kVA | 19.0% |
| 84_MVLV047216_Transformer | 176.0 kVA | 20.6% |
| 84_MVLV070146_Transformer | 176.0 kVA | 18.5% |
| 84_MVLV038630_Transformer | 176.0 kVA | 6.0% |
| 84_MVLV032702_Transformer | 275.0 kVA | 17.6% |
| 84_MVLV070563_Transformer | 440.0 kVA | 15.7% |
| 84_MVLV154530_Transformer | 275.0 kVA | 9.6% |
| 84_MVLV013030_Transformer | 440.0 kVA | 19.9% |
| 84_MVLV090395_Transformer | 176.0 kVA | 6.4% |
| 84_MVLV089412_Transformer | 275.0 kVA | 16.2% |
| 84_MVLV012915_Transformer | 110.0 kVA | 6.5% |
| 84_MVLV157051_Transformer | 440.0 kVA | 15.1% |
| 84_MVLV107327_Transformer | 110.0 kVA | 11.7% |
| 84_MVLV025069_Transformer | 275.0 kVA | 15.0% |
| 84_MVLV043755_Transformer | 176.0 kVA | 5.4% |
| 84_MVLV108723_Transformer | 176.0 kVA | 19.8% |
| 84_MVLV051857_Transformer | 275.0 kVA | 8.8% |
| 84_MVLV094042_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV154533_Transformer | 110.0 kVA | 3.6% |
| 84_MVLV157560_Transformer | 176.0 kVA | 10.9% |
| 84_MVLV027264_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV084348_Transformer | 176.0 kVA | 14.7% |
| 84_MVLV156163_Transformer | 110.0 kVA | 3.7% |
| 84_MVLV142652_Transformer | 110.0 kVA | 0.2% |
| 84_MVLV073035_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV041973_Transformer | 176.0 kVA | 15.3% |
| 84_MVLV128778_Transformer | 440.0 kVA | 17.9% |
| 84_MVLV012988_Transformer | 176.0 kVA | 8.6% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.72 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0100863' (LV, 0.24 kV) has an electrical reach of 16.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0101012' (LV, 0.24 kV) has an electrical reach of 8.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 688 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 688 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 43 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 89 |
| LV_236V | 4-wire | 599 / 599 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 599 |
| Neutral branches | 556 |
| Grounding points | 43 |
| Neutral sections | 43 |
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
| 11.78 kV | 89 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 57 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 44 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1470.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 599 / 89 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 708 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 708 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0100529_consumption, 84_LVBus0100529_production, 84_LVBus0100530_consumption, 84_LVBus0100530_production, 84_LVBus0100531_production, 84_LVBus0100532_consumption, 84_LVBus0100532_production, 84_LVBus0100533_production, 84_LVBus0100534_production, 84_LVBus0100535_production, 84_LVBus0100536_consumption, 84_LVBus0100536_production, 84_LVBus0100537_production, 84_LVBus0100542_consumption, 84_LVBus0100542_production, 84_LVBus0100543_production, 84_LVBus0100544_production, 84_LVBus0100545_production, 84_LVBus0100546_production, 84_LVBus0100547_consumption, 84_LVBus0100547_production, 84_LVBus0100548_production, 84_LVBus0100549_production, 84_LVBus0100550_consumption, 84_LVBus0100550_production, 84_LVBus0100551_consumption, 84_LVBus0100551_production, 84_LVBus0100552_production, 84_LVBus0100553_production, 84_LVBus0100554_production, 84_LVBus0100555_production, 84_LVBus0100557_consumption, 84_LVBus0100557_production, 84_LVBus0100558_production, 84_LVBus0100559_production, 84_LVBus0100560_consumption, 84_LVBus0100560_production, 84_LVBus0100561_consumption, 84_LVBus0100561_production, 84_LVBus0100562_consumption, 84_LVBus0100562_production, 84_LVBus0100563_consumption, 84_LVBus0100563_production, 84_LVBus0100564_consumption, 84_LVBus0100564_production, 84_LVBus0100565_production, 84_LVBus0100566_consumption, 84_LVBus0100566_production, 84_LVBus0100567_consumption, 84_LVBus0100567_production, 84_LVBus0100568_consumption, 84_LVBus0100568_production, 84_LVBus0100569_production, 84_LVBus0100570_consumption, 84_LVBus0100570_production, 84_LVBus0100572_production, 84_LVBus0100574_consumption, 84_LVBus0100574_production, 84_LVBus0100575_production, 84_LVBus0100576_production, 84_LVBus0100577_production, 84_LVBus0100579_production, 84_LVBus0100580_production, 84_LVBus0100581_production, 84_LVBus0100582_production, 84_LVBus0100583_production, 84_LVBus0100584_production, 84_LVBus0100586_consumption, 84_LVBus0100586_production, 84_LVBus0100587_production, 84_LVBus0100588_production, 84_LVBus0100589_production, 84_LVBus0100591_production, 84_LVBus0100592_production, 84_LVBus0100593_production, 84_LVBus0100594_consumption, 84_LVBus0100594_production, 84_LVBus0100595_production, 84_LVBus0100596_production, 84_LVBus0100597_production, 84_LVBus0100598_production, 84_LVBus0100599_production, 84_LVBus0100600_consumption, 84_LVBus0100600_production, 84_LVBus0100601_production, 84_LVBus0100602_production, 84_LVBus0100603_production, 84_LVBus0100604_consumption, 84_LVBus0100604_production, 84_LVBus0100605_production, 84_LVBus0100607_consumption, 84_LVBus0100607_production, 84_LVBus0100609_consumption, 84_LVBus0100609_production, 84_LVBus0100610_production, 84_LVBus0100612_production, 84_LVBus0100613_production, 84_LVBus0100614_production, 84_LVBus0100615_production, 84_LVBus0100616_consumption, 84_LVBus0100616_production, 84_LVBus0100617_production, 84_LVBus0100618_consumption, 84_LVBus0100618_production, 84_LVBus0100619_production, 84_LVBus0100620_production, 84_LVBus0100621_consumption, 84_LVBus0100621_production, 84_LVBus0100622_production, 84_LVBus0100623_consumption, 84_LVBus0100623_production, 84_LVBus0100624_production, 84_LVBus0100625_consumption, 84_LVBus0100625_production, 84_LVBus0100626_production, 84_LVBus0100627_production, 84_LVBus0100628_production, 84_LVBus0100632_production, 84_LVBus0100633_production, 84_LVBus0100634_production, 84_LVBus0100635_production, 84_LVBus0100637_production, 84_LVBus0100639_consumption, 84_LVBus0100639_production, 84_LVBus0100641_production, 84_LVBus0100643_production, 84_LVBus0100645_production, 84_LVBus0100647_production, 84_LVBus0100648_production, 84_LVBus0100649_production, 84_LVBus0100650_consumption, 84_LVBus0100650_production, 84_LVBus0100651_production, 84_LVBus0100652_production, 84_LVBus0100654_production, 84_LVBus0100655_production, 84_LVBus0100656_production, 84_LVBus0100657_production, 84_LVBus0100658_production, 84_LVBus0100659_production, 84_LVBus0100660_production, 84_LVBus0100661_production, 84_LVBus0100663_production, 84_LVBus0100664_production, 84_LVBus0100665_production, 84_LVBus0100666_production, 84_LVBus0100667_production, 84_LVBus0100668_production, 84_LVBus0100669_consumption, 84_LVBus0100669_production, 84_LVBus0100670_production, 84_LVBus0100671_production, 84_LVBus0100672_production, 84_LVBus0100673_production, 84_LVBus0100674_production, 84_LVBus0100675_production, 84_LVBus0100676_production, 84_LVBus0100678_consumption, 84_LVBus0100678_production, 84_LVBus0100679_production, 84_LVBus0100680_production, 84_LVBus0100681_production, 84_LVBus0100682_production, 84_LVBus0100683_production, 84_LVBus0100684_production, 84_LVBus0100686_production, 84_LVBus0100687_production, 84_LVBus0100688_production, 84_LVBus0100689_production, 84_LVBus0100690_production, 84_LVBus0100691_production, 84_LVBus0100692_production, 84_LVBus0100693_production, 84_LVBus0100694_production, 84_LVBus0100695_consumption, 84_LVBus0100695_production, 84_LVBus0100696_production, 84_LVBus0100697_production, 84_LVBus0100699_production, 84_LVBus0100700_production, 84_LVBus0100701_production, 84_LVBus0100702_production, 84_LVBus0100703_production, 84_LVBus0100704_production, 84_LVBus0100705_consumption, 84_LVBus0100705_production, 84_LVBus0100706_production, 84_LVBus0100707_production, 84_LVBus0100708_production, 84_LVBus0100709_production, 84_LVBus0100710_production, 84_LVBus0100712_production, 84_LVBus0100713_production, 84_LVBus0100714_production, 84_LVBus0100716_production, 84_LVBus0100717_production, 84_LVBus0100718_consumption, 84_LVBus0100718_production, 84_LVBus0100719_production, 84_LVBus0100720_production, 84_LVBus0100721_production, 84_LVBus0100723_consumption, 84_LVBus0100723_production, 84_LVBus0100724_production, 84_LVBus0100725_production, 84_LVBus0100726_production, 84_LVBus0100728_production, 84_LVBus0100729_consumption, 84_LVBus0100729_production, 84_LVBus0100730_production, 84_LVBus0100731_production, 84_LVBus0100732_production, 84_LVBus0100733_production, 84_LVBus0100734_production, 84_LVBus0100735_production, 84_LVBus0100737_production, 84_LVBus0100738_consumption, 84_LVBus0100738_production, 84_LVBus0100739_production, 84_LVBus0100740_production, 84_LVBus0100741_production, 84_LVBus0100742_consumption, 84_LVBus0100742_production, 84_LVBus0100743_production, 84_LVBus0100744_consumption, 84_LVBus0100744_production, 84_LVBus0100745_consumption, 84_LVBus0100745_production, 84_LVBus0100746_production, 84_LVBus0100747_consumption, 84_LVBus0100747_production, 84_LVBus0100748_consumption, 84_LVBus0100748_production, 84_LVBus0100749_consumption, 84_LVBus0100749_production, 84_LVBus0100750_production, 84_LVBus0100751_production, 84_LVBus0100752_production, 84_LVBus0100755_production, 84_LVBus0100756_production, 84_LVBus0100757_production, 84_LVBus0100758_consumption, 84_LVBus0100758_production, 84_LVBus0100759_production, 84_LVBus0100760_production, 84_LVBus0100761_production, 84_LVBus0100762_production, 84_LVBus0100764_production, 84_LVBus0100765_production, 84_LVBus0100766_production, 84_LVBus0100767_production, 84_LVBus0100768_production, 84_LVBus0100769_production, 84_LVBus0100770_production, 84_LVBus0100771_production, 84_LVBus0100772_production, 84_LVBus0100773_production, 84_LVBus0100775_consumption, 84_LVBus0100775_production, 84_LVBus0100776_consumption, 84_LVBus0100776_production, 84_LVBus0100778_consumption, 84_LVBus0100778_production, 84_LVBus0100779_consumption, 84_LVBus0100779_production, 84_LVBus0100780_production, 84_LVBus0100782_production, 84_LVBus0100783_production, 84_LVBus0100784_consumption, 84_LVBus0100784_production, 84_LVBus0100785_production, 84_LVBus0100786_production, 84_LVBus0100787_production, 84_LVBus0100788_production, 84_LVBus0100789_production, 84_LVBus0100790_production, 84_LVBus0100791_production, 84_LVBus0100793_consumption, 84_LVBus0100793_production, 84_LVBus0100794_consumption, 84_LVBus0100794_production, 84_LVBus0100795_production, 84_LVBus0100796_production, 84_LVBus0100797_production, 84_LVBus0100798_consumption, 84_LVBus0100798_production, 84_LVBus0100799_production, 84_LVBus0100800_production, 84_LVBus0100801_production, 84_LVBus0100802_consumption, 84_LVBus0100802_production, 84_LVBus0100803_production, 84_LVBus0100804_production, 84_LVBus0100805_consumption, 84_LVBus0100805_production, 84_LVBus0100806_production, 84_LVBus0100807_production, 84_LVBus0100808_production, 84_LVBus0100809_consumption, 84_LVBus0100809_production, 84_LVBus0100811_production, 84_LVBus0100812_consumption, 84_LVBus0100812_production, 84_LVBus0100813_consumption, 84_LVBus0100813_production, 84_LVBus0100814_consumption, 84_LVBus0100814_production, 84_LVBus0100815_production, 84_LVBus0100816_production, 84_LVBus0100817_production, 84_LVBus0100819_production, 84_LVBus0100820_consumption, 84_LVBus0100820_production, 84_LVBus0100821_production, 84_LVBus0100822_production, 84_LVBus0100823_production, 84_LVBus0100824_production, 84_LVBus0100825_production, 84_LVBus0100826_production, 84_LVBus0100827_production, 84_LVBus0100828_consumption, 84_LVBus0100828_production, 84_LVBus0100829_consumption, 84_LVBus0100829_production, 84_LVBus0100830_production, 84_LVBus0100831_production, 84_LVBus0100832_production, 84_LVBus0100833_production, 84_LVBus0100834_production, 84_LVBus0100835_consumption, 84_LVBus0100835_production, 84_LVBus0100836_consumption, 84_LVBus0100836_production, 84_LVBus0100837_production, 84_LVBus0100838_production, 84_LVBus0100839_consumption, 84_LVBus0100839_production, 84_LVBus0100840_production, 84_LVBus0100841_production, 84_LVBus0100842_production, 84_LVBus0100848_production, 84_LVBus0100849_consumption, 84_LVBus0100849_production, 84_LVBus0100850_production, 84_LVBus0100851_consumption, 84_LVBus0100851_production, 84_LVBus0100852_production, 84_LVBus0100853_production, 84_LVBus0100854_production, 84_LVBus0100855_production, 84_LVBus0100856_production, 84_LVBus0100857_production, 84_LVBus0100858_consumption, 84_LVBus0100858_production, 84_LVBus0100859_consumption, 84_LVBus0100859_production, 84_LVBus0100860_consumption, 84_LVBus0100860_production, 84_LVBus0100861_production, 84_LVBus0100863_consumption, 84_LVBus0100863_production, 84_LVBus0100865_consumption, 84_LVBus0100865_production, 84_LVBus0100866_production, 84_LVBus0100867_production, 84_LVBus0100868_production, 84_LVBus0100870_consumption, 84_LVBus0100870_production, 84_LVBus0100872_production, 84_LVBus0100873_production, 84_LVBus0100874_consumption, 84_LVBus0100874_production, 84_LVBus0100876_production, 84_LVBus0100877_production, 84_LVBus0100878_consumption, 84_LVBus0100878_production, 84_LVBus0100879_production, 84_LVBus0100880_production, 84_LVBus0100881_production, 84_LVBus0100882_production, 84_LVBus0100884_consumption, 84_LVBus0100884_production, 84_LVBus0100885_production, 84_LVBus0100886_consumption, 84_LVBus0100886_production, 84_LVBus0100887_production, 84_LVBus0100888_production, 84_LVBus0100889_production, 84_LVBus0100891_consumption, 84_LVBus0100891_production, 84_LVBus0100892_production, 84_LVBus0100893_production, 84_LVBus0100894_production, 84_LVBus0100896_production, 84_LVBus0100898_consumption, 84_LVBus0100898_production, 84_LVBus0100899_production, 84_LVBus0100900_production, 84_LVBus0100901_production, 84_LVBus0100902_consumption, 84_LVBus0100902_production, 84_LVBus0100903_consumption, 84_LVBus0100903_production, 84_LVBus0100905_production, 84_LVBus0100906_production, 84_LVBus0100907_production, 84_LVBus0100909_consumption, 84_LVBus0100909_production, 84_LVBus0100911_production, 84_LVBus0100913_production, 84_LVBus0100914_production, 84_LVBus0100915_production, 84_LVBus0100919_production, 84_LVBus0100920_consumption, 84_LVBus0100920_production, 84_LVBus0100921_production, 84_LVBus0100922_production, 84_LVBus0100923_production, 84_LVBus0100924_production, 84_LVBus0100925_production, 84_LVBus0100926_production, 84_LVBus0100928_production, 84_LVBus0100929_consumption, 84_LVBus0100929_production, 84_LVBus0100930_production, 84_LVBus0100931_production, 84_LVBus0100932_production, 84_LVBus0100933_production, 84_LVBus0100935_production, 84_LVBus0100936_production, 84_LVBus0100937_production, 84_LVBus0100939_production, 84_LVBus0100940_production, 84_LVBus0100941_production, 84_LVBus0100942_production, 84_LVBus0100944_production, 84_LVBus0100945_production, 84_LVBus0100946_consumption, 84_LVBus0100946_production, 84_LVBus0100947_production, 84_LVBus0100948_production, 84_LVBus0100949_production, 84_LVBus0100950_production, 84_LVBus0100951_production, 84_LVBus0100952_production, 84_LVBus0100953_consumption, 84_LVBus0100953_production, 84_LVBus0100954_production, 84_LVBus0100956_consumption, 84_LVBus0100956_production, 84_LVBus0100957_production, 84_LVBus0100959_production, 84_LVBus0100960_production, 84_LVBus0100961_consumption, 84_LVBus0100961_production, 84_LVBus0100962_production, 84_LVBus0100963_production, 84_LVBus0100964_production, 84_LVBus0100965_production, 84_LVBus0100966_production, 84_LVBus0100967_production, 84_LVBus0100968_production, 84_LVBus0100969_production, 84_LVBus0100971_production, 84_LVBus0100972_consumption, 84_LVBus0100972_production, 84_LVBus0100974_consumption, 84_LVBus0100974_production, 84_LVBus0100975_consumption, 84_LVBus0100975_production, 84_LVBus0100976_production, 84_LVBus0100977_production, 84_LVBus0100978_consumption, 84_LVBus0100978_production, 84_LVBus0100979_production, 84_LVBus0100981_production, 84_LVBus0100982_consumption, 84_LVBus0100982_production, 84_LVBus0100983_consumption, 84_LVBus0100983_production, 84_LVBus0100984_production, 84_LVBus0100985_production, 84_LVBus0100986_production, 84_LVBus0100987_production, 84_LVBus0100988_production, 84_LVBus0100989_production, 84_LVBus0100990_production, 84_LVBus0100991_production, 84_LVBus0100992_consumption, 84_LVBus0100992_production, 84_LVBus0100993_consumption, 84_LVBus0100993_production, 84_LVBus0100994_production, 84_LVBus0100996_production, 84_LVBus0100997_production, 84_LVBus0100998_production, 84_LVBus0100999_production, 84_LVBus0101000_production, 84_LVBus0101001_consumption, 84_LVBus0101001_production, 84_LVBus0101003_consumption, 84_LVBus0101003_production, 84_LVBus0101004_production, 84_LVBus0101005_consumption, 84_LVBus0101005_production, 84_LVBus0101006_consumption, 84_LVBus0101006_production, 84_LVBus0101007_production, 84_LVBus0101008_production, 84_LVBus0101009_consumption, 84_LVBus0101009_production, 84_LVBus0101010_production, 84_LVBus0101012_production, 84_LVBus0101014_production, 84_LVBus0101015_production, 84_LVBus0101016_production, 84_LVBus0101017_production, 84_LVBus0101018_production, 84_LVBus0101019_production, 84_LVBus0101020_production, 84_LVBus0101021_consumption, 84_LVBus0101021_production, 84_LVBus0101022_consumption, 84_LVBus0101022_production, 84_LVBus0101023_production, 84_LVBus0101024_production, 84_LVBus0101026_production, 84_LVBus0101027_production, 84_LVBus0101028_production, 84_LVBus0101029_production, 84_LVBus0101030_production, 84_LVBus0101034_consumption, 84_LVBus0101034_production, 84_LVBus0101035_production, 84_LVBus0101036_production, 84_LVBus0101037_production, 84_LVBus0101038_production, 84_LVBus0101039_consumption, 84_LVBus0101039_production, 84_LVBus0101040_production, 84_LVBus0101041_production, 84_LVBus0101045_production, 84_LVBus0101046_production, 84_LVBus0101047_consumption, 84_LVBus0101047_production, 84_LVBus0101048_consumption, 84_LVBus0101048_production, 84_LVBus0101050_consumption, 84_LVBus0101050_production, 84_LVBus0101051_production, 84_LVBus0101052_production, 84_LVBus0101053_production, 84_LVBus0101054_consumption, 84_LVBus0101054_production, 84_LVBus0101055_production, 84_LVBus0101056_production, 84_LVBus0101057_production, 84_LVBus0101059_consumption, 84_LVBus0101059_production, 84_LVBus0101060_production, 84_LVBus0101061_production, 84_LVBus0101063_production, 84_LVBus0101064_consumption, 84_LVBus0101064_production, 84_LVBus0101065_production, 84_LVBus0101066_consumption, 84_LVBus0101066_production, 84_LVBus0101067_consumption, 84_LVBus0101067_production, 84_LVBus0101068_production, 84_LVBus0101069_production, 84_LVBus0101070_production, 84_LVBus0101071_production, 84_LVBus0101072_production, 84_LVBus0101073_consumption, 84_LVBus0101073_production, 84_LVBus2027537_consumption, 84_LVBus2027537_production, 84_LVBus2031085_production, 84_LVBus2032689_production, 84_LVBus2032784_consumption, 84_LVBus2032784_production, 84_LVBus2037915_consumption, 84_LVBus2037915_production, 84_LVBus2037916_consumption, 84_LVBus2037916_production, 84_LVBus2062023_production, 84_LVBus2063424_production, 84_LVBus2065571_production, 84_LVBus2070144_consumption, 84_LVBus2070144_production, 84_LVBus2072645_production, 84_LVBus2086266_consumption, 84_LVBus2086266_production, 84_LVBus2087486_production, 84_LVBus2096033_production, 84_LVBus2096034_production, 84_LVBus2096035_production, 84_LVBus2096036_production, 84_LVBus2096037_production, 84_LVBus2096038_production, 84_LVBus2096039_production, 84_LVBus2096040_production, 84_LVBus2096041_production, 84_LVBus2096042_production, 84_LVBus2102037_production, 84_LVBus2111404_production, 84_LVBus2114845_production, 84_LVBus2114846_production, 84_LVBus2116560_production, 84_LVBus2118443_production, 84_LVBus2118444_consumption, 84_LVBus2118444_production, 84_LVBus2118445_production, 84_LVBus2130191_consumption, 84_LVBus2130191_production, 84_LVBus2130192_consumption, 84_LVBus2130192_production, 84_LVBus2130193_production, 84_LVBus2130194_consumption, 84_LVBus2130194_production, 84_LVBus2130195_consumption, 84_LVBus2130195_production, 84_LVBus2130196_consumption, 84_LVBus2130196_production, 84_LVBus2130197_production, 84_LVBus2130198_consumption, 84_LVBus2130198_production, 84_LVBus2130199_production, 84_LVBus2130200_consumption, 84_LVBus2130200_production, 84_LVBus2130201_production, 84_LVBus2130202_production, 84_LVBus2130203_production, 84_LVBus2130204_production, 84_LVBus2130205_production, 84_LVBus2130206_production, 84_LVBus2130207_production, 84_LVBus2130208_consumption, 84_LVBus2130208_production, 84_LVBus2137917_production, 84_LVBus2148145_production, 84_LVBus2148146_production, 84_LVBus2148147_consumption, 84_LVBus2148147_production, 84_LVBus2148148_production, 84_LVBus2148149_consumption, 84_LVBus2148149_production, 84_LVBus2152444_production, 84_LVBus2152445_production, 84_LVBus2152446_consumption, 84_LVBus2152446_production, 84_LVBus2152447_production, 84_LVBus2152448_consumption, 84_LVBus2152448_production, 84_LVBus2152449_production, 84_LVBus2157774_production, 84_LVBus2158473_production, 84_LVBus2163409_consumption, 84_LVBus2163409_production, 84_LVBus2163410_production, 84_LVBus2163419_consumption, 84_LVBus2163419_production, 84_LVBus2163420_production, 84_LVBus2166446_production, 84_LVBus2166447_production, 84_LVBus2166448_production, 84_LVBus2166449_production, 84_LVBus2167934_consumption, 84_LVBus2167934_production, 84_LVBus2169893_production, 84_LVBus2169894_production, 84_LVBus2177092_production, 84_LVBus2179742_production, 84_LVBus2179743_production, 84_LVBus2180919_consumption, 84_LVBus2180919_production, 84_LVBus2180920_consumption, 84_LVBus2180920_production, 84_LVBus2180921_consumption, 84_LVBus2180921_production, 84_LVBus2180922_consumption, 84_LVBus2180922_production, 84_LVBus2180923_consumption, 84_LVBus2180923_production, 84_LVBus2180924_consumption, 84_LVBus2180924_production, 84_LVBus2185070_consumption, 84_LVBus2185070_production, 84_LVBus2197623_consumption, 84_LVBus2197623_production, 84_LVBus2197624_consumption, 84_LVBus2197624_production, 84_LVBus2211004_production, 84_LVBus2224840_production, 84_LVBus2224841_consumption, 84_LVBus2224841_production, 84_LVBus2224842_production, 84_LVBus2239740_consumption, 84_LVBus2239740_production, 84_LVBus2239741_production, 84_LVBus2244470_production, 84_LVBus2245000_production, 84_LVBus2247254_production, 84_LVBus2254135_production, 84_MVLV043772_production, 84_MVLV088557_consumption, 84_MVLV088557_production.

## 9. Data Quality Summary

**Total findings:** 382 (0 errors, 5 warnings, 377 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  707 of 1116 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.72 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  708 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100672_consumption`  
  Load '84_LVBus0100672_consumption' has phase imbalance of 102.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100680_consumption`  
  Load '84_LVBus0100680_consumption' has phase imbalance of 213.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2148148_consumption`  
  Load '84_LVBus2148148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100687_consumption`  
  Load '84_LVBus0100687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101007_consumption`  
  Load '84_LVBus0101007_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101004_consumption`  
  Load '84_LVBus0101004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166447_consumption`  
  Load '84_LVBus2166447_consumption' has phase imbalance of 252.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2163420_consumption`  
  Load '84_LVBus2163420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100589_consumption`  
  Load '84_LVBus0100589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100732_consumption`  
  Load '84_LVBus0100732_consumption' has phase imbalance of 242.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100558_consumption`  
  Load '84_LVBus0100558_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100624_consumption`  
  Load '84_LVBus0100624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101018_consumption`  
  Load '84_LVBus0101018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100533_consumption`  
  Load '84_LVBus0100533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100799_consumption`  
  Load '84_LVBus0100799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130207_consumption`  
  Load '84_LVBus2130207_consumption' has phase imbalance of 43.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100770_consumption`  
  Load '84_LVBus0100770_consumption' has phase imbalance of 216.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100657_consumption`  
  Load '84_LVBus0100657_consumption' has phase imbalance of 256.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100855_consumption`  
  Load '84_LVBus0100855_consumption' has phase imbalance of 122.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100933_consumption`  
  Load '84_LVBus0100933_consumption' has phase imbalance of 202.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100937_consumption`  
  Load '84_LVBus0100937_consumption' has phase imbalance of 188.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100942_consumption`  
  Load '84_LVBus0100942_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100967_consumption`  
  Load '84_LVBus0100967_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101023_consumption`  
  Load '84_LVBus0101023_consumption' has phase imbalance of 292.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101015_consumption`  
  Load '84_LVBus0101015_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2169894_consumption`  
  Load '84_LVBus2169894_consumption' has phase imbalance of 243.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2239741_consumption`  
  Load '84_LVBus2239741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101070_consumption`  
  Load '84_LVBus0101070_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100690_consumption`  
  Load '84_LVBus0100690_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100684_consumption`  
  Load '84_LVBus0100684_consumption' has phase imbalance of 293.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100969_consumption`  
  Load '84_LVBus0100969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100825_consumption`  
  Load '84_LVBus0100825_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101035_consumption`  
  Load '84_LVBus0101035_consumption' has phase imbalance of 276.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100893_consumption`  
  Load '84_LVBus0100893_consumption' has phase imbalance of 138.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100913_consumption`  
  Load '84_LVBus0100913_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100576_consumption`  
  Load '84_LVBus0100576_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096038_consumption`  
  Load '84_LVBus2096038_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100660_consumption`  
  Load '84_LVBus0100660_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100580_consumption`  
  Load '84_LVBus0100580_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100682_consumption`  
  Load '84_LVBus0100682_consumption' has phase imbalance of 294.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100713_consumption`  
  Load '84_LVBus0100713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101053_consumption`  
  Load '84_LVBus0101053_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100923_consumption`  
  Load '84_LVBus0100923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100706_consumption`  
  Load '84_LVBus0100706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100957_consumption`  
  Load '84_LVBus0100957_consumption' has phase imbalance of 297.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100647_consumption`  
  Load '84_LVBus0100647_consumption' has phase imbalance of 198.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100633_consumption`  
  Load '84_LVBus0100633_consumption' has phase imbalance of 293.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2063424_consumption`  
  Load '84_LVBus2063424_consumption' has phase imbalance of 180.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100848_consumption`  
  Load '84_LVBus0100848_consumption' has phase imbalance of 253.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100731_consumption`  
  Load '84_LVBus0100731_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100964_consumption`  
  Load '84_LVBus0100964_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2157774_consumption`  
  Load '84_LVBus2157774_consumption' has phase imbalance of 55.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100626_consumption`  
  Load '84_LVBus0100626_consumption' has phase imbalance of 204.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100559_consumption`  
  Load '84_LVBus0100559_consumption' has phase imbalance of 188.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100952_consumption`  
  Load '84_LVBus0100952_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100663_consumption`  
  Load '84_LVBus0100663_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100919_consumption`  
  Load '84_LVBus0100919_consumption' has phase imbalance of 206.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100876_consumption`  
  Load '84_LVBus0100876_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100921_consumption`  
  Load '84_LVBus0100921_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101014_consumption`  
  Load '84_LVBus0101014_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100852_consumption`  
  Load '84_LVBus0100852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101055_consumption`  
  Load '84_LVBus0101055_consumption' has phase imbalance of 234.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100971_consumption`  
  Load '84_LVBus0100971_consumption' has phase imbalance of 119.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100807_consumption`  
  Load '84_LVBus0100807_consumption' has phase imbalance of 26.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100899_consumption`  
  Load '84_LVBus0100899_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100579_consumption`  
  Load '84_LVBus0100579_consumption' has phase imbalance of 224.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100593_consumption`  
  Load '84_LVBus0100593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100603_consumption`  
  Load '84_LVBus0100603_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100696_consumption`  
  Load '84_LVBus0100696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100826_consumption`  
  Load '84_LVBus0100826_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101030_consumption`  
  Load '84_LVBus0101030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2211004_consumption`  
  Load '84_LVBus2211004_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100681_consumption`  
  Load '84_LVBus0100681_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100888_consumption`  
  Load '84_LVBus0100888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100963_consumption`  
  Load '84_LVBus0100963_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100931_consumption`  
  Load '84_LVBus0100931_consumption' has phase imbalance of 298.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130206_consumption`  
  Load '84_LVBus2130206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100985_consumption`  
  Load '84_LVBus0100985_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100816_consumption`  
  Load '84_LVBus0100816_consumption' has phase imbalance of 107.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100545_consumption`  
  Load '84_LVBus0100545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100954_consumption`  
  Load '84_LVBus0100954_consumption' has phase imbalance of 275.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100668_consumption`  
  Load '84_LVBus0100668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100786_consumption`  
  Load '84_LVBus0100786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100543_consumption`  
  Load '84_LVBus0100543_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130205_consumption`  
  Load '84_LVBus2130205_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100988_consumption`  
  Load '84_LVBus0100988_consumption' has phase imbalance of 229.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100795_consumption`  
  Load '84_LVBus0100795_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100998_consumption`  
  Load '84_LVBus0100998_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2158473_consumption`  
  Load '84_LVBus2158473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100721_consumption`  
  Load '84_LVBus0100721_consumption' has phase imbalance of 59.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100854_consumption`  
  Load '84_LVBus0100854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100996_consumption`  
  Load '84_LVBus0100996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100823_consumption`  
  Load '84_LVBus0100823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096041_consumption`  
  Load '84_LVBus2096041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062023_consumption`  
  Load '84_LVBus2062023_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096040_consumption`  
  Load '84_LVBus2096040_consumption' has phase imbalance of 146.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100797_consumption`  
  Load '84_LVBus0100797_consumption' has phase imbalance of 31.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100785_consumption`  
  Load '84_LVBus0100785_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100737_consumption`  
  Load '84_LVBus0100737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100790_consumption`  
  Load '84_LVBus0100790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100840_consumption`  
  Load '84_LVBus0100840_consumption' has phase imbalance of 148.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100997_consumption`  
  Load '84_LVBus0100997_consumption' has phase imbalance of 280.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100761_consumption`  
  Load '84_LVBus0100761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2032689_consumption`  
  Load '84_LVBus2032689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101041_consumption`  
  Load '84_LVBus0101041_consumption' has phase imbalance of 238.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100880_consumption`  
  Load '84_LVBus0100880_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101016_consumption`  
  Load '84_LVBus0101016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100822_consumption`  
  Load '84_LVBus0100822_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100772_consumption`  
  Load '84_LVBus0100772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100704_consumption`  
  Load '84_LVBus0100704_consumption' has phase imbalance of 232.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100819_consumption`  
  Load '84_LVBus0100819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100596_consumption`  
  Load '84_LVBus0100596_consumption' has phase imbalance of 188.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100750_consumption`  
  Load '84_LVBus0100750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100815_consumption`  
  Load '84_LVBus0100815_consumption' has phase imbalance of 92.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100889_consumption`  
  Load '84_LVBus0100889_consumption' has phase imbalance of 245.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100548_consumption`  
  Load '84_LVBus0100548_consumption' has phase imbalance of 244.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100622_consumption`  
  Load '84_LVBus0100622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101010_consumption`  
  Load '84_LVBus0101010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100583_consumption`  
  Load '84_LVBus0100583_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101019_consumption`  
  Load '84_LVBus0101019_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100868_consumption`  
  Load '84_LVBus0100868_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100894_consumption`  
  Load '84_LVBus0100894_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100645_consumption`  
  Load '84_LVBus0100645_consumption' has phase imbalance of 229.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100811_consumption`  
  Load '84_LVBus0100811_consumption' has phase imbalance of 83.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2179743_consumption`  
  Load '84_LVBus2179743_consumption' has phase imbalance of 140.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100620_consumption`  
  Load '84_LVBus0100620_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100857_consumption`  
  Load '84_LVBus0100857_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100780_consumption`  
  Load '84_LVBus0100780_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100960_consumption`  
  Load '84_LVBus0100960_consumption' has phase imbalance of 103.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100824_consumption`  
  Load '84_LVBus0100824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101020_consumption`  
  Load '84_LVBus0101020_consumption' has phase imbalance of 220.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101038_consumption`  
  Load '84_LVBus0101038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100915_consumption`  
  Load '84_LVBus0100915_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100531_consumption`  
  Load '84_LVBus0100531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100670_consumption`  
  Load '84_LVBus0100670_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100979_consumption`  
  Load '84_LVBus0100979_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2163410_consumption`  
  Load '84_LVBus2163410_consumption' has phase imbalance of 107.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100724_consumption`  
  Load '84_LVBus0100724_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2148145_consumption`  
  Load '84_LVBus2148145_consumption' has phase imbalance of 285.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100759_consumption`  
  Load '84_LVBus0100759_consumption' has phase imbalance of 294.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100841_consumption`  
  Load '84_LVBus0100841_consumption' has phase imbalance of 232.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100788_consumption`  
  Load '84_LVBus0100788_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096037_consumption`  
  Load '84_LVBus2096037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100986_consumption`  
  Load '84_LVBus0100986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100703_consumption`  
  Load '84_LVBus0100703_consumption' has phase imbalance of 259.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100987_consumption`  
  Load '84_LVBus0100987_consumption' has phase imbalance of 188.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100569_consumption`  
  Load '84_LVBus0100569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100572_consumption`  
  Load '84_LVBus0100572_consumption' has phase imbalance of 157.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166449_consumption`  
  Load '84_LVBus2166449_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100767_consumption`  
  Load '84_LVBus0100767_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100694_consumption`  
  Load '84_LVBus0100694_consumption' has phase imbalance of 271.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100796_consumption`  
  Load '84_LVBus0100796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100671_consumption`  
  Load '84_LVBus0100671_consumption' has phase imbalance of 201.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100991_consumption`  
  Load '84_LVBus0100991_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100789_consumption`  
  Load '84_LVBus0100789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100651_consumption`  
  Load '84_LVBus0100651_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100710_consumption`  
  Load '84_LVBus0100710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100716_consumption`  
  Load '84_LVBus0100716_consumption' has phase imbalance of 203.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100658_consumption`  
  Load '84_LVBus0100658_consumption' has phase imbalance of 210.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100615_consumption`  
  Load '84_LVBus0100615_consumption' has phase imbalance of 205.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2148146_consumption`  
  Load '84_LVBus2148146_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100673_consumption`  
  Load '84_LVBus0100673_consumption' has phase imbalance of 44.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100892_consumption`  
  Load '84_LVBus0100892_consumption' has phase imbalance of 298.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101068_consumption`  
  Load '84_LVBus0101068_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100613_consumption`  
  Load '84_LVBus0100613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100866_consumption`  
  Load '84_LVBus0100866_consumption' has phase imbalance of 206.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100765_consumption`  
  Load '84_LVBus0100765_consumption' has phase imbalance of 33.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100702_consumption`  
  Load '84_LVBus0100702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101008_consumption`  
  Load '84_LVBus0101008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100534_consumption`  
  Load '84_LVBus0100534_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100940_consumption`  
  Load '84_LVBus0100940_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096033_consumption`  
  Load '84_LVBus2096033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100803_consumption`  
  Load '84_LVBus0100803_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100911_consumption`  
  Load '84_LVBus0100911_consumption' has phase imbalance of 86.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101000_consumption`  
  Load '84_LVBus0101000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100850_consumption`  
  Load '84_LVBus0100850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100928_consumption`  
  Load '84_LVBus0100928_consumption' has phase imbalance of 223.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2031085_consumption`  
  Load '84_LVBus2031085_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100699_consumption`  
  Load '84_LVBus0100699_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100762_consumption`  
  Load '84_LVBus0100762_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101029_consumption`  
  Load '84_LVBus0101029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100948_consumption`  
  Load '84_LVBus0100948_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224840_consumption`  
  Load '84_LVBus2224840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100665_consumption`  
  Load '84_LVBus0100665_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100853_consumption`  
  Load '84_LVBus0100853_consumption' has phase imbalance of 64.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100707_consumption`  
  Load '84_LVBus0100707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100591_consumption`  
  Load '84_LVBus0100591_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101056_consumption`  
  Load '84_LVBus0101056_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101024_consumption`  
  Load '84_LVBus0101024_consumption' has phase imbalance of 230.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100968_consumption`  
  Load '84_LVBus0100968_consumption' has phase imbalance of 66.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100801_consumption`  
  Load '84_LVBus0100801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100947_consumption`  
  Load '84_LVBus0100947_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096042_consumption`  
  Load '84_LVBus2096042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101057_consumption`  
  Load '84_LVBus0101057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100674_consumption`  
  Load '84_LVBus0100674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100575_consumption`  
  Load '84_LVBus0100575_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100610_consumption`  
  Load '84_LVBus0100610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100587_consumption`  
  Load '84_LVBus0100587_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100945_consumption`  
  Load '84_LVBus0100945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100896_consumption`  
  Load '84_LVBus0100896_consumption' has phase imbalance of 165.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100922_consumption`  
  Load '84_LVBus0100922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100740_consumption`  
  Load '84_LVBus0100740_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100546_consumption`  
  Load '84_LVBus0100546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100654_consumption`  
  Load '84_LVBus0100654_consumption' has phase imbalance of 85.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100602_consumption`  
  Load '84_LVBus0100602_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118445_consumption`  
  Load '84_LVBus2118445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100712_consumption`  
  Load '84_LVBus0100712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100649_consumption`  
  Load '84_LVBus0100649_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100949_consumption`  
  Load '84_LVBus0100949_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096036_consumption`  
  Load '84_LVBus2096036_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100553_consumption`  
  Load '84_LVBus0100553_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100597_consumption`  
  Load '84_LVBus0100597_consumption' has phase imbalance of 215.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100833_consumption`  
  Load '84_LVBus0100833_consumption' has phase imbalance of 127.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100708_consumption`  
  Load '84_LVBus0100708_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100907_consumption`  
  Load '84_LVBus0100907_consumption' has phase imbalance of 293.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101072_consumption`  
  Load '84_LVBus0101072_consumption' has phase imbalance of 145.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100595_consumption`  
  Load '84_LVBus0100595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100605_consumption`  
  Load '84_LVBus0100605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100932_consumption`  
  Load '84_LVBus0100932_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100627_consumption`  
  Load '84_LVBus0100627_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100906_consumption`  
  Load '84_LVBus0100906_consumption' has phase imbalance of 134.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100632_consumption`  
  Load '84_LVBus0100632_consumption' has phase imbalance of 274.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100821_consumption`  
  Load '84_LVBus0100821_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100666_consumption`  
  Load '84_LVBus0100666_consumption' has phase imbalance of 209.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100544_consumption`  
  Load '84_LVBus0100544_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2179742_consumption`  
  Load '84_LVBus2179742_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100950_consumption`  
  Load '84_LVBus0100950_consumption' has phase imbalance of 239.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100962_consumption`  
  Load '84_LVBus0100962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100990_consumption`  
  Load '84_LVBus0100990_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100944_consumption`  
  Load '84_LVBus0100944_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100599_consumption`  
  Load '84_LVBus0100599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100817_consumption`  
  Load '84_LVBus0100817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100717_consumption`  
  Load '84_LVBus0100717_consumption' has phase imbalance of 128.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100994_consumption`  
  Load '84_LVBus0100994_consumption' has phase imbalance of 168.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100664_consumption`  
  Load '84_LVBus0100664_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100959_consumption`  
  Load '84_LVBus0100959_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101037_consumption`  
  Load '84_LVBus0101037_consumption' has phase imbalance of 295.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100743_consumption`  
  Load '84_LVBus0100743_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100549_consumption`  
  Load '84_LVBus0100549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096034_consumption`  
  Load '84_LVBus2096034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100535_consumption`  
  Load '84_LVBus0100535_consumption' has phase imbalance of 264.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100656_consumption`  
  Load '84_LVBus0100656_consumption' has phase imbalance of 143.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100584_consumption`  
  Load '84_LVBus0100584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100746_consumption`  
  Load '84_LVBus0100746_consumption' has phase imbalance of 90.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101027_consumption`  
  Load '84_LVBus0101027_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100925_consumption`  
  Load '84_LVBus0100925_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101061_consumption`  
  Load '84_LVBus0101061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100930_consumption`  
  Load '84_LVBus0100930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100881_consumption`  
  Load '84_LVBus0100881_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100832_consumption`  
  Load '84_LVBus0100832_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100733_consumption`  
  Load '84_LVBus0100733_consumption' has phase imbalance of 192.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2072645_consumption`  
  Load '84_LVBus2072645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096035_consumption`  
  Load '84_LVBus2096035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100619_consumption`  
  Load '84_LVBus0100619_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130204_consumption`  
  Load '84_LVBus2130204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100709_consumption`  
  Load '84_LVBus0100709_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100856_consumption`  
  Load '84_LVBus0100856_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100924_consumption`  
  Load '84_LVBus0100924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100676_consumption`  
  Load '84_LVBus0100676_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100735_consumption`  
  Load '84_LVBus0100735_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2065571_consumption`  
  Load '84_LVBus2065571_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100827_consumption`  
  Load '84_LVBus0100827_consumption' has phase imbalance of 68.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100901_consumption`  
  Load '84_LVBus0100901_consumption' has phase imbalance of 225.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2096039_consumption`  
  Load '84_LVBus2096039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100667_consumption`  
  Load '84_LVBus0100667_consumption' has phase imbalance of 228.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100652_consumption`  
  Load '84_LVBus0100652_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100582_consumption`  
  Load '84_LVBus0100582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100766_consumption`  
  Load '84_LVBus0100766_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100577_consumption`  
  Load '84_LVBus0100577_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100782_consumption`  
  Load '84_LVBus0100782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100804_consumption`  
  Load '84_LVBus0100804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2137917_consumption`  
  Load '84_LVBus2137917_consumption' has phase imbalance of 246.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100965_consumption`  
  Load '84_LVBus0100965_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100755_consumption`  
  Load '84_LVBus0100755_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100592_consumption`  
  Load '84_LVBus0100592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100976_consumption`  
  Load '84_LVBus0100976_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100728_consumption`  
  Load '84_LVBus0100728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2114845_consumption`  
  Load '84_LVBus2114845_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100701_consumption`  
  Load '84_LVBus0100701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100537_consumption`  
  Load '84_LVBus0100537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2177092_consumption`  
  Load '84_LVBus2177092_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100739_consumption`  
  Load '84_LVBus0100739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100726_consumption`  
  Load '84_LVBus0100726_consumption' has phase imbalance of 104.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166446_consumption`  
  Load '84_LVBus2166446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100612_consumption`  
  Load '84_LVBus0100612_consumption' has phase imbalance of 269.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2116560_consumption`  
  Load '84_LVBus2116560_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101046_consumption`  
  Load '84_LVBus0101046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2169893_consumption`  
  Load '84_LVBus2169893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100659_consumption`  
  Load '84_LVBus0100659_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100601_consumption`  
  Load '84_LVBus0100601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100661_consumption`  
  Load '84_LVBus0100661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130203_consumption`  
  Load '84_LVBus2130203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100882_consumption`  
  Load '84_LVBus0100882_consumption' has phase imbalance of 30.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101069_consumption`  
  Load '84_LVBus0101069_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100935_consumption`  
  Load '84_LVBus0100935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100936_consumption`  
  Load '84_LVBus0100936_consumption' has phase imbalance of 101.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100885_consumption`  
  Load '84_LVBus0100885_consumption' has phase imbalance of 233.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100741_consumption`  
  Load '84_LVBus0100741_consumption' has phase imbalance of 267.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100581_consumption`  
  Load '84_LVBus0100581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100648_consumption`  
  Load '84_LVBus0100648_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130199_consumption`  
  Load '84_LVBus2130199_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100977_consumption`  
  Load '84_LVBus0100977_consumption' has phase imbalance of 260.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100791_consumption`  
  Load '84_LVBus0100791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100730_consumption`  
  Load '84_LVBus0100730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100989_consumption`  
  Load '84_LVBus0100989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100691_consumption`  
  Load '84_LVBus0100691_consumption' has phase imbalance of 237.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224842_consumption`  
  Load '84_LVBus2224842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100887_consumption`  
  Load '84_LVBus0100887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100830_consumption`  
  Load '84_LVBus0100830_consumption' has phase imbalance of 212.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100941_consumption`  
  Load '84_LVBus0100941_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100565_consumption`  
  Load '84_LVBus0100565_consumption' has phase imbalance of 277.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130202_consumption`  
  Load '84_LVBus2130202_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100686_consumption`  
  Load '84_LVBus0100686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2114846_consumption`  
  Load '84_LVBus2114846_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118443_consumption`  
  Load '84_LVBus2118443_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100981_consumption`  
  Load '84_LVBus0100981_consumption' has phase imbalance of 62.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100984_consumption`  
  Load '84_LVBus0100984_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101065_consumption`  
  Load '84_LVBus0101065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100692_consumption`  
  Load '84_LVBus0100692_consumption' has phase imbalance of 175.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100926_consumption`  
  Load '84_LVBus0100926_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101060_consumption`  
  Load '84_LVBus0101060_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100877_consumption`  
  Load '84_LVBus0100877_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100689_consumption`  
  Load '84_LVBus0100689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100842_consumption`  
  Load '84_LVBus0100842_consumption' has phase imbalance of 24.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100914_consumption`  
  Load '84_LVBus0100914_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100939_consumption`  
  Load '84_LVBus0100939_consumption' has phase imbalance of 264.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100966_consumption`  
  Load '84_LVBus0100966_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100714_consumption`  
  Load '84_LVBus0100714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100831_consumption`  
  Load '84_LVBus0100831_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0101036_consumption`  
  Load '84_LVBus0101036_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100808_consumption`  
  Load '84_LVBus0100808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100787_consumption`  
  Load '84_LVBus0100787_consumption' has phase imbalance of 272.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100756_consumption`  
  Load '84_LVBus0100756_consumption' has phase imbalance of 141.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100861_consumption`  
  Load '84_LVBus0100861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100951_consumption`  
  Load '84_LVBus0100951_consumption' has phase imbalance of 296.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100751_consumption`  
  Load '84_LVBus0100751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100867_consumption`  
  Load '84_LVBus0100867_consumption' has phase imbalance of 279.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100634_consumption`  
  Load '84_LVBus0100634_consumption' has phase imbalance of 264.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130201_consumption`  
  Load '84_LVBus2130201_consumption' has phase imbalance of 190.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100838_consumption`  
  Load '84_LVBus0100838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100697_consumption`  
  Load '84_LVBus0100697_consumption' has phase imbalance of 291.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100725_consumption`  
  Load '84_LVBus0100725_consumption' has phase imbalance of 157.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100800_consumption`  
  Load '84_LVBus0100800_consumption' has phase imbalance of 174.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100617_consumption`  
  Load '84_LVBus0100617_consumption' has phase imbalance of 259.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100554_consumption`  
  Load '84_LVBus0100554_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100598_consumption`  
  Load '84_LVBus0100598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100783_consumption`  
  Load '84_LVBus0100783_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100734_consumption`  
  Load '84_LVBus0100734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166448_consumption`  
  Load '84_LVBus2166448_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100693_consumption`  
  Load '84_LVBus0100693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2087486_consumption`  
  Load '84_LVBus2087486_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100655_consumption`  
  Load '84_LVBus0100655_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100588_consumption`  
  Load '84_LVBus0100588_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100999_consumption`  
  Load '84_LVBus0100999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100688_consumption`  
  Load '84_LVBus0100688_consumption' has phase imbalance of 274.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0100872_consumption`  
  Load '84_LVBus0100872_consumption' has phase imbalance of 90.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1116 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_MESSI' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0100639' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0100637' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0101012' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0100863' (LV, 0.24 kV) has an electrical reach of 16.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0101012' (LV, 0.24 kV) has an electrical reach of 8.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  688 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  226 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0100531_consumption, 84_LVBus0100533_consumption, 84_LVBus0100534_consumption, 84_LVBus0100535_consumption, 84_LVBus0100537_consumption, 84_LVBus0100544_consumption, 84_LVBus0100545_consumption, 84_LVBus0100546_consumption, 84_LVBus0100549_consumption, 84_LVBus0100558_consumption, 84_LVBus0100559_consumption, 84_LVBus0100565_consumption, 84_LVBus0100569_consumption, 84_LVBus0100572_consumption, 84_LVBus0100575_consumption, 84_LVBus0100577_consumption, 84_LVBus0100579_consumption, 84_LVBus0100580_consumption, 84_LVBus0100581_consumption, 84_LVBus0100582_consumption, 84_LVBus0100583_consumption, 84_LVBus0100584_consumption, 84_LVBus0100587_consumption, 84_LVBus0100588_consumption, 84_LVBus0100589_consumption, 84_LVBus0100591_consumption, 84_LVBus0100592_consumption, 84_LVBus0100593_consumption, 84_LVBus0100595_consumption, 84_LVBus0100596_consumption, 84_LVBus0100597_consumption, 84_LVBus0100598_consumption, 84_LVBus0100599_consumption, 84_LVBus0100601_consumption, 84_LVBus0100602_consumption, 84_LVBus0100603_consumption, 84_LVBus0100605_consumption, 84_LVBus0100610_consumption, 84_LVBus0100613_consumption, 84_LVBus0100620_consumption, 84_LVBus0100622_consumption, 84_LVBus0100624_consumption, 84_LVBus0100627_consumption, 84_LVBus0100648_consumption, 84_LVBus0100661_consumption, 84_LVBus0100663_consumption, 84_LVBus0100665_consumption, 84_LVBus0100666_consumption, 84_LVBus0100667_consumption, 84_LVBus0100668_consumption, 84_LVBus0100670_consumption, 84_LVBus0100671_consumption, 84_LVBus0100674_consumption, 84_LVBus0100681_consumption, 84_LVBus0100686_consumption, 84_LVBus0100687_consumption, 84_LVBus0100689_consumption, 84_LVBus0100691_consumption, 84_LVBus0100693_consumption, 84_LVBus0100694_consumption, 84_LVBus0100696_consumption, 84_LVBus0100699_consumption, 84_LVBus0100701_consumption, 84_LVBus0100702_consumption, 84_LVBus0100703_consumption, 84_LVBus0100704_consumption, 84_LVBus0100706_consumption, 84_LVBus0100707_consumption, 84_LVBus0100708_consumption, 84_LVBus0100709_consumption, 84_LVBus0100710_consumption, 84_LVBus0100712_consumption, 84_LVBus0100713_consumption, 84_LVBus0100714_consumption, 84_LVBus0100725_consumption, 84_LVBus0100728_consumption, 84_LVBus0100730_consumption, 84_LVBus0100732_consumption, 84_LVBus0100733_consumption, 84_LVBus0100734_consumption, 84_LVBus0100735_consumption, 84_LVBus0100737_consumption, 84_LVBus0100739_consumption, 84_LVBus0100743_consumption, 84_LVBus0100750_consumption, 84_LVBus0100751_consumption, 84_LVBus0100761_consumption, 84_LVBus0100772_consumption, 84_LVBus0100782_consumption, 84_LVBus0100783_consumption, 84_LVBus0100785_consumption, 84_LVBus0100786_consumption, 84_LVBus0100788_consumption, 84_LVBus0100789_consumption, 84_LVBus0100790_consumption, 84_LVBus0100791_consumption, 84_LVBus0100795_consumption, 84_LVBus0100796_consumption, 84_LVBus0100799_consumption, 84_LVBus0100800_consumption, 84_LVBus0100801_consumption, 84_LVBus0100804_consumption, 84_LVBus0100808_consumption, 84_LVBus0100817_consumption, 84_LVBus0100819_consumption, 84_LVBus0100821_consumption, 84_LVBus0100822_consumption, 84_LVBus0100823_consumption, 84_LVBus0100824_consumption, 84_LVBus0100825_consumption, 84_LVBus0100826_consumption, 84_LVBus0100830_consumption, 84_LVBus0100838_consumption, 84_LVBus0100848_consumption, 84_LVBus0100850_consumption, 84_LVBus0100852_consumption, 84_LVBus0100854_consumption, 84_LVBus0100857_consumption, 84_LVBus0100861_consumption, 84_LVBus0100866_consumption, 84_LVBus0100877_consumption, 84_LVBus0100881_consumption, 84_LVBus0100887_consumption, 84_LVBus0100888_consumption, 84_LVBus0100889_consumption, 84_LVBus0100894_consumption, 84_LVBus0100896_consumption, 84_LVBus0100919_consumption, 84_LVBus0100921_consumption, 84_LVBus0100922_consumption, 84_LVBus0100923_consumption, 84_LVBus0100924_consumption, 84_LVBus0100925_consumption, 84_LVBus0100926_consumption, 84_LVBus0100928_consumption, 84_LVBus0100930_consumption, 84_LVBus0100932_consumption, 84_LVBus0100935_consumption, 84_LVBus0100937_consumption, 84_LVBus0100939_consumption, 84_LVBus0100940_consumption, 84_LVBus0100941_consumption, 84_LVBus0100944_consumption, 84_LVBus0100945_consumption, 84_LVBus0100947_consumption, 84_LVBus0100950_consumption, 84_LVBus0100962_consumption, 84_LVBus0100963_consumption, 84_LVBus0100964_consumption, 84_LVBus0100965_consumption, 84_LVBus0100966_consumption, 84_LVBus0100967_consumption, 84_LVBus0100969_consumption, 84_LVBus0100984_consumption, 84_LVBus0100986_consumption, 84_LVBus0100987_consumption, 84_LVBus0100988_consumption, 84_LVBus0100989_consumption, 84_LVBus0100990_consumption, 84_LVBus0100991_consumption, 84_LVBus0100994_consumption, 84_LVBus0100996_consumption, 84_LVBus0100997_consumption, 84_LVBus0100999_consumption, 84_LVBus0101000_consumption, 84_LVBus0101004_consumption, 84_LVBus0101007_consumption, 84_LVBus0101008_consumption, 84_LVBus0101010_consumption, 84_LVBus0101014_consumption, 84_LVBus0101016_consumption, 84_LVBus0101018_consumption, 84_LVBus0101029_consumption, 84_LVBus0101030_consumption, 84_LVBus0101036_consumption, 84_LVBus0101038_consumption, 84_LVBus0101041_consumption, 84_LVBus0101046_consumption, 84_LVBus0101055_consumption, 84_LVBus0101056_consumption, 84_LVBus0101057_consumption, 84_LVBus0101060_consumption, 84_LVBus0101061_consumption, 84_LVBus0101065_consumption, 84_LVBus2032689_consumption, 84_LVBus2062023_consumption, 84_LVBus2063424_consumption, 84_LVBus2065571_consumption, 84_LVBus2072645_consumption, 84_LVBus2087486_consumption, 84_LVBus2096033_consumption, 84_LVBus2096034_consumption, 84_LVBus2096035_consumption, 84_LVBus2096036_consumption, 84_LVBus2096037_consumption, 84_LVBus2096038_consumption, 84_LVBus2096039_consumption, 84_LVBus2096041_consumption, 84_LVBus2096042_consumption, 84_LVBus2114845_consumption, 84_LVBus2114846_consumption, 84_LVBus2118443_consumption, 84_LVBus2118445_consumption, 84_LVBus2130199_consumption, 84_LVBus2130201_consumption, 84_LVBus2130202_consumption, 84_LVBus2130203_consumption, 84_LVBus2130204_consumption, 84_LVBus2130205_consumption, 84_LVBus2130206_consumption, 84_LVBus2137917_consumption, 84_LVBus2148146_consumption, 84_LVBus2148148_consumption, 84_LVBus2158473_consumption, 84_LVBus2163420_consumption, 84_LVBus2166446_consumption, 84_LVBus2166447_consumption, 84_LVBus2166448_consumption, 84_LVBus2166449_consumption, 84_LVBus2169893_consumption, 84_LVBus2169894_consumption, 84_LVBus2177092_consumption, 84_LVBus2179742_consumption, 84_LVBus2224840_consumption, 84_LVBus2224842_consumption, 84_LVBus2239741_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  558 group(s) of loads (1116 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  10 group(s) of series lines (21 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  708 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0100529_consumption, 84_LVBus0100529_production, 84_LVBus0100530_consumption, 84_LVBus0100530_production, 84_LVBus0100531_production, 84_LVBus0100532_consumption, 84_LVBus0100532_production, 84_LVBus0100533_production, 84_LVBus0100534_production, 84_LVBus0100535_production, 84_LVBus0100536_consumption, 84_LVBus0100536_production, 84_LVBus0100537_production, 84_LVBus0100542_consumption, 84_LVBus0100542_production, 84_LVBus0100543_production, 84_LVBus0100544_production, 84_LVBus0100545_production, 84_LVBus0100546_production, 84_LVBus0100547_consumption, 84_LVBus0100547_production, 84_LVBus0100548_production, 84_LVBus0100549_production, 84_LVBus0100550_consumption, 84_LVBus0100550_production, 84_LVBus0100551_consumption, 84_LVBus0100551_production, 84_LVBus0100552_production, 84_LVBus0100553_production, 84_LVBus0100554_production, 84_LVBus0100555_production, 84_LVBus0100557_consumption, 84_LVBus0100557_production, 84_LVBus0100558_production, 84_LVBus0100559_production, 84_LVBus0100560_consumption, 84_LVBus0100560_production, 84_LVBus0100561_consumption, 84_LVBus0100561_production, 84_LVBus0100562_consumption, 84_LVBus0100562_production, 84_LVBus0100563_consumption, 84_LVBus0100563_production, 84_LVBus0100564_consumption, 84_LVBus0100564_production, 84_LVBus0100565_production, 84_LVBus0100566_consumption, 84_LVBus0100566_production, 84_LVBus0100567_consumption, 84_LVBus0100567_production, 84_LVBus0100568_consumption, 84_LVBus0100568_production, 84_LVBus0100569_production, 84_LVBus0100570_consumption, 84_LVBus0100570_production, 84_LVBus0100572_production, 84_LVBus0100574_consumption, 84_LVBus0100574_production, 84_LVBus0100575_production, 84_LVBus0100576_production, 84_LVBus0100577_production, 84_LVBus0100579_production, 84_LVBus0100580_production, 84_LVBus0100581_production, 84_LVBus0100582_production, 84_LVBus0100583_production, 84_LVBus0100584_production, 84_LVBus0100586_consumption, 84_LVBus0100586_production, 84_LVBus0100587_production, 84_LVBus0100588_production, 84_LVBus0100589_production, 84_LVBus0100591_production, 84_LVBus0100592_production, 84_LVBus0100593_production, 84_LVBus0100594_consumption, 84_LVBus0100594_production, 84_LVBus0100595_production, 84_LVBus0100596_production, 84_LVBus0100597_production, 84_LVBus0100598_production, 84_LVBus0100599_production, 84_LVBus0100600_consumption, 84_LVBus0100600_production, 84_LVBus0100601_production, 84_LVBus0100602_production, 84_LVBus0100603_production, 84_LVBus0100604_consumption, 84_LVBus0100604_production, 84_LVBus0100605_production, 84_LVBus0100607_consumption, 84_LVBus0100607_production, 84_LVBus0100609_consumption, 84_LVBus0100609_production, 84_LVBus0100610_production, 84_LVBus0100612_production, 84_LVBus0100613_production, 84_LVBus0100614_production, 84_LVBus0100615_production, 84_LVBus0100616_consumption, 84_LVBus0100616_production, 84_LVBus0100617_production, 84_LVBus0100618_consumption, 84_LVBus0100618_production, 84_LVBus0100619_production, 84_LVBus0100620_production, 84_LVBus0100621_consumption, 84_LVBus0100621_production, 84_LVBus0100622_production, 84_LVBus0100623_consumption, 84_LVBus0100623_production, 84_LVBus0100624_production, 84_LVBus0100625_consumption, 84_LVBus0100625_production, 84_LVBus0100626_production, 84_LVBus0100627_production, 84_LVBus0100628_production, 84_LVBus0100632_production, 84_LVBus0100633_production, 84_LVBus0100634_production, 84_LVBus0100635_production, 84_LVBus0100637_production, 84_LVBus0100639_consumption, 84_LVBus0100639_production, 84_LVBus0100641_production, 84_LVBus0100643_production, 84_LVBus0100645_production, 84_LVBus0100647_production, 84_LVBus0100648_production, 84_LVBus0100649_production, 84_LVBus0100650_consumption, 84_LVBus0100650_production, 84_LVBus0100651_production, 84_LVBus0100652_production, 84_LVBus0100654_production, 84_LVBus0100655_production, 84_LVBus0100656_production, 84_LVBus0100657_production, 84_LVBus0100658_production, 84_LVBus0100659_production, 84_LVBus0100660_production, 84_LVBus0100661_production, 84_LVBus0100663_production, 84_LVBus0100664_production, 84_LVBus0100665_production, 84_LVBus0100666_production, 84_LVBus0100667_production, 84_LVBus0100668_production, 84_LVBus0100669_consumption, 84_LVBus0100669_production, 84_LVBus0100670_production, 84_LVBus0100671_production, 84_LVBus0100672_production, 84_LVBus0100673_production, 84_LVBus0100674_production, 84_LVBus0100675_production, 84_LVBus0100676_production, 84_LVBus0100678_consumption, 84_LVBus0100678_production, 84_LVBus0100679_production, 84_LVBus0100680_production, 84_LVBus0100681_production, 84_LVBus0100682_production, 84_LVBus0100683_production, 84_LVBus0100684_production, 84_LVBus0100686_production, 84_LVBus0100687_production, 84_LVBus0100688_production, 84_LVBus0100689_production, 84_LVBus0100690_production, 84_LVBus0100691_production, 84_LVBus0100692_production, 84_LVBus0100693_production, 84_LVBus0100694_production, 84_LVBus0100695_consumption, 84_LVBus0100695_production, 84_LVBus0100696_production, 84_LVBus0100697_production, 84_LVBus0100699_production, 84_LVBus0100700_production, 84_LVBus0100701_production, 84_LVBus0100702_production, 84_LVBus0100703_production, 84_LVBus0100704_production, 84_LVBus0100705_consumption, 84_LVBus0100705_production, 84_LVBus0100706_production, 84_LVBus0100707_production, 84_LVBus0100708_production, 84_LVBus0100709_production, 84_LVBus0100710_production, 84_LVBus0100712_production, 84_LVBus0100713_production, 84_LVBus0100714_production, 84_LVBus0100716_production, 84_LVBus0100717_production, 84_LVBus0100718_consumption, 84_LVBus0100718_production, 84_LVBus0100719_production, 84_LVBus0100720_production, 84_LVBus0100721_production, 84_LVBus0100723_consumption, 84_LVBus0100723_production, 84_LVBus0100724_production, 84_LVBus0100725_production, 84_LVBus0100726_production, 84_LVBus0100728_production, 84_LVBus0100729_consumption, 84_LVBus0100729_production, 84_LVBus0100730_production, 84_LVBus0100731_production, 84_LVBus0100732_production, 84_LVBus0100733_production, 84_LVBus0100734_production, 84_LVBus0100735_production, 84_LVBus0100737_production, 84_LVBus0100738_consumption, 84_LVBus0100738_production, 84_LVBus0100739_production, 84_LVBus0100740_production, 84_LVBus0100741_production, 84_LVBus0100742_consumption, 84_LVBus0100742_production, 84_LVBus0100743_production, 84_LVBus0100744_consumption, 84_LVBus0100744_production, 84_LVBus0100745_consumption, 84_LVBus0100745_production, 84_LVBus0100746_production, 84_LVBus0100747_consumption, 84_LVBus0100747_production, 84_LVBus0100748_consumption, 84_LVBus0100748_production, 84_LVBus0100749_consumption, 84_LVBus0100749_production, 84_LVBus0100750_production, 84_LVBus0100751_production, 84_LVBus0100752_production, 84_LVBus0100755_production, 84_LVBus0100756_production, 84_LVBus0100757_production, 84_LVBus0100758_consumption, 84_LVBus0100758_production, 84_LVBus0100759_production, 84_LVBus0100760_production, 84_LVBus0100761_production, 84_LVBus0100762_production, 84_LVBus0100764_production, 84_LVBus0100765_production, 84_LVBus0100766_production, 84_LVBus0100767_production, 84_LVBus0100768_production, 84_LVBus0100769_production, 84_LVBus0100770_production, 84_LVBus0100771_production, 84_LVBus0100772_production, 84_LVBus0100773_production, 84_LVBus0100775_consumption, 84_LVBus0100775_production, 84_LVBus0100776_consumption, 84_LVBus0100776_production, 84_LVBus0100778_consumption, 84_LVBus0100778_production, 84_LVBus0100779_consumption, 84_LVBus0100779_production, 84_LVBus0100780_production, 84_LVBus0100782_production, 84_LVBus0100783_production, 84_LVBus0100784_consumption, 84_LVBus0100784_production, 84_LVBus0100785_production, 84_LVBus0100786_production, 84_LVBus0100787_production, 84_LVBus0100788_production, 84_LVBus0100789_production, 84_LVBus0100790_production, 84_LVBus0100791_production, 84_LVBus0100793_consumption, 84_LVBus0100793_production, 84_LVBus0100794_consumption, 84_LVBus0100794_production, 84_LVBus0100795_production, 84_LVBus0100796_production, 84_LVBus0100797_production, 84_LVBus0100798_consumption, 84_LVBus0100798_production, 84_LVBus0100799_production, 84_LVBus0100800_production, 84_LVBus0100801_production, 84_LVBus0100802_consumption, 84_LVBus0100802_production, 84_LVBus0100803_production, 84_LVBus0100804_production, 84_LVBus0100805_consumption, 84_LVBus0100805_production, 84_LVBus0100806_production, 84_LVBus0100807_production, 84_LVBus0100808_production, 84_LVBus0100809_consumption, 84_LVBus0100809_production, 84_LVBus0100811_production, 84_LVBus0100812_consumption, 84_LVBus0100812_production, 84_LVBus0100813_consumption, 84_LVBus0100813_production, 84_LVBus0100814_consumption, 84_LVBus0100814_production, 84_LVBus0100815_production, 84_LVBus0100816_production, 84_LVBus0100817_production, 84_LVBus0100819_production, 84_LVBus0100820_consumption, 84_LVBus0100820_production, 84_LVBus0100821_production, 84_LVBus0100822_production, 84_LVBus0100823_production, 84_LVBus0100824_production, 84_LVBus0100825_production, 84_LVBus0100826_production, 84_LVBus0100827_production, 84_LVBus0100828_consumption, 84_LVBus0100828_production, 84_LVBus0100829_consumption, 84_LVBus0100829_production, 84_LVBus0100830_production, 84_LVBus0100831_production, 84_LVBus0100832_production, 84_LVBus0100833_production, 84_LVBus0100834_production, 84_LVBus0100835_consumption, 84_LVBus0100835_production, 84_LVBus0100836_consumption, 84_LVBus0100836_production, 84_LVBus0100837_production, 84_LVBus0100838_production, 84_LVBus0100839_consumption, 84_LVBus0100839_production, 84_LVBus0100840_production, 84_LVBus0100841_production, 84_LVBus0100842_production, 84_LVBus0100848_production, 84_LVBus0100849_consumption, 84_LVBus0100849_production, 84_LVBus0100850_production, 84_LVBus0100851_consumption, 84_LVBus0100851_production, 84_LVBus0100852_production, 84_LVBus0100853_production, 84_LVBus0100854_production, 84_LVBus0100855_production, 84_LVBus0100856_production, 84_LVBus0100857_production, 84_LVBus0100858_consumption, 84_LVBus0100858_production, 84_LVBus0100859_consumption, 84_LVBus0100859_production, 84_LVBus0100860_consumption, 84_LVBus0100860_production, 84_LVBus0100861_production, 84_LVBus0100863_consumption, 84_LVBus0100863_production, 84_LVBus0100865_consumption, 84_LVBus0100865_production, 84_LVBus0100866_production, 84_LVBus0100867_production, 84_LVBus0100868_production, 84_LVBus0100870_consumption, 84_LVBus0100870_production, 84_LVBus0100872_production, 84_LVBus0100873_production, 84_LVBus0100874_consumption, 84_LVBus0100874_production, 84_LVBus0100876_production, 84_LVBus0100877_production, 84_LVBus0100878_consumption, 84_LVBus0100878_production, 84_LVBus0100879_production, 84_LVBus0100880_production, 84_LVBus0100881_production, 84_LVBus0100882_production, 84_LVBus0100884_consumption, 84_LVBus0100884_production, 84_LVBus0100885_production, 84_LVBus0100886_consumption, 84_LVBus0100886_production, 84_LVBus0100887_production, 84_LVBus0100888_production, 84_LVBus0100889_production, 84_LVBus0100891_consumption, 84_LVBus0100891_production, 84_LVBus0100892_production, 84_LVBus0100893_production, 84_LVBus0100894_production, 84_LVBus0100896_production, 84_LVBus0100898_consumption, 84_LVBus0100898_production, 84_LVBus0100899_production, 84_LVBus0100900_production, 84_LVBus0100901_production, 84_LVBus0100902_consumption, 84_LVBus0100902_production, 84_LVBus0100903_consumption, 84_LVBus0100903_production, 84_LVBus0100905_production, 84_LVBus0100906_production, 84_LVBus0100907_production, 84_LVBus0100909_consumption, 84_LVBus0100909_production, 84_LVBus0100911_production, 84_LVBus0100913_production, 84_LVBus0100914_production, 84_LVBus0100915_production, 84_LVBus0100919_production, 84_LVBus0100920_consumption, 84_LVBus0100920_production, 84_LVBus0100921_production, 84_LVBus0100922_production, 84_LVBus0100923_production, 84_LVBus0100924_production, 84_LVBus0100925_production, 84_LVBus0100926_production, 84_LVBus0100928_production, 84_LVBus0100929_consumption, 84_LVBus0100929_production, 84_LVBus0100930_production, 84_LVBus0100931_production, 84_LVBus0100932_production, 84_LVBus0100933_production, 84_LVBus0100935_production, 84_LVBus0100936_production, 84_LVBus0100937_production, 84_LVBus0100939_production, 84_LVBus0100940_production, 84_LVBus0100941_production, 84_LVBus0100942_production, 84_LVBus0100944_production, 84_LVBus0100945_production, 84_LVBus0100946_consumption, 84_LVBus0100946_production, 84_LVBus0100947_production, 84_LVBus0100948_production, 84_LVBus0100949_production, 84_LVBus0100950_production, 84_LVBus0100951_production, 84_LVBus0100952_production, 84_LVBus0100953_consumption, 84_LVBus0100953_production, 84_LVBus0100954_production, 84_LVBus0100956_consumption, 84_LVBus0100956_production, 84_LVBus0100957_production, 84_LVBus0100959_production, 84_LVBus0100960_production, 84_LVBus0100961_consumption, 84_LVBus0100961_production, 84_LVBus0100962_production, 84_LVBus0100963_production, 84_LVBus0100964_production, 84_LVBus0100965_production, 84_LVBus0100966_production, 84_LVBus0100967_production, 84_LVBus0100968_production, 84_LVBus0100969_production, 84_LVBus0100971_production, 84_LVBus0100972_consumption, 84_LVBus0100972_production, 84_LVBus0100974_consumption, 84_LVBus0100974_production, 84_LVBus0100975_consumption, 84_LVBus0100975_production, 84_LVBus0100976_production, 84_LVBus0100977_production, 84_LVBus0100978_consumption, 84_LVBus0100978_production, 84_LVBus0100979_production, 84_LVBus0100981_production, 84_LVBus0100982_consumption, 84_LVBus0100982_production, 84_LVBus0100983_consumption, 84_LVBus0100983_production, 84_LVBus0100984_production, 84_LVBus0100985_production, 84_LVBus0100986_production, 84_LVBus0100987_production, 84_LVBus0100988_production, 84_LVBus0100989_production, 84_LVBus0100990_production, 84_LVBus0100991_production, 84_LVBus0100992_consumption, 84_LVBus0100992_production, 84_LVBus0100993_consumption, 84_LVBus0100993_production, 84_LVBus0100994_production, 84_LVBus0100996_production, 84_LVBus0100997_production, 84_LVBus0100998_production, 84_LVBus0100999_production, 84_LVBus0101000_production, 84_LVBus0101001_consumption, 84_LVBus0101001_production, 84_LVBus0101003_consumption, 84_LVBus0101003_production, 84_LVBus0101004_production, 84_LVBus0101005_consumption, 84_LVBus0101005_production, 84_LVBus0101006_consumption, 84_LVBus0101006_production, 84_LVBus0101007_production, 84_LVBus0101008_production, 84_LVBus0101009_consumption, 84_LVBus0101009_production, 84_LVBus0101010_production, 84_LVBus0101012_production, 84_LVBus0101014_production, 84_LVBus0101015_production, 84_LVBus0101016_production, 84_LVBus0101017_production, 84_LVBus0101018_production, 84_LVBus0101019_production, 84_LVBus0101020_production, 84_LVBus0101021_consumption, 84_LVBus0101021_production, 84_LVBus0101022_consumption, 84_LVBus0101022_production, 84_LVBus0101023_production, 84_LVBus0101024_production, 84_LVBus0101026_production, 84_LVBus0101027_production, 84_LVBus0101028_production, 84_LVBus0101029_production, 84_LVBus0101030_production, 84_LVBus0101034_consumption, 84_LVBus0101034_production, 84_LVBus0101035_production, 84_LVBus0101036_production, 84_LVBus0101037_production, 84_LVBus0101038_production, 84_LVBus0101039_consumption, 84_LVBus0101039_production, 84_LVBus0101040_production, 84_LVBus0101041_production, 84_LVBus0101045_production, 84_LVBus0101046_production, 84_LVBus0101047_consumption, 84_LVBus0101047_production, 84_LVBus0101048_consumption, 84_LVBus0101048_production, 84_LVBus0101050_consumption, 84_LVBus0101050_production, 84_LVBus0101051_production, 84_LVBus0101052_production, 84_LVBus0101053_production, 84_LVBus0101054_consumption, 84_LVBus0101054_production, 84_LVBus0101055_production, 84_LVBus0101056_production, 84_LVBus0101057_production, 84_LVBus0101059_consumption, 84_LVBus0101059_production, 84_LVBus0101060_production, 84_LVBus0101061_production, 84_LVBus0101063_production, 84_LVBus0101064_consumption, 84_LVBus0101064_production, 84_LVBus0101065_production, 84_LVBus0101066_consumption, 84_LVBus0101066_production, 84_LVBus0101067_consumption, 84_LVBus0101067_production, 84_LVBus0101068_production, 84_LVBus0101069_production, 84_LVBus0101070_production, 84_LVBus0101071_production, 84_LVBus0101072_production, 84_LVBus0101073_consumption, 84_LVBus0101073_production, 84_LVBus2027537_consumption, 84_LVBus2027537_production, 84_LVBus2031085_production, 84_LVBus2032689_production, 84_LVBus2032784_consumption, 84_LVBus2032784_production, 84_LVBus2037915_consumption, 84_LVBus2037915_production, 84_LVBus2037916_consumption, 84_LVBus2037916_production, 84_LVBus2062023_production, 84_LVBus2063424_production, 84_LVBus2065571_production, 84_LVBus2070144_consumption, 84_LVBus2070144_production, 84_LVBus2072645_production, 84_LVBus2086266_consumption, 84_LVBus2086266_production, 84_LVBus2087486_production, 84_LVBus2096033_production, 84_LVBus2096034_production, 84_LVBus2096035_production, 84_LVBus2096036_production, 84_LVBus2096037_production, 84_LVBus2096038_production, 84_LVBus2096039_production, 84_LVBus2096040_production, 84_LVBus2096041_production, 84_LVBus2096042_production, 84_LVBus2102037_production, 84_LVBus2111404_production, 84_LVBus2114845_production, 84_LVBus2114846_production, 84_LVBus2116560_production, 84_LVBus2118443_production, 84_LVBus2118444_consumption, 84_LVBus2118444_production, 84_LVBus2118445_production, 84_LVBus2130191_consumption, 84_LVBus2130191_production, 84_LVBus2130192_consumption, 84_LVBus2130192_production, 84_LVBus2130193_production, 84_LVBus2130194_consumption, 84_LVBus2130194_production, 84_LVBus2130195_consumption, 84_LVBus2130195_production, 84_LVBus2130196_consumption, 84_LVBus2130196_production, 84_LVBus2130197_production, 84_LVBus2130198_consumption, 84_LVBus2130198_production, 84_LVBus2130199_production, 84_LVBus2130200_consumption, 84_LVBus2130200_production, 84_LVBus2130201_production, 84_LVBus2130202_production, 84_LVBus2130203_production, 84_LVBus2130204_production, 84_LVBus2130205_production, 84_LVBus2130206_production, 84_LVBus2130207_production, 84_LVBus2130208_consumption, 84_LVBus2130208_production, 84_LVBus2137917_production, 84_LVBus2148145_production, 84_LVBus2148146_production, 84_LVBus2148147_consumption, 84_LVBus2148147_production, 84_LVBus2148148_production, 84_LVBus2148149_consumption, 84_LVBus2148149_production, 84_LVBus2152444_production, 84_LVBus2152445_production, 84_LVBus2152446_consumption, 84_LVBus2152446_production, 84_LVBus2152447_production, 84_LVBus2152448_consumption, 84_LVBus2152448_production, 84_LVBus2152449_production, 84_LVBus2157774_production, 84_LVBus2158473_production, 84_LVBus2163409_consumption, 84_LVBus2163409_production, 84_LVBus2163410_production, 84_LVBus2163419_consumption, 84_LVBus2163419_production, 84_LVBus2163420_production, 84_LVBus2166446_production, 84_LVBus2166447_production, 84_LVBus2166448_production, 84_LVBus2166449_production, 84_LVBus2167934_consumption, 84_LVBus2167934_production, 84_LVBus2169893_production, 84_LVBus2169894_production, 84_LVBus2177092_production, 84_LVBus2179742_production, 84_LVBus2179743_production, 84_LVBus2180919_consumption, 84_LVBus2180919_production, 84_LVBus2180920_consumption, 84_LVBus2180920_production, 84_LVBus2180921_consumption, 84_LVBus2180921_production, 84_LVBus2180922_consumption, 84_LVBus2180922_production, 84_LVBus2180923_consumption, 84_LVBus2180923_production, 84_LVBus2180924_consumption, 84_LVBus2180924_production, 84_LVBus2185070_consumption, 84_LVBus2185070_production, 84_LVBus2197623_consumption, 84_LVBus2197623_production, 84_LVBus2197624_consumption, 84_LVBus2197624_production, 84_LVBus2211004_production, 84_LVBus2224840_production, 84_LVBus2224841_consumption, 84_LVBus2224841_production, 84_LVBus2224842_production, 84_LVBus2239740_consumption, 84_LVBus2239740_production, 84_LVBus2239741_production, 84_LVBus2244470_production, 84_LVBus2245000_production, 84_LVBus2247254_production, 84_LVBus2254135_production, 84_MVLV043772_production, 84_MVLV088557_consumption, 84_MVLV088557_production.

