# BMOPF Network Summary: 52_MVFeeder1438

**Generated:** 2026-10-01 23:34:14  
**Findings:** 0 errors · 5 warnings · 327 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 49 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 557 |  |
| line | 507 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 804 | 2.855 MW, 856.4 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 49 |  |
| switch | 0 |  |
| transformer | 49 | Dyn11×49 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 106 | 105 | 0 | 0 |
| LV_236V | 236.0 V | 451 | 402 | 804 | 0 |

**Transformer transitions:**

- `52_MVLV004142_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009560_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV027631_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV026704_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV005197_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV097833_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV041260_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV018463_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV016624_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV068137_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV050673_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV090201_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV004194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV044619_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV041248_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV058681_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV050671_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV061955_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009561_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV035790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV053742_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV097726_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV081547_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV072250_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV077177_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV102569_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV076538_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV014487_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV097832_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV012804_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV027584_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV053292_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV064759_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV058690_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV081550_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV058691_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV097725_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104323_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV042745_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV080758_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV072514_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV035788_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV099222_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV027572_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV012428_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV027625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV065516_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV014563_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 8 |
| Degree-1 buses | 203 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 557 | 1 | 556 | 0 | 0 | 0 |
| Tier LV_236V | 451 | 49 | 402 | 0 | 0 | 0 |
| Tier MV_11.8kV | 106 | 1 | 105 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 49; skipped invalid branches: 0.

Galvanic zones: 50; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_MAZE | MV_11.8kV | 106 | 0 | 0 | 49 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2122 declared bus terminals; 1923 mapped line/closed-switch conductor edges; 199 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 35000.0 | 2.43 | 2412 |
| q_nom | 0.0 | 10500.0 | 2.43 | 2412 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.621 | 1130.0 | 1.166 | 507 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.641 | 49 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 466 of 804 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356625_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356472_consumption' has phase imbalance of 218.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356785_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356824_consumption' has phase imbalance of 264.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356846_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356827_consumption' has phase imbalance of 114.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356673_consumption' has phase imbalance of 127.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356893_consumption' has phase imbalance of 126.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356646_consumption' has phase imbalance of 127.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356918_consumption' has phase imbalance of 143.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356870_consumption' has phase imbalance of 43.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356732_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356736_consumption' has phase imbalance of 281.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356649_consumption' has phase imbalance of 289.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356582_consumption' has phase imbalance of 71.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356638_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356434_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356862_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356751_consumption' has phase imbalance of 263.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356909_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356466_consumption' has phase imbalance of 116.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356729_consumption' has phase imbalance of 139.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356933_consumption' has phase imbalance of 65.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356790_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356733_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356832_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356757_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356764_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356895_consumption' has phase imbalance of 264.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356577_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356661_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356657_consumption' has phase imbalance of 156.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356801_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356710_consumption' has phase imbalance of 38.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356665_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356708_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356910_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356907_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356882_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356473_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356847_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356871_consumption' has phase imbalance of 82.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356767_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356660_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356463_consumption' has phase imbalance of 216.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356479_consumption' has phase imbalance of 96.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356908_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356802_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356934_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356669_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356516_consumption' has phase imbalance of 128.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356770_consumption' has phase imbalance of 269.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356711_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356548_consumption' has phase imbalance of 252.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356905_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356885_consumption' has phase imbalance of 131.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356601_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356816_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1179484_consumption' has phase imbalance of 274.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1181180_consumption' has phase imbalance of 151.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356859_consumption' has phase imbalance of 166.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356578_consumption' has phase imbalance of 174.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356667_consumption' has phase imbalance of 241.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356436_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356593_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356836_consumption' has phase imbalance of 275.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356658_consumption' has phase imbalance of 280.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356595_consumption' has phase imbalance of 42.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356468_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356743_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356766_consumption' has phase imbalance of 256.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356614_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356796_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356618_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356540_consumption' has phase imbalance of 234.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356452_consumption' has phase imbalance of 104.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356627_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356723_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356852_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356844_consumption' has phase imbalance of 254.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356591_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356529_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356483_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356898_consumption' has phase imbalance of 111.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356807_consumption' has phase imbalance of 21.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356936_consumption' has phase imbalance of 140.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356460_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356834_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356728_consumption' has phase imbalance of 30.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356818_consumption' has phase imbalance of 263.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356794_consumption' has phase imbalance of 214.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356921_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356536_consumption' has phase imbalance of 160.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356881_consumption' has phase imbalance of 264.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356470_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356731_consumption' has phase imbalance of 91.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356447_consumption' has phase imbalance of 155.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356621_consumption' has phase imbalance of 248.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356542_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356707_consumption' has phase imbalance of 78.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356868_consumption' has phase imbalance of 149.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356488_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356789_consumption' has phase imbalance of 245.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356648_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356926_consumption' has phase imbalance of 26.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356876_consumption' has phase imbalance of 102.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356467_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356454_consumption' has phase imbalance of 250.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356680_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356806_consumption' has phase imbalance of 170.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356823_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356546_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356793_consumption' has phase imbalance of 267.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356630_consumption' has phase imbalance of 30.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356756_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356702_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356857_consumption' has phase imbalance of 298.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356504_consumption' has phase imbalance of 185.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356700_consumption' has phase imbalance of 31.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356634_consumption' has phase imbalance of 101.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356484_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356679_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356825_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356869_consumption' has phase imbalance of 106.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356650_consumption' has phase imbalance of 150.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356494_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356503_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356788_consumption' has phase imbalance of 195.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356643_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356883_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356919_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356706_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356897_consumption' has phase imbalance of 183.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356571_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356810_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356928_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356486_consumption' has phase imbalance of 100.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356495_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356522_consumption' has phase imbalance of 133.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356462_consumption' has phase imbalance of 279.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356879_consumption' has phase imbalance of 144.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356487_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356581_consumption' has phase imbalance of 248.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356705_consumption' has phase imbalance of 124.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356718_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356656_consumption' has phase imbalance of 275.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356499_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356583_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356855_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356902_consumption' has phase imbalance of 33.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356771_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356513_consumption' has phase imbalance of 148.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356442_consumption' has phase imbalance of 126.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356861_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356508_consumption' has phase imbalance of 133.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356476_consumption' has phase imbalance of 96.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356911_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356759_consumption' has phase imbalance of 200.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356584_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356597_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356668_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356474_consumption' has phase imbalance of 62.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356455_consumption' has phase imbalance of 242.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356635_consumption' has phase imbalance of 24.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356853_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356677_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356579_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356453_consumption' has phase imbalance of 105.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356626_consumption' has phase imbalance of 87.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356819_consumption' has phase imbalance of 269.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356781_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356891_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356760_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356615_consumption' has phase imbalance of 84.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356527_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356430_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356931_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356704_consumption' has phase imbalance of 22.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356787_consumption' has phase imbalance of 167.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356892_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356610_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356935_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356674_consumption' has phase imbalance of 221.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356506_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356851_consumption' has phase imbalance of 104.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356685_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356937_consumption' has phase imbalance of 97.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356568_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356672_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356784_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356833_consumption' has phase imbalance of 94.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356518_consumption' has phase imbalance of 212.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356500_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356437_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356554_consumption' has phase imbalance of 222.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356560_consumption' has phase imbalance of 47.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356598_consumption' has phase imbalance of 133.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356475_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356576_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356724_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356471_consumption' has phase imbalance of 37.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356864_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356716_consumption' has phase imbalance of 101.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356841_consumption' has phase imbalance of 241.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356632_consumption' has phase imbalance of 163.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356765_consumption' has phase imbalance of 193.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356890_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356459_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356482_consumption' has phase imbalance of 52.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356538_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus356550_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 804 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_UNIFORM_CONFIG]** All 804 loads share the 'WYE' configuration — no connection diversity.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.855 MW |
| Total load Q | 856.4 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV004142_Transformer | 275.0 kVA | 17.4% |
| 52_MVLV009560_Transformer | 275.0 kVA | 23.5% |
| 52_MVLV027631_Transformer | 176.0 kVA | 8.9% |
| 52_MVLV026704_Transformer | 176.0 kVA | 12.8% |
| 52_MVLV005197_Transformer | 275.0 kVA | 15.5% |
| 52_MVLV097833_Transformer | 110.0 kVA | 2.3% |
| 52_MVLV041260_Transformer | 176.0 kVA | 32.7% |
| 52_MVLV018463_Transformer | 275.0 kVA | 18.9% |
| 52_MVLV016624_Transformer | 275.0 kVA | 27.9% |
| 52_MVLV068137_Transformer | 275.0 kVA | 18.6% |
| 52_MVLV050673_Transformer | 110.0 kVA | 18.1% |
| 52_MVLV090201_Transformer | 440.0 kVA | 27.1% |
| 52_MVLV004194_Transformer | 693.0 kVA | 21.6% |
| 52_MVLV044619_Transformer | 440.0 kVA | 21.6% |
| 52_MVLV041248_Transformer | 440.0 kVA | 5.0% |
| 52_MVLV058681_Transformer | 440.0 kVA | 25.1% |
| 52_MVLV050671_Transformer | 110.0 kVA | 2.9% |
| 52_MVLV061955_Transformer | 110.0 kVA | 2.3% |
| 52_MVLV009561_Transformer | 275.0 kVA | 6.6% |
| 52_MVLV035790_Transformer | 275.0 kVA | 10.9% |
| 52_MVLV053742_Transformer | 110.0 kVA | 9.6% |
| 52_MVLV097726_Transformer | 110.0 kVA | 13.7% |
| 52_MVLV081547_Transformer | 275.0 kVA | 11.0% |
| 52_MVLV072250_Transformer | 275.0 kVA | 15.5% |
| 52_MVLV077177_Transformer | 176.0 kVA | 20.5% |
| 52_MVLV102569_Transformer | 275.0 kVA | 12.0% |
| 52_MVLV076538_Transformer | 110.0 kVA | 15.8% |
| 52_MVLV014487_Transformer | 1.1 MVA | 17.0% |
| 52_MVLV097832_Transformer | 275.0 kVA | 12.7% |
| 52_MVLV012804_Transformer | 693.0 kVA | 40.5% |
| 52_MVLV027584_Transformer | 440.0 kVA | 51.5% |
| 52_MVLV053292_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV064759_Transformer | 275.0 kVA | 18.3% |
| 52_MVLV058690_Transformer | 110.0 kVA | 11.4% |
| 52_MVLV081550_Transformer | 440.0 kVA | 27.6% |
| 52_MVLV058691_Transformer | 110.0 kVA | 1.1% |
| 52_MVLV097725_Transformer | 110.0 kVA | 1.2% |
| 52_MVLV104323_Transformer | 110.0 kVA | 29.0% |
| 52_MVLV042745_Transformer | 275.0 kVA | 22.8% |
| 52_MVLV080758_Transformer | 275.0 kVA | 14.9% |
| 52_MVLV104625_Transformer | 275.0 kVA | 24.1% |
| 52_MVLV072514_Transformer | 440.0 kVA | 12.9% |
| 52_MVLV035788_Transformer | 275.0 kVA | 19.3% |
| 52_MVLV099222_Transformer | 440.0 kVA | 50.2% |
| 52_MVLV027572_Transformer | 440.0 kVA | 18.7% |
| 52_MVLV012428_Transformer | 275.0 kVA | 28.0% |
| 52_MVLV027625_Transformer | 176.0 kVA | 49.5% |
| 52_MVLV065516_Transformer | 275.0 kVA | 24.2% |
| 52_MVLV014563_Transformer | 176.0 kVA | 17.1% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.85 MW).
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '52_MAZE' has no load connected to phase terminal '1'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '52_MAZE' has no load connected to phase terminal '2'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '52_MAZE' has no load connected to phase terminal '3'.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 557 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 557 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 49 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 106 |
| LV_236V | 4-wire | 451 / 451 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 451 |
| Neutral branches | 402 |
| Grounding points | 49 |
| Neutral sections | 49 |
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
| 11.78 kV | 106 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 50 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 50 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2240.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 451 / 106 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 467 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 467 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1179484_production, 52_LVBus1181180_production, 52_LVBus356430_production, 52_LVBus356431_consumption, 52_LVBus356431_production, 52_LVBus356432_production, 52_LVBus356433_consumption, 52_LVBus356433_production, 52_LVBus356434_production, 52_LVBus356436_production, 52_LVBus356437_production, 52_LVBus356438_consumption, 52_LVBus356438_production, 52_LVBus356439_consumption, 52_LVBus356439_production, 52_LVBus356441_consumption, 52_LVBus356441_production, 52_LVBus356442_production, 52_LVBus356443_production, 52_LVBus356444_production, 52_LVBus356446_production, 52_LVBus356447_production, 52_LVBus356448_consumption, 52_LVBus356448_production, 52_LVBus356450_production, 52_LVBus356452_production, 52_LVBus356453_production, 52_LVBus356454_production, 52_LVBus356455_production, 52_LVBus356457_production, 52_LVBus356458_production, 52_LVBus356459_production, 52_LVBus356460_production, 52_LVBus356462_production, 52_LVBus356463_production, 52_LVBus356464_consumption, 52_LVBus356464_production, 52_LVBus356466_production, 52_LVBus356467_production, 52_LVBus356468_production, 52_LVBus356470_production, 52_LVBus356471_production, 52_LVBus356472_production, 52_LVBus356473_production, 52_LVBus356474_production, 52_LVBus356475_production, 52_LVBus356476_production, 52_LVBus356478_consumption, 52_LVBus356478_production, 52_LVBus356479_production, 52_LVBus356480_production, 52_LVBus356482_production, 52_LVBus356483_production, 52_LVBus356484_production, 52_LVBus356485_consumption, 52_LVBus356485_production, 52_LVBus356486_production, 52_LVBus356487_production, 52_LVBus356488_production, 52_LVBus356490_production, 52_LVBus356492_consumption, 52_LVBus356492_production, 52_LVBus356493_consumption, 52_LVBus356493_production, 52_LVBus356494_production, 52_LVBus356495_production, 52_LVBus356496_consumption, 52_LVBus356496_production, 52_LVBus356497_consumption, 52_LVBus356497_production, 52_LVBus356498_production, 52_LVBus356499_production, 52_LVBus356500_production, 52_LVBus356501_production, 52_LVBus356502_production, 52_LVBus356503_production, 52_LVBus356504_production, 52_LVBus356505_production, 52_LVBus356506_production, 52_LVBus356507_production, 52_LVBus356508_production, 52_LVBus356509_production, 52_LVBus356510_consumption, 52_LVBus356510_production, 52_LVBus356511_production, 52_LVBus356512_consumption, 52_LVBus356512_production, 52_LVBus356513_production, 52_LVBus356514_consumption, 52_LVBus356514_production, 52_LVBus356515_production, 52_LVBus356516_production, 52_LVBus356517_consumption, 52_LVBus356517_production, 52_LVBus356518_production, 52_LVBus356519_production, 52_LVBus356520_production, 52_LVBus356521_production, 52_LVBus356522_production, 52_LVBus356524_production, 52_LVBus356525_production, 52_LVBus356526_production, 52_LVBus356527_production, 52_LVBus356529_production, 52_LVBus356531_production, 52_LVBus356532_production, 52_LVBus356533_consumption, 52_LVBus356533_production, 52_LVBus356534_consumption, 52_LVBus356534_production, 52_LVBus356535_consumption, 52_LVBus356535_production, 52_LVBus356536_production, 52_LVBus356537_production, 52_LVBus356538_production, 52_LVBus356539_production, 52_LVBus356540_production, 52_LVBus356541_consumption, 52_LVBus356541_production, 52_LVBus356542_production, 52_LVBus356543_consumption, 52_LVBus356543_production, 52_LVBus356545_production, 52_LVBus356546_production, 52_LVBus356547_production, 52_LVBus356548_production, 52_LVBus356549_production, 52_LVBus356550_production, 52_LVBus356551_consumption, 52_LVBus356551_production, 52_LVBus356553_consumption, 52_LVBus356553_production, 52_LVBus356554_production, 52_LVBus356555_consumption, 52_LVBus356555_production, 52_LVBus356556_consumption, 52_LVBus356556_production, 52_LVBus356557_production, 52_LVBus356558_production, 52_LVBus356559_production, 52_LVBus356560_production, 52_LVBus356561_production, 52_LVBus356563_production, 52_LVBus356565_production, 52_LVBus356567_consumption, 52_LVBus356567_production, 52_LVBus356568_production, 52_LVBus356569_production, 52_LVBus356570_production, 52_LVBus356571_production, 52_LVBus356572_production, 52_LVBus356574_consumption, 52_LVBus356574_production, 52_LVBus356576_production, 52_LVBus356577_production, 52_LVBus356578_production, 52_LVBus356579_production, 52_LVBus356581_production, 52_LVBus356582_production, 52_LVBus356583_production, 52_LVBus356584_production, 52_LVBus356585_consumption, 52_LVBus356585_production, 52_LVBus356586_consumption, 52_LVBus356586_production, 52_LVBus356588_consumption, 52_LVBus356588_production, 52_LVBus356589_production, 52_LVBus356590_production, 52_LVBus356591_production, 52_LVBus356592_production, 52_LVBus356593_production, 52_LVBus356594_consumption, 52_LVBus356594_production, 52_LVBus356595_production, 52_LVBus356596_production, 52_LVBus356597_production, 52_LVBus356598_production, 52_LVBus356600_production, 52_LVBus356601_production, 52_LVBus356602_production, 52_LVBus356604_consumption, 52_LVBus356604_production, 52_LVBus356605_production, 52_LVBus356606_production, 52_LVBus356607_consumption, 52_LVBus356607_production, 52_LVBus356608_production, 52_LVBus356609_production, 52_LVBus356610_production, 52_LVBus356611_production, 52_LVBus356612_production, 52_LVBus356614_production, 52_LVBus356615_production, 52_LVBus356616_consumption, 52_LVBus356616_production, 52_LVBus356618_production, 52_LVBus356619_production, 52_LVBus356621_production, 52_LVBus356622_production, 52_LVBus356623_production, 52_LVBus356625_production, 52_LVBus356626_production, 52_LVBus356627_production, 52_LVBus356628_production, 52_LVBus356630_production, 52_LVBus356632_production, 52_LVBus356634_production, 52_LVBus356635_production, 52_LVBus356637_consumption, 52_LVBus356637_production, 52_LVBus356638_production, 52_LVBus356640_production, 52_LVBus356642_consumption, 52_LVBus356642_production, 52_LVBus356643_production, 52_LVBus356644_production, 52_LVBus356645_production, 52_LVBus356646_production, 52_LVBus356648_production, 52_LVBus356649_production, 52_LVBus356650_production, 52_LVBus356652_production, 52_LVBus356654_consumption, 52_LVBus356654_production, 52_LVBus356655_production, 52_LVBus356656_production, 52_LVBus356657_production, 52_LVBus356658_production, 52_LVBus356660_production, 52_LVBus356661_production, 52_LVBus356662_production, 52_LVBus356663_production, 52_LVBus356665_production, 52_LVBus356666_production, 52_LVBus356667_production, 52_LVBus356668_production, 52_LVBus356669_production, 52_LVBus356670_consumption, 52_LVBus356670_production, 52_LVBus356672_production, 52_LVBus356673_production, 52_LVBus356674_production, 52_LVBus356675_consumption, 52_LVBus356675_production, 52_LVBus356676_consumption, 52_LVBus356676_production, 52_LVBus356677_production, 52_LVBus356678_production, 52_LVBus356679_production, 52_LVBus356680_production, 52_LVBus356682_production, 52_LVBus356683_production, 52_LVBus356684_consumption, 52_LVBus356684_production, 52_LVBus356685_production, 52_LVBus356686_production, 52_LVBus356690_production, 52_LVBus356691_production, 52_LVBus356692_production, 52_LVBus356694_production, 52_LVBus356696_production, 52_LVBus356697_consumption, 52_LVBus356697_production, 52_LVBus356698_production, 52_LVBus356699_production, 52_LVBus356700_production, 52_LVBus356701_production, 52_LVBus356702_production, 52_LVBus356704_production, 52_LVBus356705_production, 52_LVBus356706_production, 52_LVBus356707_production, 52_LVBus356708_production, 52_LVBus356710_production, 52_LVBus356711_production, 52_LVBus356713_consumption, 52_LVBus356713_production, 52_LVBus356714_production, 52_LVBus356716_production, 52_LVBus356717_consumption, 52_LVBus356717_production, 52_LVBus356718_production, 52_LVBus356720_consumption, 52_LVBus356720_production, 52_LVBus356721_consumption, 52_LVBus356721_production, 52_LVBus356723_production, 52_LVBus356724_production, 52_LVBus356725_production, 52_LVBus356727_production, 52_LVBus356728_production, 52_LVBus356729_production, 52_LVBus356730_production, 52_LVBus356731_production, 52_LVBus356732_production, 52_LVBus356733_production, 52_LVBus356734_production, 52_LVBus356735_production, 52_LVBus356736_production, 52_LVBus356741_production, 52_LVBus356742_consumption, 52_LVBus356742_production, 52_LVBus356743_production, 52_LVBus356744_production, 52_LVBus356748_production, 52_LVBus356750_consumption, 52_LVBus356750_production, 52_LVBus356751_production, 52_LVBus356752_production, 52_LVBus356754_production, 52_LVBus356755_production, 52_LVBus356756_production, 52_LVBus356757_production, 52_LVBus356759_production, 52_LVBus356760_production, 52_LVBus356761_production, 52_LVBus356763_production, 52_LVBus356764_production, 52_LVBus356765_production, 52_LVBus356766_production, 52_LVBus356767_production, 52_LVBus356768_production, 52_LVBus356769_production, 52_LVBus356770_production, 52_LVBus356771_production, 52_LVBus356772_production, 52_LVBus356774_production, 52_LVBus356775_consumption, 52_LVBus356775_production, 52_LVBus356776_consumption, 52_LVBus356776_production, 52_LVBus356777_production, 52_LVBus356778_production, 52_LVBus356781_production, 52_LVBus356782_consumption, 52_LVBus356782_production, 52_LVBus356783_production, 52_LVBus356784_production, 52_LVBus356785_production, 52_LVBus356787_production, 52_LVBus356788_production, 52_LVBus356789_production, 52_LVBus356790_production, 52_LVBus356791_production, 52_LVBus356793_production, 52_LVBus356794_production, 52_LVBus356796_production, 52_LVBus356797_production, 52_LVBus356799_production, 52_LVBus356800_production, 52_LVBus356801_production, 52_LVBus356802_production, 52_LVBus356804_production, 52_LVBus356805_production, 52_LVBus356806_production, 52_LVBus356807_production, 52_LVBus356809_production, 52_LVBus356810_production, 52_LVBus356815_consumption, 52_LVBus356815_production, 52_LVBus356816_production, 52_LVBus356817_consumption, 52_LVBus356817_production, 52_LVBus356818_production, 52_LVBus356819_production, 52_LVBus356821_consumption, 52_LVBus356821_production, 52_LVBus356822_production, 52_LVBus356823_production, 52_LVBus356824_production, 52_LVBus356825_production, 52_LVBus356826_production, 52_LVBus356827_production, 52_LVBus356832_production, 52_LVBus356833_production, 52_LVBus356834_production, 52_LVBus356836_production, 52_LVBus356837_production, 52_LVBus356838_consumption, 52_LVBus356838_production, 52_LVBus356839_consumption, 52_LVBus356839_production, 52_LVBus356840_consumption, 52_LVBus356840_production, 52_LVBus356841_production, 52_LVBus356842_production, 52_LVBus356843_production, 52_LVBus356844_production, 52_LVBus356846_production, 52_LVBus356847_production, 52_LVBus356848_production, 52_LVBus356850_consumption, 52_LVBus356850_production, 52_LVBus356851_production, 52_LVBus356852_production, 52_LVBus356853_production, 52_LVBus356855_production, 52_LVBus356856_production, 52_LVBus356857_production, 52_LVBus356858_consumption, 52_LVBus356858_production, 52_LVBus356859_production, 52_LVBus356861_production, 52_LVBus356862_production, 52_LVBus356864_production, 52_LVBus356865_production, 52_LVBus356867_production, 52_LVBus356868_production, 52_LVBus356869_production, 52_LVBus356870_production, 52_LVBus356871_production, 52_LVBus356873_production, 52_LVBus356875_production, 52_LVBus356876_production, 52_LVBus356877_production, 52_LVBus356879_production, 52_LVBus356880_production, 52_LVBus356881_production, 52_LVBus356882_production, 52_LVBus356883_production, 52_LVBus356885_production, 52_LVBus356887_consumption, 52_LVBus356887_production, 52_LVBus356888_production, 52_LVBus356890_production, 52_LVBus356891_production, 52_LVBus356892_production, 52_LVBus356893_production, 52_LVBus356895_production, 52_LVBus356896_production, 52_LVBus356897_production, 52_LVBus356898_production, 52_LVBus356900_production, 52_LVBus356901_production, 52_LVBus356902_production, 52_LVBus356903_consumption, 52_LVBus356903_production, 52_LVBus356904_consumption, 52_LVBus356904_production, 52_LVBus356905_production, 52_LVBus356907_production, 52_LVBus356908_production, 52_LVBus356909_production, 52_LVBus356910_production, 52_LVBus356911_production, 52_LVBus356913_production, 52_LVBus356914_production, 52_LVBus356918_production, 52_LVBus356919_production, 52_LVBus356920_consumption, 52_LVBus356920_production, 52_LVBus356921_production, 52_LVBus356922_production, 52_LVBus356923_production, 52_LVBus356924_production, 52_LVBus356926_production, 52_LVBus356928_production, 52_LVBus356929_consumption, 52_LVBus356929_production, 52_LVBus356930_production, 52_LVBus356931_production, 52_LVBus356933_production, 52_LVBus356934_production, 52_LVBus356935_production, 52_LVBus356936_production, 52_LVBus356937_production.

## 9. Data Quality Summary

**Total findings:** 332 (0 errors, 5 warnings, 327 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  466 of 804 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.85 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  467 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356625_consumption`  
  Load '52_LVBus356625_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356698_consumption`  
  Load '52_LVBus356698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356748_consumption`  
  Load '52_LVBus356748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356472_consumption`  
  Load '52_LVBus356472_consumption' has phase imbalance of 218.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356785_consumption`  
  Load '52_LVBus356785_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356824_consumption`  
  Load '52_LVBus356824_consumption' has phase imbalance of 264.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356842_consumption`  
  Load '52_LVBus356842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356846_consumption`  
  Load '52_LVBus356846_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356682_consumption`  
  Load '52_LVBus356682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356827_consumption`  
  Load '52_LVBus356827_consumption' has phase imbalance of 114.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356507_consumption`  
  Load '52_LVBus356507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356673_consumption`  
  Load '52_LVBus356673_consumption' has phase imbalance of 127.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356804_consumption`  
  Load '52_LVBus356804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356893_consumption`  
  Load '52_LVBus356893_consumption' has phase imbalance of 126.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356524_consumption`  
  Load '52_LVBus356524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356646_consumption`  
  Load '52_LVBus356646_consumption' has phase imbalance of 127.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356918_consumption`  
  Load '52_LVBus356918_consumption' has phase imbalance of 143.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356605_consumption`  
  Load '52_LVBus356605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356870_consumption`  
  Load '52_LVBus356870_consumption' has phase imbalance of 43.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356777_consumption`  
  Load '52_LVBus356777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356732_consumption`  
  Load '52_LVBus356732_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356458_consumption`  
  Load '52_LVBus356458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356736_consumption`  
  Load '52_LVBus356736_consumption' has phase imbalance of 281.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356649_consumption`  
  Load '52_LVBus356649_consumption' has phase imbalance of 289.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356582_consumption`  
  Load '52_LVBus356582_consumption' has phase imbalance of 71.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356638_consumption`  
  Load '52_LVBus356638_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356434_consumption`  
  Load '52_LVBus356434_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356862_consumption`  
  Load '52_LVBus356862_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356509_consumption`  
  Load '52_LVBus356509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356751_consumption`  
  Load '52_LVBus356751_consumption' has phase imbalance of 263.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356909_consumption`  
  Load '52_LVBus356909_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356880_consumption`  
  Load '52_LVBus356880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356466_consumption`  
  Load '52_LVBus356466_consumption' has phase imbalance of 116.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356729_consumption`  
  Load '52_LVBus356729_consumption' has phase imbalance of 139.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356662_consumption`  
  Load '52_LVBus356662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356933_consumption`  
  Load '52_LVBus356933_consumption' has phase imbalance of 65.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356856_consumption`  
  Load '52_LVBus356856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356790_consumption`  
  Load '52_LVBus356790_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356733_consumption`  
  Load '52_LVBus356733_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356797_consumption`  
  Load '52_LVBus356797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356490_consumption`  
  Load '52_LVBus356490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356848_consumption`  
  Load '52_LVBus356848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356769_consumption`  
  Load '52_LVBus356769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356608_consumption`  
  Load '52_LVBus356608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356832_consumption`  
  Load '52_LVBus356832_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356757_consumption`  
  Load '52_LVBus356757_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356764_consumption`  
  Load '52_LVBus356764_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356895_consumption`  
  Load '52_LVBus356895_consumption' has phase imbalance of 264.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356577_consumption`  
  Load '52_LVBus356577_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356661_consumption`  
  Load '52_LVBus356661_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356657_consumption`  
  Load '52_LVBus356657_consumption' has phase imbalance of 156.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356801_consumption`  
  Load '52_LVBus356801_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356744_consumption`  
  Load '52_LVBus356744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356501_consumption`  
  Load '52_LVBus356501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356710_consumption`  
  Load '52_LVBus356710_consumption' has phase imbalance of 38.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356665_consumption`  
  Load '52_LVBus356665_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356708_consumption`  
  Load '52_LVBus356708_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356910_consumption`  
  Load '52_LVBus356910_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356907_consumption`  
  Load '52_LVBus356907_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356882_consumption`  
  Load '52_LVBus356882_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356900_consumption`  
  Load '52_LVBus356900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356473_consumption`  
  Load '52_LVBus356473_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356847_consumption`  
  Load '52_LVBus356847_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356734_consumption`  
  Load '52_LVBus356734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356871_consumption`  
  Load '52_LVBus356871_consumption' has phase imbalance of 82.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356767_consumption`  
  Load '52_LVBus356767_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356660_consumption`  
  Load '52_LVBus356660_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356778_consumption`  
  Load '52_LVBus356778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356463_consumption`  
  Load '52_LVBus356463_consumption' has phase imbalance of 216.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356896_consumption`  
  Load '52_LVBus356896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356875_consumption`  
  Load '52_LVBus356875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356479_consumption`  
  Load '52_LVBus356479_consumption' has phase imbalance of 96.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356908_consumption`  
  Load '52_LVBus356908_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356802_consumption`  
  Load '52_LVBus356802_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356934_consumption`  
  Load '52_LVBus356934_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356669_consumption`  
  Load '52_LVBus356669_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356516_consumption`  
  Load '52_LVBus356516_consumption' has phase imbalance of 128.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356600_consumption`  
  Load '52_LVBus356600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356930_consumption`  
  Load '52_LVBus356930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356770_consumption`  
  Load '52_LVBus356770_consumption' has phase imbalance of 269.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356711_consumption`  
  Load '52_LVBus356711_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356548_consumption`  
  Load '52_LVBus356548_consumption' has phase imbalance of 252.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356905_consumption`  
  Load '52_LVBus356905_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356913_consumption`  
  Load '52_LVBus356913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356843_consumption`  
  Load '52_LVBus356843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356525_consumption`  
  Load '52_LVBus356525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356885_consumption`  
  Load '52_LVBus356885_consumption' has phase imbalance of 131.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356601_consumption`  
  Load '52_LVBus356601_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356569_consumption`  
  Load '52_LVBus356569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356816_consumption`  
  Load '52_LVBus356816_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1179484_consumption`  
  Load '52_LVBus1179484_consumption' has phase imbalance of 274.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356727_consumption`  
  Load '52_LVBus356727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356809_consumption`  
  Load '52_LVBus356809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1181180_consumption`  
  Load '52_LVBus1181180_consumption' has phase imbalance of 151.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356701_consumption`  
  Load '52_LVBus356701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356859_consumption`  
  Load '52_LVBus356859_consumption' has phase imbalance of 166.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356805_consumption`  
  Load '52_LVBus356805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356578_consumption`  
  Load '52_LVBus356578_consumption' has phase imbalance of 174.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356768_consumption`  
  Load '52_LVBus356768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356761_consumption`  
  Load '52_LVBus356761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356667_consumption`  
  Load '52_LVBus356667_consumption' has phase imbalance of 241.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356612_consumption`  
  Load '52_LVBus356612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356867_consumption`  
  Load '52_LVBus356867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356755_consumption`  
  Load '52_LVBus356755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356436_consumption`  
  Load '52_LVBus356436_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356593_consumption`  
  Load '52_LVBus356593_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356836_consumption`  
  Load '52_LVBus356836_consumption' has phase imbalance of 275.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356655_consumption`  
  Load '52_LVBus356655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356658_consumption`  
  Load '52_LVBus356658_consumption' has phase imbalance of 280.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356595_consumption`  
  Load '52_LVBus356595_consumption' has phase imbalance of 42.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356922_consumption`  
  Load '52_LVBus356922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356468_consumption`  
  Load '52_LVBus356468_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356743_consumption`  
  Load '52_LVBus356743_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356799_consumption`  
  Load '52_LVBus356799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356766_consumption`  
  Load '52_LVBus356766_consumption' has phase imbalance of 256.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356614_consumption`  
  Load '52_LVBus356614_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356796_consumption`  
  Load '52_LVBus356796_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356618_consumption`  
  Load '52_LVBus356618_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356540_consumption`  
  Load '52_LVBus356540_consumption' has phase imbalance of 234.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356452_consumption`  
  Load '52_LVBus356452_consumption' has phase imbalance of 104.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356627_consumption`  
  Load '52_LVBus356627_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356723_consumption`  
  Load '52_LVBus356723_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356852_consumption`  
  Load '52_LVBus356852_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356844_consumption`  
  Load '52_LVBus356844_consumption' has phase imbalance of 254.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356591_consumption`  
  Load '52_LVBus356591_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356529_consumption`  
  Load '52_LVBus356529_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356526_consumption`  
  Load '52_LVBus356526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356483_consumption`  
  Load '52_LVBus356483_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356714_consumption`  
  Load '52_LVBus356714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356898_consumption`  
  Load '52_LVBus356898_consumption' has phase imbalance of 111.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356807_consumption`  
  Load '52_LVBus356807_consumption' has phase imbalance of 21.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356936_consumption`  
  Load '52_LVBus356936_consumption' has phase imbalance of 140.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356460_consumption`  
  Load '52_LVBus356460_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356834_consumption`  
  Load '52_LVBus356834_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356728_consumption`  
  Load '52_LVBus356728_consumption' has phase imbalance of 30.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356772_consumption`  
  Load '52_LVBus356772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356818_consumption`  
  Load '52_LVBus356818_consumption' has phase imbalance of 263.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356794_consumption`  
  Load '52_LVBus356794_consumption' has phase imbalance of 214.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356921_consumption`  
  Load '52_LVBus356921_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356822_consumption`  
  Load '52_LVBus356822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356536_consumption`  
  Load '52_LVBus356536_consumption' has phase imbalance of 160.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356606_consumption`  
  Load '52_LVBus356606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356881_consumption`  
  Load '52_LVBus356881_consumption' has phase imbalance of 264.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356774_consumption`  
  Load '52_LVBus356774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356470_consumption`  
  Load '52_LVBus356470_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356731_consumption`  
  Load '52_LVBus356731_consumption' has phase imbalance of 91.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356447_consumption`  
  Load '52_LVBus356447_consumption' has phase imbalance of 155.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356621_consumption`  
  Load '52_LVBus356621_consumption' has phase imbalance of 248.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356572_consumption`  
  Load '52_LVBus356572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356542_consumption`  
  Load '52_LVBus356542_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356545_consumption`  
  Load '52_LVBus356545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356531_consumption`  
  Load '52_LVBus356531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356707_consumption`  
  Load '52_LVBus356707_consumption' has phase imbalance of 78.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356868_consumption`  
  Load '52_LVBus356868_consumption' has phase imbalance of 149.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356837_consumption`  
  Load '52_LVBus356837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356488_consumption`  
  Load '52_LVBus356488_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356789_consumption`  
  Load '52_LVBus356789_consumption' has phase imbalance of 245.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356648_consumption`  
  Load '52_LVBus356648_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356741_consumption`  
  Load '52_LVBus356741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356926_consumption`  
  Load '52_LVBus356926_consumption' has phase imbalance of 26.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356888_consumption`  
  Load '52_LVBus356888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356923_consumption`  
  Load '52_LVBus356923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356876_consumption`  
  Load '52_LVBus356876_consumption' has phase imbalance of 102.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356467_consumption`  
  Load '52_LVBus356467_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356454_consumption`  
  Load '52_LVBus356454_consumption' has phase imbalance of 250.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356735_consumption`  
  Load '52_LVBus356735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356680_consumption`  
  Load '52_LVBus356680_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356806_consumption`  
  Load '52_LVBus356806_consumption' has phase imbalance of 170.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356823_consumption`  
  Load '52_LVBus356823_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356546_consumption`  
  Load '52_LVBus356546_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356754_consumption`  
  Load '52_LVBus356754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356725_consumption`  
  Load '52_LVBus356725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356793_consumption`  
  Load '52_LVBus356793_consumption' has phase imbalance of 267.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356630_consumption`  
  Load '52_LVBus356630_consumption' has phase imbalance of 30.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356547_consumption`  
  Load '52_LVBus356547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356756_consumption`  
  Load '52_LVBus356756_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356702_consumption`  
  Load '52_LVBus356702_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356857_consumption`  
  Load '52_LVBus356857_consumption' has phase imbalance of 298.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356504_consumption`  
  Load '52_LVBus356504_consumption' has phase imbalance of 185.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356763_consumption`  
  Load '52_LVBus356763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356791_consumption`  
  Load '52_LVBus356791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356700_consumption`  
  Load '52_LVBus356700_consumption' has phase imbalance of 31.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356634_consumption`  
  Load '52_LVBus356634_consumption' has phase imbalance of 101.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356484_consumption`  
  Load '52_LVBus356484_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356679_consumption`  
  Load '52_LVBus356679_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356825_consumption`  
  Load '52_LVBus356825_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356869_consumption`  
  Load '52_LVBus356869_consumption' has phase imbalance of 106.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356873_consumption`  
  Load '52_LVBus356873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356650_consumption`  
  Load '52_LVBus356650_consumption' has phase imbalance of 150.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356494_consumption`  
  Load '52_LVBus356494_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356503_consumption`  
  Load '52_LVBus356503_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356788_consumption`  
  Load '52_LVBus356788_consumption' has phase imbalance of 195.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356643_consumption`  
  Load '52_LVBus356643_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356883_consumption`  
  Load '52_LVBus356883_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356919_consumption`  
  Load '52_LVBus356919_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356706_consumption`  
  Load '52_LVBus356706_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356897_consumption`  
  Load '52_LVBus356897_consumption' has phase imbalance of 183.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356571_consumption`  
  Load '52_LVBus356571_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356810_consumption`  
  Load '52_LVBus356810_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356928_consumption`  
  Load '52_LVBus356928_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356502_consumption`  
  Load '52_LVBus356502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356486_consumption`  
  Load '52_LVBus356486_consumption' has phase imbalance of 100.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356495_consumption`  
  Load '52_LVBus356495_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356522_consumption`  
  Load '52_LVBus356522_consumption' has phase imbalance of 133.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356462_consumption`  
  Load '52_LVBus356462_consumption' has phase imbalance of 279.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356879_consumption`  
  Load '52_LVBus356879_consumption' has phase imbalance of 144.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356487_consumption`  
  Load '52_LVBus356487_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356581_consumption`  
  Load '52_LVBus356581_consumption' has phase imbalance of 248.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356705_consumption`  
  Load '52_LVBus356705_consumption' has phase imbalance of 124.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356718_consumption`  
  Load '52_LVBus356718_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356656_consumption`  
  Load '52_LVBus356656_consumption' has phase imbalance of 275.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356499_consumption`  
  Load '52_LVBus356499_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356583_consumption`  
  Load '52_LVBus356583_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356644_consumption`  
  Load '52_LVBus356644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356752_consumption`  
  Load '52_LVBus356752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356877_consumption`  
  Load '52_LVBus356877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356590_consumption`  
  Load '52_LVBus356590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356609_consumption`  
  Load '52_LVBus356609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356855_consumption`  
  Load '52_LVBus356855_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356902_consumption`  
  Load '52_LVBus356902_consumption' has phase imbalance of 33.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356771_consumption`  
  Load '52_LVBus356771_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356513_consumption`  
  Load '52_LVBus356513_consumption' has phase imbalance of 148.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356442_consumption`  
  Load '52_LVBus356442_consumption' has phase imbalance of 126.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356861_consumption`  
  Load '52_LVBus356861_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356508_consumption`  
  Load '52_LVBus356508_consumption' has phase imbalance of 133.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356432_consumption`  
  Load '52_LVBus356432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356826_consumption`  
  Load '52_LVBus356826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356480_consumption`  
  Load '52_LVBus356480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356476_consumption`  
  Load '52_LVBus356476_consumption' has phase imbalance of 96.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356911_consumption`  
  Load '52_LVBus356911_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356759_consumption`  
  Load '52_LVBus356759_consumption' has phase imbalance of 200.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356584_consumption`  
  Load '52_LVBus356584_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356678_consumption`  
  Load '52_LVBus356678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356924_consumption`  
  Load '52_LVBus356924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356597_consumption`  
  Load '52_LVBus356597_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356668_consumption`  
  Load '52_LVBus356668_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356570_consumption`  
  Load '52_LVBus356570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356474_consumption`  
  Load '52_LVBus356474_consumption' has phase imbalance of 62.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356455_consumption`  
  Load '52_LVBus356455_consumption' has phase imbalance of 242.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356635_consumption`  
  Load '52_LVBus356635_consumption' has phase imbalance of 24.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356640_consumption`  
  Load '52_LVBus356640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356853_consumption`  
  Load '52_LVBus356853_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356677_consumption`  
  Load '52_LVBus356677_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356699_consumption`  
  Load '52_LVBus356699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356579_consumption`  
  Load '52_LVBus356579_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356453_consumption`  
  Load '52_LVBus356453_consumption' has phase imbalance of 105.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356626_consumption`  
  Load '52_LVBus356626_consumption' has phase imbalance of 87.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356666_consumption`  
  Load '52_LVBus356666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356819_consumption`  
  Load '52_LVBus356819_consumption' has phase imbalance of 269.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356781_consumption`  
  Load '52_LVBus356781_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356891_consumption`  
  Load '52_LVBus356891_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356760_consumption`  
  Load '52_LVBus356760_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356615_consumption`  
  Load '52_LVBus356615_consumption' has phase imbalance of 84.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356527_consumption`  
  Load '52_LVBus356527_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356430_consumption`  
  Load '52_LVBus356430_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356686_consumption`  
  Load '52_LVBus356686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356592_consumption`  
  Load '52_LVBus356592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356623_consumption`  
  Load '52_LVBus356623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356931_consumption`  
  Load '52_LVBus356931_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356645_consumption`  
  Load '52_LVBus356645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356704_consumption`  
  Load '52_LVBus356704_consumption' has phase imbalance of 22.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356787_consumption`  
  Load '52_LVBus356787_consumption' has phase imbalance of 167.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356692_consumption`  
  Load '52_LVBus356692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356914_consumption`  
  Load '52_LVBus356914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356800_consumption`  
  Load '52_LVBus356800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356892_consumption`  
  Load '52_LVBus356892_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356610_consumption`  
  Load '52_LVBus356610_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356690_consumption`  
  Load '52_LVBus356690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356935_consumption`  
  Load '52_LVBus356935_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356596_consumption`  
  Load '52_LVBus356596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356674_consumption`  
  Load '52_LVBus356674_consumption' has phase imbalance of 221.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356506_consumption`  
  Load '52_LVBus356506_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356851_consumption`  
  Load '52_LVBus356851_consumption' has phase imbalance of 104.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356685_consumption`  
  Load '52_LVBus356685_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356937_consumption`  
  Load '52_LVBus356937_consumption' has phase imbalance of 97.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356568_consumption`  
  Load '52_LVBus356568_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356672_consumption`  
  Load '52_LVBus356672_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356784_consumption`  
  Load '52_LVBus356784_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356833_consumption`  
  Load '52_LVBus356833_consumption' has phase imbalance of 94.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356518_consumption`  
  Load '52_LVBus356518_consumption' has phase imbalance of 212.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356500_consumption`  
  Load '52_LVBus356500_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356437_consumption`  
  Load '52_LVBus356437_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356554_consumption`  
  Load '52_LVBus356554_consumption' has phase imbalance of 222.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356560_consumption`  
  Load '52_LVBus356560_consumption' has phase imbalance of 47.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356598_consumption`  
  Load '52_LVBus356598_consumption' has phase imbalance of 133.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356475_consumption`  
  Load '52_LVBus356475_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356628_consumption`  
  Load '52_LVBus356628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356519_consumption`  
  Load '52_LVBus356519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356532_consumption`  
  Load '52_LVBus356532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356576_consumption`  
  Load '52_LVBus356576_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356521_consumption`  
  Load '52_LVBus356521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356611_consumption`  
  Load '52_LVBus356611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356602_consumption`  
  Load '52_LVBus356602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356724_consumption`  
  Load '52_LVBus356724_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356471_consumption`  
  Load '52_LVBus356471_consumption' has phase imbalance of 37.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356864_consumption`  
  Load '52_LVBus356864_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356716_consumption`  
  Load '52_LVBus356716_consumption' has phase imbalance of 101.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356841_consumption`  
  Load '52_LVBus356841_consumption' has phase imbalance of 241.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356632_consumption`  
  Load '52_LVBus356632_consumption' has phase imbalance of 163.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356549_consumption`  
  Load '52_LVBus356549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356765_consumption`  
  Load '52_LVBus356765_consumption' has phase imbalance of 193.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356890_consumption`  
  Load '52_LVBus356890_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356459_consumption`  
  Load '52_LVBus356459_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356589_consumption`  
  Load '52_LVBus356589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356482_consumption`  
  Load '52_LVBus356482_consumption' has phase imbalance of 52.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356538_consumption`  
  Load '52_LVBus356538_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356783_consumption`  
  Load '52_LVBus356783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus356550_consumption`  
  Load '52_LVBus356550_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 804 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_UNIFORM_CONFIG]** `load`  
  All 804 loads share the 'WYE' configuration — no connection diversity.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '52_MAZE' has no load connected to phase terminal '1'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '52_MAZE' has no load connected to phase terminal '2'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '52_MAZE' has no load connected to phase terminal '3'.
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
  557 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  205 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 52_LVBus1179484_consumption, 52_LVBus1181180_consumption, 52_LVBus356432_consumption, 52_LVBus356434_consumption, 52_LVBus356436_consumption, 52_LVBus356437_consumption, 52_LVBus356447_consumption, 52_LVBus356454_consumption, 52_LVBus356455_consumption, 52_LVBus356458_consumption, 52_LVBus356462_consumption, 52_LVBus356467_consumption, 52_LVBus356468_consumption, 52_LVBus356472_consumption, 52_LVBus356475_consumption, 52_LVBus356480_consumption, 52_LVBus356483_consumption, 52_LVBus356487_consumption, 52_LVBus356488_consumption, 52_LVBus356490_consumption, 52_LVBus356494_consumption, 52_LVBus356495_consumption, 52_LVBus356499_consumption, 52_LVBus356501_consumption, 52_LVBus356502_consumption, 52_LVBus356507_consumption, 52_LVBus356509_consumption, 52_LVBus356519_consumption, 52_LVBus356521_consumption, 52_LVBus356524_consumption, 52_LVBus356525_consumption, 52_LVBus356526_consumption, 52_LVBus356531_consumption, 52_LVBus356532_consumption, 52_LVBus356540_consumption, 52_LVBus356545_consumption, 52_LVBus356547_consumption, 52_LVBus356548_consumption, 52_LVBus356549_consumption, 52_LVBus356554_consumption, 52_LVBus356568_consumption, 52_LVBus356569_consumption, 52_LVBus356570_consumption, 52_LVBus356571_consumption, 52_LVBus356572_consumption, 52_LVBus356577_consumption, 52_LVBus356578_consumption, 52_LVBus356579_consumption, 52_LVBus356589_consumption, 52_LVBus356590_consumption, 52_LVBus356591_consumption, 52_LVBus356592_consumption, 52_LVBus356596_consumption, 52_LVBus356597_consumption, 52_LVBus356600_consumption, 52_LVBus356601_consumption, 52_LVBus356602_consumption, 52_LVBus356605_consumption, 52_LVBus356606_consumption, 52_LVBus356608_consumption, 52_LVBus356609_consumption, 52_LVBus356610_consumption, 52_LVBus356611_consumption, 52_LVBus356612_consumption, 52_LVBus356621_consumption, 52_LVBus356623_consumption, 52_LVBus356628_consumption, 52_LVBus356638_consumption, 52_LVBus356640_consumption, 52_LVBus356643_consumption, 52_LVBus356644_consumption, 52_LVBus356645_consumption, 52_LVBus356649_consumption, 52_LVBus356655_consumption, 52_LVBus356656_consumption, 52_LVBus356657_consumption, 52_LVBus356658_consumption, 52_LVBus356661_consumption, 52_LVBus356662_consumption, 52_LVBus356665_consumption, 52_LVBus356666_consumption, 52_LVBus356667_consumption, 52_LVBus356668_consumption, 52_LVBus356669_consumption, 52_LVBus356672_consumption, 52_LVBus356674_consumption, 52_LVBus356677_consumption, 52_LVBus356678_consumption, 52_LVBus356680_consumption, 52_LVBus356682_consumption, 52_LVBus356685_consumption, 52_LVBus356686_consumption, 52_LVBus356690_consumption, 52_LVBus356692_consumption, 52_LVBus356698_consumption, 52_LVBus356699_consumption, 52_LVBus356701_consumption, 52_LVBus356706_consumption, 52_LVBus356711_consumption, 52_LVBus356714_consumption, 52_LVBus356718_consumption, 52_LVBus356723_consumption, 52_LVBus356724_consumption, 52_LVBus356725_consumption, 52_LVBus356727_consumption, 52_LVBus356732_consumption, 52_LVBus356733_consumption, 52_LVBus356734_consumption, 52_LVBus356735_consumption, 52_LVBus356736_consumption, 52_LVBus356741_consumption, 52_LVBus356743_consumption, 52_LVBus356744_consumption, 52_LVBus356748_consumption, 52_LVBus356751_consumption, 52_LVBus356752_consumption, 52_LVBus356754_consumption, 52_LVBus356755_consumption, 52_LVBus356759_consumption, 52_LVBus356760_consumption, 52_LVBus356761_consumption, 52_LVBus356763_consumption, 52_LVBus356764_consumption, 52_LVBus356766_consumption, 52_LVBus356767_consumption, 52_LVBus356768_consumption, 52_LVBus356769_consumption, 52_LVBus356770_consumption, 52_LVBus356772_consumption, 52_LVBus356774_consumption, 52_LVBus356777_consumption, 52_LVBus356778_consumption, 52_LVBus356781_consumption, 52_LVBus356783_consumption, 52_LVBus356784_consumption, 52_LVBus356785_consumption, 52_LVBus356787_consumption, 52_LVBus356788_consumption, 52_LVBus356789_consumption, 52_LVBus356790_consumption, 52_LVBus356791_consumption, 52_LVBus356793_consumption, 52_LVBus356794_consumption, 52_LVBus356796_consumption, 52_LVBus356797_consumption, 52_LVBus356799_consumption, 52_LVBus356800_consumption, 52_LVBus356801_consumption, 52_LVBus356802_consumption, 52_LVBus356804_consumption, 52_LVBus356805_consumption, 52_LVBus356806_consumption, 52_LVBus356809_consumption, 52_LVBus356816_consumption, 52_LVBus356818_consumption, 52_LVBus356819_consumption, 52_LVBus356822_consumption, 52_LVBus356823_consumption, 52_LVBus356824_consumption, 52_LVBus356825_consumption, 52_LVBus356826_consumption, 52_LVBus356832_consumption, 52_LVBus356836_consumption, 52_LVBus356837_consumption, 52_LVBus356841_consumption, 52_LVBus356842_consumption, 52_LVBus356843_consumption, 52_LVBus356846_consumption, 52_LVBus356848_consumption, 52_LVBus356852_consumption, 52_LVBus356853_consumption, 52_LVBus356856_consumption, 52_LVBus356857_consumption, 52_LVBus356859_consumption, 52_LVBus356864_consumption, 52_LVBus356867_consumption, 52_LVBus356873_consumption, 52_LVBus356875_consumption, 52_LVBus356877_consumption, 52_LVBus356880_consumption, 52_LVBus356881_consumption, 52_LVBus356882_consumption, 52_LVBus356883_consumption, 52_LVBus356888_consumption, 52_LVBus356890_consumption, 52_LVBus356891_consumption, 52_LVBus356892_consumption, 52_LVBus356895_consumption, 52_LVBus356896_consumption, 52_LVBus356897_consumption, 52_LVBus356900_consumption, 52_LVBus356907_consumption, 52_LVBus356909_consumption, 52_LVBus356910_consumption, 52_LVBus356911_consumption, 52_LVBus356913_consumption, 52_LVBus356914_consumption, 52_LVBus356919_consumption, 52_LVBus356922_consumption, 52_LVBus356923_consumption, 52_LVBus356924_consumption, 52_LVBus356928_consumption, 52_LVBus356930_consumption, 52_LVBus356931_consumption, 52_LVBus356935_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  402 group(s) of loads (804 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  12 group(s) of series lines (25 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  467 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1179484_production, 52_LVBus1181180_production, 52_LVBus356430_production, 52_LVBus356431_consumption, 52_LVBus356431_production, 52_LVBus356432_production, 52_LVBus356433_consumption, 52_LVBus356433_production, 52_LVBus356434_production, 52_LVBus356436_production, 52_LVBus356437_production, 52_LVBus356438_consumption, 52_LVBus356438_production, 52_LVBus356439_consumption, 52_LVBus356439_production, 52_LVBus356441_consumption, 52_LVBus356441_production, 52_LVBus356442_production, 52_LVBus356443_production, 52_LVBus356444_production, 52_LVBus356446_production, 52_LVBus356447_production, 52_LVBus356448_consumption, 52_LVBus356448_production, 52_LVBus356450_production, 52_LVBus356452_production, 52_LVBus356453_production, 52_LVBus356454_production, 52_LVBus356455_production, 52_LVBus356457_production, 52_LVBus356458_production, 52_LVBus356459_production, 52_LVBus356460_production, 52_LVBus356462_production, 52_LVBus356463_production, 52_LVBus356464_consumption, 52_LVBus356464_production, 52_LVBus356466_production, 52_LVBus356467_production, 52_LVBus356468_production, 52_LVBus356470_production, 52_LVBus356471_production, 52_LVBus356472_production, 52_LVBus356473_production, 52_LVBus356474_production, 52_LVBus356475_production, 52_LVBus356476_production, 52_LVBus356478_consumption, 52_LVBus356478_production, 52_LVBus356479_production, 52_LVBus356480_production, 52_LVBus356482_production, 52_LVBus356483_production, 52_LVBus356484_production, 52_LVBus356485_consumption, 52_LVBus356485_production, 52_LVBus356486_production, 52_LVBus356487_production, 52_LVBus356488_production, 52_LVBus356490_production, 52_LVBus356492_consumption, 52_LVBus356492_production, 52_LVBus356493_consumption, 52_LVBus356493_production, 52_LVBus356494_production, 52_LVBus356495_production, 52_LVBus356496_consumption, 52_LVBus356496_production, 52_LVBus356497_consumption, 52_LVBus356497_production, 52_LVBus356498_production, 52_LVBus356499_production, 52_LVBus356500_production, 52_LVBus356501_production, 52_LVBus356502_production, 52_LVBus356503_production, 52_LVBus356504_production, 52_LVBus356505_production, 52_LVBus356506_production, 52_LVBus356507_production, 52_LVBus356508_production, 52_LVBus356509_production, 52_LVBus356510_consumption, 52_LVBus356510_production, 52_LVBus356511_production, 52_LVBus356512_consumption, 52_LVBus356512_production, 52_LVBus356513_production, 52_LVBus356514_consumption, 52_LVBus356514_production, 52_LVBus356515_production, 52_LVBus356516_production, 52_LVBus356517_consumption, 52_LVBus356517_production, 52_LVBus356518_production, 52_LVBus356519_production, 52_LVBus356520_production, 52_LVBus356521_production, 52_LVBus356522_production, 52_LVBus356524_production, 52_LVBus356525_production, 52_LVBus356526_production, 52_LVBus356527_production, 52_LVBus356529_production, 52_LVBus356531_production, 52_LVBus356532_production, 52_LVBus356533_consumption, 52_LVBus356533_production, 52_LVBus356534_consumption, 52_LVBus356534_production, 52_LVBus356535_consumption, 52_LVBus356535_production, 52_LVBus356536_production, 52_LVBus356537_production, 52_LVBus356538_production, 52_LVBus356539_production, 52_LVBus356540_production, 52_LVBus356541_consumption, 52_LVBus356541_production, 52_LVBus356542_production, 52_LVBus356543_consumption, 52_LVBus356543_production, 52_LVBus356545_production, 52_LVBus356546_production, 52_LVBus356547_production, 52_LVBus356548_production, 52_LVBus356549_production, 52_LVBus356550_production, 52_LVBus356551_consumption, 52_LVBus356551_production, 52_LVBus356553_consumption, 52_LVBus356553_production, 52_LVBus356554_production, 52_LVBus356555_consumption, 52_LVBus356555_production, 52_LVBus356556_consumption, 52_LVBus356556_production, 52_LVBus356557_production, 52_LVBus356558_production, 52_LVBus356559_production, 52_LVBus356560_production, 52_LVBus356561_production, 52_LVBus356563_production, 52_LVBus356565_production, 52_LVBus356567_consumption, 52_LVBus356567_production, 52_LVBus356568_production, 52_LVBus356569_production, 52_LVBus356570_production, 52_LVBus356571_production, 52_LVBus356572_production, 52_LVBus356574_consumption, 52_LVBus356574_production, 52_LVBus356576_production, 52_LVBus356577_production, 52_LVBus356578_production, 52_LVBus356579_production, 52_LVBus356581_production, 52_LVBus356582_production, 52_LVBus356583_production, 52_LVBus356584_production, 52_LVBus356585_consumption, 52_LVBus356585_production, 52_LVBus356586_consumption, 52_LVBus356586_production, 52_LVBus356588_consumption, 52_LVBus356588_production, 52_LVBus356589_production, 52_LVBus356590_production, 52_LVBus356591_production, 52_LVBus356592_production, 52_LVBus356593_production, 52_LVBus356594_consumption, 52_LVBus356594_production, 52_LVBus356595_production, 52_LVBus356596_production, 52_LVBus356597_production, 52_LVBus356598_production, 52_LVBus356600_production, 52_LVBus356601_production, 52_LVBus356602_production, 52_LVBus356604_consumption, 52_LVBus356604_production, 52_LVBus356605_production, 52_LVBus356606_production, 52_LVBus356607_consumption, 52_LVBus356607_production, 52_LVBus356608_production, 52_LVBus356609_production, 52_LVBus356610_production, 52_LVBus356611_production, 52_LVBus356612_production, 52_LVBus356614_production, 52_LVBus356615_production, 52_LVBus356616_consumption, 52_LVBus356616_production, 52_LVBus356618_production, 52_LVBus356619_production, 52_LVBus356621_production, 52_LVBus356622_production, 52_LVBus356623_production, 52_LVBus356625_production, 52_LVBus356626_production, 52_LVBus356627_production, 52_LVBus356628_production, 52_LVBus356630_production, 52_LVBus356632_production, 52_LVBus356634_production, 52_LVBus356635_production, 52_LVBus356637_consumption, 52_LVBus356637_production, 52_LVBus356638_production, 52_LVBus356640_production, 52_LVBus356642_consumption, 52_LVBus356642_production, 52_LVBus356643_production, 52_LVBus356644_production, 52_LVBus356645_production, 52_LVBus356646_production, 52_LVBus356648_production, 52_LVBus356649_production, 52_LVBus356650_production, 52_LVBus356652_production, 52_LVBus356654_consumption, 52_LVBus356654_production, 52_LVBus356655_production, 52_LVBus356656_production, 52_LVBus356657_production, 52_LVBus356658_production, 52_LVBus356660_production, 52_LVBus356661_production, 52_LVBus356662_production, 52_LVBus356663_production, 52_LVBus356665_production, 52_LVBus356666_production, 52_LVBus356667_production, 52_LVBus356668_production, 52_LVBus356669_production, 52_LVBus356670_consumption, 52_LVBus356670_production, 52_LVBus356672_production, 52_LVBus356673_production, 52_LVBus356674_production, 52_LVBus356675_consumption, 52_LVBus356675_production, 52_LVBus356676_consumption, 52_LVBus356676_production, 52_LVBus356677_production, 52_LVBus356678_production, 52_LVBus356679_production, 52_LVBus356680_production, 52_LVBus356682_production, 52_LVBus356683_production, 52_LVBus356684_consumption, 52_LVBus356684_production, 52_LVBus356685_production, 52_LVBus356686_production, 52_LVBus356690_production, 52_LVBus356691_production, 52_LVBus356692_production, 52_LVBus356694_production, 52_LVBus356696_production, 52_LVBus356697_consumption, 52_LVBus356697_production, 52_LVBus356698_production, 52_LVBus356699_production, 52_LVBus356700_production, 52_LVBus356701_production, 52_LVBus356702_production, 52_LVBus356704_production, 52_LVBus356705_production, 52_LVBus356706_production, 52_LVBus356707_production, 52_LVBus356708_production, 52_LVBus356710_production, 52_LVBus356711_production, 52_LVBus356713_consumption, 52_LVBus356713_production, 52_LVBus356714_production, 52_LVBus356716_production, 52_LVBus356717_consumption, 52_LVBus356717_production, 52_LVBus356718_production, 52_LVBus356720_consumption, 52_LVBus356720_production, 52_LVBus356721_consumption, 52_LVBus356721_production, 52_LVBus356723_production, 52_LVBus356724_production, 52_LVBus356725_production, 52_LVBus356727_production, 52_LVBus356728_production, 52_LVBus356729_production, 52_LVBus356730_production, 52_LVBus356731_production, 52_LVBus356732_production, 52_LVBus356733_production, 52_LVBus356734_production, 52_LVBus356735_production, 52_LVBus356736_production, 52_LVBus356741_production, 52_LVBus356742_consumption, 52_LVBus356742_production, 52_LVBus356743_production, 52_LVBus356744_production, 52_LVBus356748_production, 52_LVBus356750_consumption, 52_LVBus356750_production, 52_LVBus356751_production, 52_LVBus356752_production, 52_LVBus356754_production, 52_LVBus356755_production, 52_LVBus356756_production, 52_LVBus356757_production, 52_LVBus356759_production, 52_LVBus356760_production, 52_LVBus356761_production, 52_LVBus356763_production, 52_LVBus356764_production, 52_LVBus356765_production, 52_LVBus356766_production, 52_LVBus356767_production, 52_LVBus356768_production, 52_LVBus356769_production, 52_LVBus356770_production, 52_LVBus356771_production, 52_LVBus356772_production, 52_LVBus356774_production, 52_LVBus356775_consumption, 52_LVBus356775_production, 52_LVBus356776_consumption, 52_LVBus356776_production, 52_LVBus356777_production, 52_LVBus356778_production, 52_LVBus356781_production, 52_LVBus356782_consumption, 52_LVBus356782_production, 52_LVBus356783_production, 52_LVBus356784_production, 52_LVBus356785_production, 52_LVBus356787_production, 52_LVBus356788_production, 52_LVBus356789_production, 52_LVBus356790_production, 52_LVBus356791_production, 52_LVBus356793_production, 52_LVBus356794_production, 52_LVBus356796_production, 52_LVBus356797_production, 52_LVBus356799_production, 52_LVBus356800_production, 52_LVBus356801_production, 52_LVBus356802_production, 52_LVBus356804_production, 52_LVBus356805_production, 52_LVBus356806_production, 52_LVBus356807_production, 52_LVBus356809_production, 52_LVBus356810_production, 52_LVBus356815_consumption, 52_LVBus356815_production, 52_LVBus356816_production, 52_LVBus356817_consumption, 52_LVBus356817_production, 52_LVBus356818_production, 52_LVBus356819_production, 52_LVBus356821_consumption, 52_LVBus356821_production, 52_LVBus356822_production, 52_LVBus356823_production, 52_LVBus356824_production, 52_LVBus356825_production, 52_LVBus356826_production, 52_LVBus356827_production, 52_LVBus356832_production, 52_LVBus356833_production, 52_LVBus356834_production, 52_LVBus356836_production, 52_LVBus356837_production, 52_LVBus356838_consumption, 52_LVBus356838_production, 52_LVBus356839_consumption, 52_LVBus356839_production, 52_LVBus356840_consumption, 52_LVBus356840_production, 52_LVBus356841_production, 52_LVBus356842_production, 52_LVBus356843_production, 52_LVBus356844_production, 52_LVBus356846_production, 52_LVBus356847_production, 52_LVBus356848_production, 52_LVBus356850_consumption, 52_LVBus356850_production, 52_LVBus356851_production, 52_LVBus356852_production, 52_LVBus356853_production, 52_LVBus356855_production, 52_LVBus356856_production, 52_LVBus356857_production, 52_LVBus356858_consumption, 52_LVBus356858_production, 52_LVBus356859_production, 52_LVBus356861_production, 52_LVBus356862_production, 52_LVBus356864_production, 52_LVBus356865_production, 52_LVBus356867_production, 52_LVBus356868_production, 52_LVBus356869_production, 52_LVBus356870_production, 52_LVBus356871_production, 52_LVBus356873_production, 52_LVBus356875_production, 52_LVBus356876_production, 52_LVBus356877_production, 52_LVBus356879_production, 52_LVBus356880_production, 52_LVBus356881_production, 52_LVBus356882_production, 52_LVBus356883_production, 52_LVBus356885_production, 52_LVBus356887_consumption, 52_LVBus356887_production, 52_LVBus356888_production, 52_LVBus356890_production, 52_LVBus356891_production, 52_LVBus356892_production, 52_LVBus356893_production, 52_LVBus356895_production, 52_LVBus356896_production, 52_LVBus356897_production, 52_LVBus356898_production, 52_LVBus356900_production, 52_LVBus356901_production, 52_LVBus356902_production, 52_LVBus356903_consumption, 52_LVBus356903_production, 52_LVBus356904_consumption, 52_LVBus356904_production, 52_LVBus356905_production, 52_LVBus356907_production, 52_LVBus356908_production, 52_LVBus356909_production, 52_LVBus356910_production, 52_LVBus356911_production, 52_LVBus356913_production, 52_LVBus356914_production, 52_LVBus356918_production, 52_LVBus356919_production, 52_LVBus356920_consumption, 52_LVBus356920_production, 52_LVBus356921_production, 52_LVBus356922_production, 52_LVBus356923_production, 52_LVBus356924_production, 52_LVBus356926_production, 52_LVBus356928_production, 52_LVBus356929_consumption, 52_LVBus356929_production, 52_LVBus356930_production, 52_LVBus356931_production, 52_LVBus356933_production, 52_LVBus356934_production, 52_LVBus356935_production, 52_LVBus356936_production, 52_LVBus356937_production.

