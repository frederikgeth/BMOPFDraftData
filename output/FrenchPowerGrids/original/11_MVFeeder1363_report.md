# BMOPF Network Summary: 11_MVFeeder1363

**Generated:** 2026-10-01 23:33:55  
**Findings:** 0 errors · 4 warnings · 270 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 358 |  |
| line | 342 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 652 | 2.159 MW, 647.8 kvar |
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
| MV_11.8kV | 11.78 kV | 17 | 16 | 0 | 0 |
| LV_236V | 236.0 V | 341 | 326 | 652 | 0 |

**Transformer transitions:**

- `11_MVLV52159_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV62901_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV20409_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV05304_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV45363_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV35358_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV30425_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV17639_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV65832_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV09272_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV22570_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV48660_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV22572_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV43781_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV05303_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 117 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 358 | 1 | 357 | 0 | 0 | 0 |
| Tier LV_236V | 341 | 15 | 326 | 0 | 0 | 0 |
| Tier MV_11.8kV | 17 | 1 | 16 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 15; skipped invalid branches: 0.

Galvanic zones: 16; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_COUPV | MV_11.8kV | 17 | 0 | 0 | 15 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1415 declared bus terminals; 1352 mapped line/closed-switch conductor edges; 63 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 34600.0 | 2.566 | 1956 |
| q_nom | 0.0 | 10400.0 | 2.566 | 1956 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.27 | 1780.0 | 1.789 | 342 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.675 | 15 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 382 of 652 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200405_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200605_consumption' has phase imbalance of 213.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200573_consumption' has phase imbalance of 28.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1363750_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200576_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200545_consumption' has phase imbalance of 128.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200479_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200319_consumption' has phase imbalance of 108.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200338_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200476_consumption' has phase imbalance of 83.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200435_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200625_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200604_consumption' has phase imbalance of 246.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1319026_consumption' has phase imbalance of 82.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200316_consumption' has phase imbalance of 123.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1319024_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200480_consumption' has phase imbalance of 186.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200305_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200489_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200313_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200418_consumption' has phase imbalance of 212.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200345_consumption' has phase imbalance of 244.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200458_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200411_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200459_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200491_consumption' has phase imbalance of 99.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200538_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200364_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200550_consumption' has phase imbalance of 112.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200351_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200493_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200354_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1306117_consumption' has phase imbalance of 136.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1308766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200514_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200426_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200453_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200574_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1317105_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200349_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200300_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200408_consumption' has phase imbalance of 111.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200528_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200622_consumption' has phase imbalance of 92.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200483_consumption' has phase imbalance of 31.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1302578_consumption' has phase imbalance of 256.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200527_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200306_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1292553_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1306118_consumption' has phase imbalance of 215.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200502_consumption' has phase imbalance of 114.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200441_consumption' has phase imbalance of 206.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200428_consumption' has phase imbalance of 90.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1317589_consumption' has phase imbalance of 233.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200582_consumption' has phase imbalance of 255.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200365_consumption' has phase imbalance of 120.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200518_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200568_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200403_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200601_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200401_consumption' has phase imbalance of 240.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200417_consumption' has phase imbalance of 114.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1316772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200331_consumption' has phase imbalance of 295.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200592_consumption' has phase imbalance of 110.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200548_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200296_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1363746_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200575_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1317591_consumption' has phase imbalance of 102.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200295_consumption' has phase imbalance of 266.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200564_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200291_consumption' has phase imbalance of 94.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200294_consumption' has phase imbalance of 224.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200383_consumption' has phase imbalance of 148.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200467_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200593_consumption' has phase imbalance of 124.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1316640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1317593_consumption' has phase imbalance of 98.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200425_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200348_consumption' has phase imbalance of 194.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200623_consumption' has phase imbalance of 96.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1316638_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1312255_consumption' has phase imbalance of 185.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200391_consumption' has phase imbalance of 45.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200474_consumption' has phase imbalance of 166.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1311107_consumption' has phase imbalance of 85.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1363745_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200609_consumption' has phase imbalance of 88.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1301879_consumption' has phase imbalance of 68.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200464_consumption' has phase imbalance of 259.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200526_consumption' has phase imbalance of 60.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1317595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200386_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200299_consumption' has phase imbalance of 246.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200461_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200535_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200309_consumption' has phase imbalance of 143.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200580_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200347_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200292_consumption' has phase imbalance of 269.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200495_consumption' has phase imbalance of 105.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200462_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200427_consumption' has phase imbalance of 71.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200608_consumption' has phase imbalance of 258.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200558_consumption' has phase imbalance of 272.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200394_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200588_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200455_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200603_consumption' has phase imbalance of 212.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200352_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200442_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200420_consumption' has phase imbalance of 192.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200511_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200344_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1292549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200546_consumption' has phase imbalance of 31.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200561_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200613_consumption' has phase imbalance of 233.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200619_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200513_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200346_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200554_consumption' has phase imbalance of 239.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200399_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200343_consumption' has phase imbalance of 26.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200572_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200322_consumption' has phase imbalance of 72.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200440_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1311106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200356_consumption' has phase imbalance of 226.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200466_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200310_consumption' has phase imbalance of 123.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200314_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200454_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200355_consumption' has phase imbalance of 185.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200618_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200565_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200424_consumption' has phase imbalance of 156.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200566_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1285894_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1316641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1317596_consumption' has phase imbalance of 42.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200452_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200460_consumption' has phase imbalance of 231.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200543_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200612_consumption' has phase imbalance of 279.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200597_consumption' has phase imbalance of 226.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200484_consumption' has phase imbalance of 184.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1316639_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200537_consumption' has phase imbalance of 129.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200500_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200569_consumption' has phase imbalance of 281.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200290_consumption' has phase imbalance of 262.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200379_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1292548_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200361_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200336_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1292551_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200341_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200494_consumption' has phase imbalance of 120.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200610_consumption' has phase imbalance of 72.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200602_consumption' has phase imbalance of 238.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200544_consumption' has phase imbalance of 71.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200522_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200620_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200570_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200531_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200323_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200485_consumption' has phase imbalance of 50.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1292552_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200443_consumption' has phase imbalance of 47.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200430_consumption' has phase imbalance of 73.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200293_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200591_consumption' has phase imbalance of 230.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200579_consumption' has phase imbalance of 209.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1316773_consumption' has phase imbalance of 253.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1292550_consumption' has phase imbalance of 296.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200587_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200444_consumption' has phase imbalance of 281.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1319025_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200413_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1311105_consumption' has phase imbalance of 132.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200496_consumption' has phase imbalance of 250.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200311_consumption' has phase imbalance of 91.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200419_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200368_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200297_consumption' has phase imbalance of 89.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200422_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1321918_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200410_consumption' has phase imbalance of 249.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200614_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1200567_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1306116_consumption' has phase imbalance of 130.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 652 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_UNIFORM_CONFIG]** All 652 loads share the 'WYE' configuration — no connection diversity.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.159 MW |
| Total load Q | 647.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV52159_Transformer | 275.0 kVA | 62.4% |
| 11_MVLV62901_Transformer | 176.0 kVA | 47.8% |
| 11_MVLV20409_Transformer | 110.0 kVA | 30.2% |
| 11_MVLV05304_Transformer | 275.0 kVA | 47.0% |
| 11_MVLV45363_Transformer | 176.0 kVA | 59.2% |
| 11_MVLV35358_Transformer | 176.0 kVA | 83.1% |
| 11_MVLV30425_Transformer | 176.0 kVA | 52.8% |
| 11_MVLV17639_Transformer | 693.0 kVA | 35.9% |
| 11_MVLV65832_Transformer | 275.0 kVA | 68.3% |
| 11_MVLV09272_Transformer | 176.0 kVA | 54.8% |
| 11_MVLV22570_Transformer | 176.0 kVA | 73.3% |
| 11_MVLV48660_Transformer | 275.0 kVA | 81.1% |
| 11_MVLV22572_Transformer | 693.0 kVA | 49.6% |
| 11_MVLV43781_Transformer | 110.0 kVA | 71.8% |
| 11_MVLV05303_Transformer | 275.0 kVA | 67.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.16 MW).
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '1'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '2'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '3'.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 358 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 358 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 15 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 17 |
| LV_236V | 4-wire | 341 / 341 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 341 |
| Neutral branches | 326 |
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
| 11.78 kV | 17 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 593.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 341 / 17 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 383 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 383 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1200290_production, 11_LVBus1200291_production, 11_LVBus1200292_production, 11_LVBus1200293_production, 11_LVBus1200294_production, 11_LVBus1200295_production, 11_LVBus1200296_production, 11_LVBus1200297_production, 11_LVBus1200298_production, 11_LVBus1200299_production, 11_LVBus1200300_production, 11_LVBus1200302_consumption, 11_LVBus1200302_production, 11_LVBus1200303_consumption, 11_LVBus1200303_production, 11_LVBus1200304_production, 11_LVBus1200305_production, 11_LVBus1200306_production, 11_LVBus1200307_production, 11_LVBus1200309_production, 11_LVBus1200310_production, 11_LVBus1200311_production, 11_LVBus1200313_production, 11_LVBus1200314_production, 11_LVBus1200316_production, 11_LVBus1200317_production, 11_LVBus1200319_production, 11_LVBus1200320_consumption, 11_LVBus1200320_production, 11_LVBus1200321_production, 11_LVBus1200322_production, 11_LVBus1200323_production, 11_LVBus1200324_consumption, 11_LVBus1200324_production, 11_LVBus1200325_production, 11_LVBus1200326_production, 11_LVBus1200327_production, 11_LVBus1200328_production, 11_LVBus1200329_production, 11_LVBus1200330_production, 11_LVBus1200331_production, 11_LVBus1200332_production, 11_LVBus1200333_production, 11_LVBus1200334_consumption, 11_LVBus1200334_production, 11_LVBus1200335_consumption, 11_LVBus1200335_production, 11_LVBus1200336_production, 11_LVBus1200338_production, 11_LVBus1200340_production, 11_LVBus1200341_production, 11_LVBus1200342_production, 11_LVBus1200343_production, 11_LVBus1200344_production, 11_LVBus1200345_production, 11_LVBus1200346_production, 11_LVBus1200347_production, 11_LVBus1200348_production, 11_LVBus1200349_production, 11_LVBus1200351_production, 11_LVBus1200352_production, 11_LVBus1200354_production, 11_LVBus1200355_production, 11_LVBus1200356_production, 11_LVBus1200357_production, 11_LVBus1200358_production, 11_LVBus1200360_consumption, 11_LVBus1200360_production, 11_LVBus1200361_production, 11_LVBus1200362_consumption, 11_LVBus1200362_production, 11_LVBus1200363_production, 11_LVBus1200364_production, 11_LVBus1200365_production, 11_LVBus1200367_consumption, 11_LVBus1200367_production, 11_LVBus1200368_production, 11_LVBus1200369_consumption, 11_LVBus1200369_production, 11_LVBus1200370_production, 11_LVBus1200372_production, 11_LVBus1200373_consumption, 11_LVBus1200373_production, 11_LVBus1200374_production, 11_LVBus1200375_production, 11_LVBus1200377_production, 11_LVBus1200378_production, 11_LVBus1200379_production, 11_LVBus1200381_consumption, 11_LVBus1200381_production, 11_LVBus1200383_production, 11_LVBus1200385_consumption, 11_LVBus1200385_production, 11_LVBus1200386_production, 11_LVBus1200388_production, 11_LVBus1200389_consumption, 11_LVBus1200389_production, 11_LVBus1200390_production, 11_LVBus1200391_production, 11_LVBus1200393_consumption, 11_LVBus1200393_production, 11_LVBus1200394_production, 11_LVBus1200395_production, 11_LVBus1200396_consumption, 11_LVBus1200396_production, 11_LVBus1200397_production, 11_LVBus1200398_consumption, 11_LVBus1200398_production, 11_LVBus1200399_production, 11_LVBus1200401_production, 11_LVBus1200403_production, 11_LVBus1200405_production, 11_LVBus1200407_production, 11_LVBus1200408_production, 11_LVBus1200410_production, 11_LVBus1200411_production, 11_LVBus1200412_production, 11_LVBus1200413_production, 11_LVBus1200414_consumption, 11_LVBus1200414_production, 11_LVBus1200415_production, 11_LVBus1200417_production, 11_LVBus1200418_production, 11_LVBus1200419_production, 11_LVBus1200420_production, 11_LVBus1200422_production, 11_LVBus1200424_production, 11_LVBus1200425_production, 11_LVBus1200426_production, 11_LVBus1200427_production, 11_LVBus1200428_production, 11_LVBus1200430_production, 11_LVBus1200431_consumption, 11_LVBus1200431_production, 11_LVBus1200432_consumption, 11_LVBus1200432_production, 11_LVBus1200434_production, 11_LVBus1200435_production, 11_LVBus1200436_consumption, 11_LVBus1200436_production, 11_LVBus1200437_production, 11_LVBus1200438_consumption, 11_LVBus1200438_production, 11_LVBus1200440_production, 11_LVBus1200441_production, 11_LVBus1200442_production, 11_LVBus1200443_production, 11_LVBus1200444_production, 11_LVBus1200445_production, 11_LVBus1200447_production, 11_LVBus1200449_production, 11_LVBus1200452_production, 11_LVBus1200453_production, 11_LVBus1200454_production, 11_LVBus1200455_production, 11_LVBus1200457_production, 11_LVBus1200458_production, 11_LVBus1200459_production, 11_LVBus1200460_production, 11_LVBus1200461_production, 11_LVBus1200462_production, 11_LVBus1200463_production, 11_LVBus1200464_production, 11_LVBus1200466_production, 11_LVBus1200467_production, 11_LVBus1200469_consumption, 11_LVBus1200469_production, 11_LVBus1200470_production, 11_LVBus1200471_production, 11_LVBus1200472_production, 11_LVBus1200474_production, 11_LVBus1200476_production, 11_LVBus1200478_production, 11_LVBus1200479_production, 11_LVBus1200480_production, 11_LVBus1200482_consumption, 11_LVBus1200482_production, 11_LVBus1200483_production, 11_LVBus1200484_production, 11_LVBus1200485_production, 11_LVBus1200487_consumption, 11_LVBus1200487_production, 11_LVBus1200488_production, 11_LVBus1200489_production, 11_LVBus1200490_consumption, 11_LVBus1200490_production, 11_LVBus1200491_production, 11_LVBus1200493_production, 11_LVBus1200494_production, 11_LVBus1200495_production, 11_LVBus1200496_production, 11_LVBus1200498_consumption, 11_LVBus1200498_production, 11_LVBus1200499_consumption, 11_LVBus1200499_production, 11_LVBus1200500_production, 11_LVBus1200501_production, 11_LVBus1200502_production, 11_LVBus1200504_consumption, 11_LVBus1200504_production, 11_LVBus1200505_production, 11_LVBus1200506_production, 11_LVBus1200508_consumption, 11_LVBus1200508_production, 11_LVBus1200509_production, 11_LVBus1200510_consumption, 11_LVBus1200510_production, 11_LVBus1200511_production, 11_LVBus1200512_production, 11_LVBus1200513_production, 11_LVBus1200514_production, 11_LVBus1200515_production, 11_LVBus1200516_production, 11_LVBus1200517_production, 11_LVBus1200518_production, 11_LVBus1200519_production, 11_LVBus1200521_production, 11_LVBus1200522_production, 11_LVBus1200523_consumption, 11_LVBus1200523_production, 11_LVBus1200524_production, 11_LVBus1200525_production, 11_LVBus1200526_production, 11_LVBus1200527_production, 11_LVBus1200528_production, 11_LVBus1200530_consumption, 11_LVBus1200530_production, 11_LVBus1200531_production, 11_LVBus1200532_production, 11_LVBus1200533_production, 11_LVBus1200534_consumption, 11_LVBus1200534_production, 11_LVBus1200535_production, 11_LVBus1200536_production, 11_LVBus1200537_production, 11_LVBus1200538_production, 11_LVBus1200540_consumption, 11_LVBus1200540_production, 11_LVBus1200541_production, 11_LVBus1200542_consumption, 11_LVBus1200542_production, 11_LVBus1200543_production, 11_LVBus1200544_production, 11_LVBus1200545_production, 11_LVBus1200546_production, 11_LVBus1200548_production, 11_LVBus1200550_production, 11_LVBus1200552_consumption, 11_LVBus1200552_production, 11_LVBus1200554_production, 11_LVBus1200556_production, 11_LVBus1200557_consumption, 11_LVBus1200557_production, 11_LVBus1200558_production, 11_LVBus1200559_production, 11_LVBus1200560_production, 11_LVBus1200561_production, 11_LVBus1200562_consumption, 11_LVBus1200562_production, 11_LVBus1200563_consumption, 11_LVBus1200563_production, 11_LVBus1200564_production, 11_LVBus1200565_production, 11_LVBus1200566_production, 11_LVBus1200567_production, 11_LVBus1200568_production, 11_LVBus1200569_production, 11_LVBus1200570_production, 11_LVBus1200572_production, 11_LVBus1200573_production, 11_LVBus1200574_production, 11_LVBus1200575_production, 11_LVBus1200576_production, 11_LVBus1200577_consumption, 11_LVBus1200577_production, 11_LVBus1200579_production, 11_LVBus1200580_production, 11_LVBus1200581_production, 11_LVBus1200582_production, 11_LVBus1200583_production, 11_LVBus1200584_production, 11_LVBus1200586_consumption, 11_LVBus1200586_production, 11_LVBus1200587_production, 11_LVBus1200588_production, 11_LVBus1200590_production, 11_LVBus1200591_production, 11_LVBus1200592_production, 11_LVBus1200593_production, 11_LVBus1200595_production, 11_LVBus1200597_production, 11_LVBus1200599_production, 11_LVBus1200601_production, 11_LVBus1200602_production, 11_LVBus1200603_production, 11_LVBus1200604_production, 11_LVBus1200605_production, 11_LVBus1200606_production, 11_LVBus1200608_production, 11_LVBus1200609_production, 11_LVBus1200610_production, 11_LVBus1200612_production, 11_LVBus1200613_production, 11_LVBus1200614_production, 11_LVBus1200615_consumption, 11_LVBus1200615_production, 11_LVBus1200617_production, 11_LVBus1200618_production, 11_LVBus1200619_production, 11_LVBus1200620_production, 11_LVBus1200621_production, 11_LVBus1200622_production, 11_LVBus1200623_production, 11_LVBus1200624_production, 11_LVBus1200625_production, 11_LVBus1284082_consumption, 11_LVBus1284082_production, 11_LVBus1285894_production, 11_LVBus1291844_consumption, 11_LVBus1291844_production, 11_LVBus1291845_consumption, 11_LVBus1291845_production, 11_LVBus1291846_consumption, 11_LVBus1291846_production, 11_LVBus1292548_production, 11_LVBus1292549_production, 11_LVBus1292550_production, 11_LVBus1292551_production, 11_LVBus1292552_production, 11_LVBus1292553_production, 11_LVBus1292554_consumption, 11_LVBus1292554_production, 11_LVBus1301879_production, 11_LVBus1302578_production, 11_LVBus1304280_production, 11_LVBus1306114_consumption, 11_LVBus1306114_production, 11_LVBus1306115_consumption, 11_LVBus1306115_production, 11_LVBus1306116_production, 11_LVBus1306117_production, 11_LVBus1306118_production, 11_LVBus1308766_production, 11_LVBus1311105_production, 11_LVBus1311106_production, 11_LVBus1311107_production, 11_LVBus1312255_production, 11_LVBus1316638_production, 11_LVBus1316639_production, 11_LVBus1316640_production, 11_LVBus1316641_production, 11_LVBus1316642_production, 11_LVBus1316643_production, 11_LVBus1316772_production, 11_LVBus1316773_production, 11_LVBus1317105_production, 11_LVBus1317589_production, 11_LVBus1317590_consumption, 11_LVBus1317590_production, 11_LVBus1317591_production, 11_LVBus1317592_consumption, 11_LVBus1317592_production, 11_LVBus1317593_production, 11_LVBus1317594_consumption, 11_LVBus1317594_production, 11_LVBus1317595_production, 11_LVBus1317596_production, 11_LVBus1319024_production, 11_LVBus1319025_production, 11_LVBus1319026_production, 11_LVBus1321918_production, 11_LVBus1325749_consumption, 11_LVBus1325749_production, 11_LVBus1336947_production, 11_LVBus1363745_production, 11_LVBus1363746_production, 11_LVBus1363747_consumption, 11_LVBus1363747_production, 11_LVBus1363748_consumption, 11_LVBus1363748_production, 11_LVBus1363749_consumption, 11_LVBus1363749_production, 11_LVBus1363750_production.

## 9. Data Quality Summary

**Total findings:** 274 (0 errors, 4 warnings, 270 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  382 of 652 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.16 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  383 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200405_consumption`  
  Load '11_LVBus1200405_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200605_consumption`  
  Load '11_LVBus1200605_consumption' has phase imbalance of 213.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200573_consumption`  
  Load '11_LVBus1200573_consumption' has phase imbalance of 28.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1363750_consumption`  
  Load '11_LVBus1363750_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200576_consumption`  
  Load '11_LVBus1200576_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200545_consumption`  
  Load '11_LVBus1200545_consumption' has phase imbalance of 128.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200479_consumption`  
  Load '11_LVBus1200479_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200319_consumption`  
  Load '11_LVBus1200319_consumption' has phase imbalance of 108.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200506_consumption`  
  Load '11_LVBus1200506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200338_consumption`  
  Load '11_LVBus1200338_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200476_consumption`  
  Load '11_LVBus1200476_consumption' has phase imbalance of 83.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200435_consumption`  
  Load '11_LVBus1200435_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200321_consumption`  
  Load '11_LVBus1200321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200625_consumption`  
  Load '11_LVBus1200625_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200583_consumption`  
  Load '11_LVBus1200583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200604_consumption`  
  Load '11_LVBus1200604_consumption' has phase imbalance of 246.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1319026_consumption`  
  Load '11_LVBus1319026_consumption' has phase imbalance of 82.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200316_consumption`  
  Load '11_LVBus1200316_consumption' has phase imbalance of 123.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1319024_consumption`  
  Load '11_LVBus1319024_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200480_consumption`  
  Load '11_LVBus1200480_consumption' has phase imbalance of 186.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200305_consumption`  
  Load '11_LVBus1200305_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200489_consumption`  
  Load '11_LVBus1200489_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200525_consumption`  
  Load '11_LVBus1200525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200313_consumption`  
  Load '11_LVBus1200313_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200478_consumption`  
  Load '11_LVBus1200478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200418_consumption`  
  Load '11_LVBus1200418_consumption' has phase imbalance of 212.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200345_consumption`  
  Load '11_LVBus1200345_consumption' has phase imbalance of 244.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200458_consumption`  
  Load '11_LVBus1200458_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200411_consumption`  
  Load '11_LVBus1200411_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200459_consumption`  
  Load '11_LVBus1200459_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200491_consumption`  
  Load '11_LVBus1200491_consumption' has phase imbalance of 99.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200538_consumption`  
  Load '11_LVBus1200538_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200364_consumption`  
  Load '11_LVBus1200364_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200550_consumption`  
  Load '11_LVBus1200550_consumption' has phase imbalance of 112.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200351_consumption`  
  Load '11_LVBus1200351_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200493_consumption`  
  Load '11_LVBus1200493_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200532_consumption`  
  Load '11_LVBus1200532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200354_consumption`  
  Load '11_LVBus1200354_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1306117_consumption`  
  Load '11_LVBus1306117_consumption' has phase imbalance of 136.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1308766_consumption`  
  Load '11_LVBus1308766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200514_consumption`  
  Load '11_LVBus1200514_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200426_consumption`  
  Load '11_LVBus1200426_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200453_consumption`  
  Load '11_LVBus1200453_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200574_consumption`  
  Load '11_LVBus1200574_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1317105_consumption`  
  Load '11_LVBus1317105_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200363_consumption`  
  Load '11_LVBus1200363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200349_consumption`  
  Load '11_LVBus1200349_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200300_consumption`  
  Load '11_LVBus1200300_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200408_consumption`  
  Load '11_LVBus1200408_consumption' has phase imbalance of 111.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200528_consumption`  
  Load '11_LVBus1200528_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200328_consumption`  
  Load '11_LVBus1200328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200622_consumption`  
  Load '11_LVBus1200622_consumption' has phase imbalance of 92.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200483_consumption`  
  Load '11_LVBus1200483_consumption' has phase imbalance of 31.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1302578_consumption`  
  Load '11_LVBus1302578_consumption' has phase imbalance of 256.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200527_consumption`  
  Load '11_LVBus1200527_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200306_consumption`  
  Load '11_LVBus1200306_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200517_consumption`  
  Load '11_LVBus1200517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200519_consumption`  
  Load '11_LVBus1200519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1292553_consumption`  
  Load '11_LVBus1292553_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1306118_consumption`  
  Load '11_LVBus1306118_consumption' has phase imbalance of 215.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200329_consumption`  
  Load '11_LVBus1200329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200502_consumption`  
  Load '11_LVBus1200502_consumption' has phase imbalance of 114.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200441_consumption`  
  Load '11_LVBus1200441_consumption' has phase imbalance of 206.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200428_consumption`  
  Load '11_LVBus1200428_consumption' has phase imbalance of 90.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1317589_consumption`  
  Load '11_LVBus1317589_consumption' has phase imbalance of 233.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200325_consumption`  
  Load '11_LVBus1200325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200342_consumption`  
  Load '11_LVBus1200342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200471_consumption`  
  Load '11_LVBus1200471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200582_consumption`  
  Load '11_LVBus1200582_consumption' has phase imbalance of 255.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200365_consumption`  
  Load '11_LVBus1200365_consumption' has phase imbalance of 120.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200599_consumption`  
  Load '11_LVBus1200599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200518_consumption`  
  Load '11_LVBus1200518_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200568_consumption`  
  Load '11_LVBus1200568_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200403_consumption`  
  Load '11_LVBus1200403_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200601_consumption`  
  Load '11_LVBus1200601_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200584_consumption`  
  Load '11_LVBus1200584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200401_consumption`  
  Load '11_LVBus1200401_consumption' has phase imbalance of 240.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200606_consumption`  
  Load '11_LVBus1200606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200617_consumption`  
  Load '11_LVBus1200617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200417_consumption`  
  Load '11_LVBus1200417_consumption' has phase imbalance of 114.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1316772_consumption`  
  Load '11_LVBus1316772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200559_consumption`  
  Load '11_LVBus1200559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200331_consumption`  
  Load '11_LVBus1200331_consumption' has phase imbalance of 295.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200592_consumption`  
  Load '11_LVBus1200592_consumption' has phase imbalance of 110.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200548_consumption`  
  Load '11_LVBus1200548_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200296_consumption`  
  Load '11_LVBus1200296_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1363746_consumption`  
  Load '11_LVBus1363746_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200575_consumption`  
  Load '11_LVBus1200575_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1317591_consumption`  
  Load '11_LVBus1317591_consumption' has phase imbalance of 102.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200295_consumption`  
  Load '11_LVBus1200295_consumption' has phase imbalance of 266.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200564_consumption`  
  Load '11_LVBus1200564_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200291_consumption`  
  Load '11_LVBus1200291_consumption' has phase imbalance of 94.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200294_consumption`  
  Load '11_LVBus1200294_consumption' has phase imbalance of 224.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200333_consumption`  
  Load '11_LVBus1200333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200383_consumption`  
  Load '11_LVBus1200383_consumption' has phase imbalance of 148.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200467_consumption`  
  Load '11_LVBus1200467_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200332_consumption`  
  Load '11_LVBus1200332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200593_consumption`  
  Load '11_LVBus1200593_consumption' has phase imbalance of 124.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200395_consumption`  
  Load '11_LVBus1200395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1316640_consumption`  
  Load '11_LVBus1316640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200304_consumption`  
  Load '11_LVBus1200304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1317593_consumption`  
  Load '11_LVBus1317593_consumption' has phase imbalance of 98.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200425_consumption`  
  Load '11_LVBus1200425_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200348_consumption`  
  Load '11_LVBus1200348_consumption' has phase imbalance of 194.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200623_consumption`  
  Load '11_LVBus1200623_consumption' has phase imbalance of 96.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200358_consumption`  
  Load '11_LVBus1200358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1316638_consumption`  
  Load '11_LVBus1316638_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1312255_consumption`  
  Load '11_LVBus1312255_consumption' has phase imbalance of 185.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200391_consumption`  
  Load '11_LVBus1200391_consumption' has phase imbalance of 45.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200474_consumption`  
  Load '11_LVBus1200474_consumption' has phase imbalance of 166.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1311107_consumption`  
  Load '11_LVBus1311107_consumption' has phase imbalance of 85.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1363745_consumption`  
  Load '11_LVBus1363745_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200609_consumption`  
  Load '11_LVBus1200609_consumption' has phase imbalance of 88.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200472_consumption`  
  Load '11_LVBus1200472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1301879_consumption`  
  Load '11_LVBus1301879_consumption' has phase imbalance of 68.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200464_consumption`  
  Load '11_LVBus1200464_consumption' has phase imbalance of 259.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200526_consumption`  
  Load '11_LVBus1200526_consumption' has phase imbalance of 60.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200307_consumption`  
  Load '11_LVBus1200307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1317595_consumption`  
  Load '11_LVBus1317595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200560_consumption`  
  Load '11_LVBus1200560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200386_consumption`  
  Load '11_LVBus1200386_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200299_consumption`  
  Load '11_LVBus1200299_consumption' has phase imbalance of 246.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200461_consumption`  
  Load '11_LVBus1200461_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200397_consumption`  
  Load '11_LVBus1200397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200535_consumption`  
  Load '11_LVBus1200535_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200624_consumption`  
  Load '11_LVBus1200624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200309_consumption`  
  Load '11_LVBus1200309_consumption' has phase imbalance of 143.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200580_consumption`  
  Load '11_LVBus1200580_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200374_consumption`  
  Load '11_LVBus1200374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200347_consumption`  
  Load '11_LVBus1200347_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200292_consumption`  
  Load '11_LVBus1200292_consumption' has phase imbalance of 269.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200495_consumption`  
  Load '11_LVBus1200495_consumption' has phase imbalance of 105.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200541_consumption`  
  Load '11_LVBus1200541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200462_consumption`  
  Load '11_LVBus1200462_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200521_consumption`  
  Load '11_LVBus1200521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200427_consumption`  
  Load '11_LVBus1200427_consumption' has phase imbalance of 71.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200608_consumption`  
  Load '11_LVBus1200608_consumption' has phase imbalance of 258.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200558_consumption`  
  Load '11_LVBus1200558_consumption' has phase imbalance of 272.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200394_consumption`  
  Load '11_LVBus1200394_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200588_consumption`  
  Load '11_LVBus1200588_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200455_consumption`  
  Load '11_LVBus1200455_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200603_consumption`  
  Load '11_LVBus1200603_consumption' has phase imbalance of 212.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200352_consumption`  
  Load '11_LVBus1200352_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200442_consumption`  
  Load '11_LVBus1200442_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200457_consumption`  
  Load '11_LVBus1200457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200375_consumption`  
  Load '11_LVBus1200375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200501_consumption`  
  Load '11_LVBus1200501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200420_consumption`  
  Load '11_LVBus1200420_consumption' has phase imbalance of 192.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200511_consumption`  
  Load '11_LVBus1200511_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200533_consumption`  
  Load '11_LVBus1200533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200621_consumption`  
  Load '11_LVBus1200621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200344_consumption`  
  Load '11_LVBus1200344_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200515_consumption`  
  Load '11_LVBus1200515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1292549_consumption`  
  Load '11_LVBus1292549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200546_consumption`  
  Load '11_LVBus1200546_consumption' has phase imbalance of 31.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200298_consumption`  
  Load '11_LVBus1200298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200561_consumption`  
  Load '11_LVBus1200561_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200613_consumption`  
  Load '11_LVBus1200613_consumption' has phase imbalance of 233.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200619_consumption`  
  Load '11_LVBus1200619_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200513_consumption`  
  Load '11_LVBus1200513_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200463_consumption`  
  Load '11_LVBus1200463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200346_consumption`  
  Load '11_LVBus1200346_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200554_consumption`  
  Load '11_LVBus1200554_consumption' has phase imbalance of 239.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200399_consumption`  
  Load '11_LVBus1200399_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200343_consumption`  
  Load '11_LVBus1200343_consumption' has phase imbalance of 26.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200572_consumption`  
  Load '11_LVBus1200572_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200512_consumption`  
  Load '11_LVBus1200512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200505_consumption`  
  Load '11_LVBus1200505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200322_consumption`  
  Load '11_LVBus1200322_consumption' has phase imbalance of 72.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200440_consumption`  
  Load '11_LVBus1200440_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1311106_consumption`  
  Load '11_LVBus1311106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200356_consumption`  
  Load '11_LVBus1200356_consumption' has phase imbalance of 226.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200466_consumption`  
  Load '11_LVBus1200466_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200310_consumption`  
  Load '11_LVBus1200310_consumption' has phase imbalance of 123.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200314_consumption`  
  Load '11_LVBus1200314_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200454_consumption`  
  Load '11_LVBus1200454_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200355_consumption`  
  Load '11_LVBus1200355_consumption' has phase imbalance of 185.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200618_consumption`  
  Load '11_LVBus1200618_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200516_consumption`  
  Load '11_LVBus1200516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200565_consumption`  
  Load '11_LVBus1200565_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200424_consumption`  
  Load '11_LVBus1200424_consumption' has phase imbalance of 156.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200566_consumption`  
  Load '11_LVBus1200566_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1285894_consumption`  
  Load '11_LVBus1285894_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1316641_consumption`  
  Load '11_LVBus1316641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1317596_consumption`  
  Load '11_LVBus1317596_consumption' has phase imbalance of 42.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200452_consumption`  
  Load '11_LVBus1200452_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200460_consumption`  
  Load '11_LVBus1200460_consumption' has phase imbalance of 231.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200543_consumption`  
  Load '11_LVBus1200543_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200612_consumption`  
  Load '11_LVBus1200612_consumption' has phase imbalance of 279.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200597_consumption`  
  Load '11_LVBus1200597_consumption' has phase imbalance of 226.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200484_consumption`  
  Load '11_LVBus1200484_consumption' has phase imbalance of 184.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1316639_consumption`  
  Load '11_LVBus1316639_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200509_consumption`  
  Load '11_LVBus1200509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200537_consumption`  
  Load '11_LVBus1200537_consumption' has phase imbalance of 129.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200500_consumption`  
  Load '11_LVBus1200500_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200569_consumption`  
  Load '11_LVBus1200569_consumption' has phase imbalance of 281.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200556_consumption`  
  Load '11_LVBus1200556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200290_consumption`  
  Load '11_LVBus1200290_consumption' has phase imbalance of 262.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200379_consumption`  
  Load '11_LVBus1200379_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1292548_consumption`  
  Load '11_LVBus1292548_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200361_consumption`  
  Load '11_LVBus1200361_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200336_consumption`  
  Load '11_LVBus1200336_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1292551_consumption`  
  Load '11_LVBus1292551_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200341_consumption`  
  Load '11_LVBus1200341_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200494_consumption`  
  Load '11_LVBus1200494_consumption' has phase imbalance of 120.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200610_consumption`  
  Load '11_LVBus1200610_consumption' has phase imbalance of 72.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200415_consumption`  
  Load '11_LVBus1200415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200602_consumption`  
  Load '11_LVBus1200602_consumption' has phase imbalance of 238.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200330_consumption`  
  Load '11_LVBus1200330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200544_consumption`  
  Load '11_LVBus1200544_consumption' has phase imbalance of 71.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200522_consumption`  
  Load '11_LVBus1200522_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200620_consumption`  
  Load '11_LVBus1200620_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200570_consumption`  
  Load '11_LVBus1200570_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200388_consumption`  
  Load '11_LVBus1200388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200531_consumption`  
  Load '11_LVBus1200531_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200323_consumption`  
  Load '11_LVBus1200323_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200485_consumption`  
  Load '11_LVBus1200485_consumption' has phase imbalance of 50.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1292552_consumption`  
  Load '11_LVBus1292552_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200443_consumption`  
  Load '11_LVBus1200443_consumption' has phase imbalance of 47.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200430_consumption`  
  Load '11_LVBus1200430_consumption' has phase imbalance of 73.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200293_consumption`  
  Load '11_LVBus1200293_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200449_consumption`  
  Load '11_LVBus1200449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200591_consumption`  
  Load '11_LVBus1200591_consumption' has phase imbalance of 230.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200326_consumption`  
  Load '11_LVBus1200326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200377_consumption`  
  Load '11_LVBus1200377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200579_consumption`  
  Load '11_LVBus1200579_consumption' has phase imbalance of 209.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1316773_consumption`  
  Load '11_LVBus1316773_consumption' has phase imbalance of 253.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1292550_consumption`  
  Load '11_LVBus1292550_consumption' has phase imbalance of 296.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200595_consumption`  
  Load '11_LVBus1200595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200587_consumption`  
  Load '11_LVBus1200587_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200445_consumption`  
  Load '11_LVBus1200445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200444_consumption`  
  Load '11_LVBus1200444_consumption' has phase imbalance of 281.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200524_consumption`  
  Load '11_LVBus1200524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200357_consumption`  
  Load '11_LVBus1200357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1319025_consumption`  
  Load '11_LVBus1319025_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200413_consumption`  
  Load '11_LVBus1200413_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1311105_consumption`  
  Load '11_LVBus1311105_consumption' has phase imbalance of 132.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200590_consumption`  
  Load '11_LVBus1200590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200496_consumption`  
  Load '11_LVBus1200496_consumption' has phase imbalance of 250.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200311_consumption`  
  Load '11_LVBus1200311_consumption' has phase imbalance of 91.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200419_consumption`  
  Load '11_LVBus1200419_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200368_consumption`  
  Load '11_LVBus1200368_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200297_consumption`  
  Load '11_LVBus1200297_consumption' has phase imbalance of 89.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200422_consumption`  
  Load '11_LVBus1200422_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200581_consumption`  
  Load '11_LVBus1200581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1321918_consumption`  
  Load '11_LVBus1321918_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200410_consumption`  
  Load '11_LVBus1200410_consumption' has phase imbalance of 249.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200327_consumption`  
  Load '11_LVBus1200327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200412_consumption`  
  Load '11_LVBus1200412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200614_consumption`  
  Load '11_LVBus1200614_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1200567_consumption`  
  Load '11_LVBus1200567_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1306116_consumption`  
  Load '11_LVBus1306116_consumption' has phase imbalance of 130.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 652 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_UNIFORM_CONFIG]** `load`  
  All 652 loads share the 'WYE' configuration — no connection diversity.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '1'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '2'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '3'.
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
  358 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  164 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus1200290_consumption, 11_LVBus1200292_consumption, 11_LVBus1200293_consumption, 11_LVBus1200295_consumption, 11_LVBus1200296_consumption, 11_LVBus1200298_consumption, 11_LVBus1200299_consumption, 11_LVBus1200300_consumption, 11_LVBus1200304_consumption, 11_LVBus1200306_consumption, 11_LVBus1200307_consumption, 11_LVBus1200314_consumption, 11_LVBus1200321_consumption, 11_LVBus1200323_consumption, 11_LVBus1200325_consumption, 11_LVBus1200326_consumption, 11_LVBus1200327_consumption, 11_LVBus1200328_consumption, 11_LVBus1200329_consumption, 11_LVBus1200330_consumption, 11_LVBus1200331_consumption, 11_LVBus1200332_consumption, 11_LVBus1200333_consumption, 11_LVBus1200336_consumption, 11_LVBus1200338_consumption, 11_LVBus1200342_consumption, 11_LVBus1200345_consumption, 11_LVBus1200347_consumption, 11_LVBus1200348_consumption, 11_LVBus1200349_consumption, 11_LVBus1200355_consumption, 11_LVBus1200356_consumption, 11_LVBus1200357_consumption, 11_LVBus1200358_consumption, 11_LVBus1200361_consumption, 11_LVBus1200363_consumption, 11_LVBus1200368_consumption, 11_LVBus1200374_consumption, 11_LVBus1200375_consumption, 11_LVBus1200377_consumption, 11_LVBus1200386_consumption, 11_LVBus1200388_consumption, 11_LVBus1200394_consumption, 11_LVBus1200395_consumption, 11_LVBus1200397_consumption, 11_LVBus1200401_consumption, 11_LVBus1200403_consumption, 11_LVBus1200405_consumption, 11_LVBus1200410_consumption, 11_LVBus1200411_consumption, 11_LVBus1200412_consumption, 11_LVBus1200415_consumption, 11_LVBus1200418_consumption, 11_LVBus1200419_consumption, 11_LVBus1200420_consumption, 11_LVBus1200422_consumption, 11_LVBus1200425_consumption, 11_LVBus1200426_consumption, 11_LVBus1200440_consumption, 11_LVBus1200441_consumption, 11_LVBus1200444_consumption, 11_LVBus1200445_consumption, 11_LVBus1200449_consumption, 11_LVBus1200452_consumption, 11_LVBus1200455_consumption, 11_LVBus1200457_consumption, 11_LVBus1200458_consumption, 11_LVBus1200459_consumption, 11_LVBus1200460_consumption, 11_LVBus1200462_consumption, 11_LVBus1200463_consumption, 11_LVBus1200464_consumption, 11_LVBus1200467_consumption, 11_LVBus1200471_consumption, 11_LVBus1200472_consumption, 11_LVBus1200478_consumption, 11_LVBus1200480_consumption, 11_LVBus1200484_consumption, 11_LVBus1200489_consumption, 11_LVBus1200493_consumption, 11_LVBus1200496_consumption, 11_LVBus1200501_consumption, 11_LVBus1200505_consumption, 11_LVBus1200506_consumption, 11_LVBus1200509_consumption, 11_LVBus1200512_consumption, 11_LVBus1200514_consumption, 11_LVBus1200515_consumption, 11_LVBus1200516_consumption, 11_LVBus1200517_consumption, 11_LVBus1200518_consumption, 11_LVBus1200519_consumption, 11_LVBus1200521_consumption, 11_LVBus1200522_consumption, 11_LVBus1200524_consumption, 11_LVBus1200525_consumption, 11_LVBus1200527_consumption, 11_LVBus1200528_consumption, 11_LVBus1200531_consumption, 11_LVBus1200532_consumption, 11_LVBus1200533_consumption, 11_LVBus1200541_consumption, 11_LVBus1200548_consumption, 11_LVBus1200554_consumption, 11_LVBus1200556_consumption, 11_LVBus1200558_consumption, 11_LVBus1200559_consumption, 11_LVBus1200560_consumption, 11_LVBus1200564_consumption, 11_LVBus1200565_consumption, 11_LVBus1200566_consumption, 11_LVBus1200567_consumption, 11_LVBus1200569_consumption, 11_LVBus1200570_consumption, 11_LVBus1200574_consumption, 11_LVBus1200575_consumption, 11_LVBus1200576_consumption, 11_LVBus1200579_consumption, 11_LVBus1200580_consumption, 11_LVBus1200581_consumption, 11_LVBus1200582_consumption, 11_LVBus1200583_consumption, 11_LVBus1200584_consumption, 11_LVBus1200588_consumption, 11_LVBus1200590_consumption, 11_LVBus1200591_consumption, 11_LVBus1200595_consumption, 11_LVBus1200597_consumption, 11_LVBus1200599_consumption, 11_LVBus1200601_consumption, 11_LVBus1200602_consumption, 11_LVBus1200603_consumption, 11_LVBus1200604_consumption, 11_LVBus1200605_consumption, 11_LVBus1200606_consumption, 11_LVBus1200608_consumption, 11_LVBus1200612_consumption, 11_LVBus1200617_consumption, 11_LVBus1200618_consumption, 11_LVBus1200620_consumption, 11_LVBus1200621_consumption, 11_LVBus1200624_consumption, 11_LVBus1285894_consumption, 11_LVBus1292548_consumption, 11_LVBus1292549_consumption, 11_LVBus1292550_consumption, 11_LVBus1292551_consumption, 11_LVBus1292552_consumption, 11_LVBus1292553_consumption, 11_LVBus1302578_consumption, 11_LVBus1306118_consumption, 11_LVBus1308766_consumption, 11_LVBus1311106_consumption, 11_LVBus1316640_consumption, 11_LVBus1316641_consumption, 11_LVBus1316772_consumption, 11_LVBus1316773_consumption, 11_LVBus1317105_consumption, 11_LVBus1317589_consumption, 11_LVBus1317595_consumption, 11_LVBus1319024_consumption, 11_LVBus1319025_consumption, 11_LVBus1363746_consumption, 11_LVBus1363750_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  326 group(s) of loads (652 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  383 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1200290_production, 11_LVBus1200291_production, 11_LVBus1200292_production, 11_LVBus1200293_production, 11_LVBus1200294_production, 11_LVBus1200295_production, 11_LVBus1200296_production, 11_LVBus1200297_production, 11_LVBus1200298_production, 11_LVBus1200299_production, 11_LVBus1200300_production, 11_LVBus1200302_consumption, 11_LVBus1200302_production, 11_LVBus1200303_consumption, 11_LVBus1200303_production, 11_LVBus1200304_production, 11_LVBus1200305_production, 11_LVBus1200306_production, 11_LVBus1200307_production, 11_LVBus1200309_production, 11_LVBus1200310_production, 11_LVBus1200311_production, 11_LVBus1200313_production, 11_LVBus1200314_production, 11_LVBus1200316_production, 11_LVBus1200317_production, 11_LVBus1200319_production, 11_LVBus1200320_consumption, 11_LVBus1200320_production, 11_LVBus1200321_production, 11_LVBus1200322_production, 11_LVBus1200323_production, 11_LVBus1200324_consumption, 11_LVBus1200324_production, 11_LVBus1200325_production, 11_LVBus1200326_production, 11_LVBus1200327_production, 11_LVBus1200328_production, 11_LVBus1200329_production, 11_LVBus1200330_production, 11_LVBus1200331_production, 11_LVBus1200332_production, 11_LVBus1200333_production, 11_LVBus1200334_consumption, 11_LVBus1200334_production, 11_LVBus1200335_consumption, 11_LVBus1200335_production, 11_LVBus1200336_production, 11_LVBus1200338_production, 11_LVBus1200340_production, 11_LVBus1200341_production, 11_LVBus1200342_production, 11_LVBus1200343_production, 11_LVBus1200344_production, 11_LVBus1200345_production, 11_LVBus1200346_production, 11_LVBus1200347_production, 11_LVBus1200348_production, 11_LVBus1200349_production, 11_LVBus1200351_production, 11_LVBus1200352_production, 11_LVBus1200354_production, 11_LVBus1200355_production, 11_LVBus1200356_production, 11_LVBus1200357_production, 11_LVBus1200358_production, 11_LVBus1200360_consumption, 11_LVBus1200360_production, 11_LVBus1200361_production, 11_LVBus1200362_consumption, 11_LVBus1200362_production, 11_LVBus1200363_production, 11_LVBus1200364_production, 11_LVBus1200365_production, 11_LVBus1200367_consumption, 11_LVBus1200367_production, 11_LVBus1200368_production, 11_LVBus1200369_consumption, 11_LVBus1200369_production, 11_LVBus1200370_production, 11_LVBus1200372_production, 11_LVBus1200373_consumption, 11_LVBus1200373_production, 11_LVBus1200374_production, 11_LVBus1200375_production, 11_LVBus1200377_production, 11_LVBus1200378_production, 11_LVBus1200379_production, 11_LVBus1200381_consumption, 11_LVBus1200381_production, 11_LVBus1200383_production, 11_LVBus1200385_consumption, 11_LVBus1200385_production, 11_LVBus1200386_production, 11_LVBus1200388_production, 11_LVBus1200389_consumption, 11_LVBus1200389_production, 11_LVBus1200390_production, 11_LVBus1200391_production, 11_LVBus1200393_consumption, 11_LVBus1200393_production, 11_LVBus1200394_production, 11_LVBus1200395_production, 11_LVBus1200396_consumption, 11_LVBus1200396_production, 11_LVBus1200397_production, 11_LVBus1200398_consumption, 11_LVBus1200398_production, 11_LVBus1200399_production, 11_LVBus1200401_production, 11_LVBus1200403_production, 11_LVBus1200405_production, 11_LVBus1200407_production, 11_LVBus1200408_production, 11_LVBus1200410_production, 11_LVBus1200411_production, 11_LVBus1200412_production, 11_LVBus1200413_production, 11_LVBus1200414_consumption, 11_LVBus1200414_production, 11_LVBus1200415_production, 11_LVBus1200417_production, 11_LVBus1200418_production, 11_LVBus1200419_production, 11_LVBus1200420_production, 11_LVBus1200422_production, 11_LVBus1200424_production, 11_LVBus1200425_production, 11_LVBus1200426_production, 11_LVBus1200427_production, 11_LVBus1200428_production, 11_LVBus1200430_production, 11_LVBus1200431_consumption, 11_LVBus1200431_production, 11_LVBus1200432_consumption, 11_LVBus1200432_production, 11_LVBus1200434_production, 11_LVBus1200435_production, 11_LVBus1200436_consumption, 11_LVBus1200436_production, 11_LVBus1200437_production, 11_LVBus1200438_consumption, 11_LVBus1200438_production, 11_LVBus1200440_production, 11_LVBus1200441_production, 11_LVBus1200442_production, 11_LVBus1200443_production, 11_LVBus1200444_production, 11_LVBus1200445_production, 11_LVBus1200447_production, 11_LVBus1200449_production, 11_LVBus1200452_production, 11_LVBus1200453_production, 11_LVBus1200454_production, 11_LVBus1200455_production, 11_LVBus1200457_production, 11_LVBus1200458_production, 11_LVBus1200459_production, 11_LVBus1200460_production, 11_LVBus1200461_production, 11_LVBus1200462_production, 11_LVBus1200463_production, 11_LVBus1200464_production, 11_LVBus1200466_production, 11_LVBus1200467_production, 11_LVBus1200469_consumption, 11_LVBus1200469_production, 11_LVBus1200470_production, 11_LVBus1200471_production, 11_LVBus1200472_production, 11_LVBus1200474_production, 11_LVBus1200476_production, 11_LVBus1200478_production, 11_LVBus1200479_production, 11_LVBus1200480_production, 11_LVBus1200482_consumption, 11_LVBus1200482_production, 11_LVBus1200483_production, 11_LVBus1200484_production, 11_LVBus1200485_production, 11_LVBus1200487_consumption, 11_LVBus1200487_production, 11_LVBus1200488_production, 11_LVBus1200489_production, 11_LVBus1200490_consumption, 11_LVBus1200490_production, 11_LVBus1200491_production, 11_LVBus1200493_production, 11_LVBus1200494_production, 11_LVBus1200495_production, 11_LVBus1200496_production, 11_LVBus1200498_consumption, 11_LVBus1200498_production, 11_LVBus1200499_consumption, 11_LVBus1200499_production, 11_LVBus1200500_production, 11_LVBus1200501_production, 11_LVBus1200502_production, 11_LVBus1200504_consumption, 11_LVBus1200504_production, 11_LVBus1200505_production, 11_LVBus1200506_production, 11_LVBus1200508_consumption, 11_LVBus1200508_production, 11_LVBus1200509_production, 11_LVBus1200510_consumption, 11_LVBus1200510_production, 11_LVBus1200511_production, 11_LVBus1200512_production, 11_LVBus1200513_production, 11_LVBus1200514_production, 11_LVBus1200515_production, 11_LVBus1200516_production, 11_LVBus1200517_production, 11_LVBus1200518_production, 11_LVBus1200519_production, 11_LVBus1200521_production, 11_LVBus1200522_production, 11_LVBus1200523_consumption, 11_LVBus1200523_production, 11_LVBus1200524_production, 11_LVBus1200525_production, 11_LVBus1200526_production, 11_LVBus1200527_production, 11_LVBus1200528_production, 11_LVBus1200530_consumption, 11_LVBus1200530_production, 11_LVBus1200531_production, 11_LVBus1200532_production, 11_LVBus1200533_production, 11_LVBus1200534_consumption, 11_LVBus1200534_production, 11_LVBus1200535_production, 11_LVBus1200536_production, 11_LVBus1200537_production, 11_LVBus1200538_production, 11_LVBus1200540_consumption, 11_LVBus1200540_production, 11_LVBus1200541_production, 11_LVBus1200542_consumption, 11_LVBus1200542_production, 11_LVBus1200543_production, 11_LVBus1200544_production, 11_LVBus1200545_production, 11_LVBus1200546_production, 11_LVBus1200548_production, 11_LVBus1200550_production, 11_LVBus1200552_consumption, 11_LVBus1200552_production, 11_LVBus1200554_production, 11_LVBus1200556_production, 11_LVBus1200557_consumption, 11_LVBus1200557_production, 11_LVBus1200558_production, 11_LVBus1200559_production, 11_LVBus1200560_production, 11_LVBus1200561_production, 11_LVBus1200562_consumption, 11_LVBus1200562_production, 11_LVBus1200563_consumption, 11_LVBus1200563_production, 11_LVBus1200564_production, 11_LVBus1200565_production, 11_LVBus1200566_production, 11_LVBus1200567_production, 11_LVBus1200568_production, 11_LVBus1200569_production, 11_LVBus1200570_production, 11_LVBus1200572_production, 11_LVBus1200573_production, 11_LVBus1200574_production, 11_LVBus1200575_production, 11_LVBus1200576_production, 11_LVBus1200577_consumption, 11_LVBus1200577_production, 11_LVBus1200579_production, 11_LVBus1200580_production, 11_LVBus1200581_production, 11_LVBus1200582_production, 11_LVBus1200583_production, 11_LVBus1200584_production, 11_LVBus1200586_consumption, 11_LVBus1200586_production, 11_LVBus1200587_production, 11_LVBus1200588_production, 11_LVBus1200590_production, 11_LVBus1200591_production, 11_LVBus1200592_production, 11_LVBus1200593_production, 11_LVBus1200595_production, 11_LVBus1200597_production, 11_LVBus1200599_production, 11_LVBus1200601_production, 11_LVBus1200602_production, 11_LVBus1200603_production, 11_LVBus1200604_production, 11_LVBus1200605_production, 11_LVBus1200606_production, 11_LVBus1200608_production, 11_LVBus1200609_production, 11_LVBus1200610_production, 11_LVBus1200612_production, 11_LVBus1200613_production, 11_LVBus1200614_production, 11_LVBus1200615_consumption, 11_LVBus1200615_production, 11_LVBus1200617_production, 11_LVBus1200618_production, 11_LVBus1200619_production, 11_LVBus1200620_production, 11_LVBus1200621_production, 11_LVBus1200622_production, 11_LVBus1200623_production, 11_LVBus1200624_production, 11_LVBus1200625_production, 11_LVBus1284082_consumption, 11_LVBus1284082_production, 11_LVBus1285894_production, 11_LVBus1291844_consumption, 11_LVBus1291844_production, 11_LVBus1291845_consumption, 11_LVBus1291845_production, 11_LVBus1291846_consumption, 11_LVBus1291846_production, 11_LVBus1292548_production, 11_LVBus1292549_production, 11_LVBus1292550_production, 11_LVBus1292551_production, 11_LVBus1292552_production, 11_LVBus1292553_production, 11_LVBus1292554_consumption, 11_LVBus1292554_production, 11_LVBus1301879_production, 11_LVBus1302578_production, 11_LVBus1304280_production, 11_LVBus1306114_consumption, 11_LVBus1306114_production, 11_LVBus1306115_consumption, 11_LVBus1306115_production, 11_LVBus1306116_production, 11_LVBus1306117_production, 11_LVBus1306118_production, 11_LVBus1308766_production, 11_LVBus1311105_production, 11_LVBus1311106_production, 11_LVBus1311107_production, 11_LVBus1312255_production, 11_LVBus1316638_production, 11_LVBus1316639_production, 11_LVBus1316640_production, 11_LVBus1316641_production, 11_LVBus1316642_production, 11_LVBus1316643_production, 11_LVBus1316772_production, 11_LVBus1316773_production, 11_LVBus1317105_production, 11_LVBus1317589_production, 11_LVBus1317590_consumption, 11_LVBus1317590_production, 11_LVBus1317591_production, 11_LVBus1317592_consumption, 11_LVBus1317592_production, 11_LVBus1317593_production, 11_LVBus1317594_consumption, 11_LVBus1317594_production, 11_LVBus1317595_production, 11_LVBus1317596_production, 11_LVBus1319024_production, 11_LVBus1319025_production, 11_LVBus1319026_production, 11_LVBus1321918_production, 11_LVBus1325749_consumption, 11_LVBus1325749_production, 11_LVBus1336947_production, 11_LVBus1363745_production, 11_LVBus1363746_production, 11_LVBus1363747_consumption, 11_LVBus1363747_production, 11_LVBus1363748_consumption, 11_LVBus1363748_production, 11_LVBus1363749_consumption, 11_LVBus1363749_production, 11_LVBus1363750_production.

