# BMOPF Network Summary: 75_MVFeeder0100

**Generated:** 2026-10-01 23:34:21  
**Findings:** 0 errors · 5 warnings · 276 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 57 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 540 |  |
| line | 482 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 724 | 2.247 MW, 674.2 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 57 |  |
| switch | 0 |  |
| transformer | 57 | Dyn11×57 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 131 | 130 | 20 | 0 |
| LV_236V | 236.0 V | 409 | 352 | 704 | 0 |

**Transformer transitions:**

- `75_MVLV032835_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068396_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV128971_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121415_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064469_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV131389_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV150789_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV003540_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV101643_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068170_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036174_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV105233_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066981_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV051615_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV057996_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV021842_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV118870_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV086579_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV171891_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV005718_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV160861_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV150000_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV106408_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV155271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV039200_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036301_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV128716_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV114992_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV150790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV105217_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV114990_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV017701_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV039225_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121076_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149997_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV040308_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV123935_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV039205_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV017700_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV019048_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121073_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV114993_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV004329_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV060362_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149770_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV138021_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV105327_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066980_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV058000_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV135391_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149996_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV158240_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 8 |
| Degree-1 buses | 185 |
| Tree depth (max hops) | 39 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 540 | 1 | 539 | 0 | 0 | 0 |
| Tier LV_236V | 409 | 57 | 352 | 0 | 0 | 0 |
| Tier MV_11.8kV | 131 | 1 | 130 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 57; skipped invalid branches: 0.

Galvanic zones: 58; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_ARNOU | MV_11.8kV | 131 | 0 | 0 | 57 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2029 declared bus terminals; 1798 mapped line/closed-switch conductor edges; 231 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 18200.0 | 2.331 | 2172 |
| q_nom | 0.0 | 5450.0 | 2.331 | 2172 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.759 | 1280.0 | 1.352 | 482 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.652 | 57 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 448 of 724 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622750_consumption' has phase imbalance of 162.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623151_consumption' has phase imbalance of 276.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622842_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622775_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622987_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623111_consumption' has phase imbalance of 210.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623114_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623088_consumption' has phase imbalance of 66.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622743_consumption' has phase imbalance of 50.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623137_consumption' has phase imbalance of 285.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623122_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622786_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622941_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622908_consumption' has phase imbalance of 51.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622972_consumption' has phase imbalance of 204.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622954_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622830_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623139_consumption' has phase imbalance of 174.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622778_consumption' has phase imbalance of 89.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623064_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623080_consumption' has phase imbalance of 78.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623096_consumption' has phase imbalance of 244.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622831_consumption' has phase imbalance of 59.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623126_consumption' has phase imbalance of 103.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623115_consumption' has phase imbalance of 106.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622802_consumption' has phase imbalance of 130.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007255_consumption' has phase imbalance of 189.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623051_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623156_consumption' has phase imbalance of 136.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622879_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623147_consumption' has phase imbalance of 251.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622889_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623146_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1957909_consumption' has phase imbalance of 93.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007260_consumption' has phase imbalance of 199.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623101_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007274_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623158_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622739_consumption' has phase imbalance of 210.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622934_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622877_consumption' has phase imbalance of 102.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622957_consumption' has phase imbalance of 231.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622899_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623134_consumption' has phase imbalance of 110.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623077_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622814_consumption' has phase imbalance of 114.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622871_consumption' has phase imbalance of 139.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623061_consumption' has phase imbalance of 263.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622966_consumption' has phase imbalance of 194.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622839_consumption' has phase imbalance of 60.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622959_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623113_consumption' has phase imbalance of 278.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622990_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623041_consumption' has phase imbalance of 135.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622888_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622986_consumption' has phase imbalance of 34.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622912_consumption' has phase imbalance of 117.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623004_consumption' has phase imbalance of 104.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623042_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622977_consumption' has phase imbalance of 143.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622835_consumption' has phase imbalance of 229.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623105_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622763_consumption' has phase imbalance of 214.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623112_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622764_consumption' has phase imbalance of 149.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622853_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007253_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622982_consumption' has phase imbalance of 129.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622783_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622740_consumption' has phase imbalance of 30.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622980_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622865_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007257_consumption' has phase imbalance of 215.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622824_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622767_consumption' has phase imbalance of 223.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622792_consumption' has phase imbalance of 196.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623070_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622955_consumption' has phase imbalance of 139.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622841_consumption' has phase imbalance of 285.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622854_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623018_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622751_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007267_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622992_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623053_consumption' has phase imbalance of 168.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623002_consumption' has phase imbalance of 258.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622821_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622848_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623032_consumption' has phase imbalance of 198.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622994_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622996_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623085_consumption' has phase imbalance of 285.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623144_consumption' has phase imbalance of 59.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623012_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622849_consumption' has phase imbalance of 217.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007273_consumption' has phase imbalance of 249.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623107_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623091_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622826_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622836_consumption' has phase imbalance of 232.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622956_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623155_consumption' has phase imbalance of 133.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1942502_consumption' has phase imbalance of 109.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622858_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622785_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622893_consumption' has phase imbalance of 208.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007272_consumption' has phase imbalance of 258.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622984_consumption' has phase imbalance of 294.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622961_consumption' has phase imbalance of 35.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007262_consumption' has phase imbalance of 70.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623078_consumption' has phase imbalance of 109.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622949_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623027_consumption' has phase imbalance of 241.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623157_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623013_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622872_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007269_consumption' has phase imbalance of 283.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622973_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623106_consumption' has phase imbalance of 277.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622762_consumption' has phase imbalance of 114.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623103_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622967_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1979932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622862_consumption' has phase imbalance of 261.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623056_consumption' has phase imbalance of 197.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623066_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623145_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622997_consumption' has phase imbalance of 239.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623135_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623036_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623094_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623047_consumption' has phase imbalance of 276.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622771_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622960_consumption' has phase imbalance of 156.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622852_consumption' has phase imbalance of 97.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007252_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623015_consumption' has phase imbalance of 238.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623062_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623087_consumption' has phase imbalance of 291.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623133_consumption' has phase imbalance of 226.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623048_consumption' has phase imbalance of 219.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623108_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623037_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623069_consumption' has phase imbalance of 230.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622947_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623100_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622978_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622971_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622890_consumption' has phase imbalance of 127.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623052_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623124_consumption' has phase imbalance of 155.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623020_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623129_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622950_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622903_consumption' has phase imbalance of 236.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623123_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623054_consumption' has phase imbalance of 26.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622991_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622857_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007261_consumption' has phase imbalance of 180.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623119_consumption' has phase imbalance of 104.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623058_consumption' has phase imbalance of 23.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623045_consumption' has phase imbalance of 208.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623029_consumption' has phase imbalance of 141.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622901_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007271_consumption' has phase imbalance of 68.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622863_consumption' has phase imbalance of 57.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622760_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622948_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623024_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622823_consumption' has phase imbalance of 34.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2007264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622979_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622895_consumption' has phase imbalance of 170.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623009_consumption' has phase imbalance of 262.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622825_consumption' has phase imbalance of 246.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622770_consumption' has phase imbalance of 235.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622902_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0623043_consumption' has phase imbalance of 111.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0622976_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 724 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0622756' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0622937' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0622810' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.247 MW |
| Total load Q | 674.2 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV032835_Transformer | 275.0 kVA | 14.5% |
| 75_MVLV068396_Transformer | 110.0 kVA | 18.6% |
| 75_MVLV128971_Transformer | 176.0 kVA | 9.8% |
| 75_MVLV121415_Transformer | 693.0 kVA | 31.7% |
| 75_MVLV064469_Transformer | 176.0 kVA | 8.2% |
| 75_MVLV131389_Transformer | 440.0 kVA | 44.8% |
| 75_MVLV150789_Transformer | 275.0 kVA | 14.3% |
| 75_MVLV003540_Transformer | 275.0 kVA | 47.9% |
| 75_MVLV101643_Transformer | 110.0 kVA | 8.4% |
| 75_MVLV149790_Transformer | 275.0 kVA | 9.9% |
| 75_MVLV064468_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV068170_Transformer | 176.0 kVA | 11.5% |
| 75_MVLV036174_Transformer | 110.0 kVA | 11.0% |
| 75_MVLV105233_Transformer | 110.0 kVA | 1.4% |
| 75_MVLV066981_Transformer | 110.0 kVA | 9.5% |
| 75_MVLV051615_Transformer | 440.0 kVA | 27.9% |
| 75_MVLV057996_Transformer | 440.0 kVA | 19.9% |
| 75_MVLV021842_Transformer | 176.0 kVA | 3.1% |
| 75_MVLV118870_Transformer | 275.0 kVA | 17.2% |
| 75_MVLV086579_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV171891_Transformer | 275.0 kVA | 21.9% |
| 75_MVLV005718_Transformer | 110.0 kVA | 2.5% |
| 75_MVLV160861_Transformer | 693.0 kVA | 28.2% |
| 75_MVLV150000_Transformer | 176.0 kVA | 7.2% |
| 75_MVLV106408_Transformer | 440.0 kVA | 30.1% |
| 75_MVLV155271_Transformer | 176.0 kVA | 15.5% |
| 75_MVLV039200_Transformer | 176.0 kVA | 9.9% |
| 75_MVLV036301_Transformer | 110.0 kVA | 11.8% |
| 75_MVLV128716_Transformer | 275.0 kVA | 13.3% |
| 75_MVLV114992_Transformer | 110.0 kVA | 0.7% |
| 75_MVLV062483_Transformer | 176.0 kVA | 19.6% |
| 75_MVLV150790_Transformer | 110.0 kVA | 0.6% |
| 75_MVLV105217_Transformer | 110.0 kVA | 1.1% |
| 75_MVLV114990_Transformer | 176.0 kVA | 12.0% |
| 75_MVLV017701_Transformer | 176.0 kVA | 17.7% |
| 75_MVLV039225_Transformer | 110.0 kVA | 11.3% |
| 75_MVLV121076_Transformer | 176.0 kVA | 22.9% |
| 75_MVLV149997_Transformer | 110.0 kVA | 3.8% |
| 75_MVLV040308_Transformer | 176.0 kVA | 10.4% |
| 75_MVLV123935_Transformer | 176.0 kVA | 5.9% |
| 75_MVLV039205_Transformer | 110.0 kVA | 0.8% |
| 75_MVLV066985_Transformer | 440.0 kVA | 15.4% |
| 75_MVLV017700_Transformer | 275.0 kVA | 22.8% |
| 75_MVLV019048_Transformer | 275.0 kVA | 22.7% |
| 75_MVLV121073_Transformer | 110.0 kVA | 7.9% |
| 75_MVLV149764_Transformer | 110.0 kVA | 4.3% |
| 75_MVLV114993_Transformer | 176.0 kVA | 13.6% |
| 75_MVLV004329_Transformer | 110.0 kVA | 3.2% |
| 75_MVLV060362_Transformer | 693.0 kVA | 28.6% |
| 75_MVLV149770_Transformer | 110.0 kVA | 13.0% |
| 75_MVLV138021_Transformer | 176.0 kVA | 8.4% |
| 75_MVLV105327_Transformer | 110.0 kVA | 6.9% |
| 75_MVLV066980_Transformer | 176.0 kVA | 8.2% |
| 75_MVLV058000_Transformer | 176.0 kVA | 15.7% |
| 75_MVLV135391_Transformer | 275.0 kVA | 17.7% |
| 75_MVLV149996_Transformer | 176.0 kVA | 21.5% |
| 75_MVLV158240_Transformer | 275.0 kVA | 18.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.25 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0622753' (LV, 0.24 kV) has an electrical reach of 20.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0622756' (LV, 0.24 kV) has an electrical reach of 7.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0622884' (LV, 0.24 kV) has an electrical reach of 2.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 540 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 540 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 57 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 131 |
| LV_236V | 4-wire | 409 / 409 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 409 |
| Neutral branches | 352 |
| Grounding points | 57 |
| Neutral sections | 57 |
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
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 54 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 58 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1960.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 409 / 131 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 449 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 449 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0622739_production, 75_LVBus0622740_production, 75_LVBus0622741_production, 75_LVBus0622743_production, 75_LVBus0622744_production, 75_LVBus0622745_consumption, 75_LVBus0622745_production, 75_LVBus0622747_production, 75_LVBus0622748_production, 75_LVBus0622750_production, 75_LVBus0622751_production, 75_LVBus0622753_consumption, 75_LVBus0622753_production, 75_LVBus0622754_production, 75_LVBus0622756_production, 75_LVBus0622758_consumption, 75_LVBus0622758_production, 75_LVBus0622760_production, 75_LVBus0622761_production, 75_LVBus0622762_production, 75_LVBus0622763_production, 75_LVBus0622764_production, 75_LVBus0622765_production, 75_LVBus0622767_production, 75_LVBus0622768_production, 75_LVBus0622769_production, 75_LVBus0622770_production, 75_LVBus0622771_production, 75_LVBus0622774_production, 75_LVBus0622775_production, 75_LVBus0622777_production, 75_LVBus0622778_production, 75_LVBus0622781_consumption, 75_LVBus0622781_production, 75_LVBus0622782_consumption, 75_LVBus0622782_production, 75_LVBus0622783_production, 75_LVBus0622785_production, 75_LVBus0622786_production, 75_LVBus0622787_production, 75_LVBus0622789_consumption, 75_LVBus0622789_production, 75_LVBus0622790_consumption, 75_LVBus0622790_production, 75_LVBus0622791_production, 75_LVBus0622792_production, 75_LVBus0622796_consumption, 75_LVBus0622796_production, 75_LVBus0622797_production, 75_LVBus0622800_production, 75_LVBus0622801_production, 75_LVBus0622802_production, 75_LVBus0622804_production, 75_LVBus0622805_production, 75_LVBus0622806_consumption, 75_LVBus0622806_production, 75_LVBus0622808_consumption, 75_LVBus0622808_production, 75_LVBus0622810_production, 75_LVBus0622812_production, 75_LVBus0622813_production, 75_LVBus0622814_production, 75_LVBus0622816_consumption, 75_LVBus0622816_production, 75_LVBus0622817_consumption, 75_LVBus0622817_production, 75_LVBus0622818_consumption, 75_LVBus0622818_production, 75_LVBus0622819_production, 75_LVBus0622820_production, 75_LVBus0622821_production, 75_LVBus0622823_production, 75_LVBus0622824_production, 75_LVBus0622825_production, 75_LVBus0622826_production, 75_LVBus0622827_production, 75_LVBus0622828_consumption, 75_LVBus0622828_production, 75_LVBus0622829_consumption, 75_LVBus0622829_production, 75_LVBus0622830_production, 75_LVBus0622831_production, 75_LVBus0622833_production, 75_LVBus0622835_production, 75_LVBus0622836_production, 75_LVBus0622837_production, 75_LVBus0622838_production, 75_LVBus0622839_production, 75_LVBus0622840_production, 75_LVBus0622841_production, 75_LVBus0622842_production, 75_LVBus0622843_production, 75_LVBus0622845_production, 75_LVBus0622847_consumption, 75_LVBus0622847_production, 75_LVBus0622848_production, 75_LVBus0622849_production, 75_LVBus0622851_production, 75_LVBus0622852_production, 75_LVBus0622853_production, 75_LVBus0622854_production, 75_LVBus0622856_production, 75_LVBus0622857_production, 75_LVBus0622858_production, 75_LVBus0622859_production, 75_LVBus0622860_consumption, 75_LVBus0622860_production, 75_LVBus0622861_consumption, 75_LVBus0622861_production, 75_LVBus0622862_production, 75_LVBus0622863_production, 75_LVBus0622864_consumption, 75_LVBus0622864_production, 75_LVBus0622865_production, 75_LVBus0622867_production, 75_LVBus0622868_production, 75_LVBus0622869_production, 75_LVBus0622870_consumption, 75_LVBus0622870_production, 75_LVBus0622871_production, 75_LVBus0622872_production, 75_LVBus0622873_production, 75_LVBus0622875_consumption, 75_LVBus0622875_production, 75_LVBus0622876_consumption, 75_LVBus0622876_production, 75_LVBus0622877_production, 75_LVBus0622878_production, 75_LVBus0622879_production, 75_LVBus0622880_production, 75_LVBus0622881_consumption, 75_LVBus0622881_production, 75_LVBus0622884_consumption, 75_LVBus0622884_production, 75_LVBus0622886_production, 75_LVBus0622887_production, 75_LVBus0622888_production, 75_LVBus0622889_production, 75_LVBus0622890_production, 75_LVBus0622891_production, 75_LVBus0622893_production, 75_LVBus0622895_production, 75_LVBus0622897_consumption, 75_LVBus0622897_production, 75_LVBus0622899_production, 75_LVBus0622900_production, 75_LVBus0622901_production, 75_LVBus0622902_production, 75_LVBus0622903_production, 75_LVBus0622905_production, 75_LVBus0622907_consumption, 75_LVBus0622907_production, 75_LVBus0622908_production, 75_LVBus0622909_consumption, 75_LVBus0622909_production, 75_LVBus0622910_production, 75_LVBus0622912_production, 75_LVBus0622914_consumption, 75_LVBus0622914_production, 75_LVBus0622916_consumption, 75_LVBus0622916_production, 75_LVBus0622917_consumption, 75_LVBus0622917_production, 75_LVBus0622918_production, 75_LVBus0622919_production, 75_LVBus0622921_consumption, 75_LVBus0622921_production, 75_LVBus0622922_production, 75_LVBus0622923_production, 75_LVBus0622925_consumption, 75_LVBus0622925_production, 75_LVBus0622926_consumption, 75_LVBus0622926_production, 75_LVBus0622927_consumption, 75_LVBus0622927_production, 75_LVBus0622928_consumption, 75_LVBus0622928_production, 75_LVBus0622933_consumption, 75_LVBus0622933_production, 75_LVBus0622934_production, 75_LVBus0622937_production, 75_LVBus0622938_consumption, 75_LVBus0622938_production, 75_LVBus0622941_production, 75_LVBus0622943_consumption, 75_LVBus0622943_production, 75_LVBus0622945_consumption, 75_LVBus0622945_production, 75_LVBus0622946_production, 75_LVBus0622947_production, 75_LVBus0622948_production, 75_LVBus0622949_production, 75_LVBus0622950_production, 75_LVBus0622952_production, 75_LVBus0622953_production, 75_LVBus0622954_production, 75_LVBus0622955_production, 75_LVBus0622956_production, 75_LVBus0622957_production, 75_LVBus0622959_production, 75_LVBus0622960_production, 75_LVBus0622961_production, 75_LVBus0622965_consumption, 75_LVBus0622965_production, 75_LVBus0622966_production, 75_LVBus0622967_production, 75_LVBus0622969_production, 75_LVBus0622971_production, 75_LVBus0622972_production, 75_LVBus0622973_production, 75_LVBus0622974_consumption, 75_LVBus0622974_production, 75_LVBus0622976_production, 75_LVBus0622977_production, 75_LVBus0622978_production, 75_LVBus0622979_production, 75_LVBus0622980_production, 75_LVBus0622982_production, 75_LVBus0622984_production, 75_LVBus0622985_production, 75_LVBus0622986_production, 75_LVBus0622987_production, 75_LVBus0622988_consumption, 75_LVBus0622988_production, 75_LVBus0622990_production, 75_LVBus0622991_production, 75_LVBus0622992_production, 75_LVBus0622994_production, 75_LVBus0622996_production, 75_LVBus0622997_production, 75_LVBus0622998_production, 75_LVBus0622999_consumption, 75_LVBus0622999_production, 75_LVBus0623000_consumption, 75_LVBus0623000_production, 75_LVBus0623001_consumption, 75_LVBus0623001_production, 75_LVBus0623002_production, 75_LVBus0623003_production, 75_LVBus0623004_production, 75_LVBus0623006_consumption, 75_LVBus0623006_production, 75_LVBus0623007_production, 75_LVBus0623008_production, 75_LVBus0623009_production, 75_LVBus0623010_production, 75_LVBus0623011_consumption, 75_LVBus0623011_production, 75_LVBus0623012_production, 75_LVBus0623013_production, 75_LVBus0623015_production, 75_LVBus0623016_production, 75_LVBus0623018_production, 75_LVBus0623020_production, 75_LVBus0623022_consumption, 75_LVBus0623022_production, 75_LVBus0623024_production, 75_LVBus0623026_production, 75_LVBus0623027_production, 75_LVBus0623028_consumption, 75_LVBus0623028_production, 75_LVBus0623029_production, 75_LVBus0623030_production, 75_LVBus0623032_production, 75_LVBus0623034_production, 75_LVBus0623035_consumption, 75_LVBus0623035_production, 75_LVBus0623036_production, 75_LVBus0623037_production, 75_LVBus0623038_consumption, 75_LVBus0623038_production, 75_LVBus0623041_production, 75_LVBus0623042_production, 75_LVBus0623043_production, 75_LVBus0623045_production, 75_LVBus0623046_production, 75_LVBus0623047_production, 75_LVBus0623048_production, 75_LVBus0623049_production, 75_LVBus0623050_production, 75_LVBus0623051_production, 75_LVBus0623052_production, 75_LVBus0623053_production, 75_LVBus0623054_production, 75_LVBus0623056_production, 75_LVBus0623057_production, 75_LVBus0623058_production, 75_LVBus0623060_production, 75_LVBus0623061_production, 75_LVBus0623062_production, 75_LVBus0623063_production, 75_LVBus0623064_production, 75_LVBus0623065_consumption, 75_LVBus0623065_production, 75_LVBus0623066_production, 75_LVBus0623067_consumption, 75_LVBus0623067_production, 75_LVBus0623069_production, 75_LVBus0623070_production, 75_LVBus0623072_consumption, 75_LVBus0623072_production, 75_LVBus0623074_production, 75_LVBus0623076_production, 75_LVBus0623077_production, 75_LVBus0623078_production, 75_LVBus0623080_production, 75_LVBus0623081_production, 75_LVBus0623083_consumption, 75_LVBus0623083_production, 75_LVBus0623084_production, 75_LVBus0623085_production, 75_LVBus0623086_consumption, 75_LVBus0623086_production, 75_LVBus0623087_production, 75_LVBus0623088_production, 75_LVBus0623089_consumption, 75_LVBus0623089_production, 75_LVBus0623091_production, 75_LVBus0623092_consumption, 75_LVBus0623092_production, 75_LVBus0623094_production, 75_LVBus0623096_production, 75_LVBus0623098_consumption, 75_LVBus0623098_production, 75_LVBus0623099_production, 75_LVBus0623100_production, 75_LVBus0623101_production, 75_LVBus0623103_production, 75_LVBus0623105_production, 75_LVBus0623106_production, 75_LVBus0623107_production, 75_LVBus0623108_production, 75_LVBus0623109_production, 75_LVBus0623111_production, 75_LVBus0623112_production, 75_LVBus0623113_production, 75_LVBus0623114_production, 75_LVBus0623115_production, 75_LVBus0623117_consumption, 75_LVBus0623117_production, 75_LVBus0623119_production, 75_LVBus0623120_consumption, 75_LVBus0623120_production, 75_LVBus0623121_production, 75_LVBus0623122_production, 75_LVBus0623123_production, 75_LVBus0623124_production, 75_LVBus0623126_production, 75_LVBus0623127_consumption, 75_LVBus0623127_production, 75_LVBus0623128_production, 75_LVBus0623129_production, 75_LVBus0623130_production, 75_LVBus0623131_production, 75_LVBus0623132_production, 75_LVBus0623133_production, 75_LVBus0623134_production, 75_LVBus0623135_production, 75_LVBus0623136_production, 75_LVBus0623137_production, 75_LVBus0623138_consumption, 75_LVBus0623138_production, 75_LVBus0623139_production, 75_LVBus0623141_consumption, 75_LVBus0623141_production, 75_LVBus0623142_consumption, 75_LVBus0623142_production, 75_LVBus0623143_consumption, 75_LVBus0623143_production, 75_LVBus0623144_production, 75_LVBus0623145_production, 75_LVBus0623146_production, 75_LVBus0623147_production, 75_LVBus0623151_production, 75_LVBus0623152_consumption, 75_LVBus0623152_production, 75_LVBus0623153_consumption, 75_LVBus0623153_production, 75_LVBus0623154_production, 75_LVBus0623155_production, 75_LVBus0623156_production, 75_LVBus0623157_production, 75_LVBus0623158_production, 75_LVBus0623159_production, 75_LVBus0623160_production, 75_LVBus0623161_production, 75_LVBus0623162_consumption, 75_LVBus0623162_production, 75_LVBus1942502_production, 75_LVBus1957909_production, 75_LVBus1979932_production, 75_LVBus1983180_consumption, 75_LVBus1983180_production, 75_LVBus1989360_consumption, 75_LVBus1989360_production, 75_LVBus2007252_production, 75_LVBus2007253_production, 75_LVBus2007254_consumption, 75_LVBus2007254_production, 75_LVBus2007255_production, 75_LVBus2007256_production, 75_LVBus2007257_production, 75_LVBus2007258_production, 75_LVBus2007259_consumption, 75_LVBus2007259_production, 75_LVBus2007260_production, 75_LVBus2007261_production, 75_LVBus2007262_production, 75_LVBus2007263_production, 75_LVBus2007264_production, 75_LVBus2007265_production, 75_LVBus2007266_production, 75_LVBus2007267_production, 75_LVBus2007268_consumption, 75_LVBus2007268_production, 75_LVBus2007269_production, 75_LVBus2007270_consumption, 75_LVBus2007270_production, 75_LVBus2007271_production, 75_LVBus2007272_production, 75_LVBus2007273_production, 75_LVBus2007274_production, 75_LVBus2007275_production, 75_LVBus2007276_consumption, 75_LVBus2007276_production, 75_LVBus2007277_production, 75_LVBus2007278_consumption, 75_LVBus2007278_production, 75_LVBus2007279_production, 75_MVLV012820_consumption, 75_MVLV012820_production, 75_MVLV025892_consumption, 75_MVLV025892_production, 75_MVLV027379_consumption, 75_MVLV027379_production, 75_MVLV056442_consumption, 75_MVLV056442_production, 75_MVLV064447_consumption, 75_MVLV064447_production, 75_MVLV077747_consumption, 75_MVLV077747_production, 75_MVLV088718_consumption, 75_MVLV088718_production, 75_MVLV094221_consumption, 75_MVLV094221_production, 75_MVLV149747_consumption, 75_MVLV149747_production, 75_MVLV159485_consumption, 75_MVLV159485_production.

## 9. Data Quality Summary

**Total findings:** 281 (0 errors, 5 warnings, 276 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  448 of 724 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.25 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  449 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622859_consumption`  
  Load '75_LVBus0622859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622750_consumption`  
  Load '75_LVBus0622750_consumption' has phase imbalance of 162.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623151_consumption`  
  Load '75_LVBus0623151_consumption' has phase imbalance of 276.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622842_consumption`  
  Load '75_LVBus0622842_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622775_consumption`  
  Load '75_LVBus0622775_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622804_consumption`  
  Load '75_LVBus0622804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622987_consumption`  
  Load '75_LVBus0622987_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623111_consumption`  
  Load '75_LVBus0623111_consumption' has phase imbalance of 210.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623114_consumption`  
  Load '75_LVBus0623114_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623088_consumption`  
  Load '75_LVBus0623088_consumption' has phase imbalance of 66.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622743_consumption`  
  Load '75_LVBus0622743_consumption' has phase imbalance of 50.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623137_consumption`  
  Load '75_LVBus0623137_consumption' has phase imbalance of 285.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623122_consumption`  
  Load '75_LVBus0623122_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622786_consumption`  
  Load '75_LVBus0622786_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622941_consumption`  
  Load '75_LVBus0622941_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622908_consumption`  
  Load '75_LVBus0622908_consumption' has phase imbalance of 51.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622869_consumption`  
  Load '75_LVBus0622869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622774_consumption`  
  Load '75_LVBus0622774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622972_consumption`  
  Load '75_LVBus0622972_consumption' has phase imbalance of 204.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623076_consumption`  
  Load '75_LVBus0623076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622954_consumption`  
  Load '75_LVBus0622954_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622830_consumption`  
  Load '75_LVBus0622830_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623161_consumption`  
  Load '75_LVBus0623161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623139_consumption`  
  Load '75_LVBus0623139_consumption' has phase imbalance of 174.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622778_consumption`  
  Load '75_LVBus0622778_consumption' has phase imbalance of 89.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622827_consumption`  
  Load '75_LVBus0622827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622891_consumption`  
  Load '75_LVBus0622891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623064_consumption`  
  Load '75_LVBus0623064_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622923_consumption`  
  Load '75_LVBus0622923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007266_consumption`  
  Load '75_LVBus2007266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623080_consumption`  
  Load '75_LVBus0623080_consumption' has phase imbalance of 78.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623096_consumption`  
  Load '75_LVBus0623096_consumption' has phase imbalance of 244.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622831_consumption`  
  Load '75_LVBus0622831_consumption' has phase imbalance of 59.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623126_consumption`  
  Load '75_LVBus0623126_consumption' has phase imbalance of 103.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623081_consumption`  
  Load '75_LVBus0623081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622922_consumption`  
  Load '75_LVBus0622922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623115_consumption`  
  Load '75_LVBus0623115_consumption' has phase imbalance of 106.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622802_consumption`  
  Load '75_LVBus0622802_consumption' has phase imbalance of 130.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622918_consumption`  
  Load '75_LVBus0622918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622886_consumption`  
  Load '75_LVBus0622886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622769_consumption`  
  Load '75_LVBus0622769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007255_consumption`  
  Load '75_LVBus2007255_consumption' has phase imbalance of 189.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623051_consumption`  
  Load '75_LVBus0623051_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623156_consumption`  
  Load '75_LVBus0623156_consumption' has phase imbalance of 136.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622879_consumption`  
  Load '75_LVBus0622879_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623147_consumption`  
  Load '75_LVBus0623147_consumption' has phase imbalance of 251.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622889_consumption`  
  Load '75_LVBus0622889_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623146_consumption`  
  Load '75_LVBus0623146_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623046_consumption`  
  Load '75_LVBus0623046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1957909_consumption`  
  Load '75_LVBus1957909_consumption' has phase imbalance of 93.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007260_consumption`  
  Load '75_LVBus2007260_consumption' has phase imbalance of 199.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623060_consumption`  
  Load '75_LVBus0623060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623101_consumption`  
  Load '75_LVBus0623101_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007274_consumption`  
  Load '75_LVBus2007274_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623158_consumption`  
  Load '75_LVBus0623158_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622791_consumption`  
  Load '75_LVBus0622791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622739_consumption`  
  Load '75_LVBus0622739_consumption' has phase imbalance of 210.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622934_consumption`  
  Load '75_LVBus0622934_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623136_consumption`  
  Load '75_LVBus0623136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622877_consumption`  
  Load '75_LVBus0622877_consumption' has phase imbalance of 102.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622957_consumption`  
  Load '75_LVBus0622957_consumption' has phase imbalance of 231.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623049_consumption`  
  Load '75_LVBus0623049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007275_consumption`  
  Load '75_LVBus2007275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622899_consumption`  
  Load '75_LVBus0622899_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623134_consumption`  
  Load '75_LVBus0623134_consumption' has phase imbalance of 110.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623077_consumption`  
  Load '75_LVBus0623077_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622814_consumption`  
  Load '75_LVBus0622814_consumption' has phase imbalance of 114.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622741_consumption`  
  Load '75_LVBus0622741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622871_consumption`  
  Load '75_LVBus0622871_consumption' has phase imbalance of 139.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623061_consumption`  
  Load '75_LVBus0623061_consumption' has phase imbalance of 263.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622797_consumption`  
  Load '75_LVBus0622797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622966_consumption`  
  Load '75_LVBus0622966_consumption' has phase imbalance of 194.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622839_consumption`  
  Load '75_LVBus0622839_consumption' has phase imbalance of 60.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622959_consumption`  
  Load '75_LVBus0622959_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623113_consumption`  
  Load '75_LVBus0623113_consumption' has phase imbalance of 278.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622990_consumption`  
  Load '75_LVBus0622990_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623041_consumption`  
  Load '75_LVBus0623041_consumption' has phase imbalance of 135.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622888_consumption`  
  Load '75_LVBus0622888_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622985_consumption`  
  Load '75_LVBus0622985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622986_consumption`  
  Load '75_LVBus0622986_consumption' has phase imbalance of 34.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622912_consumption`  
  Load '75_LVBus0622912_consumption' has phase imbalance of 117.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622952_consumption`  
  Load '75_LVBus0622952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007277_consumption`  
  Load '75_LVBus2007277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623034_consumption`  
  Load '75_LVBus0623034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623004_consumption`  
  Load '75_LVBus0623004_consumption' has phase imbalance of 104.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623042_consumption`  
  Load '75_LVBus0623042_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622787_consumption`  
  Load '75_LVBus0622787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622977_consumption`  
  Load '75_LVBus0622977_consumption' has phase imbalance of 143.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622910_consumption`  
  Load '75_LVBus0622910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622946_consumption`  
  Load '75_LVBus0622946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622835_consumption`  
  Load '75_LVBus0622835_consumption' has phase imbalance of 229.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623105_consumption`  
  Load '75_LVBus0623105_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622763_consumption`  
  Load '75_LVBus0622763_consumption' has phase imbalance of 214.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623112_consumption`  
  Load '75_LVBus0623112_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622764_consumption`  
  Load '75_LVBus0622764_consumption' has phase imbalance of 149.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622853_consumption`  
  Load '75_LVBus0622853_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007253_consumption`  
  Load '75_LVBus2007253_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622982_consumption`  
  Load '75_LVBus0622982_consumption' has phase imbalance of 129.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622748_consumption`  
  Load '75_LVBus0622748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622783_consumption`  
  Load '75_LVBus0622783_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622740_consumption`  
  Load '75_LVBus0622740_consumption' has phase imbalance of 30.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622980_consumption`  
  Load '75_LVBus0622980_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622865_consumption`  
  Load '75_LVBus0622865_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007256_consumption`  
  Load '75_LVBus2007256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007257_consumption`  
  Load '75_LVBus2007257_consumption' has phase imbalance of 215.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622824_consumption`  
  Load '75_LVBus0622824_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622767_consumption`  
  Load '75_LVBus0622767_consumption' has phase imbalance of 223.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622792_consumption`  
  Load '75_LVBus0622792_consumption' has phase imbalance of 196.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623070_consumption`  
  Load '75_LVBus0623070_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622955_consumption`  
  Load '75_LVBus0622955_consumption' has phase imbalance of 139.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622841_consumption`  
  Load '75_LVBus0622841_consumption' has phase imbalance of 285.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622854_consumption`  
  Load '75_LVBus0622854_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623018_consumption`  
  Load '75_LVBus0623018_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622751_consumption`  
  Load '75_LVBus0622751_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007267_consumption`  
  Load '75_LVBus2007267_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623030_consumption`  
  Load '75_LVBus0623030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622992_consumption`  
  Load '75_LVBus0622992_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007279_consumption`  
  Load '75_LVBus2007279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623053_consumption`  
  Load '75_LVBus0623053_consumption' has phase imbalance of 168.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623002_consumption`  
  Load '75_LVBus0623002_consumption' has phase imbalance of 258.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622821_consumption`  
  Load '75_LVBus0622821_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622848_consumption`  
  Load '75_LVBus0622848_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007265_consumption`  
  Load '75_LVBus2007265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623032_consumption`  
  Load '75_LVBus0623032_consumption' has phase imbalance of 198.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622765_consumption`  
  Load '75_LVBus0622765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623007_consumption`  
  Load '75_LVBus0623007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622754_consumption`  
  Load '75_LVBus0622754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623003_consumption`  
  Load '75_LVBus0623003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622994_consumption`  
  Load '75_LVBus0622994_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622996_consumption`  
  Load '75_LVBus0622996_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623085_consumption`  
  Load '75_LVBus0623085_consumption' has phase imbalance of 285.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623144_consumption`  
  Load '75_LVBus0623144_consumption' has phase imbalance of 59.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623012_consumption`  
  Load '75_LVBus0623012_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622849_consumption`  
  Load '75_LVBus0622849_consumption' has phase imbalance of 217.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007273_consumption`  
  Load '75_LVBus2007273_consumption' has phase imbalance of 249.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623107_consumption`  
  Load '75_LVBus0623107_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623091_consumption`  
  Load '75_LVBus0623091_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622826_consumption`  
  Load '75_LVBus0622826_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622836_consumption`  
  Load '75_LVBus0622836_consumption' has phase imbalance of 232.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622956_consumption`  
  Load '75_LVBus0622956_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623155_consumption`  
  Load '75_LVBus0623155_consumption' has phase imbalance of 133.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1942502_consumption`  
  Load '75_LVBus1942502_consumption' has phase imbalance of 109.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622744_consumption`  
  Load '75_LVBus0622744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622858_consumption`  
  Load '75_LVBus0622858_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007263_consumption`  
  Load '75_LVBus2007263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622785_consumption`  
  Load '75_LVBus0622785_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622893_consumption`  
  Load '75_LVBus0622893_consumption' has phase imbalance of 208.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007272_consumption`  
  Load '75_LVBus2007272_consumption' has phase imbalance of 258.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622761_consumption`  
  Load '75_LVBus0622761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622984_consumption`  
  Load '75_LVBus0622984_consumption' has phase imbalance of 294.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622961_consumption`  
  Load '75_LVBus0622961_consumption' has phase imbalance of 35.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007262_consumption`  
  Load '75_LVBus2007262_consumption' has phase imbalance of 70.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623132_consumption`  
  Load '75_LVBus0623132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623078_consumption`  
  Load '75_LVBus0623078_consumption' has phase imbalance of 109.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622838_consumption`  
  Load '75_LVBus0622838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622949_consumption`  
  Load '75_LVBus0622949_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623027_consumption`  
  Load '75_LVBus0623027_consumption' has phase imbalance of 241.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623157_consumption`  
  Load '75_LVBus0623157_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622900_consumption`  
  Load '75_LVBus0622900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623013_consumption`  
  Load '75_LVBus0623013_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622872_consumption`  
  Load '75_LVBus0622872_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623121_consumption`  
  Load '75_LVBus0623121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007269_consumption`  
  Load '75_LVBus2007269_consumption' has phase imbalance of 283.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622973_consumption`  
  Load '75_LVBus0622973_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623106_consumption`  
  Load '75_LVBus0623106_consumption' has phase imbalance of 277.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622867_consumption`  
  Load '75_LVBus0622867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622762_consumption`  
  Load '75_LVBus0622762_consumption' has phase imbalance of 114.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623103_consumption`  
  Load '75_LVBus0623103_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622856_consumption`  
  Load '75_LVBus0622856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622967_consumption`  
  Load '75_LVBus0622967_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1979932_consumption`  
  Load '75_LVBus1979932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622862_consumption`  
  Load '75_LVBus0622862_consumption' has phase imbalance of 261.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623056_consumption`  
  Load '75_LVBus0623056_consumption' has phase imbalance of 197.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622819_consumption`  
  Load '75_LVBus0622819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623066_consumption`  
  Load '75_LVBus0623066_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623145_consumption`  
  Load '75_LVBus0623145_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622997_consumption`  
  Load '75_LVBus0622997_consumption' has phase imbalance of 239.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623135_consumption`  
  Load '75_LVBus0623135_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623036_consumption`  
  Load '75_LVBus0623036_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623094_consumption`  
  Load '75_LVBus0623094_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623047_consumption`  
  Load '75_LVBus0623047_consumption' has phase imbalance of 276.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622998_consumption`  
  Load '75_LVBus0622998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622771_consumption`  
  Load '75_LVBus0622771_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623084_consumption`  
  Load '75_LVBus0623084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622960_consumption`  
  Load '75_LVBus0622960_consumption' has phase imbalance of 156.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622852_consumption`  
  Load '75_LVBus0622852_consumption' has phase imbalance of 97.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622887_consumption`  
  Load '75_LVBus0622887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623159_consumption`  
  Load '75_LVBus0623159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007252_consumption`  
  Load '75_LVBus2007252_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623015_consumption`  
  Load '75_LVBus0623015_consumption' has phase imbalance of 238.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622919_consumption`  
  Load '75_LVBus0622919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623062_consumption`  
  Load '75_LVBus0623062_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623087_consumption`  
  Load '75_LVBus0623087_consumption' has phase imbalance of 291.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623133_consumption`  
  Load '75_LVBus0623133_consumption' has phase imbalance of 226.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622800_consumption`  
  Load '75_LVBus0622800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623048_consumption`  
  Load '75_LVBus0623048_consumption' has phase imbalance of 219.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623057_consumption`  
  Load '75_LVBus0623057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622820_consumption`  
  Load '75_LVBus0622820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622969_consumption`  
  Load '75_LVBus0622969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623008_consumption`  
  Load '75_LVBus0623008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622805_consumption`  
  Load '75_LVBus0622805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623108_consumption`  
  Load '75_LVBus0623108_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623037_consumption`  
  Load '75_LVBus0623037_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623069_consumption`  
  Load '75_LVBus0623069_consumption' has phase imbalance of 230.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622947_consumption`  
  Load '75_LVBus0622947_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623100_consumption`  
  Load '75_LVBus0623100_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622978_consumption`  
  Load '75_LVBus0622978_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623050_consumption`  
  Load '75_LVBus0623050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622971_consumption`  
  Load '75_LVBus0622971_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623154_consumption`  
  Load '75_LVBus0623154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622890_consumption`  
  Load '75_LVBus0622890_consumption' has phase imbalance of 127.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007258_consumption`  
  Load '75_LVBus2007258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623052_consumption`  
  Load '75_LVBus0623052_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622843_consumption`  
  Load '75_LVBus0622843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623124_consumption`  
  Load '75_LVBus0623124_consumption' has phase imbalance of 155.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623020_consumption`  
  Load '75_LVBus0623020_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623129_consumption`  
  Load '75_LVBus0623129_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622950_consumption`  
  Load '75_LVBus0622950_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622903_consumption`  
  Load '75_LVBus0622903_consumption' has phase imbalance of 236.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622851_consumption`  
  Load '75_LVBus0622851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623123_consumption`  
  Load '75_LVBus0623123_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622812_consumption`  
  Load '75_LVBus0622812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623054_consumption`  
  Load '75_LVBus0623054_consumption' has phase imbalance of 26.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622991_consumption`  
  Load '75_LVBus0622991_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623130_consumption`  
  Load '75_LVBus0623130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622857_consumption`  
  Load '75_LVBus0622857_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007261_consumption`  
  Load '75_LVBus2007261_consumption' has phase imbalance of 180.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623119_consumption`  
  Load '75_LVBus0623119_consumption' has phase imbalance of 104.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623058_consumption`  
  Load '75_LVBus0623058_consumption' has phase imbalance of 23.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623045_consumption`  
  Load '75_LVBus0623045_consumption' has phase imbalance of 208.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623029_consumption`  
  Load '75_LVBus0623029_consumption' has phase imbalance of 141.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622768_consumption`  
  Load '75_LVBus0622768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622901_consumption`  
  Load '75_LVBus0622901_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007271_consumption`  
  Load '75_LVBus2007271_consumption' has phase imbalance of 68.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622863_consumption`  
  Load '75_LVBus0622863_consumption' has phase imbalance of 57.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622840_consumption`  
  Load '75_LVBus0622840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622760_consumption`  
  Load '75_LVBus0622760_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622948_consumption`  
  Load '75_LVBus0622948_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622777_consumption`  
  Load '75_LVBus0622777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623024_consumption`  
  Load '75_LVBus0623024_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622845_consumption`  
  Load '75_LVBus0622845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622823_consumption`  
  Load '75_LVBus0622823_consumption' has phase imbalance of 34.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2007264_consumption`  
  Load '75_LVBus2007264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622979_consumption`  
  Load '75_LVBus0622979_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622895_consumption`  
  Load '75_LVBus0622895_consumption' has phase imbalance of 170.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623009_consumption`  
  Load '75_LVBus0623009_consumption' has phase imbalance of 262.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623074_consumption`  
  Load '75_LVBus0623074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623010_consumption`  
  Load '75_LVBus0623010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622825_consumption`  
  Load '75_LVBus0622825_consumption' has phase imbalance of 246.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622770_consumption`  
  Load '75_LVBus0622770_consumption' has phase imbalance of 235.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623026_consumption`  
  Load '75_LVBus0623026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622902_consumption`  
  Load '75_LVBus0622902_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0623043_consumption`  
  Load '75_LVBus0623043_consumption' has phase imbalance of 111.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0622976_consumption`  
  Load '75_LVBus0622976_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 724 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0622756' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0622937' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0622810' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0622753' (LV, 0.24 kV) has an electrical reach of 20.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0622756' (LV, 0.24 kV) has an electrical reach of 7.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0622884' (LV, 0.24 kV) has an electrical reach of 2.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  540 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '75_77418' and '75_105273' at bus '75_MVBus003649' have ||Z||_F ratio 1570.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  168 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0622739_consumption, 75_LVBus0622741_consumption, 75_LVBus0622744_consumption, 75_LVBus0622748_consumption, 75_LVBus0622750_consumption, 75_LVBus0622751_consumption, 75_LVBus0622754_consumption, 75_LVBus0622761_consumption, 75_LVBus0622763_consumption, 75_LVBus0622765_consumption, 75_LVBus0622767_consumption, 75_LVBus0622768_consumption, 75_LVBus0622769_consumption, 75_LVBus0622771_consumption, 75_LVBus0622774_consumption, 75_LVBus0622777_consumption, 75_LVBus0622787_consumption, 75_LVBus0622791_consumption, 75_LVBus0622792_consumption, 75_LVBus0622797_consumption, 75_LVBus0622800_consumption, 75_LVBus0622804_consumption, 75_LVBus0622805_consumption, 75_LVBus0622812_consumption, 75_LVBus0622819_consumption, 75_LVBus0622820_consumption, 75_LVBus0622821_consumption, 75_LVBus0622824_consumption, 75_LVBus0622825_consumption, 75_LVBus0622827_consumption, 75_LVBus0622838_consumption, 75_LVBus0622840_consumption, 75_LVBus0622841_consumption, 75_LVBus0622843_consumption, 75_LVBus0622845_consumption, 75_LVBus0622851_consumption, 75_LVBus0622853_consumption, 75_LVBus0622856_consumption, 75_LVBus0622857_consumption, 75_LVBus0622858_consumption, 75_LVBus0622859_consumption, 75_LVBus0622862_consumption, 75_LVBus0622865_consumption, 75_LVBus0622867_consumption, 75_LVBus0622869_consumption, 75_LVBus0622886_consumption, 75_LVBus0622887_consumption, 75_LVBus0622888_consumption, 75_LVBus0622889_consumption, 75_LVBus0622891_consumption, 75_LVBus0622900_consumption, 75_LVBus0622901_consumption, 75_LVBus0622903_consumption, 75_LVBus0622910_consumption, 75_LVBus0622918_consumption, 75_LVBus0622919_consumption, 75_LVBus0622922_consumption, 75_LVBus0622923_consumption, 75_LVBus0622934_consumption, 75_LVBus0622941_consumption, 75_LVBus0622946_consumption, 75_LVBus0622947_consumption, 75_LVBus0622948_consumption, 75_LVBus0622949_consumption, 75_LVBus0622950_consumption, 75_LVBus0622952_consumption, 75_LVBus0622954_consumption, 75_LVBus0622956_consumption, 75_LVBus0622957_consumption, 75_LVBus0622959_consumption, 75_LVBus0622960_consumption, 75_LVBus0622967_consumption, 75_LVBus0622969_consumption, 75_LVBus0622971_consumption, 75_LVBus0622972_consumption, 75_LVBus0622978_consumption, 75_LVBus0622979_consumption, 75_LVBus0622984_consumption, 75_LVBus0622985_consumption, 75_LVBus0622991_consumption, 75_LVBus0622992_consumption, 75_LVBus0622997_consumption, 75_LVBus0622998_consumption, 75_LVBus0623002_consumption, 75_LVBus0623003_consumption, 75_LVBus0623007_consumption, 75_LVBus0623008_consumption, 75_LVBus0623009_consumption, 75_LVBus0623010_consumption, 75_LVBus0623012_consumption, 75_LVBus0623013_consumption, 75_LVBus0623026_consumption, 75_LVBus0623027_consumption, 75_LVBus0623030_consumption, 75_LVBus0623032_consumption, 75_LVBus0623034_consumption, 75_LVBus0623036_consumption, 75_LVBus0623037_consumption, 75_LVBus0623042_consumption, 75_LVBus0623045_consumption, 75_LVBus0623046_consumption, 75_LVBus0623047_consumption, 75_LVBus0623048_consumption, 75_LVBus0623049_consumption, 75_LVBus0623050_consumption, 75_LVBus0623053_consumption, 75_LVBus0623056_consumption, 75_LVBus0623057_consumption, 75_LVBus0623060_consumption, 75_LVBus0623061_consumption, 75_LVBus0623066_consumption, 75_LVBus0623069_consumption, 75_LVBus0623074_consumption, 75_LVBus0623076_consumption, 75_LVBus0623077_consumption, 75_LVBus0623081_consumption, 75_LVBus0623084_consumption, 75_LVBus0623085_consumption, 75_LVBus0623087_consumption, 75_LVBus0623091_consumption, 75_LVBus0623094_consumption, 75_LVBus0623096_consumption, 75_LVBus0623101_consumption, 75_LVBus0623103_consumption, 75_LVBus0623105_consumption, 75_LVBus0623106_consumption, 75_LVBus0623107_consumption, 75_LVBus0623108_consumption, 75_LVBus0623111_consumption, 75_LVBus0623113_consumption, 75_LVBus0623114_consumption, 75_LVBus0623121_consumption, 75_LVBus0623122_consumption, 75_LVBus0623123_consumption, 75_LVBus0623124_consumption, 75_LVBus0623130_consumption, 75_LVBus0623132_consumption, 75_LVBus0623133_consumption, 75_LVBus0623136_consumption, 75_LVBus0623139_consumption, 75_LVBus0623145_consumption, 75_LVBus0623147_consumption, 75_LVBus0623151_consumption, 75_LVBus0623154_consumption, 75_LVBus0623157_consumption, 75_LVBus0623158_consumption, 75_LVBus0623159_consumption, 75_LVBus0623161_consumption, 75_LVBus1979932_consumption, 75_LVBus2007252_consumption, 75_LVBus2007253_consumption, 75_LVBus2007255_consumption, 75_LVBus2007256_consumption, 75_LVBus2007257_consumption, 75_LVBus2007258_consumption, 75_LVBus2007260_consumption, 75_LVBus2007261_consumption, 75_LVBus2007263_consumption, 75_LVBus2007264_consumption, 75_LVBus2007265_consumption, 75_LVBus2007266_consumption, 75_LVBus2007269_consumption, 75_LVBus2007272_consumption, 75_LVBus2007273_consumption, 75_LVBus2007274_consumption, 75_LVBus2007275_consumption, 75_LVBus2007277_consumption, 75_LVBus2007279_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  362 group(s) of loads (724 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  18 group(s) of series lines (38 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  449 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0622739_production, 75_LVBus0622740_production, 75_LVBus0622741_production, 75_LVBus0622743_production, 75_LVBus0622744_production, 75_LVBus0622745_consumption, 75_LVBus0622745_production, 75_LVBus0622747_production, 75_LVBus0622748_production, 75_LVBus0622750_production, 75_LVBus0622751_production, 75_LVBus0622753_consumption, 75_LVBus0622753_production, 75_LVBus0622754_production, 75_LVBus0622756_production, 75_LVBus0622758_consumption, 75_LVBus0622758_production, 75_LVBus0622760_production, 75_LVBus0622761_production, 75_LVBus0622762_production, 75_LVBus0622763_production, 75_LVBus0622764_production, 75_LVBus0622765_production, 75_LVBus0622767_production, 75_LVBus0622768_production, 75_LVBus0622769_production, 75_LVBus0622770_production, 75_LVBus0622771_production, 75_LVBus0622774_production, 75_LVBus0622775_production, 75_LVBus0622777_production, 75_LVBus0622778_production, 75_LVBus0622781_consumption, 75_LVBus0622781_production, 75_LVBus0622782_consumption, 75_LVBus0622782_production, 75_LVBus0622783_production, 75_LVBus0622785_production, 75_LVBus0622786_production, 75_LVBus0622787_production, 75_LVBus0622789_consumption, 75_LVBus0622789_production, 75_LVBus0622790_consumption, 75_LVBus0622790_production, 75_LVBus0622791_production, 75_LVBus0622792_production, 75_LVBus0622796_consumption, 75_LVBus0622796_production, 75_LVBus0622797_production, 75_LVBus0622800_production, 75_LVBus0622801_production, 75_LVBus0622802_production, 75_LVBus0622804_production, 75_LVBus0622805_production, 75_LVBus0622806_consumption, 75_LVBus0622806_production, 75_LVBus0622808_consumption, 75_LVBus0622808_production, 75_LVBus0622810_production, 75_LVBus0622812_production, 75_LVBus0622813_production, 75_LVBus0622814_production, 75_LVBus0622816_consumption, 75_LVBus0622816_production, 75_LVBus0622817_consumption, 75_LVBus0622817_production, 75_LVBus0622818_consumption, 75_LVBus0622818_production, 75_LVBus0622819_production, 75_LVBus0622820_production, 75_LVBus0622821_production, 75_LVBus0622823_production, 75_LVBus0622824_production, 75_LVBus0622825_production, 75_LVBus0622826_production, 75_LVBus0622827_production, 75_LVBus0622828_consumption, 75_LVBus0622828_production, 75_LVBus0622829_consumption, 75_LVBus0622829_production, 75_LVBus0622830_production, 75_LVBus0622831_production, 75_LVBus0622833_production, 75_LVBus0622835_production, 75_LVBus0622836_production, 75_LVBus0622837_production, 75_LVBus0622838_production, 75_LVBus0622839_production, 75_LVBus0622840_production, 75_LVBus0622841_production, 75_LVBus0622842_production, 75_LVBus0622843_production, 75_LVBus0622845_production, 75_LVBus0622847_consumption, 75_LVBus0622847_production, 75_LVBus0622848_production, 75_LVBus0622849_production, 75_LVBus0622851_production, 75_LVBus0622852_production, 75_LVBus0622853_production, 75_LVBus0622854_production, 75_LVBus0622856_production, 75_LVBus0622857_production, 75_LVBus0622858_production, 75_LVBus0622859_production, 75_LVBus0622860_consumption, 75_LVBus0622860_production, 75_LVBus0622861_consumption, 75_LVBus0622861_production, 75_LVBus0622862_production, 75_LVBus0622863_production, 75_LVBus0622864_consumption, 75_LVBus0622864_production, 75_LVBus0622865_production, 75_LVBus0622867_production, 75_LVBus0622868_production, 75_LVBus0622869_production, 75_LVBus0622870_consumption, 75_LVBus0622870_production, 75_LVBus0622871_production, 75_LVBus0622872_production, 75_LVBus0622873_production, 75_LVBus0622875_consumption, 75_LVBus0622875_production, 75_LVBus0622876_consumption, 75_LVBus0622876_production, 75_LVBus0622877_production, 75_LVBus0622878_production, 75_LVBus0622879_production, 75_LVBus0622880_production, 75_LVBus0622881_consumption, 75_LVBus0622881_production, 75_LVBus0622884_consumption, 75_LVBus0622884_production, 75_LVBus0622886_production, 75_LVBus0622887_production, 75_LVBus0622888_production, 75_LVBus0622889_production, 75_LVBus0622890_production, 75_LVBus0622891_production, 75_LVBus0622893_production, 75_LVBus0622895_production, 75_LVBus0622897_consumption, 75_LVBus0622897_production, 75_LVBus0622899_production, 75_LVBus0622900_production, 75_LVBus0622901_production, 75_LVBus0622902_production, 75_LVBus0622903_production, 75_LVBus0622905_production, 75_LVBus0622907_consumption, 75_LVBus0622907_production, 75_LVBus0622908_production, 75_LVBus0622909_consumption, 75_LVBus0622909_production, 75_LVBus0622910_production, 75_LVBus0622912_production, 75_LVBus0622914_consumption, 75_LVBus0622914_production, 75_LVBus0622916_consumption, 75_LVBus0622916_production, 75_LVBus0622917_consumption, 75_LVBus0622917_production, 75_LVBus0622918_production, 75_LVBus0622919_production, 75_LVBus0622921_consumption, 75_LVBus0622921_production, 75_LVBus0622922_production, 75_LVBus0622923_production, 75_LVBus0622925_consumption, 75_LVBus0622925_production, 75_LVBus0622926_consumption, 75_LVBus0622926_production, 75_LVBus0622927_consumption, 75_LVBus0622927_production, 75_LVBus0622928_consumption, 75_LVBus0622928_production, 75_LVBus0622933_consumption, 75_LVBus0622933_production, 75_LVBus0622934_production, 75_LVBus0622937_production, 75_LVBus0622938_consumption, 75_LVBus0622938_production, 75_LVBus0622941_production, 75_LVBus0622943_consumption, 75_LVBus0622943_production, 75_LVBus0622945_consumption, 75_LVBus0622945_production, 75_LVBus0622946_production, 75_LVBus0622947_production, 75_LVBus0622948_production, 75_LVBus0622949_production, 75_LVBus0622950_production, 75_LVBus0622952_production, 75_LVBus0622953_production, 75_LVBus0622954_production, 75_LVBus0622955_production, 75_LVBus0622956_production, 75_LVBus0622957_production, 75_LVBus0622959_production, 75_LVBus0622960_production, 75_LVBus0622961_production, 75_LVBus0622965_consumption, 75_LVBus0622965_production, 75_LVBus0622966_production, 75_LVBus0622967_production, 75_LVBus0622969_production, 75_LVBus0622971_production, 75_LVBus0622972_production, 75_LVBus0622973_production, 75_LVBus0622974_consumption, 75_LVBus0622974_production, 75_LVBus0622976_production, 75_LVBus0622977_production, 75_LVBus0622978_production, 75_LVBus0622979_production, 75_LVBus0622980_production, 75_LVBus0622982_production, 75_LVBus0622984_production, 75_LVBus0622985_production, 75_LVBus0622986_production, 75_LVBus0622987_production, 75_LVBus0622988_consumption, 75_LVBus0622988_production, 75_LVBus0622990_production, 75_LVBus0622991_production, 75_LVBus0622992_production, 75_LVBus0622994_production, 75_LVBus0622996_production, 75_LVBus0622997_production, 75_LVBus0622998_production, 75_LVBus0622999_consumption, 75_LVBus0622999_production, 75_LVBus0623000_consumption, 75_LVBus0623000_production, 75_LVBus0623001_consumption, 75_LVBus0623001_production, 75_LVBus0623002_production, 75_LVBus0623003_production, 75_LVBus0623004_production, 75_LVBus0623006_consumption, 75_LVBus0623006_production, 75_LVBus0623007_production, 75_LVBus0623008_production, 75_LVBus0623009_production, 75_LVBus0623010_production, 75_LVBus0623011_consumption, 75_LVBus0623011_production, 75_LVBus0623012_production, 75_LVBus0623013_production, 75_LVBus0623015_production, 75_LVBus0623016_production, 75_LVBus0623018_production, 75_LVBus0623020_production, 75_LVBus0623022_consumption, 75_LVBus0623022_production, 75_LVBus0623024_production, 75_LVBus0623026_production, 75_LVBus0623027_production, 75_LVBus0623028_consumption, 75_LVBus0623028_production, 75_LVBus0623029_production, 75_LVBus0623030_production, 75_LVBus0623032_production, 75_LVBus0623034_production, 75_LVBus0623035_consumption, 75_LVBus0623035_production, 75_LVBus0623036_production, 75_LVBus0623037_production, 75_LVBus0623038_consumption, 75_LVBus0623038_production, 75_LVBus0623041_production, 75_LVBus0623042_production, 75_LVBus0623043_production, 75_LVBus0623045_production, 75_LVBus0623046_production, 75_LVBus0623047_production, 75_LVBus0623048_production, 75_LVBus0623049_production, 75_LVBus0623050_production, 75_LVBus0623051_production, 75_LVBus0623052_production, 75_LVBus0623053_production, 75_LVBus0623054_production, 75_LVBus0623056_production, 75_LVBus0623057_production, 75_LVBus0623058_production, 75_LVBus0623060_production, 75_LVBus0623061_production, 75_LVBus0623062_production, 75_LVBus0623063_production, 75_LVBus0623064_production, 75_LVBus0623065_consumption, 75_LVBus0623065_production, 75_LVBus0623066_production, 75_LVBus0623067_consumption, 75_LVBus0623067_production, 75_LVBus0623069_production, 75_LVBus0623070_production, 75_LVBus0623072_consumption, 75_LVBus0623072_production, 75_LVBus0623074_production, 75_LVBus0623076_production, 75_LVBus0623077_production, 75_LVBus0623078_production, 75_LVBus0623080_production, 75_LVBus0623081_production, 75_LVBus0623083_consumption, 75_LVBus0623083_production, 75_LVBus0623084_production, 75_LVBus0623085_production, 75_LVBus0623086_consumption, 75_LVBus0623086_production, 75_LVBus0623087_production, 75_LVBus0623088_production, 75_LVBus0623089_consumption, 75_LVBus0623089_production, 75_LVBus0623091_production, 75_LVBus0623092_consumption, 75_LVBus0623092_production, 75_LVBus0623094_production, 75_LVBus0623096_production, 75_LVBus0623098_consumption, 75_LVBus0623098_production, 75_LVBus0623099_production, 75_LVBus0623100_production, 75_LVBus0623101_production, 75_LVBus0623103_production, 75_LVBus0623105_production, 75_LVBus0623106_production, 75_LVBus0623107_production, 75_LVBus0623108_production, 75_LVBus0623109_production, 75_LVBus0623111_production, 75_LVBus0623112_production, 75_LVBus0623113_production, 75_LVBus0623114_production, 75_LVBus0623115_production, 75_LVBus0623117_consumption, 75_LVBus0623117_production, 75_LVBus0623119_production, 75_LVBus0623120_consumption, 75_LVBus0623120_production, 75_LVBus0623121_production, 75_LVBus0623122_production, 75_LVBus0623123_production, 75_LVBus0623124_production, 75_LVBus0623126_production, 75_LVBus0623127_consumption, 75_LVBus0623127_production, 75_LVBus0623128_production, 75_LVBus0623129_production, 75_LVBus0623130_production, 75_LVBus0623131_production, 75_LVBus0623132_production, 75_LVBus0623133_production, 75_LVBus0623134_production, 75_LVBus0623135_production, 75_LVBus0623136_production, 75_LVBus0623137_production, 75_LVBus0623138_consumption, 75_LVBus0623138_production, 75_LVBus0623139_production, 75_LVBus0623141_consumption, 75_LVBus0623141_production, 75_LVBus0623142_consumption, 75_LVBus0623142_production, 75_LVBus0623143_consumption, 75_LVBus0623143_production, 75_LVBus0623144_production, 75_LVBus0623145_production, 75_LVBus0623146_production, 75_LVBus0623147_production, 75_LVBus0623151_production, 75_LVBus0623152_consumption, 75_LVBus0623152_production, 75_LVBus0623153_consumption, 75_LVBus0623153_production, 75_LVBus0623154_production, 75_LVBus0623155_production, 75_LVBus0623156_production, 75_LVBus0623157_production, 75_LVBus0623158_production, 75_LVBus0623159_production, 75_LVBus0623160_production, 75_LVBus0623161_production, 75_LVBus0623162_consumption, 75_LVBus0623162_production, 75_LVBus1942502_production, 75_LVBus1957909_production, 75_LVBus1979932_production, 75_LVBus1983180_consumption, 75_LVBus1983180_production, 75_LVBus1989360_consumption, 75_LVBus1989360_production, 75_LVBus2007252_production, 75_LVBus2007253_production, 75_LVBus2007254_consumption, 75_LVBus2007254_production, 75_LVBus2007255_production, 75_LVBus2007256_production, 75_LVBus2007257_production, 75_LVBus2007258_production, 75_LVBus2007259_consumption, 75_LVBus2007259_production, 75_LVBus2007260_production, 75_LVBus2007261_production, 75_LVBus2007262_production, 75_LVBus2007263_production, 75_LVBus2007264_production, 75_LVBus2007265_production, 75_LVBus2007266_production, 75_LVBus2007267_production, 75_LVBus2007268_consumption, 75_LVBus2007268_production, 75_LVBus2007269_production, 75_LVBus2007270_consumption, 75_LVBus2007270_production, 75_LVBus2007271_production, 75_LVBus2007272_production, 75_LVBus2007273_production, 75_LVBus2007274_production, 75_LVBus2007275_production, 75_LVBus2007276_consumption, 75_LVBus2007276_production, 75_LVBus2007277_production, 75_LVBus2007278_consumption, 75_LVBus2007278_production, 75_LVBus2007279_production, 75_MVLV012820_consumption, 75_MVLV012820_production, 75_MVLV025892_consumption, 75_MVLV025892_production, 75_MVLV027379_consumption, 75_MVLV027379_production, 75_MVLV056442_consumption, 75_MVLV056442_production, 75_MVLV064447_consumption, 75_MVLV064447_production, 75_MVLV077747_consumption, 75_MVLV077747_production, 75_MVLV088718_consumption, 75_MVLV088718_production, 75_MVLV094221_consumption, 75_MVLV094221_production, 75_MVLV149747_consumption, 75_MVLV149747_production, 75_MVLV159485_consumption, 75_MVLV159485_production.

