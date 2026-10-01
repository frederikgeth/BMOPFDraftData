# BMOPF Network Summary: 75_MVFeeder2242

**Generated:** 2026-10-01 23:34:23  
**Findings:** 0 errors · 5 warnings · 287 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 28 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 570 |  |
| line | 541 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 1020 | 4.33 MW, 1.3 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 28 |  |
| switch | 0 |  |
| transformer | 28 | Dyn11×28 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 38 | 37 | 12 | 0 |
| LV_236V | 236.0 V | 532 | 504 | 1008 | 0 |

**Transformer transitions:**

- `75_MVLV096632_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068075_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV079280_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV160192_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV082462_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV137804_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV038777_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV150164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV072374_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV026264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV156879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV019079_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV153522_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV008516_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV078674_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV030672_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV038782_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064431_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV107529_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV172362_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV049312_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149726_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV040199_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV031370_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV104372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV030698_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV024094_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV060034_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 14 |
| Degree-1 buses | 239 |
| Tree depth (max hops) | 40 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 570 | 1 | 569 | 0 | 0 | 0 |
| Tier LV_236V | 532 | 28 | 504 | 0 | 0 | 0 |
| Tier MV_11.8kV | 38 | 1 | 37 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 28; skipped invalid branches: 0.

Galvanic zones: 29; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_LUZE | MV_11.8kV | 38 | 0 | 0 | 28 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2242 declared bus terminals; 2127 mapped line/closed-switch conductor edges; 115 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 99400.0 | 3.317 | 3060 |
| q_nom | 0.0 | 29800.0 | 3.317 | 3060 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.41 | 700.0 | 1.408 | 541 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.523 | 28 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 691 of 1020 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088612_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088975_consumption' has phase imbalance of 79.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088727_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088833_consumption' has phase imbalance of 109.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088551_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088603_consumption' has phase imbalance of 122.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088860_consumption' has phase imbalance of 233.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088706_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088644_consumption' has phase imbalance of 27.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088586_consumption' has phase imbalance of 255.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088548_consumption' has phase imbalance of 59.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088985_consumption' has phase imbalance of 107.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088871_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088698_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088635_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088711_consumption' has phase imbalance of 54.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088477_consumption' has phase imbalance of 224.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088749_consumption' has phase imbalance of 179.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088574_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088455_consumption' has phase imbalance of 46.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088680_consumption' has phase imbalance of 49.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088601_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089054_consumption' has phase imbalance of 198.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088690_consumption' has phase imbalance of 215.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088845_consumption' has phase imbalance of 119.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088481_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088646_consumption' has phase imbalance of 176.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088677_consumption' has phase imbalance of 124.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088647_consumption' has phase imbalance of 95.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088858_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088447_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088542_consumption' has phase imbalance of 46.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088592_consumption' has phase imbalance of 57.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088915_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088587_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088475_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088844_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1981306_consumption' has phase imbalance of 120.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088820_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088657_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088491_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088520_consumption' has phase imbalance of 90.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088740_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088944_consumption' has phase imbalance of 34.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088983_consumption' has phase imbalance of 122.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088937_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088825_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088636_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088961_consumption' has phase imbalance of 122.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088654_consumption' has phase imbalance of 155.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088694_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088595_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088518_consumption' has phase imbalance of 249.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2001733_consumption' has phase imbalance of 77.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089047_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088583_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088916_consumption' has phase imbalance of 26.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088830_consumption' has phase imbalance of 257.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089035_consumption' has phase imbalance of 94.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088707_consumption' has phase imbalance of 60.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088838_consumption' has phase imbalance of 168.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088685_consumption' has phase imbalance of 42.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088650_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088638_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089015_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088965_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089045_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088949_consumption' has phase imbalance of 162.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088691_consumption' has phase imbalance of 86.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088815_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089046_consumption' has phase imbalance of 112.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088822_consumption' has phase imbalance of 205.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088942_consumption' has phase imbalance of 103.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088489_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089031_consumption' has phase imbalance of 20.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088667_consumption' has phase imbalance of 54.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088981_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088462_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088846_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088941_consumption' has phase imbalance of 20.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088823_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088962_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088960_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088451_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088478_consumption' has phase imbalance of 163.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088492_consumption' has phase imbalance of 77.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088741_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088560_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088746_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088977_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088648_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088652_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088697_consumption' has phase imbalance of 47.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088976_consumption' has phase imbalance of 196.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088488_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088673_consumption' has phase imbalance of 67.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088958_consumption' has phase imbalance of 74.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088452_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088953_consumption' has phase imbalance of 264.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088580_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088750_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088905_consumption' has phase imbalance of 31.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088672_consumption' has phase imbalance of 45.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088624_consumption' has phase imbalance of 158.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088747_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089034_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088441_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088540_consumption' has phase imbalance of 175.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088752_consumption' has phase imbalance of 104.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088585_consumption' has phase imbalance of 129.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088700_consumption' has phase imbalance of 135.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088696_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088596_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088742_consumption' has phase imbalance of 83.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088986_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088966_consumption' has phase imbalance of 121.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088973_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088524_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088557_consumption' has phase imbalance of 243.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088948_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088724_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088598_consumption' has phase imbalance of 38.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088851_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088950_consumption' has phase imbalance of 145.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088639_consumption' has phase imbalance of 33.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088547_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088708_consumption' has phase imbalance of 99.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088606_consumption' has phase imbalance of 106.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088751_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088735_consumption' has phase imbalance of 64.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089036_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088637_consumption' has phase imbalance of 117.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088839_consumption' has phase imbalance of 48.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088522_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088623_consumption' has phase imbalance of 240.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088972_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088854_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088967_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088897_consumption' has phase imbalance of 76.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088701_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088693_consumption' has phase imbalance of 114.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088464_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088554_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089005_consumption' has phase imbalance of 37.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089030_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088675_consumption' has phase imbalance of 68.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088641_consumption' has phase imbalance of 146.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088832_consumption' has phase imbalance of 147.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088849_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088486_consumption' has phase imbalance of 152.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088521_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088555_consumption' has phase imbalance of 237.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088453_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088469_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088525_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088847_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088590_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088543_consumption' has phase imbalance of 221.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088943_consumption' has phase imbalance of 41.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089055_consumption' has phase imbalance of 85.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088633_consumption' has phase imbalance of 119.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088626_consumption' has phase imbalance of 127.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089033_consumption' has phase imbalance of 106.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088468_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088819_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088599_consumption' has phase imbalance of 31.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088458_consumption' has phase imbalance of 237.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088577_consumption' has phase imbalance of 229.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088445_consumption' has phase imbalance of 288.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088852_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088634_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088829_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088575_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089019_consumption' has phase imbalance of 62.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088576_consumption' has phase imbalance of 58.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088539_consumption' has phase imbalance of 288.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088556_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088974_consumption' has phase imbalance of 77.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088692_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088549_consumption' has phase imbalance of 180.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088856_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1988104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088546_consumption' has phase imbalance of 211.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088553_consumption' has phase imbalance of 222.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088550_consumption' has phase imbalance of 33.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088482_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0089056_consumption' has phase imbalance of 167.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088695_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088466_consumption' has phase imbalance of 105.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088705_consumption' has phase imbalance of 51.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088699_consumption' has phase imbalance of 28.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088442_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088529_consumption' has phase imbalance of 102.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088988_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088910_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088465_consumption' has phase imbalance of 151.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0088443_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1020 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0088926' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0088499' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0088776' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0088791' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LUZE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0089059' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0088873' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0088495' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.33 MW |
| Total load Q | 1.3 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV096632_Transformer | 693.0 kVA | 18.0% |
| 75_MVLV068075_Transformer | 693.0 kVA | 13.0% |
| 75_MVLV079280_Transformer | 693.0 kVA | 45.3% |
| 75_MVLV160192_Transformer | 440.0 kVA | 47.2% |
| 75_MVLV082462_Transformer | 110.0 kVA | 6.4% |
| 75_MVLV137804_Transformer | 440.0 kVA | 13.0% |
| 75_MVLV038777_Transformer | 693.0 kVA | 48.7% |
| 75_MVLV150164_Transformer | 440.0 kVA | 58.6% |
| 75_MVLV072374_Transformer | 693.0 kVA | 14.0% |
| 75_MVLV026264_Transformer | 275.0 kVA | 43.8% |
| 75_MVLV156879_Transformer | 440.0 kVA | 20.6% |
| 75_MVLV019079_Transformer | 440.0 kVA | 10.3% |
| 75_MVLV153522_Transformer | 1.1 MVA | 25.5% |
| 75_MVLV008516_Transformer | 693.0 kVA | 53.0% |
| 75_MVLV078674_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV030672_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV038782_Transformer | 275.0 kVA | 13.7% |
| 75_MVLV064431_Transformer | 1.1 MVA | 25.3% |
| 75_MVLV107529_Transformer | 176.0 kVA | 26.7% |
| 75_MVLV172362_Transformer | 440.0 kVA | 8.2% |
| 75_MVLV049312_Transformer | 693.0 kVA | 35.5% |
| 75_MVLV149726_Transformer | 693.0 kVA | 32.2% |
| 75_MVLV040199_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV031370_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV104372_Transformer | 440.0 kVA | 41.1% |
| 75_MVLV030698_Transformer | 440.0 kVA | 64.0% |
| 75_MVLV024094_Transformer | 693.0 kVA | 12.4% |
| 75_MVLV060034_Transformer | 693.0 kVA | 57.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.33 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0088863' (LV, 0.24 kV) has an electrical reach of 13.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 570 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 570 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 28 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 38 |
| LV_236V | 4-wire | 532 / 532 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 532 |
| Neutral branches | 504 |
| Grounding points | 28 |
| Neutral sections | 28 |
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
| 11.78 kV | 38 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 58 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 47 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 43 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 29 |
| Islands without voltage reference | 0 |
| Line impedance spread | 430.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 532 / 38 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 692 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 692 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0088441_production, 75_LVBus0088442_production, 75_LVBus0088443_production, 75_LVBus0088444_production, 75_LVBus0088445_production, 75_LVBus0088447_production, 75_LVBus0088448_consumption, 75_LVBus0088448_production, 75_LVBus0088449_consumption, 75_LVBus0088449_production, 75_LVBus0088450_production, 75_LVBus0088451_production, 75_LVBus0088452_production, 75_LVBus0088453_production, 75_LVBus0088454_production, 75_LVBus0088455_production, 75_LVBus0088456_production, 75_LVBus0088457_production, 75_LVBus0088458_production, 75_LVBus0088460_consumption, 75_LVBus0088460_production, 75_LVBus0088461_production, 75_LVBus0088462_production, 75_LVBus0088463_production, 75_LVBus0088464_production, 75_LVBus0088465_production, 75_LVBus0088466_production, 75_LVBus0088467_consumption, 75_LVBus0088467_production, 75_LVBus0088468_production, 75_LVBus0088469_production, 75_LVBus0088470_production, 75_LVBus0088471_consumption, 75_LVBus0088471_production, 75_LVBus0088473_production, 75_LVBus0088475_production, 75_LVBus0088476_production, 75_LVBus0088477_production, 75_LVBus0088478_production, 75_LVBus0088479_consumption, 75_LVBus0088479_production, 75_LVBus0088480_production, 75_LVBus0088481_production, 75_LVBus0088482_production, 75_LVBus0088484_production, 75_LVBus0088486_production, 75_LVBus0088487_consumption, 75_LVBus0088487_production, 75_LVBus0088488_production, 75_LVBus0088489_production, 75_LVBus0088490_production, 75_LVBus0088491_production, 75_LVBus0088492_production, 75_LVBus0088493_production, 75_LVBus0088495_consumption, 75_LVBus0088495_production, 75_LVBus0088497_production, 75_LVBus0088499_production, 75_LVBus0088501_production, 75_LVBus0088503_production, 75_LVBus0088505_production, 75_LVBus0088507_production, 75_LVBus0088509_production, 75_LVBus0088511_consumption, 75_LVBus0088511_production, 75_LVBus0088513_production, 75_LVBus0088515_production, 75_LVBus0088516_consumption, 75_LVBus0088516_production, 75_LVBus0088517_consumption, 75_LVBus0088517_production, 75_LVBus0088518_production, 75_LVBus0088519_consumption, 75_LVBus0088519_production, 75_LVBus0088520_production, 75_LVBus0088521_production, 75_LVBus0088522_production, 75_LVBus0088524_production, 75_LVBus0088525_production, 75_LVBus0088526_consumption, 75_LVBus0088526_production, 75_LVBus0088528_consumption, 75_LVBus0088528_production, 75_LVBus0088529_production, 75_LVBus0088530_consumption, 75_LVBus0088530_production, 75_LVBus0088532_consumption, 75_LVBus0088532_production, 75_LVBus0088534_consumption, 75_LVBus0088534_production, 75_LVBus0088535_consumption, 75_LVBus0088535_production, 75_LVBus0088537_production, 75_LVBus0088538_production, 75_LVBus0088539_production, 75_LVBus0088540_production, 75_LVBus0088541_production, 75_LVBus0088542_production, 75_LVBus0088543_production, 75_LVBus0088545_consumption, 75_LVBus0088545_production, 75_LVBus0088546_production, 75_LVBus0088547_production, 75_LVBus0088548_production, 75_LVBus0088549_production, 75_LVBus0088550_production, 75_LVBus0088551_production, 75_LVBus0088553_production, 75_LVBus0088554_production, 75_LVBus0088555_production, 75_LVBus0088556_production, 75_LVBus0088557_production, 75_LVBus0088559_production, 75_LVBus0088560_production, 75_LVBus0088562_consumption, 75_LVBus0088562_production, 75_LVBus0088564_consumption, 75_LVBus0088564_production, 75_LVBus0088566_consumption, 75_LVBus0088566_production, 75_LVBus0088568_consumption, 75_LVBus0088568_production, 75_LVBus0088570_consumption, 75_LVBus0088570_production, 75_LVBus0088572_consumption, 75_LVBus0088572_production, 75_LVBus0088574_production, 75_LVBus0088575_production, 75_LVBus0088576_production, 75_LVBus0088577_production, 75_LVBus0088579_production, 75_LVBus0088580_production, 75_LVBus0088581_consumption, 75_LVBus0088581_production, 75_LVBus0088582_consumption, 75_LVBus0088582_production, 75_LVBus0088583_production, 75_LVBus0088584_production, 75_LVBus0088585_production, 75_LVBus0088586_production, 75_LVBus0088587_production, 75_LVBus0088588_consumption, 75_LVBus0088588_production, 75_LVBus0088589_consumption, 75_LVBus0088589_production, 75_LVBus0088590_production, 75_LVBus0088591_consumption, 75_LVBus0088591_production, 75_LVBus0088592_production, 75_LVBus0088593_consumption, 75_LVBus0088593_production, 75_LVBus0088594_consumption, 75_LVBus0088594_production, 75_LVBus0088595_production, 75_LVBus0088596_production, 75_LVBus0088597_production, 75_LVBus0088598_production, 75_LVBus0088599_production, 75_LVBus0088600_production, 75_LVBus0088601_production, 75_LVBus0088603_production, 75_LVBus0088605_production, 75_LVBus0088606_production, 75_LVBus0088607_consumption, 75_LVBus0088607_production, 75_LVBus0088608_production, 75_LVBus0088610_consumption, 75_LVBus0088610_production, 75_LVBus0088611_consumption, 75_LVBus0088611_production, 75_LVBus0088612_production, 75_LVBus0088613_production, 75_LVBus0088614_production, 75_LVBus0088616_consumption, 75_LVBus0088616_production, 75_LVBus0088617_consumption, 75_LVBus0088617_production, 75_LVBus0088618_consumption, 75_LVBus0088618_production, 75_LVBus0088619_consumption, 75_LVBus0088619_production, 75_LVBus0088621_production, 75_LVBus0088622_production, 75_LVBus0088623_production, 75_LVBus0088624_production, 75_LVBus0088625_production, 75_LVBus0088626_production, 75_LVBus0088628_consumption, 75_LVBus0088628_production, 75_LVBus0088630_consumption, 75_LVBus0088630_production, 75_LVBus0088632_production, 75_LVBus0088633_production, 75_LVBus0088634_production, 75_LVBus0088635_production, 75_LVBus0088636_production, 75_LVBus0088637_production, 75_LVBus0088638_production, 75_LVBus0088639_production, 75_LVBus0088640_production, 75_LVBus0088641_production, 75_LVBus0088642_production, 75_LVBus0088643_production, 75_LVBus0088644_production, 75_LVBus0088645_production, 75_LVBus0088646_production, 75_LVBus0088647_production, 75_LVBus0088648_production, 75_LVBus0088649_consumption, 75_LVBus0088649_production, 75_LVBus0088650_production, 75_LVBus0088651_production, 75_LVBus0088652_production, 75_LVBus0088653_consumption, 75_LVBus0088653_production, 75_LVBus0088654_production, 75_LVBus0088655_consumption, 75_LVBus0088655_production, 75_LVBus0088656_production, 75_LVBus0088657_production, 75_LVBus0088659_consumption, 75_LVBus0088659_production, 75_LVBus0088660_production, 75_LVBus0088661_consumption, 75_LVBus0088661_production, 75_LVBus0088662_production, 75_LVBus0088664_consumption, 75_LVBus0088664_production, 75_LVBus0088665_production, 75_LVBus0088667_production, 75_LVBus0088668_consumption, 75_LVBus0088668_production, 75_LVBus0088669_consumption, 75_LVBus0088669_production, 75_LVBus0088670_consumption, 75_LVBus0088670_production, 75_LVBus0088671_production, 75_LVBus0088672_production, 75_LVBus0088673_production, 75_LVBus0088674_production, 75_LVBus0088675_production, 75_LVBus0088676_production, 75_LVBus0088677_production, 75_LVBus0088678_production, 75_LVBus0088679_consumption, 75_LVBus0088679_production, 75_LVBus0088680_production, 75_LVBus0088681_production, 75_LVBus0088683_production, 75_LVBus0088685_production, 75_LVBus0088687_consumption, 75_LVBus0088687_production, 75_LVBus0088688_consumption, 75_LVBus0088688_production, 75_LVBus0088689_consumption, 75_LVBus0088689_production, 75_LVBus0088690_production, 75_LVBus0088691_production, 75_LVBus0088692_production, 75_LVBus0088693_production, 75_LVBus0088694_production, 75_LVBus0088695_production, 75_LVBus0088696_production, 75_LVBus0088697_production, 75_LVBus0088698_production, 75_LVBus0088699_production, 75_LVBus0088700_production, 75_LVBus0088701_production, 75_LVBus0088703_consumption, 75_LVBus0088703_production, 75_LVBus0088704_consumption, 75_LVBus0088704_production, 75_LVBus0088705_production, 75_LVBus0088706_production, 75_LVBus0088707_production, 75_LVBus0088708_production, 75_LVBus0088709_production, 75_LVBus0088710_consumption, 75_LVBus0088710_production, 75_LVBus0088711_production, 75_LVBus0088712_consumption, 75_LVBus0088712_production, 75_LVBus0088713_consumption, 75_LVBus0088713_production, 75_LVBus0088714_consumption, 75_LVBus0088714_production, 75_LVBus0088716_consumption, 75_LVBus0088716_production, 75_LVBus0088717_production, 75_LVBus0088718_production, 75_LVBus0088719_production, 75_LVBus0088720_consumption, 75_LVBus0088720_production, 75_LVBus0088721_consumption, 75_LVBus0088721_production, 75_LVBus0088722_consumption, 75_LVBus0088722_production, 75_LVBus0088724_production, 75_LVBus0088726_consumption, 75_LVBus0088726_production, 75_LVBus0088727_production, 75_LVBus0088728_consumption, 75_LVBus0088728_production, 75_LVBus0088730_production, 75_LVBus0088732_consumption, 75_LVBus0088732_production, 75_LVBus0088733_consumption, 75_LVBus0088733_production, 75_LVBus0088734_consumption, 75_LVBus0088734_production, 75_LVBus0088735_production, 75_LVBus0088736_consumption, 75_LVBus0088736_production, 75_LVBus0088737_consumption, 75_LVBus0088737_production, 75_LVBus0088739_consumption, 75_LVBus0088739_production, 75_LVBus0088740_production, 75_LVBus0088741_production, 75_LVBus0088742_production, 75_LVBus0088744_production, 75_LVBus0088746_production, 75_LVBus0088747_production, 75_LVBus0088748_production, 75_LVBus0088749_production, 75_LVBus0088750_production, 75_LVBus0088751_production, 75_LVBus0088752_production, 75_LVBus0088754_production, 75_LVBus0088756_production, 75_LVBus0088758_production, 75_LVBus0088760_consumption, 75_LVBus0088760_production, 75_LVBus0088761_production, 75_LVBus0088762_production, 75_LVBus0088764_consumption, 75_LVBus0088764_production, 75_LVBus0088766_consumption, 75_LVBus0088766_production, 75_LVBus0088768_consumption, 75_LVBus0088768_production, 75_LVBus0088770_consumption, 75_LVBus0088770_production, 75_LVBus0088772_consumption, 75_LVBus0088772_production, 75_LVBus0088774_consumption, 75_LVBus0088774_production, 75_LVBus0088776_consumption, 75_LVBus0088776_production, 75_LVBus0088777_consumption, 75_LVBus0088777_production, 75_LVBus0088779_consumption, 75_LVBus0088779_production, 75_LVBus0088780_production, 75_LVBus0088782_production, 75_LVBus0088784_production, 75_LVBus0088786_consumption, 75_LVBus0088786_production, 75_LVBus0088787_production, 75_LVBus0088789_production, 75_LVBus0088791_consumption, 75_LVBus0088791_production, 75_LVBus0088793_production, 75_LVBus0088795_production, 75_LVBus0088797_production, 75_LVBus0088799_production, 75_LVBus0088801_production, 75_LVBus0088803_consumption, 75_LVBus0088803_production, 75_LVBus0088805_consumption, 75_LVBus0088805_production, 75_LVBus0088807_consumption, 75_LVBus0088807_production, 75_LVBus0088809_consumption, 75_LVBus0088809_production, 75_LVBus0088811_consumption, 75_LVBus0088811_production, 75_LVBus0088813_consumption, 75_LVBus0088813_production, 75_LVBus0088815_production, 75_LVBus0088817_consumption, 75_LVBus0088817_production, 75_LVBus0088818_consumption, 75_LVBus0088818_production, 75_LVBus0088819_production, 75_LVBus0088820_production, 75_LVBus0088821_consumption, 75_LVBus0088821_production, 75_LVBus0088822_production, 75_LVBus0088823_production, 75_LVBus0088824_production, 75_LVBus0088825_production, 75_LVBus0088826_production, 75_LVBus0088828_production, 75_LVBus0088829_production, 75_LVBus0088830_production, 75_LVBus0088832_production, 75_LVBus0088833_production, 75_LVBus0088835_consumption, 75_LVBus0088835_production, 75_LVBus0088836_production, 75_LVBus0088837_production, 75_LVBus0088838_production, 75_LVBus0088839_production, 75_LVBus0088840_production, 75_LVBus0088841_production, 75_LVBus0088842_production, 75_LVBus0088843_production, 75_LVBus0088844_production, 75_LVBus0088845_production, 75_LVBus0088846_production, 75_LVBus0088847_production, 75_LVBus0088848_production, 75_LVBus0088849_production, 75_LVBus0088850_production, 75_LVBus0088851_production, 75_LVBus0088852_production, 75_LVBus0088854_production, 75_LVBus0088855_consumption, 75_LVBus0088855_production, 75_LVBus0088856_production, 75_LVBus0088857_consumption, 75_LVBus0088857_production, 75_LVBus0088858_production, 75_LVBus0088859_consumption, 75_LVBus0088859_production, 75_LVBus0088860_production, 75_LVBus0088861_production, 75_LVBus0088863_consumption, 75_LVBus0088863_production, 75_LVBus0088865_consumption, 75_LVBus0088865_production, 75_LVBus0088867_consumption, 75_LVBus0088867_production, 75_LVBus0088869_consumption, 75_LVBus0088869_production, 75_LVBus0088871_production, 75_LVBus0088873_consumption, 75_LVBus0088873_production, 75_LVBus0088875_consumption, 75_LVBus0088875_production, 75_LVBus0088876_production, 75_LVBus0088877_consumption, 75_LVBus0088877_production, 75_LVBus0088878_consumption, 75_LVBus0088878_production, 75_LVBus0088879_production, 75_LVBus0088880_consumption, 75_LVBus0088880_production, 75_LVBus0088882_consumption, 75_LVBus0088882_production, 75_LVBus0088883_production, 75_LVBus0088885_consumption, 75_LVBus0088885_production, 75_LVBus0088886_consumption, 75_LVBus0088886_production, 75_LVBus0088887_consumption, 75_LVBus0088887_production, 75_LVBus0088889_consumption, 75_LVBus0088889_production, 75_LVBus0088890_consumption, 75_LVBus0088890_production, 75_LVBus0088891_production, 75_LVBus0088893_consumption, 75_LVBus0088893_production, 75_LVBus0088894_consumption, 75_LVBus0088894_production, 75_LVBus0088895_production, 75_LVBus0088897_production, 75_LVBus0088899_consumption, 75_LVBus0088899_production, 75_LVBus0088901_consumption, 75_LVBus0088901_production, 75_LVBus0088903_consumption, 75_LVBus0088903_production, 75_LVBus0088905_production, 75_LVBus0088907_consumption, 75_LVBus0088907_production, 75_LVBus0088909_consumption, 75_LVBus0088909_production, 75_LVBus0088910_production, 75_LVBus0088911_production, 75_LVBus0088912_consumption, 75_LVBus0088912_production, 75_LVBus0088913_production, 75_LVBus0088914_consumption, 75_LVBus0088914_production, 75_LVBus0088915_production, 75_LVBus0088916_production, 75_LVBus0088918_production, 75_LVBus0088919_consumption, 75_LVBus0088919_production, 75_LVBus0088920_production, 75_LVBus0088921_consumption, 75_LVBus0088921_production, 75_LVBus0088923_consumption, 75_LVBus0088923_production, 75_LVBus0088924_consumption, 75_LVBus0088924_production, 75_LVBus0088926_consumption, 75_LVBus0088926_production, 75_LVBus0088927_consumption, 75_LVBus0088927_production, 75_LVBus0088928_consumption, 75_LVBus0088928_production, 75_LVBus0088929_consumption, 75_LVBus0088929_production, 75_LVBus0088931_production, 75_LVBus0088933_consumption, 75_LVBus0088933_production, 75_LVBus0088934_production, 75_LVBus0088936_consumption, 75_LVBus0088936_production, 75_LVBus0088937_production, 75_LVBus0088939_production, 75_LVBus0088941_production, 75_LVBus0088942_production, 75_LVBus0088943_production, 75_LVBus0088944_production, 75_LVBus0088946_production, 75_LVBus0088948_production, 75_LVBus0088949_production, 75_LVBus0088950_production, 75_LVBus0088951_production, 75_LVBus0088952_consumption, 75_LVBus0088952_production, 75_LVBus0088953_production, 75_LVBus0088954_production, 75_LVBus0088956_consumption, 75_LVBus0088956_production, 75_LVBus0088958_production, 75_LVBus0088959_consumption, 75_LVBus0088959_production, 75_LVBus0088960_production, 75_LVBus0088961_production, 75_LVBus0088962_production, 75_LVBus0088963_production, 75_LVBus0088964_consumption, 75_LVBus0088964_production, 75_LVBus0088965_production, 75_LVBus0088966_production, 75_LVBus0088967_production, 75_LVBus0088968_production, 75_LVBus0088969_production, 75_LVBus0088970_consumption, 75_LVBus0088970_production, 75_LVBus0088971_consumption, 75_LVBus0088971_production, 75_LVBus0088972_production, 75_LVBus0088973_production, 75_LVBus0088974_production, 75_LVBus0088975_production, 75_LVBus0088976_production, 75_LVBus0088977_production, 75_LVBus0088978_production, 75_LVBus0088980_consumption, 75_LVBus0088980_production, 75_LVBus0088981_production, 75_LVBus0088983_production, 75_LVBus0088985_production, 75_LVBus0088986_production, 75_LVBus0088988_production, 75_LVBus0088989_consumption, 75_LVBus0088989_production, 75_LVBus0088991_production, 75_LVBus0088993_consumption, 75_LVBus0088993_production, 75_LVBus0088994_production, 75_LVBus0088995_production, 75_LVBus0088997_consumption, 75_LVBus0088997_production, 75_LVBus0088998_consumption, 75_LVBus0088998_production, 75_LVBus0088999_production, 75_LVBus0089000_production, 75_LVBus0089001_production, 75_LVBus0089003_consumption, 75_LVBus0089003_production, 75_LVBus0089004_consumption, 75_LVBus0089004_production, 75_LVBus0089005_production, 75_LVBus0089006_consumption, 75_LVBus0089006_production, 75_LVBus0089008_production, 75_LVBus0089010_production, 75_LVBus0089012_production, 75_LVBus0089014_production, 75_LVBus0089015_production, 75_LVBus0089016_production, 75_LVBus0089018_production, 75_LVBus0089019_production, 75_LVBus0089020_consumption, 75_LVBus0089020_production, 75_LVBus0089021_consumption, 75_LVBus0089021_production, 75_LVBus0089022_consumption, 75_LVBus0089022_production, 75_LVBus0089024_consumption, 75_LVBus0089024_production, 75_LVBus0089025_consumption, 75_LVBus0089025_production, 75_LVBus0089026_consumption, 75_LVBus0089026_production, 75_LVBus0089027_consumption, 75_LVBus0089027_production, 75_LVBus0089028_consumption, 75_LVBus0089028_production, 75_LVBus0089029_consumption, 75_LVBus0089029_production, 75_LVBus0089030_production, 75_LVBus0089031_production, 75_LVBus0089033_production, 75_LVBus0089034_production, 75_LVBus0089035_production, 75_LVBus0089036_production, 75_LVBus0089038_consumption, 75_LVBus0089038_production, 75_LVBus0089039_consumption, 75_LVBus0089039_production, 75_LVBus0089041_consumption, 75_LVBus0089041_production, 75_LVBus0089042_consumption, 75_LVBus0089042_production, 75_LVBus0089043_production, 75_LVBus0089045_production, 75_LVBus0089046_production, 75_LVBus0089047_production, 75_LVBus0089049_production, 75_LVBus0089050_production, 75_LVBus0089052_production, 75_LVBus0089054_production, 75_LVBus0089055_production, 75_LVBus0089056_production, 75_LVBus0089057_production, 75_LVBus0089059_consumption, 75_LVBus0089059_production, 75_LVBus0089061_production, 75_LVBus0089063_consumption, 75_LVBus0089063_production, 75_LVBus0089065_consumption, 75_LVBus0089065_production, 75_LVBus0089067_consumption, 75_LVBus0089067_production, 75_LVBus0089069_consumption, 75_LVBus0089069_production, 75_LVBus1926662_production, 75_LVBus1962520_consumption, 75_LVBus1962520_production, 75_LVBus1981303_consumption, 75_LVBus1981303_production, 75_LVBus1981304_consumption, 75_LVBus1981304_production, 75_LVBus1981305_consumption, 75_LVBus1981305_production, 75_LVBus1981306_production, 75_LVBus1981307_consumption, 75_LVBus1981307_production, 75_LVBus1981308_consumption, 75_LVBus1981308_production, 75_LVBus1981309_consumption, 75_LVBus1981309_production, 75_LVBus1988103_consumption, 75_LVBus1988103_production, 75_LVBus1988104_production, 75_LVBus1994231_consumption, 75_LVBus1994231_production, 75_LVBus2001733_production, 75_LVBus2010037_consumption, 75_LVBus2010037_production, 75_LVBus2011977_production, 75_LVBus2012353_consumption, 75_LVBus2012353_production, 75_LVBus2012354_consumption, 75_LVBus2012354_production, 75_LVBus2012662_consumption, 75_LVBus2012662_production, 75_LVBus2012714_production, 75_LVBus2012855_production, 75_LVBus2012902_production, 75_LVBus2013969_consumption, 75_LVBus2013969_production, 75_MVLV015576_consumption, 75_MVLV015576_production, 75_MVLV017341_consumption, 75_MVLV017341_production, 75_MVLV031067_consumption, 75_MVLV031067_production, 75_MVLV041140_consumption, 75_MVLV041140_production, 75_MVLV077382_production, 75_MVLV169639_consumption, 75_MVLV169639_production.

## 9. Data Quality Summary

**Total findings:** 292 (0 errors, 5 warnings, 287 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  691 of 1020 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.33 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  692 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088612_consumption`  
  Load '75_LVBus0088612_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088559_consumption`  
  Load '75_LVBus0088559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088975_consumption`  
  Load '75_LVBus0088975_consumption' has phase imbalance of 79.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088727_consumption`  
  Load '75_LVBus0088727_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088584_consumption`  
  Load '75_LVBus0088584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088833_consumption`  
  Load '75_LVBus0088833_consumption' has phase imbalance of 109.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088551_consumption`  
  Load '75_LVBus0088551_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088541_consumption`  
  Load '75_LVBus0088541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088603_consumption`  
  Load '75_LVBus0088603_consumption' has phase imbalance of 122.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088860_consumption`  
  Load '75_LVBus0088860_consumption' has phase imbalance of 233.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088951_consumption`  
  Load '75_LVBus0088951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088706_consumption`  
  Load '75_LVBus0088706_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089057_consumption`  
  Load '75_LVBus0089057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088644_consumption`  
  Load '75_LVBus0088644_consumption' has phase imbalance of 27.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088586_consumption`  
  Load '75_LVBus0088586_consumption' has phase imbalance of 255.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088537_consumption`  
  Load '75_LVBus0088537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088579_consumption`  
  Load '75_LVBus0088579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088548_consumption`  
  Load '75_LVBus0088548_consumption' has phase imbalance of 59.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088985_consumption`  
  Load '75_LVBus0088985_consumption' has phase imbalance of 107.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088871_consumption`  
  Load '75_LVBus0088871_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088911_consumption`  
  Load '75_LVBus0088911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088698_consumption`  
  Load '75_LVBus0088698_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088651_consumption`  
  Load '75_LVBus0088651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088635_consumption`  
  Load '75_LVBus0088635_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088842_consumption`  
  Load '75_LVBus0088842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088711_consumption`  
  Load '75_LVBus0088711_consumption' has phase imbalance of 54.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088477_consumption`  
  Load '75_LVBus0088477_consumption' has phase imbalance of 224.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088850_consumption`  
  Load '75_LVBus0088850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088640_consumption`  
  Load '75_LVBus0088640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088749_consumption`  
  Load '75_LVBus0088749_consumption' has phase imbalance of 179.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088574_consumption`  
  Load '75_LVBus0088574_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088455_consumption`  
  Load '75_LVBus0088455_consumption' has phase imbalance of 46.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088680_consumption`  
  Load '75_LVBus0088680_consumption' has phase imbalance of 49.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088601_consumption`  
  Load '75_LVBus0088601_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089054_consumption`  
  Load '75_LVBus0089054_consumption' has phase imbalance of 198.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088597_consumption`  
  Load '75_LVBus0088597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088690_consumption`  
  Load '75_LVBus0088690_consumption' has phase imbalance of 215.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088845_consumption`  
  Load '75_LVBus0088845_consumption' has phase imbalance of 119.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088481_consumption`  
  Load '75_LVBus0088481_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088646_consumption`  
  Load '75_LVBus0088646_consumption' has phase imbalance of 176.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089018_consumption`  
  Load '75_LVBus0089018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088939_consumption`  
  Load '75_LVBus0088939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088677_consumption`  
  Load '75_LVBus0088677_consumption' has phase imbalance of 124.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088647_consumption`  
  Load '75_LVBus0088647_consumption' has phase imbalance of 95.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088858_consumption`  
  Load '75_LVBus0088858_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088447_consumption`  
  Load '75_LVBus0088447_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088542_consumption`  
  Load '75_LVBus0088542_consumption' has phase imbalance of 46.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088592_consumption`  
  Load '75_LVBus0088592_consumption' has phase imbalance of 57.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088683_consumption`  
  Load '75_LVBus0088683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088915_consumption`  
  Load '75_LVBus0088915_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089049_consumption`  
  Load '75_LVBus0089049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088587_consumption`  
  Load '75_LVBus0088587_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088475_consumption`  
  Load '75_LVBus0088475_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088844_consumption`  
  Load '75_LVBus0088844_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088621_consumption`  
  Load '75_LVBus0088621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1981306_consumption`  
  Load '75_LVBus1981306_consumption' has phase imbalance of 120.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088820_consumption`  
  Load '75_LVBus0088820_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088963_consumption`  
  Load '75_LVBus0088963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088657_consumption`  
  Load '75_LVBus0088657_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088918_consumption`  
  Load '75_LVBus0088918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088491_consumption`  
  Load '75_LVBus0088491_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088444_consumption`  
  Load '75_LVBus0088444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088520_consumption`  
  Load '75_LVBus0088520_consumption' has phase imbalance of 90.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088740_consumption`  
  Load '75_LVBus0088740_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088660_consumption`  
  Load '75_LVBus0088660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088944_consumption`  
  Load '75_LVBus0088944_consumption' has phase imbalance of 34.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088837_consumption`  
  Load '75_LVBus0088837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088983_consumption`  
  Load '75_LVBus0088983_consumption' has phase imbalance of 122.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088937_consumption`  
  Load '75_LVBus0088937_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088825_consumption`  
  Load '75_LVBus0088825_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088636_consumption`  
  Load '75_LVBus0088636_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088454_consumption`  
  Load '75_LVBus0088454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088961_consumption`  
  Load '75_LVBus0088961_consumption' has phase imbalance of 122.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088654_consumption`  
  Load '75_LVBus0088654_consumption' has phase imbalance of 155.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088694_consumption`  
  Load '75_LVBus0088694_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088595_consumption`  
  Load '75_LVBus0088595_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089043_consumption`  
  Load '75_LVBus0089043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088718_consumption`  
  Load '75_LVBus0088718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088518_consumption`  
  Load '75_LVBus0088518_consumption' has phase imbalance of 249.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2001733_consumption`  
  Load '75_LVBus2001733_consumption' has phase imbalance of 77.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089047_consumption`  
  Load '75_LVBus0089047_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088583_consumption`  
  Load '75_LVBus0088583_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088916_consumption`  
  Load '75_LVBus0088916_consumption' has phase imbalance of 26.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088824_consumption`  
  Load '75_LVBus0088824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088830_consumption`  
  Load '75_LVBus0088830_consumption' has phase imbalance of 257.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089035_consumption`  
  Load '75_LVBus0089035_consumption' has phase imbalance of 94.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088707_consumption`  
  Load '75_LVBus0088707_consumption' has phase imbalance of 60.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088838_consumption`  
  Load '75_LVBus0088838_consumption' has phase imbalance of 168.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088685_consumption`  
  Load '75_LVBus0088685_consumption' has phase imbalance of 42.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926662_consumption`  
  Load '75_LVBus1926662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088650_consumption`  
  Load '75_LVBus0088650_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088638_consumption`  
  Load '75_LVBus0088638_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089015_consumption`  
  Load '75_LVBus0089015_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088965_consumption`  
  Load '75_LVBus0088965_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089045_consumption`  
  Load '75_LVBus0089045_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088719_consumption`  
  Load '75_LVBus0088719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088538_consumption`  
  Load '75_LVBus0088538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088949_consumption`  
  Load '75_LVBus0088949_consumption' has phase imbalance of 162.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088691_consumption`  
  Load '75_LVBus0088691_consumption' has phase imbalance of 86.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088815_consumption`  
  Load '75_LVBus0088815_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088625_consumption`  
  Load '75_LVBus0088625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089046_consumption`  
  Load '75_LVBus0089046_consumption' has phase imbalance of 112.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088822_consumption`  
  Load '75_LVBus0088822_consumption' has phase imbalance of 205.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088942_consumption`  
  Load '75_LVBus0088942_consumption' has phase imbalance of 103.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088843_consumption`  
  Load '75_LVBus0088843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088489_consumption`  
  Load '75_LVBus0088489_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089031_consumption`  
  Load '75_LVBus0089031_consumption' has phase imbalance of 20.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088667_consumption`  
  Load '75_LVBus0088667_consumption' has phase imbalance of 54.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088981_consumption`  
  Load '75_LVBus0088981_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088457_consumption`  
  Load '75_LVBus0088457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088462_consumption`  
  Load '75_LVBus0088462_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088846_consumption`  
  Load '75_LVBus0088846_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088941_consumption`  
  Load '75_LVBus0088941_consumption' has phase imbalance of 20.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088826_consumption`  
  Load '75_LVBus0088826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088823_consumption`  
  Load '75_LVBus0088823_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088962_consumption`  
  Load '75_LVBus0088962_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088960_consumption`  
  Load '75_LVBus0088960_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088451_consumption`  
  Load '75_LVBus0088451_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088478_consumption`  
  Load '75_LVBus0088478_consumption' has phase imbalance of 163.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088492_consumption`  
  Load '75_LVBus0088492_consumption' has phase imbalance of 77.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088741_consumption`  
  Load '75_LVBus0088741_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088848_consumption`  
  Load '75_LVBus0088848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088560_consumption`  
  Load '75_LVBus0088560_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088746_consumption`  
  Load '75_LVBus0088746_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088643_consumption`  
  Load '75_LVBus0088643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088473_consumption`  
  Load '75_LVBus0088473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088977_consumption`  
  Load '75_LVBus0088977_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088836_consumption`  
  Load '75_LVBus0088836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088648_consumption`  
  Load '75_LVBus0088648_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088652_consumption`  
  Load '75_LVBus0088652_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088450_consumption`  
  Load '75_LVBus0088450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088697_consumption`  
  Load '75_LVBus0088697_consumption' has phase imbalance of 47.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088976_consumption`  
  Load '75_LVBus0088976_consumption' has phase imbalance of 196.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088488_consumption`  
  Load '75_LVBus0088488_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088673_consumption`  
  Load '75_LVBus0088673_consumption' has phase imbalance of 67.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088456_consumption`  
  Load '75_LVBus0088456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088958_consumption`  
  Load '75_LVBus0088958_consumption' has phase imbalance of 74.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088452_consumption`  
  Load '75_LVBus0088452_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088953_consumption`  
  Load '75_LVBus0088953_consumption' has phase imbalance of 264.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088600_consumption`  
  Load '75_LVBus0088600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088580_consumption`  
  Load '75_LVBus0088580_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088750_consumption`  
  Load '75_LVBus0088750_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088905_consumption`  
  Load '75_LVBus0088905_consumption' has phase imbalance of 31.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088672_consumption`  
  Load '75_LVBus0088672_consumption' has phase imbalance of 45.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088624_consumption`  
  Load '75_LVBus0088624_consumption' has phase imbalance of 158.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088747_consumption`  
  Load '75_LVBus0088747_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089034_consumption`  
  Load '75_LVBus0089034_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088441_consumption`  
  Load '75_LVBus0088441_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088540_consumption`  
  Load '75_LVBus0088540_consumption' has phase imbalance of 175.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088622_consumption`  
  Load '75_LVBus0088622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088752_consumption`  
  Load '75_LVBus0088752_consumption' has phase imbalance of 104.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088656_consumption`  
  Load '75_LVBus0088656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088585_consumption`  
  Load '75_LVBus0088585_consumption' has phase imbalance of 129.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088700_consumption`  
  Load '75_LVBus0088700_consumption' has phase imbalance of 135.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088696_consumption`  
  Load '75_LVBus0088696_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088596_consumption`  
  Load '75_LVBus0088596_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088742_consumption`  
  Load '75_LVBus0088742_consumption' has phase imbalance of 83.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088986_consumption`  
  Load '75_LVBus0088986_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088966_consumption`  
  Load '75_LVBus0088966_consumption' has phase imbalance of 121.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088973_consumption`  
  Load '75_LVBus0088973_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088524_consumption`  
  Load '75_LVBus0088524_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088557_consumption`  
  Load '75_LVBus0088557_consumption' has phase imbalance of 243.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088948_consumption`  
  Load '75_LVBus0088948_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088724_consumption`  
  Load '75_LVBus0088724_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088598_consumption`  
  Load '75_LVBus0088598_consumption' has phase imbalance of 38.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088851_consumption`  
  Load '75_LVBus0088851_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088476_consumption`  
  Load '75_LVBus0088476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088709_consumption`  
  Load '75_LVBus0088709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088950_consumption`  
  Load '75_LVBus0088950_consumption' has phase imbalance of 145.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088639_consumption`  
  Load '75_LVBus0088639_consumption' has phase imbalance of 33.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088547_consumption`  
  Load '75_LVBus0088547_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088708_consumption`  
  Load '75_LVBus0088708_consumption' has phase imbalance of 99.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088606_consumption`  
  Load '75_LVBus0088606_consumption' has phase imbalance of 106.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088751_consumption`  
  Load '75_LVBus0088751_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088913_consumption`  
  Load '75_LVBus0088913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088735_consumption`  
  Load '75_LVBus0088735_consumption' has phase imbalance of 64.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089036_consumption`  
  Load '75_LVBus0089036_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088637_consumption`  
  Load '75_LVBus0088637_consumption' has phase imbalance of 117.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088969_consumption`  
  Load '75_LVBus0088969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088470_consumption`  
  Load '75_LVBus0088470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088839_consumption`  
  Load '75_LVBus0088839_consumption' has phase imbalance of 48.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088522_consumption`  
  Load '75_LVBus0088522_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088623_consumption`  
  Load '75_LVBus0088623_consumption' has phase imbalance of 240.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088972_consumption`  
  Load '75_LVBus0088972_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088854_consumption`  
  Load '75_LVBus0088854_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088967_consumption`  
  Load '75_LVBus0088967_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088897_consumption`  
  Load '75_LVBus0088897_consumption' has phase imbalance of 76.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088701_consumption`  
  Load '75_LVBus0088701_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088693_consumption`  
  Load '75_LVBus0088693_consumption' has phase imbalance of 114.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088464_consumption`  
  Load '75_LVBus0088464_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088554_consumption`  
  Load '75_LVBus0088554_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089005_consumption`  
  Load '75_LVBus0089005_consumption' has phase imbalance of 37.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089030_consumption`  
  Load '75_LVBus0089030_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088675_consumption`  
  Load '75_LVBus0088675_consumption' has phase imbalance of 68.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088645_consumption`  
  Load '75_LVBus0088645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088641_consumption`  
  Load '75_LVBus0088641_consumption' has phase imbalance of 146.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088832_consumption`  
  Load '75_LVBus0088832_consumption' has phase imbalance of 147.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088849_consumption`  
  Load '75_LVBus0088849_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088486_consumption`  
  Load '75_LVBus0088486_consumption' has phase imbalance of 152.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088521_consumption`  
  Load '75_LVBus0088521_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088681_consumption`  
  Load '75_LVBus0088681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088555_consumption`  
  Load '75_LVBus0088555_consumption' has phase imbalance of 237.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088453_consumption`  
  Load '75_LVBus0088453_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088469_consumption`  
  Load '75_LVBus0088469_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088525_consumption`  
  Load '75_LVBus0088525_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088847_consumption`  
  Load '75_LVBus0088847_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088493_consumption`  
  Load '75_LVBus0088493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088590_consumption`  
  Load '75_LVBus0088590_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088543_consumption`  
  Load '75_LVBus0088543_consumption' has phase imbalance of 221.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088943_consumption`  
  Load '75_LVBus0088943_consumption' has phase imbalance of 41.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088463_consumption`  
  Load '75_LVBus0088463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089055_consumption`  
  Load '75_LVBus0089055_consumption' has phase imbalance of 85.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088920_consumption`  
  Load '75_LVBus0088920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088633_consumption`  
  Load '75_LVBus0088633_consumption' has phase imbalance of 119.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088626_consumption`  
  Load '75_LVBus0088626_consumption' has phase imbalance of 127.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089033_consumption`  
  Load '75_LVBus0089033_consumption' has phase imbalance of 106.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088468_consumption`  
  Load '75_LVBus0088468_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088819_consumption`  
  Load '75_LVBus0088819_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088613_consumption`  
  Load '75_LVBus0088613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088599_consumption`  
  Load '75_LVBus0088599_consumption' has phase imbalance of 31.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088674_consumption`  
  Load '75_LVBus0088674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088458_consumption`  
  Load '75_LVBus0088458_consumption' has phase imbalance of 237.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088577_consumption`  
  Load '75_LVBus0088577_consumption' has phase imbalance of 229.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088445_consumption`  
  Load '75_LVBus0088445_consumption' has phase imbalance of 288.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088852_consumption`  
  Load '75_LVBus0088852_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088634_consumption`  
  Load '75_LVBus0088634_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088829_consumption`  
  Load '75_LVBus0088829_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088575_consumption`  
  Load '75_LVBus0088575_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089019_consumption`  
  Load '75_LVBus0089019_consumption' has phase imbalance of 62.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088662_consumption`  
  Load '75_LVBus0088662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088861_consumption`  
  Load '75_LVBus0088861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088576_consumption`  
  Load '75_LVBus0088576_consumption' has phase imbalance of 58.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088539_consumption`  
  Load '75_LVBus0088539_consumption' has phase imbalance of 288.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088556_consumption`  
  Load '75_LVBus0088556_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088484_consumption`  
  Load '75_LVBus0088484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088605_consumption`  
  Load '75_LVBus0088605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088974_consumption`  
  Load '75_LVBus0088974_consumption' has phase imbalance of 77.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088692_consumption`  
  Load '75_LVBus0088692_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088549_consumption`  
  Load '75_LVBus0088549_consumption' has phase imbalance of 180.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088856_consumption`  
  Load '75_LVBus0088856_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1988104_consumption`  
  Load '75_LVBus1988104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088546_consumption`  
  Load '75_LVBus0088546_consumption' has phase imbalance of 211.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088553_consumption`  
  Load '75_LVBus0088553_consumption' has phase imbalance of 222.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088550_consumption`  
  Load '75_LVBus0088550_consumption' has phase imbalance of 33.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088482_consumption`  
  Load '75_LVBus0088482_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088748_consumption`  
  Load '75_LVBus0088748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088841_consumption`  
  Load '75_LVBus0088841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0089056_consumption`  
  Load '75_LVBus0089056_consumption' has phase imbalance of 167.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088695_consumption`  
  Load '75_LVBus0088695_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088466_consumption`  
  Load '75_LVBus0088466_consumption' has phase imbalance of 105.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088968_consumption`  
  Load '75_LVBus0088968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088705_consumption`  
  Load '75_LVBus0088705_consumption' has phase imbalance of 51.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088699_consumption`  
  Load '75_LVBus0088699_consumption' has phase imbalance of 28.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088840_consumption`  
  Load '75_LVBus0088840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088442_consumption`  
  Load '75_LVBus0088442_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088490_consumption`  
  Load '75_LVBus0088490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088529_consumption`  
  Load '75_LVBus0088529_consumption' has phase imbalance of 102.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088988_consumption`  
  Load '75_LVBus0088988_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088910_consumption`  
  Load '75_LVBus0088910_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088461_consumption`  
  Load '75_LVBus0088461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088828_consumption`  
  Load '75_LVBus0088828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088642_consumption`  
  Load '75_LVBus0088642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088465_consumption`  
  Load '75_LVBus0088465_consumption' has phase imbalance of 151.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0088443_consumption`  
  Load '75_LVBus0088443_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1020 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0088926' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0088499' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0088776' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0088791' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LUZE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0089059' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0088873' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0088495' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0088863' (LV, 0.24 kV) has an electrical reach of 13.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  570 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  149 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0088441_consumption, 75_LVBus0088444_consumption, 75_LVBus0088445_consumption, 75_LVBus0088447_consumption, 75_LVBus0088450_consumption, 75_LVBus0088452_consumption, 75_LVBus0088454_consumption, 75_LVBus0088456_consumption, 75_LVBus0088457_consumption, 75_LVBus0088458_consumption, 75_LVBus0088461_consumption, 75_LVBus0088462_consumption, 75_LVBus0088463_consumption, 75_LVBus0088468_consumption, 75_LVBus0088470_consumption, 75_LVBus0088473_consumption, 75_LVBus0088476_consumption, 75_LVBus0088477_consumption, 75_LVBus0088478_consumption, 75_LVBus0088481_consumption, 75_LVBus0088482_consumption, 75_LVBus0088484_consumption, 75_LVBus0088486_consumption, 75_LVBus0088488_consumption, 75_LVBus0088489_consumption, 75_LVBus0088490_consumption, 75_LVBus0088491_consumption, 75_LVBus0088493_consumption, 75_LVBus0088518_consumption, 75_LVBus0088521_consumption, 75_LVBus0088522_consumption, 75_LVBus0088524_consumption, 75_LVBus0088537_consumption, 75_LVBus0088538_consumption, 75_LVBus0088539_consumption, 75_LVBus0088540_consumption, 75_LVBus0088541_consumption, 75_LVBus0088543_consumption, 75_LVBus0088546_consumption, 75_LVBus0088547_consumption, 75_LVBus0088549_consumption, 75_LVBus0088553_consumption, 75_LVBus0088554_consumption, 75_LVBus0088555_consumption, 75_LVBus0088556_consumption, 75_LVBus0088557_consumption, 75_LVBus0088559_consumption, 75_LVBus0088577_consumption, 75_LVBus0088579_consumption, 75_LVBus0088583_consumption, 75_LVBus0088584_consumption, 75_LVBus0088586_consumption, 75_LVBus0088595_consumption, 75_LVBus0088596_consumption, 75_LVBus0088597_consumption, 75_LVBus0088600_consumption, 75_LVBus0088605_consumption, 75_LVBus0088613_consumption, 75_LVBus0088621_consumption, 75_LVBus0088622_consumption, 75_LVBus0088623_consumption, 75_LVBus0088625_consumption, 75_LVBus0088634_consumption, 75_LVBus0088635_consumption, 75_LVBus0088636_consumption, 75_LVBus0088640_consumption, 75_LVBus0088642_consumption, 75_LVBus0088643_consumption, 75_LVBus0088645_consumption, 75_LVBus0088646_consumption, 75_LVBus0088648_consumption, 75_LVBus0088651_consumption, 75_LVBus0088652_consumption, 75_LVBus0088654_consumption, 75_LVBus0088656_consumption, 75_LVBus0088660_consumption, 75_LVBus0088662_consumption, 75_LVBus0088674_consumption, 75_LVBus0088681_consumption, 75_LVBus0088683_consumption, 75_LVBus0088690_consumption, 75_LVBus0088694_consumption, 75_LVBus0088709_consumption, 75_LVBus0088718_consumption, 75_LVBus0088719_consumption, 75_LVBus0088740_consumption, 75_LVBus0088746_consumption, 75_LVBus0088747_consumption, 75_LVBus0088748_consumption, 75_LVBus0088749_consumption, 75_LVBus0088750_consumption, 75_LVBus0088815_consumption, 75_LVBus0088822_consumption, 75_LVBus0088824_consumption, 75_LVBus0088825_consumption, 75_LVBus0088826_consumption, 75_LVBus0088828_consumption, 75_LVBus0088829_consumption, 75_LVBus0088830_consumption, 75_LVBus0088836_consumption, 75_LVBus0088837_consumption, 75_LVBus0088838_consumption, 75_LVBus0088840_consumption, 75_LVBus0088841_consumption, 75_LVBus0088842_consumption, 75_LVBus0088843_consumption, 75_LVBus0088844_consumption, 75_LVBus0088846_consumption, 75_LVBus0088847_consumption, 75_LVBus0088848_consumption, 75_LVBus0088849_consumption, 75_LVBus0088850_consumption, 75_LVBus0088851_consumption, 75_LVBus0088852_consumption, 75_LVBus0088856_consumption, 75_LVBus0088860_consumption, 75_LVBus0088861_consumption, 75_LVBus0088871_consumption, 75_LVBus0088911_consumption, 75_LVBus0088913_consumption, 75_LVBus0088915_consumption, 75_LVBus0088918_consumption, 75_LVBus0088920_consumption, 75_LVBus0088937_consumption, 75_LVBus0088939_consumption, 75_LVBus0088948_consumption, 75_LVBus0088949_consumption, 75_LVBus0088951_consumption, 75_LVBus0088953_consumption, 75_LVBus0088960_consumption, 75_LVBus0088962_consumption, 75_LVBus0088963_consumption, 75_LVBus0088965_consumption, 75_LVBus0088967_consumption, 75_LVBus0088968_consumption, 75_LVBus0088969_consumption, 75_LVBus0088976_consumption, 75_LVBus0088977_consumption, 75_LVBus0089018_consumption, 75_LVBus0089034_consumption, 75_LVBus0089036_consumption, 75_LVBus0089043_consumption, 75_LVBus0089045_consumption, 75_LVBus0089049_consumption, 75_LVBus0089054_consumption, 75_LVBus0089056_consumption, 75_LVBus0089057_consumption, 75_LVBus1926662_consumption, 75_LVBus1988104_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  510 group(s) of loads (1020 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  692 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0088441_production, 75_LVBus0088442_production, 75_LVBus0088443_production, 75_LVBus0088444_production, 75_LVBus0088445_production, 75_LVBus0088447_production, 75_LVBus0088448_consumption, 75_LVBus0088448_production, 75_LVBus0088449_consumption, 75_LVBus0088449_production, 75_LVBus0088450_production, 75_LVBus0088451_production, 75_LVBus0088452_production, 75_LVBus0088453_production, 75_LVBus0088454_production, 75_LVBus0088455_production, 75_LVBus0088456_production, 75_LVBus0088457_production, 75_LVBus0088458_production, 75_LVBus0088460_consumption, 75_LVBus0088460_production, 75_LVBus0088461_production, 75_LVBus0088462_production, 75_LVBus0088463_production, 75_LVBus0088464_production, 75_LVBus0088465_production, 75_LVBus0088466_production, 75_LVBus0088467_consumption, 75_LVBus0088467_production, 75_LVBus0088468_production, 75_LVBus0088469_production, 75_LVBus0088470_production, 75_LVBus0088471_consumption, 75_LVBus0088471_production, 75_LVBus0088473_production, 75_LVBus0088475_production, 75_LVBus0088476_production, 75_LVBus0088477_production, 75_LVBus0088478_production, 75_LVBus0088479_consumption, 75_LVBus0088479_production, 75_LVBus0088480_production, 75_LVBus0088481_production, 75_LVBus0088482_production, 75_LVBus0088484_production, 75_LVBus0088486_production, 75_LVBus0088487_consumption, 75_LVBus0088487_production, 75_LVBus0088488_production, 75_LVBus0088489_production, 75_LVBus0088490_production, 75_LVBus0088491_production, 75_LVBus0088492_production, 75_LVBus0088493_production, 75_LVBus0088495_consumption, 75_LVBus0088495_production, 75_LVBus0088497_production, 75_LVBus0088499_production, 75_LVBus0088501_production, 75_LVBus0088503_production, 75_LVBus0088505_production, 75_LVBus0088507_production, 75_LVBus0088509_production, 75_LVBus0088511_consumption, 75_LVBus0088511_production, 75_LVBus0088513_production, 75_LVBus0088515_production, 75_LVBus0088516_consumption, 75_LVBus0088516_production, 75_LVBus0088517_consumption, 75_LVBus0088517_production, 75_LVBus0088518_production, 75_LVBus0088519_consumption, 75_LVBus0088519_production, 75_LVBus0088520_production, 75_LVBus0088521_production, 75_LVBus0088522_production, 75_LVBus0088524_production, 75_LVBus0088525_production, 75_LVBus0088526_consumption, 75_LVBus0088526_production, 75_LVBus0088528_consumption, 75_LVBus0088528_production, 75_LVBus0088529_production, 75_LVBus0088530_consumption, 75_LVBus0088530_production, 75_LVBus0088532_consumption, 75_LVBus0088532_production, 75_LVBus0088534_consumption, 75_LVBus0088534_production, 75_LVBus0088535_consumption, 75_LVBus0088535_production, 75_LVBus0088537_production, 75_LVBus0088538_production, 75_LVBus0088539_production, 75_LVBus0088540_production, 75_LVBus0088541_production, 75_LVBus0088542_production, 75_LVBus0088543_production, 75_LVBus0088545_consumption, 75_LVBus0088545_production, 75_LVBus0088546_production, 75_LVBus0088547_production, 75_LVBus0088548_production, 75_LVBus0088549_production, 75_LVBus0088550_production, 75_LVBus0088551_production, 75_LVBus0088553_production, 75_LVBus0088554_production, 75_LVBus0088555_production, 75_LVBus0088556_production, 75_LVBus0088557_production, 75_LVBus0088559_production, 75_LVBus0088560_production, 75_LVBus0088562_consumption, 75_LVBus0088562_production, 75_LVBus0088564_consumption, 75_LVBus0088564_production, 75_LVBus0088566_consumption, 75_LVBus0088566_production, 75_LVBus0088568_consumption, 75_LVBus0088568_production, 75_LVBus0088570_consumption, 75_LVBus0088570_production, 75_LVBus0088572_consumption, 75_LVBus0088572_production, 75_LVBus0088574_production, 75_LVBus0088575_production, 75_LVBus0088576_production, 75_LVBus0088577_production, 75_LVBus0088579_production, 75_LVBus0088580_production, 75_LVBus0088581_consumption, 75_LVBus0088581_production, 75_LVBus0088582_consumption, 75_LVBus0088582_production, 75_LVBus0088583_production, 75_LVBus0088584_production, 75_LVBus0088585_production, 75_LVBus0088586_production, 75_LVBus0088587_production, 75_LVBus0088588_consumption, 75_LVBus0088588_production, 75_LVBus0088589_consumption, 75_LVBus0088589_production, 75_LVBus0088590_production, 75_LVBus0088591_consumption, 75_LVBus0088591_production, 75_LVBus0088592_production, 75_LVBus0088593_consumption, 75_LVBus0088593_production, 75_LVBus0088594_consumption, 75_LVBus0088594_production, 75_LVBus0088595_production, 75_LVBus0088596_production, 75_LVBus0088597_production, 75_LVBus0088598_production, 75_LVBus0088599_production, 75_LVBus0088600_production, 75_LVBus0088601_production, 75_LVBus0088603_production, 75_LVBus0088605_production, 75_LVBus0088606_production, 75_LVBus0088607_consumption, 75_LVBus0088607_production, 75_LVBus0088608_production, 75_LVBus0088610_consumption, 75_LVBus0088610_production, 75_LVBus0088611_consumption, 75_LVBus0088611_production, 75_LVBus0088612_production, 75_LVBus0088613_production, 75_LVBus0088614_production, 75_LVBus0088616_consumption, 75_LVBus0088616_production, 75_LVBus0088617_consumption, 75_LVBus0088617_production, 75_LVBus0088618_consumption, 75_LVBus0088618_production, 75_LVBus0088619_consumption, 75_LVBus0088619_production, 75_LVBus0088621_production, 75_LVBus0088622_production, 75_LVBus0088623_production, 75_LVBus0088624_production, 75_LVBus0088625_production, 75_LVBus0088626_production, 75_LVBus0088628_consumption, 75_LVBus0088628_production, 75_LVBus0088630_consumption, 75_LVBus0088630_production, 75_LVBus0088632_production, 75_LVBus0088633_production, 75_LVBus0088634_production, 75_LVBus0088635_production, 75_LVBus0088636_production, 75_LVBus0088637_production, 75_LVBus0088638_production, 75_LVBus0088639_production, 75_LVBus0088640_production, 75_LVBus0088641_production, 75_LVBus0088642_production, 75_LVBus0088643_production, 75_LVBus0088644_production, 75_LVBus0088645_production, 75_LVBus0088646_production, 75_LVBus0088647_production, 75_LVBus0088648_production, 75_LVBus0088649_consumption, 75_LVBus0088649_production, 75_LVBus0088650_production, 75_LVBus0088651_production, 75_LVBus0088652_production, 75_LVBus0088653_consumption, 75_LVBus0088653_production, 75_LVBus0088654_production, 75_LVBus0088655_consumption, 75_LVBus0088655_production, 75_LVBus0088656_production, 75_LVBus0088657_production, 75_LVBus0088659_consumption, 75_LVBus0088659_production, 75_LVBus0088660_production, 75_LVBus0088661_consumption, 75_LVBus0088661_production, 75_LVBus0088662_production, 75_LVBus0088664_consumption, 75_LVBus0088664_production, 75_LVBus0088665_production, 75_LVBus0088667_production, 75_LVBus0088668_consumption, 75_LVBus0088668_production, 75_LVBus0088669_consumption, 75_LVBus0088669_production, 75_LVBus0088670_consumption, 75_LVBus0088670_production, 75_LVBus0088671_production, 75_LVBus0088672_production, 75_LVBus0088673_production, 75_LVBus0088674_production, 75_LVBus0088675_production, 75_LVBus0088676_production, 75_LVBus0088677_production, 75_LVBus0088678_production, 75_LVBus0088679_consumption, 75_LVBus0088679_production, 75_LVBus0088680_production, 75_LVBus0088681_production, 75_LVBus0088683_production, 75_LVBus0088685_production, 75_LVBus0088687_consumption, 75_LVBus0088687_production, 75_LVBus0088688_consumption, 75_LVBus0088688_production, 75_LVBus0088689_consumption, 75_LVBus0088689_production, 75_LVBus0088690_production, 75_LVBus0088691_production, 75_LVBus0088692_production, 75_LVBus0088693_production, 75_LVBus0088694_production, 75_LVBus0088695_production, 75_LVBus0088696_production, 75_LVBus0088697_production, 75_LVBus0088698_production, 75_LVBus0088699_production, 75_LVBus0088700_production, 75_LVBus0088701_production, 75_LVBus0088703_consumption, 75_LVBus0088703_production, 75_LVBus0088704_consumption, 75_LVBus0088704_production, 75_LVBus0088705_production, 75_LVBus0088706_production, 75_LVBus0088707_production, 75_LVBus0088708_production, 75_LVBus0088709_production, 75_LVBus0088710_consumption, 75_LVBus0088710_production, 75_LVBus0088711_production, 75_LVBus0088712_consumption, 75_LVBus0088712_production, 75_LVBus0088713_consumption, 75_LVBus0088713_production, 75_LVBus0088714_consumption, 75_LVBus0088714_production, 75_LVBus0088716_consumption, 75_LVBus0088716_production, 75_LVBus0088717_production, 75_LVBus0088718_production, 75_LVBus0088719_production, 75_LVBus0088720_consumption, 75_LVBus0088720_production, 75_LVBus0088721_consumption, 75_LVBus0088721_production, 75_LVBus0088722_consumption, 75_LVBus0088722_production, 75_LVBus0088724_production, 75_LVBus0088726_consumption, 75_LVBus0088726_production, 75_LVBus0088727_production, 75_LVBus0088728_consumption, 75_LVBus0088728_production, 75_LVBus0088730_production, 75_LVBus0088732_consumption, 75_LVBus0088732_production, 75_LVBus0088733_consumption, 75_LVBus0088733_production, 75_LVBus0088734_consumption, 75_LVBus0088734_production, 75_LVBus0088735_production, 75_LVBus0088736_consumption, 75_LVBus0088736_production, 75_LVBus0088737_consumption, 75_LVBus0088737_production, 75_LVBus0088739_consumption, 75_LVBus0088739_production, 75_LVBus0088740_production, 75_LVBus0088741_production, 75_LVBus0088742_production, 75_LVBus0088744_production, 75_LVBus0088746_production, 75_LVBus0088747_production, 75_LVBus0088748_production, 75_LVBus0088749_production, 75_LVBus0088750_production, 75_LVBus0088751_production, 75_LVBus0088752_production, 75_LVBus0088754_production, 75_LVBus0088756_production, 75_LVBus0088758_production, 75_LVBus0088760_consumption, 75_LVBus0088760_production, 75_LVBus0088761_production, 75_LVBus0088762_production, 75_LVBus0088764_consumption, 75_LVBus0088764_production, 75_LVBus0088766_consumption, 75_LVBus0088766_production, 75_LVBus0088768_consumption, 75_LVBus0088768_production, 75_LVBus0088770_consumption, 75_LVBus0088770_production, 75_LVBus0088772_consumption, 75_LVBus0088772_production, 75_LVBus0088774_consumption, 75_LVBus0088774_production, 75_LVBus0088776_consumption, 75_LVBus0088776_production, 75_LVBus0088777_consumption, 75_LVBus0088777_production, 75_LVBus0088779_consumption, 75_LVBus0088779_production, 75_LVBus0088780_production, 75_LVBus0088782_production, 75_LVBus0088784_production, 75_LVBus0088786_consumption, 75_LVBus0088786_production, 75_LVBus0088787_production, 75_LVBus0088789_production, 75_LVBus0088791_consumption, 75_LVBus0088791_production, 75_LVBus0088793_production, 75_LVBus0088795_production, 75_LVBus0088797_production, 75_LVBus0088799_production, 75_LVBus0088801_production, 75_LVBus0088803_consumption, 75_LVBus0088803_production, 75_LVBus0088805_consumption, 75_LVBus0088805_production, 75_LVBus0088807_consumption, 75_LVBus0088807_production, 75_LVBus0088809_consumption, 75_LVBus0088809_production, 75_LVBus0088811_consumption, 75_LVBus0088811_production, 75_LVBus0088813_consumption, 75_LVBus0088813_production, 75_LVBus0088815_production, 75_LVBus0088817_consumption, 75_LVBus0088817_production, 75_LVBus0088818_consumption, 75_LVBus0088818_production, 75_LVBus0088819_production, 75_LVBus0088820_production, 75_LVBus0088821_consumption, 75_LVBus0088821_production, 75_LVBus0088822_production, 75_LVBus0088823_production, 75_LVBus0088824_production, 75_LVBus0088825_production, 75_LVBus0088826_production, 75_LVBus0088828_production, 75_LVBus0088829_production, 75_LVBus0088830_production, 75_LVBus0088832_production, 75_LVBus0088833_production, 75_LVBus0088835_consumption, 75_LVBus0088835_production, 75_LVBus0088836_production, 75_LVBus0088837_production, 75_LVBus0088838_production, 75_LVBus0088839_production, 75_LVBus0088840_production, 75_LVBus0088841_production, 75_LVBus0088842_production, 75_LVBus0088843_production, 75_LVBus0088844_production, 75_LVBus0088845_production, 75_LVBus0088846_production, 75_LVBus0088847_production, 75_LVBus0088848_production, 75_LVBus0088849_production, 75_LVBus0088850_production, 75_LVBus0088851_production, 75_LVBus0088852_production, 75_LVBus0088854_production, 75_LVBus0088855_consumption, 75_LVBus0088855_production, 75_LVBus0088856_production, 75_LVBus0088857_consumption, 75_LVBus0088857_production, 75_LVBus0088858_production, 75_LVBus0088859_consumption, 75_LVBus0088859_production, 75_LVBus0088860_production, 75_LVBus0088861_production, 75_LVBus0088863_consumption, 75_LVBus0088863_production, 75_LVBus0088865_consumption, 75_LVBus0088865_production, 75_LVBus0088867_consumption, 75_LVBus0088867_production, 75_LVBus0088869_consumption, 75_LVBus0088869_production, 75_LVBus0088871_production, 75_LVBus0088873_consumption, 75_LVBus0088873_production, 75_LVBus0088875_consumption, 75_LVBus0088875_production, 75_LVBus0088876_production, 75_LVBus0088877_consumption, 75_LVBus0088877_production, 75_LVBus0088878_consumption, 75_LVBus0088878_production, 75_LVBus0088879_production, 75_LVBus0088880_consumption, 75_LVBus0088880_production, 75_LVBus0088882_consumption, 75_LVBus0088882_production, 75_LVBus0088883_production, 75_LVBus0088885_consumption, 75_LVBus0088885_production, 75_LVBus0088886_consumption, 75_LVBus0088886_production, 75_LVBus0088887_consumption, 75_LVBus0088887_production, 75_LVBus0088889_consumption, 75_LVBus0088889_production, 75_LVBus0088890_consumption, 75_LVBus0088890_production, 75_LVBus0088891_production, 75_LVBus0088893_consumption, 75_LVBus0088893_production, 75_LVBus0088894_consumption, 75_LVBus0088894_production, 75_LVBus0088895_production, 75_LVBus0088897_production, 75_LVBus0088899_consumption, 75_LVBus0088899_production, 75_LVBus0088901_consumption, 75_LVBus0088901_production, 75_LVBus0088903_consumption, 75_LVBus0088903_production, 75_LVBus0088905_production, 75_LVBus0088907_consumption, 75_LVBus0088907_production, 75_LVBus0088909_consumption, 75_LVBus0088909_production, 75_LVBus0088910_production, 75_LVBus0088911_production, 75_LVBus0088912_consumption, 75_LVBus0088912_production, 75_LVBus0088913_production, 75_LVBus0088914_consumption, 75_LVBus0088914_production, 75_LVBus0088915_production, 75_LVBus0088916_production, 75_LVBus0088918_production, 75_LVBus0088919_consumption, 75_LVBus0088919_production, 75_LVBus0088920_production, 75_LVBus0088921_consumption, 75_LVBus0088921_production, 75_LVBus0088923_consumption, 75_LVBus0088923_production, 75_LVBus0088924_consumption, 75_LVBus0088924_production, 75_LVBus0088926_consumption, 75_LVBus0088926_production, 75_LVBus0088927_consumption, 75_LVBus0088927_production, 75_LVBus0088928_consumption, 75_LVBus0088928_production, 75_LVBus0088929_consumption, 75_LVBus0088929_production, 75_LVBus0088931_production, 75_LVBus0088933_consumption, 75_LVBus0088933_production, 75_LVBus0088934_production, 75_LVBus0088936_consumption, 75_LVBus0088936_production, 75_LVBus0088937_production, 75_LVBus0088939_production, 75_LVBus0088941_production, 75_LVBus0088942_production, 75_LVBus0088943_production, 75_LVBus0088944_production, 75_LVBus0088946_production, 75_LVBus0088948_production, 75_LVBus0088949_production, 75_LVBus0088950_production, 75_LVBus0088951_production, 75_LVBus0088952_consumption, 75_LVBus0088952_production, 75_LVBus0088953_production, 75_LVBus0088954_production, 75_LVBus0088956_consumption, 75_LVBus0088956_production, 75_LVBus0088958_production, 75_LVBus0088959_consumption, 75_LVBus0088959_production, 75_LVBus0088960_production, 75_LVBus0088961_production, 75_LVBus0088962_production, 75_LVBus0088963_production, 75_LVBus0088964_consumption, 75_LVBus0088964_production, 75_LVBus0088965_production, 75_LVBus0088966_production, 75_LVBus0088967_production, 75_LVBus0088968_production, 75_LVBus0088969_production, 75_LVBus0088970_consumption, 75_LVBus0088970_production, 75_LVBus0088971_consumption, 75_LVBus0088971_production, 75_LVBus0088972_production, 75_LVBus0088973_production, 75_LVBus0088974_production, 75_LVBus0088975_production, 75_LVBus0088976_production, 75_LVBus0088977_production, 75_LVBus0088978_production, 75_LVBus0088980_consumption, 75_LVBus0088980_production, 75_LVBus0088981_production, 75_LVBus0088983_production, 75_LVBus0088985_production, 75_LVBus0088986_production, 75_LVBus0088988_production, 75_LVBus0088989_consumption, 75_LVBus0088989_production, 75_LVBus0088991_production, 75_LVBus0088993_consumption, 75_LVBus0088993_production, 75_LVBus0088994_production, 75_LVBus0088995_production, 75_LVBus0088997_consumption, 75_LVBus0088997_production, 75_LVBus0088998_consumption, 75_LVBus0088998_production, 75_LVBus0088999_production, 75_LVBus0089000_production, 75_LVBus0089001_production, 75_LVBus0089003_consumption, 75_LVBus0089003_production, 75_LVBus0089004_consumption, 75_LVBus0089004_production, 75_LVBus0089005_production, 75_LVBus0089006_consumption, 75_LVBus0089006_production, 75_LVBus0089008_production, 75_LVBus0089010_production, 75_LVBus0089012_production, 75_LVBus0089014_production, 75_LVBus0089015_production, 75_LVBus0089016_production, 75_LVBus0089018_production, 75_LVBus0089019_production, 75_LVBus0089020_consumption, 75_LVBus0089020_production, 75_LVBus0089021_consumption, 75_LVBus0089021_production, 75_LVBus0089022_consumption, 75_LVBus0089022_production, 75_LVBus0089024_consumption, 75_LVBus0089024_production, 75_LVBus0089025_consumption, 75_LVBus0089025_production, 75_LVBus0089026_consumption, 75_LVBus0089026_production, 75_LVBus0089027_consumption, 75_LVBus0089027_production, 75_LVBus0089028_consumption, 75_LVBus0089028_production, 75_LVBus0089029_consumption, 75_LVBus0089029_production, 75_LVBus0089030_production, 75_LVBus0089031_production, 75_LVBus0089033_production, 75_LVBus0089034_production, 75_LVBus0089035_production, 75_LVBus0089036_production, 75_LVBus0089038_consumption, 75_LVBus0089038_production, 75_LVBus0089039_consumption, 75_LVBus0089039_production, 75_LVBus0089041_consumption, 75_LVBus0089041_production, 75_LVBus0089042_consumption, 75_LVBus0089042_production, 75_LVBus0089043_production, 75_LVBus0089045_production, 75_LVBus0089046_production, 75_LVBus0089047_production, 75_LVBus0089049_production, 75_LVBus0089050_production, 75_LVBus0089052_production, 75_LVBus0089054_production, 75_LVBus0089055_production, 75_LVBus0089056_production, 75_LVBus0089057_production, 75_LVBus0089059_consumption, 75_LVBus0089059_production, 75_LVBus0089061_production, 75_LVBus0089063_consumption, 75_LVBus0089063_production, 75_LVBus0089065_consumption, 75_LVBus0089065_production, 75_LVBus0089067_consumption, 75_LVBus0089067_production, 75_LVBus0089069_consumption, 75_LVBus0089069_production, 75_LVBus1926662_production, 75_LVBus1962520_consumption, 75_LVBus1962520_production, 75_LVBus1981303_consumption, 75_LVBus1981303_production, 75_LVBus1981304_consumption, 75_LVBus1981304_production, 75_LVBus1981305_consumption, 75_LVBus1981305_production, 75_LVBus1981306_production, 75_LVBus1981307_consumption, 75_LVBus1981307_production, 75_LVBus1981308_consumption, 75_LVBus1981308_production, 75_LVBus1981309_consumption, 75_LVBus1981309_production, 75_LVBus1988103_consumption, 75_LVBus1988103_production, 75_LVBus1988104_production, 75_LVBus1994231_consumption, 75_LVBus1994231_production, 75_LVBus2001733_production, 75_LVBus2010037_consumption, 75_LVBus2010037_production, 75_LVBus2011977_production, 75_LVBus2012353_consumption, 75_LVBus2012353_production, 75_LVBus2012354_consumption, 75_LVBus2012354_production, 75_LVBus2012662_consumption, 75_LVBus2012662_production, 75_LVBus2012714_production, 75_LVBus2012855_production, 75_LVBus2012902_production, 75_LVBus2013969_consumption, 75_LVBus2013969_production, 75_MVLV015576_consumption, 75_MVLV015576_production, 75_MVLV017341_consumption, 75_MVLV017341_production, 75_MVLV031067_consumption, 75_MVLV031067_production, 75_MVLV041140_consumption, 75_MVLV041140_production, 75_MVLV077382_production, 75_MVLV169639_consumption, 75_MVLV169639_production.

