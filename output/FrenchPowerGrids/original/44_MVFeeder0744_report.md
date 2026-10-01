# BMOPF Network Summary: 44_MVFeeder0744

**Generated:** 2026-10-01 23:34:10  
**Findings:** 0 errors · 5 warnings · 278 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 37 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 507 |  |
| line | 469 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 776 | 1.496 MW, 448.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 37 |  |
| switch | 0 |  |
| transformer | 37 | Dyn11×37 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 84 | 83 | 4 | 0 |
| LV_236V | 236.0 V | 423 | 386 | 772 | 0 |

**Transformer transitions:**

- `44_MVLV48457_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV32032_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV05591_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV10467_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV29202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV57819_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV28700_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV38469_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV23999_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV13223_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV62227_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV39946_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV28456_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV46427_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV02277_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV25611_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV51713_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV46990_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV10466_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV07838_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV54055_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV05960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV25135_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV26255_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV08234_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV24873_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV62192_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV34629_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV57011_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV54419_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV10465_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV33189_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV57007_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV40595_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV04209_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV05475_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV65932_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 142 |
| Tree depth (max hops) | 39 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 507 | 1 | 506 | 0 | 0 | 0 |
| Tier LV_236V | 423 | 37 | 386 | 0 | 0 | 0 |
| Tier MV_11.8kV | 84 | 1 | 83 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 37; skipped invalid branches: 0.

Galvanic zones: 38; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 44_ETAI5 | MV_11.8kV | 84 | 0 | 0 | 37 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1944 declared bus terminals; 1793 mapped line/closed-switch conductor edges; 151 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 19600.0 | 2.89 | 2328 |
| q_nom | 0.0 | 5870.0 | 2.89 | 2328 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.846 | 2870.0 | 1.904 | 469 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.452 | 37 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 497 of 776 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604968_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus872885_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604986_consumption' has phase imbalance of 247.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605302_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605201_consumption' has phase imbalance of 69.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605162_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604978_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus885255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus885253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605215_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605052_consumption' has phase imbalance of 287.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605163_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864504_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864515_consumption' has phase imbalance of 212.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605181_consumption' has phase imbalance of 146.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605105_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus872895_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus873680_consumption' has phase imbalance of 226.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605058_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605260_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605161_consumption' has phase imbalance of 283.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858925_consumption' has phase imbalance of 276.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus877919_consumption' has phase imbalance of 236.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605088_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus872887_consumption' has phase imbalance of 273.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858921_consumption' has phase imbalance of 259.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605254_consumption' has phase imbalance of 158.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604984_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605115_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604938_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605233_consumption' has phase imbalance of 273.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605241_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605211_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864502_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604954_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus872886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus873681_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus856670_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus856493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605210_consumption' has phase imbalance of 283.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604967_consumption' has phase imbalance of 122.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858924_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus872884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605126_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605319_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605089_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605117_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605111_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605158_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605168_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605037_consumption' has phase imbalance of 89.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864509_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604964_consumption' has phase imbalance of 258.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605226_consumption' has phase imbalance of 228.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605235_consumption' has phase imbalance of 200.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605174_consumption' has phase imbalance of 248.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605012_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605323_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605263_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604991_consumption' has phase imbalance of 138.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864506_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605299_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605148_consumption' has phase imbalance of 269.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604959_consumption' has phase imbalance of 118.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605093_consumption' has phase imbalance of 221.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605269_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604941_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605200_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605271_consumption' has phase imbalance of 234.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605147_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605183_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605175_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus872888_consumption' has phase imbalance of 186.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605283_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605112_consumption' has phase imbalance of 91.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605307_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605185_consumption' has phase imbalance of 236.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605038_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605091_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605056_consumption' has phase imbalance of 25.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605326_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605076_consumption' has phase imbalance of 59.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604987_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604974_consumption' has phase imbalance of 96.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605267_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605006_consumption' has phase imbalance of 173.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605004_consumption' has phase imbalance of 264.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605142_consumption' has phase imbalance of 252.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605300_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605261_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605083_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus858923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605153_consumption' has phase imbalance of 32.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605303_consumption' has phase imbalance of 155.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605119_consumption' has phase imbalance of 193.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus877917_consumption' has phase imbalance of 237.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605159_consumption' has phase imbalance of 241.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604957_consumption' has phase imbalance of 95.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604955_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605036_consumption' has phase imbalance of 234.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605266_consumption' has phase imbalance of 271.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605008_consumption' has phase imbalance of 21.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604960_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605049_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605129_consumption' has phase imbalance of 67.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605306_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605080_consumption' has phase imbalance of 146.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605054_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605171_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605121_consumption' has phase imbalance of 258.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605001_consumption' has phase imbalance of 85.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605139_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604982_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605048_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605173_consumption' has phase imbalance of 45.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605002_consumption' has phase imbalance of 213.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605144_consumption' has phase imbalance of 281.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605202_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605120_consumption' has phase imbalance of 249.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus856669_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604981_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605150_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605317_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus885254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604973_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604958_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604947_consumption' has phase imbalance of 87.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605230_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus856494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus877916_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604946_consumption' has phase imbalance of 22.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604940_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605104_consumption' has phase imbalance of 215.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus885252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605212_consumption' has phase imbalance of 248.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605053_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605143_consumption' has phase imbalance of 96.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus885250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605070_consumption' has phase imbalance of 221.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605176_consumption' has phase imbalance of 75.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605262_consumption' has phase imbalance of 186.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605057_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605265_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604969_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604965_consumption' has phase imbalance of 98.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604953_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605059_consumption' has phase imbalance of 89.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605079_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus877920_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605214_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605029_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605208_consumption' has phase imbalance of 201.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus877918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604970_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604966_consumption' has phase imbalance of 243.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605321_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605231_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605206_consumption' has phase imbalance of 69.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605281_consumption' has phase imbalance of 242.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605114_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605060_consumption' has phase imbalance of 213.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605198_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605232_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus604952_consumption' has phase imbalance of 267.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605035_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605146_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605199_consumption' has phase imbalance of 126.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864511_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus864510_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus605050_consumption' has phase imbalance of 226.7%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 776 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus605190' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus604932' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus604928' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus605315' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus605042' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.496 MW |
| Total load Q | 448.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 44_MVLV48457_Transformer | 176.0 kVA | 36.2% |
| 44_MVLV32032_Transformer | 176.0 kVA | 0.0% |
| 44_MVLV05591_Transformer | 110.0 kVA | 20.2% |
| 44_MVLV10467_Transformer | 176.0 kVA | 0.0% |
| 44_MVLV29202_Transformer | 176.0 kVA | 45.2% |
| 44_MVLV57819_Transformer | 110.0 kVA | 4.7% |
| 44_MVLV28700_Transformer | 176.0 kVA | 44.4% |
| 44_MVLV38469_Transformer | 176.0 kVA | 43.7% |
| 44_MVLV23999_Transformer | 176.0 kVA | 42.3% |
| 44_MVLV13223_Transformer | 110.0 kVA | 2.3% |
| 44_MVLV62227_Transformer | 176.0 kVA | 30.9% |
| 44_MVLV39946_Transformer | 176.0 kVA | 25.9% |
| 44_MVLV28456_Transformer | 110.0 kVA | 37.0% |
| 44_MVLV46427_Transformer | 176.0 kVA | 34.1% |
| 44_MVLV02277_Transformer | 176.0 kVA | 0.0% |
| 44_MVLV25611_Transformer | 440.0 kVA | 30.1% |
| 44_MVLV51713_Transformer | 110.0 kVA | 14.3% |
| 44_MVLV46990_Transformer | 176.0 kVA | 38.4% |
| 44_MVLV10466_Transformer | 110.0 kVA | 1.0% |
| 44_MVLV07838_Transformer | 275.0 kVA | 26.0% |
| 44_MVLV54055_Transformer | 275.0 kVA | 43.1% |
| 44_MVLV05960_Transformer | 275.0 kVA | 30.5% |
| 44_MVLV25135_Transformer | 110.0 kVA | 3.8% |
| 44_MVLV26255_Transformer | 176.0 kVA | 23.4% |
| 44_MVLV08234_Transformer | 176.0 kVA | 27.7% |
| 44_MVLV24873_Transformer | 176.0 kVA | 0.0% |
| 44_MVLV62192_Transformer | 110.0 kVA | 9.2% |
| 44_MVLV34629_Transformer | 176.0 kVA | 23.1% |
| 44_MVLV57011_Transformer | 176.0 kVA | 0.0% |
| 44_MVLV54419_Transformer | 110.0 kVA | 31.2% |
| 44_MVLV10465_Transformer | 440.0 kVA | 27.3% |
| 44_MVLV33189_Transformer | 110.0 kVA | 46.5% |
| 44_MVLV57007_Transformer | 176.0 kVA | 50.5% |
| 44_MVLV40595_Transformer | 110.0 kVA | 9.0% |
| 44_MVLV04209_Transformer | 110.0 kVA | 9.1% |
| 44_MVLV05475_Transformer | 110.0 kVA | 7.6% |
| 44_MVLV65932_Transformer | 176.0 kVA | 0.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.5 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '44_ETAI5' (MV, 11.78 kV) has an electrical reach of 23.7 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605018' (LV, 0.24 kV) has an electrical reach of 7.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605040' (LV, 0.24 kV) has an electrical reach of 11.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605131' (LV, 0.24 kV) has an electrical reach of 7.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605313' (LV, 0.24 kV) has an electrical reach of 9.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605317' (LV, 0.24 kV) has an electrical reach of 17.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605315' (LV, 0.24 kV) has an electrical reach of 3.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605042' (LV, 0.24 kV) has an electrical reach of 18.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '44_LVBus605012' (LV, 0.24 kV) has an electrical reach of 7.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 507 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 507 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 37 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 84 |
| LV_236V | 4-wire | 423 / 423 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 423 |
| Neutral branches | 386 |
| Grounding points | 37 |
| Neutral sections | 37 |
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
| 11.78 kV | 84 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 38 |
| Islands without voltage reference | 0 |
| Line impedance spread | 3350.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 423 / 84 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 498 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 498 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus604924_consumption, 44_LVBus604924_production, 44_LVBus604925_consumption, 44_LVBus604925_production, 44_LVBus604928_production, 44_LVBus604930_consumption, 44_LVBus604930_production, 44_LVBus604932_production, 44_LVBus604934_production, 44_LVBus604936_consumption, 44_LVBus604936_production, 44_LVBus604938_production, 44_LVBus604939_production, 44_LVBus604940_production, 44_LVBus604941_production, 44_LVBus604942_production, 44_LVBus604943_production, 44_LVBus604945_production, 44_LVBus604946_production, 44_LVBus604947_production, 44_LVBus604951_production, 44_LVBus604952_production, 44_LVBus604953_production, 44_LVBus604954_production, 44_LVBus604955_production, 44_LVBus604957_production, 44_LVBus604958_production, 44_LVBus604959_production, 44_LVBus604960_production, 44_LVBus604961_production, 44_LVBus604962_production, 44_LVBus604963_consumption, 44_LVBus604963_production, 44_LVBus604964_production, 44_LVBus604965_production, 44_LVBus604966_production, 44_LVBus604967_production, 44_LVBus604968_production, 44_LVBus604969_production, 44_LVBus604970_production, 44_LVBus604972_consumption, 44_LVBus604972_production, 44_LVBus604973_production, 44_LVBus604974_production, 44_LVBus604975_production, 44_LVBus604976_consumption, 44_LVBus604976_production, 44_LVBus604977_production, 44_LVBus604978_production, 44_LVBus604979_consumption, 44_LVBus604979_production, 44_LVBus604981_production, 44_LVBus604982_production, 44_LVBus604983_production, 44_LVBus604984_production, 44_LVBus604985_consumption, 44_LVBus604985_production, 44_LVBus604986_production, 44_LVBus604987_production, 44_LVBus604988_production, 44_LVBus604989_production, 44_LVBus604991_production, 44_LVBus604992_production, 44_LVBus604993_production, 44_LVBus604994_production, 44_LVBus604995_production, 44_LVBus604996_consumption, 44_LVBus604996_production, 44_LVBus604997_production, 44_LVBus604998_production, 44_LVBus604999_production, 44_LVBus605000_consumption, 44_LVBus605000_production, 44_LVBus605001_production, 44_LVBus605002_production, 44_LVBus605003_consumption, 44_LVBus605003_production, 44_LVBus605004_production, 44_LVBus605006_production, 44_LVBus605008_production, 44_LVBus605010_production, 44_LVBus605012_production, 44_LVBus605014_consumption, 44_LVBus605014_production, 44_LVBus605016_consumption, 44_LVBus605016_production, 44_LVBus605018_production, 44_LVBus605020_consumption, 44_LVBus605020_production, 44_LVBus605021_consumption, 44_LVBus605021_production, 44_LVBus605022_consumption, 44_LVBus605022_production, 44_LVBus605023_consumption, 44_LVBus605023_production, 44_LVBus605024_production, 44_LVBus605025_consumption, 44_LVBus605025_production, 44_LVBus605026_production, 44_LVBus605027_consumption, 44_LVBus605027_production, 44_LVBus605028_production, 44_LVBus605029_production, 44_LVBus605030_production, 44_LVBus605031_consumption, 44_LVBus605031_production, 44_LVBus605032_consumption, 44_LVBus605032_production, 44_LVBus605033_production, 44_LVBus605034_production, 44_LVBus605035_production, 44_LVBus605036_production, 44_LVBus605037_production, 44_LVBus605038_production, 44_LVBus605040_consumption, 44_LVBus605040_production, 44_LVBus605042_production, 44_LVBus605044_consumption, 44_LVBus605044_production, 44_LVBus605046_consumption, 44_LVBus605046_production, 44_LVBus605048_production, 44_LVBus605049_production, 44_LVBus605050_production, 44_LVBus605052_production, 44_LVBus605053_production, 44_LVBus605054_production, 44_LVBus605056_production, 44_LVBus605057_production, 44_LVBus605058_production, 44_LVBus605059_production, 44_LVBus605060_production, 44_LVBus605061_consumption, 44_LVBus605061_production, 44_LVBus605062_consumption, 44_LVBus605062_production, 44_LVBus605063_production, 44_LVBus605064_consumption, 44_LVBus605064_production, 44_LVBus605065_consumption, 44_LVBus605065_production, 44_LVBus605067_consumption, 44_LVBus605067_production, 44_LVBus605069_consumption, 44_LVBus605069_production, 44_LVBus605070_production, 44_LVBus605071_production, 44_LVBus605072_production, 44_LVBus605074_production, 44_LVBus605075_production, 44_LVBus605076_production, 44_LVBus605077_production, 44_LVBus605078_production, 44_LVBus605079_production, 44_LVBus605080_production, 44_LVBus605082_consumption, 44_LVBus605082_production, 44_LVBus605083_production, 44_LVBus605084_consumption, 44_LVBus605084_production, 44_LVBus605085_consumption, 44_LVBus605085_production, 44_LVBus605087_consumption, 44_LVBus605087_production, 44_LVBus605088_production, 44_LVBus605089_production, 44_LVBus605090_production, 44_LVBus605091_production, 44_LVBus605092_production, 44_LVBus605093_production, 44_LVBus605094_production, 44_LVBus605095_production, 44_LVBus605096_consumption, 44_LVBus605096_production, 44_LVBus605101_production, 44_LVBus605102_production, 44_LVBus605103_production, 44_LVBus605104_production, 44_LVBus605105_production, 44_LVBus605106_production, 44_LVBus605107_production, 44_LVBus605108_consumption, 44_LVBus605108_production, 44_LVBus605109_production, 44_LVBus605110_consumption, 44_LVBus605110_production, 44_LVBus605111_production, 44_LVBus605112_production, 44_LVBus605113_production, 44_LVBus605114_production, 44_LVBus605115_production, 44_LVBus605116_consumption, 44_LVBus605116_production, 44_LVBus605117_production, 44_LVBus605119_production, 44_LVBus605120_production, 44_LVBus605121_production, 44_LVBus605122_consumption, 44_LVBus605122_production, 44_LVBus605123_consumption, 44_LVBus605123_production, 44_LVBus605124_consumption, 44_LVBus605124_production, 44_LVBus605125_consumption, 44_LVBus605125_production, 44_LVBus605126_production, 44_LVBus605127_production, 44_LVBus605128_production, 44_LVBus605129_production, 44_LVBus605131_consumption, 44_LVBus605131_production, 44_LVBus605133_consumption, 44_LVBus605133_production, 44_LVBus605135_consumption, 44_LVBus605135_production, 44_LVBus605136_production, 44_LVBus605137_consumption, 44_LVBus605137_production, 44_LVBus605138_production, 44_LVBus605139_production, 44_LVBus605141_production, 44_LVBus605142_production, 44_LVBus605143_production, 44_LVBus605144_production, 44_LVBus605146_production, 44_LVBus605147_production, 44_LVBus605148_production, 44_LVBus605149_consumption, 44_LVBus605149_production, 44_LVBus605150_production, 44_LVBus605152_consumption, 44_LVBus605152_production, 44_LVBus605153_production, 44_LVBus605154_consumption, 44_LVBus605154_production, 44_LVBus605156_consumption, 44_LVBus605156_production, 44_LVBus605157_consumption, 44_LVBus605157_production, 44_LVBus605158_production, 44_LVBus605159_production, 44_LVBus605160_consumption, 44_LVBus605160_production, 44_LVBus605161_production, 44_LVBus605162_production, 44_LVBus605163_production, 44_LVBus605164_production, 44_LVBus605165_consumption, 44_LVBus605165_production, 44_LVBus605166_consumption, 44_LVBus605166_production, 44_LVBus605167_consumption, 44_LVBus605167_production, 44_LVBus605168_production, 44_LVBus605169_consumption, 44_LVBus605169_production, 44_LVBus605170_consumption, 44_LVBus605170_production, 44_LVBus605171_production, 44_LVBus605173_production, 44_LVBus605174_production, 44_LVBus605175_production, 44_LVBus605176_production, 44_LVBus605177_production, 44_LVBus605178_consumption, 44_LVBus605178_production, 44_LVBus605179_consumption, 44_LVBus605179_production, 44_LVBus605180_production, 44_LVBus605181_production, 44_LVBus605182_production, 44_LVBus605183_production, 44_LVBus605184_production, 44_LVBus605185_production, 44_LVBus605186_production, 44_LVBus605187_production, 44_LVBus605190_production, 44_LVBus605194_production, 44_LVBus605196_production, 44_LVBus605198_production, 44_LVBus605199_production, 44_LVBus605200_production, 44_LVBus605201_production, 44_LVBus605202_production, 44_LVBus605203_production, 44_LVBus605204_production, 44_LVBus605206_production, 44_LVBus605208_production, 44_LVBus605209_consumption, 44_LVBus605209_production, 44_LVBus605210_production, 44_LVBus605211_production, 44_LVBus605212_production, 44_LVBus605214_production, 44_LVBus605215_production, 44_LVBus605216_consumption, 44_LVBus605216_production, 44_LVBus605217_consumption, 44_LVBus605217_production, 44_LVBus605218_consumption, 44_LVBus605218_production, 44_LVBus605219_consumption, 44_LVBus605219_production, 44_LVBus605220_consumption, 44_LVBus605220_production, 44_LVBus605221_consumption, 44_LVBus605221_production, 44_LVBus605222_production, 44_LVBus605223_consumption, 44_LVBus605223_production, 44_LVBus605224_production, 44_LVBus605225_consumption, 44_LVBus605225_production, 44_LVBus605226_production, 44_LVBus605228_production, 44_LVBus605229_production, 44_LVBus605230_production, 44_LVBus605231_production, 44_LVBus605232_production, 44_LVBus605233_production, 44_LVBus605234_production, 44_LVBus605235_production, 44_LVBus605237_consumption, 44_LVBus605237_production, 44_LVBus605238_consumption, 44_LVBus605238_production, 44_LVBus605239_production, 44_LVBus605240_consumption, 44_LVBus605240_production, 44_LVBus605241_production, 44_LVBus605248_consumption, 44_LVBus605248_production, 44_LVBus605249_consumption, 44_LVBus605249_production, 44_LVBus605251_consumption, 44_LVBus605251_production, 44_LVBus605252_consumption, 44_LVBus605252_production, 44_LVBus605253_consumption, 44_LVBus605253_production, 44_LVBus605254_production, 44_LVBus605255_consumption, 44_LVBus605255_production, 44_LVBus605256_consumption, 44_LVBus605256_production, 44_LVBus605257_consumption, 44_LVBus605257_production, 44_LVBus605258_production, 44_LVBus605260_production, 44_LVBus605261_production, 44_LVBus605262_production, 44_LVBus605263_production, 44_LVBus605264_consumption, 44_LVBus605264_production, 44_LVBus605265_production, 44_LVBus605266_production, 44_LVBus605267_production, 44_LVBus605269_production, 44_LVBus605270_production, 44_LVBus605271_production, 44_LVBus605272_production, 44_LVBus605273_production, 44_LVBus605275_consumption, 44_LVBus605275_production, 44_LVBus605276_consumption, 44_LVBus605276_production, 44_LVBus605277_consumption, 44_LVBus605277_production, 44_LVBus605279_consumption, 44_LVBus605279_production, 44_LVBus605280_consumption, 44_LVBus605280_production, 44_LVBus605281_production, 44_LVBus605282_consumption, 44_LVBus605282_production, 44_LVBus605283_production, 44_LVBus605284_production, 44_LVBus605285_production, 44_LVBus605286_consumption, 44_LVBus605286_production, 44_LVBus605287_production, 44_LVBus605288_consumption, 44_LVBus605288_production, 44_LVBus605289_production, 44_LVBus605291_consumption, 44_LVBus605291_production, 44_LVBus605292_production, 44_LVBus605293_production, 44_LVBus605294_production, 44_LVBus605298_production, 44_LVBus605299_production, 44_LVBus605300_production, 44_LVBus605301_consumption, 44_LVBus605301_production, 44_LVBus605302_production, 44_LVBus605303_production, 44_LVBus605304_production, 44_LVBus605306_production, 44_LVBus605307_production, 44_LVBus605308_production, 44_LVBus605313_consumption, 44_LVBus605313_production, 44_LVBus605315_production, 44_LVBus605317_production, 44_LVBus605319_production, 44_LVBus605320_consumption, 44_LVBus605320_production, 44_LVBus605321_production, 44_LVBus605322_consumption, 44_LVBus605322_production, 44_LVBus605323_production, 44_LVBus605324_production, 44_LVBus605326_production, 44_LVBus605327_production, 44_LVBus605331_consumption, 44_LVBus605331_production, 44_LVBus851399_production, 44_LVBus851536_production, 44_LVBus853305_consumption, 44_LVBus853305_production, 44_LVBus856368_consumption, 44_LVBus856368_production, 44_LVBus856493_production, 44_LVBus856494_production, 44_LVBus856523_consumption, 44_LVBus856523_production, 44_LVBus856669_production, 44_LVBus856670_production, 44_LVBus858829_consumption, 44_LVBus858829_production, 44_LVBus858920_production, 44_LVBus858921_production, 44_LVBus858922_consumption, 44_LVBus858922_production, 44_LVBus858923_production, 44_LVBus858924_production, 44_LVBus858925_production, 44_LVBus858926_production, 44_LVBus864500_consumption, 44_LVBus864500_production, 44_LVBus864501_consumption, 44_LVBus864501_production, 44_LVBus864502_production, 44_LVBus864503_production, 44_LVBus864504_production, 44_LVBus864505_production, 44_LVBus864506_production, 44_LVBus864507_production, 44_LVBus864508_production, 44_LVBus864509_production, 44_LVBus864510_production, 44_LVBus864511_production, 44_LVBus864512_production, 44_LVBus864513_production, 44_LVBus864514_production, 44_LVBus864515_production, 44_LVBus864516_production, 44_LVBus864517_production, 44_LVBus864518_production, 44_LVBus870163_consumption, 44_LVBus870163_production, 44_LVBus872884_production, 44_LVBus872885_production, 44_LVBus872886_production, 44_LVBus872887_production, 44_LVBus872888_production, 44_LVBus872889_consumption, 44_LVBus872889_production, 44_LVBus872890_production, 44_LVBus872891_production, 44_LVBus872892_production, 44_LVBus872893_consumption, 44_LVBus872893_production, 44_LVBus872894_production, 44_LVBus872895_production, 44_LVBus873680_production, 44_LVBus873681_production, 44_LVBus877916_production, 44_LVBus877917_production, 44_LVBus877918_production, 44_LVBus877919_production, 44_LVBus877920_production, 44_LVBus877921_production, 44_LVBus885249_consumption, 44_LVBus885249_production, 44_LVBus885250_production, 44_LVBus885251_consumption, 44_LVBus885251_production, 44_LVBus885252_production, 44_LVBus885253_production, 44_LVBus885254_production, 44_LVBus885255_production, 44_LVBus885256_consumption, 44_LVBus885256_production, 44_MVLV33011_consumption, 44_MVLV33011_production, 44_MVLV50806_consumption, 44_MVLV50806_production.

## 9. Data Quality Summary

**Total findings:** 283 (0 errors, 5 warnings, 278 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  497 of 776 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.5 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  498 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604968_consumption`  
  Load '44_LVBus604968_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus872885_consumption`  
  Load '44_LVBus872885_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604986_consumption`  
  Load '44_LVBus604986_consumption' has phase imbalance of 247.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605302_consumption`  
  Load '44_LVBus605302_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605201_consumption`  
  Load '44_LVBus605201_consumption' has phase imbalance of 69.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605026_consumption`  
  Load '44_LVBus605026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605102_consumption`  
  Load '44_LVBus605102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605162_consumption`  
  Load '44_LVBus605162_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605136_consumption`  
  Load '44_LVBus605136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604978_consumption`  
  Load '44_LVBus604978_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus885255_consumption`  
  Load '44_LVBus885255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus885253_consumption`  
  Load '44_LVBus885253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605215_consumption`  
  Load '44_LVBus605215_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605052_consumption`  
  Load '44_LVBus605052_consumption' has phase imbalance of 287.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858920_consumption`  
  Load '44_LVBus858920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864505_consumption`  
  Load '44_LVBus864505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605287_consumption`  
  Load '44_LVBus605287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605163_consumption`  
  Load '44_LVBus605163_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864504_consumption`  
  Load '44_LVBus864504_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864515_consumption`  
  Load '44_LVBus864515_consumption' has phase imbalance of 212.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605181_consumption`  
  Load '44_LVBus605181_consumption' has phase imbalance of 146.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605105_consumption`  
  Load '44_LVBus605105_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus872895_consumption`  
  Load '44_LVBus872895_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus873680_consumption`  
  Load '44_LVBus873680_consumption' has phase imbalance of 226.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605058_consumption`  
  Load '44_LVBus605058_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605260_consumption`  
  Load '44_LVBus605260_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605161_consumption`  
  Load '44_LVBus605161_consumption' has phase imbalance of 283.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605092_consumption`  
  Load '44_LVBus605092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605063_consumption`  
  Load '44_LVBus605063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605186_consumption`  
  Load '44_LVBus605186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605184_consumption`  
  Load '44_LVBus605184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858925_consumption`  
  Load '44_LVBus858925_consumption' has phase imbalance of 276.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus877919_consumption`  
  Load '44_LVBus877919_consumption' has phase imbalance of 236.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605088_consumption`  
  Load '44_LVBus605088_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605138_consumption`  
  Load '44_LVBus605138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus872887_consumption`  
  Load '44_LVBus872887_consumption' has phase imbalance of 273.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858921_consumption`  
  Load '44_LVBus858921_consumption' has phase imbalance of 259.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605254_consumption`  
  Load '44_LVBus605254_consumption' has phase imbalance of 158.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604984_consumption`  
  Load '44_LVBus604984_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605115_consumption`  
  Load '44_LVBus605115_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604938_consumption`  
  Load '44_LVBus604938_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605233_consumption`  
  Load '44_LVBus605233_consumption' has phase imbalance of 273.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605241_consumption`  
  Load '44_LVBus605241_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864503_consumption`  
  Load '44_LVBus864503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605211_consumption`  
  Load '44_LVBus605211_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864502_consumption`  
  Load '44_LVBus864502_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604954_consumption`  
  Load '44_LVBus604954_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus872886_consumption`  
  Load '44_LVBus872886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus873681_consumption`  
  Load '44_LVBus873681_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604975_consumption`  
  Load '44_LVBus604975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus856670_consumption`  
  Load '44_LVBus856670_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus856493_consumption`  
  Load '44_LVBus856493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604999_consumption`  
  Load '44_LVBus604999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605210_consumption`  
  Load '44_LVBus605210_consumption' has phase imbalance of 283.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605109_consumption`  
  Load '44_LVBus605109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604967_consumption`  
  Load '44_LVBus604967_consumption' has phase imbalance of 122.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858924_consumption`  
  Load '44_LVBus858924_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus872884_consumption`  
  Load '44_LVBus872884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605126_consumption`  
  Load '44_LVBus605126_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605319_consumption`  
  Load '44_LVBus605319_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605222_consumption`  
  Load '44_LVBus605222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605089_consumption`  
  Load '44_LVBus605089_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605117_consumption`  
  Load '44_LVBus605117_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605111_consumption`  
  Load '44_LVBus605111_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605158_consumption`  
  Load '44_LVBus605158_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605168_consumption`  
  Load '44_LVBus605168_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605128_consumption`  
  Load '44_LVBus605128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605037_consumption`  
  Load '44_LVBus605037_consumption' has phase imbalance of 89.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864509_consumption`  
  Load '44_LVBus864509_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604962_consumption`  
  Load '44_LVBus604962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604964_consumption`  
  Load '44_LVBus604964_consumption' has phase imbalance of 258.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605226_consumption`  
  Load '44_LVBus605226_consumption' has phase imbalance of 228.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605235_consumption`  
  Load '44_LVBus605235_consumption' has phase imbalance of 200.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605174_consumption`  
  Load '44_LVBus605174_consumption' has phase imbalance of 248.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864516_consumption`  
  Load '44_LVBus864516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605012_consumption`  
  Load '44_LVBus605012_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605101_consumption`  
  Load '44_LVBus605101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605239_consumption`  
  Load '44_LVBus605239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605323_consumption`  
  Load '44_LVBus605323_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605284_consumption`  
  Load '44_LVBus605284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605094_consumption`  
  Load '44_LVBus605094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858926_consumption`  
  Load '44_LVBus858926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605327_consumption`  
  Load '44_LVBus605327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605263_consumption`  
  Load '44_LVBus605263_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604991_consumption`  
  Load '44_LVBus604991_consumption' has phase imbalance of 138.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864506_consumption`  
  Load '44_LVBus864506_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605299_consumption`  
  Load '44_LVBus605299_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605148_consumption`  
  Load '44_LVBus605148_consumption' has phase imbalance of 269.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604959_consumption`  
  Load '44_LVBus604959_consumption' has phase imbalance of 118.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605093_consumption`  
  Load '44_LVBus605093_consumption' has phase imbalance of 221.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605203_consumption`  
  Load '44_LVBus605203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605010_consumption`  
  Load '44_LVBus605010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605293_consumption`  
  Load '44_LVBus605293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605269_consumption`  
  Load '44_LVBus605269_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604941_consumption`  
  Load '44_LVBus604941_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605071_consumption`  
  Load '44_LVBus605071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605204_consumption`  
  Load '44_LVBus605204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605200_consumption`  
  Load '44_LVBus605200_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604951_consumption`  
  Load '44_LVBus604951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605271_consumption`  
  Load '44_LVBus605271_consumption' has phase imbalance of 234.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605147_consumption`  
  Load '44_LVBus605147_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605183_consumption`  
  Load '44_LVBus605183_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605175_consumption`  
  Load '44_LVBus605175_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus872888_consumption`  
  Load '44_LVBus872888_consumption' has phase imbalance of 186.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604939_consumption`  
  Load '44_LVBus604939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605283_consumption`  
  Load '44_LVBus605283_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605028_consumption`  
  Load '44_LVBus605028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864513_consumption`  
  Load '44_LVBus864513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605112_consumption`  
  Load '44_LVBus605112_consumption' has phase imbalance of 91.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605307_consumption`  
  Load '44_LVBus605307_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605185_consumption`  
  Load '44_LVBus605185_consumption' has phase imbalance of 236.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605113_consumption`  
  Load '44_LVBus605113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605038_consumption`  
  Load '44_LVBus605038_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604998_consumption`  
  Load '44_LVBus604998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605091_consumption`  
  Load '44_LVBus605091_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605056_consumption`  
  Load '44_LVBus605056_consumption' has phase imbalance of 25.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605326_consumption`  
  Load '44_LVBus605326_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605076_consumption`  
  Load '44_LVBus605076_consumption' has phase imbalance of 59.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604987_consumption`  
  Load '44_LVBus604987_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604974_consumption`  
  Load '44_LVBus604974_consumption' has phase imbalance of 96.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605267_consumption`  
  Load '44_LVBus605267_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605006_consumption`  
  Load '44_LVBus605006_consumption' has phase imbalance of 173.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605177_consumption`  
  Load '44_LVBus605177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605004_consumption`  
  Load '44_LVBus605004_consumption' has phase imbalance of 264.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605224_consumption`  
  Load '44_LVBus605224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605182_consumption`  
  Load '44_LVBus605182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604989_consumption`  
  Load '44_LVBus604989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605142_consumption`  
  Load '44_LVBus605142_consumption' has phase imbalance of 252.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605300_consumption`  
  Load '44_LVBus605300_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605261_consumption`  
  Load '44_LVBus605261_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605083_consumption`  
  Load '44_LVBus605083_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864517_consumption`  
  Load '44_LVBus864517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus858923_consumption`  
  Load '44_LVBus858923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605141_consumption`  
  Load '44_LVBus605141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605153_consumption`  
  Load '44_LVBus605153_consumption' has phase imbalance of 32.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605303_consumption`  
  Load '44_LVBus605303_consumption' has phase imbalance of 155.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605228_consumption`  
  Load '44_LVBus605228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605298_consumption`  
  Load '44_LVBus605298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605119_consumption`  
  Load '44_LVBus605119_consumption' has phase imbalance of 193.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864512_consumption`  
  Load '44_LVBus864512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604983_consumption`  
  Load '44_LVBus604983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus877917_consumption`  
  Load '44_LVBus877917_consumption' has phase imbalance of 237.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605164_consumption`  
  Load '44_LVBus605164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605159_consumption`  
  Load '44_LVBus605159_consumption' has phase imbalance of 241.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604957_consumption`  
  Load '44_LVBus604957_consumption' has phase imbalance of 95.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604955_consumption`  
  Load '44_LVBus604955_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605036_consumption`  
  Load '44_LVBus605036_consumption' has phase imbalance of 234.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605266_consumption`  
  Load '44_LVBus605266_consumption' has phase imbalance of 271.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605008_consumption`  
  Load '44_LVBus605008_consumption' has phase imbalance of 21.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605018_consumption`  
  Load '44_LVBus605018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604977_consumption`  
  Load '44_LVBus604977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604960_consumption`  
  Load '44_LVBus604960_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605285_consumption`  
  Load '44_LVBus605285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604945_consumption`  
  Load '44_LVBus604945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605049_consumption`  
  Load '44_LVBus605049_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604988_consumption`  
  Load '44_LVBus604988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605129_consumption`  
  Load '44_LVBus605129_consumption' has phase imbalance of 67.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605306_consumption`  
  Load '44_LVBus605306_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605080_consumption`  
  Load '44_LVBus605080_consumption' has phase imbalance of 146.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605054_consumption`  
  Load '44_LVBus605054_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605171_consumption`  
  Load '44_LVBus605171_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605121_consumption`  
  Load '44_LVBus605121_consumption' has phase imbalance of 258.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605001_consumption`  
  Load '44_LVBus605001_consumption' has phase imbalance of 85.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605139_consumption`  
  Load '44_LVBus605139_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604982_consumption`  
  Load '44_LVBus604982_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605292_consumption`  
  Load '44_LVBus605292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605294_consumption`  
  Load '44_LVBus605294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605072_consumption`  
  Load '44_LVBus605072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605048_consumption`  
  Load '44_LVBus605048_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605173_consumption`  
  Load '44_LVBus605173_consumption' has phase imbalance of 45.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605002_consumption`  
  Load '44_LVBus605002_consumption' has phase imbalance of 213.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605144_consumption`  
  Load '44_LVBus605144_consumption' has phase imbalance of 281.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605202_consumption`  
  Load '44_LVBus605202_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605077_consumption`  
  Load '44_LVBus605077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605270_consumption`  
  Load '44_LVBus605270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605229_consumption`  
  Load '44_LVBus605229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864514_consumption`  
  Load '44_LVBus864514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605289_consumption`  
  Load '44_LVBus605289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605120_consumption`  
  Load '44_LVBus605120_consumption' has phase imbalance of 249.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus856669_consumption`  
  Load '44_LVBus856669_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604961_consumption`  
  Load '44_LVBus604961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604981_consumption`  
  Load '44_LVBus604981_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605090_consumption`  
  Load '44_LVBus605090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605150_consumption`  
  Load '44_LVBus605150_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605317_consumption`  
  Load '44_LVBus605317_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus885254_consumption`  
  Load '44_LVBus885254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604973_consumption`  
  Load '44_LVBus604973_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604958_consumption`  
  Load '44_LVBus604958_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604947_consumption`  
  Load '44_LVBus604947_consumption' has phase imbalance of 87.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605230_consumption`  
  Load '44_LVBus605230_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus856494_consumption`  
  Load '44_LVBus856494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus877916_consumption`  
  Load '44_LVBus877916_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604946_consumption`  
  Load '44_LVBus604946_consumption' has phase imbalance of 22.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604940_consumption`  
  Load '44_LVBus604940_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605187_consumption`  
  Load '44_LVBus605187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605104_consumption`  
  Load '44_LVBus605104_consumption' has phase imbalance of 215.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus885252_consumption`  
  Load '44_LVBus885252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605103_consumption`  
  Load '44_LVBus605103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605212_consumption`  
  Load '44_LVBus605212_consumption' has phase imbalance of 248.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605106_consumption`  
  Load '44_LVBus605106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605273_consumption`  
  Load '44_LVBus605273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605258_consumption`  
  Load '44_LVBus605258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605053_consumption`  
  Load '44_LVBus605053_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605304_consumption`  
  Load '44_LVBus605304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605143_consumption`  
  Load '44_LVBus605143_consumption' has phase imbalance of 96.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605030_consumption`  
  Load '44_LVBus605030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus885250_consumption`  
  Load '44_LVBus885250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605070_consumption`  
  Load '44_LVBus605070_consumption' has phase imbalance of 221.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605107_consumption`  
  Load '44_LVBus605107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605127_consumption`  
  Load '44_LVBus605127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605176_consumption`  
  Load '44_LVBus605176_consumption' has phase imbalance of 75.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605262_consumption`  
  Load '44_LVBus605262_consumption' has phase imbalance of 186.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605057_consumption`  
  Load '44_LVBus605057_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605265_consumption`  
  Load '44_LVBus605265_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604969_consumption`  
  Load '44_LVBus604969_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604965_consumption`  
  Load '44_LVBus604965_consumption' has phase imbalance of 98.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604953_consumption`  
  Load '44_LVBus604953_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605033_consumption`  
  Load '44_LVBus605033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605234_consumption`  
  Load '44_LVBus605234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605308_consumption`  
  Load '44_LVBus605308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605059_consumption`  
  Load '44_LVBus605059_consumption' has phase imbalance of 89.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605079_consumption`  
  Load '44_LVBus605079_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605180_consumption`  
  Load '44_LVBus605180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605095_consumption`  
  Load '44_LVBus605095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus877920_consumption`  
  Load '44_LVBus877920_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605214_consumption`  
  Load '44_LVBus605214_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605029_consumption`  
  Load '44_LVBus605029_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605208_consumption`  
  Load '44_LVBus605208_consumption' has phase imbalance of 201.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus877918_consumption`  
  Load '44_LVBus877918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604970_consumption`  
  Load '44_LVBus604970_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604966_consumption`  
  Load '44_LVBus604966_consumption' has phase imbalance of 243.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605321_consumption`  
  Load '44_LVBus605321_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605231_consumption`  
  Load '44_LVBus605231_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605206_consumption`  
  Load '44_LVBus605206_consumption' has phase imbalance of 69.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864518_consumption`  
  Load '44_LVBus864518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605281_consumption`  
  Load '44_LVBus605281_consumption' has phase imbalance of 242.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605114_consumption`  
  Load '44_LVBus605114_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605060_consumption`  
  Load '44_LVBus605060_consumption' has phase imbalance of 213.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605198_consumption`  
  Load '44_LVBus605198_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605232_consumption`  
  Load '44_LVBus605232_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus604952_consumption`  
  Load '44_LVBus604952_consumption' has phase imbalance of 267.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605035_consumption`  
  Load '44_LVBus605035_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605146_consumption`  
  Load '44_LVBus605146_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605199_consumption`  
  Load '44_LVBus605199_consumption' has phase imbalance of 126.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864511_consumption`  
  Load '44_LVBus864511_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864508_consumption`  
  Load '44_LVBus864508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605272_consumption`  
  Load '44_LVBus605272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus864510_consumption`  
  Load '44_LVBus864510_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus605050_consumption`  
  Load '44_LVBus605050_consumption' has phase imbalance of 226.7%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 776 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus605190' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus604932' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus604928' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus605315' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus605042' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '44_ETAI5' (MV, 11.78 kV) has an electrical reach of 23.7 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605018' (LV, 0.24 kV) has an electrical reach of 7.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605040' (LV, 0.24 kV) has an electrical reach of 11.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605131' (LV, 0.24 kV) has an electrical reach of 7.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605313' (LV, 0.24 kV) has an electrical reach of 9.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605317' (LV, 0.24 kV) has an electrical reach of 17.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605315' (LV, 0.24 kV) has an electrical reach of 3.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605042' (LV, 0.24 kV) has an electrical reach of 18.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '44_LVBus605012' (LV, 0.24 kV) has an electrical reach of 7.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  507 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  189 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 44_LVBus604938_consumption, 44_LVBus604939_consumption, 44_LVBus604941_consumption, 44_LVBus604945_consumption, 44_LVBus604951_consumption, 44_LVBus604952_consumption, 44_LVBus604953_consumption, 44_LVBus604954_consumption, 44_LVBus604955_consumption, 44_LVBus604958_consumption, 44_LVBus604961_consumption, 44_LVBus604962_consumption, 44_LVBus604966_consumption, 44_LVBus604970_consumption, 44_LVBus604973_consumption, 44_LVBus604975_consumption, 44_LVBus604977_consumption, 44_LVBus604978_consumption, 44_LVBus604981_consumption, 44_LVBus604982_consumption, 44_LVBus604983_consumption, 44_LVBus604984_consumption, 44_LVBus604986_consumption, 44_LVBus604987_consumption, 44_LVBus604988_consumption, 44_LVBus604989_consumption, 44_LVBus604998_consumption, 44_LVBus604999_consumption, 44_LVBus605002_consumption, 44_LVBus605004_consumption, 44_LVBus605010_consumption, 44_LVBus605012_consumption, 44_LVBus605018_consumption, 44_LVBus605026_consumption, 44_LVBus605028_consumption, 44_LVBus605030_consumption, 44_LVBus605033_consumption, 44_LVBus605035_consumption, 44_LVBus605038_consumption, 44_LVBus605048_consumption, 44_LVBus605052_consumption, 44_LVBus605054_consumption, 44_LVBus605057_consumption, 44_LVBus605060_consumption, 44_LVBus605063_consumption, 44_LVBus605070_consumption, 44_LVBus605071_consumption, 44_LVBus605072_consumption, 44_LVBus605077_consumption, 44_LVBus605083_consumption, 44_LVBus605090_consumption, 44_LVBus605092_consumption, 44_LVBus605093_consumption, 44_LVBus605094_consumption, 44_LVBus605095_consumption, 44_LVBus605101_consumption, 44_LVBus605102_consumption, 44_LVBus605103_consumption, 44_LVBus605104_consumption, 44_LVBus605105_consumption, 44_LVBus605106_consumption, 44_LVBus605107_consumption, 44_LVBus605109_consumption, 44_LVBus605111_consumption, 44_LVBus605113_consumption, 44_LVBus605114_consumption, 44_LVBus605115_consumption, 44_LVBus605117_consumption, 44_LVBus605119_consumption, 44_LVBus605120_consumption, 44_LVBus605121_consumption, 44_LVBus605126_consumption, 44_LVBus605127_consumption, 44_LVBus605128_consumption, 44_LVBus605136_consumption, 44_LVBus605138_consumption, 44_LVBus605141_consumption, 44_LVBus605144_consumption, 44_LVBus605146_consumption, 44_LVBus605147_consumption, 44_LVBus605148_consumption, 44_LVBus605150_consumption, 44_LVBus605159_consumption, 44_LVBus605161_consumption, 44_LVBus605162_consumption, 44_LVBus605163_consumption, 44_LVBus605164_consumption, 44_LVBus605168_consumption, 44_LVBus605171_consumption, 44_LVBus605174_consumption, 44_LVBus605177_consumption, 44_LVBus605180_consumption, 44_LVBus605182_consumption, 44_LVBus605183_consumption, 44_LVBus605184_consumption, 44_LVBus605185_consumption, 44_LVBus605186_consumption, 44_LVBus605187_consumption, 44_LVBus605198_consumption, 44_LVBus605202_consumption, 44_LVBus605203_consumption, 44_LVBus605204_consumption, 44_LVBus605210_consumption, 44_LVBus605212_consumption, 44_LVBus605214_consumption, 44_LVBus605215_consumption, 44_LVBus605222_consumption, 44_LVBus605224_consumption, 44_LVBus605226_consumption, 44_LVBus605228_consumption, 44_LVBus605229_consumption, 44_LVBus605231_consumption, 44_LVBus605234_consumption, 44_LVBus605235_consumption, 44_LVBus605239_consumption, 44_LVBus605241_consumption, 44_LVBus605254_consumption, 44_LVBus605258_consumption, 44_LVBus605260_consumption, 44_LVBus605262_consumption, 44_LVBus605265_consumption, 44_LVBus605266_consumption, 44_LVBus605267_consumption, 44_LVBus605269_consumption, 44_LVBus605270_consumption, 44_LVBus605272_consumption, 44_LVBus605273_consumption, 44_LVBus605281_consumption, 44_LVBus605283_consumption, 44_LVBus605284_consumption, 44_LVBus605285_consumption, 44_LVBus605287_consumption, 44_LVBus605289_consumption, 44_LVBus605292_consumption, 44_LVBus605293_consumption, 44_LVBus605294_consumption, 44_LVBus605298_consumption, 44_LVBus605299_consumption, 44_LVBus605300_consumption, 44_LVBus605302_consumption, 44_LVBus605303_consumption, 44_LVBus605304_consumption, 44_LVBus605308_consumption, 44_LVBus605321_consumption, 44_LVBus605323_consumption, 44_LVBus605326_consumption, 44_LVBus605327_consumption, 44_LVBus856493_consumption, 44_LVBus856494_consumption, 44_LVBus856669_consumption, 44_LVBus856670_consumption, 44_LVBus858920_consumption, 44_LVBus858921_consumption, 44_LVBus858923_consumption, 44_LVBus858924_consumption, 44_LVBus858925_consumption, 44_LVBus858926_consumption, 44_LVBus864502_consumption, 44_LVBus864503_consumption, 44_LVBus864504_consumption, 44_LVBus864505_consumption, 44_LVBus864506_consumption, 44_LVBus864508_consumption, 44_LVBus864510_consumption, 44_LVBus864511_consumption, 44_LVBus864512_consumption, 44_LVBus864513_consumption, 44_LVBus864514_consumption, 44_LVBus864515_consumption, 44_LVBus864516_consumption, 44_LVBus864517_consumption, 44_LVBus864518_consumption, 44_LVBus872884_consumption, 44_LVBus872885_consumption, 44_LVBus872886_consumption, 44_LVBus872887_consumption, 44_LVBus872888_consumption, 44_LVBus872895_consumption, 44_LVBus873680_consumption, 44_LVBus873681_consumption, 44_LVBus877916_consumption, 44_LVBus877917_consumption, 44_LVBus877918_consumption, 44_LVBus877919_consumption, 44_LVBus885250_consumption, 44_LVBus885252_consumption, 44_LVBus885253_consumption, 44_LVBus885254_consumption, 44_LVBus885255_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  388 group(s) of loads (776 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  5 group(s) of series lines (10 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  498 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus604924_consumption, 44_LVBus604924_production, 44_LVBus604925_consumption, 44_LVBus604925_production, 44_LVBus604928_production, 44_LVBus604930_consumption, 44_LVBus604930_production, 44_LVBus604932_production, 44_LVBus604934_production, 44_LVBus604936_consumption, 44_LVBus604936_production, 44_LVBus604938_production, 44_LVBus604939_production, 44_LVBus604940_production, 44_LVBus604941_production, 44_LVBus604942_production, 44_LVBus604943_production, 44_LVBus604945_production, 44_LVBus604946_production, 44_LVBus604947_production, 44_LVBus604951_production, 44_LVBus604952_production, 44_LVBus604953_production, 44_LVBus604954_production, 44_LVBus604955_production, 44_LVBus604957_production, 44_LVBus604958_production, 44_LVBus604959_production, 44_LVBus604960_production, 44_LVBus604961_production, 44_LVBus604962_production, 44_LVBus604963_consumption, 44_LVBus604963_production, 44_LVBus604964_production, 44_LVBus604965_production, 44_LVBus604966_production, 44_LVBus604967_production, 44_LVBus604968_production, 44_LVBus604969_production, 44_LVBus604970_production, 44_LVBus604972_consumption, 44_LVBus604972_production, 44_LVBus604973_production, 44_LVBus604974_production, 44_LVBus604975_production, 44_LVBus604976_consumption, 44_LVBus604976_production, 44_LVBus604977_production, 44_LVBus604978_production, 44_LVBus604979_consumption, 44_LVBus604979_production, 44_LVBus604981_production, 44_LVBus604982_production, 44_LVBus604983_production, 44_LVBus604984_production, 44_LVBus604985_consumption, 44_LVBus604985_production, 44_LVBus604986_production, 44_LVBus604987_production, 44_LVBus604988_production, 44_LVBus604989_production, 44_LVBus604991_production, 44_LVBus604992_production, 44_LVBus604993_production, 44_LVBus604994_production, 44_LVBus604995_production, 44_LVBus604996_consumption, 44_LVBus604996_production, 44_LVBus604997_production, 44_LVBus604998_production, 44_LVBus604999_production, 44_LVBus605000_consumption, 44_LVBus605000_production, 44_LVBus605001_production, 44_LVBus605002_production, 44_LVBus605003_consumption, 44_LVBus605003_production, 44_LVBus605004_production, 44_LVBus605006_production, 44_LVBus605008_production, 44_LVBus605010_production, 44_LVBus605012_production, 44_LVBus605014_consumption, 44_LVBus605014_production, 44_LVBus605016_consumption, 44_LVBus605016_production, 44_LVBus605018_production, 44_LVBus605020_consumption, 44_LVBus605020_production, 44_LVBus605021_consumption, 44_LVBus605021_production, 44_LVBus605022_consumption, 44_LVBus605022_production, 44_LVBus605023_consumption, 44_LVBus605023_production, 44_LVBus605024_production, 44_LVBus605025_consumption, 44_LVBus605025_production, 44_LVBus605026_production, 44_LVBus605027_consumption, 44_LVBus605027_production, 44_LVBus605028_production, 44_LVBus605029_production, 44_LVBus605030_production, 44_LVBus605031_consumption, 44_LVBus605031_production, 44_LVBus605032_consumption, 44_LVBus605032_production, 44_LVBus605033_production, 44_LVBus605034_production, 44_LVBus605035_production, 44_LVBus605036_production, 44_LVBus605037_production, 44_LVBus605038_production, 44_LVBus605040_consumption, 44_LVBus605040_production, 44_LVBus605042_production, 44_LVBus605044_consumption, 44_LVBus605044_production, 44_LVBus605046_consumption, 44_LVBus605046_production, 44_LVBus605048_production, 44_LVBus605049_production, 44_LVBus605050_production, 44_LVBus605052_production, 44_LVBus605053_production, 44_LVBus605054_production, 44_LVBus605056_production, 44_LVBus605057_production, 44_LVBus605058_production, 44_LVBus605059_production, 44_LVBus605060_production, 44_LVBus605061_consumption, 44_LVBus605061_production, 44_LVBus605062_consumption, 44_LVBus605062_production, 44_LVBus605063_production, 44_LVBus605064_consumption, 44_LVBus605064_production, 44_LVBus605065_consumption, 44_LVBus605065_production, 44_LVBus605067_consumption, 44_LVBus605067_production, 44_LVBus605069_consumption, 44_LVBus605069_production, 44_LVBus605070_production, 44_LVBus605071_production, 44_LVBus605072_production, 44_LVBus605074_production, 44_LVBus605075_production, 44_LVBus605076_production, 44_LVBus605077_production, 44_LVBus605078_production, 44_LVBus605079_production, 44_LVBus605080_production, 44_LVBus605082_consumption, 44_LVBus605082_production, 44_LVBus605083_production, 44_LVBus605084_consumption, 44_LVBus605084_production, 44_LVBus605085_consumption, 44_LVBus605085_production, 44_LVBus605087_consumption, 44_LVBus605087_production, 44_LVBus605088_production, 44_LVBus605089_production, 44_LVBus605090_production, 44_LVBus605091_production, 44_LVBus605092_production, 44_LVBus605093_production, 44_LVBus605094_production, 44_LVBus605095_production, 44_LVBus605096_consumption, 44_LVBus605096_production, 44_LVBus605101_production, 44_LVBus605102_production, 44_LVBus605103_production, 44_LVBus605104_production, 44_LVBus605105_production, 44_LVBus605106_production, 44_LVBus605107_production, 44_LVBus605108_consumption, 44_LVBus605108_production, 44_LVBus605109_production, 44_LVBus605110_consumption, 44_LVBus605110_production, 44_LVBus605111_production, 44_LVBus605112_production, 44_LVBus605113_production, 44_LVBus605114_production, 44_LVBus605115_production, 44_LVBus605116_consumption, 44_LVBus605116_production, 44_LVBus605117_production, 44_LVBus605119_production, 44_LVBus605120_production, 44_LVBus605121_production, 44_LVBus605122_consumption, 44_LVBus605122_production, 44_LVBus605123_consumption, 44_LVBus605123_production, 44_LVBus605124_consumption, 44_LVBus605124_production, 44_LVBus605125_consumption, 44_LVBus605125_production, 44_LVBus605126_production, 44_LVBus605127_production, 44_LVBus605128_production, 44_LVBus605129_production, 44_LVBus605131_consumption, 44_LVBus605131_production, 44_LVBus605133_consumption, 44_LVBus605133_production, 44_LVBus605135_consumption, 44_LVBus605135_production, 44_LVBus605136_production, 44_LVBus605137_consumption, 44_LVBus605137_production, 44_LVBus605138_production, 44_LVBus605139_production, 44_LVBus605141_production, 44_LVBus605142_production, 44_LVBus605143_production, 44_LVBus605144_production, 44_LVBus605146_production, 44_LVBus605147_production, 44_LVBus605148_production, 44_LVBus605149_consumption, 44_LVBus605149_production, 44_LVBus605150_production, 44_LVBus605152_consumption, 44_LVBus605152_production, 44_LVBus605153_production, 44_LVBus605154_consumption, 44_LVBus605154_production, 44_LVBus605156_consumption, 44_LVBus605156_production, 44_LVBus605157_consumption, 44_LVBus605157_production, 44_LVBus605158_production, 44_LVBus605159_production, 44_LVBus605160_consumption, 44_LVBus605160_production, 44_LVBus605161_production, 44_LVBus605162_production, 44_LVBus605163_production, 44_LVBus605164_production, 44_LVBus605165_consumption, 44_LVBus605165_production, 44_LVBus605166_consumption, 44_LVBus605166_production, 44_LVBus605167_consumption, 44_LVBus605167_production, 44_LVBus605168_production, 44_LVBus605169_consumption, 44_LVBus605169_production, 44_LVBus605170_consumption, 44_LVBus605170_production, 44_LVBus605171_production, 44_LVBus605173_production, 44_LVBus605174_production, 44_LVBus605175_production, 44_LVBus605176_production, 44_LVBus605177_production, 44_LVBus605178_consumption, 44_LVBus605178_production, 44_LVBus605179_consumption, 44_LVBus605179_production, 44_LVBus605180_production, 44_LVBus605181_production, 44_LVBus605182_production, 44_LVBus605183_production, 44_LVBus605184_production, 44_LVBus605185_production, 44_LVBus605186_production, 44_LVBus605187_production, 44_LVBus605190_production, 44_LVBus605194_production, 44_LVBus605196_production, 44_LVBus605198_production, 44_LVBus605199_production, 44_LVBus605200_production, 44_LVBus605201_production, 44_LVBus605202_production, 44_LVBus605203_production, 44_LVBus605204_production, 44_LVBus605206_production, 44_LVBus605208_production, 44_LVBus605209_consumption, 44_LVBus605209_production, 44_LVBus605210_production, 44_LVBus605211_production, 44_LVBus605212_production, 44_LVBus605214_production, 44_LVBus605215_production, 44_LVBus605216_consumption, 44_LVBus605216_production, 44_LVBus605217_consumption, 44_LVBus605217_production, 44_LVBus605218_consumption, 44_LVBus605218_production, 44_LVBus605219_consumption, 44_LVBus605219_production, 44_LVBus605220_consumption, 44_LVBus605220_production, 44_LVBus605221_consumption, 44_LVBus605221_production, 44_LVBus605222_production, 44_LVBus605223_consumption, 44_LVBus605223_production, 44_LVBus605224_production, 44_LVBus605225_consumption, 44_LVBus605225_production, 44_LVBus605226_production, 44_LVBus605228_production, 44_LVBus605229_production, 44_LVBus605230_production, 44_LVBus605231_production, 44_LVBus605232_production, 44_LVBus605233_production, 44_LVBus605234_production, 44_LVBus605235_production, 44_LVBus605237_consumption, 44_LVBus605237_production, 44_LVBus605238_consumption, 44_LVBus605238_production, 44_LVBus605239_production, 44_LVBus605240_consumption, 44_LVBus605240_production, 44_LVBus605241_production, 44_LVBus605248_consumption, 44_LVBus605248_production, 44_LVBus605249_consumption, 44_LVBus605249_production, 44_LVBus605251_consumption, 44_LVBus605251_production, 44_LVBus605252_consumption, 44_LVBus605252_production, 44_LVBus605253_consumption, 44_LVBus605253_production, 44_LVBus605254_production, 44_LVBus605255_consumption, 44_LVBus605255_production, 44_LVBus605256_consumption, 44_LVBus605256_production, 44_LVBus605257_consumption, 44_LVBus605257_production, 44_LVBus605258_production, 44_LVBus605260_production, 44_LVBus605261_production, 44_LVBus605262_production, 44_LVBus605263_production, 44_LVBus605264_consumption, 44_LVBus605264_production, 44_LVBus605265_production, 44_LVBus605266_production, 44_LVBus605267_production, 44_LVBus605269_production, 44_LVBus605270_production, 44_LVBus605271_production, 44_LVBus605272_production, 44_LVBus605273_production, 44_LVBus605275_consumption, 44_LVBus605275_production, 44_LVBus605276_consumption, 44_LVBus605276_production, 44_LVBus605277_consumption, 44_LVBus605277_production, 44_LVBus605279_consumption, 44_LVBus605279_production, 44_LVBus605280_consumption, 44_LVBus605280_production, 44_LVBus605281_production, 44_LVBus605282_consumption, 44_LVBus605282_production, 44_LVBus605283_production, 44_LVBus605284_production, 44_LVBus605285_production, 44_LVBus605286_consumption, 44_LVBus605286_production, 44_LVBus605287_production, 44_LVBus605288_consumption, 44_LVBus605288_production, 44_LVBus605289_production, 44_LVBus605291_consumption, 44_LVBus605291_production, 44_LVBus605292_production, 44_LVBus605293_production, 44_LVBus605294_production, 44_LVBus605298_production, 44_LVBus605299_production, 44_LVBus605300_production, 44_LVBus605301_consumption, 44_LVBus605301_production, 44_LVBus605302_production, 44_LVBus605303_production, 44_LVBus605304_production, 44_LVBus605306_production, 44_LVBus605307_production, 44_LVBus605308_production, 44_LVBus605313_consumption, 44_LVBus605313_production, 44_LVBus605315_production, 44_LVBus605317_production, 44_LVBus605319_production, 44_LVBus605320_consumption, 44_LVBus605320_production, 44_LVBus605321_production, 44_LVBus605322_consumption, 44_LVBus605322_production, 44_LVBus605323_production, 44_LVBus605324_production, 44_LVBus605326_production, 44_LVBus605327_production, 44_LVBus605331_consumption, 44_LVBus605331_production, 44_LVBus851399_production, 44_LVBus851536_production, 44_LVBus853305_consumption, 44_LVBus853305_production, 44_LVBus856368_consumption, 44_LVBus856368_production, 44_LVBus856493_production, 44_LVBus856494_production, 44_LVBus856523_consumption, 44_LVBus856523_production, 44_LVBus856669_production, 44_LVBus856670_production, 44_LVBus858829_consumption, 44_LVBus858829_production, 44_LVBus858920_production, 44_LVBus858921_production, 44_LVBus858922_consumption, 44_LVBus858922_production, 44_LVBus858923_production, 44_LVBus858924_production, 44_LVBus858925_production, 44_LVBus858926_production, 44_LVBus864500_consumption, 44_LVBus864500_production, 44_LVBus864501_consumption, 44_LVBus864501_production, 44_LVBus864502_production, 44_LVBus864503_production, 44_LVBus864504_production, 44_LVBus864505_production, 44_LVBus864506_production, 44_LVBus864507_production, 44_LVBus864508_production, 44_LVBus864509_production, 44_LVBus864510_production, 44_LVBus864511_production, 44_LVBus864512_production, 44_LVBus864513_production, 44_LVBus864514_production, 44_LVBus864515_production, 44_LVBus864516_production, 44_LVBus864517_production, 44_LVBus864518_production, 44_LVBus870163_consumption, 44_LVBus870163_production, 44_LVBus872884_production, 44_LVBus872885_production, 44_LVBus872886_production, 44_LVBus872887_production, 44_LVBus872888_production, 44_LVBus872889_consumption, 44_LVBus872889_production, 44_LVBus872890_production, 44_LVBus872891_production, 44_LVBus872892_production, 44_LVBus872893_consumption, 44_LVBus872893_production, 44_LVBus872894_production, 44_LVBus872895_production, 44_LVBus873680_production, 44_LVBus873681_production, 44_LVBus877916_production, 44_LVBus877917_production, 44_LVBus877918_production, 44_LVBus877919_production, 44_LVBus877920_production, 44_LVBus877921_production, 44_LVBus885249_consumption, 44_LVBus885249_production, 44_LVBus885250_production, 44_LVBus885251_consumption, 44_LVBus885251_production, 44_LVBus885252_production, 44_LVBus885253_production, 44_LVBus885254_production, 44_LVBus885255_production, 44_LVBus885256_consumption, 44_LVBus885256_production, 44_MVLV33011_consumption, 44_MVLV33011_production, 44_MVLV50806_consumption, 44_MVLV50806_production.

