# BMOPF Network Summary: 93_MVFeeder1218

**Generated:** 2026-10-01 23:34:49  
**Findings:** 0 errors · 6 warnings · 153 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 406 |  |
| line | 385 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 728 | 3.32 MW, 995.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 20 |  |
| switch | 0 |  |
| transformer | 20 | Dyn11×20 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 24 | 23 | 4 | 0 |
| LV_236V | 236.0 V | 382 | 362 | 724 | 0 |

**Transformer transitions:**

- `93_MVLV23144_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV52384_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV35906_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV30968_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV28257_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV23977_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV02306_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV02369_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV07937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV28982_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV28998_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV31061_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV26414_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV02635_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV41265_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV33270_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV53354_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV02659_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV28978_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV22408_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 13 |
| Degree-1 buses | 189 |
| Tree depth (max hops) | 27 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 406 | 1 | 405 | 0 | 0 | 0 |
| Tier LV_236V | 382 | 20 | 362 | 0 | 0 | 0 |
| Tier MV_11.8kV | 24 | 1 | 23 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 20; skipped invalid branches: 0.

Galvanic zones: 21; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 93_GRASS | MV_11.8kV | 24 | 0 | 0 | 20 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1600 declared bus terminals; 1517 mapped line/closed-switch conductor edges; 83 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 104000.0 | 4.143 | 2184 |
| q_nom | 0.0 | 31200.0 | 4.143 | 2184 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.33 | 1010.0 | 1.467 | 385 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.514 | 20 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 559 of 728 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447922_consumption' has phase imbalance of 113.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447609_consumption' has phase imbalance of 98.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447914_consumption' has phase imbalance of 54.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447811_consumption' has phase imbalance of 297.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447936_consumption' has phase imbalance of 90.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447800_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447743_consumption' has phase imbalance of 95.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447839_consumption' has phase imbalance of 20.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447974_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447991_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448006_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447612_consumption' has phase imbalance of 36.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448017_consumption' has phase imbalance of 50.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447615_consumption' has phase imbalance of 71.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447781_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447745_consumption' has phase imbalance of 25.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447727_consumption' has phase imbalance of 39.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447708_consumption' has phase imbalance of 101.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447751_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447636_consumption' has phase imbalance of 42.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447738_consumption' has phase imbalance of 193.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447939_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447711_consumption' has phase imbalance of 89.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447725_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447979_consumption' has phase imbalance of 26.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448085_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447950_consumption' has phase imbalance of 28.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447632_consumption' has phase imbalance of 239.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447703_consumption' has phase imbalance of 162.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447943_consumption' has phase imbalance of 77.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447826_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448081_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448052_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447858_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447625_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447947_consumption' has phase imbalance of 35.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447956_consumption' has phase imbalance of 78.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447967_consumption' has phase imbalance of 32.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448042_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447954_consumption' has phase imbalance of 43.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447957_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447637_consumption' has phase imbalance of 62.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447756_consumption' has phase imbalance of 52.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448083_consumption' has phase imbalance of 83.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447746_consumption' has phase imbalance of 145.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447701_consumption' has phase imbalance of 25.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447716_consumption' has phase imbalance of 68.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447618_consumption' has phase imbalance of 24.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447624_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447691_consumption' has phase imbalance of 63.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447714_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447702_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447877_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447814_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447710_consumption' has phase imbalance of 242.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447887_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448055_consumption' has phase imbalance of 24.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447876_consumption' has phase imbalance of 72.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447713_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448024_consumption' has phase imbalance of 114.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447850_consumption' has phase imbalance of 40.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447785_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447834_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447886_consumption' has phase imbalance of 82.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447620_consumption' has phase imbalance of 41.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447964_consumption' has phase imbalance of 73.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447728_consumption' has phase imbalance of 45.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447962_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447980_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447760_consumption' has phase imbalance of 28.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447806_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447944_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447829_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447739_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447903_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447765_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447984_consumption' has phase imbalance of 37.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447709_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447759_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447633_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447998_consumption' has phase imbalance of 33.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447631_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447809_consumption' has phase imbalance of 272.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447755_consumption' has phase imbalance of 118.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447884_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447807_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448008_consumption' has phase imbalance of 100.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448074_consumption' has phase imbalance of 41.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447869_consumption' has phase imbalance of 42.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447780_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447741_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447942_consumption' has phase imbalance of 21.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447933_consumption' has phase imbalance of 48.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448080_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447634_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447925_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447882_consumption' has phase imbalance of 259.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447669_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447733_consumption' has phase imbalance of 29.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447723_consumption' has phase imbalance of 25.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447810_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447923_consumption' has phase imbalance of 63.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448038_consumption' has phase imbalance of 43.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0448001_consumption' has phase imbalance of 56.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0447773_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 728 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0447639' has balanced aggregate load across 3 phase(s) (max spread 1.49%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_GRASS' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.32 MW |
| Total load Q | 995.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 93_MVLV23144_Transformer | 693.0 kVA | 82.3% |
| 93_MVLV52384_Transformer | 440.0 kVA | 43.7% |
| 93_MVLV35906_Transformer | 275.0 kVA | 52.1% |
| 93_MVLV30968_Transformer | 176.0 kVA | 68.9% |
| 93_MVLV28257_Transformer | 275.0 kVA | 30.1% |
| 93_MVLV23977_Transformer | 176.0 kVA | 0.0% |
| 93_MVLV02306_Transformer | 440.0 kVA | 33.1% |
| 93_MVLV02369_Transformer | 275.0 kVA | 45.5% |
| 93_MVLV07937_Transformer | 440.0 kVA | 26.7% |
| 93_MVLV28982_Transformer | 275.0 kVA | 35.0% |
| 93_MVLV28998_Transformer | 110.0 kVA | 14.5% |
| 93_MVLV31061_Transformer | 275.0 kVA | 87.5% |
| 93_MVLV26414_Transformer | 275.0 kVA | 92.6% ⚠ |
| 93_MVLV02635_Transformer | 440.0 kVA | 30.9% |
| 93_MVLV41265_Transformer | 440.0 kVA | 23.9% |
| 93_MVLV33270_Transformer | 693.0 kVA | 47.7% |
| 93_MVLV53354_Transformer | 176.0 kVA | 32.9% |
| 93_MVLV02659_Transformer | 110.0 kVA | 19.9% |
| 93_MVLV28978_Transformer | 176.0 kVA | 15.3% |
| 93_MVLV22408_Transformer | 440.0 kVA | 80.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.32 MW).
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '93_MVLV26414_Transformer' is at 92.6% utilisation at nominal load — little OPF headroom.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '93_LVBus0448083' (LV, 0.24 kV) has an electrical reach of 28.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 406 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 406 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 24 |
| LV_236V | 4-wire | 382 / 382 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 382 |
| Neutral branches | 362 |
| Grounding points | 20 |
| Neutral sections | 20 |
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
| 11.78 kV | 24 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 59 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 21 |
| Islands without voltage reference | 0 |
| Line impedance spread | 216.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 382 / 24 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 560 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 560 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0447607_consumption, 93_LVBus0447607_production, 93_LVBus0447608_consumption, 93_LVBus0447608_production, 93_LVBus0447609_production, 93_LVBus0447610_consumption, 93_LVBus0447610_production, 93_LVBus0447611_consumption, 93_LVBus0447611_production, 93_LVBus0447612_production, 93_LVBus0447613_production, 93_LVBus0447615_production, 93_LVBus0447616_consumption, 93_LVBus0447616_production, 93_LVBus0447617_consumption, 93_LVBus0447617_production, 93_LVBus0447618_production, 93_LVBus0447619_consumption, 93_LVBus0447619_production, 93_LVBus0447620_production, 93_LVBus0447621_consumption, 93_LVBus0447621_production, 93_LVBus0447623_consumption, 93_LVBus0447623_production, 93_LVBus0447624_production, 93_LVBus0447625_production, 93_LVBus0447626_consumption, 93_LVBus0447626_production, 93_LVBus0447628_consumption, 93_LVBus0447628_production, 93_LVBus0447629_production, 93_LVBus0447630_consumption, 93_LVBus0447630_production, 93_LVBus0447631_production, 93_LVBus0447632_production, 93_LVBus0447633_production, 93_LVBus0447634_production, 93_LVBus0447636_production, 93_LVBus0447637_production, 93_LVBus0447639_consumption, 93_LVBus0447639_production, 93_LVBus0447641_production, 93_LVBus0447643_production, 93_LVBus0447644_consumption, 93_LVBus0447644_production, 93_LVBus0447646_consumption, 93_LVBus0447646_production, 93_LVBus0447648_consumption, 93_LVBus0447648_production, 93_LVBus0447649_consumption, 93_LVBus0447649_production, 93_LVBus0447651_consumption, 93_LVBus0447651_production, 93_LVBus0447653_consumption, 93_LVBus0447653_production, 93_LVBus0447655_consumption, 93_LVBus0447655_production, 93_LVBus0447656_production, 93_LVBus0447658_consumption, 93_LVBus0447658_production, 93_LVBus0447660_consumption, 93_LVBus0447660_production, 93_LVBus0447662_consumption, 93_LVBus0447662_production, 93_LVBus0447664_consumption, 93_LVBus0447664_production, 93_LVBus0447665_production, 93_LVBus0447666_consumption, 93_LVBus0447666_production, 93_LVBus0447667_production, 93_LVBus0447668_consumption, 93_LVBus0447668_production, 93_LVBus0447669_production, 93_LVBus0447671_consumption, 93_LVBus0447671_production, 93_LVBus0447672_consumption, 93_LVBus0447672_production, 93_LVBus0447674_consumption, 93_LVBus0447674_production, 93_LVBus0447676_consumption, 93_LVBus0447676_production, 93_LVBus0447677_consumption, 93_LVBus0447677_production, 93_LVBus0447678_consumption, 93_LVBus0447678_production, 93_LVBus0447680_consumption, 93_LVBus0447680_production, 93_LVBus0447683_consumption, 93_LVBus0447683_production, 93_LVBus0447685_consumption, 93_LVBus0447685_production, 93_LVBus0447687_production, 93_LVBus0447689_consumption, 93_LVBus0447689_production, 93_LVBus0447691_production, 93_LVBus0447693_consumption, 93_LVBus0447693_production, 93_LVBus0447695_consumption, 93_LVBus0447695_production, 93_LVBus0447697_consumption, 93_LVBus0447697_production, 93_LVBus0447699_consumption, 93_LVBus0447699_production, 93_LVBus0447700_consumption, 93_LVBus0447700_production, 93_LVBus0447701_production, 93_LVBus0447702_production, 93_LVBus0447703_production, 93_LVBus0447704_consumption, 93_LVBus0447704_production, 93_LVBus0447705_consumption, 93_LVBus0447705_production, 93_LVBus0447706_consumption, 93_LVBus0447706_production, 93_LVBus0447707_consumption, 93_LVBus0447707_production, 93_LVBus0447708_production, 93_LVBus0447709_production, 93_LVBus0447710_production, 93_LVBus0447711_production, 93_LVBus0447712_consumption, 93_LVBus0447712_production, 93_LVBus0447713_production, 93_LVBus0447714_production, 93_LVBus0447716_production, 93_LVBus0447718_consumption, 93_LVBus0447718_production, 93_LVBus0447720_consumption, 93_LVBus0447720_production, 93_LVBus0447722_consumption, 93_LVBus0447722_production, 93_LVBus0447723_production, 93_LVBus0447724_consumption, 93_LVBus0447724_production, 93_LVBus0447725_production, 93_LVBus0447726_consumption, 93_LVBus0447726_production, 93_LVBus0447727_production, 93_LVBus0447728_production, 93_LVBus0447730_consumption, 93_LVBus0447730_production, 93_LVBus0447731_consumption, 93_LVBus0447731_production, 93_LVBus0447732_consumption, 93_LVBus0447732_production, 93_LVBus0447733_production, 93_LVBus0447735_consumption, 93_LVBus0447735_production, 93_LVBus0447736_production, 93_LVBus0447737_production, 93_LVBus0447738_production, 93_LVBus0447739_production, 93_LVBus0447740_production, 93_LVBus0447741_production, 93_LVBus0447742_consumption, 93_LVBus0447742_production, 93_LVBus0447743_production, 93_LVBus0447744_production, 93_LVBus0447745_production, 93_LVBus0447746_production, 93_LVBus0447748_consumption, 93_LVBus0447748_production, 93_LVBus0447749_production, 93_LVBus0447750_production, 93_LVBus0447751_production, 93_LVBus0447752_production, 93_LVBus0447753_consumption, 93_LVBus0447753_production, 93_LVBus0447754_production, 93_LVBus0447755_production, 93_LVBus0447756_production, 93_LVBus0447758_consumption, 93_LVBus0447758_production, 93_LVBus0447759_production, 93_LVBus0447760_production, 93_LVBus0447762_consumption, 93_LVBus0447762_production, 93_LVBus0447763_consumption, 93_LVBus0447763_production, 93_LVBus0447764_consumption, 93_LVBus0447764_production, 93_LVBus0447765_production, 93_LVBus0447767_production, 93_LVBus0447768_consumption, 93_LVBus0447768_production, 93_LVBus0447769_production, 93_LVBus0447770_production, 93_LVBus0447771_production, 93_LVBus0447772_production, 93_LVBus0447773_production, 93_LVBus0447774_production, 93_LVBus0447775_production, 93_LVBus0447776_production, 93_LVBus0447777_production, 93_LVBus0447778_production, 93_LVBus0447779_production, 93_LVBus0447780_production, 93_LVBus0447781_production, 93_LVBus0447782_production, 93_LVBus0447783_production, 93_LVBus0447784_production, 93_LVBus0447785_production, 93_LVBus0447787_production, 93_LVBus0447789_consumption, 93_LVBus0447789_production, 93_LVBus0447790_consumption, 93_LVBus0447790_production, 93_LVBus0447791_consumption, 93_LVBus0447791_production, 93_LVBus0447792_consumption, 93_LVBus0447792_production, 93_LVBus0447793_consumption, 93_LVBus0447793_production, 93_LVBus0447795_consumption, 93_LVBus0447795_production, 93_LVBus0447796_production, 93_LVBus0447797_production, 93_LVBus0447799_consumption, 93_LVBus0447799_production, 93_LVBus0447800_production, 93_LVBus0447801_consumption, 93_LVBus0447801_production, 93_LVBus0447803_consumption, 93_LVBus0447803_production, 93_LVBus0447804_production, 93_LVBus0447805_production, 93_LVBus0447806_production, 93_LVBus0447807_production, 93_LVBus0447808_production, 93_LVBus0447809_production, 93_LVBus0447810_production, 93_LVBus0447811_production, 93_LVBus0447812_production, 93_LVBus0447814_production, 93_LVBus0447816_consumption, 93_LVBus0447816_production, 93_LVBus0447817_consumption, 93_LVBus0447817_production, 93_LVBus0447818_consumption, 93_LVBus0447818_production, 93_LVBus0447820_consumption, 93_LVBus0447820_production, 93_LVBus0447822_consumption, 93_LVBus0447822_production, 93_LVBus0447823_consumption, 93_LVBus0447823_production, 93_LVBus0447824_consumption, 93_LVBus0447824_production, 93_LVBus0447826_production, 93_LVBus0447828_consumption, 93_LVBus0447828_production, 93_LVBus0447829_production, 93_LVBus0447830_consumption, 93_LVBus0447830_production, 93_LVBus0447832_consumption, 93_LVBus0447832_production, 93_LVBus0447834_production, 93_LVBus0447835_consumption, 93_LVBus0447835_production, 93_LVBus0447836_consumption, 93_LVBus0447836_production, 93_LVBus0447837_consumption, 93_LVBus0447837_production, 93_LVBus0447839_production, 93_LVBus0447840_consumption, 93_LVBus0447840_production, 93_LVBus0447842_consumption, 93_LVBus0447842_production, 93_LVBus0447844_consumption, 93_LVBus0447844_production, 93_LVBus0447845_consumption, 93_LVBus0447845_production, 93_LVBus0447846_consumption, 93_LVBus0447846_production, 93_LVBus0447848_consumption, 93_LVBus0447848_production, 93_LVBus0447850_production, 93_LVBus0447851_production, 93_LVBus0447853_consumption, 93_LVBus0447853_production, 93_LVBus0447855_consumption, 93_LVBus0447855_production, 93_LVBus0447857_consumption, 93_LVBus0447857_production, 93_LVBus0447858_production, 93_LVBus0447860_consumption, 93_LVBus0447860_production, 93_LVBus0447861_consumption, 93_LVBus0447861_production, 93_LVBus0447863_consumption, 93_LVBus0447863_production, 93_LVBus0447865_consumption, 93_LVBus0447865_production, 93_LVBus0447867_consumption, 93_LVBus0447867_production, 93_LVBus0447869_production, 93_LVBus0447871_consumption, 93_LVBus0447871_production, 93_LVBus0447873_consumption, 93_LVBus0447873_production, 93_LVBus0447875_consumption, 93_LVBus0447875_production, 93_LVBus0447876_production, 93_LVBus0447877_production, 93_LVBus0447879_consumption, 93_LVBus0447879_production, 93_LVBus0447880_consumption, 93_LVBus0447880_production, 93_LVBus0447881_consumption, 93_LVBus0447881_production, 93_LVBus0447882_production, 93_LVBus0447883_production, 93_LVBus0447884_production, 93_LVBus0447885_consumption, 93_LVBus0447885_production, 93_LVBus0447886_production, 93_LVBus0447887_production, 93_LVBus0447888_production, 93_LVBus0447889_production, 93_LVBus0447891_consumption, 93_LVBus0447891_production, 93_LVBus0447892_production, 93_LVBus0447893_production, 93_LVBus0447894_consumption, 93_LVBus0447894_production, 93_LVBus0447896_consumption, 93_LVBus0447896_production, 93_LVBus0447898_consumption, 93_LVBus0447898_production, 93_LVBus0447899_consumption, 93_LVBus0447899_production, 93_LVBus0447901_production, 93_LVBus0447903_production, 93_LVBus0447905_production, 93_LVBus0447906_consumption, 93_LVBus0447906_production, 93_LVBus0447908_consumption, 93_LVBus0447908_production, 93_LVBus0447910_consumption, 93_LVBus0447910_production, 93_LVBus0447912_consumption, 93_LVBus0447912_production, 93_LVBus0447913_consumption, 93_LVBus0447913_production, 93_LVBus0447914_production, 93_LVBus0447915_consumption, 93_LVBus0447915_production, 93_LVBus0447916_consumption, 93_LVBus0447916_production, 93_LVBus0447917_consumption, 93_LVBus0447917_production, 93_LVBus0447918_consumption, 93_LVBus0447918_production, 93_LVBus0447919_consumption, 93_LVBus0447919_production, 93_LVBus0447920_consumption, 93_LVBus0447920_production, 93_LVBus0447922_production, 93_LVBus0447923_production, 93_LVBus0447924_consumption, 93_LVBus0447924_production, 93_LVBus0447925_production, 93_LVBus0447927_consumption, 93_LVBus0447927_production, 93_LVBus0447929_consumption, 93_LVBus0447929_production, 93_LVBus0447930_consumption, 93_LVBus0447930_production, 93_LVBus0447931_production, 93_LVBus0447932_consumption, 93_LVBus0447932_production, 93_LVBus0447933_production, 93_LVBus0447934_consumption, 93_LVBus0447934_production, 93_LVBus0447936_production, 93_LVBus0447937_consumption, 93_LVBus0447937_production, 93_LVBus0447938_consumption, 93_LVBus0447938_production, 93_LVBus0447939_production, 93_LVBus0447941_consumption, 93_LVBus0447941_production, 93_LVBus0447942_production, 93_LVBus0447943_production, 93_LVBus0447944_production, 93_LVBus0447946_consumption, 93_LVBus0447946_production, 93_LVBus0447947_production, 93_LVBus0447948_consumption, 93_LVBus0447948_production, 93_LVBus0447950_production, 93_LVBus0447951_consumption, 93_LVBus0447951_production, 93_LVBus0447953_consumption, 93_LVBus0447953_production, 93_LVBus0447954_production, 93_LVBus0447956_production, 93_LVBus0447957_production, 93_LVBus0447959_consumption, 93_LVBus0447959_production, 93_LVBus0447960_consumption, 93_LVBus0447960_production, 93_LVBus0447962_production, 93_LVBus0447963_consumption, 93_LVBus0447963_production, 93_LVBus0447964_production, 93_LVBus0447966_consumption, 93_LVBus0447966_production, 93_LVBus0447967_production, 93_LVBus0447968_consumption, 93_LVBus0447968_production, 93_LVBus0447970_consumption, 93_LVBus0447970_production, 93_LVBus0447971_consumption, 93_LVBus0447971_production, 93_LVBus0447972_consumption, 93_LVBus0447972_production, 93_LVBus0447973_consumption, 93_LVBus0447973_production, 93_LVBus0447974_production, 93_LVBus0447975_production, 93_LVBus0447976_production, 93_LVBus0447977_consumption, 93_LVBus0447977_production, 93_LVBus0447979_production, 93_LVBus0447980_production, 93_LVBus0447981_production, 93_LVBus0447983_consumption, 93_LVBus0447983_production, 93_LVBus0447984_production, 93_LVBus0447987_consumption, 93_LVBus0447987_production, 93_LVBus0447989_consumption, 93_LVBus0447989_production, 93_LVBus0447990_consumption, 93_LVBus0447990_production, 93_LVBus0447991_production, 93_LVBus0447992_consumption, 93_LVBus0447992_production, 93_LVBus0447993_consumption, 93_LVBus0447993_production, 93_LVBus0447994_consumption, 93_LVBus0447994_production, 93_LVBus0447996_consumption, 93_LVBus0447996_production, 93_LVBus0447998_production, 93_LVBus0448000_production, 93_LVBus0448001_production, 93_LVBus0448003_production, 93_LVBus0448005_consumption, 93_LVBus0448005_production, 93_LVBus0448006_production, 93_LVBus0448008_production, 93_LVBus0448010_consumption, 93_LVBus0448010_production, 93_LVBus0448011_consumption, 93_LVBus0448011_production, 93_LVBus0448013_consumption, 93_LVBus0448013_production, 93_LVBus0448014_consumption, 93_LVBus0448014_production, 93_LVBus0448015_consumption, 93_LVBus0448015_production, 93_LVBus0448016_consumption, 93_LVBus0448016_production, 93_LVBus0448017_production, 93_LVBus0448019_consumption, 93_LVBus0448019_production, 93_LVBus0448020_consumption, 93_LVBus0448020_production, 93_LVBus0448021_consumption, 93_LVBus0448021_production, 93_LVBus0448022_consumption, 93_LVBus0448022_production, 93_LVBus0448023_consumption, 93_LVBus0448023_production, 93_LVBus0448024_production, 93_LVBus0448025_production, 93_LVBus0448026_production, 93_LVBus0448027_consumption, 93_LVBus0448027_production, 93_LVBus0448028_production, 93_LVBus0448030_consumption, 93_LVBus0448030_production, 93_LVBus0448031_consumption, 93_LVBus0448031_production, 93_LVBus0448032_consumption, 93_LVBus0448032_production, 93_LVBus0448034_consumption, 93_LVBus0448034_production, 93_LVBus0448035_consumption, 93_LVBus0448035_production, 93_LVBus0448037_consumption, 93_LVBus0448037_production, 93_LVBus0448038_production, 93_LVBus0448039_consumption, 93_LVBus0448039_production, 93_LVBus0448042_production, 93_LVBus0448043_consumption, 93_LVBus0448043_production, 93_LVBus0448044_production, 93_LVBus0448045_consumption, 93_LVBus0448045_production, 93_LVBus0448047_production, 93_LVBus0448048_consumption, 93_LVBus0448048_production, 93_LVBus0448049_consumption, 93_LVBus0448049_production, 93_LVBus0448050_production, 93_LVBus0448051_consumption, 93_LVBus0448051_production, 93_LVBus0448052_production, 93_LVBus0448053_consumption, 93_LVBus0448053_production, 93_LVBus0448054_consumption, 93_LVBus0448054_production, 93_LVBus0448055_production, 93_LVBus0448056_consumption, 93_LVBus0448056_production, 93_LVBus0448058_consumption, 93_LVBus0448058_production, 93_LVBus0448060_consumption, 93_LVBus0448060_production, 93_LVBus0448061_consumption, 93_LVBus0448061_production, 93_LVBus0448062_consumption, 93_LVBus0448062_production, 93_LVBus0448063_consumption, 93_LVBus0448063_production, 93_LVBus0448064_consumption, 93_LVBus0448064_production, 93_LVBus0448065_consumption, 93_LVBus0448065_production, 93_LVBus0448066_consumption, 93_LVBus0448066_production, 93_LVBus0448067_consumption, 93_LVBus0448067_production, 93_LVBus0448068_production, 93_LVBus0448069_production, 93_LVBus0448070_production, 93_LVBus0448071_consumption, 93_LVBus0448071_production, 93_LVBus0448072_consumption, 93_LVBus0448072_production, 93_LVBus0448073_consumption, 93_LVBus0448073_production, 93_LVBus0448074_production, 93_LVBus0448076_production, 93_LVBus0448078_consumption, 93_LVBus0448078_production, 93_LVBus0448079_production, 93_LVBus0448080_production, 93_LVBus0448081_production, 93_LVBus0448083_production, 93_LVBus0448085_production, 93_LVBus0448087_consumption, 93_LVBus0448087_production, 93_MVLV02082_consumption, 93_MVLV02082_production, 93_MVLV40671_production.

## 9. Data Quality Summary

**Total findings:** 159 (0 errors, 6 warnings, 153 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  559 of 728 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.32 MW).
- **[W.OPS.XFMR_OVERLOADED]** `93_MVLV26414_Transformer`  
  Transformer '93_MVLV26414_Transformer' is at 92.6% utilisation at nominal load — little OPF headroom.
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  560 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447767_consumption`  
  Load '93_LVBus0447767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447922_consumption`  
  Load '93_LVBus0447922_consumption' has phase imbalance of 113.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447609_consumption`  
  Load '93_LVBus0447609_consumption' has phase imbalance of 98.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447914_consumption`  
  Load '93_LVBus0447914_consumption' has phase imbalance of 54.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447811_consumption`  
  Load '93_LVBus0447811_consumption' has phase imbalance of 297.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447936_consumption`  
  Load '93_LVBus0447936_consumption' has phase imbalance of 90.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447888_consumption`  
  Load '93_LVBus0447888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447800_consumption`  
  Load '93_LVBus0447800_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447743_consumption`  
  Load '93_LVBus0447743_consumption' has phase imbalance of 95.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447839_consumption`  
  Load '93_LVBus0447839_consumption' has phase imbalance of 20.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447778_consumption`  
  Load '93_LVBus0447778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448070_consumption`  
  Load '93_LVBus0448070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447974_consumption`  
  Load '93_LVBus0447974_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447991_consumption`  
  Load '93_LVBus0447991_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447779_consumption`  
  Load '93_LVBus0447779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447744_consumption`  
  Load '93_LVBus0447744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448006_consumption`  
  Load '93_LVBus0448006_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447612_consumption`  
  Load '93_LVBus0447612_consumption' has phase imbalance of 36.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448017_consumption`  
  Load '93_LVBus0448017_consumption' has phase imbalance of 50.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447736_consumption`  
  Load '93_LVBus0447736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447615_consumption`  
  Load '93_LVBus0447615_consumption' has phase imbalance of 71.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447781_consumption`  
  Load '93_LVBus0447781_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447754_consumption`  
  Load '93_LVBus0447754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447745_consumption`  
  Load '93_LVBus0447745_consumption' has phase imbalance of 25.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447727_consumption`  
  Load '93_LVBus0447727_consumption' has phase imbalance of 39.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447708_consumption`  
  Load '93_LVBus0447708_consumption' has phase imbalance of 101.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447751_consumption`  
  Load '93_LVBus0447751_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447636_consumption`  
  Load '93_LVBus0447636_consumption' has phase imbalance of 42.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447738_consumption`  
  Load '93_LVBus0447738_consumption' has phase imbalance of 193.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447812_consumption`  
  Load '93_LVBus0447812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448044_consumption`  
  Load '93_LVBus0448044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447737_consumption`  
  Load '93_LVBus0447737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447939_consumption`  
  Load '93_LVBus0447939_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447711_consumption`  
  Load '93_LVBus0447711_consumption' has phase imbalance of 89.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447725_consumption`  
  Load '93_LVBus0447725_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447979_consumption`  
  Load '93_LVBus0447979_consumption' has phase imbalance of 26.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448085_consumption`  
  Load '93_LVBus0448085_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447950_consumption`  
  Load '93_LVBus0447950_consumption' has phase imbalance of 28.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447632_consumption`  
  Load '93_LVBus0447632_consumption' has phase imbalance of 239.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447703_consumption`  
  Load '93_LVBus0447703_consumption' has phase imbalance of 162.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447943_consumption`  
  Load '93_LVBus0447943_consumption' has phase imbalance of 77.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448050_consumption`  
  Load '93_LVBus0448050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447826_consumption`  
  Load '93_LVBus0447826_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448081_consumption`  
  Load '93_LVBus0448081_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448052_consumption`  
  Load '93_LVBus0448052_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447858_consumption`  
  Load '93_LVBus0447858_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447625_consumption`  
  Load '93_LVBus0447625_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447947_consumption`  
  Load '93_LVBus0447947_consumption' has phase imbalance of 35.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447956_consumption`  
  Load '93_LVBus0447956_consumption' has phase imbalance of 78.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447967_consumption`  
  Load '93_LVBus0447967_consumption' has phase imbalance of 32.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448042_consumption`  
  Load '93_LVBus0448042_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447954_consumption`  
  Load '93_LVBus0447954_consumption' has phase imbalance of 43.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447957_consumption`  
  Load '93_LVBus0447957_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447771_consumption`  
  Load '93_LVBus0447771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447637_consumption`  
  Load '93_LVBus0447637_consumption' has phase imbalance of 62.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447756_consumption`  
  Load '93_LVBus0447756_consumption' has phase imbalance of 52.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447769_consumption`  
  Load '93_LVBus0447769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448083_consumption`  
  Load '93_LVBus0448083_consumption' has phase imbalance of 83.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447776_consumption`  
  Load '93_LVBus0447776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447746_consumption`  
  Load '93_LVBus0447746_consumption' has phase imbalance of 145.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447701_consumption`  
  Load '93_LVBus0447701_consumption' has phase imbalance of 25.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447716_consumption`  
  Load '93_LVBus0447716_consumption' has phase imbalance of 68.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447618_consumption`  
  Load '93_LVBus0447618_consumption' has phase imbalance of 24.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447624_consumption`  
  Load '93_LVBus0447624_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447691_consumption`  
  Load '93_LVBus0447691_consumption' has phase imbalance of 63.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447714_consumption`  
  Load '93_LVBus0447714_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447702_consumption`  
  Load '93_LVBus0447702_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447775_consumption`  
  Load '93_LVBus0447775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447665_consumption`  
  Load '93_LVBus0447665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447772_consumption`  
  Load '93_LVBus0447772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447877_consumption`  
  Load '93_LVBus0447877_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447814_consumption`  
  Load '93_LVBus0447814_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447710_consumption`  
  Load '93_LVBus0447710_consumption' has phase imbalance of 242.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447887_consumption`  
  Load '93_LVBus0447887_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448055_consumption`  
  Load '93_LVBus0448055_consumption' has phase imbalance of 24.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447777_consumption`  
  Load '93_LVBus0447777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447783_consumption`  
  Load '93_LVBus0447783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447876_consumption`  
  Load '93_LVBus0447876_consumption' has phase imbalance of 72.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447713_consumption`  
  Load '93_LVBus0447713_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448024_consumption`  
  Load '93_LVBus0448024_consumption' has phase imbalance of 114.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447850_consumption`  
  Load '93_LVBus0447850_consumption' has phase imbalance of 40.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447785_consumption`  
  Load '93_LVBus0447785_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447834_consumption`  
  Load '93_LVBus0447834_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447750_consumption`  
  Load '93_LVBus0447750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447886_consumption`  
  Load '93_LVBus0447886_consumption' has phase imbalance of 82.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447620_consumption`  
  Load '93_LVBus0447620_consumption' has phase imbalance of 41.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447964_consumption`  
  Load '93_LVBus0447964_consumption' has phase imbalance of 73.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447728_consumption`  
  Load '93_LVBus0447728_consumption' has phase imbalance of 45.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447962_consumption`  
  Load '93_LVBus0447962_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447687_consumption`  
  Load '93_LVBus0447687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447980_consumption`  
  Load '93_LVBus0447980_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447760_consumption`  
  Load '93_LVBus0447760_consumption' has phase imbalance of 28.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447806_consumption`  
  Load '93_LVBus0447806_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447944_consumption`  
  Load '93_LVBus0447944_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447829_consumption`  
  Load '93_LVBus0447829_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447739_consumption`  
  Load '93_LVBus0447739_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447903_consumption`  
  Load '93_LVBus0447903_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447765_consumption`  
  Load '93_LVBus0447765_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447984_consumption`  
  Load '93_LVBus0447984_consumption' has phase imbalance of 37.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447770_consumption`  
  Load '93_LVBus0447770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447709_consumption`  
  Load '93_LVBus0447709_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447759_consumption`  
  Load '93_LVBus0447759_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447633_consumption`  
  Load '93_LVBus0447633_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447804_consumption`  
  Load '93_LVBus0447804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447998_consumption`  
  Load '93_LVBus0447998_consumption' has phase imbalance of 33.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447631_consumption`  
  Load '93_LVBus0447631_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447809_consumption`  
  Load '93_LVBus0447809_consumption' has phase imbalance of 272.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447755_consumption`  
  Load '93_LVBus0447755_consumption' has phase imbalance of 118.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448028_consumption`  
  Load '93_LVBus0448028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447884_consumption`  
  Load '93_LVBus0447884_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447807_consumption`  
  Load '93_LVBus0447807_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448008_consumption`  
  Load '93_LVBus0448008_consumption' has phase imbalance of 100.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448074_consumption`  
  Load '93_LVBus0448074_consumption' has phase imbalance of 41.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447749_consumption`  
  Load '93_LVBus0447749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447869_consumption`  
  Load '93_LVBus0447869_consumption' has phase imbalance of 42.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447780_consumption`  
  Load '93_LVBus0447780_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447741_consumption`  
  Load '93_LVBus0447741_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447774_consumption`  
  Load '93_LVBus0447774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448025_consumption`  
  Load '93_LVBus0448025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448000_consumption`  
  Load '93_LVBus0448000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447942_consumption`  
  Load '93_LVBus0447942_consumption' has phase imbalance of 21.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447933_consumption`  
  Load '93_LVBus0447933_consumption' has phase imbalance of 48.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447629_consumption`  
  Load '93_LVBus0447629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448080_consumption`  
  Load '93_LVBus0448080_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447634_consumption`  
  Load '93_LVBus0447634_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447925_consumption`  
  Load '93_LVBus0447925_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447882_consumption`  
  Load '93_LVBus0447882_consumption' has phase imbalance of 259.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447669_consumption`  
  Load '93_LVBus0447669_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447784_consumption`  
  Load '93_LVBus0447784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447733_consumption`  
  Load '93_LVBus0447733_consumption' has phase imbalance of 29.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447723_consumption`  
  Load '93_LVBus0447723_consumption' has phase imbalance of 25.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447810_consumption`  
  Load '93_LVBus0447810_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447923_consumption`  
  Load '93_LVBus0447923_consumption' has phase imbalance of 63.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448038_consumption`  
  Load '93_LVBus0448038_consumption' has phase imbalance of 43.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0448001_consumption`  
  Load '93_LVBus0448001_consumption' has phase imbalance of 56.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0447773_consumption`  
  Load '93_LVBus0447773_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 728 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0447639' has balanced aggregate load across 3 phase(s) (max spread 1.49%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_GRASS' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '93_LVBus0448083' (LV, 0.24 kV) has an electrical reach of 28.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  406 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  56 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 93_LVBus0447629_consumption, 93_LVBus0447631_consumption, 93_LVBus0447633_consumption, 93_LVBus0447665_consumption, 93_LVBus0447687_consumption, 93_LVBus0447702_consumption, 93_LVBus0447703_consumption, 93_LVBus0447710_consumption, 93_LVBus0447713_consumption, 93_LVBus0447725_consumption, 93_LVBus0447736_consumption, 93_LVBus0447737_consumption, 93_LVBus0447738_consumption, 93_LVBus0447739_consumption, 93_LVBus0447741_consumption, 93_LVBus0447744_consumption, 93_LVBus0447749_consumption, 93_LVBus0447750_consumption, 93_LVBus0447751_consumption, 93_LVBus0447754_consumption, 93_LVBus0447767_consumption, 93_LVBus0447769_consumption, 93_LVBus0447770_consumption, 93_LVBus0447771_consumption, 93_LVBus0447772_consumption, 93_LVBus0447773_consumption, 93_LVBus0447774_consumption, 93_LVBus0447775_consumption, 93_LVBus0447776_consumption, 93_LVBus0447777_consumption, 93_LVBus0447778_consumption, 93_LVBus0447779_consumption, 93_LVBus0447780_consumption, 93_LVBus0447781_consumption, 93_LVBus0447783_consumption, 93_LVBus0447784_consumption, 93_LVBus0447785_consumption, 93_LVBus0447804_consumption, 93_LVBus0447806_consumption, 93_LVBus0447809_consumption, 93_LVBus0447810_consumption, 93_LVBus0447811_consumption, 93_LVBus0447812_consumption, 93_LVBus0447882_consumption, 93_LVBus0447884_consumption, 93_LVBus0447888_consumption, 93_LVBus0447903_consumption, 93_LVBus0447939_consumption, 93_LVBus0447991_consumption, 93_LVBus0448000_consumption, 93_LVBus0448025_consumption, 93_LVBus0448028_consumption, 93_LVBus0448044_consumption, 93_LVBus0448050_consumption, 93_LVBus0448070_consumption, 93_LVBus0448080_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  364 group(s) of loads (728 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  560 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0447607_consumption, 93_LVBus0447607_production, 93_LVBus0447608_consumption, 93_LVBus0447608_production, 93_LVBus0447609_production, 93_LVBus0447610_consumption, 93_LVBus0447610_production, 93_LVBus0447611_consumption, 93_LVBus0447611_production, 93_LVBus0447612_production, 93_LVBus0447613_production, 93_LVBus0447615_production, 93_LVBus0447616_consumption, 93_LVBus0447616_production, 93_LVBus0447617_consumption, 93_LVBus0447617_production, 93_LVBus0447618_production, 93_LVBus0447619_consumption, 93_LVBus0447619_production, 93_LVBus0447620_production, 93_LVBus0447621_consumption, 93_LVBus0447621_production, 93_LVBus0447623_consumption, 93_LVBus0447623_production, 93_LVBus0447624_production, 93_LVBus0447625_production, 93_LVBus0447626_consumption, 93_LVBus0447626_production, 93_LVBus0447628_consumption, 93_LVBus0447628_production, 93_LVBus0447629_production, 93_LVBus0447630_consumption, 93_LVBus0447630_production, 93_LVBus0447631_production, 93_LVBus0447632_production, 93_LVBus0447633_production, 93_LVBus0447634_production, 93_LVBus0447636_production, 93_LVBus0447637_production, 93_LVBus0447639_consumption, 93_LVBus0447639_production, 93_LVBus0447641_production, 93_LVBus0447643_production, 93_LVBus0447644_consumption, 93_LVBus0447644_production, 93_LVBus0447646_consumption, 93_LVBus0447646_production, 93_LVBus0447648_consumption, 93_LVBus0447648_production, 93_LVBus0447649_consumption, 93_LVBus0447649_production, 93_LVBus0447651_consumption, 93_LVBus0447651_production, 93_LVBus0447653_consumption, 93_LVBus0447653_production, 93_LVBus0447655_consumption, 93_LVBus0447655_production, 93_LVBus0447656_production, 93_LVBus0447658_consumption, 93_LVBus0447658_production, 93_LVBus0447660_consumption, 93_LVBus0447660_production, 93_LVBus0447662_consumption, 93_LVBus0447662_production, 93_LVBus0447664_consumption, 93_LVBus0447664_production, 93_LVBus0447665_production, 93_LVBus0447666_consumption, 93_LVBus0447666_production, 93_LVBus0447667_production, 93_LVBus0447668_consumption, 93_LVBus0447668_production, 93_LVBus0447669_production, 93_LVBus0447671_consumption, 93_LVBus0447671_production, 93_LVBus0447672_consumption, 93_LVBus0447672_production, 93_LVBus0447674_consumption, 93_LVBus0447674_production, 93_LVBus0447676_consumption, 93_LVBus0447676_production, 93_LVBus0447677_consumption, 93_LVBus0447677_production, 93_LVBus0447678_consumption, 93_LVBus0447678_production, 93_LVBus0447680_consumption, 93_LVBus0447680_production, 93_LVBus0447683_consumption, 93_LVBus0447683_production, 93_LVBus0447685_consumption, 93_LVBus0447685_production, 93_LVBus0447687_production, 93_LVBus0447689_consumption, 93_LVBus0447689_production, 93_LVBus0447691_production, 93_LVBus0447693_consumption, 93_LVBus0447693_production, 93_LVBus0447695_consumption, 93_LVBus0447695_production, 93_LVBus0447697_consumption, 93_LVBus0447697_production, 93_LVBus0447699_consumption, 93_LVBus0447699_production, 93_LVBus0447700_consumption, 93_LVBus0447700_production, 93_LVBus0447701_production, 93_LVBus0447702_production, 93_LVBus0447703_production, 93_LVBus0447704_consumption, 93_LVBus0447704_production, 93_LVBus0447705_consumption, 93_LVBus0447705_production, 93_LVBus0447706_consumption, 93_LVBus0447706_production, 93_LVBus0447707_consumption, 93_LVBus0447707_production, 93_LVBus0447708_production, 93_LVBus0447709_production, 93_LVBus0447710_production, 93_LVBus0447711_production, 93_LVBus0447712_consumption, 93_LVBus0447712_production, 93_LVBus0447713_production, 93_LVBus0447714_production, 93_LVBus0447716_production, 93_LVBus0447718_consumption, 93_LVBus0447718_production, 93_LVBus0447720_consumption, 93_LVBus0447720_production, 93_LVBus0447722_consumption, 93_LVBus0447722_production, 93_LVBus0447723_production, 93_LVBus0447724_consumption, 93_LVBus0447724_production, 93_LVBus0447725_production, 93_LVBus0447726_consumption, 93_LVBus0447726_production, 93_LVBus0447727_production, 93_LVBus0447728_production, 93_LVBus0447730_consumption, 93_LVBus0447730_production, 93_LVBus0447731_consumption, 93_LVBus0447731_production, 93_LVBus0447732_consumption, 93_LVBus0447732_production, 93_LVBus0447733_production, 93_LVBus0447735_consumption, 93_LVBus0447735_production, 93_LVBus0447736_production, 93_LVBus0447737_production, 93_LVBus0447738_production, 93_LVBus0447739_production, 93_LVBus0447740_production, 93_LVBus0447741_production, 93_LVBus0447742_consumption, 93_LVBus0447742_production, 93_LVBus0447743_production, 93_LVBus0447744_production, 93_LVBus0447745_production, 93_LVBus0447746_production, 93_LVBus0447748_consumption, 93_LVBus0447748_production, 93_LVBus0447749_production, 93_LVBus0447750_production, 93_LVBus0447751_production, 93_LVBus0447752_production, 93_LVBus0447753_consumption, 93_LVBus0447753_production, 93_LVBus0447754_production, 93_LVBus0447755_production, 93_LVBus0447756_production, 93_LVBus0447758_consumption, 93_LVBus0447758_production, 93_LVBus0447759_production, 93_LVBus0447760_production, 93_LVBus0447762_consumption, 93_LVBus0447762_production, 93_LVBus0447763_consumption, 93_LVBus0447763_production, 93_LVBus0447764_consumption, 93_LVBus0447764_production, 93_LVBus0447765_production, 93_LVBus0447767_production, 93_LVBus0447768_consumption, 93_LVBus0447768_production, 93_LVBus0447769_production, 93_LVBus0447770_production, 93_LVBus0447771_production, 93_LVBus0447772_production, 93_LVBus0447773_production, 93_LVBus0447774_production, 93_LVBus0447775_production, 93_LVBus0447776_production, 93_LVBus0447777_production, 93_LVBus0447778_production, 93_LVBus0447779_production, 93_LVBus0447780_production, 93_LVBus0447781_production, 93_LVBus0447782_production, 93_LVBus0447783_production, 93_LVBus0447784_production, 93_LVBus0447785_production, 93_LVBus0447787_production, 93_LVBus0447789_consumption, 93_LVBus0447789_production, 93_LVBus0447790_consumption, 93_LVBus0447790_production, 93_LVBus0447791_consumption, 93_LVBus0447791_production, 93_LVBus0447792_consumption, 93_LVBus0447792_production, 93_LVBus0447793_consumption, 93_LVBus0447793_production, 93_LVBus0447795_consumption, 93_LVBus0447795_production, 93_LVBus0447796_production, 93_LVBus0447797_production, 93_LVBus0447799_consumption, 93_LVBus0447799_production, 93_LVBus0447800_production, 93_LVBus0447801_consumption, 93_LVBus0447801_production, 93_LVBus0447803_consumption, 93_LVBus0447803_production, 93_LVBus0447804_production, 93_LVBus0447805_production, 93_LVBus0447806_production, 93_LVBus0447807_production, 93_LVBus0447808_production, 93_LVBus0447809_production, 93_LVBus0447810_production, 93_LVBus0447811_production, 93_LVBus0447812_production, 93_LVBus0447814_production, 93_LVBus0447816_consumption, 93_LVBus0447816_production, 93_LVBus0447817_consumption, 93_LVBus0447817_production, 93_LVBus0447818_consumption, 93_LVBus0447818_production, 93_LVBus0447820_consumption, 93_LVBus0447820_production, 93_LVBus0447822_consumption, 93_LVBus0447822_production, 93_LVBus0447823_consumption, 93_LVBus0447823_production, 93_LVBus0447824_consumption, 93_LVBus0447824_production, 93_LVBus0447826_production, 93_LVBus0447828_consumption, 93_LVBus0447828_production, 93_LVBus0447829_production, 93_LVBus0447830_consumption, 93_LVBus0447830_production, 93_LVBus0447832_consumption, 93_LVBus0447832_production, 93_LVBus0447834_production, 93_LVBus0447835_consumption, 93_LVBus0447835_production, 93_LVBus0447836_consumption, 93_LVBus0447836_production, 93_LVBus0447837_consumption, 93_LVBus0447837_production, 93_LVBus0447839_production, 93_LVBus0447840_consumption, 93_LVBus0447840_production, 93_LVBus0447842_consumption, 93_LVBus0447842_production, 93_LVBus0447844_consumption, 93_LVBus0447844_production, 93_LVBus0447845_consumption, 93_LVBus0447845_production, 93_LVBus0447846_consumption, 93_LVBus0447846_production, 93_LVBus0447848_consumption, 93_LVBus0447848_production, 93_LVBus0447850_production, 93_LVBus0447851_production, 93_LVBus0447853_consumption, 93_LVBus0447853_production, 93_LVBus0447855_consumption, 93_LVBus0447855_production, 93_LVBus0447857_consumption, 93_LVBus0447857_production, 93_LVBus0447858_production, 93_LVBus0447860_consumption, 93_LVBus0447860_production, 93_LVBus0447861_consumption, 93_LVBus0447861_production, 93_LVBus0447863_consumption, 93_LVBus0447863_production, 93_LVBus0447865_consumption, 93_LVBus0447865_production, 93_LVBus0447867_consumption, 93_LVBus0447867_production, 93_LVBus0447869_production, 93_LVBus0447871_consumption, 93_LVBus0447871_production, 93_LVBus0447873_consumption, 93_LVBus0447873_production, 93_LVBus0447875_consumption, 93_LVBus0447875_production, 93_LVBus0447876_production, 93_LVBus0447877_production, 93_LVBus0447879_consumption, 93_LVBus0447879_production, 93_LVBus0447880_consumption, 93_LVBus0447880_production, 93_LVBus0447881_consumption, 93_LVBus0447881_production, 93_LVBus0447882_production, 93_LVBus0447883_production, 93_LVBus0447884_production, 93_LVBus0447885_consumption, 93_LVBus0447885_production, 93_LVBus0447886_production, 93_LVBus0447887_production, 93_LVBus0447888_production, 93_LVBus0447889_production, 93_LVBus0447891_consumption, 93_LVBus0447891_production, 93_LVBus0447892_production, 93_LVBus0447893_production, 93_LVBus0447894_consumption, 93_LVBus0447894_production, 93_LVBus0447896_consumption, 93_LVBus0447896_production, 93_LVBus0447898_consumption, 93_LVBus0447898_production, 93_LVBus0447899_consumption, 93_LVBus0447899_production, 93_LVBus0447901_production, 93_LVBus0447903_production, 93_LVBus0447905_production, 93_LVBus0447906_consumption, 93_LVBus0447906_production, 93_LVBus0447908_consumption, 93_LVBus0447908_production, 93_LVBus0447910_consumption, 93_LVBus0447910_production, 93_LVBus0447912_consumption, 93_LVBus0447912_production, 93_LVBus0447913_consumption, 93_LVBus0447913_production, 93_LVBus0447914_production, 93_LVBus0447915_consumption, 93_LVBus0447915_production, 93_LVBus0447916_consumption, 93_LVBus0447916_production, 93_LVBus0447917_consumption, 93_LVBus0447917_production, 93_LVBus0447918_consumption, 93_LVBus0447918_production, 93_LVBus0447919_consumption, 93_LVBus0447919_production, 93_LVBus0447920_consumption, 93_LVBus0447920_production, 93_LVBus0447922_production, 93_LVBus0447923_production, 93_LVBus0447924_consumption, 93_LVBus0447924_production, 93_LVBus0447925_production, 93_LVBus0447927_consumption, 93_LVBus0447927_production, 93_LVBus0447929_consumption, 93_LVBus0447929_production, 93_LVBus0447930_consumption, 93_LVBus0447930_production, 93_LVBus0447931_production, 93_LVBus0447932_consumption, 93_LVBus0447932_production, 93_LVBus0447933_production, 93_LVBus0447934_consumption, 93_LVBus0447934_production, 93_LVBus0447936_production, 93_LVBus0447937_consumption, 93_LVBus0447937_production, 93_LVBus0447938_consumption, 93_LVBus0447938_production, 93_LVBus0447939_production, 93_LVBus0447941_consumption, 93_LVBus0447941_production, 93_LVBus0447942_production, 93_LVBus0447943_production, 93_LVBus0447944_production, 93_LVBus0447946_consumption, 93_LVBus0447946_production, 93_LVBus0447947_production, 93_LVBus0447948_consumption, 93_LVBus0447948_production, 93_LVBus0447950_production, 93_LVBus0447951_consumption, 93_LVBus0447951_production, 93_LVBus0447953_consumption, 93_LVBus0447953_production, 93_LVBus0447954_production, 93_LVBus0447956_production, 93_LVBus0447957_production, 93_LVBus0447959_consumption, 93_LVBus0447959_production, 93_LVBus0447960_consumption, 93_LVBus0447960_production, 93_LVBus0447962_production, 93_LVBus0447963_consumption, 93_LVBus0447963_production, 93_LVBus0447964_production, 93_LVBus0447966_consumption, 93_LVBus0447966_production, 93_LVBus0447967_production, 93_LVBus0447968_consumption, 93_LVBus0447968_production, 93_LVBus0447970_consumption, 93_LVBus0447970_production, 93_LVBus0447971_consumption, 93_LVBus0447971_production, 93_LVBus0447972_consumption, 93_LVBus0447972_production, 93_LVBus0447973_consumption, 93_LVBus0447973_production, 93_LVBus0447974_production, 93_LVBus0447975_production, 93_LVBus0447976_production, 93_LVBus0447977_consumption, 93_LVBus0447977_production, 93_LVBus0447979_production, 93_LVBus0447980_production, 93_LVBus0447981_production, 93_LVBus0447983_consumption, 93_LVBus0447983_production, 93_LVBus0447984_production, 93_LVBus0447987_consumption, 93_LVBus0447987_production, 93_LVBus0447989_consumption, 93_LVBus0447989_production, 93_LVBus0447990_consumption, 93_LVBus0447990_production, 93_LVBus0447991_production, 93_LVBus0447992_consumption, 93_LVBus0447992_production, 93_LVBus0447993_consumption, 93_LVBus0447993_production, 93_LVBus0447994_consumption, 93_LVBus0447994_production, 93_LVBus0447996_consumption, 93_LVBus0447996_production, 93_LVBus0447998_production, 93_LVBus0448000_production, 93_LVBus0448001_production, 93_LVBus0448003_production, 93_LVBus0448005_consumption, 93_LVBus0448005_production, 93_LVBus0448006_production, 93_LVBus0448008_production, 93_LVBus0448010_consumption, 93_LVBus0448010_production, 93_LVBus0448011_consumption, 93_LVBus0448011_production, 93_LVBus0448013_consumption, 93_LVBus0448013_production, 93_LVBus0448014_consumption, 93_LVBus0448014_production, 93_LVBus0448015_consumption, 93_LVBus0448015_production, 93_LVBus0448016_consumption, 93_LVBus0448016_production, 93_LVBus0448017_production, 93_LVBus0448019_consumption, 93_LVBus0448019_production, 93_LVBus0448020_consumption, 93_LVBus0448020_production, 93_LVBus0448021_consumption, 93_LVBus0448021_production, 93_LVBus0448022_consumption, 93_LVBus0448022_production, 93_LVBus0448023_consumption, 93_LVBus0448023_production, 93_LVBus0448024_production, 93_LVBus0448025_production, 93_LVBus0448026_production, 93_LVBus0448027_consumption, 93_LVBus0448027_production, 93_LVBus0448028_production, 93_LVBus0448030_consumption, 93_LVBus0448030_production, 93_LVBus0448031_consumption, 93_LVBus0448031_production, 93_LVBus0448032_consumption, 93_LVBus0448032_production, 93_LVBus0448034_consumption, 93_LVBus0448034_production, 93_LVBus0448035_consumption, 93_LVBus0448035_production, 93_LVBus0448037_consumption, 93_LVBus0448037_production, 93_LVBus0448038_production, 93_LVBus0448039_consumption, 93_LVBus0448039_production, 93_LVBus0448042_production, 93_LVBus0448043_consumption, 93_LVBus0448043_production, 93_LVBus0448044_production, 93_LVBus0448045_consumption, 93_LVBus0448045_production, 93_LVBus0448047_production, 93_LVBus0448048_consumption, 93_LVBus0448048_production, 93_LVBus0448049_consumption, 93_LVBus0448049_production, 93_LVBus0448050_production, 93_LVBus0448051_consumption, 93_LVBus0448051_production, 93_LVBus0448052_production, 93_LVBus0448053_consumption, 93_LVBus0448053_production, 93_LVBus0448054_consumption, 93_LVBus0448054_production, 93_LVBus0448055_production, 93_LVBus0448056_consumption, 93_LVBus0448056_production, 93_LVBus0448058_consumption, 93_LVBus0448058_production, 93_LVBus0448060_consumption, 93_LVBus0448060_production, 93_LVBus0448061_consumption, 93_LVBus0448061_production, 93_LVBus0448062_consumption, 93_LVBus0448062_production, 93_LVBus0448063_consumption, 93_LVBus0448063_production, 93_LVBus0448064_consumption, 93_LVBus0448064_production, 93_LVBus0448065_consumption, 93_LVBus0448065_production, 93_LVBus0448066_consumption, 93_LVBus0448066_production, 93_LVBus0448067_consumption, 93_LVBus0448067_production, 93_LVBus0448068_production, 93_LVBus0448069_production, 93_LVBus0448070_production, 93_LVBus0448071_consumption, 93_LVBus0448071_production, 93_LVBus0448072_consumption, 93_LVBus0448072_production, 93_LVBus0448073_consumption, 93_LVBus0448073_production, 93_LVBus0448074_production, 93_LVBus0448076_production, 93_LVBus0448078_consumption, 93_LVBus0448078_production, 93_LVBus0448079_production, 93_LVBus0448080_production, 93_LVBus0448081_production, 93_LVBus0448083_production, 93_LVBus0448085_production, 93_LVBus0448087_consumption, 93_LVBus0448087_production, 93_MVLV02082_consumption, 93_MVLV02082_production, 93_MVLV40671_production.

