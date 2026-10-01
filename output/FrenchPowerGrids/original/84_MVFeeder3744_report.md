# BMOPF Network Summary: 84_MVFeeder3744

**Generated:** 2026-10-01 23:34:45  
**Findings:** 0 errors · 5 warnings · 159 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 24 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 348 |  |
| line | 323 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 594 | 3.333 MW, 999.8 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 24 |  |
| switch | 0 |  |
| transformer | 24 | Dyn11×24 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 30 | 29 | 6 | 0 |
| LV_236V | 236.0 V | 318 | 294 | 588 | 0 |

**Transformer transitions:**

- `84_MVLV021262_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV037894_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV055819_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV157593_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV065248_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV114776_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV079196_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV080021_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV006260_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV147270_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV148715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV079132_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV054961_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV149045_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV152966_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV000846_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV019210_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV150288_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115539_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV104873_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV095411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV022335_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV104285_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 11 |
| Degree-1 buses | 163 |
| Tree depth (max hops) | 30 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 348 | 1 | 347 | 0 | 0 | 0 |
| Tier LV_236V | 318 | 24 | 294 | 0 | 0 | 0 |
| Tier MV_11.8kV | 30 | 1 | 29 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 24; skipped invalid branches: 0.

Galvanic zones: 25; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MVBus092597 | MV_11.8kV | 30 | 0 | 0 | 24 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1362 declared bus terminals; 1263 mapped line/closed-switch conductor edges; 99 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 81300.0 | 3.425 | 1782 |
| q_nom | 0.0 | 24400.0 | 3.425 | 1782 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.52 | 2560.0 | 2.016 | 323 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 2.2e6 | 0.818 | 24 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 423 of 594 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319407_consumption' has phase imbalance of 124.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090790_consumption' has phase imbalance of 211.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319362_consumption' has phase imbalance of 46.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2144653_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319258_consumption' has phase imbalance of 73.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319453_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319150_consumption' has phase imbalance of 72.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2192004_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319199_consumption' has phase imbalance of 67.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319405_consumption' has phase imbalance of 71.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319277_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319203_consumption' has phase imbalance of 37.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319228_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319238_consumption' has phase imbalance of 90.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319221_consumption' has phase imbalance of 30.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319410_consumption' has phase imbalance of 42.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319233_consumption' has phase imbalance of 248.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319302_consumption' has phase imbalance of 22.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319422_consumption' has phase imbalance of 231.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319517_consumption' has phase imbalance of 24.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2144652_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319132_consumption' has phase imbalance of 40.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319267_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319351_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319209_consumption' has phase imbalance of 86.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319205_consumption' has phase imbalance of 94.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319180_consumption' has phase imbalance of 230.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319413_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319433_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319382_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319215_consumption' has phase imbalance of 55.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090787_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319232_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319315_consumption' has phase imbalance of 72.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319133_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319435_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319408_consumption' has phase imbalance of 40.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319259_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319426_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319417_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319498_consumption' has phase imbalance of 53.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090791_consumption' has phase imbalance of 51.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319378_consumption' has phase imbalance of 85.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2086353_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319301_consumption' has phase imbalance of 40.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319355_consumption' has phase imbalance of 33.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319388_consumption' has phase imbalance of 64.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319293_consumption' has phase imbalance of 42.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2086354_consumption' has phase imbalance of 25.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319359_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319434_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319354_consumption' has phase imbalance of 233.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319443_consumption' has phase imbalance of 136.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319225_consumption' has phase imbalance of 55.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319295_consumption' has phase imbalance of 52.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319178_consumption' has phase imbalance of 121.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319402_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319128_consumption' has phase imbalance of 50.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319384_consumption' has phase imbalance of 90.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319250_consumption' has phase imbalance of 116.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319356_consumption' has phase imbalance of 56.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319403_consumption' has phase imbalance of 116.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319201_consumption' has phase imbalance of 63.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319248_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319235_consumption' has phase imbalance of 120.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319440_consumption' has phase imbalance of 128.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319412_consumption' has phase imbalance of 217.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319431_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090788_consumption' has phase imbalance of 89.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319176_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319337_consumption' has phase imbalance of 52.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319328_consumption' has phase imbalance of 20.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319196_consumption' has phase imbalance of 29.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319483_consumption' has phase imbalance of 62.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319122_consumption' has phase imbalance of 124.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319419_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319424_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319125_consumption' has phase imbalance of 64.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319264_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319266_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319297_consumption' has phase imbalance of 45.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319375_consumption' has phase imbalance of 87.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319415_consumption' has phase imbalance of 125.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319310_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319420_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319469_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319421_consumption' has phase imbalance of 58.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319174_consumption' has phase imbalance of 174.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319427_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319409_consumption' has phase imbalance of 49.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319280_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319471_consumption' has phase imbalance of 51.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319191_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319399_consumption' has phase imbalance of 58.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319352_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319490_consumption' has phase imbalance of 102.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319357_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2090786_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319230_consumption' has phase imbalance of 130.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319300_consumption' has phase imbalance of 36.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319331_consumption' has phase imbalance of 26.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319294_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319154_consumption' has phase imbalance of 96.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319320_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319229_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319479_consumption' has phase imbalance of 52.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319223_consumption' has phase imbalance of 59.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166677_consumption' has phase imbalance of 50.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319436_consumption' has phase imbalance of 294.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319464_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319131_consumption' has phase imbalance of 87.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319211_consumption' has phase imbalance of 95.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319383_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319249_consumption' has phase imbalance of 202.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166678_consumption' has phase imbalance of 101.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319185_consumption' has phase imbalance of 26.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319418_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319437_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319257_consumption' has phase imbalance of 69.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1319317_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 594 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_SSGE7' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1319269' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1319156' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.333 MW |
| Total load Q | 999.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV021262_Transformer | 275.0 kVA | 22.6% |
| 84_MVLV115483_Transformer | 1.1 MVA | 29.9% |
| 84_MVLV037894_Transformer | 275.0 kVA | 29.6% |
| 84_MVLV055819_Transformer | 275.0 kVA | 32.3% |
| 84_MVLV157593_Transformer | 176.0 kVA | 38.8% |
| 84_MVLV065248_Transformer | 275.0 kVA | 11.6% |
| 84_MVLV114776_Transformer | 275.0 kVA | 10.1% |
| 84_MVLV079196_Transformer | 693.0 kVA | 22.6% |
| 84_MVLV080021_Transformer | 693.0 kVA | 22.6% |
| 84_MVLV006260_Transformer | 440.0 kVA | 15.2% |
| 84_MVLV147270_Transformer | 693.0 kVA | 36.3% |
| 84_MVLV148715_Transformer | 693.0 kVA | 13.2% |
| 84_MVLV079132_Transformer | 440.0 kVA | 28.1% |
| 84_MVLV054961_Transformer | 440.0 kVA | 45.0% |
| 84_MVLV149045_Transformer | 440.0 kVA | 41.9% |
| 84_MVLV152966_Transformer | 275.0 kVA | 17.1% |
| 84_MVLV000846_Transformer | 440.0 kVA | 35.3% |
| 84_MVLV019210_Transformer | 275.0 kVA | 14.2% |
| 84_MVLV150288_Transformer | 275.0 kVA | 20.4% |
| 84_MVLV115539_Transformer | 2.2 MVA | 18.3% |
| 84_MVLV104873_Transformer | 275.0 kVA | 51.3% |
| 84_MVLV095411_Transformer | 275.0 kVA | 17.8% |
| 84_MVLV022335_Transformer | 693.0 kVA | 30.4% |
| 84_MVLV104285_Transformer | 440.0 kVA | 26.8% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.33 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus1319494' (LV, 0.24 kV) has an electrical reach of 5.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

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

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 24 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 30 |
| LV_236V | 4-wire | 318 / 318 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 318 |
| Neutral branches | 294 |
| Grounding points | 24 |
| Neutral sections | 24 |
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
| 11.78 kV | 30 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 25 |
| Islands without voltage reference | 0 |
| Line impedance spread | 713.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 318 / 30 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 424 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 424 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1319119_consumption, 84_LVBus1319119_production, 84_LVBus1319120_consumption, 84_LVBus1319120_production, 84_LVBus1319121_consumption, 84_LVBus1319121_production, 84_LVBus1319122_production, 84_LVBus1319123_consumption, 84_LVBus1319123_production, 84_LVBus1319125_production, 84_LVBus1319126_consumption, 84_LVBus1319126_production, 84_LVBus1319127_consumption, 84_LVBus1319127_production, 84_LVBus1319128_production, 84_LVBus1319130_consumption, 84_LVBus1319130_production, 84_LVBus1319131_production, 84_LVBus1319132_production, 84_LVBus1319133_production, 84_LVBus1319135_production, 84_LVBus1319137_production, 84_LVBus1319139_consumption, 84_LVBus1319139_production, 84_LVBus1319141_consumption, 84_LVBus1319141_production, 84_LVBus1319143_consumption, 84_LVBus1319143_production, 84_LVBus1319145_consumption, 84_LVBus1319145_production, 84_LVBus1319147_consumption, 84_LVBus1319147_production, 84_LVBus1319149_consumption, 84_LVBus1319149_production, 84_LVBus1319150_production, 84_LVBus1319151_consumption, 84_LVBus1319151_production, 84_LVBus1319152_consumption, 84_LVBus1319152_production, 84_LVBus1319154_production, 84_LVBus1319156_production, 84_LVBus1319158_production, 84_LVBus1319160_production, 84_LVBus1319162_consumption, 84_LVBus1319162_production, 84_LVBus1319164_consumption, 84_LVBus1319164_production, 84_LVBus1319166_consumption, 84_LVBus1319166_production, 84_LVBus1319168_production, 84_LVBus1319170_consumption, 84_LVBus1319170_production, 84_LVBus1319172_consumption, 84_LVBus1319172_production, 84_LVBus1319174_production, 84_LVBus1319176_production, 84_LVBus1319178_production, 84_LVBus1319180_production, 84_LVBus1319182_consumption, 84_LVBus1319182_production, 84_LVBus1319183_consumption, 84_LVBus1319183_production, 84_LVBus1319185_production, 84_LVBus1319187_consumption, 84_LVBus1319187_production, 84_LVBus1319188_production, 84_LVBus1319189_consumption, 84_LVBus1319189_production, 84_LVBus1319191_production, 84_LVBus1319193_consumption, 84_LVBus1319193_production, 84_LVBus1319195_consumption, 84_LVBus1319195_production, 84_LVBus1319196_production, 84_LVBus1319198_consumption, 84_LVBus1319198_production, 84_LVBus1319199_production, 84_LVBus1319201_production, 84_LVBus1319203_production, 84_LVBus1319205_production, 84_LVBus1319207_consumption, 84_LVBus1319207_production, 84_LVBus1319209_production, 84_LVBus1319211_production, 84_LVBus1319213_consumption, 84_LVBus1319213_production, 84_LVBus1319215_production, 84_LVBus1319217_consumption, 84_LVBus1319217_production, 84_LVBus1319219_production, 84_LVBus1319221_production, 84_LVBus1319223_production, 84_LVBus1319225_production, 84_LVBus1319227_consumption, 84_LVBus1319227_production, 84_LVBus1319228_production, 84_LVBus1319229_production, 84_LVBus1319230_production, 84_LVBus1319232_production, 84_LVBus1319233_production, 84_LVBus1319234_production, 84_LVBus1319235_production, 84_LVBus1319237_consumption, 84_LVBus1319237_production, 84_LVBus1319238_production, 84_LVBus1319239_consumption, 84_LVBus1319239_production, 84_LVBus1319240_production, 84_LVBus1319242_consumption, 84_LVBus1319242_production, 84_LVBus1319243_consumption, 84_LVBus1319243_production, 84_LVBus1319244_consumption, 84_LVBus1319244_production, 84_LVBus1319246_production, 84_LVBus1319247_consumption, 84_LVBus1319247_production, 84_LVBus1319248_production, 84_LVBus1319249_production, 84_LVBus1319250_production, 84_LVBus1319255_consumption, 84_LVBus1319255_production, 84_LVBus1319256_consumption, 84_LVBus1319256_production, 84_LVBus1319257_production, 84_LVBus1319258_production, 84_LVBus1319259_production, 84_LVBus1319261_consumption, 84_LVBus1319261_production, 84_LVBus1319262_consumption, 84_LVBus1319262_production, 84_LVBus1319263_consumption, 84_LVBus1319263_production, 84_LVBus1319264_production, 84_LVBus1319265_consumption, 84_LVBus1319265_production, 84_LVBus1319266_production, 84_LVBus1319267_production, 84_LVBus1319269_consumption, 84_LVBus1319269_production, 84_LVBus1319271_production, 84_LVBus1319273_consumption, 84_LVBus1319273_production, 84_LVBus1319275_production, 84_LVBus1319277_production, 84_LVBus1319279_consumption, 84_LVBus1319279_production, 84_LVBus1319280_production, 84_LVBus1319282_consumption, 84_LVBus1319282_production, 84_LVBus1319284_production, 84_LVBus1319286_consumption, 84_LVBus1319286_production, 84_LVBus1319288_production, 84_LVBus1319289_consumption, 84_LVBus1319289_production, 84_LVBus1319290_consumption, 84_LVBus1319290_production, 84_LVBus1319291_consumption, 84_LVBus1319291_production, 84_LVBus1319292_consumption, 84_LVBus1319292_production, 84_LVBus1319293_production, 84_LVBus1319294_production, 84_LVBus1319295_production, 84_LVBus1319297_production, 84_LVBus1319299_consumption, 84_LVBus1319299_production, 84_LVBus1319300_production, 84_LVBus1319301_production, 84_LVBus1319302_production, 84_LVBus1319304_consumption, 84_LVBus1319304_production, 84_LVBus1319306_consumption, 84_LVBus1319306_production, 84_LVBus1319308_consumption, 84_LVBus1319308_production, 84_LVBus1319309_consumption, 84_LVBus1319309_production, 84_LVBus1319310_production, 84_LVBus1319312_consumption, 84_LVBus1319312_production, 84_LVBus1319313_consumption, 84_LVBus1319313_production, 84_LVBus1319315_production, 84_LVBus1319317_production, 84_LVBus1319319_consumption, 84_LVBus1319319_production, 84_LVBus1319320_production, 84_LVBus1319322_consumption, 84_LVBus1319322_production, 84_LVBus1319323_consumption, 84_LVBus1319323_production, 84_LVBus1319324_consumption, 84_LVBus1319324_production, 84_LVBus1319326_consumption, 84_LVBus1319326_production, 84_LVBus1319328_production, 84_LVBus1319329_consumption, 84_LVBus1319329_production, 84_LVBus1319331_production, 84_LVBus1319333_consumption, 84_LVBus1319333_production, 84_LVBus1319334_consumption, 84_LVBus1319334_production, 84_LVBus1319337_production, 84_LVBus1319338_consumption, 84_LVBus1319338_production, 84_LVBus1319339_production, 84_LVBus1319340_consumption, 84_LVBus1319340_production, 84_LVBus1319342_production, 84_LVBus1319343_consumption, 84_LVBus1319343_production, 84_LVBus1319344_production, 84_LVBus1319346_production, 84_LVBus1319348_consumption, 84_LVBus1319348_production, 84_LVBus1319350_production, 84_LVBus1319351_production, 84_LVBus1319352_production, 84_LVBus1319353_production, 84_LVBus1319354_production, 84_LVBus1319355_production, 84_LVBus1319356_production, 84_LVBus1319357_production, 84_LVBus1319358_production, 84_LVBus1319359_production, 84_LVBus1319361_production, 84_LVBus1319362_production, 84_LVBus1319364_production, 84_LVBus1319366_consumption, 84_LVBus1319366_production, 84_LVBus1319368_consumption, 84_LVBus1319368_production, 84_LVBus1319370_consumption, 84_LVBus1319370_production, 84_LVBus1319372_consumption, 84_LVBus1319372_production, 84_LVBus1319373_production, 84_LVBus1319375_production, 84_LVBus1319377_consumption, 84_LVBus1319377_production, 84_LVBus1319378_production, 84_LVBus1319379_consumption, 84_LVBus1319379_production, 84_LVBus1319380_consumption, 84_LVBus1319380_production, 84_LVBus1319381_consumption, 84_LVBus1319381_production, 84_LVBus1319382_production, 84_LVBus1319383_production, 84_LVBus1319384_production, 84_LVBus1319385_production, 84_LVBus1319386_production, 84_LVBus1319387_production, 84_LVBus1319388_production, 84_LVBus1319389_production, 84_LVBus1319391_production, 84_LVBus1319392_consumption, 84_LVBus1319392_production, 84_LVBus1319393_consumption, 84_LVBus1319393_production, 84_LVBus1319395_consumption, 84_LVBus1319395_production, 84_LVBus1319397_consumption, 84_LVBus1319397_production, 84_LVBus1319398_production, 84_LVBus1319399_production, 84_LVBus1319400_production, 84_LVBus1319401_production, 84_LVBus1319402_production, 84_LVBus1319403_production, 84_LVBus1319405_production, 84_LVBus1319406_consumption, 84_LVBus1319406_production, 84_LVBus1319407_production, 84_LVBus1319408_production, 84_LVBus1319409_production, 84_LVBus1319410_production, 84_LVBus1319412_production, 84_LVBus1319413_production, 84_LVBus1319414_production, 84_LVBus1319415_production, 84_LVBus1319417_production, 84_LVBus1319418_production, 84_LVBus1319419_production, 84_LVBus1319420_production, 84_LVBus1319421_production, 84_LVBus1319422_production, 84_LVBus1319424_production, 84_LVBus1319425_production, 84_LVBus1319426_production, 84_LVBus1319427_production, 84_LVBus1319429_consumption, 84_LVBus1319429_production, 84_LVBus1319431_production, 84_LVBus1319432_production, 84_LVBus1319433_production, 84_LVBus1319434_production, 84_LVBus1319435_production, 84_LVBus1319436_production, 84_LVBus1319437_production, 84_LVBus1319439_consumption, 84_LVBus1319439_production, 84_LVBus1319440_production, 84_LVBus1319442_consumption, 84_LVBus1319442_production, 84_LVBus1319443_production, 84_LVBus1319445_production, 84_LVBus1319447_production, 84_LVBus1319448_consumption, 84_LVBus1319448_production, 84_LVBus1319450_consumption, 84_LVBus1319450_production, 84_LVBus1319451_consumption, 84_LVBus1319451_production, 84_LVBus1319452_consumption, 84_LVBus1319452_production, 84_LVBus1319453_production, 84_LVBus1319455_production, 84_LVBus1319456_consumption, 84_LVBus1319456_production, 84_LVBus1319457_consumption, 84_LVBus1319457_production, 84_LVBus1319459_consumption, 84_LVBus1319459_production, 84_LVBus1319461_production, 84_LVBus1319463_consumption, 84_LVBus1319463_production, 84_LVBus1319464_production, 84_LVBus1319466_consumption, 84_LVBus1319466_production, 84_LVBus1319467_consumption, 84_LVBus1319467_production, 84_LVBus1319469_production, 84_LVBus1319471_production, 84_LVBus1319473_consumption, 84_LVBus1319473_production, 84_LVBus1319474_consumption, 84_LVBus1319474_production, 84_LVBus1319476_consumption, 84_LVBus1319476_production, 84_LVBus1319477_consumption, 84_LVBus1319477_production, 84_LVBus1319479_production, 84_LVBus1319481_consumption, 84_LVBus1319481_production, 84_LVBus1319483_production, 84_LVBus1319485_consumption, 84_LVBus1319485_production, 84_LVBus1319486_consumption, 84_LVBus1319486_production, 84_LVBus1319488_consumption, 84_LVBus1319488_production, 84_LVBus1319490_production, 84_LVBus1319492_production, 84_LVBus1319494_consumption, 84_LVBus1319494_production, 84_LVBus1319496_consumption, 84_LVBus1319496_production, 84_LVBus1319498_production, 84_LVBus1319500_consumption, 84_LVBus1319500_production, 84_LVBus1319502_consumption, 84_LVBus1319502_production, 84_LVBus1319504_consumption, 84_LVBus1319504_production, 84_LVBus1319505_consumption, 84_LVBus1319505_production, 84_LVBus1319507_consumption, 84_LVBus1319507_production, 84_LVBus1319509_consumption, 84_LVBus1319509_production, 84_LVBus1319510_consumption, 84_LVBus1319510_production, 84_LVBus1319512_consumption, 84_LVBus1319512_production, 84_LVBus1319514_consumption, 84_LVBus1319514_production, 84_LVBus1319515_consumption, 84_LVBus1319515_production, 84_LVBus1319517_production, 84_LVBus2020930_consumption, 84_LVBus2020930_production, 84_LVBus2032356_consumption, 84_LVBus2032356_production, 84_LVBus2086353_production, 84_LVBus2086354_production, 84_LVBus2090780_consumption, 84_LVBus2090780_production, 84_LVBus2090781_consumption, 84_LVBus2090781_production, 84_LVBus2090782_consumption, 84_LVBus2090782_production, 84_LVBus2090783_production, 84_LVBus2090784_production, 84_LVBus2090785_consumption, 84_LVBus2090785_production, 84_LVBus2090786_production, 84_LVBus2090787_production, 84_LVBus2090788_production, 84_LVBus2090789_production, 84_LVBus2090790_production, 84_LVBus2090791_production, 84_LVBus2108376_production, 84_LVBus2111675_production, 84_LVBus2144652_production, 84_LVBus2144653_production, 84_LVBus2166675_consumption, 84_LVBus2166675_production, 84_LVBus2166676_consumption, 84_LVBus2166676_production, 84_LVBus2166677_production, 84_LVBus2166678_production, 84_LVBus2176608_production, 84_LVBus2176609_production, 84_LVBus2192003_consumption, 84_LVBus2192003_production, 84_LVBus2192004_production, 84_MVLV037301_production, 84_MVLV079864_consumption, 84_MVLV079864_production, 84_MVLV138901_production.

## 9. Data Quality Summary

**Total findings:** 164 (0 errors, 5 warnings, 159 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  423 of 594 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.33 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  424 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319407_consumption`  
  Load '84_LVBus1319407_consumption' has phase imbalance of 124.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090790_consumption`  
  Load '84_LVBus2090790_consumption' has phase imbalance of 211.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319362_consumption`  
  Load '84_LVBus1319362_consumption' has phase imbalance of 46.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2144653_consumption`  
  Load '84_LVBus2144653_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319258_consumption`  
  Load '84_LVBus1319258_consumption' has phase imbalance of 73.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319453_consumption`  
  Load '84_LVBus1319453_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319364_consumption`  
  Load '84_LVBus1319364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319150_consumption`  
  Load '84_LVBus1319150_consumption' has phase imbalance of 72.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319401_consumption`  
  Load '84_LVBus1319401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2192004_consumption`  
  Load '84_LVBus2192004_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319199_consumption`  
  Load '84_LVBus1319199_consumption' has phase imbalance of 67.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319385_consumption`  
  Load '84_LVBus1319385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319405_consumption`  
  Load '84_LVBus1319405_consumption' has phase imbalance of 71.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319277_consumption`  
  Load '84_LVBus1319277_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319203_consumption`  
  Load '84_LVBus1319203_consumption' has phase imbalance of 37.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319228_consumption`  
  Load '84_LVBus1319228_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319238_consumption`  
  Load '84_LVBus1319238_consumption' has phase imbalance of 90.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319221_consumption`  
  Load '84_LVBus1319221_consumption' has phase imbalance of 30.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319410_consumption`  
  Load '84_LVBus1319410_consumption' has phase imbalance of 42.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090783_consumption`  
  Load '84_LVBus2090783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319137_consumption`  
  Load '84_LVBus1319137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319233_consumption`  
  Load '84_LVBus1319233_consumption' has phase imbalance of 248.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319302_consumption`  
  Load '84_LVBus1319302_consumption' has phase imbalance of 22.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319422_consumption`  
  Load '84_LVBus1319422_consumption' has phase imbalance of 231.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319517_consumption`  
  Load '84_LVBus1319517_consumption' has phase imbalance of 24.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2144652_consumption`  
  Load '84_LVBus2144652_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319132_consumption`  
  Load '84_LVBus1319132_consumption' has phase imbalance of 40.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319267_consumption`  
  Load '84_LVBus1319267_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319351_consumption`  
  Load '84_LVBus1319351_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319209_consumption`  
  Load '84_LVBus1319209_consumption' has phase imbalance of 86.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319205_consumption`  
  Load '84_LVBus1319205_consumption' has phase imbalance of 94.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319180_consumption`  
  Load '84_LVBus1319180_consumption' has phase imbalance of 230.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319413_consumption`  
  Load '84_LVBus1319413_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319433_consumption`  
  Load '84_LVBus1319433_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319382_consumption`  
  Load '84_LVBus1319382_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319215_consumption`  
  Load '84_LVBus1319215_consumption' has phase imbalance of 55.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090787_consumption`  
  Load '84_LVBus2090787_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319232_consumption`  
  Load '84_LVBus1319232_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319315_consumption`  
  Load '84_LVBus1319315_consumption' has phase imbalance of 72.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319133_consumption`  
  Load '84_LVBus1319133_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319288_consumption`  
  Load '84_LVBus1319288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319234_consumption`  
  Load '84_LVBus1319234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319188_consumption`  
  Load '84_LVBus1319188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319386_consumption`  
  Load '84_LVBus1319386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319435_consumption`  
  Load '84_LVBus1319435_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319408_consumption`  
  Load '84_LVBus1319408_consumption' has phase imbalance of 40.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319259_consumption`  
  Load '84_LVBus1319259_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319391_consumption`  
  Load '84_LVBus1319391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319426_consumption`  
  Load '84_LVBus1319426_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319417_consumption`  
  Load '84_LVBus1319417_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319498_consumption`  
  Load '84_LVBus1319498_consumption' has phase imbalance of 53.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090791_consumption`  
  Load '84_LVBus2090791_consumption' has phase imbalance of 51.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319378_consumption`  
  Load '84_LVBus1319378_consumption' has phase imbalance of 85.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2086353_consumption`  
  Load '84_LVBus2086353_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319301_consumption`  
  Load '84_LVBus1319301_consumption' has phase imbalance of 40.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319355_consumption`  
  Load '84_LVBus1319355_consumption' has phase imbalance of 33.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319388_consumption`  
  Load '84_LVBus1319388_consumption' has phase imbalance of 64.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319293_consumption`  
  Load '84_LVBus1319293_consumption' has phase imbalance of 42.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2086354_consumption`  
  Load '84_LVBus2086354_consumption' has phase imbalance of 25.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319359_consumption`  
  Load '84_LVBus1319359_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319434_consumption`  
  Load '84_LVBus1319434_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319354_consumption`  
  Load '84_LVBus1319354_consumption' has phase imbalance of 233.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319443_consumption`  
  Load '84_LVBus1319443_consumption' has phase imbalance of 136.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319225_consumption`  
  Load '84_LVBus1319225_consumption' has phase imbalance of 55.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319295_consumption`  
  Load '84_LVBus1319295_consumption' has phase imbalance of 52.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319178_consumption`  
  Load '84_LVBus1319178_consumption' has phase imbalance of 121.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319402_consumption`  
  Load '84_LVBus1319402_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319240_consumption`  
  Load '84_LVBus1319240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319128_consumption`  
  Load '84_LVBus1319128_consumption' has phase imbalance of 50.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319384_consumption`  
  Load '84_LVBus1319384_consumption' has phase imbalance of 90.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319250_consumption`  
  Load '84_LVBus1319250_consumption' has phase imbalance of 116.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319356_consumption`  
  Load '84_LVBus1319356_consumption' has phase imbalance of 56.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319403_consumption`  
  Load '84_LVBus1319403_consumption' has phase imbalance of 116.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319201_consumption`  
  Load '84_LVBus1319201_consumption' has phase imbalance of 63.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319248_consumption`  
  Load '84_LVBus1319248_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319235_consumption`  
  Load '84_LVBus1319235_consumption' has phase imbalance of 120.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319339_consumption`  
  Load '84_LVBus1319339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319440_consumption`  
  Load '84_LVBus1319440_consumption' has phase imbalance of 128.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319412_consumption`  
  Load '84_LVBus1319412_consumption' has phase imbalance of 217.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319431_consumption`  
  Load '84_LVBus1319431_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090788_consumption`  
  Load '84_LVBus2090788_consumption' has phase imbalance of 89.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319398_consumption`  
  Load '84_LVBus1319398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319176_consumption`  
  Load '84_LVBus1319176_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319337_consumption`  
  Load '84_LVBus1319337_consumption' has phase imbalance of 52.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319328_consumption`  
  Load '84_LVBus1319328_consumption' has phase imbalance of 20.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319196_consumption`  
  Load '84_LVBus1319196_consumption' has phase imbalance of 29.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319483_consumption`  
  Load '84_LVBus1319483_consumption' has phase imbalance of 62.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319122_consumption`  
  Load '84_LVBus1319122_consumption' has phase imbalance of 124.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090789_consumption`  
  Load '84_LVBus2090789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319419_consumption`  
  Load '84_LVBus1319419_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319424_consumption`  
  Load '84_LVBus1319424_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319125_consumption`  
  Load '84_LVBus1319125_consumption' has phase imbalance of 64.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319264_consumption`  
  Load '84_LVBus1319264_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319266_consumption`  
  Load '84_LVBus1319266_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319297_consumption`  
  Load '84_LVBus1319297_consumption' has phase imbalance of 45.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319375_consumption`  
  Load '84_LVBus1319375_consumption' has phase imbalance of 87.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319415_consumption`  
  Load '84_LVBus1319415_consumption' has phase imbalance of 125.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319310_consumption`  
  Load '84_LVBus1319310_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319420_consumption`  
  Load '84_LVBus1319420_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319469_consumption`  
  Load '84_LVBus1319469_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319421_consumption`  
  Load '84_LVBus1319421_consumption' has phase imbalance of 58.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319174_consumption`  
  Load '84_LVBus1319174_consumption' has phase imbalance of 174.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319358_consumption`  
  Load '84_LVBus1319358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319427_consumption`  
  Load '84_LVBus1319427_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319409_consumption`  
  Load '84_LVBus1319409_consumption' has phase imbalance of 49.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319280_consumption`  
  Load '84_LVBus1319280_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319471_consumption`  
  Load '84_LVBus1319471_consumption' has phase imbalance of 51.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319400_consumption`  
  Load '84_LVBus1319400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090784_consumption`  
  Load '84_LVBus2090784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319191_consumption`  
  Load '84_LVBus1319191_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319399_consumption`  
  Load '84_LVBus1319399_consumption' has phase imbalance of 58.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319352_consumption`  
  Load '84_LVBus1319352_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319490_consumption`  
  Load '84_LVBus1319490_consumption' has phase imbalance of 102.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319357_consumption`  
  Load '84_LVBus1319357_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2090786_consumption`  
  Load '84_LVBus2090786_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319230_consumption`  
  Load '84_LVBus1319230_consumption' has phase imbalance of 130.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319300_consumption`  
  Load '84_LVBus1319300_consumption' has phase imbalance of 36.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319331_consumption`  
  Load '84_LVBus1319331_consumption' has phase imbalance of 26.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319294_consumption`  
  Load '84_LVBus1319294_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319154_consumption`  
  Load '84_LVBus1319154_consumption' has phase imbalance of 96.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319320_consumption`  
  Load '84_LVBus1319320_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319229_consumption`  
  Load '84_LVBus1319229_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319479_consumption`  
  Load '84_LVBus1319479_consumption' has phase imbalance of 52.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319223_consumption`  
  Load '84_LVBus1319223_consumption' has phase imbalance of 59.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166677_consumption`  
  Load '84_LVBus2166677_consumption' has phase imbalance of 50.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319246_consumption`  
  Load '84_LVBus1319246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319436_consumption`  
  Load '84_LVBus1319436_consumption' has phase imbalance of 294.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319464_consumption`  
  Load '84_LVBus1319464_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319425_consumption`  
  Load '84_LVBus1319425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319284_consumption`  
  Load '84_LVBus1319284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319414_consumption`  
  Load '84_LVBus1319414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319131_consumption`  
  Load '84_LVBus1319131_consumption' has phase imbalance of 87.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319211_consumption`  
  Load '84_LVBus1319211_consumption' has phase imbalance of 95.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319383_consumption`  
  Load '84_LVBus1319383_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319249_consumption`  
  Load '84_LVBus1319249_consumption' has phase imbalance of 202.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166678_consumption`  
  Load '84_LVBus2166678_consumption' has phase imbalance of 101.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319185_consumption`  
  Load '84_LVBus1319185_consumption' has phase imbalance of 26.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319418_consumption`  
  Load '84_LVBus1319418_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319437_consumption`  
  Load '84_LVBus1319437_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319257_consumption`  
  Load '84_LVBus1319257_consumption' has phase imbalance of 69.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1319317_consumption`  
  Load '84_LVBus1319317_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 594 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_SSGE7' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1319269' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1319156' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus1319494' (LV, 0.24 kV) has an electrical reach of 5.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  348 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  52 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus1319137_consumption, 84_LVBus1319174_consumption, 84_LVBus1319176_consumption, 84_LVBus1319180_consumption, 84_LVBus1319188_consumption, 84_LVBus1319232_consumption, 84_LVBus1319233_consumption, 84_LVBus1319234_consumption, 84_LVBus1319240_consumption, 84_LVBus1319246_consumption, 84_LVBus1319248_consumption, 84_LVBus1319249_consumption, 84_LVBus1319284_consumption, 84_LVBus1319288_consumption, 84_LVBus1319339_consumption, 84_LVBus1319351_consumption, 84_LVBus1319352_consumption, 84_LVBus1319354_consumption, 84_LVBus1319357_consumption, 84_LVBus1319358_consumption, 84_LVBus1319364_consumption, 84_LVBus1319383_consumption, 84_LVBus1319385_consumption, 84_LVBus1319386_consumption, 84_LVBus1319391_consumption, 84_LVBus1319398_consumption, 84_LVBus1319400_consumption, 84_LVBus1319401_consumption, 84_LVBus1319412_consumption, 84_LVBus1319413_consumption, 84_LVBus1319414_consumption, 84_LVBus1319417_consumption, 84_LVBus1319418_consumption, 84_LVBus1319419_consumption, 84_LVBus1319420_consumption, 84_LVBus1319422_consumption, 84_LVBus1319424_consumption, 84_LVBus1319425_consumption, 84_LVBus1319426_consumption, 84_LVBus1319431_consumption, 84_LVBus1319433_consumption, 84_LVBus1319435_consumption, 84_LVBus1319436_consumption, 84_LVBus1319453_consumption, 84_LVBus2090783_consumption, 84_LVBus2090784_consumption, 84_LVBus2090786_consumption, 84_LVBus2090789_consumption, 84_LVBus2090790_consumption, 84_LVBus2144652_consumption, 84_LVBus2144653_consumption, 84_LVBus2192004_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  297 group(s) of loads (594 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  424 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1319119_consumption, 84_LVBus1319119_production, 84_LVBus1319120_consumption, 84_LVBus1319120_production, 84_LVBus1319121_consumption, 84_LVBus1319121_production, 84_LVBus1319122_production, 84_LVBus1319123_consumption, 84_LVBus1319123_production, 84_LVBus1319125_production, 84_LVBus1319126_consumption, 84_LVBus1319126_production, 84_LVBus1319127_consumption, 84_LVBus1319127_production, 84_LVBus1319128_production, 84_LVBus1319130_consumption, 84_LVBus1319130_production, 84_LVBus1319131_production, 84_LVBus1319132_production, 84_LVBus1319133_production, 84_LVBus1319135_production, 84_LVBus1319137_production, 84_LVBus1319139_consumption, 84_LVBus1319139_production, 84_LVBus1319141_consumption, 84_LVBus1319141_production, 84_LVBus1319143_consumption, 84_LVBus1319143_production, 84_LVBus1319145_consumption, 84_LVBus1319145_production, 84_LVBus1319147_consumption, 84_LVBus1319147_production, 84_LVBus1319149_consumption, 84_LVBus1319149_production, 84_LVBus1319150_production, 84_LVBus1319151_consumption, 84_LVBus1319151_production, 84_LVBus1319152_consumption, 84_LVBus1319152_production, 84_LVBus1319154_production, 84_LVBus1319156_production, 84_LVBus1319158_production, 84_LVBus1319160_production, 84_LVBus1319162_consumption, 84_LVBus1319162_production, 84_LVBus1319164_consumption, 84_LVBus1319164_production, 84_LVBus1319166_consumption, 84_LVBus1319166_production, 84_LVBus1319168_production, 84_LVBus1319170_consumption, 84_LVBus1319170_production, 84_LVBus1319172_consumption, 84_LVBus1319172_production, 84_LVBus1319174_production, 84_LVBus1319176_production, 84_LVBus1319178_production, 84_LVBus1319180_production, 84_LVBus1319182_consumption, 84_LVBus1319182_production, 84_LVBus1319183_consumption, 84_LVBus1319183_production, 84_LVBus1319185_production, 84_LVBus1319187_consumption, 84_LVBus1319187_production, 84_LVBus1319188_production, 84_LVBus1319189_consumption, 84_LVBus1319189_production, 84_LVBus1319191_production, 84_LVBus1319193_consumption, 84_LVBus1319193_production, 84_LVBus1319195_consumption, 84_LVBus1319195_production, 84_LVBus1319196_production, 84_LVBus1319198_consumption, 84_LVBus1319198_production, 84_LVBus1319199_production, 84_LVBus1319201_production, 84_LVBus1319203_production, 84_LVBus1319205_production, 84_LVBus1319207_consumption, 84_LVBus1319207_production, 84_LVBus1319209_production, 84_LVBus1319211_production, 84_LVBus1319213_consumption, 84_LVBus1319213_production, 84_LVBus1319215_production, 84_LVBus1319217_consumption, 84_LVBus1319217_production, 84_LVBus1319219_production, 84_LVBus1319221_production, 84_LVBus1319223_production, 84_LVBus1319225_production, 84_LVBus1319227_consumption, 84_LVBus1319227_production, 84_LVBus1319228_production, 84_LVBus1319229_production, 84_LVBus1319230_production, 84_LVBus1319232_production, 84_LVBus1319233_production, 84_LVBus1319234_production, 84_LVBus1319235_production, 84_LVBus1319237_consumption, 84_LVBus1319237_production, 84_LVBus1319238_production, 84_LVBus1319239_consumption, 84_LVBus1319239_production, 84_LVBus1319240_production, 84_LVBus1319242_consumption, 84_LVBus1319242_production, 84_LVBus1319243_consumption, 84_LVBus1319243_production, 84_LVBus1319244_consumption, 84_LVBus1319244_production, 84_LVBus1319246_production, 84_LVBus1319247_consumption, 84_LVBus1319247_production, 84_LVBus1319248_production, 84_LVBus1319249_production, 84_LVBus1319250_production, 84_LVBus1319255_consumption, 84_LVBus1319255_production, 84_LVBus1319256_consumption, 84_LVBus1319256_production, 84_LVBus1319257_production, 84_LVBus1319258_production, 84_LVBus1319259_production, 84_LVBus1319261_consumption, 84_LVBus1319261_production, 84_LVBus1319262_consumption, 84_LVBus1319262_production, 84_LVBus1319263_consumption, 84_LVBus1319263_production, 84_LVBus1319264_production, 84_LVBus1319265_consumption, 84_LVBus1319265_production, 84_LVBus1319266_production, 84_LVBus1319267_production, 84_LVBus1319269_consumption, 84_LVBus1319269_production, 84_LVBus1319271_production, 84_LVBus1319273_consumption, 84_LVBus1319273_production, 84_LVBus1319275_production, 84_LVBus1319277_production, 84_LVBus1319279_consumption, 84_LVBus1319279_production, 84_LVBus1319280_production, 84_LVBus1319282_consumption, 84_LVBus1319282_production, 84_LVBus1319284_production, 84_LVBus1319286_consumption, 84_LVBus1319286_production, 84_LVBus1319288_production, 84_LVBus1319289_consumption, 84_LVBus1319289_production, 84_LVBus1319290_consumption, 84_LVBus1319290_production, 84_LVBus1319291_consumption, 84_LVBus1319291_production, 84_LVBus1319292_consumption, 84_LVBus1319292_production, 84_LVBus1319293_production, 84_LVBus1319294_production, 84_LVBus1319295_production, 84_LVBus1319297_production, 84_LVBus1319299_consumption, 84_LVBus1319299_production, 84_LVBus1319300_production, 84_LVBus1319301_production, 84_LVBus1319302_production, 84_LVBus1319304_consumption, 84_LVBus1319304_production, 84_LVBus1319306_consumption, 84_LVBus1319306_production, 84_LVBus1319308_consumption, 84_LVBus1319308_production, 84_LVBus1319309_consumption, 84_LVBus1319309_production, 84_LVBus1319310_production, 84_LVBus1319312_consumption, 84_LVBus1319312_production, 84_LVBus1319313_consumption, 84_LVBus1319313_production, 84_LVBus1319315_production, 84_LVBus1319317_production, 84_LVBus1319319_consumption, 84_LVBus1319319_production, 84_LVBus1319320_production, 84_LVBus1319322_consumption, 84_LVBus1319322_production, 84_LVBus1319323_consumption, 84_LVBus1319323_production, 84_LVBus1319324_consumption, 84_LVBus1319324_production, 84_LVBus1319326_consumption, 84_LVBus1319326_production, 84_LVBus1319328_production, 84_LVBus1319329_consumption, 84_LVBus1319329_production, 84_LVBus1319331_production, 84_LVBus1319333_consumption, 84_LVBus1319333_production, 84_LVBus1319334_consumption, 84_LVBus1319334_production, 84_LVBus1319337_production, 84_LVBus1319338_consumption, 84_LVBus1319338_production, 84_LVBus1319339_production, 84_LVBus1319340_consumption, 84_LVBus1319340_production, 84_LVBus1319342_production, 84_LVBus1319343_consumption, 84_LVBus1319343_production, 84_LVBus1319344_production, 84_LVBus1319346_production, 84_LVBus1319348_consumption, 84_LVBus1319348_production, 84_LVBus1319350_production, 84_LVBus1319351_production, 84_LVBus1319352_production, 84_LVBus1319353_production, 84_LVBus1319354_production, 84_LVBus1319355_production, 84_LVBus1319356_production, 84_LVBus1319357_production, 84_LVBus1319358_production, 84_LVBus1319359_production, 84_LVBus1319361_production, 84_LVBus1319362_production, 84_LVBus1319364_production, 84_LVBus1319366_consumption, 84_LVBus1319366_production, 84_LVBus1319368_consumption, 84_LVBus1319368_production, 84_LVBus1319370_consumption, 84_LVBus1319370_production, 84_LVBus1319372_consumption, 84_LVBus1319372_production, 84_LVBus1319373_production, 84_LVBus1319375_production, 84_LVBus1319377_consumption, 84_LVBus1319377_production, 84_LVBus1319378_production, 84_LVBus1319379_consumption, 84_LVBus1319379_production, 84_LVBus1319380_consumption, 84_LVBus1319380_production, 84_LVBus1319381_consumption, 84_LVBus1319381_production, 84_LVBus1319382_production, 84_LVBus1319383_production, 84_LVBus1319384_production, 84_LVBus1319385_production, 84_LVBus1319386_production, 84_LVBus1319387_production, 84_LVBus1319388_production, 84_LVBus1319389_production, 84_LVBus1319391_production, 84_LVBus1319392_consumption, 84_LVBus1319392_production, 84_LVBus1319393_consumption, 84_LVBus1319393_production, 84_LVBus1319395_consumption, 84_LVBus1319395_production, 84_LVBus1319397_consumption, 84_LVBus1319397_production, 84_LVBus1319398_production, 84_LVBus1319399_production, 84_LVBus1319400_production, 84_LVBus1319401_production, 84_LVBus1319402_production, 84_LVBus1319403_production, 84_LVBus1319405_production, 84_LVBus1319406_consumption, 84_LVBus1319406_production, 84_LVBus1319407_production, 84_LVBus1319408_production, 84_LVBus1319409_production, 84_LVBus1319410_production, 84_LVBus1319412_production, 84_LVBus1319413_production, 84_LVBus1319414_production, 84_LVBus1319415_production, 84_LVBus1319417_production, 84_LVBus1319418_production, 84_LVBus1319419_production, 84_LVBus1319420_production, 84_LVBus1319421_production, 84_LVBus1319422_production, 84_LVBus1319424_production, 84_LVBus1319425_production, 84_LVBus1319426_production, 84_LVBus1319427_production, 84_LVBus1319429_consumption, 84_LVBus1319429_production, 84_LVBus1319431_production, 84_LVBus1319432_production, 84_LVBus1319433_production, 84_LVBus1319434_production, 84_LVBus1319435_production, 84_LVBus1319436_production, 84_LVBus1319437_production, 84_LVBus1319439_consumption, 84_LVBus1319439_production, 84_LVBus1319440_production, 84_LVBus1319442_consumption, 84_LVBus1319442_production, 84_LVBus1319443_production, 84_LVBus1319445_production, 84_LVBus1319447_production, 84_LVBus1319448_consumption, 84_LVBus1319448_production, 84_LVBus1319450_consumption, 84_LVBus1319450_production, 84_LVBus1319451_consumption, 84_LVBus1319451_production, 84_LVBus1319452_consumption, 84_LVBus1319452_production, 84_LVBus1319453_production, 84_LVBus1319455_production, 84_LVBus1319456_consumption, 84_LVBus1319456_production, 84_LVBus1319457_consumption, 84_LVBus1319457_production, 84_LVBus1319459_consumption, 84_LVBus1319459_production, 84_LVBus1319461_production, 84_LVBus1319463_consumption, 84_LVBus1319463_production, 84_LVBus1319464_production, 84_LVBus1319466_consumption, 84_LVBus1319466_production, 84_LVBus1319467_consumption, 84_LVBus1319467_production, 84_LVBus1319469_production, 84_LVBus1319471_production, 84_LVBus1319473_consumption, 84_LVBus1319473_production, 84_LVBus1319474_consumption, 84_LVBus1319474_production, 84_LVBus1319476_consumption, 84_LVBus1319476_production, 84_LVBus1319477_consumption, 84_LVBus1319477_production, 84_LVBus1319479_production, 84_LVBus1319481_consumption, 84_LVBus1319481_production, 84_LVBus1319483_production, 84_LVBus1319485_consumption, 84_LVBus1319485_production, 84_LVBus1319486_consumption, 84_LVBus1319486_production, 84_LVBus1319488_consumption, 84_LVBus1319488_production, 84_LVBus1319490_production, 84_LVBus1319492_production, 84_LVBus1319494_consumption, 84_LVBus1319494_production, 84_LVBus1319496_consumption, 84_LVBus1319496_production, 84_LVBus1319498_production, 84_LVBus1319500_consumption, 84_LVBus1319500_production, 84_LVBus1319502_consumption, 84_LVBus1319502_production, 84_LVBus1319504_consumption, 84_LVBus1319504_production, 84_LVBus1319505_consumption, 84_LVBus1319505_production, 84_LVBus1319507_consumption, 84_LVBus1319507_production, 84_LVBus1319509_consumption, 84_LVBus1319509_production, 84_LVBus1319510_consumption, 84_LVBus1319510_production, 84_LVBus1319512_consumption, 84_LVBus1319512_production, 84_LVBus1319514_consumption, 84_LVBus1319514_production, 84_LVBus1319515_consumption, 84_LVBus1319515_production, 84_LVBus1319517_production, 84_LVBus2020930_consumption, 84_LVBus2020930_production, 84_LVBus2032356_consumption, 84_LVBus2032356_production, 84_LVBus2086353_production, 84_LVBus2086354_production, 84_LVBus2090780_consumption, 84_LVBus2090780_production, 84_LVBus2090781_consumption, 84_LVBus2090781_production, 84_LVBus2090782_consumption, 84_LVBus2090782_production, 84_LVBus2090783_production, 84_LVBus2090784_production, 84_LVBus2090785_consumption, 84_LVBus2090785_production, 84_LVBus2090786_production, 84_LVBus2090787_production, 84_LVBus2090788_production, 84_LVBus2090789_production, 84_LVBus2090790_production, 84_LVBus2090791_production, 84_LVBus2108376_production, 84_LVBus2111675_production, 84_LVBus2144652_production, 84_LVBus2144653_production, 84_LVBus2166675_consumption, 84_LVBus2166675_production, 84_LVBus2166676_consumption, 84_LVBus2166676_production, 84_LVBus2166677_production, 84_LVBus2166678_production, 84_LVBus2176608_production, 84_LVBus2176609_production, 84_LVBus2192003_consumption, 84_LVBus2192003_production, 84_LVBus2192004_production, 84_MVLV037301_production, 84_MVLV079864_consumption, 84_MVLV079864_production, 84_MVLV138901_production.

