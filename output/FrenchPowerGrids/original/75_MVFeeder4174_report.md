# BMOPF Network Summary: 75_MVFeeder4174

**Generated:** 2026-10-01 23:34:29  
**Findings:** 0 errors · 5 warnings · 378 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 34 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 638 |  |
| line | 603 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1058 | 1.026 MW, 307.7 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 34 |  |
| switch | 0 |  |
| transformer | 34 | Dyn11×34 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 76 | 75 | 2 | 0 |
| LV_236V | 236.0 V | 562 | 528 | 1056 | 0 |

**Transformer transitions:**

- `75_MVLV093817_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047442_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV172636_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV134937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV046976_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047505_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV071229_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV027028_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047550_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV153334_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV083942_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV077502_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV134988_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV034826_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV172637_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV134934_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036148_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV009792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047489_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV169260_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV133580_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV098484_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV170111_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV093896_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127658_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV148971_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV008191_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV093895_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV110905_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036052_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV157184_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047479_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047524_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV089276_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 214 |
| Tree depth (max hops) | 34 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 638 | 1 | 637 | 0 | 0 | 0 |
| Tier LV_236V | 562 | 34 | 528 | 0 | 0 | 0 |
| Tier MV_11.8kV | 76 | 1 | 75 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 34; skipped invalid branches: 0.

Galvanic zones: 35; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MVBus131783 | MV_11.8kV | 76 | 0 | 0 | 34 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2476 declared bus terminals; 2337 mapped line/closed-switch conductor edges; 139 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 8650.0 | 2.803 | 3174 |
| q_nom | 0.0 | 2600.0 | 2.803 | 3174 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.12 | 1970.0 | 1.493 | 603 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.548 | 34 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 669 of 1058 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695392_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695325_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695753_consumption' has phase imbalance of 179.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695285_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695553_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1993966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695630_consumption' has phase imbalance of 168.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695409_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695562_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695367_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695453_consumption' has phase imbalance of 240.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695671_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695431_consumption' has phase imbalance of 198.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1996863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695272_consumption' has phase imbalance of 240.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695298_consumption' has phase imbalance of 227.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695405_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695457_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695333_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695542_consumption' has phase imbalance of 243.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695382_consumption' has phase imbalance of 211.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695766_consumption' has phase imbalance of 281.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695558_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695566_consumption' has phase imbalance of 114.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695538_consumption' has phase imbalance of 101.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695510_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695329_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695248_consumption' has phase imbalance of 242.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1956435_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695576_consumption' has phase imbalance of 57.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695306_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695650_consumption' has phase imbalance of 104.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695312_consumption' has phase imbalance of 249.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695311_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695491_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1956437_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1991180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695393_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695571_consumption' has phase imbalance of 112.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695789_consumption' has phase imbalance of 101.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695567_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695443_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695492_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695568_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695349_consumption' has phase imbalance of 280.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1939481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1918163_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1996860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695394_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695632_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695259_consumption' has phase imbalance of 131.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695343_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695537_consumption' has phase imbalance of 211.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695636_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695261_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695633_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695777_consumption' has phase imbalance of 264.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695386_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1956434_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695292_consumption' has phase imbalance of 266.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695526_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695738_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695675_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695672_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695447_consumption' has phase imbalance of 208.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695440_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695489_consumption' has phase imbalance of 193.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695656_consumption' has phase imbalance of 257.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695509_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695326_consumption' has phase imbalance of 264.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695780_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695759_consumption' has phase imbalance of 169.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695299_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695350_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695734_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695464_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695533_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695448_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695362_consumption' has phase imbalance of 236.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695415_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695314_consumption' has phase imbalance of 155.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695790_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695296_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1918162_consumption' has phase imbalance of 205.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695378_consumption' has phase imbalance of 155.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695622_consumption' has phase imbalance of 295.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695661_consumption' has phase imbalance of 168.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695368_consumption' has phase imbalance of 237.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695520_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695767_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695631_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695565_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695524_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695771_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1918164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695500_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695317_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1918135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695291_consumption' has phase imbalance of 252.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695663_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695305_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695249_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695273_consumption' has phase imbalance of 260.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695676_consumption' has phase imbalance of 275.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1956436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695419_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695396_consumption' has phase imbalance of 20.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695527_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695634_consumption' has phase imbalance of 126.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695264_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695723_consumption' has phase imbalance of 176.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695459_consumption' has phase imbalance of 203.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695688_consumption' has phase imbalance of 170.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695281_consumption' has phase imbalance of 288.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695381_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1991177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695422_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695605_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1991179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695646_consumption' has phase imbalance of 266.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695345_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1988145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695694_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1991181_consumption' has phase imbalance of 226.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695690_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1928902_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695578_consumption' has phase imbalance of 85.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695477_consumption' has phase imbalance of 194.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695432_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695604_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695468_consumption' has phase imbalance of 41.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695593_consumption' has phase imbalance of 266.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1918161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695399_consumption' has phase imbalance of 287.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695546_consumption' has phase imbalance of 239.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695689_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695543_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695424_consumption' has phase imbalance of 212.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695608_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695460_consumption' has phase imbalance of 173.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695260_consumption' has phase imbalance of 175.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695677_consumption' has phase imbalance of 128.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1996861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695505_consumption' has phase imbalance of 57.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695436_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695465_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695782_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695679_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695659_consumption' has phase imbalance of 270.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695572_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695712_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695266_consumption' has phase imbalance of 121.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1918157_consumption' has phase imbalance of 293.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695502_consumption' has phase imbalance of 274.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695418_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695430_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695813_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695417_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695498_consumption' has phase imbalance of 169.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695603_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695564_consumption' has phase imbalance of 262.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695300_consumption' has phase imbalance of 176.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695267_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695308_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695814_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695770_consumption' has phase imbalance of 26.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1991178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695781_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695765_consumption' has phase imbalance of 226.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695342_consumption' has phase imbalance of 143.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695693_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695709_consumption' has phase imbalance of 132.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695439_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695685_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695597_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695458_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695554_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695735_consumption' has phase imbalance of 40.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695773_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695271_consumption' has phase imbalance of 121.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695582_consumption' has phase imbalance of 232.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695626_consumption' has phase imbalance of 205.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695301_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695385_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695495_consumption' has phase imbalance of 227.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695678_consumption' has phase imbalance of 274.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695462_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695416_consumption' has phase imbalance of 197.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695408_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695376_consumption' has phase imbalance of 250.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695352_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695569_consumption' has phase imbalance of 240.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695664_consumption' has phase imbalance of 138.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695268_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695624_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695288_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695324_consumption' has phase imbalance of 30.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695494_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695366_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695697_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695788_consumption' has phase imbalance of 255.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695525_consumption' has phase imbalance of 84.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695344_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695812_consumption' has phase imbalance of 200.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695797_consumption' has phase imbalance of 274.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695265_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695680_consumption' has phase imbalance of 244.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695695_consumption' has phase imbalance of 237.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1996865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695404_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695304_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695544_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695511_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695715_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695673_consumption' has phase imbalance of 56.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695353_consumption' has phase imbalance of 246.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695620_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695452_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695756_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695791_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695555_consumption' has phase imbalance of 234.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1695669_consumption' has phase imbalance of 279.3%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1058 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1695445' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.026 MW |
| Total load Q | 307.7 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV093817_Transformer | 110.0 kVA | 2.8% |
| 75_MVLV047442_Transformer | 176.0 kVA | 10.5% |
| 75_MVLV172636_Transformer | 176.0 kVA | 21.1% |
| 75_MVLV134937_Transformer | 110.0 kVA | 2.5% |
| 75_MVLV046976_Transformer | 176.0 kVA | 6.2% |
| 75_MVLV047505_Transformer | 275.0 kVA | 12.0% |
| 75_MVLV071229_Transformer | 110.0 kVA | 7.1% |
| 75_MVLV027028_Transformer | 110.0 kVA | 12.3% |
| 75_MVLV047550_Transformer | 176.0 kVA | 17.3% |
| 75_MVLV153334_Transformer | 176.0 kVA | 6.5% |
| 75_MVLV083942_Transformer | 110.0 kVA | 4.3% |
| 75_MVLV077502_Transformer | 110.0 kVA | 8.3% |
| 75_MVLV134988_Transformer | 176.0 kVA | 18.9% |
| 75_MVLV034826_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV172637_Transformer | 440.0 kVA | 21.7% |
| 75_MVLV134934_Transformer | 176.0 kVA | 13.2% |
| 75_MVLV036148_Transformer | 275.0 kVA | 10.8% |
| 75_MVLV009792_Transformer | 110.0 kVA | 2.2% |
| 75_MVLV047489_Transformer | 275.0 kVA | 13.4% |
| 75_MVLV169260_Transformer | 176.0 kVA | 13.4% |
| 75_MVLV133580_Transformer | 440.0 kVA | 11.8% |
| 75_MVLV098484_Transformer | 110.0 kVA | 12.6% |
| 75_MVLV170111_Transformer | 176.0 kVA | 15.1% |
| 75_MVLV093896_Transformer | 440.0 kVA | 8.9% |
| 75_MVLV127658_Transformer | 275.0 kVA | 24.1% |
| 75_MVLV148971_Transformer | 176.0 kVA | 15.3% |
| 75_MVLV008191_Transformer | 110.0 kVA | 1.8% |
| 75_MVLV093895_Transformer | 440.0 kVA | 25.5% |
| 75_MVLV110905_Transformer | 110.0 kVA | 0.0% |
| 75_MVLV036052_Transformer | 440.0 kVA | 26.3% |
| 75_MVLV157184_Transformer | 440.0 kVA | 26.4% |
| 75_MVLV047479_Transformer | 110.0 kVA | 7.2% |
| 75_MVLV047524_Transformer | 176.0 kVA | 12.5% |
| 75_MVLV089276_Transformer | 275.0 kVA | 15.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.03 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1695445' (LV, 0.24 kV) has an electrical reach of 10.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 638 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 638 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 34 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 76 |
| LV_236V | 4-wire | 562 / 562 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 562 |
| Neutral branches | 528 |
| Grounding points | 34 |
| Neutral sections | 34 |
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
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 45 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 49 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 35 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1350.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 562 / 76 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 670 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 670 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1695233_consumption, 75_LVBus1695233_production, 75_LVBus1695234_consumption, 75_LVBus1695234_production, 75_LVBus1695235_consumption, 75_LVBus1695235_production, 75_LVBus1695236_consumption, 75_LVBus1695236_production, 75_LVBus1695237_production, 75_LVBus1695238_production, 75_LVBus1695239_consumption, 75_LVBus1695239_production, 75_LVBus1695240_consumption, 75_LVBus1695240_production, 75_LVBus1695241_production, 75_LVBus1695243_consumption, 75_LVBus1695243_production, 75_LVBus1695244_production, 75_LVBus1695246_production, 75_LVBus1695248_production, 75_LVBus1695249_production, 75_LVBus1695250_consumption, 75_LVBus1695250_production, 75_LVBus1695251_production, 75_LVBus1695252_production, 75_LVBus1695253_production, 75_LVBus1695255_consumption, 75_LVBus1695255_production, 75_LVBus1695257_consumption, 75_LVBus1695257_production, 75_LVBus1695258_production, 75_LVBus1695259_production, 75_LVBus1695260_production, 75_LVBus1695261_production, 75_LVBus1695262_production, 75_LVBus1695264_production, 75_LVBus1695265_production, 75_LVBus1695266_production, 75_LVBus1695267_production, 75_LVBus1695268_production, 75_LVBus1695269_consumption, 75_LVBus1695269_production, 75_LVBus1695270_production, 75_LVBus1695271_production, 75_LVBus1695272_production, 75_LVBus1695273_production, 75_LVBus1695275_consumption, 75_LVBus1695275_production, 75_LVBus1695276_production, 75_LVBus1695278_production, 75_LVBus1695279_production, 75_LVBus1695280_production, 75_LVBus1695281_production, 75_LVBus1695282_production, 75_LVBus1695283_production, 75_LVBus1695284_consumption, 75_LVBus1695284_production, 75_LVBus1695285_production, 75_LVBus1695286_consumption, 75_LVBus1695286_production, 75_LVBus1695288_production, 75_LVBus1695289_production, 75_LVBus1695290_production, 75_LVBus1695291_production, 75_LVBus1695292_production, 75_LVBus1695293_production, 75_LVBus1695294_production, 75_LVBus1695295_production, 75_LVBus1695296_production, 75_LVBus1695297_production, 75_LVBus1695298_production, 75_LVBus1695299_production, 75_LVBus1695300_production, 75_LVBus1695301_production, 75_LVBus1695303_consumption, 75_LVBus1695303_production, 75_LVBus1695304_production, 75_LVBus1695305_production, 75_LVBus1695306_production, 75_LVBus1695307_production, 75_LVBus1695308_production, 75_LVBus1695309_consumption, 75_LVBus1695309_production, 75_LVBus1695311_production, 75_LVBus1695312_production, 75_LVBus1695313_consumption, 75_LVBus1695313_production, 75_LVBus1695314_production, 75_LVBus1695315_consumption, 75_LVBus1695315_production, 75_LVBus1695316_production, 75_LVBus1695317_production, 75_LVBus1695318_production, 75_LVBus1695320_consumption, 75_LVBus1695320_production, 75_LVBus1695321_production, 75_LVBus1695322_production, 75_LVBus1695323_consumption, 75_LVBus1695323_production, 75_LVBus1695324_production, 75_LVBus1695325_production, 75_LVBus1695326_production, 75_LVBus1695327_consumption, 75_LVBus1695327_production, 75_LVBus1695328_consumption, 75_LVBus1695328_production, 75_LVBus1695329_production, 75_LVBus1695331_consumption, 75_LVBus1695331_production, 75_LVBus1695333_production, 75_LVBus1695334_production, 75_LVBus1695335_consumption, 75_LVBus1695335_production, 75_LVBus1695339_consumption, 75_LVBus1695339_production, 75_LVBus1695340_production, 75_LVBus1695341_production, 75_LVBus1695342_production, 75_LVBus1695343_production, 75_LVBus1695344_production, 75_LVBus1695345_production, 75_LVBus1695349_production, 75_LVBus1695350_production, 75_LVBus1695351_production, 75_LVBus1695352_production, 75_LVBus1695353_production, 75_LVBus1695354_consumption, 75_LVBus1695354_production, 75_LVBus1695355_production, 75_LVBus1695356_production, 75_LVBus1695357_production, 75_LVBus1695358_consumption, 75_LVBus1695358_production, 75_LVBus1695360_production, 75_LVBus1695361_consumption, 75_LVBus1695361_production, 75_LVBus1695362_production, 75_LVBus1695363_production, 75_LVBus1695364_production, 75_LVBus1695365_consumption, 75_LVBus1695365_production, 75_LVBus1695366_production, 75_LVBus1695367_production, 75_LVBus1695368_production, 75_LVBus1695369_consumption, 75_LVBus1695369_production, 75_LVBus1695371_production, 75_LVBus1695372_consumption, 75_LVBus1695372_production, 75_LVBus1695373_consumption, 75_LVBus1695373_production, 75_LVBus1695374_production, 75_LVBus1695375_consumption, 75_LVBus1695375_production, 75_LVBus1695376_production, 75_LVBus1695377_production, 75_LVBus1695378_production, 75_LVBus1695379_consumption, 75_LVBus1695379_production, 75_LVBus1695380_consumption, 75_LVBus1695380_production, 75_LVBus1695381_production, 75_LVBus1695382_production, 75_LVBus1695383_consumption, 75_LVBus1695383_production, 75_LVBus1695385_production, 75_LVBus1695386_production, 75_LVBus1695387_production, 75_LVBus1695388_consumption, 75_LVBus1695388_production, 75_LVBus1695389_production, 75_LVBus1695390_production, 75_LVBus1695391_production, 75_LVBus1695392_production, 75_LVBus1695393_production, 75_LVBus1695394_production, 75_LVBus1695396_production, 75_LVBus1695397_production, 75_LVBus1695398_production, 75_LVBus1695399_production, 75_LVBus1695400_consumption, 75_LVBus1695400_production, 75_LVBus1695402_consumption, 75_LVBus1695402_production, 75_LVBus1695403_consumption, 75_LVBus1695403_production, 75_LVBus1695404_production, 75_LVBus1695405_production, 75_LVBus1695406_production, 75_LVBus1695407_consumption, 75_LVBus1695407_production, 75_LVBus1695408_production, 75_LVBus1695409_production, 75_LVBus1695410_consumption, 75_LVBus1695410_production, 75_LVBus1695414_consumption, 75_LVBus1695414_production, 75_LVBus1695415_production, 75_LVBus1695416_production, 75_LVBus1695417_production, 75_LVBus1695418_production, 75_LVBus1695419_production, 75_LVBus1695420_production, 75_LVBus1695421_consumption, 75_LVBus1695421_production, 75_LVBus1695422_production, 75_LVBus1695423_production, 75_LVBus1695424_production, 75_LVBus1695425_production, 75_LVBus1695429_production, 75_LVBus1695430_production, 75_LVBus1695431_production, 75_LVBus1695432_production, 75_LVBus1695433_consumption, 75_LVBus1695433_production, 75_LVBus1695435_consumption, 75_LVBus1695435_production, 75_LVBus1695436_production, 75_LVBus1695438_consumption, 75_LVBus1695438_production, 75_LVBus1695439_production, 75_LVBus1695440_production, 75_LVBus1695441_consumption, 75_LVBus1695441_production, 75_LVBus1695442_consumption, 75_LVBus1695442_production, 75_LVBus1695443_production, 75_LVBus1695445_production, 75_LVBus1695447_production, 75_LVBus1695448_production, 75_LVBus1695450_production, 75_LVBus1695451_production, 75_LVBus1695452_production, 75_LVBus1695453_production, 75_LVBus1695454_production, 75_LVBus1695455_consumption, 75_LVBus1695455_production, 75_LVBus1695456_production, 75_LVBus1695457_production, 75_LVBus1695458_production, 75_LVBus1695459_production, 75_LVBus1695460_production, 75_LVBus1695461_production, 75_LVBus1695462_production, 75_LVBus1695463_production, 75_LVBus1695464_production, 75_LVBus1695465_production, 75_LVBus1695466_production, 75_LVBus1695467_consumption, 75_LVBus1695467_production, 75_LVBus1695468_production, 75_LVBus1695469_consumption, 75_LVBus1695469_production, 75_LVBus1695470_production, 75_LVBus1695472_production, 75_LVBus1695474_production, 75_LVBus1695475_consumption, 75_LVBus1695475_production, 75_LVBus1695476_consumption, 75_LVBus1695476_production, 75_LVBus1695477_production, 75_LVBus1695478_production, 75_LVBus1695482_consumption, 75_LVBus1695482_production, 75_LVBus1695483_consumption, 75_LVBus1695483_production, 75_LVBus1695485_consumption, 75_LVBus1695485_production, 75_LVBus1695486_production, 75_LVBus1695487_production, 75_LVBus1695488_consumption, 75_LVBus1695488_production, 75_LVBus1695489_production, 75_LVBus1695491_production, 75_LVBus1695492_production, 75_LVBus1695493_production, 75_LVBus1695494_production, 75_LVBus1695495_production, 75_LVBus1695496_production, 75_LVBus1695497_production, 75_LVBus1695498_production, 75_LVBus1695499_production, 75_LVBus1695500_production, 75_LVBus1695501_consumption, 75_LVBus1695501_production, 75_LVBus1695502_production, 75_LVBus1695504_production, 75_LVBus1695505_production, 75_LVBus1695506_production, 75_LVBus1695507_production, 75_LVBus1695508_production, 75_LVBus1695509_production, 75_LVBus1695510_production, 75_LVBus1695511_production, 75_LVBus1695512_production, 75_LVBus1695513_consumption, 75_LVBus1695513_production, 75_LVBus1695514_consumption, 75_LVBus1695514_production, 75_LVBus1695515_consumption, 75_LVBus1695515_production, 75_LVBus1695516_consumption, 75_LVBus1695516_production, 75_LVBus1695517_production, 75_LVBus1695519_production, 75_LVBus1695520_production, 75_LVBus1695521_production, 75_LVBus1695522_consumption, 75_LVBus1695522_production, 75_LVBus1695523_production, 75_LVBus1695524_production, 75_LVBus1695525_production, 75_LVBus1695526_production, 75_LVBus1695527_production, 75_LVBus1695529_production, 75_LVBus1695530_production, 75_LVBus1695533_production, 75_LVBus1695535_production, 75_LVBus1695536_production, 75_LVBus1695537_production, 75_LVBus1695538_production, 75_LVBus1695540_production, 75_LVBus1695541_consumption, 75_LVBus1695541_production, 75_LVBus1695542_production, 75_LVBus1695543_production, 75_LVBus1695544_production, 75_LVBus1695545_consumption, 75_LVBus1695545_production, 75_LVBus1695546_production, 75_LVBus1695547_consumption, 75_LVBus1695547_production, 75_LVBus1695549_consumption, 75_LVBus1695549_production, 75_LVBus1695551_consumption, 75_LVBus1695551_production, 75_LVBus1695553_production, 75_LVBus1695554_production, 75_LVBus1695555_production, 75_LVBus1695556_production, 75_LVBus1695558_production, 75_LVBus1695559_production, 75_LVBus1695560_consumption, 75_LVBus1695560_production, 75_LVBus1695561_consumption, 75_LVBus1695561_production, 75_LVBus1695562_production, 75_LVBus1695564_production, 75_LVBus1695565_production, 75_LVBus1695566_production, 75_LVBus1695567_production, 75_LVBus1695568_production, 75_LVBus1695569_production, 75_LVBus1695571_production, 75_LVBus1695572_production, 75_LVBus1695574_consumption, 75_LVBus1695574_production, 75_LVBus1695575_production, 75_LVBus1695576_production, 75_LVBus1695577_consumption, 75_LVBus1695577_production, 75_LVBus1695578_production, 75_LVBus1695579_production, 75_LVBus1695581_production, 75_LVBus1695582_production, 75_LVBus1695583_consumption, 75_LVBus1695583_production, 75_LVBus1695584_production, 75_LVBus1695585_consumption, 75_LVBus1695585_production, 75_LVBus1695586_consumption, 75_LVBus1695586_production, 75_LVBus1695587_consumption, 75_LVBus1695587_production, 75_LVBus1695588_production, 75_LVBus1695590_consumption, 75_LVBus1695590_production, 75_LVBus1695591_consumption, 75_LVBus1695591_production, 75_LVBus1695592_consumption, 75_LVBus1695592_production, 75_LVBus1695593_production, 75_LVBus1695594_consumption, 75_LVBus1695594_production, 75_LVBus1695595_production, 75_LVBus1695597_production, 75_LVBus1695598_production, 75_LVBus1695599_production, 75_LVBus1695601_consumption, 75_LVBus1695601_production, 75_LVBus1695602_production, 75_LVBus1695603_production, 75_LVBus1695604_production, 75_LVBus1695605_production, 75_LVBus1695606_consumption, 75_LVBus1695606_production, 75_LVBus1695607_production, 75_LVBus1695608_production, 75_LVBus1695609_production, 75_LVBus1695610_production, 75_LVBus1695612_consumption, 75_LVBus1695612_production, 75_LVBus1695613_consumption, 75_LVBus1695613_production, 75_LVBus1695614_consumption, 75_LVBus1695614_production, 75_LVBus1695615_consumption, 75_LVBus1695615_production, 75_LVBus1695616_production, 75_LVBus1695620_production, 75_LVBus1695621_production, 75_LVBus1695622_production, 75_LVBus1695623_production, 75_LVBus1695624_production, 75_LVBus1695625_production, 75_LVBus1695626_production, 75_LVBus1695628_consumption, 75_LVBus1695628_production, 75_LVBus1695629_production, 75_LVBus1695630_production, 75_LVBus1695631_production, 75_LVBus1695632_production, 75_LVBus1695633_production, 75_LVBus1695634_production, 75_LVBus1695635_consumption, 75_LVBus1695635_production, 75_LVBus1695636_production, 75_LVBus1695637_consumption, 75_LVBus1695637_production, 75_LVBus1695638_consumption, 75_LVBus1695638_production, 75_LVBus1695639_production, 75_LVBus1695643_production, 75_LVBus1695644_production, 75_LVBus1695645_production, 75_LVBus1695646_production, 75_LVBus1695647_consumption, 75_LVBus1695647_production, 75_LVBus1695648_consumption, 75_LVBus1695648_production, 75_LVBus1695649_production, 75_LVBus1695650_production, 75_LVBus1695651_consumption, 75_LVBus1695651_production, 75_LVBus1695652_production, 75_LVBus1695653_production, 75_LVBus1695654_production, 75_LVBus1695656_production, 75_LVBus1695657_consumption, 75_LVBus1695657_production, 75_LVBus1695659_production, 75_LVBus1695660_production, 75_LVBus1695661_production, 75_LVBus1695662_production, 75_LVBus1695663_production, 75_LVBus1695664_production, 75_LVBus1695666_consumption, 75_LVBus1695666_production, 75_LVBus1695668_production, 75_LVBus1695669_production, 75_LVBus1695670_production, 75_LVBus1695671_production, 75_LVBus1695672_production, 75_LVBus1695673_production, 75_LVBus1695674_consumption, 75_LVBus1695674_production, 75_LVBus1695675_production, 75_LVBus1695676_production, 75_LVBus1695677_production, 75_LVBus1695678_production, 75_LVBus1695679_production, 75_LVBus1695680_production, 75_LVBus1695681_production, 75_LVBus1695682_consumption, 75_LVBus1695682_production, 75_LVBus1695683_production, 75_LVBus1695684_production, 75_LVBus1695685_production, 75_LVBus1695687_consumption, 75_LVBus1695687_production, 75_LVBus1695688_production, 75_LVBus1695689_production, 75_LVBus1695690_production, 75_LVBus1695692_consumption, 75_LVBus1695692_production, 75_LVBus1695693_production, 75_LVBus1695694_production, 75_LVBus1695695_production, 75_LVBus1695696_production, 75_LVBus1695697_production, 75_LVBus1695698_consumption, 75_LVBus1695698_production, 75_LVBus1695699_production, 75_LVBus1695701_consumption, 75_LVBus1695701_production, 75_LVBus1695703_production, 75_LVBus1695704_production, 75_LVBus1695705_consumption, 75_LVBus1695705_production, 75_LVBus1695706_production, 75_LVBus1695707_production, 75_LVBus1695709_production, 75_LVBus1695710_production, 75_LVBus1695711_consumption, 75_LVBus1695711_production, 75_LVBus1695712_production, 75_LVBus1695713_production, 75_LVBus1695714_production, 75_LVBus1695715_production, 75_LVBus1695716_production, 75_LVBus1695717_production, 75_LVBus1695718_production, 75_LVBus1695719_production, 75_LVBus1695721_production, 75_LVBus1695722_consumption, 75_LVBus1695722_production, 75_LVBus1695723_production, 75_LVBus1695724_production, 75_LVBus1695725_production, 75_LVBus1695726_consumption, 75_LVBus1695726_production, 75_LVBus1695727_production, 75_LVBus1695728_production, 75_LVBus1695729_consumption, 75_LVBus1695729_production, 75_LVBus1695730_consumption, 75_LVBus1695730_production, 75_LVBus1695731_production, 75_LVBus1695732_consumption, 75_LVBus1695732_production, 75_LVBus1695733_consumption, 75_LVBus1695733_production, 75_LVBus1695734_production, 75_LVBus1695735_production, 75_LVBus1695736_production, 75_LVBus1695737_consumption, 75_LVBus1695737_production, 75_LVBus1695738_production, 75_LVBus1695740_consumption, 75_LVBus1695740_production, 75_LVBus1695741_consumption, 75_LVBus1695741_production, 75_LVBus1695745_production, 75_LVBus1695746_production, 75_LVBus1695747_consumption, 75_LVBus1695747_production, 75_LVBus1695748_production, 75_LVBus1695749_production, 75_LVBus1695750_consumption, 75_LVBus1695750_production, 75_LVBus1695751_production, 75_LVBus1695752_consumption, 75_LVBus1695752_production, 75_LVBus1695753_production, 75_LVBus1695754_consumption, 75_LVBus1695754_production, 75_LVBus1695755_production, 75_LVBus1695756_production, 75_LVBus1695757_production, 75_LVBus1695758_production, 75_LVBus1695759_production, 75_LVBus1695763_consumption, 75_LVBus1695763_production, 75_LVBus1695764_production, 75_LVBus1695765_production, 75_LVBus1695766_production, 75_LVBus1695767_production, 75_LVBus1695768_production, 75_LVBus1695769_production, 75_LVBus1695770_production, 75_LVBus1695771_production, 75_LVBus1695772_production, 75_LVBus1695773_production, 75_LVBus1695774_production, 75_LVBus1695776_consumption, 75_LVBus1695776_production, 75_LVBus1695777_production, 75_LVBus1695778_production, 75_LVBus1695779_production, 75_LVBus1695780_production, 75_LVBus1695781_production, 75_LVBus1695782_production, 75_LVBus1695783_production, 75_LVBus1695784_consumption, 75_LVBus1695784_production, 75_LVBus1695785_consumption, 75_LVBus1695785_production, 75_LVBus1695786_production, 75_LVBus1695787_consumption, 75_LVBus1695787_production, 75_LVBus1695788_production, 75_LVBus1695789_production, 75_LVBus1695790_production, 75_LVBus1695791_production, 75_LVBus1695792_consumption, 75_LVBus1695792_production, 75_LVBus1695793_production, 75_LVBus1695794_production, 75_LVBus1695795_production, 75_LVBus1695796_consumption, 75_LVBus1695796_production, 75_LVBus1695797_production, 75_LVBus1695798_production, 75_LVBus1695800_consumption, 75_LVBus1695800_production, 75_LVBus1695802_production, 75_LVBus1695804_production, 75_LVBus1695805_production, 75_LVBus1695806_consumption, 75_LVBus1695806_production, 75_LVBus1695807_production, 75_LVBus1695808_consumption, 75_LVBus1695808_production, 75_LVBus1695809_production, 75_LVBus1695810_consumption, 75_LVBus1695810_production, 75_LVBus1695811_production, 75_LVBus1695812_production, 75_LVBus1695813_production, 75_LVBus1695814_production, 75_LVBus1918135_production, 75_LVBus1918157_production, 75_LVBus1918158_consumption, 75_LVBus1918158_production, 75_LVBus1918159_consumption, 75_LVBus1918159_production, 75_LVBus1918160_consumption, 75_LVBus1918160_production, 75_LVBus1918161_production, 75_LVBus1918162_production, 75_LVBus1918163_production, 75_LVBus1918164_production, 75_LVBus1918165_consumption, 75_LVBus1918165_production, 75_LVBus1928902_production, 75_LVBus1939481_production, 75_LVBus1951336_consumption, 75_LVBus1951336_production, 75_LVBus1956434_production, 75_LVBus1956435_production, 75_LVBus1956436_production, 75_LVBus1956437_production, 75_LVBus1975648_consumption, 75_LVBus1975648_production, 75_LVBus1977530_consumption, 75_LVBus1977530_production, 75_LVBus1988145_production, 75_LVBus1991174_consumption, 75_LVBus1991174_production, 75_LVBus1991175_consumption, 75_LVBus1991175_production, 75_LVBus1991176_consumption, 75_LVBus1991176_production, 75_LVBus1991177_production, 75_LVBus1991178_production, 75_LVBus1991179_production, 75_LVBus1991180_production, 75_LVBus1991181_production, 75_LVBus1993966_production, 75_LVBus1996859_consumption, 75_LVBus1996859_production, 75_LVBus1996860_production, 75_LVBus1996861_production, 75_LVBus1996862_consumption, 75_LVBus1996862_production, 75_LVBus1996863_production, 75_LVBus1996864_production, 75_LVBus1996865_production, 75_MVLV047457_consumption, 75_MVLV047457_production.

## 9. Data Quality Summary

**Total findings:** 383 (0 errors, 5 warnings, 378 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  669 of 1058 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.03 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  670 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695392_consumption`  
  Load '75_LVBus1695392_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695325_consumption`  
  Load '75_LVBus1695325_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695466_consumption`  
  Load '75_LVBus1695466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695753_consumption`  
  Load '75_LVBus1695753_consumption' has phase imbalance of 179.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695285_consumption`  
  Load '75_LVBus1695285_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695645_consumption`  
  Load '75_LVBus1695645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695244_consumption`  
  Load '75_LVBus1695244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695553_consumption`  
  Load '75_LVBus1695553_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1993966_consumption`  
  Load '75_LVBus1993966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695630_consumption`  
  Load '75_LVBus1695630_consumption' has phase imbalance of 168.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695409_consumption`  
  Load '75_LVBus1695409_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695562_consumption`  
  Load '75_LVBus1695562_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695397_consumption`  
  Load '75_LVBus1695397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695293_consumption`  
  Load '75_LVBus1695293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695322_consumption`  
  Load '75_LVBus1695322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695367_consumption`  
  Load '75_LVBus1695367_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695453_consumption`  
  Load '75_LVBus1695453_consumption' has phase imbalance of 240.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695696_consumption`  
  Load '75_LVBus1695696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695671_consumption`  
  Load '75_LVBus1695671_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695431_consumption`  
  Load '75_LVBus1695431_consumption' has phase imbalance of 198.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1996863_consumption`  
  Load '75_LVBus1996863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695272_consumption`  
  Load '75_LVBus1695272_consumption' has phase imbalance of 240.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695298_consumption`  
  Load '75_LVBus1695298_consumption' has phase imbalance of 227.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695507_consumption`  
  Load '75_LVBus1695507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695405_consumption`  
  Load '75_LVBus1695405_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695456_consumption`  
  Load '75_LVBus1695456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695457_consumption`  
  Load '75_LVBus1695457_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695333_consumption`  
  Load '75_LVBus1695333_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695684_consumption`  
  Load '75_LVBus1695684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695725_consumption`  
  Load '75_LVBus1695725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695542_consumption`  
  Load '75_LVBus1695542_consumption' has phase imbalance of 243.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695382_consumption`  
  Load '75_LVBus1695382_consumption' has phase imbalance of 211.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695766_consumption`  
  Load '75_LVBus1695766_consumption' has phase imbalance of 281.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695558_consumption`  
  Load '75_LVBus1695558_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695595_consumption`  
  Load '75_LVBus1695595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695811_consumption`  
  Load '75_LVBus1695811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695556_consumption`  
  Load '75_LVBus1695556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695566_consumption`  
  Load '75_LVBus1695566_consumption' has phase imbalance of 114.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695294_consumption`  
  Load '75_LVBus1695294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695538_consumption`  
  Load '75_LVBus1695538_consumption' has phase imbalance of 101.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695510_consumption`  
  Load '75_LVBus1695510_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695329_consumption`  
  Load '75_LVBus1695329_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695252_consumption`  
  Load '75_LVBus1695252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695295_consumption`  
  Load '75_LVBus1695295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695355_consumption`  
  Load '75_LVBus1695355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695276_consumption`  
  Load '75_LVBus1695276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695699_consumption`  
  Load '75_LVBus1695699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695248_consumption`  
  Load '75_LVBus1695248_consumption' has phase imbalance of 242.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695768_consumption`  
  Load '75_LVBus1695768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695253_consumption`  
  Load '75_LVBus1695253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1956435_consumption`  
  Load '75_LVBus1956435_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695598_consumption`  
  Load '75_LVBus1695598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695360_consumption`  
  Load '75_LVBus1695360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695576_consumption`  
  Load '75_LVBus1695576_consumption' has phase imbalance of 57.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695306_consumption`  
  Load '75_LVBus1695306_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695334_consumption`  
  Load '75_LVBus1695334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695650_consumption`  
  Load '75_LVBus1695650_consumption' has phase imbalance of 104.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695312_consumption`  
  Load '75_LVBus1695312_consumption' has phase imbalance of 249.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695311_consumption`  
  Load '75_LVBus1695311_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695491_consumption`  
  Load '75_LVBus1695491_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1956437_consumption`  
  Load '75_LVBus1956437_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1991180_consumption`  
  Load '75_LVBus1991180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695356_consumption`  
  Load '75_LVBus1695356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695523_consumption`  
  Load '75_LVBus1695523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695429_consumption`  
  Load '75_LVBus1695429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695391_consumption`  
  Load '75_LVBus1695391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695363_consumption`  
  Load '75_LVBus1695363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695393_consumption`  
  Load '75_LVBus1695393_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695571_consumption`  
  Load '75_LVBus1695571_consumption' has phase imbalance of 112.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695789_consumption`  
  Load '75_LVBus1695789_consumption' has phase imbalance of 101.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695567_consumption`  
  Load '75_LVBus1695567_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695443_consumption`  
  Load '75_LVBus1695443_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695492_consumption`  
  Load '75_LVBus1695492_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695568_consumption`  
  Load '75_LVBus1695568_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695349_consumption`  
  Load '75_LVBus1695349_consumption' has phase imbalance of 280.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1939481_consumption`  
  Load '75_LVBus1939481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1918163_consumption`  
  Load '75_LVBus1918163_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1996860_consumption`  
  Load '75_LVBus1996860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695394_consumption`  
  Load '75_LVBus1695394_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695719_consumption`  
  Load '75_LVBus1695719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695727_consumption`  
  Load '75_LVBus1695727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695632_consumption`  
  Load '75_LVBus1695632_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695259_consumption`  
  Load '75_LVBus1695259_consumption' has phase imbalance of 131.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695343_consumption`  
  Load '75_LVBus1695343_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695537_consumption`  
  Load '75_LVBus1695537_consumption' has phase imbalance of 211.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695636_consumption`  
  Load '75_LVBus1695636_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695718_consumption`  
  Load '75_LVBus1695718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695261_consumption`  
  Load '75_LVBus1695261_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695633_consumption`  
  Load '75_LVBus1695633_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695731_consumption`  
  Load '75_LVBus1695731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695623_consumption`  
  Load '75_LVBus1695623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695316_consumption`  
  Load '75_LVBus1695316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695581_consumption`  
  Load '75_LVBus1695581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695487_consumption`  
  Load '75_LVBus1695487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695777_consumption`  
  Load '75_LVBus1695777_consumption' has phase imbalance of 264.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695579_consumption`  
  Load '75_LVBus1695579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695670_consumption`  
  Load '75_LVBus1695670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695386_consumption`  
  Load '75_LVBus1695386_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1956434_consumption`  
  Load '75_LVBus1956434_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695297_consumption`  
  Load '75_LVBus1695297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695292_consumption`  
  Load '75_LVBus1695292_consumption' has phase imbalance of 266.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695526_consumption`  
  Load '75_LVBus1695526_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695738_consumption`  
  Load '75_LVBus1695738_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695675_consumption`  
  Load '75_LVBus1695675_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695672_consumption`  
  Load '75_LVBus1695672_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695447_consumption`  
  Load '75_LVBus1695447_consumption' has phase imbalance of 208.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695440_consumption`  
  Load '75_LVBus1695440_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695489_consumption`  
  Load '75_LVBus1695489_consumption' has phase imbalance of 193.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695496_consumption`  
  Load '75_LVBus1695496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695721_consumption`  
  Load '75_LVBus1695721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695656_consumption`  
  Load '75_LVBus1695656_consumption' has phase imbalance of 257.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695609_consumption`  
  Load '75_LVBus1695609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695757_consumption`  
  Load '75_LVBus1695757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695607_consumption`  
  Load '75_LVBus1695607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695509_consumption`  
  Load '75_LVBus1695509_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695326_consumption`  
  Load '75_LVBus1695326_consumption' has phase imbalance of 264.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695780_consumption`  
  Load '75_LVBus1695780_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695759_consumption`  
  Load '75_LVBus1695759_consumption' has phase imbalance of 169.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695778_consumption`  
  Load '75_LVBus1695778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695299_consumption`  
  Load '75_LVBus1695299_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695350_consumption`  
  Load '75_LVBus1695350_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695450_consumption`  
  Load '75_LVBus1695450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695734_consumption`  
  Load '75_LVBus1695734_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695464_consumption`  
  Load '75_LVBus1695464_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695783_consumption`  
  Load '75_LVBus1695783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695533_consumption`  
  Load '75_LVBus1695533_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695448_consumption`  
  Load '75_LVBus1695448_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695362_consumption`  
  Load '75_LVBus1695362_consumption' has phase imbalance of 236.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695318_consumption`  
  Load '75_LVBus1695318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695415_consumption`  
  Load '75_LVBus1695415_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695314_consumption`  
  Load '75_LVBus1695314_consumption' has phase imbalance of 155.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695790_consumption`  
  Load '75_LVBus1695790_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695779_consumption`  
  Load '75_LVBus1695779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695296_consumption`  
  Load '75_LVBus1695296_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1918162_consumption`  
  Load '75_LVBus1918162_consumption' has phase imbalance of 205.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695454_consumption`  
  Load '75_LVBus1695454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695378_consumption`  
  Load '75_LVBus1695378_consumption' has phase imbalance of 155.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695622_consumption`  
  Load '75_LVBus1695622_consumption' has phase imbalance of 295.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695805_consumption`  
  Load '75_LVBus1695805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695774_consumption`  
  Load '75_LVBus1695774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695643_consumption`  
  Load '75_LVBus1695643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695661_consumption`  
  Load '75_LVBus1695661_consumption' has phase imbalance of 168.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695377_consumption`  
  Load '75_LVBus1695377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695420_consumption`  
  Load '75_LVBus1695420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695751_consumption`  
  Load '75_LVBus1695751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695368_consumption`  
  Load '75_LVBus1695368_consumption' has phase imbalance of 237.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695321_consumption`  
  Load '75_LVBus1695321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695520_consumption`  
  Load '75_LVBus1695520_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695767_consumption`  
  Load '75_LVBus1695767_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695631_consumption`  
  Load '75_LVBus1695631_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695472_consumption`  
  Load '75_LVBus1695472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695710_consumption`  
  Load '75_LVBus1695710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695565_consumption`  
  Load '75_LVBus1695565_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695506_consumption`  
  Load '75_LVBus1695506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695524_consumption`  
  Load '75_LVBus1695524_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695625_consumption`  
  Load '75_LVBus1695625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695629_consumption`  
  Load '75_LVBus1695629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695493_consumption`  
  Load '75_LVBus1695493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695771_consumption`  
  Load '75_LVBus1695771_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695351_consumption`  
  Load '75_LVBus1695351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695703_consumption`  
  Load '75_LVBus1695703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1918164_consumption`  
  Load '75_LVBus1918164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695500_consumption`  
  Load '75_LVBus1695500_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695706_consumption`  
  Load '75_LVBus1695706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695602_consumption`  
  Load '75_LVBus1695602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695317_consumption`  
  Load '75_LVBus1695317_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695804_consumption`  
  Load '75_LVBus1695804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1918135_consumption`  
  Load '75_LVBus1918135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695649_consumption`  
  Load '75_LVBus1695649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695291_consumption`  
  Load '75_LVBus1695291_consumption' has phase imbalance of 252.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695663_consumption`  
  Load '75_LVBus1695663_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695305_consumption`  
  Load '75_LVBus1695305_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695390_consumption`  
  Load '75_LVBus1695390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695280_consumption`  
  Load '75_LVBus1695280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695772_consumption`  
  Load '75_LVBus1695772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695795_consumption`  
  Load '75_LVBus1695795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695758_consumption`  
  Load '75_LVBus1695758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695249_consumption`  
  Load '75_LVBus1695249_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695273_consumption`  
  Load '75_LVBus1695273_consumption' has phase imbalance of 260.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695278_consumption`  
  Load '75_LVBus1695278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695676_consumption`  
  Load '75_LVBus1695676_consumption' has phase imbalance of 275.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695621_consumption`  
  Load '75_LVBus1695621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1956436_consumption`  
  Load '75_LVBus1956436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695419_consumption`  
  Load '75_LVBus1695419_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695463_consumption`  
  Load '75_LVBus1695463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695396_consumption`  
  Load '75_LVBus1695396_consumption' has phase imbalance of 20.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695599_consumption`  
  Load '75_LVBus1695599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695527_consumption`  
  Load '75_LVBus1695527_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695786_consumption`  
  Load '75_LVBus1695786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695634_consumption`  
  Load '75_LVBus1695634_consumption' has phase imbalance of 126.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695745_consumption`  
  Load '75_LVBus1695745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695264_consumption`  
  Load '75_LVBus1695264_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695451_consumption`  
  Load '75_LVBus1695451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695644_consumption`  
  Load '75_LVBus1695644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695723_consumption`  
  Load '75_LVBus1695723_consumption' has phase imbalance of 176.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695459_consumption`  
  Load '75_LVBus1695459_consumption' has phase imbalance of 203.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695681_consumption`  
  Load '75_LVBus1695681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695688_consumption`  
  Load '75_LVBus1695688_consumption' has phase imbalance of 170.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695281_consumption`  
  Load '75_LVBus1695281_consumption' has phase imbalance of 288.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695381_consumption`  
  Load '75_LVBus1695381_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695461_consumption`  
  Load '75_LVBus1695461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1991177_consumption`  
  Load '75_LVBus1991177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695422_consumption`  
  Load '75_LVBus1695422_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695794_consumption`  
  Load '75_LVBus1695794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695605_consumption`  
  Load '75_LVBus1695605_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1991179_consumption`  
  Load '75_LVBus1991179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695717_consumption`  
  Load '75_LVBus1695717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695646_consumption`  
  Load '75_LVBus1695646_consumption' has phase imbalance of 266.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695345_consumption`  
  Load '75_LVBus1695345_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1988145_consumption`  
  Load '75_LVBus1988145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695694_consumption`  
  Load '75_LVBus1695694_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1991181_consumption`  
  Load '75_LVBus1991181_consumption' has phase imbalance of 226.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695521_consumption`  
  Load '75_LVBus1695521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695690_consumption`  
  Load '75_LVBus1695690_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1928902_consumption`  
  Load '75_LVBus1928902_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695499_consumption`  
  Load '75_LVBus1695499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695653_consumption`  
  Load '75_LVBus1695653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695578_consumption`  
  Load '75_LVBus1695578_consumption' has phase imbalance of 85.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695477_consumption`  
  Load '75_LVBus1695477_consumption' has phase imbalance of 194.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695432_consumption`  
  Load '75_LVBus1695432_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695604_consumption`  
  Load '75_LVBus1695604_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695468_consumption`  
  Load '75_LVBus1695468_consumption' has phase imbalance of 41.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695593_consumption`  
  Load '75_LVBus1695593_consumption' has phase imbalance of 266.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1918161_consumption`  
  Load '75_LVBus1918161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695399_consumption`  
  Load '75_LVBus1695399_consumption' has phase imbalance of 287.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695546_consumption`  
  Load '75_LVBus1695546_consumption' has phase imbalance of 239.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695683_consumption`  
  Load '75_LVBus1695683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695689_consumption`  
  Load '75_LVBus1695689_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695357_consumption`  
  Load '75_LVBus1695357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695543_consumption`  
  Load '75_LVBus1695543_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695424_consumption`  
  Load '75_LVBus1695424_consumption' has phase imbalance of 212.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695279_consumption`  
  Load '75_LVBus1695279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695608_consumption`  
  Load '75_LVBus1695608_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695460_consumption`  
  Load '75_LVBus1695460_consumption' has phase imbalance of 173.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695714_consumption`  
  Load '75_LVBus1695714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695508_consumption`  
  Load '75_LVBus1695508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695668_consumption`  
  Load '75_LVBus1695668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695260_consumption`  
  Load '75_LVBus1695260_consumption' has phase imbalance of 175.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695677_consumption`  
  Load '75_LVBus1695677_consumption' has phase imbalance of 128.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1996861_consumption`  
  Load '75_LVBus1996861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695505_consumption`  
  Load '75_LVBus1695505_consumption' has phase imbalance of 57.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695436_consumption`  
  Load '75_LVBus1695436_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695465_consumption`  
  Load '75_LVBus1695465_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695782_consumption`  
  Load '75_LVBus1695782_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695679_consumption`  
  Load '75_LVBus1695679_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695659_consumption`  
  Load '75_LVBus1695659_consumption' has phase imbalance of 270.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695241_consumption`  
  Load '75_LVBus1695241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695572_consumption`  
  Load '75_LVBus1695572_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695807_consumption`  
  Load '75_LVBus1695807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695712_consumption`  
  Load '75_LVBus1695712_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695266_consumption`  
  Load '75_LVBus1695266_consumption' has phase imbalance of 121.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1918157_consumption`  
  Load '75_LVBus1918157_consumption' has phase imbalance of 293.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695736_consumption`  
  Load '75_LVBus1695736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695502_consumption`  
  Load '75_LVBus1695502_consumption' has phase imbalance of 274.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695418_consumption`  
  Load '75_LVBus1695418_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695430_consumption`  
  Load '75_LVBus1695430_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695748_consumption`  
  Load '75_LVBus1695748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695474_consumption`  
  Load '75_LVBus1695474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695813_consumption`  
  Load '75_LVBus1695813_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695417_consumption`  
  Load '75_LVBus1695417_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695616_consumption`  
  Load '75_LVBus1695616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695498_consumption`  
  Load '75_LVBus1695498_consumption' has phase imbalance of 169.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695603_consumption`  
  Load '75_LVBus1695603_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695564_consumption`  
  Load '75_LVBus1695564_consumption' has phase imbalance of 262.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695300_consumption`  
  Load '75_LVBus1695300_consumption' has phase imbalance of 176.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695798_consumption`  
  Load '75_LVBus1695798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695267_consumption`  
  Load '75_LVBus1695267_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695308_consumption`  
  Load '75_LVBus1695308_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695423_consumption`  
  Load '75_LVBus1695423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695814_consumption`  
  Load '75_LVBus1695814_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695559_consumption`  
  Load '75_LVBus1695559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695770_consumption`  
  Load '75_LVBus1695770_consumption' has phase imbalance of 26.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1991178_consumption`  
  Load '75_LVBus1991178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695781_consumption`  
  Load '75_LVBus1695781_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695660_consumption`  
  Load '75_LVBus1695660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695765_consumption`  
  Load '75_LVBus1695765_consumption' has phase imbalance of 226.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695342_consumption`  
  Load '75_LVBus1695342_consumption' has phase imbalance of 143.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695749_consumption`  
  Load '75_LVBus1695749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695693_consumption`  
  Load '75_LVBus1695693_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695662_consumption`  
  Load '75_LVBus1695662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695709_consumption`  
  Load '75_LVBus1695709_consumption' has phase imbalance of 132.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695364_consumption`  
  Load '75_LVBus1695364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695371_consumption`  
  Load '75_LVBus1695371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695439_consumption`  
  Load '75_LVBus1695439_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695685_consumption`  
  Load '75_LVBus1695685_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695597_consumption`  
  Load '75_LVBus1695597_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695458_consumption`  
  Load '75_LVBus1695458_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695470_consumption`  
  Load '75_LVBus1695470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695704_consumption`  
  Load '75_LVBus1695704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695554_consumption`  
  Load '75_LVBus1695554_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695652_consumption`  
  Load '75_LVBus1695652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695735_consumption`  
  Load '75_LVBus1695735_consumption' has phase imbalance of 40.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695773_consumption`  
  Load '75_LVBus1695773_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695271_consumption`  
  Load '75_LVBus1695271_consumption' has phase imbalance of 121.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695582_consumption`  
  Load '75_LVBus1695582_consumption' has phase imbalance of 232.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695626_consumption`  
  Load '75_LVBus1695626_consumption' has phase imbalance of 205.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695301_consumption`  
  Load '75_LVBus1695301_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695385_consumption`  
  Load '75_LVBus1695385_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695495_consumption`  
  Load '75_LVBus1695495_consumption' has phase imbalance of 227.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695678_consumption`  
  Load '75_LVBus1695678_consumption' has phase imbalance of 274.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695512_consumption`  
  Load '75_LVBus1695512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695462_consumption`  
  Load '75_LVBus1695462_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695389_consumption`  
  Load '75_LVBus1695389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695416_consumption`  
  Load '75_LVBus1695416_consumption' has phase imbalance of 197.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695408_consumption`  
  Load '75_LVBus1695408_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695376_consumption`  
  Load '75_LVBus1695376_consumption' has phase imbalance of 250.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695486_consumption`  
  Load '75_LVBus1695486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695352_consumption`  
  Load '75_LVBus1695352_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695569_consumption`  
  Load '75_LVBus1695569_consumption' has phase imbalance of 240.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695258_consumption`  
  Load '75_LVBus1695258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695664_consumption`  
  Load '75_LVBus1695664_consumption' has phase imbalance of 138.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695398_consumption`  
  Load '75_LVBus1695398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695374_consumption`  
  Load '75_LVBus1695374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695728_consumption`  
  Load '75_LVBus1695728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695262_consumption`  
  Load '75_LVBus1695262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695341_consumption`  
  Load '75_LVBus1695341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695268_consumption`  
  Load '75_LVBus1695268_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695624_consumption`  
  Load '75_LVBus1695624_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695288_consumption`  
  Load '75_LVBus1695288_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695324_consumption`  
  Load '75_LVBus1695324_consumption' has phase imbalance of 30.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695494_consumption`  
  Load '75_LVBus1695494_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695290_consumption`  
  Load '75_LVBus1695290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695366_consumption`  
  Load '75_LVBus1695366_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695497_consumption`  
  Load '75_LVBus1695497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695697_consumption`  
  Load '75_LVBus1695697_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695788_consumption`  
  Load '75_LVBus1695788_consumption' has phase imbalance of 255.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695525_consumption`  
  Load '75_LVBus1695525_consumption' has phase imbalance of 84.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695344_consumption`  
  Load '75_LVBus1695344_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695755_consumption`  
  Load '75_LVBus1695755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695530_consumption`  
  Load '75_LVBus1695530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695713_consumption`  
  Load '75_LVBus1695713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695282_consumption`  
  Load '75_LVBus1695282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695251_consumption`  
  Load '75_LVBus1695251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695812_consumption`  
  Load '75_LVBus1695812_consumption' has phase imbalance of 200.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695797_consumption`  
  Load '75_LVBus1695797_consumption' has phase imbalance of 274.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695387_consumption`  
  Load '75_LVBus1695387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695265_consumption`  
  Load '75_LVBus1695265_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695680_consumption`  
  Load '75_LVBus1695680_consumption' has phase imbalance of 244.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695695_consumption`  
  Load '75_LVBus1695695_consumption' has phase imbalance of 237.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695654_consumption`  
  Load '75_LVBus1695654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695289_consumption`  
  Load '75_LVBus1695289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1996865_consumption`  
  Load '75_LVBus1996865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695404_consumption`  
  Load '75_LVBus1695404_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695304_consumption`  
  Load '75_LVBus1695304_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695544_consumption`  
  Load '75_LVBus1695544_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695511_consumption`  
  Load '75_LVBus1695511_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695809_consumption`  
  Load '75_LVBus1695809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695715_consumption`  
  Load '75_LVBus1695715_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695673_consumption`  
  Load '75_LVBus1695673_consumption' has phase imbalance of 56.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695584_consumption`  
  Load '75_LVBus1695584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695353_consumption`  
  Load '75_LVBus1695353_consumption' has phase imbalance of 246.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695769_consumption`  
  Load '75_LVBus1695769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695620_consumption`  
  Load '75_LVBus1695620_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695452_consumption`  
  Load '75_LVBus1695452_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695764_consumption`  
  Load '75_LVBus1695764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695610_consumption`  
  Load '75_LVBus1695610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695756_consumption`  
  Load '75_LVBus1695756_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695307_consumption`  
  Load '75_LVBus1695307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695791_consumption`  
  Load '75_LVBus1695791_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695555_consumption`  
  Load '75_LVBus1695555_consumption' has phase imbalance of 234.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1695669_consumption`  
  Load '75_LVBus1695669_consumption' has phase imbalance of 279.3%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1058 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1695445' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1695445' (LV, 0.24 kV) has an electrical reach of 10.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  638 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  304 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1695241_consumption, 75_LVBus1695244_consumption, 75_LVBus1695248_consumption, 75_LVBus1695249_consumption, 75_LVBus1695251_consumption, 75_LVBus1695252_consumption, 75_LVBus1695253_consumption, 75_LVBus1695258_consumption, 75_LVBus1695260_consumption, 75_LVBus1695261_consumption, 75_LVBus1695262_consumption, 75_LVBus1695265_consumption, 75_LVBus1695268_consumption, 75_LVBus1695272_consumption, 75_LVBus1695273_consumption, 75_LVBus1695276_consumption, 75_LVBus1695278_consumption, 75_LVBus1695279_consumption, 75_LVBus1695280_consumption, 75_LVBus1695281_consumption, 75_LVBus1695282_consumption, 75_LVBus1695285_consumption, 75_LVBus1695288_consumption, 75_LVBus1695289_consumption, 75_LVBus1695290_consumption, 75_LVBus1695291_consumption, 75_LVBus1695292_consumption, 75_LVBus1695293_consumption, 75_LVBus1695294_consumption, 75_LVBus1695295_consumption, 75_LVBus1695296_consumption, 75_LVBus1695297_consumption, 75_LVBus1695298_consumption, 75_LVBus1695299_consumption, 75_LVBus1695300_consumption, 75_LVBus1695301_consumption, 75_LVBus1695304_consumption, 75_LVBus1695305_consumption, 75_LVBus1695306_consumption, 75_LVBus1695307_consumption, 75_LVBus1695308_consumption, 75_LVBus1695311_consumption, 75_LVBus1695312_consumption, 75_LVBus1695314_consumption, 75_LVBus1695316_consumption, 75_LVBus1695317_consumption, 75_LVBus1695318_consumption, 75_LVBus1695321_consumption, 75_LVBus1695322_consumption, 75_LVBus1695325_consumption, 75_LVBus1695333_consumption, 75_LVBus1695334_consumption, 75_LVBus1695341_consumption, 75_LVBus1695343_consumption, 75_LVBus1695344_consumption, 75_LVBus1695345_consumption, 75_LVBus1695349_consumption, 75_LVBus1695350_consumption, 75_LVBus1695351_consumption, 75_LVBus1695352_consumption, 75_LVBus1695353_consumption, 75_LVBus1695355_consumption, 75_LVBus1695356_consumption, 75_LVBus1695357_consumption, 75_LVBus1695360_consumption, 75_LVBus1695362_consumption, 75_LVBus1695363_consumption, 75_LVBus1695364_consumption, 75_LVBus1695366_consumption, 75_LVBus1695367_consumption, 75_LVBus1695368_consumption, 75_LVBus1695371_consumption, 75_LVBus1695374_consumption, 75_LVBus1695376_consumption, 75_LVBus1695377_consumption, 75_LVBus1695381_consumption, 75_LVBus1695382_consumption, 75_LVBus1695387_consumption, 75_LVBus1695389_consumption, 75_LVBus1695390_consumption, 75_LVBus1695391_consumption, 75_LVBus1695392_consumption, 75_LVBus1695393_consumption, 75_LVBus1695394_consumption, 75_LVBus1695397_consumption, 75_LVBus1695398_consumption, 75_LVBus1695399_consumption, 75_LVBus1695405_consumption, 75_LVBus1695408_consumption, 75_LVBus1695415_consumption, 75_LVBus1695416_consumption, 75_LVBus1695417_consumption, 75_LVBus1695418_consumption, 75_LVBus1695419_consumption, 75_LVBus1695420_consumption, 75_LVBus1695423_consumption, 75_LVBus1695424_consumption, 75_LVBus1695429_consumption, 75_LVBus1695432_consumption, 75_LVBus1695436_consumption, 75_LVBus1695439_consumption, 75_LVBus1695440_consumption, 75_LVBus1695443_consumption, 75_LVBus1695447_consumption, 75_LVBus1695448_consumption, 75_LVBus1695450_consumption, 75_LVBus1695451_consumption, 75_LVBus1695452_consumption, 75_LVBus1695453_consumption, 75_LVBus1695454_consumption, 75_LVBus1695456_consumption, 75_LVBus1695457_consumption, 75_LVBus1695458_consumption, 75_LVBus1695459_consumption, 75_LVBus1695460_consumption, 75_LVBus1695461_consumption, 75_LVBus1695462_consumption, 75_LVBus1695463_consumption, 75_LVBus1695464_consumption, 75_LVBus1695465_consumption, 75_LVBus1695466_consumption, 75_LVBus1695470_consumption, 75_LVBus1695472_consumption, 75_LVBus1695474_consumption, 75_LVBus1695477_consumption, 75_LVBus1695486_consumption, 75_LVBus1695487_consumption, 75_LVBus1695492_consumption, 75_LVBus1695493_consumption, 75_LVBus1695494_consumption, 75_LVBus1695495_consumption, 75_LVBus1695496_consumption, 75_LVBus1695497_consumption, 75_LVBus1695498_consumption, 75_LVBus1695499_consumption, 75_LVBus1695506_consumption, 75_LVBus1695507_consumption, 75_LVBus1695508_consumption, 75_LVBus1695509_consumption, 75_LVBus1695510_consumption, 75_LVBus1695511_consumption, 75_LVBus1695512_consumption, 75_LVBus1695520_consumption, 75_LVBus1695521_consumption, 75_LVBus1695523_consumption, 75_LVBus1695524_consumption, 75_LVBus1695526_consumption, 75_LVBus1695530_consumption, 75_LVBus1695533_consumption, 75_LVBus1695542_consumption, 75_LVBus1695543_consumption, 75_LVBus1695544_consumption, 75_LVBus1695546_consumption, 75_LVBus1695553_consumption, 75_LVBus1695554_consumption, 75_LVBus1695555_consumption, 75_LVBus1695556_consumption, 75_LVBus1695559_consumption, 75_LVBus1695564_consumption, 75_LVBus1695565_consumption, 75_LVBus1695568_consumption, 75_LVBus1695569_consumption, 75_LVBus1695572_consumption, 75_LVBus1695579_consumption, 75_LVBus1695581_consumption, 75_LVBus1695582_consumption, 75_LVBus1695584_consumption, 75_LVBus1695593_consumption, 75_LVBus1695595_consumption, 75_LVBus1695598_consumption, 75_LVBus1695599_consumption, 75_LVBus1695602_consumption, 75_LVBus1695603_consumption, 75_LVBus1695604_consumption, 75_LVBus1695605_consumption, 75_LVBus1695607_consumption, 75_LVBus1695609_consumption, 75_LVBus1695610_consumption, 75_LVBus1695616_consumption, 75_LVBus1695621_consumption, 75_LVBus1695623_consumption, 75_LVBus1695624_consumption, 75_LVBus1695625_consumption, 75_LVBus1695626_consumption, 75_LVBus1695629_consumption, 75_LVBus1695630_consumption, 75_LVBus1695631_consumption, 75_LVBus1695632_consumption, 75_LVBus1695636_consumption, 75_LVBus1695643_consumption, 75_LVBus1695644_consumption, 75_LVBus1695645_consumption, 75_LVBus1695646_consumption, 75_LVBus1695649_consumption, 75_LVBus1695652_consumption, 75_LVBus1695653_consumption, 75_LVBus1695654_consumption, 75_LVBus1695656_consumption, 75_LVBus1695659_consumption, 75_LVBus1695660_consumption, 75_LVBus1695661_consumption, 75_LVBus1695662_consumption, 75_LVBus1695663_consumption, 75_LVBus1695668_consumption, 75_LVBus1695669_consumption, 75_LVBus1695670_consumption, 75_LVBus1695671_consumption, 75_LVBus1695672_consumption, 75_LVBus1695675_consumption, 75_LVBus1695678_consumption, 75_LVBus1695680_consumption, 75_LVBus1695681_consumption, 75_LVBus1695683_consumption, 75_LVBus1695684_consumption, 75_LVBus1695685_consumption, 75_LVBus1695688_consumption, 75_LVBus1695689_consumption, 75_LVBus1695690_consumption, 75_LVBus1695693_consumption, 75_LVBus1695694_consumption, 75_LVBus1695695_consumption, 75_LVBus1695696_consumption, 75_LVBus1695697_consumption, 75_LVBus1695699_consumption, 75_LVBus1695703_consumption, 75_LVBus1695704_consumption, 75_LVBus1695706_consumption, 75_LVBus1695710_consumption, 75_LVBus1695712_consumption, 75_LVBus1695713_consumption, 75_LVBus1695714_consumption, 75_LVBus1695715_consumption, 75_LVBus1695717_consumption, 75_LVBus1695718_consumption, 75_LVBus1695719_consumption, 75_LVBus1695721_consumption, 75_LVBus1695723_consumption, 75_LVBus1695725_consumption, 75_LVBus1695727_consumption, 75_LVBus1695728_consumption, 75_LVBus1695731_consumption, 75_LVBus1695734_consumption, 75_LVBus1695736_consumption, 75_LVBus1695738_consumption, 75_LVBus1695745_consumption, 75_LVBus1695748_consumption, 75_LVBus1695749_consumption, 75_LVBus1695751_consumption, 75_LVBus1695753_consumption, 75_LVBus1695755_consumption, 75_LVBus1695757_consumption, 75_LVBus1695758_consumption, 75_LVBus1695764_consumption, 75_LVBus1695765_consumption, 75_LVBus1695766_consumption, 75_LVBus1695768_consumption, 75_LVBus1695769_consumption, 75_LVBus1695771_consumption, 75_LVBus1695772_consumption, 75_LVBus1695773_consumption, 75_LVBus1695774_consumption, 75_LVBus1695777_consumption, 75_LVBus1695778_consumption, 75_LVBus1695779_consumption, 75_LVBus1695780_consumption, 75_LVBus1695781_consumption, 75_LVBus1695782_consumption, 75_LVBus1695783_consumption, 75_LVBus1695786_consumption, 75_LVBus1695788_consumption, 75_LVBus1695790_consumption, 75_LVBus1695791_consumption, 75_LVBus1695794_consumption, 75_LVBus1695795_consumption, 75_LVBus1695797_consumption, 75_LVBus1695798_consumption, 75_LVBus1695804_consumption, 75_LVBus1695805_consumption, 75_LVBus1695807_consumption, 75_LVBus1695809_consumption, 75_LVBus1695811_consumption, 75_LVBus1695812_consumption, 75_LVBus1695814_consumption, 75_LVBus1918135_consumption, 75_LVBus1918157_consumption, 75_LVBus1918161_consumption, 75_LVBus1918162_consumption, 75_LVBus1918164_consumption, 75_LVBus1928902_consumption, 75_LVBus1939481_consumption, 75_LVBus1956434_consumption, 75_LVBus1956435_consumption, 75_LVBus1956436_consumption, 75_LVBus1956437_consumption, 75_LVBus1988145_consumption, 75_LVBus1991177_consumption, 75_LVBus1991178_consumption, 75_LVBus1991179_consumption, 75_LVBus1991180_consumption, 75_LVBus1993966_consumption, 75_LVBus1996860_consumption, 75_LVBus1996861_consumption, 75_LVBus1996863_consumption, 75_LVBus1996865_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  529 group(s) of loads (1058 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  7 group(s) of series lines (14 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  670 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1695233_consumption, 75_LVBus1695233_production, 75_LVBus1695234_consumption, 75_LVBus1695234_production, 75_LVBus1695235_consumption, 75_LVBus1695235_production, 75_LVBus1695236_consumption, 75_LVBus1695236_production, 75_LVBus1695237_production, 75_LVBus1695238_production, 75_LVBus1695239_consumption, 75_LVBus1695239_production, 75_LVBus1695240_consumption, 75_LVBus1695240_production, 75_LVBus1695241_production, 75_LVBus1695243_consumption, 75_LVBus1695243_production, 75_LVBus1695244_production, 75_LVBus1695246_production, 75_LVBus1695248_production, 75_LVBus1695249_production, 75_LVBus1695250_consumption, 75_LVBus1695250_production, 75_LVBus1695251_production, 75_LVBus1695252_production, 75_LVBus1695253_production, 75_LVBus1695255_consumption, 75_LVBus1695255_production, 75_LVBus1695257_consumption, 75_LVBus1695257_production, 75_LVBus1695258_production, 75_LVBus1695259_production, 75_LVBus1695260_production, 75_LVBus1695261_production, 75_LVBus1695262_production, 75_LVBus1695264_production, 75_LVBus1695265_production, 75_LVBus1695266_production, 75_LVBus1695267_production, 75_LVBus1695268_production, 75_LVBus1695269_consumption, 75_LVBus1695269_production, 75_LVBus1695270_production, 75_LVBus1695271_production, 75_LVBus1695272_production, 75_LVBus1695273_production, 75_LVBus1695275_consumption, 75_LVBus1695275_production, 75_LVBus1695276_production, 75_LVBus1695278_production, 75_LVBus1695279_production, 75_LVBus1695280_production, 75_LVBus1695281_production, 75_LVBus1695282_production, 75_LVBus1695283_production, 75_LVBus1695284_consumption, 75_LVBus1695284_production, 75_LVBus1695285_production, 75_LVBus1695286_consumption, 75_LVBus1695286_production, 75_LVBus1695288_production, 75_LVBus1695289_production, 75_LVBus1695290_production, 75_LVBus1695291_production, 75_LVBus1695292_production, 75_LVBus1695293_production, 75_LVBus1695294_production, 75_LVBus1695295_production, 75_LVBus1695296_production, 75_LVBus1695297_production, 75_LVBus1695298_production, 75_LVBus1695299_production, 75_LVBus1695300_production, 75_LVBus1695301_production, 75_LVBus1695303_consumption, 75_LVBus1695303_production, 75_LVBus1695304_production, 75_LVBus1695305_production, 75_LVBus1695306_production, 75_LVBus1695307_production, 75_LVBus1695308_production, 75_LVBus1695309_consumption, 75_LVBus1695309_production, 75_LVBus1695311_production, 75_LVBus1695312_production, 75_LVBus1695313_consumption, 75_LVBus1695313_production, 75_LVBus1695314_production, 75_LVBus1695315_consumption, 75_LVBus1695315_production, 75_LVBus1695316_production, 75_LVBus1695317_production, 75_LVBus1695318_production, 75_LVBus1695320_consumption, 75_LVBus1695320_production, 75_LVBus1695321_production, 75_LVBus1695322_production, 75_LVBus1695323_consumption, 75_LVBus1695323_production, 75_LVBus1695324_production, 75_LVBus1695325_production, 75_LVBus1695326_production, 75_LVBus1695327_consumption, 75_LVBus1695327_production, 75_LVBus1695328_consumption, 75_LVBus1695328_production, 75_LVBus1695329_production, 75_LVBus1695331_consumption, 75_LVBus1695331_production, 75_LVBus1695333_production, 75_LVBus1695334_production, 75_LVBus1695335_consumption, 75_LVBus1695335_production, 75_LVBus1695339_consumption, 75_LVBus1695339_production, 75_LVBus1695340_production, 75_LVBus1695341_production, 75_LVBus1695342_production, 75_LVBus1695343_production, 75_LVBus1695344_production, 75_LVBus1695345_production, 75_LVBus1695349_production, 75_LVBus1695350_production, 75_LVBus1695351_production, 75_LVBus1695352_production, 75_LVBus1695353_production, 75_LVBus1695354_consumption, 75_LVBus1695354_production, 75_LVBus1695355_production, 75_LVBus1695356_production, 75_LVBus1695357_production, 75_LVBus1695358_consumption, 75_LVBus1695358_production, 75_LVBus1695360_production, 75_LVBus1695361_consumption, 75_LVBus1695361_production, 75_LVBus1695362_production, 75_LVBus1695363_production, 75_LVBus1695364_production, 75_LVBus1695365_consumption, 75_LVBus1695365_production, 75_LVBus1695366_production, 75_LVBus1695367_production, 75_LVBus1695368_production, 75_LVBus1695369_consumption, 75_LVBus1695369_production, 75_LVBus1695371_production, 75_LVBus1695372_consumption, 75_LVBus1695372_production, 75_LVBus1695373_consumption, 75_LVBus1695373_production, 75_LVBus1695374_production, 75_LVBus1695375_consumption, 75_LVBus1695375_production, 75_LVBus1695376_production, 75_LVBus1695377_production, 75_LVBus1695378_production, 75_LVBus1695379_consumption, 75_LVBus1695379_production, 75_LVBus1695380_consumption, 75_LVBus1695380_production, 75_LVBus1695381_production, 75_LVBus1695382_production, 75_LVBus1695383_consumption, 75_LVBus1695383_production, 75_LVBus1695385_production, 75_LVBus1695386_production, 75_LVBus1695387_production, 75_LVBus1695388_consumption, 75_LVBus1695388_production, 75_LVBus1695389_production, 75_LVBus1695390_production, 75_LVBus1695391_production, 75_LVBus1695392_production, 75_LVBus1695393_production, 75_LVBus1695394_production, 75_LVBus1695396_production, 75_LVBus1695397_production, 75_LVBus1695398_production, 75_LVBus1695399_production, 75_LVBus1695400_consumption, 75_LVBus1695400_production, 75_LVBus1695402_consumption, 75_LVBus1695402_production, 75_LVBus1695403_consumption, 75_LVBus1695403_production, 75_LVBus1695404_production, 75_LVBus1695405_production, 75_LVBus1695406_production, 75_LVBus1695407_consumption, 75_LVBus1695407_production, 75_LVBus1695408_production, 75_LVBus1695409_production, 75_LVBus1695410_consumption, 75_LVBus1695410_production, 75_LVBus1695414_consumption, 75_LVBus1695414_production, 75_LVBus1695415_production, 75_LVBus1695416_production, 75_LVBus1695417_production, 75_LVBus1695418_production, 75_LVBus1695419_production, 75_LVBus1695420_production, 75_LVBus1695421_consumption, 75_LVBus1695421_production, 75_LVBus1695422_production, 75_LVBus1695423_production, 75_LVBus1695424_production, 75_LVBus1695425_production, 75_LVBus1695429_production, 75_LVBus1695430_production, 75_LVBus1695431_production, 75_LVBus1695432_production, 75_LVBus1695433_consumption, 75_LVBus1695433_production, 75_LVBus1695435_consumption, 75_LVBus1695435_production, 75_LVBus1695436_production, 75_LVBus1695438_consumption, 75_LVBus1695438_production, 75_LVBus1695439_production, 75_LVBus1695440_production, 75_LVBus1695441_consumption, 75_LVBus1695441_production, 75_LVBus1695442_consumption, 75_LVBus1695442_production, 75_LVBus1695443_production, 75_LVBus1695445_production, 75_LVBus1695447_production, 75_LVBus1695448_production, 75_LVBus1695450_production, 75_LVBus1695451_production, 75_LVBus1695452_production, 75_LVBus1695453_production, 75_LVBus1695454_production, 75_LVBus1695455_consumption, 75_LVBus1695455_production, 75_LVBus1695456_production, 75_LVBus1695457_production, 75_LVBus1695458_production, 75_LVBus1695459_production, 75_LVBus1695460_production, 75_LVBus1695461_production, 75_LVBus1695462_production, 75_LVBus1695463_production, 75_LVBus1695464_production, 75_LVBus1695465_production, 75_LVBus1695466_production, 75_LVBus1695467_consumption, 75_LVBus1695467_production, 75_LVBus1695468_production, 75_LVBus1695469_consumption, 75_LVBus1695469_production, 75_LVBus1695470_production, 75_LVBus1695472_production, 75_LVBus1695474_production, 75_LVBus1695475_consumption, 75_LVBus1695475_production, 75_LVBus1695476_consumption, 75_LVBus1695476_production, 75_LVBus1695477_production, 75_LVBus1695478_production, 75_LVBus1695482_consumption, 75_LVBus1695482_production, 75_LVBus1695483_consumption, 75_LVBus1695483_production, 75_LVBus1695485_consumption, 75_LVBus1695485_production, 75_LVBus1695486_production, 75_LVBus1695487_production, 75_LVBus1695488_consumption, 75_LVBus1695488_production, 75_LVBus1695489_production, 75_LVBus1695491_production, 75_LVBus1695492_production, 75_LVBus1695493_production, 75_LVBus1695494_production, 75_LVBus1695495_production, 75_LVBus1695496_production, 75_LVBus1695497_production, 75_LVBus1695498_production, 75_LVBus1695499_production, 75_LVBus1695500_production, 75_LVBus1695501_consumption, 75_LVBus1695501_production, 75_LVBus1695502_production, 75_LVBus1695504_production, 75_LVBus1695505_production, 75_LVBus1695506_production, 75_LVBus1695507_production, 75_LVBus1695508_production, 75_LVBus1695509_production, 75_LVBus1695510_production, 75_LVBus1695511_production, 75_LVBus1695512_production, 75_LVBus1695513_consumption, 75_LVBus1695513_production, 75_LVBus1695514_consumption, 75_LVBus1695514_production, 75_LVBus1695515_consumption, 75_LVBus1695515_production, 75_LVBus1695516_consumption, 75_LVBus1695516_production, 75_LVBus1695517_production, 75_LVBus1695519_production, 75_LVBus1695520_production, 75_LVBus1695521_production, 75_LVBus1695522_consumption, 75_LVBus1695522_production, 75_LVBus1695523_production, 75_LVBus1695524_production, 75_LVBus1695525_production, 75_LVBus1695526_production, 75_LVBus1695527_production, 75_LVBus1695529_production, 75_LVBus1695530_production, 75_LVBus1695533_production, 75_LVBus1695535_production, 75_LVBus1695536_production, 75_LVBus1695537_production, 75_LVBus1695538_production, 75_LVBus1695540_production, 75_LVBus1695541_consumption, 75_LVBus1695541_production, 75_LVBus1695542_production, 75_LVBus1695543_production, 75_LVBus1695544_production, 75_LVBus1695545_consumption, 75_LVBus1695545_production, 75_LVBus1695546_production, 75_LVBus1695547_consumption, 75_LVBus1695547_production, 75_LVBus1695549_consumption, 75_LVBus1695549_production, 75_LVBus1695551_consumption, 75_LVBus1695551_production, 75_LVBus1695553_production, 75_LVBus1695554_production, 75_LVBus1695555_production, 75_LVBus1695556_production, 75_LVBus1695558_production, 75_LVBus1695559_production, 75_LVBus1695560_consumption, 75_LVBus1695560_production, 75_LVBus1695561_consumption, 75_LVBus1695561_production, 75_LVBus1695562_production, 75_LVBus1695564_production, 75_LVBus1695565_production, 75_LVBus1695566_production, 75_LVBus1695567_production, 75_LVBus1695568_production, 75_LVBus1695569_production, 75_LVBus1695571_production, 75_LVBus1695572_production, 75_LVBus1695574_consumption, 75_LVBus1695574_production, 75_LVBus1695575_production, 75_LVBus1695576_production, 75_LVBus1695577_consumption, 75_LVBus1695577_production, 75_LVBus1695578_production, 75_LVBus1695579_production, 75_LVBus1695581_production, 75_LVBus1695582_production, 75_LVBus1695583_consumption, 75_LVBus1695583_production, 75_LVBus1695584_production, 75_LVBus1695585_consumption, 75_LVBus1695585_production, 75_LVBus1695586_consumption, 75_LVBus1695586_production, 75_LVBus1695587_consumption, 75_LVBus1695587_production, 75_LVBus1695588_production, 75_LVBus1695590_consumption, 75_LVBus1695590_production, 75_LVBus1695591_consumption, 75_LVBus1695591_production, 75_LVBus1695592_consumption, 75_LVBus1695592_production, 75_LVBus1695593_production, 75_LVBus1695594_consumption, 75_LVBus1695594_production, 75_LVBus1695595_production, 75_LVBus1695597_production, 75_LVBus1695598_production, 75_LVBus1695599_production, 75_LVBus1695601_consumption, 75_LVBus1695601_production, 75_LVBus1695602_production, 75_LVBus1695603_production, 75_LVBus1695604_production, 75_LVBus1695605_production, 75_LVBus1695606_consumption, 75_LVBus1695606_production, 75_LVBus1695607_production, 75_LVBus1695608_production, 75_LVBus1695609_production, 75_LVBus1695610_production, 75_LVBus1695612_consumption, 75_LVBus1695612_production, 75_LVBus1695613_consumption, 75_LVBus1695613_production, 75_LVBus1695614_consumption, 75_LVBus1695614_production, 75_LVBus1695615_consumption, 75_LVBus1695615_production, 75_LVBus1695616_production, 75_LVBus1695620_production, 75_LVBus1695621_production, 75_LVBus1695622_production, 75_LVBus1695623_production, 75_LVBus1695624_production, 75_LVBus1695625_production, 75_LVBus1695626_production, 75_LVBus1695628_consumption, 75_LVBus1695628_production, 75_LVBus1695629_production, 75_LVBus1695630_production, 75_LVBus1695631_production, 75_LVBus1695632_production, 75_LVBus1695633_production, 75_LVBus1695634_production, 75_LVBus1695635_consumption, 75_LVBus1695635_production, 75_LVBus1695636_production, 75_LVBus1695637_consumption, 75_LVBus1695637_production, 75_LVBus1695638_consumption, 75_LVBus1695638_production, 75_LVBus1695639_production, 75_LVBus1695643_production, 75_LVBus1695644_production, 75_LVBus1695645_production, 75_LVBus1695646_production, 75_LVBus1695647_consumption, 75_LVBus1695647_production, 75_LVBus1695648_consumption, 75_LVBus1695648_production, 75_LVBus1695649_production, 75_LVBus1695650_production, 75_LVBus1695651_consumption, 75_LVBus1695651_production, 75_LVBus1695652_production, 75_LVBus1695653_production, 75_LVBus1695654_production, 75_LVBus1695656_production, 75_LVBus1695657_consumption, 75_LVBus1695657_production, 75_LVBus1695659_production, 75_LVBus1695660_production, 75_LVBus1695661_production, 75_LVBus1695662_production, 75_LVBus1695663_production, 75_LVBus1695664_production, 75_LVBus1695666_consumption, 75_LVBus1695666_production, 75_LVBus1695668_production, 75_LVBus1695669_production, 75_LVBus1695670_production, 75_LVBus1695671_production, 75_LVBus1695672_production, 75_LVBus1695673_production, 75_LVBus1695674_consumption, 75_LVBus1695674_production, 75_LVBus1695675_production, 75_LVBus1695676_production, 75_LVBus1695677_production, 75_LVBus1695678_production, 75_LVBus1695679_production, 75_LVBus1695680_production, 75_LVBus1695681_production, 75_LVBus1695682_consumption, 75_LVBus1695682_production, 75_LVBus1695683_production, 75_LVBus1695684_production, 75_LVBus1695685_production, 75_LVBus1695687_consumption, 75_LVBus1695687_production, 75_LVBus1695688_production, 75_LVBus1695689_production, 75_LVBus1695690_production, 75_LVBus1695692_consumption, 75_LVBus1695692_production, 75_LVBus1695693_production, 75_LVBus1695694_production, 75_LVBus1695695_production, 75_LVBus1695696_production, 75_LVBus1695697_production, 75_LVBus1695698_consumption, 75_LVBus1695698_production, 75_LVBus1695699_production, 75_LVBus1695701_consumption, 75_LVBus1695701_production, 75_LVBus1695703_production, 75_LVBus1695704_production, 75_LVBus1695705_consumption, 75_LVBus1695705_production, 75_LVBus1695706_production, 75_LVBus1695707_production, 75_LVBus1695709_production, 75_LVBus1695710_production, 75_LVBus1695711_consumption, 75_LVBus1695711_production, 75_LVBus1695712_production, 75_LVBus1695713_production, 75_LVBus1695714_production, 75_LVBus1695715_production, 75_LVBus1695716_production, 75_LVBus1695717_production, 75_LVBus1695718_production, 75_LVBus1695719_production, 75_LVBus1695721_production, 75_LVBus1695722_consumption, 75_LVBus1695722_production, 75_LVBus1695723_production, 75_LVBus1695724_production, 75_LVBus1695725_production, 75_LVBus1695726_consumption, 75_LVBus1695726_production, 75_LVBus1695727_production, 75_LVBus1695728_production, 75_LVBus1695729_consumption, 75_LVBus1695729_production, 75_LVBus1695730_consumption, 75_LVBus1695730_production, 75_LVBus1695731_production, 75_LVBus1695732_consumption, 75_LVBus1695732_production, 75_LVBus1695733_consumption, 75_LVBus1695733_production, 75_LVBus1695734_production, 75_LVBus1695735_production, 75_LVBus1695736_production, 75_LVBus1695737_consumption, 75_LVBus1695737_production, 75_LVBus1695738_production, 75_LVBus1695740_consumption, 75_LVBus1695740_production, 75_LVBus1695741_consumption, 75_LVBus1695741_production, 75_LVBus1695745_production, 75_LVBus1695746_production, 75_LVBus1695747_consumption, 75_LVBus1695747_production, 75_LVBus1695748_production, 75_LVBus1695749_production, 75_LVBus1695750_consumption, 75_LVBus1695750_production, 75_LVBus1695751_production, 75_LVBus1695752_consumption, 75_LVBus1695752_production, 75_LVBus1695753_production, 75_LVBus1695754_consumption, 75_LVBus1695754_production, 75_LVBus1695755_production, 75_LVBus1695756_production, 75_LVBus1695757_production, 75_LVBus1695758_production, 75_LVBus1695759_production, 75_LVBus1695763_consumption, 75_LVBus1695763_production, 75_LVBus1695764_production, 75_LVBus1695765_production, 75_LVBus1695766_production, 75_LVBus1695767_production, 75_LVBus1695768_production, 75_LVBus1695769_production, 75_LVBus1695770_production, 75_LVBus1695771_production, 75_LVBus1695772_production, 75_LVBus1695773_production, 75_LVBus1695774_production, 75_LVBus1695776_consumption, 75_LVBus1695776_production, 75_LVBus1695777_production, 75_LVBus1695778_production, 75_LVBus1695779_production, 75_LVBus1695780_production, 75_LVBus1695781_production, 75_LVBus1695782_production, 75_LVBus1695783_production, 75_LVBus1695784_consumption, 75_LVBus1695784_production, 75_LVBus1695785_consumption, 75_LVBus1695785_production, 75_LVBus1695786_production, 75_LVBus1695787_consumption, 75_LVBus1695787_production, 75_LVBus1695788_production, 75_LVBus1695789_production, 75_LVBus1695790_production, 75_LVBus1695791_production, 75_LVBus1695792_consumption, 75_LVBus1695792_production, 75_LVBus1695793_production, 75_LVBus1695794_production, 75_LVBus1695795_production, 75_LVBus1695796_consumption, 75_LVBus1695796_production, 75_LVBus1695797_production, 75_LVBus1695798_production, 75_LVBus1695800_consumption, 75_LVBus1695800_production, 75_LVBus1695802_production, 75_LVBus1695804_production, 75_LVBus1695805_production, 75_LVBus1695806_consumption, 75_LVBus1695806_production, 75_LVBus1695807_production, 75_LVBus1695808_consumption, 75_LVBus1695808_production, 75_LVBus1695809_production, 75_LVBus1695810_consumption, 75_LVBus1695810_production, 75_LVBus1695811_production, 75_LVBus1695812_production, 75_LVBus1695813_production, 75_LVBus1695814_production, 75_LVBus1918135_production, 75_LVBus1918157_production, 75_LVBus1918158_consumption, 75_LVBus1918158_production, 75_LVBus1918159_consumption, 75_LVBus1918159_production, 75_LVBus1918160_consumption, 75_LVBus1918160_production, 75_LVBus1918161_production, 75_LVBus1918162_production, 75_LVBus1918163_production, 75_LVBus1918164_production, 75_LVBus1918165_consumption, 75_LVBus1918165_production, 75_LVBus1928902_production, 75_LVBus1939481_production, 75_LVBus1951336_consumption, 75_LVBus1951336_production, 75_LVBus1956434_production, 75_LVBus1956435_production, 75_LVBus1956436_production, 75_LVBus1956437_production, 75_LVBus1975648_consumption, 75_LVBus1975648_production, 75_LVBus1977530_consumption, 75_LVBus1977530_production, 75_LVBus1988145_production, 75_LVBus1991174_consumption, 75_LVBus1991174_production, 75_LVBus1991175_consumption, 75_LVBus1991175_production, 75_LVBus1991176_consumption, 75_LVBus1991176_production, 75_LVBus1991177_production, 75_LVBus1991178_production, 75_LVBus1991179_production, 75_LVBus1991180_production, 75_LVBus1991181_production, 75_LVBus1993966_production, 75_LVBus1996859_consumption, 75_LVBus1996859_production, 75_LVBus1996860_production, 75_LVBus1996861_production, 75_LVBus1996862_consumption, 75_LVBus1996862_production, 75_LVBus1996863_production, 75_LVBus1996864_production, 75_LVBus1996865_production, 75_MVLV047457_consumption, 75_MVLV047457_production.

