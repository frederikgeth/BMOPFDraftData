# BMOPF Network Summary: 53_MVFeeder0852

**Generated:** 2026-10-01 23:34:19  
**Findings:** 0 errors · 5 warnings · 446 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 46 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 702 |  |
| line | 655 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 1150 | 2.591 MW, 777.2 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 46 |  |
| switch | 0 |  |
| transformer | 46 | Dyn11×46 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 82 | 81 | 2 | 0 |
| LV_236V | 236.0 V | 620 | 574 | 1148 | 0 |

**Transformer transitions:**

- `53_MVLV31392_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV07741_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV17164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV55670_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV48768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV34784_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV41010_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV14407_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV44886_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV65190_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV22047_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV54591_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV48973_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV28332_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV04499_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV73742_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV39664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV70758_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV76245_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV80372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV28194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV65192_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV11607_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV23075_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV75400_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV65575_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV78424_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV58728_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV76661_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV48004_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV32410_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV27966_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV28182_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV56361_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV77143_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV14718_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV38155_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV03933_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV58622_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV50038_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV55242_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV36631_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV66395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV80266_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV55267_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV39662_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 258 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 702 | 1 | 701 | 0 | 0 | 0 |
| Tier LV_236V | 620 | 46 | 574 | 0 | 0 | 0 |
| Tier MV_11.8kV | 82 | 1 | 81 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 46; skipped invalid branches: 0.

Galvanic zones: 47; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 53_LANME | MV_11.8kV | 82 | 0 | 0 | 46 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2726 declared bus terminals; 2539 mapped line/closed-switch conductor edges; 187 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 5 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 35900.0 | 2.972 | 3450 |
| q_nom | 0.0 | 10800.0 | 2.972 | 3450 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.7 | 2080.0 | 1.474 | 655 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.589 | 46 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 685 of 1150 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493383_consumption' has phase imbalance of 103.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493198_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493263_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1030244_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493540_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493633_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493467_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493371_consumption' has phase imbalance of 277.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493079_consumption' has phase imbalance of 241.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus979745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493413_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493130_consumption' has phase imbalance of 209.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493287_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493541_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1035073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493244_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493231_consumption' has phase imbalance of 257.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493557_consumption' has phase imbalance of 247.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493447_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493642_consumption' has phase imbalance of 288.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493271_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493196_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1026616_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493319_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493568_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493214_consumption' has phase imbalance of 255.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1026609_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493350_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493530_consumption' has phase imbalance of 238.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493567_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493157_consumption' has phase imbalance of 280.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493282_consumption' has phase imbalance of 264.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493058_consumption' has phase imbalance of 176.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493420_consumption' has phase imbalance of 205.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus981318_consumption' has phase imbalance of 24.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493453_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1016204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493098_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493502_consumption' has phase imbalance of 121.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493151_consumption' has phase imbalance of 98.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493237_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493478_consumption' has phase imbalance of 64.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493408_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493217_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493499_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493088_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493651_consumption' has phase imbalance of 129.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493384_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493603_consumption' has phase imbalance of 239.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493415_consumption' has phase imbalance of 272.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493574_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493517_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493452_consumption' has phase imbalance of 282.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493468_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493609_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493482_consumption' has phase imbalance of 294.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493645_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493258_consumption' has phase imbalance of 217.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493083_consumption' has phase imbalance of 191.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493332_consumption' has phase imbalance of 248.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493199_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493343_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493626_consumption' has phase imbalance of 261.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493345_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493419_consumption' has phase imbalance of 191.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493118_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1036727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493075_consumption' has phase imbalance of 162.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493366_consumption' has phase imbalance of 21.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493437_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493398_consumption' has phase imbalance of 145.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493273_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493430_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493253_consumption' has phase imbalance of 280.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493242_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493386_consumption' has phase imbalance of 184.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493126_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493545_consumption' has phase imbalance of 283.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493094_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493093_consumption' has phase imbalance of 135.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493216_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493631_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493320_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493274_consumption' has phase imbalance of 223.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493566_consumption' has phase imbalance of 242.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493389_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493547_consumption' has phase imbalance of 278.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493068_consumption' has phase imbalance of 20.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493232_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493552_consumption' has phase imbalance of 231.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493295_consumption' has phase imbalance of 204.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493240_consumption' has phase imbalance of 25.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493139_consumption' has phase imbalance of 246.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493660_consumption' has phase imbalance of 272.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493649_consumption' has phase imbalance of 289.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493156_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493252_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493248_consumption' has phase imbalance of 251.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493391_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493542_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1030240_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493158_consumption' has phase imbalance of 279.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1025907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493397_consumption' has phase imbalance of 23.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493210_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493084_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493245_consumption' has phase imbalance of 167.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493289_consumption' has phase imbalance of 197.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493602_consumption' has phase imbalance of 211.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493140_consumption' has phase imbalance of 265.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493377_consumption' has phase imbalance of 249.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1035076_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493114_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493302_consumption' has phase imbalance of 109.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493100_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493640_consumption' has phase imbalance of 100.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493548_consumption' has phase imbalance of 274.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493189_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493161_consumption' has phase imbalance of 250.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493487_consumption' has phase imbalance of 241.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493246_consumption' has phase imbalance of 125.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493165_consumption' has phase imbalance of 126.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994213_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493211_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493348_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493082_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493473_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493137_consumption' has phase imbalance of 115.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493525_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493066_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493279_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493507_consumption' has phase imbalance of 125.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493077_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493644_consumption' has phase imbalance of 64.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493040_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493327_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493599_consumption' has phase imbalance of 141.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493121_consumption' has phase imbalance of 232.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus981316_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493658_consumption' has phase imbalance of 259.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493323_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493534_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994211_consumption' has phase imbalance of 186.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493197_consumption' has phase imbalance of 139.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493620_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493556_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493583_consumption' has phase imbalance of 63.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493341_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493092_consumption' has phase imbalance of 277.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus979736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493375_consumption' has phase imbalance of 175.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493433_consumption' has phase imbalance of 274.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493048_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493427_consumption' has phase imbalance of 110.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493615_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493636_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493050_consumption' has phase imbalance of 90.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493662_consumption' has phase imbalance of 260.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493555_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493091_consumption' has phase imbalance of 290.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493260_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493518_consumption' has phase imbalance of 103.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493150_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493471_consumption' has phase imbalance of 227.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493647_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493601_consumption' has phase imbalance of 228.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493107_consumption' has phase imbalance of 290.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493311_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493439_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493464_consumption' has phase imbalance of 259.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493247_consumption' has phase imbalance of 38.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus981313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493363_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493202_consumption' has phase imbalance of 144.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493122_consumption' has phase imbalance of 272.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus979735_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493664_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493564_consumption' has phase imbalance of 262.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus981314_consumption' has phase imbalance of 261.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493051_consumption' has phase imbalance of 205.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus979737_consumption' has phase imbalance of 91.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493174_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493466_consumption' has phase imbalance of 292.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493128_consumption' has phase imbalance of 106.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1030243_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493444_consumption' has phase imbalance of 208.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493146_consumption' has phase imbalance of 98.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493639_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493635_consumption' has phase imbalance of 45.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493553_consumption' has phase imbalance of 234.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493514_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493195_consumption' has phase imbalance of 122.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493395_consumption' has phase imbalance of 243.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493172_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493103_consumption' has phase imbalance of 209.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493056_consumption' has phase imbalance of 100.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493587_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493149_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493099_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493388_consumption' has phase imbalance of 289.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493256_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493379_consumption' has phase imbalance of 40.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493360_consumption' has phase imbalance of 247.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493606_consumption' has phase imbalance of 240.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493591_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493551_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493405_consumption' has phase imbalance of 51.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493155_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493250_consumption' has phase imbalance of 197.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1035074_consumption' has phase imbalance of 250.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493148_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493481_consumption' has phase imbalance of 239.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493465_consumption' has phase imbalance of 219.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493367_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493043_consumption' has phase imbalance of 271.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493390_consumption' has phase imbalance of 270.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493227_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493286_consumption' has phase imbalance of 229.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493435_consumption' has phase imbalance of 258.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493081_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493337_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493454_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus981315_consumption' has phase imbalance of 278.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493562_consumption' has phase imbalance of 263.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493338_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1035075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493638_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493067_consumption' has phase imbalance of 287.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493365_consumption' has phase imbalance of 21.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493243_consumption' has phase imbalance of 254.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1030245_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493370_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493096_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493500_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493335_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493561_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493563_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493305_consumption' has phase imbalance of 229.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493378_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493459_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493597_consumption' has phase imbalance of 282.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493598_consumption' has phase imbalance of 183.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493291_consumption' has phase imbalance of 137.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493531_consumption' has phase imbalance of 29.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493038_consumption' has phase imbalance of 238.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493046_consumption' has phase imbalance of 273.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493334_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493442_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493299_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493443_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493486_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493368_consumption' has phase imbalance of 24.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493131_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1025908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493627_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1030239_consumption' has phase imbalance of 102.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493571_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1026610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493304_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493255_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493313_consumption' has phase imbalance of 244.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493663_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493203_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus981317_consumption' has phase imbalance of 237.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493336_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1031292_consumption' has phase imbalance of 164.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493153_consumption' has phase imbalance of 242.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493361_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493493_consumption' has phase imbalance of 288.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493186_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493321_consumption' has phase imbalance of 285.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1030242_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493300_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus1022436_consumption' has phase imbalance of 172.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493184_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493411_consumption' has phase imbalance of 254.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493080_consumption' has phase imbalance of 99.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493403_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493616_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493614_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493281_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493448_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493485_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493438_consumption' has phase imbalance of 165.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493249_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493488_consumption' has phase imbalance of 278.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493463_consumption' has phase imbalance of 267.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493357_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493410_consumption' has phase imbalance of 242.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493144_consumption' has phase imbalance of 130.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493254_consumption' has phase imbalance of 139.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493666_consumption' has phase imbalance of 286.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493317_consumption' has phase imbalance of 154.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493230_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493340_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493434_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus493238_consumption' has phase imbalance of 129.5%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1150 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus493527' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus493072' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.591 MW |
| Total load Q | 777.2 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 53_MVLV31392_Transformer | 440.0 kVA | 27.3% |
| 53_MVLV07741_Transformer | 275.0 kVA | 13.2% |
| 53_MVLV17164_Transformer | 693.0 kVA | 42.7% |
| 53_MVLV55670_Transformer | 275.0 kVA | 26.6% |
| 53_MVLV48768_Transformer | 693.0 kVA | 34.5% |
| 53_MVLV34784_Transformer | 176.0 kVA | 23.3% |
| 53_MVLV41010_Transformer | 110.0 kVA | 10.6% |
| 53_MVLV14407_Transformer | 176.0 kVA | 28.4% |
| 53_MVLV44886_Transformer | 440.0 kVA | 28.2% |
| 53_MVLV65190_Transformer | 110.0 kVA | 21.2% |
| 53_MVLV22047_Transformer | 176.0 kVA | 7.1% |
| 53_MVLV54591_Transformer | 110.0 kVA | 17.2% |
| 53_MVLV48973_Transformer | 275.0 kVA | 15.0% |
| 53_MVLV28332_Transformer | 176.0 kVA | 17.7% |
| 53_MVLV04499_Transformer | 275.0 kVA | 18.8% |
| 53_MVLV73742_Transformer | 176.0 kVA | 12.5% |
| 53_MVLV39664_Transformer | 275.0 kVA | 26.3% |
| 53_MVLV70758_Transformer | 110.0 kVA | 1.8% |
| 53_MVLV76245_Transformer | 440.0 kVA | 20.4% |
| 53_MVLV80372_Transformer | 275.0 kVA | 22.3% |
| 53_MVLV28194_Transformer | 176.0 kVA | 20.2% |
| 53_MVLV65192_Transformer | 110.0 kVA | 15.1% |
| 53_MVLV11607_Transformer | 440.0 kVA | 18.7% |
| 53_MVLV23075_Transformer | 176.0 kVA | 19.0% |
| 53_MVLV75400_Transformer | 110.0 kVA | 6.3% |
| 53_MVLV65575_Transformer | 176.0 kVA | 2.5% |
| 53_MVLV78424_Transformer | 275.0 kVA | 21.2% |
| 53_MVLV58728_Transformer | 440.0 kVA | 28.8% |
| 53_MVLV76661_Transformer | 176.0 kVA | 32.2% |
| 53_MVLV48004_Transformer | 275.0 kVA | 24.6% |
| 53_MVLV32410_Transformer | 176.0 kVA | 32.9% |
| 53_MVLV27966_Transformer | 176.0 kVA | 13.8% |
| 53_MVLV28182_Transformer | 176.0 kVA | 18.4% |
| 53_MVLV56361_Transformer | 110.0 kVA | 10.8% |
| 53_MVLV77143_Transformer | 110.0 kVA | 17.8% |
| 53_MVLV14718_Transformer | 176.0 kVA | 20.7% |
| 53_MVLV38155_Transformer | 176.0 kVA | 13.9% |
| 53_MVLV03933_Transformer | 275.0 kVA | 21.5% |
| 53_MVLV58622_Transformer | 440.0 kVA | 18.7% |
| 53_MVLV50038_Transformer | 110.0 kVA | 28.3% |
| 53_MVLV55242_Transformer | 110.0 kVA | 36.4% |
| 53_MVLV36631_Transformer | 110.0 kVA | 22.5% |
| 53_MVLV66395_Transformer | 440.0 kVA | 33.0% |
| 53_MVLV80266_Transformer | 275.0 kVA | 13.9% |
| 53_MVLV55267_Transformer | 275.0 kVA | 39.1% |
| 53_MVLV39662_Transformer | 176.0 kVA | 36.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.59 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '53_LVBus493527' (LV, 0.24 kV) has an electrical reach of 8.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 702 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 702 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 46 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 82 |
| LV_236V | 4-wire | 620 / 620 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 620 |
| Neutral branches | 574 |
| Grounding points | 46 |
| Neutral sections | 46 |
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
| 11.78 kV | 82 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 53 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 47 |
| Islands without voltage reference | 0 |
| Line impedance spread | 740.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 620 / 82 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 686 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 686 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus1016204_production, 53_LVBus1022436_production, 53_LVBus1025907_production, 53_LVBus1025908_production, 53_LVBus1026609_production, 53_LVBus1026610_production, 53_LVBus1026611_consumption, 53_LVBus1026611_production, 53_LVBus1026612_consumption, 53_LVBus1026612_production, 53_LVBus1026613_consumption, 53_LVBus1026613_production, 53_LVBus1026614_consumption, 53_LVBus1026614_production, 53_LVBus1026615_production, 53_LVBus1026616_production, 53_LVBus1026617_consumption, 53_LVBus1026617_production, 53_LVBus1028404_consumption, 53_LVBus1028404_production, 53_LVBus1030239_production, 53_LVBus1030240_production, 53_LVBus1030241_production, 53_LVBus1030242_production, 53_LVBus1030243_production, 53_LVBus1030244_production, 53_LVBus1030245_production, 53_LVBus1031291_production, 53_LVBus1031292_production, 53_LVBus1035073_production, 53_LVBus1035074_production, 53_LVBus1035075_production, 53_LVBus1035076_production, 53_LVBus1035077_consumption, 53_LVBus1035077_production, 53_LVBus1035078_consumption, 53_LVBus1035078_production, 53_LVBus1035079_consumption, 53_LVBus1035079_production, 53_LVBus1036727_production, 53_LVBus493038_production, 53_LVBus493039_consumption, 53_LVBus493039_production, 53_LVBus493040_production, 53_LVBus493041_production, 53_LVBus493042_production, 53_LVBus493043_production, 53_LVBus493044_production, 53_LVBus493045_production, 53_LVBus493046_production, 53_LVBus493047_production, 53_LVBus493048_production, 53_LVBus493049_production, 53_LVBus493050_production, 53_LVBus493051_production, 53_LVBus493053_consumption, 53_LVBus493053_production, 53_LVBus493054_consumption, 53_LVBus493054_production, 53_LVBus493055_production, 53_LVBus493056_production, 53_LVBus493057_consumption, 53_LVBus493057_production, 53_LVBus493058_production, 53_LVBus493059_production, 53_LVBus493060_production, 53_LVBus493061_consumption, 53_LVBus493061_production, 53_LVBus493062_production, 53_LVBus493064_consumption, 53_LVBus493064_production, 53_LVBus493065_consumption, 53_LVBus493065_production, 53_LVBus493066_production, 53_LVBus493067_production, 53_LVBus493068_production, 53_LVBus493069_production, 53_LVBus493070_consumption, 53_LVBus493070_production, 53_LVBus493072_production, 53_LVBus493074_consumption, 53_LVBus493074_production, 53_LVBus493075_production, 53_LVBus493076_production, 53_LVBus493077_production, 53_LVBus493078_production, 53_LVBus493079_production, 53_LVBus493080_production, 53_LVBus493081_production, 53_LVBus493082_production, 53_LVBus493083_production, 53_LVBus493084_production, 53_LVBus493085_consumption, 53_LVBus493085_production, 53_LVBus493086_production, 53_LVBus493087_consumption, 53_LVBus493087_production, 53_LVBus493088_production, 53_LVBus493090_production, 53_LVBus493091_production, 53_LVBus493092_production, 53_LVBus493093_production, 53_LVBus493094_production, 53_LVBus493096_production, 53_LVBus493097_production, 53_LVBus493098_production, 53_LVBus493099_production, 53_LVBus493100_production, 53_LVBus493101_production, 53_LVBus493102_production, 53_LVBus493103_production, 53_LVBus493104_production, 53_LVBus493107_production, 53_LVBus493109_consumption, 53_LVBus493109_production, 53_LVBus493110_consumption, 53_LVBus493110_production, 53_LVBus493111_consumption, 53_LVBus493111_production, 53_LVBus493112_production, 53_LVBus493113_production, 53_LVBus493114_production, 53_LVBus493118_production, 53_LVBus493120_consumption, 53_LVBus493120_production, 53_LVBus493121_production, 53_LVBus493122_production, 53_LVBus493123_production, 53_LVBus493124_production, 53_LVBus493126_production, 53_LVBus493127_consumption, 53_LVBus493127_production, 53_LVBus493128_production, 53_LVBus493129_production, 53_LVBus493130_production, 53_LVBus493131_production, 53_LVBus493132_production, 53_LVBus493133_production, 53_LVBus493135_production, 53_LVBus493136_production, 53_LVBus493137_production, 53_LVBus493138_production, 53_LVBus493139_production, 53_LVBus493140_production, 53_LVBus493141_production, 53_LVBus493142_production, 53_LVBus493144_production, 53_LVBus493145_production, 53_LVBus493146_production, 53_LVBus493147_production, 53_LVBus493148_production, 53_LVBus493149_production, 53_LVBus493150_production, 53_LVBus493151_production, 53_LVBus493152_consumption, 53_LVBus493152_production, 53_LVBus493153_production, 53_LVBus493154_production, 53_LVBus493155_production, 53_LVBus493156_production, 53_LVBus493157_production, 53_LVBus493158_production, 53_LVBus493159_production, 53_LVBus493160_production, 53_LVBus493161_production, 53_LVBus493162_production, 53_LVBus493163_production, 53_LVBus493164_production, 53_LVBus493165_production, 53_LVBus493167_production, 53_LVBus493168_production, 53_LVBus493170_production, 53_LVBus493172_production, 53_LVBus493173_consumption, 53_LVBus493173_production, 53_LVBus493174_production, 53_LVBus493175_consumption, 53_LVBus493175_production, 53_LVBus493176_production, 53_LVBus493177_production, 53_LVBus493178_production, 53_LVBus493179_production, 53_LVBus493180_production, 53_LVBus493182_production, 53_LVBus493184_production, 53_LVBus493185_consumption, 53_LVBus493185_production, 53_LVBus493186_production, 53_LVBus493187_production, 53_LVBus493189_production, 53_LVBus493190_consumption, 53_LVBus493190_production, 53_LVBus493191_consumption, 53_LVBus493191_production, 53_LVBus493193_production, 53_LVBus493194_consumption, 53_LVBus493194_production, 53_LVBus493195_production, 53_LVBus493196_production, 53_LVBus493197_production, 53_LVBus493198_production, 53_LVBus493199_production, 53_LVBus493200_production, 53_LVBus493202_production, 53_LVBus493203_production, 53_LVBus493205_consumption, 53_LVBus493205_production, 53_LVBus493206_consumption, 53_LVBus493206_production, 53_LVBus493207_consumption, 53_LVBus493207_production, 53_LVBus493208_production, 53_LVBus493209_consumption, 53_LVBus493209_production, 53_LVBus493210_production, 53_LVBus493211_production, 53_LVBus493212_production, 53_LVBus493213_consumption, 53_LVBus493213_production, 53_LVBus493214_production, 53_LVBus493215_consumption, 53_LVBus493215_production, 53_LVBus493216_production, 53_LVBus493217_production, 53_LVBus493218_production, 53_LVBus493220_consumption, 53_LVBus493220_production, 53_LVBus493221_consumption, 53_LVBus493221_production, 53_LVBus493222_production, 53_LVBus493223_consumption, 53_LVBus493223_production, 53_LVBus493224_production, 53_LVBus493226_consumption, 53_LVBus493226_production, 53_LVBus493227_production, 53_LVBus493228_production, 53_LVBus493229_production, 53_LVBus493230_production, 53_LVBus493231_production, 53_LVBus493232_production, 53_LVBus493233_production, 53_LVBus493234_production, 53_LVBus493235_production, 53_LVBus493237_production, 53_LVBus493238_production, 53_LVBus493239_production, 53_LVBus493240_production, 53_LVBus493242_production, 53_LVBus493243_production, 53_LVBus493244_production, 53_LVBus493245_production, 53_LVBus493246_production, 53_LVBus493247_production, 53_LVBus493248_production, 53_LVBus493249_production, 53_LVBus493250_production, 53_LVBus493251_production, 53_LVBus493252_production, 53_LVBus493253_production, 53_LVBus493254_production, 53_LVBus493255_production, 53_LVBus493256_production, 53_LVBus493258_production, 53_LVBus493259_consumption, 53_LVBus493259_production, 53_LVBus493260_production, 53_LVBus493261_production, 53_LVBus493262_consumption, 53_LVBus493262_production, 53_LVBus493263_production, 53_LVBus493265_consumption, 53_LVBus493265_production, 53_LVBus493266_production, 53_LVBus493267_consumption, 53_LVBus493267_production, 53_LVBus493268_consumption, 53_LVBus493268_production, 53_LVBus493269_consumption, 53_LVBus493269_production, 53_LVBus493270_production, 53_LVBus493271_production, 53_LVBus493272_production, 53_LVBus493273_production, 53_LVBus493274_production, 53_LVBus493275_production, 53_LVBus493276_production, 53_LVBus493278_consumption, 53_LVBus493278_production, 53_LVBus493279_production, 53_LVBus493280_consumption, 53_LVBus493280_production, 53_LVBus493281_production, 53_LVBus493282_production, 53_LVBus493283_consumption, 53_LVBus493283_production, 53_LVBus493285_consumption, 53_LVBus493285_production, 53_LVBus493286_production, 53_LVBus493287_production, 53_LVBus493288_production, 53_LVBus493289_production, 53_LVBus493291_production, 53_LVBus493293_production, 53_LVBus493294_production, 53_LVBus493295_production, 53_LVBus493299_production, 53_LVBus493300_production, 53_LVBus493302_production, 53_LVBus493303_production, 53_LVBus493304_production, 53_LVBus493305_production, 53_LVBus493307_production, 53_LVBus493308_consumption, 53_LVBus493308_production, 53_LVBus493309_consumption, 53_LVBus493309_production, 53_LVBus493310_consumption, 53_LVBus493310_production, 53_LVBus493311_production, 53_LVBus493312_consumption, 53_LVBus493312_production, 53_LVBus493313_production, 53_LVBus493314_production, 53_LVBus493315_production, 53_LVBus493316_consumption, 53_LVBus493316_production, 53_LVBus493317_production, 53_LVBus493318_production, 53_LVBus493319_production, 53_LVBus493320_production, 53_LVBus493321_production, 53_LVBus493323_production, 53_LVBus493325_production, 53_LVBus493326_production, 53_LVBus493327_production, 53_LVBus493328_consumption, 53_LVBus493328_production, 53_LVBus493329_consumption, 53_LVBus493329_production, 53_LVBus493330_production, 53_LVBus493331_consumption, 53_LVBus493331_production, 53_LVBus493332_production, 53_LVBus493333_production, 53_LVBus493334_production, 53_LVBus493335_production, 53_LVBus493336_production, 53_LVBus493337_production, 53_LVBus493338_production, 53_LVBus493339_production, 53_LVBus493340_production, 53_LVBus493341_production, 53_LVBus493343_production, 53_LVBus493345_production, 53_LVBus493347_consumption, 53_LVBus493347_production, 53_LVBus493348_production, 53_LVBus493349_production, 53_LVBus493350_production, 53_LVBus493351_production, 53_LVBus493352_consumption, 53_LVBus493352_production, 53_LVBus493353_consumption, 53_LVBus493353_production, 53_LVBus493354_production, 53_LVBus493356_production, 53_LVBus493357_production, 53_LVBus493358_production, 53_LVBus493359_production, 53_LVBus493360_production, 53_LVBus493361_production, 53_LVBus493363_production, 53_LVBus493364_production, 53_LVBus493365_production, 53_LVBus493366_production, 53_LVBus493367_production, 53_LVBus493368_production, 53_LVBus493370_production, 53_LVBus493371_production, 53_LVBus493372_production, 53_LVBus493374_production, 53_LVBus493375_production, 53_LVBus493376_production, 53_LVBus493377_production, 53_LVBus493378_production, 53_LVBus493379_production, 53_LVBus493381_production, 53_LVBus493383_production, 53_LVBus493384_production, 53_LVBus493385_consumption, 53_LVBus493385_production, 53_LVBus493386_production, 53_LVBus493387_production, 53_LVBus493388_production, 53_LVBus493389_production, 53_LVBus493390_production, 53_LVBus493391_production, 53_LVBus493393_consumption, 53_LVBus493393_production, 53_LVBus493395_production, 53_LVBus493397_production, 53_LVBus493398_production, 53_LVBus493400_production, 53_LVBus493402_consumption, 53_LVBus493402_production, 53_LVBus493403_production, 53_LVBus493405_production, 53_LVBus493407_consumption, 53_LVBus493407_production, 53_LVBus493408_production, 53_LVBus493409_production, 53_LVBus493410_production, 53_LVBus493411_production, 53_LVBus493412_production, 53_LVBus493413_production, 53_LVBus493414_production, 53_LVBus493415_production, 53_LVBus493417_production, 53_LVBus493418_consumption, 53_LVBus493418_production, 53_LVBus493419_production, 53_LVBus493420_production, 53_LVBus493422_consumption, 53_LVBus493422_production, 53_LVBus493423_production, 53_LVBus493424_consumption, 53_LVBus493424_production, 53_LVBus493425_production, 53_LVBus493427_production, 53_LVBus493429_production, 53_LVBus493430_production, 53_LVBus493431_consumption, 53_LVBus493431_production, 53_LVBus493433_production, 53_LVBus493434_production, 53_LVBus493435_production, 53_LVBus493436_production, 53_LVBus493437_production, 53_LVBus493438_production, 53_LVBus493439_production, 53_LVBus493441_consumption, 53_LVBus493441_production, 53_LVBus493442_production, 53_LVBus493443_production, 53_LVBus493444_production, 53_LVBus493445_production, 53_LVBus493446_production, 53_LVBus493447_production, 53_LVBus493448_production, 53_LVBus493449_production, 53_LVBus493450_production, 53_LVBus493451_production, 53_LVBus493452_production, 53_LVBus493453_production, 53_LVBus493454_production, 53_LVBus493456_production, 53_LVBus493457_production, 53_LVBus493459_production, 53_LVBus493460_production, 53_LVBus493461_production, 53_LVBus493462_production, 53_LVBus493463_production, 53_LVBus493464_production, 53_LVBus493465_production, 53_LVBus493466_production, 53_LVBus493467_production, 53_LVBus493468_production, 53_LVBus493470_production, 53_LVBus493471_production, 53_LVBus493472_consumption, 53_LVBus493472_production, 53_LVBus493473_production, 53_LVBus493474_consumption, 53_LVBus493474_production, 53_LVBus493475_consumption, 53_LVBus493475_production, 53_LVBus493478_production, 53_LVBus493480_production, 53_LVBus493481_production, 53_LVBus493482_production, 53_LVBus493483_production, 53_LVBus493485_production, 53_LVBus493486_production, 53_LVBus493487_production, 53_LVBus493488_production, 53_LVBus493489_consumption, 53_LVBus493489_production, 53_LVBus493490_production, 53_LVBus493491_production, 53_LVBus493493_production, 53_LVBus493494_production, 53_LVBus493496_consumption, 53_LVBus493496_production, 53_LVBus493498_consumption, 53_LVBus493498_production, 53_LVBus493499_production, 53_LVBus493500_production, 53_LVBus493501_production, 53_LVBus493502_production, 53_LVBus493503_production, 53_LVBus493504_consumption, 53_LVBus493504_production, 53_LVBus493505_consumption, 53_LVBus493505_production, 53_LVBus493506_production, 53_LVBus493507_production, 53_LVBus493509_production, 53_LVBus493511_consumption, 53_LVBus493511_production, 53_LVBus493513_production, 53_LVBus493514_production, 53_LVBus493516_consumption, 53_LVBus493516_production, 53_LVBus493517_production, 53_LVBus493518_production, 53_LVBus493520_consumption, 53_LVBus493520_production, 53_LVBus493521_production, 53_LVBus493522_production, 53_LVBus493523_production, 53_LVBus493524_consumption, 53_LVBus493524_production, 53_LVBus493525_production, 53_LVBus493527_production, 53_LVBus493529_production, 53_LVBus493530_production, 53_LVBus493531_production, 53_LVBus493532_production, 53_LVBus493533_production, 53_LVBus493534_production, 53_LVBus493536_production, 53_LVBus493537_production, 53_LVBus493538_production, 53_LVBus493539_production, 53_LVBus493540_production, 53_LVBus493541_production, 53_LVBus493542_production, 53_LVBus493543_consumption, 53_LVBus493543_production, 53_LVBus493545_production, 53_LVBus493546_production, 53_LVBus493547_production, 53_LVBus493548_production, 53_LVBus493550_consumption, 53_LVBus493550_production, 53_LVBus493551_production, 53_LVBus493552_production, 53_LVBus493553_production, 53_LVBus493554_consumption, 53_LVBus493554_production, 53_LVBus493555_production, 53_LVBus493556_production, 53_LVBus493557_production, 53_LVBus493559_consumption, 53_LVBus493559_production, 53_LVBus493560_consumption, 53_LVBus493560_production, 53_LVBus493561_production, 53_LVBus493562_production, 53_LVBus493563_production, 53_LVBus493564_production, 53_LVBus493565_production, 53_LVBus493566_production, 53_LVBus493567_production, 53_LVBus493568_production, 53_LVBus493570_consumption, 53_LVBus493570_production, 53_LVBus493571_production, 53_LVBus493572_consumption, 53_LVBus493572_production, 53_LVBus493573_consumption, 53_LVBus493573_production, 53_LVBus493574_production, 53_LVBus493575_production, 53_LVBus493577_consumption, 53_LVBus493577_production, 53_LVBus493578_consumption, 53_LVBus493578_production, 53_LVBus493579_production, 53_LVBus493580_consumption, 53_LVBus493580_production, 53_LVBus493581_production, 53_LVBus493582_production, 53_LVBus493583_production, 53_LVBus493584_consumption, 53_LVBus493584_production, 53_LVBus493586_consumption, 53_LVBus493586_production, 53_LVBus493587_production, 53_LVBus493589_consumption, 53_LVBus493589_production, 53_LVBus493590_production, 53_LVBus493591_production, 53_LVBus493593_production, 53_LVBus493597_production, 53_LVBus493598_production, 53_LVBus493599_production, 53_LVBus493600_consumption, 53_LVBus493600_production, 53_LVBus493601_production, 53_LVBus493602_production, 53_LVBus493603_production, 53_LVBus493604_production, 53_LVBus493606_production, 53_LVBus493607_production, 53_LVBus493608_production, 53_LVBus493609_production, 53_LVBus493610_production, 53_LVBus493611_consumption, 53_LVBus493611_production, 53_LVBus493612_consumption, 53_LVBus493612_production, 53_LVBus493613_consumption, 53_LVBus493613_production, 53_LVBus493614_production, 53_LVBus493615_production, 53_LVBus493616_production, 53_LVBus493618_production, 53_LVBus493619_production, 53_LVBus493620_production, 53_LVBus493622_production, 53_LVBus493623_production, 53_LVBus493624_consumption, 53_LVBus493624_production, 53_LVBus493625_consumption, 53_LVBus493625_production, 53_LVBus493626_production, 53_LVBus493627_production, 53_LVBus493629_production, 53_LVBus493631_production, 53_LVBus493633_production, 53_LVBus493635_production, 53_LVBus493636_production, 53_LVBus493638_production, 53_LVBus493639_production, 53_LVBus493640_production, 53_LVBus493641_consumption, 53_LVBus493641_production, 53_LVBus493642_production, 53_LVBus493643_production, 53_LVBus493644_production, 53_LVBus493645_production, 53_LVBus493646_production, 53_LVBus493647_production, 53_LVBus493649_production, 53_LVBus493650_production, 53_LVBus493651_production, 53_LVBus493652_production, 53_LVBus493653_production, 53_LVBus493654_consumption, 53_LVBus493654_production, 53_LVBus493656_production, 53_LVBus493657_consumption, 53_LVBus493657_production, 53_LVBus493658_production, 53_LVBus493660_production, 53_LVBus493661_production, 53_LVBus493662_production, 53_LVBus493663_production, 53_LVBus493664_production, 53_LVBus493665_production, 53_LVBus493666_production, 53_LVBus979734_consumption, 53_LVBus979734_production, 53_LVBus979735_production, 53_LVBus979736_production, 53_LVBus979737_production, 53_LVBus979745_production, 53_LVBus981313_production, 53_LVBus981314_production, 53_LVBus981315_production, 53_LVBus981316_production, 53_LVBus981317_production, 53_LVBus981318_production, 53_LVBus991173_production, 53_LVBus994208_production, 53_LVBus994209_consumption, 53_LVBus994209_production, 53_LVBus994210_consumption, 53_LVBus994210_production, 53_LVBus994211_production, 53_LVBus994212_production, 53_LVBus994213_production, 53_MVLV06965_consumption, 53_MVLV06965_production.

## 9. Data Quality Summary

**Total findings:** 451 (0 errors, 5 warnings, 446 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  5 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  685 of 1150 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.59 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  686 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493383_consumption`  
  Load '53_LVBus493383_consumption' has phase imbalance of 103.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493182_consumption`  
  Load '53_LVBus493182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493198_consumption`  
  Load '53_LVBus493198_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493263_consumption`  
  Load '53_LVBus493263_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1030244_consumption`  
  Load '53_LVBus1030244_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493540_consumption`  
  Load '53_LVBus493540_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493633_consumption`  
  Load '53_LVBus493633_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493467_consumption`  
  Load '53_LVBus493467_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493229_consumption`  
  Load '53_LVBus493229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493371_consumption`  
  Load '53_LVBus493371_consumption' has phase imbalance of 277.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493104_consumption`  
  Load '53_LVBus493104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493451_consumption`  
  Load '53_LVBus493451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493170_consumption`  
  Load '53_LVBus493170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493079_consumption`  
  Load '53_LVBus493079_consumption' has phase imbalance of 241.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493086_consumption`  
  Load '53_LVBus493086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493275_consumption`  
  Load '53_LVBus493275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus979745_consumption`  
  Load '53_LVBus979745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493090_consumption`  
  Load '53_LVBus493090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493413_consumption`  
  Load '53_LVBus493413_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493622_consumption`  
  Load '53_LVBus493622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493130_consumption`  
  Load '53_LVBus493130_consumption' has phase imbalance of 209.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493287_consumption`  
  Load '53_LVBus493287_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493541_consumption`  
  Load '53_LVBus493541_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1035073_consumption`  
  Load '53_LVBus1035073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493244_consumption`  
  Load '53_LVBus493244_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493231_consumption`  
  Load '53_LVBus493231_consumption' has phase imbalance of 257.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493619_consumption`  
  Load '53_LVBus493619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493557_consumption`  
  Load '53_LVBus493557_consumption' has phase imbalance of 247.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493447_consumption`  
  Load '53_LVBus493447_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493521_consumption`  
  Load '53_LVBus493521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493642_consumption`  
  Load '53_LVBus493642_consumption' has phase imbalance of 288.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493271_consumption`  
  Load '53_LVBus493271_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493196_consumption`  
  Load '53_LVBus493196_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994212_consumption`  
  Load '53_LVBus994212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1026616_consumption`  
  Load '53_LVBus1026616_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493319_consumption`  
  Load '53_LVBus493319_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493356_consumption`  
  Load '53_LVBus493356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493568_consumption`  
  Load '53_LVBus493568_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493214_consumption`  
  Load '53_LVBus493214_consumption' has phase imbalance of 255.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1026609_consumption`  
  Load '53_LVBus1026609_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493266_consumption`  
  Load '53_LVBus493266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493350_consumption`  
  Load '53_LVBus493350_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493530_consumption`  
  Load '53_LVBus493530_consumption' has phase imbalance of 238.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493567_consumption`  
  Load '53_LVBus493567_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493157_consumption`  
  Load '53_LVBus493157_consumption' has phase imbalance of 280.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493212_consumption`  
  Load '53_LVBus493212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493282_consumption`  
  Load '53_LVBus493282_consumption' has phase imbalance of 264.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493058_consumption`  
  Load '53_LVBus493058_consumption' has phase imbalance of 176.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493420_consumption`  
  Load '53_LVBus493420_consumption' has phase imbalance of 205.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus981318_consumption`  
  Load '53_LVBus981318_consumption' has phase imbalance of 24.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493102_consumption`  
  Load '53_LVBus493102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493453_consumption`  
  Load '53_LVBus493453_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1016204_consumption`  
  Load '53_LVBus1016204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493098_consumption`  
  Load '53_LVBus493098_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493502_consumption`  
  Load '53_LVBus493502_consumption' has phase imbalance of 121.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493151_consumption`  
  Load '53_LVBus493151_consumption' has phase imbalance of 98.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493646_consumption`  
  Load '53_LVBus493646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493237_consumption`  
  Load '53_LVBus493237_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493538_consumption`  
  Load '53_LVBus493538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493478_consumption`  
  Load '53_LVBus493478_consumption' has phase imbalance of 64.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493364_consumption`  
  Load '53_LVBus493364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493041_consumption`  
  Load '53_LVBus493041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493408_consumption`  
  Load '53_LVBus493408_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493217_consumption`  
  Load '53_LVBus493217_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493270_consumption`  
  Load '53_LVBus493270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493333_consumption`  
  Load '53_LVBus493333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493499_consumption`  
  Load '53_LVBus493499_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493088_consumption`  
  Load '53_LVBus493088_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493651_consumption`  
  Load '53_LVBus493651_consumption' has phase imbalance of 129.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493384_consumption`  
  Load '53_LVBus493384_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493603_consumption`  
  Load '53_LVBus493603_consumption' has phase imbalance of 239.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493415_consumption`  
  Load '53_LVBus493415_consumption' has phase imbalance of 272.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493446_consumption`  
  Load '53_LVBus493446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493574_consumption`  
  Load '53_LVBus493574_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493517_consumption`  
  Load '53_LVBus493517_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493452_consumption`  
  Load '53_LVBus493452_consumption' has phase imbalance of 282.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493288_consumption`  
  Load '53_LVBus493288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493468_consumption`  
  Load '53_LVBus493468_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493609_consumption`  
  Load '53_LVBus493609_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493276_consumption`  
  Load '53_LVBus493276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493482_consumption`  
  Load '53_LVBus493482_consumption' has phase imbalance of 294.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493645_consumption`  
  Load '53_LVBus493645_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493258_consumption`  
  Load '53_LVBus493258_consumption' has phase imbalance of 217.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493083_consumption`  
  Load '53_LVBus493083_consumption' has phase imbalance of 191.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493112_consumption`  
  Load '53_LVBus493112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493332_consumption`  
  Load '53_LVBus493332_consumption' has phase imbalance of 248.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493199_consumption`  
  Load '53_LVBus493199_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493343_consumption`  
  Load '53_LVBus493343_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493626_consumption`  
  Load '53_LVBus493626_consumption' has phase imbalance of 261.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493345_consumption`  
  Load '53_LVBus493345_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493234_consumption`  
  Load '53_LVBus493234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493419_consumption`  
  Load '53_LVBus493419_consumption' has phase imbalance of 191.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493097_consumption`  
  Load '53_LVBus493097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493118_consumption`  
  Load '53_LVBus493118_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1036727_consumption`  
  Load '53_LVBus1036727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493409_consumption`  
  Load '53_LVBus493409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493075_consumption`  
  Load '53_LVBus493075_consumption' has phase imbalance of 162.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493366_consumption`  
  Load '53_LVBus493366_consumption' has phase imbalance of 21.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493653_consumption`  
  Load '53_LVBus493653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493575_consumption`  
  Load '53_LVBus493575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493141_consumption`  
  Load '53_LVBus493141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493437_consumption`  
  Load '53_LVBus493437_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493398_consumption`  
  Load '53_LVBus493398_consumption' has phase imbalance of 145.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493273_consumption`  
  Load '53_LVBus493273_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493494_consumption`  
  Load '53_LVBus493494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493430_consumption`  
  Load '53_LVBus493430_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493253_consumption`  
  Load '53_LVBus493253_consumption' has phase imbalance of 280.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493359_consumption`  
  Load '53_LVBus493359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493242_consumption`  
  Load '53_LVBus493242_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493386_consumption`  
  Load '53_LVBus493386_consumption' has phase imbalance of 184.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493126_consumption`  
  Load '53_LVBus493126_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493167_consumption`  
  Load '53_LVBus493167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493135_consumption`  
  Load '53_LVBus493135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493545_consumption`  
  Load '53_LVBus493545_consumption' has phase imbalance of 283.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493661_consumption`  
  Load '53_LVBus493661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493094_consumption`  
  Load '53_LVBus493094_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493376_consumption`  
  Load '53_LVBus493376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493093_consumption`  
  Load '53_LVBus493093_consumption' has phase imbalance of 135.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493216_consumption`  
  Load '53_LVBus493216_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493631_consumption`  
  Load '53_LVBus493631_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493320_consumption`  
  Load '53_LVBus493320_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493274_consumption`  
  Load '53_LVBus493274_consumption' has phase imbalance of 223.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493566_consumption`  
  Load '53_LVBus493566_consumption' has phase imbalance of 242.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493389_consumption`  
  Load '53_LVBus493389_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493547_consumption`  
  Load '53_LVBus493547_consumption' has phase imbalance of 278.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493068_consumption`  
  Load '53_LVBus493068_consumption' has phase imbalance of 20.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493232_consumption`  
  Load '53_LVBus493232_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493552_consumption`  
  Load '53_LVBus493552_consumption' has phase imbalance of 231.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493295_consumption`  
  Load '53_LVBus493295_consumption' has phase imbalance of 204.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493581_consumption`  
  Load '53_LVBus493581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493240_consumption`  
  Load '53_LVBus493240_consumption' has phase imbalance of 25.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493139_consumption`  
  Load '53_LVBus493139_consumption' has phase imbalance of 246.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493533_consumption`  
  Load '53_LVBus493533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493490_consumption`  
  Load '53_LVBus493490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493660_consumption`  
  Load '53_LVBus493660_consumption' has phase imbalance of 272.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493649_consumption`  
  Load '53_LVBus493649_consumption' has phase imbalance of 289.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493462_consumption`  
  Load '53_LVBus493462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493294_consumption`  
  Load '53_LVBus493294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493156_consumption`  
  Load '53_LVBus493156_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493252_consumption`  
  Load '53_LVBus493252_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493060_consumption`  
  Load '53_LVBus493060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493272_consumption`  
  Load '53_LVBus493272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493248_consumption`  
  Load '53_LVBus493248_consumption' has phase imbalance of 251.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493391_consumption`  
  Load '53_LVBus493391_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493436_consumption`  
  Load '53_LVBus493436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493187_consumption`  
  Load '53_LVBus493187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493542_consumption`  
  Load '53_LVBus493542_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1030240_consumption`  
  Load '53_LVBus1030240_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493045_consumption`  
  Load '53_LVBus493045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493158_consumption`  
  Load '53_LVBus493158_consumption' has phase imbalance of 279.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991173_consumption`  
  Load '53_LVBus991173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493414_consumption`  
  Load '53_LVBus493414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1025907_consumption`  
  Load '53_LVBus1025907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493397_consumption`  
  Load '53_LVBus493397_consumption' has phase imbalance of 23.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493210_consumption`  
  Load '53_LVBus493210_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493501_consumption`  
  Load '53_LVBus493501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493084_consumption`  
  Load '53_LVBus493084_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493245_consumption`  
  Load '53_LVBus493245_consumption' has phase imbalance of 167.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994208_consumption`  
  Load '53_LVBus994208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493101_consumption`  
  Load '53_LVBus493101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493289_consumption`  
  Load '53_LVBus493289_consumption' has phase imbalance of 197.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493602_consumption`  
  Load '53_LVBus493602_consumption' has phase imbalance of 211.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493140_consumption`  
  Load '53_LVBus493140_consumption' has phase imbalance of 265.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493377_consumption`  
  Load '53_LVBus493377_consumption' has phase imbalance of 249.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493423_consumption`  
  Load '53_LVBus493423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1035076_consumption`  
  Load '53_LVBus1035076_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493114_consumption`  
  Load '53_LVBus493114_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493302_consumption`  
  Load '53_LVBus493302_consumption' has phase imbalance of 109.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493100_consumption`  
  Load '53_LVBus493100_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493162_consumption`  
  Load '53_LVBus493162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493640_consumption`  
  Load '53_LVBus493640_consumption' has phase imbalance of 100.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493548_consumption`  
  Load '53_LVBus493548_consumption' has phase imbalance of 274.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493189_consumption`  
  Load '53_LVBus493189_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493161_consumption`  
  Load '53_LVBus493161_consumption' has phase imbalance of 250.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493487_consumption`  
  Load '53_LVBus493487_consumption' has phase imbalance of 241.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493246_consumption`  
  Load '53_LVBus493246_consumption' has phase imbalance of 125.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493461_consumption`  
  Load '53_LVBus493461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493165_consumption`  
  Load '53_LVBus493165_consumption' has phase imbalance of 126.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493618_consumption`  
  Load '53_LVBus493618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493483_consumption`  
  Load '53_LVBus493483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994213_consumption`  
  Load '53_LVBus994213_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493211_consumption`  
  Load '53_LVBus493211_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493348_consumption`  
  Load '53_LVBus493348_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493082_consumption`  
  Load '53_LVBus493082_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493129_consumption`  
  Load '53_LVBus493129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493473_consumption`  
  Load '53_LVBus493473_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493137_consumption`  
  Load '53_LVBus493137_consumption' has phase imbalance of 115.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493525_consumption`  
  Load '53_LVBus493525_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493218_consumption`  
  Load '53_LVBus493218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493123_consumption`  
  Load '53_LVBus493123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493078_consumption`  
  Load '53_LVBus493078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493066_consumption`  
  Load '53_LVBus493066_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493069_consumption`  
  Load '53_LVBus493069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493279_consumption`  
  Load '53_LVBus493279_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493374_consumption`  
  Load '53_LVBus493374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493507_consumption`  
  Load '53_LVBus493507_consumption' has phase imbalance of 125.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493582_consumption`  
  Load '53_LVBus493582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493233_consumption`  
  Load '53_LVBus493233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493077_consumption`  
  Load '53_LVBus493077_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493644_consumption`  
  Load '53_LVBus493644_consumption' has phase imbalance of 64.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493330_consumption`  
  Load '53_LVBus493330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493040_consumption`  
  Load '53_LVBus493040_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493327_consumption`  
  Load '53_LVBus493327_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493599_consumption`  
  Load '53_LVBus493599_consumption' has phase imbalance of 141.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493121_consumption`  
  Load '53_LVBus493121_consumption' has phase imbalance of 232.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus981316_consumption`  
  Load '53_LVBus981316_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493354_consumption`  
  Load '53_LVBus493354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493658_consumption`  
  Load '53_LVBus493658_consumption' has phase imbalance of 259.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493323_consumption`  
  Load '53_LVBus493323_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493534_consumption`  
  Load '53_LVBus493534_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994211_consumption`  
  Load '53_LVBus994211_consumption' has phase imbalance of 186.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493197_consumption`  
  Load '53_LVBus493197_consumption' has phase imbalance of 139.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493620_consumption`  
  Load '53_LVBus493620_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493556_consumption`  
  Load '53_LVBus493556_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493583_consumption`  
  Load '53_LVBus493583_consumption' has phase imbalance of 63.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493341_consumption`  
  Load '53_LVBus493341_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493092_consumption`  
  Load '53_LVBus493092_consumption' has phase imbalance of 277.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus979736_consumption`  
  Load '53_LVBus979736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493164_consumption`  
  Load '53_LVBus493164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493375_consumption`  
  Load '53_LVBus493375_consumption' has phase imbalance of 175.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493433_consumption`  
  Load '53_LVBus493433_consumption' has phase imbalance of 274.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493048_consumption`  
  Load '53_LVBus493048_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493427_consumption`  
  Load '53_LVBus493427_consumption' has phase imbalance of 110.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493076_consumption`  
  Load '53_LVBus493076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493615_consumption`  
  Load '53_LVBus493615_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493650_consumption`  
  Load '53_LVBus493650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493636_consumption`  
  Load '53_LVBus493636_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493050_consumption`  
  Load '53_LVBus493050_consumption' has phase imbalance of 90.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493662_consumption`  
  Load '53_LVBus493662_consumption' has phase imbalance of 260.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493555_consumption`  
  Load '53_LVBus493555_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493200_consumption`  
  Load '53_LVBus493200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493049_consumption`  
  Load '53_LVBus493049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493091_consumption`  
  Load '53_LVBus493091_consumption' has phase imbalance of 290.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493260_consumption`  
  Load '53_LVBus493260_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493177_consumption`  
  Load '53_LVBus493177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493518_consumption`  
  Load '53_LVBus493518_consumption' has phase imbalance of 103.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493113_consumption`  
  Load '53_LVBus493113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493150_consumption`  
  Load '53_LVBus493150_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493471_consumption`  
  Load '53_LVBus493471_consumption' has phase imbalance of 227.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493647_consumption`  
  Load '53_LVBus493647_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493261_consumption`  
  Load '53_LVBus493261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493601_consumption`  
  Load '53_LVBus493601_consumption' has phase imbalance of 228.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493107_consumption`  
  Load '53_LVBus493107_consumption' has phase imbalance of 290.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493311_consumption`  
  Load '53_LVBus493311_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493439_consumption`  
  Load '53_LVBus493439_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493464_consumption`  
  Load '53_LVBus493464_consumption' has phase imbalance of 259.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493247_consumption`  
  Load '53_LVBus493247_consumption' has phase imbalance of 38.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493656_consumption`  
  Load '53_LVBus493656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus981313_consumption`  
  Load '53_LVBus981313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493387_consumption`  
  Load '53_LVBus493387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493363_consumption`  
  Load '53_LVBus493363_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493202_consumption`  
  Load '53_LVBus493202_consumption' has phase imbalance of 144.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493122_consumption`  
  Load '53_LVBus493122_consumption' has phase imbalance of 272.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus979735_consumption`  
  Load '53_LVBus979735_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493664_consumption`  
  Load '53_LVBus493664_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493564_consumption`  
  Load '53_LVBus493564_consumption' has phase imbalance of 262.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus981314_consumption`  
  Load '53_LVBus981314_consumption' has phase imbalance of 261.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493303_consumption`  
  Load '53_LVBus493303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493604_consumption`  
  Load '53_LVBus493604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493051_consumption`  
  Load '53_LVBus493051_consumption' has phase imbalance of 205.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus979737_consumption`  
  Load '53_LVBus979737_consumption' has phase imbalance of 91.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493224_consumption`  
  Load '53_LVBus493224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493174_consumption`  
  Load '53_LVBus493174_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493643_consumption`  
  Load '53_LVBus493643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493466_consumption`  
  Load '53_LVBus493466_consumption' has phase imbalance of 292.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493128_consumption`  
  Load '53_LVBus493128_consumption' has phase imbalance of 106.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1030243_consumption`  
  Load '53_LVBus1030243_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493565_consumption`  
  Load '53_LVBus493565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493444_consumption`  
  Load '53_LVBus493444_consumption' has phase imbalance of 208.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493146_consumption`  
  Load '53_LVBus493146_consumption' has phase imbalance of 98.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493639_consumption`  
  Load '53_LVBus493639_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493470_consumption`  
  Load '53_LVBus493470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493635_consumption`  
  Load '53_LVBus493635_consumption' has phase imbalance of 45.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493553_consumption`  
  Load '53_LVBus493553_consumption' has phase imbalance of 234.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493445_consumption`  
  Load '53_LVBus493445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493514_consumption`  
  Load '53_LVBus493514_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493195_consumption`  
  Load '53_LVBus493195_consumption' has phase imbalance of 122.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493395_consumption`  
  Load '53_LVBus493395_consumption' has phase imbalance of 243.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493172_consumption`  
  Load '53_LVBus493172_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493103_consumption`  
  Load '53_LVBus493103_consumption' has phase imbalance of 209.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493056_consumption`  
  Load '53_LVBus493056_consumption' has phase imbalance of 100.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493587_consumption`  
  Load '53_LVBus493587_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493149_consumption`  
  Load '53_LVBus493149_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493208_consumption`  
  Load '53_LVBus493208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493429_consumption`  
  Load '53_LVBus493429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493099_consumption`  
  Load '53_LVBus493099_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493388_consumption`  
  Load '53_LVBus493388_consumption' has phase imbalance of 289.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493256_consumption`  
  Load '53_LVBus493256_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493307_consumption`  
  Load '53_LVBus493307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493379_consumption`  
  Load '53_LVBus493379_consumption' has phase imbalance of 40.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493360_consumption`  
  Load '53_LVBus493360_consumption' has phase imbalance of 247.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493539_consumption`  
  Load '53_LVBus493539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493623_consumption`  
  Load '53_LVBus493623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493546_consumption`  
  Load '53_LVBus493546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493606_consumption`  
  Load '53_LVBus493606_consumption' has phase imbalance of 240.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493591_consumption`  
  Load '53_LVBus493591_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493450_consumption`  
  Load '53_LVBus493450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493551_consumption`  
  Load '53_LVBus493551_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493405_consumption`  
  Load '53_LVBus493405_consumption' has phase imbalance of 51.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493155_consumption`  
  Load '53_LVBus493155_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493250_consumption`  
  Load '53_LVBus493250_consumption' has phase imbalance of 197.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493456_consumption`  
  Load '53_LVBus493456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1035074_consumption`  
  Load '53_LVBus1035074_consumption' has phase imbalance of 250.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493148_consumption`  
  Load '53_LVBus493148_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493481_consumption`  
  Load '53_LVBus493481_consumption' has phase imbalance of 239.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493133_consumption`  
  Load '53_LVBus493133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493465_consumption`  
  Load '53_LVBus493465_consumption' has phase imbalance of 219.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493367_consumption`  
  Load '53_LVBus493367_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493043_consumption`  
  Load '53_LVBus493043_consumption' has phase imbalance of 271.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493390_consumption`  
  Load '53_LVBus493390_consumption' has phase imbalance of 270.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493227_consumption`  
  Load '53_LVBus493227_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493154_consumption`  
  Load '53_LVBus493154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493286_consumption`  
  Load '53_LVBus493286_consumption' has phase imbalance of 229.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493435_consumption`  
  Load '53_LVBus493435_consumption' has phase imbalance of 258.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493081_consumption`  
  Load '53_LVBus493081_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493337_consumption`  
  Load '53_LVBus493337_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493454_consumption`  
  Load '53_LVBus493454_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus981315_consumption`  
  Load '53_LVBus981315_consumption' has phase imbalance of 278.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493326_consumption`  
  Load '53_LVBus493326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493562_consumption`  
  Load '53_LVBus493562_consumption' has phase imbalance of 263.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493523_consumption`  
  Load '53_LVBus493523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493338_consumption`  
  Load '53_LVBus493338_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493457_consumption`  
  Load '53_LVBus493457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1035075_consumption`  
  Load '53_LVBus1035075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493638_consumption`  
  Load '53_LVBus493638_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493142_consumption`  
  Load '53_LVBus493142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493067_consumption`  
  Load '53_LVBus493067_consumption' has phase imbalance of 287.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493365_consumption`  
  Load '53_LVBus493365_consumption' has phase imbalance of 21.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493243_consumption`  
  Load '53_LVBus493243_consumption' has phase imbalance of 254.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1030245_consumption`  
  Load '53_LVBus1030245_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493370_consumption`  
  Load '53_LVBus493370_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493096_consumption`  
  Load '53_LVBus493096_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493180_consumption`  
  Load '53_LVBus493180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493500_consumption`  
  Load '53_LVBus493500_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493335_consumption`  
  Load '53_LVBus493335_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493561_consumption`  
  Load '53_LVBus493561_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493593_consumption`  
  Load '53_LVBus493593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493563_consumption`  
  Load '53_LVBus493563_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493325_consumption`  
  Load '53_LVBus493325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493163_consumption`  
  Load '53_LVBus493163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493305_consumption`  
  Load '53_LVBus493305_consumption' has phase imbalance of 229.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493378_consumption`  
  Load '53_LVBus493378_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493459_consumption`  
  Load '53_LVBus493459_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493351_consumption`  
  Load '53_LVBus493351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493597_consumption`  
  Load '53_LVBus493597_consumption' has phase imbalance of 282.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493059_consumption`  
  Load '53_LVBus493059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493598_consumption`  
  Load '53_LVBus493598_consumption' has phase imbalance of 183.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493160_consumption`  
  Load '53_LVBus493160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493291_consumption`  
  Load '53_LVBus493291_consumption' has phase imbalance of 137.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493042_consumption`  
  Load '53_LVBus493042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493531_consumption`  
  Load '53_LVBus493531_consumption' has phase imbalance of 29.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493038_consumption`  
  Load '53_LVBus493038_consumption' has phase imbalance of 238.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493046_consumption`  
  Load '53_LVBus493046_consumption' has phase imbalance of 273.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493334_consumption`  
  Load '53_LVBus493334_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493442_consumption`  
  Load '53_LVBus493442_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493299_consumption`  
  Load '53_LVBus493299_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493443_consumption`  
  Load '53_LVBus493443_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493132_consumption`  
  Load '53_LVBus493132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493486_consumption`  
  Load '53_LVBus493486_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493368_consumption`  
  Load '53_LVBus493368_consumption' has phase imbalance of 24.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493178_consumption`  
  Load '53_LVBus493178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493131_consumption`  
  Load '53_LVBus493131_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1025908_consumption`  
  Load '53_LVBus1025908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493627_consumption`  
  Load '53_LVBus493627_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1030239_consumption`  
  Load '53_LVBus1030239_consumption' has phase imbalance of 102.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493228_consumption`  
  Load '53_LVBus493228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493571_consumption`  
  Load '53_LVBus493571_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1026610_consumption`  
  Load '53_LVBus1026610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493304_consumption`  
  Load '53_LVBus493304_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493255_consumption`  
  Load '53_LVBus493255_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493313_consumption`  
  Load '53_LVBus493313_consumption' has phase imbalance of 244.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493663_consumption`  
  Load '53_LVBus493663_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493235_consumption`  
  Load '53_LVBus493235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493203_consumption`  
  Load '53_LVBus493203_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus981317_consumption`  
  Load '53_LVBus981317_consumption' has phase imbalance of 237.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493336_consumption`  
  Load '53_LVBus493336_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493047_consumption`  
  Load '53_LVBus493047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1031292_consumption`  
  Load '53_LVBus1031292_consumption' has phase imbalance of 164.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493449_consumption`  
  Load '53_LVBus493449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493293_consumption`  
  Load '53_LVBus493293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493425_consumption`  
  Load '53_LVBus493425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493153_consumption`  
  Load '53_LVBus493153_consumption' has phase imbalance of 242.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493361_consumption`  
  Load '53_LVBus493361_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493493_consumption`  
  Load '53_LVBus493493_consumption' has phase imbalance of 288.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493186_consumption`  
  Load '53_LVBus493186_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493460_consumption`  
  Load '53_LVBus493460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493321_consumption`  
  Load '53_LVBus493321_consumption' has phase imbalance of 285.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1030242_consumption`  
  Load '53_LVBus1030242_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493412_consumption`  
  Load '53_LVBus493412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493532_consumption`  
  Load '53_LVBus493532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493629_consumption`  
  Load '53_LVBus493629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493300_consumption`  
  Load '53_LVBus493300_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493590_consumption`  
  Load '53_LVBus493590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus1022436_consumption`  
  Load '53_LVBus1022436_consumption' has phase imbalance of 172.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493044_consumption`  
  Load '53_LVBus493044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493184_consumption`  
  Load '53_LVBus493184_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493411_consumption`  
  Load '53_LVBus493411_consumption' has phase imbalance of 254.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493080_consumption`  
  Load '53_LVBus493080_consumption' has phase imbalance of 99.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493403_consumption`  
  Load '53_LVBus493403_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493616_consumption`  
  Load '53_LVBus493616_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493503_consumption`  
  Load '53_LVBus493503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493614_consumption`  
  Load '53_LVBus493614_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493239_consumption`  
  Load '53_LVBus493239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493281_consumption`  
  Load '53_LVBus493281_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493448_consumption`  
  Load '53_LVBus493448_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493485_consumption`  
  Load '53_LVBus493485_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493251_consumption`  
  Load '53_LVBus493251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493438_consumption`  
  Load '53_LVBus493438_consumption' has phase imbalance of 165.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493249_consumption`  
  Load '53_LVBus493249_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493488_consumption`  
  Load '53_LVBus493488_consumption' has phase imbalance of 278.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493318_consumption`  
  Load '53_LVBus493318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493463_consumption`  
  Load '53_LVBus493463_consumption' has phase imbalance of 267.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493339_consumption`  
  Load '53_LVBus493339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493357_consumption`  
  Load '53_LVBus493357_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493410_consumption`  
  Load '53_LVBus493410_consumption' has phase imbalance of 242.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493144_consumption`  
  Load '53_LVBus493144_consumption' has phase imbalance of 130.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493254_consumption`  
  Load '53_LVBus493254_consumption' has phase imbalance of 139.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493666_consumption`  
  Load '53_LVBus493666_consumption' has phase imbalance of 286.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493317_consumption`  
  Load '53_LVBus493317_consumption' has phase imbalance of 154.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493230_consumption`  
  Load '53_LVBus493230_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493340_consumption`  
  Load '53_LVBus493340_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493665_consumption`  
  Load '53_LVBus493665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493179_consumption`  
  Load '53_LVBus493179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493349_consumption`  
  Load '53_LVBus493349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493358_consumption`  
  Load '53_LVBus493358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493434_consumption`  
  Load '53_LVBus493434_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493176_consumption`  
  Load '53_LVBus493176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus493238_consumption`  
  Load '53_LVBus493238_consumption' has phase imbalance of 129.5%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1150 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus493527' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus493072' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '53_LVBus493527' (LV, 0.24 kV) has an electrical reach of 8.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  702 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  318 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 53_LVBus1016204_consumption, 53_LVBus1022436_consumption, 53_LVBus1025907_consumption, 53_LVBus1025908_consumption, 53_LVBus1026609_consumption, 53_LVBus1026610_consumption, 53_LVBus1030243_consumption, 53_LVBus1030244_consumption, 53_LVBus1030245_consumption, 53_LVBus1035073_consumption, 53_LVBus1035075_consumption, 53_LVBus1035076_consumption, 53_LVBus1036727_consumption, 53_LVBus493038_consumption, 53_LVBus493040_consumption, 53_LVBus493041_consumption, 53_LVBus493042_consumption, 53_LVBus493043_consumption, 53_LVBus493044_consumption, 53_LVBus493045_consumption, 53_LVBus493047_consumption, 53_LVBus493048_consumption, 53_LVBus493049_consumption, 53_LVBus493058_consumption, 53_LVBus493059_consumption, 53_LVBus493060_consumption, 53_LVBus493066_consumption, 53_LVBus493069_consumption, 53_LVBus493075_consumption, 53_LVBus493076_consumption, 53_LVBus493078_consumption, 53_LVBus493079_consumption, 53_LVBus493081_consumption, 53_LVBus493082_consumption, 53_LVBus493083_consumption, 53_LVBus493086_consumption, 53_LVBus493090_consumption, 53_LVBus493091_consumption, 53_LVBus493092_consumption, 53_LVBus493094_consumption, 53_LVBus493096_consumption, 53_LVBus493097_consumption, 53_LVBus493098_consumption, 53_LVBus493099_consumption, 53_LVBus493100_consumption, 53_LVBus493101_consumption, 53_LVBus493102_consumption, 53_LVBus493103_consumption, 53_LVBus493104_consumption, 53_LVBus493107_consumption, 53_LVBus493112_consumption, 53_LVBus493113_consumption, 53_LVBus493114_consumption, 53_LVBus493118_consumption, 53_LVBus493121_consumption, 53_LVBus493123_consumption, 53_LVBus493129_consumption, 53_LVBus493130_consumption, 53_LVBus493132_consumption, 53_LVBus493133_consumption, 53_LVBus493135_consumption, 53_LVBus493140_consumption, 53_LVBus493141_consumption, 53_LVBus493142_consumption, 53_LVBus493149_consumption, 53_LVBus493150_consumption, 53_LVBus493153_consumption, 53_LVBus493154_consumption, 53_LVBus493158_consumption, 53_LVBus493160_consumption, 53_LVBus493161_consumption, 53_LVBus493162_consumption, 53_LVBus493163_consumption, 53_LVBus493164_consumption, 53_LVBus493167_consumption, 53_LVBus493170_consumption, 53_LVBus493172_consumption, 53_LVBus493174_consumption, 53_LVBus493176_consumption, 53_LVBus493177_consumption, 53_LVBus493178_consumption, 53_LVBus493179_consumption, 53_LVBus493180_consumption, 53_LVBus493182_consumption, 53_LVBus493184_consumption, 53_LVBus493186_consumption, 53_LVBus493187_consumption, 53_LVBus493189_consumption, 53_LVBus493198_consumption, 53_LVBus493199_consumption, 53_LVBus493200_consumption, 53_LVBus493208_consumption, 53_LVBus493210_consumption, 53_LVBus493211_consumption, 53_LVBus493212_consumption, 53_LVBus493216_consumption, 53_LVBus493217_consumption, 53_LVBus493218_consumption, 53_LVBus493224_consumption, 53_LVBus493227_consumption, 53_LVBus493228_consumption, 53_LVBus493229_consumption, 53_LVBus493230_consumption, 53_LVBus493231_consumption, 53_LVBus493232_consumption, 53_LVBus493233_consumption, 53_LVBus493234_consumption, 53_LVBus493235_consumption, 53_LVBus493237_consumption, 53_LVBus493239_consumption, 53_LVBus493242_consumption, 53_LVBus493243_consumption, 53_LVBus493244_consumption, 53_LVBus493245_consumption, 53_LVBus493248_consumption, 53_LVBus493249_consumption, 53_LVBus493250_consumption, 53_LVBus493251_consumption, 53_LVBus493252_consumption, 53_LVBus493253_consumption, 53_LVBus493258_consumption, 53_LVBus493260_consumption, 53_LVBus493261_consumption, 53_LVBus493266_consumption, 53_LVBus493270_consumption, 53_LVBus493272_consumption, 53_LVBus493275_consumption, 53_LVBus493276_consumption, 53_LVBus493279_consumption, 53_LVBus493281_consumption, 53_LVBus493282_consumption, 53_LVBus493288_consumption, 53_LVBus493293_consumption, 53_LVBus493294_consumption, 53_LVBus493295_consumption, 53_LVBus493300_consumption, 53_LVBus493303_consumption, 53_LVBus493307_consumption, 53_LVBus493311_consumption, 53_LVBus493317_consumption, 53_LVBus493318_consumption, 53_LVBus493319_consumption, 53_LVBus493320_consumption, 53_LVBus493321_consumption, 53_LVBus493323_consumption, 53_LVBus493325_consumption, 53_LVBus493326_consumption, 53_LVBus493327_consumption, 53_LVBus493330_consumption, 53_LVBus493332_consumption, 53_LVBus493333_consumption, 53_LVBus493334_consumption, 53_LVBus493335_consumption, 53_LVBus493336_consumption, 53_LVBus493337_consumption, 53_LVBus493338_consumption, 53_LVBus493339_consumption, 53_LVBus493343_consumption, 53_LVBus493345_consumption, 53_LVBus493348_consumption, 53_LVBus493349_consumption, 53_LVBus493350_consumption, 53_LVBus493351_consumption, 53_LVBus493354_consumption, 53_LVBus493356_consumption, 53_LVBus493357_consumption, 53_LVBus493358_consumption, 53_LVBus493359_consumption, 53_LVBus493360_consumption, 53_LVBus493363_consumption, 53_LVBus493364_consumption, 53_LVBus493371_consumption, 53_LVBus493374_consumption, 53_LVBus493376_consumption, 53_LVBus493377_consumption, 53_LVBus493378_consumption, 53_LVBus493386_consumption, 53_LVBus493387_consumption, 53_LVBus493388_consumption, 53_LVBus493389_consumption, 53_LVBus493390_consumption, 53_LVBus493395_consumption, 53_LVBus493403_consumption, 53_LVBus493408_consumption, 53_LVBus493409_consumption, 53_LVBus493410_consumption, 53_LVBus493411_consumption, 53_LVBus493412_consumption, 53_LVBus493413_consumption, 53_LVBus493414_consumption, 53_LVBus493415_consumption, 53_LVBus493423_consumption, 53_LVBus493425_consumption, 53_LVBus493429_consumption, 53_LVBus493430_consumption, 53_LVBus493433_consumption, 53_LVBus493434_consumption, 53_LVBus493435_consumption, 53_LVBus493436_consumption, 53_LVBus493437_consumption, 53_LVBus493438_consumption, 53_LVBus493439_consumption, 53_LVBus493442_consumption, 53_LVBus493443_consumption, 53_LVBus493444_consumption, 53_LVBus493445_consumption, 53_LVBus493446_consumption, 53_LVBus493447_consumption, 53_LVBus493448_consumption, 53_LVBus493449_consumption, 53_LVBus493450_consumption, 53_LVBus493451_consumption, 53_LVBus493452_consumption, 53_LVBus493453_consumption, 53_LVBus493454_consumption, 53_LVBus493456_consumption, 53_LVBus493457_consumption, 53_LVBus493459_consumption, 53_LVBus493460_consumption, 53_LVBus493461_consumption, 53_LVBus493462_consumption, 53_LVBus493463_consumption, 53_LVBus493464_consumption, 53_LVBus493466_consumption, 53_LVBus493470_consumption, 53_LVBus493471_consumption, 53_LVBus493473_consumption, 53_LVBus493482_consumption, 53_LVBus493483_consumption, 53_LVBus493485_consumption, 53_LVBus493486_consumption, 53_LVBus493487_consumption, 53_LVBus493488_consumption, 53_LVBus493490_consumption, 53_LVBus493494_consumption, 53_LVBus493499_consumption, 53_LVBus493500_consumption, 53_LVBus493501_consumption, 53_LVBus493503_consumption, 53_LVBus493521_consumption, 53_LVBus493523_consumption, 53_LVBus493530_consumption, 53_LVBus493532_consumption, 53_LVBus493533_consumption, 53_LVBus493534_consumption, 53_LVBus493538_consumption, 53_LVBus493539_consumption, 53_LVBus493541_consumption, 53_LVBus493542_consumption, 53_LVBus493545_consumption, 53_LVBus493546_consumption, 53_LVBus493547_consumption, 53_LVBus493548_consumption, 53_LVBus493551_consumption, 53_LVBus493552_consumption, 53_LVBus493553_consumption, 53_LVBus493555_consumption, 53_LVBus493557_consumption, 53_LVBus493562_consumption, 53_LVBus493563_consumption, 53_LVBus493564_consumption, 53_LVBus493565_consumption, 53_LVBus493566_consumption, 53_LVBus493567_consumption, 53_LVBus493568_consumption, 53_LVBus493571_consumption, 53_LVBus493574_consumption, 53_LVBus493575_consumption, 53_LVBus493581_consumption, 53_LVBus493582_consumption, 53_LVBus493587_consumption, 53_LVBus493590_consumption, 53_LVBus493591_consumption, 53_LVBus493593_consumption, 53_LVBus493597_consumption, 53_LVBus493601_consumption, 53_LVBus493602_consumption, 53_LVBus493604_consumption, 53_LVBus493606_consumption, 53_LVBus493609_consumption, 53_LVBus493614_consumption, 53_LVBus493615_consumption, 53_LVBus493618_consumption, 53_LVBus493619_consumption, 53_LVBus493620_consumption, 53_LVBus493622_consumption, 53_LVBus493623_consumption, 53_LVBus493626_consumption, 53_LVBus493629_consumption, 53_LVBus493631_consumption, 53_LVBus493636_consumption, 53_LVBus493638_consumption, 53_LVBus493639_consumption, 53_LVBus493642_consumption, 53_LVBus493643_consumption, 53_LVBus493646_consumption, 53_LVBus493647_consumption, 53_LVBus493649_consumption, 53_LVBus493650_consumption, 53_LVBus493653_consumption, 53_LVBus493656_consumption, 53_LVBus493658_consumption, 53_LVBus493660_consumption, 53_LVBus493661_consumption, 53_LVBus493663_consumption, 53_LVBus493664_consumption, 53_LVBus493665_consumption, 53_LVBus493666_consumption, 53_LVBus979736_consumption, 53_LVBus979745_consumption, 53_LVBus981313_consumption, 53_LVBus981314_consumption, 53_LVBus981315_consumption, 53_LVBus991173_consumption, 53_LVBus994208_consumption, 53_LVBus994211_consumption, 53_LVBus994212_consumption, 53_LVBus994213_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  575 group(s) of loads (1150 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  5 group(s) of series lines (10 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  686 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus1016204_production, 53_LVBus1022436_production, 53_LVBus1025907_production, 53_LVBus1025908_production, 53_LVBus1026609_production, 53_LVBus1026610_production, 53_LVBus1026611_consumption, 53_LVBus1026611_production, 53_LVBus1026612_consumption, 53_LVBus1026612_production, 53_LVBus1026613_consumption, 53_LVBus1026613_production, 53_LVBus1026614_consumption, 53_LVBus1026614_production, 53_LVBus1026615_production, 53_LVBus1026616_production, 53_LVBus1026617_consumption, 53_LVBus1026617_production, 53_LVBus1028404_consumption, 53_LVBus1028404_production, 53_LVBus1030239_production, 53_LVBus1030240_production, 53_LVBus1030241_production, 53_LVBus1030242_production, 53_LVBus1030243_production, 53_LVBus1030244_production, 53_LVBus1030245_production, 53_LVBus1031291_production, 53_LVBus1031292_production, 53_LVBus1035073_production, 53_LVBus1035074_production, 53_LVBus1035075_production, 53_LVBus1035076_production, 53_LVBus1035077_consumption, 53_LVBus1035077_production, 53_LVBus1035078_consumption, 53_LVBus1035078_production, 53_LVBus1035079_consumption, 53_LVBus1035079_production, 53_LVBus1036727_production, 53_LVBus493038_production, 53_LVBus493039_consumption, 53_LVBus493039_production, 53_LVBus493040_production, 53_LVBus493041_production, 53_LVBus493042_production, 53_LVBus493043_production, 53_LVBus493044_production, 53_LVBus493045_production, 53_LVBus493046_production, 53_LVBus493047_production, 53_LVBus493048_production, 53_LVBus493049_production, 53_LVBus493050_production, 53_LVBus493051_production, 53_LVBus493053_consumption, 53_LVBus493053_production, 53_LVBus493054_consumption, 53_LVBus493054_production, 53_LVBus493055_production, 53_LVBus493056_production, 53_LVBus493057_consumption, 53_LVBus493057_production, 53_LVBus493058_production, 53_LVBus493059_production, 53_LVBus493060_production, 53_LVBus493061_consumption, 53_LVBus493061_production, 53_LVBus493062_production, 53_LVBus493064_consumption, 53_LVBus493064_production, 53_LVBus493065_consumption, 53_LVBus493065_production, 53_LVBus493066_production, 53_LVBus493067_production, 53_LVBus493068_production, 53_LVBus493069_production, 53_LVBus493070_consumption, 53_LVBus493070_production, 53_LVBus493072_production, 53_LVBus493074_consumption, 53_LVBus493074_production, 53_LVBus493075_production, 53_LVBus493076_production, 53_LVBus493077_production, 53_LVBus493078_production, 53_LVBus493079_production, 53_LVBus493080_production, 53_LVBus493081_production, 53_LVBus493082_production, 53_LVBus493083_production, 53_LVBus493084_production, 53_LVBus493085_consumption, 53_LVBus493085_production, 53_LVBus493086_production, 53_LVBus493087_consumption, 53_LVBus493087_production, 53_LVBus493088_production, 53_LVBus493090_production, 53_LVBus493091_production, 53_LVBus493092_production, 53_LVBus493093_production, 53_LVBus493094_production, 53_LVBus493096_production, 53_LVBus493097_production, 53_LVBus493098_production, 53_LVBus493099_production, 53_LVBus493100_production, 53_LVBus493101_production, 53_LVBus493102_production, 53_LVBus493103_production, 53_LVBus493104_production, 53_LVBus493107_production, 53_LVBus493109_consumption, 53_LVBus493109_production, 53_LVBus493110_consumption, 53_LVBus493110_production, 53_LVBus493111_consumption, 53_LVBus493111_production, 53_LVBus493112_production, 53_LVBus493113_production, 53_LVBus493114_production, 53_LVBus493118_production, 53_LVBus493120_consumption, 53_LVBus493120_production, 53_LVBus493121_production, 53_LVBus493122_production, 53_LVBus493123_production, 53_LVBus493124_production, 53_LVBus493126_production, 53_LVBus493127_consumption, 53_LVBus493127_production, 53_LVBus493128_production, 53_LVBus493129_production, 53_LVBus493130_production, 53_LVBus493131_production, 53_LVBus493132_production, 53_LVBus493133_production, 53_LVBus493135_production, 53_LVBus493136_production, 53_LVBus493137_production, 53_LVBus493138_production, 53_LVBus493139_production, 53_LVBus493140_production, 53_LVBus493141_production, 53_LVBus493142_production, 53_LVBus493144_production, 53_LVBus493145_production, 53_LVBus493146_production, 53_LVBus493147_production, 53_LVBus493148_production, 53_LVBus493149_production, 53_LVBus493150_production, 53_LVBus493151_production, 53_LVBus493152_consumption, 53_LVBus493152_production, 53_LVBus493153_production, 53_LVBus493154_production, 53_LVBus493155_production, 53_LVBus493156_production, 53_LVBus493157_production, 53_LVBus493158_production, 53_LVBus493159_production, 53_LVBus493160_production, 53_LVBus493161_production, 53_LVBus493162_production, 53_LVBus493163_production, 53_LVBus493164_production, 53_LVBus493165_production, 53_LVBus493167_production, 53_LVBus493168_production, 53_LVBus493170_production, 53_LVBus493172_production, 53_LVBus493173_consumption, 53_LVBus493173_production, 53_LVBus493174_production, 53_LVBus493175_consumption, 53_LVBus493175_production, 53_LVBus493176_production, 53_LVBus493177_production, 53_LVBus493178_production, 53_LVBus493179_production, 53_LVBus493180_production, 53_LVBus493182_production, 53_LVBus493184_production, 53_LVBus493185_consumption, 53_LVBus493185_production, 53_LVBus493186_production, 53_LVBus493187_production, 53_LVBus493189_production, 53_LVBus493190_consumption, 53_LVBus493190_production, 53_LVBus493191_consumption, 53_LVBus493191_production, 53_LVBus493193_production, 53_LVBus493194_consumption, 53_LVBus493194_production, 53_LVBus493195_production, 53_LVBus493196_production, 53_LVBus493197_production, 53_LVBus493198_production, 53_LVBus493199_production, 53_LVBus493200_production, 53_LVBus493202_production, 53_LVBus493203_production, 53_LVBus493205_consumption, 53_LVBus493205_production, 53_LVBus493206_consumption, 53_LVBus493206_production, 53_LVBus493207_consumption, 53_LVBus493207_production, 53_LVBus493208_production, 53_LVBus493209_consumption, 53_LVBus493209_production, 53_LVBus493210_production, 53_LVBus493211_production, 53_LVBus493212_production, 53_LVBus493213_consumption, 53_LVBus493213_production, 53_LVBus493214_production, 53_LVBus493215_consumption, 53_LVBus493215_production, 53_LVBus493216_production, 53_LVBus493217_production, 53_LVBus493218_production, 53_LVBus493220_consumption, 53_LVBus493220_production, 53_LVBus493221_consumption, 53_LVBus493221_production, 53_LVBus493222_production, 53_LVBus493223_consumption, 53_LVBus493223_production, 53_LVBus493224_production, 53_LVBus493226_consumption, 53_LVBus493226_production, 53_LVBus493227_production, 53_LVBus493228_production, 53_LVBus493229_production, 53_LVBus493230_production, 53_LVBus493231_production, 53_LVBus493232_production, 53_LVBus493233_production, 53_LVBus493234_production, 53_LVBus493235_production, 53_LVBus493237_production, 53_LVBus493238_production, 53_LVBus493239_production, 53_LVBus493240_production, 53_LVBus493242_production, 53_LVBus493243_production, 53_LVBus493244_production, 53_LVBus493245_production, 53_LVBus493246_production, 53_LVBus493247_production, 53_LVBus493248_production, 53_LVBus493249_production, 53_LVBus493250_production, 53_LVBus493251_production, 53_LVBus493252_production, 53_LVBus493253_production, 53_LVBus493254_production, 53_LVBus493255_production, 53_LVBus493256_production, 53_LVBus493258_production, 53_LVBus493259_consumption, 53_LVBus493259_production, 53_LVBus493260_production, 53_LVBus493261_production, 53_LVBus493262_consumption, 53_LVBus493262_production, 53_LVBus493263_production, 53_LVBus493265_consumption, 53_LVBus493265_production, 53_LVBus493266_production, 53_LVBus493267_consumption, 53_LVBus493267_production, 53_LVBus493268_consumption, 53_LVBus493268_production, 53_LVBus493269_consumption, 53_LVBus493269_production, 53_LVBus493270_production, 53_LVBus493271_production, 53_LVBus493272_production, 53_LVBus493273_production, 53_LVBus493274_production, 53_LVBus493275_production, 53_LVBus493276_production, 53_LVBus493278_consumption, 53_LVBus493278_production, 53_LVBus493279_production, 53_LVBus493280_consumption, 53_LVBus493280_production, 53_LVBus493281_production, 53_LVBus493282_production, 53_LVBus493283_consumption, 53_LVBus493283_production, 53_LVBus493285_consumption, 53_LVBus493285_production, 53_LVBus493286_production, 53_LVBus493287_production, 53_LVBus493288_production, 53_LVBus493289_production, 53_LVBus493291_production, 53_LVBus493293_production, 53_LVBus493294_production, 53_LVBus493295_production, 53_LVBus493299_production, 53_LVBus493300_production, 53_LVBus493302_production, 53_LVBus493303_production, 53_LVBus493304_production, 53_LVBus493305_production, 53_LVBus493307_production, 53_LVBus493308_consumption, 53_LVBus493308_production, 53_LVBus493309_consumption, 53_LVBus493309_production, 53_LVBus493310_consumption, 53_LVBus493310_production, 53_LVBus493311_production, 53_LVBus493312_consumption, 53_LVBus493312_production, 53_LVBus493313_production, 53_LVBus493314_production, 53_LVBus493315_production, 53_LVBus493316_consumption, 53_LVBus493316_production, 53_LVBus493317_production, 53_LVBus493318_production, 53_LVBus493319_production, 53_LVBus493320_production, 53_LVBus493321_production, 53_LVBus493323_production, 53_LVBus493325_production, 53_LVBus493326_production, 53_LVBus493327_production, 53_LVBus493328_consumption, 53_LVBus493328_production, 53_LVBus493329_consumption, 53_LVBus493329_production, 53_LVBus493330_production, 53_LVBus493331_consumption, 53_LVBus493331_production, 53_LVBus493332_production, 53_LVBus493333_production, 53_LVBus493334_production, 53_LVBus493335_production, 53_LVBus493336_production, 53_LVBus493337_production, 53_LVBus493338_production, 53_LVBus493339_production, 53_LVBus493340_production, 53_LVBus493341_production, 53_LVBus493343_production, 53_LVBus493345_production, 53_LVBus493347_consumption, 53_LVBus493347_production, 53_LVBus493348_production, 53_LVBus493349_production, 53_LVBus493350_production, 53_LVBus493351_production, 53_LVBus493352_consumption, 53_LVBus493352_production, 53_LVBus493353_consumption, 53_LVBus493353_production, 53_LVBus493354_production, 53_LVBus493356_production, 53_LVBus493357_production, 53_LVBus493358_production, 53_LVBus493359_production, 53_LVBus493360_production, 53_LVBus493361_production, 53_LVBus493363_production, 53_LVBus493364_production, 53_LVBus493365_production, 53_LVBus493366_production, 53_LVBus493367_production, 53_LVBus493368_production, 53_LVBus493370_production, 53_LVBus493371_production, 53_LVBus493372_production, 53_LVBus493374_production, 53_LVBus493375_production, 53_LVBus493376_production, 53_LVBus493377_production, 53_LVBus493378_production, 53_LVBus493379_production, 53_LVBus493381_production, 53_LVBus493383_production, 53_LVBus493384_production, 53_LVBus493385_consumption, 53_LVBus493385_production, 53_LVBus493386_production, 53_LVBus493387_production, 53_LVBus493388_production, 53_LVBus493389_production, 53_LVBus493390_production, 53_LVBus493391_production, 53_LVBus493393_consumption, 53_LVBus493393_production, 53_LVBus493395_production, 53_LVBus493397_production, 53_LVBus493398_production, 53_LVBus493400_production, 53_LVBus493402_consumption, 53_LVBus493402_production, 53_LVBus493403_production, 53_LVBus493405_production, 53_LVBus493407_consumption, 53_LVBus493407_production, 53_LVBus493408_production, 53_LVBus493409_production, 53_LVBus493410_production, 53_LVBus493411_production, 53_LVBus493412_production, 53_LVBus493413_production, 53_LVBus493414_production, 53_LVBus493415_production, 53_LVBus493417_production, 53_LVBus493418_consumption, 53_LVBus493418_production, 53_LVBus493419_production, 53_LVBus493420_production, 53_LVBus493422_consumption, 53_LVBus493422_production, 53_LVBus493423_production, 53_LVBus493424_consumption, 53_LVBus493424_production, 53_LVBus493425_production, 53_LVBus493427_production, 53_LVBus493429_production, 53_LVBus493430_production, 53_LVBus493431_consumption, 53_LVBus493431_production, 53_LVBus493433_production, 53_LVBus493434_production, 53_LVBus493435_production, 53_LVBus493436_production, 53_LVBus493437_production, 53_LVBus493438_production, 53_LVBus493439_production, 53_LVBus493441_consumption, 53_LVBus493441_production, 53_LVBus493442_production, 53_LVBus493443_production, 53_LVBus493444_production, 53_LVBus493445_production, 53_LVBus493446_production, 53_LVBus493447_production, 53_LVBus493448_production, 53_LVBus493449_production, 53_LVBus493450_production, 53_LVBus493451_production, 53_LVBus493452_production, 53_LVBus493453_production, 53_LVBus493454_production, 53_LVBus493456_production, 53_LVBus493457_production, 53_LVBus493459_production, 53_LVBus493460_production, 53_LVBus493461_production, 53_LVBus493462_production, 53_LVBus493463_production, 53_LVBus493464_production, 53_LVBus493465_production, 53_LVBus493466_production, 53_LVBus493467_production, 53_LVBus493468_production, 53_LVBus493470_production, 53_LVBus493471_production, 53_LVBus493472_consumption, 53_LVBus493472_production, 53_LVBus493473_production, 53_LVBus493474_consumption, 53_LVBus493474_production, 53_LVBus493475_consumption, 53_LVBus493475_production, 53_LVBus493478_production, 53_LVBus493480_production, 53_LVBus493481_production, 53_LVBus493482_production, 53_LVBus493483_production, 53_LVBus493485_production, 53_LVBus493486_production, 53_LVBus493487_production, 53_LVBus493488_production, 53_LVBus493489_consumption, 53_LVBus493489_production, 53_LVBus493490_production, 53_LVBus493491_production, 53_LVBus493493_production, 53_LVBus493494_production, 53_LVBus493496_consumption, 53_LVBus493496_production, 53_LVBus493498_consumption, 53_LVBus493498_production, 53_LVBus493499_production, 53_LVBus493500_production, 53_LVBus493501_production, 53_LVBus493502_production, 53_LVBus493503_production, 53_LVBus493504_consumption, 53_LVBus493504_production, 53_LVBus493505_consumption, 53_LVBus493505_production, 53_LVBus493506_production, 53_LVBus493507_production, 53_LVBus493509_production, 53_LVBus493511_consumption, 53_LVBus493511_production, 53_LVBus493513_production, 53_LVBus493514_production, 53_LVBus493516_consumption, 53_LVBus493516_production, 53_LVBus493517_production, 53_LVBus493518_production, 53_LVBus493520_consumption, 53_LVBus493520_production, 53_LVBus493521_production, 53_LVBus493522_production, 53_LVBus493523_production, 53_LVBus493524_consumption, 53_LVBus493524_production, 53_LVBus493525_production, 53_LVBus493527_production, 53_LVBus493529_production, 53_LVBus493530_production, 53_LVBus493531_production, 53_LVBus493532_production, 53_LVBus493533_production, 53_LVBus493534_production, 53_LVBus493536_production, 53_LVBus493537_production, 53_LVBus493538_production, 53_LVBus493539_production, 53_LVBus493540_production, 53_LVBus493541_production, 53_LVBus493542_production, 53_LVBus493543_consumption, 53_LVBus493543_production, 53_LVBus493545_production, 53_LVBus493546_production, 53_LVBus493547_production, 53_LVBus493548_production, 53_LVBus493550_consumption, 53_LVBus493550_production, 53_LVBus493551_production, 53_LVBus493552_production, 53_LVBus493553_production, 53_LVBus493554_consumption, 53_LVBus493554_production, 53_LVBus493555_production, 53_LVBus493556_production, 53_LVBus493557_production, 53_LVBus493559_consumption, 53_LVBus493559_production, 53_LVBus493560_consumption, 53_LVBus493560_production, 53_LVBus493561_production, 53_LVBus493562_production, 53_LVBus493563_production, 53_LVBus493564_production, 53_LVBus493565_production, 53_LVBus493566_production, 53_LVBus493567_production, 53_LVBus493568_production, 53_LVBus493570_consumption, 53_LVBus493570_production, 53_LVBus493571_production, 53_LVBus493572_consumption, 53_LVBus493572_production, 53_LVBus493573_consumption, 53_LVBus493573_production, 53_LVBus493574_production, 53_LVBus493575_production, 53_LVBus493577_consumption, 53_LVBus493577_production, 53_LVBus493578_consumption, 53_LVBus493578_production, 53_LVBus493579_production, 53_LVBus493580_consumption, 53_LVBus493580_production, 53_LVBus493581_production, 53_LVBus493582_production, 53_LVBus493583_production, 53_LVBus493584_consumption, 53_LVBus493584_production, 53_LVBus493586_consumption, 53_LVBus493586_production, 53_LVBus493587_production, 53_LVBus493589_consumption, 53_LVBus493589_production, 53_LVBus493590_production, 53_LVBus493591_production, 53_LVBus493593_production, 53_LVBus493597_production, 53_LVBus493598_production, 53_LVBus493599_production, 53_LVBus493600_consumption, 53_LVBus493600_production, 53_LVBus493601_production, 53_LVBus493602_production, 53_LVBus493603_production, 53_LVBus493604_production, 53_LVBus493606_production, 53_LVBus493607_production, 53_LVBus493608_production, 53_LVBus493609_production, 53_LVBus493610_production, 53_LVBus493611_consumption, 53_LVBus493611_production, 53_LVBus493612_consumption, 53_LVBus493612_production, 53_LVBus493613_consumption, 53_LVBus493613_production, 53_LVBus493614_production, 53_LVBus493615_production, 53_LVBus493616_production, 53_LVBus493618_production, 53_LVBus493619_production, 53_LVBus493620_production, 53_LVBus493622_production, 53_LVBus493623_production, 53_LVBus493624_consumption, 53_LVBus493624_production, 53_LVBus493625_consumption, 53_LVBus493625_production, 53_LVBus493626_production, 53_LVBus493627_production, 53_LVBus493629_production, 53_LVBus493631_production, 53_LVBus493633_production, 53_LVBus493635_production, 53_LVBus493636_production, 53_LVBus493638_production, 53_LVBus493639_production, 53_LVBus493640_production, 53_LVBus493641_consumption, 53_LVBus493641_production, 53_LVBus493642_production, 53_LVBus493643_production, 53_LVBus493644_production, 53_LVBus493645_production, 53_LVBus493646_production, 53_LVBus493647_production, 53_LVBus493649_production, 53_LVBus493650_production, 53_LVBus493651_production, 53_LVBus493652_production, 53_LVBus493653_production, 53_LVBus493654_consumption, 53_LVBus493654_production, 53_LVBus493656_production, 53_LVBus493657_consumption, 53_LVBus493657_production, 53_LVBus493658_production, 53_LVBus493660_production, 53_LVBus493661_production, 53_LVBus493662_production, 53_LVBus493663_production, 53_LVBus493664_production, 53_LVBus493665_production, 53_LVBus493666_production, 53_LVBus979734_consumption, 53_LVBus979734_production, 53_LVBus979735_production, 53_LVBus979736_production, 53_LVBus979737_production, 53_LVBus979745_production, 53_LVBus981313_production, 53_LVBus981314_production, 53_LVBus981315_production, 53_LVBus981316_production, 53_LVBus981317_production, 53_LVBus981318_production, 53_LVBus991173_production, 53_LVBus994208_production, 53_LVBus994209_consumption, 53_LVBus994209_production, 53_LVBus994210_consumption, 53_LVBus994210_production, 53_LVBus994211_production, 53_LVBus994212_production, 53_LVBus994213_production, 53_MVLV06965_consumption, 53_MVLV06965_production.

