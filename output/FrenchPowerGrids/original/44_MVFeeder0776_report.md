# BMOPF Network Summary: 44_MVFeeder0776

**Generated:** 2026-10-01 23:34:10  
**Findings:** 0 errors · 4 warnings · 268 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 348 |  |
| line | 332 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 618 | 1.632 MW, 489.5 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 15 |  |
| switch | 0 |  |
| transformer | 15 | Dyn11×15 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 26 | 25 | 4 | 0 |
| LV_236V | 236.0 V | 322 | 307 | 614 | 0 |

**Transformer transitions:**

- `44_MVLV52054_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV12205_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV00898_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV58040_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV18164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV59373_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV23345_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV33351_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV39100_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV57606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV18166_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV00123_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV08383_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV57608_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV55328_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 142 |
| Tree depth (max hops) | 32 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 348 | 1 | 347 | 0 | 0 | 0 |
| Tier LV_236V | 322 | 15 | 307 | 0 | 0 | 0 |
| Tier MV_11.8kV | 26 | 1 | 25 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 15; skipped invalid branches: 0.

Galvanic zones: 16; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 44_ETUPE | MV_11.8kV | 26 | 0 | 0 | 15 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1366 declared bus terminals; 1303 mapped line/closed-switch conductor edges; 63 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 34600.0 | 2.287 | 1854 |
| q_nom | 0.0 | 10400.0 | 2.287 | 1854 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.02 | 811.0 | 1.084 | 332 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.467 | 15 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 353 of 618 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684314_consumption' has phase imbalance of 40.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684256_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684050_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683962_consumption' has phase imbalance of 273.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684148_consumption' has phase imbalance of 66.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684049_consumption' has phase imbalance of 20.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683971_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684146_consumption' has phase imbalance of 59.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684068_consumption' has phase imbalance of 251.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684257_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684305_consumption' has phase imbalance of 121.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684034_consumption' has phase imbalance of 208.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683967_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684031_consumption' has phase imbalance of 81.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684155_consumption' has phase imbalance of 86.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683959_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684207_consumption' has phase imbalance of 100.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683960_consumption' has phase imbalance of 143.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684119_consumption' has phase imbalance of 32.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683998_consumption' has phase imbalance of 70.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684273_consumption' has phase imbalance of 125.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684063_consumption' has phase imbalance of 143.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683999_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684251_consumption' has phase imbalance of 48.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684304_consumption' has phase imbalance of 253.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684143_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684302_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684175_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684179_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684131_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683978_consumption' has phase imbalance of 252.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683992_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684170_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684306_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684058_consumption' has phase imbalance of 98.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684199_consumption' has phase imbalance of 271.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684222_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684093_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684033_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684096_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684054_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684262_consumption' has phase imbalance of 221.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684234_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684092_consumption' has phase imbalance of 177.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684194_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683997_consumption' has phase imbalance of 78.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684053_consumption' has phase imbalance of 112.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683958_consumption' has phase imbalance of 56.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684270_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684128_consumption' has phase imbalance of 70.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684043_consumption' has phase imbalance of 40.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684317_consumption' has phase imbalance of 24.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684004_consumption' has phase imbalance of 98.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683969_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684115_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684015_consumption' has phase imbalance of 21.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684209_consumption' has phase imbalance of 181.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684149_consumption' has phase imbalance of 75.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684268_consumption' has phase imbalance of 125.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684275_consumption' has phase imbalance of 101.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684081_consumption' has phase imbalance of 158.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684223_consumption' has phase imbalance of 207.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684118_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684087_consumption' has phase imbalance of 233.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684238_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684221_consumption' has phase imbalance of 59.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684229_consumption' has phase imbalance of 41.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684012_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684249_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684220_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684120_consumption' has phase imbalance of 133.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684076_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684315_consumption' has phase imbalance of 220.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684000_consumption' has phase imbalance of 140.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684002_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684016_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684009_consumption' has phase imbalance of 258.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684070_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684230_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684165_consumption' has phase imbalance of 266.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684052_consumption' has phase imbalance of 64.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684127_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684197_consumption' has phase imbalance of 103.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684163_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683966_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684089_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683982_consumption' has phase imbalance of 142.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684157_consumption' has phase imbalance of 230.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684198_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684277_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684008_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683984_consumption' has phase imbalance of 66.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684288_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683964_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683996_consumption' has phase imbalance of 67.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683979_consumption' has phase imbalance of 209.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684239_consumption' has phase imbalance of 50.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684125_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684028_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684156_consumption' has phase imbalance of 45.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684044_consumption' has phase imbalance of 59.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684168_consumption' has phase imbalance of 107.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684242_consumption' has phase imbalance of 24.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684106_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684164_consumption' has phase imbalance of 257.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684227_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684040_consumption' has phase imbalance of 183.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684261_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684080_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684077_consumption' has phase imbalance of 248.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684217_consumption' has phase imbalance of 145.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684022_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684258_consumption' has phase imbalance of 216.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684204_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684252_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684216_consumption' has phase imbalance of 72.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683993_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684117_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684099_consumption' has phase imbalance of 195.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684061_consumption' has phase imbalance of 251.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683976_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683985_consumption' has phase imbalance of 261.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684039_consumption' has phase imbalance of 144.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683968_consumption' has phase imbalance of 90.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684064_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683970_consumption' has phase imbalance of 100.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684026_consumption' has phase imbalance of 90.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683973_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684248_consumption' has phase imbalance of 251.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684243_consumption' has phase imbalance of 97.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684085_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684037_consumption' has phase imbalance of 128.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684191_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684035_consumption' has phase imbalance of 76.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684091_consumption' has phase imbalance of 282.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684029_consumption' has phase imbalance of 100.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684171_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683995_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683956_consumption' has phase imbalance of 118.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684151_consumption' has phase imbalance of 42.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684301_consumption' has phase imbalance of 27.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684298_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684095_consumption' has phase imbalance of 28.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684154_consumption' has phase imbalance of 55.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684108_consumption' has phase imbalance of 47.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684060_consumption' has phase imbalance of 93.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684215_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684250_consumption' has phase imbalance of 194.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684145_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684303_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684046_consumption' has phase imbalance of 228.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684271_consumption' has phase imbalance of 58.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683983_consumption' has phase imbalance of 83.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684045_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684147_consumption' has phase imbalance of 155.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684167_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684213_consumption' has phase imbalance of 157.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684266_consumption' has phase imbalance of 267.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684013_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684116_consumption' has phase imbalance of 72.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684254_consumption' has phase imbalance of 236.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684225_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684272_consumption' has phase imbalance of 190.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684201_consumption' has phase imbalance of 75.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684202_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684178_consumption' has phase imbalance of 274.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684296_consumption' has phase imbalance of 88.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683961_consumption' has phase imbalance of 224.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684278_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684136_consumption' has phase imbalance of 69.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684001_consumption' has phase imbalance of 170.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684210_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684142_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683974_consumption' has phase imbalance of 127.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684160_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684079_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684123_consumption' has phase imbalance of 207.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684211_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684003_consumption' has phase imbalance of 144.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684129_consumption' has phase imbalance of 230.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684121_consumption' has phase imbalance of 139.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684162_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684014_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683957_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684086_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684206_consumption' has phase imbalance of 170.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684218_consumption' has phase imbalance of 272.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684011_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683980_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684101_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683965_consumption' has phase imbalance of 214.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684005_consumption' has phase imbalance of 30.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684232_consumption' has phase imbalance of 125.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684159_consumption' has phase imbalance of 253.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684065_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683989_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684263_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684126_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684048_consumption' has phase imbalance of 49.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684023_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684102_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684021_consumption' has phase imbalance of 278.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684196_consumption' has phase imbalance of 97.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684032_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684183_consumption' has phase imbalance of 61.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684236_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus683990_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684098_consumption' has phase imbalance of 88.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684310_consumption' has phase imbalance of 202.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684189_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684260_consumption' has phase imbalance of 82.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus684203_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 618 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus684018' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.632 MW |
| Total load Q | 489.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 44_MVLV52054_Transformer | 440.0 kVA | 43.7% |
| 44_MVLV12205_Transformer | 176.0 kVA | 25.8% |
| 44_MVLV00898_Transformer | 693.0 kVA | 34.3% |
| 44_MVLV58040_Transformer | 176.0 kVA | 28.0% |
| 44_MVLV18164_Transformer | 110.0 kVA | 40.1% |
| 44_MVLV59373_Transformer | 275.0 kVA | 41.5% |
| 44_MVLV23345_Transformer | 440.0 kVA | 32.1% |
| 44_MVLV33351_Transformer | 275.0 kVA | 28.7% |
| 44_MVLV39100_Transformer | 440.0 kVA | 45.1% |
| 44_MVLV57606_Transformer | 176.0 kVA | 34.5% |
| 44_MVLV18166_Transformer | 275.0 kVA | 44.9% |
| 44_MVLV00123_Transformer | 440.0 kVA | 29.4% |
| 44_MVLV08383_Transformer | 275.0 kVA | 11.8% |
| 44_MVLV57608_Transformer | 440.0 kVA | 36.3% |
| 44_MVLV55328_Transformer | 275.0 kVA | 35.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.63 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 348 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 348 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 26 |
| LV_236V | 4-wire | 322 / 322 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 322 |
| Neutral branches | 307 |
| Grounding points | 15 |
| Neutral sections | 15 |
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
| 11.78 kV | 26 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 16 |
| Islands without voltage reference | 0 |
| Line impedance spread | 405.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 322 / 26 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 354 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 354 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus683955_production, 44_LVBus683956_production, 44_LVBus683957_production, 44_LVBus683958_production, 44_LVBus683959_production, 44_LVBus683960_production, 44_LVBus683961_production, 44_LVBus683962_production, 44_LVBus683964_production, 44_LVBus683965_production, 44_LVBus683966_production, 44_LVBus683967_production, 44_LVBus683968_production, 44_LVBus683969_production, 44_LVBus683970_production, 44_LVBus683971_production, 44_LVBus683973_production, 44_LVBus683974_production, 44_LVBus683975_production, 44_LVBus683976_production, 44_LVBus683977_production, 44_LVBus683978_production, 44_LVBus683979_production, 44_LVBus683980_production, 44_LVBus683982_production, 44_LVBus683983_production, 44_LVBus683984_production, 44_LVBus683985_production, 44_LVBus683986_production, 44_LVBus683987_consumption, 44_LVBus683987_production, 44_LVBus683988_consumption, 44_LVBus683988_production, 44_LVBus683989_production, 44_LVBus683990_production, 44_LVBus683991_production, 44_LVBus683992_production, 44_LVBus683993_production, 44_LVBus683995_production, 44_LVBus683996_production, 44_LVBus683997_production, 44_LVBus683998_production, 44_LVBus683999_production, 44_LVBus684000_production, 44_LVBus684001_production, 44_LVBus684002_production, 44_LVBus684003_production, 44_LVBus684004_production, 44_LVBus684005_production, 44_LVBus684007_consumption, 44_LVBus684007_production, 44_LVBus684008_production, 44_LVBus684009_production, 44_LVBus684010_production, 44_LVBus684011_production, 44_LVBus684012_production, 44_LVBus684013_production, 44_LVBus684014_production, 44_LVBus684015_production, 44_LVBus684016_production, 44_LVBus684018_production, 44_LVBus684020_production, 44_LVBus684021_production, 44_LVBus684022_production, 44_LVBus684023_production, 44_LVBus684024_production, 44_LVBus684025_production, 44_LVBus684026_production, 44_LVBus684028_production, 44_LVBus684029_production, 44_LVBus684031_production, 44_LVBus684032_production, 44_LVBus684033_production, 44_LVBus684034_production, 44_LVBus684035_production, 44_LVBus684037_production, 44_LVBus684039_production, 44_LVBus684040_production, 44_LVBus684042_production, 44_LVBus684043_production, 44_LVBus684044_production, 44_LVBus684045_production, 44_LVBus684046_production, 44_LVBus684048_production, 44_LVBus684049_production, 44_LVBus684050_production, 44_LVBus684052_production, 44_LVBus684053_production, 44_LVBus684054_production, 44_LVBus684055_consumption, 44_LVBus684055_production, 44_LVBus684056_consumption, 44_LVBus684056_production, 44_LVBus684057_consumption, 44_LVBus684057_production, 44_LVBus684058_production, 44_LVBus684060_production, 44_LVBus684061_production, 44_LVBus684062_production, 44_LVBus684063_production, 44_LVBus684064_production, 44_LVBus684065_production, 44_LVBus684067_consumption, 44_LVBus684067_production, 44_LVBus684068_production, 44_LVBus684070_production, 44_LVBus684071_consumption, 44_LVBus684071_production, 44_LVBus684072_consumption, 44_LVBus684072_production, 44_LVBus684074_production, 44_LVBus684075_production, 44_LVBus684076_production, 44_LVBus684077_production, 44_LVBus684078_production, 44_LVBus684079_production, 44_LVBus684080_production, 44_LVBus684081_production, 44_LVBus684082_production, 44_LVBus684084_consumption, 44_LVBus684084_production, 44_LVBus684085_production, 44_LVBus684086_production, 44_LVBus684087_production, 44_LVBus684088_production, 44_LVBus684089_production, 44_LVBus684090_production, 44_LVBus684091_production, 44_LVBus684092_production, 44_LVBus684093_production, 44_LVBus684095_production, 44_LVBus684096_production, 44_LVBus684097_production, 44_LVBus684098_production, 44_LVBus684099_production, 44_LVBus684101_production, 44_LVBus684102_production, 44_LVBus684103_production, 44_LVBus684104_production, 44_LVBus684105_consumption, 44_LVBus684105_production, 44_LVBus684106_production, 44_LVBus684107_consumption, 44_LVBus684107_production, 44_LVBus684108_production, 44_LVBus684109_consumption, 44_LVBus684109_production, 44_LVBus684111_consumption, 44_LVBus684111_production, 44_LVBus684113_production, 44_LVBus684115_production, 44_LVBus684116_production, 44_LVBus684117_production, 44_LVBus684118_production, 44_LVBus684119_production, 44_LVBus684120_production, 44_LVBus684121_production, 44_LVBus684123_production, 44_LVBus684125_production, 44_LVBus684126_production, 44_LVBus684127_production, 44_LVBus684128_production, 44_LVBus684129_production, 44_LVBus684130_production, 44_LVBus684131_production, 44_LVBus684133_consumption, 44_LVBus684133_production, 44_LVBus684134_consumption, 44_LVBus684134_production, 44_LVBus684135_consumption, 44_LVBus684135_production, 44_LVBus684136_production, 44_LVBus684138_production, 44_LVBus684140_production, 44_LVBus684141_production, 44_LVBus684142_production, 44_LVBus684143_production, 44_LVBus684145_production, 44_LVBus684146_production, 44_LVBus684147_production, 44_LVBus684148_production, 44_LVBus684149_production, 44_LVBus684151_production, 44_LVBus684152_consumption, 44_LVBus684152_production, 44_LVBus684153_production, 44_LVBus684154_production, 44_LVBus684155_production, 44_LVBus684156_production, 44_LVBus684157_production, 44_LVBus684159_production, 44_LVBus684160_production, 44_LVBus684161_production, 44_LVBus684162_production, 44_LVBus684163_production, 44_LVBus684164_production, 44_LVBus684165_production, 44_LVBus684167_production, 44_LVBus684168_production, 44_LVBus684170_production, 44_LVBus684171_production, 44_LVBus684173_consumption, 44_LVBus684173_production, 44_LVBus684174_consumption, 44_LVBus684174_production, 44_LVBus684175_production, 44_LVBus684176_consumption, 44_LVBus684176_production, 44_LVBus684178_production, 44_LVBus684179_production, 44_LVBus684180_production, 44_LVBus684181_consumption, 44_LVBus684181_production, 44_LVBus684182_consumption, 44_LVBus684182_production, 44_LVBus684183_production, 44_LVBus684185_production, 44_LVBus684186_consumption, 44_LVBus684186_production, 44_LVBus684187_consumption, 44_LVBus684187_production, 44_LVBus684188_consumption, 44_LVBus684188_production, 44_LVBus684189_production, 44_LVBus684191_production, 44_LVBus684192_production, 44_LVBus684193_production, 44_LVBus684194_production, 44_LVBus684195_production, 44_LVBus684196_production, 44_LVBus684197_production, 44_LVBus684198_production, 44_LVBus684199_production, 44_LVBus684201_production, 44_LVBus684202_production, 44_LVBus684203_production, 44_LVBus684204_production, 44_LVBus684205_production, 44_LVBus684206_production, 44_LVBus684207_production, 44_LVBus684208_production, 44_LVBus684209_production, 44_LVBus684210_production, 44_LVBus684211_production, 44_LVBus684212_production, 44_LVBus684213_production, 44_LVBus684215_production, 44_LVBus684216_production, 44_LVBus684217_production, 44_LVBus684218_production, 44_LVBus684220_production, 44_LVBus684221_production, 44_LVBus684222_production, 44_LVBus684223_production, 44_LVBus684224_consumption, 44_LVBus684224_production, 44_LVBus684225_production, 44_LVBus684227_production, 44_LVBus684229_production, 44_LVBus684230_production, 44_LVBus684232_production, 44_LVBus684233_production, 44_LVBus684234_production, 44_LVBus684236_production, 44_LVBus684238_production, 44_LVBus684239_production, 44_LVBus684240_production, 44_LVBus684241_production, 44_LVBus684242_production, 44_LVBus684243_production, 44_LVBus684244_production, 44_LVBus684245_production, 44_LVBus684246_production, 44_LVBus684248_production, 44_LVBus684249_production, 44_LVBus684250_production, 44_LVBus684251_production, 44_LVBus684252_production, 44_LVBus684253_production, 44_LVBus684254_production, 44_LVBus684256_production, 44_LVBus684257_production, 44_LVBus684258_production, 44_LVBus684260_production, 44_LVBus684261_production, 44_LVBus684262_production, 44_LVBus684263_production, 44_LVBus684264_consumption, 44_LVBus684264_production, 44_LVBus684266_production, 44_LVBus684267_production, 44_LVBus684268_production, 44_LVBus684270_production, 44_LVBus684271_production, 44_LVBus684272_production, 44_LVBus684273_production, 44_LVBus684275_production, 44_LVBus684277_production, 44_LVBus684278_production, 44_LVBus684280_consumption, 44_LVBus684280_production, 44_LVBus684281_consumption, 44_LVBus684281_production, 44_LVBus684282_consumption, 44_LVBus684282_production, 44_LVBus684283_consumption, 44_LVBus684283_production, 44_LVBus684284_consumption, 44_LVBus684284_production, 44_LVBus684285_consumption, 44_LVBus684285_production, 44_LVBus684286_consumption, 44_LVBus684286_production, 44_LVBus684287_production, 44_LVBus684288_production, 44_LVBus684289_production, 44_LVBus684290_consumption, 44_LVBus684290_production, 44_LVBus684291_consumption, 44_LVBus684291_production, 44_LVBus684292_production, 44_LVBus684293_production, 44_LVBus684294_consumption, 44_LVBus684294_production, 44_LVBus684295_consumption, 44_LVBus684295_production, 44_LVBus684296_production, 44_LVBus684297_consumption, 44_LVBus684297_production, 44_LVBus684298_production, 44_LVBus684299_consumption, 44_LVBus684299_production, 44_LVBus684301_production, 44_LVBus684302_production, 44_LVBus684303_production, 44_LVBus684304_production, 44_LVBus684305_production, 44_LVBus684306_production, 44_LVBus684308_production, 44_LVBus684309_consumption, 44_LVBus684309_production, 44_LVBus684310_production, 44_LVBus684312_production, 44_LVBus684313_production, 44_LVBus684314_production, 44_LVBus684315_production, 44_LVBus684316_consumption, 44_LVBus684316_production, 44_LVBus684317_production, 44_LVBus684318_production, 44_MVLV57406_consumption, 44_MVLV57406_production, 44_MVLV58331_consumption, 44_MVLV58331_production.

## 9. Data Quality Summary

**Total findings:** 272 (0 errors, 4 warnings, 268 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  353 of 618 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.63 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  354 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684314_consumption`  
  Load '44_LVBus684314_consumption' has phase imbalance of 40.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684256_consumption`  
  Load '44_LVBus684256_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684185_consumption`  
  Load '44_LVBus684185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684050_consumption`  
  Load '44_LVBus684050_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683962_consumption`  
  Load '44_LVBus683962_consumption' has phase imbalance of 273.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684148_consumption`  
  Load '44_LVBus684148_consumption' has phase imbalance of 66.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684049_consumption`  
  Load '44_LVBus684049_consumption' has phase imbalance of 20.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683971_consumption`  
  Load '44_LVBus683971_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684146_consumption`  
  Load '44_LVBus684146_consumption' has phase imbalance of 59.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684068_consumption`  
  Load '44_LVBus684068_consumption' has phase imbalance of 251.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684257_consumption`  
  Load '44_LVBus684257_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684305_consumption`  
  Load '44_LVBus684305_consumption' has phase imbalance of 121.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684313_consumption`  
  Load '44_LVBus684313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684034_consumption`  
  Load '44_LVBus684034_consumption' has phase imbalance of 208.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683967_consumption`  
  Load '44_LVBus683967_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684031_consumption`  
  Load '44_LVBus684031_consumption' has phase imbalance of 81.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684293_consumption`  
  Load '44_LVBus684293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684155_consumption`  
  Load '44_LVBus684155_consumption' has phase imbalance of 86.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683959_consumption`  
  Load '44_LVBus683959_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684207_consumption`  
  Load '44_LVBus684207_consumption' has phase imbalance of 100.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684289_consumption`  
  Load '44_LVBus684289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683960_consumption`  
  Load '44_LVBus683960_consumption' has phase imbalance of 143.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684119_consumption`  
  Load '44_LVBus684119_consumption' has phase imbalance of 32.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683998_consumption`  
  Load '44_LVBus683998_consumption' has phase imbalance of 70.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684273_consumption`  
  Load '44_LVBus684273_consumption' has phase imbalance of 125.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684063_consumption`  
  Load '44_LVBus684063_consumption' has phase imbalance of 143.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684244_consumption`  
  Load '44_LVBus684244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683999_consumption`  
  Load '44_LVBus683999_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684251_consumption`  
  Load '44_LVBus684251_consumption' has phase imbalance of 48.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684025_consumption`  
  Load '44_LVBus684025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684304_consumption`  
  Load '44_LVBus684304_consumption' has phase imbalance of 253.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684143_consumption`  
  Load '44_LVBus684143_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684302_consumption`  
  Load '44_LVBus684302_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684175_consumption`  
  Load '44_LVBus684175_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684179_consumption`  
  Load '44_LVBus684179_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684131_consumption`  
  Load '44_LVBus684131_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683978_consumption`  
  Load '44_LVBus683978_consumption' has phase imbalance of 252.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684140_consumption`  
  Load '44_LVBus684140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684192_consumption`  
  Load '44_LVBus684192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683992_consumption`  
  Load '44_LVBus683992_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684170_consumption`  
  Load '44_LVBus684170_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684306_consumption`  
  Load '44_LVBus684306_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684267_consumption`  
  Load '44_LVBus684267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684058_consumption`  
  Load '44_LVBus684058_consumption' has phase imbalance of 98.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684199_consumption`  
  Load '44_LVBus684199_consumption' has phase imbalance of 271.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684222_consumption`  
  Load '44_LVBus684222_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684093_consumption`  
  Load '44_LVBus684093_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684033_consumption`  
  Load '44_LVBus684033_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684096_consumption`  
  Load '44_LVBus684096_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684078_consumption`  
  Load '44_LVBus684078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684054_consumption`  
  Load '44_LVBus684054_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684262_consumption`  
  Load '44_LVBus684262_consumption' has phase imbalance of 221.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684234_consumption`  
  Load '44_LVBus684234_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684092_consumption`  
  Load '44_LVBus684092_consumption' has phase imbalance of 177.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684194_consumption`  
  Load '44_LVBus684194_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683997_consumption`  
  Load '44_LVBus683997_consumption' has phase imbalance of 78.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684053_consumption`  
  Load '44_LVBus684053_consumption' has phase imbalance of 112.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683958_consumption`  
  Load '44_LVBus683958_consumption' has phase imbalance of 56.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684024_consumption`  
  Load '44_LVBus684024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684270_consumption`  
  Load '44_LVBus684270_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684128_consumption`  
  Load '44_LVBus684128_consumption' has phase imbalance of 70.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684043_consumption`  
  Load '44_LVBus684043_consumption' has phase imbalance of 40.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684317_consumption`  
  Load '44_LVBus684317_consumption' has phase imbalance of 24.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684103_consumption`  
  Load '44_LVBus684103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684004_consumption`  
  Load '44_LVBus684004_consumption' has phase imbalance of 98.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683969_consumption`  
  Load '44_LVBus683969_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684115_consumption`  
  Load '44_LVBus684115_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684015_consumption`  
  Load '44_LVBus684015_consumption' has phase imbalance of 21.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684209_consumption`  
  Load '44_LVBus684209_consumption' has phase imbalance of 181.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684149_consumption`  
  Load '44_LVBus684149_consumption' has phase imbalance of 75.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684268_consumption`  
  Load '44_LVBus684268_consumption' has phase imbalance of 125.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683991_consumption`  
  Load '44_LVBus683991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684275_consumption`  
  Load '44_LVBus684275_consumption' has phase imbalance of 101.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684081_consumption`  
  Load '44_LVBus684081_consumption' has phase imbalance of 158.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684223_consumption`  
  Load '44_LVBus684223_consumption' has phase imbalance of 207.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684118_consumption`  
  Load '44_LVBus684118_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684087_consumption`  
  Load '44_LVBus684087_consumption' has phase imbalance of 233.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684238_consumption`  
  Load '44_LVBus684238_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684221_consumption`  
  Load '44_LVBus684221_consumption' has phase imbalance of 59.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684229_consumption`  
  Load '44_LVBus684229_consumption' has phase imbalance of 41.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684012_consumption`  
  Load '44_LVBus684012_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684249_consumption`  
  Load '44_LVBus684249_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684220_consumption`  
  Load '44_LVBus684220_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684120_consumption`  
  Load '44_LVBus684120_consumption' has phase imbalance of 133.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684076_consumption`  
  Load '44_LVBus684076_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684315_consumption`  
  Load '44_LVBus684315_consumption' has phase imbalance of 220.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684000_consumption`  
  Load '44_LVBus684000_consumption' has phase imbalance of 140.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684002_consumption`  
  Load '44_LVBus684002_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684016_consumption`  
  Load '44_LVBus684016_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684009_consumption`  
  Load '44_LVBus684009_consumption' has phase imbalance of 258.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684070_consumption`  
  Load '44_LVBus684070_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684230_consumption`  
  Load '44_LVBus684230_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684241_consumption`  
  Load '44_LVBus684241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684165_consumption`  
  Load '44_LVBus684165_consumption' has phase imbalance of 266.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684052_consumption`  
  Load '44_LVBus684052_consumption' has phase imbalance of 64.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684127_consumption`  
  Load '44_LVBus684127_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684197_consumption`  
  Load '44_LVBus684197_consumption' has phase imbalance of 103.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684163_consumption`  
  Load '44_LVBus684163_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683966_consumption`  
  Load '44_LVBus683966_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684141_consumption`  
  Load '44_LVBus684141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683975_consumption`  
  Load '44_LVBus683975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684089_consumption`  
  Load '44_LVBus684089_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683982_consumption`  
  Load '44_LVBus683982_consumption' has phase imbalance of 142.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684157_consumption`  
  Load '44_LVBus684157_consumption' has phase imbalance of 230.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684198_consumption`  
  Load '44_LVBus684198_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684277_consumption`  
  Load '44_LVBus684277_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684008_consumption`  
  Load '44_LVBus684008_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683984_consumption`  
  Load '44_LVBus683984_consumption' has phase imbalance of 66.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684288_consumption`  
  Load '44_LVBus684288_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683964_consumption`  
  Load '44_LVBus683964_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683977_consumption`  
  Load '44_LVBus683977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683996_consumption`  
  Load '44_LVBus683996_consumption' has phase imbalance of 67.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684082_consumption`  
  Load '44_LVBus684082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683979_consumption`  
  Load '44_LVBus683979_consumption' has phase imbalance of 209.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684239_consumption`  
  Load '44_LVBus684239_consumption' has phase imbalance of 50.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684125_consumption`  
  Load '44_LVBus684125_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684028_consumption`  
  Load '44_LVBus684028_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684156_consumption`  
  Load '44_LVBus684156_consumption' has phase imbalance of 45.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684044_consumption`  
  Load '44_LVBus684044_consumption' has phase imbalance of 59.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684168_consumption`  
  Load '44_LVBus684168_consumption' has phase imbalance of 107.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684242_consumption`  
  Load '44_LVBus684242_consumption' has phase imbalance of 24.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684106_consumption`  
  Load '44_LVBus684106_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684164_consumption`  
  Load '44_LVBus684164_consumption' has phase imbalance of 257.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684227_consumption`  
  Load '44_LVBus684227_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684040_consumption`  
  Load '44_LVBus684040_consumption' has phase imbalance of 183.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684261_consumption`  
  Load '44_LVBus684261_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684080_consumption`  
  Load '44_LVBus684080_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684077_consumption`  
  Load '44_LVBus684077_consumption' has phase imbalance of 248.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684217_consumption`  
  Load '44_LVBus684217_consumption' has phase imbalance of 145.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684022_consumption`  
  Load '44_LVBus684022_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684258_consumption`  
  Load '44_LVBus684258_consumption' has phase imbalance of 216.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684204_consumption`  
  Load '44_LVBus684204_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684252_consumption`  
  Load '44_LVBus684252_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684216_consumption`  
  Load '44_LVBus684216_consumption' has phase imbalance of 72.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683993_consumption`  
  Load '44_LVBus683993_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684308_consumption`  
  Load '44_LVBus684308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684240_consumption`  
  Load '44_LVBus684240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684117_consumption`  
  Load '44_LVBus684117_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684099_consumption`  
  Load '44_LVBus684099_consumption' has phase imbalance of 195.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684061_consumption`  
  Load '44_LVBus684061_consumption' has phase imbalance of 251.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683976_consumption`  
  Load '44_LVBus683976_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683985_consumption`  
  Load '44_LVBus683985_consumption' has phase imbalance of 261.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684039_consumption`  
  Load '44_LVBus684039_consumption' has phase imbalance of 144.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683968_consumption`  
  Load '44_LVBus683968_consumption' has phase imbalance of 90.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684064_consumption`  
  Load '44_LVBus684064_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683970_consumption`  
  Load '44_LVBus683970_consumption' has phase imbalance of 100.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684026_consumption`  
  Load '44_LVBus684026_consumption' has phase imbalance of 90.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684246_consumption`  
  Load '44_LVBus684246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683973_consumption`  
  Load '44_LVBus683973_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684248_consumption`  
  Load '44_LVBus684248_consumption' has phase imbalance of 251.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684243_consumption`  
  Load '44_LVBus684243_consumption' has phase imbalance of 97.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684161_consumption`  
  Load '44_LVBus684161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684085_consumption`  
  Load '44_LVBus684085_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684037_consumption`  
  Load '44_LVBus684037_consumption' has phase imbalance of 128.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684191_consumption`  
  Load '44_LVBus684191_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684035_consumption`  
  Load '44_LVBus684035_consumption' has phase imbalance of 76.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684091_consumption`  
  Load '44_LVBus684091_consumption' has phase imbalance of 282.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684062_consumption`  
  Load '44_LVBus684062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684029_consumption`  
  Load '44_LVBus684029_consumption' has phase imbalance of 100.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684171_consumption`  
  Load '44_LVBus684171_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684090_consumption`  
  Load '44_LVBus684090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683995_consumption`  
  Load '44_LVBus683995_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683956_consumption`  
  Load '44_LVBus683956_consumption' has phase imbalance of 118.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684151_consumption`  
  Load '44_LVBus684151_consumption' has phase imbalance of 42.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684301_consumption`  
  Load '44_LVBus684301_consumption' has phase imbalance of 27.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684298_consumption`  
  Load '44_LVBus684298_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684095_consumption`  
  Load '44_LVBus684095_consumption' has phase imbalance of 28.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684154_consumption`  
  Load '44_LVBus684154_consumption' has phase imbalance of 55.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684108_consumption`  
  Load '44_LVBus684108_consumption' has phase imbalance of 47.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684060_consumption`  
  Load '44_LVBus684060_consumption' has phase imbalance of 93.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684292_consumption`  
  Load '44_LVBus684292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684195_consumption`  
  Load '44_LVBus684195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684215_consumption`  
  Load '44_LVBus684215_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684250_consumption`  
  Load '44_LVBus684250_consumption' has phase imbalance of 194.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684145_consumption`  
  Load '44_LVBus684145_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684303_consumption`  
  Load '44_LVBus684303_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684046_consumption`  
  Load '44_LVBus684046_consumption' has phase imbalance of 228.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684271_consumption`  
  Load '44_LVBus684271_consumption' has phase imbalance of 58.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683983_consumption`  
  Load '44_LVBus683983_consumption' has phase imbalance of 83.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684045_consumption`  
  Load '44_LVBus684045_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684147_consumption`  
  Load '44_LVBus684147_consumption' has phase imbalance of 155.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684167_consumption`  
  Load '44_LVBus684167_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684213_consumption`  
  Load '44_LVBus684213_consumption' has phase imbalance of 157.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684266_consumption`  
  Load '44_LVBus684266_consumption' has phase imbalance of 267.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684013_consumption`  
  Load '44_LVBus684013_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684312_consumption`  
  Load '44_LVBus684312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684116_consumption`  
  Load '44_LVBus684116_consumption' has phase imbalance of 72.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684254_consumption`  
  Load '44_LVBus684254_consumption' has phase imbalance of 236.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684225_consumption`  
  Load '44_LVBus684225_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684272_consumption`  
  Load '44_LVBus684272_consumption' has phase imbalance of 190.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684074_consumption`  
  Load '44_LVBus684074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684201_consumption`  
  Load '44_LVBus684201_consumption' has phase imbalance of 75.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684202_consumption`  
  Load '44_LVBus684202_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684178_consumption`  
  Load '44_LVBus684178_consumption' has phase imbalance of 274.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684296_consumption`  
  Load '44_LVBus684296_consumption' has phase imbalance of 88.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683961_consumption`  
  Load '44_LVBus683961_consumption' has phase imbalance of 224.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684278_consumption`  
  Load '44_LVBus684278_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684136_consumption`  
  Load '44_LVBus684136_consumption' has phase imbalance of 69.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684001_consumption`  
  Load '44_LVBus684001_consumption' has phase imbalance of 170.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684210_consumption`  
  Load '44_LVBus684210_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684142_consumption`  
  Load '44_LVBus684142_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684245_consumption`  
  Load '44_LVBus684245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683974_consumption`  
  Load '44_LVBus683974_consumption' has phase imbalance of 127.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684160_consumption`  
  Load '44_LVBus684160_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684079_consumption`  
  Load '44_LVBus684079_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684123_consumption`  
  Load '44_LVBus684123_consumption' has phase imbalance of 207.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684211_consumption`  
  Load '44_LVBus684211_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684003_consumption`  
  Load '44_LVBus684003_consumption' has phase imbalance of 144.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684253_consumption`  
  Load '44_LVBus684253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684129_consumption`  
  Load '44_LVBus684129_consumption' has phase imbalance of 230.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684121_consumption`  
  Load '44_LVBus684121_consumption' has phase imbalance of 139.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684162_consumption`  
  Load '44_LVBus684162_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684042_consumption`  
  Load '44_LVBus684042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684014_consumption`  
  Load '44_LVBus684014_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684075_consumption`  
  Load '44_LVBus684075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684287_consumption`  
  Load '44_LVBus684287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683957_consumption`  
  Load '44_LVBus683957_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684205_consumption`  
  Load '44_LVBus684205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684086_consumption`  
  Load '44_LVBus684086_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684206_consumption`  
  Load '44_LVBus684206_consumption' has phase imbalance of 170.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684218_consumption`  
  Load '44_LVBus684218_consumption' has phase imbalance of 272.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684011_consumption`  
  Load '44_LVBus684011_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683980_consumption`  
  Load '44_LVBus683980_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684101_consumption`  
  Load '44_LVBus684101_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683965_consumption`  
  Load '44_LVBus683965_consumption' has phase imbalance of 214.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684005_consumption`  
  Load '44_LVBus684005_consumption' has phase imbalance of 30.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684232_consumption`  
  Load '44_LVBus684232_consumption' has phase imbalance of 125.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684159_consumption`  
  Load '44_LVBus684159_consumption' has phase imbalance of 253.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684065_consumption`  
  Load '44_LVBus684065_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683989_consumption`  
  Load '44_LVBus683989_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684263_consumption`  
  Load '44_LVBus684263_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684126_consumption`  
  Load '44_LVBus684126_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684088_consumption`  
  Load '44_LVBus684088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684212_consumption`  
  Load '44_LVBus684212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684180_consumption`  
  Load '44_LVBus684180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684048_consumption`  
  Load '44_LVBus684048_consumption' has phase imbalance of 49.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684023_consumption`  
  Load '44_LVBus684023_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684102_consumption`  
  Load '44_LVBus684102_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684021_consumption`  
  Load '44_LVBus684021_consumption' has phase imbalance of 278.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684020_consumption`  
  Load '44_LVBus684020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684196_consumption`  
  Load '44_LVBus684196_consumption' has phase imbalance of 97.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684032_consumption`  
  Load '44_LVBus684032_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684183_consumption`  
  Load '44_LVBus684183_consumption' has phase imbalance of 61.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684236_consumption`  
  Load '44_LVBus684236_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus683990_consumption`  
  Load '44_LVBus683990_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684208_consumption`  
  Load '44_LVBus684208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684104_consumption`  
  Load '44_LVBus684104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684098_consumption`  
  Load '44_LVBus684098_consumption' has phase imbalance of 88.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684310_consumption`  
  Load '44_LVBus684310_consumption' has phase imbalance of 202.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684189_consumption`  
  Load '44_LVBus684189_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684260_consumption`  
  Load '44_LVBus684260_consumption' has phase imbalance of 82.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus684203_consumption`  
  Load '44_LVBus684203_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 618 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus684018' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  348 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  128 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 44_LVBus683957_consumption, 44_LVBus683959_consumption, 44_LVBus683961_consumption, 44_LVBus683962_consumption, 44_LVBus683964_consumption, 44_LVBus683969_consumption, 44_LVBus683971_consumption, 44_LVBus683975_consumption, 44_LVBus683976_consumption, 44_LVBus683977_consumption, 44_LVBus683980_consumption, 44_LVBus683985_consumption, 44_LVBus683989_consumption, 44_LVBus683991_consumption, 44_LVBus683992_consumption, 44_LVBus684001_consumption, 44_LVBus684009_consumption, 44_LVBus684012_consumption, 44_LVBus684013_consumption, 44_LVBus684016_consumption, 44_LVBus684020_consumption, 44_LVBus684021_consumption, 44_LVBus684022_consumption, 44_LVBus684023_consumption, 44_LVBus684024_consumption, 44_LVBus684025_consumption, 44_LVBus684032_consumption, 44_LVBus684033_consumption, 44_LVBus684034_consumption, 44_LVBus684040_consumption, 44_LVBus684042_consumption, 44_LVBus684045_consumption, 44_LVBus684054_consumption, 44_LVBus684061_consumption, 44_LVBus684062_consumption, 44_LVBus684065_consumption, 44_LVBus684068_consumption, 44_LVBus684070_consumption, 44_LVBus684074_consumption, 44_LVBus684075_consumption, 44_LVBus684076_consumption, 44_LVBus684077_consumption, 44_LVBus684078_consumption, 44_LVBus684079_consumption, 44_LVBus684081_consumption, 44_LVBus684082_consumption, 44_LVBus684086_consumption, 44_LVBus684087_consumption, 44_LVBus684088_consumption, 44_LVBus684089_consumption, 44_LVBus684090_consumption, 44_LVBus684091_consumption, 44_LVBus684092_consumption, 44_LVBus684093_consumption, 44_LVBus684099_consumption, 44_LVBus684102_consumption, 44_LVBus684103_consumption, 44_LVBus684104_consumption, 44_LVBus684115_consumption, 44_LVBus684117_consumption, 44_LVBus684118_consumption, 44_LVBus684123_consumption, 44_LVBus684126_consumption, 44_LVBus684127_consumption, 44_LVBus684129_consumption, 44_LVBus684140_consumption, 44_LVBus684141_consumption, 44_LVBus684145_consumption, 44_LVBus684147_consumption, 44_LVBus684157_consumption, 44_LVBus684159_consumption, 44_LVBus684161_consumption, 44_LVBus684162_consumption, 44_LVBus684163_consumption, 44_LVBus684165_consumption, 44_LVBus684167_consumption, 44_LVBus684170_consumption, 44_LVBus684171_consumption, 44_LVBus684178_consumption, 44_LVBus684180_consumption, 44_LVBus684185_consumption, 44_LVBus684192_consumption, 44_LVBus684194_consumption, 44_LVBus684195_consumption, 44_LVBus684199_consumption, 44_LVBus684203_consumption, 44_LVBus684205_consumption, 44_LVBus684208_consumption, 44_LVBus684209_consumption, 44_LVBus684210_consumption, 44_LVBus684211_consumption, 44_LVBus684212_consumption, 44_LVBus684213_consumption, 44_LVBus684215_consumption, 44_LVBus684218_consumption, 44_LVBus684222_consumption, 44_LVBus684225_consumption, 44_LVBus684240_consumption, 44_LVBus684241_consumption, 44_LVBus684244_consumption, 44_LVBus684245_consumption, 44_LVBus684246_consumption, 44_LVBus684248_consumption, 44_LVBus684249_consumption, 44_LVBus684252_consumption, 44_LVBus684253_consumption, 44_LVBus684254_consumption, 44_LVBus684256_consumption, 44_LVBus684261_consumption, 44_LVBus684263_consumption, 44_LVBus684266_consumption, 44_LVBus684267_consumption, 44_LVBus684270_consumption, 44_LVBus684272_consumption, 44_LVBus684278_consumption, 44_LVBus684287_consumption, 44_LVBus684288_consumption, 44_LVBus684289_consumption, 44_LVBus684292_consumption, 44_LVBus684293_consumption, 44_LVBus684298_consumption, 44_LVBus684302_consumption, 44_LVBus684304_consumption, 44_LVBus684308_consumption, 44_LVBus684310_consumption, 44_LVBus684312_consumption, 44_LVBus684313_consumption, 44_LVBus684315_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  309 group(s) of loads (618 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  4 group(s) of series lines (12 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  354 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus683955_production, 44_LVBus683956_production, 44_LVBus683957_production, 44_LVBus683958_production, 44_LVBus683959_production, 44_LVBus683960_production, 44_LVBus683961_production, 44_LVBus683962_production, 44_LVBus683964_production, 44_LVBus683965_production, 44_LVBus683966_production, 44_LVBus683967_production, 44_LVBus683968_production, 44_LVBus683969_production, 44_LVBus683970_production, 44_LVBus683971_production, 44_LVBus683973_production, 44_LVBus683974_production, 44_LVBus683975_production, 44_LVBus683976_production, 44_LVBus683977_production, 44_LVBus683978_production, 44_LVBus683979_production, 44_LVBus683980_production, 44_LVBus683982_production, 44_LVBus683983_production, 44_LVBus683984_production, 44_LVBus683985_production, 44_LVBus683986_production, 44_LVBus683987_consumption, 44_LVBus683987_production, 44_LVBus683988_consumption, 44_LVBus683988_production, 44_LVBus683989_production, 44_LVBus683990_production, 44_LVBus683991_production, 44_LVBus683992_production, 44_LVBus683993_production, 44_LVBus683995_production, 44_LVBus683996_production, 44_LVBus683997_production, 44_LVBus683998_production, 44_LVBus683999_production, 44_LVBus684000_production, 44_LVBus684001_production, 44_LVBus684002_production, 44_LVBus684003_production, 44_LVBus684004_production, 44_LVBus684005_production, 44_LVBus684007_consumption, 44_LVBus684007_production, 44_LVBus684008_production, 44_LVBus684009_production, 44_LVBus684010_production, 44_LVBus684011_production, 44_LVBus684012_production, 44_LVBus684013_production, 44_LVBus684014_production, 44_LVBus684015_production, 44_LVBus684016_production, 44_LVBus684018_production, 44_LVBus684020_production, 44_LVBus684021_production, 44_LVBus684022_production, 44_LVBus684023_production, 44_LVBus684024_production, 44_LVBus684025_production, 44_LVBus684026_production, 44_LVBus684028_production, 44_LVBus684029_production, 44_LVBus684031_production, 44_LVBus684032_production, 44_LVBus684033_production, 44_LVBus684034_production, 44_LVBus684035_production, 44_LVBus684037_production, 44_LVBus684039_production, 44_LVBus684040_production, 44_LVBus684042_production, 44_LVBus684043_production, 44_LVBus684044_production, 44_LVBus684045_production, 44_LVBus684046_production, 44_LVBus684048_production, 44_LVBus684049_production, 44_LVBus684050_production, 44_LVBus684052_production, 44_LVBus684053_production, 44_LVBus684054_production, 44_LVBus684055_consumption, 44_LVBus684055_production, 44_LVBus684056_consumption, 44_LVBus684056_production, 44_LVBus684057_consumption, 44_LVBus684057_production, 44_LVBus684058_production, 44_LVBus684060_production, 44_LVBus684061_production, 44_LVBus684062_production, 44_LVBus684063_production, 44_LVBus684064_production, 44_LVBus684065_production, 44_LVBus684067_consumption, 44_LVBus684067_production, 44_LVBus684068_production, 44_LVBus684070_production, 44_LVBus684071_consumption, 44_LVBus684071_production, 44_LVBus684072_consumption, 44_LVBus684072_production, 44_LVBus684074_production, 44_LVBus684075_production, 44_LVBus684076_production, 44_LVBus684077_production, 44_LVBus684078_production, 44_LVBus684079_production, 44_LVBus684080_production, 44_LVBus684081_production, 44_LVBus684082_production, 44_LVBus684084_consumption, 44_LVBus684084_production, 44_LVBus684085_production, 44_LVBus684086_production, 44_LVBus684087_production, 44_LVBus684088_production, 44_LVBus684089_production, 44_LVBus684090_production, 44_LVBus684091_production, 44_LVBus684092_production, 44_LVBus684093_production, 44_LVBus684095_production, 44_LVBus684096_production, 44_LVBus684097_production, 44_LVBus684098_production, 44_LVBus684099_production, 44_LVBus684101_production, 44_LVBus684102_production, 44_LVBus684103_production, 44_LVBus684104_production, 44_LVBus684105_consumption, 44_LVBus684105_production, 44_LVBus684106_production, 44_LVBus684107_consumption, 44_LVBus684107_production, 44_LVBus684108_production, 44_LVBus684109_consumption, 44_LVBus684109_production, 44_LVBus684111_consumption, 44_LVBus684111_production, 44_LVBus684113_production, 44_LVBus684115_production, 44_LVBus684116_production, 44_LVBus684117_production, 44_LVBus684118_production, 44_LVBus684119_production, 44_LVBus684120_production, 44_LVBus684121_production, 44_LVBus684123_production, 44_LVBus684125_production, 44_LVBus684126_production, 44_LVBus684127_production, 44_LVBus684128_production, 44_LVBus684129_production, 44_LVBus684130_production, 44_LVBus684131_production, 44_LVBus684133_consumption, 44_LVBus684133_production, 44_LVBus684134_consumption, 44_LVBus684134_production, 44_LVBus684135_consumption, 44_LVBus684135_production, 44_LVBus684136_production, 44_LVBus684138_production, 44_LVBus684140_production, 44_LVBus684141_production, 44_LVBus684142_production, 44_LVBus684143_production, 44_LVBus684145_production, 44_LVBus684146_production, 44_LVBus684147_production, 44_LVBus684148_production, 44_LVBus684149_production, 44_LVBus684151_production, 44_LVBus684152_consumption, 44_LVBus684152_production, 44_LVBus684153_production, 44_LVBus684154_production, 44_LVBus684155_production, 44_LVBus684156_production, 44_LVBus684157_production, 44_LVBus684159_production, 44_LVBus684160_production, 44_LVBus684161_production, 44_LVBus684162_production, 44_LVBus684163_production, 44_LVBus684164_production, 44_LVBus684165_production, 44_LVBus684167_production, 44_LVBus684168_production, 44_LVBus684170_production, 44_LVBus684171_production, 44_LVBus684173_consumption, 44_LVBus684173_production, 44_LVBus684174_consumption, 44_LVBus684174_production, 44_LVBus684175_production, 44_LVBus684176_consumption, 44_LVBus684176_production, 44_LVBus684178_production, 44_LVBus684179_production, 44_LVBus684180_production, 44_LVBus684181_consumption, 44_LVBus684181_production, 44_LVBus684182_consumption, 44_LVBus684182_production, 44_LVBus684183_production, 44_LVBus684185_production, 44_LVBus684186_consumption, 44_LVBus684186_production, 44_LVBus684187_consumption, 44_LVBus684187_production, 44_LVBus684188_consumption, 44_LVBus684188_production, 44_LVBus684189_production, 44_LVBus684191_production, 44_LVBus684192_production, 44_LVBus684193_production, 44_LVBus684194_production, 44_LVBus684195_production, 44_LVBus684196_production, 44_LVBus684197_production, 44_LVBus684198_production, 44_LVBus684199_production, 44_LVBus684201_production, 44_LVBus684202_production, 44_LVBus684203_production, 44_LVBus684204_production, 44_LVBus684205_production, 44_LVBus684206_production, 44_LVBus684207_production, 44_LVBus684208_production, 44_LVBus684209_production, 44_LVBus684210_production, 44_LVBus684211_production, 44_LVBus684212_production, 44_LVBus684213_production, 44_LVBus684215_production, 44_LVBus684216_production, 44_LVBus684217_production, 44_LVBus684218_production, 44_LVBus684220_production, 44_LVBus684221_production, 44_LVBus684222_production, 44_LVBus684223_production, 44_LVBus684224_consumption, 44_LVBus684224_production, 44_LVBus684225_production, 44_LVBus684227_production, 44_LVBus684229_production, 44_LVBus684230_production, 44_LVBus684232_production, 44_LVBus684233_production, 44_LVBus684234_production, 44_LVBus684236_production, 44_LVBus684238_production, 44_LVBus684239_production, 44_LVBus684240_production, 44_LVBus684241_production, 44_LVBus684242_production, 44_LVBus684243_production, 44_LVBus684244_production, 44_LVBus684245_production, 44_LVBus684246_production, 44_LVBus684248_production, 44_LVBus684249_production, 44_LVBus684250_production, 44_LVBus684251_production, 44_LVBus684252_production, 44_LVBus684253_production, 44_LVBus684254_production, 44_LVBus684256_production, 44_LVBus684257_production, 44_LVBus684258_production, 44_LVBus684260_production, 44_LVBus684261_production, 44_LVBus684262_production, 44_LVBus684263_production, 44_LVBus684264_consumption, 44_LVBus684264_production, 44_LVBus684266_production, 44_LVBus684267_production, 44_LVBus684268_production, 44_LVBus684270_production, 44_LVBus684271_production, 44_LVBus684272_production, 44_LVBus684273_production, 44_LVBus684275_production, 44_LVBus684277_production, 44_LVBus684278_production, 44_LVBus684280_consumption, 44_LVBus684280_production, 44_LVBus684281_consumption, 44_LVBus684281_production, 44_LVBus684282_consumption, 44_LVBus684282_production, 44_LVBus684283_consumption, 44_LVBus684283_production, 44_LVBus684284_consumption, 44_LVBus684284_production, 44_LVBus684285_consumption, 44_LVBus684285_production, 44_LVBus684286_consumption, 44_LVBus684286_production, 44_LVBus684287_production, 44_LVBus684288_production, 44_LVBus684289_production, 44_LVBus684290_consumption, 44_LVBus684290_production, 44_LVBus684291_consumption, 44_LVBus684291_production, 44_LVBus684292_production, 44_LVBus684293_production, 44_LVBus684294_consumption, 44_LVBus684294_production, 44_LVBus684295_consumption, 44_LVBus684295_production, 44_LVBus684296_production, 44_LVBus684297_consumption, 44_LVBus684297_production, 44_LVBus684298_production, 44_LVBus684299_consumption, 44_LVBus684299_production, 44_LVBus684301_production, 44_LVBus684302_production, 44_LVBus684303_production, 44_LVBus684304_production, 44_LVBus684305_production, 44_LVBus684306_production, 44_LVBus684308_production, 44_LVBus684309_consumption, 44_LVBus684309_production, 44_LVBus684310_production, 44_LVBus684312_production, 44_LVBus684313_production, 44_LVBus684314_production, 44_LVBus684315_production, 44_LVBus684316_consumption, 44_LVBus684316_production, 44_LVBus684317_production, 44_LVBus684318_production, 44_MVLV57406_consumption, 44_MVLV57406_production, 44_MVLV58331_consumption, 44_MVLV58331_production.

