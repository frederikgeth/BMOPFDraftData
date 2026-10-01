# BMOPF Network Summary: 76_MVFeeder1654

**Generated:** 2026-10-01 23:34:33  
**Findings:** 0 errors · 5 warnings · 439 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 69 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 927 |  |
| line | 857 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1406 | 1.482 MW, 444.7 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 69 |  |
| switch | 0 |  |
| transformer | 69 | Dyn11×69 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 161 | 160 | 12 | 0 |
| LV_236V | 236.0 V | 766 | 697 | 1394 | 0 |

**Transformer transitions:**

- `76_MVLV117691_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV147226_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV142661_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV085543_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV091190_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV026093_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133923_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV030103_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV149459_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV090711_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV022411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080472_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV123838_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV124782_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV149327_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV089357_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV130141_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133930_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV065131_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV052554_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV100104_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV074770_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV052558_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV026079_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV089338_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV003628_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV064164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV114395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041484_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133895_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV008563_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009940_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041904_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV143266_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV002271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV130310_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV070642_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV052137_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV142650_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV102743_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV030109_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV091196_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV028112_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV070639_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV100490_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV130150_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV114396_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041839_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV142957_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV024615_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV031824_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV036426_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041492_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV091173_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV050698_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV103426_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV029517_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV094421_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV065119_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV086727_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009863_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV030099_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080498_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV024590_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV130331_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV114369_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV142668_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041486_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV130305_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 295 |
| Tree depth (max hops) | 52 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 927 | 1 | 926 | 0 | 0 | 0 |
| Tier LV_236V | 766 | 69 | 697 | 0 | 0 | 0 |
| Tier MV_11.8kV | 161 | 1 | 160 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 69; skipped invalid branches: 0.

Galvanic zones: 70; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 76_LACAU | MV_11.8kV | 161 | 0 | 0 | 69 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3547 declared bus terminals; 3268 mapped line/closed-switch conductor edges; 279 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 33400.0 | 3.857 | 4218 |
| q_nom | 0.0 | 10000.0 | 3.857 | 4218 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.581 | 6770.0 | 2.387 | 857 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.463 | 69 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 908 of 1406 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207726_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208132_consumption' has phase imbalance of 288.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207864_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208252_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208158_consumption' has phase imbalance of 217.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207913_consumption' has phase imbalance of 127.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207647_consumption' has phase imbalance of 208.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2088329_consumption' has phase imbalance of 230.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2162034_consumption' has phase imbalance of 274.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208291_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208201_consumption' has phase imbalance of 245.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153152_consumption' has phase imbalance of 228.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207733_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207529_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207798_consumption' has phase imbalance of 128.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207821_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207655_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208286_consumption' has phase imbalance of 57.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207707_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208164_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208060_consumption' has phase imbalance of 287.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208150_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207513_consumption' has phase imbalance of 193.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207912_consumption' has phase imbalance of 123.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208109_consumption' has phase imbalance of 181.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208100_consumption' has phase imbalance of 71.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207979_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207830_consumption' has phase imbalance of 204.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108081_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208026_consumption' has phase imbalance of 83.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207779_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153146_consumption' has phase imbalance of 203.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207744_consumption' has phase imbalance of 291.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208232_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2094826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207834_consumption' has phase imbalance of 263.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207730_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207788_consumption' has phase imbalance of 246.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207651_consumption' has phase imbalance of 170.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208047_consumption' has phase imbalance of 284.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207561_consumption' has phase imbalance of 187.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207565_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207743_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2162035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207636_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208011_consumption' has phase imbalance of 140.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207627_consumption' has phase imbalance of 149.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207800_consumption' has phase imbalance of 266.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207615_consumption' has phase imbalance of 280.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207724_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207747_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207880_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208254_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208210_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207677_consumption' has phase imbalance of 50.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207663_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207831_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208121_consumption' has phase imbalance of 59.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108080_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208269_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208209_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208259_consumption' has phase imbalance of 268.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207759_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207648_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208256_consumption' has phase imbalance of 288.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208045_consumption' has phase imbalance of 227.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207787_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208213_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207828_consumption' has phase imbalance of 175.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208080_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207635_consumption' has phase imbalance of 215.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208214_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208066_consumption' has phase imbalance of 98.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208183_consumption' has phase imbalance of 288.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207695_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108083_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207804_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207548_consumption' has phase imbalance of 221.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208181_consumption' has phase imbalance of 274.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207891_consumption' has phase imbalance of 289.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207545_consumption' has phase imbalance of 281.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208117_consumption' has phase imbalance of 137.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207534_consumption' has phase imbalance of 118.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208212_consumption' has phase imbalance of 39.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207616_consumption' has phase imbalance of 26.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208253_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208120_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208240_consumption' has phase imbalance of 170.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208216_consumption' has phase imbalance of 209.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2162033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208089_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207643_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207578_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208283_consumption' has phase imbalance of 138.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208204_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207867_consumption' has phase imbalance of 76.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208188_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208228_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208073_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207758_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208067_consumption' has phase imbalance of 297.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207878_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207654_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207873_consumption' has phase imbalance of 142.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2048021_consumption' has phase imbalance of 84.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208126_consumption' has phase imbalance of 127.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207642_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207982_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207916_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208211_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208165_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208072_consumption' has phase imbalance of 286.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207746_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208237_consumption' has phase imbalance of 203.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208257_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207721_consumption' has phase imbalance of 254.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207691_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207678_consumption' has phase imbalance of 103.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207869_consumption' has phase imbalance of 239.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208116_consumption' has phase imbalance of 252.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208096_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208248_consumption' has phase imbalance of 131.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208196_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207871_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207799_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207752_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207688_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207676_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108079_consumption' has phase imbalance of 142.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208219_consumption' has phase imbalance of 171.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207713_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207559_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208001_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207698_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207911_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207509_consumption' has phase imbalance of 297.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153151_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207575_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208084_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207936_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207756_consumption' has phase imbalance of 94.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207934_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207780_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207739_consumption' has phase imbalance of 98.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208090_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207874_consumption' has phase imbalance of 129.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208145_consumption' has phase imbalance of 224.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207832_consumption' has phase imbalance of 266.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207976_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208255_consumption' has phase imbalance of 65.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208281_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207940_consumption' has phase imbalance of 39.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207980_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108085_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207760_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207981_consumption' has phase imbalance of 245.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208284_consumption' has phase imbalance of 46.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208184_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207729_consumption' has phase imbalance of 180.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207626_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207666_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207656_consumption' has phase imbalance of 287.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208220_consumption' has phase imbalance of 201.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208263_consumption' has phase imbalance of 103.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207835_consumption' has phase imbalance of 143.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208198_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207690_consumption' has phase imbalance of 69.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207938_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207728_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207945_consumption' has phase imbalance of 201.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207552_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108084_consumption' has phase imbalance of 217.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208115_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208039_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208236_consumption' has phase imbalance of 121.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208088_consumption' has phase imbalance of 221.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207645_consumption' has phase imbalance of 194.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208193_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207872_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207817_consumption' has phase imbalance of 183.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208040_consumption' has phase imbalance of 117.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208217_consumption' has phase imbalance of 275.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153143_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207600_consumption' has phase imbalance of 252.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208197_consumption' has phase imbalance of 277.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208199_consumption' has phase imbalance of 280.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208260_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208122_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207928_consumption' has phase imbalance of 282.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207700_consumption' has phase imbalance of 289.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207605_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207875_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207802_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208215_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207774_consumption' has phase imbalance of 267.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207599_consumption' has phase imbalance of 287.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207833_consumption' has phase imbalance of 208.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207879_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208123_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207811_consumption' has phase imbalance of 223.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207570_consumption' has phase imbalance of 122.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208222_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207889_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208113_consumption' has phase imbalance of 289.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108089_consumption' has phase imbalance of 221.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207628_consumption' has phase imbalance of 280.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207807_consumption' has phase imbalance of 275.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207693_consumption' has phase imbalance of 235.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208285_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207604_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207720_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153142_consumption' has phase imbalance of 280.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208009_consumption' has phase imbalance of 120.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208235_consumption' has phase imbalance of 164.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208062_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208292_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207964_consumption' has phase imbalance of 50.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207673_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207845_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207514_consumption' has phase imbalance of 271.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207762_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208014_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208271_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207550_consumption' has phase imbalance of 240.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207592_consumption' has phase imbalance of 215.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208055_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207827_consumption' has phase imbalance of 187.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207881_consumption' has phase imbalance of 189.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208191_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207863_consumption' has phase imbalance of 33.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208272_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208218_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207679_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207931_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108087_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207957_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207637_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207843_consumption' has phase imbalance of 244.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2153145_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108077_consumption' has phase imbalance of 285.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207694_consumption' has phase imbalance of 146.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208127_consumption' has phase imbalance of 282.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207703_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208129_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207974_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207712_consumption' has phase imbalance of 278.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207785_consumption' has phase imbalance of 244.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207558_consumption' has phase imbalance of 80.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207710_consumption' has phase imbalance of 264.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208221_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207537_consumption' has phase imbalance of 143.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208114_consumption' has phase imbalance of 278.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208087_consumption' has phase imbalance of 85.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207844_consumption' has phase imbalance of 133.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207797_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208190_consumption' has phase imbalance of 275.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2108078_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208157_consumption' has phase imbalance of 228.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207951_consumption' has phase imbalance of 116.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207512_consumption' has phase imbalance of 268.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207755_consumption' has phase imbalance of 51.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207579_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208064_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208194_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208224_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207716_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207894_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208038_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207665_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208085_consumption' has phase imbalance of 149.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0207598_consumption' has phase imbalance of 132.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0208192_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1406 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0207989' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0207923' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0207948' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0207539' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.482 MW |
| Total load Q | 444.7 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 76_MVLV117691_Transformer | 110.0 kVA | 3.8% |
| 76_MVLV147226_Transformer | 176.0 kVA | 8.3% |
| 76_MVLV142661_Transformer | 176.0 kVA | 21.1% |
| 76_MVLV085543_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV091190_Transformer | 110.0 kVA | 4.6% |
| 76_MVLV026093_Transformer | 110.0 kVA | 2.9% |
| 76_MVLV133923_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV030103_Transformer | 110.0 kVA | 1.8% |
| 76_MVLV149459_Transformer | 275.0 kVA | 14.3% |
| 76_MVLV090711_Transformer | 176.0 kVA | 9.9% |
| 76_MVLV022411_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV080472_Transformer | 176.0 kVA | 13.7% |
| 76_MVLV123838_Transformer | 440.0 kVA | 25.5% |
| 76_MVLV124782_Transformer | 176.0 kVA | 30.1% |
| 76_MVLV149327_Transformer | 110.0 kVA | 3.2% |
| 76_MVLV089357_Transformer | 110.0 kVA | 2.5% |
| 76_MVLV130141_Transformer | 176.0 kVA | 10.1% |
| 76_MVLV133930_Transformer | 110.0 kVA | 1.5% |
| 76_MVLV065131_Transformer | 275.0 kVA | 23.5% |
| 76_MVLV052554_Transformer | 275.0 kVA | 16.0% |
| 76_MVLV100104_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV074770_Transformer | 275.0 kVA | 21.8% |
| 76_MVLV052558_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV026079_Transformer | 176.0 kVA | 6.1% |
| 76_MVLV089338_Transformer | 176.0 kVA | 11.9% |
| 76_MVLV003628_Transformer | 176.0 kVA | 5.7% |
| 76_MVLV064164_Transformer | 110.0 kVA | 17.8% |
| 76_MVLV114395_Transformer | 110.0 kVA | 0.1% |
| 76_MVLV041484_Transformer | 176.0 kVA | 16.4% |
| 76_MVLV133895_Transformer | 176.0 kVA | 7.2% |
| 76_MVLV008563_Transformer | 110.0 kVA | 7.0% |
| 76_MVLV009940_Transformer | 275.0 kVA | 10.2% |
| 76_MVLV041904_Transformer | 176.0 kVA | 12.2% |
| 76_MVLV143266_Transformer | 110.0 kVA | 3.0% |
| 76_MVLV002271_Transformer | 110.0 kVA | 8.4% |
| 76_MVLV130310_Transformer | 440.0 kVA | 25.8% |
| 76_MVLV070642_Transformer | 176.0 kVA | 11.7% |
| 76_MVLV052137_Transformer | 110.0 kVA | 7.9% |
| 76_MVLV142650_Transformer | 176.0 kVA | 10.5% |
| 76_MVLV102743_Transformer | 110.0 kVA | 13.2% |
| 76_MVLV030109_Transformer | 176.0 kVA | 4.9% |
| 76_MVLV091196_Transformer | 275.0 kVA | 17.8% |
| 76_MVLV028112_Transformer | 110.0 kVA | 5.0% |
| 76_MVLV070639_Transformer | 440.0 kVA | 17.7% |
| 76_MVLV100490_Transformer | 110.0 kVA | 1.1% |
| 76_MVLV130150_Transformer | 176.0 kVA | 11.4% |
| 76_MVLV114396_Transformer | 176.0 kVA | 5.7% |
| 76_MVLV041839_Transformer | 176.0 kVA | 6.9% |
| 76_MVLV142957_Transformer | 440.0 kVA | 28.9% |
| 76_MVLV024615_Transformer | 110.0 kVA | 4.9% |
| 76_MVLV031824_Transformer | 176.0 kVA | 7.8% |
| 76_MVLV036426_Transformer | 275.0 kVA | 16.4% |
| 76_MVLV041492_Transformer | 176.0 kVA | 8.7% |
| 76_MVLV091173_Transformer | 110.0 kVA | 3.3% |
| 76_MVLV050698_Transformer | 275.0 kVA | 12.6% |
| 76_MVLV103426_Transformer | 176.0 kVA | 10.7% |
| 76_MVLV029517_Transformer | 110.0 kVA | 0.4% |
| 76_MVLV094421_Transformer | 176.0 kVA | 13.9% |
| 76_MVLV065119_Transformer | 110.0 kVA | 3.4% |
| 76_MVLV086727_Transformer | 110.0 kVA | 0.5% |
| 76_MVLV009863_Transformer | 110.0 kVA | 4.9% |
| 76_MVLV030099_Transformer | 176.0 kVA | 17.2% |
| 76_MVLV080498_Transformer | 176.0 kVA | 12.8% |
| 76_MVLV024590_Transformer | 176.0 kVA | 14.3% |
| 76_MVLV130331_Transformer | 110.0 kVA | 6.0% |
| 76_MVLV114369_Transformer | 110.0 kVA | 7.2% |
| 76_MVLV142668_Transformer | 275.0 kVA | 29.7% |
| 76_MVLV041486_Transformer | 110.0 kVA | 2.7% |
| 76_MVLV130305_Transformer | 176.0 kVA | 19.1% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.48 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LACAU' (MV, 11.78 kV) has an electrical reach of 27.67 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0207511' (LV, 0.24 kV) has an electrical reach of 1.51 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0208267' (LV, 0.24 kV) has an electrical reach of 2.01 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0207861' (LV, 0.24 kV) has an electrical reach of 1.05 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus0207989' (LV, 0.24 kV) has an electrical reach of 7.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 927 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 927 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 69 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 161 |
| LV_236V | 4-wire | 766 / 766 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 766 |
| Neutral branches | 697 |
| Grounding points | 69 |
| Neutral sections | 69 |
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
| 11.78 kV | 161 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 52 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 70 |
| Islands without voltage reference | 0 |
| Line impedance spread | 7550.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 766 / 161 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 909 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 909 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0207500_consumption, 76_LVBus0207500_production, 76_LVBus0207501_production, 76_LVBus0207502_consumption, 76_LVBus0207502_production, 76_LVBus0207503_consumption, 76_LVBus0207503_production, 76_LVBus0207504_consumption, 76_LVBus0207504_production, 76_LVBus0207506_consumption, 76_LVBus0207506_production, 76_LVBus0207507_consumption, 76_LVBus0207507_production, 76_LVBus0207508_production, 76_LVBus0207509_production, 76_LVBus0207511_production, 76_LVBus0207512_production, 76_LVBus0207513_production, 76_LVBus0207514_production, 76_LVBus0207515_production, 76_LVBus0207516_consumption, 76_LVBus0207516_production, 76_LVBus0207517_consumption, 76_LVBus0207517_production, 76_LVBus0207518_consumption, 76_LVBus0207518_production, 76_LVBus0207519_consumption, 76_LVBus0207519_production, 76_LVBus0207520_consumption, 76_LVBus0207520_production, 76_LVBus0207521_consumption, 76_LVBus0207521_production, 76_LVBus0207522_consumption, 76_LVBus0207522_production, 76_LVBus0207523_consumption, 76_LVBus0207523_production, 76_LVBus0207524_consumption, 76_LVBus0207524_production, 76_LVBus0207525_consumption, 76_LVBus0207525_production, 76_LVBus0207526_consumption, 76_LVBus0207526_production, 76_LVBus0207527_consumption, 76_LVBus0207527_production, 76_LVBus0207528_consumption, 76_LVBus0207528_production, 76_LVBus0207529_production, 76_LVBus0207530_production, 76_LVBus0207531_production, 76_LVBus0207533_production, 76_LVBus0207534_production, 76_LVBus0207535_consumption, 76_LVBus0207535_production, 76_LVBus0207536_production, 76_LVBus0207537_production, 76_LVBus0207539_consumption, 76_LVBus0207539_production, 76_LVBus0207540_consumption, 76_LVBus0207540_production, 76_LVBus0207541_consumption, 76_LVBus0207541_production, 76_LVBus0207542_production, 76_LVBus0207543_consumption, 76_LVBus0207543_production, 76_LVBus0207545_production, 76_LVBus0207546_production, 76_LVBus0207547_production, 76_LVBus0207548_production, 76_LVBus0207549_consumption, 76_LVBus0207549_production, 76_LVBus0207550_production, 76_LVBus0207551_production, 76_LVBus0207552_production, 76_LVBus0207553_production, 76_LVBus0207554_production, 76_LVBus0207556_consumption, 76_LVBus0207556_production, 76_LVBus0207558_production, 76_LVBus0207559_production, 76_LVBus0207560_production, 76_LVBus0207561_production, 76_LVBus0207562_production, 76_LVBus0207564_consumption, 76_LVBus0207564_production, 76_LVBus0207565_production, 76_LVBus0207567_production, 76_LVBus0207568_consumption, 76_LVBus0207568_production, 76_LVBus0207569_consumption, 76_LVBus0207569_production, 76_LVBus0207570_production, 76_LVBus0207572_consumption, 76_LVBus0207572_production, 76_LVBus0207573_consumption, 76_LVBus0207573_production, 76_LVBus0207574_consumption, 76_LVBus0207574_production, 76_LVBus0207575_production, 76_LVBus0207576_consumption, 76_LVBus0207576_production, 76_LVBus0207577_consumption, 76_LVBus0207577_production, 76_LVBus0207578_production, 76_LVBus0207579_production, 76_LVBus0207582_production, 76_LVBus0207583_production, 76_LVBus0207584_consumption, 76_LVBus0207584_production, 76_LVBus0207585_production, 76_LVBus0207589_production, 76_LVBus0207590_consumption, 76_LVBus0207590_production, 76_LVBus0207591_consumption, 76_LVBus0207591_production, 76_LVBus0207592_production, 76_LVBus0207593_consumption, 76_LVBus0207593_production, 76_LVBus0207594_production, 76_LVBus0207596_production, 76_LVBus0207598_production, 76_LVBus0207599_production, 76_LVBus0207600_production, 76_LVBus0207601_production, 76_LVBus0207602_production, 76_LVBus0207603_production, 76_LVBus0207604_production, 76_LVBus0207605_production, 76_LVBus0207607_production, 76_LVBus0207609_production, 76_LVBus0207611_consumption, 76_LVBus0207611_production, 76_LVBus0207612_production, 76_LVBus0207613_consumption, 76_LVBus0207613_production, 76_LVBus0207614_consumption, 76_LVBus0207614_production, 76_LVBus0207615_production, 76_LVBus0207616_production, 76_LVBus0207618_consumption, 76_LVBus0207618_production, 76_LVBus0207620_consumption, 76_LVBus0207620_production, 76_LVBus0207621_production, 76_LVBus0207623_consumption, 76_LVBus0207623_production, 76_LVBus0207624_production, 76_LVBus0207625_production, 76_LVBus0207626_production, 76_LVBus0207627_production, 76_LVBus0207628_production, 76_LVBus0207630_consumption, 76_LVBus0207630_production, 76_LVBus0207633_consumption, 76_LVBus0207633_production, 76_LVBus0207634_production, 76_LVBus0207635_production, 76_LVBus0207636_production, 76_LVBus0207637_production, 76_LVBus0207638_production, 76_LVBus0207639_production, 76_LVBus0207640_production, 76_LVBus0207641_production, 76_LVBus0207642_production, 76_LVBus0207643_production, 76_LVBus0207644_production, 76_LVBus0207645_production, 76_LVBus0207646_production, 76_LVBus0207647_production, 76_LVBus0207648_production, 76_LVBus0207649_consumption, 76_LVBus0207649_production, 76_LVBus0207650_consumption, 76_LVBus0207650_production, 76_LVBus0207651_production, 76_LVBus0207652_consumption, 76_LVBus0207652_production, 76_LVBus0207653_production, 76_LVBus0207654_production, 76_LVBus0207655_production, 76_LVBus0207656_production, 76_LVBus0207657_production, 76_LVBus0207658_consumption, 76_LVBus0207658_production, 76_LVBus0207659_consumption, 76_LVBus0207659_production, 76_LVBus0207660_consumption, 76_LVBus0207660_production, 76_LVBus0207661_production, 76_LVBus0207662_production, 76_LVBus0207663_production, 76_LVBus0207664_production, 76_LVBus0207665_production, 76_LVBus0207666_production, 76_LVBus0207668_production, 76_LVBus0207669_consumption, 76_LVBus0207669_production, 76_LVBus0207670_consumption, 76_LVBus0207670_production, 76_LVBus0207671_production, 76_LVBus0207673_production, 76_LVBus0207674_production, 76_LVBus0207675_production, 76_LVBus0207676_production, 76_LVBus0207677_production, 76_LVBus0207678_production, 76_LVBus0207679_production, 76_LVBus0207681_consumption, 76_LVBus0207681_production, 76_LVBus0207682_production, 76_LVBus0207684_production, 76_LVBus0207685_consumption, 76_LVBus0207685_production, 76_LVBus0207686_consumption, 76_LVBus0207686_production, 76_LVBus0207688_production, 76_LVBus0207690_production, 76_LVBus0207691_production, 76_LVBus0207692_consumption, 76_LVBus0207692_production, 76_LVBus0207693_production, 76_LVBus0207694_production, 76_LVBus0207695_production, 76_LVBus0207696_production, 76_LVBus0207698_production, 76_LVBus0207700_production, 76_LVBus0207701_consumption, 76_LVBus0207701_production, 76_LVBus0207702_production, 76_LVBus0207703_production, 76_LVBus0207707_production, 76_LVBus0207708_consumption, 76_LVBus0207708_production, 76_LVBus0207709_production, 76_LVBus0207710_production, 76_LVBus0207711_production, 76_LVBus0207712_production, 76_LVBus0207713_production, 76_LVBus0207714_production, 76_LVBus0207715_production, 76_LVBus0207716_production, 76_LVBus0207717_production, 76_LVBus0207718_production, 76_LVBus0207720_production, 76_LVBus0207721_production, 76_LVBus0207722_production, 76_LVBus0207723_production, 76_LVBus0207724_production, 76_LVBus0207725_production, 76_LVBus0207726_production, 76_LVBus0207728_production, 76_LVBus0207729_production, 76_LVBus0207730_production, 76_LVBus0207731_production, 76_LVBus0207732_production, 76_LVBus0207733_production, 76_LVBus0207734_production, 76_LVBus0207735_consumption, 76_LVBus0207735_production, 76_LVBus0207736_production, 76_LVBus0207739_production, 76_LVBus0207741_consumption, 76_LVBus0207741_production, 76_LVBus0207743_production, 76_LVBus0207744_production, 76_LVBus0207745_production, 76_LVBus0207746_production, 76_LVBus0207747_production, 76_LVBus0207748_production, 76_LVBus0207749_production, 76_LVBus0207750_production, 76_LVBus0207751_production, 76_LVBus0207752_production, 76_LVBus0207753_production, 76_LVBus0207754_consumption, 76_LVBus0207754_production, 76_LVBus0207755_production, 76_LVBus0207756_production, 76_LVBus0207757_production, 76_LVBus0207758_production, 76_LVBus0207759_production, 76_LVBus0207760_production, 76_LVBus0207761_consumption, 76_LVBus0207761_production, 76_LVBus0207762_production, 76_LVBus0207763_production, 76_LVBus0207767_consumption, 76_LVBus0207767_production, 76_LVBus0207769_consumption, 76_LVBus0207769_production, 76_LVBus0207770_consumption, 76_LVBus0207770_production, 76_LVBus0207771_production, 76_LVBus0207773_consumption, 76_LVBus0207773_production, 76_LVBus0207774_production, 76_LVBus0207775_production, 76_LVBus0207777_consumption, 76_LVBus0207777_production, 76_LVBus0207778_production, 76_LVBus0207779_production, 76_LVBus0207780_production, 76_LVBus0207784_consumption, 76_LVBus0207784_production, 76_LVBus0207785_production, 76_LVBus0207786_production, 76_LVBus0207787_production, 76_LVBus0207788_production, 76_LVBus0207789_consumption, 76_LVBus0207789_production, 76_LVBus0207790_production, 76_LVBus0207792_production, 76_LVBus0207794_consumption, 76_LVBus0207794_production, 76_LVBus0207795_production, 76_LVBus0207796_production, 76_LVBus0207797_production, 76_LVBus0207798_production, 76_LVBus0207799_production, 76_LVBus0207800_production, 76_LVBus0207801_production, 76_LVBus0207802_production, 76_LVBus0207804_production, 76_LVBus0207805_production, 76_LVBus0207806_consumption, 76_LVBus0207806_production, 76_LVBus0207807_production, 76_LVBus0207808_production, 76_LVBus0207810_consumption, 76_LVBus0207810_production, 76_LVBus0207811_production, 76_LVBus0207814_consumption, 76_LVBus0207814_production, 76_LVBus0207815_consumption, 76_LVBus0207815_production, 76_LVBus0207816_consumption, 76_LVBus0207816_production, 76_LVBus0207817_production, 76_LVBus0207818_production, 76_LVBus0207819_production, 76_LVBus0207820_production, 76_LVBus0207821_production, 76_LVBus0207822_production, 76_LVBus0207823_production, 76_LVBus0207824_consumption, 76_LVBus0207824_production, 76_LVBus0207826_consumption, 76_LVBus0207826_production, 76_LVBus0207827_production, 76_LVBus0207828_production, 76_LVBus0207829_consumption, 76_LVBus0207829_production, 76_LVBus0207830_production, 76_LVBus0207831_production, 76_LVBus0207832_production, 76_LVBus0207833_production, 76_LVBus0207834_production, 76_LVBus0207835_production, 76_LVBus0207837_consumption, 76_LVBus0207837_production, 76_LVBus0207838_production, 76_LVBus0207839_production, 76_LVBus0207840_production, 76_LVBus0207841_consumption, 76_LVBus0207841_production, 76_LVBus0207842_consumption, 76_LVBus0207842_production, 76_LVBus0207843_production, 76_LVBus0207844_production, 76_LVBus0207845_production, 76_LVBus0207846_production, 76_LVBus0207847_production, 76_LVBus0207848_production, 76_LVBus0207850_production, 76_LVBus0207851_consumption, 76_LVBus0207851_production, 76_LVBus0207852_consumption, 76_LVBus0207852_production, 76_LVBus0207853_consumption, 76_LVBus0207853_production, 76_LVBus0207854_consumption, 76_LVBus0207854_production, 76_LVBus0207855_consumption, 76_LVBus0207855_production, 76_LVBus0207861_consumption, 76_LVBus0207861_production, 76_LVBus0207862_consumption, 76_LVBus0207862_production, 76_LVBus0207863_production, 76_LVBus0207864_production, 76_LVBus0207865_consumption, 76_LVBus0207865_production, 76_LVBus0207866_production, 76_LVBus0207867_production, 76_LVBus0207868_production, 76_LVBus0207869_production, 76_LVBus0207871_production, 76_LVBus0207872_production, 76_LVBus0207873_production, 76_LVBus0207874_production, 76_LVBus0207875_production, 76_LVBus0207876_production, 76_LVBus0207877_consumption, 76_LVBus0207877_production, 76_LVBus0207878_production, 76_LVBus0207879_production, 76_LVBus0207880_production, 76_LVBus0207881_production, 76_LVBus0207883_production, 76_LVBus0207885_production, 76_LVBus0207886_production, 76_LVBus0207887_production, 76_LVBus0207888_production, 76_LVBus0207889_production, 76_LVBus0207890_production, 76_LVBus0207891_production, 76_LVBus0207892_production, 76_LVBus0207893_production, 76_LVBus0207894_production, 76_LVBus0207895_production, 76_LVBus0207896_consumption, 76_LVBus0207896_production, 76_LVBus0207897_consumption, 76_LVBus0207897_production, 76_LVBus0207898_consumption, 76_LVBus0207898_production, 76_LVBus0207899_consumption, 76_LVBus0207899_production, 76_LVBus0207900_consumption, 76_LVBus0207900_production, 76_LVBus0207901_consumption, 76_LVBus0207901_production, 76_LVBus0207902_production, 76_LVBus0207903_consumption, 76_LVBus0207903_production, 76_LVBus0207904_production, 76_LVBus0207908_consumption, 76_LVBus0207908_production, 76_LVBus0207909_production, 76_LVBus0207911_production, 76_LVBus0207912_production, 76_LVBus0207913_production, 76_LVBus0207914_production, 76_LVBus0207915_production, 76_LVBus0207916_production, 76_LVBus0207917_consumption, 76_LVBus0207917_production, 76_LVBus0207918_production, 76_LVBus0207919_consumption, 76_LVBus0207919_production, 76_LVBus0207921_consumption, 76_LVBus0207921_production, 76_LVBus0207923_production, 76_LVBus0207925_production, 76_LVBus0207926_production, 76_LVBus0207927_production, 76_LVBus0207928_production, 76_LVBus0207930_consumption, 76_LVBus0207930_production, 76_LVBus0207931_production, 76_LVBus0207932_production, 76_LVBus0207934_production, 76_LVBus0207935_consumption, 76_LVBus0207935_production, 76_LVBus0207936_production, 76_LVBus0207938_production, 76_LVBus0207939_consumption, 76_LVBus0207939_production, 76_LVBus0207940_production, 76_LVBus0207941_consumption, 76_LVBus0207941_production, 76_LVBus0207942_consumption, 76_LVBus0207942_production, 76_LVBus0207943_production, 76_LVBus0207944_production, 76_LVBus0207945_production, 76_LVBus0207946_production, 76_LVBus0207948_production, 76_LVBus0207949_production, 76_LVBus0207951_production, 76_LVBus0207952_production, 76_LVBus0207953_consumption, 76_LVBus0207953_production, 76_LVBus0207954_production, 76_LVBus0207955_production, 76_LVBus0207956_consumption, 76_LVBus0207956_production, 76_LVBus0207957_production, 76_LVBus0207958_consumption, 76_LVBus0207958_production, 76_LVBus0207960_consumption, 76_LVBus0207960_production, 76_LVBus0207961_production, 76_LVBus0207963_consumption, 76_LVBus0207963_production, 76_LVBus0207964_production, 76_LVBus0207965_consumption, 76_LVBus0207965_production, 76_LVBus0207967_consumption, 76_LVBus0207967_production, 76_LVBus0207968_consumption, 76_LVBus0207968_production, 76_LVBus0207969_production, 76_LVBus0207973_production, 76_LVBus0207974_production, 76_LVBus0207975_consumption, 76_LVBus0207975_production, 76_LVBus0207976_production, 76_LVBus0207978_production, 76_LVBus0207979_production, 76_LVBus0207980_production, 76_LVBus0207981_production, 76_LVBus0207982_production, 76_LVBus0207986_consumption, 76_LVBus0207986_production, 76_LVBus0207989_production, 76_LVBus0207991_consumption, 76_LVBus0207991_production, 76_LVBus0207992_consumption, 76_LVBus0207992_production, 76_LVBus0207993_production, 76_LVBus0207994_consumption, 76_LVBus0207994_production, 76_LVBus0207995_consumption, 76_LVBus0207995_production, 76_LVBus0207996_production, 76_LVBus0207997_consumption, 76_LVBus0207997_production, 76_LVBus0207998_consumption, 76_LVBus0207998_production, 76_LVBus0207999_consumption, 76_LVBus0207999_production, 76_LVBus0208000_production, 76_LVBus0208001_production, 76_LVBus0208005_production, 76_LVBus0208006_consumption, 76_LVBus0208006_production, 76_LVBus0208007_production, 76_LVBus0208008_consumption, 76_LVBus0208008_production, 76_LVBus0208009_production, 76_LVBus0208010_production, 76_LVBus0208011_production, 76_LVBus0208012_production, 76_LVBus0208013_consumption, 76_LVBus0208013_production, 76_LVBus0208014_production, 76_LVBus0208015_production, 76_LVBus0208016_consumption, 76_LVBus0208016_production, 76_LVBus0208017_consumption, 76_LVBus0208017_production, 76_LVBus0208018_production, 76_LVBus0208019_consumption, 76_LVBus0208019_production, 76_LVBus0208020_production, 76_LVBus0208021_production, 76_LVBus0208022_production, 76_LVBus0208026_production, 76_LVBus0208028_consumption, 76_LVBus0208028_production, 76_LVBus0208030_consumption, 76_LVBus0208030_production, 76_LVBus0208031_consumption, 76_LVBus0208031_production, 76_LVBus0208032_production, 76_LVBus0208033_consumption, 76_LVBus0208033_production, 76_LVBus0208035_consumption, 76_LVBus0208035_production, 76_LVBus0208037_consumption, 76_LVBus0208037_production, 76_LVBus0208038_production, 76_LVBus0208039_production, 76_LVBus0208040_production, 76_LVBus0208042_production, 76_LVBus0208043_production, 76_LVBus0208045_production, 76_LVBus0208046_consumption, 76_LVBus0208046_production, 76_LVBus0208047_production, 76_LVBus0208048_production, 76_LVBus0208049_production, 76_LVBus0208051_consumption, 76_LVBus0208051_production, 76_LVBus0208053_consumption, 76_LVBus0208053_production, 76_LVBus0208055_production, 76_LVBus0208056_consumption, 76_LVBus0208056_production, 76_LVBus0208058_consumption, 76_LVBus0208058_production, 76_LVBus0208059_production, 76_LVBus0208060_production, 76_LVBus0208061_production, 76_LVBus0208062_production, 76_LVBus0208063_consumption, 76_LVBus0208063_production, 76_LVBus0208064_production, 76_LVBus0208065_consumption, 76_LVBus0208065_production, 76_LVBus0208066_production, 76_LVBus0208067_production, 76_LVBus0208068_production, 76_LVBus0208069_production, 76_LVBus0208071_consumption, 76_LVBus0208071_production, 76_LVBus0208072_production, 76_LVBus0208073_production, 76_LVBus0208074_production, 76_LVBus0208075_production, 76_LVBus0208076_production, 76_LVBus0208077_consumption, 76_LVBus0208077_production, 76_LVBus0208078_consumption, 76_LVBus0208078_production, 76_LVBus0208079_consumption, 76_LVBus0208079_production, 76_LVBus0208080_production, 76_LVBus0208081_production, 76_LVBus0208082_production, 76_LVBus0208084_production, 76_LVBus0208085_production, 76_LVBus0208086_consumption, 76_LVBus0208086_production, 76_LVBus0208087_production, 76_LVBus0208088_production, 76_LVBus0208089_production, 76_LVBus0208090_production, 76_LVBus0208092_consumption, 76_LVBus0208092_production, 76_LVBus0208093_consumption, 76_LVBus0208093_production, 76_LVBus0208094_production, 76_LVBus0208095_consumption, 76_LVBus0208095_production, 76_LVBus0208096_production, 76_LVBus0208098_consumption, 76_LVBus0208098_production, 76_LVBus0208099_production, 76_LVBus0208100_production, 76_LVBus0208104_production, 76_LVBus0208105_consumption, 76_LVBus0208105_production, 76_LVBus0208106_production, 76_LVBus0208107_production, 76_LVBus0208109_production, 76_LVBus0208110_production, 76_LVBus0208111_consumption, 76_LVBus0208111_production, 76_LVBus0208113_production, 76_LVBus0208114_production, 76_LVBus0208115_production, 76_LVBus0208116_production, 76_LVBus0208117_production, 76_LVBus0208118_production, 76_LVBus0208119_consumption, 76_LVBus0208119_production, 76_LVBus0208120_production, 76_LVBus0208121_production, 76_LVBus0208122_production, 76_LVBus0208123_production, 76_LVBus0208124_production, 76_LVBus0208125_production, 76_LVBus0208126_production, 76_LVBus0208127_production, 76_LVBus0208129_production, 76_LVBus0208130_production, 76_LVBus0208131_consumption, 76_LVBus0208131_production, 76_LVBus0208132_production, 76_LVBus0208133_production, 76_LVBus0208135_consumption, 76_LVBus0208135_production, 76_LVBus0208136_consumption, 76_LVBus0208136_production, 76_LVBus0208137_consumption, 76_LVBus0208137_production, 76_LVBus0208138_consumption, 76_LVBus0208138_production, 76_LVBus0208139_consumption, 76_LVBus0208139_production, 76_LVBus0208140_consumption, 76_LVBus0208140_production, 76_LVBus0208141_production, 76_LVBus0208142_consumption, 76_LVBus0208142_production, 76_LVBus0208143_consumption, 76_LVBus0208143_production, 76_LVBus0208144_consumption, 76_LVBus0208144_production, 76_LVBus0208145_production, 76_LVBus0208146_consumption, 76_LVBus0208146_production, 76_LVBus0208147_production, 76_LVBus0208149_consumption, 76_LVBus0208149_production, 76_LVBus0208150_production, 76_LVBus0208151_consumption, 76_LVBus0208151_production, 76_LVBus0208152_production, 76_LVBus0208153_consumption, 76_LVBus0208153_production, 76_LVBus0208154_production, 76_LVBus0208155_consumption, 76_LVBus0208155_production, 76_LVBus0208156_production, 76_LVBus0208157_production, 76_LVBus0208158_production, 76_LVBus0208159_consumption, 76_LVBus0208159_production, 76_LVBus0208160_production, 76_LVBus0208161_production, 76_LVBus0208162_consumption, 76_LVBus0208162_production, 76_LVBus0208163_consumption, 76_LVBus0208163_production, 76_LVBus0208164_production, 76_LVBus0208165_production, 76_LVBus0208170_consumption, 76_LVBus0208170_production, 76_LVBus0208171_consumption, 76_LVBus0208171_production, 76_LVBus0208172_consumption, 76_LVBus0208172_production, 76_LVBus0208173_consumption, 76_LVBus0208173_production, 76_LVBus0208177_production, 76_LVBus0208179_consumption, 76_LVBus0208179_production, 76_LVBus0208180_consumption, 76_LVBus0208180_production, 76_LVBus0208181_production, 76_LVBus0208182_production, 76_LVBus0208183_production, 76_LVBus0208184_production, 76_LVBus0208185_production, 76_LVBus0208186_production, 76_LVBus0208187_production, 76_LVBus0208188_production, 76_LVBus0208190_production, 76_LVBus0208191_production, 76_LVBus0208192_production, 76_LVBus0208193_production, 76_LVBus0208194_production, 76_LVBus0208196_production, 76_LVBus0208197_production, 76_LVBus0208198_production, 76_LVBus0208199_production, 76_LVBus0208200_production, 76_LVBus0208201_production, 76_LVBus0208203_production, 76_LVBus0208204_production, 76_LVBus0208205_production, 76_LVBus0208206_production, 76_LVBus0208207_consumption, 76_LVBus0208207_production, 76_LVBus0208208_production, 76_LVBus0208209_production, 76_LVBus0208210_production, 76_LVBus0208211_production, 76_LVBus0208212_production, 76_LVBus0208213_production, 76_LVBus0208214_production, 76_LVBus0208215_production, 76_LVBus0208216_production, 76_LVBus0208217_production, 76_LVBus0208218_production, 76_LVBus0208219_production, 76_LVBus0208220_production, 76_LVBus0208221_production, 76_LVBus0208222_production, 76_LVBus0208223_production, 76_LVBus0208224_production, 76_LVBus0208228_production, 76_LVBus0208229_consumption, 76_LVBus0208229_production, 76_LVBus0208231_production, 76_LVBus0208232_production, 76_LVBus0208233_production, 76_LVBus0208234_production, 76_LVBus0208235_production, 76_LVBus0208236_production, 76_LVBus0208237_production, 76_LVBus0208238_production, 76_LVBus0208239_production, 76_LVBus0208240_production, 76_LVBus0208241_consumption, 76_LVBus0208241_production, 76_LVBus0208242_consumption, 76_LVBus0208242_production, 76_LVBus0208243_production, 76_LVBus0208244_production, 76_LVBus0208245_production, 76_LVBus0208246_production, 76_LVBus0208247_consumption, 76_LVBus0208247_production, 76_LVBus0208248_production, 76_LVBus0208249_production, 76_LVBus0208251_production, 76_LVBus0208252_production, 76_LVBus0208253_production, 76_LVBus0208254_production, 76_LVBus0208255_production, 76_LVBus0208256_production, 76_LVBus0208257_production, 76_LVBus0208258_consumption, 76_LVBus0208258_production, 76_LVBus0208259_production, 76_LVBus0208260_production, 76_LVBus0208261_production, 76_LVBus0208262_consumption, 76_LVBus0208262_production, 76_LVBus0208263_production, 76_LVBus0208265_production, 76_LVBus0208267_production, 76_LVBus0208268_consumption, 76_LVBus0208268_production, 76_LVBus0208269_production, 76_LVBus0208270_production, 76_LVBus0208271_production, 76_LVBus0208272_production, 76_LVBus0208273_production, 76_LVBus0208279_production, 76_LVBus0208280_production, 76_LVBus0208281_production, 76_LVBus0208283_production, 76_LVBus0208284_production, 76_LVBus0208285_production, 76_LVBus0208286_production, 76_LVBus0208287_consumption, 76_LVBus0208287_production, 76_LVBus0208288_production, 76_LVBus0208289_production, 76_LVBus0208290_production, 76_LVBus0208291_production, 76_LVBus0208292_production, 76_LVBus0208293_production, 76_LVBus0208294_production, 76_LVBus0208295_production, 76_LVBus0208296_production, 76_LVBus0208297_consumption, 76_LVBus0208297_production, 76_LVBus2048021_production, 76_LVBus2066010_consumption, 76_LVBus2066010_production, 76_LVBus2088328_production, 76_LVBus2088329_production, 76_LVBus2094394_consumption, 76_LVBus2094394_production, 76_LVBus2094826_production, 76_LVBus2104182_consumption, 76_LVBus2104182_production, 76_LVBus2108075_production, 76_LVBus2108076_consumption, 76_LVBus2108076_production, 76_LVBus2108077_production, 76_LVBus2108078_production, 76_LVBus2108079_production, 76_LVBus2108080_production, 76_LVBus2108081_production, 76_LVBus2108082_consumption, 76_LVBus2108082_production, 76_LVBus2108083_production, 76_LVBus2108084_production, 76_LVBus2108085_production, 76_LVBus2108086_production, 76_LVBus2108087_production, 76_LVBus2108088_production, 76_LVBus2108089_production, 76_LVBus2108090_production, 76_LVBus2153139_production, 76_LVBus2153140_production, 76_LVBus2153141_production, 76_LVBus2153142_production, 76_LVBus2153143_production, 76_LVBus2153144_consumption, 76_LVBus2153144_production, 76_LVBus2153145_production, 76_LVBus2153146_production, 76_LVBus2153147_production, 76_LVBus2153148_production, 76_LVBus2153149_production, 76_LVBus2153150_production, 76_LVBus2153151_production, 76_LVBus2153152_production, 76_LVBus2153153_consumption, 76_LVBus2153153_production, 76_LVBus2153154_consumption, 76_LVBus2153154_production, 76_LVBus2156667_production, 76_LVBus2162032_consumption, 76_LVBus2162032_production, 76_LVBus2162033_production, 76_LVBus2162034_production, 76_LVBus2162035_production, 76_LVBus2162036_consumption, 76_LVBus2162036_production, 76_MVLV008940_consumption, 76_MVLV008940_production, 76_MVLV086059_consumption, 76_MVLV086059_production, 76_MVLV103102_consumption, 76_MVLV103102_production, 76_MVLV117086_consumption, 76_MVLV117086_production, 76_MVLV127359_consumption, 76_MVLV127359_production, 76_MVLV145832_consumption, 76_MVLV145832_production.

## 9. Data Quality Summary

**Total findings:** 444 (0 errors, 5 warnings, 439 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  908 of 1406 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.48 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  909 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207726_consumption`  
  Load '76_LVBus0207726_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207902_consumption`  
  Load '76_LVBus0207902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207634_consumption`  
  Load '76_LVBus0207634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208132_consumption`  
  Load '76_LVBus0208132_consumption' has phase imbalance of 288.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208233_consumption`  
  Load '76_LVBus0208233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207709_consumption`  
  Load '76_LVBus0207709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207864_consumption`  
  Load '76_LVBus0207864_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208252_consumption`  
  Load '76_LVBus0208252_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208158_consumption`  
  Load '76_LVBus0208158_consumption' has phase imbalance of 217.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207913_consumption`  
  Load '76_LVBus0207913_consumption' has phase imbalance of 127.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207711_consumption`  
  Load '76_LVBus0207711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207647_consumption`  
  Load '76_LVBus0207647_consumption' has phase imbalance of 208.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2088329_consumption`  
  Load '76_LVBus2088329_consumption' has phase imbalance of 230.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207978_consumption`  
  Load '76_LVBus0207978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2162034_consumption`  
  Load '76_LVBus2162034_consumption' has phase imbalance of 274.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208291_consumption`  
  Load '76_LVBus0208291_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208201_consumption`  
  Load '76_LVBus0208201_consumption' has phase imbalance of 245.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153152_consumption`  
  Load '76_LVBus2153152_consumption' has phase imbalance of 228.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207795_consumption`  
  Load '76_LVBus0207795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207876_consumption`  
  Load '76_LVBus0207876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207733_consumption`  
  Load '76_LVBus0207733_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207529_consumption`  
  Load '76_LVBus0207529_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108088_consumption`  
  Load '76_LVBus2108088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208208_consumption`  
  Load '76_LVBus0208208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207798_consumption`  
  Load '76_LVBus0207798_consumption' has phase imbalance of 128.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207821_consumption`  
  Load '76_LVBus0207821_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207655_consumption`  
  Load '76_LVBus0207655_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208286_consumption`  
  Load '76_LVBus0208286_consumption' has phase imbalance of 57.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207551_consumption`  
  Load '76_LVBus0207551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207707_consumption`  
  Load '76_LVBus0207707_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153149_consumption`  
  Load '76_LVBus2153149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208074_consumption`  
  Load '76_LVBus0208074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207820_consumption`  
  Load '76_LVBus0207820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207664_consumption`  
  Load '76_LVBus0207664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208164_consumption`  
  Load '76_LVBus0208164_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208060_consumption`  
  Load '76_LVBus0208060_consumption' has phase imbalance of 287.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208150_consumption`  
  Load '76_LVBus0208150_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207513_consumption`  
  Load '76_LVBus0207513_consumption' has phase imbalance of 193.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207661_consumption`  
  Load '76_LVBus0207661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207912_consumption`  
  Load '76_LVBus0207912_consumption' has phase imbalance of 123.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208109_consumption`  
  Load '76_LVBus0208109_consumption' has phase imbalance of 181.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208100_consumption`  
  Load '76_LVBus0208100_consumption' has phase imbalance of 71.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207979_consumption`  
  Load '76_LVBus0207979_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207830_consumption`  
  Load '76_LVBus0207830_consumption' has phase imbalance of 204.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108081_consumption`  
  Load '76_LVBus2108081_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207657_consumption`  
  Load '76_LVBus0207657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108075_consumption`  
  Load '76_LVBus2108075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207640_consumption`  
  Load '76_LVBus0207640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208026_consumption`  
  Load '76_LVBus0208026_consumption' has phase imbalance of 83.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207601_consumption`  
  Load '76_LVBus0207601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207779_consumption`  
  Load '76_LVBus0207779_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153146_consumption`  
  Load '76_LVBus2153146_consumption' has phase imbalance of 203.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153147_consumption`  
  Load '76_LVBus2153147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208161_consumption`  
  Load '76_LVBus0208161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207744_consumption`  
  Load '76_LVBus0207744_consumption' has phase imbalance of 291.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208049_consumption`  
  Load '76_LVBus0208049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208232_consumption`  
  Load '76_LVBus0208232_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2094826_consumption`  
  Load '76_LVBus2094826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207834_consumption`  
  Load '76_LVBus0207834_consumption' has phase imbalance of 263.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207730_consumption`  
  Load '76_LVBus0207730_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207646_consumption`  
  Load '76_LVBus0207646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207788_consumption`  
  Load '76_LVBus0207788_consumption' has phase imbalance of 246.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207651_consumption`  
  Load '76_LVBus0207651_consumption' has phase imbalance of 170.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208047_consumption`  
  Load '76_LVBus0208047_consumption' has phase imbalance of 284.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207561_consumption`  
  Load '76_LVBus0207561_consumption' has phase imbalance of 187.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207585_consumption`  
  Load '76_LVBus0207585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207565_consumption`  
  Load '76_LVBus0207565_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207743_consumption`  
  Load '76_LVBus0207743_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2162035_consumption`  
  Load '76_LVBus2162035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208094_consumption`  
  Load '76_LVBus0208094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207636_consumption`  
  Load '76_LVBus0207636_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208011_consumption`  
  Load '76_LVBus0208011_consumption' has phase imbalance of 140.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153150_consumption`  
  Load '76_LVBus2153150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153139_consumption`  
  Load '76_LVBus2153139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207627_consumption`  
  Load '76_LVBus0207627_consumption' has phase imbalance of 149.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207800_consumption`  
  Load '76_LVBus0207800_consumption' has phase imbalance of 266.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207615_consumption`  
  Load '76_LVBus0207615_consumption' has phase imbalance of 280.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208156_consumption`  
  Load '76_LVBus0208156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207724_consumption`  
  Load '76_LVBus0207724_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207747_consumption`  
  Load '76_LVBus0207747_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207880_consumption`  
  Load '76_LVBus0207880_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207671_consumption`  
  Load '76_LVBus0207671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207750_consumption`  
  Load '76_LVBus0207750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208254_consumption`  
  Load '76_LVBus0208254_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208210_consumption`  
  Load '76_LVBus0208210_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207547_consumption`  
  Load '76_LVBus0207547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207677_consumption`  
  Load '76_LVBus0207677_consumption' has phase imbalance of 50.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207663_consumption`  
  Load '76_LVBus0207663_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207831_consumption`  
  Load '76_LVBus0207831_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208121_consumption`  
  Load '76_LVBus0208121_consumption' has phase imbalance of 59.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108080_consumption`  
  Load '76_LVBus2108080_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208269_consumption`  
  Load '76_LVBus0208269_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207926_consumption`  
  Load '76_LVBus0207926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207952_consumption`  
  Load '76_LVBus0207952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208125_consumption`  
  Load '76_LVBus0208125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207501_consumption`  
  Load '76_LVBus0207501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208209_consumption`  
  Load '76_LVBus0208209_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207639_consumption`  
  Load '76_LVBus0207639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208259_consumption`  
  Load '76_LVBus0208259_consumption' has phase imbalance of 268.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208200_consumption`  
  Load '76_LVBus0208200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208177_consumption`  
  Load '76_LVBus0208177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207759_consumption`  
  Load '76_LVBus0207759_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208186_consumption`  
  Load '76_LVBus0208186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207648_consumption`  
  Load '76_LVBus0207648_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208256_consumption`  
  Load '76_LVBus0208256_consumption' has phase imbalance of 288.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208231_consumption`  
  Load '76_LVBus0208231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208239_consumption`  
  Load '76_LVBus0208239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207718_consumption`  
  Load '76_LVBus0207718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208045_consumption`  
  Load '76_LVBus0208045_consumption' has phase imbalance of 227.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207787_consumption`  
  Load '76_LVBus0207787_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207734_consumption`  
  Load '76_LVBus0207734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207850_consumption`  
  Load '76_LVBus0207850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208213_consumption`  
  Load '76_LVBus0208213_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207828_consumption`  
  Load '76_LVBus0207828_consumption' has phase imbalance of 175.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208080_consumption`  
  Load '76_LVBus0208080_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208147_consumption`  
  Load '76_LVBus0208147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207635_consumption`  
  Load '76_LVBus0207635_consumption' has phase imbalance of 215.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208182_consumption`  
  Load '76_LVBus0208182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207736_consumption`  
  Load '76_LVBus0207736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208270_consumption`  
  Load '76_LVBus0208270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208265_consumption`  
  Load '76_LVBus0208265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208214_consumption`  
  Load '76_LVBus0208214_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208141_consumption`  
  Load '76_LVBus0208141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208066_consumption`  
  Load '76_LVBus0208066_consumption' has phase imbalance of 98.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207969_consumption`  
  Load '76_LVBus0207969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208183_consumption`  
  Load '76_LVBus0208183_consumption' has phase imbalance of 288.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207695_consumption`  
  Load '76_LVBus0207695_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108083_consumption`  
  Load '76_LVBus2108083_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207892_consumption`  
  Load '76_LVBus0207892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207653_consumption`  
  Load '76_LVBus0207653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207804_consumption`  
  Load '76_LVBus0207804_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207609_consumption`  
  Load '76_LVBus0207609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207548_consumption`  
  Load '76_LVBus0207548_consumption' has phase imbalance of 221.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208181_consumption`  
  Load '76_LVBus0208181_consumption' has phase imbalance of 274.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207891_consumption`  
  Load '76_LVBus0207891_consumption' has phase imbalance of 289.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207545_consumption`  
  Load '76_LVBus0207545_consumption' has phase imbalance of 281.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208117_consumption`  
  Load '76_LVBus0208117_consumption' has phase imbalance of 137.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207534_consumption`  
  Load '76_LVBus0207534_consumption' has phase imbalance of 118.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207973_consumption`  
  Load '76_LVBus0207973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208212_consumption`  
  Load '76_LVBus0208212_consumption' has phase imbalance of 39.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207616_consumption`  
  Load '76_LVBus0207616_consumption' has phase imbalance of 26.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208253_consumption`  
  Load '76_LVBus0208253_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208120_consumption`  
  Load '76_LVBus0208120_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208240_consumption`  
  Load '76_LVBus0208240_consumption' has phase imbalance of 170.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208216_consumption`  
  Load '76_LVBus0208216_consumption' has phase imbalance of 209.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2162033_consumption`  
  Load '76_LVBus2162033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207805_consumption`  
  Load '76_LVBus0207805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208089_consumption`  
  Load '76_LVBus0208089_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207643_consumption`  
  Load '76_LVBus0207643_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207578_consumption`  
  Load '76_LVBus0207578_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208283_consumption`  
  Load '76_LVBus0208283_consumption' has phase imbalance of 138.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208204_consumption`  
  Load '76_LVBus0208204_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207757_consumption`  
  Load '76_LVBus0207757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207867_consumption`  
  Load '76_LVBus0207867_consumption' has phase imbalance of 76.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208188_consumption`  
  Load '76_LVBus0208188_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208228_consumption`  
  Load '76_LVBus0208228_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208073_consumption`  
  Load '76_LVBus0208073_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207758_consumption`  
  Load '76_LVBus0207758_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208067_consumption`  
  Load '76_LVBus0208067_consumption' has phase imbalance of 297.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207878_consumption`  
  Load '76_LVBus0207878_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208068_consumption`  
  Load '76_LVBus0208068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207654_consumption`  
  Load '76_LVBus0207654_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207873_consumption`  
  Load '76_LVBus0207873_consumption' has phase imbalance of 142.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2048021_consumption`  
  Load '76_LVBus2048021_consumption' has phase imbalance of 84.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207751_consumption`  
  Load '76_LVBus0207751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208126_consumption`  
  Load '76_LVBus0208126_consumption' has phase imbalance of 127.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207932_consumption`  
  Load '76_LVBus0207932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207642_consumption`  
  Load '76_LVBus0207642_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207982_consumption`  
  Load '76_LVBus0207982_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207916_consumption`  
  Load '76_LVBus0207916_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208211_consumption`  
  Load '76_LVBus0208211_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208165_consumption`  
  Load '76_LVBus0208165_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208072_consumption`  
  Load '76_LVBus0208072_consumption' has phase imbalance of 286.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207746_consumption`  
  Load '76_LVBus0207746_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208237_consumption`  
  Load '76_LVBus0208237_consumption' has phase imbalance of 203.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208257_consumption`  
  Load '76_LVBus0208257_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207721_consumption`  
  Load '76_LVBus0207721_consumption' has phase imbalance of 254.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207691_consumption`  
  Load '76_LVBus0207691_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153148_consumption`  
  Load '76_LVBus2153148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207678_consumption`  
  Load '76_LVBus0207678_consumption' has phase imbalance of 103.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207869_consumption`  
  Load '76_LVBus0207869_consumption' has phase imbalance of 239.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207515_consumption`  
  Load '76_LVBus0207515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208116_consumption`  
  Load '76_LVBus0208116_consumption' has phase imbalance of 252.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208096_consumption`  
  Load '76_LVBus0208096_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208248_consumption`  
  Load '76_LVBus0208248_consumption' has phase imbalance of 131.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208196_consumption`  
  Load '76_LVBus0208196_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207871_consumption`  
  Load '76_LVBus0207871_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208251_consumption`  
  Load '76_LVBus0208251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207799_consumption`  
  Load '76_LVBus0207799_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207752_consumption`  
  Load '76_LVBus0207752_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207688_consumption`  
  Load '76_LVBus0207688_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207676_consumption`  
  Load '76_LVBus0207676_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108079_consumption`  
  Load '76_LVBus2108079_consumption' has phase imbalance of 142.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208295_consumption`  
  Load '76_LVBus0208295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207801_consumption`  
  Load '76_LVBus0207801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208219_consumption`  
  Load '76_LVBus0208219_consumption' has phase imbalance of 171.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207713_consumption`  
  Load '76_LVBus0207713_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207559_consumption`  
  Load '76_LVBus0207559_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208001_consumption`  
  Load '76_LVBus0208001_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207717_consumption`  
  Load '76_LVBus0207717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207698_consumption`  
  Load '76_LVBus0207698_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207911_consumption`  
  Load '76_LVBus0207911_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207745_consumption`  
  Load '76_LVBus0207745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207509_consumption`  
  Load '76_LVBus0207509_consumption' has phase imbalance of 297.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208206_consumption`  
  Load '76_LVBus0208206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153151_consumption`  
  Load '76_LVBus2153151_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207575_consumption`  
  Load '76_LVBus0207575_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208084_consumption`  
  Load '76_LVBus0208084_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207936_consumption`  
  Load '76_LVBus0207936_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207756_consumption`  
  Load '76_LVBus0207756_consumption' has phase imbalance of 94.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208152_consumption`  
  Load '76_LVBus0208152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207934_consumption`  
  Load '76_LVBus0207934_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207780_consumption`  
  Load '76_LVBus0207780_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207739_consumption`  
  Load '76_LVBus0207739_consumption' has phase imbalance of 98.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207890_consumption`  
  Load '76_LVBus0207890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208090_consumption`  
  Load '76_LVBus0208090_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207874_consumption`  
  Load '76_LVBus0207874_consumption' has phase imbalance of 129.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208145_consumption`  
  Load '76_LVBus0208145_consumption' has phase imbalance of 224.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207511_consumption`  
  Load '76_LVBus0207511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207832_consumption`  
  Load '76_LVBus0207832_consumption' has phase imbalance of 266.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207976_consumption`  
  Load '76_LVBus0207976_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207668_consumption`  
  Load '76_LVBus0207668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207914_consumption`  
  Load '76_LVBus0207914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208255_consumption`  
  Load '76_LVBus0208255_consumption' has phase imbalance of 65.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208075_consumption`  
  Load '76_LVBus0208075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208281_consumption`  
  Load '76_LVBus0208281_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208118_consumption`  
  Load '76_LVBus0208118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207940_consumption`  
  Load '76_LVBus0207940_consumption' has phase imbalance of 39.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207749_consumption`  
  Load '76_LVBus0207749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207840_consumption`  
  Load '76_LVBus0207840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207980_consumption`  
  Load '76_LVBus0207980_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207641_consumption`  
  Load '76_LVBus0207641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208154_consumption`  
  Load '76_LVBus0208154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108085_consumption`  
  Load '76_LVBus2108085_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208022_consumption`  
  Load '76_LVBus0208022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207760_consumption`  
  Load '76_LVBus0207760_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207839_consumption`  
  Load '76_LVBus0207839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207981_consumption`  
  Load '76_LVBus0207981_consumption' has phase imbalance of 245.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208284_consumption`  
  Load '76_LVBus0208284_consumption' has phase imbalance of 46.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207808_consumption`  
  Load '76_LVBus0207808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207696_consumption`  
  Load '76_LVBus0207696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207943_consumption`  
  Load '76_LVBus0207943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208184_consumption`  
  Load '76_LVBus0208184_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208032_consumption`  
  Load '76_LVBus0208032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207729_consumption`  
  Load '76_LVBus0207729_consumption' has phase imbalance of 180.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108090_consumption`  
  Load '76_LVBus2108090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208279_consumption`  
  Load '76_LVBus0208279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207626_consumption`  
  Load '76_LVBus0207626_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207666_consumption`  
  Load '76_LVBus0207666_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207656_consumption`  
  Load '76_LVBus0207656_consumption' has phase imbalance of 287.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208220_consumption`  
  Load '76_LVBus0208220_consumption' has phase imbalance of 201.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207847_consumption`  
  Load '76_LVBus0207847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208263_consumption`  
  Load '76_LVBus0208263_consumption' has phase imbalance of 103.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207822_consumption`  
  Load '76_LVBus0207822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207893_consumption`  
  Load '76_LVBus0207893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207835_consumption`  
  Load '76_LVBus0207835_consumption' has phase imbalance of 143.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153140_consumption`  
  Load '76_LVBus2153140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208296_consumption`  
  Load '76_LVBus0208296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208198_consumption`  
  Load '76_LVBus0208198_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207690_consumption`  
  Load '76_LVBus0207690_consumption' has phase imbalance of 69.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207796_consumption`  
  Load '76_LVBus0207796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207938_consumption`  
  Load '76_LVBus0207938_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207728_consumption`  
  Load '76_LVBus0207728_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207895_consumption`  
  Load '76_LVBus0207895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207945_consumption`  
  Load '76_LVBus0207945_consumption' has phase imbalance of 201.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208082_consumption`  
  Load '76_LVBus0208082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207552_consumption`  
  Load '76_LVBus0207552_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108084_consumption`  
  Load '76_LVBus2108084_consumption' has phase imbalance of 217.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208115_consumption`  
  Load '76_LVBus0208115_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208039_consumption`  
  Load '76_LVBus0208039_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208236_consumption`  
  Load '76_LVBus0208236_consumption' has phase imbalance of 121.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207596_consumption`  
  Load '76_LVBus0207596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208088_consumption`  
  Load '76_LVBus0208088_consumption' has phase imbalance of 221.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207645_consumption`  
  Load '76_LVBus0207645_consumption' has phase imbalance of 194.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208273_consumption`  
  Load '76_LVBus0208273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208193_consumption`  
  Load '76_LVBus0208193_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207872_consumption`  
  Load '76_LVBus0207872_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207817_consumption`  
  Load '76_LVBus0207817_consumption' has phase imbalance of 183.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208040_consumption`  
  Load '76_LVBus0208040_consumption' has phase imbalance of 117.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207868_consumption`  
  Load '76_LVBus0207868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208217_consumption`  
  Load '76_LVBus0208217_consumption' has phase imbalance of 275.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207731_consumption`  
  Load '76_LVBus0207731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207674_consumption`  
  Load '76_LVBus0207674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153143_consumption`  
  Load '76_LVBus2153143_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207786_consumption`  
  Load '76_LVBus0207786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207600_consumption`  
  Load '76_LVBus0207600_consumption' has phase imbalance of 252.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208197_consumption`  
  Load '76_LVBus0208197_consumption' has phase imbalance of 277.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208199_consumption`  
  Load '76_LVBus0208199_consumption' has phase imbalance of 280.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208260_consumption`  
  Load '76_LVBus0208260_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207533_consumption`  
  Load '76_LVBus0207533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208122_consumption`  
  Load '76_LVBus0208122_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207530_consumption`  
  Load '76_LVBus0207530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207904_consumption`  
  Load '76_LVBus0207904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207928_consumption`  
  Load '76_LVBus0207928_consumption' has phase imbalance of 282.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207838_consumption`  
  Load '76_LVBus0207838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207993_consumption`  
  Load '76_LVBus0207993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207700_consumption`  
  Load '76_LVBus0207700_consumption' has phase imbalance of 289.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207605_consumption`  
  Load '76_LVBus0207605_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207875_consumption`  
  Load '76_LVBus0207875_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207802_consumption`  
  Load '76_LVBus0207802_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208215_consumption`  
  Load '76_LVBus0208215_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207774_consumption`  
  Load '76_LVBus0207774_consumption' has phase imbalance of 267.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207599_consumption`  
  Load '76_LVBus0207599_consumption' has phase imbalance of 287.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208104_consumption`  
  Load '76_LVBus0208104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207833_consumption`  
  Load '76_LVBus0207833_consumption' has phase imbalance of 208.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207879_consumption`  
  Load '76_LVBus0207879_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208123_consumption`  
  Load '76_LVBus0208123_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207811_consumption`  
  Load '76_LVBus0207811_consumption' has phase imbalance of 223.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207570_consumption`  
  Load '76_LVBus0207570_consumption' has phase imbalance of 122.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208205_consumption`  
  Load '76_LVBus0208205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208222_consumption`  
  Load '76_LVBus0208222_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207889_consumption`  
  Load '76_LVBus0207889_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208113_consumption`  
  Load '76_LVBus0208113_consumption' has phase imbalance of 289.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208015_consumption`  
  Load '76_LVBus0208015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207748_consumption`  
  Load '76_LVBus0207748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108089_consumption`  
  Load '76_LVBus2108089_consumption' has phase imbalance of 221.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207628_consumption`  
  Load '76_LVBus0207628_consumption' has phase imbalance of 280.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108086_consumption`  
  Load '76_LVBus2108086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207807_consumption`  
  Load '76_LVBus0207807_consumption' has phase imbalance of 275.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207693_consumption`  
  Load '76_LVBus0207693_consumption' has phase imbalance of 235.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207775_consumption`  
  Load '76_LVBus0207775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208285_consumption`  
  Load '76_LVBus0208285_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207604_consumption`  
  Load '76_LVBus0207604_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207887_consumption`  
  Load '76_LVBus0207887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207720_consumption`  
  Load '76_LVBus0207720_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153142_consumption`  
  Load '76_LVBus2153142_consumption' has phase imbalance of 280.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208009_consumption`  
  Load '76_LVBus0208009_consumption' has phase imbalance of 120.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208235_consumption`  
  Load '76_LVBus0208235_consumption' has phase imbalance of 164.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208062_consumption`  
  Load '76_LVBus0208062_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208292_consumption`  
  Load '76_LVBus0208292_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207964_consumption`  
  Load '76_LVBus0207964_consumption' has phase imbalance of 50.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207763_consumption`  
  Load '76_LVBus0207763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207673_consumption`  
  Load '76_LVBus0207673_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207845_consumption`  
  Load '76_LVBus0207845_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207514_consumption`  
  Load '76_LVBus0207514_consumption' has phase imbalance of 271.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207762_consumption`  
  Load '76_LVBus0207762_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208014_consumption`  
  Load '76_LVBus0208014_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207732_consumption`  
  Load '76_LVBus0207732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208271_consumption`  
  Load '76_LVBus0208271_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207550_consumption`  
  Load '76_LVBus0207550_consumption' has phase imbalance of 240.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208107_consumption`  
  Load '76_LVBus0208107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153141_consumption`  
  Load '76_LVBus2153141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207592_consumption`  
  Load '76_LVBus0207592_consumption' has phase imbalance of 215.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208055_consumption`  
  Load '76_LVBus0208055_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207827_consumption`  
  Load '76_LVBus0207827_consumption' has phase imbalance of 187.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207888_consumption`  
  Load '76_LVBus0207888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207881_consumption`  
  Load '76_LVBus0207881_consumption' has phase imbalance of 189.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207725_consumption`  
  Load '76_LVBus0207725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207675_consumption`  
  Load '76_LVBus0207675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208191_consumption`  
  Load '76_LVBus0208191_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207863_consumption`  
  Load '76_LVBus0207863_consumption' has phase imbalance of 33.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208246_consumption`  
  Load '76_LVBus0208246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208294_consumption`  
  Load '76_LVBus0208294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208272_consumption`  
  Load '76_LVBus0208272_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208218_consumption`  
  Load '76_LVBus0208218_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207644_consumption`  
  Load '76_LVBus0207644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207753_consumption`  
  Load '76_LVBus0207753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207679_consumption`  
  Load '76_LVBus0207679_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207931_consumption`  
  Load '76_LVBus0207931_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207915_consumption`  
  Load '76_LVBus0207915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207589_consumption`  
  Load '76_LVBus0207589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208293_consumption`  
  Load '76_LVBus0208293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108087_consumption`  
  Load '76_LVBus2108087_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207957_consumption`  
  Load '76_LVBus0207957_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207637_consumption`  
  Load '76_LVBus0207637_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208048_consumption`  
  Load '76_LVBus0208048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207843_consumption`  
  Load '76_LVBus0207843_consumption' has phase imbalance of 244.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2153145_consumption`  
  Load '76_LVBus2153145_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108077_consumption`  
  Load '76_LVBus2108077_consumption' has phase imbalance of 285.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207694_consumption`  
  Load '76_LVBus0207694_consumption' has phase imbalance of 146.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208127_consumption`  
  Load '76_LVBus0208127_consumption' has phase imbalance of 282.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207702_consumption`  
  Load '76_LVBus0207702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207703_consumption`  
  Load '76_LVBus0207703_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207714_consumption`  
  Load '76_LVBus0207714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208133_consumption`  
  Load '76_LVBus0208133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208129_consumption`  
  Load '76_LVBus0208129_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207974_consumption`  
  Load '76_LVBus0207974_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207712_consumption`  
  Load '76_LVBus0207712_consumption' has phase imbalance of 278.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207785_consumption`  
  Load '76_LVBus0207785_consumption' has phase imbalance of 244.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207558_consumption`  
  Load '76_LVBus0207558_consumption' has phase imbalance of 80.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207710_consumption`  
  Load '76_LVBus0207710_consumption' has phase imbalance of 264.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208124_consumption`  
  Load '76_LVBus0208124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208221_consumption`  
  Load '76_LVBus0208221_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207909_consumption`  
  Load '76_LVBus0207909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207537_consumption`  
  Load '76_LVBus0207537_consumption' has phase imbalance of 143.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207560_consumption`  
  Load '76_LVBus0207560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208114_consumption`  
  Load '76_LVBus0208114_consumption' has phase imbalance of 278.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208020_consumption`  
  Load '76_LVBus0208020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207662_consumption`  
  Load '76_LVBus0207662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208087_consumption`  
  Load '76_LVBus0208087_consumption' has phase imbalance of 85.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207844_consumption`  
  Load '76_LVBus0207844_consumption' has phase imbalance of 133.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207797_consumption`  
  Load '76_LVBus0207797_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208190_consumption`  
  Load '76_LVBus0208190_consumption' has phase imbalance of 275.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208203_consumption`  
  Load '76_LVBus0208203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2108078_consumption`  
  Load '76_LVBus2108078_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208157_consumption`  
  Load '76_LVBus0208157_consumption' has phase imbalance of 228.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208069_consumption`  
  Load '76_LVBus0208069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207951_consumption`  
  Load '76_LVBus0207951_consumption' has phase imbalance of 116.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207512_consumption`  
  Load '76_LVBus0207512_consumption' has phase imbalance of 268.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207755_consumption`  
  Load '76_LVBus0207755_consumption' has phase imbalance of 51.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207918_consumption`  
  Load '76_LVBus0207918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207579_consumption`  
  Load '76_LVBus0207579_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208064_consumption`  
  Load '76_LVBus0208064_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207823_consumption`  
  Load '76_LVBus0207823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207602_consumption`  
  Load '76_LVBus0207602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208194_consumption`  
  Load '76_LVBus0208194_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208224_consumption`  
  Load '76_LVBus0208224_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207716_consumption`  
  Load '76_LVBus0207716_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207894_consumption`  
  Load '76_LVBus0207894_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208038_consumption`  
  Load '76_LVBus0208038_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207665_consumption`  
  Load '76_LVBus0207665_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208085_consumption`  
  Load '76_LVBus0208085_consumption' has phase imbalance of 149.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0207598_consumption`  
  Load '76_LVBus0207598_consumption' has phase imbalance of 132.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0208192_consumption`  
  Load '76_LVBus0208192_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1406 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0207989' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0207923' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0207948' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0207539' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LACAU' (MV, 11.78 kV) has an electrical reach of 27.67 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0207511' (LV, 0.24 kV) has an electrical reach of 1.51 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0208267' (LV, 0.24 kV) has an electrical reach of 2.01 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0207861' (LV, 0.24 kV) has an electrical reach of 1.05 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus0207989' (LV, 0.24 kV) has an electrical reach of 7.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  927 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '76_LVBranch0610332' and '76_LVBranch0539072' at bus '76_LVBus0208267' have ||Z||_F ratio 1740.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  295 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 76_LVBus0207501_consumption, 76_LVBus0207509_consumption, 76_LVBus0207511_consumption, 76_LVBus0207512_consumption, 76_LVBus0207513_consumption, 76_LVBus0207514_consumption, 76_LVBus0207515_consumption, 76_LVBus0207529_consumption, 76_LVBus0207530_consumption, 76_LVBus0207533_consumption, 76_LVBus0207547_consumption, 76_LVBus0207550_consumption, 76_LVBus0207551_consumption, 76_LVBus0207552_consumption, 76_LVBus0207560_consumption, 76_LVBus0207575_consumption, 76_LVBus0207578_consumption, 76_LVBus0207579_consumption, 76_LVBus0207585_consumption, 76_LVBus0207589_consumption, 76_LVBus0207596_consumption, 76_LVBus0207599_consumption, 76_LVBus0207600_consumption, 76_LVBus0207601_consumption, 76_LVBus0207602_consumption, 76_LVBus0207605_consumption, 76_LVBus0207609_consumption, 76_LVBus0207615_consumption, 76_LVBus0207628_consumption, 76_LVBus0207634_consumption, 76_LVBus0207635_consumption, 76_LVBus0207636_consumption, 76_LVBus0207637_consumption, 76_LVBus0207639_consumption, 76_LVBus0207640_consumption, 76_LVBus0207641_consumption, 76_LVBus0207642_consumption, 76_LVBus0207643_consumption, 76_LVBus0207644_consumption, 76_LVBus0207645_consumption, 76_LVBus0207646_consumption, 76_LVBus0207647_consumption, 76_LVBus0207648_consumption, 76_LVBus0207653_consumption, 76_LVBus0207654_consumption, 76_LVBus0207655_consumption, 76_LVBus0207656_consumption, 76_LVBus0207657_consumption, 76_LVBus0207661_consumption, 76_LVBus0207662_consumption, 76_LVBus0207663_consumption, 76_LVBus0207664_consumption, 76_LVBus0207665_consumption, 76_LVBus0207666_consumption, 76_LVBus0207668_consumption, 76_LVBus0207671_consumption, 76_LVBus0207673_consumption, 76_LVBus0207674_consumption, 76_LVBus0207675_consumption, 76_LVBus0207688_consumption, 76_LVBus0207691_consumption, 76_LVBus0207693_consumption, 76_LVBus0207695_consumption, 76_LVBus0207696_consumption, 76_LVBus0207700_consumption, 76_LVBus0207702_consumption, 76_LVBus0207707_consumption, 76_LVBus0207709_consumption, 76_LVBus0207710_consumption, 76_LVBus0207711_consumption, 76_LVBus0207714_consumption, 76_LVBus0207717_consumption, 76_LVBus0207718_consumption, 76_LVBus0207721_consumption, 76_LVBus0207724_consumption, 76_LVBus0207725_consumption, 76_LVBus0207729_consumption, 76_LVBus0207730_consumption, 76_LVBus0207731_consumption, 76_LVBus0207732_consumption, 76_LVBus0207734_consumption, 76_LVBus0207736_consumption, 76_LVBus0207743_consumption, 76_LVBus0207744_consumption, 76_LVBus0207745_consumption, 76_LVBus0207746_consumption, 76_LVBus0207747_consumption, 76_LVBus0207748_consumption, 76_LVBus0207749_consumption, 76_LVBus0207750_consumption, 76_LVBus0207751_consumption, 76_LVBus0207752_consumption, 76_LVBus0207753_consumption, 76_LVBus0207757_consumption, 76_LVBus0207759_consumption, 76_LVBus0207760_consumption, 76_LVBus0207762_consumption, 76_LVBus0207763_consumption, 76_LVBus0207775_consumption, 76_LVBus0207779_consumption, 76_LVBus0207780_consumption, 76_LVBus0207785_consumption, 76_LVBus0207786_consumption, 76_LVBus0207787_consumption, 76_LVBus0207788_consumption, 76_LVBus0207795_consumption, 76_LVBus0207796_consumption, 76_LVBus0207797_consumption, 76_LVBus0207800_consumption, 76_LVBus0207801_consumption, 76_LVBus0207802_consumption, 76_LVBus0207804_consumption, 76_LVBus0207805_consumption, 76_LVBus0207807_consumption, 76_LVBus0207808_consumption, 76_LVBus0207811_consumption, 76_LVBus0207817_consumption, 76_LVBus0207820_consumption, 76_LVBus0207821_consumption, 76_LVBus0207822_consumption, 76_LVBus0207823_consumption, 76_LVBus0207832_consumption, 76_LVBus0207833_consumption, 76_LVBus0207834_consumption, 76_LVBus0207838_consumption, 76_LVBus0207839_consumption, 76_LVBus0207840_consumption, 76_LVBus0207843_consumption, 76_LVBus0207845_consumption, 76_LVBus0207847_consumption, 76_LVBus0207850_consumption, 76_LVBus0207864_consumption, 76_LVBus0207868_consumption, 76_LVBus0207871_consumption, 76_LVBus0207876_consumption, 76_LVBus0207878_consumption, 76_LVBus0207879_consumption, 76_LVBus0207887_consumption, 76_LVBus0207888_consumption, 76_LVBus0207889_consumption, 76_LVBus0207890_consumption, 76_LVBus0207891_consumption, 76_LVBus0207892_consumption, 76_LVBus0207893_consumption, 76_LVBus0207894_consumption, 76_LVBus0207895_consumption, 76_LVBus0207902_consumption, 76_LVBus0207904_consumption, 76_LVBus0207909_consumption, 76_LVBus0207911_consumption, 76_LVBus0207914_consumption, 76_LVBus0207915_consumption, 76_LVBus0207916_consumption, 76_LVBus0207918_consumption, 76_LVBus0207926_consumption, 76_LVBus0207928_consumption, 76_LVBus0207931_consumption, 76_LVBus0207932_consumption, 76_LVBus0207934_consumption, 76_LVBus0207936_consumption, 76_LVBus0207938_consumption, 76_LVBus0207943_consumption, 76_LVBus0207945_consumption, 76_LVBus0207952_consumption, 76_LVBus0207957_consumption, 76_LVBus0207969_consumption, 76_LVBus0207973_consumption, 76_LVBus0207974_consumption, 76_LVBus0207976_consumption, 76_LVBus0207978_consumption, 76_LVBus0207980_consumption, 76_LVBus0207981_consumption, 76_LVBus0207982_consumption, 76_LVBus0207993_consumption, 76_LVBus0208015_consumption, 76_LVBus0208020_consumption, 76_LVBus0208022_consumption, 76_LVBus0208032_consumption, 76_LVBus0208038_consumption, 76_LVBus0208045_consumption, 76_LVBus0208047_consumption, 76_LVBus0208048_consumption, 76_LVBus0208049_consumption, 76_LVBus0208055_consumption, 76_LVBus0208060_consumption, 76_LVBus0208062_consumption, 76_LVBus0208064_consumption, 76_LVBus0208067_consumption, 76_LVBus0208068_consumption, 76_LVBus0208069_consumption, 76_LVBus0208072_consumption, 76_LVBus0208073_consumption, 76_LVBus0208074_consumption, 76_LVBus0208075_consumption, 76_LVBus0208080_consumption, 76_LVBus0208082_consumption, 76_LVBus0208084_consumption, 76_LVBus0208094_consumption, 76_LVBus0208104_consumption, 76_LVBus0208107_consumption, 76_LVBus0208113_consumption, 76_LVBus0208114_consumption, 76_LVBus0208116_consumption, 76_LVBus0208118_consumption, 76_LVBus0208124_consumption, 76_LVBus0208125_consumption, 76_LVBus0208127_consumption, 76_LVBus0208132_consumption, 76_LVBus0208133_consumption, 76_LVBus0208141_consumption, 76_LVBus0208147_consumption, 76_LVBus0208150_consumption, 76_LVBus0208152_consumption, 76_LVBus0208154_consumption, 76_LVBus0208156_consumption, 76_LVBus0208157_consumption, 76_LVBus0208158_consumption, 76_LVBus0208161_consumption, 76_LVBus0208164_consumption, 76_LVBus0208165_consumption, 76_LVBus0208177_consumption, 76_LVBus0208181_consumption, 76_LVBus0208182_consumption, 76_LVBus0208183_consumption, 76_LVBus0208184_consumption, 76_LVBus0208186_consumption, 76_LVBus0208188_consumption, 76_LVBus0208190_consumption, 76_LVBus0208191_consumption, 76_LVBus0208193_consumption, 76_LVBus0208194_consumption, 76_LVBus0208196_consumption, 76_LVBus0208197_consumption, 76_LVBus0208198_consumption, 76_LVBus0208199_consumption, 76_LVBus0208200_consumption, 76_LVBus0208201_consumption, 76_LVBus0208203_consumption, 76_LVBus0208204_consumption, 76_LVBus0208205_consumption, 76_LVBus0208206_consumption, 76_LVBus0208208_consumption, 76_LVBus0208209_consumption, 76_LVBus0208211_consumption, 76_LVBus0208217_consumption, 76_LVBus0208220_consumption, 76_LVBus0208224_consumption, 76_LVBus0208231_consumption, 76_LVBus0208232_consumption, 76_LVBus0208233_consumption, 76_LVBus0208237_consumption, 76_LVBus0208239_consumption, 76_LVBus0208246_consumption, 76_LVBus0208251_consumption, 76_LVBus0208252_consumption, 76_LVBus0208254_consumption, 76_LVBus0208256_consumption, 76_LVBus0208259_consumption, 76_LVBus0208260_consumption, 76_LVBus0208265_consumption, 76_LVBus0208269_consumption, 76_LVBus0208270_consumption, 76_LVBus0208273_consumption, 76_LVBus0208279_consumption, 76_LVBus0208292_consumption, 76_LVBus0208293_consumption, 76_LVBus0208294_consumption, 76_LVBus0208295_consumption, 76_LVBus0208296_consumption, 76_LVBus2088329_consumption, 76_LVBus2094826_consumption, 76_LVBus2108075_consumption, 76_LVBus2108077_consumption, 76_LVBus2108080_consumption, 76_LVBus2108085_consumption, 76_LVBus2108086_consumption, 76_LVBus2108088_consumption, 76_LVBus2108089_consumption, 76_LVBus2108090_consumption, 76_LVBus2153139_consumption, 76_LVBus2153140_consumption, 76_LVBus2153141_consumption, 76_LVBus2153142_consumption, 76_LVBus2153143_consumption, 76_LVBus2153145_consumption, 76_LVBus2153146_consumption, 76_LVBus2153147_consumption, 76_LVBus2153148_consumption, 76_LVBus2153149_consumption, 76_LVBus2153150_consumption, 76_LVBus2153151_consumption, 76_LVBus2153152_consumption, 76_LVBus2162033_consumption, 76_LVBus2162034_consumption, 76_LVBus2162035_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  703 group(s) of loads (1406 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  17 group(s) of series lines (36 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  909 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0207500_consumption, 76_LVBus0207500_production, 76_LVBus0207501_production, 76_LVBus0207502_consumption, 76_LVBus0207502_production, 76_LVBus0207503_consumption, 76_LVBus0207503_production, 76_LVBus0207504_consumption, 76_LVBus0207504_production, 76_LVBus0207506_consumption, 76_LVBus0207506_production, 76_LVBus0207507_consumption, 76_LVBus0207507_production, 76_LVBus0207508_production, 76_LVBus0207509_production, 76_LVBus0207511_production, 76_LVBus0207512_production, 76_LVBus0207513_production, 76_LVBus0207514_production, 76_LVBus0207515_production, 76_LVBus0207516_consumption, 76_LVBus0207516_production, 76_LVBus0207517_consumption, 76_LVBus0207517_production, 76_LVBus0207518_consumption, 76_LVBus0207518_production, 76_LVBus0207519_consumption, 76_LVBus0207519_production, 76_LVBus0207520_consumption, 76_LVBus0207520_production, 76_LVBus0207521_consumption, 76_LVBus0207521_production, 76_LVBus0207522_consumption, 76_LVBus0207522_production, 76_LVBus0207523_consumption, 76_LVBus0207523_production, 76_LVBus0207524_consumption, 76_LVBus0207524_production, 76_LVBus0207525_consumption, 76_LVBus0207525_production, 76_LVBus0207526_consumption, 76_LVBus0207526_production, 76_LVBus0207527_consumption, 76_LVBus0207527_production, 76_LVBus0207528_consumption, 76_LVBus0207528_production, 76_LVBus0207529_production, 76_LVBus0207530_production, 76_LVBus0207531_production, 76_LVBus0207533_production, 76_LVBus0207534_production, 76_LVBus0207535_consumption, 76_LVBus0207535_production, 76_LVBus0207536_production, 76_LVBus0207537_production, 76_LVBus0207539_consumption, 76_LVBus0207539_production, 76_LVBus0207540_consumption, 76_LVBus0207540_production, 76_LVBus0207541_consumption, 76_LVBus0207541_production, 76_LVBus0207542_production, 76_LVBus0207543_consumption, 76_LVBus0207543_production, 76_LVBus0207545_production, 76_LVBus0207546_production, 76_LVBus0207547_production, 76_LVBus0207548_production, 76_LVBus0207549_consumption, 76_LVBus0207549_production, 76_LVBus0207550_production, 76_LVBus0207551_production, 76_LVBus0207552_production, 76_LVBus0207553_production, 76_LVBus0207554_production, 76_LVBus0207556_consumption, 76_LVBus0207556_production, 76_LVBus0207558_production, 76_LVBus0207559_production, 76_LVBus0207560_production, 76_LVBus0207561_production, 76_LVBus0207562_production, 76_LVBus0207564_consumption, 76_LVBus0207564_production, 76_LVBus0207565_production, 76_LVBus0207567_production, 76_LVBus0207568_consumption, 76_LVBus0207568_production, 76_LVBus0207569_consumption, 76_LVBus0207569_production, 76_LVBus0207570_production, 76_LVBus0207572_consumption, 76_LVBus0207572_production, 76_LVBus0207573_consumption, 76_LVBus0207573_production, 76_LVBus0207574_consumption, 76_LVBus0207574_production, 76_LVBus0207575_production, 76_LVBus0207576_consumption, 76_LVBus0207576_production, 76_LVBus0207577_consumption, 76_LVBus0207577_production, 76_LVBus0207578_production, 76_LVBus0207579_production, 76_LVBus0207582_production, 76_LVBus0207583_production, 76_LVBus0207584_consumption, 76_LVBus0207584_production, 76_LVBus0207585_production, 76_LVBus0207589_production, 76_LVBus0207590_consumption, 76_LVBus0207590_production, 76_LVBus0207591_consumption, 76_LVBus0207591_production, 76_LVBus0207592_production, 76_LVBus0207593_consumption, 76_LVBus0207593_production, 76_LVBus0207594_production, 76_LVBus0207596_production, 76_LVBus0207598_production, 76_LVBus0207599_production, 76_LVBus0207600_production, 76_LVBus0207601_production, 76_LVBus0207602_production, 76_LVBus0207603_production, 76_LVBus0207604_production, 76_LVBus0207605_production, 76_LVBus0207607_production, 76_LVBus0207609_production, 76_LVBus0207611_consumption, 76_LVBus0207611_production, 76_LVBus0207612_production, 76_LVBus0207613_consumption, 76_LVBus0207613_production, 76_LVBus0207614_consumption, 76_LVBus0207614_production, 76_LVBus0207615_production, 76_LVBus0207616_production, 76_LVBus0207618_consumption, 76_LVBus0207618_production, 76_LVBus0207620_consumption, 76_LVBus0207620_production, 76_LVBus0207621_production, 76_LVBus0207623_consumption, 76_LVBus0207623_production, 76_LVBus0207624_production, 76_LVBus0207625_production, 76_LVBus0207626_production, 76_LVBus0207627_production, 76_LVBus0207628_production, 76_LVBus0207630_consumption, 76_LVBus0207630_production, 76_LVBus0207633_consumption, 76_LVBus0207633_production, 76_LVBus0207634_production, 76_LVBus0207635_production, 76_LVBus0207636_production, 76_LVBus0207637_production, 76_LVBus0207638_production, 76_LVBus0207639_production, 76_LVBus0207640_production, 76_LVBus0207641_production, 76_LVBus0207642_production, 76_LVBus0207643_production, 76_LVBus0207644_production, 76_LVBus0207645_production, 76_LVBus0207646_production, 76_LVBus0207647_production, 76_LVBus0207648_production, 76_LVBus0207649_consumption, 76_LVBus0207649_production, 76_LVBus0207650_consumption, 76_LVBus0207650_production, 76_LVBus0207651_production, 76_LVBus0207652_consumption, 76_LVBus0207652_production, 76_LVBus0207653_production, 76_LVBus0207654_production, 76_LVBus0207655_production, 76_LVBus0207656_production, 76_LVBus0207657_production, 76_LVBus0207658_consumption, 76_LVBus0207658_production, 76_LVBus0207659_consumption, 76_LVBus0207659_production, 76_LVBus0207660_consumption, 76_LVBus0207660_production, 76_LVBus0207661_production, 76_LVBus0207662_production, 76_LVBus0207663_production, 76_LVBus0207664_production, 76_LVBus0207665_production, 76_LVBus0207666_production, 76_LVBus0207668_production, 76_LVBus0207669_consumption, 76_LVBus0207669_production, 76_LVBus0207670_consumption, 76_LVBus0207670_production, 76_LVBus0207671_production, 76_LVBus0207673_production, 76_LVBus0207674_production, 76_LVBus0207675_production, 76_LVBus0207676_production, 76_LVBus0207677_production, 76_LVBus0207678_production, 76_LVBus0207679_production, 76_LVBus0207681_consumption, 76_LVBus0207681_production, 76_LVBus0207682_production, 76_LVBus0207684_production, 76_LVBus0207685_consumption, 76_LVBus0207685_production, 76_LVBus0207686_consumption, 76_LVBus0207686_production, 76_LVBus0207688_production, 76_LVBus0207690_production, 76_LVBus0207691_production, 76_LVBus0207692_consumption, 76_LVBus0207692_production, 76_LVBus0207693_production, 76_LVBus0207694_production, 76_LVBus0207695_production, 76_LVBus0207696_production, 76_LVBus0207698_production, 76_LVBus0207700_production, 76_LVBus0207701_consumption, 76_LVBus0207701_production, 76_LVBus0207702_production, 76_LVBus0207703_production, 76_LVBus0207707_production, 76_LVBus0207708_consumption, 76_LVBus0207708_production, 76_LVBus0207709_production, 76_LVBus0207710_production, 76_LVBus0207711_production, 76_LVBus0207712_production, 76_LVBus0207713_production, 76_LVBus0207714_production, 76_LVBus0207715_production, 76_LVBus0207716_production, 76_LVBus0207717_production, 76_LVBus0207718_production, 76_LVBus0207720_production, 76_LVBus0207721_production, 76_LVBus0207722_production, 76_LVBus0207723_production, 76_LVBus0207724_production, 76_LVBus0207725_production, 76_LVBus0207726_production, 76_LVBus0207728_production, 76_LVBus0207729_production, 76_LVBus0207730_production, 76_LVBus0207731_production, 76_LVBus0207732_production, 76_LVBus0207733_production, 76_LVBus0207734_production, 76_LVBus0207735_consumption, 76_LVBus0207735_production, 76_LVBus0207736_production, 76_LVBus0207739_production, 76_LVBus0207741_consumption, 76_LVBus0207741_production, 76_LVBus0207743_production, 76_LVBus0207744_production, 76_LVBus0207745_production, 76_LVBus0207746_production, 76_LVBus0207747_production, 76_LVBus0207748_production, 76_LVBus0207749_production, 76_LVBus0207750_production, 76_LVBus0207751_production, 76_LVBus0207752_production, 76_LVBus0207753_production, 76_LVBus0207754_consumption, 76_LVBus0207754_production, 76_LVBus0207755_production, 76_LVBus0207756_production, 76_LVBus0207757_production, 76_LVBus0207758_production, 76_LVBus0207759_production, 76_LVBus0207760_production, 76_LVBus0207761_consumption, 76_LVBus0207761_production, 76_LVBus0207762_production, 76_LVBus0207763_production, 76_LVBus0207767_consumption, 76_LVBus0207767_production, 76_LVBus0207769_consumption, 76_LVBus0207769_production, 76_LVBus0207770_consumption, 76_LVBus0207770_production, 76_LVBus0207771_production, 76_LVBus0207773_consumption, 76_LVBus0207773_production, 76_LVBus0207774_production, 76_LVBus0207775_production, 76_LVBus0207777_consumption, 76_LVBus0207777_production, 76_LVBus0207778_production, 76_LVBus0207779_production, 76_LVBus0207780_production, 76_LVBus0207784_consumption, 76_LVBus0207784_production, 76_LVBus0207785_production, 76_LVBus0207786_production, 76_LVBus0207787_production, 76_LVBus0207788_production, 76_LVBus0207789_consumption, 76_LVBus0207789_production, 76_LVBus0207790_production, 76_LVBus0207792_production, 76_LVBus0207794_consumption, 76_LVBus0207794_production, 76_LVBus0207795_production, 76_LVBus0207796_production, 76_LVBus0207797_production, 76_LVBus0207798_production, 76_LVBus0207799_production, 76_LVBus0207800_production, 76_LVBus0207801_production, 76_LVBus0207802_production, 76_LVBus0207804_production, 76_LVBus0207805_production, 76_LVBus0207806_consumption, 76_LVBus0207806_production, 76_LVBus0207807_production, 76_LVBus0207808_production, 76_LVBus0207810_consumption, 76_LVBus0207810_production, 76_LVBus0207811_production, 76_LVBus0207814_consumption, 76_LVBus0207814_production, 76_LVBus0207815_consumption, 76_LVBus0207815_production, 76_LVBus0207816_consumption, 76_LVBus0207816_production, 76_LVBus0207817_production, 76_LVBus0207818_production, 76_LVBus0207819_production, 76_LVBus0207820_production, 76_LVBus0207821_production, 76_LVBus0207822_production, 76_LVBus0207823_production, 76_LVBus0207824_consumption, 76_LVBus0207824_production, 76_LVBus0207826_consumption, 76_LVBus0207826_production, 76_LVBus0207827_production, 76_LVBus0207828_production, 76_LVBus0207829_consumption, 76_LVBus0207829_production, 76_LVBus0207830_production, 76_LVBus0207831_production, 76_LVBus0207832_production, 76_LVBus0207833_production, 76_LVBus0207834_production, 76_LVBus0207835_production, 76_LVBus0207837_consumption, 76_LVBus0207837_production, 76_LVBus0207838_production, 76_LVBus0207839_production, 76_LVBus0207840_production, 76_LVBus0207841_consumption, 76_LVBus0207841_production, 76_LVBus0207842_consumption, 76_LVBus0207842_production, 76_LVBus0207843_production, 76_LVBus0207844_production, 76_LVBus0207845_production, 76_LVBus0207846_production, 76_LVBus0207847_production, 76_LVBus0207848_production, 76_LVBus0207850_production, 76_LVBus0207851_consumption, 76_LVBus0207851_production, 76_LVBus0207852_consumption, 76_LVBus0207852_production, 76_LVBus0207853_consumption, 76_LVBus0207853_production, 76_LVBus0207854_consumption, 76_LVBus0207854_production, 76_LVBus0207855_consumption, 76_LVBus0207855_production, 76_LVBus0207861_consumption, 76_LVBus0207861_production, 76_LVBus0207862_consumption, 76_LVBus0207862_production, 76_LVBus0207863_production, 76_LVBus0207864_production, 76_LVBus0207865_consumption, 76_LVBus0207865_production, 76_LVBus0207866_production, 76_LVBus0207867_production, 76_LVBus0207868_production, 76_LVBus0207869_production, 76_LVBus0207871_production, 76_LVBus0207872_production, 76_LVBus0207873_production, 76_LVBus0207874_production, 76_LVBus0207875_production, 76_LVBus0207876_production, 76_LVBus0207877_consumption, 76_LVBus0207877_production, 76_LVBus0207878_production, 76_LVBus0207879_production, 76_LVBus0207880_production, 76_LVBus0207881_production, 76_LVBus0207883_production, 76_LVBus0207885_production, 76_LVBus0207886_production, 76_LVBus0207887_production, 76_LVBus0207888_production, 76_LVBus0207889_production, 76_LVBus0207890_production, 76_LVBus0207891_production, 76_LVBus0207892_production, 76_LVBus0207893_production, 76_LVBus0207894_production, 76_LVBus0207895_production, 76_LVBus0207896_consumption, 76_LVBus0207896_production, 76_LVBus0207897_consumption, 76_LVBus0207897_production, 76_LVBus0207898_consumption, 76_LVBus0207898_production, 76_LVBus0207899_consumption, 76_LVBus0207899_production, 76_LVBus0207900_consumption, 76_LVBus0207900_production, 76_LVBus0207901_consumption, 76_LVBus0207901_production, 76_LVBus0207902_production, 76_LVBus0207903_consumption, 76_LVBus0207903_production, 76_LVBus0207904_production, 76_LVBus0207908_consumption, 76_LVBus0207908_production, 76_LVBus0207909_production, 76_LVBus0207911_production, 76_LVBus0207912_production, 76_LVBus0207913_production, 76_LVBus0207914_production, 76_LVBus0207915_production, 76_LVBus0207916_production, 76_LVBus0207917_consumption, 76_LVBus0207917_production, 76_LVBus0207918_production, 76_LVBus0207919_consumption, 76_LVBus0207919_production, 76_LVBus0207921_consumption, 76_LVBus0207921_production, 76_LVBus0207923_production, 76_LVBus0207925_production, 76_LVBus0207926_production, 76_LVBus0207927_production, 76_LVBus0207928_production, 76_LVBus0207930_consumption, 76_LVBus0207930_production, 76_LVBus0207931_production, 76_LVBus0207932_production, 76_LVBus0207934_production, 76_LVBus0207935_consumption, 76_LVBus0207935_production, 76_LVBus0207936_production, 76_LVBus0207938_production, 76_LVBus0207939_consumption, 76_LVBus0207939_production, 76_LVBus0207940_production, 76_LVBus0207941_consumption, 76_LVBus0207941_production, 76_LVBus0207942_consumption, 76_LVBus0207942_production, 76_LVBus0207943_production, 76_LVBus0207944_production, 76_LVBus0207945_production, 76_LVBus0207946_production, 76_LVBus0207948_production, 76_LVBus0207949_production, 76_LVBus0207951_production, 76_LVBus0207952_production, 76_LVBus0207953_consumption, 76_LVBus0207953_production, 76_LVBus0207954_production, 76_LVBus0207955_production, 76_LVBus0207956_consumption, 76_LVBus0207956_production, 76_LVBus0207957_production, 76_LVBus0207958_consumption, 76_LVBus0207958_production, 76_LVBus0207960_consumption, 76_LVBus0207960_production, 76_LVBus0207961_production, 76_LVBus0207963_consumption, 76_LVBus0207963_production, 76_LVBus0207964_production, 76_LVBus0207965_consumption, 76_LVBus0207965_production, 76_LVBus0207967_consumption, 76_LVBus0207967_production, 76_LVBus0207968_consumption, 76_LVBus0207968_production, 76_LVBus0207969_production, 76_LVBus0207973_production, 76_LVBus0207974_production, 76_LVBus0207975_consumption, 76_LVBus0207975_production, 76_LVBus0207976_production, 76_LVBus0207978_production, 76_LVBus0207979_production, 76_LVBus0207980_production, 76_LVBus0207981_production, 76_LVBus0207982_production, 76_LVBus0207986_consumption, 76_LVBus0207986_production, 76_LVBus0207989_production, 76_LVBus0207991_consumption, 76_LVBus0207991_production, 76_LVBus0207992_consumption, 76_LVBus0207992_production, 76_LVBus0207993_production, 76_LVBus0207994_consumption, 76_LVBus0207994_production, 76_LVBus0207995_consumption, 76_LVBus0207995_production, 76_LVBus0207996_production, 76_LVBus0207997_consumption, 76_LVBus0207997_production, 76_LVBus0207998_consumption, 76_LVBus0207998_production, 76_LVBus0207999_consumption, 76_LVBus0207999_production, 76_LVBus0208000_production, 76_LVBus0208001_production, 76_LVBus0208005_production, 76_LVBus0208006_consumption, 76_LVBus0208006_production, 76_LVBus0208007_production, 76_LVBus0208008_consumption, 76_LVBus0208008_production, 76_LVBus0208009_production, 76_LVBus0208010_production, 76_LVBus0208011_production, 76_LVBus0208012_production, 76_LVBus0208013_consumption, 76_LVBus0208013_production, 76_LVBus0208014_production, 76_LVBus0208015_production, 76_LVBus0208016_consumption, 76_LVBus0208016_production, 76_LVBus0208017_consumption, 76_LVBus0208017_production, 76_LVBus0208018_production, 76_LVBus0208019_consumption, 76_LVBus0208019_production, 76_LVBus0208020_production, 76_LVBus0208021_production, 76_LVBus0208022_production, 76_LVBus0208026_production, 76_LVBus0208028_consumption, 76_LVBus0208028_production, 76_LVBus0208030_consumption, 76_LVBus0208030_production, 76_LVBus0208031_consumption, 76_LVBus0208031_production, 76_LVBus0208032_production, 76_LVBus0208033_consumption, 76_LVBus0208033_production, 76_LVBus0208035_consumption, 76_LVBus0208035_production, 76_LVBus0208037_consumption, 76_LVBus0208037_production, 76_LVBus0208038_production, 76_LVBus0208039_production, 76_LVBus0208040_production, 76_LVBus0208042_production, 76_LVBus0208043_production, 76_LVBus0208045_production, 76_LVBus0208046_consumption, 76_LVBus0208046_production, 76_LVBus0208047_production, 76_LVBus0208048_production, 76_LVBus0208049_production, 76_LVBus0208051_consumption, 76_LVBus0208051_production, 76_LVBus0208053_consumption, 76_LVBus0208053_production, 76_LVBus0208055_production, 76_LVBus0208056_consumption, 76_LVBus0208056_production, 76_LVBus0208058_consumption, 76_LVBus0208058_production, 76_LVBus0208059_production, 76_LVBus0208060_production, 76_LVBus0208061_production, 76_LVBus0208062_production, 76_LVBus0208063_consumption, 76_LVBus0208063_production, 76_LVBus0208064_production, 76_LVBus0208065_consumption, 76_LVBus0208065_production, 76_LVBus0208066_production, 76_LVBus0208067_production, 76_LVBus0208068_production, 76_LVBus0208069_production, 76_LVBus0208071_consumption, 76_LVBus0208071_production, 76_LVBus0208072_production, 76_LVBus0208073_production, 76_LVBus0208074_production, 76_LVBus0208075_production, 76_LVBus0208076_production, 76_LVBus0208077_consumption, 76_LVBus0208077_production, 76_LVBus0208078_consumption, 76_LVBus0208078_production, 76_LVBus0208079_consumption, 76_LVBus0208079_production, 76_LVBus0208080_production, 76_LVBus0208081_production, 76_LVBus0208082_production, 76_LVBus0208084_production, 76_LVBus0208085_production, 76_LVBus0208086_consumption, 76_LVBus0208086_production, 76_LVBus0208087_production, 76_LVBus0208088_production, 76_LVBus0208089_production, 76_LVBus0208090_production, 76_LVBus0208092_consumption, 76_LVBus0208092_production, 76_LVBus0208093_consumption, 76_LVBus0208093_production, 76_LVBus0208094_production, 76_LVBus0208095_consumption, 76_LVBus0208095_production, 76_LVBus0208096_production, 76_LVBus0208098_consumption, 76_LVBus0208098_production, 76_LVBus0208099_production, 76_LVBus0208100_production, 76_LVBus0208104_production, 76_LVBus0208105_consumption, 76_LVBus0208105_production, 76_LVBus0208106_production, 76_LVBus0208107_production, 76_LVBus0208109_production, 76_LVBus0208110_production, 76_LVBus0208111_consumption, 76_LVBus0208111_production, 76_LVBus0208113_production, 76_LVBus0208114_production, 76_LVBus0208115_production, 76_LVBus0208116_production, 76_LVBus0208117_production, 76_LVBus0208118_production, 76_LVBus0208119_consumption, 76_LVBus0208119_production, 76_LVBus0208120_production, 76_LVBus0208121_production, 76_LVBus0208122_production, 76_LVBus0208123_production, 76_LVBus0208124_production, 76_LVBus0208125_production, 76_LVBus0208126_production, 76_LVBus0208127_production, 76_LVBus0208129_production, 76_LVBus0208130_production, 76_LVBus0208131_consumption, 76_LVBus0208131_production, 76_LVBus0208132_production, 76_LVBus0208133_production, 76_LVBus0208135_consumption, 76_LVBus0208135_production, 76_LVBus0208136_consumption, 76_LVBus0208136_production, 76_LVBus0208137_consumption, 76_LVBus0208137_production, 76_LVBus0208138_consumption, 76_LVBus0208138_production, 76_LVBus0208139_consumption, 76_LVBus0208139_production, 76_LVBus0208140_consumption, 76_LVBus0208140_production, 76_LVBus0208141_production, 76_LVBus0208142_consumption, 76_LVBus0208142_production, 76_LVBus0208143_consumption, 76_LVBus0208143_production, 76_LVBus0208144_consumption, 76_LVBus0208144_production, 76_LVBus0208145_production, 76_LVBus0208146_consumption, 76_LVBus0208146_production, 76_LVBus0208147_production, 76_LVBus0208149_consumption, 76_LVBus0208149_production, 76_LVBus0208150_production, 76_LVBus0208151_consumption, 76_LVBus0208151_production, 76_LVBus0208152_production, 76_LVBus0208153_consumption, 76_LVBus0208153_production, 76_LVBus0208154_production, 76_LVBus0208155_consumption, 76_LVBus0208155_production, 76_LVBus0208156_production, 76_LVBus0208157_production, 76_LVBus0208158_production, 76_LVBus0208159_consumption, 76_LVBus0208159_production, 76_LVBus0208160_production, 76_LVBus0208161_production, 76_LVBus0208162_consumption, 76_LVBus0208162_production, 76_LVBus0208163_consumption, 76_LVBus0208163_production, 76_LVBus0208164_production, 76_LVBus0208165_production, 76_LVBus0208170_consumption, 76_LVBus0208170_production, 76_LVBus0208171_consumption, 76_LVBus0208171_production, 76_LVBus0208172_consumption, 76_LVBus0208172_production, 76_LVBus0208173_consumption, 76_LVBus0208173_production, 76_LVBus0208177_production, 76_LVBus0208179_consumption, 76_LVBus0208179_production, 76_LVBus0208180_consumption, 76_LVBus0208180_production, 76_LVBus0208181_production, 76_LVBus0208182_production, 76_LVBus0208183_production, 76_LVBus0208184_production, 76_LVBus0208185_production, 76_LVBus0208186_production, 76_LVBus0208187_production, 76_LVBus0208188_production, 76_LVBus0208190_production, 76_LVBus0208191_production, 76_LVBus0208192_production, 76_LVBus0208193_production, 76_LVBus0208194_production, 76_LVBus0208196_production, 76_LVBus0208197_production, 76_LVBus0208198_production, 76_LVBus0208199_production, 76_LVBus0208200_production, 76_LVBus0208201_production, 76_LVBus0208203_production, 76_LVBus0208204_production, 76_LVBus0208205_production, 76_LVBus0208206_production, 76_LVBus0208207_consumption, 76_LVBus0208207_production, 76_LVBus0208208_production, 76_LVBus0208209_production, 76_LVBus0208210_production, 76_LVBus0208211_production, 76_LVBus0208212_production, 76_LVBus0208213_production, 76_LVBus0208214_production, 76_LVBus0208215_production, 76_LVBus0208216_production, 76_LVBus0208217_production, 76_LVBus0208218_production, 76_LVBus0208219_production, 76_LVBus0208220_production, 76_LVBus0208221_production, 76_LVBus0208222_production, 76_LVBus0208223_production, 76_LVBus0208224_production, 76_LVBus0208228_production, 76_LVBus0208229_consumption, 76_LVBus0208229_production, 76_LVBus0208231_production, 76_LVBus0208232_production, 76_LVBus0208233_production, 76_LVBus0208234_production, 76_LVBus0208235_production, 76_LVBus0208236_production, 76_LVBus0208237_production, 76_LVBus0208238_production, 76_LVBus0208239_production, 76_LVBus0208240_production, 76_LVBus0208241_consumption, 76_LVBus0208241_production, 76_LVBus0208242_consumption, 76_LVBus0208242_production, 76_LVBus0208243_production, 76_LVBus0208244_production, 76_LVBus0208245_production, 76_LVBus0208246_production, 76_LVBus0208247_consumption, 76_LVBus0208247_production, 76_LVBus0208248_production, 76_LVBus0208249_production, 76_LVBus0208251_production, 76_LVBus0208252_production, 76_LVBus0208253_production, 76_LVBus0208254_production, 76_LVBus0208255_production, 76_LVBus0208256_production, 76_LVBus0208257_production, 76_LVBus0208258_consumption, 76_LVBus0208258_production, 76_LVBus0208259_production, 76_LVBus0208260_production, 76_LVBus0208261_production, 76_LVBus0208262_consumption, 76_LVBus0208262_production, 76_LVBus0208263_production, 76_LVBus0208265_production, 76_LVBus0208267_production, 76_LVBus0208268_consumption, 76_LVBus0208268_production, 76_LVBus0208269_production, 76_LVBus0208270_production, 76_LVBus0208271_production, 76_LVBus0208272_production, 76_LVBus0208273_production, 76_LVBus0208279_production, 76_LVBus0208280_production, 76_LVBus0208281_production, 76_LVBus0208283_production, 76_LVBus0208284_production, 76_LVBus0208285_production, 76_LVBus0208286_production, 76_LVBus0208287_consumption, 76_LVBus0208287_production, 76_LVBus0208288_production, 76_LVBus0208289_production, 76_LVBus0208290_production, 76_LVBus0208291_production, 76_LVBus0208292_production, 76_LVBus0208293_production, 76_LVBus0208294_production, 76_LVBus0208295_production, 76_LVBus0208296_production, 76_LVBus0208297_consumption, 76_LVBus0208297_production, 76_LVBus2048021_production, 76_LVBus2066010_consumption, 76_LVBus2066010_production, 76_LVBus2088328_production, 76_LVBus2088329_production, 76_LVBus2094394_consumption, 76_LVBus2094394_production, 76_LVBus2094826_production, 76_LVBus2104182_consumption, 76_LVBus2104182_production, 76_LVBus2108075_production, 76_LVBus2108076_consumption, 76_LVBus2108076_production, 76_LVBus2108077_production, 76_LVBus2108078_production, 76_LVBus2108079_production, 76_LVBus2108080_production, 76_LVBus2108081_production, 76_LVBus2108082_consumption, 76_LVBus2108082_production, 76_LVBus2108083_production, 76_LVBus2108084_production, 76_LVBus2108085_production, 76_LVBus2108086_production, 76_LVBus2108087_production, 76_LVBus2108088_production, 76_LVBus2108089_production, 76_LVBus2108090_production, 76_LVBus2153139_production, 76_LVBus2153140_production, 76_LVBus2153141_production, 76_LVBus2153142_production, 76_LVBus2153143_production, 76_LVBus2153144_consumption, 76_LVBus2153144_production, 76_LVBus2153145_production, 76_LVBus2153146_production, 76_LVBus2153147_production, 76_LVBus2153148_production, 76_LVBus2153149_production, 76_LVBus2153150_production, 76_LVBus2153151_production, 76_LVBus2153152_production, 76_LVBus2153153_consumption, 76_LVBus2153153_production, 76_LVBus2153154_consumption, 76_LVBus2153154_production, 76_LVBus2156667_production, 76_LVBus2162032_consumption, 76_LVBus2162032_production, 76_LVBus2162033_production, 76_LVBus2162034_production, 76_LVBus2162035_production, 76_LVBus2162036_consumption, 76_LVBus2162036_production, 76_MVLV008940_consumption, 76_MVLV008940_production, 76_MVLV086059_consumption, 76_MVLV086059_production, 76_MVLV103102_consumption, 76_MVLV103102_production, 76_MVLV117086_consumption, 76_MVLV117086_production, 76_MVLV127359_consumption, 76_MVLV127359_production, 76_MVLV145832_consumption, 76_MVLV145832_production.

