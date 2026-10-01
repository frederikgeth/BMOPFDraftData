# BMOPF Network Summary: 93_MVFeeder0659

**Generated:** 2026-10-01 23:34:46  
**Findings:** 0 errors · 5 warnings · 255 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 12 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 441 |  |
| line | 428 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 820 | 777.91 kW, 233.4 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 12 |  |
| switch | 0 |  |
| transformer | 12 | Dyn11×12 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 23 | 22 | 8 | 0 |
| LV_236V | 236.0 V | 418 | 406 | 812 | 0 |

**Transformer transitions:**

- `93_MVLV51392_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV26902_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV47708_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV22736_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV43787_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV11783_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV31514_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV07194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV62792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV59994_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV73686_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `93_MVLV33782_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 181 |
| Tree depth (max hops) | 45 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 441 | 1 | 440 | 0 | 0 | 0 |
| Tier LV_236V | 418 | 12 | 406 | 0 | 0 | 0 |
| Tier MV_11.8kV | 23 | 1 | 22 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 12; skipped invalid branches: 0.

Galvanic zones: 13; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 93_CASTI | MV_11.8kV | 23 | 0 | 0 | 12 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1741 declared bus terminals; 1690 mapped line/closed-switch conductor edges; 51 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 20000.0 | 4.207 | 2460 |
| q_nom | 0.0 | 5990.0 | 4.207 | 2460 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.88 | 3330.0 | 3.048 | 428 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 2.2e6 | 1.689 | 12 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 559 of 820 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303891_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303838_consumption' has phase imbalance of 256.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303825_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303811_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303940_consumption' has phase imbalance of 116.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303858_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430558_consumption' has phase imbalance of 117.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303768_consumption' has phase imbalance of 95.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303834_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430560_consumption' has phase imbalance of 63.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303933_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430567_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430569_consumption' has phase imbalance of 70.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303667_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430611_consumption' has phase imbalance of 255.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303867_consumption' has phase imbalance of 212.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430633_consumption' has phase imbalance of 63.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303807_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303791_consumption' has phase imbalance of 189.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303877_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303721_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303924_consumption' has phase imbalance of 280.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303864_consumption' has phase imbalance of 215.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430563_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430643_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430631_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303713_consumption' has phase imbalance of 88.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430667_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303965_consumption' has phase imbalance of 277.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430640_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430669_consumption' has phase imbalance of 29.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303938_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430655_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303743_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303755_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303884_consumption' has phase imbalance of 268.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430651_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303889_consumption' has phase imbalance of 281.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430662_consumption' has phase imbalance of 151.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303893_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430622_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303703_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1404118_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303712_consumption' has phase imbalance of 71.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303925_consumption' has phase imbalance of 245.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303966_consumption' has phase imbalance of 216.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430606_consumption' has phase imbalance of 23.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303698_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303970_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303779_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303737_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430590_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303693_consumption' has phase imbalance of 219.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430607_consumption' has phase imbalance of 133.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430628_consumption' has phase imbalance of 191.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430597_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303664_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303704_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303705_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303817_consumption' has phase imbalance of 277.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303697_consumption' has phase imbalance of 281.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303855_consumption' has phase imbalance of 145.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303764_consumption' has phase imbalance of 229.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303723_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303724_consumption' has phase imbalance of 176.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303715_consumption' has phase imbalance of 299.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303950_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303757_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303819_consumption' has phase imbalance of 22.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430604_consumption' has phase imbalance of 101.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303968_consumption' has phase imbalance of 272.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303830_consumption' has phase imbalance of 256.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1351803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430554_consumption' has phase imbalance of 41.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303722_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303862_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303829_consumption' has phase imbalance of 172.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430639_consumption' has phase imbalance of 206.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303874_consumption' has phase imbalance of 288.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303865_consumption' has phase imbalance of 104.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430654_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430559_consumption' has phase imbalance of 133.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303691_consumption' has phase imbalance of 98.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430589_consumption' has phase imbalance of 217.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430636_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303964_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430670_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303860_consumption' has phase imbalance of 220.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303885_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430578_consumption' has phase imbalance of 21.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430668_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303742_consumption' has phase imbalance of 256.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303716_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303852_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430573_consumption' has phase imbalance of 278.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430587_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303868_consumption' has phase imbalance of 36.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303934_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303700_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303773_consumption' has phase imbalance of 72.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303780_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303948_consumption' has phase imbalance of 263.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303863_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1351800_consumption' has phase imbalance of 28.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430575_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303831_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430663_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430593_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303883_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303736_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430656_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430647_consumption' has phase imbalance of 38.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430641_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303881_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303846_consumption' has phase imbalance of 271.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303748_consumption' has phase imbalance of 82.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430556_consumption' has phase imbalance of 83.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303710_consumption' has phase imbalance of 204.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1351802_consumption' has phase imbalance of 194.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430650_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303894_consumption' has phase imbalance of 62.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303850_consumption' has phase imbalance of 57.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430638_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303871_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430592_consumption' has phase imbalance of 122.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430571_consumption' has phase imbalance of 284.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430594_consumption' has phase imbalance of 103.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303959_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430576_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303939_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303882_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303879_consumption' has phase imbalance of 212.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303783_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430596_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303824_consumption' has phase imbalance of 211.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303785_consumption' has phase imbalance of 253.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303818_consumption' has phase imbalance of 196.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303953_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430568_consumption' has phase imbalance of 25.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430642_consumption' has phase imbalance of 78.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430566_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303890_consumption' has phase imbalance of 231.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303750_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303923_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303969_consumption' has phase imbalance of 203.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303683_consumption' has phase imbalance of 125.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1357140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303975_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430574_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430626_consumption' has phase imbalance of 182.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303778_consumption' has phase imbalance of 207.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303816_consumption' has phase imbalance of 283.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430555_consumption' has phase imbalance of 33.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303954_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303741_consumption' has phase imbalance of 95.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303729_consumption' has phase imbalance of 37.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303734_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303754_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303730_consumption' has phase imbalance of 128.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303936_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303878_consumption' has phase imbalance of 222.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430564_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303836_consumption' has phase imbalance of 280.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303921_consumption' has phase imbalance of 228.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430614_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430561_consumption' has phase imbalance of 143.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430570_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430580_consumption' has phase imbalance of 214.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus1430562_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '93_LVBus0303958_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 820 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 777.91 kW |
| Total load Q | 233.4 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 93_MVLV51392_Transformer | 275.0 kVA | 53.2% |
| 93_MVLV26902_Transformer | 2.2 MVA | 7.6% |
| 93_MVLV47708_Transformer | 440.0 kVA | 41.7% |
| 93_MVLV22736_Transformer | 176.0 kVA | 40.0% |
| 93_MVLV43787_Transformer | 110.0 kVA | 0.4% |
| 93_MVLV11783_Transformer | 110.0 kVA | 5.4% |
| 93_MVLV31514_Transformer | 275.0 kVA | 52.3% |
| 93_MVLV07194_Transformer | 110.0 kVA | 9.7% |
| 93_MVLV62792_Transformer | 110.0 kVA | 16.5% |
| 93_MVLV59994_Transformer | 110.0 kVA | 3.6% |
| 93_MVLV73686_Transformer | 176.0 kVA | 29.2% |
| 93_MVLV33782_Transformer | 110.0 kVA | 9.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.78 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '93_LVBus0303720' (LV, 0.24 kV) has an electrical reach of 1.61 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '93_LVBus0303787' (LV, 0.24 kV) has an electrical reach of 1.15 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '93_LVBus0303670' (LV, 0.24 kV) has an electrical reach of 1.27 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 441 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 441 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 12 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 23 |
| LV_236V | 4-wire | 418 / 418 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 418 |
| Neutral branches | 406 |
| Grounding points | 12 |
| Neutral sections | 12 |
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
| 11.78 kV | 23 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 158 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 13 |
| Islands without voltage reference | 0 |
| Line impedance spread | 752.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 418 / 23 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 560 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 560 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0303652_production, 93_LVBus0303653_consumption, 93_LVBus0303653_production, 93_LVBus0303655_consumption, 93_LVBus0303655_production, 93_LVBus0303656_consumption, 93_LVBus0303656_production, 93_LVBus0303657_production, 93_LVBus0303658_consumption, 93_LVBus0303658_production, 93_LVBus0303659_production, 93_LVBus0303660_consumption, 93_LVBus0303660_production, 93_LVBus0303661_production, 93_LVBus0303662_consumption, 93_LVBus0303662_production, 93_LVBus0303663_consumption, 93_LVBus0303663_production, 93_LVBus0303664_production, 93_LVBus0303665_production, 93_LVBus0303666_production, 93_LVBus0303667_production, 93_LVBus0303668_production, 93_LVBus0303670_consumption, 93_LVBus0303670_production, 93_LVBus0303671_consumption, 93_LVBus0303671_production, 93_LVBus0303672_consumption, 93_LVBus0303672_production, 93_LVBus0303673_consumption, 93_LVBus0303673_production, 93_LVBus0303674_consumption, 93_LVBus0303674_production, 93_LVBus0303675_production, 93_LVBus0303677_consumption, 93_LVBus0303677_production, 93_LVBus0303678_consumption, 93_LVBus0303678_production, 93_LVBus0303679_production, 93_LVBus0303680_consumption, 93_LVBus0303680_production, 93_LVBus0303681_consumption, 93_LVBus0303681_production, 93_LVBus0303683_production, 93_LVBus0303684_consumption, 93_LVBus0303684_production, 93_LVBus0303685_consumption, 93_LVBus0303685_production, 93_LVBus0303686_production, 93_LVBus0303690_production, 93_LVBus0303691_production, 93_LVBus0303692_production, 93_LVBus0303693_production, 93_LVBus0303695_consumption, 93_LVBus0303695_production, 93_LVBus0303697_production, 93_LVBus0303698_production, 93_LVBus0303699_consumption, 93_LVBus0303699_production, 93_LVBus0303700_production, 93_LVBus0303701_consumption, 93_LVBus0303701_production, 93_LVBus0303702_consumption, 93_LVBus0303702_production, 93_LVBus0303703_production, 93_LVBus0303704_production, 93_LVBus0303705_production, 93_LVBus0303706_consumption, 93_LVBus0303706_production, 93_LVBus0303707_production, 93_LVBus0303708_consumption, 93_LVBus0303708_production, 93_LVBus0303709_production, 93_LVBus0303710_production, 93_LVBus0303711_consumption, 93_LVBus0303711_production, 93_LVBus0303712_production, 93_LVBus0303713_production, 93_LVBus0303714_consumption, 93_LVBus0303714_production, 93_LVBus0303715_production, 93_LVBus0303716_production, 93_LVBus0303717_consumption, 93_LVBus0303717_production, 93_LVBus0303718_consumption, 93_LVBus0303718_production, 93_LVBus0303720_consumption, 93_LVBus0303720_production, 93_LVBus0303721_production, 93_LVBus0303722_production, 93_LVBus0303723_production, 93_LVBus0303724_production, 93_LVBus0303725_production, 93_LVBus0303726_production, 93_LVBus0303727_consumption, 93_LVBus0303727_production, 93_LVBus0303728_consumption, 93_LVBus0303728_production, 93_LVBus0303729_production, 93_LVBus0303730_production, 93_LVBus0303732_production, 93_LVBus0303733_consumption, 93_LVBus0303733_production, 93_LVBus0303734_production, 93_LVBus0303735_production, 93_LVBus0303736_production, 93_LVBus0303737_production, 93_LVBus0303738_consumption, 93_LVBus0303738_production, 93_LVBus0303739_production, 93_LVBus0303740_production, 93_LVBus0303741_production, 93_LVBus0303742_production, 93_LVBus0303743_production, 93_LVBus0303744_production, 93_LVBus0303746_consumption, 93_LVBus0303746_production, 93_LVBus0303747_consumption, 93_LVBus0303747_production, 93_LVBus0303748_production, 93_LVBus0303749_production, 93_LVBus0303750_production, 93_LVBus0303752_production, 93_LVBus0303753_production, 93_LVBus0303754_production, 93_LVBus0303755_production, 93_LVBus0303756_production, 93_LVBus0303757_production, 93_LVBus0303758_production, 93_LVBus0303759_production, 93_LVBus0303760_consumption, 93_LVBus0303760_production, 93_LVBus0303761_consumption, 93_LVBus0303761_production, 93_LVBus0303763_production, 93_LVBus0303764_production, 93_LVBus0303766_production, 93_LVBus0303767_production, 93_LVBus0303768_production, 93_LVBus0303770_production, 93_LVBus0303771_consumption, 93_LVBus0303771_production, 93_LVBus0303772_production, 93_LVBus0303773_production, 93_LVBus0303774_consumption, 93_LVBus0303774_production, 93_LVBus0303775_production, 93_LVBus0303776_consumption, 93_LVBus0303776_production, 93_LVBus0303777_production, 93_LVBus0303778_production, 93_LVBus0303779_production, 93_LVBus0303780_production, 93_LVBus0303782_consumption, 93_LVBus0303782_production, 93_LVBus0303783_production, 93_LVBus0303784_consumption, 93_LVBus0303784_production, 93_LVBus0303785_production, 93_LVBus0303787_consumption, 93_LVBus0303787_production, 93_LVBus0303788_consumption, 93_LVBus0303788_production, 93_LVBus0303789_consumption, 93_LVBus0303789_production, 93_LVBus0303790_consumption, 93_LVBus0303790_production, 93_LVBus0303791_production, 93_LVBus0303792_consumption, 93_LVBus0303792_production, 93_LVBus0303793_consumption, 93_LVBus0303793_production, 93_LVBus0303794_consumption, 93_LVBus0303794_production, 93_LVBus0303795_consumption, 93_LVBus0303795_production, 93_LVBus0303797_consumption, 93_LVBus0303797_production, 93_LVBus0303799_production, 93_LVBus0303801_consumption, 93_LVBus0303801_production, 93_LVBus0303803_consumption, 93_LVBus0303803_production, 93_LVBus0303804_consumption, 93_LVBus0303804_production, 93_LVBus0303806_consumption, 93_LVBus0303806_production, 93_LVBus0303807_production, 93_LVBus0303808_consumption, 93_LVBus0303808_production, 93_LVBus0303809_consumption, 93_LVBus0303809_production, 93_LVBus0303810_consumption, 93_LVBus0303810_production, 93_LVBus0303811_production, 93_LVBus0303812_production, 93_LVBus0303813_production, 93_LVBus0303814_production, 93_LVBus0303815_production, 93_LVBus0303816_production, 93_LVBus0303817_production, 93_LVBus0303818_production, 93_LVBus0303819_production, 93_LVBus0303820_consumption, 93_LVBus0303820_production, 93_LVBus0303821_consumption, 93_LVBus0303821_production, 93_LVBus0303822_production, 93_LVBus0303823_production, 93_LVBus0303824_production, 93_LVBus0303825_production, 93_LVBus0303827_production, 93_LVBus0303828_production, 93_LVBus0303829_production, 93_LVBus0303830_production, 93_LVBus0303831_production, 93_LVBus0303833_production, 93_LVBus0303834_production, 93_LVBus0303836_production, 93_LVBus0303837_production, 93_LVBus0303838_production, 93_LVBus0303839_production, 93_LVBus0303840_production, 93_LVBus0303841_production, 93_LVBus0303843_consumption, 93_LVBus0303843_production, 93_LVBus0303844_production, 93_LVBus0303845_consumption, 93_LVBus0303845_production, 93_LVBus0303846_production, 93_LVBus0303847_consumption, 93_LVBus0303847_production, 93_LVBus0303848_production, 93_LVBus0303849_consumption, 93_LVBus0303849_production, 93_LVBus0303850_production, 93_LVBus0303851_consumption, 93_LVBus0303851_production, 93_LVBus0303852_production, 93_LVBus0303853_consumption, 93_LVBus0303853_production, 93_LVBus0303854_consumption, 93_LVBus0303854_production, 93_LVBus0303855_production, 93_LVBus0303857_consumption, 93_LVBus0303857_production, 93_LVBus0303858_production, 93_LVBus0303859_consumption, 93_LVBus0303859_production, 93_LVBus0303860_production, 93_LVBus0303861_production, 93_LVBus0303862_production, 93_LVBus0303863_production, 93_LVBus0303864_production, 93_LVBus0303865_production, 93_LVBus0303866_production, 93_LVBus0303867_production, 93_LVBus0303868_production, 93_LVBus0303870_consumption, 93_LVBus0303870_production, 93_LVBus0303871_production, 93_LVBus0303872_consumption, 93_LVBus0303872_production, 93_LVBus0303873_production, 93_LVBus0303874_production, 93_LVBus0303876_consumption, 93_LVBus0303876_production, 93_LVBus0303877_production, 93_LVBus0303878_production, 93_LVBus0303879_production, 93_LVBus0303880_production, 93_LVBus0303881_production, 93_LVBus0303882_production, 93_LVBus0303883_production, 93_LVBus0303884_production, 93_LVBus0303885_production, 93_LVBus0303886_production, 93_LVBus0303887_production, 93_LVBus0303888_consumption, 93_LVBus0303888_production, 93_LVBus0303889_production, 93_LVBus0303890_production, 93_LVBus0303891_production, 93_LVBus0303892_production, 93_LVBus0303893_production, 93_LVBus0303894_production, 93_LVBus0303896_consumption, 93_LVBus0303896_production, 93_LVBus0303899_consumption, 93_LVBus0303899_production, 93_LVBus0303901_consumption, 93_LVBus0303901_production, 93_LVBus0303903_consumption, 93_LVBus0303903_production, 93_LVBus0303904_consumption, 93_LVBus0303904_production, 93_LVBus0303905_production, 93_LVBus0303907_consumption, 93_LVBus0303907_production, 93_LVBus0303909_production, 93_LVBus0303910_production, 93_LVBus0303911_consumption, 93_LVBus0303911_production, 93_LVBus0303912_consumption, 93_LVBus0303912_production, 93_LVBus0303913_production, 93_LVBus0303914_consumption, 93_LVBus0303914_production, 93_LVBus0303915_production, 93_LVBus0303916_consumption, 93_LVBus0303916_production, 93_LVBus0303918_consumption, 93_LVBus0303918_production, 93_LVBus0303920_consumption, 93_LVBus0303920_production, 93_LVBus0303921_production, 93_LVBus0303922_production, 93_LVBus0303923_production, 93_LVBus0303924_production, 93_LVBus0303925_production, 93_LVBus0303926_production, 93_LVBus0303933_production, 93_LVBus0303934_production, 93_LVBus0303935_production, 93_LVBus0303936_production, 93_LVBus0303937_consumption, 93_LVBus0303937_production, 93_LVBus0303938_production, 93_LVBus0303939_production, 93_LVBus0303940_production, 93_LVBus0303941_consumption, 93_LVBus0303941_production, 93_LVBus0303942_production, 93_LVBus0303943_production, 93_LVBus0303945_consumption, 93_LVBus0303945_production, 93_LVBus0303946_production, 93_LVBus0303947_consumption, 93_LVBus0303947_production, 93_LVBus0303948_production, 93_LVBus0303949_consumption, 93_LVBus0303949_production, 93_LVBus0303950_production, 93_LVBus0303951_consumption, 93_LVBus0303951_production, 93_LVBus0303952_consumption, 93_LVBus0303952_production, 93_LVBus0303953_production, 93_LVBus0303954_production, 93_LVBus0303955_consumption, 93_LVBus0303955_production, 93_LVBus0303956_consumption, 93_LVBus0303956_production, 93_LVBus0303957_consumption, 93_LVBus0303957_production, 93_LVBus0303958_production, 93_LVBus0303959_production, 93_LVBus0303960_consumption, 93_LVBus0303960_production, 93_LVBus0303961_production, 93_LVBus0303962_consumption, 93_LVBus0303962_production, 93_LVBus0303963_production, 93_LVBus0303964_production, 93_LVBus0303965_production, 93_LVBus0303966_production, 93_LVBus0303967_consumption, 93_LVBus0303967_production, 93_LVBus0303968_production, 93_LVBus0303969_production, 93_LVBus0303970_production, 93_LVBus0303971_consumption, 93_LVBus0303971_production, 93_LVBus0303972_consumption, 93_LVBus0303972_production, 93_LVBus0303973_consumption, 93_LVBus0303973_production, 93_LVBus0303975_production, 93_LVBus1348827_consumption, 93_LVBus1348827_production, 93_LVBus1351799_consumption, 93_LVBus1351799_production, 93_LVBus1351800_production, 93_LVBus1351801_consumption, 93_LVBus1351801_production, 93_LVBus1351802_production, 93_LVBus1351803_production, 93_LVBus1357139_consumption, 93_LVBus1357139_production, 93_LVBus1357140_production, 93_LVBus1383838_consumption, 93_LVBus1383838_production, 93_LVBus1404118_production, 93_LVBus1404119_consumption, 93_LVBus1404119_production, 93_LVBus1430554_production, 93_LVBus1430555_production, 93_LVBus1430556_production, 93_LVBus1430557_consumption, 93_LVBus1430557_production, 93_LVBus1430558_production, 93_LVBus1430559_production, 93_LVBus1430560_production, 93_LVBus1430561_production, 93_LVBus1430562_production, 93_LVBus1430563_production, 93_LVBus1430564_production, 93_LVBus1430565_consumption, 93_LVBus1430565_production, 93_LVBus1430566_production, 93_LVBus1430567_production, 93_LVBus1430568_production, 93_LVBus1430569_production, 93_LVBus1430570_production, 93_LVBus1430571_production, 93_LVBus1430572_production, 93_LVBus1430573_production, 93_LVBus1430574_production, 93_LVBus1430575_production, 93_LVBus1430576_production, 93_LVBus1430577_consumption, 93_LVBus1430577_production, 93_LVBus1430578_production, 93_LVBus1430579_consumption, 93_LVBus1430579_production, 93_LVBus1430580_production, 93_LVBus1430581_consumption, 93_LVBus1430581_production, 93_LVBus1430582_consumption, 93_LVBus1430582_production, 93_LVBus1430583_consumption, 93_LVBus1430583_production, 93_LVBus1430584_consumption, 93_LVBus1430584_production, 93_LVBus1430585_consumption, 93_LVBus1430585_production, 93_LVBus1430586_production, 93_LVBus1430587_production, 93_LVBus1430588_production, 93_LVBus1430589_production, 93_LVBus1430590_production, 93_LVBus1430591_consumption, 93_LVBus1430591_production, 93_LVBus1430592_production, 93_LVBus1430593_production, 93_LVBus1430594_production, 93_LVBus1430595_production, 93_LVBus1430596_production, 93_LVBus1430597_production, 93_LVBus1430598_production, 93_LVBus1430599_consumption, 93_LVBus1430599_production, 93_LVBus1430600_consumption, 93_LVBus1430600_production, 93_LVBus1430601_consumption, 93_LVBus1430601_production, 93_LVBus1430602_consumption, 93_LVBus1430602_production, 93_LVBus1430603_consumption, 93_LVBus1430603_production, 93_LVBus1430604_production, 93_LVBus1430605_production, 93_LVBus1430606_production, 93_LVBus1430607_production, 93_LVBus1430608_consumption, 93_LVBus1430608_production, 93_LVBus1430609_production, 93_LVBus1430610_production, 93_LVBus1430611_production, 93_LVBus1430612_consumption, 93_LVBus1430612_production, 93_LVBus1430613_consumption, 93_LVBus1430613_production, 93_LVBus1430614_production, 93_LVBus1430615_consumption, 93_LVBus1430615_production, 93_LVBus1430616_consumption, 93_LVBus1430616_production, 93_LVBus1430617_production, 93_LVBus1430618_consumption, 93_LVBus1430618_production, 93_LVBus1430619_consumption, 93_LVBus1430619_production, 93_LVBus1430620_consumption, 93_LVBus1430620_production, 93_LVBus1430621_production, 93_LVBus1430622_production, 93_LVBus1430623_consumption, 93_LVBus1430623_production, 93_LVBus1430624_consumption, 93_LVBus1430624_production, 93_LVBus1430625_consumption, 93_LVBus1430625_production, 93_LVBus1430626_production, 93_LVBus1430627_consumption, 93_LVBus1430627_production, 93_LVBus1430628_production, 93_LVBus1430629_consumption, 93_LVBus1430629_production, 93_LVBus1430630_consumption, 93_LVBus1430630_production, 93_LVBus1430631_production, 93_LVBus1430632_production, 93_LVBus1430633_production, 93_LVBus1430634_production, 93_LVBus1430635_production, 93_LVBus1430636_production, 93_LVBus1430637_consumption, 93_LVBus1430637_production, 93_LVBus1430638_production, 93_LVBus1430639_production, 93_LVBus1430640_production, 93_LVBus1430641_production, 93_LVBus1430642_production, 93_LVBus1430643_production, 93_LVBus1430644_production, 93_LVBus1430645_consumption, 93_LVBus1430645_production, 93_LVBus1430646_consumption, 93_LVBus1430646_production, 93_LVBus1430647_production, 93_LVBus1430648_consumption, 93_LVBus1430648_production, 93_LVBus1430649_production, 93_LVBus1430650_production, 93_LVBus1430651_production, 93_LVBus1430652_production, 93_LVBus1430653_consumption, 93_LVBus1430653_production, 93_LVBus1430654_production, 93_LVBus1430655_production, 93_LVBus1430656_production, 93_LVBus1430657_production, 93_LVBus1430658_consumption, 93_LVBus1430658_production, 93_LVBus1430659_consumption, 93_LVBus1430659_production, 93_LVBus1430660_production, 93_LVBus1430661_consumption, 93_LVBus1430661_production, 93_LVBus1430662_production, 93_LVBus1430663_production, 93_LVBus1430664_consumption, 93_LVBus1430664_production, 93_LVBus1430665_production, 93_LVBus1430666_production, 93_LVBus1430667_production, 93_LVBus1430668_production, 93_LVBus1430669_production, 93_LVBus1430670_production, 93_LVBus1430671_consumption, 93_LVBus1430671_production, 93_MVLV13007_consumption, 93_MVLV13007_production, 93_MVLV28538_consumption, 93_MVLV28538_production, 93_MVLV43313_consumption, 93_MVLV43313_production, 93_MVLV68589_consumption, 93_MVLV68589_production.

## 9. Data Quality Summary

**Total findings:** 260 (0 errors, 5 warnings, 255 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  559 of 820 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.78 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  560 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303891_consumption`  
  Load '93_LVBus0303891_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303838_consumption`  
  Load '93_LVBus0303838_consumption' has phase imbalance of 256.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303825_consumption`  
  Load '93_LVBus0303825_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303811_consumption`  
  Load '93_LVBus0303811_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303940_consumption`  
  Load '93_LVBus0303940_consumption' has phase imbalance of 116.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303858_consumption`  
  Load '93_LVBus0303858_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303812_consumption`  
  Load '93_LVBus0303812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430558_consumption`  
  Load '93_LVBus1430558_consumption' has phase imbalance of 117.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303739_consumption`  
  Load '93_LVBus0303739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303657_consumption`  
  Load '93_LVBus0303657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303768_consumption`  
  Load '93_LVBus0303768_consumption' has phase imbalance of 95.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303848_consumption`  
  Load '93_LVBus0303848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303834_consumption`  
  Load '93_LVBus0303834_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430560_consumption`  
  Load '93_LVBus1430560_consumption' has phase imbalance of 63.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303933_consumption`  
  Load '93_LVBus0303933_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303961_consumption`  
  Load '93_LVBus0303961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430567_consumption`  
  Load '93_LVBus1430567_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430569_consumption`  
  Load '93_LVBus1430569_consumption' has phase imbalance of 70.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303667_consumption`  
  Load '93_LVBus0303667_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303752_consumption`  
  Load '93_LVBus0303752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430611_consumption`  
  Load '93_LVBus1430611_consumption' has phase imbalance of 255.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303867_consumption`  
  Load '93_LVBus0303867_consumption' has phase imbalance of 212.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303666_consumption`  
  Load '93_LVBus0303666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430633_consumption`  
  Load '93_LVBus1430633_consumption' has phase imbalance of 63.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303807_consumption`  
  Load '93_LVBus0303807_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303668_consumption`  
  Load '93_LVBus0303668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303791_consumption`  
  Load '93_LVBus0303791_consumption' has phase imbalance of 189.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303877_consumption`  
  Load '93_LVBus0303877_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303721_consumption`  
  Load '93_LVBus0303721_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303924_consumption`  
  Load '93_LVBus0303924_consumption' has phase imbalance of 280.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303864_consumption`  
  Load '93_LVBus0303864_consumption' has phase imbalance of 215.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430563_consumption`  
  Load '93_LVBus1430563_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430643_consumption`  
  Load '93_LVBus1430643_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303840_consumption`  
  Load '93_LVBus0303840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430605_consumption`  
  Load '93_LVBus1430605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430631_consumption`  
  Load '93_LVBus1430631_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303713_consumption`  
  Load '93_LVBus0303713_consumption' has phase imbalance of 88.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430667_consumption`  
  Load '93_LVBus1430667_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303965_consumption`  
  Load '93_LVBus0303965_consumption' has phase imbalance of 277.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430640_consumption`  
  Load '93_LVBus1430640_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430669_consumption`  
  Load '93_LVBus1430669_consumption' has phase imbalance of 29.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303938_consumption`  
  Load '93_LVBus0303938_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430655_consumption`  
  Load '93_LVBus1430655_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303743_consumption`  
  Load '93_LVBus0303743_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303886_consumption`  
  Load '93_LVBus0303886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303755_consumption`  
  Load '93_LVBus0303755_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303884_consumption`  
  Load '93_LVBus0303884_consumption' has phase imbalance of 268.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430651_consumption`  
  Load '93_LVBus1430651_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303889_consumption`  
  Load '93_LVBus0303889_consumption' has phase imbalance of 281.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430662_consumption`  
  Load '93_LVBus1430662_consumption' has phase imbalance of 151.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303893_consumption`  
  Load '93_LVBus0303893_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430622_consumption`  
  Load '93_LVBus1430622_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303703_consumption`  
  Load '93_LVBus0303703_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1404118_consumption`  
  Load '93_LVBus1404118_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303712_consumption`  
  Load '93_LVBus0303712_consumption' has phase imbalance of 71.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303925_consumption`  
  Load '93_LVBus0303925_consumption' has phase imbalance of 245.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303966_consumption`  
  Load '93_LVBus0303966_consumption' has phase imbalance of 216.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430606_consumption`  
  Load '93_LVBus1430606_consumption' has phase imbalance of 23.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303679_consumption`  
  Load '93_LVBus0303679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303698_consumption`  
  Load '93_LVBus0303698_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303970_consumption`  
  Load '93_LVBus0303970_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303779_consumption`  
  Load '93_LVBus0303779_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303737_consumption`  
  Load '93_LVBus0303737_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430590_consumption`  
  Load '93_LVBus1430590_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303693_consumption`  
  Load '93_LVBus0303693_consumption' has phase imbalance of 219.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303725_consumption`  
  Load '93_LVBus0303725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430607_consumption`  
  Load '93_LVBus1430607_consumption' has phase imbalance of 133.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430628_consumption`  
  Load '93_LVBus1430628_consumption' has phase imbalance of 191.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430597_consumption`  
  Load '93_LVBus1430597_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303664_consumption`  
  Load '93_LVBus0303664_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303704_consumption`  
  Load '93_LVBus0303704_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303705_consumption`  
  Load '93_LVBus0303705_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303726_consumption`  
  Load '93_LVBus0303726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303817_consumption`  
  Load '93_LVBus0303817_consumption' has phase imbalance of 277.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303697_consumption`  
  Load '93_LVBus0303697_consumption' has phase imbalance of 281.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303855_consumption`  
  Load '93_LVBus0303855_consumption' has phase imbalance of 145.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303764_consumption`  
  Load '93_LVBus0303764_consumption' has phase imbalance of 229.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303723_consumption`  
  Load '93_LVBus0303723_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303909_consumption`  
  Load '93_LVBus0303909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303724_consumption`  
  Load '93_LVBus0303724_consumption' has phase imbalance of 176.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303715_consumption`  
  Load '93_LVBus0303715_consumption' has phase imbalance of 299.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430609_consumption`  
  Load '93_LVBus1430609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303922_consumption`  
  Load '93_LVBus0303922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430660_consumption`  
  Load '93_LVBus1430660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303950_consumption`  
  Load '93_LVBus0303950_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303942_consumption`  
  Load '93_LVBus0303942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303757_consumption`  
  Load '93_LVBus0303757_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303744_consumption`  
  Load '93_LVBus0303744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303819_consumption`  
  Load '93_LVBus0303819_consumption' has phase imbalance of 22.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430604_consumption`  
  Load '93_LVBus1430604_consumption' has phase imbalance of 101.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303968_consumption`  
  Load '93_LVBus0303968_consumption' has phase imbalance of 272.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303690_consumption`  
  Load '93_LVBus0303690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303830_consumption`  
  Load '93_LVBus0303830_consumption' has phase imbalance of 256.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303815_consumption`  
  Load '93_LVBus0303815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1351803_consumption`  
  Load '93_LVBus1351803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430554_consumption`  
  Load '93_LVBus1430554_consumption' has phase imbalance of 41.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303887_consumption`  
  Load '93_LVBus0303887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303775_consumption`  
  Load '93_LVBus0303775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303722_consumption`  
  Load '93_LVBus0303722_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303732_consumption`  
  Load '93_LVBus0303732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303675_consumption`  
  Load '93_LVBus0303675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303837_consumption`  
  Load '93_LVBus0303837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303862_consumption`  
  Load '93_LVBus0303862_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303829_consumption`  
  Load '93_LVBus0303829_consumption' has phase imbalance of 172.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430639_consumption`  
  Load '93_LVBus1430639_consumption' has phase imbalance of 206.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303874_consumption`  
  Load '93_LVBus0303874_consumption' has phase imbalance of 288.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303865_consumption`  
  Load '93_LVBus0303865_consumption' has phase imbalance of 104.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430654_consumption`  
  Load '93_LVBus1430654_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430559_consumption`  
  Load '93_LVBus1430559_consumption' has phase imbalance of 133.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303691_consumption`  
  Load '93_LVBus0303691_consumption' has phase imbalance of 98.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303963_consumption`  
  Load '93_LVBus0303963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430589_consumption`  
  Load '93_LVBus1430589_consumption' has phase imbalance of 217.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303692_consumption`  
  Load '93_LVBus0303692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430636_consumption`  
  Load '93_LVBus1430636_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303964_consumption`  
  Load '93_LVBus0303964_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430632_consumption`  
  Load '93_LVBus1430632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303910_consumption`  
  Load '93_LVBus0303910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303873_consumption`  
  Load '93_LVBus0303873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303767_consumption`  
  Load '93_LVBus0303767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430670_consumption`  
  Load '93_LVBus1430670_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303665_consumption`  
  Load '93_LVBus0303665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303860_consumption`  
  Load '93_LVBus0303860_consumption' has phase imbalance of 220.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303885_consumption`  
  Load '93_LVBus0303885_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303943_consumption`  
  Load '93_LVBus0303943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430578_consumption`  
  Load '93_LVBus1430578_consumption' has phase imbalance of 21.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303772_consumption`  
  Load '93_LVBus0303772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430668_consumption`  
  Load '93_LVBus1430668_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303742_consumption`  
  Load '93_LVBus0303742_consumption' has phase imbalance of 256.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303716_consumption`  
  Load '93_LVBus0303716_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303852_consumption`  
  Load '93_LVBus0303852_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430573_consumption`  
  Load '93_LVBus1430573_consumption' has phase imbalance of 278.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430587_consumption`  
  Load '93_LVBus1430587_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303868_consumption`  
  Load '93_LVBus0303868_consumption' has phase imbalance of 36.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303934_consumption`  
  Load '93_LVBus0303934_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303823_consumption`  
  Load '93_LVBus0303823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303700_consumption`  
  Load '93_LVBus0303700_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303773_consumption`  
  Load '93_LVBus0303773_consumption' has phase imbalance of 72.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303780_consumption`  
  Load '93_LVBus0303780_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303948_consumption`  
  Load '93_LVBus0303948_consumption' has phase imbalance of 263.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303863_consumption`  
  Load '93_LVBus0303863_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1351800_consumption`  
  Load '93_LVBus1351800_consumption' has phase imbalance of 28.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303833_consumption`  
  Load '93_LVBus0303833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430575_consumption`  
  Load '93_LVBus1430575_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303831_consumption`  
  Load '93_LVBus0303831_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430663_consumption`  
  Load '93_LVBus1430663_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430593_consumption`  
  Load '93_LVBus1430593_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303883_consumption`  
  Load '93_LVBus0303883_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303736_consumption`  
  Load '93_LVBus0303736_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430656_consumption`  
  Load '93_LVBus1430656_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430647_consumption`  
  Load '93_LVBus1430647_consumption' has phase imbalance of 38.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430641_consumption`  
  Load '93_LVBus1430641_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303881_consumption`  
  Load '93_LVBus0303881_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303846_consumption`  
  Load '93_LVBus0303846_consumption' has phase imbalance of 271.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303748_consumption`  
  Load '93_LVBus0303748_consumption' has phase imbalance of 82.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430556_consumption`  
  Load '93_LVBus1430556_consumption' has phase imbalance of 83.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303710_consumption`  
  Load '93_LVBus0303710_consumption' has phase imbalance of 204.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1351802_consumption`  
  Load '93_LVBus1351802_consumption' has phase imbalance of 194.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303935_consumption`  
  Load '93_LVBus0303935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430650_consumption`  
  Load '93_LVBus1430650_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430635_consumption`  
  Load '93_LVBus1430635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303894_consumption`  
  Load '93_LVBus0303894_consumption' has phase imbalance of 62.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303756_consumption`  
  Load '93_LVBus0303756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430652_consumption`  
  Load '93_LVBus1430652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303850_consumption`  
  Load '93_LVBus0303850_consumption' has phase imbalance of 57.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430621_consumption`  
  Load '93_LVBus1430621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430638_consumption`  
  Load '93_LVBus1430638_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303871_consumption`  
  Load '93_LVBus0303871_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430592_consumption`  
  Load '93_LVBus1430592_consumption' has phase imbalance of 122.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303841_consumption`  
  Load '93_LVBus0303841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303946_consumption`  
  Load '93_LVBus0303946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303866_consumption`  
  Load '93_LVBus0303866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303799_consumption`  
  Load '93_LVBus0303799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430571_consumption`  
  Load '93_LVBus1430571_consumption' has phase imbalance of 284.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303749_consumption`  
  Load '93_LVBus0303749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430594_consumption`  
  Load '93_LVBus1430594_consumption' has phase imbalance of 103.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303959_consumption`  
  Load '93_LVBus0303959_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430576_consumption`  
  Load '93_LVBus1430576_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303939_consumption`  
  Load '93_LVBus0303939_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303882_consumption`  
  Load '93_LVBus0303882_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303879_consumption`  
  Load '93_LVBus0303879_consumption' has phase imbalance of 212.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303783_consumption`  
  Load '93_LVBus0303783_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430596_consumption`  
  Load '93_LVBus1430596_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303824_consumption`  
  Load '93_LVBus0303824_consumption' has phase imbalance of 211.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303735_consumption`  
  Load '93_LVBus0303735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303785_consumption`  
  Load '93_LVBus0303785_consumption' has phase imbalance of 253.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303818_consumption`  
  Load '93_LVBus0303818_consumption' has phase imbalance of 196.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303953_consumption`  
  Load '93_LVBus0303953_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430568_consumption`  
  Load '93_LVBus1430568_consumption' has phase imbalance of 25.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303827_consumption`  
  Load '93_LVBus0303827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430642_consumption`  
  Load '93_LVBus1430642_consumption' has phase imbalance of 78.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430566_consumption`  
  Load '93_LVBus1430566_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303890_consumption`  
  Load '93_LVBus0303890_consumption' has phase imbalance of 231.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303915_consumption`  
  Load '93_LVBus0303915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303750_consumption`  
  Load '93_LVBus0303750_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303926_consumption`  
  Load '93_LVBus0303926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303777_consumption`  
  Load '93_LVBus0303777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303923_consumption`  
  Load '93_LVBus0303923_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303969_consumption`  
  Load '93_LVBus0303969_consumption' has phase imbalance of 203.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303822_consumption`  
  Load '93_LVBus0303822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303683_consumption`  
  Load '93_LVBus0303683_consumption' has phase imbalance of 125.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1357140_consumption`  
  Load '93_LVBus1357140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303913_consumption`  
  Load '93_LVBus0303913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303975_consumption`  
  Load '93_LVBus0303975_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430574_consumption`  
  Load '93_LVBus1430574_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303892_consumption`  
  Load '93_LVBus0303892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430626_consumption`  
  Load '93_LVBus1430626_consumption' has phase imbalance of 182.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303778_consumption`  
  Load '93_LVBus0303778_consumption' has phase imbalance of 207.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303816_consumption`  
  Load '93_LVBus0303816_consumption' has phase imbalance of 283.2%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430555_consumption`  
  Load '93_LVBus1430555_consumption' has phase imbalance of 33.1%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303709_consumption`  
  Load '93_LVBus0303709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303954_consumption`  
  Load '93_LVBus0303954_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303659_consumption`  
  Load '93_LVBus0303659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303741_consumption`  
  Load '93_LVBus0303741_consumption' has phase imbalance of 95.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303729_consumption`  
  Load '93_LVBus0303729_consumption' has phase imbalance of 37.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303734_consumption`  
  Load '93_LVBus0303734_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303754_consumption`  
  Load '93_LVBus0303754_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303828_consumption`  
  Load '93_LVBus0303828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303730_consumption`  
  Load '93_LVBus0303730_consumption' has phase imbalance of 128.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303936_consumption`  
  Load '93_LVBus0303936_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430572_consumption`  
  Load '93_LVBus1430572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303878_consumption`  
  Load '93_LVBus0303878_consumption' has phase imbalance of 222.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430564_consumption`  
  Load '93_LVBus1430564_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303661_consumption`  
  Load '93_LVBus0303661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303839_consumption`  
  Load '93_LVBus0303839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303836_consumption`  
  Load '93_LVBus0303836_consumption' has phase imbalance of 280.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303921_consumption`  
  Load '93_LVBus0303921_consumption' has phase imbalance of 228.4%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430614_consumption`  
  Load '93_LVBus1430614_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430561_consumption`  
  Load '93_LVBus1430561_consumption' has phase imbalance of 143.6%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303753_consumption`  
  Load '93_LVBus0303753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303763_consumption`  
  Load '93_LVBus0303763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303861_consumption`  
  Load '93_LVBus0303861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430666_consumption`  
  Load '93_LVBus1430666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430570_consumption`  
  Load '93_LVBus1430570_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430580_consumption`  
  Load '93_LVBus1430580_consumption' has phase imbalance of 214.5%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303652_consumption`  
  Load '93_LVBus0303652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus1430562_consumption`  
  Load '93_LVBus1430562_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `93_LVBus0303958_consumption`  
  Load '93_LVBus0303958_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 820 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '93_LVBus0303720' (LV, 0.24 kV) has an electrical reach of 1.61 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '93_LVBus0303787' (LV, 0.24 kV) has an electrical reach of 1.15 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '93_LVBus0303670' (LV, 0.24 kV) has an electrical reach of 1.27 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  441 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  164 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 93_LVBus0303652_consumption, 93_LVBus0303657_consumption, 93_LVBus0303659_consumption, 93_LVBus0303661_consumption, 93_LVBus0303664_consumption, 93_LVBus0303665_consumption, 93_LVBus0303666_consumption, 93_LVBus0303667_consumption, 93_LVBus0303668_consumption, 93_LVBus0303675_consumption, 93_LVBus0303679_consumption, 93_LVBus0303690_consumption, 93_LVBus0303692_consumption, 93_LVBus0303693_consumption, 93_LVBus0303697_consumption, 93_LVBus0303698_consumption, 93_LVBus0303700_consumption, 93_LVBus0303704_consumption, 93_LVBus0303709_consumption, 93_LVBus0303710_consumption, 93_LVBus0303715_consumption, 93_LVBus0303716_consumption, 93_LVBus0303721_consumption, 93_LVBus0303723_consumption, 93_LVBus0303724_consumption, 93_LVBus0303725_consumption, 93_LVBus0303726_consumption, 93_LVBus0303732_consumption, 93_LVBus0303734_consumption, 93_LVBus0303735_consumption, 93_LVBus0303736_consumption, 93_LVBus0303739_consumption, 93_LVBus0303742_consumption, 93_LVBus0303743_consumption, 93_LVBus0303744_consumption, 93_LVBus0303749_consumption, 93_LVBus0303750_consumption, 93_LVBus0303752_consumption, 93_LVBus0303753_consumption, 93_LVBus0303754_consumption, 93_LVBus0303756_consumption, 93_LVBus0303763_consumption, 93_LVBus0303764_consumption, 93_LVBus0303767_consumption, 93_LVBus0303772_consumption, 93_LVBus0303775_consumption, 93_LVBus0303777_consumption, 93_LVBus0303778_consumption, 93_LVBus0303779_consumption, 93_LVBus0303780_consumption, 93_LVBus0303785_consumption, 93_LVBus0303791_consumption, 93_LVBus0303799_consumption, 93_LVBus0303807_consumption, 93_LVBus0303811_consumption, 93_LVBus0303812_consumption, 93_LVBus0303815_consumption, 93_LVBus0303816_consumption, 93_LVBus0303817_consumption, 93_LVBus0303818_consumption, 93_LVBus0303822_consumption, 93_LVBus0303823_consumption, 93_LVBus0303824_consumption, 93_LVBus0303825_consumption, 93_LVBus0303827_consumption, 93_LVBus0303828_consumption, 93_LVBus0303830_consumption, 93_LVBus0303831_consumption, 93_LVBus0303833_consumption, 93_LVBus0303834_consumption, 93_LVBus0303836_consumption, 93_LVBus0303837_consumption, 93_LVBus0303838_consumption, 93_LVBus0303839_consumption, 93_LVBus0303840_consumption, 93_LVBus0303841_consumption, 93_LVBus0303846_consumption, 93_LVBus0303848_consumption, 93_LVBus0303858_consumption, 93_LVBus0303860_consumption, 93_LVBus0303861_consumption, 93_LVBus0303862_consumption, 93_LVBus0303863_consumption, 93_LVBus0303864_consumption, 93_LVBus0303866_consumption, 93_LVBus0303867_consumption, 93_LVBus0303873_consumption, 93_LVBus0303874_consumption, 93_LVBus0303877_consumption, 93_LVBus0303878_consumption, 93_LVBus0303879_consumption, 93_LVBus0303881_consumption, 93_LVBus0303883_consumption, 93_LVBus0303884_consumption, 93_LVBus0303885_consumption, 93_LVBus0303886_consumption, 93_LVBus0303887_consumption, 93_LVBus0303889_consumption, 93_LVBus0303890_consumption, 93_LVBus0303891_consumption, 93_LVBus0303892_consumption, 93_LVBus0303909_consumption, 93_LVBus0303910_consumption, 93_LVBus0303913_consumption, 93_LVBus0303915_consumption, 93_LVBus0303921_consumption, 93_LVBus0303922_consumption, 93_LVBus0303923_consumption, 93_LVBus0303926_consumption, 93_LVBus0303933_consumption, 93_LVBus0303935_consumption, 93_LVBus0303936_consumption, 93_LVBus0303938_consumption, 93_LVBus0303942_consumption, 93_LVBus0303943_consumption, 93_LVBus0303946_consumption, 93_LVBus0303948_consumption, 93_LVBus0303950_consumption, 93_LVBus0303953_consumption, 93_LVBus0303954_consumption, 93_LVBus0303958_consumption, 93_LVBus0303959_consumption, 93_LVBus0303961_consumption, 93_LVBus0303963_consumption, 93_LVBus0303964_consumption, 93_LVBus0303966_consumption, 93_LVBus0303968_consumption, 93_LVBus0303970_consumption, 93_LVBus0303975_consumption, 93_LVBus1351803_consumption, 93_LVBus1357140_consumption, 93_LVBus1404118_consumption, 93_LVBus1430570_consumption, 93_LVBus1430571_consumption, 93_LVBus1430572_consumption, 93_LVBus1430573_consumption, 93_LVBus1430576_consumption, 93_LVBus1430580_consumption, 93_LVBus1430587_consumption, 93_LVBus1430596_consumption, 93_LVBus1430605_consumption, 93_LVBus1430609_consumption, 93_LVBus1430611_consumption, 93_LVBus1430614_consumption, 93_LVBus1430621_consumption, 93_LVBus1430622_consumption, 93_LVBus1430626_consumption, 93_LVBus1430628_consumption, 93_LVBus1430631_consumption, 93_LVBus1430632_consumption, 93_LVBus1430635_consumption, 93_LVBus1430636_consumption, 93_LVBus1430638_consumption, 93_LVBus1430639_consumption, 93_LVBus1430640_consumption, 93_LVBus1430641_consumption, 93_LVBus1430643_consumption, 93_LVBus1430650_consumption, 93_LVBus1430652_consumption, 93_LVBus1430654_consumption, 93_LVBus1430660_consumption, 93_LVBus1430662_consumption, 93_LVBus1430666_consumption, 93_LVBus1430670_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  410 group(s) of loads (820 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  3 group(s) of series lines (7 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  560 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 93_LVBus0303652_production, 93_LVBus0303653_consumption, 93_LVBus0303653_production, 93_LVBus0303655_consumption, 93_LVBus0303655_production, 93_LVBus0303656_consumption, 93_LVBus0303656_production, 93_LVBus0303657_production, 93_LVBus0303658_consumption, 93_LVBus0303658_production, 93_LVBus0303659_production, 93_LVBus0303660_consumption, 93_LVBus0303660_production, 93_LVBus0303661_production, 93_LVBus0303662_consumption, 93_LVBus0303662_production, 93_LVBus0303663_consumption, 93_LVBus0303663_production, 93_LVBus0303664_production, 93_LVBus0303665_production, 93_LVBus0303666_production, 93_LVBus0303667_production, 93_LVBus0303668_production, 93_LVBus0303670_consumption, 93_LVBus0303670_production, 93_LVBus0303671_consumption, 93_LVBus0303671_production, 93_LVBus0303672_consumption, 93_LVBus0303672_production, 93_LVBus0303673_consumption, 93_LVBus0303673_production, 93_LVBus0303674_consumption, 93_LVBus0303674_production, 93_LVBus0303675_production, 93_LVBus0303677_consumption, 93_LVBus0303677_production, 93_LVBus0303678_consumption, 93_LVBus0303678_production, 93_LVBus0303679_production, 93_LVBus0303680_consumption, 93_LVBus0303680_production, 93_LVBus0303681_consumption, 93_LVBus0303681_production, 93_LVBus0303683_production, 93_LVBus0303684_consumption, 93_LVBus0303684_production, 93_LVBus0303685_consumption, 93_LVBus0303685_production, 93_LVBus0303686_production, 93_LVBus0303690_production, 93_LVBus0303691_production, 93_LVBus0303692_production, 93_LVBus0303693_production, 93_LVBus0303695_consumption, 93_LVBus0303695_production, 93_LVBus0303697_production, 93_LVBus0303698_production, 93_LVBus0303699_consumption, 93_LVBus0303699_production, 93_LVBus0303700_production, 93_LVBus0303701_consumption, 93_LVBus0303701_production, 93_LVBus0303702_consumption, 93_LVBus0303702_production, 93_LVBus0303703_production, 93_LVBus0303704_production, 93_LVBus0303705_production, 93_LVBus0303706_consumption, 93_LVBus0303706_production, 93_LVBus0303707_production, 93_LVBus0303708_consumption, 93_LVBus0303708_production, 93_LVBus0303709_production, 93_LVBus0303710_production, 93_LVBus0303711_consumption, 93_LVBus0303711_production, 93_LVBus0303712_production, 93_LVBus0303713_production, 93_LVBus0303714_consumption, 93_LVBus0303714_production, 93_LVBus0303715_production, 93_LVBus0303716_production, 93_LVBus0303717_consumption, 93_LVBus0303717_production, 93_LVBus0303718_consumption, 93_LVBus0303718_production, 93_LVBus0303720_consumption, 93_LVBus0303720_production, 93_LVBus0303721_production, 93_LVBus0303722_production, 93_LVBus0303723_production, 93_LVBus0303724_production, 93_LVBus0303725_production, 93_LVBus0303726_production, 93_LVBus0303727_consumption, 93_LVBus0303727_production, 93_LVBus0303728_consumption, 93_LVBus0303728_production, 93_LVBus0303729_production, 93_LVBus0303730_production, 93_LVBus0303732_production, 93_LVBus0303733_consumption, 93_LVBus0303733_production, 93_LVBus0303734_production, 93_LVBus0303735_production, 93_LVBus0303736_production, 93_LVBus0303737_production, 93_LVBus0303738_consumption, 93_LVBus0303738_production, 93_LVBus0303739_production, 93_LVBus0303740_production, 93_LVBus0303741_production, 93_LVBus0303742_production, 93_LVBus0303743_production, 93_LVBus0303744_production, 93_LVBus0303746_consumption, 93_LVBus0303746_production, 93_LVBus0303747_consumption, 93_LVBus0303747_production, 93_LVBus0303748_production, 93_LVBus0303749_production, 93_LVBus0303750_production, 93_LVBus0303752_production, 93_LVBus0303753_production, 93_LVBus0303754_production, 93_LVBus0303755_production, 93_LVBus0303756_production, 93_LVBus0303757_production, 93_LVBus0303758_production, 93_LVBus0303759_production, 93_LVBus0303760_consumption, 93_LVBus0303760_production, 93_LVBus0303761_consumption, 93_LVBus0303761_production, 93_LVBus0303763_production, 93_LVBus0303764_production, 93_LVBus0303766_production, 93_LVBus0303767_production, 93_LVBus0303768_production, 93_LVBus0303770_production, 93_LVBus0303771_consumption, 93_LVBus0303771_production, 93_LVBus0303772_production, 93_LVBus0303773_production, 93_LVBus0303774_consumption, 93_LVBus0303774_production, 93_LVBus0303775_production, 93_LVBus0303776_consumption, 93_LVBus0303776_production, 93_LVBus0303777_production, 93_LVBus0303778_production, 93_LVBus0303779_production, 93_LVBus0303780_production, 93_LVBus0303782_consumption, 93_LVBus0303782_production, 93_LVBus0303783_production, 93_LVBus0303784_consumption, 93_LVBus0303784_production, 93_LVBus0303785_production, 93_LVBus0303787_consumption, 93_LVBus0303787_production, 93_LVBus0303788_consumption, 93_LVBus0303788_production, 93_LVBus0303789_consumption, 93_LVBus0303789_production, 93_LVBus0303790_consumption, 93_LVBus0303790_production, 93_LVBus0303791_production, 93_LVBus0303792_consumption, 93_LVBus0303792_production, 93_LVBus0303793_consumption, 93_LVBus0303793_production, 93_LVBus0303794_consumption, 93_LVBus0303794_production, 93_LVBus0303795_consumption, 93_LVBus0303795_production, 93_LVBus0303797_consumption, 93_LVBus0303797_production, 93_LVBus0303799_production, 93_LVBus0303801_consumption, 93_LVBus0303801_production, 93_LVBus0303803_consumption, 93_LVBus0303803_production, 93_LVBus0303804_consumption, 93_LVBus0303804_production, 93_LVBus0303806_consumption, 93_LVBus0303806_production, 93_LVBus0303807_production, 93_LVBus0303808_consumption, 93_LVBus0303808_production, 93_LVBus0303809_consumption, 93_LVBus0303809_production, 93_LVBus0303810_consumption, 93_LVBus0303810_production, 93_LVBus0303811_production, 93_LVBus0303812_production, 93_LVBus0303813_production, 93_LVBus0303814_production, 93_LVBus0303815_production, 93_LVBus0303816_production, 93_LVBus0303817_production, 93_LVBus0303818_production, 93_LVBus0303819_production, 93_LVBus0303820_consumption, 93_LVBus0303820_production, 93_LVBus0303821_consumption, 93_LVBus0303821_production, 93_LVBus0303822_production, 93_LVBus0303823_production, 93_LVBus0303824_production, 93_LVBus0303825_production, 93_LVBus0303827_production, 93_LVBus0303828_production, 93_LVBus0303829_production, 93_LVBus0303830_production, 93_LVBus0303831_production, 93_LVBus0303833_production, 93_LVBus0303834_production, 93_LVBus0303836_production, 93_LVBus0303837_production, 93_LVBus0303838_production, 93_LVBus0303839_production, 93_LVBus0303840_production, 93_LVBus0303841_production, 93_LVBus0303843_consumption, 93_LVBus0303843_production, 93_LVBus0303844_production, 93_LVBus0303845_consumption, 93_LVBus0303845_production, 93_LVBus0303846_production, 93_LVBus0303847_consumption, 93_LVBus0303847_production, 93_LVBus0303848_production, 93_LVBus0303849_consumption, 93_LVBus0303849_production, 93_LVBus0303850_production, 93_LVBus0303851_consumption, 93_LVBus0303851_production, 93_LVBus0303852_production, 93_LVBus0303853_consumption, 93_LVBus0303853_production, 93_LVBus0303854_consumption, 93_LVBus0303854_production, 93_LVBus0303855_production, 93_LVBus0303857_consumption, 93_LVBus0303857_production, 93_LVBus0303858_production, 93_LVBus0303859_consumption, 93_LVBus0303859_production, 93_LVBus0303860_production, 93_LVBus0303861_production, 93_LVBus0303862_production, 93_LVBus0303863_production, 93_LVBus0303864_production, 93_LVBus0303865_production, 93_LVBus0303866_production, 93_LVBus0303867_production, 93_LVBus0303868_production, 93_LVBus0303870_consumption, 93_LVBus0303870_production, 93_LVBus0303871_production, 93_LVBus0303872_consumption, 93_LVBus0303872_production, 93_LVBus0303873_production, 93_LVBus0303874_production, 93_LVBus0303876_consumption, 93_LVBus0303876_production, 93_LVBus0303877_production, 93_LVBus0303878_production, 93_LVBus0303879_production, 93_LVBus0303880_production, 93_LVBus0303881_production, 93_LVBus0303882_production, 93_LVBus0303883_production, 93_LVBus0303884_production, 93_LVBus0303885_production, 93_LVBus0303886_production, 93_LVBus0303887_production, 93_LVBus0303888_consumption, 93_LVBus0303888_production, 93_LVBus0303889_production, 93_LVBus0303890_production, 93_LVBus0303891_production, 93_LVBus0303892_production, 93_LVBus0303893_production, 93_LVBus0303894_production, 93_LVBus0303896_consumption, 93_LVBus0303896_production, 93_LVBus0303899_consumption, 93_LVBus0303899_production, 93_LVBus0303901_consumption, 93_LVBus0303901_production, 93_LVBus0303903_consumption, 93_LVBus0303903_production, 93_LVBus0303904_consumption, 93_LVBus0303904_production, 93_LVBus0303905_production, 93_LVBus0303907_consumption, 93_LVBus0303907_production, 93_LVBus0303909_production, 93_LVBus0303910_production, 93_LVBus0303911_consumption, 93_LVBus0303911_production, 93_LVBus0303912_consumption, 93_LVBus0303912_production, 93_LVBus0303913_production, 93_LVBus0303914_consumption, 93_LVBus0303914_production, 93_LVBus0303915_production, 93_LVBus0303916_consumption, 93_LVBus0303916_production, 93_LVBus0303918_consumption, 93_LVBus0303918_production, 93_LVBus0303920_consumption, 93_LVBus0303920_production, 93_LVBus0303921_production, 93_LVBus0303922_production, 93_LVBus0303923_production, 93_LVBus0303924_production, 93_LVBus0303925_production, 93_LVBus0303926_production, 93_LVBus0303933_production, 93_LVBus0303934_production, 93_LVBus0303935_production, 93_LVBus0303936_production, 93_LVBus0303937_consumption, 93_LVBus0303937_production, 93_LVBus0303938_production, 93_LVBus0303939_production, 93_LVBus0303940_production, 93_LVBus0303941_consumption, 93_LVBus0303941_production, 93_LVBus0303942_production, 93_LVBus0303943_production, 93_LVBus0303945_consumption, 93_LVBus0303945_production, 93_LVBus0303946_production, 93_LVBus0303947_consumption, 93_LVBus0303947_production, 93_LVBus0303948_production, 93_LVBus0303949_consumption, 93_LVBus0303949_production, 93_LVBus0303950_production, 93_LVBus0303951_consumption, 93_LVBus0303951_production, 93_LVBus0303952_consumption, 93_LVBus0303952_production, 93_LVBus0303953_production, 93_LVBus0303954_production, 93_LVBus0303955_consumption, 93_LVBus0303955_production, 93_LVBus0303956_consumption, 93_LVBus0303956_production, 93_LVBus0303957_consumption, 93_LVBus0303957_production, 93_LVBus0303958_production, 93_LVBus0303959_production, 93_LVBus0303960_consumption, 93_LVBus0303960_production, 93_LVBus0303961_production, 93_LVBus0303962_consumption, 93_LVBus0303962_production, 93_LVBus0303963_production, 93_LVBus0303964_production, 93_LVBus0303965_production, 93_LVBus0303966_production, 93_LVBus0303967_consumption, 93_LVBus0303967_production, 93_LVBus0303968_production, 93_LVBus0303969_production, 93_LVBus0303970_production, 93_LVBus0303971_consumption, 93_LVBus0303971_production, 93_LVBus0303972_consumption, 93_LVBus0303972_production, 93_LVBus0303973_consumption, 93_LVBus0303973_production, 93_LVBus0303975_production, 93_LVBus1348827_consumption, 93_LVBus1348827_production, 93_LVBus1351799_consumption, 93_LVBus1351799_production, 93_LVBus1351800_production, 93_LVBus1351801_consumption, 93_LVBus1351801_production, 93_LVBus1351802_production, 93_LVBus1351803_production, 93_LVBus1357139_consumption, 93_LVBus1357139_production, 93_LVBus1357140_production, 93_LVBus1383838_consumption, 93_LVBus1383838_production, 93_LVBus1404118_production, 93_LVBus1404119_consumption, 93_LVBus1404119_production, 93_LVBus1430554_production, 93_LVBus1430555_production, 93_LVBus1430556_production, 93_LVBus1430557_consumption, 93_LVBus1430557_production, 93_LVBus1430558_production, 93_LVBus1430559_production, 93_LVBus1430560_production, 93_LVBus1430561_production, 93_LVBus1430562_production, 93_LVBus1430563_production, 93_LVBus1430564_production, 93_LVBus1430565_consumption, 93_LVBus1430565_production, 93_LVBus1430566_production, 93_LVBus1430567_production, 93_LVBus1430568_production, 93_LVBus1430569_production, 93_LVBus1430570_production, 93_LVBus1430571_production, 93_LVBus1430572_production, 93_LVBus1430573_production, 93_LVBus1430574_production, 93_LVBus1430575_production, 93_LVBus1430576_production, 93_LVBus1430577_consumption, 93_LVBus1430577_production, 93_LVBus1430578_production, 93_LVBus1430579_consumption, 93_LVBus1430579_production, 93_LVBus1430580_production, 93_LVBus1430581_consumption, 93_LVBus1430581_production, 93_LVBus1430582_consumption, 93_LVBus1430582_production, 93_LVBus1430583_consumption, 93_LVBus1430583_production, 93_LVBus1430584_consumption, 93_LVBus1430584_production, 93_LVBus1430585_consumption, 93_LVBus1430585_production, 93_LVBus1430586_production, 93_LVBus1430587_production, 93_LVBus1430588_production, 93_LVBus1430589_production, 93_LVBus1430590_production, 93_LVBus1430591_consumption, 93_LVBus1430591_production, 93_LVBus1430592_production, 93_LVBus1430593_production, 93_LVBus1430594_production, 93_LVBus1430595_production, 93_LVBus1430596_production, 93_LVBus1430597_production, 93_LVBus1430598_production, 93_LVBus1430599_consumption, 93_LVBus1430599_production, 93_LVBus1430600_consumption, 93_LVBus1430600_production, 93_LVBus1430601_consumption, 93_LVBus1430601_production, 93_LVBus1430602_consumption, 93_LVBus1430602_production, 93_LVBus1430603_consumption, 93_LVBus1430603_production, 93_LVBus1430604_production, 93_LVBus1430605_production, 93_LVBus1430606_production, 93_LVBus1430607_production, 93_LVBus1430608_consumption, 93_LVBus1430608_production, 93_LVBus1430609_production, 93_LVBus1430610_production, 93_LVBus1430611_production, 93_LVBus1430612_consumption, 93_LVBus1430612_production, 93_LVBus1430613_consumption, 93_LVBus1430613_production, 93_LVBus1430614_production, 93_LVBus1430615_consumption, 93_LVBus1430615_production, 93_LVBus1430616_consumption, 93_LVBus1430616_production, 93_LVBus1430617_production, 93_LVBus1430618_consumption, 93_LVBus1430618_production, 93_LVBus1430619_consumption, 93_LVBus1430619_production, 93_LVBus1430620_consumption, 93_LVBus1430620_production, 93_LVBus1430621_production, 93_LVBus1430622_production, 93_LVBus1430623_consumption, 93_LVBus1430623_production, 93_LVBus1430624_consumption, 93_LVBus1430624_production, 93_LVBus1430625_consumption, 93_LVBus1430625_production, 93_LVBus1430626_production, 93_LVBus1430627_consumption, 93_LVBus1430627_production, 93_LVBus1430628_production, 93_LVBus1430629_consumption, 93_LVBus1430629_production, 93_LVBus1430630_consumption, 93_LVBus1430630_production, 93_LVBus1430631_production, 93_LVBus1430632_production, 93_LVBus1430633_production, 93_LVBus1430634_production, 93_LVBus1430635_production, 93_LVBus1430636_production, 93_LVBus1430637_consumption, 93_LVBus1430637_production, 93_LVBus1430638_production, 93_LVBus1430639_production, 93_LVBus1430640_production, 93_LVBus1430641_production, 93_LVBus1430642_production, 93_LVBus1430643_production, 93_LVBus1430644_production, 93_LVBus1430645_consumption, 93_LVBus1430645_production, 93_LVBus1430646_consumption, 93_LVBus1430646_production, 93_LVBus1430647_production, 93_LVBus1430648_consumption, 93_LVBus1430648_production, 93_LVBus1430649_production, 93_LVBus1430650_production, 93_LVBus1430651_production, 93_LVBus1430652_production, 93_LVBus1430653_consumption, 93_LVBus1430653_production, 93_LVBus1430654_production, 93_LVBus1430655_production, 93_LVBus1430656_production, 93_LVBus1430657_production, 93_LVBus1430658_consumption, 93_LVBus1430658_production, 93_LVBus1430659_consumption, 93_LVBus1430659_production, 93_LVBus1430660_production, 93_LVBus1430661_consumption, 93_LVBus1430661_production, 93_LVBus1430662_production, 93_LVBus1430663_production, 93_LVBus1430664_consumption, 93_LVBus1430664_production, 93_LVBus1430665_production, 93_LVBus1430666_production, 93_LVBus1430667_production, 93_LVBus1430668_production, 93_LVBus1430669_production, 93_LVBus1430670_production, 93_LVBus1430671_consumption, 93_LVBus1430671_production, 93_MVLV13007_consumption, 93_MVLV13007_production, 93_MVLV28538_consumption, 93_MVLV28538_production, 93_MVLV43313_consumption, 93_MVLV43313_production, 93_MVLV68589_consumption, 93_MVLV68589_production.

