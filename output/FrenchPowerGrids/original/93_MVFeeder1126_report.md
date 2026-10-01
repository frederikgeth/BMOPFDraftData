# BMOPF Network Summary: 93_MVFeeder1126

**Generated:** 2026-10-01 23:34:49  
**Findings:** 0 errors · 7 warnings · 280 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 26 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 615 |  |
| line | 588 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 1120 | 4.546 MW, 1.36 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 26 |  |
| switch | 0 |  |
| transformer | 26 | Dyn11×26 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 34 | 33 | 10 | 0 |
| LV_236V | 236.0 V | 581 | 555 | 1110 | 0 |

**Transformer transitions:**

- `93_MVLV21964_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV56771_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV61161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV04844_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV13730_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV33064_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV21909_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV33142_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV61345_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV22400_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV34918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV73033_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV32343_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV66879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV73024_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV41058_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV21590_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV32841_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV34919_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV61344_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV58370_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV65985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV21845_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV22395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV35042_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV34858_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 10 |
| Degree-1 buses | 254 |
| Tree depth (max hops) | 35 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 615 | 1 | 614 | 0 | 0 | 0 |
| Tier LV_236V | 581 | 26 | 555 | 0 | 0 | 0 |
| Tier MV_11.8kV | 34 | 1 | 33 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 26; skipped invalid branches: 0.

Galvanic zones: 27; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 93_GAP | MV_11.8kV | 34 | 0 | 0 | 26 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2426 declared bus terminals; 2319 mapped line/closed-switch conductor edges; 107 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 104000.0 | 4.405 | 3360 |
| q_nom | 0.0 | 31200.0 | 4.405 | 3360 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.75 | 1320.0 | 1.763 | 588 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.699 | 26 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 806 of 1120 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185531_consumption' has phase imbalance of 203.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185337_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185532_consumption' has phase imbalance of 85.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185611_consumption' has phase imbalance of 165.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185347_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185846_consumption' has phase imbalance of 50.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185769_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185394_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185558_consumption' has phase imbalance of 174.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185430_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185618_consumption' has phase imbalance of 159.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185448_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185563_consumption' has phase imbalance of 287.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185862_consumption' has phase imbalance of 125.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185252_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185776_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185670_consumption' has phase imbalance of 257.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185601_consumption' has phase imbalance of 190.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185449_consumption' has phase imbalance of 47.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185288_consumption' has phase imbalance of 289.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185677_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185560_consumption' has phase imbalance of 126.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185287_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185595_consumption' has phase imbalance of 259.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185816_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185634_consumption' has phase imbalance of 67.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185446_consumption' has phase imbalance of 25.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185587_consumption' has phase imbalance of 43.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185246_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185667_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185594_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185576_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185365_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185243_consumption' has phase imbalance of 142.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185418_consumption' has phase imbalance of 271.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185743_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185501_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185299_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185847_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1404762_consumption' has phase imbalance of 204.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185235_consumption' has phase imbalance of 53.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185502_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185453_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185510_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185801_consumption' has phase imbalance of 131.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185644_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185499_consumption' has phase imbalance of 199.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185581_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185367_consumption' has phase imbalance of 63.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185283_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1404763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185653_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185401_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185236_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185398_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185779_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185660_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185512_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185702_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185661_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185748_consumption' has phase imbalance of 30.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185504_consumption' has phase imbalance of 234.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185613_consumption' has phase imbalance of 79.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185772_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185421_consumption' has phase imbalance of 253.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185353_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185428_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185492_consumption' has phase imbalance of 90.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185471_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185561_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185589_consumption' has phase imbalance of 63.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185717_consumption' has phase imbalance of 97.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1372287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185494_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185488_consumption' has phase imbalance of 264.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185497_consumption' has phase imbalance of 51.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185591_consumption' has phase imbalance of 107.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185485_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185226_consumption' has phase imbalance of 128.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185329_consumption' has phase imbalance of 141.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185875_consumption' has phase imbalance of 51.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185511_consumption' has phase imbalance of 123.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185850_consumption' has phase imbalance of 74.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185620_consumption' has phase imbalance of 57.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185261_consumption' has phase imbalance of 213.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185313_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185380_consumption' has phase imbalance of 61.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185338_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185663_consumption' has phase imbalance of 25.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185635_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185405_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185559_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185500_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185749_consumption' has phase imbalance of 32.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185564_consumption' has phase imbalance of 84.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185631_consumption' has phase imbalance of 89.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185352_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185486_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185624_consumption' has phase imbalance of 47.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185757_consumption' has phase imbalance of 62.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1346872_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185372_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185770_consumption' has phase imbalance of 115.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185588_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185689_consumption' has phase imbalance of 59.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185489_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185530_consumption' has phase imbalance of 67.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185395_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185279_consumption' has phase imbalance of 37.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185393_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185525_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185739_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185518_consumption' has phase imbalance of 74.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185445_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185837_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185228_consumption' has phase imbalance of 33.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185385_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185498_consumption' has phase imbalance of 232.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185669_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185368_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185676_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185312_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185566_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185242_consumption' has phase imbalance of 124.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185371_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185615_consumption' has phase imbalance of 72.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185361_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185542_consumption' has phase imbalance of 59.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185538_consumption' has phase imbalance of 244.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185579_consumption' has phase imbalance of 107.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185383_consumption' has phase imbalance of 296.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185753_consumption' has phase imbalance of 41.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185536_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185562_consumption' has phase imbalance of 279.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1418039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1372286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185370_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185336_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185706_consumption' has phase imbalance of 37.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185523_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185694_consumption' has phase imbalance of 24.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185574_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185673_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185573_consumption' has phase imbalance of 143.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185602_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185567_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185700_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185422_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185245_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1371566_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185381_consumption' has phase imbalance of 236.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185416_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185412_consumption' has phase imbalance of 27.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185378_consumption' has phase imbalance of 210.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185265_consumption' has phase imbalance of 240.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185403_consumption' has phase imbalance of 194.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185685_consumption' has phase imbalance of 146.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185575_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185517_consumption' has phase imbalance of 78.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185598_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185258_consumption' has phase imbalance of 223.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185253_consumption' has phase imbalance of 225.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185482_consumption' has phase imbalance of 255.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185300_consumption' has phase imbalance of 118.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1346871_consumption' has phase imbalance of 268.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185547_consumption' has phase imbalance of 24.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185514_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185503_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185384_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185578_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185426_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185731_consumption' has phase imbalance of 47.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185521_consumption' has phase imbalance of 97.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185683_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185509_consumption' has phase imbalance of 133.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185526_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185767_consumption' has phase imbalance of 87.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185244_consumption' has phase imbalance of 29.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185580_consumption' has phase imbalance of 136.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185392_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1372288_consumption' has phase imbalance of 184.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185568_consumption' has phase imbalance of 104.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185495_consumption' has phase imbalance of 226.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185565_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185720_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185691_consumption' has phase imbalance of 33.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185577_consumption' has phase imbalance of 67.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185734_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185552_consumption' has phase imbalance of 80.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185835_consumption' has phase imbalance of 115.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185219_consumption' has phase imbalance of 96.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0185516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1120 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0185269' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_GAP' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0185432' has balanced aggregate load across 3 phase(s) (max spread 0.51%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '93_LVBus0185212' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.546 MW |
| Total load Q | 1.36 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 93_MVLV21964_Transformer | 275.0 kVA | 84.9% |
| 93_MVLV56771_Transformer | 440.0 kVA | 35.5% |
| 93_MVLV61161_Transformer | 110.0 kVA | 10.1% |
| 93_MVLV04844_Transformer | 440.0 kVA | 40.4% |
| 93_MVLV13730_Transformer | 176.0 kVA | 36.1% |
| 93_MVLV33064_Transformer | 440.0 kVA | 76.1% |
| 93_MVLV21909_Transformer | 275.0 kVA | 93.5% ⚠ |
| 93_MVLV33142_Transformer | 176.0 kVA | 82.7% |
| 93_MVLV61345_Transformer | 275.0 kVA | 91.3% ⚠ |
| 93_MVLV22400_Transformer | 440.0 kVA | 34.5% |
| 93_MVLV34918_Transformer | 176.0 kVA | 76.1% |
| 93_MVLV73033_Transformer | 176.0 kVA | 0.0% |
| 93_MVLV32343_Transformer | 176.0 kVA | 37.8% |
| 93_MVLV66879_Transformer | 110.0 kVA | 12.4% |
| 93_MVLV73024_Transformer | 110.0 kVA | 13.8% |
| 93_MVLV41058_Transformer | 275.0 kVA | 49.3% |
| 93_MVLV21590_Transformer | 275.0 kVA | 61.8% |
| 93_MVLV32841_Transformer | 693.0 kVA | 39.6% |
| 93_MVLV34919_Transformer | 275.0 kVA | 49.1% |
| 93_MVLV61344_Transformer | 275.0 kVA | 87.3% |
| 93_MVLV58370_Transformer | 1.1 MVA | 50.4% |
| 93_MVLV65985_Transformer | 176.0 kVA | 0.0% |
| 93_MVLV21845_Transformer | 275.0 kVA | 33.3% |
| 93_MVLV22395_Transformer | 176.0 kVA | 84.3% |
| 93_MVLV35042_Transformer | 693.0 kVA | 45.2% |
| 93_MVLV34858_Transformer | 275.0 kVA | 66.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.55 MW).
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '93_MVLV21909_Transformer' is at 93.5% utilisation at nominal load — little OPF headroom.
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '93_MVLV61345_Transformer' is at 91.3% utilisation at nominal load — little OPF headroom.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '93_LVBus0185883' (LV, 0.24 kV) has an electrical reach of 2.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '93_LVBus0185852' (LV, 0.24 kV) has an electrical reach of 22.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 615 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 615 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 26 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 34 |
| LV_236V | 4-wire | 581 / 581 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 581 |
| Neutral branches | 555 |
| Grounding points | 26 |
| Neutral sections | 26 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| exactly_balanced | 1 |
| decoupled | 2 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 4 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 34 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 55 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 41 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 55 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 27 |
| Islands without voltage reference | 0 |
| Line impedance spread | 322.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 581 / 34 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 807 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 807 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0185212_production, 93_LVBus0185214_production, 93_LVBus0185216_production, 93_LVBus0185218_consumption, 93_LVBus0185218_production, 93_LVBus0185219_production, 93_LVBus0185221_consumption, 93_LVBus0185221_production, 93_LVBus0185222_consumption, 93_LVBus0185222_production, 93_LVBus0185223_consumption, 93_LVBus0185223_production, 93_LVBus0185224_consumption, 93_LVBus0185224_production, 93_LVBus0185225_consumption, 93_LVBus0185225_production, 93_LVBus0185226_production, 93_LVBus0185228_production, 93_LVBus0185230_consumption, 93_LVBus0185230_production, 93_LVBus0185231_production, 93_LVBus0185232_consumption, 93_LVBus0185232_production, 93_LVBus0185233_consumption, 93_LVBus0185233_production, 93_LVBus0185234_consumption, 93_LVBus0185234_production, 93_LVBus0185235_production, 93_LVBus0185236_production, 93_LVBus0185237_consumption, 93_LVBus0185237_production, 93_LVBus0185238_consumption, 93_LVBus0185238_production, 93_LVBus0185240_consumption, 93_LVBus0185240_production, 93_LVBus0185242_production, 93_LVBus0185243_production, 93_LVBus0185244_production, 93_LVBus0185245_production, 93_LVBus0185246_production, 93_LVBus0185248_consumption, 93_LVBus0185248_production, 93_LVBus0185250_consumption, 93_LVBus0185250_production, 93_LVBus0185251_consumption, 93_LVBus0185251_production, 93_LVBus0185252_production, 93_LVBus0185253_production, 93_LVBus0185254_consumption, 93_LVBus0185254_production, 93_LVBus0185255_production, 93_LVBus0185256_consumption, 93_LVBus0185256_production, 93_LVBus0185257_production, 93_LVBus0185258_production, 93_LVBus0185259_production, 93_LVBus0185260_consumption, 93_LVBus0185260_production, 93_LVBus0185261_production, 93_LVBus0185262_consumption, 93_LVBus0185262_production, 93_LVBus0185263_production, 93_LVBus0185264_production, 93_LVBus0185265_production, 93_LVBus0185267_production, 93_LVBus0185269_production, 93_LVBus0185271_production, 93_LVBus0185272_production, 93_LVBus0185273_production, 93_LVBus0185275_production, 93_LVBus0185277_production, 93_LVBus0185279_production, 93_LVBus0185281_consumption, 93_LVBus0185281_production, 93_LVBus0185282_production, 93_LVBus0185283_production, 93_LVBus0185284_production, 93_LVBus0185285_consumption, 93_LVBus0185285_production, 93_LVBus0185286_production, 93_LVBus0185287_production, 93_LVBus0185288_production, 93_LVBus0185289_production, 93_LVBus0185291_consumption, 93_LVBus0185291_production, 93_LVBus0185292_consumption, 93_LVBus0185292_production, 93_LVBus0185293_consumption, 93_LVBus0185293_production, 93_LVBus0185295_consumption, 93_LVBus0185295_production, 93_LVBus0185296_consumption, 93_LVBus0185296_production, 93_LVBus0185297_consumption, 93_LVBus0185297_production, 93_LVBus0185298_consumption, 93_LVBus0185298_production, 93_LVBus0185299_production, 93_LVBus0185300_production, 93_LVBus0185301_production, 93_LVBus0185302_production, 93_LVBus0185303_consumption, 93_LVBus0185303_production, 93_LVBus0185304_consumption, 93_LVBus0185304_production, 93_LVBus0185305_consumption, 93_LVBus0185305_production, 93_LVBus0185306_consumption, 93_LVBus0185306_production, 93_LVBus0185307_production, 93_LVBus0185309_consumption, 93_LVBus0185309_production, 93_LVBus0185310_consumption, 93_LVBus0185310_production, 93_LVBus0185311_consumption, 93_LVBus0185311_production, 93_LVBus0185312_production, 93_LVBus0185313_production, 93_LVBus0185314_consumption, 93_LVBus0185314_production, 93_LVBus0185316_consumption, 93_LVBus0185316_production, 93_LVBus0185317_consumption, 93_LVBus0185317_production, 93_LVBus0185318_consumption, 93_LVBus0185318_production, 93_LVBus0185319_consumption, 93_LVBus0185319_production, 93_LVBus0185320_consumption, 93_LVBus0185320_production, 93_LVBus0185321_consumption, 93_LVBus0185321_production, 93_LVBus0185323_consumption, 93_LVBus0185323_production, 93_LVBus0185324_consumption, 93_LVBus0185324_production, 93_LVBus0185325_consumption, 93_LVBus0185325_production, 93_LVBus0185326_consumption, 93_LVBus0185326_production, 93_LVBus0185327_consumption, 93_LVBus0185327_production, 93_LVBus0185328_consumption, 93_LVBus0185328_production, 93_LVBus0185329_production, 93_LVBus0185330_consumption, 93_LVBus0185330_production, 93_LVBus0185332_consumption, 93_LVBus0185332_production, 93_LVBus0185334_consumption, 93_LVBus0185334_production, 93_LVBus0185335_consumption, 93_LVBus0185335_production, 93_LVBus0185336_production, 93_LVBus0185337_production, 93_LVBus0185338_production, 93_LVBus0185339_production, 93_LVBus0185340_production, 93_LVBus0185342_consumption, 93_LVBus0185342_production, 93_LVBus0185343_consumption, 93_LVBus0185343_production, 93_LVBus0185344_consumption, 93_LVBus0185344_production, 93_LVBus0185345_consumption, 93_LVBus0185345_production, 93_LVBus0185346_consumption, 93_LVBus0185346_production, 93_LVBus0185347_production, 93_LVBus0185348_consumption, 93_LVBus0185348_production, 93_LVBus0185350_consumption, 93_LVBus0185350_production, 93_LVBus0185352_production, 93_LVBus0185353_production, 93_LVBus0185354_production, 93_LVBus0185356_production, 93_LVBus0185358_consumption, 93_LVBus0185358_production, 93_LVBus0185359_production, 93_LVBus0185360_production, 93_LVBus0185361_production, 93_LVBus0185362_consumption, 93_LVBus0185362_production, 93_LVBus0185363_consumption, 93_LVBus0185363_production, 93_LVBus0185364_production, 93_LVBus0185365_production, 93_LVBus0185366_consumption, 93_LVBus0185366_production, 93_LVBus0185367_production, 93_LVBus0185368_production, 93_LVBus0185370_production, 93_LVBus0185371_production, 93_LVBus0185372_production, 93_LVBus0185373_production, 93_LVBus0185374_consumption, 93_LVBus0185374_production, 93_LVBus0185375_production, 93_LVBus0185376_production, 93_LVBus0185377_production, 93_LVBus0185378_production, 93_LVBus0185379_consumption, 93_LVBus0185379_production, 93_LVBus0185380_production, 93_LVBus0185381_production, 93_LVBus0185382_consumption, 93_LVBus0185382_production, 93_LVBus0185383_production, 93_LVBus0185384_production, 93_LVBus0185385_production, 93_LVBus0185386_production, 93_LVBus0185388_consumption, 93_LVBus0185388_production, 93_LVBus0185389_production, 93_LVBus0185390_consumption, 93_LVBus0185390_production, 93_LVBus0185391_production, 93_LVBus0185392_production, 93_LVBus0185393_production, 93_LVBus0185394_production, 93_LVBus0185395_production, 93_LVBus0185397_production, 93_LVBus0185398_production, 93_LVBus0185399_consumption, 93_LVBus0185399_production, 93_LVBus0185400_production, 93_LVBus0185401_production, 93_LVBus0185402_consumption, 93_LVBus0185402_production, 93_LVBus0185403_production, 93_LVBus0185404_production, 93_LVBus0185405_production, 93_LVBus0185406_consumption, 93_LVBus0185406_production, 93_LVBus0185408_consumption, 93_LVBus0185408_production, 93_LVBus0185409_consumption, 93_LVBus0185409_production, 93_LVBus0185410_consumption, 93_LVBus0185410_production, 93_LVBus0185411_consumption, 93_LVBus0185411_production, 93_LVBus0185412_production, 93_LVBus0185414_consumption, 93_LVBus0185414_production, 93_LVBus0185416_production, 93_LVBus0185417_consumption, 93_LVBus0185417_production, 93_LVBus0185418_production, 93_LVBus0185419_production, 93_LVBus0185420_production, 93_LVBus0185421_production, 93_LVBus0185422_production, 93_LVBus0185423_production, 93_LVBus0185424_production, 93_LVBus0185425_consumption, 93_LVBus0185425_production, 93_LVBus0185426_production, 93_LVBus0185428_production, 93_LVBus0185429_production, 93_LVBus0185430_production, 93_LVBus0185432_consumption, 93_LVBus0185432_production, 93_LVBus0185433_production, 93_LVBus0185435_production, 93_LVBus0185436_consumption, 93_LVBus0185436_production, 93_LVBus0185437_production, 93_LVBus0185439_production, 93_LVBus0185440_production, 93_LVBus0185441_consumption, 93_LVBus0185441_production, 93_LVBus0185442_production, 93_LVBus0185443_production, 93_LVBus0185445_production, 93_LVBus0185446_production, 93_LVBus0185448_production, 93_LVBus0185449_production, 93_LVBus0185450_production, 93_LVBus0185452_consumption, 93_LVBus0185452_production, 93_LVBus0185453_production, 93_LVBus0185455_consumption, 93_LVBus0185455_production, 93_LVBus0185456_consumption, 93_LVBus0185456_production, 93_LVBus0185457_consumption, 93_LVBus0185457_production, 93_LVBus0185458_production, 93_LVBus0185459_consumption, 93_LVBus0185459_production, 93_LVBus0185461_consumption, 93_LVBus0185461_production, 93_LVBus0185463_production, 93_LVBus0185465_consumption, 93_LVBus0185465_production, 93_LVBus0185467_production, 93_LVBus0185468_consumption, 93_LVBus0185468_production, 93_LVBus0185470_consumption, 93_LVBus0185470_production, 93_LVBus0185471_production, 93_LVBus0185473_consumption, 93_LVBus0185473_production, 93_LVBus0185475_consumption, 93_LVBus0185475_production, 93_LVBus0185476_consumption, 93_LVBus0185476_production, 93_LVBus0185477_consumption, 93_LVBus0185477_production, 93_LVBus0185479_consumption, 93_LVBus0185479_production, 93_LVBus0185480_production, 93_LVBus0185482_production, 93_LVBus0185483_production, 93_LVBus0185485_production, 93_LVBus0185486_production, 93_LVBus0185487_production, 93_LVBus0185488_production, 93_LVBus0185489_production, 93_LVBus0185490_production, 93_LVBus0185492_production, 93_LVBus0185493_consumption, 93_LVBus0185493_production, 93_LVBus0185494_production, 93_LVBus0185495_production, 93_LVBus0185496_production, 93_LVBus0185497_production, 93_LVBus0185498_production, 93_LVBus0185499_production, 93_LVBus0185500_production, 93_LVBus0185501_production, 93_LVBus0185502_production, 93_LVBus0185503_production, 93_LVBus0185504_production, 93_LVBus0185506_production, 93_LVBus0185507_consumption, 93_LVBus0185507_production, 93_LVBus0185508_consumption, 93_LVBus0185508_production, 93_LVBus0185509_production, 93_LVBus0185510_production, 93_LVBus0185511_production, 93_LVBus0185512_production, 93_LVBus0185513_consumption, 93_LVBus0185513_production, 93_LVBus0185514_production, 93_LVBus0185515_consumption, 93_LVBus0185515_production, 93_LVBus0185516_production, 93_LVBus0185517_production, 93_LVBus0185518_production, 93_LVBus0185519_production, 93_LVBus0185521_production, 93_LVBus0185523_production, 93_LVBus0185524_production, 93_LVBus0185525_production, 93_LVBus0185526_production, 93_LVBus0185527_consumption, 93_LVBus0185527_production, 93_LVBus0185529_consumption, 93_LVBus0185529_production, 93_LVBus0185530_production, 93_LVBus0185531_production, 93_LVBus0185532_production, 93_LVBus0185534_consumption, 93_LVBus0185534_production, 93_LVBus0185535_consumption, 93_LVBus0185535_production, 93_LVBus0185536_production, 93_LVBus0185537_consumption, 93_LVBus0185537_production, 93_LVBus0185538_production, 93_LVBus0185539_consumption, 93_LVBus0185539_production, 93_LVBus0185540_production, 93_LVBus0185541_consumption, 93_LVBus0185541_production, 93_LVBus0185542_production, 93_LVBus0185544_consumption, 93_LVBus0185544_production, 93_LVBus0185546_consumption, 93_LVBus0185546_production, 93_LVBus0185547_production, 93_LVBus0185549_consumption, 93_LVBus0185549_production, 93_LVBus0185551_consumption, 93_LVBus0185551_production, 93_LVBus0185552_production, 93_LVBus0185554_consumption, 93_LVBus0185554_production, 93_LVBus0185555_consumption, 93_LVBus0185555_production, 93_LVBus0185557_consumption, 93_LVBus0185557_production, 93_LVBus0185558_production, 93_LVBus0185559_production, 93_LVBus0185560_production, 93_LVBus0185561_production, 93_LVBus0185562_production, 93_LVBus0185563_production, 93_LVBus0185564_production, 93_LVBus0185565_production, 93_LVBus0185566_production, 93_LVBus0185567_production, 93_LVBus0185568_production, 93_LVBus0185570_production, 93_LVBus0185571_consumption, 93_LVBus0185571_production, 93_LVBus0185572_consumption, 93_LVBus0185572_production, 93_LVBus0185573_production, 93_LVBus0185574_production, 93_LVBus0185575_production, 93_LVBus0185576_production, 93_LVBus0185577_production, 93_LVBus0185578_production, 93_LVBus0185579_production, 93_LVBus0185580_production, 93_LVBus0185581_production, 93_LVBus0185582_production, 93_LVBus0185583_production, 93_LVBus0185585_production, 93_LVBus0185586_consumption, 93_LVBus0185586_production, 93_LVBus0185587_production, 93_LVBus0185588_production, 93_LVBus0185589_production, 93_LVBus0185591_production, 93_LVBus0185592_production, 93_LVBus0185594_production, 93_LVBus0185595_production, 93_LVBus0185596_production, 93_LVBus0185597_consumption, 93_LVBus0185597_production, 93_LVBus0185598_production, 93_LVBus0185600_production, 93_LVBus0185601_production, 93_LVBus0185602_production, 93_LVBus0185603_consumption, 93_LVBus0185603_production, 93_LVBus0185604_production, 93_LVBus0185605_production, 93_LVBus0185606_production, 93_LVBus0185607_production, 93_LVBus0185608_production, 93_LVBus0185609_consumption, 93_LVBus0185609_production, 93_LVBus0185610_consumption, 93_LVBus0185610_production, 93_LVBus0185611_production, 93_LVBus0185613_production, 93_LVBus0185614_consumption, 93_LVBus0185614_production, 93_LVBus0185615_production, 93_LVBus0185616_production, 93_LVBus0185618_production, 93_LVBus0185619_production, 93_LVBus0185620_production, 93_LVBus0185621_consumption, 93_LVBus0185621_production, 93_LVBus0185622_production, 93_LVBus0185623_consumption, 93_LVBus0185623_production, 93_LVBus0185624_production, 93_LVBus0185625_production, 93_LVBus0185627_consumption, 93_LVBus0185627_production, 93_LVBus0185628_consumption, 93_LVBus0185628_production, 93_LVBus0185630_consumption, 93_LVBus0185630_production, 93_LVBus0185631_production, 93_LVBus0185633_consumption, 93_LVBus0185633_production, 93_LVBus0185634_production, 93_LVBus0185635_production, 93_LVBus0185637_consumption, 93_LVBus0185637_production, 93_LVBus0185638_production, 93_LVBus0185639_production, 93_LVBus0185641_consumption, 93_LVBus0185641_production, 93_LVBus0185642_production, 93_LVBus0185643_consumption, 93_LVBus0185643_production, 93_LVBus0185644_production, 93_LVBus0185646_production, 93_LVBus0185648_production, 93_LVBus0185650_production, 93_LVBus0185652_consumption, 93_LVBus0185652_production, 93_LVBus0185653_production, 93_LVBus0185654_production, 93_LVBus0185655_production, 93_LVBus0185656_production, 93_LVBus0185657_production, 93_LVBus0185658_consumption, 93_LVBus0185658_production, 93_LVBus0185659_consumption, 93_LVBus0185659_production, 93_LVBus0185660_production, 93_LVBus0185661_production, 93_LVBus0185662_consumption, 93_LVBus0185662_production, 93_LVBus0185663_production, 93_LVBus0185664_consumption, 93_LVBus0185664_production, 93_LVBus0185665_consumption, 93_LVBus0185665_production, 93_LVBus0185666_consumption, 93_LVBus0185666_production, 93_LVBus0185667_production, 93_LVBus0185668_consumption, 93_LVBus0185668_production, 93_LVBus0185669_production, 93_LVBus0185670_production, 93_LVBus0185671_production, 93_LVBus0185672_consumption, 93_LVBus0185672_production, 93_LVBus0185673_production, 93_LVBus0185675_consumption, 93_LVBus0185675_production, 93_LVBus0185676_production, 93_LVBus0185677_production, 93_LVBus0185678_production, 93_LVBus0185679_consumption, 93_LVBus0185679_production, 93_LVBus0185681_consumption, 93_LVBus0185681_production, 93_LVBus0185682_consumption, 93_LVBus0185682_production, 93_LVBus0185683_production, 93_LVBus0185684_consumption, 93_LVBus0185684_production, 93_LVBus0185685_production, 93_LVBus0185686_production, 93_LVBus0185687_consumption, 93_LVBus0185687_production, 93_LVBus0185688_consumption, 93_LVBus0185688_production, 93_LVBus0185689_production, 93_LVBus0185690_consumption, 93_LVBus0185690_production, 93_LVBus0185691_production, 93_LVBus0185692_consumption, 93_LVBus0185692_production, 93_LVBus0185694_production, 93_LVBus0185696_consumption, 93_LVBus0185696_production, 93_LVBus0185698_production, 93_LVBus0185700_production, 93_LVBus0185701_consumption, 93_LVBus0185701_production, 93_LVBus0185702_production, 93_LVBus0185703_production, 93_LVBus0185704_consumption, 93_LVBus0185704_production, 93_LVBus0185705_consumption, 93_LVBus0185705_production, 93_LVBus0185706_production, 93_LVBus0185707_consumption, 93_LVBus0185707_production, 93_LVBus0185708_production, 93_LVBus0185709_consumption, 93_LVBus0185709_production, 93_LVBus0185711_consumption, 93_LVBus0185711_production, 93_LVBus0185712_production, 93_LVBus0185713_consumption, 93_LVBus0185713_production, 93_LVBus0185714_consumption, 93_LVBus0185714_production, 93_LVBus0185715_consumption, 93_LVBus0185715_production, 93_LVBus0185716_production, 93_LVBus0185717_production, 93_LVBus0185718_production, 93_LVBus0185719_production, 93_LVBus0185720_production, 93_LVBus0185721_production, 93_LVBus0185722_production, 93_LVBus0185724_consumption, 93_LVBus0185724_production, 93_LVBus0185726_consumption, 93_LVBus0185726_production, 93_LVBus0185727_consumption, 93_LVBus0185727_production, 93_LVBus0185728_consumption, 93_LVBus0185728_production, 93_LVBus0185729_consumption, 93_LVBus0185729_production, 93_LVBus0185730_consumption, 93_LVBus0185730_production, 93_LVBus0185731_production, 93_LVBus0185732_production, 93_LVBus0185733_consumption, 93_LVBus0185733_production, 93_LVBus0185734_production, 93_LVBus0185736_production, 93_LVBus0185737_consumption, 93_LVBus0185737_production, 93_LVBus0185738_consumption, 93_LVBus0185738_production, 93_LVBus0185739_production, 93_LVBus0185741_consumption, 93_LVBus0185741_production, 93_LVBus0185742_production, 93_LVBus0185743_production, 93_LVBus0185744_production, 93_LVBus0185745_production, 93_LVBus0185747_consumption, 93_LVBus0185747_production, 93_LVBus0185748_production, 93_LVBus0185749_production, 93_LVBus0185751_consumption, 93_LVBus0185751_production, 93_LVBus0185753_production, 93_LVBus0185755_consumption, 93_LVBus0185755_production, 93_LVBus0185756_consumption, 93_LVBus0185756_production, 93_LVBus0185757_production, 93_LVBus0185759_consumption, 93_LVBus0185759_production, 93_LVBus0185760_consumption, 93_LVBus0185760_production, 93_LVBus0185761_consumption, 93_LVBus0185761_production, 93_LVBus0185762_consumption, 93_LVBus0185762_production, 93_LVBus0185763_production, 93_LVBus0185764_production, 93_LVBus0185765_production, 93_LVBus0185766_consumption, 93_LVBus0185766_production, 93_LVBus0185767_production, 93_LVBus0185768_consumption, 93_LVBus0185768_production, 93_LVBus0185769_production, 93_LVBus0185770_production, 93_LVBus0185771_consumption, 93_LVBus0185771_production, 93_LVBus0185772_production, 93_LVBus0185773_production, 93_LVBus0185775_production, 93_LVBus0185776_production, 93_LVBus0185778_consumption, 93_LVBus0185778_production, 93_LVBus0185779_production, 93_LVBus0185781_consumption, 93_LVBus0185781_production, 93_LVBus0185782_consumption, 93_LVBus0185782_production, 93_LVBus0185783_consumption, 93_LVBus0185783_production, 93_LVBus0185784_consumption, 93_LVBus0185784_production, 93_LVBus0185786_consumption, 93_LVBus0185786_production, 93_LVBus0185788_consumption, 93_LVBus0185788_production, 93_LVBus0185789_consumption, 93_LVBus0185789_production, 93_LVBus0185790_consumption, 93_LVBus0185790_production, 93_LVBus0185791_consumption, 93_LVBus0185791_production, 93_LVBus0185792_consumption, 93_LVBus0185792_production, 93_LVBus0185793_consumption, 93_LVBus0185793_production, 93_LVBus0185794_consumption, 93_LVBus0185794_production, 93_LVBus0185795_consumption, 93_LVBus0185795_production, 93_LVBus0185796_consumption, 93_LVBus0185796_production, 93_LVBus0185797_consumption, 93_LVBus0185797_production, 93_LVBus0185798_consumption, 93_LVBus0185798_production, 93_LVBus0185800_consumption, 93_LVBus0185800_production, 93_LVBus0185801_production, 93_LVBus0185802_consumption, 93_LVBus0185802_production, 93_LVBus0185803_consumption, 93_LVBus0185803_production, 93_LVBus0185804_consumption, 93_LVBus0185804_production, 93_LVBus0185805_consumption, 93_LVBus0185805_production, 93_LVBus0185806_consumption, 93_LVBus0185806_production, 93_LVBus0185809_consumption, 93_LVBus0185809_production, 93_LVBus0185810_consumption, 93_LVBus0185810_production, 93_LVBus0185811_consumption, 93_LVBus0185811_production, 93_LVBus0185812_consumption, 93_LVBus0185812_production, 93_LVBus0185813_production, 93_LVBus0185815_consumption, 93_LVBus0185815_production, 93_LVBus0185816_production, 93_LVBus0185818_consumption, 93_LVBus0185818_production, 93_LVBus0185820_consumption, 93_LVBus0185820_production, 93_LVBus0185821_consumption, 93_LVBus0185821_production, 93_LVBus0185823_production, 93_LVBus0185825_consumption, 93_LVBus0185825_production, 93_LVBus0185826_consumption, 93_LVBus0185826_production, 93_LVBus0185828_consumption, 93_LVBus0185828_production, 93_LVBus0185830_consumption, 93_LVBus0185830_production, 93_LVBus0185831_consumption, 93_LVBus0185831_production, 93_LVBus0185835_production, 93_LVBus0185837_production, 93_LVBus0185839_consumption, 93_LVBus0185839_production, 93_LVBus0185841_production, 93_LVBus0185842_consumption, 93_LVBus0185842_production, 93_LVBus0185843_consumption, 93_LVBus0185843_production, 93_LVBus0185844_production, 93_LVBus0185845_consumption, 93_LVBus0185845_production, 93_LVBus0185846_production, 93_LVBus0185847_production, 93_LVBus0185848_production, 93_LVBus0185850_production, 93_LVBus0185852_consumption, 93_LVBus0185852_production, 93_LVBus0185854_consumption, 93_LVBus0185854_production, 93_LVBus0185856_consumption, 93_LVBus0185856_production, 93_LVBus0185858_consumption, 93_LVBus0185858_production, 93_LVBus0185860_consumption, 93_LVBus0185860_production, 93_LVBus0185861_consumption, 93_LVBus0185861_production, 93_LVBus0185862_production, 93_LVBus0185865_consumption, 93_LVBus0185865_production, 93_LVBus0185866_consumption, 93_LVBus0185866_production, 93_LVBus0185868_consumption, 93_LVBus0185868_production, 93_LVBus0185870_consumption, 93_LVBus0185870_production, 93_LVBus0185872_consumption, 93_LVBus0185872_production, 93_LVBus0185874_consumption, 93_LVBus0185874_production, 93_LVBus0185875_production, 93_LVBus0185877_consumption, 93_LVBus0185877_production, 93_LVBus0185878_consumption, 93_LVBus0185878_production, 93_LVBus0185880_consumption, 93_LVBus0185880_production, 93_LVBus0185881_consumption, 93_LVBus0185881_production, 93_LVBus0185883_consumption, 93_LVBus0185883_production, 93_LVBus1346871_production, 93_LVBus1346872_production, 93_LVBus1371565_consumption, 93_LVBus1371565_production, 93_LVBus1371566_production, 93_LVBus1372286_production, 93_LVBus1372287_production, 93_LVBus1372288_production, 93_LVBus1375062_consumption, 93_LVBus1375062_production, 93_LVBus1375063_consumption, 93_LVBus1375063_production, 93_LVBus1375064_production, 93_LVBus1402525_consumption, 93_LVBus1402525_production, 93_LVBus1404761_consumption, 93_LVBus1404761_production, 93_LVBus1404762_production, 93_LVBus1404763_production, 93_LVBus1418038_consumption, 93_LVBus1418038_production, 93_LVBus1418039_production, 93_MVLV19541_consumption, 93_MVLV19541_production, 93_MVLV33393_production, 93_MVLV41378_consumption, 93_MVLV41378_production, 93_MVLV42522_consumption, 93_MVLV42522_production, 93_MVLV62909_production.

## 9. Data Quality Summary

**Total findings:** 287 (0 errors, 7 warnings, 280 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  806 of 1120 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.55 MW).
- **[W.OPS.XFMR_OVERLOADED]** `93_MVLV21909_Transformer`  
  Transformer '93_MVLV21909_Transformer' is at 93.5% utilisation at nominal load — little OPF headroom.
- **[W.OPS.XFMR_OVERLOADED]** `93_MVLV61345_Transformer`  
  Transformer '93_MVLV61345_Transformer' is at 91.3% utilisation at nominal load — little OPF headroom.
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  807 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185531_consumption`  
  Load '93_LVBus0185531_consumption' has phase imbalance of 203.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185231_consumption`  
  Load '93_LVBus0185231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185337_consumption`  
  Load '93_LVBus0185337_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185532_consumption`  
  Load '93_LVBus0185532_consumption' has phase imbalance of 85.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185611_consumption`  
  Load '93_LVBus0185611_consumption' has phase imbalance of 165.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185347_consumption`  
  Load '93_LVBus0185347_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185764_consumption`  
  Load '93_LVBus0185764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185386_consumption`  
  Load '93_LVBus0185386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185846_consumption`  
  Load '93_LVBus0185846_consumption' has phase imbalance of 50.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185490_consumption`  
  Load '93_LVBus0185490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185769_consumption`  
  Load '93_LVBus0185769_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185394_consumption`  
  Load '93_LVBus0185394_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185558_consumption`  
  Load '93_LVBus0185558_consumption' has phase imbalance of 174.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185430_consumption`  
  Load '93_LVBus0185430_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185618_consumption`  
  Load '93_LVBus0185618_consumption' has phase imbalance of 159.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185448_consumption`  
  Load '93_LVBus0185448_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185563_consumption`  
  Load '93_LVBus0185563_consumption' has phase imbalance of 287.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185862_consumption`  
  Load '93_LVBus0185862_consumption' has phase imbalance of 125.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185282_consumption`  
  Load '93_LVBus0185282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185252_consumption`  
  Load '93_LVBus0185252_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185744_consumption`  
  Load '93_LVBus0185744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185776_consumption`  
  Load '93_LVBus0185776_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185670_consumption`  
  Load '93_LVBus0185670_consumption' has phase imbalance of 257.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185585_consumption`  
  Load '93_LVBus0185585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185601_consumption`  
  Load '93_LVBus0185601_consumption' has phase imbalance of 190.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185449_consumption`  
  Load '93_LVBus0185449_consumption' has phase imbalance of 47.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185524_consumption`  
  Load '93_LVBus0185524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185288_consumption`  
  Load '93_LVBus0185288_consumption' has phase imbalance of 289.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185677_consumption`  
  Load '93_LVBus0185677_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185608_consumption`  
  Load '93_LVBus0185608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185560_consumption`  
  Load '93_LVBus0185560_consumption' has phase imbalance of 126.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185287_consumption`  
  Load '93_LVBus0185287_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185595_consumption`  
  Load '93_LVBus0185595_consumption' has phase imbalance of 259.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185606_consumption`  
  Load '93_LVBus0185606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185816_consumption`  
  Load '93_LVBus0185816_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185634_consumption`  
  Load '93_LVBus0185634_consumption' has phase imbalance of 67.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185446_consumption`  
  Load '93_LVBus0185446_consumption' has phase imbalance of 25.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185587_consumption`  
  Load '93_LVBus0185587_consumption' has phase imbalance of 43.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185721_consumption`  
  Load '93_LVBus0185721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185246_consumption`  
  Load '93_LVBus0185246_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185667_consumption`  
  Load '93_LVBus0185667_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185594_consumption`  
  Load '93_LVBus0185594_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185360_consumption`  
  Load '93_LVBus0185360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185576_consumption`  
  Load '93_LVBus0185576_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185365_consumption`  
  Load '93_LVBus0185365_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185243_consumption`  
  Load '93_LVBus0185243_consumption' has phase imbalance of 142.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185418_consumption`  
  Load '93_LVBus0185418_consumption' has phase imbalance of 271.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185743_consumption`  
  Load '93_LVBus0185743_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185596_consumption`  
  Load '93_LVBus0185596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185389_consumption`  
  Load '93_LVBus0185389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185501_consumption`  
  Load '93_LVBus0185501_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185429_consumption`  
  Load '93_LVBus0185429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185299_consumption`  
  Load '93_LVBus0185299_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185646_consumption`  
  Load '93_LVBus0185646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185847_consumption`  
  Load '93_LVBus0185847_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1404762_consumption`  
  Load '93_LVBus1404762_consumption' has phase imbalance of 204.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185235_consumption`  
  Load '93_LVBus0185235_consumption' has phase imbalance of 53.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185502_consumption`  
  Load '93_LVBus0185502_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185453_consumption`  
  Load '93_LVBus0185453_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185510_consumption`  
  Load '93_LVBus0185510_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185801_consumption`  
  Load '93_LVBus0185801_consumption' has phase imbalance of 131.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185644_consumption`  
  Load '93_LVBus0185644_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185450_consumption`  
  Load '93_LVBus0185450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185499_consumption`  
  Load '93_LVBus0185499_consumption' has phase imbalance of 199.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185581_consumption`  
  Load '93_LVBus0185581_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185367_consumption`  
  Load '93_LVBus0185367_consumption' has phase imbalance of 63.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185582_consumption`  
  Load '93_LVBus0185582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185848_consumption`  
  Load '93_LVBus0185848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185283_consumption`  
  Load '93_LVBus0185283_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1404763_consumption`  
  Load '93_LVBus1404763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185653_consumption`  
  Load '93_LVBus0185653_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185401_consumption`  
  Load '93_LVBus0185401_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185671_consumption`  
  Load '93_LVBus0185671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185236_consumption`  
  Load '93_LVBus0185236_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185398_consumption`  
  Load '93_LVBus0185398_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185779_consumption`  
  Load '93_LVBus0185779_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185570_consumption`  
  Load '93_LVBus0185570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185419_consumption`  
  Load '93_LVBus0185419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185660_consumption`  
  Load '93_LVBus0185660_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185512_consumption`  
  Load '93_LVBus0185512_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185702_consumption`  
  Load '93_LVBus0185702_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185661_consumption`  
  Load '93_LVBus0185661_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185423_consumption`  
  Load '93_LVBus0185423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185748_consumption`  
  Load '93_LVBus0185748_consumption' has phase imbalance of 30.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185504_consumption`  
  Load '93_LVBus0185504_consumption' has phase imbalance of 234.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185286_consumption`  
  Load '93_LVBus0185286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185583_consumption`  
  Load '93_LVBus0185583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185765_consumption`  
  Load '93_LVBus0185765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185613_consumption`  
  Load '93_LVBus0185613_consumption' has phase imbalance of 79.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185359_consumption`  
  Load '93_LVBus0185359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185772_consumption`  
  Load '93_LVBus0185772_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185421_consumption`  
  Load '93_LVBus0185421_consumption' has phase imbalance of 253.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185353_consumption`  
  Load '93_LVBus0185353_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185775_consumption`  
  Load '93_LVBus0185775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185397_consumption`  
  Load '93_LVBus0185397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185428_consumption`  
  Load '93_LVBus0185428_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185492_consumption`  
  Load '93_LVBus0185492_consumption' has phase imbalance of 90.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185471_consumption`  
  Load '93_LVBus0185471_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185561_consumption`  
  Load '93_LVBus0185561_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185589_consumption`  
  Load '93_LVBus0185589_consumption' has phase imbalance of 63.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185717_consumption`  
  Load '93_LVBus0185717_consumption' has phase imbalance of 97.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185264_consumption`  
  Load '93_LVBus0185264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1372287_consumption`  
  Load '93_LVBus1372287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185494_consumption`  
  Load '93_LVBus0185494_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185488_consumption`  
  Load '93_LVBus0185488_consumption' has phase imbalance of 264.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185605_consumption`  
  Load '93_LVBus0185605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185497_consumption`  
  Load '93_LVBus0185497_consumption' has phase imbalance of 51.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185591_consumption`  
  Load '93_LVBus0185591_consumption' has phase imbalance of 107.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185485_consumption`  
  Load '93_LVBus0185485_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185404_consumption`  
  Load '93_LVBus0185404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185263_consumption`  
  Load '93_LVBus0185263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185226_consumption`  
  Load '93_LVBus0185226_consumption' has phase imbalance of 128.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185424_consumption`  
  Load '93_LVBus0185424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185329_consumption`  
  Load '93_LVBus0185329_consumption' has phase imbalance of 141.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185400_consumption`  
  Load '93_LVBus0185400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185875_consumption`  
  Load '93_LVBus0185875_consumption' has phase imbalance of 51.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185267_consumption`  
  Load '93_LVBus0185267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185511_consumption`  
  Load '93_LVBus0185511_consumption' has phase imbalance of 123.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185732_consumption`  
  Load '93_LVBus0185732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185850_consumption`  
  Load '93_LVBus0185850_consumption' has phase imbalance of 74.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185620_consumption`  
  Load '93_LVBus0185620_consumption' has phase imbalance of 57.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185261_consumption`  
  Load '93_LVBus0185261_consumption' has phase imbalance of 213.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185313_consumption`  
  Load '93_LVBus0185313_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185380_consumption`  
  Load '93_LVBus0185380_consumption' has phase imbalance of 61.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185338_consumption`  
  Load '93_LVBus0185338_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185375_consumption`  
  Load '93_LVBus0185375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185663_consumption`  
  Load '93_LVBus0185663_consumption' has phase imbalance of 25.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185635_consumption`  
  Load '93_LVBus0185635_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185405_consumption`  
  Load '93_LVBus0185405_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185259_consumption`  
  Load '93_LVBus0185259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185559_consumption`  
  Load '93_LVBus0185559_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185500_consumption`  
  Load '93_LVBus0185500_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185749_consumption`  
  Load '93_LVBus0185749_consumption' has phase imbalance of 32.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185564_consumption`  
  Load '93_LVBus0185564_consumption' has phase imbalance of 84.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185604_consumption`  
  Load '93_LVBus0185604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185631_consumption`  
  Load '93_LVBus0185631_consumption' has phase imbalance of 89.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185352_consumption`  
  Load '93_LVBus0185352_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185376_consumption`  
  Load '93_LVBus0185376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185486_consumption`  
  Load '93_LVBus0185486_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185624_consumption`  
  Load '93_LVBus0185624_consumption' has phase imbalance of 47.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185496_consumption`  
  Load '93_LVBus0185496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185757_consumption`  
  Load '93_LVBus0185757_consumption' has phase imbalance of 62.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185284_consumption`  
  Load '93_LVBus0185284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1346872_consumption`  
  Load '93_LVBus1346872_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185372_consumption`  
  Load '93_LVBus0185372_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185736_consumption`  
  Load '93_LVBus0185736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185770_consumption`  
  Load '93_LVBus0185770_consumption' has phase imbalance of 115.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185588_consumption`  
  Load '93_LVBus0185588_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185689_consumption`  
  Load '93_LVBus0185689_consumption' has phase imbalance of 59.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185489_consumption`  
  Load '93_LVBus0185489_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185622_consumption`  
  Load '93_LVBus0185622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185530_consumption`  
  Load '93_LVBus0185530_consumption' has phase imbalance of 67.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185395_consumption`  
  Load '93_LVBus0185395_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185279_consumption`  
  Load '93_LVBus0185279_consumption' has phase imbalance of 37.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185354_consumption`  
  Load '93_LVBus0185354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185393_consumption`  
  Load '93_LVBus0185393_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185458_consumption`  
  Load '93_LVBus0185458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185525_consumption`  
  Load '93_LVBus0185525_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185719_consumption`  
  Load '93_LVBus0185719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185739_consumption`  
  Load '93_LVBus0185739_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185518_consumption`  
  Load '93_LVBus0185518_consumption' has phase imbalance of 74.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185445_consumption`  
  Load '93_LVBus0185445_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185837_consumption`  
  Load '93_LVBus0185837_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185228_consumption`  
  Load '93_LVBus0185228_consumption' has phase imbalance of 33.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185257_consumption`  
  Load '93_LVBus0185257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185373_consumption`  
  Load '93_LVBus0185373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185657_consumption`  
  Load '93_LVBus0185657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185385_consumption`  
  Load '93_LVBus0185385_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185498_consumption`  
  Load '93_LVBus0185498_consumption' has phase imbalance of 232.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185669_consumption`  
  Load '93_LVBus0185669_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185654_consumption`  
  Load '93_LVBus0185654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185368_consumption`  
  Load '93_LVBus0185368_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185676_consumption`  
  Load '93_LVBus0185676_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185312_consumption`  
  Load '93_LVBus0185312_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185566_consumption`  
  Load '93_LVBus0185566_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185242_consumption`  
  Load '93_LVBus0185242_consumption' has phase imbalance of 124.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185371_consumption`  
  Load '93_LVBus0185371_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185615_consumption`  
  Load '93_LVBus0185615_consumption' has phase imbalance of 72.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185361_consumption`  
  Load '93_LVBus0185361_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185542_consumption`  
  Load '93_LVBus0185542_consumption' has phase imbalance of 59.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185538_consumption`  
  Load '93_LVBus0185538_consumption' has phase imbalance of 244.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185579_consumption`  
  Load '93_LVBus0185579_consumption' has phase imbalance of 107.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185383_consumption`  
  Load '93_LVBus0185383_consumption' has phase imbalance of 296.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185753_consumption`  
  Load '93_LVBus0185753_consumption' has phase imbalance of 41.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185420_consumption`  
  Load '93_LVBus0185420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185536_consumption`  
  Load '93_LVBus0185536_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185562_consumption`  
  Load '93_LVBus0185562_consumption' has phase imbalance of 279.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185289_consumption`  
  Load '93_LVBus0185289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185686_consumption`  
  Load '93_LVBus0185686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1418039_consumption`  
  Load '93_LVBus1418039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1372286_consumption`  
  Load '93_LVBus1372286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185506_consumption`  
  Load '93_LVBus0185506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185370_consumption`  
  Load '93_LVBus0185370_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185336_consumption`  
  Load '93_LVBus0185336_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185706_consumption`  
  Load '93_LVBus0185706_consumption' has phase imbalance of 37.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185523_consumption`  
  Load '93_LVBus0185523_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185694_consumption`  
  Load '93_LVBus0185694_consumption' has phase imbalance of 24.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185574_consumption`  
  Load '93_LVBus0185574_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185673_consumption`  
  Load '93_LVBus0185673_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185573_consumption`  
  Load '93_LVBus0185573_consumption' has phase imbalance of 143.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185602_consumption`  
  Load '93_LVBus0185602_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185567_consumption`  
  Load '93_LVBus0185567_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185700_consumption`  
  Load '93_LVBus0185700_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185422_consumption`  
  Load '93_LVBus0185422_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185245_consumption`  
  Load '93_LVBus0185245_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1371566_consumption`  
  Load '93_LVBus1371566_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185381_consumption`  
  Load '93_LVBus0185381_consumption' has phase imbalance of 236.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185416_consumption`  
  Load '93_LVBus0185416_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185412_consumption`  
  Load '93_LVBus0185412_consumption' has phase imbalance of 27.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185378_consumption`  
  Load '93_LVBus0185378_consumption' has phase imbalance of 210.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185265_consumption`  
  Load '93_LVBus0185265_consumption' has phase imbalance of 240.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185403_consumption`  
  Load '93_LVBus0185403_consumption' has phase imbalance of 194.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185685_consumption`  
  Load '93_LVBus0185685_consumption' has phase imbalance of 146.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185377_consumption`  
  Load '93_LVBus0185377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185575_consumption`  
  Load '93_LVBus0185575_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185517_consumption`  
  Load '93_LVBus0185517_consumption' has phase imbalance of 78.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185598_consumption`  
  Load '93_LVBus0185598_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185258_consumption`  
  Load '93_LVBus0185258_consumption' has phase imbalance of 223.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185253_consumption`  
  Load '93_LVBus0185253_consumption' has phase imbalance of 225.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185482_consumption`  
  Load '93_LVBus0185482_consumption' has phase imbalance of 255.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185300_consumption`  
  Load '93_LVBus0185300_consumption' has phase imbalance of 118.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1346871_consumption`  
  Load '93_LVBus1346871_consumption' has phase imbalance of 268.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185547_consumption`  
  Load '93_LVBus0185547_consumption' has phase imbalance of 24.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185763_consumption`  
  Load '93_LVBus0185763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185364_consumption`  
  Load '93_LVBus0185364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185514_consumption`  
  Load '93_LVBus0185514_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185503_consumption`  
  Load '93_LVBus0185503_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185384_consumption`  
  Load '93_LVBus0185384_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185578_consumption`  
  Load '93_LVBus0185578_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185426_consumption`  
  Load '93_LVBus0185426_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185731_consumption`  
  Load '93_LVBus0185731_consumption' has phase imbalance of 47.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185521_consumption`  
  Load '93_LVBus0185521_consumption' has phase imbalance of 97.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185678_consumption`  
  Load '93_LVBus0185678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185683_consumption`  
  Load '93_LVBus0185683_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185509_consumption`  
  Load '93_LVBus0185509_consumption' has phase imbalance of 133.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185526_consumption`  
  Load '93_LVBus0185526_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185767_consumption`  
  Load '93_LVBus0185767_consumption' has phase imbalance of 87.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185600_consumption`  
  Load '93_LVBus0185600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185244_consumption`  
  Load '93_LVBus0185244_consumption' has phase imbalance of 29.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185580_consumption`  
  Load '93_LVBus0185580_consumption' has phase imbalance of 136.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185392_consumption`  
  Load '93_LVBus0185392_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185655_consumption`  
  Load '93_LVBus0185655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1372288_consumption`  
  Load '93_LVBus1372288_consumption' has phase imbalance of 184.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185568_consumption`  
  Load '93_LVBus0185568_consumption' has phase imbalance of 104.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185495_consumption`  
  Load '93_LVBus0185495_consumption' has phase imbalance of 226.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185565_consumption`  
  Load '93_LVBus0185565_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185720_consumption`  
  Load '93_LVBus0185720_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185656_consumption`  
  Load '93_LVBus0185656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185691_consumption`  
  Load '93_LVBus0185691_consumption' has phase imbalance of 33.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185340_consumption`  
  Load '93_LVBus0185340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185577_consumption`  
  Load '93_LVBus0185577_consumption' has phase imbalance of 67.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185734_consumption`  
  Load '93_LVBus0185734_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185307_consumption`  
  Load '93_LVBus0185307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185552_consumption`  
  Load '93_LVBus0185552_consumption' has phase imbalance of 80.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185835_consumption`  
  Load '93_LVBus0185835_consumption' has phase imbalance of 115.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185773_consumption`  
  Load '93_LVBus0185773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185219_consumption`  
  Load '93_LVBus0185219_consumption' has phase imbalance of 96.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185607_consumption`  
  Load '93_LVBus0185607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0185516_consumption`  
  Load '93_LVBus0185516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1120 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0185269' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_GAP' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0185432' has balanced aggregate load across 3 phase(s) (max spread 0.51%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '93_LVBus0185212' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '93_LVBus0185883' (LV, 0.24 kV) has an electrical reach of 2.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '93_LVBus0185852' (LV, 0.24 kV) has an electrical reach of 22.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  615 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  154 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 93_LVBus0185231_consumption, 93_LVBus0185236_consumption, 93_LVBus0185246_consumption, 93_LVBus0185252_consumption, 93_LVBus0185253_consumption, 93_LVBus0185257_consumption, 93_LVBus0185258_consumption, 93_LVBus0185259_consumption, 93_LVBus0185261_consumption, 93_LVBus0185263_consumption, 93_LVBus0185264_consumption, 93_LVBus0185265_consumption, 93_LVBus0185267_consumption, 93_LVBus0185282_consumption, 93_LVBus0185283_consumption, 93_LVBus0185284_consumption, 93_LVBus0185286_consumption, 93_LVBus0185287_consumption, 93_LVBus0185289_consumption, 93_LVBus0185299_consumption, 93_LVBus0185307_consumption, 93_LVBus0185313_consumption, 93_LVBus0185336_consumption, 93_LVBus0185338_consumption, 93_LVBus0185340_consumption, 93_LVBus0185347_consumption, 93_LVBus0185352_consumption, 93_LVBus0185354_consumption, 93_LVBus0185359_consumption, 93_LVBus0185360_consumption, 93_LVBus0185361_consumption, 93_LVBus0185364_consumption, 93_LVBus0185365_consumption, 93_LVBus0185368_consumption, 93_LVBus0185370_consumption, 93_LVBus0185373_consumption, 93_LVBus0185375_consumption, 93_LVBus0185376_consumption, 93_LVBus0185377_consumption, 93_LVBus0185381_consumption, 93_LVBus0185383_consumption, 93_LVBus0185384_consumption, 93_LVBus0185385_consumption, 93_LVBus0185386_consumption, 93_LVBus0185389_consumption, 93_LVBus0185392_consumption, 93_LVBus0185393_consumption, 93_LVBus0185397_consumption, 93_LVBus0185400_consumption, 93_LVBus0185401_consumption, 93_LVBus0185403_consumption, 93_LVBus0185404_consumption, 93_LVBus0185405_consumption, 93_LVBus0185416_consumption, 93_LVBus0185418_consumption, 93_LVBus0185419_consumption, 93_LVBus0185420_consumption, 93_LVBus0185421_consumption, 93_LVBus0185422_consumption, 93_LVBus0185423_consumption, 93_LVBus0185424_consumption, 93_LVBus0185426_consumption, 93_LVBus0185428_consumption, 93_LVBus0185429_consumption, 93_LVBus0185430_consumption, 93_LVBus0185448_consumption, 93_LVBus0185450_consumption, 93_LVBus0185458_consumption, 93_LVBus0185482_consumption, 93_LVBus0185485_consumption, 93_LVBus0185486_consumption, 93_LVBus0185490_consumption, 93_LVBus0185494_consumption, 93_LVBus0185495_consumption, 93_LVBus0185496_consumption, 93_LVBus0185498_consumption, 93_LVBus0185499_consumption, 93_LVBus0185500_consumption, 93_LVBus0185504_consumption, 93_LVBus0185506_consumption, 93_LVBus0185510_consumption, 93_LVBus0185516_consumption, 93_LVBus0185523_consumption, 93_LVBus0185524_consumption, 93_LVBus0185531_consumption, 93_LVBus0185538_consumption, 93_LVBus0185558_consumption, 93_LVBus0185561_consumption, 93_LVBus0185562_consumption, 93_LVBus0185563_consumption, 93_LVBus0185567_consumption, 93_LVBus0185570_consumption, 93_LVBus0185576_consumption, 93_LVBus0185578_consumption, 93_LVBus0185581_consumption, 93_LVBus0185582_consumption, 93_LVBus0185583_consumption, 93_LVBus0185585_consumption, 93_LVBus0185588_consumption, 93_LVBus0185595_consumption, 93_LVBus0185596_consumption, 93_LVBus0185598_consumption, 93_LVBus0185600_consumption, 93_LVBus0185601_consumption, 93_LVBus0185602_consumption, 93_LVBus0185604_consumption, 93_LVBus0185605_consumption, 93_LVBus0185606_consumption, 93_LVBus0185607_consumption, 93_LVBus0185608_consumption, 93_LVBus0185611_consumption, 93_LVBus0185618_consumption, 93_LVBus0185622_consumption, 93_LVBus0185635_consumption, 93_LVBus0185646_consumption, 93_LVBus0185653_consumption, 93_LVBus0185654_consumption, 93_LVBus0185655_consumption, 93_LVBus0185656_consumption, 93_LVBus0185657_consumption, 93_LVBus0185667_consumption, 93_LVBus0185669_consumption, 93_LVBus0185670_consumption, 93_LVBus0185671_consumption, 93_LVBus0185673_consumption, 93_LVBus0185676_consumption, 93_LVBus0185678_consumption, 93_LVBus0185686_consumption, 93_LVBus0185700_consumption, 93_LVBus0185719_consumption, 93_LVBus0185720_consumption, 93_LVBus0185721_consumption, 93_LVBus0185732_consumption, 93_LVBus0185734_consumption, 93_LVBus0185736_consumption, 93_LVBus0185743_consumption, 93_LVBus0185744_consumption, 93_LVBus0185763_consumption, 93_LVBus0185764_consumption, 93_LVBus0185765_consumption, 93_LVBus0185772_consumption, 93_LVBus0185773_consumption, 93_LVBus0185775_consumption, 93_LVBus0185776_consumption, 93_LVBus0185848_consumption, 93_LVBus1346871_consumption, 93_LVBus1346872_consumption, 93_LVBus1371566_consumption, 93_LVBus1372286_consumption, 93_LVBus1372287_consumption, 93_LVBus1372288_consumption, 93_LVBus1404762_consumption, 93_LVBus1404763_consumption, 93_LVBus1418039_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  560 group(s) of loads (1120 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (2 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  807 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0185212_production, 93_LVBus0185214_production, 93_LVBus0185216_production, 93_LVBus0185218_consumption, 93_LVBus0185218_production, 93_LVBus0185219_production, 93_LVBus0185221_consumption, 93_LVBus0185221_production, 93_LVBus0185222_consumption, 93_LVBus0185222_production, 93_LVBus0185223_consumption, 93_LVBus0185223_production, 93_LVBus0185224_consumption, 93_LVBus0185224_production, 93_LVBus0185225_consumption, 93_LVBus0185225_production, 93_LVBus0185226_production, 93_LVBus0185228_production, 93_LVBus0185230_consumption, 93_LVBus0185230_production, 93_LVBus0185231_production, 93_LVBus0185232_consumption, 93_LVBus0185232_production, 93_LVBus0185233_consumption, 93_LVBus0185233_production, 93_LVBus0185234_consumption, 93_LVBus0185234_production, 93_LVBus0185235_production, 93_LVBus0185236_production, 93_LVBus0185237_consumption, 93_LVBus0185237_production, 93_LVBus0185238_consumption, 93_LVBus0185238_production, 93_LVBus0185240_consumption, 93_LVBus0185240_production, 93_LVBus0185242_production, 93_LVBus0185243_production, 93_LVBus0185244_production, 93_LVBus0185245_production, 93_LVBus0185246_production, 93_LVBus0185248_consumption, 93_LVBus0185248_production, 93_LVBus0185250_consumption, 93_LVBus0185250_production, 93_LVBus0185251_consumption, 93_LVBus0185251_production, 93_LVBus0185252_production, 93_LVBus0185253_production, 93_LVBus0185254_consumption, 93_LVBus0185254_production, 93_LVBus0185255_production, 93_LVBus0185256_consumption, 93_LVBus0185256_production, 93_LVBus0185257_production, 93_LVBus0185258_production, 93_LVBus0185259_production, 93_LVBus0185260_consumption, 93_LVBus0185260_production, 93_LVBus0185261_production, 93_LVBus0185262_consumption, 93_LVBus0185262_production, 93_LVBus0185263_production, 93_LVBus0185264_production, 93_LVBus0185265_production, 93_LVBus0185267_production, 93_LVBus0185269_production, 93_LVBus0185271_production, 93_LVBus0185272_production, 93_LVBus0185273_production, 93_LVBus0185275_production, 93_LVBus0185277_production, 93_LVBus0185279_production, 93_LVBus0185281_consumption, 93_LVBus0185281_production, 93_LVBus0185282_production, 93_LVBus0185283_production, 93_LVBus0185284_production, 93_LVBus0185285_consumption, 93_LVBus0185285_production, 93_LVBus0185286_production, 93_LVBus0185287_production, 93_LVBus0185288_production, 93_LVBus0185289_production, 93_LVBus0185291_consumption, 93_LVBus0185291_production, 93_LVBus0185292_consumption, 93_LVBus0185292_production, 93_LVBus0185293_consumption, 93_LVBus0185293_production, 93_LVBus0185295_consumption, 93_LVBus0185295_production, 93_LVBus0185296_consumption, 93_LVBus0185296_production, 93_LVBus0185297_consumption, 93_LVBus0185297_production, 93_LVBus0185298_consumption, 93_LVBus0185298_production, 93_LVBus0185299_production, 93_LVBus0185300_production, 93_LVBus0185301_production, 93_LVBus0185302_production, 93_LVBus0185303_consumption, 93_LVBus0185303_production, 93_LVBus0185304_consumption, 93_LVBus0185304_production, 93_LVBus0185305_consumption, 93_LVBus0185305_production, 93_LVBus0185306_consumption, 93_LVBus0185306_production, 93_LVBus0185307_production, 93_LVBus0185309_consumption, 93_LVBus0185309_production, 93_LVBus0185310_consumption, 93_LVBus0185310_production, 93_LVBus0185311_consumption, 93_LVBus0185311_production, 93_LVBus0185312_production, 93_LVBus0185313_production, 93_LVBus0185314_consumption, 93_LVBus0185314_production, 93_LVBus0185316_consumption, 93_LVBus0185316_production, 93_LVBus0185317_consumption, 93_LVBus0185317_production, 93_LVBus0185318_consumption, 93_LVBus0185318_production, 93_LVBus0185319_consumption, 93_LVBus0185319_production, 93_LVBus0185320_consumption, 93_LVBus0185320_production, 93_LVBus0185321_consumption, 93_LVBus0185321_production, 93_LVBus0185323_consumption, 93_LVBus0185323_production, 93_LVBus0185324_consumption, 93_LVBus0185324_production, 93_LVBus0185325_consumption, 93_LVBus0185325_production, 93_LVBus0185326_consumption, 93_LVBus0185326_production, 93_LVBus0185327_consumption, 93_LVBus0185327_production, 93_LVBus0185328_consumption, 93_LVBus0185328_production, 93_LVBus0185329_production, 93_LVBus0185330_consumption, 93_LVBus0185330_production, 93_LVBus0185332_consumption, 93_LVBus0185332_production, 93_LVBus0185334_consumption, 93_LVBus0185334_production, 93_LVBus0185335_consumption, 93_LVBus0185335_production, 93_LVBus0185336_production, 93_LVBus0185337_production, 93_LVBus0185338_production, 93_LVBus0185339_production, 93_LVBus0185340_production, 93_LVBus0185342_consumption, 93_LVBus0185342_production, 93_LVBus0185343_consumption, 93_LVBus0185343_production, 93_LVBus0185344_consumption, 93_LVBus0185344_production, 93_LVBus0185345_consumption, 93_LVBus0185345_production, 93_LVBus0185346_consumption, 93_LVBus0185346_production, 93_LVBus0185347_production, 93_LVBus0185348_consumption, 93_LVBus0185348_production, 93_LVBus0185350_consumption, 93_LVBus0185350_production, 93_LVBus0185352_production, 93_LVBus0185353_production, 93_LVBus0185354_production, 93_LVBus0185356_production, 93_LVBus0185358_consumption, 93_LVBus0185358_production, 93_LVBus0185359_production, 93_LVBus0185360_production, 93_LVBus0185361_production, 93_LVBus0185362_consumption, 93_LVBus0185362_production, 93_LVBus0185363_consumption, 93_LVBus0185363_production, 93_LVBus0185364_production, 93_LVBus0185365_production, 93_LVBus0185366_consumption, 93_LVBus0185366_production, 93_LVBus0185367_production, 93_LVBus0185368_production, 93_LVBus0185370_production, 93_LVBus0185371_production, 93_LVBus0185372_production, 93_LVBus0185373_production, 93_LVBus0185374_consumption, 93_LVBus0185374_production, 93_LVBus0185375_production, 93_LVBus0185376_production, 93_LVBus0185377_production, 93_LVBus0185378_production, 93_LVBus0185379_consumption, 93_LVBus0185379_production, 93_LVBus0185380_production, 93_LVBus0185381_production, 93_LVBus0185382_consumption, 93_LVBus0185382_production, 93_LVBus0185383_production, 93_LVBus0185384_production, 93_LVBus0185385_production, 93_LVBus0185386_production, 93_LVBus0185388_consumption, 93_LVBus0185388_production, 93_LVBus0185389_production, 93_LVBus0185390_consumption, 93_LVBus0185390_production, 93_LVBus0185391_production, 93_LVBus0185392_production, 93_LVBus0185393_production, 93_LVBus0185394_production, 93_LVBus0185395_production, 93_LVBus0185397_production, 93_LVBus0185398_production, 93_LVBus0185399_consumption, 93_LVBus0185399_production, 93_LVBus0185400_production, 93_LVBus0185401_production, 93_LVBus0185402_consumption, 93_LVBus0185402_production, 93_LVBus0185403_production, 93_LVBus0185404_production, 93_LVBus0185405_production, 93_LVBus0185406_consumption, 93_LVBus0185406_production, 93_LVBus0185408_consumption, 93_LVBus0185408_production, 93_LVBus0185409_consumption, 93_LVBus0185409_production, 93_LVBus0185410_consumption, 93_LVBus0185410_production, 93_LVBus0185411_consumption, 93_LVBus0185411_production, 93_LVBus0185412_production, 93_LVBus0185414_consumption, 93_LVBus0185414_production, 93_LVBus0185416_production, 93_LVBus0185417_consumption, 93_LVBus0185417_production, 93_LVBus0185418_production, 93_LVBus0185419_production, 93_LVBus0185420_production, 93_LVBus0185421_production, 93_LVBus0185422_production, 93_LVBus0185423_production, 93_LVBus0185424_production, 93_LVBus0185425_consumption, 93_LVBus0185425_production, 93_LVBus0185426_production, 93_LVBus0185428_production, 93_LVBus0185429_production, 93_LVBus0185430_production, 93_LVBus0185432_consumption, 93_LVBus0185432_production, 93_LVBus0185433_production, 93_LVBus0185435_production, 93_LVBus0185436_consumption, 93_LVBus0185436_production, 93_LVBus0185437_production, 93_LVBus0185439_production, 93_LVBus0185440_production, 93_LVBus0185441_consumption, 93_LVBus0185441_production, 93_LVBus0185442_production, 93_LVBus0185443_production, 93_LVBus0185445_production, 93_LVBus0185446_production, 93_LVBus0185448_production, 93_LVBus0185449_production, 93_LVBus0185450_production, 93_LVBus0185452_consumption, 93_LVBus0185452_production, 93_LVBus0185453_production, 93_LVBus0185455_consumption, 93_LVBus0185455_production, 93_LVBus0185456_consumption, 93_LVBus0185456_production, 93_LVBus0185457_consumption, 93_LVBus0185457_production, 93_LVBus0185458_production, 93_LVBus0185459_consumption, 93_LVBus0185459_production, 93_LVBus0185461_consumption, 93_LVBus0185461_production, 93_LVBus0185463_production, 93_LVBus0185465_consumption, 93_LVBus0185465_production, 93_LVBus0185467_production, 93_LVBus0185468_consumption, 93_LVBus0185468_production, 93_LVBus0185470_consumption, 93_LVBus0185470_production, 93_LVBus0185471_production, 93_LVBus0185473_consumption, 93_LVBus0185473_production, 93_LVBus0185475_consumption, 93_LVBus0185475_production, 93_LVBus0185476_consumption, 93_LVBus0185476_production, 93_LVBus0185477_consumption, 93_LVBus0185477_production, 93_LVBus0185479_consumption, 93_LVBus0185479_production, 93_LVBus0185480_production, 93_LVBus0185482_production, 93_LVBus0185483_production, 93_LVBus0185485_production, 93_LVBus0185486_production, 93_LVBus0185487_production, 93_LVBus0185488_production, 93_LVBus0185489_production, 93_LVBus0185490_production, 93_LVBus0185492_production, 93_LVBus0185493_consumption, 93_LVBus0185493_production, 93_LVBus0185494_production, 93_LVBus0185495_production, 93_LVBus0185496_production, 93_LVBus0185497_production, 93_LVBus0185498_production, 93_LVBus0185499_production, 93_LVBus0185500_production, 93_LVBus0185501_production, 93_LVBus0185502_production, 93_LVBus0185503_production, 93_LVBus0185504_production, 93_LVBus0185506_production, 93_LVBus0185507_consumption, 93_LVBus0185507_production, 93_LVBus0185508_consumption, 93_LVBus0185508_production, 93_LVBus0185509_production, 93_LVBus0185510_production, 93_LVBus0185511_production, 93_LVBus0185512_production, 93_LVBus0185513_consumption, 93_LVBus0185513_production, 93_LVBus0185514_production, 93_LVBus0185515_consumption, 93_LVBus0185515_production, 93_LVBus0185516_production, 93_LVBus0185517_production, 93_LVBus0185518_production, 93_LVBus0185519_production, 93_LVBus0185521_production, 93_LVBus0185523_production, 93_LVBus0185524_production, 93_LVBus0185525_production, 93_LVBus0185526_production, 93_LVBus0185527_consumption, 93_LVBus0185527_production, 93_LVBus0185529_consumption, 93_LVBus0185529_production, 93_LVBus0185530_production, 93_LVBus0185531_production, 93_LVBus0185532_production, 93_LVBus0185534_consumption, 93_LVBus0185534_production, 93_LVBus0185535_consumption, 93_LVBus0185535_production, 93_LVBus0185536_production, 93_LVBus0185537_consumption, 93_LVBus0185537_production, 93_LVBus0185538_production, 93_LVBus0185539_consumption, 93_LVBus0185539_production, 93_LVBus0185540_production, 93_LVBus0185541_consumption, 93_LVBus0185541_production, 93_LVBus0185542_production, 93_LVBus0185544_consumption, 93_LVBus0185544_production, 93_LVBus0185546_consumption, 93_LVBus0185546_production, 93_LVBus0185547_production, 93_LVBus0185549_consumption, 93_LVBus0185549_production, 93_LVBus0185551_consumption, 93_LVBus0185551_production, 93_LVBus0185552_production, 93_LVBus0185554_consumption, 93_LVBus0185554_production, 93_LVBus0185555_consumption, 93_LVBus0185555_production, 93_LVBus0185557_consumption, 93_LVBus0185557_production, 93_LVBus0185558_production, 93_LVBus0185559_production, 93_LVBus0185560_production, 93_LVBus0185561_production, 93_LVBus0185562_production, 93_LVBus0185563_production, 93_LVBus0185564_production, 93_LVBus0185565_production, 93_LVBus0185566_production, 93_LVBus0185567_production, 93_LVBus0185568_production, 93_LVBus0185570_production, 93_LVBus0185571_consumption, 93_LVBus0185571_production, 93_LVBus0185572_consumption, 93_LVBus0185572_production, 93_LVBus0185573_production, 93_LVBus0185574_production, 93_LVBus0185575_production, 93_LVBus0185576_production, 93_LVBus0185577_production, 93_LVBus0185578_production, 93_LVBus0185579_production, 93_LVBus0185580_production, 93_LVBus0185581_production, 93_LVBus0185582_production, 93_LVBus0185583_production, 93_LVBus0185585_production, 93_LVBus0185586_consumption, 93_LVBus0185586_production, 93_LVBus0185587_production, 93_LVBus0185588_production, 93_LVBus0185589_production, 93_LVBus0185591_production, 93_LVBus0185592_production, 93_LVBus0185594_production, 93_LVBus0185595_production, 93_LVBus0185596_production, 93_LVBus0185597_consumption, 93_LVBus0185597_production, 93_LVBus0185598_production, 93_LVBus0185600_production, 93_LVBus0185601_production, 93_LVBus0185602_production, 93_LVBus0185603_consumption, 93_LVBus0185603_production, 93_LVBus0185604_production, 93_LVBus0185605_production, 93_LVBus0185606_production, 93_LVBus0185607_production, 93_LVBus0185608_production, 93_LVBus0185609_consumption, 93_LVBus0185609_production, 93_LVBus0185610_consumption, 93_LVBus0185610_production, 93_LVBus0185611_production, 93_LVBus0185613_production, 93_LVBus0185614_consumption, 93_LVBus0185614_production, 93_LVBus0185615_production, 93_LVBus0185616_production, 93_LVBus0185618_production, 93_LVBus0185619_production, 93_LVBus0185620_production, 93_LVBus0185621_consumption, 93_LVBus0185621_production, 93_LVBus0185622_production, 93_LVBus0185623_consumption, 93_LVBus0185623_production, 93_LVBus0185624_production, 93_LVBus0185625_production, 93_LVBus0185627_consumption, 93_LVBus0185627_production, 93_LVBus0185628_consumption, 93_LVBus0185628_production, 93_LVBus0185630_consumption, 93_LVBus0185630_production, 93_LVBus0185631_production, 93_LVBus0185633_consumption, 93_LVBus0185633_production, 93_LVBus0185634_production, 93_LVBus0185635_production, 93_LVBus0185637_consumption, 93_LVBus0185637_production, 93_LVBus0185638_production, 93_LVBus0185639_production, 93_LVBus0185641_consumption, 93_LVBus0185641_production, 93_LVBus0185642_production, 93_LVBus0185643_consumption, 93_LVBus0185643_production, 93_LVBus0185644_production, 93_LVBus0185646_production, 93_LVBus0185648_production, 93_LVBus0185650_production, 93_LVBus0185652_consumption, 93_LVBus0185652_production, 93_LVBus0185653_production, 93_LVBus0185654_production, 93_LVBus0185655_production, 93_LVBus0185656_production, 93_LVBus0185657_production, 93_LVBus0185658_consumption, 93_LVBus0185658_production, 93_LVBus0185659_consumption, 93_LVBus0185659_production, 93_LVBus0185660_production, 93_LVBus0185661_production, 93_LVBus0185662_consumption, 93_LVBus0185662_production, 93_LVBus0185663_production, 93_LVBus0185664_consumption, 93_LVBus0185664_production, 93_LVBus0185665_consumption, 93_LVBus0185665_production, 93_LVBus0185666_consumption, 93_LVBus0185666_production, 93_LVBus0185667_production, 93_LVBus0185668_consumption, 93_LVBus0185668_production, 93_LVBus0185669_production, 93_LVBus0185670_production, 93_LVBus0185671_production, 93_LVBus0185672_consumption, 93_LVBus0185672_production, 93_LVBus0185673_production, 93_LVBus0185675_consumption, 93_LVBus0185675_production, 93_LVBus0185676_production, 93_LVBus0185677_production, 93_LVBus0185678_production, 93_LVBus0185679_consumption, 93_LVBus0185679_production, 93_LVBus0185681_consumption, 93_LVBus0185681_production, 93_LVBus0185682_consumption, 93_LVBus0185682_production, 93_LVBus0185683_production, 93_LVBus0185684_consumption, 93_LVBus0185684_production, 93_LVBus0185685_production, 93_LVBus0185686_production, 93_LVBus0185687_consumption, 93_LVBus0185687_production, 93_LVBus0185688_consumption, 93_LVBus0185688_production, 93_LVBus0185689_production, 93_LVBus0185690_consumption, 93_LVBus0185690_production, 93_LVBus0185691_production, 93_LVBus0185692_consumption, 93_LVBus0185692_production, 93_LVBus0185694_production, 93_LVBus0185696_consumption, 93_LVBus0185696_production, 93_LVBus0185698_production, 93_LVBus0185700_production, 93_LVBus0185701_consumption, 93_LVBus0185701_production, 93_LVBus0185702_production, 93_LVBus0185703_production, 93_LVBus0185704_consumption, 93_LVBus0185704_production, 93_LVBus0185705_consumption, 93_LVBus0185705_production, 93_LVBus0185706_production, 93_LVBus0185707_consumption, 93_LVBus0185707_production, 93_LVBus0185708_production, 93_LVBus0185709_consumption, 93_LVBus0185709_production, 93_LVBus0185711_consumption, 93_LVBus0185711_production, 93_LVBus0185712_production, 93_LVBus0185713_consumption, 93_LVBus0185713_production, 93_LVBus0185714_consumption, 93_LVBus0185714_production, 93_LVBus0185715_consumption, 93_LVBus0185715_production, 93_LVBus0185716_production, 93_LVBus0185717_production, 93_LVBus0185718_production, 93_LVBus0185719_production, 93_LVBus0185720_production, 93_LVBus0185721_production, 93_LVBus0185722_production, 93_LVBus0185724_consumption, 93_LVBus0185724_production, 93_LVBus0185726_consumption, 93_LVBus0185726_production, 93_LVBus0185727_consumption, 93_LVBus0185727_production, 93_LVBus0185728_consumption, 93_LVBus0185728_production, 93_LVBus0185729_consumption, 93_LVBus0185729_production, 93_LVBus0185730_consumption, 93_LVBus0185730_production, 93_LVBus0185731_production, 93_LVBus0185732_production, 93_LVBus0185733_consumption, 93_LVBus0185733_production, 93_LVBus0185734_production, 93_LVBus0185736_production, 93_LVBus0185737_consumption, 93_LVBus0185737_production, 93_LVBus0185738_consumption, 93_LVBus0185738_production, 93_LVBus0185739_production, 93_LVBus0185741_consumption, 93_LVBus0185741_production, 93_LVBus0185742_production, 93_LVBus0185743_production, 93_LVBus0185744_production, 93_LVBus0185745_production, 93_LVBus0185747_consumption, 93_LVBus0185747_production, 93_LVBus0185748_production, 93_LVBus0185749_production, 93_LVBus0185751_consumption, 93_LVBus0185751_production, 93_LVBus0185753_production, 93_LVBus0185755_consumption, 93_LVBus0185755_production, 93_LVBus0185756_consumption, 93_LVBus0185756_production, 93_LVBus0185757_production, 93_LVBus0185759_consumption, 93_LVBus0185759_production, 93_LVBus0185760_consumption, 93_LVBus0185760_production, 93_LVBus0185761_consumption, 93_LVBus0185761_production, 93_LVBus0185762_consumption, 93_LVBus0185762_production, 93_LVBus0185763_production, 93_LVBus0185764_production, 93_LVBus0185765_production, 93_LVBus0185766_consumption, 93_LVBus0185766_production, 93_LVBus0185767_production, 93_LVBus0185768_consumption, 93_LVBus0185768_production, 93_LVBus0185769_production, 93_LVBus0185770_production, 93_LVBus0185771_consumption, 93_LVBus0185771_production, 93_LVBus0185772_production, 93_LVBus0185773_production, 93_LVBus0185775_production, 93_LVBus0185776_production, 93_LVBus0185778_consumption, 93_LVBus0185778_production, 93_LVBus0185779_production, 93_LVBus0185781_consumption, 93_LVBus0185781_production, 93_LVBus0185782_consumption, 93_LVBus0185782_production, 93_LVBus0185783_consumption, 93_LVBus0185783_production, 93_LVBus0185784_consumption, 93_LVBus0185784_production, 93_LVBus0185786_consumption, 93_LVBus0185786_production, 93_LVBus0185788_consumption, 93_LVBus0185788_production, 93_LVBus0185789_consumption, 93_LVBus0185789_production, 93_LVBus0185790_consumption, 93_LVBus0185790_production, 93_LVBus0185791_consumption, 93_LVBus0185791_production, 93_LVBus0185792_consumption, 93_LVBus0185792_production, 93_LVBus0185793_consumption, 93_LVBus0185793_production, 93_LVBus0185794_consumption, 93_LVBus0185794_production, 93_LVBus0185795_consumption, 93_LVBus0185795_production, 93_LVBus0185796_consumption, 93_LVBus0185796_production, 93_LVBus0185797_consumption, 93_LVBus0185797_production, 93_LVBus0185798_consumption, 93_LVBus0185798_production, 93_LVBus0185800_consumption, 93_LVBus0185800_production, 93_LVBus0185801_production, 93_LVBus0185802_consumption, 93_LVBus0185802_production, 93_LVBus0185803_consumption, 93_LVBus0185803_production, 93_LVBus0185804_consumption, 93_LVBus0185804_production, 93_LVBus0185805_consumption, 93_LVBus0185805_production, 93_LVBus0185806_consumption, 93_LVBus0185806_production, 93_LVBus0185809_consumption, 93_LVBus0185809_production, 93_LVBus0185810_consumption, 93_LVBus0185810_production, 93_LVBus0185811_consumption, 93_LVBus0185811_production, 93_LVBus0185812_consumption, 93_LVBus0185812_production, 93_LVBus0185813_production, 93_LVBus0185815_consumption, 93_LVBus0185815_production, 93_LVBus0185816_production, 93_LVBus0185818_consumption, 93_LVBus0185818_production, 93_LVBus0185820_consumption, 93_LVBus0185820_production, 93_LVBus0185821_consumption, 93_LVBus0185821_production, 93_LVBus0185823_production, 93_LVBus0185825_consumption, 93_LVBus0185825_production, 93_LVBus0185826_consumption, 93_LVBus0185826_production, 93_LVBus0185828_consumption, 93_LVBus0185828_production, 93_LVBus0185830_consumption, 93_LVBus0185830_production, 93_LVBus0185831_consumption, 93_LVBus0185831_production, 93_LVBus0185835_production, 93_LVBus0185837_production, 93_LVBus0185839_consumption, 93_LVBus0185839_production, 93_LVBus0185841_production, 93_LVBus0185842_consumption, 93_LVBus0185842_production, 93_LVBus0185843_consumption, 93_LVBus0185843_production, 93_LVBus0185844_production, 93_LVBus0185845_consumption, 93_LVBus0185845_production, 93_LVBus0185846_production, 93_LVBus0185847_production, 93_LVBus0185848_production, 93_LVBus0185850_production, 93_LVBus0185852_consumption, 93_LVBus0185852_production, 93_LVBus0185854_consumption, 93_LVBus0185854_production, 93_LVBus0185856_consumption, 93_LVBus0185856_production, 93_LVBus0185858_consumption, 93_LVBus0185858_production, 93_LVBus0185860_consumption, 93_LVBus0185860_production, 93_LVBus0185861_consumption, 93_LVBus0185861_production, 93_LVBus0185862_production, 93_LVBus0185865_consumption, 93_LVBus0185865_production, 93_LVBus0185866_consumption, 93_LVBus0185866_production, 93_LVBus0185868_consumption, 93_LVBus0185868_production, 93_LVBus0185870_consumption, 93_LVBus0185870_production, 93_LVBus0185872_consumption, 93_LVBus0185872_production, 93_LVBus0185874_consumption, 93_LVBus0185874_production, 93_LVBus0185875_production, 93_LVBus0185877_consumption, 93_LVBus0185877_production, 93_LVBus0185878_consumption, 93_LVBus0185878_production, 93_LVBus0185880_consumption, 93_LVBus0185880_production, 93_LVBus0185881_consumption, 93_LVBus0185881_production, 93_LVBus0185883_consumption, 93_LVBus0185883_production, 93_LVBus1346871_production, 93_LVBus1346872_production, 93_LVBus1371565_consumption, 93_LVBus1371565_production, 93_LVBus1371566_production, 93_LVBus1372286_production, 93_LVBus1372287_production, 93_LVBus1372288_production, 93_LVBus1375062_consumption, 93_LVBus1375062_production, 93_LVBus1375063_consumption, 93_LVBus1375063_production, 93_LVBus1375064_production, 93_LVBus1402525_consumption, 93_LVBus1402525_production, 93_LVBus1404761_consumption, 93_LVBus1404761_production, 93_LVBus1404762_production, 93_LVBus1404763_production, 93_LVBus1418038_consumption, 93_LVBus1418038_production, 93_LVBus1418039_production, 93_MVLV19541_consumption, 93_MVLV19541_production, 93_MVLV33393_production, 93_MVLV41378_consumption, 93_MVLV41378_production, 93_MVLV42522_consumption, 93_MVLV42522_production, 93_MVLV62909_production.

