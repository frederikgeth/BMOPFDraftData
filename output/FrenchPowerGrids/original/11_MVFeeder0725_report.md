# BMOPF Network Summary: 11_MVFeeder0725

**Generated:** 2026-10-01 23:33:54  
**Findings:** 0 errors · 5 warnings · 200 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 335 |  |
| line | 324 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 626 | 2.229 MW, 668.7 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 10 |  |
| switch | 0 |  |
| transformer | 10 | Dyn11×10 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 14 | 13 | 4 | 0 |
| LV_236V | 236.0 V | 321 | 311 | 622 | 0 |

**Transformer transitions:**

- `11_MVLV22874_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV73493_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV14690_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV35159_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV23213_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV73455_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV66105_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV66984_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV36338_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV16194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 112 |
| Tree depth (max hops) | 21 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 335 | 1 | 334 | 0 | 0 | 0 |
| Tier LV_236V | 321 | 10 | 311 | 0 | 0 | 0 |
| Tier MV_11.8kV | 14 | 1 | 13 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 10; skipped invalid branches: 0.

Galvanic zones: 11; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_BUZEN | MV_11.8kV | 14 | 0 | 0 | 10 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1326 declared bus terminals; 1283 mapped line/closed-switch conductor edges; 43 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 60500.0 | 3.435 | 1878 |
| q_nom | 0.0 | 18100.0 | 3.435 | 1878 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.369 | 1210.0 | 1.879 | 324 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 2.2e6 | 1.273 | 10 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 430 of 626 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536613_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536361_consumption' has phase imbalance of 149.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1338566_consumption' has phase imbalance of 46.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1315224_consumption' has phase imbalance of 82.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536533_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295373_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536363_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536434_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536475_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536428_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536442_consumption' has phase imbalance of 255.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536501_consumption' has phase imbalance of 44.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536632_consumption' has phase imbalance of 80.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536530_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1311664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536426_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536567_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536560_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536498_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295410_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536612_consumption' has phase imbalance of 273.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536465_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1287196_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295368_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536574_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536451_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536461_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536407_consumption' has phase imbalance of 36.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536522_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536623_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536554_consumption' has phase imbalance of 261.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536353_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536547_consumption' has phase imbalance of 126.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1352410_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536416_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536528_consumption' has phase imbalance of 107.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536534_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536555_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1285783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536568_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536502_consumption' has phase imbalance of 64.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536404_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536578_consumption' has phase imbalance of 259.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536355_consumption' has phase imbalance of 52.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536449_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1311665_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536448_consumption' has phase imbalance of 37.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536474_consumption' has phase imbalance of 78.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1285134_consumption' has phase imbalance of 271.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536582_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295370_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1300463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536356_consumption' has phase imbalance of 254.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536358_consumption' has phase imbalance of 143.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536350_consumption' has phase imbalance of 31.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536548_consumption' has phase imbalance of 39.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536546_consumption' has phase imbalance of 53.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536523_consumption' has phase imbalance of 211.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536466_consumption' has phase imbalance of 51.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536460_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536516_consumption' has phase imbalance of 290.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536571_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536354_consumption' has phase imbalance of 101.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536570_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536573_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536627_consumption' has phase imbalance of 94.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536443_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1297362_consumption' has phase imbalance of 27.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536628_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536467_consumption' has phase imbalance of 24.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536617_consumption' has phase imbalance of 106.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1289345_consumption' has phase imbalance of 45.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536626_consumption' has phase imbalance of 231.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536535_consumption' has phase imbalance of 222.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536630_consumption' has phase imbalance of 124.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536420_consumption' has phase imbalance of 23.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536422_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536455_consumption' has phase imbalance of 38.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536440_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536411_consumption' has phase imbalance of 177.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536409_consumption' has phase imbalance of 70.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536584_consumption' has phase imbalance of 125.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536614_consumption' has phase imbalance of 136.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536349_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536491_consumption' has phase imbalance of 63.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536398_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536519_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1300466_consumption' has phase imbalance of 188.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536340_consumption' has phase imbalance of 26.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536468_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536589_consumption' has phase imbalance of 28.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536445_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536437_consumption' has phase imbalance of 253.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536615_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536590_consumption' has phase imbalance of 95.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536620_consumption' has phase imbalance of 65.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536352_consumption' has phase imbalance of 231.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536400_consumption' has phase imbalance of 56.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295366_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536540_consumption' has phase imbalance of 185.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1300465_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536610_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295369_consumption' has phase imbalance of 230.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536424_consumption' has phase imbalance of 90.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536591_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536588_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536518_consumption' has phase imbalance of 113.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1300462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536473_consumption' has phase imbalance of 106.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536412_consumption' has phase imbalance of 124.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536413_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536396_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536635_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1285782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1285784_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536596_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536441_consumption' has phase imbalance of 299.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536604_consumption' has phase imbalance of 35.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536394_consumption' has phase imbalance of 240.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536493_consumption' has phase imbalance of 29.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295411_consumption' has phase imbalance of 147.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536525_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536417_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1300418_consumption' has phase imbalance of 71.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536597_consumption' has phase imbalance of 261.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295374_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536389_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536558_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536576_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536478_consumption' has phase imbalance of 70.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536427_consumption' has phase imbalance of 70.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1300461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536489_consumption' has phase imbalance of 195.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536543_consumption' has phase imbalance of 49.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1300464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536488_consumption' has phase imbalance of 47.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536464_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536447_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1295372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536621_consumption' has phase imbalance of 58.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1338558_consumption' has phase imbalance of 32.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0536551_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 626 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_BUZEN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.229 MW |
| Total load Q | 668.7 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV22874_Transformer | 275.0 kVA | 64.2% |
| 11_MVLV73493_Transformer | 440.0 kVA | 79.6% |
| 11_MVLV14690_Transformer | 440.0 kVA | 52.7% |
| 11_MVLV35159_Transformer | 275.0 kVA | 71.2% |
| 11_MVLV23213_Transformer | 346.5 kVA | 89.0% |
| 11_MVLV73455_Transformer | 275.0 kVA | 52.7% |
| 11_MVLV66105_Transformer | 110.0 kVA | 54.4% |
| 11_MVLV66984_Transformer | 2.2 MVA | 15.7% |
| 11_MVLV36338_Transformer | 176.0 kVA | 79.8% |
| 11_MVLV16194_Transformer | 275.0 kVA | 66.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.23 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 335 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 335 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 14 |
| LV_236V | 4-wire | 321 / 321 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 321 |
| Neutral branches | 311 |
| Grounding points | 10 |
| Neutral sections | 10 |
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
| 11.78 kV | 14 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 46 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 52 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 11 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1390.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 321 / 14 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 431 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 431 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0536338_consumption, 11_LVBus0536338_production, 11_LVBus0536339_consumption, 11_LVBus0536339_production, 11_LVBus0536340_production, 11_LVBus0536341_consumption, 11_LVBus0536341_production, 11_LVBus0536342_consumption, 11_LVBus0536342_production, 11_LVBus0536343_consumption, 11_LVBus0536343_production, 11_LVBus0536344_consumption, 11_LVBus0536344_production, 11_LVBus0536345_consumption, 11_LVBus0536345_production, 11_LVBus0536347_consumption, 11_LVBus0536347_production, 11_LVBus0536348_consumption, 11_LVBus0536348_production, 11_LVBus0536349_production, 11_LVBus0536350_production, 11_LVBus0536352_production, 11_LVBus0536353_production, 11_LVBus0536354_production, 11_LVBus0536355_production, 11_LVBus0536356_production, 11_LVBus0536357_consumption, 11_LVBus0536357_production, 11_LVBus0536358_production, 11_LVBus0536360_consumption, 11_LVBus0536360_production, 11_LVBus0536361_production, 11_LVBus0536363_production, 11_LVBus0536364_consumption, 11_LVBus0536364_production, 11_LVBus0536365_consumption, 11_LVBus0536365_production, 11_LVBus0536366_consumption, 11_LVBus0536366_production, 11_LVBus0536367_consumption, 11_LVBus0536367_production, 11_LVBus0536368_consumption, 11_LVBus0536368_production, 11_LVBus0536369_consumption, 11_LVBus0536369_production, 11_LVBus0536371_consumption, 11_LVBus0536371_production, 11_LVBus0536372_consumption, 11_LVBus0536372_production, 11_LVBus0536373_consumption, 11_LVBus0536373_production, 11_LVBus0536374_consumption, 11_LVBus0536374_production, 11_LVBus0536375_consumption, 11_LVBus0536375_production, 11_LVBus0536376_consumption, 11_LVBus0536376_production, 11_LVBus0536377_consumption, 11_LVBus0536377_production, 11_LVBus0536378_consumption, 11_LVBus0536378_production, 11_LVBus0536379_consumption, 11_LVBus0536379_production, 11_LVBus0536381_consumption, 11_LVBus0536381_production, 11_LVBus0536382_consumption, 11_LVBus0536382_production, 11_LVBus0536383_consumption, 11_LVBus0536383_production, 11_LVBus0536384_consumption, 11_LVBus0536384_production, 11_LVBus0536385_consumption, 11_LVBus0536385_production, 11_LVBus0536386_consumption, 11_LVBus0536386_production, 11_LVBus0536387_consumption, 11_LVBus0536387_production, 11_LVBus0536388_consumption, 11_LVBus0536388_production, 11_LVBus0536389_production, 11_LVBus0536391_consumption, 11_LVBus0536391_production, 11_LVBus0536394_production, 11_LVBus0536395_consumption, 11_LVBus0536395_production, 11_LVBus0536396_production, 11_LVBus0536397_production, 11_LVBus0536398_production, 11_LVBus0536399_production, 11_LVBus0536400_production, 11_LVBus0536401_production, 11_LVBus0536402_consumption, 11_LVBus0536402_production, 11_LVBus0536403_consumption, 11_LVBus0536403_production, 11_LVBus0536404_production, 11_LVBus0536405_production, 11_LVBus0536406_consumption, 11_LVBus0536406_production, 11_LVBus0536407_production, 11_LVBus0536409_production, 11_LVBus0536411_production, 11_LVBus0536412_production, 11_LVBus0536413_production, 11_LVBus0536414_consumption, 11_LVBus0536414_production, 11_LVBus0536415_consumption, 11_LVBus0536415_production, 11_LVBus0536416_production, 11_LVBus0536417_production, 11_LVBus0536418_consumption, 11_LVBus0536418_production, 11_LVBus0536420_production, 11_LVBus0536422_production, 11_LVBus0536423_consumption, 11_LVBus0536423_production, 11_LVBus0536424_production, 11_LVBus0536425_production, 11_LVBus0536426_production, 11_LVBus0536427_production, 11_LVBus0536428_production, 11_LVBus0536429_production, 11_LVBus0536430_consumption, 11_LVBus0536430_production, 11_LVBus0536432_consumption, 11_LVBus0536432_production, 11_LVBus0536433_consumption, 11_LVBus0536433_production, 11_LVBus0536434_production, 11_LVBus0536435_consumption, 11_LVBus0536435_production, 11_LVBus0536436_production, 11_LVBus0536437_production, 11_LVBus0536438_consumption, 11_LVBus0536438_production, 11_LVBus0536439_consumption, 11_LVBus0536439_production, 11_LVBus0536440_production, 11_LVBus0536441_production, 11_LVBus0536442_production, 11_LVBus0536443_production, 11_LVBus0536444_production, 11_LVBus0536445_production, 11_LVBus0536446_consumption, 11_LVBus0536446_production, 11_LVBus0536447_production, 11_LVBus0536448_production, 11_LVBus0536449_production, 11_LVBus0536450_production, 11_LVBus0536451_production, 11_LVBus0536453_consumption, 11_LVBus0536453_production, 11_LVBus0536455_production, 11_LVBus0536456_consumption, 11_LVBus0536456_production, 11_LVBus0536457_production, 11_LVBus0536458_production, 11_LVBus0536459_production, 11_LVBus0536460_production, 11_LVBus0536461_production, 11_LVBus0536462_consumption, 11_LVBus0536462_production, 11_LVBus0536463_production, 11_LVBus0536464_production, 11_LVBus0536465_production, 11_LVBus0536466_production, 11_LVBus0536467_production, 11_LVBus0536468_production, 11_LVBus0536469_production, 11_LVBus0536471_consumption, 11_LVBus0536471_production, 11_LVBus0536472_consumption, 11_LVBus0536472_production, 11_LVBus0536473_production, 11_LVBus0536474_production, 11_LVBus0536475_production, 11_LVBus0536477_consumption, 11_LVBus0536477_production, 11_LVBus0536478_production, 11_LVBus0536480_consumption, 11_LVBus0536480_production, 11_LVBus0536481_consumption, 11_LVBus0536481_production, 11_LVBus0536483_production, 11_LVBus0536484_production, 11_LVBus0536485_consumption, 11_LVBus0536485_production, 11_LVBus0536486_consumption, 11_LVBus0536486_production, 11_LVBus0536487_consumption, 11_LVBus0536487_production, 11_LVBus0536488_production, 11_LVBus0536489_production, 11_LVBus0536490_production, 11_LVBus0536491_production, 11_LVBus0536493_production, 11_LVBus0536495_consumption, 11_LVBus0536495_production, 11_LVBus0536497_consumption, 11_LVBus0536497_production, 11_LVBus0536498_production, 11_LVBus0536499_consumption, 11_LVBus0536499_production, 11_LVBus0536500_production, 11_LVBus0536501_production, 11_LVBus0536502_production, 11_LVBus0536504_production, 11_LVBus0536505_consumption, 11_LVBus0536505_production, 11_LVBus0536507_production, 11_LVBus0536509_production, 11_LVBus0536510_consumption, 11_LVBus0536510_production, 11_LVBus0536511_production, 11_LVBus0536512_production, 11_LVBus0536513_consumption, 11_LVBus0536513_production, 11_LVBus0536514_production, 11_LVBus0536515_production, 11_LVBus0536516_production, 11_LVBus0536518_production, 11_LVBus0536519_production, 11_LVBus0536520_production, 11_LVBus0536522_production, 11_LVBus0536523_production, 11_LVBus0536524_production, 11_LVBus0536525_production, 11_LVBus0536527_consumption, 11_LVBus0536527_production, 11_LVBus0536528_production, 11_LVBus0536530_production, 11_LVBus0536532_production, 11_LVBus0536533_production, 11_LVBus0536534_production, 11_LVBus0536535_production, 11_LVBus0536536_production, 11_LVBus0536537_production, 11_LVBus0536538_consumption, 11_LVBus0536538_production, 11_LVBus0536539_consumption, 11_LVBus0536539_production, 11_LVBus0536540_production, 11_LVBus0536542_consumption, 11_LVBus0536542_production, 11_LVBus0536543_production, 11_LVBus0536545_consumption, 11_LVBus0536545_production, 11_LVBus0536546_production, 11_LVBus0536547_production, 11_LVBus0536548_production, 11_LVBus0536550_consumption, 11_LVBus0536550_production, 11_LVBus0536551_production, 11_LVBus0536552_production, 11_LVBus0536554_production, 11_LVBus0536555_production, 11_LVBus0536557_consumption, 11_LVBus0536557_production, 11_LVBus0536558_production, 11_LVBus0536560_production, 11_LVBus0536561_production, 11_LVBus0536563_consumption, 11_LVBus0536563_production, 11_LVBus0536564_consumption, 11_LVBus0536564_production, 11_LVBus0536565_production, 11_LVBus0536567_production, 11_LVBus0536568_production, 11_LVBus0536569_consumption, 11_LVBus0536569_production, 11_LVBus0536570_production, 11_LVBus0536571_production, 11_LVBus0536573_production, 11_LVBus0536574_production, 11_LVBus0536576_production, 11_LVBus0536577_production, 11_LVBus0536578_production, 11_LVBus0536580_consumption, 11_LVBus0536580_production, 11_LVBus0536581_production, 11_LVBus0536582_production, 11_LVBus0536583_production, 11_LVBus0536584_production, 11_LVBus0536585_consumption, 11_LVBus0536585_production, 11_LVBus0536586_consumption, 11_LVBus0536586_production, 11_LVBus0536587_consumption, 11_LVBus0536587_production, 11_LVBus0536588_production, 11_LVBus0536589_production, 11_LVBus0536590_production, 11_LVBus0536591_production, 11_LVBus0536593_production, 11_LVBus0536594_consumption, 11_LVBus0536594_production, 11_LVBus0536595_production, 11_LVBus0536596_production, 11_LVBus0536597_production, 11_LVBus0536598_production, 11_LVBus0536599_consumption, 11_LVBus0536599_production, 11_LVBus0536600_consumption, 11_LVBus0536600_production, 11_LVBus0536601_consumption, 11_LVBus0536601_production, 11_LVBus0536602_production, 11_LVBus0536603_consumption, 11_LVBus0536603_production, 11_LVBus0536604_production, 11_LVBus0536606_consumption, 11_LVBus0536606_production, 11_LVBus0536607_consumption, 11_LVBus0536607_production, 11_LVBus0536609_consumption, 11_LVBus0536609_production, 11_LVBus0536610_production, 11_LVBus0536611_consumption, 11_LVBus0536611_production, 11_LVBus0536612_production, 11_LVBus0536613_production, 11_LVBus0536614_production, 11_LVBus0536615_production, 11_LVBus0536616_production, 11_LVBus0536617_production, 11_LVBus0536618_consumption, 11_LVBus0536618_production, 11_LVBus0536620_production, 11_LVBus0536621_production, 11_LVBus0536622_production, 11_LVBus0536623_production, 11_LVBus0536624_production, 11_LVBus0536625_production, 11_LVBus0536626_production, 11_LVBus0536627_production, 11_LVBus0536628_production, 11_LVBus0536629_production, 11_LVBus0536630_production, 11_LVBus0536632_production, 11_LVBus0536633_consumption, 11_LVBus0536633_production, 11_LVBus0536634_consumption, 11_LVBus0536634_production, 11_LVBus0536635_production, 11_LVBus1285134_production, 11_LVBus1285781_production, 11_LVBus1285782_production, 11_LVBus1285783_production, 11_LVBus1285784_production, 11_LVBus1287195_consumption, 11_LVBus1287195_production, 11_LVBus1287196_production, 11_LVBus1289345_production, 11_LVBus1295366_production, 11_LVBus1295367_consumption, 11_LVBus1295367_production, 11_LVBus1295368_production, 11_LVBus1295369_production, 11_LVBus1295370_production, 11_LVBus1295371_production, 11_LVBus1295372_production, 11_LVBus1295373_production, 11_LVBus1295374_production, 11_LVBus1295409_consumption, 11_LVBus1295409_production, 11_LVBus1295410_production, 11_LVBus1295411_production, 11_LVBus1295412_consumption, 11_LVBus1295412_production, 11_LVBus1295413_production, 11_LVBus1295414_production, 11_LVBus1297362_production, 11_LVBus1300418_production, 11_LVBus1300461_production, 11_LVBus1300462_production, 11_LVBus1300463_production, 11_LVBus1300464_production, 11_LVBus1300465_production, 11_LVBus1300466_production, 11_LVBus1308717_production, 11_LVBus1308718_production, 11_LVBus1311664_production, 11_LVBus1311665_production, 11_LVBus1315224_production, 11_LVBus1338557_consumption, 11_LVBus1338557_production, 11_LVBus1338558_production, 11_LVBus1338559_consumption, 11_LVBus1338559_production, 11_LVBus1338560_consumption, 11_LVBus1338560_production, 11_LVBus1338561_consumption, 11_LVBus1338561_production, 11_LVBus1338562_consumption, 11_LVBus1338562_production, 11_LVBus1338563_consumption, 11_LVBus1338563_production, 11_LVBus1338564_consumption, 11_LVBus1338564_production, 11_LVBus1338565_consumption, 11_LVBus1338565_production, 11_LVBus1338566_production, 11_LVBus1338567_consumption, 11_LVBus1338567_production, 11_LVBus1338568_consumption, 11_LVBus1338568_production, 11_LVBus1338569_consumption, 11_LVBus1338569_production, 11_LVBus1338570_consumption, 11_LVBus1338570_production, 11_LVBus1338571_consumption, 11_LVBus1338571_production, 11_LVBus1338572_consumption, 11_LVBus1338572_production, 11_LVBus1338573_production, 11_LVBus1338574_consumption, 11_LVBus1338574_production, 11_LVBus1338575_consumption, 11_LVBus1338575_production, 11_LVBus1338576_consumption, 11_LVBus1338576_production, 11_LVBus1338577_consumption, 11_LVBus1338577_production, 11_LVBus1351112_consumption, 11_LVBus1351112_production, 11_LVBus1352410_production, 11_LVBus1355131_consumption, 11_LVBus1355131_production, 11_MVLV14683_production, 11_MVLV52721_consumption, 11_MVLV52721_production.

## 9. Data Quality Summary

**Total findings:** 205 (0 errors, 5 warnings, 200 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  430 of 626 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.23 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  431 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536613_consumption`  
  Load '11_LVBus0536613_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536361_consumption`  
  Load '11_LVBus0536361_consumption' has phase imbalance of 149.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1338566_consumption`  
  Load '11_LVBus1338566_consumption' has phase imbalance of 46.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1315224_consumption`  
  Load '11_LVBus1315224_consumption' has phase imbalance of 82.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536533_consumption`  
  Load '11_LVBus0536533_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295373_consumption`  
  Load '11_LVBus1295373_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536363_consumption`  
  Load '11_LVBus0536363_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536434_consumption`  
  Load '11_LVBus0536434_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536475_consumption`  
  Load '11_LVBus0536475_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536428_consumption`  
  Load '11_LVBus0536428_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536442_consumption`  
  Load '11_LVBus0536442_consumption' has phase imbalance of 255.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536501_consumption`  
  Load '11_LVBus0536501_consumption' has phase imbalance of 44.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536632_consumption`  
  Load '11_LVBus0536632_consumption' has phase imbalance of 80.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536530_consumption`  
  Load '11_LVBus0536530_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1311664_consumption`  
  Load '11_LVBus1311664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536426_consumption`  
  Load '11_LVBus0536426_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536567_consumption`  
  Load '11_LVBus0536567_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536560_consumption`  
  Load '11_LVBus0536560_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536498_consumption`  
  Load '11_LVBus0536498_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295410_consumption`  
  Load '11_LVBus1295410_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295414_consumption`  
  Load '11_LVBus1295414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536612_consumption`  
  Load '11_LVBus0536612_consumption' has phase imbalance of 273.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536465_consumption`  
  Load '11_LVBus0536465_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1287196_consumption`  
  Load '11_LVBus1287196_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295368_consumption`  
  Load '11_LVBus1295368_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536574_consumption`  
  Load '11_LVBus0536574_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536451_consumption`  
  Load '11_LVBus0536451_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536461_consumption`  
  Load '11_LVBus0536461_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536407_consumption`  
  Load '11_LVBus0536407_consumption' has phase imbalance of 36.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536522_consumption`  
  Load '11_LVBus0536522_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536623_consumption`  
  Load '11_LVBus0536623_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536554_consumption`  
  Load '11_LVBus0536554_consumption' has phase imbalance of 261.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536353_consumption`  
  Load '11_LVBus0536353_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536547_consumption`  
  Load '11_LVBus0536547_consumption' has phase imbalance of 126.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1352410_consumption`  
  Load '11_LVBus1352410_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536416_consumption`  
  Load '11_LVBus0536416_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536532_consumption`  
  Load '11_LVBus0536532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536528_consumption`  
  Load '11_LVBus0536528_consumption' has phase imbalance of 107.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536397_consumption`  
  Load '11_LVBus0536397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536534_consumption`  
  Load '11_LVBus0536534_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536555_consumption`  
  Load '11_LVBus0536555_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1285783_consumption`  
  Load '11_LVBus1285783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536515_consumption`  
  Load '11_LVBus0536515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536568_consumption`  
  Load '11_LVBus0536568_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536502_consumption`  
  Load '11_LVBus0536502_consumption' has phase imbalance of 64.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536404_consumption`  
  Load '11_LVBus0536404_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536578_consumption`  
  Load '11_LVBus0536578_consumption' has phase imbalance of 259.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536355_consumption`  
  Load '11_LVBus0536355_consumption' has phase imbalance of 52.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536449_consumption`  
  Load '11_LVBus0536449_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1311665_consumption`  
  Load '11_LVBus1311665_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536448_consumption`  
  Load '11_LVBus0536448_consumption' has phase imbalance of 37.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536474_consumption`  
  Load '11_LVBus0536474_consumption' has phase imbalance of 78.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1285134_consumption`  
  Load '11_LVBus1285134_consumption' has phase imbalance of 271.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536582_consumption`  
  Load '11_LVBus0536582_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295370_consumption`  
  Load '11_LVBus1295370_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1300463_consumption`  
  Load '11_LVBus1300463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536356_consumption`  
  Load '11_LVBus0536356_consumption' has phase imbalance of 254.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536358_consumption`  
  Load '11_LVBus0536358_consumption' has phase imbalance of 143.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536624_consumption`  
  Load '11_LVBus0536624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536350_consumption`  
  Load '11_LVBus0536350_consumption' has phase imbalance of 31.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536548_consumption`  
  Load '11_LVBus0536548_consumption' has phase imbalance of 39.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536546_consumption`  
  Load '11_LVBus0536546_consumption' has phase imbalance of 53.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536523_consumption`  
  Load '11_LVBus0536523_consumption' has phase imbalance of 211.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536466_consumption`  
  Load '11_LVBus0536466_consumption' has phase imbalance of 51.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536460_consumption`  
  Load '11_LVBus0536460_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536436_consumption`  
  Load '11_LVBus0536436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536516_consumption`  
  Load '11_LVBus0536516_consumption' has phase imbalance of 290.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536571_consumption`  
  Load '11_LVBus0536571_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536354_consumption`  
  Load '11_LVBus0536354_consumption' has phase imbalance of 101.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536457_consumption`  
  Load '11_LVBus0536457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536458_consumption`  
  Load '11_LVBus0536458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536570_consumption`  
  Load '11_LVBus0536570_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536573_consumption`  
  Load '11_LVBus0536573_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536627_consumption`  
  Load '11_LVBus0536627_consumption' has phase imbalance of 94.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536443_consumption`  
  Load '11_LVBus0536443_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536602_consumption`  
  Load '11_LVBus0536602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1297362_consumption`  
  Load '11_LVBus1297362_consumption' has phase imbalance of 27.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295371_consumption`  
  Load '11_LVBus1295371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536628_consumption`  
  Load '11_LVBus0536628_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536467_consumption`  
  Load '11_LVBus0536467_consumption' has phase imbalance of 24.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536617_consumption`  
  Load '11_LVBus0536617_consumption' has phase imbalance of 106.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536509_consumption`  
  Load '11_LVBus0536509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1289345_consumption`  
  Load '11_LVBus1289345_consumption' has phase imbalance of 45.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536626_consumption`  
  Load '11_LVBus0536626_consumption' has phase imbalance of 231.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536535_consumption`  
  Load '11_LVBus0536535_consumption' has phase imbalance of 222.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536630_consumption`  
  Load '11_LVBus0536630_consumption' has phase imbalance of 124.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536420_consumption`  
  Load '11_LVBus0536420_consumption' has phase imbalance of 23.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536422_consumption`  
  Load '11_LVBus0536422_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536625_consumption`  
  Load '11_LVBus0536625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536455_consumption`  
  Load '11_LVBus0536455_consumption' has phase imbalance of 38.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536440_consumption`  
  Load '11_LVBus0536440_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536484_consumption`  
  Load '11_LVBus0536484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536593_consumption`  
  Load '11_LVBus0536593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536411_consumption`  
  Load '11_LVBus0536411_consumption' has phase imbalance of 177.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536444_consumption`  
  Load '11_LVBus0536444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536463_consumption`  
  Load '11_LVBus0536463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536409_consumption`  
  Load '11_LVBus0536409_consumption' has phase imbalance of 70.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536584_consumption`  
  Load '11_LVBus0536584_consumption' has phase imbalance of 125.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308718_consumption`  
  Load '11_LVBus1308718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536614_consumption`  
  Load '11_LVBus0536614_consumption' has phase imbalance of 136.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536524_consumption`  
  Load '11_LVBus0536524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536514_consumption`  
  Load '11_LVBus0536514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536349_consumption`  
  Load '11_LVBus0536349_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536491_consumption`  
  Load '11_LVBus0536491_consumption' has phase imbalance of 63.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536398_consumption`  
  Load '11_LVBus0536398_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536459_consumption`  
  Load '11_LVBus0536459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536519_consumption`  
  Load '11_LVBus0536519_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536581_consumption`  
  Load '11_LVBus0536581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1300466_consumption`  
  Load '11_LVBus1300466_consumption' has phase imbalance of 188.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536340_consumption`  
  Load '11_LVBus0536340_consumption' has phase imbalance of 26.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536468_consumption`  
  Load '11_LVBus0536468_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536399_consumption`  
  Load '11_LVBus0536399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536589_consumption`  
  Load '11_LVBus0536589_consumption' has phase imbalance of 28.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536401_consumption`  
  Load '11_LVBus0536401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536500_consumption`  
  Load '11_LVBus0536500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536445_consumption`  
  Load '11_LVBus0536445_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536565_consumption`  
  Load '11_LVBus0536565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536437_consumption`  
  Load '11_LVBus0536437_consumption' has phase imbalance of 253.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536615_consumption`  
  Load '11_LVBus0536615_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536590_consumption`  
  Load '11_LVBus0536590_consumption' has phase imbalance of 95.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536536_consumption`  
  Load '11_LVBus0536536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536620_consumption`  
  Load '11_LVBus0536620_consumption' has phase imbalance of 65.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536352_consumption`  
  Load '11_LVBus0536352_consumption' has phase imbalance of 231.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536400_consumption`  
  Load '11_LVBus0536400_consumption' has phase imbalance of 56.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295366_consumption`  
  Load '11_LVBus1295366_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536540_consumption`  
  Load '11_LVBus0536540_consumption' has phase imbalance of 185.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1300465_consumption`  
  Load '11_LVBus1300465_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536520_consumption`  
  Load '11_LVBus0536520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536610_consumption`  
  Load '11_LVBus0536610_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295369_consumption`  
  Load '11_LVBus1295369_consumption' has phase imbalance of 230.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536424_consumption`  
  Load '11_LVBus0536424_consumption' has phase imbalance of 90.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536591_consumption`  
  Load '11_LVBus0536591_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536511_consumption`  
  Load '11_LVBus0536511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536588_consumption`  
  Load '11_LVBus0536588_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308717_consumption`  
  Load '11_LVBus1308717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536518_consumption`  
  Load '11_LVBus0536518_consumption' has phase imbalance of 113.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536429_consumption`  
  Load '11_LVBus0536429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1300462_consumption`  
  Load '11_LVBus1300462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536583_consumption`  
  Load '11_LVBus0536583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536473_consumption`  
  Load '11_LVBus0536473_consumption' has phase imbalance of 106.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536412_consumption`  
  Load '11_LVBus0536412_consumption' has phase imbalance of 124.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536413_consumption`  
  Load '11_LVBus0536413_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536396_consumption`  
  Load '11_LVBus0536396_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536635_consumption`  
  Load '11_LVBus0536635_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536537_consumption`  
  Load '11_LVBus0536537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536595_consumption`  
  Load '11_LVBus0536595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536425_consumption`  
  Load '11_LVBus0536425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1285782_consumption`  
  Load '11_LVBus1285782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1285784_consumption`  
  Load '11_LVBus1285784_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536596_consumption`  
  Load '11_LVBus0536596_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536598_consumption`  
  Load '11_LVBus0536598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536441_consumption`  
  Load '11_LVBus0536441_consumption' has phase imbalance of 299.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536622_consumption`  
  Load '11_LVBus0536622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536604_consumption`  
  Load '11_LVBus0536604_consumption' has phase imbalance of 35.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536394_consumption`  
  Load '11_LVBus0536394_consumption' has phase imbalance of 240.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536493_consumption`  
  Load '11_LVBus0536493_consumption' has phase imbalance of 29.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536469_consumption`  
  Load '11_LVBus0536469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295411_consumption`  
  Load '11_LVBus1295411_consumption' has phase imbalance of 147.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536525_consumption`  
  Load '11_LVBus0536525_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536417_consumption`  
  Load '11_LVBus0536417_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1300418_consumption`  
  Load '11_LVBus1300418_consumption' has phase imbalance of 71.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536597_consumption`  
  Load '11_LVBus0536597_consumption' has phase imbalance of 261.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295374_consumption`  
  Load '11_LVBus1295374_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536389_consumption`  
  Load '11_LVBus0536389_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536512_consumption`  
  Load '11_LVBus0536512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536558_consumption`  
  Load '11_LVBus0536558_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536576_consumption`  
  Load '11_LVBus0536576_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536478_consumption`  
  Load '11_LVBus0536478_consumption' has phase imbalance of 70.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536577_consumption`  
  Load '11_LVBus0536577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536427_consumption`  
  Load '11_LVBus0536427_consumption' has phase imbalance of 70.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1300461_consumption`  
  Load '11_LVBus1300461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536561_consumption`  
  Load '11_LVBus0536561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536489_consumption`  
  Load '11_LVBus0536489_consumption' has phase imbalance of 195.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536543_consumption`  
  Load '11_LVBus0536543_consumption' has phase imbalance of 49.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1300464_consumption`  
  Load '11_LVBus1300464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536488_consumption`  
  Load '11_LVBus0536488_consumption' has phase imbalance of 47.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536483_consumption`  
  Load '11_LVBus0536483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536464_consumption`  
  Load '11_LVBus0536464_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536447_consumption`  
  Load '11_LVBus0536447_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1295372_consumption`  
  Load '11_LVBus1295372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536616_consumption`  
  Load '11_LVBus0536616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536450_consumption`  
  Load '11_LVBus0536450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536621_consumption`  
  Load '11_LVBus0536621_consumption' has phase imbalance of 58.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1338558_consumption`  
  Load '11_LVBus1338558_consumption' has phase imbalance of 32.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0536551_consumption`  
  Load '11_LVBus0536551_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 626 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_BUZEN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  335 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  109 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus0536349_consumption, 11_LVBus0536352_consumption, 11_LVBus0536356_consumption, 11_LVBus0536394_consumption, 11_LVBus0536396_consumption, 11_LVBus0536397_consumption, 11_LVBus0536398_consumption, 11_LVBus0536399_consumption, 11_LVBus0536401_consumption, 11_LVBus0536413_consumption, 11_LVBus0536417_consumption, 11_LVBus0536422_consumption, 11_LVBus0536425_consumption, 11_LVBus0536426_consumption, 11_LVBus0536428_consumption, 11_LVBus0536429_consumption, 11_LVBus0536434_consumption, 11_LVBus0536436_consumption, 11_LVBus0536437_consumption, 11_LVBus0536440_consumption, 11_LVBus0536441_consumption, 11_LVBus0536442_consumption, 11_LVBus0536443_consumption, 11_LVBus0536444_consumption, 11_LVBus0536445_consumption, 11_LVBus0536447_consumption, 11_LVBus0536449_consumption, 11_LVBus0536450_consumption, 11_LVBus0536451_consumption, 11_LVBus0536457_consumption, 11_LVBus0536458_consumption, 11_LVBus0536459_consumption, 11_LVBus0536460_consumption, 11_LVBus0536463_consumption, 11_LVBus0536468_consumption, 11_LVBus0536469_consumption, 11_LVBus0536483_consumption, 11_LVBus0536484_consumption, 11_LVBus0536489_consumption, 11_LVBus0536500_consumption, 11_LVBus0536509_consumption, 11_LVBus0536511_consumption, 11_LVBus0536512_consumption, 11_LVBus0536514_consumption, 11_LVBus0536515_consumption, 11_LVBus0536516_consumption, 11_LVBus0536520_consumption, 11_LVBus0536523_consumption, 11_LVBus0536524_consumption, 11_LVBus0536525_consumption, 11_LVBus0536530_consumption, 11_LVBus0536532_consumption, 11_LVBus0536533_consumption, 11_LVBus0536534_consumption, 11_LVBus0536535_consumption, 11_LVBus0536536_consumption, 11_LVBus0536537_consumption, 11_LVBus0536540_consumption, 11_LVBus0536554_consumption, 11_LVBus0536560_consumption, 11_LVBus0536561_consumption, 11_LVBus0536565_consumption, 11_LVBus0536568_consumption, 11_LVBus0536570_consumption, 11_LVBus0536573_consumption, 11_LVBus0536574_consumption, 11_LVBus0536576_consumption, 11_LVBus0536577_consumption, 11_LVBus0536578_consumption, 11_LVBus0536581_consumption, 11_LVBus0536582_consumption, 11_LVBus0536583_consumption, 11_LVBus0536588_consumption, 11_LVBus0536591_consumption, 11_LVBus0536593_consumption, 11_LVBus0536595_consumption, 11_LVBus0536597_consumption, 11_LVBus0536598_consumption, 11_LVBus0536602_consumption, 11_LVBus0536610_consumption, 11_LVBus0536612_consumption, 11_LVBus0536616_consumption, 11_LVBus0536622_consumption, 11_LVBus0536623_consumption, 11_LVBus0536624_consumption, 11_LVBus0536625_consumption, 11_LVBus0536626_consumption, 11_LVBus0536635_consumption, 11_LVBus1285134_consumption, 11_LVBus1285782_consumption, 11_LVBus1285783_consumption, 11_LVBus1285784_consumption, 11_LVBus1287196_consumption, 11_LVBus1295366_consumption, 11_LVBus1295369_consumption, 11_LVBus1295371_consumption, 11_LVBus1295372_consumption, 11_LVBus1295373_consumption, 11_LVBus1295410_consumption, 11_LVBus1295414_consumption, 11_LVBus1300461_consumption, 11_LVBus1300462_consumption, 11_LVBus1300463_consumption, 11_LVBus1300464_consumption, 11_LVBus1300466_consumption, 11_LVBus1308717_consumption, 11_LVBus1308718_consumption, 11_LVBus1311664_consumption, 11_LVBus1352410_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  313 group(s) of loads (626 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  431 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0536338_consumption, 11_LVBus0536338_production, 11_LVBus0536339_consumption, 11_LVBus0536339_production, 11_LVBus0536340_production, 11_LVBus0536341_consumption, 11_LVBus0536341_production, 11_LVBus0536342_consumption, 11_LVBus0536342_production, 11_LVBus0536343_consumption, 11_LVBus0536343_production, 11_LVBus0536344_consumption, 11_LVBus0536344_production, 11_LVBus0536345_consumption, 11_LVBus0536345_production, 11_LVBus0536347_consumption, 11_LVBus0536347_production, 11_LVBus0536348_consumption, 11_LVBus0536348_production, 11_LVBus0536349_production, 11_LVBus0536350_production, 11_LVBus0536352_production, 11_LVBus0536353_production, 11_LVBus0536354_production, 11_LVBus0536355_production, 11_LVBus0536356_production, 11_LVBus0536357_consumption, 11_LVBus0536357_production, 11_LVBus0536358_production, 11_LVBus0536360_consumption, 11_LVBus0536360_production, 11_LVBus0536361_production, 11_LVBus0536363_production, 11_LVBus0536364_consumption, 11_LVBus0536364_production, 11_LVBus0536365_consumption, 11_LVBus0536365_production, 11_LVBus0536366_consumption, 11_LVBus0536366_production, 11_LVBus0536367_consumption, 11_LVBus0536367_production, 11_LVBus0536368_consumption, 11_LVBus0536368_production, 11_LVBus0536369_consumption, 11_LVBus0536369_production, 11_LVBus0536371_consumption, 11_LVBus0536371_production, 11_LVBus0536372_consumption, 11_LVBus0536372_production, 11_LVBus0536373_consumption, 11_LVBus0536373_production, 11_LVBus0536374_consumption, 11_LVBus0536374_production, 11_LVBus0536375_consumption, 11_LVBus0536375_production, 11_LVBus0536376_consumption, 11_LVBus0536376_production, 11_LVBus0536377_consumption, 11_LVBus0536377_production, 11_LVBus0536378_consumption, 11_LVBus0536378_production, 11_LVBus0536379_consumption, 11_LVBus0536379_production, 11_LVBus0536381_consumption, 11_LVBus0536381_production, 11_LVBus0536382_consumption, 11_LVBus0536382_production, 11_LVBus0536383_consumption, 11_LVBus0536383_production, 11_LVBus0536384_consumption, 11_LVBus0536384_production, 11_LVBus0536385_consumption, 11_LVBus0536385_production, 11_LVBus0536386_consumption, 11_LVBus0536386_production, 11_LVBus0536387_consumption, 11_LVBus0536387_production, 11_LVBus0536388_consumption, 11_LVBus0536388_production, 11_LVBus0536389_production, 11_LVBus0536391_consumption, 11_LVBus0536391_production, 11_LVBus0536394_production, 11_LVBus0536395_consumption, 11_LVBus0536395_production, 11_LVBus0536396_production, 11_LVBus0536397_production, 11_LVBus0536398_production, 11_LVBus0536399_production, 11_LVBus0536400_production, 11_LVBus0536401_production, 11_LVBus0536402_consumption, 11_LVBus0536402_production, 11_LVBus0536403_consumption, 11_LVBus0536403_production, 11_LVBus0536404_production, 11_LVBus0536405_production, 11_LVBus0536406_consumption, 11_LVBus0536406_production, 11_LVBus0536407_production, 11_LVBus0536409_production, 11_LVBus0536411_production, 11_LVBus0536412_production, 11_LVBus0536413_production, 11_LVBus0536414_consumption, 11_LVBus0536414_production, 11_LVBus0536415_consumption, 11_LVBus0536415_production, 11_LVBus0536416_production, 11_LVBus0536417_production, 11_LVBus0536418_consumption, 11_LVBus0536418_production, 11_LVBus0536420_production, 11_LVBus0536422_production, 11_LVBus0536423_consumption, 11_LVBus0536423_production, 11_LVBus0536424_production, 11_LVBus0536425_production, 11_LVBus0536426_production, 11_LVBus0536427_production, 11_LVBus0536428_production, 11_LVBus0536429_production, 11_LVBus0536430_consumption, 11_LVBus0536430_production, 11_LVBus0536432_consumption, 11_LVBus0536432_production, 11_LVBus0536433_consumption, 11_LVBus0536433_production, 11_LVBus0536434_production, 11_LVBus0536435_consumption, 11_LVBus0536435_production, 11_LVBus0536436_production, 11_LVBus0536437_production, 11_LVBus0536438_consumption, 11_LVBus0536438_production, 11_LVBus0536439_consumption, 11_LVBus0536439_production, 11_LVBus0536440_production, 11_LVBus0536441_production, 11_LVBus0536442_production, 11_LVBus0536443_production, 11_LVBus0536444_production, 11_LVBus0536445_production, 11_LVBus0536446_consumption, 11_LVBus0536446_production, 11_LVBus0536447_production, 11_LVBus0536448_production, 11_LVBus0536449_production, 11_LVBus0536450_production, 11_LVBus0536451_production, 11_LVBus0536453_consumption, 11_LVBus0536453_production, 11_LVBus0536455_production, 11_LVBus0536456_consumption, 11_LVBus0536456_production, 11_LVBus0536457_production, 11_LVBus0536458_production, 11_LVBus0536459_production, 11_LVBus0536460_production, 11_LVBus0536461_production, 11_LVBus0536462_consumption, 11_LVBus0536462_production, 11_LVBus0536463_production, 11_LVBus0536464_production, 11_LVBus0536465_production, 11_LVBus0536466_production, 11_LVBus0536467_production, 11_LVBus0536468_production, 11_LVBus0536469_production, 11_LVBus0536471_consumption, 11_LVBus0536471_production, 11_LVBus0536472_consumption, 11_LVBus0536472_production, 11_LVBus0536473_production, 11_LVBus0536474_production, 11_LVBus0536475_production, 11_LVBus0536477_consumption, 11_LVBus0536477_production, 11_LVBus0536478_production, 11_LVBus0536480_consumption, 11_LVBus0536480_production, 11_LVBus0536481_consumption, 11_LVBus0536481_production, 11_LVBus0536483_production, 11_LVBus0536484_production, 11_LVBus0536485_consumption, 11_LVBus0536485_production, 11_LVBus0536486_consumption, 11_LVBus0536486_production, 11_LVBus0536487_consumption, 11_LVBus0536487_production, 11_LVBus0536488_production, 11_LVBus0536489_production, 11_LVBus0536490_production, 11_LVBus0536491_production, 11_LVBus0536493_production, 11_LVBus0536495_consumption, 11_LVBus0536495_production, 11_LVBus0536497_consumption, 11_LVBus0536497_production, 11_LVBus0536498_production, 11_LVBus0536499_consumption, 11_LVBus0536499_production, 11_LVBus0536500_production, 11_LVBus0536501_production, 11_LVBus0536502_production, 11_LVBus0536504_production, 11_LVBus0536505_consumption, 11_LVBus0536505_production, 11_LVBus0536507_production, 11_LVBus0536509_production, 11_LVBus0536510_consumption, 11_LVBus0536510_production, 11_LVBus0536511_production, 11_LVBus0536512_production, 11_LVBus0536513_consumption, 11_LVBus0536513_production, 11_LVBus0536514_production, 11_LVBus0536515_production, 11_LVBus0536516_production, 11_LVBus0536518_production, 11_LVBus0536519_production, 11_LVBus0536520_production, 11_LVBus0536522_production, 11_LVBus0536523_production, 11_LVBus0536524_production, 11_LVBus0536525_production, 11_LVBus0536527_consumption, 11_LVBus0536527_production, 11_LVBus0536528_production, 11_LVBus0536530_production, 11_LVBus0536532_production, 11_LVBus0536533_production, 11_LVBus0536534_production, 11_LVBus0536535_production, 11_LVBus0536536_production, 11_LVBus0536537_production, 11_LVBus0536538_consumption, 11_LVBus0536538_production, 11_LVBus0536539_consumption, 11_LVBus0536539_production, 11_LVBus0536540_production, 11_LVBus0536542_consumption, 11_LVBus0536542_production, 11_LVBus0536543_production, 11_LVBus0536545_consumption, 11_LVBus0536545_production, 11_LVBus0536546_production, 11_LVBus0536547_production, 11_LVBus0536548_production, 11_LVBus0536550_consumption, 11_LVBus0536550_production, 11_LVBus0536551_production, 11_LVBus0536552_production, 11_LVBus0536554_production, 11_LVBus0536555_production, 11_LVBus0536557_consumption, 11_LVBus0536557_production, 11_LVBus0536558_production, 11_LVBus0536560_production, 11_LVBus0536561_production, 11_LVBus0536563_consumption, 11_LVBus0536563_production, 11_LVBus0536564_consumption, 11_LVBus0536564_production, 11_LVBus0536565_production, 11_LVBus0536567_production, 11_LVBus0536568_production, 11_LVBus0536569_consumption, 11_LVBus0536569_production, 11_LVBus0536570_production, 11_LVBus0536571_production, 11_LVBus0536573_production, 11_LVBus0536574_production, 11_LVBus0536576_production, 11_LVBus0536577_production, 11_LVBus0536578_production, 11_LVBus0536580_consumption, 11_LVBus0536580_production, 11_LVBus0536581_production, 11_LVBus0536582_production, 11_LVBus0536583_production, 11_LVBus0536584_production, 11_LVBus0536585_consumption, 11_LVBus0536585_production, 11_LVBus0536586_consumption, 11_LVBus0536586_production, 11_LVBus0536587_consumption, 11_LVBus0536587_production, 11_LVBus0536588_production, 11_LVBus0536589_production, 11_LVBus0536590_production, 11_LVBus0536591_production, 11_LVBus0536593_production, 11_LVBus0536594_consumption, 11_LVBus0536594_production, 11_LVBus0536595_production, 11_LVBus0536596_production, 11_LVBus0536597_production, 11_LVBus0536598_production, 11_LVBus0536599_consumption, 11_LVBus0536599_production, 11_LVBus0536600_consumption, 11_LVBus0536600_production, 11_LVBus0536601_consumption, 11_LVBus0536601_production, 11_LVBus0536602_production, 11_LVBus0536603_consumption, 11_LVBus0536603_production, 11_LVBus0536604_production, 11_LVBus0536606_consumption, 11_LVBus0536606_production, 11_LVBus0536607_consumption, 11_LVBus0536607_production, 11_LVBus0536609_consumption, 11_LVBus0536609_production, 11_LVBus0536610_production, 11_LVBus0536611_consumption, 11_LVBus0536611_production, 11_LVBus0536612_production, 11_LVBus0536613_production, 11_LVBus0536614_production, 11_LVBus0536615_production, 11_LVBus0536616_production, 11_LVBus0536617_production, 11_LVBus0536618_consumption, 11_LVBus0536618_production, 11_LVBus0536620_production, 11_LVBus0536621_production, 11_LVBus0536622_production, 11_LVBus0536623_production, 11_LVBus0536624_production, 11_LVBus0536625_production, 11_LVBus0536626_production, 11_LVBus0536627_production, 11_LVBus0536628_production, 11_LVBus0536629_production, 11_LVBus0536630_production, 11_LVBus0536632_production, 11_LVBus0536633_consumption, 11_LVBus0536633_production, 11_LVBus0536634_consumption, 11_LVBus0536634_production, 11_LVBus0536635_production, 11_LVBus1285134_production, 11_LVBus1285781_production, 11_LVBus1285782_production, 11_LVBus1285783_production, 11_LVBus1285784_production, 11_LVBus1287195_consumption, 11_LVBus1287195_production, 11_LVBus1287196_production, 11_LVBus1289345_production, 11_LVBus1295366_production, 11_LVBus1295367_consumption, 11_LVBus1295367_production, 11_LVBus1295368_production, 11_LVBus1295369_production, 11_LVBus1295370_production, 11_LVBus1295371_production, 11_LVBus1295372_production, 11_LVBus1295373_production, 11_LVBus1295374_production, 11_LVBus1295409_consumption, 11_LVBus1295409_production, 11_LVBus1295410_production, 11_LVBus1295411_production, 11_LVBus1295412_consumption, 11_LVBus1295412_production, 11_LVBus1295413_production, 11_LVBus1295414_production, 11_LVBus1297362_production, 11_LVBus1300418_production, 11_LVBus1300461_production, 11_LVBus1300462_production, 11_LVBus1300463_production, 11_LVBus1300464_production, 11_LVBus1300465_production, 11_LVBus1300466_production, 11_LVBus1308717_production, 11_LVBus1308718_production, 11_LVBus1311664_production, 11_LVBus1311665_production, 11_LVBus1315224_production, 11_LVBus1338557_consumption, 11_LVBus1338557_production, 11_LVBus1338558_production, 11_LVBus1338559_consumption, 11_LVBus1338559_production, 11_LVBus1338560_consumption, 11_LVBus1338560_production, 11_LVBus1338561_consumption, 11_LVBus1338561_production, 11_LVBus1338562_consumption, 11_LVBus1338562_production, 11_LVBus1338563_consumption, 11_LVBus1338563_production, 11_LVBus1338564_consumption, 11_LVBus1338564_production, 11_LVBus1338565_consumption, 11_LVBus1338565_production, 11_LVBus1338566_production, 11_LVBus1338567_consumption, 11_LVBus1338567_production, 11_LVBus1338568_consumption, 11_LVBus1338568_production, 11_LVBus1338569_consumption, 11_LVBus1338569_production, 11_LVBus1338570_consumption, 11_LVBus1338570_production, 11_LVBus1338571_consumption, 11_LVBus1338571_production, 11_LVBus1338572_consumption, 11_LVBus1338572_production, 11_LVBus1338573_production, 11_LVBus1338574_consumption, 11_LVBus1338574_production, 11_LVBus1338575_consumption, 11_LVBus1338575_production, 11_LVBus1338576_consumption, 11_LVBus1338576_production, 11_LVBus1338577_consumption, 11_LVBus1338577_production, 11_LVBus1351112_consumption, 11_LVBus1351112_production, 11_LVBus1352410_production, 11_LVBus1355131_consumption, 11_LVBus1355131_production, 11_MVLV14683_production, 11_MVLV52721_consumption, 11_MVLV52721_production.

