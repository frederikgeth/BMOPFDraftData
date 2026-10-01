# BMOPF Network Summary: 24_MVFeeder1448

**Generated:** 2026-10-01 23:33:58  
**Findings:** 0 errors · 5 warnings · 300 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 41 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 526 |  |
| line | 484 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 802 | 2.242 MW, 672.5 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 41 |  |
| switch | 0 |  |
| transformer | 41 | Dyn11×41 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 100 | 99 | 32 | 0 |
| LV_236V | 236.0 V | 426 | 385 | 770 | 0 |

**Transformer transitions:**

- `24_MVLV79880_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV25166_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV10016_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV73813_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV29927_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV70372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV02929_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV37083_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV35057_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV80430_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV06920_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14106_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV10477_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV58648_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14835_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV18943_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV89612_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV22080_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV85293_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV22078_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV71676_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV06665_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV27367_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV60220_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV86379_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV28301_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV10745_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV70017_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV25265_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV01069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV35065_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV30109_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV10902_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV45876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV39098_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV18955_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36204_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV59570_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV24869_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV56426_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69646_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 8 |
| Degree-1 buses | 190 |
| Tree depth (max hops) | 34 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 526 | 1 | 525 | 0 | 0 | 0 |
| Tier LV_236V | 426 | 41 | 385 | 0 | 0 | 0 |
| Tier MV_11.8kV | 100 | 1 | 99 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 41; skipped invalid branches: 0.

Galvanic zones: 42; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 24_MVBus47361 | MV_11.8kV | 100 | 0 | 0 | 41 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2004 declared bus terminals; 1837 mapped line/closed-switch conductor edges; 167 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 30400.0 | 2.724 | 2406 |
| q_nom | 0.0 | 9110.0 | 2.724 | 2406 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.46 | 2260.0 | 1.531 | 484 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.686 | 41 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 497 of 802 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165093_consumption' has phase imbalance of 146.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164898_consumption' has phase imbalance of 70.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164761_consumption' has phase imbalance of 263.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165091_consumption' has phase imbalance of 94.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165176_consumption' has phase imbalance of 200.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164958_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164888_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165114_consumption' has phase imbalance of 32.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165123_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165168_consumption' has phase imbalance of 297.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164802_consumption' has phase imbalance of 157.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164960_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164944_consumption' has phase imbalance of 266.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164941_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164967_consumption' has phase imbalance of 267.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164862_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164823_consumption' has phase imbalance of 289.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164782_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164821_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165047_consumption' has phase imbalance of 186.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164954_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164921_consumption' has phase imbalance of 89.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165181_consumption' has phase imbalance of 198.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164896_consumption' has phase imbalance of 142.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165016_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164887_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164865_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164711_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834022_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165048_consumption' has phase imbalance of 176.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164933_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164806_consumption' has phase imbalance of 168.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164805_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165151_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164804_consumption' has phase imbalance of 214.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164815_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165001_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164957_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164769_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164961_consumption' has phase imbalance of 24.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164895_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165088_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165012_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164825_consumption' has phase imbalance of 165.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165172_consumption' has phase imbalance of 256.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164920_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164956_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165084_consumption' has phase imbalance of 33.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164909_consumption' has phase imbalance of 198.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164814_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164760_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165140_consumption' has phase imbalance of 105.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164820_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164753_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165108_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164785_consumption' has phase imbalance of 244.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164964_consumption' has phase imbalance of 260.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164722_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164974_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165023_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164911_consumption' has phase imbalance of 229.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165128_consumption' has phase imbalance of 196.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165160_consumption' has phase imbalance of 149.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165127_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165011_consumption' has phase imbalance of 274.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165152_consumption' has phase imbalance of 122.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165050_consumption' has phase imbalance of 223.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165073_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164781_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164963_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164710_consumption' has phase imbalance of 25.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164946_consumption' has phase imbalance of 263.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164945_consumption' has phase imbalance of 51.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164917_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165121_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165025_consumption' has phase imbalance of 83.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165051_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164813_consumption' has phase imbalance of 210.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165154_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164959_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164829_consumption' has phase imbalance of 97.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164830_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164834_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165028_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165126_consumption' has phase imbalance of 277.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164916_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165118_consumption' has phase imbalance of 241.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165149_consumption' has phase imbalance of 221.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165089_consumption' has phase imbalance of 251.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164996_consumption' has phase imbalance of 115.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164838_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165132_consumption' has phase imbalance of 48.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165049_consumption' has phase imbalance of 261.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165002_consumption' has phase imbalance of 146.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165155_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164971_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164918_consumption' has phase imbalance of 127.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164839_consumption' has phase imbalance of 145.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164866_consumption' has phase imbalance of 148.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165131_consumption' has phase imbalance of 116.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164979_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164726_consumption' has phase imbalance of 237.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164844_consumption' has phase imbalance of 262.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165055_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164870_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834016_consumption' has phase imbalance of 221.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164914_consumption' has phase imbalance of 121.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165167_consumption' has phase imbalance of 141.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164892_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164712_consumption' has phase imbalance of 64.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164847_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165136_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164872_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165113_consumption' has phase imbalance of 33.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164905_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164713_consumption' has phase imbalance of 257.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164745_consumption' has phase imbalance of 223.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165018_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165105_consumption' has phase imbalance of 50.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164861_consumption' has phase imbalance of 73.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164787_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165054_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164885_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834023_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834024_consumption' has phase imbalance of 178.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164882_consumption' has phase imbalance of 281.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164751_consumption' has phase imbalance of 124.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164835_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164903_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164902_consumption' has phase imbalance of 134.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165006_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165000_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165014_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165027_consumption' has phase imbalance of 234.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165102_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164843_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164807_consumption' has phase imbalance of 118.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164937_consumption' has phase imbalance of 275.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165046_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164811_consumption' has phase imbalance of 249.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165008_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164832_consumption' has phase imbalance of 268.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164886_consumption' has phase imbalance of 100.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164755_consumption' has phase imbalance of 256.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164788_consumption' has phase imbalance of 270.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165005_consumption' has phase imbalance of 39.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164780_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164953_consumption' has phase imbalance of 117.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165056_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164940_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164912_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165117_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165060_consumption' has phase imbalance of 281.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164748_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165007_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165170_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164883_consumption' has phase imbalance of 233.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164880_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834019_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834017_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164955_consumption' has phase imbalance of 217.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165090_consumption' has phase imbalance of 23.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165052_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164966_consumption' has phase imbalance of 57.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164984_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164936_consumption' has phase imbalance of 23.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164900_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164851_consumption' has phase imbalance of 146.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164818_consumption' has phase imbalance of 228.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164919_consumption' has phase imbalance of 168.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165158_consumption' has phase imbalance of 107.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164842_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164860_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164978_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164910_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164824_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165077_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164923_consumption' has phase imbalance of 134.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164925_consumption' has phase imbalance of 217.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164715_consumption' has phase imbalance of 143.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164871_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164809_consumption' has phase imbalance of 130.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164934_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164973_consumption' has phase imbalance of 260.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165171_consumption' has phase imbalance of 54.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164792_consumption' has phase imbalance of 242.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165041_consumption' has phase imbalance of 222.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164831_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165138_consumption' has phase imbalance of 109.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164889_consumption' has phase imbalance of 146.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164709_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165115_consumption' has phase imbalance of 184.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164943_consumption' has phase imbalance of 72.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164901_consumption' has phase imbalance of 113.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165173_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164890_consumption' has phase imbalance of 220.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus165174_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus164746_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 802 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus164950' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus164856' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.242 MW |
| Total load Q | 672.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 24_MVLV79880_Transformer | 440.0 kVA | 43.3% |
| 24_MVLV25166_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV10016_Transformer | 110.0 kVA | 5.3% |
| 24_MVLV73813_Transformer | 275.0 kVA | 12.9% |
| 24_MVLV29927_Transformer | 693.0 kVA | 44.7% |
| 24_MVLV70372_Transformer | 440.0 kVA | 24.9% |
| 24_MVLV02929_Transformer | 110.0 kVA | 2.7% |
| 24_MVLV37083_Transformer | 440.0 kVA | 18.0% |
| 24_MVLV35057_Transformer | 275.0 kVA | 35.2% |
| 24_MVLV80430_Transformer | 176.0 kVA | 2.0% |
| 24_MVLV06920_Transformer | 110.0 kVA | 0.7% |
| 24_MVLV14106_Transformer | 110.0 kVA | 9.4% |
| 24_MVLV10477_Transformer | 275.0 kVA | 24.1% |
| 24_MVLV58648_Transformer | 275.0 kVA | 19.5% |
| 24_MVLV14835_Transformer | 693.0 kVA | 19.9% |
| 24_MVLV18943_Transformer | 176.0 kVA | 10.6% |
| 24_MVLV89612_Transformer | 110.0 kVA | 1.2% |
| 24_MVLV22080_Transformer | 440.0 kVA | 42.0% |
| 24_MVLV85293_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV22078_Transformer | 110.0 kVA | 3.4% |
| 24_MVLV71676_Transformer | 110.0 kVA | 2.7% |
| 24_MVLV06665_Transformer | 110.0 kVA | 11.4% |
| 24_MVLV27367_Transformer | 693.0 kVA | 32.4% |
| 24_MVLV60220_Transformer | 275.0 kVA | 22.2% |
| 24_MVLV86379_Transformer | 440.0 kVA | 24.3% |
| 24_MVLV28301_Transformer | 110.0 kVA | 19.6% |
| 24_MVLV10745_Transformer | 110.0 kVA | 2.7% |
| 24_MVLV70017_Transformer | 275.0 kVA | 18.8% |
| 24_MVLV25265_Transformer | 110.0 kVA | 16.9% |
| 24_MVLV01069_Transformer | 275.0 kVA | 29.8% |
| 24_MVLV35065_Transformer | 110.0 kVA | 1.9% |
| 24_MVLV30109_Transformer | 275.0 kVA | 13.3% |
| 24_MVLV10902_Transformer | 110.0 kVA | 2.8% |
| 24_MVLV45876_Transformer | 440.0 kVA | 35.6% |
| 24_MVLV39098_Transformer | 176.0 kVA | 10.9% |
| 24_MVLV18955_Transformer | 110.0 kVA | 4.8% |
| 24_MVLV36204_Transformer | 275.0 kVA | 24.4% |
| 24_MVLV59570_Transformer | 110.0 kVA | 10.2% |
| 24_MVLV24869_Transformer | 440.0 kVA | 31.0% |
| 24_MVLV56426_Transformer | 110.0 kVA | 1.8% |
| 24_MVLV69646_Transformer | 110.0 kVA | 4.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.24 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus165095' (LV, 0.24 kV) has an electrical reach of 13.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus164856' (LV, 0.24 kV) has an electrical reach of 13.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 526 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 526 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 41 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 100 |
| LV_236V | 4-wire | 426 / 426 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 426 |
| Neutral branches | 385 |
| Grounding points | 41 |
| Neutral sections | 41 |
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
| 11.78 kV | 100 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 42 |
| Islands without voltage reference | 0 |
| Line impedance spread | 5190.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 426 / 100 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 498 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 498 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus164709_production, 24_LVBus164710_production, 24_LVBus164711_production, 24_LVBus164712_production, 24_LVBus164713_production, 24_LVBus164715_production, 24_LVBus164717_consumption, 24_LVBus164717_production, 24_LVBus164719_consumption, 24_LVBus164719_production, 24_LVBus164720_consumption, 24_LVBus164720_production, 24_LVBus164721_production, 24_LVBus164722_production, 24_LVBus164726_production, 24_LVBus164727_consumption, 24_LVBus164727_production, 24_LVBus164728_consumption, 24_LVBus164728_production, 24_LVBus164729_consumption, 24_LVBus164729_production, 24_LVBus164730_production, 24_LVBus164734_consumption, 24_LVBus164734_production, 24_LVBus164735_consumption, 24_LVBus164735_production, 24_LVBus164736_consumption, 24_LVBus164736_production, 24_LVBus164737_production, 24_LVBus164738_consumption, 24_LVBus164738_production, 24_LVBus164739_consumption, 24_LVBus164739_production, 24_LVBus164741_consumption, 24_LVBus164741_production, 24_LVBus164742_consumption, 24_LVBus164742_production, 24_LVBus164743_consumption, 24_LVBus164743_production, 24_LVBus164744_production, 24_LVBus164745_production, 24_LVBus164746_production, 24_LVBus164748_production, 24_LVBus164749_production, 24_LVBus164750_production, 24_LVBus164751_production, 24_LVBus164752_production, 24_LVBus164753_production, 24_LVBus164754_consumption, 24_LVBus164754_production, 24_LVBus164755_production, 24_LVBus164756_production, 24_LVBus164757_production, 24_LVBus164758_production, 24_LVBus164759_production, 24_LVBus164760_production, 24_LVBus164761_production, 24_LVBus164763_production, 24_LVBus164765_consumption, 24_LVBus164765_production, 24_LVBus164766_production, 24_LVBus164767_consumption, 24_LVBus164767_production, 24_LVBus164768_production, 24_LVBus164769_production, 24_LVBus164771_consumption, 24_LVBus164771_production, 24_LVBus164772_consumption, 24_LVBus164772_production, 24_LVBus164773_production, 24_LVBus164775_consumption, 24_LVBus164775_production, 24_LVBus164776_production, 24_LVBus164778_production, 24_LVBus164780_production, 24_LVBus164781_production, 24_LVBus164782_production, 24_LVBus164784_consumption, 24_LVBus164784_production, 24_LVBus164785_production, 24_LVBus164786_production, 24_LVBus164787_production, 24_LVBus164788_production, 24_LVBus164790_consumption, 24_LVBus164790_production, 24_LVBus164791_consumption, 24_LVBus164791_production, 24_LVBus164792_production, 24_LVBus164794_consumption, 24_LVBus164794_production, 24_LVBus164795_consumption, 24_LVBus164795_production, 24_LVBus164796_consumption, 24_LVBus164796_production, 24_LVBus164797_consumption, 24_LVBus164797_production, 24_LVBus164798_consumption, 24_LVBus164798_production, 24_LVBus164799_production, 24_LVBus164800_production, 24_LVBus164802_production, 24_LVBus164803_production, 24_LVBus164804_production, 24_LVBus164805_production, 24_LVBus164806_production, 24_LVBus164807_production, 24_LVBus164809_production, 24_LVBus164810_production, 24_LVBus164811_production, 24_LVBus164813_production, 24_LVBus164814_production, 24_LVBus164815_production, 24_LVBus164816_production, 24_LVBus164817_production, 24_LVBus164818_production, 24_LVBus164819_production, 24_LVBus164820_production, 24_LVBus164821_production, 24_LVBus164823_production, 24_LVBus164824_production, 24_LVBus164825_production, 24_LVBus164827_consumption, 24_LVBus164827_production, 24_LVBus164829_production, 24_LVBus164830_production, 24_LVBus164831_production, 24_LVBus164832_production, 24_LVBus164834_production, 24_LVBus164835_production, 24_LVBus164836_production, 24_LVBus164837_production, 24_LVBus164838_production, 24_LVBus164839_production, 24_LVBus164840_consumption, 24_LVBus164840_production, 24_LVBus164842_production, 24_LVBus164843_production, 24_LVBus164844_production, 24_LVBus164845_production, 24_LVBus164846_consumption, 24_LVBus164846_production, 24_LVBus164847_production, 24_LVBus164848_consumption, 24_LVBus164848_production, 24_LVBus164850_production, 24_LVBus164851_production, 24_LVBus164853_consumption, 24_LVBus164853_production, 24_LVBus164856_production, 24_LVBus164858_consumption, 24_LVBus164858_production, 24_LVBus164859_production, 24_LVBus164860_production, 24_LVBus164861_production, 24_LVBus164862_production, 24_LVBus164863_production, 24_LVBus164864_production, 24_LVBus164865_production, 24_LVBus164866_production, 24_LVBus164868_production, 24_LVBus164870_production, 24_LVBus164871_production, 24_LVBus164872_production, 24_LVBus164873_production, 24_LVBus164875_production, 24_LVBus164877_production, 24_LVBus164878_production, 24_LVBus164879_consumption, 24_LVBus164879_production, 24_LVBus164880_production, 24_LVBus164882_production, 24_LVBus164883_production, 24_LVBus164885_production, 24_LVBus164886_production, 24_LVBus164887_production, 24_LVBus164888_production, 24_LVBus164889_production, 24_LVBus164890_production, 24_LVBus164891_production, 24_LVBus164892_production, 24_LVBus164893_production, 24_LVBus164895_production, 24_LVBus164896_production, 24_LVBus164897_production, 24_LVBus164898_production, 24_LVBus164900_production, 24_LVBus164901_production, 24_LVBus164902_production, 24_LVBus164903_production, 24_LVBus164904_production, 24_LVBus164905_production, 24_LVBus164906_production, 24_LVBus164907_consumption, 24_LVBus164907_production, 24_LVBus164909_production, 24_LVBus164910_production, 24_LVBus164911_production, 24_LVBus164912_production, 24_LVBus164914_production, 24_LVBus164916_production, 24_LVBus164917_production, 24_LVBus164918_production, 24_LVBus164919_production, 24_LVBus164920_production, 24_LVBus164921_production, 24_LVBus164923_production, 24_LVBus164924_production, 24_LVBus164925_production, 24_LVBus164926_production, 24_LVBus164927_production, 24_LVBus164928_production, 24_LVBus164932_production, 24_LVBus164933_production, 24_LVBus164934_production, 24_LVBus164935_consumption, 24_LVBus164935_production, 24_LVBus164936_production, 24_LVBus164937_production, 24_LVBus164939_consumption, 24_LVBus164939_production, 24_LVBus164940_production, 24_LVBus164941_production, 24_LVBus164942_production, 24_LVBus164943_production, 24_LVBus164944_production, 24_LVBus164945_production, 24_LVBus164946_production, 24_LVBus164950_production, 24_LVBus164951_consumption, 24_LVBus164951_production, 24_LVBus164953_production, 24_LVBus164954_production, 24_LVBus164955_production, 24_LVBus164956_production, 24_LVBus164957_production, 24_LVBus164958_production, 24_LVBus164959_production, 24_LVBus164960_production, 24_LVBus164961_production, 24_LVBus164963_production, 24_LVBus164964_production, 24_LVBus164965_consumption, 24_LVBus164965_production, 24_LVBus164966_production, 24_LVBus164967_production, 24_LVBus164970_consumption, 24_LVBus164970_production, 24_LVBus164971_production, 24_LVBus164972_production, 24_LVBus164973_production, 24_LVBus164974_production, 24_LVBus164975_production, 24_LVBus164977_consumption, 24_LVBus164977_production, 24_LVBus164978_production, 24_LVBus164979_production, 24_LVBus164980_consumption, 24_LVBus164980_production, 24_LVBus164981_consumption, 24_LVBus164981_production, 24_LVBus164982_production, 24_LVBus164983_consumption, 24_LVBus164983_production, 24_LVBus164984_production, 24_LVBus164992_consumption, 24_LVBus164992_production, 24_LVBus164993_production, 24_LVBus164994_production, 24_LVBus164995_consumption, 24_LVBus164995_production, 24_LVBus164996_production, 24_LVBus164997_consumption, 24_LVBus164997_production, 24_LVBus164998_consumption, 24_LVBus164998_production, 24_LVBus164999_production, 24_LVBus165000_production, 24_LVBus165001_production, 24_LVBus165002_production, 24_LVBus165004_production, 24_LVBus165005_production, 24_LVBus165006_production, 24_LVBus165007_production, 24_LVBus165008_production, 24_LVBus165009_production, 24_LVBus165011_production, 24_LVBus165012_production, 24_LVBus165013_consumption, 24_LVBus165013_production, 24_LVBus165014_production, 24_LVBus165015_consumption, 24_LVBus165015_production, 24_LVBus165016_production, 24_LVBus165017_production, 24_LVBus165018_production, 24_LVBus165020_production, 24_LVBus165022_production, 24_LVBus165023_production, 24_LVBus165025_production, 24_LVBus165027_production, 24_LVBus165028_production, 24_LVBus165029_production, 24_LVBus165030_production, 24_LVBus165031_production, 24_LVBus165033_production, 24_LVBus165034_production, 24_LVBus165035_production, 24_LVBus165036_consumption, 24_LVBus165036_production, 24_LVBus165037_production, 24_LVBus165039_production, 24_LVBus165040_consumption, 24_LVBus165040_production, 24_LVBus165041_production, 24_LVBus165042_production, 24_LVBus165043_production, 24_LVBus165044_consumption, 24_LVBus165044_production, 24_LVBus165046_production, 24_LVBus165047_production, 24_LVBus165048_production, 24_LVBus165049_production, 24_LVBus165050_production, 24_LVBus165051_production, 24_LVBus165052_production, 24_LVBus165054_production, 24_LVBus165055_production, 24_LVBus165056_production, 24_LVBus165059_consumption, 24_LVBus165059_production, 24_LVBus165060_production, 24_LVBus165062_consumption, 24_LVBus165062_production, 24_LVBus165064_consumption, 24_LVBus165064_production, 24_LVBus165067_production, 24_LVBus165068_production, 24_LVBus165069_production, 24_LVBus165070_production, 24_LVBus165071_production, 24_LVBus165072_production, 24_LVBus165073_production, 24_LVBus165074_production, 24_LVBus165075_production, 24_LVBus165076_production, 24_LVBus165077_production, 24_LVBus165078_production, 24_LVBus165079_production, 24_LVBus165083_consumption, 24_LVBus165083_production, 24_LVBus165084_production, 24_LVBus165085_production, 24_LVBus165086_production, 24_LVBus165088_production, 24_LVBus165089_production, 24_LVBus165090_production, 24_LVBus165091_production, 24_LVBus165093_production, 24_LVBus165095_production, 24_LVBus165097_production, 24_LVBus165098_consumption, 24_LVBus165098_production, 24_LVBus165099_production, 24_LVBus165101_consumption, 24_LVBus165101_production, 24_LVBus165102_production, 24_LVBus165104_consumption, 24_LVBus165104_production, 24_LVBus165105_production, 24_LVBus165107_consumption, 24_LVBus165107_production, 24_LVBus165108_production, 24_LVBus165109_production, 24_LVBus165110_production, 24_LVBus165113_production, 24_LVBus165114_production, 24_LVBus165115_production, 24_LVBus165117_production, 24_LVBus165118_production, 24_LVBus165120_production, 24_LVBus165121_production, 24_LVBus165122_production, 24_LVBus165123_production, 24_LVBus165124_production, 24_LVBus165125_production, 24_LVBus165126_production, 24_LVBus165127_production, 24_LVBus165128_production, 24_LVBus165129_production, 24_LVBus165130_consumption, 24_LVBus165130_production, 24_LVBus165131_production, 24_LVBus165132_production, 24_LVBus165134_production, 24_LVBus165136_production, 24_LVBus165138_production, 24_LVBus165140_production, 24_LVBus165141_production, 24_LVBus165142_consumption, 24_LVBus165142_production, 24_LVBus165143_consumption, 24_LVBus165143_production, 24_LVBus165144_production, 24_LVBus165146_consumption, 24_LVBus165146_production, 24_LVBus165147_consumption, 24_LVBus165147_production, 24_LVBus165149_production, 24_LVBus165150_consumption, 24_LVBus165150_production, 24_LVBus165151_production, 24_LVBus165152_production, 24_LVBus165154_production, 24_LVBus165155_production, 24_LVBus165156_consumption, 24_LVBus165156_production, 24_LVBus165157_consumption, 24_LVBus165157_production, 24_LVBus165158_production, 24_LVBus165159_consumption, 24_LVBus165159_production, 24_LVBus165160_production, 24_LVBus165162_consumption, 24_LVBus165162_production, 24_LVBus165163_consumption, 24_LVBus165163_production, 24_LVBus165164_consumption, 24_LVBus165164_production, 24_LVBus165165_production, 24_LVBus165166_production, 24_LVBus165167_production, 24_LVBus165168_production, 24_LVBus165169_production, 24_LVBus165170_production, 24_LVBus165171_production, 24_LVBus165172_production, 24_LVBus165173_production, 24_LVBus165174_production, 24_LVBus165175_consumption, 24_LVBus165175_production, 24_LVBus165176_production, 24_LVBus165177_consumption, 24_LVBus165177_production, 24_LVBus165178_consumption, 24_LVBus165178_production, 24_LVBus165179_consumption, 24_LVBus165179_production, 24_LVBus165180_consumption, 24_LVBus165180_production, 24_LVBus165181_production, 24_LVBus165182_consumption, 24_LVBus165182_production, 24_LVBus165183_consumption, 24_LVBus165183_production, 24_LVBus165184_production, 24_LVBus165187_production, 24_LVBus834015_production, 24_LVBus834016_production, 24_LVBus834017_production, 24_LVBus834018_production, 24_LVBus834019_production, 24_LVBus834020_production, 24_LVBus834021_production, 24_LVBus834022_production, 24_LVBus834023_production, 24_LVBus834024_production, 24_MVLV00541_consumption, 24_MVLV00541_production, 24_MVLV07694_consumption, 24_MVLV07694_production, 24_MVLV10015_consumption, 24_MVLV10015_production, 24_MVLV16779_consumption, 24_MVLV16779_production, 24_MVLV16780_consumption, 24_MVLV16780_production, 24_MVLV25262_consumption, 24_MVLV25262_production, 24_MVLV26839_consumption, 24_MVLV26839_production, 24_MVLV39105_consumption, 24_MVLV39105_production, 24_MVLV43476_consumption, 24_MVLV43476_production, 24_MVLV46581_consumption, 24_MVLV46581_production, 24_MVLV49814_consumption, 24_MVLV49814_production, 24_MVLV59565_consumption, 24_MVLV59565_production, 24_MVLV61047_consumption, 24_MVLV61047_production, 24_MVLV63161_consumption, 24_MVLV63161_production, 24_MVLV81856_consumption, 24_MVLV81856_production, 24_MVLV85847_consumption, 24_MVLV85847_production.

## 9. Data Quality Summary

**Total findings:** 305 (0 errors, 5 warnings, 300 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  497 of 802 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.24 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  498 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164737_consumption`  
  Load '24_LVBus164737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165093_consumption`  
  Load '24_LVBus165093_consumption' has phase imbalance of 146.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164898_consumption`  
  Load '24_LVBus164898_consumption' has phase imbalance of 70.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164761_consumption`  
  Load '24_LVBus164761_consumption' has phase imbalance of 263.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164803_consumption`  
  Load '24_LVBus164803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165091_consumption`  
  Load '24_LVBus165091_consumption' has phase imbalance of 94.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165176_consumption`  
  Load '24_LVBus165176_consumption' has phase imbalance of 200.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834015_consumption`  
  Load '24_LVBus834015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164958_consumption`  
  Load '24_LVBus164958_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164888_consumption`  
  Load '24_LVBus164888_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165114_consumption`  
  Load '24_LVBus165114_consumption' has phase imbalance of 32.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165123_consumption`  
  Load '24_LVBus165123_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165168_consumption`  
  Load '24_LVBus165168_consumption' has phase imbalance of 297.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164802_consumption`  
  Load '24_LVBus164802_consumption' has phase imbalance of 157.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164960_consumption`  
  Load '24_LVBus164960_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165069_consumption`  
  Load '24_LVBus165069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164944_consumption`  
  Load '24_LVBus164944_consumption' has phase imbalance of 266.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164941_consumption`  
  Load '24_LVBus164941_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164893_consumption`  
  Load '24_LVBus164893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164928_consumption`  
  Load '24_LVBus164928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164967_consumption`  
  Load '24_LVBus164967_consumption' has phase imbalance of 267.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164862_consumption`  
  Load '24_LVBus164862_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165095_consumption`  
  Load '24_LVBus165095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164758_consumption`  
  Load '24_LVBus164758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164823_consumption`  
  Load '24_LVBus164823_consumption' has phase imbalance of 289.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164782_consumption`  
  Load '24_LVBus164782_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164821_consumption`  
  Load '24_LVBus164821_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165047_consumption`  
  Load '24_LVBus165047_consumption' has phase imbalance of 186.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164859_consumption`  
  Load '24_LVBus164859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164800_consumption`  
  Load '24_LVBus164800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164763_consumption`  
  Load '24_LVBus164763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834020_consumption`  
  Load '24_LVBus834020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164954_consumption`  
  Load '24_LVBus164954_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164921_consumption`  
  Load '24_LVBus164921_consumption' has phase imbalance of 89.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165181_consumption`  
  Load '24_LVBus165181_consumption' has phase imbalance of 198.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164863_consumption`  
  Load '24_LVBus164863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165187_consumption`  
  Load '24_LVBus165187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164896_consumption`  
  Load '24_LVBus164896_consumption' has phase imbalance of 142.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165122_consumption`  
  Load '24_LVBus165122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165016_consumption`  
  Load '24_LVBus165016_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164887_consumption`  
  Load '24_LVBus164887_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165068_consumption`  
  Load '24_LVBus165068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164865_consumption`  
  Load '24_LVBus164865_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164711_consumption`  
  Load '24_LVBus164711_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834022_consumption`  
  Load '24_LVBus834022_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165048_consumption`  
  Load '24_LVBus165048_consumption' has phase imbalance of 176.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164933_consumption`  
  Load '24_LVBus164933_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164806_consumption`  
  Load '24_LVBus164806_consumption' has phase imbalance of 168.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165134_consumption`  
  Load '24_LVBus165134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164805_consumption`  
  Load '24_LVBus164805_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164816_consumption`  
  Load '24_LVBus164816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165151_consumption`  
  Load '24_LVBus165151_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164804_consumption`  
  Load '24_LVBus164804_consumption' has phase imbalance of 214.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165125_consumption`  
  Load '24_LVBus165125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164815_consumption`  
  Load '24_LVBus164815_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165001_consumption`  
  Load '24_LVBus165001_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164957_consumption`  
  Load '24_LVBus164957_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164769_consumption`  
  Load '24_LVBus164769_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164961_consumption`  
  Load '24_LVBus164961_consumption' has phase imbalance of 24.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164895_consumption`  
  Load '24_LVBus164895_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165088_consumption`  
  Load '24_LVBus165088_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165012_consumption`  
  Load '24_LVBus165012_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164825_consumption`  
  Load '24_LVBus164825_consumption' has phase imbalance of 165.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834018_consumption`  
  Load '24_LVBus834018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165172_consumption`  
  Load '24_LVBus165172_consumption' has phase imbalance of 256.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164920_consumption`  
  Load '24_LVBus164920_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164752_consumption`  
  Load '24_LVBus164752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164956_consumption`  
  Load '24_LVBus164956_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165084_consumption`  
  Load '24_LVBus165084_consumption' has phase imbalance of 33.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165037_consumption`  
  Load '24_LVBus165037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164909_consumption`  
  Load '24_LVBus164909_consumption' has phase imbalance of 198.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164814_consumption`  
  Load '24_LVBus164814_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164926_consumption`  
  Load '24_LVBus164926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164760_consumption`  
  Load '24_LVBus164760_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165140_consumption`  
  Load '24_LVBus165140_consumption' has phase imbalance of 105.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165169_consumption`  
  Load '24_LVBus165169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164766_consumption`  
  Load '24_LVBus164766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164721_consumption`  
  Load '24_LVBus164721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164820_consumption`  
  Load '24_LVBus164820_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164753_consumption`  
  Load '24_LVBus164753_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165108_consumption`  
  Load '24_LVBus165108_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164785_consumption`  
  Load '24_LVBus164785_consumption' has phase imbalance of 244.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165017_consumption`  
  Load '24_LVBus165017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164964_consumption`  
  Load '24_LVBus164964_consumption' has phase imbalance of 260.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164722_consumption`  
  Load '24_LVBus164722_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164974_consumption`  
  Load '24_LVBus164974_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165023_consumption`  
  Load '24_LVBus165023_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164911_consumption`  
  Load '24_LVBus164911_consumption' has phase imbalance of 229.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165128_consumption`  
  Load '24_LVBus165128_consumption' has phase imbalance of 196.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165160_consumption`  
  Load '24_LVBus165160_consumption' has phase imbalance of 149.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165079_consumption`  
  Load '24_LVBus165079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165127_consumption`  
  Load '24_LVBus165127_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165011_consumption`  
  Load '24_LVBus165011_consumption' has phase imbalance of 274.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165152_consumption`  
  Load '24_LVBus165152_consumption' has phase imbalance of 122.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165050_consumption`  
  Load '24_LVBus165050_consumption' has phase imbalance of 223.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165073_consumption`  
  Load '24_LVBus165073_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164781_consumption`  
  Load '24_LVBus164781_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164963_consumption`  
  Load '24_LVBus164963_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164710_consumption`  
  Load '24_LVBus164710_consumption' has phase imbalance of 25.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165009_consumption`  
  Load '24_LVBus165009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164946_consumption`  
  Load '24_LVBus164946_consumption' has phase imbalance of 263.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165072_consumption`  
  Load '24_LVBus165072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165144_consumption`  
  Load '24_LVBus165144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165074_consumption`  
  Load '24_LVBus165074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164945_consumption`  
  Load '24_LVBus164945_consumption' has phase imbalance of 51.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164917_consumption`  
  Load '24_LVBus164917_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165121_consumption`  
  Load '24_LVBus165121_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165025_consumption`  
  Load '24_LVBus165025_consumption' has phase imbalance of 83.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165029_consumption`  
  Load '24_LVBus165029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165051_consumption`  
  Load '24_LVBus165051_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164904_consumption`  
  Load '24_LVBus164904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164813_consumption`  
  Load '24_LVBus164813_consumption' has phase imbalance of 210.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165154_consumption`  
  Load '24_LVBus165154_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164959_consumption`  
  Load '24_LVBus164959_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164756_consumption`  
  Load '24_LVBus164756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164829_consumption`  
  Load '24_LVBus164829_consumption' has phase imbalance of 97.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164830_consumption`  
  Load '24_LVBus164830_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164834_consumption`  
  Load '24_LVBus164834_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165166_consumption`  
  Load '24_LVBus165166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165028_consumption`  
  Load '24_LVBus165028_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164759_consumption`  
  Load '24_LVBus164759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165126_consumption`  
  Load '24_LVBus165126_consumption' has phase imbalance of 277.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164916_consumption`  
  Load '24_LVBus164916_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164768_consumption`  
  Load '24_LVBus164768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165118_consumption`  
  Load '24_LVBus165118_consumption' has phase imbalance of 241.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165149_consumption`  
  Load '24_LVBus165149_consumption' has phase imbalance of 221.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165089_consumption`  
  Load '24_LVBus165089_consumption' has phase imbalance of 251.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164996_consumption`  
  Load '24_LVBus164996_consumption' has phase imbalance of 115.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164838_consumption`  
  Load '24_LVBus164838_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165132_consumption`  
  Load '24_LVBus165132_consumption' has phase imbalance of 48.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165075_consumption`  
  Load '24_LVBus165075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165049_consumption`  
  Load '24_LVBus165049_consumption' has phase imbalance of 261.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165002_consumption`  
  Load '24_LVBus165002_consumption' has phase imbalance of 146.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165155_consumption`  
  Load '24_LVBus165155_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164971_consumption`  
  Load '24_LVBus164971_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164918_consumption`  
  Load '24_LVBus164918_consumption' has phase imbalance of 127.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164839_consumption`  
  Load '24_LVBus164839_consumption' has phase imbalance of 145.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164866_consumption`  
  Load '24_LVBus164866_consumption' has phase imbalance of 148.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165131_consumption`  
  Load '24_LVBus165131_consumption' has phase imbalance of 116.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165035_consumption`  
  Load '24_LVBus165035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164979_consumption`  
  Load '24_LVBus164979_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164726_consumption`  
  Load '24_LVBus164726_consumption' has phase imbalance of 237.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164844_consumption`  
  Load '24_LVBus164844_consumption' has phase imbalance of 262.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165076_consumption`  
  Load '24_LVBus165076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164750_consumption`  
  Load '24_LVBus164750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165055_consumption`  
  Load '24_LVBus165055_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164870_consumption`  
  Load '24_LVBus164870_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834016_consumption`  
  Load '24_LVBus834016_consumption' has phase imbalance of 221.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165124_consumption`  
  Load '24_LVBus165124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164914_consumption`  
  Load '24_LVBus164914_consumption' has phase imbalance of 121.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165167_consumption`  
  Load '24_LVBus165167_consumption' has phase imbalance of 141.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165022_consumption`  
  Load '24_LVBus165022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164892_consumption`  
  Load '24_LVBus164892_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164712_consumption`  
  Load '24_LVBus164712_consumption' has phase imbalance of 64.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164877_consumption`  
  Load '24_LVBus164877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164847_consumption`  
  Load '24_LVBus164847_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165136_consumption`  
  Load '24_LVBus165136_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164872_consumption`  
  Load '24_LVBus164872_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165113_consumption`  
  Load '24_LVBus165113_consumption' has phase imbalance of 33.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164905_consumption`  
  Load '24_LVBus164905_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164713_consumption`  
  Load '24_LVBus164713_consumption' has phase imbalance of 257.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164745_consumption`  
  Load '24_LVBus164745_consumption' has phase imbalance of 223.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165039_consumption`  
  Load '24_LVBus165039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165018_consumption`  
  Load '24_LVBus165018_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165105_consumption`  
  Load '24_LVBus165105_consumption' has phase imbalance of 50.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164861_consumption`  
  Load '24_LVBus164861_consumption' has phase imbalance of 73.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164787_consumption`  
  Load '24_LVBus164787_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165054_consumption`  
  Load '24_LVBus165054_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164885_consumption`  
  Load '24_LVBus164885_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834023_consumption`  
  Load '24_LVBus834023_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164817_consumption`  
  Load '24_LVBus164817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834024_consumption`  
  Load '24_LVBus834024_consumption' has phase imbalance of 178.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165078_consumption`  
  Load '24_LVBus165078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165129_consumption`  
  Load '24_LVBus165129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165042_consumption`  
  Load '24_LVBus165042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164882_consumption`  
  Load '24_LVBus164882_consumption' has phase imbalance of 281.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164751_consumption`  
  Load '24_LVBus164751_consumption' has phase imbalance of 124.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164835_consumption`  
  Load '24_LVBus164835_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164903_consumption`  
  Load '24_LVBus164903_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164902_consumption`  
  Load '24_LVBus164902_consumption' has phase imbalance of 134.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164927_consumption`  
  Load '24_LVBus164927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164799_consumption`  
  Load '24_LVBus164799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164975_consumption`  
  Load '24_LVBus164975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165006_consumption`  
  Load '24_LVBus165006_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165141_consumption`  
  Load '24_LVBus165141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165000_consumption`  
  Load '24_LVBus165000_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165014_consumption`  
  Load '24_LVBus165014_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165027_consumption`  
  Load '24_LVBus165027_consumption' has phase imbalance of 234.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165102_consumption`  
  Load '24_LVBus165102_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164843_consumption`  
  Load '24_LVBus164843_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164807_consumption`  
  Load '24_LVBus164807_consumption' has phase imbalance of 118.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164937_consumption`  
  Load '24_LVBus164937_consumption' has phase imbalance of 275.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165110_consumption`  
  Load '24_LVBus165110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165046_consumption`  
  Load '24_LVBus165046_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164811_consumption`  
  Load '24_LVBus164811_consumption' has phase imbalance of 249.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165008_consumption`  
  Load '24_LVBus165008_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164932_consumption`  
  Load '24_LVBus164932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834021_consumption`  
  Load '24_LVBus834021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164749_consumption`  
  Load '24_LVBus164749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164832_consumption`  
  Load '24_LVBus164832_consumption' has phase imbalance of 268.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164757_consumption`  
  Load '24_LVBus164757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164819_consumption`  
  Load '24_LVBus164819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165165_consumption`  
  Load '24_LVBus165165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164886_consumption`  
  Load '24_LVBus164886_consumption' has phase imbalance of 100.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164755_consumption`  
  Load '24_LVBus164755_consumption' has phase imbalance of 256.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164788_consumption`  
  Load '24_LVBus164788_consumption' has phase imbalance of 270.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164776_consumption`  
  Load '24_LVBus164776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165005_consumption`  
  Load '24_LVBus165005_consumption' has phase imbalance of 39.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164837_consumption`  
  Load '24_LVBus164837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165071_consumption`  
  Load '24_LVBus165071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164780_consumption`  
  Load '24_LVBus164780_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165031_consumption`  
  Load '24_LVBus165031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164953_consumption`  
  Load '24_LVBus164953_consumption' has phase imbalance of 117.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165056_consumption`  
  Load '24_LVBus165056_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164940_consumption`  
  Load '24_LVBus164940_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164912_consumption`  
  Load '24_LVBus164912_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165117_consumption`  
  Load '24_LVBus165117_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165060_consumption`  
  Load '24_LVBus165060_consumption' has phase imbalance of 281.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165184_consumption`  
  Load '24_LVBus165184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164748_consumption`  
  Load '24_LVBus164748_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165007_consumption`  
  Load '24_LVBus165007_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165170_consumption`  
  Load '24_LVBus165170_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164883_consumption`  
  Load '24_LVBus164883_consumption' has phase imbalance of 233.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164810_consumption`  
  Load '24_LVBus164810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164880_consumption`  
  Load '24_LVBus164880_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164868_consumption`  
  Load '24_LVBus164868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834019_consumption`  
  Load '24_LVBus834019_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165109_consumption`  
  Load '24_LVBus165109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834017_consumption`  
  Load '24_LVBus834017_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164955_consumption`  
  Load '24_LVBus164955_consumption' has phase imbalance of 217.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165090_consumption`  
  Load '24_LVBus165090_consumption' has phase imbalance of 23.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165067_consumption`  
  Load '24_LVBus165067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165052_consumption`  
  Load '24_LVBus165052_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164966_consumption`  
  Load '24_LVBus164966_consumption' has phase imbalance of 57.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164984_consumption`  
  Load '24_LVBus164984_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164936_consumption`  
  Load '24_LVBus164936_consumption' has phase imbalance of 23.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164900_consumption`  
  Load '24_LVBus164900_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164851_consumption`  
  Load '24_LVBus164851_consumption' has phase imbalance of 146.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164850_consumption`  
  Load '24_LVBus164850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164818_consumption`  
  Load '24_LVBus164818_consumption' has phase imbalance of 228.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165085_consumption`  
  Load '24_LVBus165085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164919_consumption`  
  Load '24_LVBus164919_consumption' has phase imbalance of 168.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165158_consumption`  
  Load '24_LVBus165158_consumption' has phase imbalance of 107.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164744_consumption`  
  Load '24_LVBus164744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164842_consumption`  
  Load '24_LVBus164842_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164860_consumption`  
  Load '24_LVBus164860_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164978_consumption`  
  Load '24_LVBus164978_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165070_consumption`  
  Load '24_LVBus165070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164910_consumption`  
  Load '24_LVBus164910_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164824_consumption`  
  Load '24_LVBus164824_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165077_consumption`  
  Load '24_LVBus165077_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165097_consumption`  
  Load '24_LVBus165097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164923_consumption`  
  Load '24_LVBus164923_consumption' has phase imbalance of 134.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164925_consumption`  
  Load '24_LVBus164925_consumption' has phase imbalance of 217.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165034_consumption`  
  Load '24_LVBus165034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164715_consumption`  
  Load '24_LVBus164715_consumption' has phase imbalance of 143.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164871_consumption`  
  Load '24_LVBus164871_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164809_consumption`  
  Load '24_LVBus164809_consumption' has phase imbalance of 130.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164773_consumption`  
  Load '24_LVBus164773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164934_consumption`  
  Load '24_LVBus164934_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164973_consumption`  
  Load '24_LVBus164973_consumption' has phase imbalance of 260.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165171_consumption`  
  Load '24_LVBus165171_consumption' has phase imbalance of 54.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164730_consumption`  
  Load '24_LVBus164730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164792_consumption`  
  Load '24_LVBus164792_consumption' has phase imbalance of 242.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165041_consumption`  
  Load '24_LVBus165041_consumption' has phase imbalance of 222.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164831_consumption`  
  Load '24_LVBus164831_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164897_consumption`  
  Load '24_LVBus164897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165138_consumption`  
  Load '24_LVBus165138_consumption' has phase imbalance of 109.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164889_consumption`  
  Load '24_LVBus164889_consumption' has phase imbalance of 146.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164709_consumption`  
  Load '24_LVBus164709_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165115_consumption`  
  Load '24_LVBus165115_consumption' has phase imbalance of 184.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164943_consumption`  
  Load '24_LVBus164943_consumption' has phase imbalance of 72.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164901_consumption`  
  Load '24_LVBus164901_consumption' has phase imbalance of 113.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165173_consumption`  
  Load '24_LVBus165173_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165043_consumption`  
  Load '24_LVBus165043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165033_consumption`  
  Load '24_LVBus165033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165004_consumption`  
  Load '24_LVBus165004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164890_consumption`  
  Load '24_LVBus164890_consumption' has phase imbalance of 220.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus165174_consumption`  
  Load '24_LVBus165174_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164878_consumption`  
  Load '24_LVBus164878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus164746_consumption`  
  Load '24_LVBus164746_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 802 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus164950' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus164856' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus165095' (LV, 0.24 kV) has an electrical reach of 13.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus164856' (LV, 0.24 kV) has an electrical reach of 13.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  526 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  179 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 24_LVBus164709_consumption, 24_LVBus164711_consumption, 24_LVBus164713_consumption, 24_LVBus164721_consumption, 24_LVBus164722_consumption, 24_LVBus164726_consumption, 24_LVBus164730_consumption, 24_LVBus164737_consumption, 24_LVBus164744_consumption, 24_LVBus164745_consumption, 24_LVBus164746_consumption, 24_LVBus164749_consumption, 24_LVBus164750_consumption, 24_LVBus164752_consumption, 24_LVBus164753_consumption, 24_LVBus164755_consumption, 24_LVBus164756_consumption, 24_LVBus164757_consumption, 24_LVBus164758_consumption, 24_LVBus164759_consumption, 24_LVBus164760_consumption, 24_LVBus164761_consumption, 24_LVBus164763_consumption, 24_LVBus164766_consumption, 24_LVBus164768_consumption, 24_LVBus164769_consumption, 24_LVBus164773_consumption, 24_LVBus164776_consumption, 24_LVBus164780_consumption, 24_LVBus164782_consumption, 24_LVBus164785_consumption, 24_LVBus164792_consumption, 24_LVBus164799_consumption, 24_LVBus164800_consumption, 24_LVBus164802_consumption, 24_LVBus164803_consumption, 24_LVBus164804_consumption, 24_LVBus164805_consumption, 24_LVBus164806_consumption, 24_LVBus164810_consumption, 24_LVBus164811_consumption, 24_LVBus164813_consumption, 24_LVBus164814_consumption, 24_LVBus164815_consumption, 24_LVBus164816_consumption, 24_LVBus164817_consumption, 24_LVBus164818_consumption, 24_LVBus164819_consumption, 24_LVBus164820_consumption, 24_LVBus164821_consumption, 24_LVBus164823_consumption, 24_LVBus164830_consumption, 24_LVBus164831_consumption, 24_LVBus164832_consumption, 24_LVBus164834_consumption, 24_LVBus164837_consumption, 24_LVBus164844_consumption, 24_LVBus164850_consumption, 24_LVBus164859_consumption, 24_LVBus164862_consumption, 24_LVBus164863_consumption, 24_LVBus164865_consumption, 24_LVBus164868_consumption, 24_LVBus164870_consumption, 24_LVBus164871_consumption, 24_LVBus164877_consumption, 24_LVBus164878_consumption, 24_LVBus164880_consumption, 24_LVBus164882_consumption, 24_LVBus164885_consumption, 24_LVBus164887_consumption, 24_LVBus164890_consumption, 24_LVBus164892_consumption, 24_LVBus164893_consumption, 24_LVBus164897_consumption, 24_LVBus164900_consumption, 24_LVBus164904_consumption, 24_LVBus164909_consumption, 24_LVBus164912_consumption, 24_LVBus164916_consumption, 24_LVBus164917_consumption, 24_LVBus164926_consumption, 24_LVBus164927_consumption, 24_LVBus164928_consumption, 24_LVBus164932_consumption, 24_LVBus164933_consumption, 24_LVBus164934_consumption, 24_LVBus164946_consumption, 24_LVBus164954_consumption, 24_LVBus164955_consumption, 24_LVBus164956_consumption, 24_LVBus164958_consumption, 24_LVBus164959_consumption, 24_LVBus164960_consumption, 24_LVBus164963_consumption, 24_LVBus164964_consumption, 24_LVBus164967_consumption, 24_LVBus164971_consumption, 24_LVBus164973_consumption, 24_LVBus164974_consumption, 24_LVBus164975_consumption, 24_LVBus164978_consumption, 24_LVBus164979_consumption, 24_LVBus165004_consumption, 24_LVBus165008_consumption, 24_LVBus165009_consumption, 24_LVBus165011_consumption, 24_LVBus165012_consumption, 24_LVBus165014_consumption, 24_LVBus165017_consumption, 24_LVBus165022_consumption, 24_LVBus165023_consumption, 24_LVBus165029_consumption, 24_LVBus165031_consumption, 24_LVBus165033_consumption, 24_LVBus165034_consumption, 24_LVBus165035_consumption, 24_LVBus165037_consumption, 24_LVBus165039_consumption, 24_LVBus165042_consumption, 24_LVBus165043_consumption, 24_LVBus165046_consumption, 24_LVBus165047_consumption, 24_LVBus165049_consumption, 24_LVBus165050_consumption, 24_LVBus165052_consumption, 24_LVBus165054_consumption, 24_LVBus165056_consumption, 24_LVBus165067_consumption, 24_LVBus165068_consumption, 24_LVBus165069_consumption, 24_LVBus165070_consumption, 24_LVBus165071_consumption, 24_LVBus165072_consumption, 24_LVBus165073_consumption, 24_LVBus165074_consumption, 24_LVBus165075_consumption, 24_LVBus165076_consumption, 24_LVBus165078_consumption, 24_LVBus165079_consumption, 24_LVBus165085_consumption, 24_LVBus165088_consumption, 24_LVBus165089_consumption, 24_LVBus165095_consumption, 24_LVBus165097_consumption, 24_LVBus165108_consumption, 24_LVBus165109_consumption, 24_LVBus165110_consumption, 24_LVBus165115_consumption, 24_LVBus165118_consumption, 24_LVBus165121_consumption, 24_LVBus165122_consumption, 24_LVBus165123_consumption, 24_LVBus165124_consumption, 24_LVBus165125_consumption, 24_LVBus165126_consumption, 24_LVBus165128_consumption, 24_LVBus165129_consumption, 24_LVBus165134_consumption, 24_LVBus165141_consumption, 24_LVBus165144_consumption, 24_LVBus165149_consumption, 24_LVBus165151_consumption, 24_LVBus165165_consumption, 24_LVBus165166_consumption, 24_LVBus165168_consumption, 24_LVBus165169_consumption, 24_LVBus165172_consumption, 24_LVBus165174_consumption, 24_LVBus165176_consumption, 24_LVBus165184_consumption, 24_LVBus165187_consumption, 24_LVBus834015_consumption, 24_LVBus834016_consumption, 24_LVBus834018_consumption, 24_LVBus834020_consumption, 24_LVBus834021_consumption, 24_LVBus834022_consumption, 24_LVBus834024_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  401 group(s) of loads (802 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  13 group(s) of series lines (29 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  498 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus164709_production, 24_LVBus164710_production, 24_LVBus164711_production, 24_LVBus164712_production, 24_LVBus164713_production, 24_LVBus164715_production, 24_LVBus164717_consumption, 24_LVBus164717_production, 24_LVBus164719_consumption, 24_LVBus164719_production, 24_LVBus164720_consumption, 24_LVBus164720_production, 24_LVBus164721_production, 24_LVBus164722_production, 24_LVBus164726_production, 24_LVBus164727_consumption, 24_LVBus164727_production, 24_LVBus164728_consumption, 24_LVBus164728_production, 24_LVBus164729_consumption, 24_LVBus164729_production, 24_LVBus164730_production, 24_LVBus164734_consumption, 24_LVBus164734_production, 24_LVBus164735_consumption, 24_LVBus164735_production, 24_LVBus164736_consumption, 24_LVBus164736_production, 24_LVBus164737_production, 24_LVBus164738_consumption, 24_LVBus164738_production, 24_LVBus164739_consumption, 24_LVBus164739_production, 24_LVBus164741_consumption, 24_LVBus164741_production, 24_LVBus164742_consumption, 24_LVBus164742_production, 24_LVBus164743_consumption, 24_LVBus164743_production, 24_LVBus164744_production, 24_LVBus164745_production, 24_LVBus164746_production, 24_LVBus164748_production, 24_LVBus164749_production, 24_LVBus164750_production, 24_LVBus164751_production, 24_LVBus164752_production, 24_LVBus164753_production, 24_LVBus164754_consumption, 24_LVBus164754_production, 24_LVBus164755_production, 24_LVBus164756_production, 24_LVBus164757_production, 24_LVBus164758_production, 24_LVBus164759_production, 24_LVBus164760_production, 24_LVBus164761_production, 24_LVBus164763_production, 24_LVBus164765_consumption, 24_LVBus164765_production, 24_LVBus164766_production, 24_LVBus164767_consumption, 24_LVBus164767_production, 24_LVBus164768_production, 24_LVBus164769_production, 24_LVBus164771_consumption, 24_LVBus164771_production, 24_LVBus164772_consumption, 24_LVBus164772_production, 24_LVBus164773_production, 24_LVBus164775_consumption, 24_LVBus164775_production, 24_LVBus164776_production, 24_LVBus164778_production, 24_LVBus164780_production, 24_LVBus164781_production, 24_LVBus164782_production, 24_LVBus164784_consumption, 24_LVBus164784_production, 24_LVBus164785_production, 24_LVBus164786_production, 24_LVBus164787_production, 24_LVBus164788_production, 24_LVBus164790_consumption, 24_LVBus164790_production, 24_LVBus164791_consumption, 24_LVBus164791_production, 24_LVBus164792_production, 24_LVBus164794_consumption, 24_LVBus164794_production, 24_LVBus164795_consumption, 24_LVBus164795_production, 24_LVBus164796_consumption, 24_LVBus164796_production, 24_LVBus164797_consumption, 24_LVBus164797_production, 24_LVBus164798_consumption, 24_LVBus164798_production, 24_LVBus164799_production, 24_LVBus164800_production, 24_LVBus164802_production, 24_LVBus164803_production, 24_LVBus164804_production, 24_LVBus164805_production, 24_LVBus164806_production, 24_LVBus164807_production, 24_LVBus164809_production, 24_LVBus164810_production, 24_LVBus164811_production, 24_LVBus164813_production, 24_LVBus164814_production, 24_LVBus164815_production, 24_LVBus164816_production, 24_LVBus164817_production, 24_LVBus164818_production, 24_LVBus164819_production, 24_LVBus164820_production, 24_LVBus164821_production, 24_LVBus164823_production, 24_LVBus164824_production, 24_LVBus164825_production, 24_LVBus164827_consumption, 24_LVBus164827_production, 24_LVBus164829_production, 24_LVBus164830_production, 24_LVBus164831_production, 24_LVBus164832_production, 24_LVBus164834_production, 24_LVBus164835_production, 24_LVBus164836_production, 24_LVBus164837_production, 24_LVBus164838_production, 24_LVBus164839_production, 24_LVBus164840_consumption, 24_LVBus164840_production, 24_LVBus164842_production, 24_LVBus164843_production, 24_LVBus164844_production, 24_LVBus164845_production, 24_LVBus164846_consumption, 24_LVBus164846_production, 24_LVBus164847_production, 24_LVBus164848_consumption, 24_LVBus164848_production, 24_LVBus164850_production, 24_LVBus164851_production, 24_LVBus164853_consumption, 24_LVBus164853_production, 24_LVBus164856_production, 24_LVBus164858_consumption, 24_LVBus164858_production, 24_LVBus164859_production, 24_LVBus164860_production, 24_LVBus164861_production, 24_LVBus164862_production, 24_LVBus164863_production, 24_LVBus164864_production, 24_LVBus164865_production, 24_LVBus164866_production, 24_LVBus164868_production, 24_LVBus164870_production, 24_LVBus164871_production, 24_LVBus164872_production, 24_LVBus164873_production, 24_LVBus164875_production, 24_LVBus164877_production, 24_LVBus164878_production, 24_LVBus164879_consumption, 24_LVBus164879_production, 24_LVBus164880_production, 24_LVBus164882_production, 24_LVBus164883_production, 24_LVBus164885_production, 24_LVBus164886_production, 24_LVBus164887_production, 24_LVBus164888_production, 24_LVBus164889_production, 24_LVBus164890_production, 24_LVBus164891_production, 24_LVBus164892_production, 24_LVBus164893_production, 24_LVBus164895_production, 24_LVBus164896_production, 24_LVBus164897_production, 24_LVBus164898_production, 24_LVBus164900_production, 24_LVBus164901_production, 24_LVBus164902_production, 24_LVBus164903_production, 24_LVBus164904_production, 24_LVBus164905_production, 24_LVBus164906_production, 24_LVBus164907_consumption, 24_LVBus164907_production, 24_LVBus164909_production, 24_LVBus164910_production, 24_LVBus164911_production, 24_LVBus164912_production, 24_LVBus164914_production, 24_LVBus164916_production, 24_LVBus164917_production, 24_LVBus164918_production, 24_LVBus164919_production, 24_LVBus164920_production, 24_LVBus164921_production, 24_LVBus164923_production, 24_LVBus164924_production, 24_LVBus164925_production, 24_LVBus164926_production, 24_LVBus164927_production, 24_LVBus164928_production, 24_LVBus164932_production, 24_LVBus164933_production, 24_LVBus164934_production, 24_LVBus164935_consumption, 24_LVBus164935_production, 24_LVBus164936_production, 24_LVBus164937_production, 24_LVBus164939_consumption, 24_LVBus164939_production, 24_LVBus164940_production, 24_LVBus164941_production, 24_LVBus164942_production, 24_LVBus164943_production, 24_LVBus164944_production, 24_LVBus164945_production, 24_LVBus164946_production, 24_LVBus164950_production, 24_LVBus164951_consumption, 24_LVBus164951_production, 24_LVBus164953_production, 24_LVBus164954_production, 24_LVBus164955_production, 24_LVBus164956_production, 24_LVBus164957_production, 24_LVBus164958_production, 24_LVBus164959_production, 24_LVBus164960_production, 24_LVBus164961_production, 24_LVBus164963_production, 24_LVBus164964_production, 24_LVBus164965_consumption, 24_LVBus164965_production, 24_LVBus164966_production, 24_LVBus164967_production, 24_LVBus164970_consumption, 24_LVBus164970_production, 24_LVBus164971_production, 24_LVBus164972_production, 24_LVBus164973_production, 24_LVBus164974_production, 24_LVBus164975_production, 24_LVBus164977_consumption, 24_LVBus164977_production, 24_LVBus164978_production, 24_LVBus164979_production, 24_LVBus164980_consumption, 24_LVBus164980_production, 24_LVBus164981_consumption, 24_LVBus164981_production, 24_LVBus164982_production, 24_LVBus164983_consumption, 24_LVBus164983_production, 24_LVBus164984_production, 24_LVBus164992_consumption, 24_LVBus164992_production, 24_LVBus164993_production, 24_LVBus164994_production, 24_LVBus164995_consumption, 24_LVBus164995_production, 24_LVBus164996_production, 24_LVBus164997_consumption, 24_LVBus164997_production, 24_LVBus164998_consumption, 24_LVBus164998_production, 24_LVBus164999_production, 24_LVBus165000_production, 24_LVBus165001_production, 24_LVBus165002_production, 24_LVBus165004_production, 24_LVBus165005_production, 24_LVBus165006_production, 24_LVBus165007_production, 24_LVBus165008_production, 24_LVBus165009_production, 24_LVBus165011_production, 24_LVBus165012_production, 24_LVBus165013_consumption, 24_LVBus165013_production, 24_LVBus165014_production, 24_LVBus165015_consumption, 24_LVBus165015_production, 24_LVBus165016_production, 24_LVBus165017_production, 24_LVBus165018_production, 24_LVBus165020_production, 24_LVBus165022_production, 24_LVBus165023_production, 24_LVBus165025_production, 24_LVBus165027_production, 24_LVBus165028_production, 24_LVBus165029_production, 24_LVBus165030_production, 24_LVBus165031_production, 24_LVBus165033_production, 24_LVBus165034_production, 24_LVBus165035_production, 24_LVBus165036_consumption, 24_LVBus165036_production, 24_LVBus165037_production, 24_LVBus165039_production, 24_LVBus165040_consumption, 24_LVBus165040_production, 24_LVBus165041_production, 24_LVBus165042_production, 24_LVBus165043_production, 24_LVBus165044_consumption, 24_LVBus165044_production, 24_LVBus165046_production, 24_LVBus165047_production, 24_LVBus165048_production, 24_LVBus165049_production, 24_LVBus165050_production, 24_LVBus165051_production, 24_LVBus165052_production, 24_LVBus165054_production, 24_LVBus165055_production, 24_LVBus165056_production, 24_LVBus165059_consumption, 24_LVBus165059_production, 24_LVBus165060_production, 24_LVBus165062_consumption, 24_LVBus165062_production, 24_LVBus165064_consumption, 24_LVBus165064_production, 24_LVBus165067_production, 24_LVBus165068_production, 24_LVBus165069_production, 24_LVBus165070_production, 24_LVBus165071_production, 24_LVBus165072_production, 24_LVBus165073_production, 24_LVBus165074_production, 24_LVBus165075_production, 24_LVBus165076_production, 24_LVBus165077_production, 24_LVBus165078_production, 24_LVBus165079_production, 24_LVBus165083_consumption, 24_LVBus165083_production, 24_LVBus165084_production, 24_LVBus165085_production, 24_LVBus165086_production, 24_LVBus165088_production, 24_LVBus165089_production, 24_LVBus165090_production, 24_LVBus165091_production, 24_LVBus165093_production, 24_LVBus165095_production, 24_LVBus165097_production, 24_LVBus165098_consumption, 24_LVBus165098_production, 24_LVBus165099_production, 24_LVBus165101_consumption, 24_LVBus165101_production, 24_LVBus165102_production, 24_LVBus165104_consumption, 24_LVBus165104_production, 24_LVBus165105_production, 24_LVBus165107_consumption, 24_LVBus165107_production, 24_LVBus165108_production, 24_LVBus165109_production, 24_LVBus165110_production, 24_LVBus165113_production, 24_LVBus165114_production, 24_LVBus165115_production, 24_LVBus165117_production, 24_LVBus165118_production, 24_LVBus165120_production, 24_LVBus165121_production, 24_LVBus165122_production, 24_LVBus165123_production, 24_LVBus165124_production, 24_LVBus165125_production, 24_LVBus165126_production, 24_LVBus165127_production, 24_LVBus165128_production, 24_LVBus165129_production, 24_LVBus165130_consumption, 24_LVBus165130_production, 24_LVBus165131_production, 24_LVBus165132_production, 24_LVBus165134_production, 24_LVBus165136_production, 24_LVBus165138_production, 24_LVBus165140_production, 24_LVBus165141_production, 24_LVBus165142_consumption, 24_LVBus165142_production, 24_LVBus165143_consumption, 24_LVBus165143_production, 24_LVBus165144_production, 24_LVBus165146_consumption, 24_LVBus165146_production, 24_LVBus165147_consumption, 24_LVBus165147_production, 24_LVBus165149_production, 24_LVBus165150_consumption, 24_LVBus165150_production, 24_LVBus165151_production, 24_LVBus165152_production, 24_LVBus165154_production, 24_LVBus165155_production, 24_LVBus165156_consumption, 24_LVBus165156_production, 24_LVBus165157_consumption, 24_LVBus165157_production, 24_LVBus165158_production, 24_LVBus165159_consumption, 24_LVBus165159_production, 24_LVBus165160_production, 24_LVBus165162_consumption, 24_LVBus165162_production, 24_LVBus165163_consumption, 24_LVBus165163_production, 24_LVBus165164_consumption, 24_LVBus165164_production, 24_LVBus165165_production, 24_LVBus165166_production, 24_LVBus165167_production, 24_LVBus165168_production, 24_LVBus165169_production, 24_LVBus165170_production, 24_LVBus165171_production, 24_LVBus165172_production, 24_LVBus165173_production, 24_LVBus165174_production, 24_LVBus165175_consumption, 24_LVBus165175_production, 24_LVBus165176_production, 24_LVBus165177_consumption, 24_LVBus165177_production, 24_LVBus165178_consumption, 24_LVBus165178_production, 24_LVBus165179_consumption, 24_LVBus165179_production, 24_LVBus165180_consumption, 24_LVBus165180_production, 24_LVBus165181_production, 24_LVBus165182_consumption, 24_LVBus165182_production, 24_LVBus165183_consumption, 24_LVBus165183_production, 24_LVBus165184_production, 24_LVBus165187_production, 24_LVBus834015_production, 24_LVBus834016_production, 24_LVBus834017_production, 24_LVBus834018_production, 24_LVBus834019_production, 24_LVBus834020_production, 24_LVBus834021_production, 24_LVBus834022_production, 24_LVBus834023_production, 24_LVBus834024_production, 24_MVLV00541_consumption, 24_MVLV00541_production, 24_MVLV07694_consumption, 24_MVLV07694_production, 24_MVLV10015_consumption, 24_MVLV10015_production, 24_MVLV16779_consumption, 24_MVLV16779_production, 24_MVLV16780_consumption, 24_MVLV16780_production, 24_MVLV25262_consumption, 24_MVLV25262_production, 24_MVLV26839_consumption, 24_MVLV26839_production, 24_MVLV39105_consumption, 24_MVLV39105_production, 24_MVLV43476_consumption, 24_MVLV43476_production, 24_MVLV46581_consumption, 24_MVLV46581_production, 24_MVLV49814_consumption, 24_MVLV49814_production, 24_MVLV59565_consumption, 24_MVLV59565_production, 24_MVLV61047_consumption, 24_MVLV61047_production, 24_MVLV63161_consumption, 24_MVLV63161_production, 24_MVLV81856_consumption, 24_MVLV81856_production, 24_MVLV85847_consumption, 24_MVLV85847_production.

