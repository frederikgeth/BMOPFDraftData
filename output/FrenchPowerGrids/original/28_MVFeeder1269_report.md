# BMOPF Network Summary: 28_MVFeeder1269

**Generated:** 2026-10-01 23:34:03  
**Findings:** 0 errors · 5 warnings · 525 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 75 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 949 |  |
| line | 873 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1430 | 3.733 MW, 1.12 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 75 |  |
| switch | 0 |  |
| transformer | 75 | Dyn11×75 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 170 | 169 | 22 | 0 |
| LV_236V | 236.0 V | 779 | 704 | 1408 | 0 |

**Transformer transitions:**

- `28_MVLV60179_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV27154_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26368_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47855_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57875_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV44741_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV08952_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV33224_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42378_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32559_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57208_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV12731_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV53651_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV63985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV56933_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV16405_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV63371_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42427_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84669_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49826_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57622_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV10874_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32561_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV28970_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV19754_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV52459_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13881_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55126_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV43798_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57835_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV10907_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV00122_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV31901_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV73617_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41055_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV34341_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV04892_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV63621_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV03012_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV10156_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40348_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV03185_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85025_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV56956_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85364_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV34110_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49823_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76315_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV50096_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49795_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80146_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13793_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV27128_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV07478_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV19352_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80145_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV78570_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV19355_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV43903_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV60177_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV02359_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80284_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57149_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV28836_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49874_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV56997_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32570_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV62194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42379_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV19351_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV63650_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55632_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV08891_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 8 |
| Degree-1 buses | 326 |
| Tree depth (max hops) | 55 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 949 | 1 | 948 | 0 | 0 | 0 |
| Tier LV_236V | 779 | 75 | 704 | 0 | 0 | 0 |
| Tier MV_11.8kV | 170 | 1 | 169 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 75; skipped invalid branches: 0.

Galvanic zones: 76; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_HARCA | MV_11.8kV | 170 | 0 | 0 | 75 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3626 declared bus terminals; 3323 mapped line/closed-switch conductor edges; 303 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 36900.0 | 2.743 | 4290 |
| q_nom | 0.0 | 11100.0 | 2.743 | 4290 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.06 | 1940.0 | 1.513 | 873 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.57 | 75 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 892 of 1430 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962170_consumption' has phase imbalance of 250.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181917_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182372_consumption' has phase imbalance of 38.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884445_consumption' has phase imbalance of 36.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181725_consumption' has phase imbalance of 99.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181894_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus963804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus968668_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182194_consumption' has phase imbalance of 139.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus895805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181997_consumption' has phase imbalance of 135.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182377_consumption' has phase imbalance of 147.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181981_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182257_consumption' has phase imbalance of 85.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182362_consumption' has phase imbalance of 197.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946718_consumption' has phase imbalance of 75.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus867218_consumption' has phase imbalance of 274.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus968667_consumption' has phase imbalance of 221.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus925033_consumption' has phase imbalance of 210.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948994_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus942769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182251_consumption' has phase imbalance of 295.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus895806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182343_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181726_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182136_consumption' has phase imbalance of 174.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957075_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus868903_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181683_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181899_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182281_consumption' has phase imbalance of 284.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182160_consumption' has phase imbalance of 274.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181691_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182079_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181707_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus856498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181747_consumption' has phase imbalance of 255.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182373_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912064_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181813_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182180_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182001_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus926431_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182366_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus963806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182157_consumption' has phase imbalance of 198.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus955400_consumption' has phase imbalance of 117.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182052_consumption' has phase imbalance of 53.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182210_consumption' has phase imbalance of 147.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181716_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182058_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182238_consumption' has phase imbalance of 217.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182049_consumption' has phase imbalance of 239.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182193_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182297_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181822_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181700_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182134_consumption' has phase imbalance of 225.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182161_consumption' has phase imbalance of 244.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus852560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181769_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181862_consumption' has phase imbalance of 182.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus880315_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182124_consumption' has phase imbalance of 208.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965483_consumption' has phase imbalance of 196.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182061_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182337_consumption' has phase imbalance of 218.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182192_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181843_consumption' has phase imbalance of 87.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182302_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181906_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182043_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182215_consumption' has phase imbalance of 220.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182320_consumption' has phase imbalance of 275.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182273_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181931_consumption' has phase imbalance of 28.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182265_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182142_consumption' has phase imbalance of 250.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181832_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181972_consumption' has phase imbalance of 145.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181684_consumption' has phase imbalance of 278.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901238_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181821_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182269_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus973767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182283_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965485_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182285_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182010_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182186_consumption' has phase imbalance of 195.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948999_consumption' has phase imbalance of 167.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181863_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181936_consumption' has phase imbalance of 137.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182311_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181715_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181934_consumption' has phase imbalance of 261.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus852559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181953_consumption' has phase imbalance of 239.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182094_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus974198_consumption' has phase imbalance of 141.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus963801_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182087_consumption' has phase imbalance of 292.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948997_consumption' has phase imbalance of 265.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182229_consumption' has phase imbalance of 32.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182128_consumption' has phase imbalance of 182.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182235_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus925034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947182_consumption' has phase imbalance of 254.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181811_consumption' has phase imbalance of 277.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus977372_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182172_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181748_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181975_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182034_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181890_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948995_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962169_consumption' has phase imbalance of 144.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus895807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181980_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182354_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181743_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181943_consumption' has phase imbalance of 267.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965488_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181861_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181785_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182254_consumption' has phase imbalance of 125.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181930_consumption' has phase imbalance of 288.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus972364_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182059_consumption' has phase imbalance of 191.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182324_consumption' has phase imbalance of 33.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181865_consumption' has phase imbalance of 146.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181746_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181690_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182315_consumption' has phase imbalance of 224.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus955402_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus903773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus960379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182011_consumption' has phase imbalance of 133.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182258_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus977175_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181783_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182319_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181856_consumption' has phase imbalance of 244.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus963798_consumption' has phase imbalance of 254.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182108_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus880316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181694_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182096_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus974197_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181915_consumption' has phase imbalance of 157.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182146_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182017_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181949_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946790_consumption' has phase imbalance of 158.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181912_consumption' has phase imbalance of 125.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181927_consumption' has phase imbalance of 273.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181965_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181770_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182092_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181814_consumption' has phase imbalance of 64.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus977173_consumption' has phase imbalance of 225.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182039_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181946_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus856496_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182332_consumption' has phase imbalance of 241.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962172_consumption' has phase imbalance of 242.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus860858_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus974199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182348_consumption' has phase imbalance of 204.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182126_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182208_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181733_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182280_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181957_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181893_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182063_consumption' has phase imbalance of 210.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181721_consumption' has phase imbalance of 103.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182288_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182267_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181892_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181921_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181693_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus868901_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181782_consumption' has phase imbalance of 140.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182344_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus968554_consumption' has phase imbalance of 200.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182042_consumption' has phase imbalance of 258.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus868902_consumption' has phase imbalance of 233.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181918_consumption' has phase imbalance of 73.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus939655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912065_consumption' has phase imbalance of 24.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957074_consumption' has phase imbalance of 65.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181944_consumption' has phase imbalance of 287.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182028_consumption' has phase imbalance of 41.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181777_consumption' has phase imbalance of 146.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882132_consumption' has phase imbalance of 260.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946787_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181829_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182159_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus963802_consumption' has phase imbalance of 288.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181723_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181699_consumption' has phase imbalance of 272.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181826_consumption' has phase imbalance of 204.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182290_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182349_consumption' has phase imbalance of 185.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181935_consumption' has phase imbalance of 84.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181970_consumption' has phase imbalance of 34.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957882_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182027_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181879_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181698_consumption' has phase imbalance of 21.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181709_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181719_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182338_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182144_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus963796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181779_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181960_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181704_consumption' has phase imbalance of 214.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182382_consumption' has phase imbalance of 163.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181848_consumption' has phase imbalance of 191.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus974196_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181728_consumption' has phase imbalance of 260.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182335_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus977172_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus968669_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus852557_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182232_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182276_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182187_consumption' has phase imbalance of 253.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182005_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181902_consumption' has phase imbalance of 20.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181937_consumption' has phase imbalance of 183.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182148_consumption' has phase imbalance of 201.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181876_consumption' has phase imbalance of 269.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947301_consumption' has phase imbalance of 212.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181845_consumption' has phase imbalance of 185.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182361_consumption' has phase imbalance of 139.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182292_consumption' has phase imbalance of 274.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181866_consumption' has phase imbalance of 266.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182314_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus872015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182384_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181818_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus895717_consumption' has phase imbalance of 260.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181966_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182084_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181954_consumption' has phase imbalance of 82.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181840_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181974_consumption' has phase imbalance of 109.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962173_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182347_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182323_consumption' has phase imbalance of 129.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182081_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962174_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182151_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182201_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181977_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181823_consumption' has phase imbalance of 118.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182000_consumption' has phase imbalance of 178.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181692_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus873791_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181864_consumption' has phase imbalance of 64.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182380_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947200_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181791_consumption' has phase imbalance of 86.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182298_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus968666_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182205_consumption' has phase imbalance of 57.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182345_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181999_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181945_consumption' has phase imbalance of 262.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182275_consumption' has phase imbalance of 186.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181933_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus873052_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182342_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181796_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182237_consumption' has phase imbalance of 255.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182024_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182231_consumption' has phase imbalance of 205.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181720_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181956_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181729_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181799_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus904328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182305_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181947_consumption' has phase imbalance of 261.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182012_consumption' has phase imbalance of 87.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962175_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus856497_consumption' has phase imbalance of 249.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus942768_consumption' has phase imbalance of 39.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182056_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181722_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182225_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182095_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181924_consumption' has phase imbalance of 238.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181979_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181940_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182195_consumption' has phase imbalance of 136.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181760_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181901_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182351_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182093_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182080_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182318_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181872_consumption' has phase imbalance of 246.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus927456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181958_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus856056_consumption' has phase imbalance of 196.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181928_consumption' has phase imbalance of 231.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182241_consumption' has phase imbalance of 147.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182217_consumption' has phase imbalance of 36.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus867220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181753_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181846_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182190_consumption' has phase imbalance of 176.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182065_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912816_consumption' has phase imbalance of 139.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus929721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181801_consumption' has phase imbalance of 74.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182236_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus856499_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181738_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948780_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182346_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181849_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182089_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus972586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus852606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182350_consumption' has phase imbalance of 67.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181870_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947300_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182033_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181702_consumption' has phase imbalance of 278.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus859955_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181925_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181984_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182057_consumption' has phase imbalance of 214.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182018_consumption' has phase imbalance of 131.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181809_consumption' has phase imbalance of 213.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181955_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965489_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus873704_consumption' has phase imbalance of 168.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182106_consumption' has phase imbalance of 156.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus892920_consumption' has phase imbalance of 213.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181703_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182289_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181941_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182099_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946496_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus972365_consumption' has phase imbalance of 85.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182077_consumption' has phase imbalance of 267.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182381_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182211_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181932_consumption' has phase imbalance of 101.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus903774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus182213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus181914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1430 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.733 MW |
| Total load Q | 1.12 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV60179_Transformer | 275.0 kVA | 21.8% |
| 28_MVLV27154_Transformer | 176.0 kVA | 16.6% |
| 28_MVLV26368_Transformer | 275.0 kVA | 12.9% |
| 28_MVLV47855_Transformer | 440.0 kVA | 32.9% |
| 28_MVLV57875_Transformer | 176.0 kVA | 16.0% |
| 28_MVLV44741_Transformer | 176.0 kVA | 17.3% |
| 28_MVLV08952_Transformer | 176.0 kVA | 14.3% |
| 28_MVLV33224_Transformer | 110.0 kVA | 19.3% |
| 28_MVLV42378_Transformer | 275.0 kVA | 22.0% |
| 28_MVLV32559_Transformer | 275.0 kVA | 19.0% |
| 28_MVLV57208_Transformer | 176.0 kVA | 11.9% |
| 28_MVLV12731_Transformer | 176.0 kVA | 17.6% |
| 28_MVLV53651_Transformer | 176.0 kVA | 15.0% |
| 28_MVLV63985_Transformer | 440.0 kVA | 49.4% |
| 28_MVLV56933_Transformer | 275.0 kVA | 24.7% |
| 28_MVLV57876_Transformer | 110.0 kVA | 24.1% |
| 28_MVLV16405_Transformer | 275.0 kVA | 20.1% |
| 28_MVLV63371_Transformer | 275.0 kVA | 20.4% |
| 28_MVLV42427_Transformer | 176.0 kVA | 17.0% |
| 28_MVLV84669_Transformer | 110.0 kVA | 2.8% |
| 28_MVLV49826_Transformer | 275.0 kVA | 24.3% |
| 28_MVLV57622_Transformer | 275.0 kVA | 21.6% |
| 28_MVLV10874_Transformer | 440.0 kVA | 20.1% |
| 28_MVLV32561_Transformer | 693.0 kVA | 12.8% |
| 28_MVLV28970_Transformer | 275.0 kVA | 20.7% |
| 28_MVLV19754_Transformer | 110.0 kVA | 7.9% |
| 28_MVLV52459_Transformer | 110.0 kVA | 0.1% |
| 28_MVLV13881_Transformer | 176.0 kVA | 0.0% |
| 28_MVLV55126_Transformer | 176.0 kVA | 0.0% |
| 28_MVLV43798_Transformer | 275.0 kVA | 20.0% |
| 28_MVLV57835_Transformer | 110.0 kVA | 5.5% |
| 28_MVLV10907_Transformer | 440.0 kVA | 25.8% |
| 28_MVLV00122_Transformer | 275.0 kVA | 16.6% |
| 28_MVLV31901_Transformer | 110.0 kVA | 12.9% |
| 28_MVLV73617_Transformer | 440.0 kVA | 34.2% |
| 28_MVLV41055_Transformer | 275.0 kVA | 34.7% |
| 28_MVLV34341_Transformer | 110.0 kVA | 1.6% |
| 28_MVLV04892_Transformer | 275.0 kVA | 17.5% |
| 28_MVLV63621_Transformer | 275.0 kVA | 25.1% |
| 28_MVLV03012_Transformer | 110.0 kVA | 9.6% |
| 28_MVLV10156_Transformer | 110.0 kVA | 19.3% |
| 28_MVLV40348_Transformer | 275.0 kVA | 28.5% |
| 28_MVLV03185_Transformer | 176.0 kVA | 21.0% |
| 28_MVLV85025_Transformer | 440.0 kVA | 24.0% |
| 28_MVLV56956_Transformer | 110.0 kVA | 30.3% |
| 28_MVLV85364_Transformer | 110.0 kVA | 20.0% |
| 28_MVLV34110_Transformer | 275.0 kVA | 24.7% |
| 28_MVLV49823_Transformer | 176.0 kVA | 9.7% |
| 28_MVLV76315_Transformer | 176.0 kVA | 9.3% |
| 28_MVLV50096_Transformer | 693.0 kVA | 29.0% |
| 28_MVLV49795_Transformer | 275.0 kVA | 28.2% |
| 28_MVLV42411_Transformer | 275.0 kVA | 12.6% |
| 28_MVLV80146_Transformer | 176.0 kVA | 28.6% |
| 28_MVLV13793_Transformer | 110.0 kVA | 2.4% |
| 28_MVLV27128_Transformer | 110.0 kVA | 5.6% |
| 28_MVLV07478_Transformer | 110.0 kVA | 15.0% |
| 28_MVLV19352_Transformer | 176.0 kVA | 40.8% |
| 28_MVLV80145_Transformer | 110.0 kVA | 18.3% |
| 28_MVLV78570_Transformer | 693.0 kVA | 34.8% |
| 28_MVLV19355_Transformer | 275.0 kVA | 28.7% |
| 28_MVLV43903_Transformer | 275.0 kVA | 31.7% |
| 28_MVLV60177_Transformer | 275.0 kVA | 18.6% |
| 28_MVLV02359_Transformer | 440.0 kVA | 27.3% |
| 28_MVLV80284_Transformer | 275.0 kVA | 27.3% |
| 28_MVLV57149_Transformer | 275.0 kVA | 12.8% |
| 28_MVLV28836_Transformer | 110.0 kVA | 14.6% |
| 28_MVLV49874_Transformer | 176.0 kVA | 12.4% |
| 28_MVLV56997_Transformer | 275.0 kVA | 17.5% |
| 28_MVLV32570_Transformer | 176.0 kVA | 19.4% |
| 28_MVLV62194_Transformer | 110.0 kVA | 3.3% |
| 28_MVLV42379_Transformer | 440.0 kVA | 32.0% |
| 28_MVLV19351_Transformer | 110.0 kVA | 16.9% |
| 28_MVLV63650_Transformer | 110.0 kVA | 6.5% |
| 28_MVLV55632_Transformer | 110.0 kVA | 0.1% |
| 28_MVLV08891_Transformer | 275.0 kVA | 13.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.73 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '28_HARCA' (MV, 11.78 kV) has an electrical reach of 21.26 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 949 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 949 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 75 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 170 |
| LV_236V | 4-wire | 779 / 779 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 779 |
| Neutral branches | 704 |
| Grounding points | 75 |
| Neutral sections | 75 |
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
| 11.78 kV | 170 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 76 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1700.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 779 / 170 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 893 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 893 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus181683_production, 28_LVBus181684_production, 28_LVBus181685_production, 28_LVBus181686_production, 28_LVBus181690_production, 28_LVBus181691_production, 28_LVBus181692_production, 28_LVBus181693_production, 28_LVBus181694_production, 28_LVBus181695_consumption, 28_LVBus181695_production, 28_LVBus181696_production, 28_LVBus181698_production, 28_LVBus181699_production, 28_LVBus181700_production, 28_LVBus181701_production, 28_LVBus181702_production, 28_LVBus181703_production, 28_LVBus181704_production, 28_LVBus181705_production, 28_LVBus181707_production, 28_LVBus181708_consumption, 28_LVBus181708_production, 28_LVBus181709_production, 28_LVBus181710_production, 28_LVBus181714_consumption, 28_LVBus181714_production, 28_LVBus181715_production, 28_LVBus181716_production, 28_LVBus181717_production, 28_LVBus181719_production, 28_LVBus181720_production, 28_LVBus181721_production, 28_LVBus181722_production, 28_LVBus181723_production, 28_LVBus181725_production, 28_LVBus181726_production, 28_LVBus181727_consumption, 28_LVBus181727_production, 28_LVBus181728_production, 28_LVBus181729_production, 28_LVBus181730_consumption, 28_LVBus181730_production, 28_LVBus181731_production, 28_LVBus181732_production, 28_LVBus181733_production, 28_LVBus181734_production, 28_LVBus181736_production, 28_LVBus181737_production, 28_LVBus181738_production, 28_LVBus181742_consumption, 28_LVBus181742_production, 28_LVBus181743_production, 28_LVBus181744_production, 28_LVBus181745_production, 28_LVBus181746_production, 28_LVBus181747_production, 28_LVBus181748_production, 28_LVBus181749_consumption, 28_LVBus181749_production, 28_LVBus181750_production, 28_LVBus181752_production, 28_LVBus181753_production, 28_LVBus181754_production, 28_LVBus181756_production, 28_LVBus181757_consumption, 28_LVBus181757_production, 28_LVBus181759_production, 28_LVBus181760_production, 28_LVBus181761_consumption, 28_LVBus181761_production, 28_LVBus181763_production, 28_LVBus181764_production, 28_LVBus181766_production, 28_LVBus181767_consumption, 28_LVBus181767_production, 28_LVBus181768_consumption, 28_LVBus181768_production, 28_LVBus181769_production, 28_LVBus181770_production, 28_LVBus181771_production, 28_LVBus181772_production, 28_LVBus181773_production, 28_LVBus181777_production, 28_LVBus181779_production, 28_LVBus181781_production, 28_LVBus181782_production, 28_LVBus181783_production, 28_LVBus181785_production, 28_LVBus181787_production, 28_LVBus181789_consumption, 28_LVBus181789_production, 28_LVBus181791_production, 28_LVBus181793_consumption, 28_LVBus181793_production, 28_LVBus181795_production, 28_LVBus181796_production, 28_LVBus181797_production, 28_LVBus181798_production, 28_LVBus181799_production, 28_LVBus181801_production, 28_LVBus181803_consumption, 28_LVBus181803_production, 28_LVBus181804_consumption, 28_LVBus181804_production, 28_LVBus181805_consumption, 28_LVBus181805_production, 28_LVBus181806_production, 28_LVBus181807_production, 28_LVBus181808_production, 28_LVBus181809_production, 28_LVBus181811_production, 28_LVBus181813_production, 28_LVBus181814_production, 28_LVBus181815_production, 28_LVBus181817_production, 28_LVBus181818_production, 28_LVBus181819_production, 28_LVBus181820_consumption, 28_LVBus181820_production, 28_LVBus181821_production, 28_LVBus181822_production, 28_LVBus181823_production, 28_LVBus181824_production, 28_LVBus181826_production, 28_LVBus181827_production, 28_LVBus181828_consumption, 28_LVBus181828_production, 28_LVBus181829_production, 28_LVBus181830_consumption, 28_LVBus181830_production, 28_LVBus181831_production, 28_LVBus181832_production, 28_LVBus181834_consumption, 28_LVBus181834_production, 28_LVBus181835_production, 28_LVBus181837_production, 28_LVBus181840_production, 28_LVBus181842_production, 28_LVBus181843_production, 28_LVBus181844_consumption, 28_LVBus181844_production, 28_LVBus181845_production, 28_LVBus181846_production, 28_LVBus181848_production, 28_LVBus181849_production, 28_LVBus181851_consumption, 28_LVBus181851_production, 28_LVBus181852_production, 28_LVBus181853_production, 28_LVBus181855_consumption, 28_LVBus181855_production, 28_LVBus181856_production, 28_LVBus181857_consumption, 28_LVBus181857_production, 28_LVBus181861_production, 28_LVBus181862_production, 28_LVBus181863_production, 28_LVBus181864_production, 28_LVBus181865_production, 28_LVBus181866_production, 28_LVBus181867_production, 28_LVBus181869_production, 28_LVBus181870_production, 28_LVBus181871_production, 28_LVBus181872_production, 28_LVBus181874_consumption, 28_LVBus181874_production, 28_LVBus181875_production, 28_LVBus181876_production, 28_LVBus181878_production, 28_LVBus181879_production, 28_LVBus181881_consumption, 28_LVBus181881_production, 28_LVBus181882_consumption, 28_LVBus181882_production, 28_LVBus181884_consumption, 28_LVBus181884_production, 28_LVBus181885_consumption, 28_LVBus181885_production, 28_LVBus181886_consumption, 28_LVBus181886_production, 28_LVBus181887_consumption, 28_LVBus181887_production, 28_LVBus181888_consumption, 28_LVBus181888_production, 28_LVBus181889_production, 28_LVBus181890_production, 28_LVBus181892_production, 28_LVBus181893_production, 28_LVBus181894_production, 28_LVBus181898_consumption, 28_LVBus181898_production, 28_LVBus181899_production, 28_LVBus181900_consumption, 28_LVBus181900_production, 28_LVBus181901_production, 28_LVBus181902_production, 28_LVBus181906_production, 28_LVBus181907_consumption, 28_LVBus181907_production, 28_LVBus181909_consumption, 28_LVBus181909_production, 28_LVBus181912_production, 28_LVBus181914_production, 28_LVBus181915_production, 28_LVBus181917_production, 28_LVBus181918_production, 28_LVBus181919_production, 28_LVBus181920_production, 28_LVBus181921_production, 28_LVBus181922_consumption, 28_LVBus181922_production, 28_LVBus181923_consumption, 28_LVBus181923_production, 28_LVBus181924_production, 28_LVBus181925_production, 28_LVBus181926_production, 28_LVBus181927_production, 28_LVBus181928_production, 28_LVBus181930_production, 28_LVBus181931_production, 28_LVBus181932_production, 28_LVBus181933_production, 28_LVBus181934_production, 28_LVBus181935_production, 28_LVBus181936_production, 28_LVBus181937_production, 28_LVBus181939_production, 28_LVBus181940_production, 28_LVBus181941_production, 28_LVBus181942_production, 28_LVBus181943_production, 28_LVBus181944_production, 28_LVBus181945_production, 28_LVBus181946_production, 28_LVBus181947_production, 28_LVBus181949_production, 28_LVBus181951_consumption, 28_LVBus181951_production, 28_LVBus181952_production, 28_LVBus181953_production, 28_LVBus181954_production, 28_LVBus181955_production, 28_LVBus181956_production, 28_LVBus181957_production, 28_LVBus181958_production, 28_LVBus181959_consumption, 28_LVBus181959_production, 28_LVBus181960_production, 28_LVBus181962_production, 28_LVBus181963_consumption, 28_LVBus181963_production, 28_LVBus181965_production, 28_LVBus181966_production, 28_LVBus181968_production, 28_LVBus181970_production, 28_LVBus181972_production, 28_LVBus181973_consumption, 28_LVBus181973_production, 28_LVBus181974_production, 28_LVBus181975_production, 28_LVBus181977_production, 28_LVBus181978_consumption, 28_LVBus181978_production, 28_LVBus181979_production, 28_LVBus181980_production, 28_LVBus181981_production, 28_LVBus181982_consumption, 28_LVBus181982_production, 28_LVBus181983_production, 28_LVBus181984_production, 28_LVBus181985_production, 28_LVBus181989_production, 28_LVBus181991_production, 28_LVBus181993_consumption, 28_LVBus181993_production, 28_LVBus181995_production, 28_LVBus181997_production, 28_LVBus181999_production, 28_LVBus182000_production, 28_LVBus182001_production, 28_LVBus182003_production, 28_LVBus182004_consumption, 28_LVBus182004_production, 28_LVBus182005_production, 28_LVBus182006_production, 28_LVBus182007_production, 28_LVBus182009_consumption, 28_LVBus182009_production, 28_LVBus182010_production, 28_LVBus182011_production, 28_LVBus182012_production, 28_LVBus182013_production, 28_LVBus182015_production, 28_LVBus182016_production, 28_LVBus182017_production, 28_LVBus182018_production, 28_LVBus182019_consumption, 28_LVBus182019_production, 28_LVBus182020_production, 28_LVBus182022_production, 28_LVBus182023_consumption, 28_LVBus182023_production, 28_LVBus182024_production, 28_LVBus182026_consumption, 28_LVBus182026_production, 28_LVBus182027_production, 28_LVBus182028_production, 28_LVBus182029_production, 28_LVBus182033_production, 28_LVBus182034_production, 28_LVBus182035_production, 28_LVBus182036_consumption, 28_LVBus182036_production, 28_LVBus182038_production, 28_LVBus182039_production, 28_LVBus182040_consumption, 28_LVBus182040_production, 28_LVBus182041_consumption, 28_LVBus182041_production, 28_LVBus182042_production, 28_LVBus182043_production, 28_LVBus182044_production, 28_LVBus182046_consumption, 28_LVBus182046_production, 28_LVBus182047_consumption, 28_LVBus182047_production, 28_LVBus182048_production, 28_LVBus182049_production, 28_LVBus182051_consumption, 28_LVBus182051_production, 28_LVBus182052_production, 28_LVBus182054_consumption, 28_LVBus182054_production, 28_LVBus182056_production, 28_LVBus182057_production, 28_LVBus182058_production, 28_LVBus182059_production, 28_LVBus182060_production, 28_LVBus182061_production, 28_LVBus182062_consumption, 28_LVBus182062_production, 28_LVBus182063_production, 28_LVBus182064_consumption, 28_LVBus182064_production, 28_LVBus182065_production, 28_LVBus182067_consumption, 28_LVBus182067_production, 28_LVBus182068_consumption, 28_LVBus182068_production, 28_LVBus182069_consumption, 28_LVBus182069_production, 28_LVBus182070_consumption, 28_LVBus182070_production, 28_LVBus182071_production, 28_LVBus182072_consumption, 28_LVBus182072_production, 28_LVBus182073_consumption, 28_LVBus182073_production, 28_LVBus182077_production, 28_LVBus182079_production, 28_LVBus182080_production, 28_LVBus182081_production, 28_LVBus182083_consumption, 28_LVBus182083_production, 28_LVBus182084_production, 28_LVBus182086_consumption, 28_LVBus182086_production, 28_LVBus182087_production, 28_LVBus182088_production, 28_LVBus182089_production, 28_LVBus182091_production, 28_LVBus182092_production, 28_LVBus182093_production, 28_LVBus182094_production, 28_LVBus182095_production, 28_LVBus182096_production, 28_LVBus182098_consumption, 28_LVBus182098_production, 28_LVBus182099_production, 28_LVBus182100_consumption, 28_LVBus182100_production, 28_LVBus182101_consumption, 28_LVBus182101_production, 28_LVBus182102_consumption, 28_LVBus182102_production, 28_LVBus182106_production, 28_LVBus182108_production, 28_LVBus182110_consumption, 28_LVBus182110_production, 28_LVBus182111_consumption, 28_LVBus182111_production, 28_LVBus182112_consumption, 28_LVBus182112_production, 28_LVBus182113_consumption, 28_LVBus182113_production, 28_LVBus182115_consumption, 28_LVBus182115_production, 28_LVBus182116_consumption, 28_LVBus182116_production, 28_LVBus182117_consumption, 28_LVBus182117_production, 28_LVBus182118_production, 28_LVBus182120_production, 28_LVBus182121_production, 28_LVBus182122_production, 28_LVBus182123_production, 28_LVBus182124_production, 28_LVBus182125_production, 28_LVBus182126_production, 28_LVBus182127_consumption, 28_LVBus182127_production, 28_LVBus182128_production, 28_LVBus182129_production, 28_LVBus182131_consumption, 28_LVBus182131_production, 28_LVBus182132_consumption, 28_LVBus182132_production, 28_LVBus182133_production, 28_LVBus182134_production, 28_LVBus182136_production, 28_LVBus182137_consumption, 28_LVBus182137_production, 28_LVBus182138_production, 28_LVBus182139_production, 28_LVBus182140_production, 28_LVBus182141_production, 28_LVBus182142_production, 28_LVBus182144_production, 28_LVBus182145_consumption, 28_LVBus182145_production, 28_LVBus182146_production, 28_LVBus182147_production, 28_LVBus182148_production, 28_LVBus182150_consumption, 28_LVBus182150_production, 28_LVBus182151_production, 28_LVBus182152_production, 28_LVBus182153_production, 28_LVBus182154_consumption, 28_LVBus182154_production, 28_LVBus182156_consumption, 28_LVBus182156_production, 28_LVBus182157_production, 28_LVBus182158_consumption, 28_LVBus182158_production, 28_LVBus182159_production, 28_LVBus182160_production, 28_LVBus182161_production, 28_LVBus182166_production, 28_LVBus182168_consumption, 28_LVBus182168_production, 28_LVBus182170_production, 28_LVBus182172_production, 28_LVBus182174_consumption, 28_LVBus182174_production, 28_LVBus182175_consumption, 28_LVBus182175_production, 28_LVBus182176_consumption, 28_LVBus182176_production, 28_LVBus182177_production, 28_LVBus182178_consumption, 28_LVBus182178_production, 28_LVBus182179_consumption, 28_LVBus182179_production, 28_LVBus182180_production, 28_LVBus182181_consumption, 28_LVBus182181_production, 28_LVBus182185_consumption, 28_LVBus182185_production, 28_LVBus182186_production, 28_LVBus182187_production, 28_LVBus182188_production, 28_LVBus182190_production, 28_LVBus182192_production, 28_LVBus182193_production, 28_LVBus182194_production, 28_LVBus182195_production, 28_LVBus182197_consumption, 28_LVBus182197_production, 28_LVBus182199_consumption, 28_LVBus182199_production, 28_LVBus182200_consumption, 28_LVBus182200_production, 28_LVBus182201_production, 28_LVBus182202_production, 28_LVBus182204_consumption, 28_LVBus182204_production, 28_LVBus182205_production, 28_LVBus182206_production, 28_LVBus182208_production, 28_LVBus182210_production, 28_LVBus182211_production, 28_LVBus182213_production, 28_LVBus182215_production, 28_LVBus182216_consumption, 28_LVBus182216_production, 28_LVBus182217_production, 28_LVBus182218_production, 28_LVBus182219_production, 28_LVBus182221_consumption, 28_LVBus182221_production, 28_LVBus182222_production, 28_LVBus182223_production, 28_LVBus182225_production, 28_LVBus182227_production, 28_LVBus182229_production, 28_LVBus182230_consumption, 28_LVBus182230_production, 28_LVBus182231_production, 28_LVBus182232_production, 28_LVBus182233_production, 28_LVBus182235_production, 28_LVBus182236_production, 28_LVBus182237_production, 28_LVBus182238_production, 28_LVBus182239_production, 28_LVBus182241_production, 28_LVBus182242_production, 28_LVBus182243_consumption, 28_LVBus182243_production, 28_LVBus182244_production, 28_LVBus182246_production, 28_LVBus182247_consumption, 28_LVBus182247_production, 28_LVBus182248_production, 28_LVBus182250_production, 28_LVBus182251_production, 28_LVBus182252_production, 28_LVBus182254_production, 28_LVBus182255_production, 28_LVBus182257_production, 28_LVBus182258_production, 28_LVBus182259_production, 28_LVBus182261_production, 28_LVBus182262_production, 28_LVBus182265_production, 28_LVBus182267_production, 28_LVBus182268_production, 28_LVBus182269_production, 28_LVBus182270_consumption, 28_LVBus182270_production, 28_LVBus182272_production, 28_LVBus182273_production, 28_LVBus182274_production, 28_LVBus182275_production, 28_LVBus182276_production, 28_LVBus182277_production, 28_LVBus182278_production, 28_LVBus182280_production, 28_LVBus182281_production, 28_LVBus182282_production, 28_LVBus182283_production, 28_LVBus182284_production, 28_LVBus182285_production, 28_LVBus182286_consumption, 28_LVBus182286_production, 28_LVBus182288_production, 28_LVBus182289_production, 28_LVBus182290_production, 28_LVBus182291_production, 28_LVBus182292_production, 28_LVBus182294_production, 28_LVBus182295_consumption, 28_LVBus182295_production, 28_LVBus182296_production, 28_LVBus182297_production, 28_LVBus182298_production, 28_LVBus182300_consumption, 28_LVBus182300_production, 28_LVBus182301_consumption, 28_LVBus182301_production, 28_LVBus182302_production, 28_LVBus182303_consumption, 28_LVBus182303_production, 28_LVBus182304_production, 28_LVBus182305_production, 28_LVBus182310_consumption, 28_LVBus182310_production, 28_LVBus182311_production, 28_LVBus182312_production, 28_LVBus182313_consumption, 28_LVBus182313_production, 28_LVBus182314_production, 28_LVBus182315_production, 28_LVBus182317_consumption, 28_LVBus182317_production, 28_LVBus182318_production, 28_LVBus182319_production, 28_LVBus182320_production, 28_LVBus182321_consumption, 28_LVBus182321_production, 28_LVBus182323_production, 28_LVBus182324_production, 28_LVBus182326_production, 28_LVBus182328_consumption, 28_LVBus182328_production, 28_LVBus182329_production, 28_LVBus182330_production, 28_LVBus182331_consumption, 28_LVBus182331_production, 28_LVBus182332_production, 28_LVBus182333_production, 28_LVBus182335_production, 28_LVBus182336_production, 28_LVBus182337_production, 28_LVBus182338_production, 28_LVBus182339_production, 28_LVBus182340_production, 28_LVBus182342_production, 28_LVBus182343_production, 28_LVBus182344_production, 28_LVBus182345_production, 28_LVBus182346_production, 28_LVBus182347_production, 28_LVBus182348_production, 28_LVBus182349_production, 28_LVBus182350_production, 28_LVBus182351_production, 28_LVBus182353_production, 28_LVBus182354_production, 28_LVBus182355_production, 28_LVBus182356_production, 28_LVBus182358_consumption, 28_LVBus182358_production, 28_LVBus182359_production, 28_LVBus182360_consumption, 28_LVBus182360_production, 28_LVBus182361_production, 28_LVBus182362_production, 28_LVBus182363_production, 28_LVBus182364_production, 28_LVBus182365_consumption, 28_LVBus182365_production, 28_LVBus182366_production, 28_LVBus182367_production, 28_LVBus182368_consumption, 28_LVBus182368_production, 28_LVBus182369_production, 28_LVBus182370_consumption, 28_LVBus182370_production, 28_LVBus182371_consumption, 28_LVBus182371_production, 28_LVBus182372_production, 28_LVBus182373_production, 28_LVBus182374_production, 28_LVBus182375_production, 28_LVBus182376_production, 28_LVBus182377_production, 28_LVBus182379_production, 28_LVBus182380_production, 28_LVBus182381_production, 28_LVBus182382_production, 28_LVBus182384_production, 28_LVBus182385_consumption, 28_LVBus182385_production, 28_LVBus182386_production, 28_LVBus852557_production, 28_LVBus852558_consumption, 28_LVBus852558_production, 28_LVBus852559_production, 28_LVBus852560_production, 28_LVBus852606_production, 28_LVBus856056_production, 28_LVBus856496_production, 28_LVBus856497_production, 28_LVBus856498_production, 28_LVBus856499_production, 28_LVBus859955_production, 28_LVBus860858_production, 28_LVBus867217_consumption, 28_LVBus867217_production, 28_LVBus867218_production, 28_LVBus867219_consumption, 28_LVBus867219_production, 28_LVBus867220_production, 28_LVBus868900_consumption, 28_LVBus868900_production, 28_LVBus868901_production, 28_LVBus868902_production, 28_LVBus868903_production, 28_LVBus868984_production, 28_LVBus870907_consumption, 28_LVBus870907_production, 28_LVBus872015_production, 28_LVBus873052_production, 28_LVBus873704_production, 28_LVBus873789_consumption, 28_LVBus873789_production, 28_LVBus873790_consumption, 28_LVBus873790_production, 28_LVBus873791_production, 28_LVBus874539_production, 28_LVBus880315_production, 28_LVBus880316_production, 28_LVBus882132_production, 28_LVBus884445_production, 28_LVBus885392_consumption, 28_LVBus885392_production, 28_LVBus892920_production, 28_LVBus894933_consumption, 28_LVBus894933_production, 28_LVBus894934_consumption, 28_LVBus894934_production, 28_LVBus895715_consumption, 28_LVBus895715_production, 28_LVBus895716_consumption, 28_LVBus895716_production, 28_LVBus895717_production, 28_LVBus895805_production, 28_LVBus895806_production, 28_LVBus895807_production, 28_LVBus901238_production, 28_LVBus902915_consumption, 28_LVBus902915_production, 28_LVBus903773_production, 28_LVBus903774_production, 28_LVBus904328_production, 28_LVBus907995_consumption, 28_LVBus907995_production, 28_LVBus910091_consumption, 28_LVBus910091_production, 28_LVBus912060_consumption, 28_LVBus912060_production, 28_LVBus912061_consumption, 28_LVBus912061_production, 28_LVBus912062_production, 28_LVBus912063_production, 28_LVBus912064_production, 28_LVBus912065_production, 28_LVBus912815_consumption, 28_LVBus912815_production, 28_LVBus912816_production, 28_LVBus912817_production, 28_LVBus925033_production, 28_LVBus925034_production, 28_LVBus926431_production, 28_LVBus927456_production, 28_LVBus929541_consumption, 28_LVBus929541_production, 28_LVBus929721_production, 28_LVBus939655_production, 28_LVBus942768_production, 28_LVBus942769_production, 28_LVBus946496_production, 28_LVBus946497_production, 28_LVBus946498_production, 28_LVBus946499_production, 28_LVBus946718_production, 28_LVBus946719_production, 28_LVBus946785_consumption, 28_LVBus946785_production, 28_LVBus946786_consumption, 28_LVBus946786_production, 28_LVBus946787_production, 28_LVBus946788_consumption, 28_LVBus946788_production, 28_LVBus946789_production, 28_LVBus946790_production, 28_LVBus946919_production, 28_LVBus947180_consumption, 28_LVBus947180_production, 28_LVBus947181_production, 28_LVBus947182_production, 28_LVBus947200_production, 28_LVBus947299_consumption, 28_LVBus947299_production, 28_LVBus947300_production, 28_LVBus947301_production, 28_LVBus948778_production, 28_LVBus948779_consumption, 28_LVBus948779_production, 28_LVBus948780_production, 28_LVBus948994_production, 28_LVBus948995_production, 28_LVBus948996_production, 28_LVBus948997_production, 28_LVBus948998_production, 28_LVBus948999_production, 28_LVBus949000_production, 28_LVBus950930_consumption, 28_LVBus950930_production, 28_LVBus955400_production, 28_LVBus955401_consumption, 28_LVBus955401_production, 28_LVBus955402_production, 28_LVBus956520_consumption, 28_LVBus956520_production, 28_LVBus957074_production, 28_LVBus957075_production, 28_LVBus957880_production, 28_LVBus957881_consumption, 28_LVBus957881_production, 28_LVBus957882_production, 28_LVBus957883_production, 28_LVBus957884_production, 28_LVBus959440_consumption, 28_LVBus959440_production, 28_LVBus960378_production, 28_LVBus960379_production, 28_LVBus962168_production, 28_LVBus962169_production, 28_LVBus962170_production, 28_LVBus962171_consumption, 28_LVBus962171_production, 28_LVBus962172_production, 28_LVBus962173_production, 28_LVBus962174_production, 28_LVBus962175_production, 28_LVBus963179_consumption, 28_LVBus963179_production, 28_LVBus963795_consumption, 28_LVBus963795_production, 28_LVBus963796_production, 28_LVBus963797_consumption, 28_LVBus963797_production, 28_LVBus963798_production, 28_LVBus963799_consumption, 28_LVBus963799_production, 28_LVBus963800_consumption, 28_LVBus963800_production, 28_LVBus963801_production, 28_LVBus963802_production, 28_LVBus963803_consumption, 28_LVBus963803_production, 28_LVBus963804_production, 28_LVBus963805_consumption, 28_LVBus963805_production, 28_LVBus963806_production, 28_LVBus964423_production, 28_LVBus964469_production, 28_LVBus964470_production, 28_LVBus964471_production, 28_LVBus964472_consumption, 28_LVBus964472_production, 28_LVBus964473_production, 28_LVBus965483_production, 28_LVBus965484_production, 28_LVBus965485_production, 28_LVBus965486_consumption, 28_LVBus965486_production, 28_LVBus965487_production, 28_LVBus965488_production, 28_LVBus965489_production, 28_LVBus968554_production, 28_LVBus968666_production, 28_LVBus968667_production, 28_LVBus968668_production, 28_LVBus968669_production, 28_LVBus972364_production, 28_LVBus972365_production, 28_LVBus972586_production, 28_LVBus972587_consumption, 28_LVBus972587_production, 28_LVBus972588_production, 28_LVBus973767_production, 28_LVBus974195_consumption, 28_LVBus974195_production, 28_LVBus974196_production, 28_LVBus974197_production, 28_LVBus974198_production, 28_LVBus974199_production, 28_LVBus977171_consumption, 28_LVBus977171_production, 28_LVBus977172_production, 28_LVBus977173_production, 28_LVBus977174_consumption, 28_LVBus977174_production, 28_LVBus977175_production, 28_LVBus977372_production, 28_MVLV00656_consumption, 28_MVLV00656_production, 28_MVLV16181_consumption, 28_MVLV16181_production, 28_MVLV26619_consumption, 28_MVLV26619_production, 28_MVLV30592_consumption, 28_MVLV30592_production, 28_MVLV34347_consumption, 28_MVLV34347_production, 28_MVLV41018_consumption, 28_MVLV41018_production, 28_MVLV43797_consumption, 28_MVLV43797_production, 28_MVLV43802_consumption, 28_MVLV43802_production, 28_MVLV52958_consumption, 28_MVLV52958_production, 28_MVLV72679_consumption, 28_MVLV72679_production, 28_MVLV79313_consumption, 28_MVLV79313_production.

## 9. Data Quality Summary

**Total findings:** 530 (0 errors, 5 warnings, 525 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  892 of 1430 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.73 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  893 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962170_consumption`  
  Load '28_LVBus962170_consumption' has phase imbalance of 250.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182367_consumption`  
  Load '28_LVBus182367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181962_consumption`  
  Load '28_LVBus181962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181917_consumption`  
  Load '28_LVBus181917_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182372_consumption`  
  Load '28_LVBus182372_consumption' has phase imbalance of 38.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884445_consumption`  
  Load '28_LVBus884445_consumption' has phase imbalance of 36.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182227_consumption`  
  Load '28_LVBus182227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181725_consumption`  
  Load '28_LVBus181725_consumption' has phase imbalance of 99.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182048_consumption`  
  Load '28_LVBus182048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181894_consumption`  
  Load '28_LVBus181894_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus963804_consumption`  
  Load '28_LVBus963804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus968668_consumption`  
  Load '28_LVBus968668_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182194_consumption`  
  Load '28_LVBus182194_consumption' has phase imbalance of 139.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus895805_consumption`  
  Load '28_LVBus895805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181997_consumption`  
  Load '28_LVBus181997_consumption' has phase imbalance of 135.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957880_consumption`  
  Load '28_LVBus957880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182377_consumption`  
  Load '28_LVBus182377_consumption' has phase imbalance of 147.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181806_consumption`  
  Load '28_LVBus181806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181981_consumption`  
  Load '28_LVBus181981_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182257_consumption`  
  Load '28_LVBus182257_consumption' has phase imbalance of 85.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182362_consumption`  
  Load '28_LVBus182362_consumption' has phase imbalance of 197.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946718_consumption`  
  Load '28_LVBus946718_consumption' has phase imbalance of 75.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus867218_consumption`  
  Load '28_LVBus867218_consumption' has phase imbalance of 274.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181852_consumption`  
  Load '28_LVBus181852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus968667_consumption`  
  Load '28_LVBus968667_consumption' has phase imbalance of 221.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus925033_consumption`  
  Load '28_LVBus925033_consumption' has phase imbalance of 210.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948994_consumption`  
  Load '28_LVBus948994_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus942769_consumption`  
  Load '28_LVBus942769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182251_consumption`  
  Load '28_LVBus182251_consumption' has phase imbalance of 295.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus895806_consumption`  
  Load '28_LVBus895806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181705_consumption`  
  Load '28_LVBus181705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182343_consumption`  
  Load '28_LVBus182343_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181726_consumption`  
  Load '28_LVBus181726_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182136_consumption`  
  Load '28_LVBus182136_consumption' has phase imbalance of 174.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957075_consumption`  
  Load '28_LVBus957075_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus868903_consumption`  
  Load '28_LVBus868903_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181683_consumption`  
  Load '28_LVBus181683_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181989_consumption`  
  Load '28_LVBus181989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181899_consumption`  
  Load '28_LVBus181899_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182333_consumption`  
  Load '28_LVBus182333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182312_consumption`  
  Load '28_LVBus182312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181819_consumption`  
  Load '28_LVBus181819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182281_consumption`  
  Load '28_LVBus182281_consumption' has phase imbalance of 284.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182160_consumption`  
  Load '28_LVBus182160_consumption' has phase imbalance of 274.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181691_consumption`  
  Load '28_LVBus181691_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182079_consumption`  
  Load '28_LVBus182079_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181707_consumption`  
  Load '28_LVBus181707_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus856498_consumption`  
  Load '28_LVBus856498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181747_consumption`  
  Load '28_LVBus181747_consumption' has phase imbalance of 255.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181919_consumption`  
  Load '28_LVBus181919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182373_consumption`  
  Load '28_LVBus182373_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182219_consumption`  
  Load '28_LVBus182219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912064_consumption`  
  Load '28_LVBus912064_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181745_consumption`  
  Load '28_LVBus181745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181813_consumption`  
  Load '28_LVBus181813_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182166_consumption`  
  Load '28_LVBus182166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182180_consumption`  
  Load '28_LVBus182180_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182001_consumption`  
  Load '28_LVBus182001_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus926431_consumption`  
  Load '28_LVBus926431_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182366_consumption`  
  Load '28_LVBus182366_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946498_consumption`  
  Load '28_LVBus946498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus963806_consumption`  
  Load '28_LVBus963806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182157_consumption`  
  Load '28_LVBus182157_consumption' has phase imbalance of 198.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus955400_consumption`  
  Load '28_LVBus955400_consumption' has phase imbalance of 117.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182052_consumption`  
  Load '28_LVBus182052_consumption' has phase imbalance of 53.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181781_consumption`  
  Load '28_LVBus181781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182210_consumption`  
  Load '28_LVBus182210_consumption' has phase imbalance of 147.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182262_consumption`  
  Load '28_LVBus182262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181716_consumption`  
  Load '28_LVBus181716_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182058_consumption`  
  Load '28_LVBus182058_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181710_consumption`  
  Load '28_LVBus181710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182238_consumption`  
  Load '28_LVBus182238_consumption' has phase imbalance of 217.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182139_consumption`  
  Load '28_LVBus182139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182088_consumption`  
  Load '28_LVBus182088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182049_consumption`  
  Load '28_LVBus182049_consumption' has phase imbalance of 239.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965484_consumption`  
  Load '28_LVBus965484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182329_consumption`  
  Load '28_LVBus182329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182193_consumption`  
  Load '28_LVBus182193_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182297_consumption`  
  Load '28_LVBus182297_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181822_consumption`  
  Load '28_LVBus181822_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181700_consumption`  
  Load '28_LVBus181700_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182134_consumption`  
  Load '28_LVBus182134_consumption' has phase imbalance of 225.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182035_consumption`  
  Load '28_LVBus182035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182161_consumption`  
  Load '28_LVBus182161_consumption' has phase imbalance of 244.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus852560_consumption`  
  Load '28_LVBus852560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181769_consumption`  
  Load '28_LVBus181769_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181862_consumption`  
  Load '28_LVBus181862_consumption' has phase imbalance of 182.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus880315_consumption`  
  Load '28_LVBus880315_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182379_consumption`  
  Load '28_LVBus182379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182124_consumption`  
  Load '28_LVBus182124_consumption' has phase imbalance of 208.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965483_consumption`  
  Load '28_LVBus965483_consumption' has phase imbalance of 196.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181817_consumption`  
  Load '28_LVBus181817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182061_consumption`  
  Load '28_LVBus182061_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181875_consumption`  
  Load '28_LVBus181875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182337_consumption`  
  Load '28_LVBus182337_consumption' has phase imbalance of 218.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182192_consumption`  
  Load '28_LVBus182192_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181843_consumption`  
  Load '28_LVBus181843_consumption' has phase imbalance of 87.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962168_consumption`  
  Load '28_LVBus962168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182302_consumption`  
  Load '28_LVBus182302_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181906_consumption`  
  Load '28_LVBus181906_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182043_consumption`  
  Load '28_LVBus182043_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182215_consumption`  
  Load '28_LVBus182215_consumption' has phase imbalance of 220.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182320_consumption`  
  Load '28_LVBus182320_consumption' has phase imbalance of 275.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182273_consumption`  
  Load '28_LVBus182273_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181991_consumption`  
  Load '28_LVBus181991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181931_consumption`  
  Load '28_LVBus181931_consumption' has phase imbalance of 28.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182265_consumption`  
  Load '28_LVBus182265_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181696_consumption`  
  Load '28_LVBus181696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182071_consumption`  
  Load '28_LVBus182071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182142_consumption`  
  Load '28_LVBus182142_consumption' has phase imbalance of 250.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181832_consumption`  
  Load '28_LVBus181832_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964469_consumption`  
  Load '28_LVBus964469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182060_consumption`  
  Load '28_LVBus182060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182020_consumption`  
  Load '28_LVBus182020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181972_consumption`  
  Load '28_LVBus181972_consumption' has phase imbalance of 145.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181684_consumption`  
  Load '28_LVBus181684_consumption' has phase imbalance of 278.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957883_consumption`  
  Load '28_LVBus957883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901238_consumption`  
  Load '28_LVBus901238_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182252_consumption`  
  Load '28_LVBus182252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181821_consumption`  
  Load '28_LVBus181821_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182044_consumption`  
  Load '28_LVBus182044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912062_consumption`  
  Load '28_LVBus912062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182269_consumption`  
  Load '28_LVBus182269_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus973767_consumption`  
  Load '28_LVBus973767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182283_consumption`  
  Load '28_LVBus182283_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965485_consumption`  
  Load '28_LVBus965485_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948778_consumption`  
  Load '28_LVBus948778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182285_consumption`  
  Load '28_LVBus182285_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182218_consumption`  
  Load '28_LVBus182218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912063_consumption`  
  Load '28_LVBus912063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182010_consumption`  
  Load '28_LVBus182010_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182186_consumption`  
  Load '28_LVBus182186_consumption' has phase imbalance of 195.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181878_consumption`  
  Load '28_LVBus181878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948999_consumption`  
  Load '28_LVBus948999_consumption' has phase imbalance of 167.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181863_consumption`  
  Load '28_LVBus181863_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181936_consumption`  
  Load '28_LVBus181936_consumption' has phase imbalance of 137.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182311_consumption`  
  Load '28_LVBus182311_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182277_consumption`  
  Load '28_LVBus182277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181715_consumption`  
  Load '28_LVBus181715_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181701_consumption`  
  Load '28_LVBus181701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181985_consumption`  
  Load '28_LVBus181985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181934_consumption`  
  Load '28_LVBus181934_consumption' has phase imbalance of 261.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus852559_consumption`  
  Load '28_LVBus852559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946497_consumption`  
  Load '28_LVBus946497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181953_consumption`  
  Load '28_LVBus181953_consumption' has phase imbalance of 239.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182094_consumption`  
  Load '28_LVBus182094_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182326_consumption`  
  Load '28_LVBus182326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus974198_consumption`  
  Load '28_LVBus974198_consumption' has phase imbalance of 141.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181815_consumption`  
  Load '28_LVBus181815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus963801_consumption`  
  Load '28_LVBus963801_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182087_consumption`  
  Load '28_LVBus182087_consumption' has phase imbalance of 292.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948997_consumption`  
  Load '28_LVBus948997_consumption' has phase imbalance of 265.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182246_consumption`  
  Load '28_LVBus182246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182229_consumption`  
  Load '28_LVBus182229_consumption' has phase imbalance of 32.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182128_consumption`  
  Load '28_LVBus182128_consumption' has phase imbalance of 182.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182038_consumption`  
  Load '28_LVBus182038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182235_consumption`  
  Load '28_LVBus182235_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182296_consumption`  
  Load '28_LVBus182296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus925034_consumption`  
  Load '28_LVBus925034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947182_consumption`  
  Load '28_LVBus947182_consumption' has phase imbalance of 254.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181811_consumption`  
  Load '28_LVBus181811_consumption' has phase imbalance of 277.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus977372_consumption`  
  Load '28_LVBus977372_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182172_consumption`  
  Load '28_LVBus182172_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181748_consumption`  
  Load '28_LVBus181748_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181975_consumption`  
  Load '28_LVBus181975_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182034_consumption`  
  Load '28_LVBus182034_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181890_consumption`  
  Load '28_LVBus181890_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948995_consumption`  
  Load '28_LVBus948995_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962169_consumption`  
  Load '28_LVBus962169_consumption' has phase imbalance of 144.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus895807_consumption`  
  Load '28_LVBus895807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946499_consumption`  
  Load '28_LVBus946499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181980_consumption`  
  Load '28_LVBus181980_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182255_consumption`  
  Load '28_LVBus182255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182141_consumption`  
  Load '28_LVBus182141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182354_consumption`  
  Load '28_LVBus182354_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181831_consumption`  
  Load '28_LVBus181831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181743_consumption`  
  Load '28_LVBus181743_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181943_consumption`  
  Load '28_LVBus181943_consumption' has phase imbalance of 267.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965488_consumption`  
  Load '28_LVBus965488_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181861_consumption`  
  Load '28_LVBus181861_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181920_consumption`  
  Load '28_LVBus181920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181685_consumption`  
  Load '28_LVBus181685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181785_consumption`  
  Load '28_LVBus181785_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182125_consumption`  
  Load '28_LVBus182125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182254_consumption`  
  Load '28_LVBus182254_consumption' has phase imbalance of 125.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181930_consumption`  
  Load '28_LVBus181930_consumption' has phase imbalance of 288.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus972364_consumption`  
  Load '28_LVBus972364_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182059_consumption`  
  Load '28_LVBus182059_consumption' has phase imbalance of 191.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182324_consumption`  
  Load '28_LVBus182324_consumption' has phase imbalance of 33.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181865_consumption`  
  Load '28_LVBus181865_consumption' has phase imbalance of 146.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181746_consumption`  
  Load '28_LVBus181746_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181690_consumption`  
  Load '28_LVBus181690_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182315_consumption`  
  Load '28_LVBus182315_consumption' has phase imbalance of 224.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus955402_consumption`  
  Load '28_LVBus955402_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus903773_consumption`  
  Load '28_LVBus903773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus960379_consumption`  
  Load '28_LVBus960379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182011_consumption`  
  Load '28_LVBus182011_consumption' has phase imbalance of 133.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182268_consumption`  
  Load '28_LVBus182268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182258_consumption`  
  Load '28_LVBus182258_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus977175_consumption`  
  Load '28_LVBus977175_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181771_consumption`  
  Load '28_LVBus181771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181783_consumption`  
  Load '28_LVBus181783_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182274_consumption`  
  Load '28_LVBus182274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182319_consumption`  
  Load '28_LVBus182319_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181856_consumption`  
  Load '28_LVBus181856_consumption' has phase imbalance of 244.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus963798_consumption`  
  Load '28_LVBus963798_consumption' has phase imbalance of 254.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181827_consumption`  
  Load '28_LVBus181827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182108_consumption`  
  Load '28_LVBus182108_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus880316_consumption`  
  Load '28_LVBus880316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181694_consumption`  
  Load '28_LVBus181694_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182096_consumption`  
  Load '28_LVBus182096_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus974197_consumption`  
  Load '28_LVBus974197_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181915_consumption`  
  Load '28_LVBus181915_consumption' has phase imbalance of 157.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182146_consumption`  
  Load '28_LVBus182146_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182017_consumption`  
  Load '28_LVBus182017_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182259_consumption`  
  Load '28_LVBus182259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181949_consumption`  
  Load '28_LVBus181949_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946790_consumption`  
  Load '28_LVBus946790_consumption' has phase imbalance of 158.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181764_consumption`  
  Load '28_LVBus181764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182123_consumption`  
  Load '28_LVBus182123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912817_consumption`  
  Load '28_LVBus912817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181912_consumption`  
  Load '28_LVBus181912_consumption' has phase imbalance of 125.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181927_consumption`  
  Load '28_LVBus181927_consumption' has phase imbalance of 273.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181965_consumption`  
  Load '28_LVBus181965_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181770_consumption`  
  Load '28_LVBus181770_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182092_consumption`  
  Load '28_LVBus182092_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182170_consumption`  
  Load '28_LVBus182170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964470_consumption`  
  Load '28_LVBus964470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182016_consumption`  
  Load '28_LVBus182016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181814_consumption`  
  Load '28_LVBus181814_consumption' has phase imbalance of 64.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus977173_consumption`  
  Load '28_LVBus977173_consumption' has phase imbalance of 225.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182039_consumption`  
  Load '28_LVBus182039_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181946_consumption`  
  Load '28_LVBus181946_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus856496_consumption`  
  Load '28_LVBus856496_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182332_consumption`  
  Load '28_LVBus182332_consumption' has phase imbalance of 241.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962172_consumption`  
  Load '28_LVBus962172_consumption' has phase imbalance of 242.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus860858_consumption`  
  Load '28_LVBus860858_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus974199_consumption`  
  Load '28_LVBus974199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182348_consumption`  
  Load '28_LVBus182348_consumption' has phase imbalance of 204.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182126_consumption`  
  Load '28_LVBus182126_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182208_consumption`  
  Load '28_LVBus182208_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181772_consumption`  
  Load '28_LVBus181772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181766_consumption`  
  Load '28_LVBus181766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181733_consumption`  
  Load '28_LVBus181733_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182291_consumption`  
  Load '28_LVBus182291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182015_consumption`  
  Load '28_LVBus182015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182280_consumption`  
  Load '28_LVBus182280_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181759_consumption`  
  Load '28_LVBus181759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181957_consumption`  
  Load '28_LVBus181957_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181807_consumption`  
  Load '28_LVBus181807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181893_consumption`  
  Load '28_LVBus181893_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182140_consumption`  
  Load '28_LVBus182140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182340_consumption`  
  Load '28_LVBus182340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182063_consumption`  
  Load '28_LVBus182063_consumption' has phase imbalance of 210.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181721_consumption`  
  Load '28_LVBus181721_consumption' has phase imbalance of 103.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182288_consumption`  
  Load '28_LVBus182288_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957884_consumption`  
  Load '28_LVBus957884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182267_consumption`  
  Load '28_LVBus182267_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181892_consumption`  
  Load '28_LVBus181892_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181921_consumption`  
  Load '28_LVBus181921_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181693_consumption`  
  Load '28_LVBus181693_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus868901_consumption`  
  Load '28_LVBus868901_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181782_consumption`  
  Load '28_LVBus181782_consumption' has phase imbalance of 140.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182374_consumption`  
  Load '28_LVBus182374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182344_consumption`  
  Load '28_LVBus182344_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181926_consumption`  
  Load '28_LVBus181926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus968554_consumption`  
  Load '28_LVBus968554_consumption' has phase imbalance of 200.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182042_consumption`  
  Load '28_LVBus182042_consumption' has phase imbalance of 258.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus868902_consumption`  
  Load '28_LVBus868902_consumption' has phase imbalance of 233.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181918_consumption`  
  Load '28_LVBus181918_consumption' has phase imbalance of 73.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182222_consumption`  
  Load '28_LVBus182222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus939655_consumption`  
  Load '28_LVBus939655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182177_consumption`  
  Load '28_LVBus182177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912065_consumption`  
  Load '28_LVBus912065_consumption' has phase imbalance of 24.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957074_consumption`  
  Load '28_LVBus957074_consumption' has phase imbalance of 65.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181944_consumption`  
  Load '28_LVBus181944_consumption' has phase imbalance of 287.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182028_consumption`  
  Load '28_LVBus182028_consumption' has phase imbalance of 41.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946919_consumption`  
  Load '28_LVBus946919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181777_consumption`  
  Load '28_LVBus181777_consumption' has phase imbalance of 146.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882132_consumption`  
  Load '28_LVBus882132_consumption' has phase imbalance of 260.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946787_consumption`  
  Load '28_LVBus946787_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181829_consumption`  
  Load '28_LVBus181829_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182159_consumption`  
  Load '28_LVBus182159_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus963802_consumption`  
  Load '28_LVBus963802_consumption' has phase imbalance of 288.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181750_consumption`  
  Load '28_LVBus181750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181723_consumption`  
  Load '28_LVBus181723_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181699_consumption`  
  Load '28_LVBus181699_consumption' has phase imbalance of 272.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181826_consumption`  
  Load '28_LVBus181826_consumption' has phase imbalance of 204.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182290_consumption`  
  Load '28_LVBus182290_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182349_consumption`  
  Load '28_LVBus182349_consumption' has phase imbalance of 185.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181935_consumption`  
  Load '28_LVBus181935_consumption' has phase imbalance of 84.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181970_consumption`  
  Load '28_LVBus181970_consumption' has phase imbalance of 34.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957882_consumption`  
  Load '28_LVBus957882_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182027_consumption`  
  Load '28_LVBus182027_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181879_consumption`  
  Load '28_LVBus181879_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181698_consumption`  
  Load '28_LVBus181698_consumption' has phase imbalance of 21.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181709_consumption`  
  Load '28_LVBus181709_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181719_consumption`  
  Load '28_LVBus181719_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182338_consumption`  
  Load '28_LVBus182338_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182223_consumption`  
  Load '28_LVBus182223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182144_consumption`  
  Load '28_LVBus182144_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus963796_consumption`  
  Load '28_LVBus963796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181779_consumption`  
  Load '28_LVBus181779_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182122_consumption`  
  Load '28_LVBus182122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181960_consumption`  
  Load '28_LVBus181960_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181704_consumption`  
  Load '28_LVBus181704_consumption' has phase imbalance of 214.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182239_consumption`  
  Load '28_LVBus182239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181773_consumption`  
  Load '28_LVBus181773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182382_consumption`  
  Load '28_LVBus182382_consumption' has phase imbalance of 163.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181848_consumption`  
  Load '28_LVBus181848_consumption' has phase imbalance of 191.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181797_consumption`  
  Load '28_LVBus181797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus974196_consumption`  
  Load '28_LVBus974196_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181728_consumption`  
  Load '28_LVBus181728_consumption' has phase imbalance of 260.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182335_consumption`  
  Load '28_LVBus182335_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965487_consumption`  
  Load '28_LVBus965487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181737_consumption`  
  Load '28_LVBus181737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus977172_consumption`  
  Load '28_LVBus977172_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus968669_consumption`  
  Load '28_LVBus968669_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181968_consumption`  
  Load '28_LVBus181968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181808_consumption`  
  Load '28_LVBus181808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181732_consumption`  
  Load '28_LVBus181732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus852557_consumption`  
  Load '28_LVBus852557_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182232_consumption`  
  Load '28_LVBus182232_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964471_consumption`  
  Load '28_LVBus964471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182007_consumption`  
  Load '28_LVBus182007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181867_consumption`  
  Load '28_LVBus181867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182276_consumption`  
  Load '28_LVBus182276_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182120_consumption`  
  Load '28_LVBus182120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182206_consumption`  
  Load '28_LVBus182206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182187_consumption`  
  Load '28_LVBus182187_consumption' has phase imbalance of 253.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182005_consumption`  
  Load '28_LVBus182005_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181902_consumption`  
  Load '28_LVBus181902_consumption' has phase imbalance of 20.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181937_consumption`  
  Load '28_LVBus181937_consumption' has phase imbalance of 183.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182148_consumption`  
  Load '28_LVBus182148_consumption' has phase imbalance of 201.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181876_consumption`  
  Load '28_LVBus181876_consumption' has phase imbalance of 269.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947301_consumption`  
  Load '28_LVBus947301_consumption' has phase imbalance of 212.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181845_consumption`  
  Load '28_LVBus181845_consumption' has phase imbalance of 185.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182003_consumption`  
  Load '28_LVBus182003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182361_consumption`  
  Load '28_LVBus182361_consumption' has phase imbalance of 139.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182292_consumption`  
  Load '28_LVBus182292_consumption' has phase imbalance of 274.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181866_consumption`  
  Load '28_LVBus181866_consumption' has phase imbalance of 266.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182314_consumption`  
  Load '28_LVBus182314_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus872015_consumption`  
  Load '28_LVBus872015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949000_consumption`  
  Load '28_LVBus949000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182384_consumption`  
  Load '28_LVBus182384_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181818_consumption`  
  Load '28_LVBus181818_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus895717_consumption`  
  Load '28_LVBus895717_consumption' has phase imbalance of 260.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181966_consumption`  
  Load '28_LVBus181966_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182284_consumption`  
  Load '28_LVBus182284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182084_consumption`  
  Load '28_LVBus182084_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181954_consumption`  
  Load '28_LVBus181954_consumption' has phase imbalance of 82.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182355_consumption`  
  Load '28_LVBus182355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181840_consumption`  
  Load '28_LVBus181840_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182138_consumption`  
  Load '28_LVBus182138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182022_consumption`  
  Load '28_LVBus182022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182272_consumption`  
  Load '28_LVBus182272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181974_consumption`  
  Load '28_LVBus181974_consumption' has phase imbalance of 109.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962173_consumption`  
  Load '28_LVBus962173_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182347_consumption`  
  Load '28_LVBus182347_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182323_consumption`  
  Load '28_LVBus182323_consumption' has phase imbalance of 129.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946719_consumption`  
  Load '28_LVBus946719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182081_consumption`  
  Load '28_LVBus182081_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962174_consumption`  
  Load '28_LVBus962174_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182353_consumption`  
  Load '28_LVBus182353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182151_consumption`  
  Load '28_LVBus182151_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182201_consumption`  
  Load '28_LVBus182201_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181977_consumption`  
  Load '28_LVBus181977_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181823_consumption`  
  Load '28_LVBus181823_consumption' has phase imbalance of 118.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182000_consumption`  
  Load '28_LVBus182000_consumption' has phase imbalance of 178.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181692_consumption`  
  Load '28_LVBus181692_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182359_consumption`  
  Load '28_LVBus182359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus873791_consumption`  
  Load '28_LVBus873791_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181864_consumption`  
  Load '28_LVBus181864_consumption' has phase imbalance of 64.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182380_consumption`  
  Load '28_LVBus182380_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947200_consumption`  
  Load '28_LVBus947200_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181791_consumption`  
  Load '28_LVBus181791_consumption' has phase imbalance of 86.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182298_consumption`  
  Load '28_LVBus182298_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus968666_consumption`  
  Load '28_LVBus968666_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182205_consumption`  
  Load '28_LVBus182205_consumption' has phase imbalance of 57.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182118_consumption`  
  Load '28_LVBus182118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948996_consumption`  
  Load '28_LVBus948996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182345_consumption`  
  Load '28_LVBus182345_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181999_consumption`  
  Load '28_LVBus181999_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181945_consumption`  
  Load '28_LVBus181945_consumption' has phase imbalance of 262.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182275_consumption`  
  Load '28_LVBus182275_consumption' has phase imbalance of 186.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181933_consumption`  
  Load '28_LVBus181933_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus873052_consumption`  
  Load '28_LVBus873052_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947181_consumption`  
  Load '28_LVBus947181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182342_consumption`  
  Load '28_LVBus182342_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181796_consumption`  
  Load '28_LVBus181796_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182237_consumption`  
  Load '28_LVBus182237_consumption' has phase imbalance of 255.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182024_consumption`  
  Load '28_LVBus182024_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182231_consumption`  
  Load '28_LVBus182231_consumption' has phase imbalance of 205.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181853_consumption`  
  Load '28_LVBus181853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181720_consumption`  
  Load '28_LVBus181720_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182330_consumption`  
  Load '28_LVBus182330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182386_consumption`  
  Load '28_LVBus182386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181956_consumption`  
  Load '28_LVBus181956_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181729_consumption`  
  Load '28_LVBus181729_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182013_consumption`  
  Load '28_LVBus182013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181799_consumption`  
  Load '28_LVBus181799_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus904328_consumption`  
  Load '28_LVBus904328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182305_consumption`  
  Load '28_LVBus182305_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181947_consumption`  
  Load '28_LVBus181947_consumption' has phase imbalance of 261.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182012_consumption`  
  Load '28_LVBus182012_consumption' has phase imbalance of 87.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962175_consumption`  
  Load '28_LVBus962175_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus856497_consumption`  
  Load '28_LVBus856497_consumption' has phase imbalance of 249.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus942768_consumption`  
  Load '28_LVBus942768_consumption' has phase imbalance of 39.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181939_consumption`  
  Load '28_LVBus181939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182056_consumption`  
  Load '28_LVBus182056_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182233_consumption`  
  Load '28_LVBus182233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182244_consumption`  
  Load '28_LVBus182244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181722_consumption`  
  Load '28_LVBus181722_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182225_consumption`  
  Load '28_LVBus182225_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182006_consumption`  
  Load '28_LVBus182006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182095_consumption`  
  Load '28_LVBus182095_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182133_consumption`  
  Load '28_LVBus182133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181924_consumption`  
  Load '28_LVBus181924_consumption' has phase imbalance of 238.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181979_consumption`  
  Load '28_LVBus181979_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181940_consumption`  
  Load '28_LVBus181940_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182195_consumption`  
  Load '28_LVBus182195_consumption' has phase imbalance of 136.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181760_consumption`  
  Load '28_LVBus181760_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182376_consumption`  
  Load '28_LVBus182376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181901_consumption`  
  Load '28_LVBus181901_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182351_consumption`  
  Load '28_LVBus182351_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182093_consumption`  
  Load '28_LVBus182093_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182080_consumption`  
  Load '28_LVBus182080_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182318_consumption`  
  Load '28_LVBus182318_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181872_consumption`  
  Load '28_LVBus181872_consumption' has phase imbalance of 246.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus927456_consumption`  
  Load '28_LVBus927456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181958_consumption`  
  Load '28_LVBus181958_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182188_consumption`  
  Load '28_LVBus182188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182121_consumption`  
  Load '28_LVBus182121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182202_consumption`  
  Load '28_LVBus182202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus856056_consumption`  
  Load '28_LVBus856056_consumption' has phase imbalance of 196.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182364_consumption`  
  Load '28_LVBus182364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181752_consumption`  
  Load '28_LVBus181752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964473_consumption`  
  Load '28_LVBus964473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181928_consumption`  
  Load '28_LVBus181928_consumption' has phase imbalance of 231.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182241_consumption`  
  Load '28_LVBus182241_consumption' has phase imbalance of 147.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182217_consumption`  
  Load '28_LVBus182217_consumption' has phase imbalance of 36.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus867220_consumption`  
  Load '28_LVBus867220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181753_consumption`  
  Load '28_LVBus181753_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181846_consumption`  
  Load '28_LVBus181846_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964423_consumption`  
  Load '28_LVBus964423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182129_consumption`  
  Load '28_LVBus182129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182190_consumption`  
  Load '28_LVBus182190_consumption' has phase imbalance of 176.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182065_consumption`  
  Load '28_LVBus182065_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912816_consumption`  
  Load '28_LVBus912816_consumption' has phase imbalance of 139.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus929721_consumption`  
  Load '28_LVBus929721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181801_consumption`  
  Load '28_LVBus181801_consumption' has phase imbalance of 74.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181889_consumption`  
  Load '28_LVBus181889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181798_consumption`  
  Load '28_LVBus181798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182236_consumption`  
  Load '28_LVBus182236_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182278_consumption`  
  Load '28_LVBus182278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus856499_consumption`  
  Load '28_LVBus856499_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181738_consumption`  
  Load '28_LVBus181738_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181787_consumption`  
  Load '28_LVBus181787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948780_consumption`  
  Load '28_LVBus948780_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181795_consumption`  
  Load '28_LVBus181795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182346_consumption`  
  Load '28_LVBus182346_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181849_consumption`  
  Load '28_LVBus181849_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182089_consumption`  
  Load '28_LVBus182089_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus972586_consumption`  
  Load '28_LVBus972586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus852606_consumption`  
  Load '28_LVBus852606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182350_consumption`  
  Load '28_LVBus182350_consumption' has phase imbalance of 67.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182336_consumption`  
  Load '28_LVBus182336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181870_consumption`  
  Load '28_LVBus181870_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947300_consumption`  
  Load '28_LVBus947300_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181731_consumption`  
  Load '28_LVBus181731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182033_consumption`  
  Load '28_LVBus182033_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181702_consumption`  
  Load '28_LVBus181702_consumption' has phase imbalance of 278.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus859955_consumption`  
  Load '28_LVBus859955_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181925_consumption`  
  Load '28_LVBus181925_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181837_consumption`  
  Load '28_LVBus181837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181744_consumption`  
  Load '28_LVBus181744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181984_consumption`  
  Load '28_LVBus181984_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182057_consumption`  
  Load '28_LVBus182057_consumption' has phase imbalance of 214.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181686_consumption`  
  Load '28_LVBus181686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182018_consumption`  
  Load '28_LVBus182018_consumption' has phase imbalance of 131.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181995_consumption`  
  Load '28_LVBus181995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181809_consumption`  
  Load '28_LVBus181809_consumption' has phase imbalance of 213.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181824_consumption`  
  Load '28_LVBus181824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181955_consumption`  
  Load '28_LVBus181955_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965489_consumption`  
  Load '28_LVBus965489_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus873704_consumption`  
  Load '28_LVBus873704_consumption' has phase imbalance of 168.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182106_consumption`  
  Load '28_LVBus182106_consumption' has phase imbalance of 156.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181756_consumption`  
  Load '28_LVBus181756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182250_consumption`  
  Load '28_LVBus182250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181952_consumption`  
  Load '28_LVBus181952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus892920_consumption`  
  Load '28_LVBus892920_consumption' has phase imbalance of 213.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181703_consumption`  
  Load '28_LVBus181703_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182294_consumption`  
  Load '28_LVBus182294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182248_consumption`  
  Load '28_LVBus182248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182289_consumption`  
  Load '28_LVBus182289_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181941_consumption`  
  Load '28_LVBus181941_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182099_consumption`  
  Load '28_LVBus182099_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181717_consumption`  
  Load '28_LVBus181717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946496_consumption`  
  Load '28_LVBus946496_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus972365_consumption`  
  Load '28_LVBus972365_consumption' has phase imbalance of 85.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182077_consumption`  
  Load '28_LVBus182077_consumption' has phase imbalance of 267.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182381_consumption`  
  Load '28_LVBus182381_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182211_consumption`  
  Load '28_LVBus182211_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948998_consumption`  
  Load '28_LVBus948998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181932_consumption`  
  Load '28_LVBus181932_consumption' has phase imbalance of 101.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181736_consumption`  
  Load '28_LVBus181736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus903774_consumption`  
  Load '28_LVBus903774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus182213_consumption`  
  Load '28_LVBus182213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus181914_consumption`  
  Load '28_LVBus181914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1430 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '28_HARCA' (MV, 11.78 kV) has an electrical reach of 21.26 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  949 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  387 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus181684_consumption, 28_LVBus181685_consumption, 28_LVBus181686_consumption, 28_LVBus181690_consumption, 28_LVBus181691_consumption, 28_LVBus181692_consumption, 28_LVBus181694_consumption, 28_LVBus181696_consumption, 28_LVBus181699_consumption, 28_LVBus181700_consumption, 28_LVBus181701_consumption, 28_LVBus181702_consumption, 28_LVBus181703_consumption, 28_LVBus181704_consumption, 28_LVBus181705_consumption, 28_LVBus181707_consumption, 28_LVBus181709_consumption, 28_LVBus181710_consumption, 28_LVBus181715_consumption, 28_LVBus181716_consumption, 28_LVBus181717_consumption, 28_LVBus181720_consumption, 28_LVBus181722_consumption, 28_LVBus181723_consumption, 28_LVBus181726_consumption, 28_LVBus181728_consumption, 28_LVBus181729_consumption, 28_LVBus181731_consumption, 28_LVBus181732_consumption, 28_LVBus181733_consumption, 28_LVBus181736_consumption, 28_LVBus181737_consumption, 28_LVBus181743_consumption, 28_LVBus181744_consumption, 28_LVBus181745_consumption, 28_LVBus181746_consumption, 28_LVBus181750_consumption, 28_LVBus181752_consumption, 28_LVBus181756_consumption, 28_LVBus181759_consumption, 28_LVBus181760_consumption, 28_LVBus181764_consumption, 28_LVBus181766_consumption, 28_LVBus181769_consumption, 28_LVBus181770_consumption, 28_LVBus181771_consumption, 28_LVBus181772_consumption, 28_LVBus181773_consumption, 28_LVBus181781_consumption, 28_LVBus181783_consumption, 28_LVBus181785_consumption, 28_LVBus181787_consumption, 28_LVBus181795_consumption, 28_LVBus181796_consumption, 28_LVBus181797_consumption, 28_LVBus181798_consumption, 28_LVBus181799_consumption, 28_LVBus181806_consumption, 28_LVBus181807_consumption, 28_LVBus181808_consumption, 28_LVBus181809_consumption, 28_LVBus181811_consumption, 28_LVBus181815_consumption, 28_LVBus181817_consumption, 28_LVBus181818_consumption, 28_LVBus181819_consumption, 28_LVBus181822_consumption, 28_LVBus181824_consumption, 28_LVBus181826_consumption, 28_LVBus181827_consumption, 28_LVBus181829_consumption, 28_LVBus181831_consumption, 28_LVBus181837_consumption, 28_LVBus181840_consumption, 28_LVBus181846_consumption, 28_LVBus181852_consumption, 28_LVBus181853_consumption, 28_LVBus181863_consumption, 28_LVBus181867_consumption, 28_LVBus181870_consumption, 28_LVBus181875_consumption, 28_LVBus181876_consumption, 28_LVBus181878_consumption, 28_LVBus181889_consumption, 28_LVBus181892_consumption, 28_LVBus181893_consumption, 28_LVBus181894_consumption, 28_LVBus181899_consumption, 28_LVBus181901_consumption, 28_LVBus181906_consumption, 28_LVBus181914_consumption, 28_LVBus181915_consumption, 28_LVBus181917_consumption, 28_LVBus181919_consumption, 28_LVBus181920_consumption, 28_LVBus181921_consumption, 28_LVBus181924_consumption, 28_LVBus181925_consumption, 28_LVBus181926_consumption, 28_LVBus181927_consumption, 28_LVBus181928_consumption, 28_LVBus181934_consumption, 28_LVBus181939_consumption, 28_LVBus181940_consumption, 28_LVBus181941_consumption, 28_LVBus181943_consumption, 28_LVBus181944_consumption, 28_LVBus181946_consumption, 28_LVBus181947_consumption, 28_LVBus181949_consumption, 28_LVBus181952_consumption, 28_LVBus181953_consumption, 28_LVBus181955_consumption, 28_LVBus181956_consumption, 28_LVBus181958_consumption, 28_LVBus181960_consumption, 28_LVBus181962_consumption, 28_LVBus181968_consumption, 28_LVBus181975_consumption, 28_LVBus181977_consumption, 28_LVBus181979_consumption, 28_LVBus181981_consumption, 28_LVBus181984_consumption, 28_LVBus181985_consumption, 28_LVBus181989_consumption, 28_LVBus181991_consumption, 28_LVBus181995_consumption, 28_LVBus181999_consumption, 28_LVBus182000_consumption, 28_LVBus182001_consumption, 28_LVBus182003_consumption, 28_LVBus182006_consumption, 28_LVBus182007_consumption, 28_LVBus182010_consumption, 28_LVBus182013_consumption, 28_LVBus182015_consumption, 28_LVBus182016_consumption, 28_LVBus182020_consumption, 28_LVBus182022_consumption, 28_LVBus182027_consumption, 28_LVBus182034_consumption, 28_LVBus182035_consumption, 28_LVBus182038_consumption, 28_LVBus182039_consumption, 28_LVBus182042_consumption, 28_LVBus182044_consumption, 28_LVBus182048_consumption, 28_LVBus182049_consumption, 28_LVBus182057_consumption, 28_LVBus182058_consumption, 28_LVBus182059_consumption, 28_LVBus182060_consumption, 28_LVBus182061_consumption, 28_LVBus182065_consumption, 28_LVBus182071_consumption, 28_LVBus182077_consumption, 28_LVBus182079_consumption, 28_LVBus182084_consumption, 28_LVBus182087_consumption, 28_LVBus182088_consumption, 28_LVBus182089_consumption, 28_LVBus182092_consumption, 28_LVBus182093_consumption, 28_LVBus182094_consumption, 28_LVBus182095_consumption, 28_LVBus182096_consumption, 28_LVBus182099_consumption, 28_LVBus182108_consumption, 28_LVBus182118_consumption, 28_LVBus182120_consumption, 28_LVBus182121_consumption, 28_LVBus182122_consumption, 28_LVBus182123_consumption, 28_LVBus182124_consumption, 28_LVBus182125_consumption, 28_LVBus182126_consumption, 28_LVBus182129_consumption, 28_LVBus182133_consumption, 28_LVBus182134_consumption, 28_LVBus182136_consumption, 28_LVBus182138_consumption, 28_LVBus182139_consumption, 28_LVBus182140_consumption, 28_LVBus182141_consumption, 28_LVBus182142_consumption, 28_LVBus182146_consumption, 28_LVBus182148_consumption, 28_LVBus182151_consumption, 28_LVBus182159_consumption, 28_LVBus182160_consumption, 28_LVBus182161_consumption, 28_LVBus182166_consumption, 28_LVBus182170_consumption, 28_LVBus182177_consumption, 28_LVBus182186_consumption, 28_LVBus182187_consumption, 28_LVBus182188_consumption, 28_LVBus182190_consumption, 28_LVBus182192_consumption, 28_LVBus182193_consumption, 28_LVBus182202_consumption, 28_LVBus182206_consumption, 28_LVBus182208_consumption, 28_LVBus182211_consumption, 28_LVBus182213_consumption, 28_LVBus182215_consumption, 28_LVBus182218_consumption, 28_LVBus182219_consumption, 28_LVBus182222_consumption, 28_LVBus182223_consumption, 28_LVBus182225_consumption, 28_LVBus182227_consumption, 28_LVBus182233_consumption, 28_LVBus182235_consumption, 28_LVBus182236_consumption, 28_LVBus182237_consumption, 28_LVBus182238_consumption, 28_LVBus182239_consumption, 28_LVBus182244_consumption, 28_LVBus182246_consumption, 28_LVBus182248_consumption, 28_LVBus182250_consumption, 28_LVBus182251_consumption, 28_LVBus182252_consumption, 28_LVBus182255_consumption, 28_LVBus182258_consumption, 28_LVBus182259_consumption, 28_LVBus182262_consumption, 28_LVBus182265_consumption, 28_LVBus182267_consumption, 28_LVBus182268_consumption, 28_LVBus182272_consumption, 28_LVBus182273_consumption, 28_LVBus182274_consumption, 28_LVBus182275_consumption, 28_LVBus182276_consumption, 28_LVBus182277_consumption, 28_LVBus182278_consumption, 28_LVBus182280_consumption, 28_LVBus182283_consumption, 28_LVBus182284_consumption, 28_LVBus182288_consumption, 28_LVBus182290_consumption, 28_LVBus182291_consumption, 28_LVBus182294_consumption, 28_LVBus182296_consumption, 28_LVBus182297_consumption, 28_LVBus182302_consumption, 28_LVBus182311_consumption, 28_LVBus182312_consumption, 28_LVBus182314_consumption, 28_LVBus182315_consumption, 28_LVBus182318_consumption, 28_LVBus182319_consumption, 28_LVBus182320_consumption, 28_LVBus182326_consumption, 28_LVBus182329_consumption, 28_LVBus182330_consumption, 28_LVBus182333_consumption, 28_LVBus182336_consumption, 28_LVBus182337_consumption, 28_LVBus182338_consumption, 28_LVBus182340_consumption, 28_LVBus182343_consumption, 28_LVBus182345_consumption, 28_LVBus182347_consumption, 28_LVBus182349_consumption, 28_LVBus182351_consumption, 28_LVBus182353_consumption, 28_LVBus182354_consumption, 28_LVBus182355_consumption, 28_LVBus182359_consumption, 28_LVBus182362_consumption, 28_LVBus182364_consumption, 28_LVBus182366_consumption, 28_LVBus182367_consumption, 28_LVBus182373_consumption, 28_LVBus182374_consumption, 28_LVBus182376_consumption, 28_LVBus182379_consumption, 28_LVBus182380_consumption, 28_LVBus182381_consumption, 28_LVBus182382_consumption, 28_LVBus182384_consumption, 28_LVBus182386_consumption, 28_LVBus852557_consumption, 28_LVBus852559_consumption, 28_LVBus852560_consumption, 28_LVBus852606_consumption, 28_LVBus856056_consumption, 28_LVBus856497_consumption, 28_LVBus856498_consumption, 28_LVBus860858_consumption, 28_LVBus867218_consumption, 28_LVBus867220_consumption, 28_LVBus868901_consumption, 28_LVBus868902_consumption, 28_LVBus868903_consumption, 28_LVBus872015_consumption, 28_LVBus873052_consumption, 28_LVBus873704_consumption, 28_LVBus873791_consumption, 28_LVBus880315_consumption, 28_LVBus880316_consumption, 28_LVBus892920_consumption, 28_LVBus895717_consumption, 28_LVBus895805_consumption, 28_LVBus895806_consumption, 28_LVBus895807_consumption, 28_LVBus901238_consumption, 28_LVBus903773_consumption, 28_LVBus903774_consumption, 28_LVBus904328_consumption, 28_LVBus912062_consumption, 28_LVBus912063_consumption, 28_LVBus912064_consumption, 28_LVBus912817_consumption, 28_LVBus925033_consumption, 28_LVBus925034_consumption, 28_LVBus926431_consumption, 28_LVBus927456_consumption, 28_LVBus929721_consumption, 28_LVBus939655_consumption, 28_LVBus942769_consumption, 28_LVBus946496_consumption, 28_LVBus946497_consumption, 28_LVBus946498_consumption, 28_LVBus946499_consumption, 28_LVBus946719_consumption, 28_LVBus946787_consumption, 28_LVBus946790_consumption, 28_LVBus946919_consumption, 28_LVBus947181_consumption, 28_LVBus947182_consumption, 28_LVBus947200_consumption, 28_LVBus947300_consumption, 28_LVBus947301_consumption, 28_LVBus948778_consumption, 28_LVBus948780_consumption, 28_LVBus948994_consumption, 28_LVBus948995_consumption, 28_LVBus948996_consumption, 28_LVBus948997_consumption, 28_LVBus948998_consumption, 28_LVBus948999_consumption, 28_LVBus949000_consumption, 28_LVBus955402_consumption, 28_LVBus957075_consumption, 28_LVBus957880_consumption, 28_LVBus957882_consumption, 28_LVBus957883_consumption, 28_LVBus957884_consumption, 28_LVBus960379_consumption, 28_LVBus962168_consumption, 28_LVBus962170_consumption, 28_LVBus962172_consumption, 28_LVBus962173_consumption, 28_LVBus962174_consumption, 28_LVBus962175_consumption, 28_LVBus963796_consumption, 28_LVBus963798_consumption, 28_LVBus963801_consumption, 28_LVBus963802_consumption, 28_LVBus963804_consumption, 28_LVBus963806_consumption, 28_LVBus964423_consumption, 28_LVBus964469_consumption, 28_LVBus964470_consumption, 28_LVBus964471_consumption, 28_LVBus964473_consumption, 28_LVBus965483_consumption, 28_LVBus965484_consumption, 28_LVBus965485_consumption, 28_LVBus965487_consumption, 28_LVBus965488_consumption, 28_LVBus965489_consumption, 28_LVBus968554_consumption, 28_LVBus968666_consumption, 28_LVBus968667_consumption, 28_LVBus968668_consumption, 28_LVBus968669_consumption, 28_LVBus972586_consumption, 28_LVBus973767_consumption, 28_LVBus974197_consumption, 28_LVBus974199_consumption, 28_LVBus977173_consumption, 28_LVBus977372_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  715 group(s) of loads (1430 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  17 group(s) of series lines (36 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  893 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus181683_production, 28_LVBus181684_production, 28_LVBus181685_production, 28_LVBus181686_production, 28_LVBus181690_production, 28_LVBus181691_production, 28_LVBus181692_production, 28_LVBus181693_production, 28_LVBus181694_production, 28_LVBus181695_consumption, 28_LVBus181695_production, 28_LVBus181696_production, 28_LVBus181698_production, 28_LVBus181699_production, 28_LVBus181700_production, 28_LVBus181701_production, 28_LVBus181702_production, 28_LVBus181703_production, 28_LVBus181704_production, 28_LVBus181705_production, 28_LVBus181707_production, 28_LVBus181708_consumption, 28_LVBus181708_production, 28_LVBus181709_production, 28_LVBus181710_production, 28_LVBus181714_consumption, 28_LVBus181714_production, 28_LVBus181715_production, 28_LVBus181716_production, 28_LVBus181717_production, 28_LVBus181719_production, 28_LVBus181720_production, 28_LVBus181721_production, 28_LVBus181722_production, 28_LVBus181723_production, 28_LVBus181725_production, 28_LVBus181726_production, 28_LVBus181727_consumption, 28_LVBus181727_production, 28_LVBus181728_production, 28_LVBus181729_production, 28_LVBus181730_consumption, 28_LVBus181730_production, 28_LVBus181731_production, 28_LVBus181732_production, 28_LVBus181733_production, 28_LVBus181734_production, 28_LVBus181736_production, 28_LVBus181737_production, 28_LVBus181738_production, 28_LVBus181742_consumption, 28_LVBus181742_production, 28_LVBus181743_production, 28_LVBus181744_production, 28_LVBus181745_production, 28_LVBus181746_production, 28_LVBus181747_production, 28_LVBus181748_production, 28_LVBus181749_consumption, 28_LVBus181749_production, 28_LVBus181750_production, 28_LVBus181752_production, 28_LVBus181753_production, 28_LVBus181754_production, 28_LVBus181756_production, 28_LVBus181757_consumption, 28_LVBus181757_production, 28_LVBus181759_production, 28_LVBus181760_production, 28_LVBus181761_consumption, 28_LVBus181761_production, 28_LVBus181763_production, 28_LVBus181764_production, 28_LVBus181766_production, 28_LVBus181767_consumption, 28_LVBus181767_production, 28_LVBus181768_consumption, 28_LVBus181768_production, 28_LVBus181769_production, 28_LVBus181770_production, 28_LVBus181771_production, 28_LVBus181772_production, 28_LVBus181773_production, 28_LVBus181777_production, 28_LVBus181779_production, 28_LVBus181781_production, 28_LVBus181782_production, 28_LVBus181783_production, 28_LVBus181785_production, 28_LVBus181787_production, 28_LVBus181789_consumption, 28_LVBus181789_production, 28_LVBus181791_production, 28_LVBus181793_consumption, 28_LVBus181793_production, 28_LVBus181795_production, 28_LVBus181796_production, 28_LVBus181797_production, 28_LVBus181798_production, 28_LVBus181799_production, 28_LVBus181801_production, 28_LVBus181803_consumption, 28_LVBus181803_production, 28_LVBus181804_consumption, 28_LVBus181804_production, 28_LVBus181805_consumption, 28_LVBus181805_production, 28_LVBus181806_production, 28_LVBus181807_production, 28_LVBus181808_production, 28_LVBus181809_production, 28_LVBus181811_production, 28_LVBus181813_production, 28_LVBus181814_production, 28_LVBus181815_production, 28_LVBus181817_production, 28_LVBus181818_production, 28_LVBus181819_production, 28_LVBus181820_consumption, 28_LVBus181820_production, 28_LVBus181821_production, 28_LVBus181822_production, 28_LVBus181823_production, 28_LVBus181824_production, 28_LVBus181826_production, 28_LVBus181827_production, 28_LVBus181828_consumption, 28_LVBus181828_production, 28_LVBus181829_production, 28_LVBus181830_consumption, 28_LVBus181830_production, 28_LVBus181831_production, 28_LVBus181832_production, 28_LVBus181834_consumption, 28_LVBus181834_production, 28_LVBus181835_production, 28_LVBus181837_production, 28_LVBus181840_production, 28_LVBus181842_production, 28_LVBus181843_production, 28_LVBus181844_consumption, 28_LVBus181844_production, 28_LVBus181845_production, 28_LVBus181846_production, 28_LVBus181848_production, 28_LVBus181849_production, 28_LVBus181851_consumption, 28_LVBus181851_production, 28_LVBus181852_production, 28_LVBus181853_production, 28_LVBus181855_consumption, 28_LVBus181855_production, 28_LVBus181856_production, 28_LVBus181857_consumption, 28_LVBus181857_production, 28_LVBus181861_production, 28_LVBus181862_production, 28_LVBus181863_production, 28_LVBus181864_production, 28_LVBus181865_production, 28_LVBus181866_production, 28_LVBus181867_production, 28_LVBus181869_production, 28_LVBus181870_production, 28_LVBus181871_production, 28_LVBus181872_production, 28_LVBus181874_consumption, 28_LVBus181874_production, 28_LVBus181875_production, 28_LVBus181876_production, 28_LVBus181878_production, 28_LVBus181879_production, 28_LVBus181881_consumption, 28_LVBus181881_production, 28_LVBus181882_consumption, 28_LVBus181882_production, 28_LVBus181884_consumption, 28_LVBus181884_production, 28_LVBus181885_consumption, 28_LVBus181885_production, 28_LVBus181886_consumption, 28_LVBus181886_production, 28_LVBus181887_consumption, 28_LVBus181887_production, 28_LVBus181888_consumption, 28_LVBus181888_production, 28_LVBus181889_production, 28_LVBus181890_production, 28_LVBus181892_production, 28_LVBus181893_production, 28_LVBus181894_production, 28_LVBus181898_consumption, 28_LVBus181898_production, 28_LVBus181899_production, 28_LVBus181900_consumption, 28_LVBus181900_production, 28_LVBus181901_production, 28_LVBus181902_production, 28_LVBus181906_production, 28_LVBus181907_consumption, 28_LVBus181907_production, 28_LVBus181909_consumption, 28_LVBus181909_production, 28_LVBus181912_production, 28_LVBus181914_production, 28_LVBus181915_production, 28_LVBus181917_production, 28_LVBus181918_production, 28_LVBus181919_production, 28_LVBus181920_production, 28_LVBus181921_production, 28_LVBus181922_consumption, 28_LVBus181922_production, 28_LVBus181923_consumption, 28_LVBus181923_production, 28_LVBus181924_production, 28_LVBus181925_production, 28_LVBus181926_production, 28_LVBus181927_production, 28_LVBus181928_production, 28_LVBus181930_production, 28_LVBus181931_production, 28_LVBus181932_production, 28_LVBus181933_production, 28_LVBus181934_production, 28_LVBus181935_production, 28_LVBus181936_production, 28_LVBus181937_production, 28_LVBus181939_production, 28_LVBus181940_production, 28_LVBus181941_production, 28_LVBus181942_production, 28_LVBus181943_production, 28_LVBus181944_production, 28_LVBus181945_production, 28_LVBus181946_production, 28_LVBus181947_production, 28_LVBus181949_production, 28_LVBus181951_consumption, 28_LVBus181951_production, 28_LVBus181952_production, 28_LVBus181953_production, 28_LVBus181954_production, 28_LVBus181955_production, 28_LVBus181956_production, 28_LVBus181957_production, 28_LVBus181958_production, 28_LVBus181959_consumption, 28_LVBus181959_production, 28_LVBus181960_production, 28_LVBus181962_production, 28_LVBus181963_consumption, 28_LVBus181963_production, 28_LVBus181965_production, 28_LVBus181966_production, 28_LVBus181968_production, 28_LVBus181970_production, 28_LVBus181972_production, 28_LVBus181973_consumption, 28_LVBus181973_production, 28_LVBus181974_production, 28_LVBus181975_production, 28_LVBus181977_production, 28_LVBus181978_consumption, 28_LVBus181978_production, 28_LVBus181979_production, 28_LVBus181980_production, 28_LVBus181981_production, 28_LVBus181982_consumption, 28_LVBus181982_production, 28_LVBus181983_production, 28_LVBus181984_production, 28_LVBus181985_production, 28_LVBus181989_production, 28_LVBus181991_production, 28_LVBus181993_consumption, 28_LVBus181993_production, 28_LVBus181995_production, 28_LVBus181997_production, 28_LVBus181999_production, 28_LVBus182000_production, 28_LVBus182001_production, 28_LVBus182003_production, 28_LVBus182004_consumption, 28_LVBus182004_production, 28_LVBus182005_production, 28_LVBus182006_production, 28_LVBus182007_production, 28_LVBus182009_consumption, 28_LVBus182009_production, 28_LVBus182010_production, 28_LVBus182011_production, 28_LVBus182012_production, 28_LVBus182013_production, 28_LVBus182015_production, 28_LVBus182016_production, 28_LVBus182017_production, 28_LVBus182018_production, 28_LVBus182019_consumption, 28_LVBus182019_production, 28_LVBus182020_production, 28_LVBus182022_production, 28_LVBus182023_consumption, 28_LVBus182023_production, 28_LVBus182024_production, 28_LVBus182026_consumption, 28_LVBus182026_production, 28_LVBus182027_production, 28_LVBus182028_production, 28_LVBus182029_production, 28_LVBus182033_production, 28_LVBus182034_production, 28_LVBus182035_production, 28_LVBus182036_consumption, 28_LVBus182036_production, 28_LVBus182038_production, 28_LVBus182039_production, 28_LVBus182040_consumption, 28_LVBus182040_production, 28_LVBus182041_consumption, 28_LVBus182041_production, 28_LVBus182042_production, 28_LVBus182043_production, 28_LVBus182044_production, 28_LVBus182046_consumption, 28_LVBus182046_production, 28_LVBus182047_consumption, 28_LVBus182047_production, 28_LVBus182048_production, 28_LVBus182049_production, 28_LVBus182051_consumption, 28_LVBus182051_production, 28_LVBus182052_production, 28_LVBus182054_consumption, 28_LVBus182054_production, 28_LVBus182056_production, 28_LVBus182057_production, 28_LVBus182058_production, 28_LVBus182059_production, 28_LVBus182060_production, 28_LVBus182061_production, 28_LVBus182062_consumption, 28_LVBus182062_production, 28_LVBus182063_production, 28_LVBus182064_consumption, 28_LVBus182064_production, 28_LVBus182065_production, 28_LVBus182067_consumption, 28_LVBus182067_production, 28_LVBus182068_consumption, 28_LVBus182068_production, 28_LVBus182069_consumption, 28_LVBus182069_production, 28_LVBus182070_consumption, 28_LVBus182070_production, 28_LVBus182071_production, 28_LVBus182072_consumption, 28_LVBus182072_production, 28_LVBus182073_consumption, 28_LVBus182073_production, 28_LVBus182077_production, 28_LVBus182079_production, 28_LVBus182080_production, 28_LVBus182081_production, 28_LVBus182083_consumption, 28_LVBus182083_production, 28_LVBus182084_production, 28_LVBus182086_consumption, 28_LVBus182086_production, 28_LVBus182087_production, 28_LVBus182088_production, 28_LVBus182089_production, 28_LVBus182091_production, 28_LVBus182092_production, 28_LVBus182093_production, 28_LVBus182094_production, 28_LVBus182095_production, 28_LVBus182096_production, 28_LVBus182098_consumption, 28_LVBus182098_production, 28_LVBus182099_production, 28_LVBus182100_consumption, 28_LVBus182100_production, 28_LVBus182101_consumption, 28_LVBus182101_production, 28_LVBus182102_consumption, 28_LVBus182102_production, 28_LVBus182106_production, 28_LVBus182108_production, 28_LVBus182110_consumption, 28_LVBus182110_production, 28_LVBus182111_consumption, 28_LVBus182111_production, 28_LVBus182112_consumption, 28_LVBus182112_production, 28_LVBus182113_consumption, 28_LVBus182113_production, 28_LVBus182115_consumption, 28_LVBus182115_production, 28_LVBus182116_consumption, 28_LVBus182116_production, 28_LVBus182117_consumption, 28_LVBus182117_production, 28_LVBus182118_production, 28_LVBus182120_production, 28_LVBus182121_production, 28_LVBus182122_production, 28_LVBus182123_production, 28_LVBus182124_production, 28_LVBus182125_production, 28_LVBus182126_production, 28_LVBus182127_consumption, 28_LVBus182127_production, 28_LVBus182128_production, 28_LVBus182129_production, 28_LVBus182131_consumption, 28_LVBus182131_production, 28_LVBus182132_consumption, 28_LVBus182132_production, 28_LVBus182133_production, 28_LVBus182134_production, 28_LVBus182136_production, 28_LVBus182137_consumption, 28_LVBus182137_production, 28_LVBus182138_production, 28_LVBus182139_production, 28_LVBus182140_production, 28_LVBus182141_production, 28_LVBus182142_production, 28_LVBus182144_production, 28_LVBus182145_consumption, 28_LVBus182145_production, 28_LVBus182146_production, 28_LVBus182147_production, 28_LVBus182148_production, 28_LVBus182150_consumption, 28_LVBus182150_production, 28_LVBus182151_production, 28_LVBus182152_production, 28_LVBus182153_production, 28_LVBus182154_consumption, 28_LVBus182154_production, 28_LVBus182156_consumption, 28_LVBus182156_production, 28_LVBus182157_production, 28_LVBus182158_consumption, 28_LVBus182158_production, 28_LVBus182159_production, 28_LVBus182160_production, 28_LVBus182161_production, 28_LVBus182166_production, 28_LVBus182168_consumption, 28_LVBus182168_production, 28_LVBus182170_production, 28_LVBus182172_production, 28_LVBus182174_consumption, 28_LVBus182174_production, 28_LVBus182175_consumption, 28_LVBus182175_production, 28_LVBus182176_consumption, 28_LVBus182176_production, 28_LVBus182177_production, 28_LVBus182178_consumption, 28_LVBus182178_production, 28_LVBus182179_consumption, 28_LVBus182179_production, 28_LVBus182180_production, 28_LVBus182181_consumption, 28_LVBus182181_production, 28_LVBus182185_consumption, 28_LVBus182185_production, 28_LVBus182186_production, 28_LVBus182187_production, 28_LVBus182188_production, 28_LVBus182190_production, 28_LVBus182192_production, 28_LVBus182193_production, 28_LVBus182194_production, 28_LVBus182195_production, 28_LVBus182197_consumption, 28_LVBus182197_production, 28_LVBus182199_consumption, 28_LVBus182199_production, 28_LVBus182200_consumption, 28_LVBus182200_production, 28_LVBus182201_production, 28_LVBus182202_production, 28_LVBus182204_consumption, 28_LVBus182204_production, 28_LVBus182205_production, 28_LVBus182206_production, 28_LVBus182208_production, 28_LVBus182210_production, 28_LVBus182211_production, 28_LVBus182213_production, 28_LVBus182215_production, 28_LVBus182216_consumption, 28_LVBus182216_production, 28_LVBus182217_production, 28_LVBus182218_production, 28_LVBus182219_production, 28_LVBus182221_consumption, 28_LVBus182221_production, 28_LVBus182222_production, 28_LVBus182223_production, 28_LVBus182225_production, 28_LVBus182227_production, 28_LVBus182229_production, 28_LVBus182230_consumption, 28_LVBus182230_production, 28_LVBus182231_production, 28_LVBus182232_production, 28_LVBus182233_production, 28_LVBus182235_production, 28_LVBus182236_production, 28_LVBus182237_production, 28_LVBus182238_production, 28_LVBus182239_production, 28_LVBus182241_production, 28_LVBus182242_production, 28_LVBus182243_consumption, 28_LVBus182243_production, 28_LVBus182244_production, 28_LVBus182246_production, 28_LVBus182247_consumption, 28_LVBus182247_production, 28_LVBus182248_production, 28_LVBus182250_production, 28_LVBus182251_production, 28_LVBus182252_production, 28_LVBus182254_production, 28_LVBus182255_production, 28_LVBus182257_production, 28_LVBus182258_production, 28_LVBus182259_production, 28_LVBus182261_production, 28_LVBus182262_production, 28_LVBus182265_production, 28_LVBus182267_production, 28_LVBus182268_production, 28_LVBus182269_production, 28_LVBus182270_consumption, 28_LVBus182270_production, 28_LVBus182272_production, 28_LVBus182273_production, 28_LVBus182274_production, 28_LVBus182275_production, 28_LVBus182276_production, 28_LVBus182277_production, 28_LVBus182278_production, 28_LVBus182280_production, 28_LVBus182281_production, 28_LVBus182282_production, 28_LVBus182283_production, 28_LVBus182284_production, 28_LVBus182285_production, 28_LVBus182286_consumption, 28_LVBus182286_production, 28_LVBus182288_production, 28_LVBus182289_production, 28_LVBus182290_production, 28_LVBus182291_production, 28_LVBus182292_production, 28_LVBus182294_production, 28_LVBus182295_consumption, 28_LVBus182295_production, 28_LVBus182296_production, 28_LVBus182297_production, 28_LVBus182298_production, 28_LVBus182300_consumption, 28_LVBus182300_production, 28_LVBus182301_consumption, 28_LVBus182301_production, 28_LVBus182302_production, 28_LVBus182303_consumption, 28_LVBus182303_production, 28_LVBus182304_production, 28_LVBus182305_production, 28_LVBus182310_consumption, 28_LVBus182310_production, 28_LVBus182311_production, 28_LVBus182312_production, 28_LVBus182313_consumption, 28_LVBus182313_production, 28_LVBus182314_production, 28_LVBus182315_production, 28_LVBus182317_consumption, 28_LVBus182317_production, 28_LVBus182318_production, 28_LVBus182319_production, 28_LVBus182320_production, 28_LVBus182321_consumption, 28_LVBus182321_production, 28_LVBus182323_production, 28_LVBus182324_production, 28_LVBus182326_production, 28_LVBus182328_consumption, 28_LVBus182328_production, 28_LVBus182329_production, 28_LVBus182330_production, 28_LVBus182331_consumption, 28_LVBus182331_production, 28_LVBus182332_production, 28_LVBus182333_production, 28_LVBus182335_production, 28_LVBus182336_production, 28_LVBus182337_production, 28_LVBus182338_production, 28_LVBus182339_production, 28_LVBus182340_production, 28_LVBus182342_production, 28_LVBus182343_production, 28_LVBus182344_production, 28_LVBus182345_production, 28_LVBus182346_production, 28_LVBus182347_production, 28_LVBus182348_production, 28_LVBus182349_production, 28_LVBus182350_production, 28_LVBus182351_production, 28_LVBus182353_production, 28_LVBus182354_production, 28_LVBus182355_production, 28_LVBus182356_production, 28_LVBus182358_consumption, 28_LVBus182358_production, 28_LVBus182359_production, 28_LVBus182360_consumption, 28_LVBus182360_production, 28_LVBus182361_production, 28_LVBus182362_production, 28_LVBus182363_production, 28_LVBus182364_production, 28_LVBus182365_consumption, 28_LVBus182365_production, 28_LVBus182366_production, 28_LVBus182367_production, 28_LVBus182368_consumption, 28_LVBus182368_production, 28_LVBus182369_production, 28_LVBus182370_consumption, 28_LVBus182370_production, 28_LVBus182371_consumption, 28_LVBus182371_production, 28_LVBus182372_production, 28_LVBus182373_production, 28_LVBus182374_production, 28_LVBus182375_production, 28_LVBus182376_production, 28_LVBus182377_production, 28_LVBus182379_production, 28_LVBus182380_production, 28_LVBus182381_production, 28_LVBus182382_production, 28_LVBus182384_production, 28_LVBus182385_consumption, 28_LVBus182385_production, 28_LVBus182386_production, 28_LVBus852557_production, 28_LVBus852558_consumption, 28_LVBus852558_production, 28_LVBus852559_production, 28_LVBus852560_production, 28_LVBus852606_production, 28_LVBus856056_production, 28_LVBus856496_production, 28_LVBus856497_production, 28_LVBus856498_production, 28_LVBus856499_production, 28_LVBus859955_production, 28_LVBus860858_production, 28_LVBus867217_consumption, 28_LVBus867217_production, 28_LVBus867218_production, 28_LVBus867219_consumption, 28_LVBus867219_production, 28_LVBus867220_production, 28_LVBus868900_consumption, 28_LVBus868900_production, 28_LVBus868901_production, 28_LVBus868902_production, 28_LVBus868903_production, 28_LVBus868984_production, 28_LVBus870907_consumption, 28_LVBus870907_production, 28_LVBus872015_production, 28_LVBus873052_production, 28_LVBus873704_production, 28_LVBus873789_consumption, 28_LVBus873789_production, 28_LVBus873790_consumption, 28_LVBus873790_production, 28_LVBus873791_production, 28_LVBus874539_production, 28_LVBus880315_production, 28_LVBus880316_production, 28_LVBus882132_production, 28_LVBus884445_production, 28_LVBus885392_consumption, 28_LVBus885392_production, 28_LVBus892920_production, 28_LVBus894933_consumption, 28_LVBus894933_production, 28_LVBus894934_consumption, 28_LVBus894934_production, 28_LVBus895715_consumption, 28_LVBus895715_production, 28_LVBus895716_consumption, 28_LVBus895716_production, 28_LVBus895717_production, 28_LVBus895805_production, 28_LVBus895806_production, 28_LVBus895807_production, 28_LVBus901238_production, 28_LVBus902915_consumption, 28_LVBus902915_production, 28_LVBus903773_production, 28_LVBus903774_production, 28_LVBus904328_production, 28_LVBus907995_consumption, 28_LVBus907995_production, 28_LVBus910091_consumption, 28_LVBus910091_production, 28_LVBus912060_consumption, 28_LVBus912060_production, 28_LVBus912061_consumption, 28_LVBus912061_production, 28_LVBus912062_production, 28_LVBus912063_production, 28_LVBus912064_production, 28_LVBus912065_production, 28_LVBus912815_consumption, 28_LVBus912815_production, 28_LVBus912816_production, 28_LVBus912817_production, 28_LVBus925033_production, 28_LVBus925034_production, 28_LVBus926431_production, 28_LVBus927456_production, 28_LVBus929541_consumption, 28_LVBus929541_production, 28_LVBus929721_production, 28_LVBus939655_production, 28_LVBus942768_production, 28_LVBus942769_production, 28_LVBus946496_production, 28_LVBus946497_production, 28_LVBus946498_production, 28_LVBus946499_production, 28_LVBus946718_production, 28_LVBus946719_production, 28_LVBus946785_consumption, 28_LVBus946785_production, 28_LVBus946786_consumption, 28_LVBus946786_production, 28_LVBus946787_production, 28_LVBus946788_consumption, 28_LVBus946788_production, 28_LVBus946789_production, 28_LVBus946790_production, 28_LVBus946919_production, 28_LVBus947180_consumption, 28_LVBus947180_production, 28_LVBus947181_production, 28_LVBus947182_production, 28_LVBus947200_production, 28_LVBus947299_consumption, 28_LVBus947299_production, 28_LVBus947300_production, 28_LVBus947301_production, 28_LVBus948778_production, 28_LVBus948779_consumption, 28_LVBus948779_production, 28_LVBus948780_production, 28_LVBus948994_production, 28_LVBus948995_production, 28_LVBus948996_production, 28_LVBus948997_production, 28_LVBus948998_production, 28_LVBus948999_production, 28_LVBus949000_production, 28_LVBus950930_consumption, 28_LVBus950930_production, 28_LVBus955400_production, 28_LVBus955401_consumption, 28_LVBus955401_production, 28_LVBus955402_production, 28_LVBus956520_consumption, 28_LVBus956520_production, 28_LVBus957074_production, 28_LVBus957075_production, 28_LVBus957880_production, 28_LVBus957881_consumption, 28_LVBus957881_production, 28_LVBus957882_production, 28_LVBus957883_production, 28_LVBus957884_production, 28_LVBus959440_consumption, 28_LVBus959440_production, 28_LVBus960378_production, 28_LVBus960379_production, 28_LVBus962168_production, 28_LVBus962169_production, 28_LVBus962170_production, 28_LVBus962171_consumption, 28_LVBus962171_production, 28_LVBus962172_production, 28_LVBus962173_production, 28_LVBus962174_production, 28_LVBus962175_production, 28_LVBus963179_consumption, 28_LVBus963179_production, 28_LVBus963795_consumption, 28_LVBus963795_production, 28_LVBus963796_production, 28_LVBus963797_consumption, 28_LVBus963797_production, 28_LVBus963798_production, 28_LVBus963799_consumption, 28_LVBus963799_production, 28_LVBus963800_consumption, 28_LVBus963800_production, 28_LVBus963801_production, 28_LVBus963802_production, 28_LVBus963803_consumption, 28_LVBus963803_production, 28_LVBus963804_production, 28_LVBus963805_consumption, 28_LVBus963805_production, 28_LVBus963806_production, 28_LVBus964423_production, 28_LVBus964469_production, 28_LVBus964470_production, 28_LVBus964471_production, 28_LVBus964472_consumption, 28_LVBus964472_production, 28_LVBus964473_production, 28_LVBus965483_production, 28_LVBus965484_production, 28_LVBus965485_production, 28_LVBus965486_consumption, 28_LVBus965486_production, 28_LVBus965487_production, 28_LVBus965488_production, 28_LVBus965489_production, 28_LVBus968554_production, 28_LVBus968666_production, 28_LVBus968667_production, 28_LVBus968668_production, 28_LVBus968669_production, 28_LVBus972364_production, 28_LVBus972365_production, 28_LVBus972586_production, 28_LVBus972587_consumption, 28_LVBus972587_production, 28_LVBus972588_production, 28_LVBus973767_production, 28_LVBus974195_consumption, 28_LVBus974195_production, 28_LVBus974196_production, 28_LVBus974197_production, 28_LVBus974198_production, 28_LVBus974199_production, 28_LVBus977171_consumption, 28_LVBus977171_production, 28_LVBus977172_production, 28_LVBus977173_production, 28_LVBus977174_consumption, 28_LVBus977174_production, 28_LVBus977175_production, 28_LVBus977372_production, 28_MVLV00656_consumption, 28_MVLV00656_production, 28_MVLV16181_consumption, 28_MVLV16181_production, 28_MVLV26619_consumption, 28_MVLV26619_production, 28_MVLV30592_consumption, 28_MVLV30592_production, 28_MVLV34347_consumption, 28_MVLV34347_production, 28_MVLV41018_consumption, 28_MVLV41018_production, 28_MVLV43797_consumption, 28_MVLV43797_production, 28_MVLV43802_consumption, 28_MVLV43802_production, 28_MVLV52958_consumption, 28_MVLV52958_production, 28_MVLV72679_consumption, 28_MVLV72679_production, 28_MVLV79313_consumption, 28_MVLV79313_production.

