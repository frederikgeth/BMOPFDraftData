# BMOPF Network Summary: 28_MVFeeder0290

**Generated:** 2026-10-01 23:34:01  
**Findings:** 0 errors · 5 warnings · 518 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 61 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 896 |  |
| line | 834 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1408 | 2.07 MW, 621.0 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 61 |  |
| switch | 0 |  |
| transformer | 61 | Dyn11×61 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 137 | 136 | 12 | 0 |
| LV_236V | 236.0 V | 759 | 698 | 1396 | 0 |

**Transformer transitions:**

- `28_MVLV71097_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV73504_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55097_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24890_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV62365_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV14352_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV21705_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV73895_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76035_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40732_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV37764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22642_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22814_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49362_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV03602_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV33691_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV17854_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22837_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46227_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40704_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47948_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV16392_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV65090_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13569_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59632_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV39089_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24455_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76010_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV14467_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV35938_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85508_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22458_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85512_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV33534_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV60724_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV61324_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV83691_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV05502_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76001_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59378_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV18717_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22827_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV83715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22838_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV45914_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV21714_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47709_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV17793_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV74260_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85694_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84943_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV54793_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85509_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22601_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV03883_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV74248_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV08188_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85507_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV68545_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 271 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 896 | 1 | 895 | 0 | 0 | 0 |
| Tier LV_236V | 759 | 61 | 698 | 0 | 0 | 0 |
| Tier MV_11.8kV | 137 | 1 | 136 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 61; skipped invalid branches: 0.

Galvanic zones: 62; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_BOSCH | MV_11.8kV | 137 | 0 | 0 | 61 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3447 declared bus terminals; 3200 mapped line/closed-switch conductor edges; 247 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 11300.0 | 2.516 | 4224 |
| q_nom | 0.0 | 3390.0 | 2.516 | 4224 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.413 | 3000.0 | 1.923 | 834 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.406 | 61 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 891 of 1408 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384054_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383799_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384411_consumption' has phase imbalance of 212.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383963_consumption' has phase imbalance of 214.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus968024_consumption' has phase imbalance of 117.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383758_consumption' has phase imbalance of 238.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383797_consumption' has phase imbalance of 250.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384164_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus867496_consumption' has phase imbalance of 233.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384464_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus976506_consumption' has phase imbalance of 33.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384070_consumption' has phase imbalance of 285.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384558_consumption' has phase imbalance of 188.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384249_consumption' has phase imbalance of 113.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384394_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384523_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384358_consumption' has phase imbalance of 224.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus958807_consumption' has phase imbalance of 294.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383740_consumption' has phase imbalance of 156.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383953_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383783_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384176_consumption' has phase imbalance of 222.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383846_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384425_consumption' has phase imbalance of 164.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384045_consumption' has phase imbalance of 62.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus876280_consumption' has phase imbalance of 266.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus942218_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383802_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383752_consumption' has phase imbalance of 69.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384456_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383928_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875708_consumption' has phase imbalance of 105.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384424_consumption' has phase imbalance of 193.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384106_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946810_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383880_consumption' has phase imbalance of 155.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384429_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384170_consumption' has phase imbalance of 164.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383732_consumption' has phase imbalance of 216.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus859398_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus976504_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384333_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383875_consumption' has phase imbalance of 133.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383811_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384229_consumption' has phase imbalance of 98.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus936642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384293_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384451_consumption' has phase imbalance of 109.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383951_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus896599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus880509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384323_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus878610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384324_consumption' has phase imbalance of 180.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384341_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384482_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384393_consumption' has phase imbalance of 65.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384368_consumption' has phase imbalance of 126.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384384_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384357_consumption' has phase imbalance of 252.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384400_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384273_consumption' has phase imbalance of 76.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384328_consumption' has phase imbalance of 146.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383914_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus915597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384528_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus958809_consumption' has phase imbalance of 235.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384378_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383973_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383969_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus933884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384198_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383843_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383874_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384120_consumption' has phase imbalance of 127.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384334_consumption' has phase imbalance of 227.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384370_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383834_consumption' has phase imbalance of 94.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383935_consumption' has phase imbalance of 257.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384555_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus907924_consumption' has phase imbalance of 68.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384158_consumption' has phase imbalance of 113.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus858252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383731_consumption' has phase imbalance of 247.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383889_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384401_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383836_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383905_consumption' has phase imbalance of 100.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384379_consumption' has phase imbalance of 252.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus859399_consumption' has phase imbalance of 293.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384532_consumption' has phase imbalance of 231.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384392_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383885_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus972582_consumption' has phase imbalance of 271.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384214_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383966_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384330_consumption' has phase imbalance of 186.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383789_consumption' has phase imbalance of 233.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384497_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384506_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384108_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus973389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384105_consumption' has phase imbalance of 67.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384128_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus900517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus958810_consumption' has phase imbalance of 149.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384499_consumption' has phase imbalance of 291.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384382_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383824_consumption' has phase imbalance of 223.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384515_consumption' has phase imbalance of 118.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384553_consumption' has phase imbalance of 234.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383741_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383888_consumption' has phase imbalance of 233.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384174_consumption' has phase imbalance of 176.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384458_consumption' has phase imbalance of 231.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383815_consumption' has phase imbalance of 149.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384407_consumption' has phase imbalance of 224.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384203_consumption' has phase imbalance of 122.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384337_consumption' has phase imbalance of 215.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383941_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384539_consumption' has phase imbalance of 223.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384193_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus976505_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384009_consumption' has phase imbalance of 276.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384372_consumption' has phase imbalance of 207.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384338_consumption' has phase imbalance of 101.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384276_consumption' has phase imbalance of 57.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947231_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383821_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920892_consumption' has phase imbalance of 156.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383980_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383738_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383742_consumption' has phase imbalance of 237.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384402_consumption' has phase imbalance of 142.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384367_consumption' has phase imbalance of 102.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384410_consumption' has phase imbalance of 131.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383781_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882829_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882825_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384441_consumption' has phase imbalance of 182.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus888320_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384211_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383930_consumption' has phase imbalance of 261.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383805_consumption' has phase imbalance of 68.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383760_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383858_consumption' has phase imbalance of 229.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383945_consumption' has phase imbalance of 127.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384232_consumption' has phase imbalance of 229.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384369_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384449_consumption' has phase imbalance of 185.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384281_consumption' has phase imbalance of 213.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384461_consumption' has phase imbalance of 117.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383937_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383938_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384187_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384420_consumption' has phase imbalance of 221.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384221_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383972_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384387_consumption' has phase imbalance of 177.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384024_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384156_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384071_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384339_consumption' has phase imbalance of 146.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384542_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384017_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384074_consumption' has phase imbalance of 86.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383818_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384329_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384288_consumption' has phase imbalance of 95.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384046_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384138_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384480_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946811_consumption' has phase imbalance of 43.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920896_consumption' has phase imbalance of 274.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384388_consumption' has phase imbalance of 117.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus857312_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384444_consumption' has phase imbalance of 41.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus973391_consumption' has phase imbalance of 295.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383820_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383862_consumption' has phase imbalance of 244.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus968426_consumption' has phase imbalance of 247.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus933881_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383857_consumption' has phase imbalance of 97.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384467_consumption' has phase imbalance of 46.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384213_consumption' has phase imbalance of 264.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384062_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383934_consumption' has phase imbalance of 207.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384343_consumption' has phase imbalance of 140.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384533_consumption' has phase imbalance of 236.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384366_consumption' has phase imbalance of 186.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384362_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948191_consumption' has phase imbalance of 285.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384025_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383810_consumption' has phase imbalance of 100.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384545_consumption' has phase imbalance of 260.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948190_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383714_consumption' has phase imbalance of 61.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383775_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383881_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946807_consumption' has phase imbalance of 86.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384332_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383813_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383872_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383778_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384104_consumption' has phase imbalance of 233.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384231_consumption' has phase imbalance of 285.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384559_consumption' has phase imbalance of 256.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384207_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384173_consumption' has phase imbalance of 262.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384172_consumption' has phase imbalance of 64.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384269_consumption' has phase imbalance of 121.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384209_consumption' has phase imbalance of 261.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383808_consumption' has phase imbalance of 260.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383878_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383780_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383746_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383866_consumption' has phase imbalance of 119.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384513_consumption' has phase imbalance of 201.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384236_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383925_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383776_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384155_consumption' has phase imbalance of 209.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384008_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383940_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384013_consumption' has phase imbalance of 277.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384183_consumption' has phase imbalance of 82.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384344_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384204_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384524_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384208_consumption' has phase imbalance of 246.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920889_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384285_consumption' has phase imbalance of 95.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384537_consumption' has phase imbalance of 193.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384543_consumption' has phase imbalance of 94.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus976503_consumption' has phase imbalance of 220.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383873_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus866721_consumption' has phase imbalance of 297.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383965_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383852_consumption' has phase imbalance of 263.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947230_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus973108_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384126_consumption' has phase imbalance of 295.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384282_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384272_consumption' has phase imbalance of 158.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948193_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384234_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384154_consumption' has phase imbalance of 157.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383884_consumption' has phase imbalance of 244.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus973388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383835_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384058_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus958808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383956_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383825_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383968_consumption' has phase imbalance of 255.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus899963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383766_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384408_consumption' has phase imbalance of 143.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383944_consumption' has phase imbalance of 262.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384199_consumption' has phase imbalance of 182.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384210_consumption' has phase imbalance of 265.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383979_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384078_consumption' has phase imbalance of 252.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965357_consumption' has phase imbalance of 79.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384107_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383767_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384465_consumption' has phase imbalance of 123.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus899951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus958811_consumption' has phase imbalance of 252.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383716_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384500_consumption' has phase imbalance of 118.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383957_consumption' has phase imbalance of 296.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384186_consumption' has phase imbalance of 194.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384228_consumption' has phase imbalance of 237.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384021_consumption' has phase imbalance of 204.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384383_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384504_consumption' has phase imbalance of 259.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384470_consumption' has phase imbalance of 167.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383981_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920893_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383898_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384063_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384226_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383903_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384439_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383964_consumption' has phase imbalance of 171.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384215_consumption' has phase imbalance of 46.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384386_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383828_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384271_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384397_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383715_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384377_consumption' has phase imbalance of 118.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus973390_consumption' has phase imbalance of 26.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383729_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383927_consumption' has phase imbalance of 257.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384127_consumption' has phase imbalance of 223.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus920890_consumption' has phase imbalance of 255.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383954_consumption' has phase imbalance of 97.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus896164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882591_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus973109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384169_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus862125_consumption' has phase imbalance of 77.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383958_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384529_consumption' has phase imbalance of 230.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384525_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853387_consumption' has phase imbalance of 268.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384185_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384414_consumption' has phase imbalance of 268.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383728_consumption' has phase imbalance of 291.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus868948_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383879_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384342_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384416_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384469_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384540_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383886_consumption' has phase imbalance of 175.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384047_consumption' has phase imbalance of 185.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384527_consumption' has phase imbalance of 220.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383759_consumption' has phase imbalance of 209.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383774_consumption' has phase imbalance of 262.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383720_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383893_consumption' has phase imbalance of 74.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383904_consumption' has phase imbalance of 245.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384073_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383921_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus946495_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383844_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384012_consumption' has phase imbalance of 236.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383769_consumption' has phase imbalance of 270.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus383909_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384452_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384165_consumption' has phase imbalance of 105.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384363_consumption' has phase imbalance of 288.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus976502_consumption' has phase imbalance of 249.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384077_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus384053_consumption' has phase imbalance of 260.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1408 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus384488' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.07 MW |
| Total load Q | 621.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV71097_Transformer | 275.0 kVA | 18.8% |
| 28_MVLV73504_Transformer | 275.0 kVA | 15.5% |
| 28_MVLV55097_Transformer | 440.0 kVA | 17.7% |
| 28_MVLV24890_Transformer | 110.0 kVA | 3.4% |
| 28_MVLV62365_Transformer | 110.0 kVA | 17.7% |
| 28_MVLV14352_Transformer | 176.0 kVA | 19.2% |
| 28_MVLV21705_Transformer | 275.0 kVA | 10.9% |
| 28_MVLV73895_Transformer | 440.0 kVA | 18.1% |
| 28_MVLV76035_Transformer | 176.0 kVA | 15.2% |
| 28_MVLV40732_Transformer | 275.0 kVA | 13.8% |
| 28_MVLV37764_Transformer | 440.0 kVA | 14.7% |
| 28_MVLV22642_Transformer | 176.0 kVA | 19.2% |
| 28_MVLV22814_Transformer | 176.0 kVA | 9.1% |
| 28_MVLV49362_Transformer | 275.0 kVA | 17.2% |
| 28_MVLV03602_Transformer | 275.0 kVA | 21.6% |
| 28_MVLV33691_Transformer | 176.0 kVA | 0.0% |
| 28_MVLV17854_Transformer | 440.0 kVA | 14.6% |
| 28_MVLV22837_Transformer | 275.0 kVA | 13.0% |
| 28_MVLV46227_Transformer | 275.0 kVA | 11.7% |
| 28_MVLV40704_Transformer | 110.0 kVA | 0.0% |
| 28_MVLV47948_Transformer | 440.0 kVA | 18.4% |
| 28_MVLV16392_Transformer | 176.0 kVA | 22.9% |
| 28_MVLV65090_Transformer | 275.0 kVA | 16.5% |
| 28_MVLV13569_Transformer | 176.0 kVA | 8.4% |
| 28_MVLV59632_Transformer | 110.0 kVA | 0.0% |
| 28_MVLV39089_Transformer | 440.0 kVA | 13.3% |
| 28_MVLV24455_Transformer | 275.0 kVA | 18.6% |
| 28_MVLV76010_Transformer | 275.0 kVA | 14.5% |
| 28_MVLV14467_Transformer | 440.0 kVA | 10.1% |
| 28_MVLV35938_Transformer | 275.0 kVA | 18.7% |
| 28_MVLV85508_Transformer | 275.0 kVA | 16.8% |
| 28_MVLV22458_Transformer | 110.0 kVA | 4.0% |
| 28_MVLV85512_Transformer | 275.0 kVA | 9.7% |
| 28_MVLV33534_Transformer | 275.0 kVA | 9.6% |
| 28_MVLV60724_Transformer | 176.0 kVA | 10.0% |
| 28_MVLV61324_Transformer | 275.0 kVA | 17.4% |
| 28_MVLV83691_Transformer | 176.0 kVA | 9.6% |
| 28_MVLV05502_Transformer | 110.0 kVA | 5.6% |
| 28_MVLV76001_Transformer | 275.0 kVA | 11.6% |
| 28_MVLV84792_Transformer | 275.0 kVA | 16.4% |
| 28_MVLV59378_Transformer | 176.0 kVA | 6.4% |
| 28_MVLV18717_Transformer | 440.0 kVA | 21.9% |
| 28_MVLV22827_Transformer | 275.0 kVA | 9.6% |
| 28_MVLV83715_Transformer | 275.0 kVA | 11.8% |
| 28_MVLV84937_Transformer | 176.0 kVA | 9.1% |
| 28_MVLV22838_Transformer | 176.0 kVA | 5.8% |
| 28_MVLV45914_Transformer | 110.0 kVA | 9.8% |
| 28_MVLV21714_Transformer | 110.0 kVA | 9.6% |
| 28_MVLV47709_Transformer | 275.0 kVA | 11.1% |
| 28_MVLV17793_Transformer | 275.0 kVA | 18.0% |
| 28_MVLV74260_Transformer | 440.0 kVA | 13.1% |
| 28_MVLV85694_Transformer | 176.0 kVA | 15.1% |
| 28_MVLV84943_Transformer | 176.0 kVA | 4.2% |
| 28_MVLV54793_Transformer | 440.0 kVA | 15.6% |
| 28_MVLV85509_Transformer | 275.0 kVA | 18.1% |
| 28_MVLV22601_Transformer | 275.0 kVA | 12.7% |
| 28_MVLV03883_Transformer | 275.0 kVA | 11.3% |
| 28_MVLV74248_Transformer | 440.0 kVA | 11.8% |
| 28_MVLV08188_Transformer | 275.0 kVA | 19.6% |
| 28_MVLV85507_Transformer | 176.0 kVA | 6.1% |
| 28_MVLV68545_Transformer | 176.0 kVA | 12.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.07 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus384112' (LV, 0.24 kV) has an electrical reach of 18.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus384251' (LV, 0.24 kV) has an electrical reach of 9.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 896 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 896 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 61 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 137 |
| LV_236V | 4-wire | 759 / 759 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 759 |
| Neutral branches | 698 |
| Grounding points | 61 |
| Neutral sections | 61 |
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
| 11.78 kV | 137 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 62 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2070.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 759 / 137 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 892 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 892 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus383714_production, 28_LVBus383715_production, 28_LVBus383716_production, 28_LVBus383717_production, 28_LVBus383718_production, 28_LVBus383719_production, 28_LVBus383720_production, 28_LVBus383721_production, 28_LVBus383723_consumption, 28_LVBus383723_production, 28_LVBus383724_consumption, 28_LVBus383724_production, 28_LVBus383725_consumption, 28_LVBus383725_production, 28_LVBus383726_production, 28_LVBus383727_production, 28_LVBus383728_production, 28_LVBus383729_production, 28_LVBus383731_production, 28_LVBus383732_production, 28_LVBus383733_consumption, 28_LVBus383733_production, 28_LVBus383735_consumption, 28_LVBus383735_production, 28_LVBus383736_production, 28_LVBus383737_consumption, 28_LVBus383737_production, 28_LVBus383738_production, 28_LVBus383739_production, 28_LVBus383740_production, 28_LVBus383741_production, 28_LVBus383742_production, 28_LVBus383744_production, 28_LVBus383745_consumption, 28_LVBus383745_production, 28_LVBus383746_production, 28_LVBus383748_production, 28_LVBus383749_production, 28_LVBus383751_production, 28_LVBus383752_production, 28_LVBus383754_production, 28_LVBus383755_production, 28_LVBus383756_consumption, 28_LVBus383756_production, 28_LVBus383758_production, 28_LVBus383759_production, 28_LVBus383760_production, 28_LVBus383761_consumption, 28_LVBus383761_production, 28_LVBus383765_production, 28_LVBus383766_production, 28_LVBus383767_production, 28_LVBus383769_production, 28_LVBus383770_production, 28_LVBus383771_production, 28_LVBus383773_production, 28_LVBus383774_production, 28_LVBus383775_production, 28_LVBus383776_production, 28_LVBus383777_production, 28_LVBus383778_production, 28_LVBus383779_production, 28_LVBus383780_production, 28_LVBus383781_production, 28_LVBus383783_production, 28_LVBus383784_consumption, 28_LVBus383784_production, 28_LVBus383785_consumption, 28_LVBus383785_production, 28_LVBus383786_production, 28_LVBus383788_consumption, 28_LVBus383788_production, 28_LVBus383789_production, 28_LVBus383790_production, 28_LVBus383791_consumption, 28_LVBus383791_production, 28_LVBus383792_consumption, 28_LVBus383792_production, 28_LVBus383793_consumption, 28_LVBus383793_production, 28_LVBus383794_production, 28_LVBus383795_production, 28_LVBus383796_production, 28_LVBus383797_production, 28_LVBus383798_consumption, 28_LVBus383798_production, 28_LVBus383799_production, 28_LVBus383800_production, 28_LVBus383801_consumption, 28_LVBus383801_production, 28_LVBus383802_production, 28_LVBus383803_production, 28_LVBus383805_production, 28_LVBus383806_consumption, 28_LVBus383806_production, 28_LVBus383807_production, 28_LVBus383808_production, 28_LVBus383809_production, 28_LVBus383810_production, 28_LVBus383811_production, 28_LVBus383813_production, 28_LVBus383815_production, 28_LVBus383817_consumption, 28_LVBus383817_production, 28_LVBus383818_production, 28_LVBus383819_production, 28_LVBus383820_production, 28_LVBus383821_production, 28_LVBus383823_consumption, 28_LVBus383823_production, 28_LVBus383824_production, 28_LVBus383825_production, 28_LVBus383826_production, 28_LVBus383827_consumption, 28_LVBus383827_production, 28_LVBus383828_production, 28_LVBus383832_consumption, 28_LVBus383832_production, 28_LVBus383833_consumption, 28_LVBus383833_production, 28_LVBus383834_production, 28_LVBus383835_production, 28_LVBus383836_production, 28_LVBus383838_consumption, 28_LVBus383838_production, 28_LVBus383839_production, 28_LVBus383841_consumption, 28_LVBus383841_production, 28_LVBus383842_production, 28_LVBus383843_production, 28_LVBus383844_production, 28_LVBus383845_production, 28_LVBus383846_production, 28_LVBus383848_consumption, 28_LVBus383848_production, 28_LVBus383849_production, 28_LVBus383850_consumption, 28_LVBus383850_production, 28_LVBus383851_consumption, 28_LVBus383851_production, 28_LVBus383852_production, 28_LVBus383853_production, 28_LVBus383855_consumption, 28_LVBus383855_production, 28_LVBus383856_consumption, 28_LVBus383856_production, 28_LVBus383857_production, 28_LVBus383858_production, 28_LVBus383860_consumption, 28_LVBus383860_production, 28_LVBus383861_production, 28_LVBus383862_production, 28_LVBus383864_consumption, 28_LVBus383864_production, 28_LVBus383865_production, 28_LVBus383866_production, 28_LVBus383867_production, 28_LVBus383868_consumption, 28_LVBus383868_production, 28_LVBus383870_consumption, 28_LVBus383870_production, 28_LVBus383871_consumption, 28_LVBus383871_production, 28_LVBus383872_production, 28_LVBus383873_production, 28_LVBus383874_production, 28_LVBus383875_production, 28_LVBus383877_consumption, 28_LVBus383877_production, 28_LVBus383878_production, 28_LVBus383879_production, 28_LVBus383880_production, 28_LVBus383881_production, 28_LVBus383883_consumption, 28_LVBus383883_production, 28_LVBus383884_production, 28_LVBus383885_production, 28_LVBus383886_production, 28_LVBus383887_production, 28_LVBus383888_production, 28_LVBus383889_production, 28_LVBus383891_production, 28_LVBus383892_production, 28_LVBus383893_production, 28_LVBus383894_production, 28_LVBus383895_production, 28_LVBus383898_production, 28_LVBus383899_consumption, 28_LVBus383899_production, 28_LVBus383903_production, 28_LVBus383904_production, 28_LVBus383905_production, 28_LVBus383907_production, 28_LVBus383908_consumption, 28_LVBus383908_production, 28_LVBus383909_production, 28_LVBus383910_consumption, 28_LVBus383910_production, 28_LVBus383912_consumption, 28_LVBus383912_production, 28_LVBus383913_production, 28_LVBus383914_production, 28_LVBus383917_consumption, 28_LVBus383917_production, 28_LVBus383918_production, 28_LVBus383919_consumption, 28_LVBus383919_production, 28_LVBus383920_production, 28_LVBus383921_production, 28_LVBus383922_consumption, 28_LVBus383922_production, 28_LVBus383925_production, 28_LVBus383926_consumption, 28_LVBus383926_production, 28_LVBus383927_production, 28_LVBus383928_production, 28_LVBus383929_production, 28_LVBus383930_production, 28_LVBus383934_production, 28_LVBus383935_production, 28_LVBus383937_production, 28_LVBus383938_production, 28_LVBus383940_production, 28_LVBus383941_production, 28_LVBus383942_production, 28_LVBus383943_consumption, 28_LVBus383943_production, 28_LVBus383944_production, 28_LVBus383945_production, 28_LVBus383946_production, 28_LVBus383950_consumption, 28_LVBus383950_production, 28_LVBus383951_production, 28_LVBus383953_production, 28_LVBus383954_production, 28_LVBus383956_production, 28_LVBus383957_production, 28_LVBus383958_production, 28_LVBus383963_production, 28_LVBus383964_production, 28_LVBus383965_production, 28_LVBus383966_production, 28_LVBus383968_production, 28_LVBus383969_production, 28_LVBus383971_consumption, 28_LVBus383971_production, 28_LVBus383972_production, 28_LVBus383973_production, 28_LVBus383975_production, 28_LVBus383976_consumption, 28_LVBus383976_production, 28_LVBus383977_production, 28_LVBus383978_production, 28_LVBus383979_production, 28_LVBus383980_production, 28_LVBus383981_production, 28_LVBus384008_production, 28_LVBus384009_production, 28_LVBus384011_consumption, 28_LVBus384011_production, 28_LVBus384012_production, 28_LVBus384013_production, 28_LVBus384015_production, 28_LVBus384016_production, 28_LVBus384017_production, 28_LVBus384019_consumption, 28_LVBus384019_production, 28_LVBus384020_production, 28_LVBus384021_production, 28_LVBus384022_production, 28_LVBus384023_consumption, 28_LVBus384023_production, 28_LVBus384024_production, 28_LVBus384025_production, 28_LVBus384027_consumption, 28_LVBus384027_production, 28_LVBus384028_production, 28_LVBus384029_consumption, 28_LVBus384029_production, 28_LVBus384033_production, 28_LVBus384035_production, 28_LVBus384037_production, 28_LVBus384039_consumption, 28_LVBus384039_production, 28_LVBus384040_consumption, 28_LVBus384040_production, 28_LVBus384043_consumption, 28_LVBus384043_production, 28_LVBus384044_production, 28_LVBus384045_production, 28_LVBus384046_production, 28_LVBus384047_production, 28_LVBus384048_production, 28_LVBus384049_production, 28_LVBus384051_consumption, 28_LVBus384051_production, 28_LVBus384052_production, 28_LVBus384053_production, 28_LVBus384054_production, 28_LVBus384055_consumption, 28_LVBus384055_production, 28_LVBus384056_consumption, 28_LVBus384056_production, 28_LVBus384057_production, 28_LVBus384058_production, 28_LVBus384059_production, 28_LVBus384061_consumption, 28_LVBus384061_production, 28_LVBus384062_production, 28_LVBus384063_production, 28_LVBus384068_production, 28_LVBus384070_production, 28_LVBus384071_production, 28_LVBus384073_production, 28_LVBus384074_production, 28_LVBus384076_production, 28_LVBus384077_production, 28_LVBus384078_production, 28_LVBus384101_production, 28_LVBus384102_production, 28_LVBus384103_production, 28_LVBus384104_production, 28_LVBus384105_production, 28_LVBus384106_production, 28_LVBus384107_production, 28_LVBus384108_production, 28_LVBus384112_consumption, 28_LVBus384112_production, 28_LVBus384114_consumption, 28_LVBus384114_production, 28_LVBus384116_consumption, 28_LVBus384116_production, 28_LVBus384117_consumption, 28_LVBus384117_production, 28_LVBus384118_consumption, 28_LVBus384118_production, 28_LVBus384119_consumption, 28_LVBus384119_production, 28_LVBus384120_production, 28_LVBus384121_production, 28_LVBus384123_consumption, 28_LVBus384123_production, 28_LVBus384124_consumption, 28_LVBus384124_production, 28_LVBus384126_production, 28_LVBus384127_production, 28_LVBus384128_production, 28_LVBus384129_production, 28_LVBus384130_production, 28_LVBus384132_consumption, 28_LVBus384132_production, 28_LVBus384134_production, 28_LVBus384135_production, 28_LVBus384136_consumption, 28_LVBus384136_production, 28_LVBus384137_production, 28_LVBus384138_production, 28_LVBus384139_consumption, 28_LVBus384139_production, 28_LVBus384140_consumption, 28_LVBus384140_production, 28_LVBus384141_consumption, 28_LVBus384141_production, 28_LVBus384152_consumption, 28_LVBus384152_production, 28_LVBus384153_production, 28_LVBus384154_production, 28_LVBus384155_production, 28_LVBus384156_production, 28_LVBus384157_production, 28_LVBus384158_production, 28_LVBus384160_production, 28_LVBus384161_consumption, 28_LVBus384161_production, 28_LVBus384162_production, 28_LVBus384163_consumption, 28_LVBus384163_production, 28_LVBus384164_production, 28_LVBus384165_production, 28_LVBus384169_production, 28_LVBus384170_production, 28_LVBus384171_production, 28_LVBus384172_production, 28_LVBus384173_production, 28_LVBus384174_production, 28_LVBus384176_production, 28_LVBus384177_consumption, 28_LVBus384177_production, 28_LVBus384178_production, 28_LVBus384180_production, 28_LVBus384181_production, 28_LVBus384182_production, 28_LVBus384183_production, 28_LVBus384184_production, 28_LVBus384185_production, 28_LVBus384186_production, 28_LVBus384187_production, 28_LVBus384191_production, 28_LVBus384193_production, 28_LVBus384195_consumption, 28_LVBus384195_production, 28_LVBus384197_consumption, 28_LVBus384197_production, 28_LVBus384198_production, 28_LVBus384199_production, 28_LVBus384201_production, 28_LVBus384202_production, 28_LVBus384203_production, 28_LVBus384204_production, 28_LVBus384206_consumption, 28_LVBus384206_production, 28_LVBus384207_production, 28_LVBus384208_production, 28_LVBus384209_production, 28_LVBus384210_production, 28_LVBus384211_production, 28_LVBus384212_production, 28_LVBus384213_production, 28_LVBus384214_production, 28_LVBus384215_production, 28_LVBus384220_production, 28_LVBus384221_production, 28_LVBus384222_production, 28_LVBus384223_consumption, 28_LVBus384223_production, 28_LVBus384224_production, 28_LVBus384226_production, 28_LVBus384227_consumption, 28_LVBus384227_production, 28_LVBus384228_production, 28_LVBus384229_production, 28_LVBus384231_production, 28_LVBus384232_production, 28_LVBus384233_consumption, 28_LVBus384233_production, 28_LVBus384234_production, 28_LVBus384235_consumption, 28_LVBus384235_production, 28_LVBus384236_production, 28_LVBus384239_consumption, 28_LVBus384239_production, 28_LVBus384240_consumption, 28_LVBus384240_production, 28_LVBus384241_consumption, 28_LVBus384241_production, 28_LVBus384243_consumption, 28_LVBus384243_production, 28_LVBus384244_consumption, 28_LVBus384244_production, 28_LVBus384245_consumption, 28_LVBus384245_production, 28_LVBus384246_consumption, 28_LVBus384246_production, 28_LVBus384247_production, 28_LVBus384248_production, 28_LVBus384249_production, 28_LVBus384251_consumption, 28_LVBus384251_production, 28_LVBus384253_consumption, 28_LVBus384253_production, 28_LVBus384254_production, 28_LVBus384255_consumption, 28_LVBus384255_production, 28_LVBus384256_production, 28_LVBus384257_production, 28_LVBus384258_consumption, 28_LVBus384258_production, 28_LVBus384259_production, 28_LVBus384260_consumption, 28_LVBus384260_production, 28_LVBus384261_consumption, 28_LVBus384261_production, 28_LVBus384262_production, 28_LVBus384266_consumption, 28_LVBus384266_production, 28_LVBus384267_consumption, 28_LVBus384267_production, 28_LVBus384268_production, 28_LVBus384269_production, 28_LVBus384270_consumption, 28_LVBus384270_production, 28_LVBus384271_production, 28_LVBus384272_production, 28_LVBus384273_production, 28_LVBus384274_production, 28_LVBus384275_production, 28_LVBus384276_production, 28_LVBus384280_consumption, 28_LVBus384280_production, 28_LVBus384281_production, 28_LVBus384282_production, 28_LVBus384284_production, 28_LVBus384285_production, 28_LVBus384287_production, 28_LVBus384288_production, 28_LVBus384289_consumption, 28_LVBus384289_production, 28_LVBus384290_production, 28_LVBus384291_consumption, 28_LVBus384291_production, 28_LVBus384293_production, 28_LVBus384294_production, 28_LVBus384296_consumption, 28_LVBus384296_production, 28_LVBus384323_production, 28_LVBus384324_production, 28_LVBus384325_consumption, 28_LVBus384325_production, 28_LVBus384326_production, 28_LVBus384328_production, 28_LVBus384329_production, 28_LVBus384330_production, 28_LVBus384331_production, 28_LVBus384332_production, 28_LVBus384333_production, 28_LVBus384334_production, 28_LVBus384336_consumption, 28_LVBus384336_production, 28_LVBus384337_production, 28_LVBus384338_production, 28_LVBus384339_production, 28_LVBus384340_consumption, 28_LVBus384340_production, 28_LVBus384341_production, 28_LVBus384342_production, 28_LVBus384343_production, 28_LVBus384344_production, 28_LVBus384345_consumption, 28_LVBus384345_production, 28_LVBus384346_consumption, 28_LVBus384346_production, 28_LVBus384347_consumption, 28_LVBus384347_production, 28_LVBus384348_consumption, 28_LVBus384348_production, 28_LVBus384349_consumption, 28_LVBus384349_production, 28_LVBus384354_production, 28_LVBus384355_production, 28_LVBus384356_production, 28_LVBus384357_production, 28_LVBus384358_production, 28_LVBus384359_production, 28_LVBus384360_production, 28_LVBus384362_production, 28_LVBus384363_production, 28_LVBus384364_consumption, 28_LVBus384364_production, 28_LVBus384366_production, 28_LVBus384367_production, 28_LVBus384368_production, 28_LVBus384369_production, 28_LVBus384370_production, 28_LVBus384371_consumption, 28_LVBus384371_production, 28_LVBus384372_production, 28_LVBus384374_production, 28_LVBus384375_consumption, 28_LVBus384375_production, 28_LVBus384377_production, 28_LVBus384378_production, 28_LVBus384379_production, 28_LVBus384381_consumption, 28_LVBus384381_production, 28_LVBus384382_production, 28_LVBus384383_production, 28_LVBus384384_production, 28_LVBus384385_consumption, 28_LVBus384385_production, 28_LVBus384386_production, 28_LVBus384387_production, 28_LVBus384388_production, 28_LVBus384390_consumption, 28_LVBus384390_production, 28_LVBus384392_production, 28_LVBus384393_production, 28_LVBus384394_production, 28_LVBus384396_consumption, 28_LVBus384396_production, 28_LVBus384397_production, 28_LVBus384399_production, 28_LVBus384400_production, 28_LVBus384401_production, 28_LVBus384402_production, 28_LVBus384403_production, 28_LVBus384405_consumption, 28_LVBus384405_production, 28_LVBus384407_production, 28_LVBus384408_production, 28_LVBus384410_production, 28_LVBus384411_production, 28_LVBus384412_production, 28_LVBus384413_consumption, 28_LVBus384413_production, 28_LVBus384414_production, 28_LVBus384415_production, 28_LVBus384416_production, 28_LVBus384420_production, 28_LVBus384421_production, 28_LVBus384422_consumption, 28_LVBus384422_production, 28_LVBus384423_production, 28_LVBus384424_production, 28_LVBus384425_production, 28_LVBus384427_production, 28_LVBus384428_production, 28_LVBus384429_production, 28_LVBus384430_consumption, 28_LVBus384430_production, 28_LVBus384432_consumption, 28_LVBus384432_production, 28_LVBus384433_consumption, 28_LVBus384433_production, 28_LVBus384437_consumption, 28_LVBus384437_production, 28_LVBus384438_consumption, 28_LVBus384438_production, 28_LVBus384439_production, 28_LVBus384440_consumption, 28_LVBus384440_production, 28_LVBus384441_production, 28_LVBus384442_consumption, 28_LVBus384442_production, 28_LVBus384443_production, 28_LVBus384444_production, 28_LVBus384445_production, 28_LVBus384448_consumption, 28_LVBus384448_production, 28_LVBus384449_production, 28_LVBus384451_production, 28_LVBus384452_production, 28_LVBus384453_consumption, 28_LVBus384453_production, 28_LVBus384455_consumption, 28_LVBus384455_production, 28_LVBus384456_production, 28_LVBus384457_production, 28_LVBus384458_production, 28_LVBus384460_production, 28_LVBus384461_production, 28_LVBus384462_production, 28_LVBus384464_production, 28_LVBus384465_production, 28_LVBus384466_production, 28_LVBus384467_production, 28_LVBus384469_production, 28_LVBus384470_production, 28_LVBus384472_consumption, 28_LVBus384472_production, 28_LVBus384473_production, 28_LVBus384474_production, 28_LVBus384475_consumption, 28_LVBus384475_production, 28_LVBus384476_consumption, 28_LVBus384476_production, 28_LVBus384477_consumption, 28_LVBus384477_production, 28_LVBus384478_consumption, 28_LVBus384478_production, 28_LVBus384479_production, 28_LVBus384480_production, 28_LVBus384481_production, 28_LVBus384482_production, 28_LVBus384483_production, 28_LVBus384488_consumption, 28_LVBus384488_production, 28_LVBus384489_production, 28_LVBus384490_consumption, 28_LVBus384490_production, 28_LVBus384491_production, 28_LVBus384497_production, 28_LVBus384499_production, 28_LVBus384500_production, 28_LVBus384501_production, 28_LVBus384502_production, 28_LVBus384503_consumption, 28_LVBus384503_production, 28_LVBus384504_production, 28_LVBus384506_production, 28_LVBus384507_production, 28_LVBus384508_production, 28_LVBus384509_production, 28_LVBus384511_production, 28_LVBus384512_production, 28_LVBus384513_production, 28_LVBus384514_consumption, 28_LVBus384514_production, 28_LVBus384515_production, 28_LVBus384517_consumption, 28_LVBus384517_production, 28_LVBus384518_consumption, 28_LVBus384518_production, 28_LVBus384519_production, 28_LVBus384521_production, 28_LVBus384522_consumption, 28_LVBus384522_production, 28_LVBus384523_production, 28_LVBus384524_production, 28_LVBus384525_production, 28_LVBus384526_consumption, 28_LVBus384526_production, 28_LVBus384527_production, 28_LVBus384528_production, 28_LVBus384529_production, 28_LVBus384532_production, 28_LVBus384533_production, 28_LVBus384534_consumption, 28_LVBus384534_production, 28_LVBus384535_consumption, 28_LVBus384535_production, 28_LVBus384536_production, 28_LVBus384537_production, 28_LVBus384538_consumption, 28_LVBus384538_production, 28_LVBus384539_production, 28_LVBus384540_production, 28_LVBus384541_production, 28_LVBus384542_production, 28_LVBus384543_production, 28_LVBus384544_consumption, 28_LVBus384544_production, 28_LVBus384545_production, 28_LVBus384549_consumption, 28_LVBus384549_production, 28_LVBus384550_production, 28_LVBus384551_consumption, 28_LVBus384551_production, 28_LVBus384552_consumption, 28_LVBus384552_production, 28_LVBus384553_production, 28_LVBus384554_production, 28_LVBus384555_production, 28_LVBus384556_production, 28_LVBus384557_consumption, 28_LVBus384557_production, 28_LVBus384558_production, 28_LVBus384559_production, 28_LVBus384560_production, 28_LVBus384561_production, 28_LVBus853387_production, 28_LVBus853388_production, 28_LVBus857312_production, 28_LVBus858252_production, 28_LVBus859398_production, 28_LVBus859399_production, 28_LVBus862125_production, 28_LVBus862201_consumption, 28_LVBus862201_production, 28_LVBus866721_production, 28_LVBus867496_production, 28_LVBus868948_production, 28_LVBus875700_consumption, 28_LVBus875700_production, 28_LVBus875701_consumption, 28_LVBus875701_production, 28_LVBus875702_consumption, 28_LVBus875702_production, 28_LVBus875703_production, 28_LVBus875704_consumption, 28_LVBus875704_production, 28_LVBus875705_consumption, 28_LVBus875705_production, 28_LVBus875706_consumption, 28_LVBus875706_production, 28_LVBus875707_consumption, 28_LVBus875707_production, 28_LVBus875708_production, 28_LVBus875709_production, 28_LVBus875710_production, 28_LVBus875711_consumption, 28_LVBus875711_production, 28_LVBus876280_production, 28_LVBus878610_production, 28_LVBus880508_consumption, 28_LVBus880508_production, 28_LVBus880509_production, 28_LVBus882586_production, 28_LVBus882587_consumption, 28_LVBus882587_production, 28_LVBus882588_consumption, 28_LVBus882588_production, 28_LVBus882589_consumption, 28_LVBus882589_production, 28_LVBus882590_production, 28_LVBus882591_production, 28_LVBus882823_production, 28_LVBus882824_consumption, 28_LVBus882824_production, 28_LVBus882825_production, 28_LVBus882826_production, 28_LVBus882827_production, 28_LVBus882828_consumption, 28_LVBus882828_production, 28_LVBus882829_production, 28_LVBus886578_consumption, 28_LVBus886578_production, 28_LVBus888319_consumption, 28_LVBus888319_production, 28_LVBus888320_production, 28_LVBus896164_production, 28_LVBus896599_production, 28_LVBus897753_consumption, 28_LVBus897753_production, 28_LVBus897754_consumption, 28_LVBus897754_production, 28_LVBus897755_production, 28_LVBus899951_production, 28_LVBus899963_production, 28_LVBus900517_production, 28_LVBus901757_consumption, 28_LVBus901757_production, 28_LVBus907924_production, 28_LVBus909744_consumption, 28_LVBus909744_production, 28_LVBus912140_production, 28_LVBus915596_consumption, 28_LVBus915596_production, 28_LVBus915597_production, 28_LVBus920889_production, 28_LVBus920890_production, 28_LVBus920891_production, 28_LVBus920892_production, 28_LVBus920893_production, 28_LVBus920894_consumption, 28_LVBus920894_production, 28_LVBus920895_production, 28_LVBus920896_production, 28_LVBus920897_production, 28_LVBus933881_production, 28_LVBus933882_consumption, 28_LVBus933882_production, 28_LVBus933883_consumption, 28_LVBus933883_production, 28_LVBus933884_production, 28_LVBus936642_production, 28_LVBus942217_consumption, 28_LVBus942217_production, 28_LVBus942218_production, 28_LVBus946495_production, 28_LVBus946600_production, 28_LVBus946807_production, 28_LVBus946808_production, 28_LVBus946809_production, 28_LVBus946810_production, 28_LVBus946811_production, 28_LVBus946812_production, 28_LVBus947034_production, 28_LVBus947228_production, 28_LVBus947229_consumption, 28_LVBus947229_production, 28_LVBus947230_production, 28_LVBus947231_production, 28_LVBus948190_production, 28_LVBus948191_production, 28_LVBus948192_production, 28_LVBus948193_production, 28_LVBus958807_production, 28_LVBus958808_production, 28_LVBus958809_production, 28_LVBus958810_production, 28_LVBus958811_production, 28_LVBus960410_production, 28_LVBus965357_production, 28_LVBus965358_production, 28_LVBus968024_production, 28_LVBus968426_production, 28_LVBus972582_production, 28_LVBus973107_consumption, 28_LVBus973107_production, 28_LVBus973108_production, 28_LVBus973109_production, 28_LVBus973388_production, 28_LVBus973389_production, 28_LVBus973390_production, 28_LVBus973391_production, 28_LVBus976502_production, 28_LVBus976503_production, 28_LVBus976504_production, 28_LVBus976505_production, 28_LVBus976506_production, 28_MVLV03530_consumption, 28_MVLV03530_production, 28_MVLV21704_consumption, 28_MVLV21704_production, 28_MVLV61838_consumption, 28_MVLV61838_production, 28_MVLV66122_consumption, 28_MVLV66122_production, 28_MVLV74435_consumption, 28_MVLV74435_production, 28_MVLV81617_consumption, 28_MVLV81617_production.

## 9. Data Quality Summary

**Total findings:** 523 (0 errors, 5 warnings, 518 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  891 of 1408 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.07 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  892 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384054_consumption`  
  Load '28_LVBus384054_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383796_consumption`  
  Load '28_LVBus383796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383717_consumption`  
  Load '28_LVBus383717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383751_consumption`  
  Load '28_LVBus383751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384541_consumption`  
  Load '28_LVBus384541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383799_consumption`  
  Load '28_LVBus383799_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383839_consumption`  
  Load '28_LVBus383839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965358_consumption`  
  Load '28_LVBus965358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384411_consumption`  
  Load '28_LVBus384411_consumption' has phase imbalance of 212.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383754_consumption`  
  Load '28_LVBus383754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383963_consumption`  
  Load '28_LVBus383963_consumption' has phase imbalance of 214.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus968024_consumption`  
  Load '28_LVBus968024_consumption' has phase imbalance of 117.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383758_consumption`  
  Load '28_LVBus383758_consumption' has phase imbalance of 238.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383797_consumption`  
  Load '28_LVBus383797_consumption' has phase imbalance of 250.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384164_consumption`  
  Load '28_LVBus384164_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383771_consumption`  
  Load '28_LVBus383771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384037_consumption`  
  Load '28_LVBus384037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384556_consumption`  
  Load '28_LVBus384556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus867496_consumption`  
  Load '28_LVBus867496_consumption' has phase imbalance of 233.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384511_consumption`  
  Load '28_LVBus384511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384464_consumption`  
  Load '28_LVBus384464_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus976506_consumption`  
  Load '28_LVBus976506_consumption' has phase imbalance of 33.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384153_consumption`  
  Load '28_LVBus384153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384070_consumption`  
  Load '28_LVBus384070_consumption' has phase imbalance of 285.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384290_consumption`  
  Load '28_LVBus384290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384103_consumption`  
  Load '28_LVBus384103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384558_consumption`  
  Load '28_LVBus384558_consumption' has phase imbalance of 188.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384249_consumption`  
  Load '28_LVBus384249_consumption' has phase imbalance of 113.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384479_consumption`  
  Load '28_LVBus384479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384135_consumption`  
  Load '28_LVBus384135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384160_consumption`  
  Load '28_LVBus384160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384394_consumption`  
  Load '28_LVBus384394_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384523_consumption`  
  Load '28_LVBus384523_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384358_consumption`  
  Load '28_LVBus384358_consumption' has phase imbalance of 224.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus958807_consumption`  
  Load '28_LVBus958807_consumption' has phase imbalance of 294.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383740_consumption`  
  Load '28_LVBus383740_consumption' has phase imbalance of 156.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383953_consumption`  
  Load '28_LVBus383953_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383861_consumption`  
  Load '28_LVBus383861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383783_consumption`  
  Load '28_LVBus383783_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882823_consumption`  
  Load '28_LVBus882823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384176_consumption`  
  Load '28_LVBus384176_consumption' has phase imbalance of 222.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383846_consumption`  
  Load '28_LVBus383846_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384374_consumption`  
  Load '28_LVBus384374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384425_consumption`  
  Load '28_LVBus384425_consumption' has phase imbalance of 164.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384045_consumption`  
  Load '28_LVBus384045_consumption' has phase imbalance of 62.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus876280_consumption`  
  Load '28_LVBus876280_consumption' has phase imbalance of 266.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus942218_consumption`  
  Load '28_LVBus942218_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383802_consumption`  
  Load '28_LVBus383802_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383790_consumption`  
  Load '28_LVBus383790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383865_consumption`  
  Load '28_LVBus383865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383752_consumption`  
  Load '28_LVBus383752_consumption' has phase imbalance of 69.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384220_consumption`  
  Load '28_LVBus384220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948192_consumption`  
  Load '28_LVBus948192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384456_consumption`  
  Load '28_LVBus384456_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383928_consumption`  
  Load '28_LVBus383928_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875708_consumption`  
  Load '28_LVBus875708_consumption' has phase imbalance of 105.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384424_consumption`  
  Load '28_LVBus384424_consumption' has phase imbalance of 193.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383907_consumption`  
  Load '28_LVBus383907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384106_consumption`  
  Load '28_LVBus384106_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384428_consumption`  
  Load '28_LVBus384428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946810_consumption`  
  Load '28_LVBus946810_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383880_consumption`  
  Load '28_LVBus383880_consumption' has phase imbalance of 155.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384429_consumption`  
  Load '28_LVBus384429_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384170_consumption`  
  Load '28_LVBus384170_consumption' has phase imbalance of 164.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383732_consumption`  
  Load '28_LVBus383732_consumption' has phase imbalance of 216.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus859398_consumption`  
  Load '28_LVBus859398_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus976504_consumption`  
  Load '28_LVBus976504_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384333_consumption`  
  Load '28_LVBus384333_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383845_consumption`  
  Load '28_LVBus383845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383875_consumption`  
  Load '28_LVBus383875_consumption' has phase imbalance of 133.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383811_consumption`  
  Load '28_LVBus383811_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384229_consumption`  
  Load '28_LVBus384229_consumption' has phase imbalance of 98.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus936642_consumption`  
  Load '28_LVBus936642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384293_consumption`  
  Load '28_LVBus384293_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384451_consumption`  
  Load '28_LVBus384451_consumption' has phase imbalance of 109.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383951_consumption`  
  Load '28_LVBus383951_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383794_consumption`  
  Load '28_LVBus383794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus896599_consumption`  
  Load '28_LVBus896599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus880509_consumption`  
  Load '28_LVBus880509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384323_consumption`  
  Load '28_LVBus384323_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383739_consumption`  
  Load '28_LVBus383739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus878610_consumption`  
  Load '28_LVBus878610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384324_consumption`  
  Load '28_LVBus384324_consumption' has phase imbalance of 180.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384341_consumption`  
  Load '28_LVBus384341_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384482_consumption`  
  Load '28_LVBus384482_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384393_consumption`  
  Load '28_LVBus384393_consumption' has phase imbalance of 65.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384368_consumption`  
  Load '28_LVBus384368_consumption' has phase imbalance of 126.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947228_consumption`  
  Load '28_LVBus947228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383920_consumption`  
  Load '28_LVBus383920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384384_consumption`  
  Load '28_LVBus384384_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384357_consumption`  
  Load '28_LVBus384357_consumption' has phase imbalance of 252.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383826_consumption`  
  Load '28_LVBus383826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384400_consumption`  
  Load '28_LVBus384400_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384273_consumption`  
  Load '28_LVBus384273_consumption' has phase imbalance of 76.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384328_consumption`  
  Load '28_LVBus384328_consumption' has phase imbalance of 146.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383914_consumption`  
  Load '28_LVBus383914_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus915597_consumption`  
  Load '28_LVBus915597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384528_consumption`  
  Load '28_LVBus384528_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383726_consumption`  
  Load '28_LVBus383726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384052_consumption`  
  Load '28_LVBus384052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus958809_consumption`  
  Load '28_LVBus958809_consumption' has phase imbalance of 235.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384378_consumption`  
  Load '28_LVBus384378_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383973_consumption`  
  Load '28_LVBus383973_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383892_consumption`  
  Load '28_LVBus383892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383969_consumption`  
  Load '28_LVBus383969_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus933884_consumption`  
  Load '28_LVBus933884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383721_consumption`  
  Load '28_LVBus383721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384198_consumption`  
  Load '28_LVBus384198_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383718_consumption`  
  Load '28_LVBus383718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383843_consumption`  
  Load '28_LVBus383843_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383895_consumption`  
  Load '28_LVBus383895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383874_consumption`  
  Load '28_LVBus383874_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383765_consumption`  
  Load '28_LVBus383765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384120_consumption`  
  Load '28_LVBus384120_consumption' has phase imbalance of 127.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384334_consumption`  
  Load '28_LVBus384334_consumption' has phase imbalance of 227.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384370_consumption`  
  Load '28_LVBus384370_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383800_consumption`  
  Load '28_LVBus383800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383834_consumption`  
  Load '28_LVBus383834_consumption' has phase imbalance of 94.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383935_consumption`  
  Load '28_LVBus383935_consumption' has phase imbalance of 257.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384184_consumption`  
  Load '28_LVBus384184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384102_consumption`  
  Load '28_LVBus384102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384555_consumption`  
  Load '28_LVBus384555_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus907924_consumption`  
  Load '28_LVBus907924_consumption' has phase imbalance of 68.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383842_consumption`  
  Load '28_LVBus383842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384121_consumption`  
  Load '28_LVBus384121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384158_consumption`  
  Load '28_LVBus384158_consumption' has phase imbalance of 113.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882586_consumption`  
  Load '28_LVBus882586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920891_consumption`  
  Load '28_LVBus920891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus858252_consumption`  
  Load '28_LVBus858252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920895_consumption`  
  Load '28_LVBus920895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383731_consumption`  
  Load '28_LVBus383731_consumption' has phase imbalance of 247.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383889_consumption`  
  Load '28_LVBus383889_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384460_consumption`  
  Load '28_LVBus384460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384016_consumption`  
  Load '28_LVBus384016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384022_consumption`  
  Load '28_LVBus384022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384401_consumption`  
  Load '28_LVBus384401_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384028_consumption`  
  Load '28_LVBus384028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384507_consumption`  
  Load '28_LVBus384507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383836_consumption`  
  Load '28_LVBus383836_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383905_consumption`  
  Load '28_LVBus383905_consumption' has phase imbalance of 100.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384379_consumption`  
  Load '28_LVBus384379_consumption' has phase imbalance of 252.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus859399_consumption`  
  Load '28_LVBus859399_consumption' has phase imbalance of 293.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384532_consumption`  
  Load '28_LVBus384532_consumption' has phase imbalance of 231.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383795_consumption`  
  Load '28_LVBus383795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384392_consumption`  
  Load '28_LVBus384392_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383885_consumption`  
  Load '28_LVBus383885_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384035_consumption`  
  Load '28_LVBus384035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus972582_consumption`  
  Load '28_LVBus972582_consumption' has phase imbalance of 271.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384560_consumption`  
  Load '28_LVBus384560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384214_consumption`  
  Load '28_LVBus384214_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383966_consumption`  
  Load '28_LVBus383966_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384481_consumption`  
  Load '28_LVBus384481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384330_consumption`  
  Load '28_LVBus384330_consumption' has phase imbalance of 186.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383789_consumption`  
  Load '28_LVBus383789_consumption' has phase imbalance of 233.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875703_consumption`  
  Load '28_LVBus875703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384497_consumption`  
  Load '28_LVBus384497_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384506_consumption`  
  Load '28_LVBus384506_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384108_consumption`  
  Load '28_LVBus384108_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384473_consumption`  
  Load '28_LVBus384473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384354_consumption`  
  Load '28_LVBus384354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus973389_consumption`  
  Load '28_LVBus973389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384415_consumption`  
  Load '28_LVBus384415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384105_consumption`  
  Load '28_LVBus384105_consumption' has phase imbalance of 67.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384128_consumption`  
  Load '28_LVBus384128_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus900517_consumption`  
  Load '28_LVBus900517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383849_consumption`  
  Load '28_LVBus383849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus958810_consumption`  
  Load '28_LVBus958810_consumption' has phase imbalance of 149.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384499_consumption`  
  Load '28_LVBus384499_consumption' has phase imbalance of 291.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384382_consumption`  
  Load '28_LVBus384382_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383824_consumption`  
  Load '28_LVBus383824_consumption' has phase imbalance of 223.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384515_consumption`  
  Load '28_LVBus384515_consumption' has phase imbalance of 118.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383786_consumption`  
  Load '28_LVBus383786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384201_consumption`  
  Load '28_LVBus384201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384553_consumption`  
  Load '28_LVBus384553_consumption' has phase imbalance of 234.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383741_consumption`  
  Load '28_LVBus383741_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383888_consumption`  
  Load '28_LVBus383888_consumption' has phase imbalance of 233.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384174_consumption`  
  Load '28_LVBus384174_consumption' has phase imbalance of 176.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384212_consumption`  
  Load '28_LVBus384212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384049_consumption`  
  Load '28_LVBus384049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384521_consumption`  
  Load '28_LVBus384521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384458_consumption`  
  Load '28_LVBus384458_consumption' has phase imbalance of 231.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384129_consumption`  
  Load '28_LVBus384129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383815_consumption`  
  Load '28_LVBus383815_consumption' has phase imbalance of 149.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384407_consumption`  
  Load '28_LVBus384407_consumption' has phase imbalance of 224.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383913_consumption`  
  Load '28_LVBus383913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384274_consumption`  
  Load '28_LVBus384274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384203_consumption`  
  Load '28_LVBus384203_consumption' has phase imbalance of 122.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383887_consumption`  
  Load '28_LVBus383887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384337_consumption`  
  Load '28_LVBus384337_consumption' has phase imbalance of 215.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383941_consumption`  
  Load '28_LVBus383941_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383978_consumption`  
  Load '28_LVBus383978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384539_consumption`  
  Load '28_LVBus384539_consumption' has phase imbalance of 223.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384193_consumption`  
  Load '28_LVBus384193_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus976505_consumption`  
  Load '28_LVBus976505_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384009_consumption`  
  Load '28_LVBus384009_consumption' has phase imbalance of 276.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384372_consumption`  
  Load '28_LVBus384372_consumption' has phase imbalance of 207.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384360_consumption`  
  Load '28_LVBus384360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384222_consumption`  
  Load '28_LVBus384222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384338_consumption`  
  Load '28_LVBus384338_consumption' has phase imbalance of 101.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384276_consumption`  
  Load '28_LVBus384276_consumption' has phase imbalance of 57.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947231_consumption`  
  Load '28_LVBus947231_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383821_consumption`  
  Load '28_LVBus383821_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920892_consumption`  
  Load '28_LVBus920892_consumption' has phase imbalance of 156.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383980_consumption`  
  Load '28_LVBus383980_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383738_consumption`  
  Load '28_LVBus383738_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383742_consumption`  
  Load '28_LVBus383742_consumption' has phase imbalance of 237.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384247_consumption`  
  Load '28_LVBus384247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384402_consumption`  
  Load '28_LVBus384402_consumption' has phase imbalance of 142.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384367_consumption`  
  Load '28_LVBus384367_consumption' has phase imbalance of 102.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384410_consumption`  
  Load '28_LVBus384410_consumption' has phase imbalance of 131.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383781_consumption`  
  Load '28_LVBus383781_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384057_consumption`  
  Load '28_LVBus384057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384268_consumption`  
  Load '28_LVBus384268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383748_consumption`  
  Load '28_LVBus383748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383719_consumption`  
  Load '28_LVBus383719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882829_consumption`  
  Load '28_LVBus882829_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882825_consumption`  
  Load '28_LVBus882825_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384441_consumption`  
  Load '28_LVBus384441_consumption' has phase imbalance of 182.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384561_consumption`  
  Load '28_LVBus384561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus888320_consumption`  
  Load '28_LVBus888320_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384211_consumption`  
  Load '28_LVBus384211_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384181_consumption`  
  Load '28_LVBus384181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383930_consumption`  
  Load '28_LVBus383930_consumption' has phase imbalance of 261.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383805_consumption`  
  Load '28_LVBus383805_consumption' has phase imbalance of 68.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383760_consumption`  
  Load '28_LVBus383760_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383891_consumption`  
  Load '28_LVBus383891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383858_consumption`  
  Load '28_LVBus383858_consumption' has phase imbalance of 229.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383945_consumption`  
  Load '28_LVBus383945_consumption' has phase imbalance of 127.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384232_consumption`  
  Load '28_LVBus384232_consumption' has phase imbalance of 229.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897755_consumption`  
  Load '28_LVBus897755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383770_consumption`  
  Load '28_LVBus383770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384369_consumption`  
  Load '28_LVBus384369_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384449_consumption`  
  Load '28_LVBus384449_consumption' has phase imbalance of 185.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384281_consumption`  
  Load '28_LVBus384281_consumption' has phase imbalance of 213.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384162_consumption`  
  Load '28_LVBus384162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384461_consumption`  
  Load '28_LVBus384461_consumption' has phase imbalance of 117.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383937_consumption`  
  Load '28_LVBus383937_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383938_consumption`  
  Load '28_LVBus383938_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384187_consumption`  
  Load '28_LVBus384187_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384420_consumption`  
  Load '28_LVBus384420_consumption' has phase imbalance of 221.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384554_consumption`  
  Load '28_LVBus384554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946812_consumption`  
  Load '28_LVBus946812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383918_consumption`  
  Load '28_LVBus383918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384033_consumption`  
  Load '28_LVBus384033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384221_consumption`  
  Load '28_LVBus384221_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383972_consumption`  
  Load '28_LVBus383972_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384224_consumption`  
  Load '28_LVBus384224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384068_consumption`  
  Load '28_LVBus384068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384387_consumption`  
  Load '28_LVBus384387_consumption' has phase imbalance of 177.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384024_consumption`  
  Load '28_LVBus384024_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384156_consumption`  
  Load '28_LVBus384156_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384071_consumption`  
  Load '28_LVBus384071_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384339_consumption`  
  Load '28_LVBus384339_consumption' has phase imbalance of 146.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384457_consumption`  
  Load '28_LVBus384457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384542_consumption`  
  Load '28_LVBus384542_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384017_consumption`  
  Load '28_LVBus384017_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384074_consumption`  
  Load '28_LVBus384074_consumption' has phase imbalance of 86.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383818_consumption`  
  Load '28_LVBus383818_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384329_consumption`  
  Load '28_LVBus384329_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383755_consumption`  
  Load '28_LVBus383755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384288_consumption`  
  Load '28_LVBus384288_consumption' has phase imbalance of 95.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875710_consumption`  
  Load '28_LVBus875710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384046_consumption`  
  Load '28_LVBus384046_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384138_consumption`  
  Load '28_LVBus384138_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384480_consumption`  
  Load '28_LVBus384480_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946811_consumption`  
  Load '28_LVBus946811_consumption' has phase imbalance of 43.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383779_consumption`  
  Load '28_LVBus383779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920896_consumption`  
  Load '28_LVBus920896_consumption' has phase imbalance of 274.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947034_consumption`  
  Load '28_LVBus947034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384536_consumption`  
  Load '28_LVBus384536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384388_consumption`  
  Load '28_LVBus384388_consumption' has phase imbalance of 117.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384331_consumption`  
  Load '28_LVBus384331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus857312_consumption`  
  Load '28_LVBus857312_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384444_consumption`  
  Load '28_LVBus384444_consumption' has phase imbalance of 41.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus973391_consumption`  
  Load '28_LVBus973391_consumption' has phase imbalance of 295.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383946_consumption`  
  Load '28_LVBus383946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384483_consumption`  
  Load '28_LVBus384483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383820_consumption`  
  Load '28_LVBus383820_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383862_consumption`  
  Load '28_LVBus383862_consumption' has phase imbalance of 244.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus968426_consumption`  
  Load '28_LVBus968426_consumption' has phase imbalance of 247.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus933881_consumption`  
  Load '28_LVBus933881_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383736_consumption`  
  Load '28_LVBus383736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383857_consumption`  
  Load '28_LVBus383857_consumption' has phase imbalance of 97.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384467_consumption`  
  Load '28_LVBus384467_consumption' has phase imbalance of 46.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384213_consumption`  
  Load '28_LVBus384213_consumption' has phase imbalance of 264.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384062_consumption`  
  Load '28_LVBus384062_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384355_consumption`  
  Load '28_LVBus384355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383934_consumption`  
  Load '28_LVBus383934_consumption' has phase imbalance of 207.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384343_consumption`  
  Load '28_LVBus384343_consumption' has phase imbalance of 140.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384421_consumption`  
  Load '28_LVBus384421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384533_consumption`  
  Load '28_LVBus384533_consumption' has phase imbalance of 236.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384366_consumption`  
  Load '28_LVBus384366_consumption' has phase imbalance of 186.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384362_consumption`  
  Load '28_LVBus384362_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912140_consumption`  
  Load '28_LVBus912140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948191_consumption`  
  Load '28_LVBus948191_consumption' has phase imbalance of 285.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383942_consumption`  
  Load '28_LVBus383942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384508_consumption`  
  Load '28_LVBus384508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882590_consumption`  
  Load '28_LVBus882590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384519_consumption`  
  Load '28_LVBus384519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384025_consumption`  
  Load '28_LVBus384025_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383773_consumption`  
  Load '28_LVBus383773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384423_consumption`  
  Load '28_LVBus384423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383810_consumption`  
  Load '28_LVBus383810_consumption' has phase imbalance of 100.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384545_consumption`  
  Load '28_LVBus384545_consumption' has phase imbalance of 260.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384462_consumption`  
  Load '28_LVBus384462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384044_consumption`  
  Load '28_LVBus384044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383777_consumption`  
  Load '28_LVBus383777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948190_consumption`  
  Load '28_LVBus948190_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384101_consumption`  
  Load '28_LVBus384101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383714_consumption`  
  Load '28_LVBus383714_consumption' has phase imbalance of 61.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383775_consumption`  
  Load '28_LVBus383775_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384202_consumption`  
  Load '28_LVBus384202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383881_consumption`  
  Load '28_LVBus383881_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383749_consumption`  
  Load '28_LVBus383749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383929_consumption`  
  Load '28_LVBus383929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946807_consumption`  
  Load '28_LVBus946807_consumption' has phase imbalance of 86.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384015_consumption`  
  Load '28_LVBus384015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384332_consumption`  
  Load '28_LVBus384332_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383813_consumption`  
  Load '28_LVBus383813_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383872_consumption`  
  Load '28_LVBus383872_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383778_consumption`  
  Load '28_LVBus383778_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384104_consumption`  
  Load '28_LVBus384104_consumption' has phase imbalance of 233.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384231_consumption`  
  Load '28_LVBus384231_consumption' has phase imbalance of 285.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384559_consumption`  
  Load '28_LVBus384559_consumption' has phase imbalance of 256.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384048_consumption`  
  Load '28_LVBus384048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384059_consumption`  
  Load '28_LVBus384059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384207_consumption`  
  Load '28_LVBus384207_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384173_consumption`  
  Load '28_LVBus384173_consumption' has phase imbalance of 262.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384172_consumption`  
  Load '28_LVBus384172_consumption' has phase imbalance of 64.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384269_consumption`  
  Load '28_LVBus384269_consumption' has phase imbalance of 121.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384209_consumption`  
  Load '28_LVBus384209_consumption' has phase imbalance of 261.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383808_consumption`  
  Load '28_LVBus383808_consumption' has phase imbalance of 260.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383878_consumption`  
  Load '28_LVBus383878_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384294_consumption`  
  Load '28_LVBus384294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383780_consumption`  
  Load '28_LVBus383780_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383746_consumption`  
  Load '28_LVBus383746_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383866_consumption`  
  Load '28_LVBus383866_consumption' has phase imbalance of 119.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384513_consumption`  
  Load '28_LVBus384513_consumption' has phase imbalance of 201.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384356_consumption`  
  Load '28_LVBus384356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384236_consumption`  
  Load '28_LVBus384236_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384020_consumption`  
  Load '28_LVBus384020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383925_consumption`  
  Load '28_LVBus383925_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383776_consumption`  
  Load '28_LVBus383776_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384155_consumption`  
  Load '28_LVBus384155_consumption' has phase imbalance of 209.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384134_consumption`  
  Load '28_LVBus384134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384008_consumption`  
  Load '28_LVBus384008_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383940_consumption`  
  Load '28_LVBus383940_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384359_consumption`  
  Load '28_LVBus384359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882827_consumption`  
  Load '28_LVBus882827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384427_consumption`  
  Load '28_LVBus384427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384013_consumption`  
  Load '28_LVBus384013_consumption' has phase imbalance of 277.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384182_consumption`  
  Load '28_LVBus384182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384183_consumption`  
  Load '28_LVBus384183_consumption' has phase imbalance of 82.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384344_consumption`  
  Load '28_LVBus384344_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384204_consumption`  
  Load '28_LVBus384204_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384524_consumption`  
  Load '28_LVBus384524_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384208_consumption`  
  Load '28_LVBus384208_consumption' has phase imbalance of 246.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384403_consumption`  
  Load '28_LVBus384403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920889_consumption`  
  Load '28_LVBus920889_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383853_consumption`  
  Load '28_LVBus383853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384285_consumption`  
  Load '28_LVBus384285_consumption' has phase imbalance of 95.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384537_consumption`  
  Load '28_LVBus384537_consumption' has phase imbalance of 193.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384543_consumption`  
  Load '28_LVBus384543_consumption' has phase imbalance of 94.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus976503_consumption`  
  Load '28_LVBus976503_consumption' has phase imbalance of 220.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383873_consumption`  
  Load '28_LVBus383873_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384180_consumption`  
  Load '28_LVBus384180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384262_consumption`  
  Load '28_LVBus384262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus866721_consumption`  
  Load '28_LVBus866721_consumption' has phase imbalance of 297.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383965_consumption`  
  Load '28_LVBus383965_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383852_consumption`  
  Load '28_LVBus383852_consumption' has phase imbalance of 263.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947230_consumption`  
  Load '28_LVBus947230_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus973108_consumption`  
  Load '28_LVBus973108_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384126_consumption`  
  Load '28_LVBus384126_consumption' has phase imbalance of 295.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384501_consumption`  
  Load '28_LVBus384501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384282_consumption`  
  Load '28_LVBus384282_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384272_consumption`  
  Load '28_LVBus384272_consumption' has phase imbalance of 158.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948193_consumption`  
  Load '28_LVBus948193_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384234_consumption`  
  Load '28_LVBus384234_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384502_consumption`  
  Load '28_LVBus384502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384154_consumption`  
  Load '28_LVBus384154_consumption' has phase imbalance of 157.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383884_consumption`  
  Load '28_LVBus383884_consumption' has phase imbalance of 244.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384130_consumption`  
  Load '28_LVBus384130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus973388_consumption`  
  Load '28_LVBus973388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383835_consumption`  
  Load '28_LVBus383835_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384058_consumption`  
  Load '28_LVBus384058_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383867_consumption`  
  Load '28_LVBus383867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus958808_consumption`  
  Load '28_LVBus958808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383956_consumption`  
  Load '28_LVBus383956_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383825_consumption`  
  Load '28_LVBus383825_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384550_consumption`  
  Load '28_LVBus384550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946600_consumption`  
  Load '28_LVBus946600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384466_consumption`  
  Load '28_LVBus384466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383968_consumption`  
  Load '28_LVBus383968_consumption' has phase imbalance of 255.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus899963_consumption`  
  Load '28_LVBus899963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384254_consumption`  
  Load '28_LVBus384254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383766_consumption`  
  Load '28_LVBus383766_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384408_consumption`  
  Load '28_LVBus384408_consumption' has phase imbalance of 143.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383944_consumption`  
  Load '28_LVBus383944_consumption' has phase imbalance of 262.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384199_consumption`  
  Load '28_LVBus384199_consumption' has phase imbalance of 182.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383727_consumption`  
  Load '28_LVBus383727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384210_consumption`  
  Load '28_LVBus384210_consumption' has phase imbalance of 265.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383979_consumption`  
  Load '28_LVBus383979_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384078_consumption`  
  Load '28_LVBus384078_consumption' has phase imbalance of 252.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965357_consumption`  
  Load '28_LVBus965357_consumption' has phase imbalance of 79.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384107_consumption`  
  Load '28_LVBus384107_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383767_consumption`  
  Load '28_LVBus383767_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384412_consumption`  
  Load '28_LVBus384412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384465_consumption`  
  Load '28_LVBus384465_consumption' has phase imbalance of 123.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus899951_consumption`  
  Load '28_LVBus899951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus958811_consumption`  
  Load '28_LVBus958811_consumption' has phase imbalance of 252.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383716_consumption`  
  Load '28_LVBus383716_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384500_consumption`  
  Load '28_LVBus384500_consumption' has phase imbalance of 118.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384326_consumption`  
  Load '28_LVBus384326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384191_consumption`  
  Load '28_LVBus384191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383957_consumption`  
  Load '28_LVBus383957_consumption' has phase imbalance of 296.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384186_consumption`  
  Load '28_LVBus384186_consumption' has phase imbalance of 194.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384228_consumption`  
  Load '28_LVBus384228_consumption' has phase imbalance of 237.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384021_consumption`  
  Load '28_LVBus384021_consumption' has phase imbalance of 204.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384383_consumption`  
  Load '28_LVBus384383_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384504_consumption`  
  Load '28_LVBus384504_consumption' has phase imbalance of 259.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384470_consumption`  
  Load '28_LVBus384470_consumption' has phase imbalance of 167.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383981_consumption`  
  Load '28_LVBus383981_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920893_consumption`  
  Load '28_LVBus920893_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383898_consumption`  
  Load '28_LVBus383898_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384063_consumption`  
  Load '28_LVBus384063_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384226_consumption`  
  Load '28_LVBus384226_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383807_consumption`  
  Load '28_LVBus383807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383903_consumption`  
  Load '28_LVBus383903_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384439_consumption`  
  Load '28_LVBus384439_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383964_consumption`  
  Load '28_LVBus383964_consumption' has phase imbalance of 171.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384215_consumption`  
  Load '28_LVBus384215_consumption' has phase imbalance of 46.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384386_consumption`  
  Load '28_LVBus384386_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384137_consumption`  
  Load '28_LVBus384137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383828_consumption`  
  Load '28_LVBus383828_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384271_consumption`  
  Load '28_LVBus384271_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384397_consumption`  
  Load '28_LVBus384397_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383715_consumption`  
  Load '28_LVBus383715_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383809_consumption`  
  Load '28_LVBus383809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384377_consumption`  
  Load '28_LVBus384377_consumption' has phase imbalance of 118.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384275_consumption`  
  Load '28_LVBus384275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882826_consumption`  
  Load '28_LVBus882826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus973390_consumption`  
  Load '28_LVBus973390_consumption' has phase imbalance of 26.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383729_consumption`  
  Load '28_LVBus383729_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875709_consumption`  
  Load '28_LVBus875709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383927_consumption`  
  Load '28_LVBus383927_consumption' has phase imbalance of 257.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920897_consumption`  
  Load '28_LVBus920897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384127_consumption`  
  Load '28_LVBus384127_consumption' has phase imbalance of 223.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384076_consumption`  
  Load '28_LVBus384076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus920890_consumption`  
  Load '28_LVBus920890_consumption' has phase imbalance of 255.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383954_consumption`  
  Load '28_LVBus383954_consumption' has phase imbalance of 97.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus896164_consumption`  
  Load '28_LVBus896164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882591_consumption`  
  Load '28_LVBus882591_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384256_consumption`  
  Load '28_LVBus384256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383819_consumption`  
  Load '28_LVBus383819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus973109_consumption`  
  Load '28_LVBus973109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384169_consumption`  
  Load '28_LVBus384169_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus862125_consumption`  
  Load '28_LVBus862125_consumption' has phase imbalance of 77.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383977_consumption`  
  Load '28_LVBus383977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384284_consumption`  
  Load '28_LVBus384284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383958_consumption`  
  Load '28_LVBus383958_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384178_consumption`  
  Load '28_LVBus384178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384529_consumption`  
  Load '28_LVBus384529_consumption' has phase imbalance of 230.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384525_consumption`  
  Load '28_LVBus384525_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853387_consumption`  
  Load '28_LVBus853387_consumption' has phase imbalance of 268.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384185_consumption`  
  Load '28_LVBus384185_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384414_consumption`  
  Load '28_LVBus384414_consumption' has phase imbalance of 268.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383728_consumption`  
  Load '28_LVBus383728_consumption' has phase imbalance of 291.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus868948_consumption`  
  Load '28_LVBus868948_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383879_consumption`  
  Load '28_LVBus383879_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384342_consumption`  
  Load '28_LVBus384342_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384416_consumption`  
  Load '28_LVBus384416_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384469_consumption`  
  Load '28_LVBus384469_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384540_consumption`  
  Load '28_LVBus384540_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384287_consumption`  
  Load '28_LVBus384287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383886_consumption`  
  Load '28_LVBus383886_consumption' has phase imbalance of 175.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384047_consumption`  
  Load '28_LVBus384047_consumption' has phase imbalance of 185.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384527_consumption`  
  Load '28_LVBus384527_consumption' has phase imbalance of 220.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383759_consumption`  
  Load '28_LVBus383759_consumption' has phase imbalance of 209.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383774_consumption`  
  Load '28_LVBus383774_consumption' has phase imbalance of 262.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383720_consumption`  
  Load '28_LVBus383720_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383893_consumption`  
  Load '28_LVBus383893_consumption' has phase imbalance of 74.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383744_consumption`  
  Load '28_LVBus383744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384445_consumption`  
  Load '28_LVBus384445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383904_consumption`  
  Load '28_LVBus383904_consumption' has phase imbalance of 245.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384073_consumption`  
  Load '28_LVBus384073_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383921_consumption`  
  Load '28_LVBus383921_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus946495_consumption`  
  Load '28_LVBus946495_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383803_consumption`  
  Load '28_LVBus383803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383844_consumption`  
  Load '28_LVBus383844_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384012_consumption`  
  Load '28_LVBus384012_consumption' has phase imbalance of 236.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383769_consumption`  
  Load '28_LVBus383769_consumption' has phase imbalance of 270.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus383909_consumption`  
  Load '28_LVBus383909_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384452_consumption`  
  Load '28_LVBus384452_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384165_consumption`  
  Load '28_LVBus384165_consumption' has phase imbalance of 105.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384363_consumption`  
  Load '28_LVBus384363_consumption' has phase imbalance of 288.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus976502_consumption`  
  Load '28_LVBus976502_consumption' has phase imbalance of 249.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384399_consumption`  
  Load '28_LVBus384399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384474_consumption`  
  Load '28_LVBus384474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384077_consumption`  
  Load '28_LVBus384077_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus384053_consumption`  
  Load '28_LVBus384053_consumption' has phase imbalance of 260.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1408 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus384488' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus384112' (LV, 0.24 kV) has an electrical reach of 18.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus384251' (LV, 0.24 kV) has an electrical reach of 9.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  896 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  388 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus383715_consumption, 28_LVBus383716_consumption, 28_LVBus383717_consumption, 28_LVBus383718_consumption, 28_LVBus383719_consumption, 28_LVBus383720_consumption, 28_LVBus383721_consumption, 28_LVBus383726_consumption, 28_LVBus383727_consumption, 28_LVBus383729_consumption, 28_LVBus383731_consumption, 28_LVBus383732_consumption, 28_LVBus383736_consumption, 28_LVBus383738_consumption, 28_LVBus383739_consumption, 28_LVBus383740_consumption, 28_LVBus383741_consumption, 28_LVBus383742_consumption, 28_LVBus383744_consumption, 28_LVBus383746_consumption, 28_LVBus383748_consumption, 28_LVBus383749_consumption, 28_LVBus383751_consumption, 28_LVBus383754_consumption, 28_LVBus383755_consumption, 28_LVBus383758_consumption, 28_LVBus383759_consumption, 28_LVBus383760_consumption, 28_LVBus383765_consumption, 28_LVBus383766_consumption, 28_LVBus383767_consumption, 28_LVBus383769_consumption, 28_LVBus383770_consumption, 28_LVBus383771_consumption, 28_LVBus383773_consumption, 28_LVBus383774_consumption, 28_LVBus383775_consumption, 28_LVBus383777_consumption, 28_LVBus383778_consumption, 28_LVBus383779_consumption, 28_LVBus383780_consumption, 28_LVBus383781_consumption, 28_LVBus383783_consumption, 28_LVBus383786_consumption, 28_LVBus383789_consumption, 28_LVBus383790_consumption, 28_LVBus383794_consumption, 28_LVBus383795_consumption, 28_LVBus383796_consumption, 28_LVBus383797_consumption, 28_LVBus383799_consumption, 28_LVBus383800_consumption, 28_LVBus383802_consumption, 28_LVBus383803_consumption, 28_LVBus383807_consumption, 28_LVBus383808_consumption, 28_LVBus383809_consumption, 28_LVBus383811_consumption, 28_LVBus383813_consumption, 28_LVBus383818_consumption, 28_LVBus383819_consumption, 28_LVBus383820_consumption, 28_LVBus383824_consumption, 28_LVBus383825_consumption, 28_LVBus383826_consumption, 28_LVBus383828_consumption, 28_LVBus383836_consumption, 28_LVBus383839_consumption, 28_LVBus383842_consumption, 28_LVBus383843_consumption, 28_LVBus383844_consumption, 28_LVBus383845_consumption, 28_LVBus383846_consumption, 28_LVBus383849_consumption, 28_LVBus383852_consumption, 28_LVBus383853_consumption, 28_LVBus383858_consumption, 28_LVBus383861_consumption, 28_LVBus383862_consumption, 28_LVBus383865_consumption, 28_LVBus383867_consumption, 28_LVBus383874_consumption, 28_LVBus383884_consumption, 28_LVBus383886_consumption, 28_LVBus383887_consumption, 28_LVBus383889_consumption, 28_LVBus383891_consumption, 28_LVBus383892_consumption, 28_LVBus383895_consumption, 28_LVBus383898_consumption, 28_LVBus383903_consumption, 28_LVBus383904_consumption, 28_LVBus383907_consumption, 28_LVBus383909_consumption, 28_LVBus383913_consumption, 28_LVBus383914_consumption, 28_LVBus383918_consumption, 28_LVBus383920_consumption, 28_LVBus383921_consumption, 28_LVBus383925_consumption, 28_LVBus383927_consumption, 28_LVBus383929_consumption, 28_LVBus383930_consumption, 28_LVBus383935_consumption, 28_LVBus383942_consumption, 28_LVBus383946_consumption, 28_LVBus383951_consumption, 28_LVBus383953_consumption, 28_LVBus383956_consumption, 28_LVBus383957_consumption, 28_LVBus383958_consumption, 28_LVBus383963_consumption, 28_LVBus383964_consumption, 28_LVBus383965_consumption, 28_LVBus383966_consumption, 28_LVBus383968_consumption, 28_LVBus383969_consumption, 28_LVBus383972_consumption, 28_LVBus383973_consumption, 28_LVBus383977_consumption, 28_LVBus383978_consumption, 28_LVBus383979_consumption, 28_LVBus383980_consumption, 28_LVBus383981_consumption, 28_LVBus384008_consumption, 28_LVBus384009_consumption, 28_LVBus384012_consumption, 28_LVBus384013_consumption, 28_LVBus384015_consumption, 28_LVBus384016_consumption, 28_LVBus384017_consumption, 28_LVBus384020_consumption, 28_LVBus384021_consumption, 28_LVBus384022_consumption, 28_LVBus384028_consumption, 28_LVBus384033_consumption, 28_LVBus384035_consumption, 28_LVBus384037_consumption, 28_LVBus384044_consumption, 28_LVBus384046_consumption, 28_LVBus384047_consumption, 28_LVBus384048_consumption, 28_LVBus384049_consumption, 28_LVBus384052_consumption, 28_LVBus384053_consumption, 28_LVBus384054_consumption, 28_LVBus384057_consumption, 28_LVBus384058_consumption, 28_LVBus384059_consumption, 28_LVBus384062_consumption, 28_LVBus384068_consumption, 28_LVBus384070_consumption, 28_LVBus384073_consumption, 28_LVBus384076_consumption, 28_LVBus384077_consumption, 28_LVBus384078_consumption, 28_LVBus384101_consumption, 28_LVBus384102_consumption, 28_LVBus384103_consumption, 28_LVBus384104_consumption, 28_LVBus384107_consumption, 28_LVBus384108_consumption, 28_LVBus384121_consumption, 28_LVBus384127_consumption, 28_LVBus384128_consumption, 28_LVBus384129_consumption, 28_LVBus384130_consumption, 28_LVBus384134_consumption, 28_LVBus384135_consumption, 28_LVBus384137_consumption, 28_LVBus384138_consumption, 28_LVBus384153_consumption, 28_LVBus384154_consumption, 28_LVBus384155_consumption, 28_LVBus384156_consumption, 28_LVBus384160_consumption, 28_LVBus384162_consumption, 28_LVBus384169_consumption, 28_LVBus384173_consumption, 28_LVBus384174_consumption, 28_LVBus384176_consumption, 28_LVBus384178_consumption, 28_LVBus384180_consumption, 28_LVBus384181_consumption, 28_LVBus384182_consumption, 28_LVBus384184_consumption, 28_LVBus384185_consumption, 28_LVBus384186_consumption, 28_LVBus384187_consumption, 28_LVBus384191_consumption, 28_LVBus384193_consumption, 28_LVBus384198_consumption, 28_LVBus384201_consumption, 28_LVBus384202_consumption, 28_LVBus384204_consumption, 28_LVBus384207_consumption, 28_LVBus384208_consumption, 28_LVBus384209_consumption, 28_LVBus384210_consumption, 28_LVBus384211_consumption, 28_LVBus384212_consumption, 28_LVBus384213_consumption, 28_LVBus384214_consumption, 28_LVBus384220_consumption, 28_LVBus384221_consumption, 28_LVBus384222_consumption, 28_LVBus384224_consumption, 28_LVBus384226_consumption, 28_LVBus384228_consumption, 28_LVBus384231_consumption, 28_LVBus384232_consumption, 28_LVBus384234_consumption, 28_LVBus384236_consumption, 28_LVBus384247_consumption, 28_LVBus384254_consumption, 28_LVBus384256_consumption, 28_LVBus384262_consumption, 28_LVBus384268_consumption, 28_LVBus384272_consumption, 28_LVBus384274_consumption, 28_LVBus384275_consumption, 28_LVBus384281_consumption, 28_LVBus384282_consumption, 28_LVBus384284_consumption, 28_LVBus384287_consumption, 28_LVBus384290_consumption, 28_LVBus384293_consumption, 28_LVBus384294_consumption, 28_LVBus384323_consumption, 28_LVBus384324_consumption, 28_LVBus384326_consumption, 28_LVBus384329_consumption, 28_LVBus384330_consumption, 28_LVBus384331_consumption, 28_LVBus384332_consumption, 28_LVBus384334_consumption, 28_LVBus384341_consumption, 28_LVBus384344_consumption, 28_LVBus384354_consumption, 28_LVBus384355_consumption, 28_LVBus384356_consumption, 28_LVBus384357_consumption, 28_LVBus384358_consumption, 28_LVBus384359_consumption, 28_LVBus384360_consumption, 28_LVBus384362_consumption, 28_LVBus384363_consumption, 28_LVBus384366_consumption, 28_LVBus384370_consumption, 28_LVBus384374_consumption, 28_LVBus384378_consumption, 28_LVBus384379_consumption, 28_LVBus384382_consumption, 28_LVBus384383_consumption, 28_LVBus384384_consumption, 28_LVBus384386_consumption, 28_LVBus384387_consumption, 28_LVBus384392_consumption, 28_LVBus384394_consumption, 28_LVBus384397_consumption, 28_LVBus384399_consumption, 28_LVBus384400_consumption, 28_LVBus384403_consumption, 28_LVBus384411_consumption, 28_LVBus384412_consumption, 28_LVBus384414_consumption, 28_LVBus384415_consumption, 28_LVBus384420_consumption, 28_LVBus384421_consumption, 28_LVBus384423_consumption, 28_LVBus384424_consumption, 28_LVBus384425_consumption, 28_LVBus384427_consumption, 28_LVBus384428_consumption, 28_LVBus384429_consumption, 28_LVBus384439_consumption, 28_LVBus384445_consumption, 28_LVBus384449_consumption, 28_LVBus384452_consumption, 28_LVBus384457_consumption, 28_LVBus384458_consumption, 28_LVBus384460_consumption, 28_LVBus384462_consumption, 28_LVBus384464_consumption, 28_LVBus384466_consumption, 28_LVBus384469_consumption, 28_LVBus384470_consumption, 28_LVBus384473_consumption, 28_LVBus384474_consumption, 28_LVBus384479_consumption, 28_LVBus384480_consumption, 28_LVBus384481_consumption, 28_LVBus384482_consumption, 28_LVBus384483_consumption, 28_LVBus384497_consumption, 28_LVBus384499_consumption, 28_LVBus384501_consumption, 28_LVBus384502_consumption, 28_LVBus384507_consumption, 28_LVBus384508_consumption, 28_LVBus384511_consumption, 28_LVBus384513_consumption, 28_LVBus384519_consumption, 28_LVBus384521_consumption, 28_LVBus384523_consumption, 28_LVBus384525_consumption, 28_LVBus384527_consumption, 28_LVBus384528_consumption, 28_LVBus384529_consumption, 28_LVBus384532_consumption, 28_LVBus384533_consumption, 28_LVBus384536_consumption, 28_LVBus384537_consumption, 28_LVBus384539_consumption, 28_LVBus384540_consumption, 28_LVBus384541_consumption, 28_LVBus384542_consumption, 28_LVBus384545_consumption, 28_LVBus384550_consumption, 28_LVBus384554_consumption, 28_LVBus384556_consumption, 28_LVBus384558_consumption, 28_LVBus384559_consumption, 28_LVBus384560_consumption, 28_LVBus384561_consumption, 28_LVBus853387_consumption, 28_LVBus857312_consumption, 28_LVBus858252_consumption, 28_LVBus859398_consumption, 28_LVBus859399_consumption, 28_LVBus868948_consumption, 28_LVBus875703_consumption, 28_LVBus875709_consumption, 28_LVBus875710_consumption, 28_LVBus876280_consumption, 28_LVBus878610_consumption, 28_LVBus880509_consumption, 28_LVBus882586_consumption, 28_LVBus882590_consumption, 28_LVBus882591_consumption, 28_LVBus882823_consumption, 28_LVBus882825_consumption, 28_LVBus882826_consumption, 28_LVBus882827_consumption, 28_LVBus882829_consumption, 28_LVBus888320_consumption, 28_LVBus896164_consumption, 28_LVBus896599_consumption, 28_LVBus897755_consumption, 28_LVBus899951_consumption, 28_LVBus899963_consumption, 28_LVBus900517_consumption, 28_LVBus912140_consumption, 28_LVBus915597_consumption, 28_LVBus920889_consumption, 28_LVBus920890_consumption, 28_LVBus920891_consumption, 28_LVBus920892_consumption, 28_LVBus920893_consumption, 28_LVBus920895_consumption, 28_LVBus920896_consumption, 28_LVBus920897_consumption, 28_LVBus933881_consumption, 28_LVBus933884_consumption, 28_LVBus936642_consumption, 28_LVBus946495_consumption, 28_LVBus946600_consumption, 28_LVBus946810_consumption, 28_LVBus946812_consumption, 28_LVBus947034_consumption, 28_LVBus947228_consumption, 28_LVBus947231_consumption, 28_LVBus948190_consumption, 28_LVBus948191_consumption, 28_LVBus948192_consumption, 28_LVBus948193_consumption, 28_LVBus958807_consumption, 28_LVBus958808_consumption, 28_LVBus958809_consumption, 28_LVBus965358_consumption, 28_LVBus972582_consumption, 28_LVBus973108_consumption, 28_LVBus973109_consumption, 28_LVBus973388_consumption, 28_LVBus973389_consumption, 28_LVBus976502_consumption, 28_LVBus976503_consumption, 28_LVBus976504_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  704 group(s) of loads (1408 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  16 group(s) of series lines (34 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  892 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus383714_production, 28_LVBus383715_production, 28_LVBus383716_production, 28_LVBus383717_production, 28_LVBus383718_production, 28_LVBus383719_production, 28_LVBus383720_production, 28_LVBus383721_production, 28_LVBus383723_consumption, 28_LVBus383723_production, 28_LVBus383724_consumption, 28_LVBus383724_production, 28_LVBus383725_consumption, 28_LVBus383725_production, 28_LVBus383726_production, 28_LVBus383727_production, 28_LVBus383728_production, 28_LVBus383729_production, 28_LVBus383731_production, 28_LVBus383732_production, 28_LVBus383733_consumption, 28_LVBus383733_production, 28_LVBus383735_consumption, 28_LVBus383735_production, 28_LVBus383736_production, 28_LVBus383737_consumption, 28_LVBus383737_production, 28_LVBus383738_production, 28_LVBus383739_production, 28_LVBus383740_production, 28_LVBus383741_production, 28_LVBus383742_production, 28_LVBus383744_production, 28_LVBus383745_consumption, 28_LVBus383745_production, 28_LVBus383746_production, 28_LVBus383748_production, 28_LVBus383749_production, 28_LVBus383751_production, 28_LVBus383752_production, 28_LVBus383754_production, 28_LVBus383755_production, 28_LVBus383756_consumption, 28_LVBus383756_production, 28_LVBus383758_production, 28_LVBus383759_production, 28_LVBus383760_production, 28_LVBus383761_consumption, 28_LVBus383761_production, 28_LVBus383765_production, 28_LVBus383766_production, 28_LVBus383767_production, 28_LVBus383769_production, 28_LVBus383770_production, 28_LVBus383771_production, 28_LVBus383773_production, 28_LVBus383774_production, 28_LVBus383775_production, 28_LVBus383776_production, 28_LVBus383777_production, 28_LVBus383778_production, 28_LVBus383779_production, 28_LVBus383780_production, 28_LVBus383781_production, 28_LVBus383783_production, 28_LVBus383784_consumption, 28_LVBus383784_production, 28_LVBus383785_consumption, 28_LVBus383785_production, 28_LVBus383786_production, 28_LVBus383788_consumption, 28_LVBus383788_production, 28_LVBus383789_production, 28_LVBus383790_production, 28_LVBus383791_consumption, 28_LVBus383791_production, 28_LVBus383792_consumption, 28_LVBus383792_production, 28_LVBus383793_consumption, 28_LVBus383793_production, 28_LVBus383794_production, 28_LVBus383795_production, 28_LVBus383796_production, 28_LVBus383797_production, 28_LVBus383798_consumption, 28_LVBus383798_production, 28_LVBus383799_production, 28_LVBus383800_production, 28_LVBus383801_consumption, 28_LVBus383801_production, 28_LVBus383802_production, 28_LVBus383803_production, 28_LVBus383805_production, 28_LVBus383806_consumption, 28_LVBus383806_production, 28_LVBus383807_production, 28_LVBus383808_production, 28_LVBus383809_production, 28_LVBus383810_production, 28_LVBus383811_production, 28_LVBus383813_production, 28_LVBus383815_production, 28_LVBus383817_consumption, 28_LVBus383817_production, 28_LVBus383818_production, 28_LVBus383819_production, 28_LVBus383820_production, 28_LVBus383821_production, 28_LVBus383823_consumption, 28_LVBus383823_production, 28_LVBus383824_production, 28_LVBus383825_production, 28_LVBus383826_production, 28_LVBus383827_consumption, 28_LVBus383827_production, 28_LVBus383828_production, 28_LVBus383832_consumption, 28_LVBus383832_production, 28_LVBus383833_consumption, 28_LVBus383833_production, 28_LVBus383834_production, 28_LVBus383835_production, 28_LVBus383836_production, 28_LVBus383838_consumption, 28_LVBus383838_production, 28_LVBus383839_production, 28_LVBus383841_consumption, 28_LVBus383841_production, 28_LVBus383842_production, 28_LVBus383843_production, 28_LVBus383844_production, 28_LVBus383845_production, 28_LVBus383846_production, 28_LVBus383848_consumption, 28_LVBus383848_production, 28_LVBus383849_production, 28_LVBus383850_consumption, 28_LVBus383850_production, 28_LVBus383851_consumption, 28_LVBus383851_production, 28_LVBus383852_production, 28_LVBus383853_production, 28_LVBus383855_consumption, 28_LVBus383855_production, 28_LVBus383856_consumption, 28_LVBus383856_production, 28_LVBus383857_production, 28_LVBus383858_production, 28_LVBus383860_consumption, 28_LVBus383860_production, 28_LVBus383861_production, 28_LVBus383862_production, 28_LVBus383864_consumption, 28_LVBus383864_production, 28_LVBus383865_production, 28_LVBus383866_production, 28_LVBus383867_production, 28_LVBus383868_consumption, 28_LVBus383868_production, 28_LVBus383870_consumption, 28_LVBus383870_production, 28_LVBus383871_consumption, 28_LVBus383871_production, 28_LVBus383872_production, 28_LVBus383873_production, 28_LVBus383874_production, 28_LVBus383875_production, 28_LVBus383877_consumption, 28_LVBus383877_production, 28_LVBus383878_production, 28_LVBus383879_production, 28_LVBus383880_production, 28_LVBus383881_production, 28_LVBus383883_consumption, 28_LVBus383883_production, 28_LVBus383884_production, 28_LVBus383885_production, 28_LVBus383886_production, 28_LVBus383887_production, 28_LVBus383888_production, 28_LVBus383889_production, 28_LVBus383891_production, 28_LVBus383892_production, 28_LVBus383893_production, 28_LVBus383894_production, 28_LVBus383895_production, 28_LVBus383898_production, 28_LVBus383899_consumption, 28_LVBus383899_production, 28_LVBus383903_production, 28_LVBus383904_production, 28_LVBus383905_production, 28_LVBus383907_production, 28_LVBus383908_consumption, 28_LVBus383908_production, 28_LVBus383909_production, 28_LVBus383910_consumption, 28_LVBus383910_production, 28_LVBus383912_consumption, 28_LVBus383912_production, 28_LVBus383913_production, 28_LVBus383914_production, 28_LVBus383917_consumption, 28_LVBus383917_production, 28_LVBus383918_production, 28_LVBus383919_consumption, 28_LVBus383919_production, 28_LVBus383920_production, 28_LVBus383921_production, 28_LVBus383922_consumption, 28_LVBus383922_production, 28_LVBus383925_production, 28_LVBus383926_consumption, 28_LVBus383926_production, 28_LVBus383927_production, 28_LVBus383928_production, 28_LVBus383929_production, 28_LVBus383930_production, 28_LVBus383934_production, 28_LVBus383935_production, 28_LVBus383937_production, 28_LVBus383938_production, 28_LVBus383940_production, 28_LVBus383941_production, 28_LVBus383942_production, 28_LVBus383943_consumption, 28_LVBus383943_production, 28_LVBus383944_production, 28_LVBus383945_production, 28_LVBus383946_production, 28_LVBus383950_consumption, 28_LVBus383950_production, 28_LVBus383951_production, 28_LVBus383953_production, 28_LVBus383954_production, 28_LVBus383956_production, 28_LVBus383957_production, 28_LVBus383958_production, 28_LVBus383963_production, 28_LVBus383964_production, 28_LVBus383965_production, 28_LVBus383966_production, 28_LVBus383968_production, 28_LVBus383969_production, 28_LVBus383971_consumption, 28_LVBus383971_production, 28_LVBus383972_production, 28_LVBus383973_production, 28_LVBus383975_production, 28_LVBus383976_consumption, 28_LVBus383976_production, 28_LVBus383977_production, 28_LVBus383978_production, 28_LVBus383979_production, 28_LVBus383980_production, 28_LVBus383981_production, 28_LVBus384008_production, 28_LVBus384009_production, 28_LVBus384011_consumption, 28_LVBus384011_production, 28_LVBus384012_production, 28_LVBus384013_production, 28_LVBus384015_production, 28_LVBus384016_production, 28_LVBus384017_production, 28_LVBus384019_consumption, 28_LVBus384019_production, 28_LVBus384020_production, 28_LVBus384021_production, 28_LVBus384022_production, 28_LVBus384023_consumption, 28_LVBus384023_production, 28_LVBus384024_production, 28_LVBus384025_production, 28_LVBus384027_consumption, 28_LVBus384027_production, 28_LVBus384028_production, 28_LVBus384029_consumption, 28_LVBus384029_production, 28_LVBus384033_production, 28_LVBus384035_production, 28_LVBus384037_production, 28_LVBus384039_consumption, 28_LVBus384039_production, 28_LVBus384040_consumption, 28_LVBus384040_production, 28_LVBus384043_consumption, 28_LVBus384043_production, 28_LVBus384044_production, 28_LVBus384045_production, 28_LVBus384046_production, 28_LVBus384047_production, 28_LVBus384048_production, 28_LVBus384049_production, 28_LVBus384051_consumption, 28_LVBus384051_production, 28_LVBus384052_production, 28_LVBus384053_production, 28_LVBus384054_production, 28_LVBus384055_consumption, 28_LVBus384055_production, 28_LVBus384056_consumption, 28_LVBus384056_production, 28_LVBus384057_production, 28_LVBus384058_production, 28_LVBus384059_production, 28_LVBus384061_consumption, 28_LVBus384061_production, 28_LVBus384062_production, 28_LVBus384063_production, 28_LVBus384068_production, 28_LVBus384070_production, 28_LVBus384071_production, 28_LVBus384073_production, 28_LVBus384074_production, 28_LVBus384076_production, 28_LVBus384077_production, 28_LVBus384078_production, 28_LVBus384101_production, 28_LVBus384102_production, 28_LVBus384103_production, 28_LVBus384104_production, 28_LVBus384105_production, 28_LVBus384106_production, 28_LVBus384107_production, 28_LVBus384108_production, 28_LVBus384112_consumption, 28_LVBus384112_production, 28_LVBus384114_consumption, 28_LVBus384114_production, 28_LVBus384116_consumption, 28_LVBus384116_production, 28_LVBus384117_consumption, 28_LVBus384117_production, 28_LVBus384118_consumption, 28_LVBus384118_production, 28_LVBus384119_consumption, 28_LVBus384119_production, 28_LVBus384120_production, 28_LVBus384121_production, 28_LVBus384123_consumption, 28_LVBus384123_production, 28_LVBus384124_consumption, 28_LVBus384124_production, 28_LVBus384126_production, 28_LVBus384127_production, 28_LVBus384128_production, 28_LVBus384129_production, 28_LVBus384130_production, 28_LVBus384132_consumption, 28_LVBus384132_production, 28_LVBus384134_production, 28_LVBus384135_production, 28_LVBus384136_consumption, 28_LVBus384136_production, 28_LVBus384137_production, 28_LVBus384138_production, 28_LVBus384139_consumption, 28_LVBus384139_production, 28_LVBus384140_consumption, 28_LVBus384140_production, 28_LVBus384141_consumption, 28_LVBus384141_production, 28_LVBus384152_consumption, 28_LVBus384152_production, 28_LVBus384153_production, 28_LVBus384154_production, 28_LVBus384155_production, 28_LVBus384156_production, 28_LVBus384157_production, 28_LVBus384158_production, 28_LVBus384160_production, 28_LVBus384161_consumption, 28_LVBus384161_production, 28_LVBus384162_production, 28_LVBus384163_consumption, 28_LVBus384163_production, 28_LVBus384164_production, 28_LVBus384165_production, 28_LVBus384169_production, 28_LVBus384170_production, 28_LVBus384171_production, 28_LVBus384172_production, 28_LVBus384173_production, 28_LVBus384174_production, 28_LVBus384176_production, 28_LVBus384177_consumption, 28_LVBus384177_production, 28_LVBus384178_production, 28_LVBus384180_production, 28_LVBus384181_production, 28_LVBus384182_production, 28_LVBus384183_production, 28_LVBus384184_production, 28_LVBus384185_production, 28_LVBus384186_production, 28_LVBus384187_production, 28_LVBus384191_production, 28_LVBus384193_production, 28_LVBus384195_consumption, 28_LVBus384195_production, 28_LVBus384197_consumption, 28_LVBus384197_production, 28_LVBus384198_production, 28_LVBus384199_production, 28_LVBus384201_production, 28_LVBus384202_production, 28_LVBus384203_production, 28_LVBus384204_production, 28_LVBus384206_consumption, 28_LVBus384206_production, 28_LVBus384207_production, 28_LVBus384208_production, 28_LVBus384209_production, 28_LVBus384210_production, 28_LVBus384211_production, 28_LVBus384212_production, 28_LVBus384213_production, 28_LVBus384214_production, 28_LVBus384215_production, 28_LVBus384220_production, 28_LVBus384221_production, 28_LVBus384222_production, 28_LVBus384223_consumption, 28_LVBus384223_production, 28_LVBus384224_production, 28_LVBus384226_production, 28_LVBus384227_consumption, 28_LVBus384227_production, 28_LVBus384228_production, 28_LVBus384229_production, 28_LVBus384231_production, 28_LVBus384232_production, 28_LVBus384233_consumption, 28_LVBus384233_production, 28_LVBus384234_production, 28_LVBus384235_consumption, 28_LVBus384235_production, 28_LVBus384236_production, 28_LVBus384239_consumption, 28_LVBus384239_production, 28_LVBus384240_consumption, 28_LVBus384240_production, 28_LVBus384241_consumption, 28_LVBus384241_production, 28_LVBus384243_consumption, 28_LVBus384243_production, 28_LVBus384244_consumption, 28_LVBus384244_production, 28_LVBus384245_consumption, 28_LVBus384245_production, 28_LVBus384246_consumption, 28_LVBus384246_production, 28_LVBus384247_production, 28_LVBus384248_production, 28_LVBus384249_production, 28_LVBus384251_consumption, 28_LVBus384251_production, 28_LVBus384253_consumption, 28_LVBus384253_production, 28_LVBus384254_production, 28_LVBus384255_consumption, 28_LVBus384255_production, 28_LVBus384256_production, 28_LVBus384257_production, 28_LVBus384258_consumption, 28_LVBus384258_production, 28_LVBus384259_production, 28_LVBus384260_consumption, 28_LVBus384260_production, 28_LVBus384261_consumption, 28_LVBus384261_production, 28_LVBus384262_production, 28_LVBus384266_consumption, 28_LVBus384266_production, 28_LVBus384267_consumption, 28_LVBus384267_production, 28_LVBus384268_production, 28_LVBus384269_production, 28_LVBus384270_consumption, 28_LVBus384270_production, 28_LVBus384271_production, 28_LVBus384272_production, 28_LVBus384273_production, 28_LVBus384274_production, 28_LVBus384275_production, 28_LVBus384276_production, 28_LVBus384280_consumption, 28_LVBus384280_production, 28_LVBus384281_production, 28_LVBus384282_production, 28_LVBus384284_production, 28_LVBus384285_production, 28_LVBus384287_production, 28_LVBus384288_production, 28_LVBus384289_consumption, 28_LVBus384289_production, 28_LVBus384290_production, 28_LVBus384291_consumption, 28_LVBus384291_production, 28_LVBus384293_production, 28_LVBus384294_production, 28_LVBus384296_consumption, 28_LVBus384296_production, 28_LVBus384323_production, 28_LVBus384324_production, 28_LVBus384325_consumption, 28_LVBus384325_production, 28_LVBus384326_production, 28_LVBus384328_production, 28_LVBus384329_production, 28_LVBus384330_production, 28_LVBus384331_production, 28_LVBus384332_production, 28_LVBus384333_production, 28_LVBus384334_production, 28_LVBus384336_consumption, 28_LVBus384336_production, 28_LVBus384337_production, 28_LVBus384338_production, 28_LVBus384339_production, 28_LVBus384340_consumption, 28_LVBus384340_production, 28_LVBus384341_production, 28_LVBus384342_production, 28_LVBus384343_production, 28_LVBus384344_production, 28_LVBus384345_consumption, 28_LVBus384345_production, 28_LVBus384346_consumption, 28_LVBus384346_production, 28_LVBus384347_consumption, 28_LVBus384347_production, 28_LVBus384348_consumption, 28_LVBus384348_production, 28_LVBus384349_consumption, 28_LVBus384349_production, 28_LVBus384354_production, 28_LVBus384355_production, 28_LVBus384356_production, 28_LVBus384357_production, 28_LVBus384358_production, 28_LVBus384359_production, 28_LVBus384360_production, 28_LVBus384362_production, 28_LVBus384363_production, 28_LVBus384364_consumption, 28_LVBus384364_production, 28_LVBus384366_production, 28_LVBus384367_production, 28_LVBus384368_production, 28_LVBus384369_production, 28_LVBus384370_production, 28_LVBus384371_consumption, 28_LVBus384371_production, 28_LVBus384372_production, 28_LVBus384374_production, 28_LVBus384375_consumption, 28_LVBus384375_production, 28_LVBus384377_production, 28_LVBus384378_production, 28_LVBus384379_production, 28_LVBus384381_consumption, 28_LVBus384381_production, 28_LVBus384382_production, 28_LVBus384383_production, 28_LVBus384384_production, 28_LVBus384385_consumption, 28_LVBus384385_production, 28_LVBus384386_production, 28_LVBus384387_production, 28_LVBus384388_production, 28_LVBus384390_consumption, 28_LVBus384390_production, 28_LVBus384392_production, 28_LVBus384393_production, 28_LVBus384394_production, 28_LVBus384396_consumption, 28_LVBus384396_production, 28_LVBus384397_production, 28_LVBus384399_production, 28_LVBus384400_production, 28_LVBus384401_production, 28_LVBus384402_production, 28_LVBus384403_production, 28_LVBus384405_consumption, 28_LVBus384405_production, 28_LVBus384407_production, 28_LVBus384408_production, 28_LVBus384410_production, 28_LVBus384411_production, 28_LVBus384412_production, 28_LVBus384413_consumption, 28_LVBus384413_production, 28_LVBus384414_production, 28_LVBus384415_production, 28_LVBus384416_production, 28_LVBus384420_production, 28_LVBus384421_production, 28_LVBus384422_consumption, 28_LVBus384422_production, 28_LVBus384423_production, 28_LVBus384424_production, 28_LVBus384425_production, 28_LVBus384427_production, 28_LVBus384428_production, 28_LVBus384429_production, 28_LVBus384430_consumption, 28_LVBus384430_production, 28_LVBus384432_consumption, 28_LVBus384432_production, 28_LVBus384433_consumption, 28_LVBus384433_production, 28_LVBus384437_consumption, 28_LVBus384437_production, 28_LVBus384438_consumption, 28_LVBus384438_production, 28_LVBus384439_production, 28_LVBus384440_consumption, 28_LVBus384440_production, 28_LVBus384441_production, 28_LVBus384442_consumption, 28_LVBus384442_production, 28_LVBus384443_production, 28_LVBus384444_production, 28_LVBus384445_production, 28_LVBus384448_consumption, 28_LVBus384448_production, 28_LVBus384449_production, 28_LVBus384451_production, 28_LVBus384452_production, 28_LVBus384453_consumption, 28_LVBus384453_production, 28_LVBus384455_consumption, 28_LVBus384455_production, 28_LVBus384456_production, 28_LVBus384457_production, 28_LVBus384458_production, 28_LVBus384460_production, 28_LVBus384461_production, 28_LVBus384462_production, 28_LVBus384464_production, 28_LVBus384465_production, 28_LVBus384466_production, 28_LVBus384467_production, 28_LVBus384469_production, 28_LVBus384470_production, 28_LVBus384472_consumption, 28_LVBus384472_production, 28_LVBus384473_production, 28_LVBus384474_production, 28_LVBus384475_consumption, 28_LVBus384475_production, 28_LVBus384476_consumption, 28_LVBus384476_production, 28_LVBus384477_consumption, 28_LVBus384477_production, 28_LVBus384478_consumption, 28_LVBus384478_production, 28_LVBus384479_production, 28_LVBus384480_production, 28_LVBus384481_production, 28_LVBus384482_production, 28_LVBus384483_production, 28_LVBus384488_consumption, 28_LVBus384488_production, 28_LVBus384489_production, 28_LVBus384490_consumption, 28_LVBus384490_production, 28_LVBus384491_production, 28_LVBus384497_production, 28_LVBus384499_production, 28_LVBus384500_production, 28_LVBus384501_production, 28_LVBus384502_production, 28_LVBus384503_consumption, 28_LVBus384503_production, 28_LVBus384504_production, 28_LVBus384506_production, 28_LVBus384507_production, 28_LVBus384508_production, 28_LVBus384509_production, 28_LVBus384511_production, 28_LVBus384512_production, 28_LVBus384513_production, 28_LVBus384514_consumption, 28_LVBus384514_production, 28_LVBus384515_production, 28_LVBus384517_consumption, 28_LVBus384517_production, 28_LVBus384518_consumption, 28_LVBus384518_production, 28_LVBus384519_production, 28_LVBus384521_production, 28_LVBus384522_consumption, 28_LVBus384522_production, 28_LVBus384523_production, 28_LVBus384524_production, 28_LVBus384525_production, 28_LVBus384526_consumption, 28_LVBus384526_production, 28_LVBus384527_production, 28_LVBus384528_production, 28_LVBus384529_production, 28_LVBus384532_production, 28_LVBus384533_production, 28_LVBus384534_consumption, 28_LVBus384534_production, 28_LVBus384535_consumption, 28_LVBus384535_production, 28_LVBus384536_production, 28_LVBus384537_production, 28_LVBus384538_consumption, 28_LVBus384538_production, 28_LVBus384539_production, 28_LVBus384540_production, 28_LVBus384541_production, 28_LVBus384542_production, 28_LVBus384543_production, 28_LVBus384544_consumption, 28_LVBus384544_production, 28_LVBus384545_production, 28_LVBus384549_consumption, 28_LVBus384549_production, 28_LVBus384550_production, 28_LVBus384551_consumption, 28_LVBus384551_production, 28_LVBus384552_consumption, 28_LVBus384552_production, 28_LVBus384553_production, 28_LVBus384554_production, 28_LVBus384555_production, 28_LVBus384556_production, 28_LVBus384557_consumption, 28_LVBus384557_production, 28_LVBus384558_production, 28_LVBus384559_production, 28_LVBus384560_production, 28_LVBus384561_production, 28_LVBus853387_production, 28_LVBus853388_production, 28_LVBus857312_production, 28_LVBus858252_production, 28_LVBus859398_production, 28_LVBus859399_production, 28_LVBus862125_production, 28_LVBus862201_consumption, 28_LVBus862201_production, 28_LVBus866721_production, 28_LVBus867496_production, 28_LVBus868948_production, 28_LVBus875700_consumption, 28_LVBus875700_production, 28_LVBus875701_consumption, 28_LVBus875701_production, 28_LVBus875702_consumption, 28_LVBus875702_production, 28_LVBus875703_production, 28_LVBus875704_consumption, 28_LVBus875704_production, 28_LVBus875705_consumption, 28_LVBus875705_production, 28_LVBus875706_consumption, 28_LVBus875706_production, 28_LVBus875707_consumption, 28_LVBus875707_production, 28_LVBus875708_production, 28_LVBus875709_production, 28_LVBus875710_production, 28_LVBus875711_consumption, 28_LVBus875711_production, 28_LVBus876280_production, 28_LVBus878610_production, 28_LVBus880508_consumption, 28_LVBus880508_production, 28_LVBus880509_production, 28_LVBus882586_production, 28_LVBus882587_consumption, 28_LVBus882587_production, 28_LVBus882588_consumption, 28_LVBus882588_production, 28_LVBus882589_consumption, 28_LVBus882589_production, 28_LVBus882590_production, 28_LVBus882591_production, 28_LVBus882823_production, 28_LVBus882824_consumption, 28_LVBus882824_production, 28_LVBus882825_production, 28_LVBus882826_production, 28_LVBus882827_production, 28_LVBus882828_consumption, 28_LVBus882828_production, 28_LVBus882829_production, 28_LVBus886578_consumption, 28_LVBus886578_production, 28_LVBus888319_consumption, 28_LVBus888319_production, 28_LVBus888320_production, 28_LVBus896164_production, 28_LVBus896599_production, 28_LVBus897753_consumption, 28_LVBus897753_production, 28_LVBus897754_consumption, 28_LVBus897754_production, 28_LVBus897755_production, 28_LVBus899951_production, 28_LVBus899963_production, 28_LVBus900517_production, 28_LVBus901757_consumption, 28_LVBus901757_production, 28_LVBus907924_production, 28_LVBus909744_consumption, 28_LVBus909744_production, 28_LVBus912140_production, 28_LVBus915596_consumption, 28_LVBus915596_production, 28_LVBus915597_production, 28_LVBus920889_production, 28_LVBus920890_production, 28_LVBus920891_production, 28_LVBus920892_production, 28_LVBus920893_production, 28_LVBus920894_consumption, 28_LVBus920894_production, 28_LVBus920895_production, 28_LVBus920896_production, 28_LVBus920897_production, 28_LVBus933881_production, 28_LVBus933882_consumption, 28_LVBus933882_production, 28_LVBus933883_consumption, 28_LVBus933883_production, 28_LVBus933884_production, 28_LVBus936642_production, 28_LVBus942217_consumption, 28_LVBus942217_production, 28_LVBus942218_production, 28_LVBus946495_production, 28_LVBus946600_production, 28_LVBus946807_production, 28_LVBus946808_production, 28_LVBus946809_production, 28_LVBus946810_production, 28_LVBus946811_production, 28_LVBus946812_production, 28_LVBus947034_production, 28_LVBus947228_production, 28_LVBus947229_consumption, 28_LVBus947229_production, 28_LVBus947230_production, 28_LVBus947231_production, 28_LVBus948190_production, 28_LVBus948191_production, 28_LVBus948192_production, 28_LVBus948193_production, 28_LVBus958807_production, 28_LVBus958808_production, 28_LVBus958809_production, 28_LVBus958810_production, 28_LVBus958811_production, 28_LVBus960410_production, 28_LVBus965357_production, 28_LVBus965358_production, 28_LVBus968024_production, 28_LVBus968426_production, 28_LVBus972582_production, 28_LVBus973107_consumption, 28_LVBus973107_production, 28_LVBus973108_production, 28_LVBus973109_production, 28_LVBus973388_production, 28_LVBus973389_production, 28_LVBus973390_production, 28_LVBus973391_production, 28_LVBus976502_production, 28_LVBus976503_production, 28_LVBus976504_production, 28_LVBus976505_production, 28_LVBus976506_production, 28_MVLV03530_consumption, 28_MVLV03530_production, 28_MVLV21704_consumption, 28_MVLV21704_production, 28_MVLV61838_consumption, 28_MVLV61838_production, 28_MVLV66122_consumption, 28_MVLV66122_production, 28_MVLV74435_consumption, 28_MVLV74435_production, 28_MVLV81617_consumption, 28_MVLV81617_production.

