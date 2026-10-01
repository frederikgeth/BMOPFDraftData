# BMOPF Network Summary: 84_MVFeeder1493

**Generated:** 2026-10-01 23:34:40  
**Findings:** 0 errors · 5 warnings · 213 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 71 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 555 |  |
| line | 483 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 680 | 720.37 kW, 216.1 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 71 |  |
| switch | 0 |  |
| transformer | 71 | Dyn11×71 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 160 | 159 | 32 | 0 |
| LV_236V | 236.0 V | 395 | 324 | 648 | 0 |

**Transformer transitions:**

- `84_MVLV137054_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV154606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV025593_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV088591_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV002226_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV031558_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV033470_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV048624_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV004801_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV033539_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV068062_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV088495_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV070555_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128403_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV092381_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128289_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV090129_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV070939_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV055698_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV007809_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV137002_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV122951_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV136138_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV122905_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV019420_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV122496_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV049180_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV024947_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV025107_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV090325_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV154579_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV003098_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV136975_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV127473_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV033341_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV137375_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV135216_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128404_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV141646_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV092317_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV091657_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV111113_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV029968_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV049920_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044295_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV022087_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV150849_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV002228_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV041044_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV025609_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV125611_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV152614_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV049623_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128292_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128398_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV049199_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV136933_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV068692_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV060125_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV003097_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044220_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV072854_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV006440_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV135220_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV014960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV123001_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV033041_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV122981_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044314_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV090549_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV145171_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 196 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 555 | 1 | 554 | 0 | 0 | 0 |
| Tier LV_236V | 395 | 71 | 324 | 0 | 0 | 0 |
| Tier MV_11.8kV | 160 | 1 | 159 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 71; skipped invalid branches: 0.

Galvanic zones: 72; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_DONJO | MV_11.8kV | 160 | 0 | 0 | 71 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2060 declared bus terminals; 1773 mapped line/closed-switch conductor edges; 287 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 12300.0 | 3.388 | 2040 |
| q_nom | 0.0 | 3680.0 | 3.388 | 2040 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.5 | 2010.0 | 1.245 | 483 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 275000.0 | 0.246 | 71 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 454 of 680 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048924_consumption' has phase imbalance of 34.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048922_consumption' has phase imbalance of 258.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048871_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2014150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048722_consumption' has phase imbalance of 149.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048925_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049023_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048820_consumption' has phase imbalance of 232.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048755_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049056_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048958_consumption' has phase imbalance of 249.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049135_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048954_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049051_consumption' has phase imbalance of 72.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048898_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048997_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048959_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048727_consumption' has phase imbalance of 226.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049100_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2014473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048993_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2011881_consumption' has phase imbalance of 222.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048979_consumption' has phase imbalance of 249.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048706_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048912_consumption' has phase imbalance of 290.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048781_consumption' has phase imbalance of 272.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048785_consumption' has phase imbalance of 79.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048857_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048903_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048905_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048946_consumption' has phase imbalance of 150.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048730_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048845_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048746_consumption' has phase imbalance of 261.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048877_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049067_consumption' has phase imbalance of 255.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049035_consumption' has phase imbalance of 228.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048801_consumption' has phase imbalance of 135.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049068_consumption' has phase imbalance of 93.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048777_consumption' has phase imbalance of 288.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048928_consumption' has phase imbalance of 280.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048940_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048947_consumption' has phase imbalance of 37.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048992_consumption' has phase imbalance of 266.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2010937_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048878_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049005_consumption' has phase imbalance of 98.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048995_consumption' has phase imbalance of 209.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048916_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049103_consumption' has phase imbalance of 42.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048792_consumption' has phase imbalance of 207.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048806_consumption' has phase imbalance of 254.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048982_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048994_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2011880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049085_consumption' has phase imbalance of 57.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2009563_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048970_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048740_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048759_consumption' has phase imbalance of 28.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049014_consumption' has phase imbalance of 21.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048742_consumption' has phase imbalance of 296.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048936_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048921_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048708_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048716_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048724_consumption' has phase imbalance of 287.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048930_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049090_consumption' has phase imbalance of 203.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2010543_consumption' has phase imbalance of 285.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048784_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2010938_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048719_consumption' has phase imbalance of 194.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2009564_consumption' has phase imbalance of 271.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048931_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049021_consumption' has phase imbalance of 158.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048697_consumption' has phase imbalance of 296.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049080_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048891_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049047_consumption' has phase imbalance of 247.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2014474_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048825_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049041_consumption' has phase imbalance of 120.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048819_consumption' has phase imbalance of 136.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048952_consumption' has phase imbalance of 238.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2009562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048926_consumption' has phase imbalance of 29.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049116_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048802_consumption' has phase imbalance of 265.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048829_consumption' has phase imbalance of 217.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2010936_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049101_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048934_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048910_consumption' has phase imbalance of 186.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2009561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2009672_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048841_consumption' has phase imbalance of 207.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048747_consumption' has phase imbalance of 274.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048731_consumption' has phase imbalance of 278.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049129_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048899_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048990_consumption' has phase imbalance of 266.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048748_consumption' has phase imbalance of 283.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048796_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049134_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048935_consumption' has phase imbalance of 296.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2012919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048723_consumption' has phase imbalance of 84.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048789_consumption' has phase imbalance of 147.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048942_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048701_consumption' has phase imbalance of 182.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049087_consumption' has phase imbalance of 290.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048981_consumption' has phase imbalance of 278.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049091_consumption' has phase imbalance of 254.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048909_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0049054_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0048773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 680 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0048880' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0049072' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 720.37 kW |
| Total load Q | 216.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV137054_Transformer | 110.0 kVA | 5.6% |
| 84_MVLV154606_Transformer | 110.0 kVA | 1.8% |
| 84_MVLV025593_Transformer | 110.0 kVA | 4.3% |
| 84_MVLV088591_Transformer | 110.0 kVA | 1.0% |
| 84_MVLV002226_Transformer | 110.0 kVA | 25.6% |
| 84_MVLV031558_Transformer | 110.0 kVA | 0.5% |
| 84_MVLV033470_Transformer | 110.0 kVA | 7.7% |
| 84_MVLV048624_Transformer | 110.0 kVA | 0.2% |
| 84_MVLV004801_Transformer | 110.0 kVA | 7.1% |
| 84_MVLV033539_Transformer | 110.0 kVA | 23.9% |
| 84_MVLV068062_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV088495_Transformer | 275.0 kVA | 38.9% |
| 84_MVLV070555_Transformer | 110.0 kVA | 5.9% |
| 84_MVLV128403_Transformer | 110.0 kVA | 4.8% |
| 84_MVLV092381_Transformer | 275.0 kVA | 41.0% |
| 84_MVLV128289_Transformer | 110.0 kVA | 12.5% |
| 84_MVLV090129_Transformer | 110.0 kVA | 2.9% |
| 84_MVLV070939_Transformer | 110.0 kVA | 0.3% |
| 84_MVLV055698_Transformer | 110.0 kVA | 9.3% |
| 84_MVLV007809_Transformer | 110.0 kVA | 1.8% |
| 84_MVLV137002_Transformer | 110.0 kVA | 2.8% |
| 84_MVLV122951_Transformer | 110.0 kVA | 4.4% |
| 84_MVLV136138_Transformer | 110.0 kVA | 6.6% |
| 84_MVLV122905_Transformer | 110.0 kVA | 8.2% |
| 84_MVLV019420_Transformer | 110.0 kVA | 6.8% |
| 84_MVLV122496_Transformer | 110.0 kVA | 1.6% |
| 84_MVLV049180_Transformer | 110.0 kVA | 5.7% |
| 84_MVLV024947_Transformer | 110.0 kVA | 7.5% |
| 84_MVLV025107_Transformer | 110.0 kVA | 7.0% |
| 84_MVLV090325_Transformer | 110.0 kVA | 2.5% |
| 84_MVLV154579_Transformer | 110.0 kVA | 7.3% |
| 84_MVLV003098_Transformer | 110.0 kVA | 5.2% |
| 84_MVLV136975_Transformer | 110.0 kVA | 1.6% |
| 84_MVLV127473_Transformer | 110.0 kVA | 3.3% |
| 84_MVLV033341_Transformer | 110.0 kVA | 6.8% |
| 84_MVLV137375_Transformer | 110.0 kVA | 2.4% |
| 84_MVLV135216_Transformer | 110.0 kVA | 1.2% |
| 84_MVLV128404_Transformer | 110.0 kVA | 1.5% |
| 84_MVLV141646_Transformer | 110.0 kVA | 10.8% |
| 84_MVLV092317_Transformer | 110.0 kVA | 6.7% |
| 84_MVLV091657_Transformer | 110.0 kVA | 4.4% |
| 84_MVLV111113_Transformer | 110.0 kVA | 7.1% |
| 84_MVLV029968_Transformer | 110.0 kVA | 0.2% |
| 84_MVLV049920_Transformer | 110.0 kVA | 7.8% |
| 84_MVLV044295_Transformer | 110.0 kVA | 14.2% |
| 84_MVLV022087_Transformer | 110.0 kVA | 6.1% |
| 84_MVLV150849_Transformer | 110.0 kVA | 7.9% |
| 84_MVLV002228_Transformer | 110.0 kVA | 5.0% |
| 84_MVLV041044_Transformer | 110.0 kVA | 14.7% |
| 84_MVLV025609_Transformer | 110.0 kVA | 13.3% |
| 84_MVLV125611_Transformer | 110.0 kVA | 14.8% |
| 84_MVLV152614_Transformer | 110.0 kVA | 8.7% |
| 84_MVLV049623_Transformer | 110.0 kVA | 4.0% |
| 84_MVLV128292_Transformer | 110.0 kVA | 30.2% |
| 84_MVLV128398_Transformer | 110.0 kVA | 2.1% |
| 84_MVLV049199_Transformer | 110.0 kVA | 3.5% |
| 84_MVLV136933_Transformer | 110.0 kVA | 3.2% |
| 84_MVLV068692_Transformer | 110.0 kVA | 3.5% |
| 84_MVLV060125_Transformer | 110.0 kVA | 4.7% |
| 84_MVLV003097_Transformer | 110.0 kVA | 1.1% |
| 84_MVLV044220_Transformer | 110.0 kVA | 0.7% |
| 84_MVLV072854_Transformer | 110.0 kVA | 1.3% |
| 84_MVLV006440_Transformer | 110.0 kVA | 34.0% |
| 84_MVLV135220_Transformer | 110.0 kVA | 11.0% |
| 84_MVLV014960_Transformer | 110.0 kVA | 19.1% |
| 84_MVLV123001_Transformer | 110.0 kVA | 3.6% |
| 84_MVLV033041_Transformer | 110.0 kVA | 7.7% |
| 84_MVLV122981_Transformer | 110.0 kVA | 7.2% |
| 84_MVLV044314_Transformer | 110.0 kVA | 18.3% |
| 84_MVLV090549_Transformer | 110.0 kVA | 6.8% |
| 84_MVLV145171_Transformer | 110.0 kVA | 2.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.72 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_DONJO' (MV, 11.78 kV) has an electrical reach of 20.05 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0048706' (LV, 0.24 kV) has an electrical reach of 16.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0049005' (LV, 0.24 kV) has an electrical reach of 27.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0048798' (LV, 0.24 kV) has an electrical reach of 6.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 555 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 555 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 71 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 160 |
| LV_236V | 4-wire | 395 / 395 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 395 |
| Neutral branches | 324 |
| Grounding points | 71 |
| Neutral sections | 71 |
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
| 11.78 kV | 160 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 72 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2780.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 395 / 160 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 455 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 455 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0048696_consumption, 84_LVBus0048696_production, 84_LVBus0048697_production, 84_LVBus0048698_consumption, 84_LVBus0048698_production, 84_LVBus0048699_production, 84_LVBus0048700_consumption, 84_LVBus0048700_production, 84_LVBus0048701_production, 84_LVBus0048702_production, 84_LVBus0048706_production, 84_LVBus0048708_production, 84_LVBus0048710_production, 84_LVBus0048711_production, 84_LVBus0048712_production, 84_LVBus0048716_production, 84_LVBus0048717_consumption, 84_LVBus0048717_production, 84_LVBus0048718_production, 84_LVBus0048719_production, 84_LVBus0048721_production, 84_LVBus0048722_production, 84_LVBus0048723_production, 84_LVBus0048724_production, 84_LVBus0048725_production, 84_LVBus0048726_production, 84_LVBus0048727_production, 84_LVBus0048728_consumption, 84_LVBus0048728_production, 84_LVBus0048729_consumption, 84_LVBus0048729_production, 84_LVBus0048730_production, 84_LVBus0048731_production, 84_LVBus0048735_production, 84_LVBus0048737_consumption, 84_LVBus0048737_production, 84_LVBus0048738_consumption, 84_LVBus0048738_production, 84_LVBus0048739_production, 84_LVBus0048740_production, 84_LVBus0048741_production, 84_LVBus0048742_production, 84_LVBus0048743_consumption, 84_LVBus0048743_production, 84_LVBus0048744_production, 84_LVBus0048745_production, 84_LVBus0048746_production, 84_LVBus0048747_production, 84_LVBus0048748_production, 84_LVBus0048752_consumption, 84_LVBus0048752_production, 84_LVBus0048753_consumption, 84_LVBus0048753_production, 84_LVBus0048754_production, 84_LVBus0048755_production, 84_LVBus0048756_consumption, 84_LVBus0048756_production, 84_LVBus0048757_consumption, 84_LVBus0048757_production, 84_LVBus0048758_consumption, 84_LVBus0048758_production, 84_LVBus0048759_production, 84_LVBus0048761_consumption, 84_LVBus0048761_production, 84_LVBus0048763_consumption, 84_LVBus0048763_production, 84_LVBus0048765_consumption, 84_LVBus0048765_production, 84_LVBus0048766_production, 84_LVBus0048767_consumption, 84_LVBus0048767_production, 84_LVBus0048768_consumption, 84_LVBus0048768_production, 84_LVBus0048769_production, 84_LVBus0048770_consumption, 84_LVBus0048770_production, 84_LVBus0048771_production, 84_LVBus0048772_production, 84_LVBus0048773_production, 84_LVBus0048777_production, 84_LVBus0048779_production, 84_LVBus0048781_production, 84_LVBus0048783_consumption, 84_LVBus0048783_production, 84_LVBus0048784_production, 84_LVBus0048785_production, 84_LVBus0048789_production, 84_LVBus0048790_consumption, 84_LVBus0048790_production, 84_LVBus0048791_consumption, 84_LVBus0048791_production, 84_LVBus0048792_production, 84_LVBus0048796_production, 84_LVBus0048798_production, 84_LVBus0048800_consumption, 84_LVBus0048800_production, 84_LVBus0048801_production, 84_LVBus0048802_production, 84_LVBus0048806_production, 84_LVBus0048807_production, 84_LVBus0048808_production, 84_LVBus0048812_consumption, 84_LVBus0048812_production, 84_LVBus0048813_production, 84_LVBus0048814_production, 84_LVBus0048818_consumption, 84_LVBus0048818_production, 84_LVBus0048819_production, 84_LVBus0048820_production, 84_LVBus0048821_production, 84_LVBus0048824_consumption, 84_LVBus0048824_production, 84_LVBus0048825_production, 84_LVBus0048826_production, 84_LVBus0048827_production, 84_LVBus0048828_production, 84_LVBus0048829_production, 84_LVBus0048830_consumption, 84_LVBus0048830_production, 84_LVBus0048834_consumption, 84_LVBus0048834_production, 84_LVBus0048835_consumption, 84_LVBus0048835_production, 84_LVBus0048836_production, 84_LVBus0048840_consumption, 84_LVBus0048840_production, 84_LVBus0048841_production, 84_LVBus0048842_production, 84_LVBus0048843_consumption, 84_LVBus0048843_production, 84_LVBus0048845_production, 84_LVBus0048849_production, 84_LVBus0048851_production, 84_LVBus0048852_production, 84_LVBus0048853_consumption, 84_LVBus0048853_production, 84_LVBus0048854_consumption, 84_LVBus0048854_production, 84_LVBus0048855_consumption, 84_LVBus0048855_production, 84_LVBus0048856_production, 84_LVBus0048857_production, 84_LVBus0048859_consumption, 84_LVBus0048859_production, 84_LVBus0048860_production, 84_LVBus0048861_production, 84_LVBus0048865_consumption, 84_LVBus0048865_production, 84_LVBus0048866_production, 84_LVBus0048867_consumption, 84_LVBus0048867_production, 84_LVBus0048871_production, 84_LVBus0048873_consumption, 84_LVBus0048873_production, 84_LVBus0048874_consumption, 84_LVBus0048874_production, 84_LVBus0048875_production, 84_LVBus0048876_consumption, 84_LVBus0048876_production, 84_LVBus0048877_production, 84_LVBus0048878_production, 84_LVBus0048880_production, 84_LVBus0048882_consumption, 84_LVBus0048882_production, 84_LVBus0048884_production, 84_LVBus0048886_consumption, 84_LVBus0048886_production, 84_LVBus0048887_consumption, 84_LVBus0048887_production, 84_LVBus0048890_consumption, 84_LVBus0048890_production, 84_LVBus0048891_production, 84_LVBus0048892_production, 84_LVBus0048893_consumption, 84_LVBus0048893_production, 84_LVBus0048895_production, 84_LVBus0048896_consumption, 84_LVBus0048896_production, 84_LVBus0048897_production, 84_LVBus0048898_production, 84_LVBus0048899_production, 84_LVBus0048903_production, 84_LVBus0048905_production, 84_LVBus0048907_consumption, 84_LVBus0048907_production, 84_LVBus0048908_production, 84_LVBus0048909_production, 84_LVBus0048910_production, 84_LVBus0048911_production, 84_LVBus0048912_production, 84_LVBus0048913_production, 84_LVBus0048914_production, 84_LVBus0048915_production, 84_LVBus0048916_production, 84_LVBus0048917_consumption, 84_LVBus0048917_production, 84_LVBus0048919_production, 84_LVBus0048920_production, 84_LVBus0048921_production, 84_LVBus0048922_production, 84_LVBus0048923_production, 84_LVBus0048924_production, 84_LVBus0048925_production, 84_LVBus0048926_production, 84_LVBus0048927_production, 84_LVBus0048928_production, 84_LVBus0048929_production, 84_LVBus0048930_production, 84_LVBus0048931_production, 84_LVBus0048932_production, 84_LVBus0048933_consumption, 84_LVBus0048933_production, 84_LVBus0048934_production, 84_LVBus0048935_production, 84_LVBus0048936_production, 84_LVBus0048938_consumption, 84_LVBus0048938_production, 84_LVBus0048939_production, 84_LVBus0048940_production, 84_LVBus0048942_production, 84_LVBus0048944_consumption, 84_LVBus0048944_production, 84_LVBus0048945_consumption, 84_LVBus0048945_production, 84_LVBus0048946_production, 84_LVBus0048947_production, 84_LVBus0048951_consumption, 84_LVBus0048951_production, 84_LVBus0048952_production, 84_LVBus0048954_production, 84_LVBus0048955_consumption, 84_LVBus0048955_production, 84_LVBus0048956_consumption, 84_LVBus0048956_production, 84_LVBus0048957_consumption, 84_LVBus0048957_production, 84_LVBus0048958_production, 84_LVBus0048959_production, 84_LVBus0048963_consumption, 84_LVBus0048963_production, 84_LVBus0048964_production, 84_LVBus0048965_consumption, 84_LVBus0048965_production, 84_LVBus0048967_production, 84_LVBus0048969_production, 84_LVBus0048970_production, 84_LVBus0048972_production, 84_LVBus0048974_consumption, 84_LVBus0048974_production, 84_LVBus0048975_production, 84_LVBus0048977_production, 84_LVBus0048979_production, 84_LVBus0048980_production, 84_LVBus0048981_production, 84_LVBus0048982_production, 84_LVBus0048983_consumption, 84_LVBus0048983_production, 84_LVBus0048984_consumption, 84_LVBus0048984_production, 84_LVBus0048985_production, 84_LVBus0048986_production, 84_LVBus0048988_production, 84_LVBus0048989_production, 84_LVBus0048990_production, 84_LVBus0048991_production, 84_LVBus0048992_production, 84_LVBus0048993_production, 84_LVBus0048994_production, 84_LVBus0048995_production, 84_LVBus0048997_production, 84_LVBus0048998_production, 84_LVBus0048999_production, 84_LVBus0049003_consumption, 84_LVBus0049003_production, 84_LVBus0049005_production, 84_LVBus0049007_production, 84_LVBus0049008_consumption, 84_LVBus0049008_production, 84_LVBus0049009_production, 84_LVBus0049013_consumption, 84_LVBus0049013_production, 84_LVBus0049014_production, 84_LVBus0049015_production, 84_LVBus0049016_production, 84_LVBus0049017_production, 84_LVBus0049021_production, 84_LVBus0049023_production, 84_LVBus0049024_production, 84_LVBus0049025_consumption, 84_LVBus0049025_production, 84_LVBus0049026_consumption, 84_LVBus0049026_production, 84_LVBus0049027_consumption, 84_LVBus0049027_production, 84_LVBus0049029_production, 84_LVBus0049033_production, 84_LVBus0049035_production, 84_LVBus0049036_consumption, 84_LVBus0049036_production, 84_LVBus0049037_consumption, 84_LVBus0049037_production, 84_LVBus0049038_production, 84_LVBus0049039_production, 84_LVBus0049041_production, 84_LVBus0049045_consumption, 84_LVBus0049045_production, 84_LVBus0049046_production, 84_LVBus0049047_production, 84_LVBus0049049_production, 84_LVBus0049051_production, 84_LVBus0049052_production, 84_LVBus0049054_production, 84_LVBus0049056_production, 84_LVBus0049058_consumption, 84_LVBus0049058_production, 84_LVBus0049059_consumption, 84_LVBus0049059_production, 84_LVBus0049060_production, 84_LVBus0049061_production, 84_LVBus0049062_production, 84_LVBus0049063_production, 84_LVBus0049064_consumption, 84_LVBus0049064_production, 84_LVBus0049065_consumption, 84_LVBus0049065_production, 84_LVBus0049066_production, 84_LVBus0049067_production, 84_LVBus0049068_production, 84_LVBus0049072_production, 84_LVBus0049074_production, 84_LVBus0049076_production, 84_LVBus0049078_consumption, 84_LVBus0049078_production, 84_LVBus0049079_production, 84_LVBus0049080_production, 84_LVBus0049084_consumption, 84_LVBus0049084_production, 84_LVBus0049085_production, 84_LVBus0049087_production, 84_LVBus0049089_consumption, 84_LVBus0049089_production, 84_LVBus0049090_production, 84_LVBus0049091_production, 84_LVBus0049095_production, 84_LVBus0049097_production, 84_LVBus0049099_production, 84_LVBus0049100_production, 84_LVBus0049101_production, 84_LVBus0049102_production, 84_LVBus0049103_production, 84_LVBus0049104_production, 84_LVBus0049108_production, 84_LVBus0049110_production, 84_LVBus0049112_production, 84_LVBus0049114_consumption, 84_LVBus0049114_production, 84_LVBus0049115_production, 84_LVBus0049116_production, 84_LVBus0049117_consumption, 84_LVBus0049117_production, 84_LVBus0049118_consumption, 84_LVBus0049118_production, 84_LVBus0049119_consumption, 84_LVBus0049119_production, 84_LVBus0049120_production, 84_LVBus0049121_consumption, 84_LVBus0049121_production, 84_LVBus0049122_production, 84_LVBus0049123_production, 84_LVBus0049127_consumption, 84_LVBus0049127_production, 84_LVBus0049128_production, 84_LVBus0049129_production, 84_LVBus0049133_consumption, 84_LVBus0049133_production, 84_LVBus0049134_production, 84_LVBus0049135_production, 84_LVBus0049136_consumption, 84_LVBus0049136_production, 84_LVBus0049140_consumption, 84_LVBus0049140_production, 84_LVBus0049141_consumption, 84_LVBus0049141_production, 84_LVBus0049142_consumption, 84_LVBus0049142_production, 84_LVBus0049143_consumption, 84_LVBus0049143_production, 84_LVBus0049144_production, 84_LVBus2008394_consumption, 84_LVBus2008394_production, 84_LVBus2009560_consumption, 84_LVBus2009560_production, 84_LVBus2009561_production, 84_LVBus2009562_production, 84_LVBus2009563_production, 84_LVBus2009564_production, 84_LVBus2009672_production, 84_LVBus2009690_consumption, 84_LVBus2009690_production, 84_LVBus2010543_production, 84_LVBus2010936_production, 84_LVBus2010937_production, 84_LVBus2010938_production, 84_LVBus2011465_consumption, 84_LVBus2011465_production, 84_LVBus2011879_consumption, 84_LVBus2011879_production, 84_LVBus2011880_production, 84_LVBus2011881_production, 84_LVBus2012306_production, 84_LVBus2012919_production, 84_LVBus2013063_consumption, 84_LVBus2013063_production, 84_LVBus2013260_consumption, 84_LVBus2013260_production, 84_LVBus2014150_production, 84_LVBus2014472_consumption, 84_LVBus2014472_production, 84_LVBus2014473_production, 84_LVBus2014474_production, 84_LVBus2017720_production, 84_LVBus2020906_consumption, 84_LVBus2020906_production, 84_MVLV003074_consumption, 84_MVLV003074_production, 84_MVLV005118_consumption, 84_MVLV005118_production, 84_MVLV007654_consumption, 84_MVLV007654_production, 84_MVLV028854_consumption, 84_MVLV028854_production, 84_MVLV031539_consumption, 84_MVLV031539_production, 84_MVLV032213_consumption, 84_MVLV032213_production, 84_MVLV052912_consumption, 84_MVLV052912_production, 84_MVLV058900_consumption, 84_MVLV058900_production, 84_MVLV059069_consumption, 84_MVLV059069_production, 84_MVLV070103_consumption, 84_MVLV070103_production, 84_MVLV093311_consumption, 84_MVLV093311_production, 84_MVLV095072_consumption, 84_MVLV095072_production, 84_MVLV099107_consumption, 84_MVLV099107_production, 84_MVLV147115_consumption, 84_MVLV147115_production, 84_MVLV150531_consumption, 84_MVLV150531_production, 84_MVLV153876_consumption, 84_MVLV153876_production.

## 9. Data Quality Summary

**Total findings:** 218 (0 errors, 5 warnings, 213 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  454 of 680 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.72 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  455 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049144_consumption`  
  Load '84_LVBus0049144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048985_consumption`  
  Load '84_LVBus0048985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048754_consumption`  
  Load '84_LVBus0048754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048924_consumption`  
  Load '84_LVBus0048924_consumption' has phase imbalance of 34.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048922_consumption`  
  Load '84_LVBus0048922_consumption' has phase imbalance of 258.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048871_consumption`  
  Load '84_LVBus0048871_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049017_consumption`  
  Load '84_LVBus0049017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2014150_consumption`  
  Load '84_LVBus2014150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048914_consumption`  
  Load '84_LVBus0048914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048722_consumption`  
  Load '84_LVBus0048722_consumption' has phase imbalance of 149.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048925_consumption`  
  Load '84_LVBus0048925_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049023_consumption`  
  Load '84_LVBus0049023_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048820_consumption`  
  Load '84_LVBus0048820_consumption' has phase imbalance of 232.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048755_consumption`  
  Load '84_LVBus0048755_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048769_consumption`  
  Load '84_LVBus0048769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049056_consumption`  
  Load '84_LVBus0049056_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048958_consumption`  
  Load '84_LVBus0048958_consumption' has phase imbalance of 249.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049049_consumption`  
  Load '84_LVBus0049049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049060_consumption`  
  Load '84_LVBus0049060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049135_consumption`  
  Load '84_LVBus0049135_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048954_consumption`  
  Load '84_LVBus0048954_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049051_consumption`  
  Load '84_LVBus0049051_consumption' has phase imbalance of 72.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048852_consumption`  
  Load '84_LVBus0048852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048929_consumption`  
  Load '84_LVBus0048929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048766_consumption`  
  Load '84_LVBus0048766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048898_consumption`  
  Load '84_LVBus0048898_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048908_consumption`  
  Load '84_LVBus0048908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048997_consumption`  
  Load '84_LVBus0048997_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048851_consumption`  
  Load '84_LVBus0048851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049063_consumption`  
  Load '84_LVBus0049063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048959_consumption`  
  Load '84_LVBus0048959_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048727_consumption`  
  Load '84_LVBus0048727_consumption' has phase imbalance of 226.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049100_consumption`  
  Load '84_LVBus0049100_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2014473_consumption`  
  Load '84_LVBus2014473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048993_consumption`  
  Load '84_LVBus0048993_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2011881_consumption`  
  Load '84_LVBus2011881_consumption' has phase imbalance of 222.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048979_consumption`  
  Load '84_LVBus0048979_consumption' has phase imbalance of 249.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048706_consumption`  
  Load '84_LVBus0048706_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048895_consumption`  
  Load '84_LVBus0048895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048911_consumption`  
  Load '84_LVBus0048911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048860_consumption`  
  Load '84_LVBus0048860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048912_consumption`  
  Load '84_LVBus0048912_consumption' has phase imbalance of 290.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048781_consumption`  
  Load '84_LVBus0048781_consumption' has phase imbalance of 272.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048785_consumption`  
  Load '84_LVBus0048785_consumption' has phase imbalance of 79.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048857_consumption`  
  Load '84_LVBus0048857_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048915_consumption`  
  Load '84_LVBus0048915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048903_consumption`  
  Load '84_LVBus0048903_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048905_consumption`  
  Load '84_LVBus0048905_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048946_consumption`  
  Load '84_LVBus0048946_consumption' has phase imbalance of 150.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048730_consumption`  
  Load '84_LVBus0048730_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048726_consumption`  
  Load '84_LVBus0048726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048845_consumption`  
  Load '84_LVBus0048845_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048746_consumption`  
  Load '84_LVBus0048746_consumption' has phase imbalance of 261.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048877_consumption`  
  Load '84_LVBus0048877_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049067_consumption`  
  Load '84_LVBus0049067_consumption' has phase imbalance of 255.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049035_consumption`  
  Load '84_LVBus0049035_consumption' has phase imbalance of 228.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048801_consumption`  
  Load '84_LVBus0048801_consumption' has phase imbalance of 135.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048813_consumption`  
  Load '84_LVBus0048813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048927_consumption`  
  Load '84_LVBus0048927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049068_consumption`  
  Load '84_LVBus0049068_consumption' has phase imbalance of 93.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048777_consumption`  
  Load '84_LVBus0048777_consumption' has phase imbalance of 288.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049038_consumption`  
  Load '84_LVBus0049038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049112_consumption`  
  Load '84_LVBus0049112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048928_consumption`  
  Load '84_LVBus0048928_consumption' has phase imbalance of 280.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048940_consumption`  
  Load '84_LVBus0048940_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048947_consumption`  
  Load '84_LVBus0048947_consumption' has phase imbalance of 37.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049039_consumption`  
  Load '84_LVBus0049039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048992_consumption`  
  Load '84_LVBus0048992_consumption' has phase imbalance of 266.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2010937_consumption`  
  Load '84_LVBus2010937_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048932_consumption`  
  Load '84_LVBus0048932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048878_consumption`  
  Load '84_LVBus0048878_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049005_consumption`  
  Load '84_LVBus0049005_consumption' has phase imbalance of 98.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049016_consumption`  
  Load '84_LVBus0049016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049097_consumption`  
  Load '84_LVBus0049097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048995_consumption`  
  Load '84_LVBus0048995_consumption' has phase imbalance of 209.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048916_consumption`  
  Load '84_LVBus0048916_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048735_consumption`  
  Load '84_LVBus0048735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049123_consumption`  
  Load '84_LVBus0049123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049103_consumption`  
  Load '84_LVBus0049103_consumption' has phase imbalance of 42.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048986_consumption`  
  Load '84_LVBus0048986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049052_consumption`  
  Load '84_LVBus0049052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048861_consumption`  
  Load '84_LVBus0048861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049009_consumption`  
  Load '84_LVBus0049009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048792_consumption`  
  Load '84_LVBus0048792_consumption' has phase imbalance of 207.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048919_consumption`  
  Load '84_LVBus0048919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048806_consumption`  
  Load '84_LVBus0048806_consumption' has phase imbalance of 254.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048982_consumption`  
  Load '84_LVBus0048982_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048994_consumption`  
  Load '84_LVBus0048994_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048712_consumption`  
  Load '84_LVBus0048712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2011880_consumption`  
  Load '84_LVBus2011880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049062_consumption`  
  Load '84_LVBus0049062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048923_consumption`  
  Load '84_LVBus0048923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048744_consumption`  
  Load '84_LVBus0048744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049085_consumption`  
  Load '84_LVBus0049085_consumption' has phase imbalance of 57.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048856_consumption`  
  Load '84_LVBus0048856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2009563_consumption`  
  Load '84_LVBus2009563_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048827_consumption`  
  Load '84_LVBus0048827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048970_consumption`  
  Load '84_LVBus0048970_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048740_consumption`  
  Load '84_LVBus0048740_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048808_consumption`  
  Load '84_LVBus0048808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048721_consumption`  
  Load '84_LVBus0048721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049120_consumption`  
  Load '84_LVBus0049120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048826_consumption`  
  Load '84_LVBus0048826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048759_consumption`  
  Load '84_LVBus0048759_consumption' has phase imbalance of 28.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048745_consumption`  
  Load '84_LVBus0048745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049014_consumption`  
  Load '84_LVBus0049014_consumption' has phase imbalance of 21.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048977_consumption`  
  Load '84_LVBus0048977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048742_consumption`  
  Load '84_LVBus0048742_consumption' has phase imbalance of 296.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048936_consumption`  
  Load '84_LVBus0048936_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048921_consumption`  
  Load '84_LVBus0048921_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048708_consumption`  
  Load '84_LVBus0048708_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048716_consumption`  
  Load '84_LVBus0048716_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048724_consumption`  
  Load '84_LVBus0048724_consumption' has phase imbalance of 287.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048930_consumption`  
  Load '84_LVBus0048930_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048725_consumption`  
  Load '84_LVBus0048725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048989_consumption`  
  Load '84_LVBus0048989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048771_consumption`  
  Load '84_LVBus0048771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049090_consumption`  
  Load '84_LVBus0049090_consumption' has phase imbalance of 203.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048866_consumption`  
  Load '84_LVBus0048866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2010543_consumption`  
  Load '84_LVBus2010543_consumption' has phase imbalance of 285.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049061_consumption`  
  Load '84_LVBus0049061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048784_consumption`  
  Load '84_LVBus0048784_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048913_consumption`  
  Load '84_LVBus0048913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2010938_consumption`  
  Load '84_LVBus2010938_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048719_consumption`  
  Load '84_LVBus0048719_consumption' has phase imbalance of 194.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2009564_consumption`  
  Load '84_LVBus2009564_consumption' has phase imbalance of 271.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048999_consumption`  
  Load '84_LVBus0048999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048931_consumption`  
  Load '84_LVBus0048931_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049021_consumption`  
  Load '84_LVBus0049021_consumption' has phase imbalance of 158.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048697_consumption`  
  Load '84_LVBus0048697_consumption' has phase imbalance of 296.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049080_consumption`  
  Load '84_LVBus0049080_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048772_consumption`  
  Load '84_LVBus0048772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048891_consumption`  
  Load '84_LVBus0048891_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049047_consumption`  
  Load '84_LVBus0049047_consumption' has phase imbalance of 247.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2014474_consumption`  
  Load '84_LVBus2014474_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048825_consumption`  
  Load '84_LVBus0048825_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049029_consumption`  
  Load '84_LVBus0049029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049041_consumption`  
  Load '84_LVBus0049041_consumption' has phase imbalance of 120.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048836_consumption`  
  Load '84_LVBus0048836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048819_consumption`  
  Load '84_LVBus0048819_consumption' has phase imbalance of 136.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048741_consumption`  
  Load '84_LVBus0048741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048952_consumption`  
  Load '84_LVBus0048952_consumption' has phase imbalance of 238.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2009562_consumption`  
  Load '84_LVBus2009562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049079_consumption`  
  Load '84_LVBus0049079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048926_consumption`  
  Load '84_LVBus0048926_consumption' has phase imbalance of 29.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049116_consumption`  
  Load '84_LVBus0049116_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048802_consumption`  
  Load '84_LVBus0048802_consumption' has phase imbalance of 265.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048829_consumption`  
  Load '84_LVBus0048829_consumption' has phase imbalance of 217.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2010936_consumption`  
  Load '84_LVBus2010936_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049101_consumption`  
  Load '84_LVBus0049101_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048842_consumption`  
  Load '84_LVBus0048842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048892_consumption`  
  Load '84_LVBus0048892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048934_consumption`  
  Load '84_LVBus0048934_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048875_consumption`  
  Load '84_LVBus0048875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048739_consumption`  
  Load '84_LVBus0048739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048910_consumption`  
  Load '84_LVBus0048910_consumption' has phase imbalance of 186.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2009561_consumption`  
  Load '84_LVBus2009561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048718_consumption`  
  Load '84_LVBus0048718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2009672_consumption`  
  Load '84_LVBus2009672_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049015_consumption`  
  Load '84_LVBus0049015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048841_consumption`  
  Load '84_LVBus0048841_consumption' has phase imbalance of 207.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048998_consumption`  
  Load '84_LVBus0048998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048849_consumption`  
  Load '84_LVBus0048849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049066_consumption`  
  Load '84_LVBus0049066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049128_consumption`  
  Load '84_LVBus0049128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048710_consumption`  
  Load '84_LVBus0048710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049007_consumption`  
  Load '84_LVBus0049007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048798_consumption`  
  Load '84_LVBus0048798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048747_consumption`  
  Load '84_LVBus0048747_consumption' has phase imbalance of 274.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048731_consumption`  
  Load '84_LVBus0048731_consumption' has phase imbalance of 278.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049129_consumption`  
  Load '84_LVBus0049129_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048899_consumption`  
  Load '84_LVBus0048899_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048990_consumption`  
  Load '84_LVBus0048990_consumption' has phase imbalance of 266.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048748_consumption`  
  Load '84_LVBus0048748_consumption' has phase imbalance of 283.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048796_consumption`  
  Load '84_LVBus0048796_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049134_consumption`  
  Load '84_LVBus0049134_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048935_consumption`  
  Load '84_LVBus0048935_consumption' has phase imbalance of 296.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2012919_consumption`  
  Load '84_LVBus2012919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048897_consumption`  
  Load '84_LVBus0048897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048723_consumption`  
  Load '84_LVBus0048723_consumption' has phase imbalance of 84.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048789_consumption`  
  Load '84_LVBus0048789_consumption' has phase imbalance of 147.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048942_consumption`  
  Load '84_LVBus0048942_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048701_consumption`  
  Load '84_LVBus0048701_consumption' has phase imbalance of 182.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049087_consumption`  
  Load '84_LVBus0049087_consumption' has phase imbalance of 290.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048939_consumption`  
  Load '84_LVBus0048939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049024_consumption`  
  Load '84_LVBus0049024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048981_consumption`  
  Load '84_LVBus0048981_consumption' has phase imbalance of 278.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049091_consumption`  
  Load '84_LVBus0049091_consumption' has phase imbalance of 254.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048909_consumption`  
  Load '84_LVBus0048909_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0049054_consumption`  
  Load '84_LVBus0049054_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048702_consumption`  
  Load '84_LVBus0048702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0048773_consumption`  
  Load '84_LVBus0048773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 680 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0048880' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0049072' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_DONJO' (MV, 11.78 kV) has an electrical reach of 20.05 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0048706' (LV, 0.24 kV) has an electrical reach of 16.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0049005' (LV, 0.24 kV) has an electrical reach of 27.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0048798' (LV, 0.24 kV) has an electrical reach of 6.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  555 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  128 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0048701_consumption, 84_LVBus0048702_consumption, 84_LVBus0048710_consumption, 84_LVBus0048712_consumption, 84_LVBus0048716_consumption, 84_LVBus0048718_consumption, 84_LVBus0048719_consumption, 84_LVBus0048721_consumption, 84_LVBus0048725_consumption, 84_LVBus0048726_consumption, 84_LVBus0048735_consumption, 84_LVBus0048739_consumption, 84_LVBus0048740_consumption, 84_LVBus0048741_consumption, 84_LVBus0048744_consumption, 84_LVBus0048745_consumption, 84_LVBus0048746_consumption, 84_LVBus0048748_consumption, 84_LVBus0048754_consumption, 84_LVBus0048766_consumption, 84_LVBus0048769_consumption, 84_LVBus0048771_consumption, 84_LVBus0048772_consumption, 84_LVBus0048773_consumption, 84_LVBus0048798_consumption, 84_LVBus0048806_consumption, 84_LVBus0048808_consumption, 84_LVBus0048813_consumption, 84_LVBus0048826_consumption, 84_LVBus0048827_consumption, 84_LVBus0048836_consumption, 84_LVBus0048841_consumption, 84_LVBus0048842_consumption, 84_LVBus0048849_consumption, 84_LVBus0048851_consumption, 84_LVBus0048852_consumption, 84_LVBus0048856_consumption, 84_LVBus0048857_consumption, 84_LVBus0048860_consumption, 84_LVBus0048861_consumption, 84_LVBus0048866_consumption, 84_LVBus0048871_consumption, 84_LVBus0048875_consumption, 84_LVBus0048877_consumption, 84_LVBus0048892_consumption, 84_LVBus0048895_consumption, 84_LVBus0048897_consumption, 84_LVBus0048898_consumption, 84_LVBus0048899_consumption, 84_LVBus0048903_consumption, 84_LVBus0048905_consumption, 84_LVBus0048908_consumption, 84_LVBus0048909_consumption, 84_LVBus0048910_consumption, 84_LVBus0048911_consumption, 84_LVBus0048913_consumption, 84_LVBus0048914_consumption, 84_LVBus0048915_consumption, 84_LVBus0048916_consumption, 84_LVBus0048919_consumption, 84_LVBus0048923_consumption, 84_LVBus0048927_consumption, 84_LVBus0048928_consumption, 84_LVBus0048929_consumption, 84_LVBus0048932_consumption, 84_LVBus0048934_consumption, 84_LVBus0048935_consumption, 84_LVBus0048936_consumption, 84_LVBus0048939_consumption, 84_LVBus0048940_consumption, 84_LVBus0048970_consumption, 84_LVBus0048977_consumption, 84_LVBus0048979_consumption, 84_LVBus0048981_consumption, 84_LVBus0048982_consumption, 84_LVBus0048985_consumption, 84_LVBus0048986_consumption, 84_LVBus0048989_consumption, 84_LVBus0048990_consumption, 84_LVBus0048994_consumption, 84_LVBus0048997_consumption, 84_LVBus0048998_consumption, 84_LVBus0048999_consumption, 84_LVBus0049007_consumption, 84_LVBus0049009_consumption, 84_LVBus0049015_consumption, 84_LVBus0049016_consumption, 84_LVBus0049017_consumption, 84_LVBus0049023_consumption, 84_LVBus0049024_consumption, 84_LVBus0049029_consumption, 84_LVBus0049038_consumption, 84_LVBus0049039_consumption, 84_LVBus0049049_consumption, 84_LVBus0049052_consumption, 84_LVBus0049054_consumption, 84_LVBus0049056_consumption, 84_LVBus0049060_consumption, 84_LVBus0049061_consumption, 84_LVBus0049062_consumption, 84_LVBus0049063_consumption, 84_LVBus0049066_consumption, 84_LVBus0049067_consumption, 84_LVBus0049079_consumption, 84_LVBus0049080_consumption, 84_LVBus0049087_consumption, 84_LVBus0049097_consumption, 84_LVBus0049101_consumption, 84_LVBus0049112_consumption, 84_LVBus0049116_consumption, 84_LVBus0049120_consumption, 84_LVBus0049123_consumption, 84_LVBus0049128_consumption, 84_LVBus0049129_consumption, 84_LVBus0049135_consumption, 84_LVBus0049144_consumption, 84_LVBus2009561_consumption, 84_LVBus2009562_consumption, 84_LVBus2009563_consumption, 84_LVBus2009564_consumption, 84_LVBus2009672_consumption, 84_LVBus2010936_consumption, 84_LVBus2010937_consumption, 84_LVBus2010938_consumption, 84_LVBus2011880_consumption, 84_LVBus2012919_consumption, 84_LVBus2014150_consumption, 84_LVBus2014473_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  340 group(s) of loads (680 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  16 group(s) of series lines (32 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  455 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0048696_consumption, 84_LVBus0048696_production, 84_LVBus0048697_production, 84_LVBus0048698_consumption, 84_LVBus0048698_production, 84_LVBus0048699_production, 84_LVBus0048700_consumption, 84_LVBus0048700_production, 84_LVBus0048701_production, 84_LVBus0048702_production, 84_LVBus0048706_production, 84_LVBus0048708_production, 84_LVBus0048710_production, 84_LVBus0048711_production, 84_LVBus0048712_production, 84_LVBus0048716_production, 84_LVBus0048717_consumption, 84_LVBus0048717_production, 84_LVBus0048718_production, 84_LVBus0048719_production, 84_LVBus0048721_production, 84_LVBus0048722_production, 84_LVBus0048723_production, 84_LVBus0048724_production, 84_LVBus0048725_production, 84_LVBus0048726_production, 84_LVBus0048727_production, 84_LVBus0048728_consumption, 84_LVBus0048728_production, 84_LVBus0048729_consumption, 84_LVBus0048729_production, 84_LVBus0048730_production, 84_LVBus0048731_production, 84_LVBus0048735_production, 84_LVBus0048737_consumption, 84_LVBus0048737_production, 84_LVBus0048738_consumption, 84_LVBus0048738_production, 84_LVBus0048739_production, 84_LVBus0048740_production, 84_LVBus0048741_production, 84_LVBus0048742_production, 84_LVBus0048743_consumption, 84_LVBus0048743_production, 84_LVBus0048744_production, 84_LVBus0048745_production, 84_LVBus0048746_production, 84_LVBus0048747_production, 84_LVBus0048748_production, 84_LVBus0048752_consumption, 84_LVBus0048752_production, 84_LVBus0048753_consumption, 84_LVBus0048753_production, 84_LVBus0048754_production, 84_LVBus0048755_production, 84_LVBus0048756_consumption, 84_LVBus0048756_production, 84_LVBus0048757_consumption, 84_LVBus0048757_production, 84_LVBus0048758_consumption, 84_LVBus0048758_production, 84_LVBus0048759_production, 84_LVBus0048761_consumption, 84_LVBus0048761_production, 84_LVBus0048763_consumption, 84_LVBus0048763_production, 84_LVBus0048765_consumption, 84_LVBus0048765_production, 84_LVBus0048766_production, 84_LVBus0048767_consumption, 84_LVBus0048767_production, 84_LVBus0048768_consumption, 84_LVBus0048768_production, 84_LVBus0048769_production, 84_LVBus0048770_consumption, 84_LVBus0048770_production, 84_LVBus0048771_production, 84_LVBus0048772_production, 84_LVBus0048773_production, 84_LVBus0048777_production, 84_LVBus0048779_production, 84_LVBus0048781_production, 84_LVBus0048783_consumption, 84_LVBus0048783_production, 84_LVBus0048784_production, 84_LVBus0048785_production, 84_LVBus0048789_production, 84_LVBus0048790_consumption, 84_LVBus0048790_production, 84_LVBus0048791_consumption, 84_LVBus0048791_production, 84_LVBus0048792_production, 84_LVBus0048796_production, 84_LVBus0048798_production, 84_LVBus0048800_consumption, 84_LVBus0048800_production, 84_LVBus0048801_production, 84_LVBus0048802_production, 84_LVBus0048806_production, 84_LVBus0048807_production, 84_LVBus0048808_production, 84_LVBus0048812_consumption, 84_LVBus0048812_production, 84_LVBus0048813_production, 84_LVBus0048814_production, 84_LVBus0048818_consumption, 84_LVBus0048818_production, 84_LVBus0048819_production, 84_LVBus0048820_production, 84_LVBus0048821_production, 84_LVBus0048824_consumption, 84_LVBus0048824_production, 84_LVBus0048825_production, 84_LVBus0048826_production, 84_LVBus0048827_production, 84_LVBus0048828_production, 84_LVBus0048829_production, 84_LVBus0048830_consumption, 84_LVBus0048830_production, 84_LVBus0048834_consumption, 84_LVBus0048834_production, 84_LVBus0048835_consumption, 84_LVBus0048835_production, 84_LVBus0048836_production, 84_LVBus0048840_consumption, 84_LVBus0048840_production, 84_LVBus0048841_production, 84_LVBus0048842_production, 84_LVBus0048843_consumption, 84_LVBus0048843_production, 84_LVBus0048845_production, 84_LVBus0048849_production, 84_LVBus0048851_production, 84_LVBus0048852_production, 84_LVBus0048853_consumption, 84_LVBus0048853_production, 84_LVBus0048854_consumption, 84_LVBus0048854_production, 84_LVBus0048855_consumption, 84_LVBus0048855_production, 84_LVBus0048856_production, 84_LVBus0048857_production, 84_LVBus0048859_consumption, 84_LVBus0048859_production, 84_LVBus0048860_production, 84_LVBus0048861_production, 84_LVBus0048865_consumption, 84_LVBus0048865_production, 84_LVBus0048866_production, 84_LVBus0048867_consumption, 84_LVBus0048867_production, 84_LVBus0048871_production, 84_LVBus0048873_consumption, 84_LVBus0048873_production, 84_LVBus0048874_consumption, 84_LVBus0048874_production, 84_LVBus0048875_production, 84_LVBus0048876_consumption, 84_LVBus0048876_production, 84_LVBus0048877_production, 84_LVBus0048878_production, 84_LVBus0048880_production, 84_LVBus0048882_consumption, 84_LVBus0048882_production, 84_LVBus0048884_production, 84_LVBus0048886_consumption, 84_LVBus0048886_production, 84_LVBus0048887_consumption, 84_LVBus0048887_production, 84_LVBus0048890_consumption, 84_LVBus0048890_production, 84_LVBus0048891_production, 84_LVBus0048892_production, 84_LVBus0048893_consumption, 84_LVBus0048893_production, 84_LVBus0048895_production, 84_LVBus0048896_consumption, 84_LVBus0048896_production, 84_LVBus0048897_production, 84_LVBus0048898_production, 84_LVBus0048899_production, 84_LVBus0048903_production, 84_LVBus0048905_production, 84_LVBus0048907_consumption, 84_LVBus0048907_production, 84_LVBus0048908_production, 84_LVBus0048909_production, 84_LVBus0048910_production, 84_LVBus0048911_production, 84_LVBus0048912_production, 84_LVBus0048913_production, 84_LVBus0048914_production, 84_LVBus0048915_production, 84_LVBus0048916_production, 84_LVBus0048917_consumption, 84_LVBus0048917_production, 84_LVBus0048919_production, 84_LVBus0048920_production, 84_LVBus0048921_production, 84_LVBus0048922_production, 84_LVBus0048923_production, 84_LVBus0048924_production, 84_LVBus0048925_production, 84_LVBus0048926_production, 84_LVBus0048927_production, 84_LVBus0048928_production, 84_LVBus0048929_production, 84_LVBus0048930_production, 84_LVBus0048931_production, 84_LVBus0048932_production, 84_LVBus0048933_consumption, 84_LVBus0048933_production, 84_LVBus0048934_production, 84_LVBus0048935_production, 84_LVBus0048936_production, 84_LVBus0048938_consumption, 84_LVBus0048938_production, 84_LVBus0048939_production, 84_LVBus0048940_production, 84_LVBus0048942_production, 84_LVBus0048944_consumption, 84_LVBus0048944_production, 84_LVBus0048945_consumption, 84_LVBus0048945_production, 84_LVBus0048946_production, 84_LVBus0048947_production, 84_LVBus0048951_consumption, 84_LVBus0048951_production, 84_LVBus0048952_production, 84_LVBus0048954_production, 84_LVBus0048955_consumption, 84_LVBus0048955_production, 84_LVBus0048956_consumption, 84_LVBus0048956_production, 84_LVBus0048957_consumption, 84_LVBus0048957_production, 84_LVBus0048958_production, 84_LVBus0048959_production, 84_LVBus0048963_consumption, 84_LVBus0048963_production, 84_LVBus0048964_production, 84_LVBus0048965_consumption, 84_LVBus0048965_production, 84_LVBus0048967_production, 84_LVBus0048969_production, 84_LVBus0048970_production, 84_LVBus0048972_production, 84_LVBus0048974_consumption, 84_LVBus0048974_production, 84_LVBus0048975_production, 84_LVBus0048977_production, 84_LVBus0048979_production, 84_LVBus0048980_production, 84_LVBus0048981_production, 84_LVBus0048982_production, 84_LVBus0048983_consumption, 84_LVBus0048983_production, 84_LVBus0048984_consumption, 84_LVBus0048984_production, 84_LVBus0048985_production, 84_LVBus0048986_production, 84_LVBus0048988_production, 84_LVBus0048989_production, 84_LVBus0048990_production, 84_LVBus0048991_production, 84_LVBus0048992_production, 84_LVBus0048993_production, 84_LVBus0048994_production, 84_LVBus0048995_production, 84_LVBus0048997_production, 84_LVBus0048998_production, 84_LVBus0048999_production, 84_LVBus0049003_consumption, 84_LVBus0049003_production, 84_LVBus0049005_production, 84_LVBus0049007_production, 84_LVBus0049008_consumption, 84_LVBus0049008_production, 84_LVBus0049009_production, 84_LVBus0049013_consumption, 84_LVBus0049013_production, 84_LVBus0049014_production, 84_LVBus0049015_production, 84_LVBus0049016_production, 84_LVBus0049017_production, 84_LVBus0049021_production, 84_LVBus0049023_production, 84_LVBus0049024_production, 84_LVBus0049025_consumption, 84_LVBus0049025_production, 84_LVBus0049026_consumption, 84_LVBus0049026_production, 84_LVBus0049027_consumption, 84_LVBus0049027_production, 84_LVBus0049029_production, 84_LVBus0049033_production, 84_LVBus0049035_production, 84_LVBus0049036_consumption, 84_LVBus0049036_production, 84_LVBus0049037_consumption, 84_LVBus0049037_production, 84_LVBus0049038_production, 84_LVBus0049039_production, 84_LVBus0049041_production, 84_LVBus0049045_consumption, 84_LVBus0049045_production, 84_LVBus0049046_production, 84_LVBus0049047_production, 84_LVBus0049049_production, 84_LVBus0049051_production, 84_LVBus0049052_production, 84_LVBus0049054_production, 84_LVBus0049056_production, 84_LVBus0049058_consumption, 84_LVBus0049058_production, 84_LVBus0049059_consumption, 84_LVBus0049059_production, 84_LVBus0049060_production, 84_LVBus0049061_production, 84_LVBus0049062_production, 84_LVBus0049063_production, 84_LVBus0049064_consumption, 84_LVBus0049064_production, 84_LVBus0049065_consumption, 84_LVBus0049065_production, 84_LVBus0049066_production, 84_LVBus0049067_production, 84_LVBus0049068_production, 84_LVBus0049072_production, 84_LVBus0049074_production, 84_LVBus0049076_production, 84_LVBus0049078_consumption, 84_LVBus0049078_production, 84_LVBus0049079_production, 84_LVBus0049080_production, 84_LVBus0049084_consumption, 84_LVBus0049084_production, 84_LVBus0049085_production, 84_LVBus0049087_production, 84_LVBus0049089_consumption, 84_LVBus0049089_production, 84_LVBus0049090_production, 84_LVBus0049091_production, 84_LVBus0049095_production, 84_LVBus0049097_production, 84_LVBus0049099_production, 84_LVBus0049100_production, 84_LVBus0049101_production, 84_LVBus0049102_production, 84_LVBus0049103_production, 84_LVBus0049104_production, 84_LVBus0049108_production, 84_LVBus0049110_production, 84_LVBus0049112_production, 84_LVBus0049114_consumption, 84_LVBus0049114_production, 84_LVBus0049115_production, 84_LVBus0049116_production, 84_LVBus0049117_consumption, 84_LVBus0049117_production, 84_LVBus0049118_consumption, 84_LVBus0049118_production, 84_LVBus0049119_consumption, 84_LVBus0049119_production, 84_LVBus0049120_production, 84_LVBus0049121_consumption, 84_LVBus0049121_production, 84_LVBus0049122_production, 84_LVBus0049123_production, 84_LVBus0049127_consumption, 84_LVBus0049127_production, 84_LVBus0049128_production, 84_LVBus0049129_production, 84_LVBus0049133_consumption, 84_LVBus0049133_production, 84_LVBus0049134_production, 84_LVBus0049135_production, 84_LVBus0049136_consumption, 84_LVBus0049136_production, 84_LVBus0049140_consumption, 84_LVBus0049140_production, 84_LVBus0049141_consumption, 84_LVBus0049141_production, 84_LVBus0049142_consumption, 84_LVBus0049142_production, 84_LVBus0049143_consumption, 84_LVBus0049143_production, 84_LVBus0049144_production, 84_LVBus2008394_consumption, 84_LVBus2008394_production, 84_LVBus2009560_consumption, 84_LVBus2009560_production, 84_LVBus2009561_production, 84_LVBus2009562_production, 84_LVBus2009563_production, 84_LVBus2009564_production, 84_LVBus2009672_production, 84_LVBus2009690_consumption, 84_LVBus2009690_production, 84_LVBus2010543_production, 84_LVBus2010936_production, 84_LVBus2010937_production, 84_LVBus2010938_production, 84_LVBus2011465_consumption, 84_LVBus2011465_production, 84_LVBus2011879_consumption, 84_LVBus2011879_production, 84_LVBus2011880_production, 84_LVBus2011881_production, 84_LVBus2012306_production, 84_LVBus2012919_production, 84_LVBus2013063_consumption, 84_LVBus2013063_production, 84_LVBus2013260_consumption, 84_LVBus2013260_production, 84_LVBus2014150_production, 84_LVBus2014472_consumption, 84_LVBus2014472_production, 84_LVBus2014473_production, 84_LVBus2014474_production, 84_LVBus2017720_production, 84_LVBus2020906_consumption, 84_LVBus2020906_production, 84_MVLV003074_consumption, 84_MVLV003074_production, 84_MVLV005118_consumption, 84_MVLV005118_production, 84_MVLV007654_consumption, 84_MVLV007654_production, 84_MVLV028854_consumption, 84_MVLV028854_production, 84_MVLV031539_consumption, 84_MVLV031539_production, 84_MVLV032213_consumption, 84_MVLV032213_production, 84_MVLV052912_consumption, 84_MVLV052912_production, 84_MVLV058900_consumption, 84_MVLV058900_production, 84_MVLV059069_consumption, 84_MVLV059069_production, 84_MVLV070103_consumption, 84_MVLV070103_production, 84_MVLV093311_consumption, 84_MVLV093311_production, 84_MVLV095072_consumption, 84_MVLV095072_production, 84_MVLV099107_consumption, 84_MVLV099107_production, 84_MVLV147115_consumption, 84_MVLV147115_production, 84_MVLV150531_consumption, 84_MVLV150531_production, 84_MVLV153876_consumption, 84_MVLV153876_production.

