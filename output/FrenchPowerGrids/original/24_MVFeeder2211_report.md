# BMOPF Network Summary: 24_MVFeeder2211

**Generated:** 2026-10-01 23:33:59  
**Findings:** 0 errors · 5 warnings · 403 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 70 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 739 |  |
| line | 668 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1026 | 1.567 MW, 470.2 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 70 |  |
| switch | 0 |  |
| transformer | 70 | Dyn11×70 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 162 | 161 | 12 | 0 |
| LV_236V | 236.0 V | 577 | 507 | 1014 | 0 |

**Transformer transitions:**

- `24_MVLV35891_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV16743_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV47967_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV57443_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV66633_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69933_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69992_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV66602_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV75164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV07461_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV11265_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV18845_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV13946_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV72501_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14814_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV29575_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV85917_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV47968_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV41115_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV57417_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV48536_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV70941_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV06006_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV40649_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV21722_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV30135_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV42514_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36685_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV72860_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV55272_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV90810_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV28950_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV46246_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV10046_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV35152_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14983_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV55277_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV00616_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV10055_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV09404_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV51272_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV10054_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV22614_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69560_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36314_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV20556_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV11256_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV62039_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV35890_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV25266_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV20544_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV33828_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV64495_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV85916_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV48455_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV45670_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV70506_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV47385_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV30159_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV20545_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV69925_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV85910_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV65753_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV66603_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV13947_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV66632_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV27685_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV34287_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV53801_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 245 |
| Tree depth (max hops) | 36 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 739 | 1 | 738 | 0 | 0 | 0 |
| Tier LV_236V | 577 | 70 | 507 | 0 | 0 | 0 |
| Tier MV_11.8kV | 162 | 1 | 161 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 70; skipped invalid branches: 0.

Galvanic zones: 71; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 24_MVBus68079 | MV_11.8kV | 162 | 0 | 0 | 70 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2794 declared bus terminals; 2511 mapped line/closed-switch conductor edges; 283 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 7 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 36500.0 | 3.477 | 3078 |
| q_nom | 0.0 | 10900.0 | 3.477 | 3078 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.501 | 6070.0 | 2.231 | 668 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.587 | 70 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 622 of 1026 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221102_consumption' has phase imbalance of 148.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221068_consumption' has phase imbalance of 133.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221268_consumption' has phase imbalance of 186.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220694_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221117_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221205_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220988_consumption' has phase imbalance of 266.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220992_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857045_consumption' has phase imbalance of 184.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220693_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221029_consumption' has phase imbalance of 217.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220879_consumption' has phase imbalance of 263.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221002_consumption' has phase imbalance of 134.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus833311_consumption' has phase imbalance of 112.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221044_consumption' has phase imbalance of 99.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221065_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221261_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220963_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus835930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220729_consumption' has phase imbalance of 261.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220857_consumption' has phase imbalance of 276.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221262_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220732_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221110_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus835929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221080_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220830_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220859_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220782_consumption' has phase imbalance of 138.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221030_consumption' has phase imbalance of 198.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220748_consumption' has phase imbalance of 227.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220762_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221260_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220858_consumption' has phase imbalance of 104.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221012_consumption' has phase imbalance of 260.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221128_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221101_consumption' has phase imbalance of 101.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220964_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221043_consumption' has phase imbalance of 291.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221033_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220894_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221000_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221151_consumption' has phase imbalance of 100.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220903_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220759_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221091_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221134_consumption' has phase imbalance of 207.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220917_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220870_consumption' has phase imbalance of 148.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220862_consumption' has phase imbalance of 108.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221113_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220933_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220919_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221108_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220766_consumption' has phase imbalance of 278.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221178_consumption' has phase imbalance of 86.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220994_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220711_consumption' has phase imbalance of 98.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221255_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220990_consumption' has phase imbalance of 253.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221292_consumption' has phase imbalance of 249.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221148_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220733_consumption' has phase imbalance of 27.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857044_consumption' has phase imbalance of 287.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221007_consumption' has phase imbalance of 285.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221291_consumption' has phase imbalance of 123.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221118_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221010_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221216_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221186_consumption' has phase imbalance of 246.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221122_consumption' has phase imbalance of 28.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221182_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220702_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221204_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221276_consumption' has phase imbalance of 258.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220750_consumption' has phase imbalance of 165.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843813_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221163_consumption' has phase imbalance of 290.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221208_consumption' has phase imbalance of 107.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220812_consumption' has phase imbalance of 60.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220818_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861564_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220884_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221183_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221144_consumption' has phase imbalance of 280.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220844_consumption' has phase imbalance of 52.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221170_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221022_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220813_consumption' has phase imbalance of 236.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220831_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857469_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221210_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221242_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220971_consumption' has phase imbalance of 218.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221031_consumption' has phase imbalance of 75.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221166_consumption' has phase imbalance of 101.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220706_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861566_consumption' has phase imbalance of 43.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220716_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220849_consumption' has phase imbalance of 52.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221279_consumption' has phase imbalance of 114.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus852187_consumption' has phase imbalance of 82.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221055_consumption' has phase imbalance of 121.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220868_consumption' has phase imbalance of 240.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220896_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221201_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221269_consumption' has phase imbalance of 106.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220792_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220998_consumption' has phase imbalance of 264.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221172_consumption' has phase imbalance of 288.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221114_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221233_consumption' has phase imbalance of 266.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus858484_consumption' has phase imbalance of 248.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220745_consumption' has phase imbalance of 132.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220728_consumption' has phase imbalance of 151.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221142_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221084_consumption' has phase imbalance of 138.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus858993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221283_consumption' has phase imbalance of 31.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221052_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220905_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220756_consumption' has phase imbalance of 246.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220989_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220828_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220938_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221193_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221161_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221229_consumption' has phase imbalance of 216.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220810_consumption' has phase imbalance of 20.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220855_consumption' has phase imbalance of 286.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221126_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220997_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221037_consumption' has phase imbalance of 39.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220699_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220958_consumption' has phase imbalance of 166.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus856544_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus859815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220758_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220795_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus833824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221047_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221280_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220978_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220724_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221064_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857470_consumption' has phase imbalance of 206.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221217_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220796_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221072_consumption' has phase imbalance of 252.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221155_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221056_consumption' has phase imbalance of 225.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221214_consumption' has phase imbalance of 257.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221185_consumption' has phase imbalance of 71.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221127_consumption' has phase imbalance of 44.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220790_consumption' has phase imbalance of 213.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220881_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220765_consumption' has phase imbalance of 64.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220901_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843814_consumption' has phase imbalance of 209.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221206_consumption' has phase imbalance of 295.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220835_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220701_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220925_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221103_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221129_consumption' has phase imbalance of 274.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221287_consumption' has phase imbalance of 179.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220727_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220899_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221116_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221082_consumption' has phase imbalance of 286.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220991_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221267_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220973_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220832_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221167_consumption' has phase imbalance of 37.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus838927_consumption' has phase imbalance of 103.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220852_consumption' has phase imbalance of 108.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220703_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221141_consumption' has phase imbalance of 129.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220867_consumption' has phase imbalance of 236.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220916_consumption' has phase imbalance of 265.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221164_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220785_consumption' has phase imbalance of 280.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221212_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220898_consumption' has phase imbalance of 232.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220977_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860438_consumption' has phase imbalance of 268.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus856086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221194_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221240_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221049_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221014_consumption' has phase imbalance of 246.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220979_consumption' has phase imbalance of 68.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220700_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221147_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220967_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221278_consumption' has phase imbalance of 138.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220982_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221115_consumption' has phase imbalance of 254.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860533_consumption' has phase imbalance of 201.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220850_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220897_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220823_consumption' has phase imbalance of 215.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220802_consumption' has phase imbalance of 110.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221111_consumption' has phase imbalance of 270.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220985_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221188_consumption' has phase imbalance of 238.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220906_consumption' has phase imbalance of 267.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221097_consumption' has phase imbalance of 284.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221152_consumption' has phase imbalance of 92.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221277_consumption' has phase imbalance of 220.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221285_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221094_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220736_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220864_consumption' has phase imbalance of 278.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220918_consumption' has phase imbalance of 126.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221153_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220715_consumption' has phase imbalance of 259.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221140_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221289_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221059_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220959_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221256_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220757_consumption' has phase imbalance of 216.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221154_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220838_consumption' has phase imbalance of 283.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857047_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220996_consumption' has phase imbalance of 135.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220697_consumption' has phase imbalance of 216.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220969_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220809_consumption' has phase imbalance of 135.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221162_consumption' has phase imbalance of 257.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220761_consumption' has phase imbalance of 129.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221180_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221175_consumption' has phase imbalance of 287.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221060_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221158_consumption' has phase imbalance of 150.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus842201_consumption' has phase imbalance of 265.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220776_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221273_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220984_consumption' has phase imbalance of 149.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221054_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220970_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220779_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220820_consumption' has phase imbalance of 214.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220983_consumption' has phase imbalance of 202.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221133_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220878_consumption' has phase imbalance of 123.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860111_consumption' has phase imbalance of 230.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857046_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221124_consumption' has phase imbalance of 182.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220722_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221247_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220714_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220755_consumption' has phase imbalance of 257.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220839_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221288_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221174_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221005_consumption' has phase imbalance of 292.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843697_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221293_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221093_consumption' has phase imbalance of 118.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220707_consumption' has phase imbalance of 204.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220974_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220819_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861567_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221237_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221036_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221136_consumption' has phase imbalance of 120.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220837_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus855540_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221096_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus221251_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220752_consumption' has phase imbalance of 243.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus220783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1026 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.567 MW |
| Total load Q | 470.2 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 24_MVLV35891_Transformer | 110.0 kVA | 4.3% |
| 24_MVLV16743_Transformer | 110.0 kVA | 4.5% |
| 24_MVLV47967_Transformer | 110.0 kVA | 4.5% |
| 24_MVLV57443_Transformer | 176.0 kVA | 10.6% |
| 24_MVLV66633_Transformer | 110.0 kVA | 5.8% |
| 24_MVLV69933_Transformer | 176.0 kVA | 8.5% |
| 24_MVLV69992_Transformer | 110.0 kVA | 1.4% |
| 24_MVLV66602_Transformer | 440.0 kVA | 21.6% |
| 24_MVLV75164_Transformer | 176.0 kVA | 12.2% |
| 24_MVLV07461_Transformer | 176.0 kVA | 4.4% |
| 24_MVLV11265_Transformer | 110.0 kVA | 0.7% |
| 24_MVLV18845_Transformer | 176.0 kVA | 7.3% |
| 24_MVLV13946_Transformer | 440.0 kVA | 12.9% |
| 24_MVLV72501_Transformer | 110.0 kVA | 7.4% |
| 24_MVLV14814_Transformer | 110.0 kVA | 0.4% |
| 24_MVLV29575_Transformer | 110.0 kVA | 1.4% |
| 24_MVLV85917_Transformer | 176.0 kVA | 7.9% |
| 24_MVLV47968_Transformer | 176.0 kVA | 6.8% |
| 24_MVLV41115_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV57417_Transformer | 440.0 kVA | 19.3% |
| 24_MVLV48536_Transformer | 275.0 kVA | 16.2% |
| 24_MVLV70941_Transformer | 110.0 kVA | 7.8% |
| 24_MVLV06006_Transformer | 275.0 kVA | 9.4% |
| 24_MVLV40649_Transformer | 275.0 kVA | 22.4% |
| 24_MVLV21722_Transformer | 275.0 kVA | 7.0% |
| 24_MVLV30135_Transformer | 440.0 kVA | 8.2% |
| 24_MVLV42514_Transformer | 110.0 kVA | 0.5% |
| 24_MVLV36685_Transformer | 275.0 kVA | 8.0% |
| 24_MVLV72860_Transformer | 110.0 kVA | 0.3% |
| 24_MVLV55272_Transformer | 176.0 kVA | 10.7% |
| 24_MVLV90810_Transformer | 440.0 kVA | 16.5% |
| 24_MVLV28950_Transformer | 176.0 kVA | 12.6% |
| 24_MVLV14625_Transformer | 176.0 kVA | 8.2% |
| 24_MVLV46246_Transformer | 440.0 kVA | 16.0% |
| 24_MVLV10046_Transformer | 110.0 kVA | 7.2% |
| 24_MVLV35152_Transformer | 110.0 kVA | 1.1% |
| 24_MVLV14983_Transformer | 176.0 kVA | 3.4% |
| 24_MVLV55277_Transformer | 110.0 kVA | 4.6% |
| 24_MVLV00616_Transformer | 110.0 kVA | 7.7% |
| 24_MVLV10055_Transformer | 440.0 kVA | 21.4% |
| 24_MVLV09404_Transformer | 275.0 kVA | 7.4% |
| 24_MVLV51272_Transformer | 275.0 kVA | 10.5% |
| 24_MVLV10054_Transformer | 110.0 kVA | 0.2% |
| 24_MVLV22614_Transformer | 176.0 kVA | 3.5% |
| 24_MVLV69560_Transformer | 110.0 kVA | 8.3% |
| 24_MVLV36314_Transformer | 275.0 kVA | 8.1% |
| 24_MVLV20556_Transformer | 110.0 kVA | 2.9% |
| 24_MVLV11256_Transformer | 110.0 kVA | 7.3% |
| 24_MVLV62039_Transformer | 176.0 kVA | 7.9% |
| 24_MVLV35890_Transformer | 275.0 kVA | 5.5% |
| 24_MVLV25266_Transformer | 693.0 kVA | 27.7% |
| 24_MVLV20544_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV33828_Transformer | 110.0 kVA | 1.7% |
| 24_MVLV64495_Transformer | 440.0 kVA | 18.9% |
| 24_MVLV85916_Transformer | 275.0 kVA | 5.9% |
| 24_MVLV48455_Transformer | 275.0 kVA | 8.6% |
| 24_MVLV45670_Transformer | 440.0 kVA | 18.1% |
| 24_MVLV70506_Transformer | 110.0 kVA | 6.6% |
| 24_MVLV47385_Transformer | 176.0 kVA | 9.6% |
| 24_MVLV30159_Transformer | 176.0 kVA | 17.0% |
| 24_MVLV20545_Transformer | 110.0 kVA | 6.1% |
| 24_MVLV69925_Transformer | 176.0 kVA | 7.7% |
| 24_MVLV85910_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV65753_Transformer | 110.0 kVA | 2.8% |
| 24_MVLV66603_Transformer | 275.0 kVA | 16.2% |
| 24_MVLV13947_Transformer | 110.0 kVA | 6.3% |
| 24_MVLV66632_Transformer | 176.0 kVA | 13.0% |
| 24_MVLV27685_Transformer | 176.0 kVA | 5.6% |
| 24_MVLV34287_Transformer | 176.0 kVA | 19.0% |
| 24_MVLV53801_Transformer | 110.0 kVA | 4.8% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.57 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '24_V.AVR' (MV, 11.78 kV) has an electrical reach of 21.6 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus221237' (LV, 0.24 kV) has an electrical reach of 24.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus221253' (LV, 0.24 kV) has an electrical reach of 15.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus221216' (LV, 0.24 kV) has an electrical reach of 21.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus220954' (LV, 0.24 kV) has an electrical reach of 0.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 739 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 739 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 70 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 162 |
| LV_236V | 4-wire | 577 / 577 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 577 |
| Neutral branches | 507 |
| Grounding points | 70 |
| Neutral sections | 70 |
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
| 11.78 kV | 162 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 71 |
| Islands without voltage reference | 0 |
| Line impedance spread | 5140.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 577 / 162 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 623 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 623 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus220689_production, 24_LVBus220693_production, 24_LVBus220694_production, 24_LVBus220696_production, 24_LVBus220697_production, 24_LVBus220699_production, 24_LVBus220700_production, 24_LVBus220701_production, 24_LVBus220702_production, 24_LVBus220703_production, 24_LVBus220704_production, 24_LVBus220705_production, 24_LVBus220706_production, 24_LVBus220707_production, 24_LVBus220708_production, 24_LVBus220709_production, 24_LVBus220710_production, 24_LVBus220711_production, 24_LVBus220712_production, 24_LVBus220713_consumption, 24_LVBus220713_production, 24_LVBus220714_production, 24_LVBus220715_production, 24_LVBus220716_production, 24_LVBus220717_production, 24_LVBus220718_consumption, 24_LVBus220718_production, 24_LVBus220719_production, 24_LVBus220721_consumption, 24_LVBus220721_production, 24_LVBus220722_production, 24_LVBus220724_production, 24_LVBus220725_production, 24_LVBus220727_production, 24_LVBus220728_production, 24_LVBus220729_production, 24_LVBus220731_production, 24_LVBus220732_production, 24_LVBus220733_production, 24_LVBus220734_consumption, 24_LVBus220734_production, 24_LVBus220735_consumption, 24_LVBus220735_production, 24_LVBus220736_production, 24_LVBus220740_consumption, 24_LVBus220740_production, 24_LVBus220741_consumption, 24_LVBus220741_production, 24_LVBus220744_production, 24_LVBus220745_production, 24_LVBus220748_production, 24_LVBus220749_consumption, 24_LVBus220749_production, 24_LVBus220750_production, 24_LVBus220751_production, 24_LVBus220752_production, 24_LVBus220753_production, 24_LVBus220755_production, 24_LVBus220756_production, 24_LVBus220757_production, 24_LVBus220758_production, 24_LVBus220759_production, 24_LVBus220761_production, 24_LVBus220762_production, 24_LVBus220763_production, 24_LVBus220765_production, 24_LVBus220766_production, 24_LVBus220767_consumption, 24_LVBus220767_production, 24_LVBus220769_production, 24_LVBus220770_production, 24_LVBus220771_consumption, 24_LVBus220771_production, 24_LVBus220773_production, 24_LVBus220775_production, 24_LVBus220776_production, 24_LVBus220777_production, 24_LVBus220779_production, 24_LVBus220781_consumption, 24_LVBus220781_production, 24_LVBus220782_production, 24_LVBus220783_production, 24_LVBus220785_production, 24_LVBus220787_consumption, 24_LVBus220787_production, 24_LVBus220788_production, 24_LVBus220789_production, 24_LVBus220790_production, 24_LVBus220792_production, 24_LVBus220794_production, 24_LVBus220795_production, 24_LVBus220796_production, 24_LVBus220797_production, 24_LVBus220798_production, 24_LVBus220799_production, 24_LVBus220800_production, 24_LVBus220802_production, 24_LVBus220803_production, 24_LVBus220805_consumption, 24_LVBus220805_production, 24_LVBus220806_production, 24_LVBus220807_production, 24_LVBus220809_production, 24_LVBus220810_production, 24_LVBus220811_production, 24_LVBus220812_production, 24_LVBus220813_production, 24_LVBus220815_consumption, 24_LVBus220815_production, 24_LVBus220817_consumption, 24_LVBus220817_production, 24_LVBus220818_production, 24_LVBus220819_production, 24_LVBus220820_production, 24_LVBus220822_consumption, 24_LVBus220822_production, 24_LVBus220823_production, 24_LVBus220825_consumption, 24_LVBus220825_production, 24_LVBus220827_production, 24_LVBus220828_production, 24_LVBus220829_consumption, 24_LVBus220829_production, 24_LVBus220830_production, 24_LVBus220831_production, 24_LVBus220832_production, 24_LVBus220833_production, 24_LVBus220835_production, 24_LVBus220836_production, 24_LVBus220837_production, 24_LVBus220838_production, 24_LVBus220839_production, 24_LVBus220841_consumption, 24_LVBus220841_production, 24_LVBus220842_consumption, 24_LVBus220842_production, 24_LVBus220843_consumption, 24_LVBus220843_production, 24_LVBus220844_production, 24_LVBus220845_consumption, 24_LVBus220845_production, 24_LVBus220848_production, 24_LVBus220849_production, 24_LVBus220850_production, 24_LVBus220851_production, 24_LVBus220852_production, 24_LVBus220853_production, 24_LVBus220855_production, 24_LVBus220856_production, 24_LVBus220857_production, 24_LVBus220858_production, 24_LVBus220859_production, 24_LVBus220861_consumption, 24_LVBus220861_production, 24_LVBus220862_production, 24_LVBus220863_consumption, 24_LVBus220863_production, 24_LVBus220864_production, 24_LVBus220867_production, 24_LVBus220868_production, 24_LVBus220869_production, 24_LVBus220870_production, 24_LVBus220872_production, 24_LVBus220876_consumption, 24_LVBus220876_production, 24_LVBus220877_production, 24_LVBus220878_production, 24_LVBus220879_production, 24_LVBus220880_production, 24_LVBus220881_production, 24_LVBus220883_production, 24_LVBus220884_production, 24_LVBus220886_production, 24_LVBus220888_production, 24_LVBus220889_consumption, 24_LVBus220889_production, 24_LVBus220890_production, 24_LVBus220891_production, 24_LVBus220892_consumption, 24_LVBus220892_production, 24_LVBus220894_production, 24_LVBus220896_production, 24_LVBus220897_production, 24_LVBus220898_production, 24_LVBus220899_production, 24_LVBus220901_production, 24_LVBus220903_production, 24_LVBus220904_production, 24_LVBus220905_production, 24_LVBus220906_production, 24_LVBus220907_production, 24_LVBus220911_production, 24_LVBus220913_production, 24_LVBus220914_consumption, 24_LVBus220914_production, 24_LVBus220915_production, 24_LVBus220916_production, 24_LVBus220917_production, 24_LVBus220918_production, 24_LVBus220919_production, 24_LVBus220923_consumption, 24_LVBus220923_production, 24_LVBus220924_production, 24_LVBus220925_production, 24_LVBus220926_consumption, 24_LVBus220926_production, 24_LVBus220927_production, 24_LVBus220931_consumption, 24_LVBus220931_production, 24_LVBus220932_consumption, 24_LVBus220932_production, 24_LVBus220933_production, 24_LVBus220934_consumption, 24_LVBus220934_production, 24_LVBus220935_consumption, 24_LVBus220935_production, 24_LVBus220936_consumption, 24_LVBus220936_production, 24_LVBus220937_consumption, 24_LVBus220937_production, 24_LVBus220938_production, 24_LVBus220942_production, 24_LVBus220944_consumption, 24_LVBus220944_production, 24_LVBus220946_consumption, 24_LVBus220946_production, 24_LVBus220948_consumption, 24_LVBus220948_production, 24_LVBus220950_consumption, 24_LVBus220950_production, 24_LVBus220952_consumption, 24_LVBus220952_production, 24_LVBus220954_consumption, 24_LVBus220954_production, 24_LVBus220956_consumption, 24_LVBus220956_production, 24_LVBus220957_consumption, 24_LVBus220957_production, 24_LVBus220958_production, 24_LVBus220959_production, 24_LVBus220963_production, 24_LVBus220964_production, 24_LVBus220966_production, 24_LVBus220967_production, 24_LVBus220968_production, 24_LVBus220969_production, 24_LVBus220970_production, 24_LVBus220971_production, 24_LVBus220973_production, 24_LVBus220974_production, 24_LVBus220976_consumption, 24_LVBus220976_production, 24_LVBus220977_production, 24_LVBus220978_production, 24_LVBus220979_production, 24_LVBus220982_production, 24_LVBus220983_production, 24_LVBus220984_production, 24_LVBus220985_production, 24_LVBus220987_consumption, 24_LVBus220987_production, 24_LVBus220988_production, 24_LVBus220989_production, 24_LVBus220990_production, 24_LVBus220991_production, 24_LVBus220992_production, 24_LVBus220994_production, 24_LVBus220995_production, 24_LVBus220996_production, 24_LVBus220997_production, 24_LVBus220998_production, 24_LVBus220999_consumption, 24_LVBus220999_production, 24_LVBus221000_production, 24_LVBus221002_production, 24_LVBus221004_consumption, 24_LVBus221004_production, 24_LVBus221005_production, 24_LVBus221006_production, 24_LVBus221007_production, 24_LVBus221009_consumption, 24_LVBus221009_production, 24_LVBus221010_production, 24_LVBus221011_production, 24_LVBus221012_production, 24_LVBus221014_production, 24_LVBus221015_consumption, 24_LVBus221015_production, 24_LVBus221016_production, 24_LVBus221017_production, 24_LVBus221019_consumption, 24_LVBus221019_production, 24_LVBus221020_production, 24_LVBus221021_production, 24_LVBus221022_production, 24_LVBus221024_consumption, 24_LVBus221024_production, 24_LVBus221025_production, 24_LVBus221026_consumption, 24_LVBus221026_production, 24_LVBus221029_production, 24_LVBus221030_production, 24_LVBus221031_production, 24_LVBus221033_production, 24_LVBus221034_production, 24_LVBus221035_consumption, 24_LVBus221035_production, 24_LVBus221036_production, 24_LVBus221037_production, 24_LVBus221038_consumption, 24_LVBus221038_production, 24_LVBus221039_production, 24_LVBus221040_consumption, 24_LVBus221040_production, 24_LVBus221043_production, 24_LVBus221044_production, 24_LVBus221045_production, 24_LVBus221046_production, 24_LVBus221047_production, 24_LVBus221048_production, 24_LVBus221049_production, 24_LVBus221050_production, 24_LVBus221052_production, 24_LVBus221054_production, 24_LVBus221055_production, 24_LVBus221056_production, 24_LVBus221058_consumption, 24_LVBus221058_production, 24_LVBus221059_production, 24_LVBus221060_production, 24_LVBus221062_production, 24_LVBus221063_consumption, 24_LVBus221063_production, 24_LVBus221064_production, 24_LVBus221065_production, 24_LVBus221066_production, 24_LVBus221067_consumption, 24_LVBus221067_production, 24_LVBus221068_production, 24_LVBus221070_production, 24_LVBus221071_production, 24_LVBus221072_production, 24_LVBus221074_production, 24_LVBus221075_consumption, 24_LVBus221075_production, 24_LVBus221076_production, 24_LVBus221077_production, 24_LVBus221078_production, 24_LVBus221079_production, 24_LVBus221080_production, 24_LVBus221081_production, 24_LVBus221082_production, 24_LVBus221083_production, 24_LVBus221084_production, 24_LVBus221085_production, 24_LVBus221087_consumption, 24_LVBus221087_production, 24_LVBus221088_production, 24_LVBus221090_consumption, 24_LVBus221090_production, 24_LVBus221091_production, 24_LVBus221092_production, 24_LVBus221093_production, 24_LVBus221094_production, 24_LVBus221095_production, 24_LVBus221096_production, 24_LVBus221097_production, 24_LVBus221098_consumption, 24_LVBus221098_production, 24_LVBus221100_production, 24_LVBus221101_production, 24_LVBus221102_production, 24_LVBus221103_production, 24_LVBus221104_production, 24_LVBus221106_production, 24_LVBus221107_production, 24_LVBus221108_production, 24_LVBus221109_consumption, 24_LVBus221109_production, 24_LVBus221110_production, 24_LVBus221111_production, 24_LVBus221113_production, 24_LVBus221114_production, 24_LVBus221115_production, 24_LVBus221116_production, 24_LVBus221117_production, 24_LVBus221118_production, 24_LVBus221122_production, 24_LVBus221123_consumption, 24_LVBus221123_production, 24_LVBus221124_production, 24_LVBus221126_production, 24_LVBus221127_production, 24_LVBus221128_production, 24_LVBus221129_production, 24_LVBus221130_production, 24_LVBus221132_production, 24_LVBus221133_production, 24_LVBus221134_production, 24_LVBus221136_production, 24_LVBus221138_production, 24_LVBus221140_production, 24_LVBus221141_production, 24_LVBus221142_production, 24_LVBus221143_consumption, 24_LVBus221143_production, 24_LVBus221144_production, 24_LVBus221146_consumption, 24_LVBus221146_production, 24_LVBus221147_production, 24_LVBus221148_production, 24_LVBus221149_production, 24_LVBus221150_production, 24_LVBus221151_production, 24_LVBus221152_production, 24_LVBus221153_production, 24_LVBus221154_production, 24_LVBus221155_production, 24_LVBus221156_consumption, 24_LVBus221156_production, 24_LVBus221157_production, 24_LVBus221158_production, 24_LVBus221159_production, 24_LVBus221161_production, 24_LVBus221162_production, 24_LVBus221163_production, 24_LVBus221164_production, 24_LVBus221165_production, 24_LVBus221166_production, 24_LVBus221167_production, 24_LVBus221169_production, 24_LVBus221170_production, 24_LVBus221172_production, 24_LVBus221173_production, 24_LVBus221174_production, 24_LVBus221175_production, 24_LVBus221177_production, 24_LVBus221178_production, 24_LVBus221179_production, 24_LVBus221180_production, 24_LVBus221182_production, 24_LVBus221183_production, 24_LVBus221184_production, 24_LVBus221185_production, 24_LVBus221186_production, 24_LVBus221187_production, 24_LVBus221188_production, 24_LVBus221192_consumption, 24_LVBus221192_production, 24_LVBus221193_production, 24_LVBus221194_production, 24_LVBus221195_production, 24_LVBus221197_consumption, 24_LVBus221197_production, 24_LVBus221198_consumption, 24_LVBus221198_production, 24_LVBus221199_consumption, 24_LVBus221199_production, 24_LVBus221200_production, 24_LVBus221201_production, 24_LVBus221203_production, 24_LVBus221204_production, 24_LVBus221205_production, 24_LVBus221206_production, 24_LVBus221207_consumption, 24_LVBus221207_production, 24_LVBus221208_production, 24_LVBus221210_production, 24_LVBus221212_production, 24_LVBus221213_production, 24_LVBus221214_production, 24_LVBus221216_production, 24_LVBus221217_production, 24_LVBus221219_production, 24_LVBus221220_consumption, 24_LVBus221220_production, 24_LVBus221221_production, 24_LVBus221222_consumption, 24_LVBus221222_production, 24_LVBus221223_production, 24_LVBus221227_consumption, 24_LVBus221227_production, 24_LVBus221228_production, 24_LVBus221229_production, 24_LVBus221230_production, 24_LVBus221233_production, 24_LVBus221234_production, 24_LVBus221235_production, 24_LVBus221237_production, 24_LVBus221239_production, 24_LVBus221240_production, 24_LVBus221241_consumption, 24_LVBus221241_production, 24_LVBus221242_production, 24_LVBus221243_production, 24_LVBus221244_consumption, 24_LVBus221244_production, 24_LVBus221245_consumption, 24_LVBus221245_production, 24_LVBus221247_production, 24_LVBus221248_production, 24_LVBus221249_consumption, 24_LVBus221249_production, 24_LVBus221250_consumption, 24_LVBus221250_production, 24_LVBus221251_production, 24_LVBus221253_consumption, 24_LVBus221253_production, 24_LVBus221255_production, 24_LVBus221256_production, 24_LVBus221257_production, 24_LVBus221258_consumption, 24_LVBus221258_production, 24_LVBus221259_consumption, 24_LVBus221259_production, 24_LVBus221260_production, 24_LVBus221261_production, 24_LVBus221262_production, 24_LVBus221263_production, 24_LVBus221264_production, 24_LVBus221265_consumption, 24_LVBus221265_production, 24_LVBus221267_production, 24_LVBus221268_production, 24_LVBus221269_production, 24_LVBus221270_consumption, 24_LVBus221270_production, 24_LVBus221271_consumption, 24_LVBus221271_production, 24_LVBus221272_production, 24_LVBus221273_production, 24_LVBus221275_production, 24_LVBus221276_production, 24_LVBus221277_production, 24_LVBus221278_production, 24_LVBus221279_production, 24_LVBus221280_production, 24_LVBus221281_consumption, 24_LVBus221281_production, 24_LVBus221283_production, 24_LVBus221285_production, 24_LVBus221286_production, 24_LVBus221287_production, 24_LVBus221288_production, 24_LVBus221289_production, 24_LVBus221291_production, 24_LVBus221292_production, 24_LVBus221293_production, 24_LVBus832407_consumption, 24_LVBus832407_production, 24_LVBus832408_consumption, 24_LVBus832408_production, 24_LVBus832787_consumption, 24_LVBus832787_production, 24_LVBus833311_production, 24_LVBus833824_production, 24_LVBus835929_production, 24_LVBus835930_production, 24_LVBus838927_production, 24_LVBus842201_production, 24_LVBus843697_production, 24_LVBus843699_consumption, 24_LVBus843699_production, 24_LVBus843812_production, 24_LVBus843813_production, 24_LVBus843814_production, 24_LVBus844278_consumption, 24_LVBus844278_production, 24_LVBus852187_production, 24_LVBus855540_production, 24_LVBus856086_production, 24_LVBus856544_production, 24_LVBus857041_consumption, 24_LVBus857041_production, 24_LVBus857042_consumption, 24_LVBus857042_production, 24_LVBus857043_consumption, 24_LVBus857043_production, 24_LVBus857044_production, 24_LVBus857045_production, 24_LVBus857046_production, 24_LVBus857047_production, 24_LVBus857469_production, 24_LVBus857470_production, 24_LVBus858484_production, 24_LVBus858485_production, 24_LVBus858993_production, 24_LVBus859815_production, 24_LVBus860074_consumption, 24_LVBus860074_production, 24_LVBus860075_consumption, 24_LVBus860075_production, 24_LVBus860111_production, 24_LVBus860438_production, 24_LVBus860439_consumption, 24_LVBus860439_production, 24_LVBus860440_consumption, 24_LVBus860440_production, 24_LVBus860532_production, 24_LVBus860533_production, 24_LVBus861561_consumption, 24_LVBus861561_production, 24_LVBus861562_consumption, 24_LVBus861562_production, 24_LVBus861563_consumption, 24_LVBus861563_production, 24_LVBus861564_production, 24_LVBus861565_consumption, 24_LVBus861565_production, 24_LVBus861566_production, 24_LVBus861567_production, 24_MVLV24494_consumption, 24_MVLV24494_production, 24_MVLV29603_consumption, 24_MVLV29603_production, 24_MVLV55274_consumption, 24_MVLV55274_production, 24_MVLV69124_consumption, 24_MVLV69124_production, 24_MVLV71043_consumption, 24_MVLV71043_production, 24_MVLV74478_consumption, 24_MVLV74478_production.

## 9. Data Quality Summary

**Total findings:** 408 (0 errors, 5 warnings, 403 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  7 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  622 of 1026 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.57 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  623 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221102_consumption`  
  Load '24_LVBus221102_consumption' has phase imbalance of 148.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221068_consumption`  
  Load '24_LVBus221068_consumption' has phase imbalance of 133.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221268_consumption`  
  Load '24_LVBus221268_consumption' has phase imbalance of 186.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220694_consumption`  
  Load '24_LVBus220694_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221117_consumption`  
  Load '24_LVBus221117_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221205_consumption`  
  Load '24_LVBus221205_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220988_consumption`  
  Load '24_LVBus220988_consumption' has phase imbalance of 266.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220992_consumption`  
  Load '24_LVBus220992_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857045_consumption`  
  Load '24_LVBus857045_consumption' has phase imbalance of 184.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220693_consumption`  
  Load '24_LVBus220693_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221029_consumption`  
  Load '24_LVBus221029_consumption' has phase imbalance of 217.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220879_consumption`  
  Load '24_LVBus220879_consumption' has phase imbalance of 263.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220891_consumption`  
  Load '24_LVBus220891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221002_consumption`  
  Load '24_LVBus221002_consumption' has phase imbalance of 134.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus833311_consumption`  
  Load '24_LVBus833311_consumption' has phase imbalance of 112.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221034_consumption`  
  Load '24_LVBus221034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220827_consumption`  
  Load '24_LVBus220827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221044_consumption`  
  Load '24_LVBus221044_consumption' has phase imbalance of 99.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221065_consumption`  
  Load '24_LVBus221065_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221261_consumption`  
  Load '24_LVBus221261_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220963_consumption`  
  Load '24_LVBus220963_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus835930_consumption`  
  Load '24_LVBus835930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220729_consumption`  
  Load '24_LVBus220729_consumption' has phase imbalance of 261.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220857_consumption`  
  Load '24_LVBus220857_consumption' has phase imbalance of 276.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221262_consumption`  
  Load '24_LVBus221262_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220732_consumption`  
  Load '24_LVBus220732_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221275_consumption`  
  Load '24_LVBus221275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221149_consumption`  
  Load '24_LVBus221149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221110_consumption`  
  Load '24_LVBus221110_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus835929_consumption`  
  Load '24_LVBus835929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221080_consumption`  
  Load '24_LVBus221080_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220830_consumption`  
  Load '24_LVBus220830_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220859_consumption`  
  Load '24_LVBus220859_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220782_consumption`  
  Load '24_LVBus220782_consumption' has phase imbalance of 138.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221030_consumption`  
  Load '24_LVBus221030_consumption' has phase imbalance of 198.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221083_consumption`  
  Load '24_LVBus221083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220748_consumption`  
  Load '24_LVBus220748_consumption' has phase imbalance of 227.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220762_consumption`  
  Load '24_LVBus220762_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221260_consumption`  
  Load '24_LVBus221260_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220858_consumption`  
  Load '24_LVBus220858_consumption' has phase imbalance of 104.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221012_consumption`  
  Load '24_LVBus221012_consumption' has phase imbalance of 260.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221128_consumption`  
  Load '24_LVBus221128_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221169_consumption`  
  Load '24_LVBus221169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221101_consumption`  
  Load '24_LVBus221101_consumption' has phase imbalance of 101.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220964_consumption`  
  Load '24_LVBus220964_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221043_consumption`  
  Load '24_LVBus221043_consumption' has phase imbalance of 291.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221033_consumption`  
  Load '24_LVBus221033_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220894_consumption`  
  Load '24_LVBus220894_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221150_consumption`  
  Load '24_LVBus221150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220942_consumption`  
  Load '24_LVBus220942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220913_consumption`  
  Load '24_LVBus220913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220800_consumption`  
  Load '24_LVBus220800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221159_consumption`  
  Load '24_LVBus221159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221000_consumption`  
  Load '24_LVBus221000_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221151_consumption`  
  Load '24_LVBus221151_consumption' has phase imbalance of 100.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220903_consumption`  
  Load '24_LVBus220903_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220759_consumption`  
  Load '24_LVBus220759_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221106_consumption`  
  Load '24_LVBus221106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220966_consumption`  
  Load '24_LVBus220966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221091_consumption`  
  Load '24_LVBus221091_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221134_consumption`  
  Load '24_LVBus221134_consumption' has phase imbalance of 207.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221085_consumption`  
  Load '24_LVBus221085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220917_consumption`  
  Load '24_LVBus220917_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220870_consumption`  
  Load '24_LVBus220870_consumption' has phase imbalance of 148.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221070_consumption`  
  Load '24_LVBus221070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220709_consumption`  
  Load '24_LVBus220709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221219_consumption`  
  Load '24_LVBus221219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220862_consumption`  
  Load '24_LVBus220862_consumption' has phase imbalance of 108.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221113_consumption`  
  Load '24_LVBus221113_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221203_consumption`  
  Load '24_LVBus221203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220933_consumption`  
  Load '24_LVBus220933_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220919_consumption`  
  Load '24_LVBus220919_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221108_consumption`  
  Load '24_LVBus221108_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220766_consumption`  
  Load '24_LVBus220766_consumption' has phase imbalance of 278.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221178_consumption`  
  Load '24_LVBus221178_consumption' has phase imbalance of 86.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220994_consumption`  
  Load '24_LVBus220994_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220711_consumption`  
  Load '24_LVBus220711_consumption' has phase imbalance of 98.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221255_consumption`  
  Load '24_LVBus221255_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220990_consumption`  
  Load '24_LVBus220990_consumption' has phase imbalance of 253.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221292_consumption`  
  Load '24_LVBus221292_consumption' has phase imbalance of 249.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220915_consumption`  
  Load '24_LVBus220915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220886_consumption`  
  Load '24_LVBus220886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221148_consumption`  
  Load '24_LVBus221148_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220806_consumption`  
  Load '24_LVBus220806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221264_consumption`  
  Load '24_LVBus221264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220733_consumption`  
  Load '24_LVBus220733_consumption' has phase imbalance of 27.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857044_consumption`  
  Load '24_LVBus857044_consumption' has phase imbalance of 287.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221007_consumption`  
  Load '24_LVBus221007_consumption' has phase imbalance of 285.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221291_consumption`  
  Load '24_LVBus221291_consumption' has phase imbalance of 123.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221118_consumption`  
  Load '24_LVBus221118_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221010_consumption`  
  Load '24_LVBus221010_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221216_consumption`  
  Load '24_LVBus221216_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221186_consumption`  
  Load '24_LVBus221186_consumption' has phase imbalance of 246.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221165_consumption`  
  Load '24_LVBus221165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221122_consumption`  
  Load '24_LVBus221122_consumption' has phase imbalance of 28.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221182_consumption`  
  Load '24_LVBus221182_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220702_consumption`  
  Load '24_LVBus220702_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221204_consumption`  
  Load '24_LVBus221204_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221276_consumption`  
  Load '24_LVBus221276_consumption' has phase imbalance of 258.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220750_consumption`  
  Load '24_LVBus220750_consumption' has phase imbalance of 165.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843813_consumption`  
  Load '24_LVBus843813_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220890_consumption`  
  Load '24_LVBus220890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221163_consumption`  
  Load '24_LVBus221163_consumption' has phase imbalance of 290.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221208_consumption`  
  Load '24_LVBus221208_consumption' has phase imbalance of 107.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220812_consumption`  
  Load '24_LVBus220812_consumption' has phase imbalance of 60.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220744_consumption`  
  Load '24_LVBus220744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220818_consumption`  
  Load '24_LVBus220818_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220794_consumption`  
  Load '24_LVBus220794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861564_consumption`  
  Load '24_LVBus861564_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221286_consumption`  
  Load '24_LVBus221286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220884_consumption`  
  Load '24_LVBus220884_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221183_consumption`  
  Load '24_LVBus221183_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221144_consumption`  
  Load '24_LVBus221144_consumption' has phase imbalance of 280.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220844_consumption`  
  Load '24_LVBus220844_consumption' has phase imbalance of 52.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221170_consumption`  
  Load '24_LVBus221170_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221022_consumption`  
  Load '24_LVBus221022_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221076_consumption`  
  Load '24_LVBus221076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221221_consumption`  
  Load '24_LVBus221221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220813_consumption`  
  Load '24_LVBus220813_consumption' has phase imbalance of 236.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220831_consumption`  
  Load '24_LVBus220831_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857469_consumption`  
  Load '24_LVBus857469_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221210_consumption`  
  Load '24_LVBus221210_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221242_consumption`  
  Load '24_LVBus221242_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220971_consumption`  
  Load '24_LVBus220971_consumption' has phase imbalance of 218.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221031_consumption`  
  Load '24_LVBus221031_consumption' has phase imbalance of 75.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221166_consumption`  
  Load '24_LVBus221166_consumption' has phase imbalance of 101.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220706_consumption`  
  Load '24_LVBus220706_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861566_consumption`  
  Load '24_LVBus861566_consumption' has phase imbalance of 43.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220716_consumption`  
  Load '24_LVBus220716_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221016_consumption`  
  Load '24_LVBus221016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220849_consumption`  
  Load '24_LVBus220849_consumption' has phase imbalance of 52.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221279_consumption`  
  Load '24_LVBus221279_consumption' has phase imbalance of 114.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus852187_consumption`  
  Load '24_LVBus852187_consumption' has phase imbalance of 82.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220924_consumption`  
  Load '24_LVBus220924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221055_consumption`  
  Load '24_LVBus221055_consumption' has phase imbalance of 121.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221020_consumption`  
  Load '24_LVBus221020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220868_consumption`  
  Load '24_LVBus220868_consumption' has phase imbalance of 240.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220704_consumption`  
  Load '24_LVBus220704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220689_consumption`  
  Load '24_LVBus220689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220896_consumption`  
  Load '24_LVBus220896_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220904_consumption`  
  Load '24_LVBus220904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221201_consumption`  
  Load '24_LVBus221201_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221195_consumption`  
  Load '24_LVBus221195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221269_consumption`  
  Load '24_LVBus221269_consumption' has phase imbalance of 106.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220792_consumption`  
  Load '24_LVBus220792_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220998_consumption`  
  Load '24_LVBus220998_consumption' has phase imbalance of 264.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221006_consumption`  
  Load '24_LVBus221006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220836_consumption`  
  Load '24_LVBus220836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221172_consumption`  
  Load '24_LVBus221172_consumption' has phase imbalance of 288.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221114_consumption`  
  Load '24_LVBus221114_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221233_consumption`  
  Load '24_LVBus221233_consumption' has phase imbalance of 266.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus858484_consumption`  
  Load '24_LVBus858484_consumption' has phase imbalance of 248.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220745_consumption`  
  Load '24_LVBus220745_consumption' has phase imbalance of 132.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220728_consumption`  
  Load '24_LVBus220728_consumption' has phase imbalance of 151.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221142_consumption`  
  Load '24_LVBus221142_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221084_consumption`  
  Load '24_LVBus221084_consumption' has phase imbalance of 138.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221173_consumption`  
  Load '24_LVBus221173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221011_consumption`  
  Load '24_LVBus221011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus858993_consumption`  
  Load '24_LVBus858993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220712_consumption`  
  Load '24_LVBus220712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221283_consumption`  
  Load '24_LVBus221283_consumption' has phase imbalance of 31.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221052_consumption`  
  Load '24_LVBus221052_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220905_consumption`  
  Load '24_LVBus220905_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220756_consumption`  
  Load '24_LVBus220756_consumption' has phase imbalance of 246.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220989_consumption`  
  Load '24_LVBus220989_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220828_consumption`  
  Load '24_LVBus220828_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220938_consumption`  
  Load '24_LVBus220938_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220833_consumption`  
  Load '24_LVBus220833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220811_consumption`  
  Load '24_LVBus220811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221193_consumption`  
  Load '24_LVBus221193_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221161_consumption`  
  Load '24_LVBus221161_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221229_consumption`  
  Load '24_LVBus221229_consumption' has phase imbalance of 216.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220810_consumption`  
  Load '24_LVBus220810_consumption' has phase imbalance of 20.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220855_consumption`  
  Load '24_LVBus220855_consumption' has phase imbalance of 286.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221126_consumption`  
  Load '24_LVBus221126_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220997_consumption`  
  Load '24_LVBus220997_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221037_consumption`  
  Load '24_LVBus221037_consumption' has phase imbalance of 39.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220699_consumption`  
  Load '24_LVBus220699_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220958_consumption`  
  Load '24_LVBus220958_consumption' has phase imbalance of 166.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus856544_consumption`  
  Load '24_LVBus856544_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus859815_consumption`  
  Load '24_LVBus859815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220758_consumption`  
  Load '24_LVBus220758_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220795_consumption`  
  Load '24_LVBus220795_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus833824_consumption`  
  Load '24_LVBus833824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221047_consumption`  
  Load '24_LVBus221047_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220856_consumption`  
  Load '24_LVBus220856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221280_consumption`  
  Load '24_LVBus221280_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220978_consumption`  
  Load '24_LVBus220978_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220724_consumption`  
  Load '24_LVBus220724_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221064_consumption`  
  Load '24_LVBus221064_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857470_consumption`  
  Load '24_LVBus857470_consumption' has phase imbalance of 206.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221217_consumption`  
  Load '24_LVBus221217_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220796_consumption`  
  Load '24_LVBus220796_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221048_consumption`  
  Load '24_LVBus221048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221072_consumption`  
  Load '24_LVBus221072_consumption' has phase imbalance of 252.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221155_consumption`  
  Load '24_LVBus221155_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221230_consumption`  
  Load '24_LVBus221230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221056_consumption`  
  Load '24_LVBus221056_consumption' has phase imbalance of 225.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221214_consumption`  
  Load '24_LVBus221214_consumption' has phase imbalance of 257.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221185_consumption`  
  Load '24_LVBus221185_consumption' has phase imbalance of 71.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221127_consumption`  
  Load '24_LVBus221127_consumption' has phase imbalance of 44.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220797_consumption`  
  Load '24_LVBus220797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220790_consumption`  
  Load '24_LVBus220790_consumption' has phase imbalance of 213.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220881_consumption`  
  Load '24_LVBus220881_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220765_consumption`  
  Load '24_LVBus220765_consumption' has phase imbalance of 64.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220763_consumption`  
  Load '24_LVBus220763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220901_consumption`  
  Load '24_LVBus220901_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843814_consumption`  
  Load '24_LVBus843814_consumption' has phase imbalance of 209.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221206_consumption`  
  Load '24_LVBus221206_consumption' has phase imbalance of 295.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221243_consumption`  
  Load '24_LVBus221243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220835_consumption`  
  Load '24_LVBus220835_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220701_consumption`  
  Load '24_LVBus220701_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220925_consumption`  
  Load '24_LVBus220925_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221177_consumption`  
  Load '24_LVBus221177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221021_consumption`  
  Load '24_LVBus221021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221103_consumption`  
  Load '24_LVBus221103_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221129_consumption`  
  Load '24_LVBus221129_consumption' has phase imbalance of 274.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221287_consumption`  
  Load '24_LVBus221287_consumption' has phase imbalance of 179.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220727_consumption`  
  Load '24_LVBus220727_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221228_consumption`  
  Load '24_LVBus221228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220899_consumption`  
  Load '24_LVBus220899_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221116_consumption`  
  Load '24_LVBus221116_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221082_consumption`  
  Load '24_LVBus221082_consumption' has phase imbalance of 286.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220991_consumption`  
  Load '24_LVBus220991_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221267_consumption`  
  Load '24_LVBus221267_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220973_consumption`  
  Load '24_LVBus220973_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220832_consumption`  
  Load '24_LVBus220832_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221167_consumption`  
  Load '24_LVBus221167_consumption' has phase imbalance of 37.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus838927_consumption`  
  Load '24_LVBus838927_consumption' has phase imbalance of 103.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221092_consumption`  
  Load '24_LVBus221092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220852_consumption`  
  Load '24_LVBus220852_consumption' has phase imbalance of 108.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220703_consumption`  
  Load '24_LVBus220703_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221187_consumption`  
  Load '24_LVBus221187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221141_consumption`  
  Load '24_LVBus221141_consumption' has phase imbalance of 129.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220867_consumption`  
  Load '24_LVBus220867_consumption' has phase imbalance of 236.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220916_consumption`  
  Load '24_LVBus220916_consumption' has phase imbalance of 265.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221079_consumption`  
  Load '24_LVBus221079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221017_consumption`  
  Load '24_LVBus221017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221164_consumption`  
  Load '24_LVBus221164_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220785_consumption`  
  Load '24_LVBus220785_consumption' has phase imbalance of 280.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221212_consumption`  
  Load '24_LVBus221212_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220898_consumption`  
  Load '24_LVBus220898_consumption' has phase imbalance of 232.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221223_consumption`  
  Load '24_LVBus221223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220977_consumption`  
  Load '24_LVBus220977_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860438_consumption`  
  Load '24_LVBus860438_consumption' has phase imbalance of 268.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220751_consumption`  
  Load '24_LVBus220751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus856086_consumption`  
  Load '24_LVBus856086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221194_consumption`  
  Load '24_LVBus221194_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221240_consumption`  
  Load '24_LVBus221240_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221049_consumption`  
  Load '24_LVBus221049_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221077_consumption`  
  Load '24_LVBus221077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221014_consumption`  
  Load '24_LVBus221014_consumption' has phase imbalance of 246.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220979_consumption`  
  Load '24_LVBus220979_consumption' has phase imbalance of 68.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221213_consumption`  
  Load '24_LVBus221213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220700_consumption`  
  Load '24_LVBus220700_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221248_consumption`  
  Load '24_LVBus221248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221147_consumption`  
  Load '24_LVBus221147_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220799_consumption`  
  Load '24_LVBus220799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220967_consumption`  
  Load '24_LVBus220967_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220907_consumption`  
  Load '24_LVBus220907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221278_consumption`  
  Load '24_LVBus221278_consumption' has phase imbalance of 138.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220725_consumption`  
  Load '24_LVBus220725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220982_consumption`  
  Load '24_LVBus220982_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221066_consumption`  
  Load '24_LVBus221066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220995_consumption`  
  Load '24_LVBus220995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221115_consumption`  
  Load '24_LVBus221115_consumption' has phase imbalance of 254.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220717_consumption`  
  Load '24_LVBus220717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860533_consumption`  
  Load '24_LVBus860533_consumption' has phase imbalance of 201.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220850_consumption`  
  Load '24_LVBus220850_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220753_consumption`  
  Load '24_LVBus220753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220897_consumption`  
  Load '24_LVBus220897_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220823_consumption`  
  Load '24_LVBus220823_consumption' has phase imbalance of 215.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220802_consumption`  
  Load '24_LVBus220802_consumption' has phase imbalance of 110.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220807_consumption`  
  Load '24_LVBus220807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221111_consumption`  
  Load '24_LVBus221111_consumption' has phase imbalance of 270.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220985_consumption`  
  Load '24_LVBus220985_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221188_consumption`  
  Load '24_LVBus221188_consumption' has phase imbalance of 238.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220872_consumption`  
  Load '24_LVBus220872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221239_consumption`  
  Load '24_LVBus221239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220906_consumption`  
  Load '24_LVBus220906_consumption' has phase imbalance of 267.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221097_consumption`  
  Load '24_LVBus221097_consumption' has phase imbalance of 284.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221152_consumption`  
  Load '24_LVBus221152_consumption' has phase imbalance of 92.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221277_consumption`  
  Load '24_LVBus221277_consumption' has phase imbalance of 220.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221234_consumption`  
  Load '24_LVBus221234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221071_consumption`  
  Load '24_LVBus221071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221285_consumption`  
  Load '24_LVBus221285_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221094_consumption`  
  Load '24_LVBus221094_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220803_consumption`  
  Load '24_LVBus220803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220736_consumption`  
  Load '24_LVBus220736_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221062_consumption`  
  Load '24_LVBus221062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221138_consumption`  
  Load '24_LVBus221138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220705_consumption`  
  Load '24_LVBus220705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220864_consumption`  
  Load '24_LVBus220864_consumption' has phase imbalance of 278.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220918_consumption`  
  Load '24_LVBus220918_consumption' has phase imbalance of 126.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221153_consumption`  
  Load '24_LVBus221153_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220715_consumption`  
  Load '24_LVBus220715_consumption' has phase imbalance of 259.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860532_consumption`  
  Load '24_LVBus860532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220710_consumption`  
  Load '24_LVBus220710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221140_consumption`  
  Load '24_LVBus221140_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221025_consumption`  
  Load '24_LVBus221025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221289_consumption`  
  Load '24_LVBus221289_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221059_consumption`  
  Load '24_LVBus221059_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221200_consumption`  
  Load '24_LVBus221200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220789_consumption`  
  Load '24_LVBus220789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221078_consumption`  
  Load '24_LVBus221078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220959_consumption`  
  Load '24_LVBus220959_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221256_consumption`  
  Load '24_LVBus221256_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220757_consumption`  
  Load '24_LVBus220757_consumption' has phase imbalance of 216.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221154_consumption`  
  Load '24_LVBus221154_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220838_consumption`  
  Load '24_LVBus220838_consumption' has phase imbalance of 283.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857047_consumption`  
  Load '24_LVBus857047_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220996_consumption`  
  Load '24_LVBus220996_consumption' has phase imbalance of 135.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220697_consumption`  
  Load '24_LVBus220697_consumption' has phase imbalance of 216.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220969_consumption`  
  Load '24_LVBus220969_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220809_consumption`  
  Load '24_LVBus220809_consumption' has phase imbalance of 135.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221162_consumption`  
  Load '24_LVBus221162_consumption' has phase imbalance of 257.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220761_consumption`  
  Load '24_LVBus220761_consumption' has phase imbalance of 129.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221180_consumption`  
  Load '24_LVBus221180_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221175_consumption`  
  Load '24_LVBus221175_consumption' has phase imbalance of 287.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221060_consumption`  
  Load '24_LVBus221060_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221263_consumption`  
  Load '24_LVBus221263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220888_consumption`  
  Load '24_LVBus220888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221158_consumption`  
  Load '24_LVBus221158_consumption' has phase imbalance of 150.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220911_consumption`  
  Load '24_LVBus220911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221184_consumption`  
  Load '24_LVBus221184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus842201_consumption`  
  Load '24_LVBus842201_consumption' has phase imbalance of 265.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220776_consumption`  
  Load '24_LVBus220776_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221273_consumption`  
  Load '24_LVBus221273_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220770_consumption`  
  Load '24_LVBus220770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220984_consumption`  
  Load '24_LVBus220984_consumption' has phase imbalance of 149.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221039_consumption`  
  Load '24_LVBus221039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843812_consumption`  
  Load '24_LVBus843812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221054_consumption`  
  Load '24_LVBus221054_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220970_consumption`  
  Load '24_LVBus220970_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221107_consumption`  
  Load '24_LVBus221107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221235_consumption`  
  Load '24_LVBus221235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220779_consumption`  
  Load '24_LVBus220779_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220820_consumption`  
  Load '24_LVBus220820_consumption' has phase imbalance of 214.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220983_consumption`  
  Load '24_LVBus220983_consumption' has phase imbalance of 202.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221133_consumption`  
  Load '24_LVBus221133_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220696_consumption`  
  Load '24_LVBus220696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220878_consumption`  
  Load '24_LVBus220878_consumption' has phase imbalance of 123.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860111_consumption`  
  Load '24_LVBus860111_consumption' has phase imbalance of 230.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857046_consumption`  
  Load '24_LVBus857046_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221124_consumption`  
  Load '24_LVBus221124_consumption' has phase imbalance of 182.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220722_consumption`  
  Load '24_LVBus220722_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220775_consumption`  
  Load '24_LVBus220775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221247_consumption`  
  Load '24_LVBus221247_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220714_consumption`  
  Load '24_LVBus220714_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220755_consumption`  
  Load '24_LVBus220755_consumption' has phase imbalance of 257.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221179_consumption`  
  Load '24_LVBus221179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220839_consumption`  
  Load '24_LVBus220839_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220719_consumption`  
  Load '24_LVBus220719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221288_consumption`  
  Load '24_LVBus221288_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221050_consumption`  
  Load '24_LVBus221050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221174_consumption`  
  Load '24_LVBus221174_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220777_consumption`  
  Load '24_LVBus220777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221005_consumption`  
  Load '24_LVBus221005_consumption' has phase imbalance of 292.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843697_consumption`  
  Load '24_LVBus843697_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220731_consumption`  
  Load '24_LVBus220731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220798_consumption`  
  Load '24_LVBus220798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221293_consumption`  
  Load '24_LVBus221293_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221093_consumption`  
  Load '24_LVBus221093_consumption' has phase imbalance of 118.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220707_consumption`  
  Load '24_LVBus220707_consumption' has phase imbalance of 204.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221257_consumption`  
  Load '24_LVBus221257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221130_consumption`  
  Load '24_LVBus221130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220927_consumption`  
  Load '24_LVBus220927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220974_consumption`  
  Load '24_LVBus220974_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221046_consumption`  
  Load '24_LVBus221046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220819_consumption`  
  Load '24_LVBus220819_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861567_consumption`  
  Load '24_LVBus861567_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221237_consumption`  
  Load '24_LVBus221237_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221036_consumption`  
  Load '24_LVBus221036_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220773_consumption`  
  Load '24_LVBus220773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221136_consumption`  
  Load '24_LVBus221136_consumption' has phase imbalance of 120.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220837_consumption`  
  Load '24_LVBus220837_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus855540_consumption`  
  Load '24_LVBus855540_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221096_consumption`  
  Load '24_LVBus221096_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220869_consumption`  
  Load '24_LVBus220869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus221251_consumption`  
  Load '24_LVBus221251_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220752_consumption`  
  Load '24_LVBus220752_consumption' has phase imbalance of 243.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220708_consumption`  
  Load '24_LVBus220708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus220783_consumption`  
  Load '24_LVBus220783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1026 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '24_V.AVR' (MV, 11.78 kV) has an electrical reach of 21.6 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus221237' (LV, 0.24 kV) has an electrical reach of 24.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus221253' (LV, 0.24 kV) has an electrical reach of 15.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus221216' (LV, 0.24 kV) has an electrical reach of 21.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus220954' (LV, 0.24 kV) has an electrical reach of 0.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  739 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  259 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 24_LVBus220689_consumption, 24_LVBus220693_consumption, 24_LVBus220694_consumption, 24_LVBus220696_consumption, 24_LVBus220697_consumption, 24_LVBus220700_consumption, 24_LVBus220701_consumption, 24_LVBus220704_consumption, 24_LVBus220705_consumption, 24_LVBus220707_consumption, 24_LVBus220708_consumption, 24_LVBus220709_consumption, 24_LVBus220710_consumption, 24_LVBus220712_consumption, 24_LVBus220714_consumption, 24_LVBus220715_consumption, 24_LVBus220716_consumption, 24_LVBus220717_consumption, 24_LVBus220719_consumption, 24_LVBus220722_consumption, 24_LVBus220724_consumption, 24_LVBus220725_consumption, 24_LVBus220727_consumption, 24_LVBus220728_consumption, 24_LVBus220731_consumption, 24_LVBus220744_consumption, 24_LVBus220748_consumption, 24_LVBus220751_consumption, 24_LVBus220752_consumption, 24_LVBus220753_consumption, 24_LVBus220756_consumption, 24_LVBus220757_consumption, 24_LVBus220758_consumption, 24_LVBus220759_consumption, 24_LVBus220762_consumption, 24_LVBus220763_consumption, 24_LVBus220766_consumption, 24_LVBus220770_consumption, 24_LVBus220773_consumption, 24_LVBus220775_consumption, 24_LVBus220776_consumption, 24_LVBus220777_consumption, 24_LVBus220783_consumption, 24_LVBus220789_consumption, 24_LVBus220792_consumption, 24_LVBus220794_consumption, 24_LVBus220795_consumption, 24_LVBus220796_consumption, 24_LVBus220797_consumption, 24_LVBus220798_consumption, 24_LVBus220799_consumption, 24_LVBus220800_consumption, 24_LVBus220803_consumption, 24_LVBus220806_consumption, 24_LVBus220807_consumption, 24_LVBus220811_consumption, 24_LVBus220813_consumption, 24_LVBus220818_consumption, 24_LVBus220819_consumption, 24_LVBus220827_consumption, 24_LVBus220828_consumption, 24_LVBus220830_consumption, 24_LVBus220832_consumption, 24_LVBus220833_consumption, 24_LVBus220835_consumption, 24_LVBus220836_consumption, 24_LVBus220838_consumption, 24_LVBus220839_consumption, 24_LVBus220855_consumption, 24_LVBus220856_consumption, 24_LVBus220857_consumption, 24_LVBus220864_consumption, 24_LVBus220868_consumption, 24_LVBus220869_consumption, 24_LVBus220872_consumption, 24_LVBus220881_consumption, 24_LVBus220886_consumption, 24_LVBus220888_consumption, 24_LVBus220890_consumption, 24_LVBus220891_consumption, 24_LVBus220894_consumption, 24_LVBus220896_consumption, 24_LVBus220899_consumption, 24_LVBus220903_consumption, 24_LVBus220904_consumption, 24_LVBus220905_consumption, 24_LVBus220906_consumption, 24_LVBus220907_consumption, 24_LVBus220911_consumption, 24_LVBus220913_consumption, 24_LVBus220915_consumption, 24_LVBus220916_consumption, 24_LVBus220924_consumption, 24_LVBus220927_consumption, 24_LVBus220938_consumption, 24_LVBus220942_consumption, 24_LVBus220958_consumption, 24_LVBus220959_consumption, 24_LVBus220966_consumption, 24_LVBus220967_consumption, 24_LVBus220970_consumption, 24_LVBus220973_consumption, 24_LVBus220977_consumption, 24_LVBus220982_consumption, 24_LVBus220983_consumption, 24_LVBus220985_consumption, 24_LVBus220988_consumption, 24_LVBus220989_consumption, 24_LVBus220990_consumption, 24_LVBus220992_consumption, 24_LVBus220994_consumption, 24_LVBus220995_consumption, 24_LVBus220997_consumption, 24_LVBus220998_consumption, 24_LVBus221000_consumption, 24_LVBus221005_consumption, 24_LVBus221006_consumption, 24_LVBus221010_consumption, 24_LVBus221011_consumption, 24_LVBus221014_consumption, 24_LVBus221016_consumption, 24_LVBus221017_consumption, 24_LVBus221020_consumption, 24_LVBus221021_consumption, 24_LVBus221022_consumption, 24_LVBus221025_consumption, 24_LVBus221029_consumption, 24_LVBus221030_consumption, 24_LVBus221033_consumption, 24_LVBus221034_consumption, 24_LVBus221036_consumption, 24_LVBus221039_consumption, 24_LVBus221046_consumption, 24_LVBus221048_consumption, 24_LVBus221049_consumption, 24_LVBus221050_consumption, 24_LVBus221052_consumption, 24_LVBus221056_consumption, 24_LVBus221059_consumption, 24_LVBus221062_consumption, 24_LVBus221064_consumption, 24_LVBus221066_consumption, 24_LVBus221070_consumption, 24_LVBus221071_consumption, 24_LVBus221072_consumption, 24_LVBus221076_consumption, 24_LVBus221077_consumption, 24_LVBus221078_consumption, 24_LVBus221079_consumption, 24_LVBus221080_consumption, 24_LVBus221082_consumption, 24_LVBus221083_consumption, 24_LVBus221085_consumption, 24_LVBus221092_consumption, 24_LVBus221094_consumption, 24_LVBus221096_consumption, 24_LVBus221097_consumption, 24_LVBus221106_consumption, 24_LVBus221107_consumption, 24_LVBus221108_consumption, 24_LVBus221111_consumption, 24_LVBus221114_consumption, 24_LVBus221117_consumption, 24_LVBus221118_consumption, 24_LVBus221126_consumption, 24_LVBus221129_consumption, 24_LVBus221130_consumption, 24_LVBus221133_consumption, 24_LVBus221134_consumption, 24_LVBus221138_consumption, 24_LVBus221140_consumption, 24_LVBus221144_consumption, 24_LVBus221147_consumption, 24_LVBus221148_consumption, 24_LVBus221149_consumption, 24_LVBus221150_consumption, 24_LVBus221153_consumption, 24_LVBus221154_consumption, 24_LVBus221155_consumption, 24_LVBus221158_consumption, 24_LVBus221159_consumption, 24_LVBus221162_consumption, 24_LVBus221163_consumption, 24_LVBus221164_consumption, 24_LVBus221165_consumption, 24_LVBus221169_consumption, 24_LVBus221170_consumption, 24_LVBus221172_consumption, 24_LVBus221173_consumption, 24_LVBus221174_consumption, 24_LVBus221175_consumption, 24_LVBus221177_consumption, 24_LVBus221179_consumption, 24_LVBus221182_consumption, 24_LVBus221183_consumption, 24_LVBus221184_consumption, 24_LVBus221186_consumption, 24_LVBus221187_consumption, 24_LVBus221188_consumption, 24_LVBus221193_consumption, 24_LVBus221194_consumption, 24_LVBus221195_consumption, 24_LVBus221200_consumption, 24_LVBus221203_consumption, 24_LVBus221204_consumption, 24_LVBus221213_consumption, 24_LVBus221216_consumption, 24_LVBus221217_consumption, 24_LVBus221219_consumption, 24_LVBus221221_consumption, 24_LVBus221223_consumption, 24_LVBus221228_consumption, 24_LVBus221229_consumption, 24_LVBus221230_consumption, 24_LVBus221233_consumption, 24_LVBus221234_consumption, 24_LVBus221235_consumption, 24_LVBus221237_consumption, 24_LVBus221239_consumption, 24_LVBus221240_consumption, 24_LVBus221243_consumption, 24_LVBus221247_consumption, 24_LVBus221248_consumption, 24_LVBus221255_consumption, 24_LVBus221256_consumption, 24_LVBus221257_consumption, 24_LVBus221263_consumption, 24_LVBus221264_consumption, 24_LVBus221275_consumption, 24_LVBus221276_consumption, 24_LVBus221277_consumption, 24_LVBus221285_consumption, 24_LVBus221286_consumption, 24_LVBus221287_consumption, 24_LVBus221289_consumption, 24_LVBus221292_consumption, 24_LVBus221293_consumption, 24_LVBus833824_consumption, 24_LVBus835929_consumption, 24_LVBus835930_consumption, 24_LVBus843697_consumption, 24_LVBus843812_consumption, 24_LVBus843813_consumption, 24_LVBus843814_consumption, 24_LVBus855540_consumption, 24_LVBus856086_consumption, 24_LVBus856544_consumption, 24_LVBus857044_consumption, 24_LVBus857045_consumption, 24_LVBus857046_consumption, 24_LVBus857470_consumption, 24_LVBus858993_consumption, 24_LVBus859815_consumption, 24_LVBus860111_consumption, 24_LVBus860438_consumption, 24_LVBus860532_consumption, 24_LVBus860533_consumption, 24_LVBus861564_consumption, 24_LVBus861567_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  513 group(s) of loads (1026 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  15 group(s) of series lines (30 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  623 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus220689_production, 24_LVBus220693_production, 24_LVBus220694_production, 24_LVBus220696_production, 24_LVBus220697_production, 24_LVBus220699_production, 24_LVBus220700_production, 24_LVBus220701_production, 24_LVBus220702_production, 24_LVBus220703_production, 24_LVBus220704_production, 24_LVBus220705_production, 24_LVBus220706_production, 24_LVBus220707_production, 24_LVBus220708_production, 24_LVBus220709_production, 24_LVBus220710_production, 24_LVBus220711_production, 24_LVBus220712_production, 24_LVBus220713_consumption, 24_LVBus220713_production, 24_LVBus220714_production, 24_LVBus220715_production, 24_LVBus220716_production, 24_LVBus220717_production, 24_LVBus220718_consumption, 24_LVBus220718_production, 24_LVBus220719_production, 24_LVBus220721_consumption, 24_LVBus220721_production, 24_LVBus220722_production, 24_LVBus220724_production, 24_LVBus220725_production, 24_LVBus220727_production, 24_LVBus220728_production, 24_LVBus220729_production, 24_LVBus220731_production, 24_LVBus220732_production, 24_LVBus220733_production, 24_LVBus220734_consumption, 24_LVBus220734_production, 24_LVBus220735_consumption, 24_LVBus220735_production, 24_LVBus220736_production, 24_LVBus220740_consumption, 24_LVBus220740_production, 24_LVBus220741_consumption, 24_LVBus220741_production, 24_LVBus220744_production, 24_LVBus220745_production, 24_LVBus220748_production, 24_LVBus220749_consumption, 24_LVBus220749_production, 24_LVBus220750_production, 24_LVBus220751_production, 24_LVBus220752_production, 24_LVBus220753_production, 24_LVBus220755_production, 24_LVBus220756_production, 24_LVBus220757_production, 24_LVBus220758_production, 24_LVBus220759_production, 24_LVBus220761_production, 24_LVBus220762_production, 24_LVBus220763_production, 24_LVBus220765_production, 24_LVBus220766_production, 24_LVBus220767_consumption, 24_LVBus220767_production, 24_LVBus220769_production, 24_LVBus220770_production, 24_LVBus220771_consumption, 24_LVBus220771_production, 24_LVBus220773_production, 24_LVBus220775_production, 24_LVBus220776_production, 24_LVBus220777_production, 24_LVBus220779_production, 24_LVBus220781_consumption, 24_LVBus220781_production, 24_LVBus220782_production, 24_LVBus220783_production, 24_LVBus220785_production, 24_LVBus220787_consumption, 24_LVBus220787_production, 24_LVBus220788_production, 24_LVBus220789_production, 24_LVBus220790_production, 24_LVBus220792_production, 24_LVBus220794_production, 24_LVBus220795_production, 24_LVBus220796_production, 24_LVBus220797_production, 24_LVBus220798_production, 24_LVBus220799_production, 24_LVBus220800_production, 24_LVBus220802_production, 24_LVBus220803_production, 24_LVBus220805_consumption, 24_LVBus220805_production, 24_LVBus220806_production, 24_LVBus220807_production, 24_LVBus220809_production, 24_LVBus220810_production, 24_LVBus220811_production, 24_LVBus220812_production, 24_LVBus220813_production, 24_LVBus220815_consumption, 24_LVBus220815_production, 24_LVBus220817_consumption, 24_LVBus220817_production, 24_LVBus220818_production, 24_LVBus220819_production, 24_LVBus220820_production, 24_LVBus220822_consumption, 24_LVBus220822_production, 24_LVBus220823_production, 24_LVBus220825_consumption, 24_LVBus220825_production, 24_LVBus220827_production, 24_LVBus220828_production, 24_LVBus220829_consumption, 24_LVBus220829_production, 24_LVBus220830_production, 24_LVBus220831_production, 24_LVBus220832_production, 24_LVBus220833_production, 24_LVBus220835_production, 24_LVBus220836_production, 24_LVBus220837_production, 24_LVBus220838_production, 24_LVBus220839_production, 24_LVBus220841_consumption, 24_LVBus220841_production, 24_LVBus220842_consumption, 24_LVBus220842_production, 24_LVBus220843_consumption, 24_LVBus220843_production, 24_LVBus220844_production, 24_LVBus220845_consumption, 24_LVBus220845_production, 24_LVBus220848_production, 24_LVBus220849_production, 24_LVBus220850_production, 24_LVBus220851_production, 24_LVBus220852_production, 24_LVBus220853_production, 24_LVBus220855_production, 24_LVBus220856_production, 24_LVBus220857_production, 24_LVBus220858_production, 24_LVBus220859_production, 24_LVBus220861_consumption, 24_LVBus220861_production, 24_LVBus220862_production, 24_LVBus220863_consumption, 24_LVBus220863_production, 24_LVBus220864_production, 24_LVBus220867_production, 24_LVBus220868_production, 24_LVBus220869_production, 24_LVBus220870_production, 24_LVBus220872_production, 24_LVBus220876_consumption, 24_LVBus220876_production, 24_LVBus220877_production, 24_LVBus220878_production, 24_LVBus220879_production, 24_LVBus220880_production, 24_LVBus220881_production, 24_LVBus220883_production, 24_LVBus220884_production, 24_LVBus220886_production, 24_LVBus220888_production, 24_LVBus220889_consumption, 24_LVBus220889_production, 24_LVBus220890_production, 24_LVBus220891_production, 24_LVBus220892_consumption, 24_LVBus220892_production, 24_LVBus220894_production, 24_LVBus220896_production, 24_LVBus220897_production, 24_LVBus220898_production, 24_LVBus220899_production, 24_LVBus220901_production, 24_LVBus220903_production, 24_LVBus220904_production, 24_LVBus220905_production, 24_LVBus220906_production, 24_LVBus220907_production, 24_LVBus220911_production, 24_LVBus220913_production, 24_LVBus220914_consumption, 24_LVBus220914_production, 24_LVBus220915_production, 24_LVBus220916_production, 24_LVBus220917_production, 24_LVBus220918_production, 24_LVBus220919_production, 24_LVBus220923_consumption, 24_LVBus220923_production, 24_LVBus220924_production, 24_LVBus220925_production, 24_LVBus220926_consumption, 24_LVBus220926_production, 24_LVBus220927_production, 24_LVBus220931_consumption, 24_LVBus220931_production, 24_LVBus220932_consumption, 24_LVBus220932_production, 24_LVBus220933_production, 24_LVBus220934_consumption, 24_LVBus220934_production, 24_LVBus220935_consumption, 24_LVBus220935_production, 24_LVBus220936_consumption, 24_LVBus220936_production, 24_LVBus220937_consumption, 24_LVBus220937_production, 24_LVBus220938_production, 24_LVBus220942_production, 24_LVBus220944_consumption, 24_LVBus220944_production, 24_LVBus220946_consumption, 24_LVBus220946_production, 24_LVBus220948_consumption, 24_LVBus220948_production, 24_LVBus220950_consumption, 24_LVBus220950_production, 24_LVBus220952_consumption, 24_LVBus220952_production, 24_LVBus220954_consumption, 24_LVBus220954_production, 24_LVBus220956_consumption, 24_LVBus220956_production, 24_LVBus220957_consumption, 24_LVBus220957_production, 24_LVBus220958_production, 24_LVBus220959_production, 24_LVBus220963_production, 24_LVBus220964_production, 24_LVBus220966_production, 24_LVBus220967_production, 24_LVBus220968_production, 24_LVBus220969_production, 24_LVBus220970_production, 24_LVBus220971_production, 24_LVBus220973_production, 24_LVBus220974_production, 24_LVBus220976_consumption, 24_LVBus220976_production, 24_LVBus220977_production, 24_LVBus220978_production, 24_LVBus220979_production, 24_LVBus220982_production, 24_LVBus220983_production, 24_LVBus220984_production, 24_LVBus220985_production, 24_LVBus220987_consumption, 24_LVBus220987_production, 24_LVBus220988_production, 24_LVBus220989_production, 24_LVBus220990_production, 24_LVBus220991_production, 24_LVBus220992_production, 24_LVBus220994_production, 24_LVBus220995_production, 24_LVBus220996_production, 24_LVBus220997_production, 24_LVBus220998_production, 24_LVBus220999_consumption, 24_LVBus220999_production, 24_LVBus221000_production, 24_LVBus221002_production, 24_LVBus221004_consumption, 24_LVBus221004_production, 24_LVBus221005_production, 24_LVBus221006_production, 24_LVBus221007_production, 24_LVBus221009_consumption, 24_LVBus221009_production, 24_LVBus221010_production, 24_LVBus221011_production, 24_LVBus221012_production, 24_LVBus221014_production, 24_LVBus221015_consumption, 24_LVBus221015_production, 24_LVBus221016_production, 24_LVBus221017_production, 24_LVBus221019_consumption, 24_LVBus221019_production, 24_LVBus221020_production, 24_LVBus221021_production, 24_LVBus221022_production, 24_LVBus221024_consumption, 24_LVBus221024_production, 24_LVBus221025_production, 24_LVBus221026_consumption, 24_LVBus221026_production, 24_LVBus221029_production, 24_LVBus221030_production, 24_LVBus221031_production, 24_LVBus221033_production, 24_LVBus221034_production, 24_LVBus221035_consumption, 24_LVBus221035_production, 24_LVBus221036_production, 24_LVBus221037_production, 24_LVBus221038_consumption, 24_LVBus221038_production, 24_LVBus221039_production, 24_LVBus221040_consumption, 24_LVBus221040_production, 24_LVBus221043_production, 24_LVBus221044_production, 24_LVBus221045_production, 24_LVBus221046_production, 24_LVBus221047_production, 24_LVBus221048_production, 24_LVBus221049_production, 24_LVBus221050_production, 24_LVBus221052_production, 24_LVBus221054_production, 24_LVBus221055_production, 24_LVBus221056_production, 24_LVBus221058_consumption, 24_LVBus221058_production, 24_LVBus221059_production, 24_LVBus221060_production, 24_LVBus221062_production, 24_LVBus221063_consumption, 24_LVBus221063_production, 24_LVBus221064_production, 24_LVBus221065_production, 24_LVBus221066_production, 24_LVBus221067_consumption, 24_LVBus221067_production, 24_LVBus221068_production, 24_LVBus221070_production, 24_LVBus221071_production, 24_LVBus221072_production, 24_LVBus221074_production, 24_LVBus221075_consumption, 24_LVBus221075_production, 24_LVBus221076_production, 24_LVBus221077_production, 24_LVBus221078_production, 24_LVBus221079_production, 24_LVBus221080_production, 24_LVBus221081_production, 24_LVBus221082_production, 24_LVBus221083_production, 24_LVBus221084_production, 24_LVBus221085_production, 24_LVBus221087_consumption, 24_LVBus221087_production, 24_LVBus221088_production, 24_LVBus221090_consumption, 24_LVBus221090_production, 24_LVBus221091_production, 24_LVBus221092_production, 24_LVBus221093_production, 24_LVBus221094_production, 24_LVBus221095_production, 24_LVBus221096_production, 24_LVBus221097_production, 24_LVBus221098_consumption, 24_LVBus221098_production, 24_LVBus221100_production, 24_LVBus221101_production, 24_LVBus221102_production, 24_LVBus221103_production, 24_LVBus221104_production, 24_LVBus221106_production, 24_LVBus221107_production, 24_LVBus221108_production, 24_LVBus221109_consumption, 24_LVBus221109_production, 24_LVBus221110_production, 24_LVBus221111_production, 24_LVBus221113_production, 24_LVBus221114_production, 24_LVBus221115_production, 24_LVBus221116_production, 24_LVBus221117_production, 24_LVBus221118_production, 24_LVBus221122_production, 24_LVBus221123_consumption, 24_LVBus221123_production, 24_LVBus221124_production, 24_LVBus221126_production, 24_LVBus221127_production, 24_LVBus221128_production, 24_LVBus221129_production, 24_LVBus221130_production, 24_LVBus221132_production, 24_LVBus221133_production, 24_LVBus221134_production, 24_LVBus221136_production, 24_LVBus221138_production, 24_LVBus221140_production, 24_LVBus221141_production, 24_LVBus221142_production, 24_LVBus221143_consumption, 24_LVBus221143_production, 24_LVBus221144_production, 24_LVBus221146_consumption, 24_LVBus221146_production, 24_LVBus221147_production, 24_LVBus221148_production, 24_LVBus221149_production, 24_LVBus221150_production, 24_LVBus221151_production, 24_LVBus221152_production, 24_LVBus221153_production, 24_LVBus221154_production, 24_LVBus221155_production, 24_LVBus221156_consumption, 24_LVBus221156_production, 24_LVBus221157_production, 24_LVBus221158_production, 24_LVBus221159_production, 24_LVBus221161_production, 24_LVBus221162_production, 24_LVBus221163_production, 24_LVBus221164_production, 24_LVBus221165_production, 24_LVBus221166_production, 24_LVBus221167_production, 24_LVBus221169_production, 24_LVBus221170_production, 24_LVBus221172_production, 24_LVBus221173_production, 24_LVBus221174_production, 24_LVBus221175_production, 24_LVBus221177_production, 24_LVBus221178_production, 24_LVBus221179_production, 24_LVBus221180_production, 24_LVBus221182_production, 24_LVBus221183_production, 24_LVBus221184_production, 24_LVBus221185_production, 24_LVBus221186_production, 24_LVBus221187_production, 24_LVBus221188_production, 24_LVBus221192_consumption, 24_LVBus221192_production, 24_LVBus221193_production, 24_LVBus221194_production, 24_LVBus221195_production, 24_LVBus221197_consumption, 24_LVBus221197_production, 24_LVBus221198_consumption, 24_LVBus221198_production, 24_LVBus221199_consumption, 24_LVBus221199_production, 24_LVBus221200_production, 24_LVBus221201_production, 24_LVBus221203_production, 24_LVBus221204_production, 24_LVBus221205_production, 24_LVBus221206_production, 24_LVBus221207_consumption, 24_LVBus221207_production, 24_LVBus221208_production, 24_LVBus221210_production, 24_LVBus221212_production, 24_LVBus221213_production, 24_LVBus221214_production, 24_LVBus221216_production, 24_LVBus221217_production, 24_LVBus221219_production, 24_LVBus221220_consumption, 24_LVBus221220_production, 24_LVBus221221_production, 24_LVBus221222_consumption, 24_LVBus221222_production, 24_LVBus221223_production, 24_LVBus221227_consumption, 24_LVBus221227_production, 24_LVBus221228_production, 24_LVBus221229_production, 24_LVBus221230_production, 24_LVBus221233_production, 24_LVBus221234_production, 24_LVBus221235_production, 24_LVBus221237_production, 24_LVBus221239_production, 24_LVBus221240_production, 24_LVBus221241_consumption, 24_LVBus221241_production, 24_LVBus221242_production, 24_LVBus221243_production, 24_LVBus221244_consumption, 24_LVBus221244_production, 24_LVBus221245_consumption, 24_LVBus221245_production, 24_LVBus221247_production, 24_LVBus221248_production, 24_LVBus221249_consumption, 24_LVBus221249_production, 24_LVBus221250_consumption, 24_LVBus221250_production, 24_LVBus221251_production, 24_LVBus221253_consumption, 24_LVBus221253_production, 24_LVBus221255_production, 24_LVBus221256_production, 24_LVBus221257_production, 24_LVBus221258_consumption, 24_LVBus221258_production, 24_LVBus221259_consumption, 24_LVBus221259_production, 24_LVBus221260_production, 24_LVBus221261_production, 24_LVBus221262_production, 24_LVBus221263_production, 24_LVBus221264_production, 24_LVBus221265_consumption, 24_LVBus221265_production, 24_LVBus221267_production, 24_LVBus221268_production, 24_LVBus221269_production, 24_LVBus221270_consumption, 24_LVBus221270_production, 24_LVBus221271_consumption, 24_LVBus221271_production, 24_LVBus221272_production, 24_LVBus221273_production, 24_LVBus221275_production, 24_LVBus221276_production, 24_LVBus221277_production, 24_LVBus221278_production, 24_LVBus221279_production, 24_LVBus221280_production, 24_LVBus221281_consumption, 24_LVBus221281_production, 24_LVBus221283_production, 24_LVBus221285_production, 24_LVBus221286_production, 24_LVBus221287_production, 24_LVBus221288_production, 24_LVBus221289_production, 24_LVBus221291_production, 24_LVBus221292_production, 24_LVBus221293_production, 24_LVBus832407_consumption, 24_LVBus832407_production, 24_LVBus832408_consumption, 24_LVBus832408_production, 24_LVBus832787_consumption, 24_LVBus832787_production, 24_LVBus833311_production, 24_LVBus833824_production, 24_LVBus835929_production, 24_LVBus835930_production, 24_LVBus838927_production, 24_LVBus842201_production, 24_LVBus843697_production, 24_LVBus843699_consumption, 24_LVBus843699_production, 24_LVBus843812_production, 24_LVBus843813_production, 24_LVBus843814_production, 24_LVBus844278_consumption, 24_LVBus844278_production, 24_LVBus852187_production, 24_LVBus855540_production, 24_LVBus856086_production, 24_LVBus856544_production, 24_LVBus857041_consumption, 24_LVBus857041_production, 24_LVBus857042_consumption, 24_LVBus857042_production, 24_LVBus857043_consumption, 24_LVBus857043_production, 24_LVBus857044_production, 24_LVBus857045_production, 24_LVBus857046_production, 24_LVBus857047_production, 24_LVBus857469_production, 24_LVBus857470_production, 24_LVBus858484_production, 24_LVBus858485_production, 24_LVBus858993_production, 24_LVBus859815_production, 24_LVBus860074_consumption, 24_LVBus860074_production, 24_LVBus860075_consumption, 24_LVBus860075_production, 24_LVBus860111_production, 24_LVBus860438_production, 24_LVBus860439_consumption, 24_LVBus860439_production, 24_LVBus860440_consumption, 24_LVBus860440_production, 24_LVBus860532_production, 24_LVBus860533_production, 24_LVBus861561_consumption, 24_LVBus861561_production, 24_LVBus861562_consumption, 24_LVBus861562_production, 24_LVBus861563_consumption, 24_LVBus861563_production, 24_LVBus861564_production, 24_LVBus861565_consumption, 24_LVBus861565_production, 24_LVBus861566_production, 24_LVBus861567_production, 24_MVLV24494_consumption, 24_MVLV24494_production, 24_MVLV29603_consumption, 24_MVLV29603_production, 24_MVLV55274_consumption, 24_MVLV55274_production, 24_MVLV69124_consumption, 24_MVLV69124_production, 24_MVLV71043_consumption, 24_MVLV71043_production, 24_MVLV74478_consumption, 24_MVLV74478_production.

