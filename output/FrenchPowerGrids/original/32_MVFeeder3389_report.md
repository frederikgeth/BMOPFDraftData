# BMOPF Network Summary: 32_MVFeeder3389

**Generated:** 2026-10-01 23:34:09  
**Findings:** 0 errors · 5 warnings · 262 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 385 |  |
| line | 369 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 700 | 2.465 MW, 739.6 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 15 |  |
| switch | 0 |  |
| transformer | 15 | Dyn11×15 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 22 | 21 | 4 | 0 |
| LV_236V | 236.0 V | 363 | 348 | 696 | 0 |

**Transformer transitions:**

- `32_MVLV72874_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV07415_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV40911_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV54732_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV74319_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV54733_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV37746_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV25906_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV49157_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV05781_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV72328_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV46060_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV25625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV54730_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV25904_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 8 |
| Degree-1 buses | 134 |
| Tree depth (max hops) | 25 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 385 | 1 | 384 | 0 | 0 | 0 |
| Tier LV_236V | 363 | 15 | 348 | 0 | 0 | 0 |
| Tier MV_11.8kV | 22 | 1 | 21 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 15; skipped invalid branches: 0.

Galvanic zones: 16; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_MVBus44388 | MV_11.8kV | 22 | 0 | 0 | 15 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1518 declared bus terminals; 1455 mapped line/closed-switch conductor edges; 63 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 62400.0 | 3.017 | 2100 |
| q_nom | 0.0 | 18700.0 | 3.017 | 2100 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.39 | 576.0 | 1.13 | 369 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 440000.0 | 0.304 | 15 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 432 of 700 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633957_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633664_consumption' has phase imbalance of 36.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633592_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633850_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633676_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633838_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633605_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633926_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633900_consumption' has phase imbalance of 41.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633723_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633899_consumption' has phase imbalance of 259.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633642_consumption' has phase imbalance of 190.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633557_consumption' has phase imbalance of 229.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633729_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633553_consumption' has phase imbalance of 234.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633556_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633732_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633569_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633647_consumption' has phase imbalance of 171.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633765_consumption' has phase imbalance of 232.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633909_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633718_consumption' has phase imbalance of 244.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633580_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633750_consumption' has phase imbalance of 78.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633780_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633560_consumption' has phase imbalance of 253.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633884_consumption' has phase imbalance of 64.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633648_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633704_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633805_consumption' has phase imbalance of 65.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633771_consumption' has phase imbalance of 220.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633596_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633603_consumption' has phase imbalance of 119.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633814_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633564_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633769_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633563_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633687_consumption' has phase imbalance of 91.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633551_consumption' has phase imbalance of 250.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633731_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633804_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633940_consumption' has phase imbalance of 282.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633651_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633590_consumption' has phase imbalance of 195.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633583_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633821_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633694_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633681_consumption' has phase imbalance of 44.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633845_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633568_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633925_consumption' has phase imbalance of 119.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633615_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633600_consumption' has phase imbalance of 117.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633626_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633567_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633646_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633808_consumption' has phase imbalance of 123.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633743_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633870_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633784_consumption' has phase imbalance of 144.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633726_consumption' has phase imbalance of 191.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633764_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633869_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633919_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633943_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633918_consumption' has phase imbalance of 83.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633817_consumption' has phase imbalance of 235.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633650_consumption' has phase imbalance of 127.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1135374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633861_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633739_consumption' has phase imbalance of 267.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633928_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633823_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633599_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633827_consumption' has phase imbalance of 207.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633923_consumption' has phase imbalance of 118.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633825_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633588_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633730_consumption' has phase imbalance of 106.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633793_consumption' has phase imbalance of 186.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633763_consumption' has phase imbalance of 135.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633698_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633690_consumption' has phase imbalance of 52.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633610_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633830_consumption' has phase imbalance of 247.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633785_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633934_consumption' has phase imbalance of 57.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633575_consumption' has phase imbalance of 172.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633612_consumption' has phase imbalance of 255.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633570_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633717_consumption' has phase imbalance of 38.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633806_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633585_consumption' has phase imbalance of 70.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633815_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633714_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633942_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633738_consumption' has phase imbalance of 281.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633924_consumption' has phase imbalance of 139.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633916_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633851_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633554_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633576_consumption' has phase imbalance of 276.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633941_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633565_consumption' has phase imbalance of 265.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633710_consumption' has phase imbalance of 174.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633719_consumption' has phase imbalance of 52.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633665_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633852_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633894_consumption' has phase imbalance of 41.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633713_consumption' has phase imbalance of 278.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633574_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633945_consumption' has phase imbalance of 180.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633963_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633621_consumption' has phase imbalance of 277.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633839_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633921_consumption' has phase imbalance of 147.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633854_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633917_consumption' has phase imbalance of 197.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633601_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633807_consumption' has phase imbalance of 227.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633874_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633908_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633777_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633637_consumption' has phase imbalance of 20.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633837_consumption' has phase imbalance of 268.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633587_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633645_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633552_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633677_consumption' has phase imbalance of 37.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633699_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633877_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633857_consumption' has phase imbalance of 57.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633649_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633613_consumption' has phase imbalance of 117.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633602_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633961_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633700_consumption' has phase imbalance of 82.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633628_consumption' has phase imbalance of 75.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633946_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633573_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633652_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633593_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633794_consumption' has phase imbalance of 58.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1135375_consumption' has phase imbalance of 104.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633775_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633616_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633644_consumption' has phase imbalance of 212.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633773_consumption' has phase imbalance of 240.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633819_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633818_consumption' has phase imbalance of 128.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633757_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633875_consumption' has phase imbalance of 189.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633630_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633853_consumption' has phase imbalance of 37.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633906_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633624_consumption' has phase imbalance of 254.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633761_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633632_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633774_consumption' has phase imbalance of 72.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633722_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633653_consumption' has phase imbalance of 249.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633786_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633586_consumption' has phase imbalance of 131.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633912_consumption' has phase imbalance of 223.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633801_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633618_consumption' has phase imbalance of 251.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633627_consumption' has phase imbalance of 55.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633595_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633625_consumption' has phase imbalance of 115.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633922_consumption' has phase imbalance of 125.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633878_consumption' has phase imbalance of 43.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633582_consumption' has phase imbalance of 253.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633787_consumption' has phase imbalance of 85.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633581_consumption' has phase imbalance of 245.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633952_consumption' has phase imbalance of 94.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633654_consumption' has phase imbalance of 148.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633638_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633711_consumption' has phase imbalance of 244.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633707_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633669_consumption' has phase imbalance of 24.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633882_consumption' has phase imbalance of 122.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633617_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633834_consumption' has phase imbalance of 23.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633907_consumption' has phase imbalance of 115.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633949_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633846_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633802_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633944_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633811_consumption' has phase imbalance of 77.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633591_consumption' has phase imbalance of 99.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633727_consumption' has phase imbalance of 90.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633611_consumption' has phase imbalance of 164.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633733_consumption' has phase imbalance of 22.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633873_consumption' has phase imbalance of 78.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633783_consumption' has phase imbalance of 119.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633844_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633622_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633584_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633724_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633824_consumption' has phase imbalance of 143.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633705_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus633555_consumption' has phase imbalance of 57.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 700 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus633656' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.465 MW |
| Total load Q | 739.6 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV72874_Transformer | 275.0 kVA | 55.5% |
| 32_MVLV07415_Transformer | 440.0 kVA | 39.0% |
| 32_MVLV40911_Transformer | 275.0 kVA | 36.9% |
| 32_MVLV54732_Transformer | 275.0 kVA | 50.9% |
| 32_MVLV74319_Transformer | 440.0 kVA | 56.3% |
| 32_MVLV54733_Transformer | 275.0 kVA | 40.4% |
| 32_MVLV37746_Transformer | 275.0 kVA | 65.1% |
| 32_MVLV25906_Transformer | 275.0 kVA | 71.7% |
| 32_MVLV49157_Transformer | 275.0 kVA | 62.2% |
| 32_MVLV05781_Transformer | 440.0 kVA | 69.8% |
| 32_MVLV72328_Transformer | 440.0 kVA | 52.1% |
| 32_MVLV46060_Transformer | 440.0 kVA | 42.2% |
| 32_MVLV25625_Transformer | 176.0 kVA | 55.2% |
| 32_MVLV54730_Transformer | 275.0 kVA | 82.8% |
| 32_MVLV25904_Transformer | 176.0 kVA | 31.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.47 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 385 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 385 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 22 |
| LV_236V | 4-wire | 363 / 363 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 363 |
| Neutral branches | 348 |
| Grounding points | 15 |
| Neutral sections | 15 |
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
| 11.78 kV | 22 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 16 |
| Islands without voltage reference | 0 |
| Line impedance spread | 176.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 363 / 22 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 433 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 433 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1135374_production, 32_LVBus1135375_production, 32_LVBus1135376_consumption, 32_LVBus1135376_production, 32_LVBus633550_production, 32_LVBus633551_production, 32_LVBus633552_production, 32_LVBus633553_production, 32_LVBus633554_production, 32_LVBus633555_production, 32_LVBus633556_production, 32_LVBus633557_production, 32_LVBus633558_production, 32_LVBus633560_production, 32_LVBus633562_consumption, 32_LVBus633562_production, 32_LVBus633563_production, 32_LVBus633564_production, 32_LVBus633565_production, 32_LVBus633566_consumption, 32_LVBus633566_production, 32_LVBus633567_production, 32_LVBus633568_production, 32_LVBus633569_production, 32_LVBus633570_production, 32_LVBus633571_consumption, 32_LVBus633571_production, 32_LVBus633572_production, 32_LVBus633573_production, 32_LVBus633574_production, 32_LVBus633575_production, 32_LVBus633576_production, 32_LVBus633577_production, 32_LVBus633579_production, 32_LVBus633580_production, 32_LVBus633581_production, 32_LVBus633582_production, 32_LVBus633583_production, 32_LVBus633584_production, 32_LVBus633585_production, 32_LVBus633586_production, 32_LVBus633587_production, 32_LVBus633588_production, 32_LVBus633590_production, 32_LVBus633591_production, 32_LVBus633592_production, 32_LVBus633593_production, 32_LVBus633594_production, 32_LVBus633595_production, 32_LVBus633596_production, 32_LVBus633597_production, 32_LVBus633598_consumption, 32_LVBus633598_production, 32_LVBus633599_production, 32_LVBus633600_production, 32_LVBus633601_production, 32_LVBus633602_production, 32_LVBus633603_production, 32_LVBus633605_production, 32_LVBus633607_production, 32_LVBus633608_production, 32_LVBus633609_consumption, 32_LVBus633609_production, 32_LVBus633610_production, 32_LVBus633611_production, 32_LVBus633612_production, 32_LVBus633613_production, 32_LVBus633615_production, 32_LVBus633616_production, 32_LVBus633617_production, 32_LVBus633618_production, 32_LVBus633619_consumption, 32_LVBus633619_production, 32_LVBus633621_production, 32_LVBus633622_production, 32_LVBus633623_production, 32_LVBus633624_production, 32_LVBus633625_production, 32_LVBus633626_production, 32_LVBus633627_production, 32_LVBus633628_production, 32_LVBus633629_production, 32_LVBus633630_production, 32_LVBus633632_production, 32_LVBus633634_consumption, 32_LVBus633634_production, 32_LVBus633635_production, 32_LVBus633636_consumption, 32_LVBus633636_production, 32_LVBus633637_production, 32_LVBus633638_production, 32_LVBus633639_consumption, 32_LVBus633639_production, 32_LVBus633640_production, 32_LVBus633642_production, 32_LVBus633643_production, 32_LVBus633644_production, 32_LVBus633645_production, 32_LVBus633646_production, 32_LVBus633647_production, 32_LVBus633648_production, 32_LVBus633649_production, 32_LVBus633650_production, 32_LVBus633651_production, 32_LVBus633652_production, 32_LVBus633653_production, 32_LVBus633654_production, 32_LVBus633656_production, 32_LVBus633658_production, 32_LVBus633659_production, 32_LVBus633660_production, 32_LVBus633662_consumption, 32_LVBus633662_production, 32_LVBus633663_consumption, 32_LVBus633663_production, 32_LVBus633664_production, 32_LVBus633665_production, 32_LVBus633667_consumption, 32_LVBus633667_production, 32_LVBus633668_consumption, 32_LVBus633668_production, 32_LVBus633669_production, 32_LVBus633670_consumption, 32_LVBus633670_production, 32_LVBus633672_consumption, 32_LVBus633672_production, 32_LVBus633674_consumption, 32_LVBus633674_production, 32_LVBus633675_consumption, 32_LVBus633675_production, 32_LVBus633676_production, 32_LVBus633677_production, 32_LVBus633679_consumption, 32_LVBus633679_production, 32_LVBus633680_consumption, 32_LVBus633680_production, 32_LVBus633681_production, 32_LVBus633683_consumption, 32_LVBus633683_production, 32_LVBus633684_consumption, 32_LVBus633684_production, 32_LVBus633685_consumption, 32_LVBus633685_production, 32_LVBus633686_consumption, 32_LVBus633686_production, 32_LVBus633687_production, 32_LVBus633688_consumption, 32_LVBus633688_production, 32_LVBus633689_consumption, 32_LVBus633689_production, 32_LVBus633690_production, 32_LVBus633691_consumption, 32_LVBus633691_production, 32_LVBus633692_consumption, 32_LVBus633692_production, 32_LVBus633694_production, 32_LVBus633696_production, 32_LVBus633698_production, 32_LVBus633699_production, 32_LVBus633700_production, 32_LVBus633701_production, 32_LVBus633702_production, 32_LVBus633703_production, 32_LVBus633704_production, 32_LVBus633705_production, 32_LVBus633706_production, 32_LVBus633707_production, 32_LVBus633708_production, 32_LVBus633709_production, 32_LVBus633710_production, 32_LVBus633711_production, 32_LVBus633712_production, 32_LVBus633713_production, 32_LVBus633714_production, 32_LVBus633716_consumption, 32_LVBus633716_production, 32_LVBus633717_production, 32_LVBus633718_production, 32_LVBus633719_production, 32_LVBus633721_consumption, 32_LVBus633721_production, 32_LVBus633722_production, 32_LVBus633723_production, 32_LVBus633724_production, 32_LVBus633725_production, 32_LVBus633726_production, 32_LVBus633727_production, 32_LVBus633728_production, 32_LVBus633729_production, 32_LVBus633730_production, 32_LVBus633731_production, 32_LVBus633732_production, 32_LVBus633733_production, 32_LVBus633735_consumption, 32_LVBus633735_production, 32_LVBus633736_consumption, 32_LVBus633736_production, 32_LVBus633738_production, 32_LVBus633739_production, 32_LVBus633740_production, 32_LVBus633742_production, 32_LVBus633743_production, 32_LVBus633744_consumption, 32_LVBus633744_production, 32_LVBus633746_production, 32_LVBus633748_production, 32_LVBus633750_production, 32_LVBus633751_production, 32_LVBus633752_production, 32_LVBus633753_production, 32_LVBus633754_production, 32_LVBus633756_production, 32_LVBus633757_production, 32_LVBus633759_consumption, 32_LVBus633759_production, 32_LVBus633760_consumption, 32_LVBus633760_production, 32_LVBus633761_production, 32_LVBus633762_consumption, 32_LVBus633762_production, 32_LVBus633763_production, 32_LVBus633764_production, 32_LVBus633765_production, 32_LVBus633767_consumption, 32_LVBus633767_production, 32_LVBus633768_production, 32_LVBus633769_production, 32_LVBus633770_production, 32_LVBus633771_production, 32_LVBus633773_production, 32_LVBus633774_production, 32_LVBus633775_production, 32_LVBus633777_production, 32_LVBus633778_consumption, 32_LVBus633778_production, 32_LVBus633779_production, 32_LVBus633780_production, 32_LVBus633781_consumption, 32_LVBus633781_production, 32_LVBus633782_consumption, 32_LVBus633782_production, 32_LVBus633783_production, 32_LVBus633784_production, 32_LVBus633785_production, 32_LVBus633786_production, 32_LVBus633787_production, 32_LVBus633789_consumption, 32_LVBus633789_production, 32_LVBus633791_production, 32_LVBus633793_production, 32_LVBus633794_production, 32_LVBus633795_consumption, 32_LVBus633795_production, 32_LVBus633797_production, 32_LVBus633799_consumption, 32_LVBus633799_production, 32_LVBus633800_production, 32_LVBus633801_production, 32_LVBus633802_production, 32_LVBus633804_production, 32_LVBus633805_production, 32_LVBus633806_production, 32_LVBus633807_production, 32_LVBus633808_production, 32_LVBus633810_consumption, 32_LVBus633810_production, 32_LVBus633811_production, 32_LVBus633813_consumption, 32_LVBus633813_production, 32_LVBus633814_production, 32_LVBus633815_production, 32_LVBus633816_production, 32_LVBus633817_production, 32_LVBus633818_production, 32_LVBus633819_production, 32_LVBus633821_production, 32_LVBus633823_production, 32_LVBus633824_production, 32_LVBus633825_production, 32_LVBus633826_production, 32_LVBus633827_production, 32_LVBus633828_production, 32_LVBus633830_production, 32_LVBus633831_consumption, 32_LVBus633831_production, 32_LVBus633832_production, 32_LVBus633833_consumption, 32_LVBus633833_production, 32_LVBus633834_production, 32_LVBus633836_production, 32_LVBus633837_production, 32_LVBus633838_production, 32_LVBus633839_production, 32_LVBus633840_production, 32_LVBus633842_consumption, 32_LVBus633842_production, 32_LVBus633843_production, 32_LVBus633844_production, 32_LVBus633845_production, 32_LVBus633846_production, 32_LVBus633848_consumption, 32_LVBus633848_production, 32_LVBus633849_production, 32_LVBus633850_production, 32_LVBus633851_production, 32_LVBus633852_production, 32_LVBus633853_production, 32_LVBus633854_production, 32_LVBus633856_production, 32_LVBus633857_production, 32_LVBus633858_consumption, 32_LVBus633858_production, 32_LVBus633860_consumption, 32_LVBus633860_production, 32_LVBus633861_production, 32_LVBus633863_consumption, 32_LVBus633863_production, 32_LVBus633865_consumption, 32_LVBus633865_production, 32_LVBus633866_production, 32_LVBus633867_consumption, 32_LVBus633867_production, 32_LVBus633868_consumption, 32_LVBus633868_production, 32_LVBus633869_production, 32_LVBus633870_production, 32_LVBus633871_production, 32_LVBus633873_production, 32_LVBus633874_production, 32_LVBus633875_production, 32_LVBus633876_production, 32_LVBus633877_production, 32_LVBus633878_production, 32_LVBus633882_production, 32_LVBus633883_consumption, 32_LVBus633883_production, 32_LVBus633884_production, 32_LVBus633886_consumption, 32_LVBus633886_production, 32_LVBus633887_consumption, 32_LVBus633887_production, 32_LVBus633888_consumption, 32_LVBus633888_production, 32_LVBus633889_consumption, 32_LVBus633889_production, 32_LVBus633890_consumption, 32_LVBus633890_production, 32_LVBus633891_consumption, 32_LVBus633891_production, 32_LVBus633893_production, 32_LVBus633894_production, 32_LVBus633895_production, 32_LVBus633896_consumption, 32_LVBus633896_production, 32_LVBus633897_production, 32_LVBus633899_production, 32_LVBus633900_production, 32_LVBus633906_production, 32_LVBus633907_production, 32_LVBus633908_production, 32_LVBus633909_production, 32_LVBus633910_consumption, 32_LVBus633910_production, 32_LVBus633911_consumption, 32_LVBus633911_production, 32_LVBus633912_production, 32_LVBus633913_production, 32_LVBus633914_production, 32_LVBus633915_production, 32_LVBus633916_production, 32_LVBus633917_production, 32_LVBus633918_production, 32_LVBus633919_production, 32_LVBus633921_production, 32_LVBus633922_production, 32_LVBus633923_production, 32_LVBus633924_production, 32_LVBus633925_production, 32_LVBus633926_production, 32_LVBus633927_production, 32_LVBus633928_production, 32_LVBus633930_production, 32_LVBus633931_consumption, 32_LVBus633931_production, 32_LVBus633933_consumption, 32_LVBus633933_production, 32_LVBus633934_production, 32_LVBus633935_production, 32_LVBus633937_consumption, 32_LVBus633937_production, 32_LVBus633939_consumption, 32_LVBus633939_production, 32_LVBus633940_production, 32_LVBus633941_production, 32_LVBus633942_production, 32_LVBus633943_production, 32_LVBus633944_production, 32_LVBus633945_production, 32_LVBus633946_production, 32_LVBus633948_consumption, 32_LVBus633948_production, 32_LVBus633949_production, 32_LVBus633950_consumption, 32_LVBus633950_production, 32_LVBus633951_consumption, 32_LVBus633951_production, 32_LVBus633952_production, 32_LVBus633953_consumption, 32_LVBus633953_production, 32_LVBus633954_consumption, 32_LVBus633954_production, 32_LVBus633955_consumption, 32_LVBus633955_production, 32_LVBus633956_consumption, 32_LVBus633956_production, 32_LVBus633957_production, 32_LVBus633958_consumption, 32_LVBus633958_production, 32_LVBus633959_consumption, 32_LVBus633959_production, 32_LVBus633960_consumption, 32_LVBus633960_production, 32_LVBus633961_production, 32_LVBus633962_consumption, 32_LVBus633962_production, 32_LVBus633963_production, 32_LVBus633964_consumption, 32_LVBus633964_production, 32_LVBus633965_production, 32_MVLV00683_consumption, 32_MVLV00683_production, 32_MVLV09343_consumption, 32_MVLV09343_production.

## 9. Data Quality Summary

**Total findings:** 267 (0 errors, 5 warnings, 262 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  432 of 700 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.47 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  433 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633957_consumption`  
  Load '32_LVBus633957_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633664_consumption`  
  Load '32_LVBus633664_consumption' has phase imbalance of 36.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633623_consumption`  
  Load '32_LVBus633623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633592_consumption`  
  Load '32_LVBus633592_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633728_consumption`  
  Load '32_LVBus633728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633850_consumption`  
  Load '32_LVBus633850_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633676_consumption`  
  Load '32_LVBus633676_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633742_consumption`  
  Load '32_LVBus633742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633838_consumption`  
  Load '32_LVBus633838_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633605_consumption`  
  Load '32_LVBus633605_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633926_consumption`  
  Load '32_LVBus633926_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633900_consumption`  
  Load '32_LVBus633900_consumption' has phase imbalance of 41.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633723_consumption`  
  Load '32_LVBus633723_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633899_consumption`  
  Load '32_LVBus633899_consumption' has phase imbalance of 259.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633642_consumption`  
  Load '32_LVBus633642_consumption' has phase imbalance of 190.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633557_consumption`  
  Load '32_LVBus633557_consumption' has phase imbalance of 229.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633729_consumption`  
  Load '32_LVBus633729_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633849_consumption`  
  Load '32_LVBus633849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633701_consumption`  
  Load '32_LVBus633701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633553_consumption`  
  Load '32_LVBus633553_consumption' has phase imbalance of 234.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633556_consumption`  
  Load '32_LVBus633556_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633732_consumption`  
  Load '32_LVBus633732_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633569_consumption`  
  Load '32_LVBus633569_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633647_consumption`  
  Load '32_LVBus633647_consumption' has phase imbalance of 171.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633754_consumption`  
  Load '32_LVBus633754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633765_consumption`  
  Load '32_LVBus633765_consumption' has phase imbalance of 232.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633909_consumption`  
  Load '32_LVBus633909_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633718_consumption`  
  Load '32_LVBus633718_consumption' has phase imbalance of 244.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633580_consumption`  
  Load '32_LVBus633580_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633750_consumption`  
  Load '32_LVBus633750_consumption' has phase imbalance of 78.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633780_consumption`  
  Load '32_LVBus633780_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633597_consumption`  
  Load '32_LVBus633597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633560_consumption`  
  Load '32_LVBus633560_consumption' has phase imbalance of 253.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633884_consumption`  
  Load '32_LVBus633884_consumption' has phase imbalance of 64.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633648_consumption`  
  Load '32_LVBus633648_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633704_consumption`  
  Load '32_LVBus633704_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633805_consumption`  
  Load '32_LVBus633805_consumption' has phase imbalance of 65.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633771_consumption`  
  Load '32_LVBus633771_consumption' has phase imbalance of 220.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633596_consumption`  
  Load '32_LVBus633596_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633603_consumption`  
  Load '32_LVBus633603_consumption' has phase imbalance of 119.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633814_consumption`  
  Load '32_LVBus633814_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633564_consumption`  
  Load '32_LVBus633564_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633769_consumption`  
  Load '32_LVBus633769_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633563_consumption`  
  Load '32_LVBus633563_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633725_consumption`  
  Load '32_LVBus633725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633687_consumption`  
  Load '32_LVBus633687_consumption' has phase imbalance of 91.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633551_consumption`  
  Load '32_LVBus633551_consumption' has phase imbalance of 250.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633731_consumption`  
  Load '32_LVBus633731_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633804_consumption`  
  Load '32_LVBus633804_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633635_consumption`  
  Load '32_LVBus633635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633940_consumption`  
  Load '32_LVBus633940_consumption' has phase imbalance of 282.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633866_consumption`  
  Load '32_LVBus633866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633651_consumption`  
  Load '32_LVBus633651_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633590_consumption`  
  Load '32_LVBus633590_consumption' has phase imbalance of 195.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633583_consumption`  
  Load '32_LVBus633583_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633821_consumption`  
  Load '32_LVBus633821_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633876_consumption`  
  Load '32_LVBus633876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633694_consumption`  
  Load '32_LVBus633694_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633681_consumption`  
  Load '32_LVBus633681_consumption' has phase imbalance of 44.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633845_consumption`  
  Load '32_LVBus633845_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633568_consumption`  
  Load '32_LVBus633568_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633925_consumption`  
  Load '32_LVBus633925_consumption' has phase imbalance of 119.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633615_consumption`  
  Load '32_LVBus633615_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633893_consumption`  
  Load '32_LVBus633893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633600_consumption`  
  Load '32_LVBus633600_consumption' has phase imbalance of 117.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633626_consumption`  
  Load '32_LVBus633626_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633567_consumption`  
  Load '32_LVBus633567_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633770_consumption`  
  Load '32_LVBus633770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633646_consumption`  
  Load '32_LVBus633646_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633808_consumption`  
  Load '32_LVBus633808_consumption' has phase imbalance of 123.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633743_consumption`  
  Load '32_LVBus633743_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633870_consumption`  
  Load '32_LVBus633870_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633784_consumption`  
  Load '32_LVBus633784_consumption' has phase imbalance of 144.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633779_consumption`  
  Load '32_LVBus633779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633913_consumption`  
  Load '32_LVBus633913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633726_consumption`  
  Load '32_LVBus633726_consumption' has phase imbalance of 191.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633764_consumption`  
  Load '32_LVBus633764_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633869_consumption`  
  Load '32_LVBus633869_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633840_consumption`  
  Load '32_LVBus633840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633919_consumption`  
  Load '32_LVBus633919_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633643_consumption`  
  Load '32_LVBus633643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633943_consumption`  
  Load '32_LVBus633943_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633791_consumption`  
  Load '32_LVBus633791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633918_consumption`  
  Load '32_LVBus633918_consumption' has phase imbalance of 83.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633817_consumption`  
  Load '32_LVBus633817_consumption' has phase imbalance of 235.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633650_consumption`  
  Load '32_LVBus633650_consumption' has phase imbalance of 127.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633703_consumption`  
  Load '32_LVBus633703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1135374_consumption`  
  Load '32_LVBus1135374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633861_consumption`  
  Load '32_LVBus633861_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633739_consumption`  
  Load '32_LVBus633739_consumption' has phase imbalance of 267.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633712_consumption`  
  Load '32_LVBus633712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633928_consumption`  
  Load '32_LVBus633928_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633823_consumption`  
  Load '32_LVBus633823_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633599_consumption`  
  Load '32_LVBus633599_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633572_consumption`  
  Load '32_LVBus633572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633827_consumption`  
  Load '32_LVBus633827_consumption' has phase imbalance of 207.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633923_consumption`  
  Load '32_LVBus633923_consumption' has phase imbalance of 118.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633825_consumption`  
  Load '32_LVBus633825_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633588_consumption`  
  Load '32_LVBus633588_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633730_consumption`  
  Load '32_LVBus633730_consumption' has phase imbalance of 106.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633793_consumption`  
  Load '32_LVBus633793_consumption' has phase imbalance of 186.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633763_consumption`  
  Load '32_LVBus633763_consumption' has phase imbalance of 135.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633698_consumption`  
  Load '32_LVBus633698_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633579_consumption`  
  Load '32_LVBus633579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633690_consumption`  
  Load '32_LVBus633690_consumption' has phase imbalance of 52.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633610_consumption`  
  Load '32_LVBus633610_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633751_consumption`  
  Load '32_LVBus633751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633830_consumption`  
  Load '32_LVBus633830_consumption' has phase imbalance of 247.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633785_consumption`  
  Load '32_LVBus633785_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633934_consumption`  
  Load '32_LVBus633934_consumption' has phase imbalance of 57.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633708_consumption`  
  Load '32_LVBus633708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633575_consumption`  
  Load '32_LVBus633575_consumption' has phase imbalance of 172.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633702_consumption`  
  Load '32_LVBus633702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633612_consumption`  
  Load '32_LVBus633612_consumption' has phase imbalance of 255.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633570_consumption`  
  Load '32_LVBus633570_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633717_consumption`  
  Load '32_LVBus633717_consumption' has phase imbalance of 38.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633806_consumption`  
  Load '32_LVBus633806_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633709_consumption`  
  Load '32_LVBus633709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633585_consumption`  
  Load '32_LVBus633585_consumption' has phase imbalance of 70.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633696_consumption`  
  Load '32_LVBus633696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633828_consumption`  
  Load '32_LVBus633828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633815_consumption`  
  Load '32_LVBus633815_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633714_consumption`  
  Load '32_LVBus633714_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633942_consumption`  
  Load '32_LVBus633942_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633738_consumption`  
  Load '32_LVBus633738_consumption' has phase imbalance of 281.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633924_consumption`  
  Load '32_LVBus633924_consumption' has phase imbalance of 139.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633916_consumption`  
  Load '32_LVBus633916_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633851_consumption`  
  Load '32_LVBus633851_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633594_consumption`  
  Load '32_LVBus633594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633554_consumption`  
  Load '32_LVBus633554_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633576_consumption`  
  Load '32_LVBus633576_consumption' has phase imbalance of 276.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633941_consumption`  
  Load '32_LVBus633941_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633565_consumption`  
  Load '32_LVBus633565_consumption' has phase imbalance of 265.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633710_consumption`  
  Load '32_LVBus633710_consumption' has phase imbalance of 174.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633719_consumption`  
  Load '32_LVBus633719_consumption' has phase imbalance of 52.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633665_consumption`  
  Load '32_LVBus633665_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633852_consumption`  
  Load '32_LVBus633852_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633894_consumption`  
  Load '32_LVBus633894_consumption' has phase imbalance of 41.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633713_consumption`  
  Load '32_LVBus633713_consumption' has phase imbalance of 278.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633574_consumption`  
  Load '32_LVBus633574_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633945_consumption`  
  Load '32_LVBus633945_consumption' has phase imbalance of 180.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633963_consumption`  
  Load '32_LVBus633963_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633621_consumption`  
  Load '32_LVBus633621_consumption' has phase imbalance of 277.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633839_consumption`  
  Load '32_LVBus633839_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633921_consumption`  
  Load '32_LVBus633921_consumption' has phase imbalance of 147.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633854_consumption`  
  Load '32_LVBus633854_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633917_consumption`  
  Load '32_LVBus633917_consumption' has phase imbalance of 197.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633601_consumption`  
  Load '32_LVBus633601_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633843_consumption`  
  Load '32_LVBus633843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633807_consumption`  
  Load '32_LVBus633807_consumption' has phase imbalance of 227.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633874_consumption`  
  Load '32_LVBus633874_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633908_consumption`  
  Load '32_LVBus633908_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633777_consumption`  
  Load '32_LVBus633777_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633637_consumption`  
  Load '32_LVBus633637_consumption' has phase imbalance of 20.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633837_consumption`  
  Load '32_LVBus633837_consumption' has phase imbalance of 268.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633915_consumption`  
  Load '32_LVBus633915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633587_consumption`  
  Load '32_LVBus633587_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633645_consumption`  
  Load '32_LVBus633645_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633552_consumption`  
  Load '32_LVBus633552_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633677_consumption`  
  Load '32_LVBus633677_consumption' has phase imbalance of 37.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633699_consumption`  
  Load '32_LVBus633699_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633800_consumption`  
  Load '32_LVBus633800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633877_consumption`  
  Load '32_LVBus633877_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633857_consumption`  
  Load '32_LVBus633857_consumption' has phase imbalance of 57.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633649_consumption`  
  Load '32_LVBus633649_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633613_consumption`  
  Load '32_LVBus633613_consumption' has phase imbalance of 117.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633914_consumption`  
  Load '32_LVBus633914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633602_consumption`  
  Load '32_LVBus633602_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633961_consumption`  
  Load '32_LVBus633961_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633700_consumption`  
  Load '32_LVBus633700_consumption' has phase imbalance of 82.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633628_consumption`  
  Load '32_LVBus633628_consumption' has phase imbalance of 75.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633946_consumption`  
  Load '32_LVBus633946_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633573_consumption`  
  Load '32_LVBus633573_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633652_consumption`  
  Load '32_LVBus633652_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633593_consumption`  
  Load '32_LVBus633593_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633794_consumption`  
  Load '32_LVBus633794_consumption' has phase imbalance of 58.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1135375_consumption`  
  Load '32_LVBus1135375_consumption' has phase imbalance of 104.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633775_consumption`  
  Load '32_LVBus633775_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633616_consumption`  
  Load '32_LVBus633616_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633644_consumption`  
  Load '32_LVBus633644_consumption' has phase imbalance of 212.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633773_consumption`  
  Load '32_LVBus633773_consumption' has phase imbalance of 240.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633819_consumption`  
  Load '32_LVBus633819_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633818_consumption`  
  Load '32_LVBus633818_consumption' has phase imbalance of 128.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633757_consumption`  
  Load '32_LVBus633757_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633706_consumption`  
  Load '32_LVBus633706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633875_consumption`  
  Load '32_LVBus633875_consumption' has phase imbalance of 189.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633630_consumption`  
  Load '32_LVBus633630_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633853_consumption`  
  Load '32_LVBus633853_consumption' has phase imbalance of 37.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633906_consumption`  
  Load '32_LVBus633906_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633624_consumption`  
  Load '32_LVBus633624_consumption' has phase imbalance of 254.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633826_consumption`  
  Load '32_LVBus633826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633761_consumption`  
  Load '32_LVBus633761_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633608_consumption`  
  Load '32_LVBus633608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633632_consumption`  
  Load '32_LVBus633632_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633816_consumption`  
  Load '32_LVBus633816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633774_consumption`  
  Load '32_LVBus633774_consumption' has phase imbalance of 72.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633640_consumption`  
  Load '32_LVBus633640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633722_consumption`  
  Load '32_LVBus633722_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633653_consumption`  
  Load '32_LVBus633653_consumption' has phase imbalance of 249.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633786_consumption`  
  Load '32_LVBus633786_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633586_consumption`  
  Load '32_LVBus633586_consumption' has phase imbalance of 131.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633912_consumption`  
  Load '32_LVBus633912_consumption' has phase imbalance of 223.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633801_consumption`  
  Load '32_LVBus633801_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633836_consumption`  
  Load '32_LVBus633836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633618_consumption`  
  Load '32_LVBus633618_consumption' has phase imbalance of 251.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633550_consumption`  
  Load '32_LVBus633550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633627_consumption`  
  Load '32_LVBus633627_consumption' has phase imbalance of 55.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633595_consumption`  
  Load '32_LVBus633595_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633625_consumption`  
  Load '32_LVBus633625_consumption' has phase imbalance of 115.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633922_consumption`  
  Load '32_LVBus633922_consumption' has phase imbalance of 125.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633878_consumption`  
  Load '32_LVBus633878_consumption' has phase imbalance of 43.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633582_consumption`  
  Load '32_LVBus633582_consumption' has phase imbalance of 253.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633787_consumption`  
  Load '32_LVBus633787_consumption' has phase imbalance of 85.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633577_consumption`  
  Load '32_LVBus633577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633581_consumption`  
  Load '32_LVBus633581_consumption' has phase imbalance of 245.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633752_consumption`  
  Load '32_LVBus633752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633952_consumption`  
  Load '32_LVBus633952_consumption' has phase imbalance of 94.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633654_consumption`  
  Load '32_LVBus633654_consumption' has phase imbalance of 148.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633638_consumption`  
  Load '32_LVBus633638_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633711_consumption`  
  Load '32_LVBus633711_consumption' has phase imbalance of 244.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633707_consumption`  
  Load '32_LVBus633707_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633669_consumption`  
  Load '32_LVBus633669_consumption' has phase imbalance of 24.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633882_consumption`  
  Load '32_LVBus633882_consumption' has phase imbalance of 122.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633617_consumption`  
  Load '32_LVBus633617_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633834_consumption`  
  Load '32_LVBus633834_consumption' has phase imbalance of 23.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633907_consumption`  
  Load '32_LVBus633907_consumption' has phase imbalance of 115.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633949_consumption`  
  Load '32_LVBus633949_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633846_consumption`  
  Load '32_LVBus633846_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633802_consumption`  
  Load '32_LVBus633802_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633944_consumption`  
  Load '32_LVBus633944_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633811_consumption`  
  Load '32_LVBus633811_consumption' has phase imbalance of 77.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633591_consumption`  
  Load '32_LVBus633591_consumption' has phase imbalance of 99.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633727_consumption`  
  Load '32_LVBus633727_consumption' has phase imbalance of 90.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633611_consumption`  
  Load '32_LVBus633611_consumption' has phase imbalance of 164.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633733_consumption`  
  Load '32_LVBus633733_consumption' has phase imbalance of 22.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633873_consumption`  
  Load '32_LVBus633873_consumption' has phase imbalance of 78.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633783_consumption`  
  Load '32_LVBus633783_consumption' has phase imbalance of 119.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633844_consumption`  
  Load '32_LVBus633844_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633622_consumption`  
  Load '32_LVBus633622_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633584_consumption`  
  Load '32_LVBus633584_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633724_consumption`  
  Load '32_LVBus633724_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633607_consumption`  
  Load '32_LVBus633607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633824_consumption`  
  Load '32_LVBus633824_consumption' has phase imbalance of 143.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633629_consumption`  
  Load '32_LVBus633629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633705_consumption`  
  Load '32_LVBus633705_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus633555_consumption`  
  Load '32_LVBus633555_consumption' has phase imbalance of 57.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 700 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus633656' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  385 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  142 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus1135374_consumption, 32_LVBus633550_consumption, 32_LVBus633551_consumption, 32_LVBus633553_consumption, 32_LVBus633554_consumption, 32_LVBus633557_consumption, 32_LVBus633560_consumption, 32_LVBus633563_consumption, 32_LVBus633564_consumption, 32_LVBus633565_consumption, 32_LVBus633567_consumption, 32_LVBus633570_consumption, 32_LVBus633572_consumption, 32_LVBus633574_consumption, 32_LVBus633575_consumption, 32_LVBus633576_consumption, 32_LVBus633577_consumption, 32_LVBus633579_consumption, 32_LVBus633580_consumption, 32_LVBus633581_consumption, 32_LVBus633582_consumption, 32_LVBus633584_consumption, 32_LVBus633587_consumption, 32_LVBus633590_consumption, 32_LVBus633593_consumption, 32_LVBus633594_consumption, 32_LVBus633595_consumption, 32_LVBus633597_consumption, 32_LVBus633599_consumption, 32_LVBus633607_consumption, 32_LVBus633608_consumption, 32_LVBus633612_consumption, 32_LVBus633615_consumption, 32_LVBus633616_consumption, 32_LVBus633618_consumption, 32_LVBus633621_consumption, 32_LVBus633622_consumption, 32_LVBus633623_consumption, 32_LVBus633624_consumption, 32_LVBus633629_consumption, 32_LVBus633630_consumption, 32_LVBus633635_consumption, 32_LVBus633638_consumption, 32_LVBus633640_consumption, 32_LVBus633642_consumption, 32_LVBus633643_consumption, 32_LVBus633645_consumption, 32_LVBus633647_consumption, 32_LVBus633648_consumption, 32_LVBus633649_consumption, 32_LVBus633651_consumption, 32_LVBus633653_consumption, 32_LVBus633665_consumption, 32_LVBus633694_consumption, 32_LVBus633696_consumption, 32_LVBus633698_consumption, 32_LVBus633699_consumption, 32_LVBus633701_consumption, 32_LVBus633702_consumption, 32_LVBus633703_consumption, 32_LVBus633704_consumption, 32_LVBus633705_consumption, 32_LVBus633706_consumption, 32_LVBus633707_consumption, 32_LVBus633708_consumption, 32_LVBus633709_consumption, 32_LVBus633710_consumption, 32_LVBus633711_consumption, 32_LVBus633712_consumption, 32_LVBus633718_consumption, 32_LVBus633724_consumption, 32_LVBus633725_consumption, 32_LVBus633726_consumption, 32_LVBus633728_consumption, 32_LVBus633729_consumption, 32_LVBus633731_consumption, 32_LVBus633732_consumption, 32_LVBus633738_consumption, 32_LVBus633739_consumption, 32_LVBus633742_consumption, 32_LVBus633751_consumption, 32_LVBus633752_consumption, 32_LVBus633754_consumption, 32_LVBus633761_consumption, 32_LVBus633764_consumption, 32_LVBus633765_consumption, 32_LVBus633770_consumption, 32_LVBus633771_consumption, 32_LVBus633773_consumption, 32_LVBus633775_consumption, 32_LVBus633777_consumption, 32_LVBus633779_consumption, 32_LVBus633780_consumption, 32_LVBus633785_consumption, 32_LVBus633791_consumption, 32_LVBus633793_consumption, 32_LVBus633800_consumption, 32_LVBus633801_consumption, 32_LVBus633804_consumption, 32_LVBus633807_consumption, 32_LVBus633814_consumption, 32_LVBus633815_consumption, 32_LVBus633816_consumption, 32_LVBus633817_consumption, 32_LVBus633819_consumption, 32_LVBus633823_consumption, 32_LVBus633825_consumption, 32_LVBus633826_consumption, 32_LVBus633827_consumption, 32_LVBus633828_consumption, 32_LVBus633830_consumption, 32_LVBus633836_consumption, 32_LVBus633837_consumption, 32_LVBus633838_consumption, 32_LVBus633839_consumption, 32_LVBus633840_consumption, 32_LVBus633843_consumption, 32_LVBus633845_consumption, 32_LVBus633846_consumption, 32_LVBus633849_consumption, 32_LVBus633850_consumption, 32_LVBus633851_consumption, 32_LVBus633866_consumption, 32_LVBus633869_consumption, 32_LVBus633870_consumption, 32_LVBus633874_consumption, 32_LVBus633875_consumption, 32_LVBus633876_consumption, 32_LVBus633893_consumption, 32_LVBus633899_consumption, 32_LVBus633906_consumption, 32_LVBus633909_consumption, 32_LVBus633912_consumption, 32_LVBus633913_consumption, 32_LVBus633914_consumption, 32_LVBus633915_consumption, 32_LVBus633916_consumption, 32_LVBus633917_consumption, 32_LVBus633940_consumption, 32_LVBus633941_consumption, 32_LVBus633943_consumption, 32_LVBus633957_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  350 group(s) of loads (700 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (2 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  433 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1135374_production, 32_LVBus1135375_production, 32_LVBus1135376_consumption, 32_LVBus1135376_production, 32_LVBus633550_production, 32_LVBus633551_production, 32_LVBus633552_production, 32_LVBus633553_production, 32_LVBus633554_production, 32_LVBus633555_production, 32_LVBus633556_production, 32_LVBus633557_production, 32_LVBus633558_production, 32_LVBus633560_production, 32_LVBus633562_consumption, 32_LVBus633562_production, 32_LVBus633563_production, 32_LVBus633564_production, 32_LVBus633565_production, 32_LVBus633566_consumption, 32_LVBus633566_production, 32_LVBus633567_production, 32_LVBus633568_production, 32_LVBus633569_production, 32_LVBus633570_production, 32_LVBus633571_consumption, 32_LVBus633571_production, 32_LVBus633572_production, 32_LVBus633573_production, 32_LVBus633574_production, 32_LVBus633575_production, 32_LVBus633576_production, 32_LVBus633577_production, 32_LVBus633579_production, 32_LVBus633580_production, 32_LVBus633581_production, 32_LVBus633582_production, 32_LVBus633583_production, 32_LVBus633584_production, 32_LVBus633585_production, 32_LVBus633586_production, 32_LVBus633587_production, 32_LVBus633588_production, 32_LVBus633590_production, 32_LVBus633591_production, 32_LVBus633592_production, 32_LVBus633593_production, 32_LVBus633594_production, 32_LVBus633595_production, 32_LVBus633596_production, 32_LVBus633597_production, 32_LVBus633598_consumption, 32_LVBus633598_production, 32_LVBus633599_production, 32_LVBus633600_production, 32_LVBus633601_production, 32_LVBus633602_production, 32_LVBus633603_production, 32_LVBus633605_production, 32_LVBus633607_production, 32_LVBus633608_production, 32_LVBus633609_consumption, 32_LVBus633609_production, 32_LVBus633610_production, 32_LVBus633611_production, 32_LVBus633612_production, 32_LVBus633613_production, 32_LVBus633615_production, 32_LVBus633616_production, 32_LVBus633617_production, 32_LVBus633618_production, 32_LVBus633619_consumption, 32_LVBus633619_production, 32_LVBus633621_production, 32_LVBus633622_production, 32_LVBus633623_production, 32_LVBus633624_production, 32_LVBus633625_production, 32_LVBus633626_production, 32_LVBus633627_production, 32_LVBus633628_production, 32_LVBus633629_production, 32_LVBus633630_production, 32_LVBus633632_production, 32_LVBus633634_consumption, 32_LVBus633634_production, 32_LVBus633635_production, 32_LVBus633636_consumption, 32_LVBus633636_production, 32_LVBus633637_production, 32_LVBus633638_production, 32_LVBus633639_consumption, 32_LVBus633639_production, 32_LVBus633640_production, 32_LVBus633642_production, 32_LVBus633643_production, 32_LVBus633644_production, 32_LVBus633645_production, 32_LVBus633646_production, 32_LVBus633647_production, 32_LVBus633648_production, 32_LVBus633649_production, 32_LVBus633650_production, 32_LVBus633651_production, 32_LVBus633652_production, 32_LVBus633653_production, 32_LVBus633654_production, 32_LVBus633656_production, 32_LVBus633658_production, 32_LVBus633659_production, 32_LVBus633660_production, 32_LVBus633662_consumption, 32_LVBus633662_production, 32_LVBus633663_consumption, 32_LVBus633663_production, 32_LVBus633664_production, 32_LVBus633665_production, 32_LVBus633667_consumption, 32_LVBus633667_production, 32_LVBus633668_consumption, 32_LVBus633668_production, 32_LVBus633669_production, 32_LVBus633670_consumption, 32_LVBus633670_production, 32_LVBus633672_consumption, 32_LVBus633672_production, 32_LVBus633674_consumption, 32_LVBus633674_production, 32_LVBus633675_consumption, 32_LVBus633675_production, 32_LVBus633676_production, 32_LVBus633677_production, 32_LVBus633679_consumption, 32_LVBus633679_production, 32_LVBus633680_consumption, 32_LVBus633680_production, 32_LVBus633681_production, 32_LVBus633683_consumption, 32_LVBus633683_production, 32_LVBus633684_consumption, 32_LVBus633684_production, 32_LVBus633685_consumption, 32_LVBus633685_production, 32_LVBus633686_consumption, 32_LVBus633686_production, 32_LVBus633687_production, 32_LVBus633688_consumption, 32_LVBus633688_production, 32_LVBus633689_consumption, 32_LVBus633689_production, 32_LVBus633690_production, 32_LVBus633691_consumption, 32_LVBus633691_production, 32_LVBus633692_consumption, 32_LVBus633692_production, 32_LVBus633694_production, 32_LVBus633696_production, 32_LVBus633698_production, 32_LVBus633699_production, 32_LVBus633700_production, 32_LVBus633701_production, 32_LVBus633702_production, 32_LVBus633703_production, 32_LVBus633704_production, 32_LVBus633705_production, 32_LVBus633706_production, 32_LVBus633707_production, 32_LVBus633708_production, 32_LVBus633709_production, 32_LVBus633710_production, 32_LVBus633711_production, 32_LVBus633712_production, 32_LVBus633713_production, 32_LVBus633714_production, 32_LVBus633716_consumption, 32_LVBus633716_production, 32_LVBus633717_production, 32_LVBus633718_production, 32_LVBus633719_production, 32_LVBus633721_consumption, 32_LVBus633721_production, 32_LVBus633722_production, 32_LVBus633723_production, 32_LVBus633724_production, 32_LVBus633725_production, 32_LVBus633726_production, 32_LVBus633727_production, 32_LVBus633728_production, 32_LVBus633729_production, 32_LVBus633730_production, 32_LVBus633731_production, 32_LVBus633732_production, 32_LVBus633733_production, 32_LVBus633735_consumption, 32_LVBus633735_production, 32_LVBus633736_consumption, 32_LVBus633736_production, 32_LVBus633738_production, 32_LVBus633739_production, 32_LVBus633740_production, 32_LVBus633742_production, 32_LVBus633743_production, 32_LVBus633744_consumption, 32_LVBus633744_production, 32_LVBus633746_production, 32_LVBus633748_production, 32_LVBus633750_production, 32_LVBus633751_production, 32_LVBus633752_production, 32_LVBus633753_production, 32_LVBus633754_production, 32_LVBus633756_production, 32_LVBus633757_production, 32_LVBus633759_consumption, 32_LVBus633759_production, 32_LVBus633760_consumption, 32_LVBus633760_production, 32_LVBus633761_production, 32_LVBus633762_consumption, 32_LVBus633762_production, 32_LVBus633763_production, 32_LVBus633764_production, 32_LVBus633765_production, 32_LVBus633767_consumption, 32_LVBus633767_production, 32_LVBus633768_production, 32_LVBus633769_production, 32_LVBus633770_production, 32_LVBus633771_production, 32_LVBus633773_production, 32_LVBus633774_production, 32_LVBus633775_production, 32_LVBus633777_production, 32_LVBus633778_consumption, 32_LVBus633778_production, 32_LVBus633779_production, 32_LVBus633780_production, 32_LVBus633781_consumption, 32_LVBus633781_production, 32_LVBus633782_consumption, 32_LVBus633782_production, 32_LVBus633783_production, 32_LVBus633784_production, 32_LVBus633785_production, 32_LVBus633786_production, 32_LVBus633787_production, 32_LVBus633789_consumption, 32_LVBus633789_production, 32_LVBus633791_production, 32_LVBus633793_production, 32_LVBus633794_production, 32_LVBus633795_consumption, 32_LVBus633795_production, 32_LVBus633797_production, 32_LVBus633799_consumption, 32_LVBus633799_production, 32_LVBus633800_production, 32_LVBus633801_production, 32_LVBus633802_production, 32_LVBus633804_production, 32_LVBus633805_production, 32_LVBus633806_production, 32_LVBus633807_production, 32_LVBus633808_production, 32_LVBus633810_consumption, 32_LVBus633810_production, 32_LVBus633811_production, 32_LVBus633813_consumption, 32_LVBus633813_production, 32_LVBus633814_production, 32_LVBus633815_production, 32_LVBus633816_production, 32_LVBus633817_production, 32_LVBus633818_production, 32_LVBus633819_production, 32_LVBus633821_production, 32_LVBus633823_production, 32_LVBus633824_production, 32_LVBus633825_production, 32_LVBus633826_production, 32_LVBus633827_production, 32_LVBus633828_production, 32_LVBus633830_production, 32_LVBus633831_consumption, 32_LVBus633831_production, 32_LVBus633832_production, 32_LVBus633833_consumption, 32_LVBus633833_production, 32_LVBus633834_production, 32_LVBus633836_production, 32_LVBus633837_production, 32_LVBus633838_production, 32_LVBus633839_production, 32_LVBus633840_production, 32_LVBus633842_consumption, 32_LVBus633842_production, 32_LVBus633843_production, 32_LVBus633844_production, 32_LVBus633845_production, 32_LVBus633846_production, 32_LVBus633848_consumption, 32_LVBus633848_production, 32_LVBus633849_production, 32_LVBus633850_production, 32_LVBus633851_production, 32_LVBus633852_production, 32_LVBus633853_production, 32_LVBus633854_production, 32_LVBus633856_production, 32_LVBus633857_production, 32_LVBus633858_consumption, 32_LVBus633858_production, 32_LVBus633860_consumption, 32_LVBus633860_production, 32_LVBus633861_production, 32_LVBus633863_consumption, 32_LVBus633863_production, 32_LVBus633865_consumption, 32_LVBus633865_production, 32_LVBus633866_production, 32_LVBus633867_consumption, 32_LVBus633867_production, 32_LVBus633868_consumption, 32_LVBus633868_production, 32_LVBus633869_production, 32_LVBus633870_production, 32_LVBus633871_production, 32_LVBus633873_production, 32_LVBus633874_production, 32_LVBus633875_production, 32_LVBus633876_production, 32_LVBus633877_production, 32_LVBus633878_production, 32_LVBus633882_production, 32_LVBus633883_consumption, 32_LVBus633883_production, 32_LVBus633884_production, 32_LVBus633886_consumption, 32_LVBus633886_production, 32_LVBus633887_consumption, 32_LVBus633887_production, 32_LVBus633888_consumption, 32_LVBus633888_production, 32_LVBus633889_consumption, 32_LVBus633889_production, 32_LVBus633890_consumption, 32_LVBus633890_production, 32_LVBus633891_consumption, 32_LVBus633891_production, 32_LVBus633893_production, 32_LVBus633894_production, 32_LVBus633895_production, 32_LVBus633896_consumption, 32_LVBus633896_production, 32_LVBus633897_production, 32_LVBus633899_production, 32_LVBus633900_production, 32_LVBus633906_production, 32_LVBus633907_production, 32_LVBus633908_production, 32_LVBus633909_production, 32_LVBus633910_consumption, 32_LVBus633910_production, 32_LVBus633911_consumption, 32_LVBus633911_production, 32_LVBus633912_production, 32_LVBus633913_production, 32_LVBus633914_production, 32_LVBus633915_production, 32_LVBus633916_production, 32_LVBus633917_production, 32_LVBus633918_production, 32_LVBus633919_production, 32_LVBus633921_production, 32_LVBus633922_production, 32_LVBus633923_production, 32_LVBus633924_production, 32_LVBus633925_production, 32_LVBus633926_production, 32_LVBus633927_production, 32_LVBus633928_production, 32_LVBus633930_production, 32_LVBus633931_consumption, 32_LVBus633931_production, 32_LVBus633933_consumption, 32_LVBus633933_production, 32_LVBus633934_production, 32_LVBus633935_production, 32_LVBus633937_consumption, 32_LVBus633937_production, 32_LVBus633939_consumption, 32_LVBus633939_production, 32_LVBus633940_production, 32_LVBus633941_production, 32_LVBus633942_production, 32_LVBus633943_production, 32_LVBus633944_production, 32_LVBus633945_production, 32_LVBus633946_production, 32_LVBus633948_consumption, 32_LVBus633948_production, 32_LVBus633949_production, 32_LVBus633950_consumption, 32_LVBus633950_production, 32_LVBus633951_consumption, 32_LVBus633951_production, 32_LVBus633952_production, 32_LVBus633953_consumption, 32_LVBus633953_production, 32_LVBus633954_consumption, 32_LVBus633954_production, 32_LVBus633955_consumption, 32_LVBus633955_production, 32_LVBus633956_consumption, 32_LVBus633956_production, 32_LVBus633957_production, 32_LVBus633958_consumption, 32_LVBus633958_production, 32_LVBus633959_consumption, 32_LVBus633959_production, 32_LVBus633960_consumption, 32_LVBus633960_production, 32_LVBus633961_production, 32_LVBus633962_consumption, 32_LVBus633962_production, 32_LVBus633963_production, 32_LVBus633964_consumption, 32_LVBus633964_production, 32_LVBus633965_production, 32_MVLV00683_consumption, 32_MVLV00683_production, 32_MVLV09343_consumption, 32_MVLV09343_production.

