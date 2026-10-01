# BMOPF Network Summary: 75_MVFeeder3206

**Generated:** 2026-10-01 23:34:26  
**Findings:** 0 errors · 5 warnings · 312 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 31 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 502 |  |
| line | 470 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 800 | 2.018 MW, 605.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 31 |  |
| switch | 0 |  |
| transformer | 31 | Dyn11×31 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 76 | 75 | 10 | 0 |
| LV_236V | 236.0 V | 426 | 395 | 790 | 0 |

**Transformer transitions:**

- `75_MVLV065510_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064523_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066173_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV088919_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV086361_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV009859_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV085761_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV063193_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV116188_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV017611_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV086958_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV019508_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV093304_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV056650_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV042618_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV038856_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121009_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV080479_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV020186_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV043494_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV122715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV034727_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV091243_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV098609_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV059918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV139306_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121826_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV013513_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV135746_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV034726_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV019519_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 175 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 502 | 1 | 501 | 0 | 0 | 0 |
| Tier LV_236V | 426 | 31 | 395 | 0 | 0 | 0 |
| Tier MV_11.8kV | 76 | 1 | 75 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 31; skipped invalid branches: 0.

Galvanic zones: 32; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MVBus096803 | MV_11.8kV | 76 | 0 | 0 | 31 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1932 declared bus terminals; 1805 mapped line/closed-switch conductor edges; 127 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 48700.0 | 3.244 | 2400 |
| q_nom | 0.0 | 14600.0 | 3.244 | 2400 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.867 | 3710.0 | 2.011 | 470 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.584 | 31 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 492 of 800 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392686_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392809_consumption' has phase imbalance of 20.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392738_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392889_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392870_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392910_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392543_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2009143_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1977264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392536_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392909_consumption' has phase imbalance of 93.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392559_consumption' has phase imbalance of 26.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392656_consumption' has phase imbalance of 206.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392843_consumption' has phase imbalance of 248.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392695_consumption' has phase imbalance of 131.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392602_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392825_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392796_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392853_consumption' has phase imbalance of 147.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392877_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392759_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392510_consumption' has phase imbalance of 249.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392832_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392605_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392540_consumption' has phase imbalance of 111.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1994615_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392619_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392753_consumption' has phase imbalance of 248.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392621_consumption' has phase imbalance of 225.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392893_consumption' has phase imbalance of 113.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392712_consumption' has phase imbalance of 60.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392912_consumption' has phase imbalance of 263.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1977265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1977266_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392913_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392495_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392610_consumption' has phase imbalance of 261.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392558_consumption' has phase imbalance of 184.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392786_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392571_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392549_consumption' has phase imbalance of 91.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392895_consumption' has phase imbalance of 145.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1992741_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392891_consumption' has phase imbalance of 114.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1977045_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392489_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392818_consumption' has phase imbalance of 29.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392856_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392586_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392718_consumption' has phase imbalance of 156.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392682_consumption' has phase imbalance of 194.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392608_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392763_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392677_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392482_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392494_consumption' has phase imbalance of 282.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392855_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392573_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1939291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392574_consumption' has phase imbalance of 163.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392788_consumption' has phase imbalance of 138.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392638_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392644_consumption' has phase imbalance of 229.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392858_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392826_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392523_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392701_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1965258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392752_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392694_consumption' has phase imbalance of 58.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392600_consumption' has phase imbalance of 53.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392874_consumption' has phase imbalance of 200.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392552_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392916_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392876_consumption' has phase imbalance of 55.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392620_consumption' has phase imbalance of 201.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392762_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392740_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392869_consumption' has phase imbalance of 237.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392707_consumption' has phase imbalance of 195.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392736_consumption' has phase imbalance of 91.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392719_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1977267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392761_consumption' has phase imbalance of 26.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2004552_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392532_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392754_consumption' has phase imbalance of 53.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1981698_consumption' has phase imbalance of 239.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392846_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392603_consumption' has phase imbalance of 207.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392838_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1965257_consumption' has phase imbalance of 266.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392604_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392538_consumption' has phase imbalance of 228.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392631_consumption' has phase imbalance of 220.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392844_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392561_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392799_consumption' has phase imbalance of 87.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1977268_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392566_consumption' has phase imbalance of 227.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1994616_consumption' has phase imbalance of 256.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392601_consumption' has phase imbalance of 254.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392915_consumption' has phase imbalance of 179.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392911_consumption' has phase imbalance of 183.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392739_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392634_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392645_consumption' has phase imbalance of 206.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392562_consumption' has phase imbalance of 287.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392622_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392567_consumption' has phase imbalance of 89.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392521_consumption' has phase imbalance of 228.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1965256_consumption' has phase imbalance of 230.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1994612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392773_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392485_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392899_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392729_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392866_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392901_consumption' has phase imbalance of 103.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1994617_consumption' has phase imbalance of 248.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392646_consumption' has phase imbalance of 206.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392669_consumption' has phase imbalance of 242.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392508_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392647_consumption' has phase imbalance of 243.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392516_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392488_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392672_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392519_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392795_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392625_consumption' has phase imbalance of 105.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392530_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392548_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392864_consumption' has phase imbalance of 53.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392733_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392784_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392727_consumption' has phase imbalance of 237.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392676_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1981700_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392681_consumption' has phase imbalance of 109.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392900_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392852_consumption' has phase imbalance of 246.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392879_consumption' has phase imbalance of 75.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392580_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392674_consumption' has phase imbalance of 123.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392732_consumption' has phase imbalance of 232.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392572_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392505_consumption' has phase imbalance of 95.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392747_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392811_consumption' has phase imbalance of 239.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392841_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392491_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392525_consumption' has phase imbalance of 109.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392794_consumption' has phase imbalance of 221.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392757_consumption' has phase imbalance of 265.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1994613_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392692_consumption' has phase imbalance of 186.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392806_consumption' has phase imbalance of 62.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392613_consumption' has phase imbalance of 229.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392708_consumption' has phase imbalance of 203.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392760_consumption' has phase imbalance of 145.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392749_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392688_consumption' has phase imbalance of 62.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392917_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392668_consumption' has phase imbalance of 64.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392479_consumption' has phase imbalance of 227.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392680_consumption' has phase imbalance of 281.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392648_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392478_consumption' has phase imbalance of 234.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392868_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392769_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392848_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392723_consumption' has phase imbalance of 61.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392875_consumption' has phase imbalance of 79.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392871_consumption' has phase imbalance of 106.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392629_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392529_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392764_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392531_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392724_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392746_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392802_consumption' has phase imbalance of 48.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392787_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392640_consumption' has phase imbalance of 24.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392570_consumption' has phase imbalance of 185.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1981697_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392643_consumption' has phase imbalance of 118.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392726_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392657_consumption' has phase imbalance of 114.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392642_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392867_consumption' has phase imbalance of 247.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392882_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392880_consumption' has phase imbalance of 213.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392697_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392812_consumption' has phase imbalance of 24.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392504_consumption' has phase imbalance of 43.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392535_consumption' has phase imbalance of 244.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392689_consumption' has phase imbalance of 247.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392768_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392696_consumption' has phase imbalance of 29.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392831_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392804_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392698_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392857_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392533_consumption' has phase imbalance of 269.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392550_consumption' has phase imbalance of 134.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392872_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392837_consumption' has phase imbalance of 269.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392564_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392785_consumption' has phase imbalance of 98.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0392881_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 800 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_POMER' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0392650' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.018 MW |
| Total load Q | 605.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV065510_Transformer | 275.0 kVA | 21.3% |
| 75_MVLV064523_Transformer | 440.0 kVA | 24.2% |
| 75_MVLV066173_Transformer | 275.0 kVA | 18.2% |
| 75_MVLV088919_Transformer | 275.0 kVA | 24.7% |
| 75_MVLV086361_Transformer | 693.0 kVA | 20.9% |
| 75_MVLV009859_Transformer | 275.0 kVA | 12.5% |
| 75_MVLV085761_Transformer | 176.0 kVA | 11.0% |
| 75_MVLV063193_Transformer | 176.0 kVA | 14.2% |
| 75_MVLV116188_Transformer | 275.0 kVA | 16.9% |
| 75_MVLV017611_Transformer | 275.0 kVA | 16.4% |
| 75_MVLV086958_Transformer | 275.0 kVA | 11.9% |
| 75_MVLV019508_Transformer | 275.0 kVA | 16.0% |
| 75_MVLV093304_Transformer | 176.0 kVA | 6.1% |
| 75_MVLV056650_Transformer | 110.0 kVA | 9.6% |
| 75_MVLV042618_Transformer | 440.0 kVA | 16.9% |
| 75_MVLV038856_Transformer | 440.0 kVA | 17.4% |
| 75_MVLV121009_Transformer | 275.0 kVA | 18.5% |
| 75_MVLV080479_Transformer | 440.0 kVA | 22.1% |
| 75_MVLV020186_Transformer | 440.0 kVA | 23.0% |
| 75_MVLV043494_Transformer | 110.0 kVA | 2.8% |
| 75_MVLV122715_Transformer | 275.0 kVA | 20.1% |
| 75_MVLV034727_Transformer | 693.0 kVA | 14.3% |
| 75_MVLV091243_Transformer | 1.1 MVA | 20.4% |
| 75_MVLV098609_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV059918_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV139306_Transformer | 440.0 kVA | 13.0% |
| 75_MVLV121826_Transformer | 440.0 kVA | 38.9% |
| 75_MVLV013513_Transformer | 440.0 kVA | 17.7% |
| 75_MVLV135746_Transformer | 275.0 kVA | 8.0% |
| 75_MVLV034726_Transformer | 693.0 kVA | 17.1% |
| 75_MVLV019519_Transformer | 275.0 kVA | 10.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.02 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_POMER' (MV, 11.78 kV) has an electrical reach of 21.79 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0392650' (LV, 0.24 kV) has an electrical reach of 18.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 502 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 502 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 31 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 76 |
| LV_236V | 4-wire | 426 / 426 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 426 |
| Neutral branches | 395 |
| Grounding points | 31 |
| Neutral sections | 31 |
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
| 11.78 kV | 76 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 32 |
| Islands without voltage reference | 0 |
| Line impedance spread | 3270.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 426 / 76 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 493 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 493 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0392478_production, 75_LVBus0392479_production, 75_LVBus0392480_production, 75_LVBus0392481_consumption, 75_LVBus0392481_production, 75_LVBus0392482_production, 75_LVBus0392484_consumption, 75_LVBus0392484_production, 75_LVBus0392485_production, 75_LVBus0392486_production, 75_LVBus0392487_consumption, 75_LVBus0392487_production, 75_LVBus0392488_production, 75_LVBus0392489_production, 75_LVBus0392490_production, 75_LVBus0392491_production, 75_LVBus0392493_production, 75_LVBus0392494_production, 75_LVBus0392495_production, 75_LVBus0392496_production, 75_LVBus0392497_consumption, 75_LVBus0392497_production, 75_LVBus0392498_production, 75_LVBus0392499_consumption, 75_LVBus0392499_production, 75_LVBus0392500_production, 75_LVBus0392501_production, 75_LVBus0392503_consumption, 75_LVBus0392503_production, 75_LVBus0392504_production, 75_LVBus0392505_production, 75_LVBus0392506_production, 75_LVBus0392507_production, 75_LVBus0392508_production, 75_LVBus0392509_production, 75_LVBus0392510_production, 75_LVBus0392512_production, 75_LVBus0392513_production, 75_LVBus0392514_consumption, 75_LVBus0392514_production, 75_LVBus0392515_consumption, 75_LVBus0392515_production, 75_LVBus0392516_production, 75_LVBus0392517_production, 75_LVBus0392518_production, 75_LVBus0392519_production, 75_LVBus0392521_production, 75_LVBus0392523_production, 75_LVBus0392524_consumption, 75_LVBus0392524_production, 75_LVBus0392525_production, 75_LVBus0392526_production, 75_LVBus0392527_consumption, 75_LVBus0392527_production, 75_LVBus0392529_production, 75_LVBus0392530_production, 75_LVBus0392531_production, 75_LVBus0392532_production, 75_LVBus0392533_production, 75_LVBus0392535_production, 75_LVBus0392536_production, 75_LVBus0392537_production, 75_LVBus0392538_production, 75_LVBus0392539_production, 75_LVBus0392540_production, 75_LVBus0392541_consumption, 75_LVBus0392541_production, 75_LVBus0392542_consumption, 75_LVBus0392542_production, 75_LVBus0392543_production, 75_LVBus0392545_production, 75_LVBus0392546_production, 75_LVBus0392547_consumption, 75_LVBus0392547_production, 75_LVBus0392548_production, 75_LVBus0392549_production, 75_LVBus0392550_production, 75_LVBus0392551_production, 75_LVBus0392552_production, 75_LVBus0392553_consumption, 75_LVBus0392553_production, 75_LVBus0392554_consumption, 75_LVBus0392554_production, 75_LVBus0392555_consumption, 75_LVBus0392555_production, 75_LVBus0392556_consumption, 75_LVBus0392556_production, 75_LVBus0392558_production, 75_LVBus0392559_production, 75_LVBus0392560_consumption, 75_LVBus0392560_production, 75_LVBus0392561_production, 75_LVBus0392562_production, 75_LVBus0392563_consumption, 75_LVBus0392563_production, 75_LVBus0392564_production, 75_LVBus0392565_consumption, 75_LVBus0392565_production, 75_LVBus0392566_production, 75_LVBus0392567_production, 75_LVBus0392568_consumption, 75_LVBus0392568_production, 75_LVBus0392569_production, 75_LVBus0392570_production, 75_LVBus0392571_production, 75_LVBus0392572_production, 75_LVBus0392573_production, 75_LVBus0392574_production, 75_LVBus0392575_production, 75_LVBus0392579_production, 75_LVBus0392580_production, 75_LVBus0392581_consumption, 75_LVBus0392581_production, 75_LVBus0392582_consumption, 75_LVBus0392582_production, 75_LVBus0392583_production, 75_LVBus0392584_production, 75_LVBus0392585_production, 75_LVBus0392586_production, 75_LVBus0392588_consumption, 75_LVBus0392588_production, 75_LVBus0392590_consumption, 75_LVBus0392590_production, 75_LVBus0392592_production, 75_LVBus0392593_production, 75_LVBus0392594_consumption, 75_LVBus0392594_production, 75_LVBus0392596_consumption, 75_LVBus0392596_production, 75_LVBus0392598_consumption, 75_LVBus0392598_production, 75_LVBus0392600_production, 75_LVBus0392601_production, 75_LVBus0392602_production, 75_LVBus0392603_production, 75_LVBus0392604_production, 75_LVBus0392605_production, 75_LVBus0392606_production, 75_LVBus0392608_production, 75_LVBus0392609_consumption, 75_LVBus0392609_production, 75_LVBus0392610_production, 75_LVBus0392611_production, 75_LVBus0392612_production, 75_LVBus0392613_production, 75_LVBus0392614_production, 75_LVBus0392618_production, 75_LVBus0392619_production, 75_LVBus0392620_production, 75_LVBus0392621_production, 75_LVBus0392622_production, 75_LVBus0392623_consumption, 75_LVBus0392623_production, 75_LVBus0392624_production, 75_LVBus0392625_production, 75_LVBus0392627_production, 75_LVBus0392628_consumption, 75_LVBus0392628_production, 75_LVBus0392629_production, 75_LVBus0392631_production, 75_LVBus0392632_production, 75_LVBus0392633_production, 75_LVBus0392634_production, 75_LVBus0392635_production, 75_LVBus0392637_production, 75_LVBus0392638_production, 75_LVBus0392639_production, 75_LVBus0392640_production, 75_LVBus0392641_consumption, 75_LVBus0392641_production, 75_LVBus0392642_production, 75_LVBus0392643_production, 75_LVBus0392644_production, 75_LVBus0392645_production, 75_LVBus0392646_production, 75_LVBus0392647_production, 75_LVBus0392648_production, 75_LVBus0392650_production, 75_LVBus0392652_consumption, 75_LVBus0392652_production, 75_LVBus0392653_consumption, 75_LVBus0392653_production, 75_LVBus0392654_production, 75_LVBus0392655_consumption, 75_LVBus0392655_production, 75_LVBus0392656_production, 75_LVBus0392657_production, 75_LVBus0392659_consumption, 75_LVBus0392659_production, 75_LVBus0392661_consumption, 75_LVBus0392661_production, 75_LVBus0392662_consumption, 75_LVBus0392662_production, 75_LVBus0392663_consumption, 75_LVBus0392663_production, 75_LVBus0392665_consumption, 75_LVBus0392665_production, 75_LVBus0392666_consumption, 75_LVBus0392666_production, 75_LVBus0392667_consumption, 75_LVBus0392667_production, 75_LVBus0392668_production, 75_LVBus0392669_production, 75_LVBus0392670_consumption, 75_LVBus0392670_production, 75_LVBus0392671_consumption, 75_LVBus0392671_production, 75_LVBus0392672_production, 75_LVBus0392674_production, 75_LVBus0392676_production, 75_LVBus0392677_production, 75_LVBus0392678_production, 75_LVBus0392679_production, 75_LVBus0392680_production, 75_LVBus0392681_production, 75_LVBus0392682_production, 75_LVBus0392683_production, 75_LVBus0392684_production, 75_LVBus0392685_consumption, 75_LVBus0392685_production, 75_LVBus0392686_production, 75_LVBus0392687_production, 75_LVBus0392688_production, 75_LVBus0392689_production, 75_LVBus0392690_production, 75_LVBus0392691_consumption, 75_LVBus0392691_production, 75_LVBus0392692_production, 75_LVBus0392694_production, 75_LVBus0392695_production, 75_LVBus0392696_production, 75_LVBus0392697_production, 75_LVBus0392698_production, 75_LVBus0392700_consumption, 75_LVBus0392700_production, 75_LVBus0392701_production, 75_LVBus0392702_production, 75_LVBus0392703_consumption, 75_LVBus0392703_production, 75_LVBus0392704_consumption, 75_LVBus0392704_production, 75_LVBus0392705_consumption, 75_LVBus0392705_production, 75_LVBus0392707_production, 75_LVBus0392708_production, 75_LVBus0392710_consumption, 75_LVBus0392710_production, 75_LVBus0392711_consumption, 75_LVBus0392711_production, 75_LVBus0392712_production, 75_LVBus0392713_production, 75_LVBus0392714_production, 75_LVBus0392716_production, 75_LVBus0392718_production, 75_LVBus0392719_production, 75_LVBus0392720_consumption, 75_LVBus0392720_production, 75_LVBus0392721_production, 75_LVBus0392723_production, 75_LVBus0392724_production, 75_LVBus0392725_production, 75_LVBus0392726_production, 75_LVBus0392727_production, 75_LVBus0392728_production, 75_LVBus0392729_production, 75_LVBus0392730_production, 75_LVBus0392732_production, 75_LVBus0392733_production, 75_LVBus0392734_production, 75_LVBus0392735_consumption, 75_LVBus0392735_production, 75_LVBus0392736_production, 75_LVBus0392737_consumption, 75_LVBus0392737_production, 75_LVBus0392738_production, 75_LVBus0392739_production, 75_LVBus0392740_production, 75_LVBus0392741_production, 75_LVBus0392742_production, 75_LVBus0392746_production, 75_LVBus0392747_production, 75_LVBus0392748_production, 75_LVBus0392749_production, 75_LVBus0392750_consumption, 75_LVBus0392750_production, 75_LVBus0392752_production, 75_LVBus0392753_production, 75_LVBus0392754_production, 75_LVBus0392756_production, 75_LVBus0392757_production, 75_LVBus0392758_consumption, 75_LVBus0392758_production, 75_LVBus0392759_production, 75_LVBus0392760_production, 75_LVBus0392761_production, 75_LVBus0392762_production, 75_LVBus0392763_production, 75_LVBus0392764_production, 75_LVBus0392766_production, 75_LVBus0392767_production, 75_LVBus0392768_production, 75_LVBus0392769_production, 75_LVBus0392771_consumption, 75_LVBus0392771_production, 75_LVBus0392772_production, 75_LVBus0392773_production, 75_LVBus0392774_production, 75_LVBus0392775_production, 75_LVBus0392776_consumption, 75_LVBus0392776_production, 75_LVBus0392777_production, 75_LVBus0392778_consumption, 75_LVBus0392778_production, 75_LVBus0392779_production, 75_LVBus0392781_production, 75_LVBus0392782_consumption, 75_LVBus0392782_production, 75_LVBus0392783_consumption, 75_LVBus0392783_production, 75_LVBus0392784_production, 75_LVBus0392785_production, 75_LVBus0392786_production, 75_LVBus0392787_production, 75_LVBus0392788_production, 75_LVBus0392790_consumption, 75_LVBus0392790_production, 75_LVBus0392792_consumption, 75_LVBus0392792_production, 75_LVBus0392793_production, 75_LVBus0392794_production, 75_LVBus0392795_production, 75_LVBus0392796_production, 75_LVBus0392798_production, 75_LVBus0392799_production, 75_LVBus0392800_production, 75_LVBus0392801_production, 75_LVBus0392802_production, 75_LVBus0392803_consumption, 75_LVBus0392803_production, 75_LVBus0392804_production, 75_LVBus0392806_production, 75_LVBus0392807_production, 75_LVBus0392808_consumption, 75_LVBus0392808_production, 75_LVBus0392809_production, 75_LVBus0392810_production, 75_LVBus0392811_production, 75_LVBus0392812_production, 75_LVBus0392813_production, 75_LVBus0392815_production, 75_LVBus0392817_consumption, 75_LVBus0392817_production, 75_LVBus0392818_production, 75_LVBus0392819_production, 75_LVBus0392820_consumption, 75_LVBus0392820_production, 75_LVBus0392821_consumption, 75_LVBus0392821_production, 75_LVBus0392822_consumption, 75_LVBus0392822_production, 75_LVBus0392823_consumption, 75_LVBus0392823_production, 75_LVBus0392824_consumption, 75_LVBus0392824_production, 75_LVBus0392825_production, 75_LVBus0392826_production, 75_LVBus0392827_production, 75_LVBus0392829_consumption, 75_LVBus0392829_production, 75_LVBus0392830_consumption, 75_LVBus0392830_production, 75_LVBus0392831_production, 75_LVBus0392832_production, 75_LVBus0392833_production, 75_LVBus0392835_consumption, 75_LVBus0392835_production, 75_LVBus0392837_production, 75_LVBus0392838_production, 75_LVBus0392839_production, 75_LVBus0392840_production, 75_LVBus0392841_production, 75_LVBus0392843_production, 75_LVBus0392844_production, 75_LVBus0392845_production, 75_LVBus0392846_production, 75_LVBus0392847_consumption, 75_LVBus0392847_production, 75_LVBus0392848_production, 75_LVBus0392849_production, 75_LVBus0392852_production, 75_LVBus0392853_production, 75_LVBus0392854_consumption, 75_LVBus0392854_production, 75_LVBus0392855_production, 75_LVBus0392856_production, 75_LVBus0392857_production, 75_LVBus0392858_production, 75_LVBus0392859_consumption, 75_LVBus0392859_production, 75_LVBus0392860_production, 75_LVBus0392862_consumption, 75_LVBus0392862_production, 75_LVBus0392864_production, 75_LVBus0392865_production, 75_LVBus0392866_production, 75_LVBus0392867_production, 75_LVBus0392868_production, 75_LVBus0392869_production, 75_LVBus0392870_production, 75_LVBus0392871_production, 75_LVBus0392872_production, 75_LVBus0392874_production, 75_LVBus0392875_production, 75_LVBus0392876_production, 75_LVBus0392877_production, 75_LVBus0392879_production, 75_LVBus0392880_production, 75_LVBus0392881_production, 75_LVBus0392882_production, 75_LVBus0392884_consumption, 75_LVBus0392884_production, 75_LVBus0392885_consumption, 75_LVBus0392885_production, 75_LVBus0392888_production, 75_LVBus0392889_production, 75_LVBus0392890_consumption, 75_LVBus0392890_production, 75_LVBus0392891_production, 75_LVBus0392892_production, 75_LVBus0392893_production, 75_LVBus0392894_consumption, 75_LVBus0392894_production, 75_LVBus0392895_production, 75_LVBus0392896_production, 75_LVBus0392897_production, 75_LVBus0392899_production, 75_LVBus0392900_production, 75_LVBus0392901_production, 75_LVBus0392903_consumption, 75_LVBus0392903_production, 75_LVBus0392905_consumption, 75_LVBus0392905_production, 75_LVBus0392907_consumption, 75_LVBus0392907_production, 75_LVBus0392909_production, 75_LVBus0392910_production, 75_LVBus0392911_production, 75_LVBus0392912_production, 75_LVBus0392913_production, 75_LVBus0392915_production, 75_LVBus0392916_production, 75_LVBus0392917_production, 75_LVBus0392918_production, 75_LVBus0392919_production, 75_LVBus1939291_production, 75_LVBus1953818_production, 75_LVBus1965256_production, 75_LVBus1965257_production, 75_LVBus1965258_production, 75_LVBus1977045_production, 75_LVBus1977264_production, 75_LVBus1977265_production, 75_LVBus1977266_production, 75_LVBus1977267_production, 75_LVBus1977268_production, 75_LVBus1981697_production, 75_LVBus1981698_production, 75_LVBus1981699_consumption, 75_LVBus1981699_production, 75_LVBus1981700_production, 75_LVBus1982250_production, 75_LVBus1992741_production, 75_LVBus1994612_production, 75_LVBus1994613_production, 75_LVBus1994614_consumption, 75_LVBus1994614_production, 75_LVBus1994615_production, 75_LVBus1994616_production, 75_LVBus1994617_production, 75_LVBus1994618_production, 75_LVBus2004552_production, 75_LVBus2006785_consumption, 75_LVBus2006785_production, 75_LVBus2009143_production, 75_MVLV022119_production, 75_MVLV055038_consumption, 75_MVLV055038_production, 75_MVLV063757_consumption, 75_MVLV063757_production, 75_MVLV128570_consumption, 75_MVLV128570_production, 75_MVLV155338_consumption, 75_MVLV155338_production.

## 9. Data Quality Summary

**Total findings:** 317 (0 errors, 5 warnings, 312 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  492 of 800 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.02 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  493 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392686_consumption`  
  Load '75_LVBus0392686_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392896_consumption`  
  Load '75_LVBus0392896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392809_consumption`  
  Load '75_LVBus0392809_consumption' has phase imbalance of 20.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392738_consumption`  
  Load '75_LVBus0392738_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392888_consumption`  
  Load '75_LVBus0392888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392919_consumption`  
  Load '75_LVBus0392919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392889_consumption`  
  Load '75_LVBus0392889_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392870_consumption`  
  Load '75_LVBus0392870_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392910_consumption`  
  Load '75_LVBus0392910_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392501_consumption`  
  Load '75_LVBus0392501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392897_consumption`  
  Load '75_LVBus0392897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392543_consumption`  
  Load '75_LVBus0392543_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392730_consumption`  
  Load '75_LVBus0392730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2009143_consumption`  
  Load '75_LVBus2009143_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1977264_consumption`  
  Load '75_LVBus1977264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392536_consumption`  
  Load '75_LVBus0392536_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392627_consumption`  
  Load '75_LVBus0392627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392509_consumption`  
  Load '75_LVBus0392509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392909_consumption`  
  Load '75_LVBus0392909_consumption' has phase imbalance of 93.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392559_consumption`  
  Load '75_LVBus0392559_consumption' has phase imbalance of 26.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392656_consumption`  
  Load '75_LVBus0392656_consumption' has phase imbalance of 206.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392843_consumption`  
  Load '75_LVBus0392843_consumption' has phase imbalance of 248.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392695_consumption`  
  Load '75_LVBus0392695_consumption' has phase imbalance of 131.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392602_consumption`  
  Load '75_LVBus0392602_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392507_consumption`  
  Load '75_LVBus0392507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392825_consumption`  
  Load '75_LVBus0392825_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392796_consumption`  
  Load '75_LVBus0392796_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392853_consumption`  
  Load '75_LVBus0392853_consumption' has phase imbalance of 147.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392877_consumption`  
  Load '75_LVBus0392877_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392759_consumption`  
  Load '75_LVBus0392759_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392510_consumption`  
  Load '75_LVBus0392510_consumption' has phase imbalance of 249.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392635_consumption`  
  Load '75_LVBus0392635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392832_consumption`  
  Load '75_LVBus0392832_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392605_consumption`  
  Load '75_LVBus0392605_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392713_consumption`  
  Load '75_LVBus0392713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392540_consumption`  
  Load '75_LVBus0392540_consumption' has phase imbalance of 111.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392774_consumption`  
  Load '75_LVBus0392774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392637_consumption`  
  Load '75_LVBus0392637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1994615_consumption`  
  Load '75_LVBus1994615_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392619_consumption`  
  Load '75_LVBus0392619_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392490_consumption`  
  Load '75_LVBus0392490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392753_consumption`  
  Load '75_LVBus0392753_consumption' has phase imbalance of 248.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392606_consumption`  
  Load '75_LVBus0392606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392725_consumption`  
  Load '75_LVBus0392725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392621_consumption`  
  Load '75_LVBus0392621_consumption' has phase imbalance of 225.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392893_consumption`  
  Load '75_LVBus0392893_consumption' has phase imbalance of 113.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392845_consumption`  
  Load '75_LVBus0392845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392800_consumption`  
  Load '75_LVBus0392800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392712_consumption`  
  Load '75_LVBus0392712_consumption' has phase imbalance of 60.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392480_consumption`  
  Load '75_LVBus0392480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392912_consumption`  
  Load '75_LVBus0392912_consumption' has phase imbalance of 263.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1977265_consumption`  
  Load '75_LVBus1977265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1977266_consumption`  
  Load '75_LVBus1977266_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392684_consumption`  
  Load '75_LVBus0392684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392913_consumption`  
  Load '75_LVBus0392913_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392495_consumption`  
  Load '75_LVBus0392495_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392610_consumption`  
  Load '75_LVBus0392610_consumption' has phase imbalance of 261.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392612_consumption`  
  Load '75_LVBus0392612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392558_consumption`  
  Load '75_LVBus0392558_consumption' has phase imbalance of 184.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392756_consumption`  
  Load '75_LVBus0392756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392786_consumption`  
  Load '75_LVBus0392786_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392571_consumption`  
  Load '75_LVBus0392571_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392549_consumption`  
  Load '75_LVBus0392549_consumption' has phase imbalance of 91.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392632_consumption`  
  Load '75_LVBus0392632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392546_consumption`  
  Load '75_LVBus0392546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392895_consumption`  
  Load '75_LVBus0392895_consumption' has phase imbalance of 145.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392849_consumption`  
  Load '75_LVBus0392849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1992741_consumption`  
  Load '75_LVBus1992741_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392891_consumption`  
  Load '75_LVBus0392891_consumption' has phase imbalance of 114.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392777_consumption`  
  Load '75_LVBus0392777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1977045_consumption`  
  Load '75_LVBus1977045_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392489_consumption`  
  Load '75_LVBus0392489_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392818_consumption`  
  Load '75_LVBus0392818_consumption' has phase imbalance of 29.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392496_consumption`  
  Load '75_LVBus0392496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392856_consumption`  
  Load '75_LVBus0392856_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392592_consumption`  
  Load '75_LVBus0392592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392679_consumption`  
  Load '75_LVBus0392679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392586_consumption`  
  Load '75_LVBus0392586_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392718_consumption`  
  Load '75_LVBus0392718_consumption' has phase imbalance of 156.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392682_consumption`  
  Load '75_LVBus0392682_consumption' has phase imbalance of 194.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392608_consumption`  
  Load '75_LVBus0392608_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392763_consumption`  
  Load '75_LVBus0392763_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392677_consumption`  
  Load '75_LVBus0392677_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392639_consumption`  
  Load '75_LVBus0392639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392482_consumption`  
  Load '75_LVBus0392482_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392494_consumption`  
  Load '75_LVBus0392494_consumption' has phase imbalance of 282.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392855_consumption`  
  Load '75_LVBus0392855_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392573_consumption`  
  Load '75_LVBus0392573_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392767_consumption`  
  Load '75_LVBus0392767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1939291_consumption`  
  Load '75_LVBus1939291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392574_consumption`  
  Load '75_LVBus0392574_consumption' has phase imbalance of 163.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392618_consumption`  
  Load '75_LVBus0392618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392788_consumption`  
  Load '75_LVBus0392788_consumption' has phase imbalance of 138.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392638_consumption`  
  Load '75_LVBus0392638_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392644_consumption`  
  Load '75_LVBus0392644_consumption' has phase imbalance of 229.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392858_consumption`  
  Load '75_LVBus0392858_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392826_consumption`  
  Load '75_LVBus0392826_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392584_consumption`  
  Load '75_LVBus0392584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392523_consumption`  
  Load '75_LVBus0392523_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392701_consumption`  
  Load '75_LVBus0392701_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1965258_consumption`  
  Load '75_LVBus1965258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392827_consumption`  
  Load '75_LVBus0392827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392575_consumption`  
  Load '75_LVBus0392575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392752_consumption`  
  Load '75_LVBus0392752_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392694_consumption`  
  Load '75_LVBus0392694_consumption' has phase imbalance of 58.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392600_consumption`  
  Load '75_LVBus0392600_consumption' has phase imbalance of 53.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392874_consumption`  
  Load '75_LVBus0392874_consumption' has phase imbalance of 200.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392552_consumption`  
  Load '75_LVBus0392552_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392916_consumption`  
  Load '75_LVBus0392916_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392876_consumption`  
  Load '75_LVBus0392876_consumption' has phase imbalance of 55.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392860_consumption`  
  Load '75_LVBus0392860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392620_consumption`  
  Load '75_LVBus0392620_consumption' has phase imbalance of 201.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392762_consumption`  
  Load '75_LVBus0392762_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392740_consumption`  
  Load '75_LVBus0392740_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392579_consumption`  
  Load '75_LVBus0392579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392569_consumption`  
  Load '75_LVBus0392569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392869_consumption`  
  Load '75_LVBus0392869_consumption' has phase imbalance of 237.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392707_consumption`  
  Load '75_LVBus0392707_consumption' has phase imbalance of 195.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392736_consumption`  
  Load '75_LVBus0392736_consumption' has phase imbalance of 91.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392798_consumption`  
  Load '75_LVBus0392798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392719_consumption`  
  Load '75_LVBus0392719_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392500_consumption`  
  Load '75_LVBus0392500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392498_consumption`  
  Load '75_LVBus0392498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1977267_consumption`  
  Load '75_LVBus1977267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392761_consumption`  
  Load '75_LVBus0392761_consumption' has phase imbalance of 26.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2004552_consumption`  
  Load '75_LVBus2004552_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392532_consumption`  
  Load '75_LVBus0392532_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392754_consumption`  
  Load '75_LVBus0392754_consumption' has phase imbalance of 53.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1981698_consumption`  
  Load '75_LVBus1981698_consumption' has phase imbalance of 239.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392846_consumption`  
  Load '75_LVBus0392846_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392603_consumption`  
  Load '75_LVBus0392603_consumption' has phase imbalance of 207.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392838_consumption`  
  Load '75_LVBus0392838_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392545_consumption`  
  Load '75_LVBus0392545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1965257_consumption`  
  Load '75_LVBus1965257_consumption' has phase imbalance of 266.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392604_consumption`  
  Load '75_LVBus0392604_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392538_consumption`  
  Load '75_LVBus0392538_consumption' has phase imbalance of 228.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392518_consumption`  
  Load '75_LVBus0392518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392631_consumption`  
  Load '75_LVBus0392631_consumption' has phase imbalance of 220.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392844_consumption`  
  Load '75_LVBus0392844_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392561_consumption`  
  Load '75_LVBus0392561_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392799_consumption`  
  Load '75_LVBus0392799_consumption' has phase imbalance of 87.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392537_consumption`  
  Load '75_LVBus0392537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1977268_consumption`  
  Load '75_LVBus1977268_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392918_consumption`  
  Load '75_LVBus0392918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392566_consumption`  
  Load '75_LVBus0392566_consumption' has phase imbalance of 227.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1994616_consumption`  
  Load '75_LVBus1994616_consumption' has phase imbalance of 256.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392601_consumption`  
  Load '75_LVBus0392601_consumption' has phase imbalance of 254.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392815_consumption`  
  Load '75_LVBus0392815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392748_consumption`  
  Load '75_LVBus0392748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392915_consumption`  
  Load '75_LVBus0392915_consumption' has phase imbalance of 179.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392678_consumption`  
  Load '75_LVBus0392678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392911_consumption`  
  Load '75_LVBus0392911_consumption' has phase imbalance of 183.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392734_consumption`  
  Load '75_LVBus0392734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392739_consumption`  
  Load '75_LVBus0392739_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392819_consumption`  
  Load '75_LVBus0392819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392683_consumption`  
  Load '75_LVBus0392683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392634_consumption`  
  Load '75_LVBus0392634_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392781_consumption`  
  Load '75_LVBus0392781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392687_consumption`  
  Load '75_LVBus0392687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392645_consumption`  
  Load '75_LVBus0392645_consumption' has phase imbalance of 206.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392840_consumption`  
  Load '75_LVBus0392840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392562_consumption`  
  Load '75_LVBus0392562_consumption' has phase imbalance of 287.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392654_consumption`  
  Load '75_LVBus0392654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392766_consumption`  
  Load '75_LVBus0392766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392622_consumption`  
  Load '75_LVBus0392622_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392567_consumption`  
  Load '75_LVBus0392567_consumption' has phase imbalance of 89.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392521_consumption`  
  Load '75_LVBus0392521_consumption' has phase imbalance of 228.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1965256_consumption`  
  Load '75_LVBus1965256_consumption' has phase imbalance of 230.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392810_consumption`  
  Load '75_LVBus0392810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1994612_consumption`  
  Load '75_LVBus1994612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392773_consumption`  
  Load '75_LVBus0392773_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392485_consumption`  
  Load '75_LVBus0392485_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392899_consumption`  
  Load '75_LVBus0392899_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392729_consumption`  
  Load '75_LVBus0392729_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392506_consumption`  
  Load '75_LVBus0392506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392866_consumption`  
  Load '75_LVBus0392866_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392742_consumption`  
  Load '75_LVBus0392742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392901_consumption`  
  Load '75_LVBus0392901_consumption' has phase imbalance of 103.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1994617_consumption`  
  Load '75_LVBus1994617_consumption' has phase imbalance of 248.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392646_consumption`  
  Load '75_LVBus0392646_consumption' has phase imbalance of 206.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392669_consumption`  
  Load '75_LVBus0392669_consumption' has phase imbalance of 242.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392508_consumption`  
  Load '75_LVBus0392508_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392647_consumption`  
  Load '75_LVBus0392647_consumption' has phase imbalance of 243.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392714_consumption`  
  Load '75_LVBus0392714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392516_consumption`  
  Load '75_LVBus0392516_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392488_consumption`  
  Load '75_LVBus0392488_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392672_consumption`  
  Load '75_LVBus0392672_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392519_consumption`  
  Load '75_LVBus0392519_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392795_consumption`  
  Load '75_LVBus0392795_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392625_consumption`  
  Load '75_LVBus0392625_consumption' has phase imbalance of 105.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392530_consumption`  
  Load '75_LVBus0392530_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392548_consumption`  
  Load '75_LVBus0392548_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392864_consumption`  
  Load '75_LVBus0392864_consumption' has phase imbalance of 53.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392801_consumption`  
  Load '75_LVBus0392801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392733_consumption`  
  Load '75_LVBus0392733_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392784_consumption`  
  Load '75_LVBus0392784_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392727_consumption`  
  Load '75_LVBus0392727_consumption' has phase imbalance of 237.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392676_consumption`  
  Load '75_LVBus0392676_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1981700_consumption`  
  Load '75_LVBus1981700_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392793_consumption`  
  Load '75_LVBus0392793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392681_consumption`  
  Load '75_LVBus0392681_consumption' has phase imbalance of 109.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392900_consumption`  
  Load '75_LVBus0392900_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392852_consumption`  
  Load '75_LVBus0392852_consumption' has phase imbalance of 246.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392879_consumption`  
  Load '75_LVBus0392879_consumption' has phase imbalance of 75.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392580_consumption`  
  Load '75_LVBus0392580_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392674_consumption`  
  Load '75_LVBus0392674_consumption' has phase imbalance of 123.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392732_consumption`  
  Load '75_LVBus0392732_consumption' has phase imbalance of 232.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392572_consumption`  
  Load '75_LVBus0392572_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392505_consumption`  
  Load '75_LVBus0392505_consumption' has phase imbalance of 95.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392747_consumption`  
  Load '75_LVBus0392747_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392892_consumption`  
  Load '75_LVBus0392892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392811_consumption`  
  Load '75_LVBus0392811_consumption' has phase imbalance of 239.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392841_consumption`  
  Load '75_LVBus0392841_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392491_consumption`  
  Load '75_LVBus0392491_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392525_consumption`  
  Load '75_LVBus0392525_consumption' has phase imbalance of 109.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392794_consumption`  
  Load '75_LVBus0392794_consumption' has phase imbalance of 221.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392757_consumption`  
  Load '75_LVBus0392757_consumption' has phase imbalance of 265.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1994613_consumption`  
  Load '75_LVBus1994613_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392692_consumption`  
  Load '75_LVBus0392692_consumption' has phase imbalance of 186.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392806_consumption`  
  Load '75_LVBus0392806_consumption' has phase imbalance of 62.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392865_consumption`  
  Load '75_LVBus0392865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392613_consumption`  
  Load '75_LVBus0392613_consumption' has phase imbalance of 229.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392708_consumption`  
  Load '75_LVBus0392708_consumption' has phase imbalance of 203.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392526_consumption`  
  Load '75_LVBus0392526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392512_consumption`  
  Load '75_LVBus0392512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392760_consumption`  
  Load '75_LVBus0392760_consumption' has phase imbalance of 145.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392749_consumption`  
  Load '75_LVBus0392749_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392688_consumption`  
  Load '75_LVBus0392688_consumption' has phase imbalance of 62.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392917_consumption`  
  Load '75_LVBus0392917_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392728_consumption`  
  Load '75_LVBus0392728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392668_consumption`  
  Load '75_LVBus0392668_consumption' has phase imbalance of 64.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392772_consumption`  
  Load '75_LVBus0392772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392479_consumption`  
  Load '75_LVBus0392479_consumption' has phase imbalance of 227.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392680_consumption`  
  Load '75_LVBus0392680_consumption' has phase imbalance of 281.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392702_consumption`  
  Load '75_LVBus0392702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392648_consumption`  
  Load '75_LVBus0392648_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392478_consumption`  
  Load '75_LVBus0392478_consumption' has phase imbalance of 234.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392513_consumption`  
  Load '75_LVBus0392513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392775_consumption`  
  Load '75_LVBus0392775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392868_consumption`  
  Load '75_LVBus0392868_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392769_consumption`  
  Load '75_LVBus0392769_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392848_consumption`  
  Load '75_LVBus0392848_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392741_consumption`  
  Load '75_LVBus0392741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392723_consumption`  
  Load '75_LVBus0392723_consumption' has phase imbalance of 61.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392875_consumption`  
  Load '75_LVBus0392875_consumption' has phase imbalance of 79.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392871_consumption`  
  Load '75_LVBus0392871_consumption' has phase imbalance of 106.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392633_consumption`  
  Load '75_LVBus0392633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392629_consumption`  
  Load '75_LVBus0392629_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392529_consumption`  
  Load '75_LVBus0392529_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392721_consumption`  
  Load '75_LVBus0392721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392764_consumption`  
  Load '75_LVBus0392764_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392531_consumption`  
  Load '75_LVBus0392531_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392724_consumption`  
  Load '75_LVBus0392724_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392746_consumption`  
  Load '75_LVBus0392746_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392802_consumption`  
  Load '75_LVBus0392802_consumption' has phase imbalance of 48.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392787_consumption`  
  Load '75_LVBus0392787_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392690_consumption`  
  Load '75_LVBus0392690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392640_consumption`  
  Load '75_LVBus0392640_consumption' has phase imbalance of 24.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392570_consumption`  
  Load '75_LVBus0392570_consumption' has phase imbalance of 185.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1981697_consumption`  
  Load '75_LVBus1981697_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392643_consumption`  
  Load '75_LVBus0392643_consumption' has phase imbalance of 118.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392726_consumption`  
  Load '75_LVBus0392726_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392807_consumption`  
  Load '75_LVBus0392807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392657_consumption`  
  Load '75_LVBus0392657_consumption' has phase imbalance of 114.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392642_consumption`  
  Load '75_LVBus0392642_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392867_consumption`  
  Load '75_LVBus0392867_consumption' has phase imbalance of 247.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392882_consumption`  
  Load '75_LVBus0392882_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392517_consumption`  
  Load '75_LVBus0392517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392880_consumption`  
  Load '75_LVBus0392880_consumption' has phase imbalance of 213.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392697_consumption`  
  Load '75_LVBus0392697_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392812_consumption`  
  Load '75_LVBus0392812_consumption' has phase imbalance of 24.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392504_consumption`  
  Load '75_LVBus0392504_consumption' has phase imbalance of 43.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392535_consumption`  
  Load '75_LVBus0392535_consumption' has phase imbalance of 244.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392539_consumption`  
  Load '75_LVBus0392539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392689_consumption`  
  Load '75_LVBus0392689_consumption' has phase imbalance of 247.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392493_consumption`  
  Load '75_LVBus0392493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392768_consumption`  
  Load '75_LVBus0392768_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392696_consumption`  
  Load '75_LVBus0392696_consumption' has phase imbalance of 29.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392831_consumption`  
  Load '75_LVBus0392831_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392804_consumption`  
  Load '75_LVBus0392804_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392698_consumption`  
  Load '75_LVBus0392698_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392857_consumption`  
  Load '75_LVBus0392857_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392585_consumption`  
  Load '75_LVBus0392585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392486_consumption`  
  Load '75_LVBus0392486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392779_consumption`  
  Load '75_LVBus0392779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392533_consumption`  
  Load '75_LVBus0392533_consumption' has phase imbalance of 269.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392550_consumption`  
  Load '75_LVBus0392550_consumption' has phase imbalance of 134.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392872_consumption`  
  Load '75_LVBus0392872_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392837_consumption`  
  Load '75_LVBus0392837_consumption' has phase imbalance of 269.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392564_consumption`  
  Load '75_LVBus0392564_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392785_consumption`  
  Load '75_LVBus0392785_consumption' has phase imbalance of 98.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392839_consumption`  
  Load '75_LVBus0392839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0392881_consumption`  
  Load '75_LVBus0392881_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 800 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_POMER' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0392650' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_POMER' (MV, 11.78 kV) has an electrical reach of 21.79 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0392650' (LV, 0.24 kV) has an electrical reach of 18.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  502 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  210 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0392478_consumption, 75_LVBus0392479_consumption, 75_LVBus0392480_consumption, 75_LVBus0392482_consumption, 75_LVBus0392485_consumption, 75_LVBus0392486_consumption, 75_LVBus0392488_consumption, 75_LVBus0392489_consumption, 75_LVBus0392490_consumption, 75_LVBus0392491_consumption, 75_LVBus0392493_consumption, 75_LVBus0392494_consumption, 75_LVBus0392496_consumption, 75_LVBus0392498_consumption, 75_LVBus0392500_consumption, 75_LVBus0392501_consumption, 75_LVBus0392506_consumption, 75_LVBus0392507_consumption, 75_LVBus0392508_consumption, 75_LVBus0392509_consumption, 75_LVBus0392510_consumption, 75_LVBus0392512_consumption, 75_LVBus0392513_consumption, 75_LVBus0392516_consumption, 75_LVBus0392517_consumption, 75_LVBus0392518_consumption, 75_LVBus0392521_consumption, 75_LVBus0392523_consumption, 75_LVBus0392526_consumption, 75_LVBus0392529_consumption, 75_LVBus0392531_consumption, 75_LVBus0392532_consumption, 75_LVBus0392533_consumption, 75_LVBus0392535_consumption, 75_LVBus0392536_consumption, 75_LVBus0392537_consumption, 75_LVBus0392538_consumption, 75_LVBus0392539_consumption, 75_LVBus0392543_consumption, 75_LVBus0392545_consumption, 75_LVBus0392546_consumption, 75_LVBus0392552_consumption, 75_LVBus0392558_consumption, 75_LVBus0392561_consumption, 75_LVBus0392562_consumption, 75_LVBus0392566_consumption, 75_LVBus0392569_consumption, 75_LVBus0392570_consumption, 75_LVBus0392571_consumption, 75_LVBus0392572_consumption, 75_LVBus0392573_consumption, 75_LVBus0392575_consumption, 75_LVBus0392579_consumption, 75_LVBus0392580_consumption, 75_LVBus0392584_consumption, 75_LVBus0392585_consumption, 75_LVBus0392586_consumption, 75_LVBus0392592_consumption, 75_LVBus0392601_consumption, 75_LVBus0392603_consumption, 75_LVBus0392605_consumption, 75_LVBus0392606_consumption, 75_LVBus0392608_consumption, 75_LVBus0392610_consumption, 75_LVBus0392612_consumption, 75_LVBus0392613_consumption, 75_LVBus0392618_consumption, 75_LVBus0392619_consumption, 75_LVBus0392620_consumption, 75_LVBus0392621_consumption, 75_LVBus0392627_consumption, 75_LVBus0392629_consumption, 75_LVBus0392631_consumption, 75_LVBus0392632_consumption, 75_LVBus0392633_consumption, 75_LVBus0392634_consumption, 75_LVBus0392635_consumption, 75_LVBus0392637_consumption, 75_LVBus0392638_consumption, 75_LVBus0392639_consumption, 75_LVBus0392642_consumption, 75_LVBus0392644_consumption, 75_LVBus0392646_consumption, 75_LVBus0392647_consumption, 75_LVBus0392654_consumption, 75_LVBus0392656_consumption, 75_LVBus0392672_consumption, 75_LVBus0392676_consumption, 75_LVBus0392677_consumption, 75_LVBus0392678_consumption, 75_LVBus0392679_consumption, 75_LVBus0392680_consumption, 75_LVBus0392682_consumption, 75_LVBus0392683_consumption, 75_LVBus0392684_consumption, 75_LVBus0392687_consumption, 75_LVBus0392689_consumption, 75_LVBus0392690_consumption, 75_LVBus0392692_consumption, 75_LVBus0392697_consumption, 75_LVBus0392701_consumption, 75_LVBus0392702_consumption, 75_LVBus0392707_consumption, 75_LVBus0392713_consumption, 75_LVBus0392714_consumption, 75_LVBus0392718_consumption, 75_LVBus0392719_consumption, 75_LVBus0392721_consumption, 75_LVBus0392724_consumption, 75_LVBus0392725_consumption, 75_LVBus0392726_consumption, 75_LVBus0392727_consumption, 75_LVBus0392728_consumption, 75_LVBus0392729_consumption, 75_LVBus0392730_consumption, 75_LVBus0392733_consumption, 75_LVBus0392734_consumption, 75_LVBus0392738_consumption, 75_LVBus0392739_consumption, 75_LVBus0392740_consumption, 75_LVBus0392741_consumption, 75_LVBus0392742_consumption, 75_LVBus0392748_consumption, 75_LVBus0392749_consumption, 75_LVBus0392752_consumption, 75_LVBus0392756_consumption, 75_LVBus0392757_consumption, 75_LVBus0392759_consumption, 75_LVBus0392762_consumption, 75_LVBus0392763_consumption, 75_LVBus0392764_consumption, 75_LVBus0392766_consumption, 75_LVBus0392767_consumption, 75_LVBus0392768_consumption, 75_LVBus0392769_consumption, 75_LVBus0392772_consumption, 75_LVBus0392773_consumption, 75_LVBus0392774_consumption, 75_LVBus0392775_consumption, 75_LVBus0392777_consumption, 75_LVBus0392779_consumption, 75_LVBus0392781_consumption, 75_LVBus0392784_consumption, 75_LVBus0392793_consumption, 75_LVBus0392794_consumption, 75_LVBus0392795_consumption, 75_LVBus0392798_consumption, 75_LVBus0392800_consumption, 75_LVBus0392801_consumption, 75_LVBus0392804_consumption, 75_LVBus0392807_consumption, 75_LVBus0392810_consumption, 75_LVBus0392811_consumption, 75_LVBus0392815_consumption, 75_LVBus0392819_consumption, 75_LVBus0392826_consumption, 75_LVBus0392827_consumption, 75_LVBus0392831_consumption, 75_LVBus0392832_consumption, 75_LVBus0392837_consumption, 75_LVBus0392839_consumption, 75_LVBus0392840_consumption, 75_LVBus0392841_consumption, 75_LVBus0392843_consumption, 75_LVBus0392844_consumption, 75_LVBus0392845_consumption, 75_LVBus0392846_consumption, 75_LVBus0392849_consumption, 75_LVBus0392852_consumption, 75_LVBus0392860_consumption, 75_LVBus0392865_consumption, 75_LVBus0392867_consumption, 75_LVBus0392868_consumption, 75_LVBus0392869_consumption, 75_LVBus0392870_consumption, 75_LVBus0392872_consumption, 75_LVBus0392874_consumption, 75_LVBus0392880_consumption, 75_LVBus0392881_consumption, 75_LVBus0392882_consumption, 75_LVBus0392888_consumption, 75_LVBus0392892_consumption, 75_LVBus0392896_consumption, 75_LVBus0392897_consumption, 75_LVBus0392899_consumption, 75_LVBus0392900_consumption, 75_LVBus0392911_consumption, 75_LVBus0392912_consumption, 75_LVBus0392916_consumption, 75_LVBus0392917_consumption, 75_LVBus0392918_consumption, 75_LVBus0392919_consumption, 75_LVBus1939291_consumption, 75_LVBus1965256_consumption, 75_LVBus1965257_consumption, 75_LVBus1965258_consumption, 75_LVBus1977264_consumption, 75_LVBus1977265_consumption, 75_LVBus1977266_consumption, 75_LVBus1977267_consumption, 75_LVBus1977268_consumption, 75_LVBus1981697_consumption, 75_LVBus1981698_consumption, 75_LVBus1981700_consumption, 75_LVBus1992741_consumption, 75_LVBus1994612_consumption, 75_LVBus1994613_consumption, 75_LVBus1994615_consumption, 75_LVBus1994617_consumption, 75_LVBus2004552_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  400 group(s) of loads (800 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  11 group(s) of series lines (27 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  493 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0392478_production, 75_LVBus0392479_production, 75_LVBus0392480_production, 75_LVBus0392481_consumption, 75_LVBus0392481_production, 75_LVBus0392482_production, 75_LVBus0392484_consumption, 75_LVBus0392484_production, 75_LVBus0392485_production, 75_LVBus0392486_production, 75_LVBus0392487_consumption, 75_LVBus0392487_production, 75_LVBus0392488_production, 75_LVBus0392489_production, 75_LVBus0392490_production, 75_LVBus0392491_production, 75_LVBus0392493_production, 75_LVBus0392494_production, 75_LVBus0392495_production, 75_LVBus0392496_production, 75_LVBus0392497_consumption, 75_LVBus0392497_production, 75_LVBus0392498_production, 75_LVBus0392499_consumption, 75_LVBus0392499_production, 75_LVBus0392500_production, 75_LVBus0392501_production, 75_LVBus0392503_consumption, 75_LVBus0392503_production, 75_LVBus0392504_production, 75_LVBus0392505_production, 75_LVBus0392506_production, 75_LVBus0392507_production, 75_LVBus0392508_production, 75_LVBus0392509_production, 75_LVBus0392510_production, 75_LVBus0392512_production, 75_LVBus0392513_production, 75_LVBus0392514_consumption, 75_LVBus0392514_production, 75_LVBus0392515_consumption, 75_LVBus0392515_production, 75_LVBus0392516_production, 75_LVBus0392517_production, 75_LVBus0392518_production, 75_LVBus0392519_production, 75_LVBus0392521_production, 75_LVBus0392523_production, 75_LVBus0392524_consumption, 75_LVBus0392524_production, 75_LVBus0392525_production, 75_LVBus0392526_production, 75_LVBus0392527_consumption, 75_LVBus0392527_production, 75_LVBus0392529_production, 75_LVBus0392530_production, 75_LVBus0392531_production, 75_LVBus0392532_production, 75_LVBus0392533_production, 75_LVBus0392535_production, 75_LVBus0392536_production, 75_LVBus0392537_production, 75_LVBus0392538_production, 75_LVBus0392539_production, 75_LVBus0392540_production, 75_LVBus0392541_consumption, 75_LVBus0392541_production, 75_LVBus0392542_consumption, 75_LVBus0392542_production, 75_LVBus0392543_production, 75_LVBus0392545_production, 75_LVBus0392546_production, 75_LVBus0392547_consumption, 75_LVBus0392547_production, 75_LVBus0392548_production, 75_LVBus0392549_production, 75_LVBus0392550_production, 75_LVBus0392551_production, 75_LVBus0392552_production, 75_LVBus0392553_consumption, 75_LVBus0392553_production, 75_LVBus0392554_consumption, 75_LVBus0392554_production, 75_LVBus0392555_consumption, 75_LVBus0392555_production, 75_LVBus0392556_consumption, 75_LVBus0392556_production, 75_LVBus0392558_production, 75_LVBus0392559_production, 75_LVBus0392560_consumption, 75_LVBus0392560_production, 75_LVBus0392561_production, 75_LVBus0392562_production, 75_LVBus0392563_consumption, 75_LVBus0392563_production, 75_LVBus0392564_production, 75_LVBus0392565_consumption, 75_LVBus0392565_production, 75_LVBus0392566_production, 75_LVBus0392567_production, 75_LVBus0392568_consumption, 75_LVBus0392568_production, 75_LVBus0392569_production, 75_LVBus0392570_production, 75_LVBus0392571_production, 75_LVBus0392572_production, 75_LVBus0392573_production, 75_LVBus0392574_production, 75_LVBus0392575_production, 75_LVBus0392579_production, 75_LVBus0392580_production, 75_LVBus0392581_consumption, 75_LVBus0392581_production, 75_LVBus0392582_consumption, 75_LVBus0392582_production, 75_LVBus0392583_production, 75_LVBus0392584_production, 75_LVBus0392585_production, 75_LVBus0392586_production, 75_LVBus0392588_consumption, 75_LVBus0392588_production, 75_LVBus0392590_consumption, 75_LVBus0392590_production, 75_LVBus0392592_production, 75_LVBus0392593_production, 75_LVBus0392594_consumption, 75_LVBus0392594_production, 75_LVBus0392596_consumption, 75_LVBus0392596_production, 75_LVBus0392598_consumption, 75_LVBus0392598_production, 75_LVBus0392600_production, 75_LVBus0392601_production, 75_LVBus0392602_production, 75_LVBus0392603_production, 75_LVBus0392604_production, 75_LVBus0392605_production, 75_LVBus0392606_production, 75_LVBus0392608_production, 75_LVBus0392609_consumption, 75_LVBus0392609_production, 75_LVBus0392610_production, 75_LVBus0392611_production, 75_LVBus0392612_production, 75_LVBus0392613_production, 75_LVBus0392614_production, 75_LVBus0392618_production, 75_LVBus0392619_production, 75_LVBus0392620_production, 75_LVBus0392621_production, 75_LVBus0392622_production, 75_LVBus0392623_consumption, 75_LVBus0392623_production, 75_LVBus0392624_production, 75_LVBus0392625_production, 75_LVBus0392627_production, 75_LVBus0392628_consumption, 75_LVBus0392628_production, 75_LVBus0392629_production, 75_LVBus0392631_production, 75_LVBus0392632_production, 75_LVBus0392633_production, 75_LVBus0392634_production, 75_LVBus0392635_production, 75_LVBus0392637_production, 75_LVBus0392638_production, 75_LVBus0392639_production, 75_LVBus0392640_production, 75_LVBus0392641_consumption, 75_LVBus0392641_production, 75_LVBus0392642_production, 75_LVBus0392643_production, 75_LVBus0392644_production, 75_LVBus0392645_production, 75_LVBus0392646_production, 75_LVBus0392647_production, 75_LVBus0392648_production, 75_LVBus0392650_production, 75_LVBus0392652_consumption, 75_LVBus0392652_production, 75_LVBus0392653_consumption, 75_LVBus0392653_production, 75_LVBus0392654_production, 75_LVBus0392655_consumption, 75_LVBus0392655_production, 75_LVBus0392656_production, 75_LVBus0392657_production, 75_LVBus0392659_consumption, 75_LVBus0392659_production, 75_LVBus0392661_consumption, 75_LVBus0392661_production, 75_LVBus0392662_consumption, 75_LVBus0392662_production, 75_LVBus0392663_consumption, 75_LVBus0392663_production, 75_LVBus0392665_consumption, 75_LVBus0392665_production, 75_LVBus0392666_consumption, 75_LVBus0392666_production, 75_LVBus0392667_consumption, 75_LVBus0392667_production, 75_LVBus0392668_production, 75_LVBus0392669_production, 75_LVBus0392670_consumption, 75_LVBus0392670_production, 75_LVBus0392671_consumption, 75_LVBus0392671_production, 75_LVBus0392672_production, 75_LVBus0392674_production, 75_LVBus0392676_production, 75_LVBus0392677_production, 75_LVBus0392678_production, 75_LVBus0392679_production, 75_LVBus0392680_production, 75_LVBus0392681_production, 75_LVBus0392682_production, 75_LVBus0392683_production, 75_LVBus0392684_production, 75_LVBus0392685_consumption, 75_LVBus0392685_production, 75_LVBus0392686_production, 75_LVBus0392687_production, 75_LVBus0392688_production, 75_LVBus0392689_production, 75_LVBus0392690_production, 75_LVBus0392691_consumption, 75_LVBus0392691_production, 75_LVBus0392692_production, 75_LVBus0392694_production, 75_LVBus0392695_production, 75_LVBus0392696_production, 75_LVBus0392697_production, 75_LVBus0392698_production, 75_LVBus0392700_consumption, 75_LVBus0392700_production, 75_LVBus0392701_production, 75_LVBus0392702_production, 75_LVBus0392703_consumption, 75_LVBus0392703_production, 75_LVBus0392704_consumption, 75_LVBus0392704_production, 75_LVBus0392705_consumption, 75_LVBus0392705_production, 75_LVBus0392707_production, 75_LVBus0392708_production, 75_LVBus0392710_consumption, 75_LVBus0392710_production, 75_LVBus0392711_consumption, 75_LVBus0392711_production, 75_LVBus0392712_production, 75_LVBus0392713_production, 75_LVBus0392714_production, 75_LVBus0392716_production, 75_LVBus0392718_production, 75_LVBus0392719_production, 75_LVBus0392720_consumption, 75_LVBus0392720_production, 75_LVBus0392721_production, 75_LVBus0392723_production, 75_LVBus0392724_production, 75_LVBus0392725_production, 75_LVBus0392726_production, 75_LVBus0392727_production, 75_LVBus0392728_production, 75_LVBus0392729_production, 75_LVBus0392730_production, 75_LVBus0392732_production, 75_LVBus0392733_production, 75_LVBus0392734_production, 75_LVBus0392735_consumption, 75_LVBus0392735_production, 75_LVBus0392736_production, 75_LVBus0392737_consumption, 75_LVBus0392737_production, 75_LVBus0392738_production, 75_LVBus0392739_production, 75_LVBus0392740_production, 75_LVBus0392741_production, 75_LVBus0392742_production, 75_LVBus0392746_production, 75_LVBus0392747_production, 75_LVBus0392748_production, 75_LVBus0392749_production, 75_LVBus0392750_consumption, 75_LVBus0392750_production, 75_LVBus0392752_production, 75_LVBus0392753_production, 75_LVBus0392754_production, 75_LVBus0392756_production, 75_LVBus0392757_production, 75_LVBus0392758_consumption, 75_LVBus0392758_production, 75_LVBus0392759_production, 75_LVBus0392760_production, 75_LVBus0392761_production, 75_LVBus0392762_production, 75_LVBus0392763_production, 75_LVBus0392764_production, 75_LVBus0392766_production, 75_LVBus0392767_production, 75_LVBus0392768_production, 75_LVBus0392769_production, 75_LVBus0392771_consumption, 75_LVBus0392771_production, 75_LVBus0392772_production, 75_LVBus0392773_production, 75_LVBus0392774_production, 75_LVBus0392775_production, 75_LVBus0392776_consumption, 75_LVBus0392776_production, 75_LVBus0392777_production, 75_LVBus0392778_consumption, 75_LVBus0392778_production, 75_LVBus0392779_production, 75_LVBus0392781_production, 75_LVBus0392782_consumption, 75_LVBus0392782_production, 75_LVBus0392783_consumption, 75_LVBus0392783_production, 75_LVBus0392784_production, 75_LVBus0392785_production, 75_LVBus0392786_production, 75_LVBus0392787_production, 75_LVBus0392788_production, 75_LVBus0392790_consumption, 75_LVBus0392790_production, 75_LVBus0392792_consumption, 75_LVBus0392792_production, 75_LVBus0392793_production, 75_LVBus0392794_production, 75_LVBus0392795_production, 75_LVBus0392796_production, 75_LVBus0392798_production, 75_LVBus0392799_production, 75_LVBus0392800_production, 75_LVBus0392801_production, 75_LVBus0392802_production, 75_LVBus0392803_consumption, 75_LVBus0392803_production, 75_LVBus0392804_production, 75_LVBus0392806_production, 75_LVBus0392807_production, 75_LVBus0392808_consumption, 75_LVBus0392808_production, 75_LVBus0392809_production, 75_LVBus0392810_production, 75_LVBus0392811_production, 75_LVBus0392812_production, 75_LVBus0392813_production, 75_LVBus0392815_production, 75_LVBus0392817_consumption, 75_LVBus0392817_production, 75_LVBus0392818_production, 75_LVBus0392819_production, 75_LVBus0392820_consumption, 75_LVBus0392820_production, 75_LVBus0392821_consumption, 75_LVBus0392821_production, 75_LVBus0392822_consumption, 75_LVBus0392822_production, 75_LVBus0392823_consumption, 75_LVBus0392823_production, 75_LVBus0392824_consumption, 75_LVBus0392824_production, 75_LVBus0392825_production, 75_LVBus0392826_production, 75_LVBus0392827_production, 75_LVBus0392829_consumption, 75_LVBus0392829_production, 75_LVBus0392830_consumption, 75_LVBus0392830_production, 75_LVBus0392831_production, 75_LVBus0392832_production, 75_LVBus0392833_production, 75_LVBus0392835_consumption, 75_LVBus0392835_production, 75_LVBus0392837_production, 75_LVBus0392838_production, 75_LVBus0392839_production, 75_LVBus0392840_production, 75_LVBus0392841_production, 75_LVBus0392843_production, 75_LVBus0392844_production, 75_LVBus0392845_production, 75_LVBus0392846_production, 75_LVBus0392847_consumption, 75_LVBus0392847_production, 75_LVBus0392848_production, 75_LVBus0392849_production, 75_LVBus0392852_production, 75_LVBus0392853_production, 75_LVBus0392854_consumption, 75_LVBus0392854_production, 75_LVBus0392855_production, 75_LVBus0392856_production, 75_LVBus0392857_production, 75_LVBus0392858_production, 75_LVBus0392859_consumption, 75_LVBus0392859_production, 75_LVBus0392860_production, 75_LVBus0392862_consumption, 75_LVBus0392862_production, 75_LVBus0392864_production, 75_LVBus0392865_production, 75_LVBus0392866_production, 75_LVBus0392867_production, 75_LVBus0392868_production, 75_LVBus0392869_production, 75_LVBus0392870_production, 75_LVBus0392871_production, 75_LVBus0392872_production, 75_LVBus0392874_production, 75_LVBus0392875_production, 75_LVBus0392876_production, 75_LVBus0392877_production, 75_LVBus0392879_production, 75_LVBus0392880_production, 75_LVBus0392881_production, 75_LVBus0392882_production, 75_LVBus0392884_consumption, 75_LVBus0392884_production, 75_LVBus0392885_consumption, 75_LVBus0392885_production, 75_LVBus0392888_production, 75_LVBus0392889_production, 75_LVBus0392890_consumption, 75_LVBus0392890_production, 75_LVBus0392891_production, 75_LVBus0392892_production, 75_LVBus0392893_production, 75_LVBus0392894_consumption, 75_LVBus0392894_production, 75_LVBus0392895_production, 75_LVBus0392896_production, 75_LVBus0392897_production, 75_LVBus0392899_production, 75_LVBus0392900_production, 75_LVBus0392901_production, 75_LVBus0392903_consumption, 75_LVBus0392903_production, 75_LVBus0392905_consumption, 75_LVBus0392905_production, 75_LVBus0392907_consumption, 75_LVBus0392907_production, 75_LVBus0392909_production, 75_LVBus0392910_production, 75_LVBus0392911_production, 75_LVBus0392912_production, 75_LVBus0392913_production, 75_LVBus0392915_production, 75_LVBus0392916_production, 75_LVBus0392917_production, 75_LVBus0392918_production, 75_LVBus0392919_production, 75_LVBus1939291_production, 75_LVBus1953818_production, 75_LVBus1965256_production, 75_LVBus1965257_production, 75_LVBus1965258_production, 75_LVBus1977045_production, 75_LVBus1977264_production, 75_LVBus1977265_production, 75_LVBus1977266_production, 75_LVBus1977267_production, 75_LVBus1977268_production, 75_LVBus1981697_production, 75_LVBus1981698_production, 75_LVBus1981699_consumption, 75_LVBus1981699_production, 75_LVBus1981700_production, 75_LVBus1982250_production, 75_LVBus1992741_production, 75_LVBus1994612_production, 75_LVBus1994613_production, 75_LVBus1994614_consumption, 75_LVBus1994614_production, 75_LVBus1994615_production, 75_LVBus1994616_production, 75_LVBus1994617_production, 75_LVBus1994618_production, 75_LVBus2004552_production, 75_LVBus2006785_consumption, 75_LVBus2006785_production, 75_LVBus2009143_production, 75_MVLV022119_production, 75_MVLV055038_consumption, 75_MVLV055038_production, 75_MVLV063757_consumption, 75_MVLV063757_production, 75_MVLV128570_consumption, 75_MVLV128570_production, 75_MVLV155338_consumption, 75_MVLV155338_production.

