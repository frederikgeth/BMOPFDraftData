# BMOPF Network Summary: 53_MVFeeder0883

**Generated:** 2026-10-01 23:34:19  
**Findings:** 0 errors · 5 warnings · 372 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 59 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 682 |  |
| line | 622 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 998 | 2.391 MW, 717.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 59 |  |
| switch | 0 |  |
| transformer | 59 | Dyn11×59 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 130 | 129 | 12 | 0 |
| LV_236V | 236.0 V | 552 | 493 | 986 | 0 |

**Transformer transitions:**

- `53_MVLV16382_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV56372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV49163_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV18834_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV55966_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV36795_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV77015_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV21814_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV13417_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV16968_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV35109_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV20080_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV80271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV81768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV56055_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV80503_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV80732_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV53649_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV19688_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV56735_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV13416_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV30436_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV39046_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV62452_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV05678_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV48764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV78138_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV12659_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV67502_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV30451_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV71821_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV14678_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV25334_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV71995_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV63102_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV35271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV71523_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV68628_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV40129_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV24492_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV42883_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV39696_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV00689_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV30406_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV09496_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV59932_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV70144_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV40128_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV50264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV81007_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV61963_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV82673_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV71822_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV80291_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV80510_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV74941_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV28653_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV33126_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV83987_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 254 |
| Tree depth (max hops) | 32 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 682 | 1 | 681 | 0 | 0 | 0 |
| Tier LV_236V | 552 | 59 | 493 | 0 | 0 | 0 |
| Tier MV_11.8kV | 130 | 1 | 129 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 59; skipped invalid branches: 0.

Galvanic zones: 60; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 53_LANNI | MV_11.8kV | 130 | 0 | 0 | 59 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2598 declared bus terminals; 2359 mapped line/closed-switch conductor edges; 239 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 17400.0 | 2.507 | 2994 |
| q_nom | 0.0 | 5210.0 | 2.507 | 2994 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.982 | 1860.0 | 1.156 | 622 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.536 | 59 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 604 of 998 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637090_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637393_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637163_consumption' has phase imbalance of 49.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637402_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637207_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1008586_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637420_consumption' has phase imbalance of 207.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637211_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637381_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637272_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637255_consumption' has phase imbalance of 235.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637167_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637141_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637376_consumption' has phase imbalance of 21.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637078_consumption' has phase imbalance of 288.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637395_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637102_consumption' has phase imbalance of 89.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637481_consumption' has phase imbalance of 79.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637552_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1018088_consumption' has phase imbalance of 77.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637540_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637205_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637242_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637175_consumption' has phase imbalance of 145.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637281_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637504_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637077_consumption' has phase imbalance of 262.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637305_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637215_consumption' has phase imbalance of 272.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637626_consumption' has phase imbalance of 164.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637306_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637493_consumption' has phase imbalance of 63.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1012181_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637614_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637194_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637392_consumption' has phase imbalance of 117.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637366_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637461_consumption' has phase imbalance of 136.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637189_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637368_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637275_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637439_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637054_consumption' has phase imbalance of 163.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637361_consumption' has phase imbalance of 223.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1023082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637139_consumption' has phase imbalance of 255.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637075_consumption' has phase imbalance of 245.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637098_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637350_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637309_consumption' has phase imbalance of 197.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637240_consumption' has phase imbalance of 267.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637103_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637354_consumption' has phase imbalance of 239.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637405_consumption' has phase imbalance of 114.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637083_consumption' has phase imbalance of 126.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637343_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637184_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637190_consumption' has phase imbalance of 289.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637375_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637076_consumption' has phase imbalance of 247.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637477_consumption' has phase imbalance of 234.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637455_consumption' has phase imbalance of 250.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637406_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637342_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1008584_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637260_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637612_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637225_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1013050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637616_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637320_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637507_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637452_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637465_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637599_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637362_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637171_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus995391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637085_consumption' has phase imbalance of 266.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637491_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637314_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637357_consumption' has phase imbalance of 268.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637230_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637170_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1008583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637089_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637554_consumption' has phase imbalance of 228.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637094_consumption' has phase imbalance of 76.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637253_consumption' has phase imbalance of 51.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637425_consumption' has phase imbalance of 291.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637349_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637384_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637382_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1012182_consumption' has phase imbalance of 238.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637227_consumption' has phase imbalance of 183.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637237_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637443_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637235_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637567_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637396_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1013049_consumption' has phase imbalance of 140.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637534_consumption' has phase imbalance of 287.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637399_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637515_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637360_consumption' has phase imbalance of 121.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637440_consumption' has phase imbalance of 266.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637134_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637487_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637625_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637485_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus979202_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1028248_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637377_consumption' has phase imbalance of 80.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1030632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637093_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637288_consumption' has phase imbalance of 89.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637564_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637490_consumption' has phase imbalance of 143.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637299_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637251_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637510_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637494_consumption' has phase imbalance of 70.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637365_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637442_consumption' has phase imbalance of 240.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637374_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637598_consumption' has phase imbalance of 185.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637517_consumption' has phase imbalance of 175.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637137_consumption' has phase imbalance of 243.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637297_consumption' has phase imbalance of 93.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637224_consumption' has phase imbalance of 119.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637099_consumption' has phase imbalance of 132.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637351_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637264_consumption' has phase imbalance of 284.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637232_consumption' has phase imbalance of 126.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637404_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637380_consumption' has phase imbalance of 129.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637223_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637603_consumption' has phase imbalance of 30.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637527_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637615_consumption' has phase imbalance of 184.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637623_consumption' has phase imbalance of 250.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637576_consumption' has phase imbalance of 221.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637276_consumption' has phase imbalance of 110.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637483_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637217_consumption' has phase imbalance of 222.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637169_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637325_consumption' has phase imbalance of 44.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637087_consumption' has phase imbalance of 266.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637408_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637203_consumption' has phase imbalance of 186.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637470_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637323_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637132_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637209_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637135_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637403_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637160_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637421_consumption' has phase imbalance of 58.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1012180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637319_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637100_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637186_consumption' has phase imbalance of 241.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637095_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637378_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637422_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637301_consumption' has phase imbalance of 47.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637488_consumption' has phase imbalance of 223.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637055_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637411_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637273_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus995390_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637398_consumption' has phase imbalance of 216.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637097_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637270_consumption' has phase imbalance of 133.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637606_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637117_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637563_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637544_consumption' has phase imbalance of 202.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637316_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637369_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637133_consumption' has phase imbalance of 136.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637573_consumption' has phase imbalance of 76.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637070_consumption' has phase imbalance of 274.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1008585_consumption' has phase imbalance of 72.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637427_consumption' has phase imbalance of 129.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637389_consumption' has phase imbalance of 126.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637271_consumption' has phase imbalance of 98.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637415_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637197_consumption' has phase imbalance of 51.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637379_consumption' has phase imbalance of 243.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637519_consumption' has phase imbalance of 239.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637159_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637468_consumption' has phase imbalance of 84.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637151_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637601_consumption' has phase imbalance of 224.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637347_consumption' has phase imbalance of 276.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637236_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637082_consumption' has phase imbalance of 254.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637418_consumption' has phase imbalance of 237.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637492_consumption' has phase imbalance of 286.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637071_consumption' has phase imbalance of 257.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637105_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637401_consumption' has phase imbalance of 225.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637165_consumption' has phase imbalance of 87.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637611_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637143_consumption' has phase imbalance of 141.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637317_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637198_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637542_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637155_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637568_consumption' has phase imbalance of 182.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1012184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637498_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637177_consumption' has phase imbalance of 259.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637409_consumption' has phase imbalance of 73.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637450_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637597_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637345_consumption' has phase imbalance of 249.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637522_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637283_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637216_consumption' has phase imbalance of 97.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637578_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus637268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 998 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus637429' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus637581' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus637595' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus637153' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.391 MW |
| Total load Q | 717.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 53_MVLV16382_Transformer | 275.0 kVA | 37.2% |
| 53_MVLV56372_Transformer | 110.0 kVA | 4.9% |
| 53_MVLV49163_Transformer | 176.0 kVA | 9.5% |
| 53_MVLV18834_Transformer | 275.0 kVA | 19.8% |
| 53_MVLV55966_Transformer | 176.0 kVA | 13.0% |
| 53_MVLV36795_Transformer | 275.0 kVA | 9.0% |
| 53_MVLV77015_Transformer | 176.0 kVA | 13.5% |
| 53_MVLV21814_Transformer | 110.0 kVA | 11.1% |
| 53_MVLV13417_Transformer | 110.0 kVA | 14.0% |
| 53_MVLV16968_Transformer | 110.0 kVA | 12.5% |
| 53_MVLV35109_Transformer | 176.0 kVA | 28.5% |
| 53_MVLV20080_Transformer | 110.0 kVA | 22.1% |
| 53_MVLV80271_Transformer | 176.0 kVA | 23.0% |
| 53_MVLV81768_Transformer | 110.0 kVA | 0.9% |
| 53_MVLV56055_Transformer | 275.0 kVA | 37.6% |
| 53_MVLV80503_Transformer | 110.0 kVA | 1.1% |
| 53_MVLV80732_Transformer | 110.0 kVA | 16.4% |
| 53_MVLV53649_Transformer | 440.0 kVA | 44.2% |
| 53_MVLV19688_Transformer | 440.0 kVA | 35.0% |
| 53_MVLV56735_Transformer | 176.0 kVA | 25.1% |
| 53_MVLV13416_Transformer | 110.0 kVA | 7.8% |
| 53_MVLV30436_Transformer | 440.0 kVA | 30.5% |
| 53_MVLV39046_Transformer | 110.0 kVA | 14.4% |
| 53_MVLV62452_Transformer | 110.0 kVA | 5.8% |
| 53_MVLV05678_Transformer | 110.0 kVA | 21.5% |
| 53_MVLV48764_Transformer | 176.0 kVA | 24.3% |
| 53_MVLV78138_Transformer | 110.0 kVA | 19.4% |
| 53_MVLV12659_Transformer | 440.0 kVA | 33.5% |
| 53_MVLV67502_Transformer | 440.0 kVA | 11.9% |
| 53_MVLV30451_Transformer | 275.0 kVA | 20.5% |
| 53_MVLV71821_Transformer | 176.0 kVA | 10.0% |
| 53_MVLV14678_Transformer | 110.0 kVA | 9.4% |
| 53_MVLV25334_Transformer | 275.0 kVA | 18.2% |
| 53_MVLV71995_Transformer | 110.0 kVA | 13.1% |
| 53_MVLV63102_Transformer | 275.0 kVA | 23.4% |
| 53_MVLV35271_Transformer | 440.0 kVA | 13.1% |
| 53_MVLV71523_Transformer | 176.0 kVA | 20.2% |
| 53_MVLV68628_Transformer | 176.0 kVA | 26.7% |
| 53_MVLV40129_Transformer | 110.0 kVA | 32.5% |
| 53_MVLV24492_Transformer | 176.0 kVA | 10.6% |
| 53_MVLV42883_Transformer | 110.0 kVA | 12.4% |
| 53_MVLV39696_Transformer | 110.0 kVA | 6.0% |
| 53_MVLV00689_Transformer | 110.0 kVA | 4.7% |
| 53_MVLV30406_Transformer | 275.0 kVA | 13.5% |
| 53_MVLV09496_Transformer | 176.0 kVA | 15.2% |
| 53_MVLV59932_Transformer | 275.0 kVA | 10.2% |
| 53_MVLV70144_Transformer | 176.0 kVA | 14.4% |
| 53_MVLV40128_Transformer | 176.0 kVA | 13.5% |
| 53_MVLV50264_Transformer | 110.0 kVA | 28.3% |
| 53_MVLV81007_Transformer | 440.0 kVA | 12.4% |
| 53_MVLV61963_Transformer | 440.0 kVA | 18.4% |
| 53_MVLV82673_Transformer | 275.0 kVA | 29.8% |
| 53_MVLV71822_Transformer | 275.0 kVA | 24.7% |
| 53_MVLV80291_Transformer | 176.0 kVA | 7.6% |
| 53_MVLV80510_Transformer | 275.0 kVA | 18.1% |
| 53_MVLV74941_Transformer | 176.0 kVA | 21.8% |
| 53_MVLV28653_Transformer | 110.0 kVA | 14.4% |
| 53_MVLV33126_Transformer | 176.0 kVA | 5.2% |
| 53_MVLV83987_Transformer | 440.0 kVA | 23.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.39 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '53_LVBus637434' (LV, 0.24 kV) has an electrical reach of 1.1 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '53_LVBus637299' (LV, 0.24 kV) has an electrical reach of 18.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '53_LVBus637153' (LV, 0.24 kV) has an electrical reach of 6.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 682 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 682 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 59 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 130 |
| LV_236V | 4-wire | 552 / 552 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 552 |
| Neutral branches | 493 |
| Grounding points | 59 |
| Neutral sections | 59 |
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
| 11.78 kV | 130 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 60 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2050.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 552 / 130 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 605 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 605 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus1008582_consumption, 53_LVBus1008582_production, 53_LVBus1008583_production, 53_LVBus1008584_production, 53_LVBus1008585_production, 53_LVBus1008586_production, 53_LVBus1012180_production, 53_LVBus1012181_production, 53_LVBus1012182_production, 53_LVBus1012183_consumption, 53_LVBus1012183_production, 53_LVBus1012184_production, 53_LVBus1013048_production, 53_LVBus1013049_production, 53_LVBus1013050_production, 53_LVBus1018088_production, 53_LVBus1023082_production, 53_LVBus1028248_production, 53_LVBus1030629_consumption, 53_LVBus1030629_production, 53_LVBus1030630_consumption, 53_LVBus1030630_production, 53_LVBus1030631_consumption, 53_LVBus1030631_production, 53_LVBus1030632_production, 53_LVBus637054_production, 53_LVBus637055_production, 53_LVBus637057_consumption, 53_LVBus637057_production, 53_LVBus637059_production, 53_LVBus637061_production, 53_LVBus637062_production, 53_LVBus637063_production, 53_LVBus637064_production, 53_LVBus637065_consumption, 53_LVBus637065_production, 53_LVBus637066_consumption, 53_LVBus637066_production, 53_LVBus637067_production, 53_LVBus637068_production, 53_LVBus637070_production, 53_LVBus637071_production, 53_LVBus637072_production, 53_LVBus637073_production, 53_LVBus637074_production, 53_LVBus637075_production, 53_LVBus637076_production, 53_LVBus637077_production, 53_LVBus637078_production, 53_LVBus637079_consumption, 53_LVBus637079_production, 53_LVBus637080_consumption, 53_LVBus637080_production, 53_LVBus637082_production, 53_LVBus637083_production, 53_LVBus637084_consumption, 53_LVBus637084_production, 53_LVBus637085_production, 53_LVBus637086_production, 53_LVBus637087_production, 53_LVBus637088_production, 53_LVBus637089_production, 53_LVBus637090_production, 53_LVBus637091_production, 53_LVBus637093_production, 53_LVBus637094_production, 53_LVBus637095_production, 53_LVBus637097_production, 53_LVBus637098_production, 53_LVBus637099_production, 53_LVBus637100_production, 53_LVBus637102_production, 53_LVBus637103_production, 53_LVBus637105_production, 53_LVBus637106_consumption, 53_LVBus637106_production, 53_LVBus637107_production, 53_LVBus637108_consumption, 53_LVBus637108_production, 53_LVBus637109_consumption, 53_LVBus637109_production, 53_LVBus637110_production, 53_LVBus637112_production, 53_LVBus637113_consumption, 53_LVBus637113_production, 53_LVBus637114_consumption, 53_LVBus637114_production, 53_LVBus637115_consumption, 53_LVBus637115_production, 53_LVBus637117_production, 53_LVBus637118_consumption, 53_LVBus637118_production, 53_LVBus637119_consumption, 53_LVBus637119_production, 53_LVBus637120_production, 53_LVBus637122_production, 53_LVBus637123_production, 53_LVBus637124_consumption, 53_LVBus637124_production, 53_LVBus637125_production, 53_LVBus637126_consumption, 53_LVBus637126_production, 53_LVBus637128_consumption, 53_LVBus637128_production, 53_LVBus637130_consumption, 53_LVBus637130_production, 53_LVBus637131_production, 53_LVBus637132_production, 53_LVBus637133_production, 53_LVBus637134_production, 53_LVBus637135_production, 53_LVBus637136_consumption, 53_LVBus637136_production, 53_LVBus637137_production, 53_LVBus637139_production, 53_LVBus637140_production, 53_LVBus637141_production, 53_LVBus637142_production, 53_LVBus637143_production, 53_LVBus637145_production, 53_LVBus637147_production, 53_LVBus637148_consumption, 53_LVBus637148_production, 53_LVBus637149_consumption, 53_LVBus637149_production, 53_LVBus637150_production, 53_LVBus637151_production, 53_LVBus637153_production, 53_LVBus637155_production, 53_LVBus637156_production, 53_LVBus637157_production, 53_LVBus637158_consumption, 53_LVBus637158_production, 53_LVBus637159_production, 53_LVBus637160_production, 53_LVBus637161_production, 53_LVBus637162_production, 53_LVBus637163_production, 53_LVBus637164_production, 53_LVBus637165_production, 53_LVBus637166_production, 53_LVBus637167_production, 53_LVBus637169_production, 53_LVBus637170_production, 53_LVBus637171_production, 53_LVBus637175_production, 53_LVBus637176_production, 53_LVBus637177_production, 53_LVBus637179_consumption, 53_LVBus637179_production, 53_LVBus637180_production, 53_LVBus637182_production, 53_LVBus637184_production, 53_LVBus637186_production, 53_LVBus637187_production, 53_LVBus637189_production, 53_LVBus637190_production, 53_LVBus637191_consumption, 53_LVBus637191_production, 53_LVBus637192_production, 53_LVBus637194_production, 53_LVBus637195_production, 53_LVBus637196_consumption, 53_LVBus637196_production, 53_LVBus637197_production, 53_LVBus637198_production, 53_LVBus637199_production, 53_LVBus637200_production, 53_LVBus637201_production, 53_LVBus637202_production, 53_LVBus637203_production, 53_LVBus637204_production, 53_LVBus637205_production, 53_LVBus637206_consumption, 53_LVBus637206_production, 53_LVBus637207_production, 53_LVBus637209_production, 53_LVBus637210_consumption, 53_LVBus637210_production, 53_LVBus637211_production, 53_LVBus637212_consumption, 53_LVBus637212_production, 53_LVBus637213_production, 53_LVBus637215_production, 53_LVBus637216_production, 53_LVBus637217_production, 53_LVBus637219_production, 53_LVBus637220_production, 53_LVBus637221_production, 53_LVBus637223_production, 53_LVBus637224_production, 53_LVBus637225_production, 53_LVBus637227_production, 53_LVBus637228_production, 53_LVBus637229_production, 53_LVBus637230_production, 53_LVBus637231_production, 53_LVBus637232_production, 53_LVBus637233_production, 53_LVBus637235_production, 53_LVBus637236_production, 53_LVBus637237_production, 53_LVBus637240_production, 53_LVBus637241_production, 53_LVBus637242_production, 53_LVBus637243_consumption, 53_LVBus637243_production, 53_LVBus637244_production, 53_LVBus637245_consumption, 53_LVBus637245_production, 53_LVBus637247_production, 53_LVBus637248_production, 53_LVBus637249_consumption, 53_LVBus637249_production, 53_LVBus637251_production, 53_LVBus637253_production, 53_LVBus637255_production, 53_LVBus637256_consumption, 53_LVBus637256_production, 53_LVBus637257_production, 53_LVBus637258_production, 53_LVBus637259_consumption, 53_LVBus637259_production, 53_LVBus637260_production, 53_LVBus637261_production, 53_LVBus637262_production, 53_LVBus637263_production, 53_LVBus637264_production, 53_LVBus637265_production, 53_LVBus637266_production, 53_LVBus637267_production, 53_LVBus637268_production, 53_LVBus637270_production, 53_LVBus637271_production, 53_LVBus637272_production, 53_LVBus637273_production, 53_LVBus637274_production, 53_LVBus637275_production, 53_LVBus637276_production, 53_LVBus637277_production, 53_LVBus637278_consumption, 53_LVBus637278_production, 53_LVBus637279_production, 53_LVBus637280_production, 53_LVBus637281_production, 53_LVBus637282_production, 53_LVBus637283_production, 53_LVBus637285_consumption, 53_LVBus637285_production, 53_LVBus637287_consumption, 53_LVBus637287_production, 53_LVBus637288_production, 53_LVBus637289_production, 53_LVBus637290_production, 53_LVBus637291_production, 53_LVBus637293_consumption, 53_LVBus637293_production, 53_LVBus637294_production, 53_LVBus637295_production, 53_LVBus637296_consumption, 53_LVBus637296_production, 53_LVBus637297_production, 53_LVBus637299_production, 53_LVBus637301_production, 53_LVBus637302_consumption, 53_LVBus637302_production, 53_LVBus637303_production, 53_LVBus637304_production, 53_LVBus637305_production, 53_LVBus637306_production, 53_LVBus637308_production, 53_LVBus637309_production, 53_LVBus637310_consumption, 53_LVBus637310_production, 53_LVBus637311_production, 53_LVBus637312_production, 53_LVBus637314_production, 53_LVBus637316_production, 53_LVBus637317_production, 53_LVBus637319_production, 53_LVBus637320_production, 53_LVBus637321_production, 53_LVBus637322_consumption, 53_LVBus637322_production, 53_LVBus637323_production, 53_LVBus637324_consumption, 53_LVBus637324_production, 53_LVBus637325_production, 53_LVBus637326_production, 53_LVBus637328_production, 53_LVBus637329_production, 53_LVBus637330_production, 53_LVBus637331_consumption, 53_LVBus637331_production, 53_LVBus637332_production, 53_LVBus637333_production, 53_LVBus637334_consumption, 53_LVBus637334_production, 53_LVBus637339_production, 53_LVBus637340_production, 53_LVBus637341_consumption, 53_LVBus637341_production, 53_LVBus637342_production, 53_LVBus637343_production, 53_LVBus637344_consumption, 53_LVBus637344_production, 53_LVBus637345_production, 53_LVBus637347_production, 53_LVBus637348_production, 53_LVBus637349_production, 53_LVBus637350_production, 53_LVBus637351_production, 53_LVBus637353_consumption, 53_LVBus637353_production, 53_LVBus637354_production, 53_LVBus637355_production, 53_LVBus637356_production, 53_LVBus637357_production, 53_LVBus637359_production, 53_LVBus637360_production, 53_LVBus637361_production, 53_LVBus637362_production, 53_LVBus637363_production, 53_LVBus637364_production, 53_LVBus637365_production, 53_LVBus637366_production, 53_LVBus637367_production, 53_LVBus637368_production, 53_LVBus637369_production, 53_LVBus637371_production, 53_LVBus637373_production, 53_LVBus637374_production, 53_LVBus637375_production, 53_LVBus637376_production, 53_LVBus637377_production, 53_LVBus637378_production, 53_LVBus637379_production, 53_LVBus637380_production, 53_LVBus637381_production, 53_LVBus637382_production, 53_LVBus637384_production, 53_LVBus637386_consumption, 53_LVBus637386_production, 53_LVBus637388_production, 53_LVBus637389_production, 53_LVBus637390_production, 53_LVBus637392_production, 53_LVBus637393_production, 53_LVBus637395_production, 53_LVBus637396_production, 53_LVBus637397_production, 53_LVBus637398_production, 53_LVBus637399_production, 53_LVBus637401_production, 53_LVBus637402_production, 53_LVBus637403_production, 53_LVBus637404_production, 53_LVBus637405_production, 53_LVBus637406_production, 53_LVBus637407_production, 53_LVBus637408_production, 53_LVBus637409_production, 53_LVBus637411_production, 53_LVBus637412_production, 53_LVBus637413_production, 53_LVBus637415_production, 53_LVBus637416_consumption, 53_LVBus637416_production, 53_LVBus637418_production, 53_LVBus637419_production, 53_LVBus637420_production, 53_LVBus637421_production, 53_LVBus637422_production, 53_LVBus637423_production, 53_LVBus637424_consumption, 53_LVBus637424_production, 53_LVBus637425_production, 53_LVBus637427_production, 53_LVBus637429_production, 53_LVBus637430_production, 53_LVBus637432_production, 53_LVBus637434_consumption, 53_LVBus637434_production, 53_LVBus637435_consumption, 53_LVBus637435_production, 53_LVBus637436_production, 53_LVBus637438_consumption, 53_LVBus637438_production, 53_LVBus637439_production, 53_LVBus637440_production, 53_LVBus637441_consumption, 53_LVBus637441_production, 53_LVBus637442_production, 53_LVBus637443_production, 53_LVBus637444_production, 53_LVBus637445_consumption, 53_LVBus637445_production, 53_LVBus637446_consumption, 53_LVBus637446_production, 53_LVBus637447_consumption, 53_LVBus637447_production, 53_LVBus637448_consumption, 53_LVBus637448_production, 53_LVBus637449_consumption, 53_LVBus637449_production, 53_LVBus637450_production, 53_LVBus637451_production, 53_LVBus637452_production, 53_LVBus637454_consumption, 53_LVBus637454_production, 53_LVBus637455_production, 53_LVBus637456_consumption, 53_LVBus637456_production, 53_LVBus637457_production, 53_LVBus637458_production, 53_LVBus637459_production, 53_LVBus637460_consumption, 53_LVBus637460_production, 53_LVBus637461_production, 53_LVBus637462_consumption, 53_LVBus637462_production, 53_LVBus637463_production, 53_LVBus637465_production, 53_LVBus637466_consumption, 53_LVBus637466_production, 53_LVBus637467_consumption, 53_LVBus637467_production, 53_LVBus637468_production, 53_LVBus637469_production, 53_LVBus637470_production, 53_LVBus637471_production, 53_LVBus637472_production, 53_LVBus637476_production, 53_LVBus637477_production, 53_LVBus637478_consumption, 53_LVBus637478_production, 53_LVBus637479_production, 53_LVBus637480_production, 53_LVBus637481_production, 53_LVBus637483_production, 53_LVBus637484_production, 53_LVBus637485_production, 53_LVBus637486_production, 53_LVBus637487_production, 53_LVBus637488_production, 53_LVBus637490_production, 53_LVBus637491_production, 53_LVBus637492_production, 53_LVBus637493_production, 53_LVBus637494_production, 53_LVBus637496_consumption, 53_LVBus637496_production, 53_LVBus637497_production, 53_LVBus637498_production, 53_LVBus637499_production, 53_LVBus637500_production, 53_LVBus637502_consumption, 53_LVBus637502_production, 53_LVBus637503_production, 53_LVBus637504_production, 53_LVBus637505_production, 53_LVBus637506_production, 53_LVBus637507_production, 53_LVBus637508_production, 53_LVBus637509_consumption, 53_LVBus637509_production, 53_LVBus637510_production, 53_LVBus637512_consumption, 53_LVBus637512_production, 53_LVBus637513_consumption, 53_LVBus637513_production, 53_LVBus637514_production, 53_LVBus637515_production, 53_LVBus637516_consumption, 53_LVBus637516_production, 53_LVBus637517_production, 53_LVBus637519_production, 53_LVBus637520_production, 53_LVBus637521_consumption, 53_LVBus637521_production, 53_LVBus637522_production, 53_LVBus637523_production, 53_LVBus637525_production, 53_LVBus637527_production, 53_LVBus637528_consumption, 53_LVBus637528_production, 53_LVBus637529_consumption, 53_LVBus637529_production, 53_LVBus637530_production, 53_LVBus637531_production, 53_LVBus637533_consumption, 53_LVBus637533_production, 53_LVBus637534_production, 53_LVBus637535_consumption, 53_LVBus637535_production, 53_LVBus637536_consumption, 53_LVBus637536_production, 53_LVBus637538_production, 53_LVBus637539_production, 53_LVBus637540_production, 53_LVBus637542_production, 53_LVBus637543_production, 53_LVBus637544_production, 53_LVBus637546_consumption, 53_LVBus637546_production, 53_LVBus637547_production, 53_LVBus637548_consumption, 53_LVBus637548_production, 53_LVBus637549_consumption, 53_LVBus637549_production, 53_LVBus637550_production, 53_LVBus637551_consumption, 53_LVBus637551_production, 53_LVBus637552_production, 53_LVBus637553_production, 53_LVBus637554_production, 53_LVBus637557_consumption, 53_LVBus637557_production, 53_LVBus637559_production, 53_LVBus637561_production, 53_LVBus637562_production, 53_LVBus637563_production, 53_LVBus637564_production, 53_LVBus637565_consumption, 53_LVBus637565_production, 53_LVBus637567_production, 53_LVBus637568_production, 53_LVBus637569_production, 53_LVBus637570_consumption, 53_LVBus637570_production, 53_LVBus637571_production, 53_LVBus637572_production, 53_LVBus637573_production, 53_LVBus637575_production, 53_LVBus637576_production, 53_LVBus637577_production, 53_LVBus637578_production, 53_LVBus637579_production, 53_LVBus637581_production, 53_LVBus637582_production, 53_LVBus637584_production, 53_LVBus637585_production, 53_LVBus637586_consumption, 53_LVBus637586_production, 53_LVBus637588_production, 53_LVBus637590_production, 53_LVBus637591_consumption, 53_LVBus637591_production, 53_LVBus637592_production, 53_LVBus637595_production, 53_LVBus637597_production, 53_LVBus637598_production, 53_LVBus637599_production, 53_LVBus637600_production, 53_LVBus637601_production, 53_LVBus637602_production, 53_LVBus637603_production, 53_LVBus637605_consumption, 53_LVBus637605_production, 53_LVBus637606_production, 53_LVBus637607_production, 53_LVBus637608_production, 53_LVBus637610_consumption, 53_LVBus637610_production, 53_LVBus637611_production, 53_LVBus637612_production, 53_LVBus637613_consumption, 53_LVBus637613_production, 53_LVBus637614_production, 53_LVBus637615_production, 53_LVBus637616_production, 53_LVBus637618_production, 53_LVBus637619_consumption, 53_LVBus637619_production, 53_LVBus637620_consumption, 53_LVBus637620_production, 53_LVBus637621_production, 53_LVBus637622_production, 53_LVBus637623_production, 53_LVBus637624_production, 53_LVBus637625_production, 53_LVBus637626_production, 53_LVBus637627_production, 53_LVBus976921_consumption, 53_LVBus976921_production, 53_LVBus979202_production, 53_LVBus984538_consumption, 53_LVBus984538_production, 53_LVBus985464_consumption, 53_LVBus985464_production, 53_LVBus995390_production, 53_LVBus995391_production, 53_LVBus995716_production, 53_MVLV11171_consumption, 53_MVLV11171_production, 53_MVLV21471_consumption, 53_MVLV21471_production, 53_MVLV39566_consumption, 53_MVLV39566_production, 53_MVLV52046_consumption, 53_MVLV52046_production, 53_MVLV53642_consumption, 53_MVLV53642_production, 53_MVLV81384_consumption, 53_MVLV81384_production.

## 9. Data Quality Summary

**Total findings:** 377 (0 errors, 5 warnings, 372 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  604 of 998 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.39 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  605 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637090_consumption`  
  Load '53_LVBus637090_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637393_consumption`  
  Load '53_LVBus637393_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637163_consumption`  
  Load '53_LVBus637163_consumption' has phase imbalance of 49.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637059_consumption`  
  Load '53_LVBus637059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637402_consumption`  
  Load '53_LVBus637402_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637207_consumption`  
  Load '53_LVBus637207_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1008586_consumption`  
  Load '53_LVBus1008586_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637086_consumption`  
  Load '53_LVBus637086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637622_consumption`  
  Load '53_LVBus637622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637420_consumption`  
  Load '53_LVBus637420_consumption' has phase imbalance of 207.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637211_consumption`  
  Load '53_LVBus637211_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637500_consumption`  
  Load '53_LVBus637500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637381_consumption`  
  Load '53_LVBus637381_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637397_consumption`  
  Load '53_LVBus637397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637371_consumption`  
  Load '53_LVBus637371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637272_consumption`  
  Load '53_LVBus637272_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637255_consumption`  
  Load '53_LVBus637255_consumption' has phase imbalance of 235.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637167_consumption`  
  Load '53_LVBus637167_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637141_consumption`  
  Load '53_LVBus637141_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637376_consumption`  
  Load '53_LVBus637376_consumption' has phase imbalance of 21.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637078_consumption`  
  Load '53_LVBus637078_consumption' has phase imbalance of 288.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637395_consumption`  
  Load '53_LVBus637395_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637102_consumption`  
  Load '53_LVBus637102_consumption' has phase imbalance of 89.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637481_consumption`  
  Load '53_LVBus637481_consumption' has phase imbalance of 79.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637552_consumption`  
  Load '53_LVBus637552_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1018088_consumption`  
  Load '53_LVBus1018088_consumption' has phase imbalance of 77.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637540_consumption`  
  Load '53_LVBus637540_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637247_consumption`  
  Load '53_LVBus637247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637561_consumption`  
  Load '53_LVBus637561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637205_consumption`  
  Load '53_LVBus637205_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637303_consumption`  
  Load '53_LVBus637303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637242_consumption`  
  Load '53_LVBus637242_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637175_consumption`  
  Load '53_LVBus637175_consumption' has phase imbalance of 145.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637204_consumption`  
  Load '53_LVBus637204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637364_consumption`  
  Load '53_LVBus637364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637164_consumption`  
  Load '53_LVBus637164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637538_consumption`  
  Load '53_LVBus637538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637281_consumption`  
  Load '53_LVBus637281_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637504_consumption`  
  Load '53_LVBus637504_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637145_consumption`  
  Load '53_LVBus637145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637077_consumption`  
  Load '53_LVBus637077_consumption' has phase imbalance of 262.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637508_consumption`  
  Load '53_LVBus637508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637279_consumption`  
  Load '53_LVBus637279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637280_consumption`  
  Load '53_LVBus637280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637110_consumption`  
  Load '53_LVBus637110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637305_consumption`  
  Load '53_LVBus637305_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637215_consumption`  
  Load '53_LVBus637215_consumption' has phase imbalance of 272.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637329_consumption`  
  Load '53_LVBus637329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637626_consumption`  
  Load '53_LVBus637626_consumption' has phase imbalance of 164.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637306_consumption`  
  Load '53_LVBus637306_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637531_consumption`  
  Load '53_LVBus637531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637067_consumption`  
  Load '53_LVBus637067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637258_consumption`  
  Load '53_LVBus637258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637493_consumption`  
  Load '53_LVBus637493_consumption' has phase imbalance of 63.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1012181_consumption`  
  Load '53_LVBus1012181_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637614_consumption`  
  Load '53_LVBus637614_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637194_consumption`  
  Load '53_LVBus637194_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637392_consumption`  
  Load '53_LVBus637392_consumption' has phase imbalance of 117.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637472_consumption`  
  Load '53_LVBus637472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637366_consumption`  
  Load '53_LVBus637366_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637340_consumption`  
  Load '53_LVBus637340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637461_consumption`  
  Load '53_LVBus637461_consumption' has phase imbalance of 136.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637063_consumption`  
  Load '53_LVBus637063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637189_consumption`  
  Load '53_LVBus637189_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637368_consumption`  
  Load '53_LVBus637368_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637275_consumption`  
  Load '53_LVBus637275_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637192_consumption`  
  Load '53_LVBus637192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637439_consumption`  
  Load '53_LVBus637439_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637054_consumption`  
  Load '53_LVBus637054_consumption' has phase imbalance of 163.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637436_consumption`  
  Load '53_LVBus637436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637361_consumption`  
  Load '53_LVBus637361_consumption' has phase imbalance of 223.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1023082_consumption`  
  Load '53_LVBus1023082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637139_consumption`  
  Load '53_LVBus637139_consumption' has phase imbalance of 255.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637476_consumption`  
  Load '53_LVBus637476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637328_consumption`  
  Load '53_LVBus637328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637282_consumption`  
  Load '53_LVBus637282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637075_consumption`  
  Load '53_LVBus637075_consumption' has phase imbalance of 245.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637098_consumption`  
  Load '53_LVBus637098_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637350_consumption`  
  Load '53_LVBus637350_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637309_consumption`  
  Load '53_LVBus637309_consumption' has phase imbalance of 197.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637240_consumption`  
  Load '53_LVBus637240_consumption' has phase imbalance of 267.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637103_consumption`  
  Load '53_LVBus637103_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637354_consumption`  
  Load '53_LVBus637354_consumption' has phase imbalance of 239.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637602_consumption`  
  Load '53_LVBus637602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637199_consumption`  
  Load '53_LVBus637199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637405_consumption`  
  Load '53_LVBus637405_consumption' has phase imbalance of 114.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637083_consumption`  
  Load '53_LVBus637083_consumption' has phase imbalance of 126.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637363_consumption`  
  Load '53_LVBus637363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637343_consumption`  
  Load '53_LVBus637343_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637184_consumption`  
  Load '53_LVBus637184_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637190_consumption`  
  Load '53_LVBus637190_consumption' has phase imbalance of 289.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637375_consumption`  
  Load '53_LVBus637375_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637076_consumption`  
  Load '53_LVBus637076_consumption' has phase imbalance of 247.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637477_consumption`  
  Load '53_LVBus637477_consumption' has phase imbalance of 234.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637455_consumption`  
  Load '53_LVBus637455_consumption' has phase imbalance of 250.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637304_consumption`  
  Load '53_LVBus637304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637182_consumption`  
  Load '53_LVBus637182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637406_consumption`  
  Load '53_LVBus637406_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637342_consumption`  
  Load '53_LVBus637342_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637219_consumption`  
  Load '53_LVBus637219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1008584_consumption`  
  Load '53_LVBus1008584_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637260_consumption`  
  Load '53_LVBus637260_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637612_consumption`  
  Load '53_LVBus637612_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637225_consumption`  
  Load '53_LVBus637225_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1013050_consumption`  
  Load '53_LVBus1013050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637616_consumption`  
  Load '53_LVBus637616_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637241_consumption`  
  Load '53_LVBus637241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637539_consumption`  
  Load '53_LVBus637539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637559_consumption`  
  Load '53_LVBus637559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637320_consumption`  
  Load '53_LVBus637320_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637507_consumption`  
  Load '53_LVBus637507_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637452_consumption`  
  Load '53_LVBus637452_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637088_consumption`  
  Load '53_LVBus637088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637465_consumption`  
  Load '53_LVBus637465_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637599_consumption`  
  Load '53_LVBus637599_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637362_consumption`  
  Load '53_LVBus637362_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637171_consumption`  
  Load '53_LVBus637171_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus995391_consumption`  
  Load '53_LVBus995391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637085_consumption`  
  Load '53_LVBus637085_consumption' has phase imbalance of 266.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637261_consumption`  
  Load '53_LVBus637261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637491_consumption`  
  Load '53_LVBus637491_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637314_consumption`  
  Load '53_LVBus637314_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637321_consumption`  
  Load '53_LVBus637321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637357_consumption`  
  Load '53_LVBus637357_consumption' has phase imbalance of 268.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637230_consumption`  
  Load '53_LVBus637230_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637170_consumption`  
  Load '53_LVBus637170_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1008583_consumption`  
  Load '53_LVBus1008583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637091_consumption`  
  Load '53_LVBus637091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637202_consumption`  
  Load '53_LVBus637202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637131_consumption`  
  Load '53_LVBus637131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637486_consumption`  
  Load '53_LVBus637486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637089_consumption`  
  Load '53_LVBus637089_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637554_consumption`  
  Load '53_LVBus637554_consumption' has phase imbalance of 228.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637094_consumption`  
  Load '53_LVBus637094_consumption' has phase imbalance of 76.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637253_consumption`  
  Load '53_LVBus637253_consumption' has phase imbalance of 51.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637425_consumption`  
  Load '53_LVBus637425_consumption' has phase imbalance of 291.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637349_consumption`  
  Load '53_LVBus637349_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637412_consumption`  
  Load '53_LVBus637412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637384_consumption`  
  Load '53_LVBus637384_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637382_consumption`  
  Load '53_LVBus637382_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1012182_consumption`  
  Load '53_LVBus1012182_consumption' has phase imbalance of 238.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637062_consumption`  
  Load '53_LVBus637062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637227_consumption`  
  Load '53_LVBus637227_consumption' has phase imbalance of 183.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637356_consumption`  
  Load '53_LVBus637356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637122_consumption`  
  Load '53_LVBus637122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637484_consumption`  
  Load '53_LVBus637484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637237_consumption`  
  Load '53_LVBus637237_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637180_consumption`  
  Load '53_LVBus637180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637562_consumption`  
  Load '53_LVBus637562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637575_consumption`  
  Load '53_LVBus637575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637499_consumption`  
  Load '53_LVBus637499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637577_consumption`  
  Load '53_LVBus637577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637443_consumption`  
  Load '53_LVBus637443_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637367_consumption`  
  Load '53_LVBus637367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637235_consumption`  
  Load '53_LVBus637235_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637567_consumption`  
  Load '53_LVBus637567_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637396_consumption`  
  Load '53_LVBus637396_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1013049_consumption`  
  Load '53_LVBus1013049_consumption' has phase imbalance of 140.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637534_consumption`  
  Load '53_LVBus637534_consumption' has phase imbalance of 287.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637399_consumption`  
  Load '53_LVBus637399_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637624_consumption`  
  Load '53_LVBus637624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637515_consumption`  
  Load '53_LVBus637515_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637233_consumption`  
  Load '53_LVBus637233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637355_consumption`  
  Load '53_LVBus637355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637458_consumption`  
  Load '53_LVBus637458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637150_consumption`  
  Load '53_LVBus637150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637360_consumption`  
  Load '53_LVBus637360_consumption' has phase imbalance of 121.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637440_consumption`  
  Load '53_LVBus637440_consumption' has phase imbalance of 266.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637569_consumption`  
  Load '53_LVBus637569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637134_consumption`  
  Load '53_LVBus637134_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637220_consumption`  
  Load '53_LVBus637220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637487_consumption`  
  Load '53_LVBus637487_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637625_consumption`  
  Load '53_LVBus637625_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637263_consumption`  
  Load '53_LVBus637263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637485_consumption`  
  Load '53_LVBus637485_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637359_consumption`  
  Load '53_LVBus637359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637107_consumption`  
  Load '53_LVBus637107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus979202_consumption`  
  Load '53_LVBus979202_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1028248_consumption`  
  Load '53_LVBus1028248_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637377_consumption`  
  Load '53_LVBus637377_consumption' has phase imbalance of 80.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1030632_consumption`  
  Load '53_LVBus1030632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637093_consumption`  
  Load '53_LVBus637093_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637388_consumption`  
  Load '53_LVBus637388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637497_consumption`  
  Load '53_LVBus637497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637288_consumption`  
  Load '53_LVBus637288_consumption' has phase imbalance of 89.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637274_consumption`  
  Load '53_LVBus637274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637161_consumption`  
  Load '53_LVBus637161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637195_consumption`  
  Load '53_LVBus637195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637564_consumption`  
  Load '53_LVBus637564_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637490_consumption`  
  Load '53_LVBus637490_consumption' has phase imbalance of 143.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637299_consumption`  
  Load '53_LVBus637299_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637251_consumption`  
  Load '53_LVBus637251_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637510_consumption`  
  Load '53_LVBus637510_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637494_consumption`  
  Load '53_LVBus637494_consumption' has phase imbalance of 70.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637068_consumption`  
  Load '53_LVBus637068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637265_consumption`  
  Load '53_LVBus637265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637221_consumption`  
  Load '53_LVBus637221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637365_consumption`  
  Load '53_LVBus637365_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637442_consumption`  
  Load '53_LVBus637442_consumption' has phase imbalance of 240.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637374_consumption`  
  Load '53_LVBus637374_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637598_consumption`  
  Load '53_LVBus637598_consumption' has phase imbalance of 185.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637517_consumption`  
  Load '53_LVBus637517_consumption' has phase imbalance of 175.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637201_consumption`  
  Load '53_LVBus637201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637257_consumption`  
  Load '53_LVBus637257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637137_consumption`  
  Load '53_LVBus637137_consumption' has phase imbalance of 243.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637444_consumption`  
  Load '53_LVBus637444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637459_consumption`  
  Load '53_LVBus637459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637297_consumption`  
  Load '53_LVBus637297_consumption' has phase imbalance of 93.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637224_consumption`  
  Load '53_LVBus637224_consumption' has phase imbalance of 119.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637099_consumption`  
  Load '53_LVBus637099_consumption' has phase imbalance of 132.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637351_consumption`  
  Load '53_LVBus637351_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637264_consumption`  
  Load '53_LVBus637264_consumption' has phase imbalance of 284.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637312_consumption`  
  Load '53_LVBus637312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637373_consumption`  
  Load '53_LVBus637373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637072_consumption`  
  Load '53_LVBus637072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637232_consumption`  
  Load '53_LVBus637232_consumption' has phase imbalance of 126.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637404_consumption`  
  Load '53_LVBus637404_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637073_consumption`  
  Load '53_LVBus637073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637231_consumption`  
  Load '53_LVBus637231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637380_consumption`  
  Load '53_LVBus637380_consumption' has phase imbalance of 129.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637223_consumption`  
  Load '53_LVBus637223_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637603_consumption`  
  Load '53_LVBus637603_consumption' has phase imbalance of 30.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637200_consumption`  
  Load '53_LVBus637200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637330_consumption`  
  Load '53_LVBus637330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637527_consumption`  
  Load '53_LVBus637527_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637615_consumption`  
  Load '53_LVBus637615_consumption' has phase imbalance of 184.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637147_consumption`  
  Load '53_LVBus637147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637623_consumption`  
  Load '53_LVBus637623_consumption' has phase imbalance of 250.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637576_consumption`  
  Load '53_LVBus637576_consumption' has phase imbalance of 221.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637276_consumption`  
  Load '53_LVBus637276_consumption' has phase imbalance of 110.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637483_consumption`  
  Load '53_LVBus637483_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637244_consumption`  
  Load '53_LVBus637244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637217_consumption`  
  Load '53_LVBus637217_consumption' has phase imbalance of 222.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637600_consumption`  
  Load '53_LVBus637600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637169_consumption`  
  Load '53_LVBus637169_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637325_consumption`  
  Load '53_LVBus637325_consumption' has phase imbalance of 44.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637087_consumption`  
  Load '53_LVBus637087_consumption' has phase imbalance of 266.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637213_consumption`  
  Load '53_LVBus637213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637408_consumption`  
  Load '53_LVBus637408_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637203_consumption`  
  Load '53_LVBus637203_consumption' has phase imbalance of 186.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637295_consumption`  
  Load '53_LVBus637295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637470_consumption`  
  Load '53_LVBus637470_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637457_consumption`  
  Load '53_LVBus637457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637323_consumption`  
  Load '53_LVBus637323_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637132_consumption`  
  Load '53_LVBus637132_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637209_consumption`  
  Load '53_LVBus637209_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637608_consumption`  
  Load '53_LVBus637608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637579_consumption`  
  Load '53_LVBus637579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637135_consumption`  
  Load '53_LVBus637135_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637064_consumption`  
  Load '53_LVBus637064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637403_consumption`  
  Load '53_LVBus637403_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637160_consumption`  
  Load '53_LVBus637160_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637421_consumption`  
  Load '53_LVBus637421_consumption' has phase imbalance of 58.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1012180_consumption`  
  Load '53_LVBus1012180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637319_consumption`  
  Load '53_LVBus637319_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637100_consumption`  
  Load '53_LVBus637100_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637294_consumption`  
  Load '53_LVBus637294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637186_consumption`  
  Load '53_LVBus637186_consumption' has phase imbalance of 241.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637095_consumption`  
  Load '53_LVBus637095_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637378_consumption`  
  Load '53_LVBus637378_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637422_consumption`  
  Load '53_LVBus637422_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637061_consumption`  
  Load '53_LVBus637061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637301_consumption`  
  Load '53_LVBus637301_consumption' has phase imbalance of 47.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637488_consumption`  
  Load '53_LVBus637488_consumption' has phase imbalance of 223.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637142_consumption`  
  Load '53_LVBus637142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637463_consumption`  
  Load '53_LVBus637463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637266_consumption`  
  Load '53_LVBus637266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637055_consumption`  
  Load '53_LVBus637055_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637411_consumption`  
  Load '53_LVBus637411_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637273_consumption`  
  Load '53_LVBus637273_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus995390_consumption`  
  Load '53_LVBus995390_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637398_consumption`  
  Load '53_LVBus637398_consumption' has phase imbalance of 216.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637097_consumption`  
  Load '53_LVBus637097_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637123_consumption`  
  Load '53_LVBus637123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637270_consumption`  
  Load '53_LVBus637270_consumption' has phase imbalance of 133.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637606_consumption`  
  Load '53_LVBus637606_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637120_consumption`  
  Load '53_LVBus637120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637267_consumption`  
  Load '53_LVBus637267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637117_consumption`  
  Load '53_LVBus637117_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637471_consumption`  
  Load '53_LVBus637471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637563_consumption`  
  Load '53_LVBus637563_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637544_consumption`  
  Load '53_LVBus637544_consumption' has phase imbalance of 202.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637316_consumption`  
  Load '53_LVBus637316_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637332_consumption`  
  Load '53_LVBus637332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637369_consumption`  
  Load '53_LVBus637369_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637133_consumption`  
  Load '53_LVBus637133_consumption' has phase imbalance of 136.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637573_consumption`  
  Load '53_LVBus637573_consumption' has phase imbalance of 76.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637070_consumption`  
  Load '53_LVBus637070_consumption' has phase imbalance of 274.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637176_consumption`  
  Load '53_LVBus637176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1008585_consumption`  
  Load '53_LVBus1008585_consumption' has phase imbalance of 72.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637308_consumption`  
  Load '53_LVBus637308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637390_consumption`  
  Load '53_LVBus637390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637427_consumption`  
  Load '53_LVBus637427_consumption' has phase imbalance of 129.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637389_consumption`  
  Load '53_LVBus637389_consumption' has phase imbalance of 126.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637271_consumption`  
  Load '53_LVBus637271_consumption' has phase imbalance of 98.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637229_consumption`  
  Load '53_LVBus637229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637166_consumption`  
  Load '53_LVBus637166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637415_consumption`  
  Load '53_LVBus637415_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637197_consumption`  
  Load '53_LVBus637197_consumption' has phase imbalance of 51.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637379_consumption`  
  Load '53_LVBus637379_consumption' has phase imbalance of 243.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637519_consumption`  
  Load '53_LVBus637519_consumption' has phase imbalance of 239.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637159_consumption`  
  Load '53_LVBus637159_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637468_consumption`  
  Load '53_LVBus637468_consumption' has phase imbalance of 84.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637151_consumption`  
  Load '53_LVBus637151_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637262_consumption`  
  Load '53_LVBus637262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637601_consumption`  
  Load '53_LVBus637601_consumption' has phase imbalance of 224.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637347_consumption`  
  Load '53_LVBus637347_consumption' has phase imbalance of 276.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637236_consumption`  
  Load '53_LVBus637236_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637082_consumption`  
  Load '53_LVBus637082_consumption' has phase imbalance of 254.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637418_consumption`  
  Load '53_LVBus637418_consumption' has phase imbalance of 237.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637492_consumption`  
  Load '53_LVBus637492_consumption' has phase imbalance of 286.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637071_consumption`  
  Load '53_LVBus637071_consumption' has phase imbalance of 257.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637105_consumption`  
  Load '53_LVBus637105_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637112_consumption`  
  Load '53_LVBus637112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637401_consumption`  
  Load '53_LVBus637401_consumption' has phase imbalance of 225.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637165_consumption`  
  Load '53_LVBus637165_consumption' has phase imbalance of 87.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637480_consumption`  
  Load '53_LVBus637480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637339_consumption`  
  Load '53_LVBus637339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637611_consumption`  
  Load '53_LVBus637611_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637143_consumption`  
  Load '53_LVBus637143_consumption' has phase imbalance of 141.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637547_consumption`  
  Load '53_LVBus637547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637317_consumption`  
  Load '53_LVBus637317_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637523_consumption`  
  Load '53_LVBus637523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637621_consumption`  
  Load '53_LVBus637621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637198_consumption`  
  Load '53_LVBus637198_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637156_consumption`  
  Load '53_LVBus637156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637542_consumption`  
  Load '53_LVBus637542_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637550_consumption`  
  Load '53_LVBus637550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637155_consumption`  
  Load '53_LVBus637155_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637520_consumption`  
  Load '53_LVBus637520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637277_consumption`  
  Load '53_LVBus637277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637451_consumption`  
  Load '53_LVBus637451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637187_consumption`  
  Load '53_LVBus637187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637505_consumption`  
  Load '53_LVBus637505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637530_consumption`  
  Load '53_LVBus637530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637568_consumption`  
  Load '53_LVBus637568_consumption' has phase imbalance of 182.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1012184_consumption`  
  Load '53_LVBus1012184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637498_consumption`  
  Load '53_LVBus637498_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637177_consumption`  
  Load '53_LVBus637177_consumption' has phase imbalance of 259.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637409_consumption`  
  Load '53_LVBus637409_consumption' has phase imbalance of 73.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637450_consumption`  
  Load '53_LVBus637450_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637597_consumption`  
  Load '53_LVBus637597_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637345_consumption`  
  Load '53_LVBus637345_consumption' has phase imbalance of 249.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637522_consumption`  
  Load '53_LVBus637522_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637326_consumption`  
  Load '53_LVBus637326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637228_consumption`  
  Load '53_LVBus637228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637283_consumption`  
  Load '53_LVBus637283_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637216_consumption`  
  Load '53_LVBus637216_consumption' has phase imbalance of 97.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637578_consumption`  
  Load '53_LVBus637578_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus637268_consumption`  
  Load '53_LVBus637268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 998 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus637429' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus637581' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus637595' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus637153' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '53_LVBus637434' (LV, 0.24 kV) has an electrical reach of 1.1 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '53_LVBus637299' (LV, 0.24 kV) has an electrical reach of 18.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '53_LVBus637153' (LV, 0.24 kV) has an electrical reach of 6.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  682 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  262 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 53_LVBus1008583_consumption, 53_LVBus1008586_consumption, 53_LVBus1012180_consumption, 53_LVBus1012182_consumption, 53_LVBus1012184_consumption, 53_LVBus1013050_consumption, 53_LVBus1023082_consumption, 53_LVBus1028248_consumption, 53_LVBus1030632_consumption, 53_LVBus637054_consumption, 53_LVBus637055_consumption, 53_LVBus637059_consumption, 53_LVBus637061_consumption, 53_LVBus637062_consumption, 53_LVBus637063_consumption, 53_LVBus637064_consumption, 53_LVBus637067_consumption, 53_LVBus637068_consumption, 53_LVBus637072_consumption, 53_LVBus637073_consumption, 53_LVBus637075_consumption, 53_LVBus637076_consumption, 53_LVBus637077_consumption, 53_LVBus637078_consumption, 53_LVBus637082_consumption, 53_LVBus637085_consumption, 53_LVBus637086_consumption, 53_LVBus637088_consumption, 53_LVBus637089_consumption, 53_LVBus637090_consumption, 53_LVBus637091_consumption, 53_LVBus637093_consumption, 53_LVBus637095_consumption, 53_LVBus637097_consumption, 53_LVBus637100_consumption, 53_LVBus637107_consumption, 53_LVBus637110_consumption, 53_LVBus637112_consumption, 53_LVBus637117_consumption, 53_LVBus637120_consumption, 53_LVBus637122_consumption, 53_LVBus637123_consumption, 53_LVBus637131_consumption, 53_LVBus637132_consumption, 53_LVBus637134_consumption, 53_LVBus637135_consumption, 53_LVBus637137_consumption, 53_LVBus637139_consumption, 53_LVBus637141_consumption, 53_LVBus637142_consumption, 53_LVBus637145_consumption, 53_LVBus637147_consumption, 53_LVBus637150_consumption, 53_LVBus637151_consumption, 53_LVBus637156_consumption, 53_LVBus637161_consumption, 53_LVBus637164_consumption, 53_LVBus637166_consumption, 53_LVBus637167_consumption, 53_LVBus637176_consumption, 53_LVBus637177_consumption, 53_LVBus637180_consumption, 53_LVBus637182_consumption, 53_LVBus637184_consumption, 53_LVBus637186_consumption, 53_LVBus637187_consumption, 53_LVBus637189_consumption, 53_LVBus637190_consumption, 53_LVBus637192_consumption, 53_LVBus637194_consumption, 53_LVBus637195_consumption, 53_LVBus637198_consumption, 53_LVBus637199_consumption, 53_LVBus637200_consumption, 53_LVBus637201_consumption, 53_LVBus637202_consumption, 53_LVBus637203_consumption, 53_LVBus637204_consumption, 53_LVBus637205_consumption, 53_LVBus637207_consumption, 53_LVBus637209_consumption, 53_LVBus637211_consumption, 53_LVBus637213_consumption, 53_LVBus637215_consumption, 53_LVBus637217_consumption, 53_LVBus637219_consumption, 53_LVBus637220_consumption, 53_LVBus637221_consumption, 53_LVBus637223_consumption, 53_LVBus637225_consumption, 53_LVBus637227_consumption, 53_LVBus637228_consumption, 53_LVBus637229_consumption, 53_LVBus637230_consumption, 53_LVBus637231_consumption, 53_LVBus637233_consumption, 53_LVBus637235_consumption, 53_LVBus637237_consumption, 53_LVBus637240_consumption, 53_LVBus637241_consumption, 53_LVBus637242_consumption, 53_LVBus637244_consumption, 53_LVBus637247_consumption, 53_LVBus637255_consumption, 53_LVBus637257_consumption, 53_LVBus637258_consumption, 53_LVBus637260_consumption, 53_LVBus637261_consumption, 53_LVBus637262_consumption, 53_LVBus637263_consumption, 53_LVBus637265_consumption, 53_LVBus637266_consumption, 53_LVBus637267_consumption, 53_LVBus637268_consumption, 53_LVBus637272_consumption, 53_LVBus637273_consumption, 53_LVBus637274_consumption, 53_LVBus637275_consumption, 53_LVBus637277_consumption, 53_LVBus637279_consumption, 53_LVBus637280_consumption, 53_LVBus637281_consumption, 53_LVBus637282_consumption, 53_LVBus637294_consumption, 53_LVBus637295_consumption, 53_LVBus637299_consumption, 53_LVBus637303_consumption, 53_LVBus637304_consumption, 53_LVBus637305_consumption, 53_LVBus637306_consumption, 53_LVBus637308_consumption, 53_LVBus637309_consumption, 53_LVBus637312_consumption, 53_LVBus637314_consumption, 53_LVBus637317_consumption, 53_LVBus637319_consumption, 53_LVBus637320_consumption, 53_LVBus637321_consumption, 53_LVBus637323_consumption, 53_LVBus637326_consumption, 53_LVBus637328_consumption, 53_LVBus637329_consumption, 53_LVBus637330_consumption, 53_LVBus637332_consumption, 53_LVBus637339_consumption, 53_LVBus637340_consumption, 53_LVBus637342_consumption, 53_LVBus637343_consumption, 53_LVBus637345_consumption, 53_LVBus637347_consumption, 53_LVBus637349_consumption, 53_LVBus637350_consumption, 53_LVBus637351_consumption, 53_LVBus637354_consumption, 53_LVBus637355_consumption, 53_LVBus637356_consumption, 53_LVBus637357_consumption, 53_LVBus637359_consumption, 53_LVBus637361_consumption, 53_LVBus637362_consumption, 53_LVBus637363_consumption, 53_LVBus637364_consumption, 53_LVBus637365_consumption, 53_LVBus637366_consumption, 53_LVBus637367_consumption, 53_LVBus637368_consumption, 53_LVBus637369_consumption, 53_LVBus637371_consumption, 53_LVBus637373_consumption, 53_LVBus637374_consumption, 53_LVBus637378_consumption, 53_LVBus637379_consumption, 53_LVBus637381_consumption, 53_LVBus637382_consumption, 53_LVBus637384_consumption, 53_LVBus637388_consumption, 53_LVBus637390_consumption, 53_LVBus637397_consumption, 53_LVBus637399_consumption, 53_LVBus637401_consumption, 53_LVBus637404_consumption, 53_LVBus637406_consumption, 53_LVBus637408_consumption, 53_LVBus637411_consumption, 53_LVBus637412_consumption, 53_LVBus637420_consumption, 53_LVBus637422_consumption, 53_LVBus637436_consumption, 53_LVBus637439_consumption, 53_LVBus637442_consumption, 53_LVBus637443_consumption, 53_LVBus637444_consumption, 53_LVBus637450_consumption, 53_LVBus637451_consumption, 53_LVBus637452_consumption, 53_LVBus637455_consumption, 53_LVBus637457_consumption, 53_LVBus637458_consumption, 53_LVBus637459_consumption, 53_LVBus637463_consumption, 53_LVBus637465_consumption, 53_LVBus637471_consumption, 53_LVBus637472_consumption, 53_LVBus637476_consumption, 53_LVBus637480_consumption, 53_LVBus637483_consumption, 53_LVBus637484_consumption, 53_LVBus637485_consumption, 53_LVBus637486_consumption, 53_LVBus637487_consumption, 53_LVBus637488_consumption, 53_LVBus637492_consumption, 53_LVBus637497_consumption, 53_LVBus637498_consumption, 53_LVBus637499_consumption, 53_LVBus637500_consumption, 53_LVBus637504_consumption, 53_LVBus637505_consumption, 53_LVBus637508_consumption, 53_LVBus637510_consumption, 53_LVBus637519_consumption, 53_LVBus637520_consumption, 53_LVBus637522_consumption, 53_LVBus637523_consumption, 53_LVBus637527_consumption, 53_LVBus637530_consumption, 53_LVBus637531_consumption, 53_LVBus637534_consumption, 53_LVBus637538_consumption, 53_LVBus637539_consumption, 53_LVBus637540_consumption, 53_LVBus637542_consumption, 53_LVBus637547_consumption, 53_LVBus637550_consumption, 53_LVBus637552_consumption, 53_LVBus637559_consumption, 53_LVBus637561_consumption, 53_LVBus637562_consumption, 53_LVBus637563_consumption, 53_LVBus637567_consumption, 53_LVBus637569_consumption, 53_LVBus637575_consumption, 53_LVBus637576_consumption, 53_LVBus637577_consumption, 53_LVBus637578_consumption, 53_LVBus637579_consumption, 53_LVBus637598_consumption, 53_LVBus637600_consumption, 53_LVBus637601_consumption, 53_LVBus637602_consumption, 53_LVBus637606_consumption, 53_LVBus637608_consumption, 53_LVBus637611_consumption, 53_LVBus637614_consumption, 53_LVBus637615_consumption, 53_LVBus637621_consumption, 53_LVBus637622_consumption, 53_LVBus637623_consumption, 53_LVBus637624_consumption, 53_LVBus637626_consumption, 53_LVBus995390_consumption, 53_LVBus995391_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  499 group(s) of loads (998 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  10 group(s) of series lines (21 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  605 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus1008582_consumption, 53_LVBus1008582_production, 53_LVBus1008583_production, 53_LVBus1008584_production, 53_LVBus1008585_production, 53_LVBus1008586_production, 53_LVBus1012180_production, 53_LVBus1012181_production, 53_LVBus1012182_production, 53_LVBus1012183_consumption, 53_LVBus1012183_production, 53_LVBus1012184_production, 53_LVBus1013048_production, 53_LVBus1013049_production, 53_LVBus1013050_production, 53_LVBus1018088_production, 53_LVBus1023082_production, 53_LVBus1028248_production, 53_LVBus1030629_consumption, 53_LVBus1030629_production, 53_LVBus1030630_consumption, 53_LVBus1030630_production, 53_LVBus1030631_consumption, 53_LVBus1030631_production, 53_LVBus1030632_production, 53_LVBus637054_production, 53_LVBus637055_production, 53_LVBus637057_consumption, 53_LVBus637057_production, 53_LVBus637059_production, 53_LVBus637061_production, 53_LVBus637062_production, 53_LVBus637063_production, 53_LVBus637064_production, 53_LVBus637065_consumption, 53_LVBus637065_production, 53_LVBus637066_consumption, 53_LVBus637066_production, 53_LVBus637067_production, 53_LVBus637068_production, 53_LVBus637070_production, 53_LVBus637071_production, 53_LVBus637072_production, 53_LVBus637073_production, 53_LVBus637074_production, 53_LVBus637075_production, 53_LVBus637076_production, 53_LVBus637077_production, 53_LVBus637078_production, 53_LVBus637079_consumption, 53_LVBus637079_production, 53_LVBus637080_consumption, 53_LVBus637080_production, 53_LVBus637082_production, 53_LVBus637083_production, 53_LVBus637084_consumption, 53_LVBus637084_production, 53_LVBus637085_production, 53_LVBus637086_production, 53_LVBus637087_production, 53_LVBus637088_production, 53_LVBus637089_production, 53_LVBus637090_production, 53_LVBus637091_production, 53_LVBus637093_production, 53_LVBus637094_production, 53_LVBus637095_production, 53_LVBus637097_production, 53_LVBus637098_production, 53_LVBus637099_production, 53_LVBus637100_production, 53_LVBus637102_production, 53_LVBus637103_production, 53_LVBus637105_production, 53_LVBus637106_consumption, 53_LVBus637106_production, 53_LVBus637107_production, 53_LVBus637108_consumption, 53_LVBus637108_production, 53_LVBus637109_consumption, 53_LVBus637109_production, 53_LVBus637110_production, 53_LVBus637112_production, 53_LVBus637113_consumption, 53_LVBus637113_production, 53_LVBus637114_consumption, 53_LVBus637114_production, 53_LVBus637115_consumption, 53_LVBus637115_production, 53_LVBus637117_production, 53_LVBus637118_consumption, 53_LVBus637118_production, 53_LVBus637119_consumption, 53_LVBus637119_production, 53_LVBus637120_production, 53_LVBus637122_production, 53_LVBus637123_production, 53_LVBus637124_consumption, 53_LVBus637124_production, 53_LVBus637125_production, 53_LVBus637126_consumption, 53_LVBus637126_production, 53_LVBus637128_consumption, 53_LVBus637128_production, 53_LVBus637130_consumption, 53_LVBus637130_production, 53_LVBus637131_production, 53_LVBus637132_production, 53_LVBus637133_production, 53_LVBus637134_production, 53_LVBus637135_production, 53_LVBus637136_consumption, 53_LVBus637136_production, 53_LVBus637137_production, 53_LVBus637139_production, 53_LVBus637140_production, 53_LVBus637141_production, 53_LVBus637142_production, 53_LVBus637143_production, 53_LVBus637145_production, 53_LVBus637147_production, 53_LVBus637148_consumption, 53_LVBus637148_production, 53_LVBus637149_consumption, 53_LVBus637149_production, 53_LVBus637150_production, 53_LVBus637151_production, 53_LVBus637153_production, 53_LVBus637155_production, 53_LVBus637156_production, 53_LVBus637157_production, 53_LVBus637158_consumption, 53_LVBus637158_production, 53_LVBus637159_production, 53_LVBus637160_production, 53_LVBus637161_production, 53_LVBus637162_production, 53_LVBus637163_production, 53_LVBus637164_production, 53_LVBus637165_production, 53_LVBus637166_production, 53_LVBus637167_production, 53_LVBus637169_production, 53_LVBus637170_production, 53_LVBus637171_production, 53_LVBus637175_production, 53_LVBus637176_production, 53_LVBus637177_production, 53_LVBus637179_consumption, 53_LVBus637179_production, 53_LVBus637180_production, 53_LVBus637182_production, 53_LVBus637184_production, 53_LVBus637186_production, 53_LVBus637187_production, 53_LVBus637189_production, 53_LVBus637190_production, 53_LVBus637191_consumption, 53_LVBus637191_production, 53_LVBus637192_production, 53_LVBus637194_production, 53_LVBus637195_production, 53_LVBus637196_consumption, 53_LVBus637196_production, 53_LVBus637197_production, 53_LVBus637198_production, 53_LVBus637199_production, 53_LVBus637200_production, 53_LVBus637201_production, 53_LVBus637202_production, 53_LVBus637203_production, 53_LVBus637204_production, 53_LVBus637205_production, 53_LVBus637206_consumption, 53_LVBus637206_production, 53_LVBus637207_production, 53_LVBus637209_production, 53_LVBus637210_consumption, 53_LVBus637210_production, 53_LVBus637211_production, 53_LVBus637212_consumption, 53_LVBus637212_production, 53_LVBus637213_production, 53_LVBus637215_production, 53_LVBus637216_production, 53_LVBus637217_production, 53_LVBus637219_production, 53_LVBus637220_production, 53_LVBus637221_production, 53_LVBus637223_production, 53_LVBus637224_production, 53_LVBus637225_production, 53_LVBus637227_production, 53_LVBus637228_production, 53_LVBus637229_production, 53_LVBus637230_production, 53_LVBus637231_production, 53_LVBus637232_production, 53_LVBus637233_production, 53_LVBus637235_production, 53_LVBus637236_production, 53_LVBus637237_production, 53_LVBus637240_production, 53_LVBus637241_production, 53_LVBus637242_production, 53_LVBus637243_consumption, 53_LVBus637243_production, 53_LVBus637244_production, 53_LVBus637245_consumption, 53_LVBus637245_production, 53_LVBus637247_production, 53_LVBus637248_production, 53_LVBus637249_consumption, 53_LVBus637249_production, 53_LVBus637251_production, 53_LVBus637253_production, 53_LVBus637255_production, 53_LVBus637256_consumption, 53_LVBus637256_production, 53_LVBus637257_production, 53_LVBus637258_production, 53_LVBus637259_consumption, 53_LVBus637259_production, 53_LVBus637260_production, 53_LVBus637261_production, 53_LVBus637262_production, 53_LVBus637263_production, 53_LVBus637264_production, 53_LVBus637265_production, 53_LVBus637266_production, 53_LVBus637267_production, 53_LVBus637268_production, 53_LVBus637270_production, 53_LVBus637271_production, 53_LVBus637272_production, 53_LVBus637273_production, 53_LVBus637274_production, 53_LVBus637275_production, 53_LVBus637276_production, 53_LVBus637277_production, 53_LVBus637278_consumption, 53_LVBus637278_production, 53_LVBus637279_production, 53_LVBus637280_production, 53_LVBus637281_production, 53_LVBus637282_production, 53_LVBus637283_production, 53_LVBus637285_consumption, 53_LVBus637285_production, 53_LVBus637287_consumption, 53_LVBus637287_production, 53_LVBus637288_production, 53_LVBus637289_production, 53_LVBus637290_production, 53_LVBus637291_production, 53_LVBus637293_consumption, 53_LVBus637293_production, 53_LVBus637294_production, 53_LVBus637295_production, 53_LVBus637296_consumption, 53_LVBus637296_production, 53_LVBus637297_production, 53_LVBus637299_production, 53_LVBus637301_production, 53_LVBus637302_consumption, 53_LVBus637302_production, 53_LVBus637303_production, 53_LVBus637304_production, 53_LVBus637305_production, 53_LVBus637306_production, 53_LVBus637308_production, 53_LVBus637309_production, 53_LVBus637310_consumption, 53_LVBus637310_production, 53_LVBus637311_production, 53_LVBus637312_production, 53_LVBus637314_production, 53_LVBus637316_production, 53_LVBus637317_production, 53_LVBus637319_production, 53_LVBus637320_production, 53_LVBus637321_production, 53_LVBus637322_consumption, 53_LVBus637322_production, 53_LVBus637323_production, 53_LVBus637324_consumption, 53_LVBus637324_production, 53_LVBus637325_production, 53_LVBus637326_production, 53_LVBus637328_production, 53_LVBus637329_production, 53_LVBus637330_production, 53_LVBus637331_consumption, 53_LVBus637331_production, 53_LVBus637332_production, 53_LVBus637333_production, 53_LVBus637334_consumption, 53_LVBus637334_production, 53_LVBus637339_production, 53_LVBus637340_production, 53_LVBus637341_consumption, 53_LVBus637341_production, 53_LVBus637342_production, 53_LVBus637343_production, 53_LVBus637344_consumption, 53_LVBus637344_production, 53_LVBus637345_production, 53_LVBus637347_production, 53_LVBus637348_production, 53_LVBus637349_production, 53_LVBus637350_production, 53_LVBus637351_production, 53_LVBus637353_consumption, 53_LVBus637353_production, 53_LVBus637354_production, 53_LVBus637355_production, 53_LVBus637356_production, 53_LVBus637357_production, 53_LVBus637359_production, 53_LVBus637360_production, 53_LVBus637361_production, 53_LVBus637362_production, 53_LVBus637363_production, 53_LVBus637364_production, 53_LVBus637365_production, 53_LVBus637366_production, 53_LVBus637367_production, 53_LVBus637368_production, 53_LVBus637369_production, 53_LVBus637371_production, 53_LVBus637373_production, 53_LVBus637374_production, 53_LVBus637375_production, 53_LVBus637376_production, 53_LVBus637377_production, 53_LVBus637378_production, 53_LVBus637379_production, 53_LVBus637380_production, 53_LVBus637381_production, 53_LVBus637382_production, 53_LVBus637384_production, 53_LVBus637386_consumption, 53_LVBus637386_production, 53_LVBus637388_production, 53_LVBus637389_production, 53_LVBus637390_production, 53_LVBus637392_production, 53_LVBus637393_production, 53_LVBus637395_production, 53_LVBus637396_production, 53_LVBus637397_production, 53_LVBus637398_production, 53_LVBus637399_production, 53_LVBus637401_production, 53_LVBus637402_production, 53_LVBus637403_production, 53_LVBus637404_production, 53_LVBus637405_production, 53_LVBus637406_production, 53_LVBus637407_production, 53_LVBus637408_production, 53_LVBus637409_production, 53_LVBus637411_production, 53_LVBus637412_production, 53_LVBus637413_production, 53_LVBus637415_production, 53_LVBus637416_consumption, 53_LVBus637416_production, 53_LVBus637418_production, 53_LVBus637419_production, 53_LVBus637420_production, 53_LVBus637421_production, 53_LVBus637422_production, 53_LVBus637423_production, 53_LVBus637424_consumption, 53_LVBus637424_production, 53_LVBus637425_production, 53_LVBus637427_production, 53_LVBus637429_production, 53_LVBus637430_production, 53_LVBus637432_production, 53_LVBus637434_consumption, 53_LVBus637434_production, 53_LVBus637435_consumption, 53_LVBus637435_production, 53_LVBus637436_production, 53_LVBus637438_consumption, 53_LVBus637438_production, 53_LVBus637439_production, 53_LVBus637440_production, 53_LVBus637441_consumption, 53_LVBus637441_production, 53_LVBus637442_production, 53_LVBus637443_production, 53_LVBus637444_production, 53_LVBus637445_consumption, 53_LVBus637445_production, 53_LVBus637446_consumption, 53_LVBus637446_production, 53_LVBus637447_consumption, 53_LVBus637447_production, 53_LVBus637448_consumption, 53_LVBus637448_production, 53_LVBus637449_consumption, 53_LVBus637449_production, 53_LVBus637450_production, 53_LVBus637451_production, 53_LVBus637452_production, 53_LVBus637454_consumption, 53_LVBus637454_production, 53_LVBus637455_production, 53_LVBus637456_consumption, 53_LVBus637456_production, 53_LVBus637457_production, 53_LVBus637458_production, 53_LVBus637459_production, 53_LVBus637460_consumption, 53_LVBus637460_production, 53_LVBus637461_production, 53_LVBus637462_consumption, 53_LVBus637462_production, 53_LVBus637463_production, 53_LVBus637465_production, 53_LVBus637466_consumption, 53_LVBus637466_production, 53_LVBus637467_consumption, 53_LVBus637467_production, 53_LVBus637468_production, 53_LVBus637469_production, 53_LVBus637470_production, 53_LVBus637471_production, 53_LVBus637472_production, 53_LVBus637476_production, 53_LVBus637477_production, 53_LVBus637478_consumption, 53_LVBus637478_production, 53_LVBus637479_production, 53_LVBus637480_production, 53_LVBus637481_production, 53_LVBus637483_production, 53_LVBus637484_production, 53_LVBus637485_production, 53_LVBus637486_production, 53_LVBus637487_production, 53_LVBus637488_production, 53_LVBus637490_production, 53_LVBus637491_production, 53_LVBus637492_production, 53_LVBus637493_production, 53_LVBus637494_production, 53_LVBus637496_consumption, 53_LVBus637496_production, 53_LVBus637497_production, 53_LVBus637498_production, 53_LVBus637499_production, 53_LVBus637500_production, 53_LVBus637502_consumption, 53_LVBus637502_production, 53_LVBus637503_production, 53_LVBus637504_production, 53_LVBus637505_production, 53_LVBus637506_production, 53_LVBus637507_production, 53_LVBus637508_production, 53_LVBus637509_consumption, 53_LVBus637509_production, 53_LVBus637510_production, 53_LVBus637512_consumption, 53_LVBus637512_production, 53_LVBus637513_consumption, 53_LVBus637513_production, 53_LVBus637514_production, 53_LVBus637515_production, 53_LVBus637516_consumption, 53_LVBus637516_production, 53_LVBus637517_production, 53_LVBus637519_production, 53_LVBus637520_production, 53_LVBus637521_consumption, 53_LVBus637521_production, 53_LVBus637522_production, 53_LVBus637523_production, 53_LVBus637525_production, 53_LVBus637527_production, 53_LVBus637528_consumption, 53_LVBus637528_production, 53_LVBus637529_consumption, 53_LVBus637529_production, 53_LVBus637530_production, 53_LVBus637531_production, 53_LVBus637533_consumption, 53_LVBus637533_production, 53_LVBus637534_production, 53_LVBus637535_consumption, 53_LVBus637535_production, 53_LVBus637536_consumption, 53_LVBus637536_production, 53_LVBus637538_production, 53_LVBus637539_production, 53_LVBus637540_production, 53_LVBus637542_production, 53_LVBus637543_production, 53_LVBus637544_production, 53_LVBus637546_consumption, 53_LVBus637546_production, 53_LVBus637547_production, 53_LVBus637548_consumption, 53_LVBus637548_production, 53_LVBus637549_consumption, 53_LVBus637549_production, 53_LVBus637550_production, 53_LVBus637551_consumption, 53_LVBus637551_production, 53_LVBus637552_production, 53_LVBus637553_production, 53_LVBus637554_production, 53_LVBus637557_consumption, 53_LVBus637557_production, 53_LVBus637559_production, 53_LVBus637561_production, 53_LVBus637562_production, 53_LVBus637563_production, 53_LVBus637564_production, 53_LVBus637565_consumption, 53_LVBus637565_production, 53_LVBus637567_production, 53_LVBus637568_production, 53_LVBus637569_production, 53_LVBus637570_consumption, 53_LVBus637570_production, 53_LVBus637571_production, 53_LVBus637572_production, 53_LVBus637573_production, 53_LVBus637575_production, 53_LVBus637576_production, 53_LVBus637577_production, 53_LVBus637578_production, 53_LVBus637579_production, 53_LVBus637581_production, 53_LVBus637582_production, 53_LVBus637584_production, 53_LVBus637585_production, 53_LVBus637586_consumption, 53_LVBus637586_production, 53_LVBus637588_production, 53_LVBus637590_production, 53_LVBus637591_consumption, 53_LVBus637591_production, 53_LVBus637592_production, 53_LVBus637595_production, 53_LVBus637597_production, 53_LVBus637598_production, 53_LVBus637599_production, 53_LVBus637600_production, 53_LVBus637601_production, 53_LVBus637602_production, 53_LVBus637603_production, 53_LVBus637605_consumption, 53_LVBus637605_production, 53_LVBus637606_production, 53_LVBus637607_production, 53_LVBus637608_production, 53_LVBus637610_consumption, 53_LVBus637610_production, 53_LVBus637611_production, 53_LVBus637612_production, 53_LVBus637613_consumption, 53_LVBus637613_production, 53_LVBus637614_production, 53_LVBus637615_production, 53_LVBus637616_production, 53_LVBus637618_production, 53_LVBus637619_consumption, 53_LVBus637619_production, 53_LVBus637620_consumption, 53_LVBus637620_production, 53_LVBus637621_production, 53_LVBus637622_production, 53_LVBus637623_production, 53_LVBus637624_production, 53_LVBus637625_production, 53_LVBus637626_production, 53_LVBus637627_production, 53_LVBus976921_consumption, 53_LVBus976921_production, 53_LVBus979202_production, 53_LVBus984538_consumption, 53_LVBus984538_production, 53_LVBus985464_consumption, 53_LVBus985464_production, 53_LVBus995390_production, 53_LVBus995391_production, 53_LVBus995716_production, 53_MVLV11171_consumption, 53_MVLV11171_production, 53_MVLV21471_consumption, 53_MVLV21471_production, 53_MVLV39566_consumption, 53_MVLV39566_production, 53_MVLV52046_consumption, 53_MVLV52046_production, 53_MVLV53642_consumption, 53_MVLV53642_production, 53_MVLV81384_consumption, 53_MVLV81384_production.

