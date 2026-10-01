# BMOPF Network Summary: 75_MVFeeder2888

**Generated:** 2026-10-01 23:34:25  
**Findings:** 0 errors · 5 warnings · 353 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 74 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 765 |  |
| line | 690 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1108 | 1.766 MW, 529.8 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 74 |  |
| switch | 0 |  |
| transformer | 74 | Dyn11×74 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 139 | 138 | 4 | 0 |
| LV_236V | 236.0 V | 626 | 552 | 1104 | 0 |

**Transformer transitions:**

- `75_MVLV168811_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066816_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV009180_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV170209_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV051149_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV065623_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV093098_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV031198_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV078984_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062818_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067421_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV097229_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV090096_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV101772_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV137958_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV042692_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV138943_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127275_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068078_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127286_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV145263_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV015897_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV134471_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV044755_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV144383_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV168758_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV170006_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV019757_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV163005_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067991_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064420_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV031264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062414_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV126900_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149728_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV122458_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV144402_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV038785_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV019573_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV020080_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV061751_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127302_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV069418_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV043784_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV008428_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068086_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV003467_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV004174_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066373_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV170490_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV168790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV016907_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV085891_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036651_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV112647_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127274_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067990_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV049213_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV000303_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV112649_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV168741_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036981_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV012863_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV081981_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002550_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064422_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067558_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV017165_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV162865_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV160540_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV137975_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121946_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV090173_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV019759_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 261 |
| Tree depth (max hops) | 47 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 765 | 1 | 764 | 0 | 0 | 0 |
| Tier LV_236V | 626 | 74 | 552 | 0 | 0 | 0 |
| Tier MV_11.8kV | 139 | 1 | 138 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 74; skipped invalid branches: 0.

Galvanic zones: 75; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MVBus090514 | MV_11.8kV | 139 | 0 | 0 | 74 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2921 declared bus terminals; 2622 mapped line/closed-switch conductor edges; 299 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 22500.0 | 3.161 | 3324 |
| q_nom | 0.0 | 6740.0 | 3.161 | 3324 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.696 | 2920.0 | 1.342 | 690 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.503 | 74 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 739 of 1108 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213540_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1929146_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1929144_consumption' has phase imbalance of 111.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213747_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213513_consumption' has phase imbalance of 284.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213542_consumption' has phase imbalance of 134.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213836_consumption' has phase imbalance of 223.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213965_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214126_consumption' has phase imbalance of 65.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213794_consumption' has phase imbalance of 131.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213937_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213580_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213676_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214036_consumption' has phase imbalance of 259.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213677_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213746_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1929143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214117_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213518_consumption' has phase imbalance of 99.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213618_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213986_consumption' has phase imbalance of 141.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213621_consumption' has phase imbalance of 265.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213576_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213957_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213697_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213798_consumption' has phase imbalance of 75.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214116_consumption' has phase imbalance of 271.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1929145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214139_consumption' has phase imbalance of 131.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213885_consumption' has phase imbalance of 269.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213661_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214012_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213462_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213887_consumption' has phase imbalance of 37.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213610_consumption' has phase imbalance of 24.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213504_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213535_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214150_consumption' has phase imbalance of 201.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213554_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1929749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213914_consumption' has phase imbalance of 198.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214153_consumption' has phase imbalance of 291.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213632_consumption' has phase imbalance of 158.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213775_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213866_consumption' has phase imbalance of 222.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213663_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214034_consumption' has phase imbalance of 212.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214040_consumption' has phase imbalance of 274.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213891_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213894_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213666_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213820_consumption' has phase imbalance of 126.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213879_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213899_consumption' has phase imbalance of 117.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213544_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213711_consumption' has phase imbalance of 214.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213870_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213923_consumption' has phase imbalance of 268.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213977_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214099_consumption' has phase imbalance of 83.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213797_consumption' has phase imbalance of 268.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213970_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213895_consumption' has phase imbalance of 235.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213638_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214125_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213649_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213976_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214106_consumption' has phase imbalance of 156.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213695_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213772_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214140_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214062_consumption' has phase imbalance of 272.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213664_consumption' has phase imbalance of 131.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214148_consumption' has phase imbalance of 101.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213669_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213835_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213888_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213489_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214039_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214066_consumption' has phase imbalance of 28.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213842_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1945184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213572_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213925_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213916_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213738_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213802_consumption' has phase imbalance of 170.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213752_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213955_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213501_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214006_consumption' has phase imbalance of 102.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214105_consumption' has phase imbalance of 56.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213499_consumption' has phase imbalance of 215.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213896_consumption' has phase imbalance of 249.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213521_consumption' has phase imbalance of 249.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213881_consumption' has phase imbalance of 215.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213941_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213855_consumption' has phase imbalance of 272.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213475_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213821_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214137_consumption' has phase imbalance of 254.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214112_consumption' has phase imbalance of 99.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213698_consumption' has phase imbalance of 233.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214149_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213468_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214009_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213936_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214068_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214069_consumption' has phase imbalance of 100.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214071_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213484_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213814_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214111_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213898_consumption' has phase imbalance of 112.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213700_consumption' has phase imbalance of 275.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213478_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213950_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1929142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213599_consumption' has phase imbalance of 289.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214001_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213568_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213776_consumption' has phase imbalance of 218.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213675_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214083_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213994_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214070_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213807_consumption' has phase imbalance of 201.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213516_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214118_consumption' has phase imbalance of 235.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213543_consumption' has phase imbalance of 242.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213708_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213877_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213813_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213948_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214081_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214061_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213670_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214055_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213792_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213628_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213824_consumption' has phase imbalance of 112.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213519_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213893_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213862_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213999_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213680_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214064_consumption' has phase imbalance of 87.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213992_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213874_consumption' has phase imbalance of 81.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213886_consumption' has phase imbalance of 283.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213940_consumption' has phase imbalance of 216.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213620_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213556_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213742_consumption' has phase imbalance of 215.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213579_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213765_consumption' has phase imbalance of 237.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213694_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213560_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213485_consumption' has phase imbalance of 129.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214152_consumption' has phase imbalance of 207.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214059_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213639_consumption' has phase imbalance of 50.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213668_consumption' has phase imbalance of 158.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214030_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213880_consumption' has phase imbalance of 290.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213667_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214058_consumption' has phase imbalance of 47.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213921_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213564_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214093_consumption' has phase imbalance of 171.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214024_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213616_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213510_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1214092_consumption' has phase imbalance of 253.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213876_consumption' has phase imbalance of 239.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1213981_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1108 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1213829' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1213800' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1213723' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.766 MW |
| Total load Q | 529.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV168811_Transformer | 110.0 kVA | 0.0% |
| 75_MVLV066816_Transformer | 110.0 kVA | 8.2% |
| 75_MVLV009180_Transformer | 275.0 kVA | 17.8% |
| 75_MVLV170209_Transformer | 275.0 kVA | 21.8% |
| 75_MVLV051149_Transformer | 110.0 kVA | 0.2% |
| 75_MVLV065623_Transformer | 176.0 kVA | 13.8% |
| 75_MVLV093098_Transformer | 176.0 kVA | 15.3% |
| 75_MVLV031198_Transformer | 110.0 kVA | 17.5% |
| 75_MVLV078984_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV062818_Transformer | 176.0 kVA | 15.8% |
| 75_MVLV067421_Transformer | 110.0 kVA | 31.3% |
| 75_MVLV097229_Transformer | 440.0 kVA | 23.4% |
| 75_MVLV090096_Transformer | 110.0 kVA | 1.2% |
| 75_MVLV101772_Transformer | 110.0 kVA | 5.5% |
| 75_MVLV137958_Transformer | 110.0 kVA | 12.7% |
| 75_MVLV042692_Transformer | 275.0 kVA | 34.7% |
| 75_MVLV138943_Transformer | 110.0 kVA | 7.2% |
| 75_MVLV127275_Transformer | 110.0 kVA | 11.0% |
| 75_MVLV068078_Transformer | 110.0 kVA | 15.4% |
| 75_MVLV127286_Transformer | 176.0 kVA | 10.1% |
| 75_MVLV145263_Transformer | 110.0 kVA | 2.6% |
| 75_MVLV015897_Transformer | 275.0 kVA | 26.2% |
| 75_MVLV134471_Transformer | 110.0 kVA | 19.2% |
| 75_MVLV044755_Transformer | 440.0 kVA | 21.5% |
| 75_MVLV144383_Transformer | 110.0 kVA | 7.1% |
| 75_MVLV168758_Transformer | 275.0 kVA | 21.9% |
| 75_MVLV170006_Transformer | 275.0 kVA | 15.7% |
| 75_MVLV019757_Transformer | 110.0 kVA | 14.9% |
| 75_MVLV163005_Transformer | 275.0 kVA | 28.4% |
| 75_MVLV067991_Transformer | 110.0 kVA | 0.9% |
| 75_MVLV064420_Transformer | 110.0 kVA | 4.2% |
| 75_MVLV031264_Transformer | 176.0 kVA | 14.2% |
| 75_MVLV062414_Transformer | 110.0 kVA | 5.2% |
| 75_MVLV126900_Transformer | 110.0 kVA | 1.5% |
| 75_MVLV149728_Transformer | 110.0 kVA | 1.4% |
| 75_MVLV122458_Transformer | 110.0 kVA | 8.4% |
| 75_MVLV144402_Transformer | 176.0 kVA | 12.8% |
| 75_MVLV038785_Transformer | 110.0 kVA | 8.2% |
| 75_MVLV019573_Transformer | 110.0 kVA | 21.8% |
| 75_MVLV020080_Transformer | 110.0 kVA | 7.2% |
| 75_MVLV061751_Transformer | 110.0 kVA | 0.7% |
| 75_MVLV127302_Transformer | 110.0 kVA | 8.0% |
| 75_MVLV069418_Transformer | 110.0 kVA | 1.0% |
| 75_MVLV043784_Transformer | 275.0 kVA | 9.5% |
| 75_MVLV008428_Transformer | 176.0 kVA | 15.4% |
| 75_MVLV068086_Transformer | 176.0 kVA | 12.5% |
| 75_MVLV003467_Transformer | 176.0 kVA | 12.3% |
| 75_MVLV004174_Transformer | 110.0 kVA | 25.2% |
| 75_MVLV066373_Transformer | 110.0 kVA | 0.0% |
| 75_MVLV170490_Transformer | 110.0 kVA | 22.3% |
| 75_MVLV168790_Transformer | 176.0 kVA | 9.7% |
| 75_MVLV016907_Transformer | 176.0 kVA | 31.2% |
| 75_MVLV085891_Transformer | 110.0 kVA | 13.1% |
| 75_MVLV036651_Transformer | 275.0 kVA | 18.0% |
| 75_MVLV112647_Transformer | 110.0 kVA | 9.5% |
| 75_MVLV127274_Transformer | 176.0 kVA | 7.0% |
| 75_MVLV067990_Transformer | 110.0 kVA | 23.1% |
| 75_MVLV049213_Transformer | 176.0 kVA | 7.7% |
| 75_MVLV000303_Transformer | 110.0 kVA | 21.4% |
| 75_MVLV112649_Transformer | 110.0 kVA | 11.5% |
| 75_MVLV168741_Transformer | 176.0 kVA | 26.0% |
| 75_MVLV036981_Transformer | 110.0 kVA | 8.8% |
| 75_MVLV012863_Transformer | 110.0 kVA | 9.6% |
| 75_MVLV081981_Transformer | 176.0 kVA | 15.9% |
| 75_MVLV002550_Transformer | 110.0 kVA | 1.0% |
| 75_MVLV064422_Transformer | 110.0 kVA | 18.8% |
| 75_MVLV067558_Transformer | 110.0 kVA | 0.5% |
| 75_MVLV017165_Transformer | 110.0 kVA | 15.4% |
| 75_MVLV162865_Transformer | 110.0 kVA | 7.3% |
| 75_MVLV160540_Transformer | 440.0 kVA | 22.4% |
| 75_MVLV137975_Transformer | 275.0 kVA | 30.0% |
| 75_MVLV121946_Transformer | 176.0 kVA | 9.9% |
| 75_MVLV090173_Transformer | 275.0 kVA | 22.8% |
| 75_MVLV019759_Transformer | 110.0 kVA | 12.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.77 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_ORTH5' (MV, 11.78 kV) has an electrical reach of 20.58 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1213829' (LV, 0.24 kV) has an electrical reach of 13.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1213950' (LV, 0.24 kV) has an electrical reach of 16.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1213831' (LV, 0.24 kV) has an electrical reach of 22.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1214131' (LV, 0.24 kV) has an electrical reach of 11.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 765 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 765 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 74 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 139 |
| LV_236V | 4-wire | 626 / 626 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 626 |
| Neutral branches | 552 |
| Grounding points | 74 |
| Neutral sections | 74 |
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
| 11.78 kV | 139 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 75 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2200.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 626 / 139 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 740 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 740 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1213458_consumption, 75_LVBus1213458_production, 75_LVBus1213459_consumption, 75_LVBus1213459_production, 75_LVBus1213460_consumption, 75_LVBus1213460_production, 75_LVBus1213461_consumption, 75_LVBus1213461_production, 75_LVBus1213462_production, 75_LVBus1213463_production, 75_LVBus1213464_consumption, 75_LVBus1213464_production, 75_LVBus1213465_consumption, 75_LVBus1213465_production, 75_LVBus1213466_production, 75_LVBus1213468_production, 75_LVBus1213469_production, 75_LVBus1213471_production, 75_LVBus1213472_production, 75_LVBus1213473_production, 75_LVBus1213474_production, 75_LVBus1213475_production, 75_LVBus1213477_production, 75_LVBus1213478_production, 75_LVBus1213479_production, 75_LVBus1213480_production, 75_LVBus1213481_consumption, 75_LVBus1213481_production, 75_LVBus1213482_consumption, 75_LVBus1213482_production, 75_LVBus1213484_production, 75_LVBus1213485_production, 75_LVBus1213486_production, 75_LVBus1213487_consumption, 75_LVBus1213487_production, 75_LVBus1213488_consumption, 75_LVBus1213488_production, 75_LVBus1213489_production, 75_LVBus1213490_production, 75_LVBus1213492_consumption, 75_LVBus1213492_production, 75_LVBus1213496_production, 75_LVBus1213497_production, 75_LVBus1213498_production, 75_LVBus1213499_production, 75_LVBus1213500_consumption, 75_LVBus1213500_production, 75_LVBus1213501_production, 75_LVBus1213502_consumption, 75_LVBus1213502_production, 75_LVBus1213503_consumption, 75_LVBus1213503_production, 75_LVBus1213504_production, 75_LVBus1213509_consumption, 75_LVBus1213509_production, 75_LVBus1213510_production, 75_LVBus1213511_consumption, 75_LVBus1213511_production, 75_LVBus1213512_production, 75_LVBus1213513_production, 75_LVBus1213514_production, 75_LVBus1213515_consumption, 75_LVBus1213515_production, 75_LVBus1213516_production, 75_LVBus1213517_production, 75_LVBus1213518_production, 75_LVBus1213519_production, 75_LVBus1213521_production, 75_LVBus1213522_consumption, 75_LVBus1213522_production, 75_LVBus1213523_consumption, 75_LVBus1213523_production, 75_LVBus1213524_production, 75_LVBus1213526_consumption, 75_LVBus1213526_production, 75_LVBus1213527_consumption, 75_LVBus1213527_production, 75_LVBus1213528_consumption, 75_LVBus1213528_production, 75_LVBus1213529_consumption, 75_LVBus1213529_production, 75_LVBus1213530_production, 75_LVBus1213534_production, 75_LVBus1213535_production, 75_LVBus1213536_consumption, 75_LVBus1213536_production, 75_LVBus1213537_production, 75_LVBus1213538_consumption, 75_LVBus1213538_production, 75_LVBus1213539_production, 75_LVBus1213540_production, 75_LVBus1213541_consumption, 75_LVBus1213541_production, 75_LVBus1213542_production, 75_LVBus1213543_production, 75_LVBus1213544_production, 75_LVBus1213545_consumption, 75_LVBus1213545_production, 75_LVBus1213546_production, 75_LVBus1213547_production, 75_LVBus1213549_consumption, 75_LVBus1213549_production, 75_LVBus1213550_production, 75_LVBus1213551_consumption, 75_LVBus1213551_production, 75_LVBus1213553_consumption, 75_LVBus1213553_production, 75_LVBus1213554_production, 75_LVBus1213555_consumption, 75_LVBus1213555_production, 75_LVBus1213556_production, 75_LVBus1213558_consumption, 75_LVBus1213558_production, 75_LVBus1213559_production, 75_LVBus1213560_production, 75_LVBus1213562_production, 75_LVBus1213563_consumption, 75_LVBus1213563_production, 75_LVBus1213564_production, 75_LVBus1213565_production, 75_LVBus1213566_consumption, 75_LVBus1213566_production, 75_LVBus1213567_consumption, 75_LVBus1213567_production, 75_LVBus1213568_production, 75_LVBus1213570_consumption, 75_LVBus1213570_production, 75_LVBus1213571_consumption, 75_LVBus1213571_production, 75_LVBus1213572_production, 75_LVBus1213573_consumption, 75_LVBus1213573_production, 75_LVBus1213574_consumption, 75_LVBus1213574_production, 75_LVBus1213575_production, 75_LVBus1213576_production, 75_LVBus1213577_production, 75_LVBus1213579_production, 75_LVBus1213580_production, 75_LVBus1213581_production, 75_LVBus1213582_production, 75_LVBus1213583_production, 75_LVBus1213585_consumption, 75_LVBus1213585_production, 75_LVBus1213586_consumption, 75_LVBus1213586_production, 75_LVBus1213587_consumption, 75_LVBus1213587_production, 75_LVBus1213588_consumption, 75_LVBus1213588_production, 75_LVBus1213589_consumption, 75_LVBus1213589_production, 75_LVBus1213590_consumption, 75_LVBus1213590_production, 75_LVBus1213591_consumption, 75_LVBus1213591_production, 75_LVBus1213592_production, 75_LVBus1213593_production, 75_LVBus1213594_consumption, 75_LVBus1213594_production, 75_LVBus1213596_consumption, 75_LVBus1213596_production, 75_LVBus1213597_production, 75_LVBus1213599_production, 75_LVBus1213601_consumption, 75_LVBus1213601_production, 75_LVBus1213602_production, 75_LVBus1213603_consumption, 75_LVBus1213603_production, 75_LVBus1213604_production, 75_LVBus1213607_production, 75_LVBus1213608_production, 75_LVBus1213609_production, 75_LVBus1213610_production, 75_LVBus1213611_production, 75_LVBus1213615_consumption, 75_LVBus1213615_production, 75_LVBus1213616_production, 75_LVBus1213617_consumption, 75_LVBus1213617_production, 75_LVBus1213618_production, 75_LVBus1213619_consumption, 75_LVBus1213619_production, 75_LVBus1213620_production, 75_LVBus1213621_production, 75_LVBus1213622_consumption, 75_LVBus1213622_production, 75_LVBus1213623_production, 75_LVBus1213624_production, 75_LVBus1213625_production, 75_LVBus1213626_consumption, 75_LVBus1213626_production, 75_LVBus1213627_consumption, 75_LVBus1213627_production, 75_LVBus1213628_production, 75_LVBus1213632_production, 75_LVBus1213633_consumption, 75_LVBus1213633_production, 75_LVBus1213634_production, 75_LVBus1213635_production, 75_LVBus1213637_production, 75_LVBus1213638_production, 75_LVBus1213639_production, 75_LVBus1213640_consumption, 75_LVBus1213640_production, 75_LVBus1213641_production, 75_LVBus1213642_consumption, 75_LVBus1213642_production, 75_LVBus1213643_consumption, 75_LVBus1213643_production, 75_LVBus1213645_consumption, 75_LVBus1213645_production, 75_LVBus1213646_production, 75_LVBus1213648_consumption, 75_LVBus1213648_production, 75_LVBus1213649_production, 75_LVBus1213650_consumption, 75_LVBus1213650_production, 75_LVBus1213654_consumption, 75_LVBus1213654_production, 75_LVBus1213655_production, 75_LVBus1213656_production, 75_LVBus1213660_consumption, 75_LVBus1213660_production, 75_LVBus1213661_production, 75_LVBus1213662_production, 75_LVBus1213663_production, 75_LVBus1213664_production, 75_LVBus1213665_consumption, 75_LVBus1213665_production, 75_LVBus1213666_production, 75_LVBus1213667_production, 75_LVBus1213668_production, 75_LVBus1213669_production, 75_LVBus1213670_production, 75_LVBus1213674_consumption, 75_LVBus1213674_production, 75_LVBus1213675_production, 75_LVBus1213676_production, 75_LVBus1213677_production, 75_LVBus1213678_consumption, 75_LVBus1213678_production, 75_LVBus1213679_production, 75_LVBus1213680_production, 75_LVBus1213682_consumption, 75_LVBus1213682_production, 75_LVBus1213683_production, 75_LVBus1213684_production, 75_LVBus1213688_production, 75_LVBus1213689_production, 75_LVBus1213690_production, 75_LVBus1213691_production, 75_LVBus1213692_production, 75_LVBus1213693_production, 75_LVBus1213694_production, 75_LVBus1213695_production, 75_LVBus1213696_production, 75_LVBus1213697_production, 75_LVBus1213698_production, 75_LVBus1213699_production, 75_LVBus1213700_production, 75_LVBus1213705_consumption, 75_LVBus1213705_production, 75_LVBus1213707_consumption, 75_LVBus1213707_production, 75_LVBus1213708_production, 75_LVBus1213710_consumption, 75_LVBus1213710_production, 75_LVBus1213711_production, 75_LVBus1213712_production, 75_LVBus1213713_production, 75_LVBus1213714_production, 75_LVBus1213718_consumption, 75_LVBus1213718_production, 75_LVBus1213719_production, 75_LVBus1213721_production, 75_LVBus1213723_production, 75_LVBus1213725_consumption, 75_LVBus1213725_production, 75_LVBus1213727_consumption, 75_LVBus1213727_production, 75_LVBus1213728_consumption, 75_LVBus1213728_production, 75_LVBus1213729_consumption, 75_LVBus1213729_production, 75_LVBus1213730_production, 75_LVBus1213731_consumption, 75_LVBus1213731_production, 75_LVBus1213733_consumption, 75_LVBus1213733_production, 75_LVBus1213734_consumption, 75_LVBus1213734_production, 75_LVBus1213735_consumption, 75_LVBus1213735_production, 75_LVBus1213736_consumption, 75_LVBus1213736_production, 75_LVBus1213737_production, 75_LVBus1213738_production, 75_LVBus1213739_consumption, 75_LVBus1213739_production, 75_LVBus1213742_production, 75_LVBus1213743_consumption, 75_LVBus1213743_production, 75_LVBus1213744_production, 75_LVBus1213745_production, 75_LVBus1213746_production, 75_LVBus1213747_production, 75_LVBus1213748_production, 75_LVBus1213749_consumption, 75_LVBus1213749_production, 75_LVBus1213750_production, 75_LVBus1213751_consumption, 75_LVBus1213751_production, 75_LVBus1213752_production, 75_LVBus1213754_consumption, 75_LVBus1213754_production, 75_LVBus1213755_consumption, 75_LVBus1213755_production, 75_LVBus1213756_production, 75_LVBus1213757_consumption, 75_LVBus1213757_production, 75_LVBus1213758_production, 75_LVBus1213759_consumption, 75_LVBus1213759_production, 75_LVBus1213760_production, 75_LVBus1213761_production, 75_LVBus1213762_consumption, 75_LVBus1213762_production, 75_LVBus1213764_production, 75_LVBus1213765_production, 75_LVBus1213766_consumption, 75_LVBus1213766_production, 75_LVBus1213767_production, 75_LVBus1213768_production, 75_LVBus1213769_production, 75_LVBus1213771_consumption, 75_LVBus1213771_production, 75_LVBus1213772_production, 75_LVBus1213774_consumption, 75_LVBus1213774_production, 75_LVBus1213775_production, 75_LVBus1213776_production, 75_LVBus1213780_consumption, 75_LVBus1213780_production, 75_LVBus1213782_consumption, 75_LVBus1213782_production, 75_LVBus1213784_consumption, 75_LVBus1213784_production, 75_LVBus1213786_consumption, 75_LVBus1213786_production, 75_LVBus1213787_production, 75_LVBus1213788_consumption, 75_LVBus1213788_production, 75_LVBus1213789_production, 75_LVBus1213790_production, 75_LVBus1213791_production, 75_LVBus1213792_production, 75_LVBus1213793_consumption, 75_LVBus1213793_production, 75_LVBus1213794_production, 75_LVBus1213796_production, 75_LVBus1213797_production, 75_LVBus1213798_production, 75_LVBus1213800_production, 75_LVBus1213802_production, 75_LVBus1213803_production, 75_LVBus1213805_production, 75_LVBus1213806_consumption, 75_LVBus1213806_production, 75_LVBus1213807_production, 75_LVBus1213809_production, 75_LVBus1213811_production, 75_LVBus1213813_production, 75_LVBus1213814_production, 75_LVBus1213815_production, 75_LVBus1213816_consumption, 75_LVBus1213816_production, 75_LVBus1213817_consumption, 75_LVBus1213817_production, 75_LVBus1213818_consumption, 75_LVBus1213818_production, 75_LVBus1213820_production, 75_LVBus1213821_production, 75_LVBus1213823_production, 75_LVBus1213824_production, 75_LVBus1213825_production, 75_LVBus1213826_consumption, 75_LVBus1213826_production, 75_LVBus1213829_production, 75_LVBus1213831_consumption, 75_LVBus1213831_production, 75_LVBus1213833_production, 75_LVBus1213834_consumption, 75_LVBus1213834_production, 75_LVBus1213835_production, 75_LVBus1213836_production, 75_LVBus1213837_production, 75_LVBus1213839_consumption, 75_LVBus1213839_production, 75_LVBus1213840_consumption, 75_LVBus1213840_production, 75_LVBus1213841_production, 75_LVBus1213842_production, 75_LVBus1213843_production, 75_LVBus1213845_consumption, 75_LVBus1213845_production, 75_LVBus1213846_consumption, 75_LVBus1213846_production, 75_LVBus1213847_production, 75_LVBus1213848_consumption, 75_LVBus1213848_production, 75_LVBus1213849_consumption, 75_LVBus1213849_production, 75_LVBus1213850_consumption, 75_LVBus1213850_production, 75_LVBus1213851_production, 75_LVBus1213852_consumption, 75_LVBus1213852_production, 75_LVBus1213853_production, 75_LVBus1213854_consumption, 75_LVBus1213854_production, 75_LVBus1213855_production, 75_LVBus1213856_production, 75_LVBus1213857_consumption, 75_LVBus1213857_production, 75_LVBus1213859_consumption, 75_LVBus1213859_production, 75_LVBus1213860_consumption, 75_LVBus1213860_production, 75_LVBus1213861_consumption, 75_LVBus1213861_production, 75_LVBus1213862_production, 75_LVBus1213864_production, 75_LVBus1213865_production, 75_LVBus1213866_production, 75_LVBus1213867_production, 75_LVBus1213868_consumption, 75_LVBus1213868_production, 75_LVBus1213869_production, 75_LVBus1213870_production, 75_LVBus1213871_consumption, 75_LVBus1213871_production, 75_LVBus1213873_production, 75_LVBus1213874_production, 75_LVBus1213876_production, 75_LVBus1213877_production, 75_LVBus1213878_consumption, 75_LVBus1213878_production, 75_LVBus1213879_production, 75_LVBus1213880_production, 75_LVBus1213881_production, 75_LVBus1213883_production, 75_LVBus1213884_production, 75_LVBus1213885_production, 75_LVBus1213886_production, 75_LVBus1213887_production, 75_LVBus1213888_production, 75_LVBus1213889_production, 75_LVBus1213890_production, 75_LVBus1213891_production, 75_LVBus1213892_production, 75_LVBus1213893_production, 75_LVBus1213894_production, 75_LVBus1213895_production, 75_LVBus1213896_production, 75_LVBus1213897_consumption, 75_LVBus1213897_production, 75_LVBus1213898_production, 75_LVBus1213899_production, 75_LVBus1213900_production, 75_LVBus1213901_production, 75_LVBus1213905_consumption, 75_LVBus1213905_production, 75_LVBus1213906_consumption, 75_LVBus1213906_production, 75_LVBus1213907_production, 75_LVBus1213908_production, 75_LVBus1213912_consumption, 75_LVBus1213912_production, 75_LVBus1213913_production, 75_LVBus1213914_production, 75_LVBus1213915_consumption, 75_LVBus1213915_production, 75_LVBus1213916_production, 75_LVBus1213920_consumption, 75_LVBus1213920_production, 75_LVBus1213921_production, 75_LVBus1213922_production, 75_LVBus1213923_production, 75_LVBus1213924_consumption, 75_LVBus1213924_production, 75_LVBus1213925_production, 75_LVBus1213926_consumption, 75_LVBus1213926_production, 75_LVBus1213928_consumption, 75_LVBus1213928_production, 75_LVBus1213929_production, 75_LVBus1213930_production, 75_LVBus1213931_consumption, 75_LVBus1213931_production, 75_LVBus1213932_consumption, 75_LVBus1213932_production, 75_LVBus1213933_consumption, 75_LVBus1213933_production, 75_LVBus1213934_consumption, 75_LVBus1213934_production, 75_LVBus1213935_production, 75_LVBus1213936_production, 75_LVBus1213937_production, 75_LVBus1213939_consumption, 75_LVBus1213939_production, 75_LVBus1213940_production, 75_LVBus1213941_production, 75_LVBus1213943_production, 75_LVBus1213944_consumption, 75_LVBus1213944_production, 75_LVBus1213945_production, 75_LVBus1213946_consumption, 75_LVBus1213946_production, 75_LVBus1213947_consumption, 75_LVBus1213947_production, 75_LVBus1213948_production, 75_LVBus1213950_production, 75_LVBus1213952_production, 75_LVBus1213954_consumption, 75_LVBus1213954_production, 75_LVBus1213955_production, 75_LVBus1213956_production, 75_LVBus1213957_production, 75_LVBus1213961_consumption, 75_LVBus1213961_production, 75_LVBus1213962_consumption, 75_LVBus1213962_production, 75_LVBus1213963_consumption, 75_LVBus1213963_production, 75_LVBus1213964_consumption, 75_LVBus1213964_production, 75_LVBus1213965_production, 75_LVBus1213967_consumption, 75_LVBus1213967_production, 75_LVBus1213968_production, 75_LVBus1213969_production, 75_LVBus1213970_production, 75_LVBus1213971_production, 75_LVBus1213972_production, 75_LVBus1213976_production, 75_LVBus1213977_production, 75_LVBus1213978_production, 75_LVBus1213980_production, 75_LVBus1213981_production, 75_LVBus1213982_consumption, 75_LVBus1213982_production, 75_LVBus1213983_production, 75_LVBus1213984_production, 75_LVBus1213985_production, 75_LVBus1213986_production, 75_LVBus1213990_consumption, 75_LVBus1213990_production, 75_LVBus1213991_consumption, 75_LVBus1213991_production, 75_LVBus1213992_production, 75_LVBus1213993_production, 75_LVBus1213994_production, 75_LVBus1213998_production, 75_LVBus1213999_production, 75_LVBus1214000_production, 75_LVBus1214001_production, 75_LVBus1214002_production, 75_LVBus1214003_production, 75_LVBus1214004_production, 75_LVBus1214006_production, 75_LVBus1214007_consumption, 75_LVBus1214007_production, 75_LVBus1214009_production, 75_LVBus1214010_production, 75_LVBus1214011_production, 75_LVBus1214012_production, 75_LVBus1214013_production, 75_LVBus1214015_production, 75_LVBus1214016_production, 75_LVBus1214017_production, 75_LVBus1214018_consumption, 75_LVBus1214018_production, 75_LVBus1214019_consumption, 75_LVBus1214019_production, 75_LVBus1214022_consumption, 75_LVBus1214022_production, 75_LVBus1214023_consumption, 75_LVBus1214023_production, 75_LVBus1214024_production, 75_LVBus1214025_production, 75_LVBus1214027_consumption, 75_LVBus1214027_production, 75_LVBus1214028_production, 75_LVBus1214029_consumption, 75_LVBus1214029_production, 75_LVBus1214030_production, 75_LVBus1214034_production, 75_LVBus1214036_production, 75_LVBus1214037_consumption, 75_LVBus1214037_production, 75_LVBus1214038_production, 75_LVBus1214039_production, 75_LVBus1214040_production, 75_LVBus1214041_production, 75_LVBus1214043_consumption, 75_LVBus1214043_production, 75_LVBus1214044_consumption, 75_LVBus1214044_production, 75_LVBus1214045_consumption, 75_LVBus1214045_production, 75_LVBus1214046_consumption, 75_LVBus1214046_production, 75_LVBus1214047_production, 75_LVBus1214048_production, 75_LVBus1214049_consumption, 75_LVBus1214049_production, 75_LVBus1214050_consumption, 75_LVBus1214050_production, 75_LVBus1214051_production, 75_LVBus1214052_production, 75_LVBus1214054_production, 75_LVBus1214055_production, 75_LVBus1214056_consumption, 75_LVBus1214056_production, 75_LVBus1214058_production, 75_LVBus1214059_production, 75_LVBus1214060_production, 75_LVBus1214061_production, 75_LVBus1214062_production, 75_LVBus1214063_production, 75_LVBus1214064_production, 75_LVBus1214065_consumption, 75_LVBus1214065_production, 75_LVBus1214066_production, 75_LVBus1214067_production, 75_LVBus1214068_production, 75_LVBus1214069_production, 75_LVBus1214070_production, 75_LVBus1214071_production, 75_LVBus1214075_production, 75_LVBus1214076_production, 75_LVBus1214078_consumption, 75_LVBus1214078_production, 75_LVBus1214079_production, 75_LVBus1214081_production, 75_LVBus1214082_production, 75_LVBus1214083_production, 75_LVBus1214084_consumption, 75_LVBus1214084_production, 75_LVBus1214085_production, 75_LVBus1214086_production, 75_LVBus1214088_consumption, 75_LVBus1214088_production, 75_LVBus1214090_production, 75_LVBus1214091_production, 75_LVBus1214092_production, 75_LVBus1214093_production, 75_LVBus1214094_consumption, 75_LVBus1214094_production, 75_LVBus1214095_production, 75_LVBus1214097_consumption, 75_LVBus1214097_production, 75_LVBus1214098_consumption, 75_LVBus1214098_production, 75_LVBus1214099_production, 75_LVBus1214100_production, 75_LVBus1214101_production, 75_LVBus1214102_production, 75_LVBus1214103_production, 75_LVBus1214104_consumption, 75_LVBus1214104_production, 75_LVBus1214105_production, 75_LVBus1214106_production, 75_LVBus1214107_production, 75_LVBus1214108_consumption, 75_LVBus1214108_production, 75_LVBus1214110_consumption, 75_LVBus1214110_production, 75_LVBus1214111_production, 75_LVBus1214112_production, 75_LVBus1214113_production, 75_LVBus1214114_consumption, 75_LVBus1214114_production, 75_LVBus1214116_production, 75_LVBus1214117_production, 75_LVBus1214118_production, 75_LVBus1214119_production, 75_LVBus1214123_production, 75_LVBus1214125_production, 75_LVBus1214126_production, 75_LVBus1214127_production, 75_LVBus1214128_production, 75_LVBus1214129_production, 75_LVBus1214131_consumption, 75_LVBus1214131_production, 75_LVBus1214133_production, 75_LVBus1214134_consumption, 75_LVBus1214134_production, 75_LVBus1214135_production, 75_LVBus1214136_production, 75_LVBus1214137_production, 75_LVBus1214138_production, 75_LVBus1214139_production, 75_LVBus1214140_production, 75_LVBus1214144_production, 75_LVBus1214145_consumption, 75_LVBus1214145_production, 75_LVBus1214146_consumption, 75_LVBus1214146_production, 75_LVBus1214147_production, 75_LVBus1214148_production, 75_LVBus1214149_production, 75_LVBus1214150_production, 75_LVBus1214151_consumption, 75_LVBus1214151_production, 75_LVBus1214152_production, 75_LVBus1214153_production, 75_LVBus1214155_consumption, 75_LVBus1214155_production, 75_LVBus1214156_consumption, 75_LVBus1214156_production, 75_LVBus1214157_consumption, 75_LVBus1214157_production, 75_LVBus1214158_production, 75_LVBus1214159_production, 75_LVBus1926269_consumption, 75_LVBus1926269_production, 75_LVBus1929142_production, 75_LVBus1929143_production, 75_LVBus1929144_production, 75_LVBus1929145_production, 75_LVBus1929146_production, 75_LVBus1929749_production, 75_LVBus1945184_production, 75_LVBus1974649_production, 75_MVLV064430_consumption, 75_MVLV064430_production, 75_MVLV087795_consumption, 75_MVLV087795_production.

## 9. Data Quality Summary

**Total findings:** 358 (0 errors, 5 warnings, 353 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  739 of 1108 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.77 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  740 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213540_consumption`  
  Load '75_LVBus1213540_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213593_consumption`  
  Load '75_LVBus1213593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1929146_consumption`  
  Load '75_LVBus1929146_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213547_consumption`  
  Load '75_LVBus1213547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214051_consumption`  
  Load '75_LVBus1214051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1929144_consumption`  
  Load '75_LVBus1929144_consumption' has phase imbalance of 111.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213935_consumption`  
  Load '75_LVBus1213935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213747_consumption`  
  Load '75_LVBus1213747_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213480_consumption`  
  Load '75_LVBus1213480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213513_consumption`  
  Load '75_LVBus1213513_consumption' has phase imbalance of 284.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214159_consumption`  
  Load '75_LVBus1214159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213486_consumption`  
  Load '75_LVBus1213486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214010_consumption`  
  Load '75_LVBus1214010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213930_consumption`  
  Load '75_LVBus1213930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213721_consumption`  
  Load '75_LVBus1213721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214086_consumption`  
  Load '75_LVBus1214086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213542_consumption`  
  Load '75_LVBus1213542_consumption' has phase imbalance of 134.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213836_consumption`  
  Load '75_LVBus1213836_consumption' has phase imbalance of 223.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213965_consumption`  
  Load '75_LVBus1213965_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214126_consumption`  
  Load '75_LVBus1214126_consumption' has phase imbalance of 65.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213889_consumption`  
  Load '75_LVBus1213889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213691_consumption`  
  Load '75_LVBus1213691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214113_consumption`  
  Load '75_LVBus1214113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214052_consumption`  
  Load '75_LVBus1214052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213794_consumption`  
  Load '75_LVBus1213794_consumption' has phase imbalance of 131.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213907_consumption`  
  Load '75_LVBus1213907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213937_consumption`  
  Load '75_LVBus1213937_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213580_consumption`  
  Load '75_LVBus1213580_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213676_consumption`  
  Load '75_LVBus1213676_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214036_consumption`  
  Load '75_LVBus1214036_consumption' has phase imbalance of 259.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213677_consumption`  
  Load '75_LVBus1213677_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213514_consumption`  
  Load '75_LVBus1213514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213746_consumption`  
  Load '75_LVBus1213746_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214017_consumption`  
  Load '75_LVBus1214017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1929143_consumption`  
  Load '75_LVBus1929143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214117_consumption`  
  Load '75_LVBus1214117_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213518_consumption`  
  Load '75_LVBus1213518_consumption' has phase imbalance of 99.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213618_consumption`  
  Load '75_LVBus1213618_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213537_consumption`  
  Load '75_LVBus1213537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213562_consumption`  
  Load '75_LVBus1213562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213756_consumption`  
  Load '75_LVBus1213756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213922_consumption`  
  Load '75_LVBus1213922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213986_consumption`  
  Load '75_LVBus1213986_consumption' has phase imbalance of 141.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213539_consumption`  
  Load '75_LVBus1213539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213908_consumption`  
  Load '75_LVBus1213908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213789_consumption`  
  Load '75_LVBus1213789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213621_consumption`  
  Load '75_LVBus1213621_consumption' has phase imbalance of 265.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214102_consumption`  
  Load '75_LVBus1214102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213576_consumption`  
  Load '75_LVBus1213576_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213768_consumption`  
  Load '75_LVBus1213768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213611_consumption`  
  Load '75_LVBus1213611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213957_consumption`  
  Load '75_LVBus1213957_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213697_consumption`  
  Load '75_LVBus1213697_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214128_consumption`  
  Load '75_LVBus1214128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213798_consumption`  
  Load '75_LVBus1213798_consumption' has phase imbalance of 75.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213803_consumption`  
  Load '75_LVBus1213803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213469_consumption`  
  Load '75_LVBus1213469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214116_consumption`  
  Load '75_LVBus1214116_consumption' has phase imbalance of 271.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1929145_consumption`  
  Load '75_LVBus1929145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213524_consumption`  
  Load '75_LVBus1213524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214139_consumption`  
  Load '75_LVBus1214139_consumption' has phase imbalance of 131.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213530_consumption`  
  Load '75_LVBus1213530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213683_consumption`  
  Load '75_LVBus1213683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213885_consumption`  
  Load '75_LVBus1213885_consumption' has phase imbalance of 269.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214133_consumption`  
  Load '75_LVBus1214133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213661_consumption`  
  Load '75_LVBus1213661_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213646_consumption`  
  Load '75_LVBus1213646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213497_consumption`  
  Load '75_LVBus1213497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214012_consumption`  
  Load '75_LVBus1214012_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213462_consumption`  
  Load '75_LVBus1213462_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213887_consumption`  
  Load '75_LVBus1213887_consumption' has phase imbalance of 37.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213693_consumption`  
  Load '75_LVBus1213693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213610_consumption`  
  Load '75_LVBus1213610_consumption' has phase imbalance of 24.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213577_consumption`  
  Load '75_LVBus1213577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213823_consumption`  
  Load '75_LVBus1213823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213602_consumption`  
  Load '75_LVBus1213602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213635_consumption`  
  Load '75_LVBus1213635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213504_consumption`  
  Load '75_LVBus1213504_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213498_consumption`  
  Load '75_LVBus1213498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214047_consumption`  
  Load '75_LVBus1214047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213890_consumption`  
  Load '75_LVBus1213890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214041_consumption`  
  Load '75_LVBus1214041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213535_consumption`  
  Load '75_LVBus1213535_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214150_consumption`  
  Load '75_LVBus1214150_consumption' has phase imbalance of 201.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213624_consumption`  
  Load '75_LVBus1213624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213554_consumption`  
  Load '75_LVBus1213554_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213550_consumption`  
  Load '75_LVBus1213550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1929749_consumption`  
  Load '75_LVBus1929749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213914_consumption`  
  Load '75_LVBus1213914_consumption' has phase imbalance of 198.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213656_consumption`  
  Load '75_LVBus1213656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214153_consumption`  
  Load '75_LVBus1214153_consumption' has phase imbalance of 291.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213761_consumption`  
  Load '75_LVBus1213761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213811_consumption`  
  Load '75_LVBus1213811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214095_consumption`  
  Load '75_LVBus1214095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213769_consumption`  
  Load '75_LVBus1213769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213632_consumption`  
  Load '75_LVBus1213632_consumption' has phase imbalance of 158.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213775_consumption`  
  Load '75_LVBus1213775_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213866_consumption`  
  Load '75_LVBus1213866_consumption' has phase imbalance of 222.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213663_consumption`  
  Load '75_LVBus1213663_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214135_consumption`  
  Load '75_LVBus1214135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213512_consumption`  
  Load '75_LVBus1213512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213692_consumption`  
  Load '75_LVBus1213692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213744_consumption`  
  Load '75_LVBus1213744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214034_consumption`  
  Load '75_LVBus1214034_consumption' has phase imbalance of 212.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214040_consumption`  
  Load '75_LVBus1214040_consumption' has phase imbalance of 274.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213477_consumption`  
  Load '75_LVBus1213477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213993_consumption`  
  Load '75_LVBus1213993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213891_consumption`  
  Load '75_LVBus1213891_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213894_consumption`  
  Load '75_LVBus1213894_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214085_consumption`  
  Load '75_LVBus1214085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213466_consumption`  
  Load '75_LVBus1213466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213666_consumption`  
  Load '75_LVBus1213666_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213841_consumption`  
  Load '75_LVBus1213841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213820_consumption`  
  Load '75_LVBus1213820_consumption' has phase imbalance of 126.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214147_consumption`  
  Load '75_LVBus1214147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213879_consumption`  
  Load '75_LVBus1213879_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214003_consumption`  
  Load '75_LVBus1214003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213479_consumption`  
  Load '75_LVBus1213479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214048_consumption`  
  Load '75_LVBus1214048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213737_consumption`  
  Load '75_LVBus1213737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213945_consumption`  
  Load '75_LVBus1213945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213899_consumption`  
  Load '75_LVBus1213899_consumption' has phase imbalance of 117.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213544_consumption`  
  Load '75_LVBus1213544_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213791_consumption`  
  Load '75_LVBus1213791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213856_consumption`  
  Load '75_LVBus1213856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213679_consumption`  
  Load '75_LVBus1213679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213711_consumption`  
  Load '75_LVBus1213711_consumption' has phase imbalance of 214.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213847_consumption`  
  Load '75_LVBus1213847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213870_consumption`  
  Load '75_LVBus1213870_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213923_consumption`  
  Load '75_LVBus1213923_consumption' has phase imbalance of 268.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213565_consumption`  
  Load '75_LVBus1213565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213977_consumption`  
  Load '75_LVBus1213977_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214090_consumption`  
  Load '75_LVBus1214090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214099_consumption`  
  Load '75_LVBus1214099_consumption' has phase imbalance of 83.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213797_consumption`  
  Load '75_LVBus1213797_consumption' has phase imbalance of 268.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213592_consumption`  
  Load '75_LVBus1213592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213970_consumption`  
  Load '75_LVBus1213970_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213895_consumption`  
  Load '75_LVBus1213895_consumption' has phase imbalance of 235.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214002_consumption`  
  Load '75_LVBus1214002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213638_consumption`  
  Load '75_LVBus1213638_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214125_consumption`  
  Load '75_LVBus1214125_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213649_consumption`  
  Load '75_LVBus1213649_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213976_consumption`  
  Load '75_LVBus1213976_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214106_consumption`  
  Load '75_LVBus1214106_consumption' has phase imbalance of 156.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213943_consumption`  
  Load '75_LVBus1213943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214079_consumption`  
  Load '75_LVBus1214079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213582_consumption`  
  Load '75_LVBus1213582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213607_consumption`  
  Load '75_LVBus1213607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213695_consumption`  
  Load '75_LVBus1213695_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214004_consumption`  
  Load '75_LVBus1214004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213869_consumption`  
  Load '75_LVBus1213869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213772_consumption`  
  Load '75_LVBus1213772_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214140_consumption`  
  Load '75_LVBus1214140_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214011_consumption`  
  Load '75_LVBus1214011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214062_consumption`  
  Load '75_LVBus1214062_consumption' has phase imbalance of 272.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213664_consumption`  
  Load '75_LVBus1213664_consumption' has phase imbalance of 131.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214107_consumption`  
  Load '75_LVBus1214107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213969_consumption`  
  Load '75_LVBus1213969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213496_consumption`  
  Load '75_LVBus1213496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214148_consumption`  
  Load '75_LVBus1214148_consumption' has phase imbalance of 101.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213669_consumption`  
  Load '75_LVBus1213669_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213758_consumption`  
  Load '75_LVBus1213758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213835_consumption`  
  Load '75_LVBus1213835_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213748_consumption`  
  Load '75_LVBus1213748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213867_consumption`  
  Load '75_LVBus1213867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213490_consumption`  
  Load '75_LVBus1213490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214076_consumption`  
  Load '75_LVBus1214076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213623_consumption`  
  Load '75_LVBus1213623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213684_consumption`  
  Load '75_LVBus1213684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213604_consumption`  
  Load '75_LVBus1213604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214091_consumption`  
  Load '75_LVBus1214091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214129_consumption`  
  Load '75_LVBus1214129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213888_consumption`  
  Load '75_LVBus1213888_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214063_consumption`  
  Load '75_LVBus1214063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213489_consumption`  
  Load '75_LVBus1213489_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213968_consumption`  
  Load '75_LVBus1213968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214039_consumption`  
  Load '75_LVBus1214039_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214066_consumption`  
  Load '75_LVBus1214066_consumption' has phase imbalance of 28.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213842_consumption`  
  Load '75_LVBus1213842_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1945184_consumption`  
  Load '75_LVBus1945184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213805_consumption`  
  Load '75_LVBus1213805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213572_consumption`  
  Load '75_LVBus1213572_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214015_consumption`  
  Load '75_LVBus1214015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213925_consumption`  
  Load '75_LVBus1213925_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213916_consumption`  
  Load '75_LVBus1213916_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213738_consumption`  
  Load '75_LVBus1213738_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214136_consumption`  
  Load '75_LVBus1214136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213802_consumption`  
  Load '75_LVBus1213802_consumption' has phase imbalance of 170.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214000_consumption`  
  Load '75_LVBus1214000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213752_consumption`  
  Load '75_LVBus1213752_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214101_consumption`  
  Load '75_LVBus1214101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213955_consumption`  
  Load '75_LVBus1213955_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214138_consumption`  
  Load '75_LVBus1214138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213501_consumption`  
  Load '75_LVBus1213501_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214006_consumption`  
  Load '75_LVBus1214006_consumption' has phase imbalance of 102.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214105_consumption`  
  Load '75_LVBus1214105_consumption' has phase imbalance of 56.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213815_consumption`  
  Load '75_LVBus1213815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213499_consumption`  
  Load '75_LVBus1213499_consumption' has phase imbalance of 215.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213896_consumption`  
  Load '75_LVBus1213896_consumption' has phase imbalance of 249.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213796_consumption`  
  Load '75_LVBus1213796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213521_consumption`  
  Load '75_LVBus1213521_consumption' has phase imbalance of 249.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213881_consumption`  
  Load '75_LVBus1213881_consumption' has phase imbalance of 215.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213941_consumption`  
  Load '75_LVBus1213941_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213583_consumption`  
  Load '75_LVBus1213583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213855_consumption`  
  Load '75_LVBus1213855_consumption' has phase imbalance of 272.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213475_consumption`  
  Load '75_LVBus1213475_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213821_consumption`  
  Load '75_LVBus1213821_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214137_consumption`  
  Load '75_LVBus1214137_consumption' has phase imbalance of 254.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213837_consumption`  
  Load '75_LVBus1213837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214112_consumption`  
  Load '75_LVBus1214112_consumption' has phase imbalance of 99.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213698_consumption`  
  Load '75_LVBus1213698_consumption' has phase imbalance of 233.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214149_consumption`  
  Load '75_LVBus1214149_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213767_consumption`  
  Load '75_LVBus1213767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213468_consumption`  
  Load '75_LVBus1213468_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214009_consumption`  
  Load '75_LVBus1214009_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213936_consumption`  
  Load '75_LVBus1213936_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214068_consumption`  
  Load '75_LVBus1214068_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214069_consumption`  
  Load '75_LVBus1214069_consumption' has phase imbalance of 100.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214071_consumption`  
  Load '75_LVBus1214071_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213853_consumption`  
  Load '75_LVBus1213853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213833_consumption`  
  Load '75_LVBus1213833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213484_consumption`  
  Load '75_LVBus1213484_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213814_consumption`  
  Load '75_LVBus1213814_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214111_consumption`  
  Load '75_LVBus1214111_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213898_consumption`  
  Load '75_LVBus1213898_consumption' has phase imbalance of 112.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214103_consumption`  
  Load '75_LVBus1214103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213700_consumption`  
  Load '75_LVBus1213700_consumption' has phase imbalance of 275.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213478_consumption`  
  Load '75_LVBus1213478_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213950_consumption`  
  Load '75_LVBus1213950_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1929142_consumption`  
  Load '75_LVBus1929142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213634_consumption`  
  Load '75_LVBus1213634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213851_consumption`  
  Load '75_LVBus1213851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213599_consumption`  
  Load '75_LVBus1213599_consumption' has phase imbalance of 289.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214001_consumption`  
  Load '75_LVBus1214001_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213892_consumption`  
  Load '75_LVBus1213892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213865_consumption`  
  Load '75_LVBus1213865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213568_consumption`  
  Load '75_LVBus1213568_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213913_consumption`  
  Load '75_LVBus1213913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213776_consumption`  
  Load '75_LVBus1213776_consumption' has phase imbalance of 218.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213712_consumption`  
  Load '75_LVBus1213712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213696_consumption`  
  Load '75_LVBus1213696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213675_consumption`  
  Load '75_LVBus1213675_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213625_consumption`  
  Load '75_LVBus1213625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214083_consumption`  
  Load '75_LVBus1214083_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213994_consumption`  
  Load '75_LVBus1213994_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213662_consumption`  
  Load '75_LVBus1213662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213689_consumption`  
  Load '75_LVBus1213689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214070_consumption`  
  Load '75_LVBus1214070_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213807_consumption`  
  Load '75_LVBus1213807_consumption' has phase imbalance of 201.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213516_consumption`  
  Load '75_LVBus1213516_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213843_consumption`  
  Load '75_LVBus1213843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214118_consumption`  
  Load '75_LVBus1214118_consumption' has phase imbalance of 235.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213543_consumption`  
  Load '75_LVBus1213543_consumption' has phase imbalance of 242.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213655_consumption`  
  Load '75_LVBus1213655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213708_consumption`  
  Load '75_LVBus1213708_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213877_consumption`  
  Load '75_LVBus1213877_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214100_consumption`  
  Load '75_LVBus1214100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213813_consumption`  
  Load '75_LVBus1213813_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213948_consumption`  
  Load '75_LVBus1213948_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214081_consumption`  
  Load '75_LVBus1214081_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214061_consumption`  
  Load '75_LVBus1214061_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213670_consumption`  
  Load '75_LVBus1213670_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214055_consumption`  
  Load '75_LVBus1214055_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213581_consumption`  
  Load '75_LVBus1213581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213792_consumption`  
  Load '75_LVBus1213792_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213575_consumption`  
  Load '75_LVBus1213575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213628_consumption`  
  Load '75_LVBus1213628_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213900_consumption`  
  Load '75_LVBus1213900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213517_consumption`  
  Load '75_LVBus1213517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213824_consumption`  
  Load '75_LVBus1213824_consumption' has phase imbalance of 112.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214144_consumption`  
  Load '75_LVBus1214144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214028_consumption`  
  Load '75_LVBus1214028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213519_consumption`  
  Load '75_LVBus1213519_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213893_consumption`  
  Load '75_LVBus1213893_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213862_consumption`  
  Load '75_LVBus1213862_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213999_consumption`  
  Load '75_LVBus1213999_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213680_consumption`  
  Load '75_LVBus1213680_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213641_consumption`  
  Load '75_LVBus1213641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214064_consumption`  
  Load '75_LVBus1214064_consumption' has phase imbalance of 87.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213992_consumption`  
  Load '75_LVBus1213992_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213745_consumption`  
  Load '75_LVBus1213745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213874_consumption`  
  Load '75_LVBus1213874_consumption' has phase imbalance of 81.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213886_consumption`  
  Load '75_LVBus1213886_consumption' has phase imbalance of 283.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213940_consumption`  
  Load '75_LVBus1213940_consumption' has phase imbalance of 216.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213690_consumption`  
  Load '75_LVBus1213690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213719_consumption`  
  Load '75_LVBus1213719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213620_consumption`  
  Load '75_LVBus1213620_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213556_consumption`  
  Load '75_LVBus1213556_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213742_consumption`  
  Load '75_LVBus1213742_consumption' has phase imbalance of 215.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213579_consumption`  
  Load '75_LVBus1213579_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213546_consumption`  
  Load '75_LVBus1213546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213929_consumption`  
  Load '75_LVBus1213929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213765_consumption`  
  Load '75_LVBus1213765_consumption' has phase imbalance of 237.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213750_consumption`  
  Load '75_LVBus1213750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213694_consumption`  
  Load '75_LVBus1213694_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214016_consumption`  
  Load '75_LVBus1214016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214060_consumption`  
  Load '75_LVBus1214060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213978_consumption`  
  Load '75_LVBus1213978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213560_consumption`  
  Load '75_LVBus1213560_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213485_consumption`  
  Load '75_LVBus1213485_consumption' has phase imbalance of 129.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213471_consumption`  
  Load '75_LVBus1213471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214152_consumption`  
  Load '75_LVBus1214152_consumption' has phase imbalance of 207.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214059_consumption`  
  Load '75_LVBus1214059_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213609_consumption`  
  Load '75_LVBus1213609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213473_consumption`  
  Load '75_LVBus1213473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213639_consumption`  
  Load '75_LVBus1213639_consumption' has phase imbalance of 50.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213668_consumption`  
  Load '75_LVBus1213668_consumption' has phase imbalance of 158.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214030_consumption`  
  Load '75_LVBus1214030_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213880_consumption`  
  Load '75_LVBus1213880_consumption' has phase imbalance of 290.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213559_consumption`  
  Load '75_LVBus1213559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213463_consumption`  
  Load '75_LVBus1213463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213667_consumption`  
  Load '75_LVBus1213667_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214013_consumption`  
  Load '75_LVBus1214013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214058_consumption`  
  Load '75_LVBus1214058_consumption' has phase imbalance of 47.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214067_consumption`  
  Load '75_LVBus1214067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213985_consumption`  
  Load '75_LVBus1213985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213921_consumption`  
  Load '75_LVBus1213921_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213564_consumption`  
  Load '75_LVBus1213564_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214093_consumption`  
  Load '75_LVBus1214093_consumption' has phase imbalance of 171.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214024_consumption`  
  Load '75_LVBus1214024_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213873_consumption`  
  Load '75_LVBus1213873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213787_consumption`  
  Load '75_LVBus1213787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213472_consumption`  
  Load '75_LVBus1213472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213616_consumption`  
  Load '75_LVBus1213616_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213510_consumption`  
  Load '75_LVBus1213510_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213730_consumption`  
  Load '75_LVBus1213730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1214092_consumption`  
  Load '75_LVBus1214092_consumption' has phase imbalance of 253.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213608_consumption`  
  Load '75_LVBus1213608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213876_consumption`  
  Load '75_LVBus1213876_consumption' has phase imbalance of 239.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1213981_consumption`  
  Load '75_LVBus1213981_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1108 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1213829' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1213800' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1213723' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_ORTH5' (MV, 11.78 kV) has an electrical reach of 20.58 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1213829' (LV, 0.24 kV) has an electrical reach of 13.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1213950' (LV, 0.24 kV) has an electrical reach of 16.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1213831' (LV, 0.24 kV) has an electrical reach of 22.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1214131' (LV, 0.24 kV) has an electrical reach of 11.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  765 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  268 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1213463_consumption, 75_LVBus1213466_consumption, 75_LVBus1213468_consumption, 75_LVBus1213469_consumption, 75_LVBus1213471_consumption, 75_LVBus1213472_consumption, 75_LVBus1213473_consumption, 75_LVBus1213475_consumption, 75_LVBus1213477_consumption, 75_LVBus1213479_consumption, 75_LVBus1213480_consumption, 75_LVBus1213486_consumption, 75_LVBus1213489_consumption, 75_LVBus1213490_consumption, 75_LVBus1213496_consumption, 75_LVBus1213497_consumption, 75_LVBus1213498_consumption, 75_LVBus1213499_consumption, 75_LVBus1213501_consumption, 75_LVBus1213504_consumption, 75_LVBus1213510_consumption, 75_LVBus1213512_consumption, 75_LVBus1213513_consumption, 75_LVBus1213514_consumption, 75_LVBus1213516_consumption, 75_LVBus1213517_consumption, 75_LVBus1213519_consumption, 75_LVBus1213521_consumption, 75_LVBus1213524_consumption, 75_LVBus1213530_consumption, 75_LVBus1213535_consumption, 75_LVBus1213537_consumption, 75_LVBus1213539_consumption, 75_LVBus1213540_consumption, 75_LVBus1213543_consumption, 75_LVBus1213544_consumption, 75_LVBus1213546_consumption, 75_LVBus1213547_consumption, 75_LVBus1213550_consumption, 75_LVBus1213556_consumption, 75_LVBus1213559_consumption, 75_LVBus1213560_consumption, 75_LVBus1213562_consumption, 75_LVBus1213564_consumption, 75_LVBus1213565_consumption, 75_LVBus1213568_consumption, 75_LVBus1213572_consumption, 75_LVBus1213575_consumption, 75_LVBus1213576_consumption, 75_LVBus1213577_consumption, 75_LVBus1213579_consumption, 75_LVBus1213580_consumption, 75_LVBus1213581_consumption, 75_LVBus1213582_consumption, 75_LVBus1213583_consumption, 75_LVBus1213592_consumption, 75_LVBus1213593_consumption, 75_LVBus1213602_consumption, 75_LVBus1213604_consumption, 75_LVBus1213607_consumption, 75_LVBus1213608_consumption, 75_LVBus1213609_consumption, 75_LVBus1213611_consumption, 75_LVBus1213618_consumption, 75_LVBus1213620_consumption, 75_LVBus1213621_consumption, 75_LVBus1213623_consumption, 75_LVBus1213624_consumption, 75_LVBus1213625_consumption, 75_LVBus1213628_consumption, 75_LVBus1213632_consumption, 75_LVBus1213634_consumption, 75_LVBus1213635_consumption, 75_LVBus1213638_consumption, 75_LVBus1213641_consumption, 75_LVBus1213646_consumption, 75_LVBus1213649_consumption, 75_LVBus1213655_consumption, 75_LVBus1213656_consumption, 75_LVBus1213662_consumption, 75_LVBus1213663_consumption, 75_LVBus1213667_consumption, 75_LVBus1213668_consumption, 75_LVBus1213669_consumption, 75_LVBus1213670_consumption, 75_LVBus1213675_consumption, 75_LVBus1213676_consumption, 75_LVBus1213679_consumption, 75_LVBus1213680_consumption, 75_LVBus1213683_consumption, 75_LVBus1213684_consumption, 75_LVBus1213689_consumption, 75_LVBus1213690_consumption, 75_LVBus1213691_consumption, 75_LVBus1213692_consumption, 75_LVBus1213693_consumption, 75_LVBus1213694_consumption, 75_LVBus1213695_consumption, 75_LVBus1213696_consumption, 75_LVBus1213697_consumption, 75_LVBus1213698_consumption, 75_LVBus1213700_consumption, 75_LVBus1213712_consumption, 75_LVBus1213719_consumption, 75_LVBus1213721_consumption, 75_LVBus1213730_consumption, 75_LVBus1213737_consumption, 75_LVBus1213738_consumption, 75_LVBus1213742_consumption, 75_LVBus1213744_consumption, 75_LVBus1213745_consumption, 75_LVBus1213747_consumption, 75_LVBus1213748_consumption, 75_LVBus1213750_consumption, 75_LVBus1213752_consumption, 75_LVBus1213756_consumption, 75_LVBus1213758_consumption, 75_LVBus1213761_consumption, 75_LVBus1213767_consumption, 75_LVBus1213768_consumption, 75_LVBus1213769_consumption, 75_LVBus1213772_consumption, 75_LVBus1213775_consumption, 75_LVBus1213776_consumption, 75_LVBus1213787_consumption, 75_LVBus1213789_consumption, 75_LVBus1213791_consumption, 75_LVBus1213792_consumption, 75_LVBus1213796_consumption, 75_LVBus1213802_consumption, 75_LVBus1213803_consumption, 75_LVBus1213805_consumption, 75_LVBus1213807_consumption, 75_LVBus1213811_consumption, 75_LVBus1213813_consumption, 75_LVBus1213814_consumption, 75_LVBus1213815_consumption, 75_LVBus1213821_consumption, 75_LVBus1213823_consumption, 75_LVBus1213833_consumption, 75_LVBus1213835_consumption, 75_LVBus1213836_consumption, 75_LVBus1213837_consumption, 75_LVBus1213841_consumption, 75_LVBus1213842_consumption, 75_LVBus1213843_consumption, 75_LVBus1213847_consumption, 75_LVBus1213851_consumption, 75_LVBus1213853_consumption, 75_LVBus1213855_consumption, 75_LVBus1213856_consumption, 75_LVBus1213862_consumption, 75_LVBus1213865_consumption, 75_LVBus1213866_consumption, 75_LVBus1213867_consumption, 75_LVBus1213869_consumption, 75_LVBus1213870_consumption, 75_LVBus1213873_consumption, 75_LVBus1213876_consumption, 75_LVBus1213877_consumption, 75_LVBus1213879_consumption, 75_LVBus1213885_consumption, 75_LVBus1213886_consumption, 75_LVBus1213888_consumption, 75_LVBus1213889_consumption, 75_LVBus1213890_consumption, 75_LVBus1213892_consumption, 75_LVBus1213894_consumption, 75_LVBus1213895_consumption, 75_LVBus1213896_consumption, 75_LVBus1213900_consumption, 75_LVBus1213907_consumption, 75_LVBus1213908_consumption, 75_LVBus1213913_consumption, 75_LVBus1213914_consumption, 75_LVBus1213916_consumption, 75_LVBus1213921_consumption, 75_LVBus1213922_consumption, 75_LVBus1213929_consumption, 75_LVBus1213930_consumption, 75_LVBus1213935_consumption, 75_LVBus1213937_consumption, 75_LVBus1213940_consumption, 75_LVBus1213941_consumption, 75_LVBus1213943_consumption, 75_LVBus1213945_consumption, 75_LVBus1213948_consumption, 75_LVBus1213950_consumption, 75_LVBus1213955_consumption, 75_LVBus1213957_consumption, 75_LVBus1213965_consumption, 75_LVBus1213968_consumption, 75_LVBus1213969_consumption, 75_LVBus1213970_consumption, 75_LVBus1213976_consumption, 75_LVBus1213977_consumption, 75_LVBus1213978_consumption, 75_LVBus1213981_consumption, 75_LVBus1213985_consumption, 75_LVBus1213992_consumption, 75_LVBus1213993_consumption, 75_LVBus1213994_consumption, 75_LVBus1213999_consumption, 75_LVBus1214000_consumption, 75_LVBus1214001_consumption, 75_LVBus1214002_consumption, 75_LVBus1214003_consumption, 75_LVBus1214004_consumption, 75_LVBus1214009_consumption, 75_LVBus1214010_consumption, 75_LVBus1214011_consumption, 75_LVBus1214013_consumption, 75_LVBus1214015_consumption, 75_LVBus1214016_consumption, 75_LVBus1214017_consumption, 75_LVBus1214028_consumption, 75_LVBus1214039_consumption, 75_LVBus1214041_consumption, 75_LVBus1214047_consumption, 75_LVBus1214048_consumption, 75_LVBus1214051_consumption, 75_LVBus1214052_consumption, 75_LVBus1214060_consumption, 75_LVBus1214062_consumption, 75_LVBus1214063_consumption, 75_LVBus1214067_consumption, 75_LVBus1214068_consumption, 75_LVBus1214070_consumption, 75_LVBus1214076_consumption, 75_LVBus1214079_consumption, 75_LVBus1214081_consumption, 75_LVBus1214085_consumption, 75_LVBus1214086_consumption, 75_LVBus1214090_consumption, 75_LVBus1214091_consumption, 75_LVBus1214093_consumption, 75_LVBus1214095_consumption, 75_LVBus1214100_consumption, 75_LVBus1214101_consumption, 75_LVBus1214102_consumption, 75_LVBus1214103_consumption, 75_LVBus1214106_consumption, 75_LVBus1214107_consumption, 75_LVBus1214111_consumption, 75_LVBus1214113_consumption, 75_LVBus1214116_consumption, 75_LVBus1214117_consumption, 75_LVBus1214118_consumption, 75_LVBus1214128_consumption, 75_LVBus1214129_consumption, 75_LVBus1214133_consumption, 75_LVBus1214135_consumption, 75_LVBus1214136_consumption, 75_LVBus1214137_consumption, 75_LVBus1214138_consumption, 75_LVBus1214140_consumption, 75_LVBus1214144_consumption, 75_LVBus1214147_consumption, 75_LVBus1214150_consumption, 75_LVBus1214152_consumption, 75_LVBus1214153_consumption, 75_LVBus1214159_consumption, 75_LVBus1929142_consumption, 75_LVBus1929143_consumption, 75_LVBus1929145_consumption, 75_LVBus1929146_consumption, 75_LVBus1929749_consumption, 75_LVBus1945184_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  554 group(s) of loads (1108 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  15 group(s) of series lines (30 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  740 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1213458_consumption, 75_LVBus1213458_production, 75_LVBus1213459_consumption, 75_LVBus1213459_production, 75_LVBus1213460_consumption, 75_LVBus1213460_production, 75_LVBus1213461_consumption, 75_LVBus1213461_production, 75_LVBus1213462_production, 75_LVBus1213463_production, 75_LVBus1213464_consumption, 75_LVBus1213464_production, 75_LVBus1213465_consumption, 75_LVBus1213465_production, 75_LVBus1213466_production, 75_LVBus1213468_production, 75_LVBus1213469_production, 75_LVBus1213471_production, 75_LVBus1213472_production, 75_LVBus1213473_production, 75_LVBus1213474_production, 75_LVBus1213475_production, 75_LVBus1213477_production, 75_LVBus1213478_production, 75_LVBus1213479_production, 75_LVBus1213480_production, 75_LVBus1213481_consumption, 75_LVBus1213481_production, 75_LVBus1213482_consumption, 75_LVBus1213482_production, 75_LVBus1213484_production, 75_LVBus1213485_production, 75_LVBus1213486_production, 75_LVBus1213487_consumption, 75_LVBus1213487_production, 75_LVBus1213488_consumption, 75_LVBus1213488_production, 75_LVBus1213489_production, 75_LVBus1213490_production, 75_LVBus1213492_consumption, 75_LVBus1213492_production, 75_LVBus1213496_production, 75_LVBus1213497_production, 75_LVBus1213498_production, 75_LVBus1213499_production, 75_LVBus1213500_consumption, 75_LVBus1213500_production, 75_LVBus1213501_production, 75_LVBus1213502_consumption, 75_LVBus1213502_production, 75_LVBus1213503_consumption, 75_LVBus1213503_production, 75_LVBus1213504_production, 75_LVBus1213509_consumption, 75_LVBus1213509_production, 75_LVBus1213510_production, 75_LVBus1213511_consumption, 75_LVBus1213511_production, 75_LVBus1213512_production, 75_LVBus1213513_production, 75_LVBus1213514_production, 75_LVBus1213515_consumption, 75_LVBus1213515_production, 75_LVBus1213516_production, 75_LVBus1213517_production, 75_LVBus1213518_production, 75_LVBus1213519_production, 75_LVBus1213521_production, 75_LVBus1213522_consumption, 75_LVBus1213522_production, 75_LVBus1213523_consumption, 75_LVBus1213523_production, 75_LVBus1213524_production, 75_LVBus1213526_consumption, 75_LVBus1213526_production, 75_LVBus1213527_consumption, 75_LVBus1213527_production, 75_LVBus1213528_consumption, 75_LVBus1213528_production, 75_LVBus1213529_consumption, 75_LVBus1213529_production, 75_LVBus1213530_production, 75_LVBus1213534_production, 75_LVBus1213535_production, 75_LVBus1213536_consumption, 75_LVBus1213536_production, 75_LVBus1213537_production, 75_LVBus1213538_consumption, 75_LVBus1213538_production, 75_LVBus1213539_production, 75_LVBus1213540_production, 75_LVBus1213541_consumption, 75_LVBus1213541_production, 75_LVBus1213542_production, 75_LVBus1213543_production, 75_LVBus1213544_production, 75_LVBus1213545_consumption, 75_LVBus1213545_production, 75_LVBus1213546_production, 75_LVBus1213547_production, 75_LVBus1213549_consumption, 75_LVBus1213549_production, 75_LVBus1213550_production, 75_LVBus1213551_consumption, 75_LVBus1213551_production, 75_LVBus1213553_consumption, 75_LVBus1213553_production, 75_LVBus1213554_production, 75_LVBus1213555_consumption, 75_LVBus1213555_production, 75_LVBus1213556_production, 75_LVBus1213558_consumption, 75_LVBus1213558_production, 75_LVBus1213559_production, 75_LVBus1213560_production, 75_LVBus1213562_production, 75_LVBus1213563_consumption, 75_LVBus1213563_production, 75_LVBus1213564_production, 75_LVBus1213565_production, 75_LVBus1213566_consumption, 75_LVBus1213566_production, 75_LVBus1213567_consumption, 75_LVBus1213567_production, 75_LVBus1213568_production, 75_LVBus1213570_consumption, 75_LVBus1213570_production, 75_LVBus1213571_consumption, 75_LVBus1213571_production, 75_LVBus1213572_production, 75_LVBus1213573_consumption, 75_LVBus1213573_production, 75_LVBus1213574_consumption, 75_LVBus1213574_production, 75_LVBus1213575_production, 75_LVBus1213576_production, 75_LVBus1213577_production, 75_LVBus1213579_production, 75_LVBus1213580_production, 75_LVBus1213581_production, 75_LVBus1213582_production, 75_LVBus1213583_production, 75_LVBus1213585_consumption, 75_LVBus1213585_production, 75_LVBus1213586_consumption, 75_LVBus1213586_production, 75_LVBus1213587_consumption, 75_LVBus1213587_production, 75_LVBus1213588_consumption, 75_LVBus1213588_production, 75_LVBus1213589_consumption, 75_LVBus1213589_production, 75_LVBus1213590_consumption, 75_LVBus1213590_production, 75_LVBus1213591_consumption, 75_LVBus1213591_production, 75_LVBus1213592_production, 75_LVBus1213593_production, 75_LVBus1213594_consumption, 75_LVBus1213594_production, 75_LVBus1213596_consumption, 75_LVBus1213596_production, 75_LVBus1213597_production, 75_LVBus1213599_production, 75_LVBus1213601_consumption, 75_LVBus1213601_production, 75_LVBus1213602_production, 75_LVBus1213603_consumption, 75_LVBus1213603_production, 75_LVBus1213604_production, 75_LVBus1213607_production, 75_LVBus1213608_production, 75_LVBus1213609_production, 75_LVBus1213610_production, 75_LVBus1213611_production, 75_LVBus1213615_consumption, 75_LVBus1213615_production, 75_LVBus1213616_production, 75_LVBus1213617_consumption, 75_LVBus1213617_production, 75_LVBus1213618_production, 75_LVBus1213619_consumption, 75_LVBus1213619_production, 75_LVBus1213620_production, 75_LVBus1213621_production, 75_LVBus1213622_consumption, 75_LVBus1213622_production, 75_LVBus1213623_production, 75_LVBus1213624_production, 75_LVBus1213625_production, 75_LVBus1213626_consumption, 75_LVBus1213626_production, 75_LVBus1213627_consumption, 75_LVBus1213627_production, 75_LVBus1213628_production, 75_LVBus1213632_production, 75_LVBus1213633_consumption, 75_LVBus1213633_production, 75_LVBus1213634_production, 75_LVBus1213635_production, 75_LVBus1213637_production, 75_LVBus1213638_production, 75_LVBus1213639_production, 75_LVBus1213640_consumption, 75_LVBus1213640_production, 75_LVBus1213641_production, 75_LVBus1213642_consumption, 75_LVBus1213642_production, 75_LVBus1213643_consumption, 75_LVBus1213643_production, 75_LVBus1213645_consumption, 75_LVBus1213645_production, 75_LVBus1213646_production, 75_LVBus1213648_consumption, 75_LVBus1213648_production, 75_LVBus1213649_production, 75_LVBus1213650_consumption, 75_LVBus1213650_production, 75_LVBus1213654_consumption, 75_LVBus1213654_production, 75_LVBus1213655_production, 75_LVBus1213656_production, 75_LVBus1213660_consumption, 75_LVBus1213660_production, 75_LVBus1213661_production, 75_LVBus1213662_production, 75_LVBus1213663_production, 75_LVBus1213664_production, 75_LVBus1213665_consumption, 75_LVBus1213665_production, 75_LVBus1213666_production, 75_LVBus1213667_production, 75_LVBus1213668_production, 75_LVBus1213669_production, 75_LVBus1213670_production, 75_LVBus1213674_consumption, 75_LVBus1213674_production, 75_LVBus1213675_production, 75_LVBus1213676_production, 75_LVBus1213677_production, 75_LVBus1213678_consumption, 75_LVBus1213678_production, 75_LVBus1213679_production, 75_LVBus1213680_production, 75_LVBus1213682_consumption, 75_LVBus1213682_production, 75_LVBus1213683_production, 75_LVBus1213684_production, 75_LVBus1213688_production, 75_LVBus1213689_production, 75_LVBus1213690_production, 75_LVBus1213691_production, 75_LVBus1213692_production, 75_LVBus1213693_production, 75_LVBus1213694_production, 75_LVBus1213695_production, 75_LVBus1213696_production, 75_LVBus1213697_production, 75_LVBus1213698_production, 75_LVBus1213699_production, 75_LVBus1213700_production, 75_LVBus1213705_consumption, 75_LVBus1213705_production, 75_LVBus1213707_consumption, 75_LVBus1213707_production, 75_LVBus1213708_production, 75_LVBus1213710_consumption, 75_LVBus1213710_production, 75_LVBus1213711_production, 75_LVBus1213712_production, 75_LVBus1213713_production, 75_LVBus1213714_production, 75_LVBus1213718_consumption, 75_LVBus1213718_production, 75_LVBus1213719_production, 75_LVBus1213721_production, 75_LVBus1213723_production, 75_LVBus1213725_consumption, 75_LVBus1213725_production, 75_LVBus1213727_consumption, 75_LVBus1213727_production, 75_LVBus1213728_consumption, 75_LVBus1213728_production, 75_LVBus1213729_consumption, 75_LVBus1213729_production, 75_LVBus1213730_production, 75_LVBus1213731_consumption, 75_LVBus1213731_production, 75_LVBus1213733_consumption, 75_LVBus1213733_production, 75_LVBus1213734_consumption, 75_LVBus1213734_production, 75_LVBus1213735_consumption, 75_LVBus1213735_production, 75_LVBus1213736_consumption, 75_LVBus1213736_production, 75_LVBus1213737_production, 75_LVBus1213738_production, 75_LVBus1213739_consumption, 75_LVBus1213739_production, 75_LVBus1213742_production, 75_LVBus1213743_consumption, 75_LVBus1213743_production, 75_LVBus1213744_production, 75_LVBus1213745_production, 75_LVBus1213746_production, 75_LVBus1213747_production, 75_LVBus1213748_production, 75_LVBus1213749_consumption, 75_LVBus1213749_production, 75_LVBus1213750_production, 75_LVBus1213751_consumption, 75_LVBus1213751_production, 75_LVBus1213752_production, 75_LVBus1213754_consumption, 75_LVBus1213754_production, 75_LVBus1213755_consumption, 75_LVBus1213755_production, 75_LVBus1213756_production, 75_LVBus1213757_consumption, 75_LVBus1213757_production, 75_LVBus1213758_production, 75_LVBus1213759_consumption, 75_LVBus1213759_production, 75_LVBus1213760_production, 75_LVBus1213761_production, 75_LVBus1213762_consumption, 75_LVBus1213762_production, 75_LVBus1213764_production, 75_LVBus1213765_production, 75_LVBus1213766_consumption, 75_LVBus1213766_production, 75_LVBus1213767_production, 75_LVBus1213768_production, 75_LVBus1213769_production, 75_LVBus1213771_consumption, 75_LVBus1213771_production, 75_LVBus1213772_production, 75_LVBus1213774_consumption, 75_LVBus1213774_production, 75_LVBus1213775_production, 75_LVBus1213776_production, 75_LVBus1213780_consumption, 75_LVBus1213780_production, 75_LVBus1213782_consumption, 75_LVBus1213782_production, 75_LVBus1213784_consumption, 75_LVBus1213784_production, 75_LVBus1213786_consumption, 75_LVBus1213786_production, 75_LVBus1213787_production, 75_LVBus1213788_consumption, 75_LVBus1213788_production, 75_LVBus1213789_production, 75_LVBus1213790_production, 75_LVBus1213791_production, 75_LVBus1213792_production, 75_LVBus1213793_consumption, 75_LVBus1213793_production, 75_LVBus1213794_production, 75_LVBus1213796_production, 75_LVBus1213797_production, 75_LVBus1213798_production, 75_LVBus1213800_production, 75_LVBus1213802_production, 75_LVBus1213803_production, 75_LVBus1213805_production, 75_LVBus1213806_consumption, 75_LVBus1213806_production, 75_LVBus1213807_production, 75_LVBus1213809_production, 75_LVBus1213811_production, 75_LVBus1213813_production, 75_LVBus1213814_production, 75_LVBus1213815_production, 75_LVBus1213816_consumption, 75_LVBus1213816_production, 75_LVBus1213817_consumption, 75_LVBus1213817_production, 75_LVBus1213818_consumption, 75_LVBus1213818_production, 75_LVBus1213820_production, 75_LVBus1213821_production, 75_LVBus1213823_production, 75_LVBus1213824_production, 75_LVBus1213825_production, 75_LVBus1213826_consumption, 75_LVBus1213826_production, 75_LVBus1213829_production, 75_LVBus1213831_consumption, 75_LVBus1213831_production, 75_LVBus1213833_production, 75_LVBus1213834_consumption, 75_LVBus1213834_production, 75_LVBus1213835_production, 75_LVBus1213836_production, 75_LVBus1213837_production, 75_LVBus1213839_consumption, 75_LVBus1213839_production, 75_LVBus1213840_consumption, 75_LVBus1213840_production, 75_LVBus1213841_production, 75_LVBus1213842_production, 75_LVBus1213843_production, 75_LVBus1213845_consumption, 75_LVBus1213845_production, 75_LVBus1213846_consumption, 75_LVBus1213846_production, 75_LVBus1213847_production, 75_LVBus1213848_consumption, 75_LVBus1213848_production, 75_LVBus1213849_consumption, 75_LVBus1213849_production, 75_LVBus1213850_consumption, 75_LVBus1213850_production, 75_LVBus1213851_production, 75_LVBus1213852_consumption, 75_LVBus1213852_production, 75_LVBus1213853_production, 75_LVBus1213854_consumption, 75_LVBus1213854_production, 75_LVBus1213855_production, 75_LVBus1213856_production, 75_LVBus1213857_consumption, 75_LVBus1213857_production, 75_LVBus1213859_consumption, 75_LVBus1213859_production, 75_LVBus1213860_consumption, 75_LVBus1213860_production, 75_LVBus1213861_consumption, 75_LVBus1213861_production, 75_LVBus1213862_production, 75_LVBus1213864_production, 75_LVBus1213865_production, 75_LVBus1213866_production, 75_LVBus1213867_production, 75_LVBus1213868_consumption, 75_LVBus1213868_production, 75_LVBus1213869_production, 75_LVBus1213870_production, 75_LVBus1213871_consumption, 75_LVBus1213871_production, 75_LVBus1213873_production, 75_LVBus1213874_production, 75_LVBus1213876_production, 75_LVBus1213877_production, 75_LVBus1213878_consumption, 75_LVBus1213878_production, 75_LVBus1213879_production, 75_LVBus1213880_production, 75_LVBus1213881_production, 75_LVBus1213883_production, 75_LVBus1213884_production, 75_LVBus1213885_production, 75_LVBus1213886_production, 75_LVBus1213887_production, 75_LVBus1213888_production, 75_LVBus1213889_production, 75_LVBus1213890_production, 75_LVBus1213891_production, 75_LVBus1213892_production, 75_LVBus1213893_production, 75_LVBus1213894_production, 75_LVBus1213895_production, 75_LVBus1213896_production, 75_LVBus1213897_consumption, 75_LVBus1213897_production, 75_LVBus1213898_production, 75_LVBus1213899_production, 75_LVBus1213900_production, 75_LVBus1213901_production, 75_LVBus1213905_consumption, 75_LVBus1213905_production, 75_LVBus1213906_consumption, 75_LVBus1213906_production, 75_LVBus1213907_production, 75_LVBus1213908_production, 75_LVBus1213912_consumption, 75_LVBus1213912_production, 75_LVBus1213913_production, 75_LVBus1213914_production, 75_LVBus1213915_consumption, 75_LVBus1213915_production, 75_LVBus1213916_production, 75_LVBus1213920_consumption, 75_LVBus1213920_production, 75_LVBus1213921_production, 75_LVBus1213922_production, 75_LVBus1213923_production, 75_LVBus1213924_consumption, 75_LVBus1213924_production, 75_LVBus1213925_production, 75_LVBus1213926_consumption, 75_LVBus1213926_production, 75_LVBus1213928_consumption, 75_LVBus1213928_production, 75_LVBus1213929_production, 75_LVBus1213930_production, 75_LVBus1213931_consumption, 75_LVBus1213931_production, 75_LVBus1213932_consumption, 75_LVBus1213932_production, 75_LVBus1213933_consumption, 75_LVBus1213933_production, 75_LVBus1213934_consumption, 75_LVBus1213934_production, 75_LVBus1213935_production, 75_LVBus1213936_production, 75_LVBus1213937_production, 75_LVBus1213939_consumption, 75_LVBus1213939_production, 75_LVBus1213940_production, 75_LVBus1213941_production, 75_LVBus1213943_production, 75_LVBus1213944_consumption, 75_LVBus1213944_production, 75_LVBus1213945_production, 75_LVBus1213946_consumption, 75_LVBus1213946_production, 75_LVBus1213947_consumption, 75_LVBus1213947_production, 75_LVBus1213948_production, 75_LVBus1213950_production, 75_LVBus1213952_production, 75_LVBus1213954_consumption, 75_LVBus1213954_production, 75_LVBus1213955_production, 75_LVBus1213956_production, 75_LVBus1213957_production, 75_LVBus1213961_consumption, 75_LVBus1213961_production, 75_LVBus1213962_consumption, 75_LVBus1213962_production, 75_LVBus1213963_consumption, 75_LVBus1213963_production, 75_LVBus1213964_consumption, 75_LVBus1213964_production, 75_LVBus1213965_production, 75_LVBus1213967_consumption, 75_LVBus1213967_production, 75_LVBus1213968_production, 75_LVBus1213969_production, 75_LVBus1213970_production, 75_LVBus1213971_production, 75_LVBus1213972_production, 75_LVBus1213976_production, 75_LVBus1213977_production, 75_LVBus1213978_production, 75_LVBus1213980_production, 75_LVBus1213981_production, 75_LVBus1213982_consumption, 75_LVBus1213982_production, 75_LVBus1213983_production, 75_LVBus1213984_production, 75_LVBus1213985_production, 75_LVBus1213986_production, 75_LVBus1213990_consumption, 75_LVBus1213990_production, 75_LVBus1213991_consumption, 75_LVBus1213991_production, 75_LVBus1213992_production, 75_LVBus1213993_production, 75_LVBus1213994_production, 75_LVBus1213998_production, 75_LVBus1213999_production, 75_LVBus1214000_production, 75_LVBus1214001_production, 75_LVBus1214002_production, 75_LVBus1214003_production, 75_LVBus1214004_production, 75_LVBus1214006_production, 75_LVBus1214007_consumption, 75_LVBus1214007_production, 75_LVBus1214009_production, 75_LVBus1214010_production, 75_LVBus1214011_production, 75_LVBus1214012_production, 75_LVBus1214013_production, 75_LVBus1214015_production, 75_LVBus1214016_production, 75_LVBus1214017_production, 75_LVBus1214018_consumption, 75_LVBus1214018_production, 75_LVBus1214019_consumption, 75_LVBus1214019_production, 75_LVBus1214022_consumption, 75_LVBus1214022_production, 75_LVBus1214023_consumption, 75_LVBus1214023_production, 75_LVBus1214024_production, 75_LVBus1214025_production, 75_LVBus1214027_consumption, 75_LVBus1214027_production, 75_LVBus1214028_production, 75_LVBus1214029_consumption, 75_LVBus1214029_production, 75_LVBus1214030_production, 75_LVBus1214034_production, 75_LVBus1214036_production, 75_LVBus1214037_consumption, 75_LVBus1214037_production, 75_LVBus1214038_production, 75_LVBus1214039_production, 75_LVBus1214040_production, 75_LVBus1214041_production, 75_LVBus1214043_consumption, 75_LVBus1214043_production, 75_LVBus1214044_consumption, 75_LVBus1214044_production, 75_LVBus1214045_consumption, 75_LVBus1214045_production, 75_LVBus1214046_consumption, 75_LVBus1214046_production, 75_LVBus1214047_production, 75_LVBus1214048_production, 75_LVBus1214049_consumption, 75_LVBus1214049_production, 75_LVBus1214050_consumption, 75_LVBus1214050_production, 75_LVBus1214051_production, 75_LVBus1214052_production, 75_LVBus1214054_production, 75_LVBus1214055_production, 75_LVBus1214056_consumption, 75_LVBus1214056_production, 75_LVBus1214058_production, 75_LVBus1214059_production, 75_LVBus1214060_production, 75_LVBus1214061_production, 75_LVBus1214062_production, 75_LVBus1214063_production, 75_LVBus1214064_production, 75_LVBus1214065_consumption, 75_LVBus1214065_production, 75_LVBus1214066_production, 75_LVBus1214067_production, 75_LVBus1214068_production, 75_LVBus1214069_production, 75_LVBus1214070_production, 75_LVBus1214071_production, 75_LVBus1214075_production, 75_LVBus1214076_production, 75_LVBus1214078_consumption, 75_LVBus1214078_production, 75_LVBus1214079_production, 75_LVBus1214081_production, 75_LVBus1214082_production, 75_LVBus1214083_production, 75_LVBus1214084_consumption, 75_LVBus1214084_production, 75_LVBus1214085_production, 75_LVBus1214086_production, 75_LVBus1214088_consumption, 75_LVBus1214088_production, 75_LVBus1214090_production, 75_LVBus1214091_production, 75_LVBus1214092_production, 75_LVBus1214093_production, 75_LVBus1214094_consumption, 75_LVBus1214094_production, 75_LVBus1214095_production, 75_LVBus1214097_consumption, 75_LVBus1214097_production, 75_LVBus1214098_consumption, 75_LVBus1214098_production, 75_LVBus1214099_production, 75_LVBus1214100_production, 75_LVBus1214101_production, 75_LVBus1214102_production, 75_LVBus1214103_production, 75_LVBus1214104_consumption, 75_LVBus1214104_production, 75_LVBus1214105_production, 75_LVBus1214106_production, 75_LVBus1214107_production, 75_LVBus1214108_consumption, 75_LVBus1214108_production, 75_LVBus1214110_consumption, 75_LVBus1214110_production, 75_LVBus1214111_production, 75_LVBus1214112_production, 75_LVBus1214113_production, 75_LVBus1214114_consumption, 75_LVBus1214114_production, 75_LVBus1214116_production, 75_LVBus1214117_production, 75_LVBus1214118_production, 75_LVBus1214119_production, 75_LVBus1214123_production, 75_LVBus1214125_production, 75_LVBus1214126_production, 75_LVBus1214127_production, 75_LVBus1214128_production, 75_LVBus1214129_production, 75_LVBus1214131_consumption, 75_LVBus1214131_production, 75_LVBus1214133_production, 75_LVBus1214134_consumption, 75_LVBus1214134_production, 75_LVBus1214135_production, 75_LVBus1214136_production, 75_LVBus1214137_production, 75_LVBus1214138_production, 75_LVBus1214139_production, 75_LVBus1214140_production, 75_LVBus1214144_production, 75_LVBus1214145_consumption, 75_LVBus1214145_production, 75_LVBus1214146_consumption, 75_LVBus1214146_production, 75_LVBus1214147_production, 75_LVBus1214148_production, 75_LVBus1214149_production, 75_LVBus1214150_production, 75_LVBus1214151_consumption, 75_LVBus1214151_production, 75_LVBus1214152_production, 75_LVBus1214153_production, 75_LVBus1214155_consumption, 75_LVBus1214155_production, 75_LVBus1214156_consumption, 75_LVBus1214156_production, 75_LVBus1214157_consumption, 75_LVBus1214157_production, 75_LVBus1214158_production, 75_LVBus1214159_production, 75_LVBus1926269_consumption, 75_LVBus1926269_production, 75_LVBus1929142_production, 75_LVBus1929143_production, 75_LVBus1929144_production, 75_LVBus1929145_production, 75_LVBus1929146_production, 75_LVBus1929749_production, 75_LVBus1945184_production, 75_LVBus1974649_production, 75_MVLV064430_consumption, 75_MVLV064430_production, 75_MVLV087795_consumption, 75_MVLV087795_production.

