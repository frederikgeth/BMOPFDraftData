# BMOPF Network Summary: 75_MVFeeder2269

**Generated:** 2026-10-01 23:34:24  
**Findings:** 0 errors · 5 warnings · 298 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 50 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 561 |  |
| line | 510 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 832 | 756.112 kW, 226.8 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 50 |  |
| switch | 0 |  |
| transformer | 50 | Dyn11×50 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 103 | 102 | 16 | 0 |
| LV_236V | 236.0 V | 458 | 408 | 816 | 0 |

**Transformer transitions:**

- `75_MVLV077093_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV103721_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV159734_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV006425_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV016683_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127779_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV038053_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV133019_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV054852_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV057664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV108437_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV046270_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV110327_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067135_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV161718_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062982_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV154918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV094365_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV092797_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV122293_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV072831_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149925_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV137537_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV116422_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV069567_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV174451_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV120392_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV045655_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV045654_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV044516_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV154917_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV094474_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV143272_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV078068_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068926_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV046682_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV038054_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149924_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002269_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV085724_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV082668_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV035396_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV139613_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV105059_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV152274_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV008501_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV170628_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV143279_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 194 |
| Tree depth (max hops) | 47 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 561 | 1 | 560 | 0 | 0 | 0 |
| Tier LV_236V | 458 | 50 | 408 | 0 | 0 | 0 |
| Tier MV_11.8kV | 103 | 1 | 102 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 50; skipped invalid branches: 0.

Galvanic zones: 51; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_M.VIR | MV_11.8kV | 103 | 0 | 0 | 50 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2141 declared bus terminals; 1938 mapped line/closed-switch conductor edges; 203 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 10100.0 | 3.075 | 2496 |
| q_nom | 0.0 | 3030.0 | 3.075 | 2496 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.638 | 1930.0 | 1.56 | 510 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.641 | 50 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 533 of 832 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005378_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005555_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005630_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005418_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005701_consumption' has phase imbalance of 283.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005736_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005392_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005683_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005406_consumption' has phase imbalance of 227.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005776_consumption' has phase imbalance of 111.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005711_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005527_consumption' has phase imbalance of 281.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005645_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005557_consumption' has phase imbalance of 261.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005614_consumption' has phase imbalance of 266.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005580_consumption' has phase imbalance of 234.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005596_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005716_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005413_consumption' has phase imbalance of 147.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005476_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005480_consumption' has phase imbalance of 193.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005753_consumption' has phase imbalance of 156.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005638_consumption' has phase imbalance of 61.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005773_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005747_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005673_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005551_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005536_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005515_consumption' has phase imbalance of 171.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005723_consumption' has phase imbalance of 156.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005545_consumption' has phase imbalance of 268.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005746_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005839_consumption' has phase imbalance of 220.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005672_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005567_consumption' has phase imbalance of 253.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005704_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005404_consumption' has phase imbalance of 175.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005405_consumption' has phase imbalance of 130.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005423_consumption' has phase imbalance of 287.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005521_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005504_consumption' has phase imbalance of 200.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005566_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005838_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005842_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005474_consumption' has phase imbalance of 290.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005816_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005610_consumption' has phase imbalance of 171.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005410_consumption' has phase imbalance of 198.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005411_consumption' has phase imbalance of 290.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005755_consumption' has phase imbalance of 268.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005626_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005383_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005620_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005792_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005694_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005649_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005830_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005581_consumption' has phase imbalance of 273.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005518_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005718_consumption' has phase imbalance of 84.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005470_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005729_consumption' has phase imbalance of 77.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005738_consumption' has phase imbalance of 134.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005540_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005483_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005825_consumption' has phase imbalance of 261.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005781_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005766_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005646_consumption' has phase imbalance of 286.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005453_consumption' has phase imbalance of 230.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005508_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005749_consumption' has phase imbalance of 264.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005462_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005731_consumption' has phase imbalance of 279.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005403_consumption' has phase imbalance of 138.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005849_consumption' has phase imbalance of 198.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005507_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005494_consumption' has phase imbalance of 238.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005743_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005384_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005426_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005612_consumption' has phase imbalance of 156.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005397_consumption' has phase imbalance of 142.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005780_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005855_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005564_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005505_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005750_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005826_consumption' has phase imbalance of 183.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005796_consumption' has phase imbalance of 143.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005613_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005684_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005705_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005574_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005748_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005528_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005429_consumption' has phase imbalance of 111.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005502_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005568_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005719_consumption' has phase imbalance of 292.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005785_consumption' has phase imbalance of 119.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005492_consumption' has phase imbalance of 281.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005380_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005414_consumption' has phase imbalance of 288.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005463_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005447_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005760_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005663_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005513_consumption' has phase imbalance of 142.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005713_consumption' has phase imbalance of 87.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005642_consumption' has phase imbalance of 259.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005534_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005832_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005535_consumption' has phase imbalance of 256.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005430_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005688_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005819_consumption' has phase imbalance of 123.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005720_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005485_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005498_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005477_consumption' has phase imbalance of 259.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005844_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005522_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005754_consumption' has phase imbalance of 284.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005592_consumption' has phase imbalance of 283.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005461_consumption' has phase imbalance of 111.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005829_consumption' has phase imbalance of 273.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005728_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005611_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005850_consumption' has phase imbalance of 198.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005621_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005761_consumption' has phase imbalance of 255.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005432_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005431_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005604_consumption' has phase imbalance of 230.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005818_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005543_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005739_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005786_consumption' has phase imbalance of 275.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005482_consumption' has phase imbalance of 271.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005400_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005751_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005479_consumption' has phase imbalance of 287.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005643_consumption' has phase imbalance of 228.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005857_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005717_consumption' has phase imbalance of 215.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005509_consumption' has phase imbalance of 286.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005769_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005648_consumption' has phase imbalance of 143.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005722_consumption' has phase imbalance of 283.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005576_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005416_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005740_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005650_consumption' has phase imbalance of 212.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005396_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005475_consumption' has phase imbalance of 272.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005558_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005784_consumption' has phase imbalance of 131.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1005506_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 832 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1005677' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1005859' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 756.112 kW |
| Total load Q | 226.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV077093_Transformer | 110.0 kVA | 0.7% |
| 75_MVLV103721_Transformer | 110.0 kVA | 0.4% |
| 75_MVLV159734_Transformer | 110.0 kVA | 9.4% |
| 75_MVLV006425_Transformer | 176.0 kVA | 11.3% |
| 75_MVLV016683_Transformer | 110.0 kVA | 1.2% |
| 75_MVLV127779_Transformer | 110.0 kVA | 5.8% |
| 75_MVLV038053_Transformer | 110.0 kVA | 0.4% |
| 75_MVLV133019_Transformer | 110.0 kVA | 4.2% |
| 75_MVLV054852_Transformer | 110.0 kVA | 3.9% |
| 75_MVLV057664_Transformer | 275.0 kVA | 14.9% |
| 75_MVLV108437_Transformer | 110.0 kVA | 7.8% |
| 75_MVLV046270_Transformer | 110.0 kVA | 1.4% |
| 75_MVLV110327_Transformer | 176.0 kVA | 16.6% |
| 75_MVLV067135_Transformer | 176.0 kVA | 11.1% |
| 75_MVLV161718_Transformer | 110.0 kVA | 6.5% |
| 75_MVLV062982_Transformer | 275.0 kVA | 5.1% |
| 75_MVLV154918_Transformer | 176.0 kVA | 13.0% |
| 75_MVLV094365_Transformer | 110.0 kVA | 2.7% |
| 75_MVLV092797_Transformer | 110.0 kVA | 1.9% |
| 75_MVLV122293_Transformer | 110.0 kVA | 9.5% |
| 75_MVLV066918_Transformer | 275.0 kVA | 16.0% |
| 75_MVLV072831_Transformer | 110.0 kVA | 2.2% |
| 75_MVLV149925_Transformer | 693.0 kVA | 20.0% |
| 75_MVLV137537_Transformer | 110.0 kVA | 5.7% |
| 75_MVLV116422_Transformer | 176.0 kVA | 5.3% |
| 75_MVLV069567_Transformer | 110.0 kVA | 2.8% |
| 75_MVLV174451_Transformer | 110.0 kVA | 0.1% |
| 75_MVLV120392_Transformer | 110.0 kVA | 4.2% |
| 75_MVLV045655_Transformer | 110.0 kVA | 7.7% |
| 75_MVLV045654_Transformer | 110.0 kVA | 1.1% |
| 75_MVLV044516_Transformer | 176.0 kVA | 14.6% |
| 75_MVLV154917_Transformer | 176.0 kVA | 8.0% |
| 75_MVLV094474_Transformer | 176.0 kVA | 20.7% |
| 75_MVLV143272_Transformer | 110.0 kVA | 7.4% |
| 75_MVLV078068_Transformer | 110.0 kVA | 4.8% |
| 75_MVLV068926_Transformer | 110.0 kVA | 8.7% |
| 75_MVLV046682_Transformer | 110.0 kVA | 11.7% |
| 75_MVLV038054_Transformer | 110.0 kVA | 5.7% |
| 75_MVLV149924_Transformer | 440.0 kVA | 19.8% |
| 75_MVLV002269_Transformer | 275.0 kVA | 9.0% |
| 75_MVLV085724_Transformer | 176.0 kVA | 11.7% |
| 75_MVLV082668_Transformer | 110.0 kVA | 10.2% |
| 75_MVLV149937_Transformer | 176.0 kVA | 10.3% |
| 75_MVLV035396_Transformer | 275.0 kVA | 13.2% |
| 75_MVLV139613_Transformer | 110.0 kVA | 5.8% |
| 75_MVLV105059_Transformer | 110.0 kVA | 4.9% |
| 75_MVLV152274_Transformer | 176.0 kVA | 6.9% |
| 75_MVLV008501_Transformer | 110.0 kVA | 0.1% |
| 75_MVLV170628_Transformer | 110.0 kVA | 9.5% |
| 75_MVLV143279_Transformer | 110.0 kVA | 11.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.76 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_M.VIR' (MV, 11.78 kV) has an electrical reach of 34.63 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_LVBus1005436' (LV, 0.24 kV) has an electrical reach of 1.19 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_LVBus1005395' (LV, 0.24 kV) has an electrical reach of 1.69 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_LVBus1005564' (LV, 0.24 kV) has an electrical reach of 1.09 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1005616' (LV, 0.24 kV) has an electrical reach of 6.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 561 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 561 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 50 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 103 |
| LV_236V | 4-wire | 458 / 458 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 458 |
| Neutral branches | 408 |
| Grounding points | 50 |
| Neutral sections | 50 |
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
| 11.78 kV | 103 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 55 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 51 |
| Islands without voltage reference | 0 |
| Line impedance spread | 3840.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 458 / 103 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 534 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 534 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1005366_production, 75_LVBus1005368_consumption, 75_LVBus1005368_production, 75_LVBus1005370_production, 75_LVBus1005371_consumption, 75_LVBus1005371_production, 75_LVBus1005372_consumption, 75_LVBus1005372_production, 75_LVBus1005373_consumption, 75_LVBus1005373_production, 75_LVBus1005374_production, 75_LVBus1005375_production, 75_LVBus1005376_production, 75_LVBus1005378_production, 75_LVBus1005379_production, 75_LVBus1005380_production, 75_LVBus1005382_consumption, 75_LVBus1005382_production, 75_LVBus1005383_production, 75_LVBus1005384_production, 75_LVBus1005385_production, 75_LVBus1005388_production, 75_LVBus1005390_production, 75_LVBus1005391_production, 75_LVBus1005392_production, 75_LVBus1005393_consumption, 75_LVBus1005393_production, 75_LVBus1005395_production, 75_LVBus1005396_production, 75_LVBus1005397_production, 75_LVBus1005398_production, 75_LVBus1005399_production, 75_LVBus1005400_production, 75_LVBus1005401_production, 75_LVBus1005403_production, 75_LVBus1005404_production, 75_LVBus1005405_production, 75_LVBus1005406_production, 75_LVBus1005407_consumption, 75_LVBus1005407_production, 75_LVBus1005408_consumption, 75_LVBus1005408_production, 75_LVBus1005409_production, 75_LVBus1005410_production, 75_LVBus1005411_production, 75_LVBus1005412_consumption, 75_LVBus1005412_production, 75_LVBus1005413_production, 75_LVBus1005414_production, 75_LVBus1005416_production, 75_LVBus1005418_production, 75_LVBus1005419_consumption, 75_LVBus1005419_production, 75_LVBus1005420_production, 75_LVBus1005421_consumption, 75_LVBus1005421_production, 75_LVBus1005422_consumption, 75_LVBus1005422_production, 75_LVBus1005423_production, 75_LVBus1005425_production, 75_LVBus1005426_production, 75_LVBus1005427_consumption, 75_LVBus1005427_production, 75_LVBus1005428_production, 75_LVBus1005429_production, 75_LVBus1005430_production, 75_LVBus1005431_production, 75_LVBus1005432_production, 75_LVBus1005436_consumption, 75_LVBus1005436_production, 75_LVBus1005437_consumption, 75_LVBus1005437_production, 75_LVBus1005438_production, 75_LVBus1005439_consumption, 75_LVBus1005439_production, 75_LVBus1005440_consumption, 75_LVBus1005440_production, 75_LVBus1005441_consumption, 75_LVBus1005441_production, 75_LVBus1005442_consumption, 75_LVBus1005442_production, 75_LVBus1005443_consumption, 75_LVBus1005443_production, 75_LVBus1005444_consumption, 75_LVBus1005444_production, 75_LVBus1005445_consumption, 75_LVBus1005445_production, 75_LVBus1005447_production, 75_LVBus1005448_consumption, 75_LVBus1005448_production, 75_LVBus1005449_consumption, 75_LVBus1005449_production, 75_LVBus1005450_production, 75_LVBus1005451_production, 75_LVBus1005452_consumption, 75_LVBus1005452_production, 75_LVBus1005453_production, 75_LVBus1005454_consumption, 75_LVBus1005454_production, 75_LVBus1005456_production, 75_LVBus1005458_consumption, 75_LVBus1005458_production, 75_LVBus1005459_production, 75_LVBus1005460_production, 75_LVBus1005461_production, 75_LVBus1005462_production, 75_LVBus1005463_production, 75_LVBus1005464_consumption, 75_LVBus1005464_production, 75_LVBus1005465_consumption, 75_LVBus1005465_production, 75_LVBus1005466_production, 75_LVBus1005468_consumption, 75_LVBus1005468_production, 75_LVBus1005469_consumption, 75_LVBus1005469_production, 75_LVBus1005470_production, 75_LVBus1005471_production, 75_LVBus1005473_production, 75_LVBus1005474_production, 75_LVBus1005475_production, 75_LVBus1005476_production, 75_LVBus1005477_production, 75_LVBus1005479_production, 75_LVBus1005480_production, 75_LVBus1005481_production, 75_LVBus1005482_production, 75_LVBus1005483_production, 75_LVBus1005484_production, 75_LVBus1005485_production, 75_LVBus1005490_production, 75_LVBus1005491_production, 75_LVBus1005492_production, 75_LVBus1005493_consumption, 75_LVBus1005493_production, 75_LVBus1005494_production, 75_LVBus1005495_consumption, 75_LVBus1005495_production, 75_LVBus1005497_consumption, 75_LVBus1005497_production, 75_LVBus1005498_production, 75_LVBus1005499_consumption, 75_LVBus1005499_production, 75_LVBus1005500_production, 75_LVBus1005501_production, 75_LVBus1005502_production, 75_LVBus1005503_production, 75_LVBus1005504_production, 75_LVBus1005505_production, 75_LVBus1005506_production, 75_LVBus1005507_production, 75_LVBus1005508_production, 75_LVBus1005509_production, 75_LVBus1005510_consumption, 75_LVBus1005510_production, 75_LVBus1005511_production, 75_LVBus1005512_consumption, 75_LVBus1005512_production, 75_LVBus1005513_production, 75_LVBus1005514_consumption, 75_LVBus1005514_production, 75_LVBus1005515_production, 75_LVBus1005517_consumption, 75_LVBus1005517_production, 75_LVBus1005518_production, 75_LVBus1005519_production, 75_LVBus1005520_consumption, 75_LVBus1005520_production, 75_LVBus1005521_production, 75_LVBus1005522_production, 75_LVBus1005523_production, 75_LVBus1005524_production, 75_LVBus1005525_production, 75_LVBus1005526_consumption, 75_LVBus1005526_production, 75_LVBus1005527_production, 75_LVBus1005528_production, 75_LVBus1005534_production, 75_LVBus1005535_production, 75_LVBus1005536_production, 75_LVBus1005537_consumption, 75_LVBus1005537_production, 75_LVBus1005538_production, 75_LVBus1005539_production, 75_LVBus1005540_production, 75_LVBus1005542_consumption, 75_LVBus1005542_production, 75_LVBus1005543_production, 75_LVBus1005544_consumption, 75_LVBus1005544_production, 75_LVBus1005545_production, 75_LVBus1005546_production, 75_LVBus1005547_production, 75_LVBus1005551_production, 75_LVBus1005553_consumption, 75_LVBus1005553_production, 75_LVBus1005554_production, 75_LVBus1005555_production, 75_LVBus1005557_production, 75_LVBus1005558_production, 75_LVBus1005559_production, 75_LVBus1005560_consumption, 75_LVBus1005560_production, 75_LVBus1005561_production, 75_LVBus1005562_consumption, 75_LVBus1005562_production, 75_LVBus1005564_production, 75_LVBus1005565_production, 75_LVBus1005566_production, 75_LVBus1005567_production, 75_LVBus1005568_production, 75_LVBus1005569_production, 75_LVBus1005570_consumption, 75_LVBus1005570_production, 75_LVBus1005572_production, 75_LVBus1005574_production, 75_LVBus1005575_production, 75_LVBus1005576_production, 75_LVBus1005578_consumption, 75_LVBus1005578_production, 75_LVBus1005579_production, 75_LVBus1005580_production, 75_LVBus1005581_production, 75_LVBus1005582_consumption, 75_LVBus1005582_production, 75_LVBus1005583_consumption, 75_LVBus1005583_production, 75_LVBus1005584_consumption, 75_LVBus1005584_production, 75_LVBus1005585_consumption, 75_LVBus1005585_production, 75_LVBus1005587_production, 75_LVBus1005588_consumption, 75_LVBus1005588_production, 75_LVBus1005589_production, 75_LVBus1005591_consumption, 75_LVBus1005591_production, 75_LVBus1005592_production, 75_LVBus1005594_consumption, 75_LVBus1005594_production, 75_LVBus1005595_consumption, 75_LVBus1005595_production, 75_LVBus1005596_production, 75_LVBus1005598_consumption, 75_LVBus1005598_production, 75_LVBus1005600_consumption, 75_LVBus1005600_production, 75_LVBus1005602_production, 75_LVBus1005604_production, 75_LVBus1005605_production, 75_LVBus1005607_consumption, 75_LVBus1005607_production, 75_LVBus1005609_production, 75_LVBus1005610_production, 75_LVBus1005611_production, 75_LVBus1005612_production, 75_LVBus1005613_production, 75_LVBus1005614_production, 75_LVBus1005616_production, 75_LVBus1005618_consumption, 75_LVBus1005618_production, 75_LVBus1005619_consumption, 75_LVBus1005619_production, 75_LVBus1005620_production, 75_LVBus1005621_production, 75_LVBus1005622_consumption, 75_LVBus1005622_production, 75_LVBus1005624_consumption, 75_LVBus1005624_production, 75_LVBus1005625_production, 75_LVBus1005626_production, 75_LVBus1005627_consumption, 75_LVBus1005627_production, 75_LVBus1005628_production, 75_LVBus1005629_production, 75_LVBus1005630_production, 75_LVBus1005631_consumption, 75_LVBus1005631_production, 75_LVBus1005632_production, 75_LVBus1005633_consumption, 75_LVBus1005633_production, 75_LVBus1005634_production, 75_LVBus1005635_production, 75_LVBus1005637_production, 75_LVBus1005638_production, 75_LVBus1005639_consumption, 75_LVBus1005639_production, 75_LVBus1005640_production, 75_LVBus1005641_production, 75_LVBus1005642_production, 75_LVBus1005643_production, 75_LVBus1005644_production, 75_LVBus1005645_production, 75_LVBus1005646_production, 75_LVBus1005648_production, 75_LVBus1005649_production, 75_LVBus1005650_production, 75_LVBus1005652_production, 75_LVBus1005653_consumption, 75_LVBus1005653_production, 75_LVBus1005654_production, 75_LVBus1005655_consumption, 75_LVBus1005655_production, 75_LVBus1005656_consumption, 75_LVBus1005656_production, 75_LVBus1005658_production, 75_LVBus1005659_consumption, 75_LVBus1005659_production, 75_LVBus1005660_production, 75_LVBus1005661_consumption, 75_LVBus1005661_production, 75_LVBus1005663_production, 75_LVBus1005664_production, 75_LVBus1005665_production, 75_LVBus1005667_consumption, 75_LVBus1005667_production, 75_LVBus1005668_production, 75_LVBus1005670_consumption, 75_LVBus1005670_production, 75_LVBus1005671_production, 75_LVBus1005672_production, 75_LVBus1005673_production, 75_LVBus1005674_production, 75_LVBus1005675_production, 75_LVBus1005677_consumption, 75_LVBus1005677_production, 75_LVBus1005678_consumption, 75_LVBus1005678_production, 75_LVBus1005679_production, 75_LVBus1005681_production, 75_LVBus1005682_production, 75_LVBus1005683_production, 75_LVBus1005684_production, 75_LVBus1005686_consumption, 75_LVBus1005686_production, 75_LVBus1005687_consumption, 75_LVBus1005687_production, 75_LVBus1005688_production, 75_LVBus1005689_production, 75_LVBus1005690_production, 75_LVBus1005691_production, 75_LVBus1005692_production, 75_LVBus1005693_consumption, 75_LVBus1005693_production, 75_LVBus1005694_production, 75_LVBus1005696_consumption, 75_LVBus1005696_production, 75_LVBus1005697_consumption, 75_LVBus1005697_production, 75_LVBus1005698_consumption, 75_LVBus1005698_production, 75_LVBus1005699_production, 75_LVBus1005700_consumption, 75_LVBus1005700_production, 75_LVBus1005701_production, 75_LVBus1005702_production, 75_LVBus1005704_production, 75_LVBus1005705_production, 75_LVBus1005706_production, 75_LVBus1005707_production, 75_LVBus1005708_production, 75_LVBus1005709_production, 75_LVBus1005711_production, 75_LVBus1005713_production, 75_LVBus1005714_production, 75_LVBus1005716_production, 75_LVBus1005717_production, 75_LVBus1005718_production, 75_LVBus1005719_production, 75_LVBus1005720_production, 75_LVBus1005721_production, 75_LVBus1005722_production, 75_LVBus1005723_production, 75_LVBus1005724_production, 75_LVBus1005725_production, 75_LVBus1005726_production, 75_LVBus1005727_production, 75_LVBus1005728_production, 75_LVBus1005729_production, 75_LVBus1005731_production, 75_LVBus1005732_consumption, 75_LVBus1005732_production, 75_LVBus1005733_production, 75_LVBus1005734_production, 75_LVBus1005735_production, 75_LVBus1005736_production, 75_LVBus1005738_production, 75_LVBus1005739_production, 75_LVBus1005740_production, 75_LVBus1005741_production, 75_LVBus1005743_production, 75_LVBus1005744_consumption, 75_LVBus1005744_production, 75_LVBus1005745_production, 75_LVBus1005746_production, 75_LVBus1005747_production, 75_LVBus1005748_production, 75_LVBus1005749_production, 75_LVBus1005750_production, 75_LVBus1005751_production, 75_LVBus1005752_consumption, 75_LVBus1005752_production, 75_LVBus1005753_production, 75_LVBus1005754_production, 75_LVBus1005755_production, 75_LVBus1005756_production, 75_LVBus1005757_consumption, 75_LVBus1005757_production, 75_LVBus1005758_production, 75_LVBus1005759_production, 75_LVBus1005760_production, 75_LVBus1005761_production, 75_LVBus1005763_production, 75_LVBus1005764_production, 75_LVBus1005765_production, 75_LVBus1005766_production, 75_LVBus1005767_production, 75_LVBus1005768_production, 75_LVBus1005769_production, 75_LVBus1005770_production, 75_LVBus1005771_production, 75_LVBus1005772_production, 75_LVBus1005773_production, 75_LVBus1005774_production, 75_LVBus1005776_production, 75_LVBus1005777_consumption, 75_LVBus1005777_production, 75_LVBus1005778_consumption, 75_LVBus1005778_production, 75_LVBus1005779_production, 75_LVBus1005780_production, 75_LVBus1005781_production, 75_LVBus1005782_production, 75_LVBus1005784_production, 75_LVBus1005785_production, 75_LVBus1005786_production, 75_LVBus1005787_consumption, 75_LVBus1005787_production, 75_LVBus1005788_consumption, 75_LVBus1005788_production, 75_LVBus1005789_consumption, 75_LVBus1005789_production, 75_LVBus1005791_consumption, 75_LVBus1005791_production, 75_LVBus1005792_production, 75_LVBus1005793_production, 75_LVBus1005794_production, 75_LVBus1005795_production, 75_LVBus1005796_production, 75_LVBus1005797_production, 75_LVBus1005798_production, 75_LVBus1005802_production, 75_LVBus1005804_consumption, 75_LVBus1005804_production, 75_LVBus1005805_production, 75_LVBus1005806_production, 75_LVBus1005807_consumption, 75_LVBus1005807_production, 75_LVBus1005809_consumption, 75_LVBus1005809_production, 75_LVBus1005810_production, 75_LVBus1005811_production, 75_LVBus1005812_production, 75_LVBus1005814_consumption, 75_LVBus1005814_production, 75_LVBus1005815_consumption, 75_LVBus1005815_production, 75_LVBus1005816_production, 75_LVBus1005817_production, 75_LVBus1005818_production, 75_LVBus1005819_production, 75_LVBus1005821_consumption, 75_LVBus1005821_production, 75_LVBus1005822_consumption, 75_LVBus1005822_production, 75_LVBus1005823_consumption, 75_LVBus1005823_production, 75_LVBus1005824_production, 75_LVBus1005825_production, 75_LVBus1005826_production, 75_LVBus1005827_production, 75_LVBus1005828_production, 75_LVBus1005829_production, 75_LVBus1005830_production, 75_LVBus1005831_production, 75_LVBus1005832_production, 75_LVBus1005833_production, 75_LVBus1005834_consumption, 75_LVBus1005834_production, 75_LVBus1005836_consumption, 75_LVBus1005836_production, 75_LVBus1005837_production, 75_LVBus1005838_production, 75_LVBus1005839_production, 75_LVBus1005840_production, 75_LVBus1005842_production, 75_LVBus1005843_production, 75_LVBus1005844_production, 75_LVBus1005846_consumption, 75_LVBus1005846_production, 75_LVBus1005847_production, 75_LVBus1005848_consumption, 75_LVBus1005848_production, 75_LVBus1005849_production, 75_LVBus1005850_production, 75_LVBus1005851_consumption, 75_LVBus1005851_production, 75_LVBus1005852_consumption, 75_LVBus1005852_production, 75_LVBus1005853_consumption, 75_LVBus1005853_production, 75_LVBus1005854_production, 75_LVBus1005855_production, 75_LVBus1005856_production, 75_LVBus1005857_production, 75_LVBus1005859_production, 75_LVBus1925392_consumption, 75_LVBus1925392_production, 75_MVLV029809_consumption, 75_MVLV029809_production, 75_MVLV061283_consumption, 75_MVLV061283_production, 75_MVLV067136_consumption, 75_MVLV067136_production, 75_MVLV085210_consumption, 75_MVLV085210_production, 75_MVLV111344_consumption, 75_MVLV111344_production, 75_MVLV147762_consumption, 75_MVLV147762_production, 75_MVLV152518_consumption, 75_MVLV152518_production, 75_MVLV167393_consumption, 75_MVLV167393_production.

## 9. Data Quality Summary

**Total findings:** 303 (0 errors, 5 warnings, 298 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  533 of 832 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.76 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  534 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005451_consumption`  
  Load '75_LVBus1005451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005378_consumption`  
  Load '75_LVBus1005378_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005539_consumption`  
  Load '75_LVBus1005539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005450_consumption`  
  Load '75_LVBus1005450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005555_consumption`  
  Load '75_LVBus1005555_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005511_consumption`  
  Load '75_LVBus1005511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005840_consumption`  
  Load '75_LVBus1005840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005630_consumption`  
  Load '75_LVBus1005630_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005418_consumption`  
  Load '75_LVBus1005418_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005701_consumption`  
  Load '75_LVBus1005701_consumption' has phase imbalance of 283.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005660_consumption`  
  Load '75_LVBus1005660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005833_consumption`  
  Load '75_LVBus1005833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005793_consumption`  
  Load '75_LVBus1005793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005579_consumption`  
  Load '75_LVBus1005579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005736_consumption`  
  Load '75_LVBus1005736_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005392_consumption`  
  Load '75_LVBus1005392_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005683_consumption`  
  Load '75_LVBus1005683_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005374_consumption`  
  Load '75_LVBus1005374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005406_consumption`  
  Load '75_LVBus1005406_consumption' has phase imbalance of 227.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005702_consumption`  
  Load '75_LVBus1005702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005776_consumption`  
  Load '75_LVBus1005776_consumption' has phase imbalance of 111.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005711_consumption`  
  Load '75_LVBus1005711_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005385_consumption`  
  Load '75_LVBus1005385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005388_consumption`  
  Load '75_LVBus1005388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005490_consumption`  
  Load '75_LVBus1005490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005856_consumption`  
  Load '75_LVBus1005856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005811_consumption`  
  Load '75_LVBus1005811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005527_consumption`  
  Load '75_LVBus1005527_consumption' has phase imbalance of 281.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005575_consumption`  
  Load '75_LVBus1005575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005645_consumption`  
  Load '75_LVBus1005645_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005726_consumption`  
  Load '75_LVBus1005726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005557_consumption`  
  Load '75_LVBus1005557_consumption' has phase imbalance of 261.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005629_consumption`  
  Load '75_LVBus1005629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005854_consumption`  
  Load '75_LVBus1005854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005706_consumption`  
  Load '75_LVBus1005706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005614_consumption`  
  Load '75_LVBus1005614_consumption' has phase imbalance of 266.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005580_consumption`  
  Load '75_LVBus1005580_consumption' has phase imbalance of 234.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005668_consumption`  
  Load '75_LVBus1005668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005596_consumption`  
  Load '75_LVBus1005596_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005716_consumption`  
  Load '75_LVBus1005716_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005413_consumption`  
  Load '75_LVBus1005413_consumption' has phase imbalance of 147.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005768_consumption`  
  Load '75_LVBus1005768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005476_consumption`  
  Load '75_LVBus1005476_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005480_consumption`  
  Load '75_LVBus1005480_consumption' has phase imbalance of 193.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005753_consumption`  
  Load '75_LVBus1005753_consumption' has phase imbalance of 156.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005569_consumption`  
  Load '75_LVBus1005569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005638_consumption`  
  Load '75_LVBus1005638_consumption' has phase imbalance of 61.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005773_consumption`  
  Load '75_LVBus1005773_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005747_consumption`  
  Load '75_LVBus1005747_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005673_consumption`  
  Load '75_LVBus1005673_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005551_consumption`  
  Load '75_LVBus1005551_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005536_consumption`  
  Load '75_LVBus1005536_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005515_consumption`  
  Load '75_LVBus1005515_consumption' has phase imbalance of 171.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005723_consumption`  
  Load '75_LVBus1005723_consumption' has phase imbalance of 156.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005545_consumption`  
  Load '75_LVBus1005545_consumption' has phase imbalance of 268.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005589_consumption`  
  Load '75_LVBus1005589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005745_consumption`  
  Load '75_LVBus1005745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005828_consumption`  
  Load '75_LVBus1005828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005772_consumption`  
  Load '75_LVBus1005772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005519_consumption`  
  Load '75_LVBus1005519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005746_consumption`  
  Load '75_LVBus1005746_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005839_consumption`  
  Load '75_LVBus1005839_consumption' has phase imbalance of 220.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005764_consumption`  
  Load '75_LVBus1005764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005672_consumption`  
  Load '75_LVBus1005672_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005399_consumption`  
  Load '75_LVBus1005399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005398_consumption`  
  Load '75_LVBus1005398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005567_consumption`  
  Load '75_LVBus1005567_consumption' has phase imbalance of 253.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005704_consumption`  
  Load '75_LVBus1005704_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005404_consumption`  
  Load '75_LVBus1005404_consumption' has phase imbalance of 175.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005405_consumption`  
  Load '75_LVBus1005405_consumption' has phase imbalance of 130.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005665_consumption`  
  Load '75_LVBus1005665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005501_consumption`  
  Load '75_LVBus1005501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005423_consumption`  
  Load '75_LVBus1005423_consumption' has phase imbalance of 287.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005428_consumption`  
  Load '75_LVBus1005428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005503_consumption`  
  Load '75_LVBus1005503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005525_consumption`  
  Load '75_LVBus1005525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005521_consumption`  
  Load '75_LVBus1005521_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005771_consumption`  
  Load '75_LVBus1005771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005572_consumption`  
  Load '75_LVBus1005572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005504_consumption`  
  Load '75_LVBus1005504_consumption' has phase imbalance of 200.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005566_consumption`  
  Load '75_LVBus1005566_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005838_consumption`  
  Load '75_LVBus1005838_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005842_consumption`  
  Load '75_LVBus1005842_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005474_consumption`  
  Load '75_LVBus1005474_consumption' has phase imbalance of 290.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005395_consumption`  
  Load '75_LVBus1005395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005816_consumption`  
  Load '75_LVBus1005816_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005837_consumption`  
  Load '75_LVBus1005837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005610_consumption`  
  Load '75_LVBus1005610_consumption' has phase imbalance of 171.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005410_consumption`  
  Load '75_LVBus1005410_consumption' has phase imbalance of 198.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005681_consumption`  
  Load '75_LVBus1005681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005411_consumption`  
  Load '75_LVBus1005411_consumption' has phase imbalance of 290.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005755_consumption`  
  Load '75_LVBus1005755_consumption' has phase imbalance of 268.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005626_consumption`  
  Load '75_LVBus1005626_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005383_consumption`  
  Load '75_LVBus1005383_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005620_consumption`  
  Load '75_LVBus1005620_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005547_consumption`  
  Load '75_LVBus1005547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005792_consumption`  
  Load '75_LVBus1005792_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005694_consumption`  
  Load '75_LVBus1005694_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005401_consumption`  
  Load '75_LVBus1005401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005649_consumption`  
  Load '75_LVBus1005649_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005692_consumption`  
  Load '75_LVBus1005692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005671_consumption`  
  Load '75_LVBus1005671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005481_consumption`  
  Load '75_LVBus1005481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005830_consumption`  
  Load '75_LVBus1005830_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005581_consumption`  
  Load '75_LVBus1005581_consumption' has phase imbalance of 273.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005518_consumption`  
  Load '75_LVBus1005518_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005718_consumption`  
  Load '75_LVBus1005718_consumption' has phase imbalance of 84.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005690_consumption`  
  Load '75_LVBus1005690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005470_consumption`  
  Load '75_LVBus1005470_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005641_consumption`  
  Load '75_LVBus1005641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005729_consumption`  
  Load '75_LVBus1005729_consumption' has phase imbalance of 77.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005767_consumption`  
  Load '75_LVBus1005767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005824_consumption`  
  Load '75_LVBus1005824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005714_consumption`  
  Load '75_LVBus1005714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005797_consumption`  
  Load '75_LVBus1005797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005554_consumption`  
  Load '75_LVBus1005554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005625_consumption`  
  Load '75_LVBus1005625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005756_consumption`  
  Load '75_LVBus1005756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005741_consumption`  
  Load '75_LVBus1005741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005817_consumption`  
  Load '75_LVBus1005817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005738_consumption`  
  Load '75_LVBus1005738_consumption' has phase imbalance of 134.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005540_consumption`  
  Load '75_LVBus1005540_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005707_consumption`  
  Load '75_LVBus1005707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005483_consumption`  
  Load '75_LVBus1005483_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005634_consumption`  
  Load '75_LVBus1005634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005825_consumption`  
  Load '75_LVBus1005825_consumption' has phase imbalance of 261.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005781_consumption`  
  Load '75_LVBus1005781_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005766_consumption`  
  Load '75_LVBus1005766_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005646_consumption`  
  Load '75_LVBus1005646_consumption' has phase imbalance of 286.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005453_consumption`  
  Load '75_LVBus1005453_consumption' has phase imbalance of 230.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005508_consumption`  
  Load '75_LVBus1005508_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005664_consumption`  
  Load '75_LVBus1005664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005749_consumption`  
  Load '75_LVBus1005749_consumption' has phase imbalance of 264.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005689_consumption`  
  Load '75_LVBus1005689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005391_consumption`  
  Load '75_LVBus1005391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005561_consumption`  
  Load '75_LVBus1005561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005462_consumption`  
  Load '75_LVBus1005462_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005731_consumption`  
  Load '75_LVBus1005731_consumption' has phase imbalance of 279.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005403_consumption`  
  Load '75_LVBus1005403_consumption' has phase imbalance of 138.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005849_consumption`  
  Load '75_LVBus1005849_consumption' has phase imbalance of 198.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005644_consumption`  
  Load '75_LVBus1005644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005759_consumption`  
  Load '75_LVBus1005759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005507_consumption`  
  Load '75_LVBus1005507_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005524_consumption`  
  Load '75_LVBus1005524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005494_consumption`  
  Load '75_LVBus1005494_consumption' has phase imbalance of 238.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005758_consumption`  
  Load '75_LVBus1005758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005743_consumption`  
  Load '75_LVBus1005743_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005384_consumption`  
  Load '75_LVBus1005384_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005843_consumption`  
  Load '75_LVBus1005843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005616_consumption`  
  Load '75_LVBus1005616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005426_consumption`  
  Load '75_LVBus1005426_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005612_consumption`  
  Load '75_LVBus1005612_consumption' has phase imbalance of 156.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005397_consumption`  
  Load '75_LVBus1005397_consumption' has phase imbalance of 142.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005780_consumption`  
  Load '75_LVBus1005780_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005855_consumption`  
  Load '75_LVBus1005855_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005564_consumption`  
  Load '75_LVBus1005564_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005425_consumption`  
  Load '75_LVBus1005425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005505_consumption`  
  Load '75_LVBus1005505_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005750_consumption`  
  Load '75_LVBus1005750_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005826_consumption`  
  Load '75_LVBus1005826_consumption' has phase imbalance of 183.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005471_consumption`  
  Load '75_LVBus1005471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005796_consumption`  
  Load '75_LVBus1005796_consumption' has phase imbalance of 143.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005613_consumption`  
  Load '75_LVBus1005613_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005682_consumption`  
  Load '75_LVBus1005682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005684_consumption`  
  Load '75_LVBus1005684_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005705_consumption`  
  Load '75_LVBus1005705_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005473_consumption`  
  Load '75_LVBus1005473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005574_consumption`  
  Load '75_LVBus1005574_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005748_consumption`  
  Load '75_LVBus1005748_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005528_consumption`  
  Load '75_LVBus1005528_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005429_consumption`  
  Load '75_LVBus1005429_consumption' has phase imbalance of 111.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005523_consumption`  
  Load '75_LVBus1005523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005502_consumption`  
  Load '75_LVBus1005502_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005675_consumption`  
  Load '75_LVBus1005675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005725_consumption`  
  Load '75_LVBus1005725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005376_consumption`  
  Load '75_LVBus1005376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005409_consumption`  
  Load '75_LVBus1005409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005640_consumption`  
  Load '75_LVBus1005640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005568_consumption`  
  Load '75_LVBus1005568_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005605_consumption`  
  Load '75_LVBus1005605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005719_consumption`  
  Load '75_LVBus1005719_consumption' has phase imbalance of 292.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005456_consumption`  
  Load '75_LVBus1005456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005785_consumption`  
  Load '75_LVBus1005785_consumption' has phase imbalance of 119.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005492_consumption`  
  Load '75_LVBus1005492_consumption' has phase imbalance of 281.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005652_consumption`  
  Load '75_LVBus1005652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005380_consumption`  
  Load '75_LVBus1005380_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005414_consumption`  
  Load '75_LVBus1005414_consumption' has phase imbalance of 288.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005379_consumption`  
  Load '75_LVBus1005379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005765_consumption`  
  Load '75_LVBus1005765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005463_consumption`  
  Load '75_LVBus1005463_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005447_consumption`  
  Load '75_LVBus1005447_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005760_consumption`  
  Load '75_LVBus1005760_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005663_consumption`  
  Load '75_LVBus1005663_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005513_consumption`  
  Load '75_LVBus1005513_consumption' has phase imbalance of 142.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005713_consumption`  
  Load '75_LVBus1005713_consumption' has phase imbalance of 87.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005658_consumption`  
  Load '75_LVBus1005658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005642_consumption`  
  Load '75_LVBus1005642_consumption' has phase imbalance of 259.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005534_consumption`  
  Load '75_LVBus1005534_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005832_consumption`  
  Load '75_LVBus1005832_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005535_consumption`  
  Load '75_LVBus1005535_consumption' has phase imbalance of 256.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005430_consumption`  
  Load '75_LVBus1005430_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005688_consumption`  
  Load '75_LVBus1005688_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005819_consumption`  
  Load '75_LVBus1005819_consumption' has phase imbalance of 123.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005720_consumption`  
  Load '75_LVBus1005720_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005485_consumption`  
  Load '75_LVBus1005485_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005691_consumption`  
  Load '75_LVBus1005691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005498_consumption`  
  Load '75_LVBus1005498_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005477_consumption`  
  Load '75_LVBus1005477_consumption' has phase imbalance of 259.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005538_consumption`  
  Load '75_LVBus1005538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005708_consumption`  
  Load '75_LVBus1005708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005635_consumption`  
  Load '75_LVBus1005635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005844_consumption`  
  Load '75_LVBus1005844_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005831_consumption`  
  Load '75_LVBus1005831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005522_consumption`  
  Load '75_LVBus1005522_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005754_consumption`  
  Load '75_LVBus1005754_consumption' has phase imbalance of 284.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005674_consumption`  
  Load '75_LVBus1005674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005438_consumption`  
  Load '75_LVBus1005438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005592_consumption`  
  Load '75_LVBus1005592_consumption' has phase imbalance of 283.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005461_consumption`  
  Load '75_LVBus1005461_consumption' has phase imbalance of 111.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005829_consumption`  
  Load '75_LVBus1005829_consumption' has phase imbalance of 273.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005628_consumption`  
  Load '75_LVBus1005628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005794_consumption`  
  Load '75_LVBus1005794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005728_consumption`  
  Load '75_LVBus1005728_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005559_consumption`  
  Load '75_LVBus1005559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005611_consumption`  
  Load '75_LVBus1005611_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005850_consumption`  
  Load '75_LVBus1005850_consumption' has phase imbalance of 198.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005621_consumption`  
  Load '75_LVBus1005621_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005420_consumption`  
  Load '75_LVBus1005420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005654_consumption`  
  Load '75_LVBus1005654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005779_consumption`  
  Load '75_LVBus1005779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005761_consumption`  
  Load '75_LVBus1005761_consumption' has phase imbalance of 255.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005432_consumption`  
  Load '75_LVBus1005432_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005827_consumption`  
  Load '75_LVBus1005827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005431_consumption`  
  Load '75_LVBus1005431_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005604_consumption`  
  Load '75_LVBus1005604_consumption' has phase imbalance of 230.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005818_consumption`  
  Load '75_LVBus1005818_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005810_consumption`  
  Load '75_LVBus1005810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005543_consumption`  
  Load '75_LVBus1005543_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005739_consumption`  
  Load '75_LVBus1005739_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005500_consumption`  
  Load '75_LVBus1005500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005786_consumption`  
  Load '75_LVBus1005786_consumption' has phase imbalance of 275.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005482_consumption`  
  Load '75_LVBus1005482_consumption' has phase imbalance of 271.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005735_consumption`  
  Load '75_LVBus1005735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005400_consumption`  
  Load '75_LVBus1005400_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005699_consumption`  
  Load '75_LVBus1005699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005782_consumption`  
  Load '75_LVBus1005782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005637_consumption`  
  Load '75_LVBus1005637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005466_consumption`  
  Load '75_LVBus1005466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005751_consumption`  
  Load '75_LVBus1005751_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005479_consumption`  
  Load '75_LVBus1005479_consumption' has phase imbalance of 287.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005643_consumption`  
  Load '75_LVBus1005643_consumption' has phase imbalance of 228.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005847_consumption`  
  Load '75_LVBus1005847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005857_consumption`  
  Load '75_LVBus1005857_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005717_consumption`  
  Load '75_LVBus1005717_consumption' has phase imbalance of 215.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005375_consumption`  
  Load '75_LVBus1005375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005770_consumption`  
  Load '75_LVBus1005770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005459_consumption`  
  Load '75_LVBus1005459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005509_consumption`  
  Load '75_LVBus1005509_consumption' has phase imbalance of 286.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005769_consumption`  
  Load '75_LVBus1005769_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005632_consumption`  
  Load '75_LVBus1005632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005648_consumption`  
  Load '75_LVBus1005648_consumption' has phase imbalance of 143.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005722_consumption`  
  Load '75_LVBus1005722_consumption' has phase imbalance of 283.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005576_consumption`  
  Load '75_LVBus1005576_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005416_consumption`  
  Load '75_LVBus1005416_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005546_consumption`  
  Load '75_LVBus1005546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005812_consumption`  
  Load '75_LVBus1005812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005740_consumption`  
  Load '75_LVBus1005740_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005727_consumption`  
  Load '75_LVBus1005727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005650_consumption`  
  Load '75_LVBus1005650_consumption' has phase imbalance of 212.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005396_consumption`  
  Load '75_LVBus1005396_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005475_consumption`  
  Load '75_LVBus1005475_consumption' has phase imbalance of 272.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005558_consumption`  
  Load '75_LVBus1005558_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005565_consumption`  
  Load '75_LVBus1005565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005784_consumption`  
  Load '75_LVBus1005784_consumption' has phase imbalance of 131.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005709_consumption`  
  Load '75_LVBus1005709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1005506_consumption`  
  Load '75_LVBus1005506_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 832 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1005677' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1005859' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_M.VIR' (MV, 11.78 kV) has an electrical reach of 34.63 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_LVBus1005436' (LV, 0.24 kV) has an electrical reach of 1.19 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_LVBus1005395' (LV, 0.24 kV) has an electrical reach of 1.69 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_LVBus1005564' (LV, 0.24 kV) has an electrical reach of 1.09 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1005616' (LV, 0.24 kV) has an electrical reach of 6.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  561 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  230 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1005374_consumption, 75_LVBus1005375_consumption, 75_LVBus1005376_consumption, 75_LVBus1005378_consumption, 75_LVBus1005379_consumption, 75_LVBus1005380_consumption, 75_LVBus1005384_consumption, 75_LVBus1005385_consumption, 75_LVBus1005388_consumption, 75_LVBus1005391_consumption, 75_LVBus1005392_consumption, 75_LVBus1005395_consumption, 75_LVBus1005396_consumption, 75_LVBus1005398_consumption, 75_LVBus1005399_consumption, 75_LVBus1005401_consumption, 75_LVBus1005409_consumption, 75_LVBus1005411_consumption, 75_LVBus1005416_consumption, 75_LVBus1005418_consumption, 75_LVBus1005420_consumption, 75_LVBus1005423_consumption, 75_LVBus1005425_consumption, 75_LVBus1005426_consumption, 75_LVBus1005428_consumption, 75_LVBus1005430_consumption, 75_LVBus1005431_consumption, 75_LVBus1005432_consumption, 75_LVBus1005438_consumption, 75_LVBus1005447_consumption, 75_LVBus1005450_consumption, 75_LVBus1005451_consumption, 75_LVBus1005453_consumption, 75_LVBus1005456_consumption, 75_LVBus1005459_consumption, 75_LVBus1005462_consumption, 75_LVBus1005463_consumption, 75_LVBus1005466_consumption, 75_LVBus1005470_consumption, 75_LVBus1005471_consumption, 75_LVBus1005473_consumption, 75_LVBus1005474_consumption, 75_LVBus1005475_consumption, 75_LVBus1005479_consumption, 75_LVBus1005480_consumption, 75_LVBus1005481_consumption, 75_LVBus1005482_consumption, 75_LVBus1005485_consumption, 75_LVBus1005490_consumption, 75_LVBus1005492_consumption, 75_LVBus1005494_consumption, 75_LVBus1005498_consumption, 75_LVBus1005500_consumption, 75_LVBus1005501_consumption, 75_LVBus1005503_consumption, 75_LVBus1005504_consumption, 75_LVBus1005505_consumption, 75_LVBus1005507_consumption, 75_LVBus1005508_consumption, 75_LVBus1005509_consumption, 75_LVBus1005511_consumption, 75_LVBus1005515_consumption, 75_LVBus1005518_consumption, 75_LVBus1005519_consumption, 75_LVBus1005521_consumption, 75_LVBus1005522_consumption, 75_LVBus1005523_consumption, 75_LVBus1005524_consumption, 75_LVBus1005525_consumption, 75_LVBus1005527_consumption, 75_LVBus1005528_consumption, 75_LVBus1005534_consumption, 75_LVBus1005535_consumption, 75_LVBus1005536_consumption, 75_LVBus1005538_consumption, 75_LVBus1005539_consumption, 75_LVBus1005540_consumption, 75_LVBus1005543_consumption, 75_LVBus1005545_consumption, 75_LVBus1005546_consumption, 75_LVBus1005547_consumption, 75_LVBus1005551_consumption, 75_LVBus1005554_consumption, 75_LVBus1005555_consumption, 75_LVBus1005557_consumption, 75_LVBus1005558_consumption, 75_LVBus1005559_consumption, 75_LVBus1005561_consumption, 75_LVBus1005564_consumption, 75_LVBus1005565_consumption, 75_LVBus1005566_consumption, 75_LVBus1005567_consumption, 75_LVBus1005568_consumption, 75_LVBus1005569_consumption, 75_LVBus1005572_consumption, 75_LVBus1005574_consumption, 75_LVBus1005575_consumption, 75_LVBus1005576_consumption, 75_LVBus1005579_consumption, 75_LVBus1005580_consumption, 75_LVBus1005581_consumption, 75_LVBus1005589_consumption, 75_LVBus1005592_consumption, 75_LVBus1005596_consumption, 75_LVBus1005605_consumption, 75_LVBus1005610_consumption, 75_LVBus1005612_consumption, 75_LVBus1005613_consumption, 75_LVBus1005614_consumption, 75_LVBus1005616_consumption, 75_LVBus1005620_consumption, 75_LVBus1005625_consumption, 75_LVBus1005626_consumption, 75_LVBus1005628_consumption, 75_LVBus1005629_consumption, 75_LVBus1005630_consumption, 75_LVBus1005632_consumption, 75_LVBus1005634_consumption, 75_LVBus1005635_consumption, 75_LVBus1005637_consumption, 75_LVBus1005640_consumption, 75_LVBus1005641_consumption, 75_LVBus1005642_consumption, 75_LVBus1005644_consumption, 75_LVBus1005646_consumption, 75_LVBus1005650_consumption, 75_LVBus1005652_consumption, 75_LVBus1005654_consumption, 75_LVBus1005658_consumption, 75_LVBus1005660_consumption, 75_LVBus1005663_consumption, 75_LVBus1005664_consumption, 75_LVBus1005665_consumption, 75_LVBus1005668_consumption, 75_LVBus1005671_consumption, 75_LVBus1005672_consumption, 75_LVBus1005673_consumption, 75_LVBus1005674_consumption, 75_LVBus1005675_consumption, 75_LVBus1005681_consumption, 75_LVBus1005682_consumption, 75_LVBus1005684_consumption, 75_LVBus1005688_consumption, 75_LVBus1005689_consumption, 75_LVBus1005690_consumption, 75_LVBus1005691_consumption, 75_LVBus1005692_consumption, 75_LVBus1005694_consumption, 75_LVBus1005699_consumption, 75_LVBus1005701_consumption, 75_LVBus1005702_consumption, 75_LVBus1005704_consumption, 75_LVBus1005706_consumption, 75_LVBus1005707_consumption, 75_LVBus1005708_consumption, 75_LVBus1005709_consumption, 75_LVBus1005711_consumption, 75_LVBus1005714_consumption, 75_LVBus1005716_consumption, 75_LVBus1005717_consumption, 75_LVBus1005719_consumption, 75_LVBus1005720_consumption, 75_LVBus1005722_consumption, 75_LVBus1005725_consumption, 75_LVBus1005726_consumption, 75_LVBus1005727_consumption, 75_LVBus1005728_consumption, 75_LVBus1005731_consumption, 75_LVBus1005735_consumption, 75_LVBus1005739_consumption, 75_LVBus1005740_consumption, 75_LVBus1005741_consumption, 75_LVBus1005745_consumption, 75_LVBus1005747_consumption, 75_LVBus1005750_consumption, 75_LVBus1005751_consumption, 75_LVBus1005753_consumption, 75_LVBus1005754_consumption, 75_LVBus1005755_consumption, 75_LVBus1005756_consumption, 75_LVBus1005758_consumption, 75_LVBus1005759_consumption, 75_LVBus1005760_consumption, 75_LVBus1005761_consumption, 75_LVBus1005764_consumption, 75_LVBus1005765_consumption, 75_LVBus1005766_consumption, 75_LVBus1005767_consumption, 75_LVBus1005768_consumption, 75_LVBus1005769_consumption, 75_LVBus1005770_consumption, 75_LVBus1005771_consumption, 75_LVBus1005772_consumption, 75_LVBus1005773_consumption, 75_LVBus1005779_consumption, 75_LVBus1005782_consumption, 75_LVBus1005786_consumption, 75_LVBus1005792_consumption, 75_LVBus1005793_consumption, 75_LVBus1005794_consumption, 75_LVBus1005797_consumption, 75_LVBus1005810_consumption, 75_LVBus1005811_consumption, 75_LVBus1005812_consumption, 75_LVBus1005816_consumption, 75_LVBus1005817_consumption, 75_LVBus1005818_consumption, 75_LVBus1005824_consumption, 75_LVBus1005825_consumption, 75_LVBus1005826_consumption, 75_LVBus1005827_consumption, 75_LVBus1005828_consumption, 75_LVBus1005829_consumption, 75_LVBus1005830_consumption, 75_LVBus1005831_consumption, 75_LVBus1005832_consumption, 75_LVBus1005833_consumption, 75_LVBus1005837_consumption, 75_LVBus1005838_consumption, 75_LVBus1005839_consumption, 75_LVBus1005840_consumption, 75_LVBus1005843_consumption, 75_LVBus1005844_consumption, 75_LVBus1005847_consumption, 75_LVBus1005849_consumption, 75_LVBus1005850_consumption, 75_LVBus1005854_consumption, 75_LVBus1005855_consumption, 75_LVBus1005856_consumption, 75_LVBus1005857_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  416 group(s) of loads (832 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  10 group(s) of series lines (20 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  534 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1005366_production, 75_LVBus1005368_consumption, 75_LVBus1005368_production, 75_LVBus1005370_production, 75_LVBus1005371_consumption, 75_LVBus1005371_production, 75_LVBus1005372_consumption, 75_LVBus1005372_production, 75_LVBus1005373_consumption, 75_LVBus1005373_production, 75_LVBus1005374_production, 75_LVBus1005375_production, 75_LVBus1005376_production, 75_LVBus1005378_production, 75_LVBus1005379_production, 75_LVBus1005380_production, 75_LVBus1005382_consumption, 75_LVBus1005382_production, 75_LVBus1005383_production, 75_LVBus1005384_production, 75_LVBus1005385_production, 75_LVBus1005388_production, 75_LVBus1005390_production, 75_LVBus1005391_production, 75_LVBus1005392_production, 75_LVBus1005393_consumption, 75_LVBus1005393_production, 75_LVBus1005395_production, 75_LVBus1005396_production, 75_LVBus1005397_production, 75_LVBus1005398_production, 75_LVBus1005399_production, 75_LVBus1005400_production, 75_LVBus1005401_production, 75_LVBus1005403_production, 75_LVBus1005404_production, 75_LVBus1005405_production, 75_LVBus1005406_production, 75_LVBus1005407_consumption, 75_LVBus1005407_production, 75_LVBus1005408_consumption, 75_LVBus1005408_production, 75_LVBus1005409_production, 75_LVBus1005410_production, 75_LVBus1005411_production, 75_LVBus1005412_consumption, 75_LVBus1005412_production, 75_LVBus1005413_production, 75_LVBus1005414_production, 75_LVBus1005416_production, 75_LVBus1005418_production, 75_LVBus1005419_consumption, 75_LVBus1005419_production, 75_LVBus1005420_production, 75_LVBus1005421_consumption, 75_LVBus1005421_production, 75_LVBus1005422_consumption, 75_LVBus1005422_production, 75_LVBus1005423_production, 75_LVBus1005425_production, 75_LVBus1005426_production, 75_LVBus1005427_consumption, 75_LVBus1005427_production, 75_LVBus1005428_production, 75_LVBus1005429_production, 75_LVBus1005430_production, 75_LVBus1005431_production, 75_LVBus1005432_production, 75_LVBus1005436_consumption, 75_LVBus1005436_production, 75_LVBus1005437_consumption, 75_LVBus1005437_production, 75_LVBus1005438_production, 75_LVBus1005439_consumption, 75_LVBus1005439_production, 75_LVBus1005440_consumption, 75_LVBus1005440_production, 75_LVBus1005441_consumption, 75_LVBus1005441_production, 75_LVBus1005442_consumption, 75_LVBus1005442_production, 75_LVBus1005443_consumption, 75_LVBus1005443_production, 75_LVBus1005444_consumption, 75_LVBus1005444_production, 75_LVBus1005445_consumption, 75_LVBus1005445_production, 75_LVBus1005447_production, 75_LVBus1005448_consumption, 75_LVBus1005448_production, 75_LVBus1005449_consumption, 75_LVBus1005449_production, 75_LVBus1005450_production, 75_LVBus1005451_production, 75_LVBus1005452_consumption, 75_LVBus1005452_production, 75_LVBus1005453_production, 75_LVBus1005454_consumption, 75_LVBus1005454_production, 75_LVBus1005456_production, 75_LVBus1005458_consumption, 75_LVBus1005458_production, 75_LVBus1005459_production, 75_LVBus1005460_production, 75_LVBus1005461_production, 75_LVBus1005462_production, 75_LVBus1005463_production, 75_LVBus1005464_consumption, 75_LVBus1005464_production, 75_LVBus1005465_consumption, 75_LVBus1005465_production, 75_LVBus1005466_production, 75_LVBus1005468_consumption, 75_LVBus1005468_production, 75_LVBus1005469_consumption, 75_LVBus1005469_production, 75_LVBus1005470_production, 75_LVBus1005471_production, 75_LVBus1005473_production, 75_LVBus1005474_production, 75_LVBus1005475_production, 75_LVBus1005476_production, 75_LVBus1005477_production, 75_LVBus1005479_production, 75_LVBus1005480_production, 75_LVBus1005481_production, 75_LVBus1005482_production, 75_LVBus1005483_production, 75_LVBus1005484_production, 75_LVBus1005485_production, 75_LVBus1005490_production, 75_LVBus1005491_production, 75_LVBus1005492_production, 75_LVBus1005493_consumption, 75_LVBus1005493_production, 75_LVBus1005494_production, 75_LVBus1005495_consumption, 75_LVBus1005495_production, 75_LVBus1005497_consumption, 75_LVBus1005497_production, 75_LVBus1005498_production, 75_LVBus1005499_consumption, 75_LVBus1005499_production, 75_LVBus1005500_production, 75_LVBus1005501_production, 75_LVBus1005502_production, 75_LVBus1005503_production, 75_LVBus1005504_production, 75_LVBus1005505_production, 75_LVBus1005506_production, 75_LVBus1005507_production, 75_LVBus1005508_production, 75_LVBus1005509_production, 75_LVBus1005510_consumption, 75_LVBus1005510_production, 75_LVBus1005511_production, 75_LVBus1005512_consumption, 75_LVBus1005512_production, 75_LVBus1005513_production, 75_LVBus1005514_consumption, 75_LVBus1005514_production, 75_LVBus1005515_production, 75_LVBus1005517_consumption, 75_LVBus1005517_production, 75_LVBus1005518_production, 75_LVBus1005519_production, 75_LVBus1005520_consumption, 75_LVBus1005520_production, 75_LVBus1005521_production, 75_LVBus1005522_production, 75_LVBus1005523_production, 75_LVBus1005524_production, 75_LVBus1005525_production, 75_LVBus1005526_consumption, 75_LVBus1005526_production, 75_LVBus1005527_production, 75_LVBus1005528_production, 75_LVBus1005534_production, 75_LVBus1005535_production, 75_LVBus1005536_production, 75_LVBus1005537_consumption, 75_LVBus1005537_production, 75_LVBus1005538_production, 75_LVBus1005539_production, 75_LVBus1005540_production, 75_LVBus1005542_consumption, 75_LVBus1005542_production, 75_LVBus1005543_production, 75_LVBus1005544_consumption, 75_LVBus1005544_production, 75_LVBus1005545_production, 75_LVBus1005546_production, 75_LVBus1005547_production, 75_LVBus1005551_production, 75_LVBus1005553_consumption, 75_LVBus1005553_production, 75_LVBus1005554_production, 75_LVBus1005555_production, 75_LVBus1005557_production, 75_LVBus1005558_production, 75_LVBus1005559_production, 75_LVBus1005560_consumption, 75_LVBus1005560_production, 75_LVBus1005561_production, 75_LVBus1005562_consumption, 75_LVBus1005562_production, 75_LVBus1005564_production, 75_LVBus1005565_production, 75_LVBus1005566_production, 75_LVBus1005567_production, 75_LVBus1005568_production, 75_LVBus1005569_production, 75_LVBus1005570_consumption, 75_LVBus1005570_production, 75_LVBus1005572_production, 75_LVBus1005574_production, 75_LVBus1005575_production, 75_LVBus1005576_production, 75_LVBus1005578_consumption, 75_LVBus1005578_production, 75_LVBus1005579_production, 75_LVBus1005580_production, 75_LVBus1005581_production, 75_LVBus1005582_consumption, 75_LVBus1005582_production, 75_LVBus1005583_consumption, 75_LVBus1005583_production, 75_LVBus1005584_consumption, 75_LVBus1005584_production, 75_LVBus1005585_consumption, 75_LVBus1005585_production, 75_LVBus1005587_production, 75_LVBus1005588_consumption, 75_LVBus1005588_production, 75_LVBus1005589_production, 75_LVBus1005591_consumption, 75_LVBus1005591_production, 75_LVBus1005592_production, 75_LVBus1005594_consumption, 75_LVBus1005594_production, 75_LVBus1005595_consumption, 75_LVBus1005595_production, 75_LVBus1005596_production, 75_LVBus1005598_consumption, 75_LVBus1005598_production, 75_LVBus1005600_consumption, 75_LVBus1005600_production, 75_LVBus1005602_production, 75_LVBus1005604_production, 75_LVBus1005605_production, 75_LVBus1005607_consumption, 75_LVBus1005607_production, 75_LVBus1005609_production, 75_LVBus1005610_production, 75_LVBus1005611_production, 75_LVBus1005612_production, 75_LVBus1005613_production, 75_LVBus1005614_production, 75_LVBus1005616_production, 75_LVBus1005618_consumption, 75_LVBus1005618_production, 75_LVBus1005619_consumption, 75_LVBus1005619_production, 75_LVBus1005620_production, 75_LVBus1005621_production, 75_LVBus1005622_consumption, 75_LVBus1005622_production, 75_LVBus1005624_consumption, 75_LVBus1005624_production, 75_LVBus1005625_production, 75_LVBus1005626_production, 75_LVBus1005627_consumption, 75_LVBus1005627_production, 75_LVBus1005628_production, 75_LVBus1005629_production, 75_LVBus1005630_production, 75_LVBus1005631_consumption, 75_LVBus1005631_production, 75_LVBus1005632_production, 75_LVBus1005633_consumption, 75_LVBus1005633_production, 75_LVBus1005634_production, 75_LVBus1005635_production, 75_LVBus1005637_production, 75_LVBus1005638_production, 75_LVBus1005639_consumption, 75_LVBus1005639_production, 75_LVBus1005640_production, 75_LVBus1005641_production, 75_LVBus1005642_production, 75_LVBus1005643_production, 75_LVBus1005644_production, 75_LVBus1005645_production, 75_LVBus1005646_production, 75_LVBus1005648_production, 75_LVBus1005649_production, 75_LVBus1005650_production, 75_LVBus1005652_production, 75_LVBus1005653_consumption, 75_LVBus1005653_production, 75_LVBus1005654_production, 75_LVBus1005655_consumption, 75_LVBus1005655_production, 75_LVBus1005656_consumption, 75_LVBus1005656_production, 75_LVBus1005658_production, 75_LVBus1005659_consumption, 75_LVBus1005659_production, 75_LVBus1005660_production, 75_LVBus1005661_consumption, 75_LVBus1005661_production, 75_LVBus1005663_production, 75_LVBus1005664_production, 75_LVBus1005665_production, 75_LVBus1005667_consumption, 75_LVBus1005667_production, 75_LVBus1005668_production, 75_LVBus1005670_consumption, 75_LVBus1005670_production, 75_LVBus1005671_production, 75_LVBus1005672_production, 75_LVBus1005673_production, 75_LVBus1005674_production, 75_LVBus1005675_production, 75_LVBus1005677_consumption, 75_LVBus1005677_production, 75_LVBus1005678_consumption, 75_LVBus1005678_production, 75_LVBus1005679_production, 75_LVBus1005681_production, 75_LVBus1005682_production, 75_LVBus1005683_production, 75_LVBus1005684_production, 75_LVBus1005686_consumption, 75_LVBus1005686_production, 75_LVBus1005687_consumption, 75_LVBus1005687_production, 75_LVBus1005688_production, 75_LVBus1005689_production, 75_LVBus1005690_production, 75_LVBus1005691_production, 75_LVBus1005692_production, 75_LVBus1005693_consumption, 75_LVBus1005693_production, 75_LVBus1005694_production, 75_LVBus1005696_consumption, 75_LVBus1005696_production, 75_LVBus1005697_consumption, 75_LVBus1005697_production, 75_LVBus1005698_consumption, 75_LVBus1005698_production, 75_LVBus1005699_production, 75_LVBus1005700_consumption, 75_LVBus1005700_production, 75_LVBus1005701_production, 75_LVBus1005702_production, 75_LVBus1005704_production, 75_LVBus1005705_production, 75_LVBus1005706_production, 75_LVBus1005707_production, 75_LVBus1005708_production, 75_LVBus1005709_production, 75_LVBus1005711_production, 75_LVBus1005713_production, 75_LVBus1005714_production, 75_LVBus1005716_production, 75_LVBus1005717_production, 75_LVBus1005718_production, 75_LVBus1005719_production, 75_LVBus1005720_production, 75_LVBus1005721_production, 75_LVBus1005722_production, 75_LVBus1005723_production, 75_LVBus1005724_production, 75_LVBus1005725_production, 75_LVBus1005726_production, 75_LVBus1005727_production, 75_LVBus1005728_production, 75_LVBus1005729_production, 75_LVBus1005731_production, 75_LVBus1005732_consumption, 75_LVBus1005732_production, 75_LVBus1005733_production, 75_LVBus1005734_production, 75_LVBus1005735_production, 75_LVBus1005736_production, 75_LVBus1005738_production, 75_LVBus1005739_production, 75_LVBus1005740_production, 75_LVBus1005741_production, 75_LVBus1005743_production, 75_LVBus1005744_consumption, 75_LVBus1005744_production, 75_LVBus1005745_production, 75_LVBus1005746_production, 75_LVBus1005747_production, 75_LVBus1005748_production, 75_LVBus1005749_production, 75_LVBus1005750_production, 75_LVBus1005751_production, 75_LVBus1005752_consumption, 75_LVBus1005752_production, 75_LVBus1005753_production, 75_LVBus1005754_production, 75_LVBus1005755_production, 75_LVBus1005756_production, 75_LVBus1005757_consumption, 75_LVBus1005757_production, 75_LVBus1005758_production, 75_LVBus1005759_production, 75_LVBus1005760_production, 75_LVBus1005761_production, 75_LVBus1005763_production, 75_LVBus1005764_production, 75_LVBus1005765_production, 75_LVBus1005766_production, 75_LVBus1005767_production, 75_LVBus1005768_production, 75_LVBus1005769_production, 75_LVBus1005770_production, 75_LVBus1005771_production, 75_LVBus1005772_production, 75_LVBus1005773_production, 75_LVBus1005774_production, 75_LVBus1005776_production, 75_LVBus1005777_consumption, 75_LVBus1005777_production, 75_LVBus1005778_consumption, 75_LVBus1005778_production, 75_LVBus1005779_production, 75_LVBus1005780_production, 75_LVBus1005781_production, 75_LVBus1005782_production, 75_LVBus1005784_production, 75_LVBus1005785_production, 75_LVBus1005786_production, 75_LVBus1005787_consumption, 75_LVBus1005787_production, 75_LVBus1005788_consumption, 75_LVBus1005788_production, 75_LVBus1005789_consumption, 75_LVBus1005789_production, 75_LVBus1005791_consumption, 75_LVBus1005791_production, 75_LVBus1005792_production, 75_LVBus1005793_production, 75_LVBus1005794_production, 75_LVBus1005795_production, 75_LVBus1005796_production, 75_LVBus1005797_production, 75_LVBus1005798_production, 75_LVBus1005802_production, 75_LVBus1005804_consumption, 75_LVBus1005804_production, 75_LVBus1005805_production, 75_LVBus1005806_production, 75_LVBus1005807_consumption, 75_LVBus1005807_production, 75_LVBus1005809_consumption, 75_LVBus1005809_production, 75_LVBus1005810_production, 75_LVBus1005811_production, 75_LVBus1005812_production, 75_LVBus1005814_consumption, 75_LVBus1005814_production, 75_LVBus1005815_consumption, 75_LVBus1005815_production, 75_LVBus1005816_production, 75_LVBus1005817_production, 75_LVBus1005818_production, 75_LVBus1005819_production, 75_LVBus1005821_consumption, 75_LVBus1005821_production, 75_LVBus1005822_consumption, 75_LVBus1005822_production, 75_LVBus1005823_consumption, 75_LVBus1005823_production, 75_LVBus1005824_production, 75_LVBus1005825_production, 75_LVBus1005826_production, 75_LVBus1005827_production, 75_LVBus1005828_production, 75_LVBus1005829_production, 75_LVBus1005830_production, 75_LVBus1005831_production, 75_LVBus1005832_production, 75_LVBus1005833_production, 75_LVBus1005834_consumption, 75_LVBus1005834_production, 75_LVBus1005836_consumption, 75_LVBus1005836_production, 75_LVBus1005837_production, 75_LVBus1005838_production, 75_LVBus1005839_production, 75_LVBus1005840_production, 75_LVBus1005842_production, 75_LVBus1005843_production, 75_LVBus1005844_production, 75_LVBus1005846_consumption, 75_LVBus1005846_production, 75_LVBus1005847_production, 75_LVBus1005848_consumption, 75_LVBus1005848_production, 75_LVBus1005849_production, 75_LVBus1005850_production, 75_LVBus1005851_consumption, 75_LVBus1005851_production, 75_LVBus1005852_consumption, 75_LVBus1005852_production, 75_LVBus1005853_consumption, 75_LVBus1005853_production, 75_LVBus1005854_production, 75_LVBus1005855_production, 75_LVBus1005856_production, 75_LVBus1005857_production, 75_LVBus1005859_production, 75_LVBus1925392_consumption, 75_LVBus1925392_production, 75_MVLV029809_consumption, 75_MVLV029809_production, 75_MVLV061283_consumption, 75_MVLV061283_production, 75_MVLV067136_consumption, 75_MVLV067136_production, 75_MVLV085210_consumption, 75_MVLV085210_production, 75_MVLV111344_consumption, 75_MVLV111344_production, 75_MVLV147762_consumption, 75_MVLV147762_production, 75_MVLV152518_consumption, 75_MVLV152518_production, 75_MVLV167393_consumption, 75_MVLV167393_production.

