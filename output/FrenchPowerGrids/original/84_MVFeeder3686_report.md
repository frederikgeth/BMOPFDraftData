# BMOPF Network Summary: 84_MVFeeder3686

**Generated:** 2026-10-01 23:34:45  
**Findings:** 0 errors · 4 warnings · 320 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 62 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 747 |  |
| line | 684 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1130 | 1.441 MW, 432.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 62 |  |
| switch | 0 |  |
| transformer | 62 | Dyn11×62 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 131 | 130 | 22 | 0 |
| LV_236V | 236.0 V | 616 | 554 | 1108 | 0 |

**Transformer transitions:**

- `84_MVLV039451_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV034369_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV106355_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094808_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV035202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV151476_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV062824_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV002052_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV073075_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV108351_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV106365_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV023355_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115725_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115836_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044889_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV020169_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV009419_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV147605_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV031844_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV031751_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094213_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV035015_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV099469_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044131_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV067248_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV092739_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV003947_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV131773_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV098918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV151524_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV037012_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV131583_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV034763_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV059439_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV016812_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV083213_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV124931_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094620_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV062294_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV016590_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV095847_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV113780_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV080137_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV030225_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115587_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV047082_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV034764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV077196_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV078452_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV031729_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV098043_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV030641_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV072395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV028739_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV056800_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094420_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV098713_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV018951_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV016595_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV067306_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV031733_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV016591_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 245 |
| Tree depth (max hops) | 45 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 747 | 1 | 746 | 0 | 0 | 0 |
| Tier LV_236V | 616 | 62 | 554 | 0 | 0 | 0 |
| Tier MV_11.8kV | 131 | 1 | 130 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 62; skipped invalid branches: 0.

Galvanic zones: 63; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MVBus091363 | MV_11.8kV | 131 | 0 | 0 | 62 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2857 declared bus terminals; 2606 mapped line/closed-switch conductor edges; 251 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 21100.0 | 3.904 | 3390 |
| q_nom | 0.0 | 6340.0 | 3.904 | 3390 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.45 | 3700.0 | 1.71 | 684 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.64 | 62 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 791 of 1130 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533212_consumption' has phase imbalance of 72.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533400_consumption' has phase imbalance of 290.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533329_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533404_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533390_consumption' has phase imbalance of 271.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532996_consumption' has phase imbalance of 92.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533437_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533093_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532940_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533357_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533416_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533032_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533382_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533055_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532919_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533420_consumption' has phase imbalance of 155.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532923_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533098_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532935_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533049_consumption' has phase imbalance of 283.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533105_consumption' has phase imbalance of 191.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533510_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533190_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533225_consumption' has phase imbalance of 204.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533232_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533311_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532871_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532956_consumption' has phase imbalance of 35.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2049579_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533166_consumption' has phase imbalance of 220.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533383_consumption' has phase imbalance of 181.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533054_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533325_consumption' has phase imbalance of 121.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533366_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533023_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533340_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533040_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533200_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533338_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533028_consumption' has phase imbalance of 137.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532957_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533027_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532954_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533421_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533430_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533001_consumption' has phase imbalance of 197.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2016519_consumption' has phase imbalance of 159.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533488_consumption' has phase imbalance of 231.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533151_consumption' has phase imbalance of 230.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533501_consumption' has phase imbalance of 134.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532979_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533492_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533487_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532890_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533047_consumption' has phase imbalance of 182.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532906_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532994_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533006_consumption' has phase imbalance of 267.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533507_consumption' has phase imbalance of 41.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533036_consumption' has phase imbalance of 138.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2074610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532953_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532939_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2238908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532990_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533051_consumption' has phase imbalance of 187.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2044933_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533349_consumption' has phase imbalance of 211.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532933_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533163_consumption' has phase imbalance of 270.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532982_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533048_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533039_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533396_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533171_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533402_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533207_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533186_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532907_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533174_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533197_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533238_consumption' has phase imbalance of 284.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533360_consumption' has phase imbalance of 47.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533300_consumption' has phase imbalance of 256.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532980_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2249254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532947_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533491_consumption' has phase imbalance of 42.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533016_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532870_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533025_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533463_consumption' has phase imbalance of 273.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533244_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533485_consumption' has phase imbalance of 139.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533211_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532955_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533479_consumption' has phase imbalance of 267.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533083_consumption' has phase imbalance of 106.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533050_consumption' has phase imbalance of 128.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533450_consumption' has phase imbalance of 112.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532931_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533411_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533176_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2044931_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533081_consumption' has phase imbalance of 212.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533201_consumption' has phase imbalance of 121.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533094_consumption' has phase imbalance of 191.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533061_consumption' has phase imbalance of 205.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2143525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532938_consumption' has phase imbalance of 289.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532942_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2249255_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532918_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532908_consumption' has phase imbalance of 44.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532970_consumption' has phase imbalance of 266.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533495_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533210_consumption' has phase imbalance of 256.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533029_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2044932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533502_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533111_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533370_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533352_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533347_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533497_consumption' has phase imbalance of 97.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2014980_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533432_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533306_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533348_consumption' has phase imbalance of 278.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533038_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533209_consumption' has phase imbalance of 146.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533405_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533230_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533410_consumption' has phase imbalance of 284.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532917_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533343_consumption' has phase imbalance of 25.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2047187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533158_consumption' has phase imbalance of 62.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533059_consumption' has phase imbalance of 219.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532879_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533017_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533422_consumption' has phase imbalance of 73.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533474_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533035_consumption' has phase imbalance of 180.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533192_consumption' has phase imbalance of 61.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533493_consumption' has phase imbalance of 120.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533031_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532967_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533037_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533413_consumption' has phase imbalance of 239.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533056_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533185_consumption' has phase imbalance of 83.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533060_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533328_consumption' has phase imbalance of 33.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533500_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532963_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533053_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533116_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532912_consumption' has phase imbalance of 69.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533058_consumption' has phase imbalance of 142.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532934_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2044940_consumption' has phase imbalance of 52.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532905_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533317_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533447_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533506_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532920_consumption' has phase imbalance of 237.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533412_consumption' has phase imbalance of 36.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532910_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533496_consumption' has phase imbalance of 204.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533275_consumption' has phase imbalance of 58.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532944_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533203_consumption' has phase imbalance of 75.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2044934_consumption' has phase imbalance of 121.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533119_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1532899_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533476_consumption' has phase imbalance of 263.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533314_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1533135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1130 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1533088' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1533512' has balanced aggregate load across 3 phase(s) (max spread 0.94%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1533455' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.441 MW |
| Total load Q | 432.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV039451_Transformer | 110.0 kVA | 5.8% |
| 84_MVLV034369_Transformer | 110.0 kVA | 0.9% |
| 84_MVLV106355_Transformer | 440.0 kVA | 20.1% |
| 84_MVLV094808_Transformer | 110.0 kVA | 3.0% |
| 84_MVLV035202_Transformer | 110.0 kVA | 0.9% |
| 84_MVLV151476_Transformer | 110.0 kVA | 2.6% |
| 84_MVLV062824_Transformer | 110.0 kVA | 1.6% |
| 84_MVLV002052_Transformer | 110.0 kVA | 4.2% |
| 84_MVLV073075_Transformer | 275.0 kVA | 18.8% |
| 84_MVLV108351_Transformer | 440.0 kVA | 15.2% |
| 84_MVLV106365_Transformer | 176.0 kVA | 23.1% |
| 84_MVLV023355_Transformer | 110.0 kVA | 6.7% |
| 84_MVLV115725_Transformer | 110.0 kVA | 7.7% |
| 84_MVLV115836_Transformer | 275.0 kVA | 19.2% |
| 84_MVLV044889_Transformer | 110.0 kVA | 1.1% |
| 84_MVLV020169_Transformer | 110.0 kVA | 9.2% |
| 84_MVLV009419_Transformer | 176.0 kVA | 12.7% |
| 84_MVLV147605_Transformer | 110.0 kVA | 3.2% |
| 84_MVLV031844_Transformer | 440.0 kVA | 28.0% |
| 84_MVLV031751_Transformer | 275.0 kVA | 17.3% |
| 84_MVLV094213_Transformer | 110.0 kVA | 2.9% |
| 84_MVLV035015_Transformer | 440.0 kVA | 20.0% |
| 84_MVLV099469_Transformer | 176.0 kVA | 6.4% |
| 84_MVLV044131_Transformer | 110.0 kVA | 2.8% |
| 84_MVLV067248_Transformer | 110.0 kVA | 0.1% |
| 84_MVLV092739_Transformer | 110.0 kVA | 4.8% |
| 84_MVLV003947_Transformer | 110.0 kVA | 10.2% |
| 84_MVLV131773_Transformer | 275.0 kVA | 13.0% |
| 84_MVLV098918_Transformer | 110.0 kVA | 3.5% |
| 84_MVLV151524_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV037012_Transformer | 110.0 kVA | 14.1% |
| 84_MVLV131583_Transformer | 440.0 kVA | 23.3% |
| 84_MVLV034763_Transformer | 110.0 kVA | 2.0% |
| 84_MVLV059439_Transformer | 176.0 kVA | 9.1% |
| 84_MVLV016812_Transformer | 176.0 kVA | 15.8% |
| 84_MVLV083213_Transformer | 110.0 kVA | 6.4% |
| 84_MVLV124931_Transformer | 176.0 kVA | 17.5% |
| 84_MVLV094620_Transformer | 110.0 kVA | 2.3% |
| 84_MVLV062294_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV016590_Transformer | 440.0 kVA | 29.2% |
| 84_MVLV095847_Transformer | 440.0 kVA | 29.5% |
| 84_MVLV113780_Transformer | 110.0 kVA | 4.0% |
| 84_MVLV080137_Transformer | 110.0 kVA | 2.3% |
| 84_MVLV030225_Transformer | 110.0 kVA | 0.5% |
| 84_MVLV115587_Transformer | 110.0 kVA | 3.8% |
| 84_MVLV047082_Transformer | 110.0 kVA | 2.4% |
| 84_MVLV034764_Transformer | 440.0 kVA | 12.8% |
| 84_MVLV077196_Transformer | 110.0 kVA | 4.5% |
| 84_MVLV078452_Transformer | 176.0 kVA | 10.6% |
| 84_MVLV031729_Transformer | 110.0 kVA | 7.1% |
| 84_MVLV098043_Transformer | 176.0 kVA | 13.4% |
| 84_MVLV030641_Transformer | 110.0 kVA | 4.7% |
| 84_MVLV072395_Transformer | 440.0 kVA | 12.7% |
| 84_MVLV028739_Transformer | 440.0 kVA | 14.5% |
| 84_MVLV056800_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV094420_Transformer | 110.0 kVA | 7.3% |
| 84_MVLV098713_Transformer | 110.0 kVA | 2.1% |
| 84_MVLV018951_Transformer | 110.0 kVA | 1.9% |
| 84_MVLV016595_Transformer | 110.0 kVA | 7.5% |
| 84_MVLV067306_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV031733_Transformer | 110.0 kVA | 14.2% |
| 84_MVLV016591_Transformer | 176.0 kVA | 27.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.44 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_SSCL5' (MV, 11.78 kV) has an electrical reach of 24.77 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus1533010' (LV, 0.24 kV) has an electrical reach of 20.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus1533101' (LV, 0.24 kV) has an electrical reach of 1.3 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus1533250' (LV, 0.24 kV) has an electrical reach of 1.07 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus1533158' (LV, 0.24 kV) has an electrical reach of 1.05 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus1533168' (LV, 0.24 kV) has an electrical reach of 13.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus1533461' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus1533180' (LV, 0.24 kV) has an electrical reach of 9.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus1533178' (LV, 0.24 kV) has an electrical reach of 11.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus1533156' (LV, 0.24 kV) has an electrical reach of 21.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 747 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 747 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 62 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 131 |
| LV_236V | 4-wire | 616 / 616 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 616 |
| Neutral branches | 554 |
| Grounding points | 62 |
| Neutral sections | 62 |
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
| 11.78 kV | 131 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 41 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 63 |
| Islands without voltage reference | 0 |
| Line impedance spread | 3810.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 616 / 131 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 792 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 792 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1532863_consumption, 84_LVBus1532863_production, 84_LVBus1532864_consumption, 84_LVBus1532864_production, 84_LVBus1532865_consumption, 84_LVBus1532865_production, 84_LVBus1532866_production, 84_LVBus1532867_consumption, 84_LVBus1532867_production, 84_LVBus1532868_production, 84_LVBus1532869_consumption, 84_LVBus1532869_production, 84_LVBus1532870_production, 84_LVBus1532871_production, 84_LVBus1532876_production, 84_LVBus1532877_production, 84_LVBus1532878_consumption, 84_LVBus1532878_production, 84_LVBus1532879_production, 84_LVBus1532880_production, 84_LVBus1532881_consumption, 84_LVBus1532881_production, 84_LVBus1532882_consumption, 84_LVBus1532882_production, 84_LVBus1532883_production, 84_LVBus1532884_production, 84_LVBus1532886_consumption, 84_LVBus1532886_production, 84_LVBus1532888_consumption, 84_LVBus1532888_production, 84_LVBus1532889_production, 84_LVBus1532890_production, 84_LVBus1532891_consumption, 84_LVBus1532891_production, 84_LVBus1532892_production, 84_LVBus1532893_production, 84_LVBus1532894_consumption, 84_LVBus1532894_production, 84_LVBus1532895_consumption, 84_LVBus1532895_production, 84_LVBus1532896_production, 84_LVBus1532897_consumption, 84_LVBus1532897_production, 84_LVBus1532898_consumption, 84_LVBus1532898_production, 84_LVBus1532899_production, 84_LVBus1532901_consumption, 84_LVBus1532901_production, 84_LVBus1532902_production, 84_LVBus1532904_consumption, 84_LVBus1532904_production, 84_LVBus1532905_production, 84_LVBus1532906_production, 84_LVBus1532907_production, 84_LVBus1532908_production, 84_LVBus1532909_consumption, 84_LVBus1532909_production, 84_LVBus1532910_production, 84_LVBus1532911_production, 84_LVBus1532912_production, 84_LVBus1532913_production, 84_LVBus1532914_consumption, 84_LVBus1532914_production, 84_LVBus1532916_consumption, 84_LVBus1532916_production, 84_LVBus1532917_production, 84_LVBus1532918_production, 84_LVBus1532919_production, 84_LVBus1532920_production, 84_LVBus1532921_production, 84_LVBus1532922_production, 84_LVBus1532923_production, 84_LVBus1532924_production, 84_LVBus1532926_production, 84_LVBus1532927_production, 84_LVBus1532928_consumption, 84_LVBus1532928_production, 84_LVBus1532929_production, 84_LVBus1532930_production, 84_LVBus1532931_production, 84_LVBus1532932_consumption, 84_LVBus1532932_production, 84_LVBus1532933_production, 84_LVBus1532934_production, 84_LVBus1532935_production, 84_LVBus1532937_production, 84_LVBus1532938_production, 84_LVBus1532939_production, 84_LVBus1532940_production, 84_LVBus1532941_production, 84_LVBus1532942_production, 84_LVBus1532943_consumption, 84_LVBus1532943_production, 84_LVBus1532944_production, 84_LVBus1532946_production, 84_LVBus1532947_production, 84_LVBus1532949_consumption, 84_LVBus1532949_production, 84_LVBus1532950_production, 84_LVBus1532951_consumption, 84_LVBus1532951_production, 84_LVBus1532952_consumption, 84_LVBus1532952_production, 84_LVBus1532953_production, 84_LVBus1532954_production, 84_LVBus1532955_production, 84_LVBus1532956_production, 84_LVBus1532957_production, 84_LVBus1532961_production, 84_LVBus1532963_production, 84_LVBus1532965_production, 84_LVBus1532967_production, 84_LVBus1532968_production, 84_LVBus1532969_production, 84_LVBus1532970_production, 84_LVBus1532973_consumption, 84_LVBus1532973_production, 84_LVBus1532976_consumption, 84_LVBus1532976_production, 84_LVBus1532977_production, 84_LVBus1532978_production, 84_LVBus1532979_production, 84_LVBus1532980_production, 84_LVBus1532981_consumption, 84_LVBus1532981_production, 84_LVBus1532982_production, 84_LVBus1532983_production, 84_LVBus1532985_production, 84_LVBus1532986_production, 84_LVBus1532987_consumption, 84_LVBus1532987_production, 84_LVBus1532988_consumption, 84_LVBus1532988_production, 84_LVBus1532989_consumption, 84_LVBus1532989_production, 84_LVBus1532990_production, 84_LVBus1532992_consumption, 84_LVBus1532992_production, 84_LVBus1532994_production, 84_LVBus1532996_production, 84_LVBus1532998_consumption, 84_LVBus1532998_production, 84_LVBus1532999_consumption, 84_LVBus1532999_production, 84_LVBus1533000_consumption, 84_LVBus1533000_production, 84_LVBus1533001_production, 84_LVBus1533002_production, 84_LVBus1533004_production, 84_LVBus1533005_production, 84_LVBus1533006_production, 84_LVBus1533008_production, 84_LVBus1533010_production, 84_LVBus1533012_consumption, 84_LVBus1533012_production, 84_LVBus1533013_production, 84_LVBus1533015_production, 84_LVBus1533016_production, 84_LVBus1533017_production, 84_LVBus1533018_consumption, 84_LVBus1533018_production, 84_LVBus1533019_consumption, 84_LVBus1533019_production, 84_LVBus1533020_production, 84_LVBus1533023_production, 84_LVBus1533024_production, 84_LVBus1533025_production, 84_LVBus1533027_production, 84_LVBus1533028_production, 84_LVBus1533029_production, 84_LVBus1533031_production, 84_LVBus1533032_production, 84_LVBus1533034_consumption, 84_LVBus1533034_production, 84_LVBus1533035_production, 84_LVBus1533036_production, 84_LVBus1533037_production, 84_LVBus1533038_production, 84_LVBus1533039_production, 84_LVBus1533040_production, 84_LVBus1533041_production, 84_LVBus1533043_consumption, 84_LVBus1533043_production, 84_LVBus1533044_consumption, 84_LVBus1533044_production, 84_LVBus1533045_production, 84_LVBus1533047_production, 84_LVBus1533048_production, 84_LVBus1533049_production, 84_LVBus1533050_production, 84_LVBus1533051_production, 84_LVBus1533053_production, 84_LVBus1533054_production, 84_LVBus1533055_production, 84_LVBus1533056_production, 84_LVBus1533057_production, 84_LVBus1533058_production, 84_LVBus1533059_production, 84_LVBus1533060_production, 84_LVBus1533061_production, 84_LVBus1533064_consumption, 84_LVBus1533064_production, 84_LVBus1533065_production, 84_LVBus1533066_consumption, 84_LVBus1533066_production, 84_LVBus1533067_consumption, 84_LVBus1533067_production, 84_LVBus1533069_production, 84_LVBus1533070_production, 84_LVBus1533071_consumption, 84_LVBus1533071_production, 84_LVBus1533072_consumption, 84_LVBus1533072_production, 84_LVBus1533073_production, 84_LVBus1533075_production, 84_LVBus1533076_production, 84_LVBus1533077_consumption, 84_LVBus1533077_production, 84_LVBus1533079_production, 84_LVBus1533080_consumption, 84_LVBus1533080_production, 84_LVBus1533081_production, 84_LVBus1533082_consumption, 84_LVBus1533082_production, 84_LVBus1533083_production, 84_LVBus1533084_consumption, 84_LVBus1533084_production, 84_LVBus1533085_production, 84_LVBus1533086_consumption, 84_LVBus1533086_production, 84_LVBus1533088_consumption, 84_LVBus1533088_production, 84_LVBus1533089_consumption, 84_LVBus1533089_production, 84_LVBus1533090_production, 84_LVBus1533091_consumption, 84_LVBus1533091_production, 84_LVBus1533093_production, 84_LVBus1533094_production, 84_LVBus1533095_consumption, 84_LVBus1533095_production, 84_LVBus1533097_consumption, 84_LVBus1533097_production, 84_LVBus1533098_production, 84_LVBus1533101_consumption, 84_LVBus1533101_production, 84_LVBus1533102_consumption, 84_LVBus1533102_production, 84_LVBus1533103_production, 84_LVBus1533104_consumption, 84_LVBus1533104_production, 84_LVBus1533105_production, 84_LVBus1533106_production, 84_LVBus1533107_consumption, 84_LVBus1533107_production, 84_LVBus1533109_consumption, 84_LVBus1533109_production, 84_LVBus1533110_consumption, 84_LVBus1533110_production, 84_LVBus1533111_production, 84_LVBus1533112_production, 84_LVBus1533113_consumption, 84_LVBus1533113_production, 84_LVBus1533115_consumption, 84_LVBus1533115_production, 84_LVBus1533116_production, 84_LVBus1533117_production, 84_LVBus1533118_production, 84_LVBus1533119_production, 84_LVBus1533125_consumption, 84_LVBus1533125_production, 84_LVBus1533126_consumption, 84_LVBus1533126_production, 84_LVBus1533127_production, 84_LVBus1533128_consumption, 84_LVBus1533128_production, 84_LVBus1533129_consumption, 84_LVBus1533129_production, 84_LVBus1533130_consumption, 84_LVBus1533130_production, 84_LVBus1533131_production, 84_LVBus1533132_consumption, 84_LVBus1533132_production, 84_LVBus1533133_consumption, 84_LVBus1533133_production, 84_LVBus1533134_production, 84_LVBus1533135_production, 84_LVBus1533136_production, 84_LVBus1533139_consumption, 84_LVBus1533139_production, 84_LVBus1533140_production, 84_LVBus1533141_consumption, 84_LVBus1533141_production, 84_LVBus1533142_consumption, 84_LVBus1533142_production, 84_LVBus1533143_consumption, 84_LVBus1533143_production, 84_LVBus1533144_consumption, 84_LVBus1533144_production, 84_LVBus1533145_production, 84_LVBus1533146_consumption, 84_LVBus1533146_production, 84_LVBus1533147_consumption, 84_LVBus1533147_production, 84_LVBus1533149_consumption, 84_LVBus1533149_production, 84_LVBus1533150_production, 84_LVBus1533151_production, 84_LVBus1533152_consumption, 84_LVBus1533152_production, 84_LVBus1533156_consumption, 84_LVBus1533156_production, 84_LVBus1533158_production, 84_LVBus1533160_production, 84_LVBus1533162_consumption, 84_LVBus1533162_production, 84_LVBus1533163_production, 84_LVBus1533164_consumption, 84_LVBus1533164_production, 84_LVBus1533165_production, 84_LVBus1533166_production, 84_LVBus1533168_consumption, 84_LVBus1533168_production, 84_LVBus1533170_production, 84_LVBus1533171_production, 84_LVBus1533173_consumption, 84_LVBus1533173_production, 84_LVBus1533174_production, 84_LVBus1533175_consumption, 84_LVBus1533175_production, 84_LVBus1533176_production, 84_LVBus1533178_production, 84_LVBus1533180_consumption, 84_LVBus1533180_production, 84_LVBus1533182_production, 84_LVBus1533183_production, 84_LVBus1533184_production, 84_LVBus1533185_production, 84_LVBus1533186_production, 84_LVBus1533187_production, 84_LVBus1533188_production, 84_LVBus1533190_production, 84_LVBus1533191_consumption, 84_LVBus1533191_production, 84_LVBus1533192_production, 84_LVBus1533193_production, 84_LVBus1533194_consumption, 84_LVBus1533194_production, 84_LVBus1533196_consumption, 84_LVBus1533196_production, 84_LVBus1533197_production, 84_LVBus1533198_consumption, 84_LVBus1533198_production, 84_LVBus1533199_consumption, 84_LVBus1533199_production, 84_LVBus1533200_production, 84_LVBus1533201_production, 84_LVBus1533202_production, 84_LVBus1533203_production, 84_LVBus1533204_consumption, 84_LVBus1533204_production, 84_LVBus1533205_production, 84_LVBus1533206_production, 84_LVBus1533207_production, 84_LVBus1533208_production, 84_LVBus1533209_production, 84_LVBus1533210_production, 84_LVBus1533211_production, 84_LVBus1533212_production, 84_LVBus1533214_consumption, 84_LVBus1533214_production, 84_LVBus1533217_consumption, 84_LVBus1533217_production, 84_LVBus1533218_consumption, 84_LVBus1533218_production, 84_LVBus1533219_production, 84_LVBus1533220_consumption, 84_LVBus1533220_production, 84_LVBus1533221_production, 84_LVBus1533222_consumption, 84_LVBus1533222_production, 84_LVBus1533223_consumption, 84_LVBus1533223_production, 84_LVBus1533224_production, 84_LVBus1533225_production, 84_LVBus1533229_consumption, 84_LVBus1533229_production, 84_LVBus1533230_production, 84_LVBus1533231_production, 84_LVBus1533232_production, 84_LVBus1533233_consumption, 84_LVBus1533233_production, 84_LVBus1533234_production, 84_LVBus1533235_consumption, 84_LVBus1533235_production, 84_LVBus1533236_consumption, 84_LVBus1533236_production, 84_LVBus1533237_production, 84_LVBus1533238_production, 84_LVBus1533239_production, 84_LVBus1533241_consumption, 84_LVBus1533241_production, 84_LVBus1533242_consumption, 84_LVBus1533242_production, 84_LVBus1533243_production, 84_LVBus1533244_production, 84_LVBus1533245_consumption, 84_LVBus1533245_production, 84_LVBus1533246_consumption, 84_LVBus1533246_production, 84_LVBus1533247_production, 84_LVBus1533248_production, 84_LVBus1533250_consumption, 84_LVBus1533250_production, 84_LVBus1533251_consumption, 84_LVBus1533251_production, 84_LVBus1533252_consumption, 84_LVBus1533252_production, 84_LVBus1533253_production, 84_LVBus1533254_consumption, 84_LVBus1533254_production, 84_LVBus1533255_consumption, 84_LVBus1533255_production, 84_LVBus1533256_consumption, 84_LVBus1533256_production, 84_LVBus1533257_consumption, 84_LVBus1533257_production, 84_LVBus1533258_production, 84_LVBus1533259_production, 84_LVBus1533260_consumption, 84_LVBus1533260_production, 84_LVBus1533261_production, 84_LVBus1533262_consumption, 84_LVBus1533262_production, 84_LVBus1533263_production, 84_LVBus1533264_production, 84_LVBus1533267_production, 84_LVBus1533269_consumption, 84_LVBus1533269_production, 84_LVBus1533270_consumption, 84_LVBus1533270_production, 84_LVBus1533271_consumption, 84_LVBus1533271_production, 84_LVBus1533272_consumption, 84_LVBus1533272_production, 84_LVBus1533273_production, 84_LVBus1533274_consumption, 84_LVBus1533274_production, 84_LVBus1533275_production, 84_LVBus1533276_consumption, 84_LVBus1533276_production, 84_LVBus1533278_consumption, 84_LVBus1533278_production, 84_LVBus1533280_consumption, 84_LVBus1533280_production, 84_LVBus1533282_production, 84_LVBus1533283_consumption, 84_LVBus1533283_production, 84_LVBus1533285_consumption, 84_LVBus1533285_production, 84_LVBus1533286_consumption, 84_LVBus1533286_production, 84_LVBus1533287_consumption, 84_LVBus1533287_production, 84_LVBus1533288_production, 84_LVBus1533289_production, 84_LVBus1533291_consumption, 84_LVBus1533291_production, 84_LVBus1533292_consumption, 84_LVBus1533292_production, 84_LVBus1533293_consumption, 84_LVBus1533293_production, 84_LVBus1533294_consumption, 84_LVBus1533294_production, 84_LVBus1533295_production, 84_LVBus1533296_production, 84_LVBus1533297_consumption, 84_LVBus1533297_production, 84_LVBus1533298_consumption, 84_LVBus1533298_production, 84_LVBus1533299_consumption, 84_LVBus1533299_production, 84_LVBus1533300_production, 84_LVBus1533301_consumption, 84_LVBus1533301_production, 84_LVBus1533302_consumption, 84_LVBus1533302_production, 84_LVBus1533303_consumption, 84_LVBus1533303_production, 84_LVBus1533304_production, 84_LVBus1533305_consumption, 84_LVBus1533305_production, 84_LVBus1533306_production, 84_LVBus1533307_production, 84_LVBus1533309_consumption, 84_LVBus1533309_production, 84_LVBus1533310_consumption, 84_LVBus1533310_production, 84_LVBus1533311_production, 84_LVBus1533312_consumption, 84_LVBus1533312_production, 84_LVBus1533313_consumption, 84_LVBus1533313_production, 84_LVBus1533314_production, 84_LVBus1533315_consumption, 84_LVBus1533315_production, 84_LVBus1533317_production, 84_LVBus1533319_production, 84_LVBus1533324_consumption, 84_LVBus1533324_production, 84_LVBus1533325_production, 84_LVBus1533327_consumption, 84_LVBus1533327_production, 84_LVBus1533328_production, 84_LVBus1533329_production, 84_LVBus1533330_production, 84_LVBus1533331_production, 84_LVBus1533332_production, 84_LVBus1533333_consumption, 84_LVBus1533333_production, 84_LVBus1533334_production, 84_LVBus1533335_consumption, 84_LVBus1533335_production, 84_LVBus1533336_consumption, 84_LVBus1533336_production, 84_LVBus1533338_production, 84_LVBus1533339_production, 84_LVBus1533340_production, 84_LVBus1533341_production, 84_LVBus1533342_production, 84_LVBus1533343_production, 84_LVBus1533344_consumption, 84_LVBus1533344_production, 84_LVBus1533345_consumption, 84_LVBus1533345_production, 84_LVBus1533346_consumption, 84_LVBus1533346_production, 84_LVBus1533347_production, 84_LVBus1533348_production, 84_LVBus1533349_production, 84_LVBus1533351_consumption, 84_LVBus1533351_production, 84_LVBus1533352_production, 84_LVBus1533353_production, 84_LVBus1533355_production, 84_LVBus1533356_production, 84_LVBus1533357_production, 84_LVBus1533358_consumption, 84_LVBus1533358_production, 84_LVBus1533359_production, 84_LVBus1533360_production, 84_LVBus1533364_consumption, 84_LVBus1533364_production, 84_LVBus1533365_consumption, 84_LVBus1533365_production, 84_LVBus1533366_production, 84_LVBus1533368_consumption, 84_LVBus1533368_production, 84_LVBus1533369_consumption, 84_LVBus1533369_production, 84_LVBus1533370_production, 84_LVBus1533371_production, 84_LVBus1533374_consumption, 84_LVBus1533374_production, 84_LVBus1533375_production, 84_LVBus1533376_consumption, 84_LVBus1533376_production, 84_LVBus1533377_production, 84_LVBus1533378_consumption, 84_LVBus1533378_production, 84_LVBus1533379_consumption, 84_LVBus1533379_production, 84_LVBus1533380_consumption, 84_LVBus1533380_production, 84_LVBus1533382_production, 84_LVBus1533383_production, 84_LVBus1533384_production, 84_LVBus1533385_production, 84_LVBus1533386_consumption, 84_LVBus1533386_production, 84_LVBus1533387_production, 84_LVBus1533388_production, 84_LVBus1533389_consumption, 84_LVBus1533389_production, 84_LVBus1533390_production, 84_LVBus1533391_production, 84_LVBus1533395_production, 84_LVBus1533396_production, 84_LVBus1533397_production, 84_LVBus1533398_production, 84_LVBus1533399_production, 84_LVBus1533400_production, 84_LVBus1533401_production, 84_LVBus1533402_production, 84_LVBus1533403_production, 84_LVBus1533404_production, 84_LVBus1533405_production, 84_LVBus1533408_consumption, 84_LVBus1533408_production, 84_LVBus1533409_consumption, 84_LVBus1533409_production, 84_LVBus1533410_production, 84_LVBus1533411_production, 84_LVBus1533412_production, 84_LVBus1533413_production, 84_LVBus1533414_production, 84_LVBus1533416_production, 84_LVBus1533417_consumption, 84_LVBus1533417_production, 84_LVBus1533418_consumption, 84_LVBus1533418_production, 84_LVBus1533419_production, 84_LVBus1533420_production, 84_LVBus1533421_production, 84_LVBus1533422_production, 84_LVBus1533424_production, 84_LVBus1533426_production, 84_LVBus1533427_consumption, 84_LVBus1533427_production, 84_LVBus1533428_production, 84_LVBus1533429_consumption, 84_LVBus1533429_production, 84_LVBus1533430_production, 84_LVBus1533432_production, 84_LVBus1533434_consumption, 84_LVBus1533434_production, 84_LVBus1533435_consumption, 84_LVBus1533435_production, 84_LVBus1533436_production, 84_LVBus1533437_production, 84_LVBus1533438_consumption, 84_LVBus1533438_production, 84_LVBus1533439_consumption, 84_LVBus1533439_production, 84_LVBus1533440_consumption, 84_LVBus1533440_production, 84_LVBus1533441_consumption, 84_LVBus1533441_production, 84_LVBus1533442_consumption, 84_LVBus1533442_production, 84_LVBus1533443_consumption, 84_LVBus1533443_production, 84_LVBus1533444_consumption, 84_LVBus1533444_production, 84_LVBus1533445_consumption, 84_LVBus1533445_production, 84_LVBus1533446_consumption, 84_LVBus1533446_production, 84_LVBus1533447_production, 84_LVBus1533448_consumption, 84_LVBus1533448_production, 84_LVBus1533449_consumption, 84_LVBus1533449_production, 84_LVBus1533450_production, 84_LVBus1533451_consumption, 84_LVBus1533451_production, 84_LVBus1533452_consumption, 84_LVBus1533452_production, 84_LVBus1533453_consumption, 84_LVBus1533453_production, 84_LVBus1533455_consumption, 84_LVBus1533455_production, 84_LVBus1533456_production, 84_LVBus1533457_production, 84_LVBus1533461_production, 84_LVBus1533462_production, 84_LVBus1533463_production, 84_LVBus1533464_production, 84_LVBus1533465_production, 84_LVBus1533466_production, 84_LVBus1533468_consumption, 84_LVBus1533468_production, 84_LVBus1533469_production, 84_LVBus1533472_production, 84_LVBus1533474_production, 84_LVBus1533475_production, 84_LVBus1533476_production, 84_LVBus1533477_production, 84_LVBus1533479_production, 84_LVBus1533480_consumption, 84_LVBus1533480_production, 84_LVBus1533481_production, 84_LVBus1533482_consumption, 84_LVBus1533482_production, 84_LVBus1533483_production, 84_LVBus1533485_production, 84_LVBus1533487_production, 84_LVBus1533488_production, 84_LVBus1533489_production, 84_LVBus1533491_production, 84_LVBus1533492_production, 84_LVBus1533493_production, 84_LVBus1533494_production, 84_LVBus1533495_production, 84_LVBus1533496_production, 84_LVBus1533497_production, 84_LVBus1533499_consumption, 84_LVBus1533499_production, 84_LVBus1533500_production, 84_LVBus1533501_production, 84_LVBus1533502_production, 84_LVBus1533504_consumption, 84_LVBus1533504_production, 84_LVBus1533505_consumption, 84_LVBus1533505_production, 84_LVBus1533506_production, 84_LVBus1533507_production, 84_LVBus1533508_consumption, 84_LVBus1533508_production, 84_LVBus1533509_consumption, 84_LVBus1533509_production, 84_LVBus1533510_production, 84_LVBus1533512_production, 84_LVBus1533514_consumption, 84_LVBus1533514_production, 84_LVBus1533515_production, 84_LVBus1533516_consumption, 84_LVBus1533516_production, 84_LVBus1533517_consumption, 84_LVBus1533517_production, 84_LVBus1533519_production, 84_LVBus1533520_consumption, 84_LVBus1533520_production, 84_LVBus1533521_production, 84_LVBus1533523_consumption, 84_LVBus1533523_production, 84_LVBus1533524_consumption, 84_LVBus1533524_production, 84_LVBus1533525_production, 84_LVBus1533526_consumption, 84_LVBus1533526_production, 84_LVBus1533527_consumption, 84_LVBus1533527_production, 84_LVBus1533528_consumption, 84_LVBus1533528_production, 84_LVBus1533529_consumption, 84_LVBus1533529_production, 84_LVBus1533530_production, 84_LVBus1533533_consumption, 84_LVBus1533533_production, 84_LVBus2014980_production, 84_LVBus2016519_production, 84_LVBus2044931_production, 84_LVBus2044932_production, 84_LVBus2044933_production, 84_LVBus2044934_production, 84_LVBus2044935_consumption, 84_LVBus2044935_production, 84_LVBus2044936_consumption, 84_LVBus2044936_production, 84_LVBus2044937_consumption, 84_LVBus2044937_production, 84_LVBus2044938_consumption, 84_LVBus2044938_production, 84_LVBus2044939_consumption, 84_LVBus2044939_production, 84_LVBus2044940_production, 84_LVBus2047187_production, 84_LVBus2047188_consumption, 84_LVBus2047188_production, 84_LVBus2049579_production, 84_LVBus2056802_consumption, 84_LVBus2056802_production, 84_LVBus2062936_consumption, 84_LVBus2062936_production, 84_LVBus2074610_production, 84_LVBus2143525_production, 84_LVBus2238908_production, 84_LVBus2249254_production, 84_LVBus2249255_production, 84_MVLV033374_consumption, 84_MVLV033374_production, 84_MVLV049602_consumption, 84_MVLV049602_production, 84_MVLV062262_consumption, 84_MVLV062262_production, 84_MVLV084747_consumption, 84_MVLV084747_production, 84_MVLV091136_consumption, 84_MVLV091136_production, 84_MVLV093265_consumption, 84_MVLV093265_production, 84_MVLV095645_consumption, 84_MVLV095645_production, 84_MVLV121115_consumption, 84_MVLV121115_production, 84_MVLV125712_consumption, 84_MVLV125712_production, 84_MVLV131610_consumption, 84_MVLV131610_production, 84_MVLV154489_consumption, 84_MVLV154489_production.

## 9. Data Quality Summary

**Total findings:** 324 (0 errors, 4 warnings, 320 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  791 of 1130 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.44 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  792 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533212_consumption`  
  Load '84_LVBus1533212_consumption' has phase imbalance of 72.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533296_consumption`  
  Load '84_LVBus1533296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533400_consumption`  
  Load '84_LVBus1533400_consumption' has phase imbalance of 290.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533329_consumption`  
  Load '84_LVBus1533329_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533404_consumption`  
  Load '84_LVBus1533404_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533385_consumption`  
  Load '84_LVBus1533385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533390_consumption`  
  Load '84_LVBus1533390_consumption' has phase imbalance of 271.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533219_consumption`  
  Load '84_LVBus1533219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532996_consumption`  
  Load '84_LVBus1532996_consumption' has phase imbalance of 92.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533437_consumption`  
  Load '84_LVBus1533437_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532926_consumption`  
  Load '84_LVBus1532926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533093_consumption`  
  Load '84_LVBus1533093_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532896_consumption`  
  Load '84_LVBus1532896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532940_consumption`  
  Load '84_LVBus1532940_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533002_consumption`  
  Load '84_LVBus1533002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533461_consumption`  
  Load '84_LVBus1533461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533357_consumption`  
  Load '84_LVBus1533357_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533416_consumption`  
  Load '84_LVBus1533416_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533032_consumption`  
  Load '84_LVBus1533032_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533382_consumption`  
  Load '84_LVBus1533382_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533259_consumption`  
  Load '84_LVBus1533259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533055_consumption`  
  Load '84_LVBus1533055_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532919_consumption`  
  Load '84_LVBus1532919_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533420_consumption`  
  Load '84_LVBus1533420_consumption' has phase imbalance of 155.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533419_consumption`  
  Load '84_LVBus1533419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532923_consumption`  
  Load '84_LVBus1532923_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533098_consumption`  
  Load '84_LVBus1533098_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532935_consumption`  
  Load '84_LVBus1532935_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533049_consumption`  
  Load '84_LVBus1533049_consumption' has phase imbalance of 283.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533105_consumption`  
  Load '84_LVBus1533105_consumption' has phase imbalance of 191.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532892_consumption`  
  Load '84_LVBus1532892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533510_consumption`  
  Load '84_LVBus1533510_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533398_consumption`  
  Load '84_LVBus1533398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533190_consumption`  
  Load '84_LVBus1533190_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533225_consumption`  
  Load '84_LVBus1533225_consumption' has phase imbalance of 204.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533232_consumption`  
  Load '84_LVBus1533232_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533311_consumption`  
  Load '84_LVBus1533311_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532871_consumption`  
  Load '84_LVBus1532871_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532956_consumption`  
  Load '84_LVBus1532956_consumption' has phase imbalance of 35.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2049579_consumption`  
  Load '84_LVBus2049579_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533234_consumption`  
  Load '84_LVBus1533234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533166_consumption`  
  Load '84_LVBus1533166_consumption' has phase imbalance of 220.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533383_consumption`  
  Load '84_LVBus1533383_consumption' has phase imbalance of 181.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533054_consumption`  
  Load '84_LVBus1533054_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532884_consumption`  
  Load '84_LVBus1532884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533325_consumption`  
  Load '84_LVBus1533325_consumption' has phase imbalance of 121.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533118_consumption`  
  Load '84_LVBus1533118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533366_consumption`  
  Load '84_LVBus1533366_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533023_consumption`  
  Load '84_LVBus1533023_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533340_consumption`  
  Load '84_LVBus1533340_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533040_consumption`  
  Load '84_LVBus1533040_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533200_consumption`  
  Load '84_LVBus1533200_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533258_consumption`  
  Load '84_LVBus1533258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533338_consumption`  
  Load '84_LVBus1533338_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533481_consumption`  
  Load '84_LVBus1533481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533028_consumption`  
  Load '84_LVBus1533028_consumption' has phase imbalance of 137.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532957_consumption`  
  Load '84_LVBus1532957_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533027_consumption`  
  Load '84_LVBus1533027_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532954_consumption`  
  Load '84_LVBus1532954_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533421_consumption`  
  Load '84_LVBus1533421_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533430_consumption`  
  Load '84_LVBus1533430_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533001_consumption`  
  Load '84_LVBus1533001_consumption' has phase imbalance of 197.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2016519_consumption`  
  Load '84_LVBus2016519_consumption' has phase imbalance of 159.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533488_consumption`  
  Load '84_LVBus1533488_consumption' has phase imbalance of 231.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533151_consumption`  
  Load '84_LVBus1533151_consumption' has phase imbalance of 230.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533501_consumption`  
  Load '84_LVBus1533501_consumption' has phase imbalance of 134.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532979_consumption`  
  Load '84_LVBus1532979_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533492_consumption`  
  Load '84_LVBus1533492_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532985_consumption`  
  Load '84_LVBus1532985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533487_consumption`  
  Load '84_LVBus1533487_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532866_consumption`  
  Load '84_LVBus1532866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532890_consumption`  
  Load '84_LVBus1532890_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533483_consumption`  
  Load '84_LVBus1533483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533047_consumption`  
  Load '84_LVBus1533047_consumption' has phase imbalance of 182.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532906_consumption`  
  Load '84_LVBus1532906_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532994_consumption`  
  Load '84_LVBus1532994_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533006_consumption`  
  Load '84_LVBus1533006_consumption' has phase imbalance of 267.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533507_consumption`  
  Load '84_LVBus1533507_consumption' has phase imbalance of 41.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533008_consumption`  
  Load '84_LVBus1533008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533036_consumption`  
  Load '84_LVBus1533036_consumption' has phase imbalance of 138.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2074610_consumption`  
  Load '84_LVBus2074610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532953_consumption`  
  Load '84_LVBus1532953_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532939_consumption`  
  Load '84_LVBus1532939_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2238908_consumption`  
  Load '84_LVBus2238908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532990_consumption`  
  Load '84_LVBus1532990_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533051_consumption`  
  Load '84_LVBus1533051_consumption' has phase imbalance of 187.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2044933_consumption`  
  Load '84_LVBus2044933_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533243_consumption`  
  Load '84_LVBus1533243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533349_consumption`  
  Load '84_LVBus1533349_consumption' has phase imbalance of 211.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532933_consumption`  
  Load '84_LVBus1532933_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533163_consumption`  
  Load '84_LVBus1533163_consumption' has phase imbalance of 270.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532982_consumption`  
  Load '84_LVBus1532982_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533024_consumption`  
  Load '84_LVBus1533024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533307_consumption`  
  Load '84_LVBus1533307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533048_consumption`  
  Load '84_LVBus1533048_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533039_consumption`  
  Load '84_LVBus1533039_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533057_consumption`  
  Load '84_LVBus1533057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533396_consumption`  
  Load '84_LVBus1533396_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533171_consumption`  
  Load '84_LVBus1533171_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533402_consumption`  
  Load '84_LVBus1533402_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533207_consumption`  
  Load '84_LVBus1533207_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533186_consumption`  
  Load '84_LVBus1533186_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533525_consumption`  
  Load '84_LVBus1533525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532907_consumption`  
  Load '84_LVBus1532907_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533174_consumption`  
  Load '84_LVBus1533174_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533353_consumption`  
  Load '84_LVBus1533353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533197_consumption`  
  Load '84_LVBus1533197_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533238_consumption`  
  Load '84_LVBus1533238_consumption' has phase imbalance of 284.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533399_consumption`  
  Load '84_LVBus1533399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533288_consumption`  
  Load '84_LVBus1533288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533334_consumption`  
  Load '84_LVBus1533334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533160_consumption`  
  Load '84_LVBus1533160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533360_consumption`  
  Load '84_LVBus1533360_consumption' has phase imbalance of 47.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533300_consumption`  
  Load '84_LVBus1533300_consumption' has phase imbalance of 256.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532980_consumption`  
  Load '84_LVBus1532980_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533375_consumption`  
  Load '84_LVBus1533375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2249254_consumption`  
  Load '84_LVBus2249254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533206_consumption`  
  Load '84_LVBus1533206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532947_consumption`  
  Load '84_LVBus1532947_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533491_consumption`  
  Load '84_LVBus1533491_consumption' has phase imbalance of 42.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533016_consumption`  
  Load '84_LVBus1533016_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533521_consumption`  
  Load '84_LVBus1533521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533015_consumption`  
  Load '84_LVBus1533015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533248_consumption`  
  Load '84_LVBus1533248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533391_consumption`  
  Load '84_LVBus1533391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533377_consumption`  
  Load '84_LVBus1533377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532870_consumption`  
  Load '84_LVBus1532870_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532978_consumption`  
  Load '84_LVBus1532978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533025_consumption`  
  Load '84_LVBus1533025_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533463_consumption`  
  Load '84_LVBus1533463_consumption' has phase imbalance of 273.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533244_consumption`  
  Load '84_LVBus1533244_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533485_consumption`  
  Load '84_LVBus1533485_consumption' has phase imbalance of 139.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532880_consumption`  
  Load '84_LVBus1532880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533211_consumption`  
  Load '84_LVBus1533211_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533145_consumption`  
  Load '84_LVBus1533145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532955_consumption`  
  Load '84_LVBus1532955_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533479_consumption`  
  Load '84_LVBus1533479_consumption' has phase imbalance of 267.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533083_consumption`  
  Load '84_LVBus1533083_consumption' has phase imbalance of 106.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533050_consumption`  
  Load '84_LVBus1533050_consumption' has phase imbalance of 128.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532929_consumption`  
  Load '84_LVBus1532929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533341_consumption`  
  Load '84_LVBus1533341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533450_consumption`  
  Load '84_LVBus1533450_consumption' has phase imbalance of 112.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532931_consumption`  
  Load '84_LVBus1532931_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533411_consumption`  
  Load '84_LVBus1533411_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532927_consumption`  
  Load '84_LVBus1532927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533176_consumption`  
  Load '84_LVBus1533176_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2044931_consumption`  
  Load '84_LVBus2044931_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533261_consumption`  
  Load '84_LVBus1533261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533359_consumption`  
  Load '84_LVBus1533359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533081_consumption`  
  Load '84_LVBus1533081_consumption' has phase imbalance of 212.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532889_consumption`  
  Load '84_LVBus1532889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533131_consumption`  
  Load '84_LVBus1533131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533201_consumption`  
  Load '84_LVBus1533201_consumption' has phase imbalance of 121.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533094_consumption`  
  Load '84_LVBus1533094_consumption' has phase imbalance of 191.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533289_consumption`  
  Load '84_LVBus1533289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533134_consumption`  
  Load '84_LVBus1533134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533494_consumption`  
  Load '84_LVBus1533494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533061_consumption`  
  Load '84_LVBus1533061_consumption' has phase imbalance of 205.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533127_consumption`  
  Load '84_LVBus1533127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533395_consumption`  
  Load '84_LVBus1533395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2143525_consumption`  
  Load '84_LVBus2143525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532883_consumption`  
  Load '84_LVBus1532883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532930_consumption`  
  Load '84_LVBus1532930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532938_consumption`  
  Load '84_LVBus1532938_consumption' has phase imbalance of 289.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533515_consumption`  
  Load '84_LVBus1533515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532942_consumption`  
  Load '84_LVBus1532942_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533013_consumption`  
  Load '84_LVBus1533013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532986_consumption`  
  Load '84_LVBus1532986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533253_consumption`  
  Load '84_LVBus1533253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2249255_consumption`  
  Load '84_LVBus2249255_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533263_consumption`  
  Load '84_LVBus1533263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533020_consumption`  
  Load '84_LVBus1533020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533065_consumption`  
  Load '84_LVBus1533065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532918_consumption`  
  Load '84_LVBus1532918_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532908_consumption`  
  Load '84_LVBus1532908_consumption' has phase imbalance of 44.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533462_consumption`  
  Load '84_LVBus1533462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532970_consumption`  
  Load '84_LVBus1532970_consumption' has phase imbalance of 266.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533239_consumption`  
  Load '84_LVBus1533239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533187_consumption`  
  Load '84_LVBus1533187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533342_consumption`  
  Load '84_LVBus1533342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532977_consumption`  
  Load '84_LVBus1532977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533495_consumption`  
  Load '84_LVBus1533495_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533464_consumption`  
  Load '84_LVBus1533464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533170_consumption`  
  Load '84_LVBus1533170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533210_consumption`  
  Load '84_LVBus1533210_consumption' has phase imbalance of 256.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533029_consumption`  
  Load '84_LVBus1533029_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533136_consumption`  
  Load '84_LVBus1533136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533330_consumption`  
  Load '84_LVBus1533330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533436_consumption`  
  Load '84_LVBus1533436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2044932_consumption`  
  Load '84_LVBus2044932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533502_consumption`  
  Load '84_LVBus1533502_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533111_consumption`  
  Load '84_LVBus1533111_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533370_consumption`  
  Load '84_LVBus1533370_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533352_consumption`  
  Load '84_LVBus1533352_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533347_consumption`  
  Load '84_LVBus1533347_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533497_consumption`  
  Load '84_LVBus1533497_consumption' has phase imbalance of 97.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2014980_consumption`  
  Load '84_LVBus2014980_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533432_consumption`  
  Load '84_LVBus1533432_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533306_consumption`  
  Load '84_LVBus1533306_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533348_consumption`  
  Load '84_LVBus1533348_consumption' has phase imbalance of 278.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533038_consumption`  
  Load '84_LVBus1533038_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533209_consumption`  
  Load '84_LVBus1533209_consumption' has phase imbalance of 146.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533405_consumption`  
  Load '84_LVBus1533405_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533202_consumption`  
  Load '84_LVBus1533202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533282_consumption`  
  Load '84_LVBus1533282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533230_consumption`  
  Load '84_LVBus1533230_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533182_consumption`  
  Load '84_LVBus1533182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533247_consumption`  
  Load '84_LVBus1533247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533410_consumption`  
  Load '84_LVBus1533410_consumption' has phase imbalance of 284.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532917_consumption`  
  Load '84_LVBus1532917_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533070_consumption`  
  Load '84_LVBus1533070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533165_consumption`  
  Load '84_LVBus1533165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533343_consumption`  
  Load '84_LVBus1533343_consumption' has phase imbalance of 25.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533264_consumption`  
  Load '84_LVBus1533264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2047187_consumption`  
  Load '84_LVBus2047187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533158_consumption`  
  Load '84_LVBus1533158_consumption' has phase imbalance of 62.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533059_consumption`  
  Load '84_LVBus1533059_consumption' has phase imbalance of 219.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532879_consumption`  
  Load '84_LVBus1532879_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533017_consumption`  
  Load '84_LVBus1533017_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533466_consumption`  
  Load '84_LVBus1533466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533422_consumption`  
  Load '84_LVBus1533422_consumption' has phase imbalance of 73.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533474_consumption`  
  Load '84_LVBus1533474_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533273_consumption`  
  Load '84_LVBus1533273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533035_consumption`  
  Load '84_LVBus1533035_consumption' has phase imbalance of 180.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532969_consumption`  
  Load '84_LVBus1532969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533192_consumption`  
  Load '84_LVBus1533192_consumption' has phase imbalance of 61.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533493_consumption`  
  Load '84_LVBus1533493_consumption' has phase imbalance of 120.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533031_consumption`  
  Load '84_LVBus1533031_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532967_consumption`  
  Load '84_LVBus1532967_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533519_consumption`  
  Load '84_LVBus1533519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533397_consumption`  
  Load '84_LVBus1533397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533037_consumption`  
  Load '84_LVBus1533037_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532913_consumption`  
  Load '84_LVBus1532913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533010_consumption`  
  Load '84_LVBus1533010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533413_consumption`  
  Load '84_LVBus1533413_consumption' has phase imbalance of 239.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532968_consumption`  
  Load '84_LVBus1532968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533056_consumption`  
  Load '84_LVBus1533056_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532877_consumption`  
  Load '84_LVBus1532877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533371_consumption`  
  Load '84_LVBus1533371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533185_consumption`  
  Load '84_LVBus1533185_consumption' has phase imbalance of 83.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533060_consumption`  
  Load '84_LVBus1533060_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533328_consumption`  
  Load '84_LVBus1533328_consumption' has phase imbalance of 33.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533500_consumption`  
  Load '84_LVBus1533500_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532963_consumption`  
  Load '84_LVBus1532963_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533355_consumption`  
  Load '84_LVBus1533355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533332_consumption`  
  Load '84_LVBus1533332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533053_consumption`  
  Load '84_LVBus1533053_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533103_consumption`  
  Load '84_LVBus1533103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533224_consumption`  
  Load '84_LVBus1533224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533116_consumption`  
  Load '84_LVBus1533116_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532983_consumption`  
  Load '84_LVBus1532983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533295_consumption`  
  Load '84_LVBus1533295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532912_consumption`  
  Load '84_LVBus1532912_consumption' has phase imbalance of 69.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533112_consumption`  
  Load '84_LVBus1533112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533231_consumption`  
  Load '84_LVBus1533231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533477_consumption`  
  Load '84_LVBus1533477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533058_consumption`  
  Load '84_LVBus1533058_consumption' has phase imbalance of 142.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532934_consumption`  
  Load '84_LVBus1532934_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2044940_consumption`  
  Load '84_LVBus2044940_consumption' has phase imbalance of 52.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532905_consumption`  
  Load '84_LVBus1532905_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533317_consumption`  
  Load '84_LVBus1533317_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533004_consumption`  
  Load '84_LVBus1533004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533447_consumption`  
  Load '84_LVBus1533447_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533388_consumption`  
  Load '84_LVBus1533388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533506_consumption`  
  Load '84_LVBus1533506_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532920_consumption`  
  Load '84_LVBus1532920_consumption' has phase imbalance of 237.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532893_consumption`  
  Load '84_LVBus1532893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532946_consumption`  
  Load '84_LVBus1532946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533041_consumption`  
  Load '84_LVBus1533041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533106_consumption`  
  Load '84_LVBus1533106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533356_consumption`  
  Load '84_LVBus1533356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532902_consumption`  
  Load '84_LVBus1532902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533412_consumption`  
  Load '84_LVBus1533412_consumption' has phase imbalance of 36.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532876_consumption`  
  Load '84_LVBus1532876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533304_consumption`  
  Load '84_LVBus1533304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532910_consumption`  
  Load '84_LVBus1532910_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533150_consumption`  
  Load '84_LVBus1533150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533496_consumption`  
  Load '84_LVBus1533496_consumption' has phase imbalance of 204.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533275_consumption`  
  Load '84_LVBus1533275_consumption' has phase imbalance of 58.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532944_consumption`  
  Load '84_LVBus1532944_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533203_consumption`  
  Load '84_LVBus1533203_consumption' has phase imbalance of 75.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2044934_consumption`  
  Load '84_LVBus2044934_consumption' has phase imbalance of 121.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533178_consumption`  
  Load '84_LVBus1533178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533119_consumption`  
  Load '84_LVBus1533119_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532868_consumption`  
  Load '84_LVBus1532868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1532899_consumption`  
  Load '84_LVBus1532899_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533401_consumption`  
  Load '84_LVBus1533401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533476_consumption`  
  Load '84_LVBus1533476_consumption' has phase imbalance of 263.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533387_consumption`  
  Load '84_LVBus1533387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533414_consumption`  
  Load '84_LVBus1533414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533314_consumption`  
  Load '84_LVBus1533314_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1533135_consumption`  
  Load '84_LVBus1533135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1130 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1533088' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1533512' has balanced aggregate load across 3 phase(s) (max spread 0.94%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1533455' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_SSCL5' (MV, 11.78 kV) has an electrical reach of 24.77 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533010' (LV, 0.24 kV) has an electrical reach of 20.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533101' (LV, 0.24 kV) has an electrical reach of 1.3 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533250' (LV, 0.24 kV) has an electrical reach of 1.07 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533158' (LV, 0.24 kV) has an electrical reach of 1.05 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533168' (LV, 0.24 kV) has an electrical reach of 13.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533461' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533180' (LV, 0.24 kV) has an electrical reach of 9.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533178' (LV, 0.24 kV) has an electrical reach of 11.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus1533156' (LV, 0.24 kV) has an electrical reach of 21.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  747 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  232 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus1532866_consumption, 84_LVBus1532868_consumption, 84_LVBus1532870_consumption, 84_LVBus1532871_consumption, 84_LVBus1532876_consumption, 84_LVBus1532877_consumption, 84_LVBus1532880_consumption, 84_LVBus1532883_consumption, 84_LVBus1532884_consumption, 84_LVBus1532889_consumption, 84_LVBus1532890_consumption, 84_LVBus1532892_consumption, 84_LVBus1532893_consumption, 84_LVBus1532896_consumption, 84_LVBus1532899_consumption, 84_LVBus1532902_consumption, 84_LVBus1532905_consumption, 84_LVBus1532906_consumption, 84_LVBus1532913_consumption, 84_LVBus1532917_consumption, 84_LVBus1532920_consumption, 84_LVBus1532923_consumption, 84_LVBus1532926_consumption, 84_LVBus1532927_consumption, 84_LVBus1532929_consumption, 84_LVBus1532930_consumption, 84_LVBus1532931_consumption, 84_LVBus1532933_consumption, 84_LVBus1532934_consumption, 84_LVBus1532935_consumption, 84_LVBus1532938_consumption, 84_LVBus1532940_consumption, 84_LVBus1532944_consumption, 84_LVBus1532946_consumption, 84_LVBus1532953_consumption, 84_LVBus1532954_consumption, 84_LVBus1532957_consumption, 84_LVBus1532967_consumption, 84_LVBus1532968_consumption, 84_LVBus1532969_consumption, 84_LVBus1532970_consumption, 84_LVBus1532977_consumption, 84_LVBus1532978_consumption, 84_LVBus1532979_consumption, 84_LVBus1532980_consumption, 84_LVBus1532982_consumption, 84_LVBus1532983_consumption, 84_LVBus1532985_consumption, 84_LVBus1532986_consumption, 84_LVBus1532990_consumption, 84_LVBus1532994_consumption, 84_LVBus1533001_consumption, 84_LVBus1533002_consumption, 84_LVBus1533004_consumption, 84_LVBus1533006_consumption, 84_LVBus1533008_consumption, 84_LVBus1533010_consumption, 84_LVBus1533013_consumption, 84_LVBus1533015_consumption, 84_LVBus1533016_consumption, 84_LVBus1533017_consumption, 84_LVBus1533020_consumption, 84_LVBus1533024_consumption, 84_LVBus1533025_consumption, 84_LVBus1533027_consumption, 84_LVBus1533029_consumption, 84_LVBus1533031_consumption, 84_LVBus1533037_consumption, 84_LVBus1533038_consumption, 84_LVBus1533039_consumption, 84_LVBus1533041_consumption, 84_LVBus1533047_consumption, 84_LVBus1533048_consumption, 84_LVBus1533049_consumption, 84_LVBus1533051_consumption, 84_LVBus1533053_consumption, 84_LVBus1533054_consumption, 84_LVBus1533055_consumption, 84_LVBus1533057_consumption, 84_LVBus1533059_consumption, 84_LVBus1533060_consumption, 84_LVBus1533061_consumption, 84_LVBus1533065_consumption, 84_LVBus1533070_consumption, 84_LVBus1533081_consumption, 84_LVBus1533093_consumption, 84_LVBus1533094_consumption, 84_LVBus1533098_consumption, 84_LVBus1533103_consumption, 84_LVBus1533105_consumption, 84_LVBus1533106_consumption, 84_LVBus1533111_consumption, 84_LVBus1533112_consumption, 84_LVBus1533116_consumption, 84_LVBus1533118_consumption, 84_LVBus1533119_consumption, 84_LVBus1533127_consumption, 84_LVBus1533131_consumption, 84_LVBus1533134_consumption, 84_LVBus1533135_consumption, 84_LVBus1533136_consumption, 84_LVBus1533145_consumption, 84_LVBus1533150_consumption, 84_LVBus1533151_consumption, 84_LVBus1533160_consumption, 84_LVBus1533163_consumption, 84_LVBus1533165_consumption, 84_LVBus1533166_consumption, 84_LVBus1533170_consumption, 84_LVBus1533171_consumption, 84_LVBus1533174_consumption, 84_LVBus1533176_consumption, 84_LVBus1533178_consumption, 84_LVBus1533182_consumption, 84_LVBus1533187_consumption, 84_LVBus1533190_consumption, 84_LVBus1533197_consumption, 84_LVBus1533200_consumption, 84_LVBus1533202_consumption, 84_LVBus1533206_consumption, 84_LVBus1533210_consumption, 84_LVBus1533211_consumption, 84_LVBus1533219_consumption, 84_LVBus1533224_consumption, 84_LVBus1533225_consumption, 84_LVBus1533231_consumption, 84_LVBus1533232_consumption, 84_LVBus1533234_consumption, 84_LVBus1533238_consumption, 84_LVBus1533239_consumption, 84_LVBus1533243_consumption, 84_LVBus1533244_consumption, 84_LVBus1533247_consumption, 84_LVBus1533248_consumption, 84_LVBus1533253_consumption, 84_LVBus1533258_consumption, 84_LVBus1533259_consumption, 84_LVBus1533261_consumption, 84_LVBus1533263_consumption, 84_LVBus1533264_consumption, 84_LVBus1533273_consumption, 84_LVBus1533282_consumption, 84_LVBus1533288_consumption, 84_LVBus1533289_consumption, 84_LVBus1533295_consumption, 84_LVBus1533296_consumption, 84_LVBus1533300_consumption, 84_LVBus1533304_consumption, 84_LVBus1533306_consumption, 84_LVBus1533307_consumption, 84_LVBus1533311_consumption, 84_LVBus1533314_consumption, 84_LVBus1533317_consumption, 84_LVBus1533329_consumption, 84_LVBus1533330_consumption, 84_LVBus1533332_consumption, 84_LVBus1533334_consumption, 84_LVBus1533340_consumption, 84_LVBus1533341_consumption, 84_LVBus1533342_consumption, 84_LVBus1533347_consumption, 84_LVBus1533348_consumption, 84_LVBus1533349_consumption, 84_LVBus1533352_consumption, 84_LVBus1533353_consumption, 84_LVBus1533355_consumption, 84_LVBus1533356_consumption, 84_LVBus1533357_consumption, 84_LVBus1533359_consumption, 84_LVBus1533366_consumption, 84_LVBus1533370_consumption, 84_LVBus1533371_consumption, 84_LVBus1533375_consumption, 84_LVBus1533377_consumption, 84_LVBus1533382_consumption, 84_LVBus1533383_consumption, 84_LVBus1533385_consumption, 84_LVBus1533387_consumption, 84_LVBus1533388_consumption, 84_LVBus1533390_consumption, 84_LVBus1533391_consumption, 84_LVBus1533395_consumption, 84_LVBus1533396_consumption, 84_LVBus1533397_consumption, 84_LVBus1533398_consumption, 84_LVBus1533399_consumption, 84_LVBus1533400_consumption, 84_LVBus1533401_consumption, 84_LVBus1533404_consumption, 84_LVBus1533405_consumption, 84_LVBus1533410_consumption, 84_LVBus1533411_consumption, 84_LVBus1533413_consumption, 84_LVBus1533414_consumption, 84_LVBus1533416_consumption, 84_LVBus1533419_consumption, 84_LVBus1533420_consumption, 84_LVBus1533421_consumption, 84_LVBus1533436_consumption, 84_LVBus1533437_consumption, 84_LVBus1533447_consumption, 84_LVBus1533461_consumption, 84_LVBus1533462_consumption, 84_LVBus1533464_consumption, 84_LVBus1533466_consumption, 84_LVBus1533474_consumption, 84_LVBus1533476_consumption, 84_LVBus1533477_consumption, 84_LVBus1533479_consumption, 84_LVBus1533481_consumption, 84_LVBus1533483_consumption, 84_LVBus1533487_consumption, 84_LVBus1533488_consumption, 84_LVBus1533494_consumption, 84_LVBus1533495_consumption, 84_LVBus1533496_consumption, 84_LVBus1533500_consumption, 84_LVBus1533515_consumption, 84_LVBus1533519_consumption, 84_LVBus1533521_consumption, 84_LVBus1533525_consumption, 84_LVBus2014980_consumption, 84_LVBus2044931_consumption, 84_LVBus2044932_consumption, 84_LVBus2044933_consumption, 84_LVBus2047187_consumption, 84_LVBus2049579_consumption, 84_LVBus2074610_consumption, 84_LVBus2143525_consumption, 84_LVBus2238908_consumption, 84_LVBus2249254_consumption, 84_LVBus2249255_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  565 group(s) of loads (1130 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  19 group(s) of series lines (39 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  792 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1532863_consumption, 84_LVBus1532863_production, 84_LVBus1532864_consumption, 84_LVBus1532864_production, 84_LVBus1532865_consumption, 84_LVBus1532865_production, 84_LVBus1532866_production, 84_LVBus1532867_consumption, 84_LVBus1532867_production, 84_LVBus1532868_production, 84_LVBus1532869_consumption, 84_LVBus1532869_production, 84_LVBus1532870_production, 84_LVBus1532871_production, 84_LVBus1532876_production, 84_LVBus1532877_production, 84_LVBus1532878_consumption, 84_LVBus1532878_production, 84_LVBus1532879_production, 84_LVBus1532880_production, 84_LVBus1532881_consumption, 84_LVBus1532881_production, 84_LVBus1532882_consumption, 84_LVBus1532882_production, 84_LVBus1532883_production, 84_LVBus1532884_production, 84_LVBus1532886_consumption, 84_LVBus1532886_production, 84_LVBus1532888_consumption, 84_LVBus1532888_production, 84_LVBus1532889_production, 84_LVBus1532890_production, 84_LVBus1532891_consumption, 84_LVBus1532891_production, 84_LVBus1532892_production, 84_LVBus1532893_production, 84_LVBus1532894_consumption, 84_LVBus1532894_production, 84_LVBus1532895_consumption, 84_LVBus1532895_production, 84_LVBus1532896_production, 84_LVBus1532897_consumption, 84_LVBus1532897_production, 84_LVBus1532898_consumption, 84_LVBus1532898_production, 84_LVBus1532899_production, 84_LVBus1532901_consumption, 84_LVBus1532901_production, 84_LVBus1532902_production, 84_LVBus1532904_consumption, 84_LVBus1532904_production, 84_LVBus1532905_production, 84_LVBus1532906_production, 84_LVBus1532907_production, 84_LVBus1532908_production, 84_LVBus1532909_consumption, 84_LVBus1532909_production, 84_LVBus1532910_production, 84_LVBus1532911_production, 84_LVBus1532912_production, 84_LVBus1532913_production, 84_LVBus1532914_consumption, 84_LVBus1532914_production, 84_LVBus1532916_consumption, 84_LVBus1532916_production, 84_LVBus1532917_production, 84_LVBus1532918_production, 84_LVBus1532919_production, 84_LVBus1532920_production, 84_LVBus1532921_production, 84_LVBus1532922_production, 84_LVBus1532923_production, 84_LVBus1532924_production, 84_LVBus1532926_production, 84_LVBus1532927_production, 84_LVBus1532928_consumption, 84_LVBus1532928_production, 84_LVBus1532929_production, 84_LVBus1532930_production, 84_LVBus1532931_production, 84_LVBus1532932_consumption, 84_LVBus1532932_production, 84_LVBus1532933_production, 84_LVBus1532934_production, 84_LVBus1532935_production, 84_LVBus1532937_production, 84_LVBus1532938_production, 84_LVBus1532939_production, 84_LVBus1532940_production, 84_LVBus1532941_production, 84_LVBus1532942_production, 84_LVBus1532943_consumption, 84_LVBus1532943_production, 84_LVBus1532944_production, 84_LVBus1532946_production, 84_LVBus1532947_production, 84_LVBus1532949_consumption, 84_LVBus1532949_production, 84_LVBus1532950_production, 84_LVBus1532951_consumption, 84_LVBus1532951_production, 84_LVBus1532952_consumption, 84_LVBus1532952_production, 84_LVBus1532953_production, 84_LVBus1532954_production, 84_LVBus1532955_production, 84_LVBus1532956_production, 84_LVBus1532957_production, 84_LVBus1532961_production, 84_LVBus1532963_production, 84_LVBus1532965_production, 84_LVBus1532967_production, 84_LVBus1532968_production, 84_LVBus1532969_production, 84_LVBus1532970_production, 84_LVBus1532973_consumption, 84_LVBus1532973_production, 84_LVBus1532976_consumption, 84_LVBus1532976_production, 84_LVBus1532977_production, 84_LVBus1532978_production, 84_LVBus1532979_production, 84_LVBus1532980_production, 84_LVBus1532981_consumption, 84_LVBus1532981_production, 84_LVBus1532982_production, 84_LVBus1532983_production, 84_LVBus1532985_production, 84_LVBus1532986_production, 84_LVBus1532987_consumption, 84_LVBus1532987_production, 84_LVBus1532988_consumption, 84_LVBus1532988_production, 84_LVBus1532989_consumption, 84_LVBus1532989_production, 84_LVBus1532990_production, 84_LVBus1532992_consumption, 84_LVBus1532992_production, 84_LVBus1532994_production, 84_LVBus1532996_production, 84_LVBus1532998_consumption, 84_LVBus1532998_production, 84_LVBus1532999_consumption, 84_LVBus1532999_production, 84_LVBus1533000_consumption, 84_LVBus1533000_production, 84_LVBus1533001_production, 84_LVBus1533002_production, 84_LVBus1533004_production, 84_LVBus1533005_production, 84_LVBus1533006_production, 84_LVBus1533008_production, 84_LVBus1533010_production, 84_LVBus1533012_consumption, 84_LVBus1533012_production, 84_LVBus1533013_production, 84_LVBus1533015_production, 84_LVBus1533016_production, 84_LVBus1533017_production, 84_LVBus1533018_consumption, 84_LVBus1533018_production, 84_LVBus1533019_consumption, 84_LVBus1533019_production, 84_LVBus1533020_production, 84_LVBus1533023_production, 84_LVBus1533024_production, 84_LVBus1533025_production, 84_LVBus1533027_production, 84_LVBus1533028_production, 84_LVBus1533029_production, 84_LVBus1533031_production, 84_LVBus1533032_production, 84_LVBus1533034_consumption, 84_LVBus1533034_production, 84_LVBus1533035_production, 84_LVBus1533036_production, 84_LVBus1533037_production, 84_LVBus1533038_production, 84_LVBus1533039_production, 84_LVBus1533040_production, 84_LVBus1533041_production, 84_LVBus1533043_consumption, 84_LVBus1533043_production, 84_LVBus1533044_consumption, 84_LVBus1533044_production, 84_LVBus1533045_production, 84_LVBus1533047_production, 84_LVBus1533048_production, 84_LVBus1533049_production, 84_LVBus1533050_production, 84_LVBus1533051_production, 84_LVBus1533053_production, 84_LVBus1533054_production, 84_LVBus1533055_production, 84_LVBus1533056_production, 84_LVBus1533057_production, 84_LVBus1533058_production, 84_LVBus1533059_production, 84_LVBus1533060_production, 84_LVBus1533061_production, 84_LVBus1533064_consumption, 84_LVBus1533064_production, 84_LVBus1533065_production, 84_LVBus1533066_consumption, 84_LVBus1533066_production, 84_LVBus1533067_consumption, 84_LVBus1533067_production, 84_LVBus1533069_production, 84_LVBus1533070_production, 84_LVBus1533071_consumption, 84_LVBus1533071_production, 84_LVBus1533072_consumption, 84_LVBus1533072_production, 84_LVBus1533073_production, 84_LVBus1533075_production, 84_LVBus1533076_production, 84_LVBus1533077_consumption, 84_LVBus1533077_production, 84_LVBus1533079_production, 84_LVBus1533080_consumption, 84_LVBus1533080_production, 84_LVBus1533081_production, 84_LVBus1533082_consumption, 84_LVBus1533082_production, 84_LVBus1533083_production, 84_LVBus1533084_consumption, 84_LVBus1533084_production, 84_LVBus1533085_production, 84_LVBus1533086_consumption, 84_LVBus1533086_production, 84_LVBus1533088_consumption, 84_LVBus1533088_production, 84_LVBus1533089_consumption, 84_LVBus1533089_production, 84_LVBus1533090_production, 84_LVBus1533091_consumption, 84_LVBus1533091_production, 84_LVBus1533093_production, 84_LVBus1533094_production, 84_LVBus1533095_consumption, 84_LVBus1533095_production, 84_LVBus1533097_consumption, 84_LVBus1533097_production, 84_LVBus1533098_production, 84_LVBus1533101_consumption, 84_LVBus1533101_production, 84_LVBus1533102_consumption, 84_LVBus1533102_production, 84_LVBus1533103_production, 84_LVBus1533104_consumption, 84_LVBus1533104_production, 84_LVBus1533105_production, 84_LVBus1533106_production, 84_LVBus1533107_consumption, 84_LVBus1533107_production, 84_LVBus1533109_consumption, 84_LVBus1533109_production, 84_LVBus1533110_consumption, 84_LVBus1533110_production, 84_LVBus1533111_production, 84_LVBus1533112_production, 84_LVBus1533113_consumption, 84_LVBus1533113_production, 84_LVBus1533115_consumption, 84_LVBus1533115_production, 84_LVBus1533116_production, 84_LVBus1533117_production, 84_LVBus1533118_production, 84_LVBus1533119_production, 84_LVBus1533125_consumption, 84_LVBus1533125_production, 84_LVBus1533126_consumption, 84_LVBus1533126_production, 84_LVBus1533127_production, 84_LVBus1533128_consumption, 84_LVBus1533128_production, 84_LVBus1533129_consumption, 84_LVBus1533129_production, 84_LVBus1533130_consumption, 84_LVBus1533130_production, 84_LVBus1533131_production, 84_LVBus1533132_consumption, 84_LVBus1533132_production, 84_LVBus1533133_consumption, 84_LVBus1533133_production, 84_LVBus1533134_production, 84_LVBus1533135_production, 84_LVBus1533136_production, 84_LVBus1533139_consumption, 84_LVBus1533139_production, 84_LVBus1533140_production, 84_LVBus1533141_consumption, 84_LVBus1533141_production, 84_LVBus1533142_consumption, 84_LVBus1533142_production, 84_LVBus1533143_consumption, 84_LVBus1533143_production, 84_LVBus1533144_consumption, 84_LVBus1533144_production, 84_LVBus1533145_production, 84_LVBus1533146_consumption, 84_LVBus1533146_production, 84_LVBus1533147_consumption, 84_LVBus1533147_production, 84_LVBus1533149_consumption, 84_LVBus1533149_production, 84_LVBus1533150_production, 84_LVBus1533151_production, 84_LVBus1533152_consumption, 84_LVBus1533152_production, 84_LVBus1533156_consumption, 84_LVBus1533156_production, 84_LVBus1533158_production, 84_LVBus1533160_production, 84_LVBus1533162_consumption, 84_LVBus1533162_production, 84_LVBus1533163_production, 84_LVBus1533164_consumption, 84_LVBus1533164_production, 84_LVBus1533165_production, 84_LVBus1533166_production, 84_LVBus1533168_consumption, 84_LVBus1533168_production, 84_LVBus1533170_production, 84_LVBus1533171_production, 84_LVBus1533173_consumption, 84_LVBus1533173_production, 84_LVBus1533174_production, 84_LVBus1533175_consumption, 84_LVBus1533175_production, 84_LVBus1533176_production, 84_LVBus1533178_production, 84_LVBus1533180_consumption, 84_LVBus1533180_production, 84_LVBus1533182_production, 84_LVBus1533183_production, 84_LVBus1533184_production, 84_LVBus1533185_production, 84_LVBus1533186_production, 84_LVBus1533187_production, 84_LVBus1533188_production, 84_LVBus1533190_production, 84_LVBus1533191_consumption, 84_LVBus1533191_production, 84_LVBus1533192_production, 84_LVBus1533193_production, 84_LVBus1533194_consumption, 84_LVBus1533194_production, 84_LVBus1533196_consumption, 84_LVBus1533196_production, 84_LVBus1533197_production, 84_LVBus1533198_consumption, 84_LVBus1533198_production, 84_LVBus1533199_consumption, 84_LVBus1533199_production, 84_LVBus1533200_production, 84_LVBus1533201_production, 84_LVBus1533202_production, 84_LVBus1533203_production, 84_LVBus1533204_consumption, 84_LVBus1533204_production, 84_LVBus1533205_production, 84_LVBus1533206_production, 84_LVBus1533207_production, 84_LVBus1533208_production, 84_LVBus1533209_production, 84_LVBus1533210_production, 84_LVBus1533211_production, 84_LVBus1533212_production, 84_LVBus1533214_consumption, 84_LVBus1533214_production, 84_LVBus1533217_consumption, 84_LVBus1533217_production, 84_LVBus1533218_consumption, 84_LVBus1533218_production, 84_LVBus1533219_production, 84_LVBus1533220_consumption, 84_LVBus1533220_production, 84_LVBus1533221_production, 84_LVBus1533222_consumption, 84_LVBus1533222_production, 84_LVBus1533223_consumption, 84_LVBus1533223_production, 84_LVBus1533224_production, 84_LVBus1533225_production, 84_LVBus1533229_consumption, 84_LVBus1533229_production, 84_LVBus1533230_production, 84_LVBus1533231_production, 84_LVBus1533232_production, 84_LVBus1533233_consumption, 84_LVBus1533233_production, 84_LVBus1533234_production, 84_LVBus1533235_consumption, 84_LVBus1533235_production, 84_LVBus1533236_consumption, 84_LVBus1533236_production, 84_LVBus1533237_production, 84_LVBus1533238_production, 84_LVBus1533239_production, 84_LVBus1533241_consumption, 84_LVBus1533241_production, 84_LVBus1533242_consumption, 84_LVBus1533242_production, 84_LVBus1533243_production, 84_LVBus1533244_production, 84_LVBus1533245_consumption, 84_LVBus1533245_production, 84_LVBus1533246_consumption, 84_LVBus1533246_production, 84_LVBus1533247_production, 84_LVBus1533248_production, 84_LVBus1533250_consumption, 84_LVBus1533250_production, 84_LVBus1533251_consumption, 84_LVBus1533251_production, 84_LVBus1533252_consumption, 84_LVBus1533252_production, 84_LVBus1533253_production, 84_LVBus1533254_consumption, 84_LVBus1533254_production, 84_LVBus1533255_consumption, 84_LVBus1533255_production, 84_LVBus1533256_consumption, 84_LVBus1533256_production, 84_LVBus1533257_consumption, 84_LVBus1533257_production, 84_LVBus1533258_production, 84_LVBus1533259_production, 84_LVBus1533260_consumption, 84_LVBus1533260_production, 84_LVBus1533261_production, 84_LVBus1533262_consumption, 84_LVBus1533262_production, 84_LVBus1533263_production, 84_LVBus1533264_production, 84_LVBus1533267_production, 84_LVBus1533269_consumption, 84_LVBus1533269_production, 84_LVBus1533270_consumption, 84_LVBus1533270_production, 84_LVBus1533271_consumption, 84_LVBus1533271_production, 84_LVBus1533272_consumption, 84_LVBus1533272_production, 84_LVBus1533273_production, 84_LVBus1533274_consumption, 84_LVBus1533274_production, 84_LVBus1533275_production, 84_LVBus1533276_consumption, 84_LVBus1533276_production, 84_LVBus1533278_consumption, 84_LVBus1533278_production, 84_LVBus1533280_consumption, 84_LVBus1533280_production, 84_LVBus1533282_production, 84_LVBus1533283_consumption, 84_LVBus1533283_production, 84_LVBus1533285_consumption, 84_LVBus1533285_production, 84_LVBus1533286_consumption, 84_LVBus1533286_production, 84_LVBus1533287_consumption, 84_LVBus1533287_production, 84_LVBus1533288_production, 84_LVBus1533289_production, 84_LVBus1533291_consumption, 84_LVBus1533291_production, 84_LVBus1533292_consumption, 84_LVBus1533292_production, 84_LVBus1533293_consumption, 84_LVBus1533293_production, 84_LVBus1533294_consumption, 84_LVBus1533294_production, 84_LVBus1533295_production, 84_LVBus1533296_production, 84_LVBus1533297_consumption, 84_LVBus1533297_production, 84_LVBus1533298_consumption, 84_LVBus1533298_production, 84_LVBus1533299_consumption, 84_LVBus1533299_production, 84_LVBus1533300_production, 84_LVBus1533301_consumption, 84_LVBus1533301_production, 84_LVBus1533302_consumption, 84_LVBus1533302_production, 84_LVBus1533303_consumption, 84_LVBus1533303_production, 84_LVBus1533304_production, 84_LVBus1533305_consumption, 84_LVBus1533305_production, 84_LVBus1533306_production, 84_LVBus1533307_production, 84_LVBus1533309_consumption, 84_LVBus1533309_production, 84_LVBus1533310_consumption, 84_LVBus1533310_production, 84_LVBus1533311_production, 84_LVBus1533312_consumption, 84_LVBus1533312_production, 84_LVBus1533313_consumption, 84_LVBus1533313_production, 84_LVBus1533314_production, 84_LVBus1533315_consumption, 84_LVBus1533315_production, 84_LVBus1533317_production, 84_LVBus1533319_production, 84_LVBus1533324_consumption, 84_LVBus1533324_production, 84_LVBus1533325_production, 84_LVBus1533327_consumption, 84_LVBus1533327_production, 84_LVBus1533328_production, 84_LVBus1533329_production, 84_LVBus1533330_production, 84_LVBus1533331_production, 84_LVBus1533332_production, 84_LVBus1533333_consumption, 84_LVBus1533333_production, 84_LVBus1533334_production, 84_LVBus1533335_consumption, 84_LVBus1533335_production, 84_LVBus1533336_consumption, 84_LVBus1533336_production, 84_LVBus1533338_production, 84_LVBus1533339_production, 84_LVBus1533340_production, 84_LVBus1533341_production, 84_LVBus1533342_production, 84_LVBus1533343_production, 84_LVBus1533344_consumption, 84_LVBus1533344_production, 84_LVBus1533345_consumption, 84_LVBus1533345_production, 84_LVBus1533346_consumption, 84_LVBus1533346_production, 84_LVBus1533347_production, 84_LVBus1533348_production, 84_LVBus1533349_production, 84_LVBus1533351_consumption, 84_LVBus1533351_production, 84_LVBus1533352_production, 84_LVBus1533353_production, 84_LVBus1533355_production, 84_LVBus1533356_production, 84_LVBus1533357_production, 84_LVBus1533358_consumption, 84_LVBus1533358_production, 84_LVBus1533359_production, 84_LVBus1533360_production, 84_LVBus1533364_consumption, 84_LVBus1533364_production, 84_LVBus1533365_consumption, 84_LVBus1533365_production, 84_LVBus1533366_production, 84_LVBus1533368_consumption, 84_LVBus1533368_production, 84_LVBus1533369_consumption, 84_LVBus1533369_production, 84_LVBus1533370_production, 84_LVBus1533371_production, 84_LVBus1533374_consumption, 84_LVBus1533374_production, 84_LVBus1533375_production, 84_LVBus1533376_consumption, 84_LVBus1533376_production, 84_LVBus1533377_production, 84_LVBus1533378_consumption, 84_LVBus1533378_production, 84_LVBus1533379_consumption, 84_LVBus1533379_production, 84_LVBus1533380_consumption, 84_LVBus1533380_production, 84_LVBus1533382_production, 84_LVBus1533383_production, 84_LVBus1533384_production, 84_LVBus1533385_production, 84_LVBus1533386_consumption, 84_LVBus1533386_production, 84_LVBus1533387_production, 84_LVBus1533388_production, 84_LVBus1533389_consumption, 84_LVBus1533389_production, 84_LVBus1533390_production, 84_LVBus1533391_production, 84_LVBus1533395_production, 84_LVBus1533396_production, 84_LVBus1533397_production, 84_LVBus1533398_production, 84_LVBus1533399_production, 84_LVBus1533400_production, 84_LVBus1533401_production, 84_LVBus1533402_production, 84_LVBus1533403_production, 84_LVBus1533404_production, 84_LVBus1533405_production, 84_LVBus1533408_consumption, 84_LVBus1533408_production, 84_LVBus1533409_consumption, 84_LVBus1533409_production, 84_LVBus1533410_production, 84_LVBus1533411_production, 84_LVBus1533412_production, 84_LVBus1533413_production, 84_LVBus1533414_production, 84_LVBus1533416_production, 84_LVBus1533417_consumption, 84_LVBus1533417_production, 84_LVBus1533418_consumption, 84_LVBus1533418_production, 84_LVBus1533419_production, 84_LVBus1533420_production, 84_LVBus1533421_production, 84_LVBus1533422_production, 84_LVBus1533424_production, 84_LVBus1533426_production, 84_LVBus1533427_consumption, 84_LVBus1533427_production, 84_LVBus1533428_production, 84_LVBus1533429_consumption, 84_LVBus1533429_production, 84_LVBus1533430_production, 84_LVBus1533432_production, 84_LVBus1533434_consumption, 84_LVBus1533434_production, 84_LVBus1533435_consumption, 84_LVBus1533435_production, 84_LVBus1533436_production, 84_LVBus1533437_production, 84_LVBus1533438_consumption, 84_LVBus1533438_production, 84_LVBus1533439_consumption, 84_LVBus1533439_production, 84_LVBus1533440_consumption, 84_LVBus1533440_production, 84_LVBus1533441_consumption, 84_LVBus1533441_production, 84_LVBus1533442_consumption, 84_LVBus1533442_production, 84_LVBus1533443_consumption, 84_LVBus1533443_production, 84_LVBus1533444_consumption, 84_LVBus1533444_production, 84_LVBus1533445_consumption, 84_LVBus1533445_production, 84_LVBus1533446_consumption, 84_LVBus1533446_production, 84_LVBus1533447_production, 84_LVBus1533448_consumption, 84_LVBus1533448_production, 84_LVBus1533449_consumption, 84_LVBus1533449_production, 84_LVBus1533450_production, 84_LVBus1533451_consumption, 84_LVBus1533451_production, 84_LVBus1533452_consumption, 84_LVBus1533452_production, 84_LVBus1533453_consumption, 84_LVBus1533453_production, 84_LVBus1533455_consumption, 84_LVBus1533455_production, 84_LVBus1533456_production, 84_LVBus1533457_production, 84_LVBus1533461_production, 84_LVBus1533462_production, 84_LVBus1533463_production, 84_LVBus1533464_production, 84_LVBus1533465_production, 84_LVBus1533466_production, 84_LVBus1533468_consumption, 84_LVBus1533468_production, 84_LVBus1533469_production, 84_LVBus1533472_production, 84_LVBus1533474_production, 84_LVBus1533475_production, 84_LVBus1533476_production, 84_LVBus1533477_production, 84_LVBus1533479_production, 84_LVBus1533480_consumption, 84_LVBus1533480_production, 84_LVBus1533481_production, 84_LVBus1533482_consumption, 84_LVBus1533482_production, 84_LVBus1533483_production, 84_LVBus1533485_production, 84_LVBus1533487_production, 84_LVBus1533488_production, 84_LVBus1533489_production, 84_LVBus1533491_production, 84_LVBus1533492_production, 84_LVBus1533493_production, 84_LVBus1533494_production, 84_LVBus1533495_production, 84_LVBus1533496_production, 84_LVBus1533497_production, 84_LVBus1533499_consumption, 84_LVBus1533499_production, 84_LVBus1533500_production, 84_LVBus1533501_production, 84_LVBus1533502_production, 84_LVBus1533504_consumption, 84_LVBus1533504_production, 84_LVBus1533505_consumption, 84_LVBus1533505_production, 84_LVBus1533506_production, 84_LVBus1533507_production, 84_LVBus1533508_consumption, 84_LVBus1533508_production, 84_LVBus1533509_consumption, 84_LVBus1533509_production, 84_LVBus1533510_production, 84_LVBus1533512_production, 84_LVBus1533514_consumption, 84_LVBus1533514_production, 84_LVBus1533515_production, 84_LVBus1533516_consumption, 84_LVBus1533516_production, 84_LVBus1533517_consumption, 84_LVBus1533517_production, 84_LVBus1533519_production, 84_LVBus1533520_consumption, 84_LVBus1533520_production, 84_LVBus1533521_production, 84_LVBus1533523_consumption, 84_LVBus1533523_production, 84_LVBus1533524_consumption, 84_LVBus1533524_production, 84_LVBus1533525_production, 84_LVBus1533526_consumption, 84_LVBus1533526_production, 84_LVBus1533527_consumption, 84_LVBus1533527_production, 84_LVBus1533528_consumption, 84_LVBus1533528_production, 84_LVBus1533529_consumption, 84_LVBus1533529_production, 84_LVBus1533530_production, 84_LVBus1533533_consumption, 84_LVBus1533533_production, 84_LVBus2014980_production, 84_LVBus2016519_production, 84_LVBus2044931_production, 84_LVBus2044932_production, 84_LVBus2044933_production, 84_LVBus2044934_production, 84_LVBus2044935_consumption, 84_LVBus2044935_production, 84_LVBus2044936_consumption, 84_LVBus2044936_production, 84_LVBus2044937_consumption, 84_LVBus2044937_production, 84_LVBus2044938_consumption, 84_LVBus2044938_production, 84_LVBus2044939_consumption, 84_LVBus2044939_production, 84_LVBus2044940_production, 84_LVBus2047187_production, 84_LVBus2047188_consumption, 84_LVBus2047188_production, 84_LVBus2049579_production, 84_LVBus2056802_consumption, 84_LVBus2056802_production, 84_LVBus2062936_consumption, 84_LVBus2062936_production, 84_LVBus2074610_production, 84_LVBus2143525_production, 84_LVBus2238908_production, 84_LVBus2249254_production, 84_LVBus2249255_production, 84_MVLV033374_consumption, 84_MVLV033374_production, 84_MVLV049602_consumption, 84_MVLV049602_production, 84_MVLV062262_consumption, 84_MVLV062262_production, 84_MVLV084747_consumption, 84_MVLV084747_production, 84_MVLV091136_consumption, 84_MVLV091136_production, 84_MVLV093265_consumption, 84_MVLV093265_production, 84_MVLV095645_consumption, 84_MVLV095645_production, 84_MVLV121115_consumption, 84_MVLV121115_production, 84_MVLV125712_consumption, 84_MVLV125712_production, 84_MVLV131610_consumption, 84_MVLV131610_production, 84_MVLV154489_consumption, 84_MVLV154489_production.

