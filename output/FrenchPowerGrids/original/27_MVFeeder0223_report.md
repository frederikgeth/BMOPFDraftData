# BMOPF Network Summary: 27_MVFeeder0223

**Generated:** 2026-10-01 23:34:00  
**Findings:** 0 errors · 4 warnings · 393 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 41 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 626 |  |
| line | 584 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 994 | 1.736 MW, 520.8 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 41 |  |
| switch | 0 |  |
| transformer | 41 | Dyn11×41 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 93 | 92 | 10 | 0 |
| LV_236V | 236.0 V | 533 | 492 | 984 | 0 |

**Transformer transitions:**

- `27_MVLV17464_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV07961_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV18584_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV66366_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV75049_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV58284_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV15680_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV40481_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV17363_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV01136_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV50721_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV58008_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV21480_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV63143_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV19041_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV43664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV18763_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV06948_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV18764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV83035_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV39032_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV03854_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV75032_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV70484_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV09688_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV17463_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV62689_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV75379_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV18727_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV43462_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV30800_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV66367_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV74748_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV72921_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV21972_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV23727_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV45023_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV07960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV04234_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV41365_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV43463_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 182 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 626 | 1 | 625 | 0 | 0 | 0 |
| Tier LV_236V | 533 | 41 | 492 | 0 | 0 | 0 |
| Tier MV_11.8kV | 93 | 1 | 92 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 41; skipped invalid branches: 0.

Galvanic zones: 42; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 27_AVALL | MV_11.8kV | 93 | 0 | 0 | 41 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2411 declared bus terminals; 2244 mapped line/closed-switch conductor edges; 167 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 15500.0 | 2.591 | 2982 |
| q_nom | 0.0 | 4640.0 | 2.591 | 2982 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.03 | 3320.0 | 2.132 | 584 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.653 | 41 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 595 of 994 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus986663_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus974862_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680074_consumption' has phase imbalance of 20.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus985271_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680127_consumption' has phase imbalance of 278.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680057_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus962153_consumption' has phase imbalance of 102.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680183_consumption' has phase imbalance of 257.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680290_consumption' has phase imbalance of 106.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680045_consumption' has phase imbalance of 270.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus962151_consumption' has phase imbalance of 107.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679958_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus955137_consumption' has phase imbalance of 258.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus950619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680237_consumption' has phase imbalance of 67.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680119_consumption' has phase imbalance of 271.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus968121_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680241_consumption' has phase imbalance of 252.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680378_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680053_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus947284_consumption' has phase imbalance of 234.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680118_consumption' has phase imbalance of 282.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680268_consumption' has phase imbalance of 24.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus953642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus984518_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680215_consumption' has phase imbalance of 127.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680302_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus968877_consumption' has phase imbalance of 211.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679992_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680034_consumption' has phase imbalance of 105.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680029_consumption' has phase imbalance of 181.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679981_consumption' has phase imbalance of 57.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680335_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679939_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680031_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680211_consumption' has phase imbalance of 86.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679938_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680067_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680108_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680289_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680243_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus945353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus979787_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679964_consumption' has phase imbalance of 260.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680137_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680214_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680168_consumption' has phase imbalance of 37.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680387_consumption' has phase imbalance of 298.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680158_consumption' has phase imbalance of 148.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680205_consumption' has phase imbalance of 269.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680085_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680078_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680055_consumption' has phase imbalance of 234.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1004436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680047_consumption' has phase imbalance of 208.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680369_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679956_consumption' has phase imbalance of 140.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680376_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680313_consumption' has phase imbalance of 133.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus955020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680334_consumption' has phase imbalance of 261.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus970391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680106_consumption' has phase imbalance of 176.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680252_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680389_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680203_consumption' has phase imbalance of 250.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680270_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus979786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus984517_consumption' has phase imbalance of 23.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680206_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus953638_consumption' has phase imbalance of 239.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680310_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus985272_consumption' has phase imbalance of 218.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus974861_consumption' has phase imbalance of 252.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680112_consumption' has phase imbalance of 208.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680116_consumption' has phase imbalance of 209.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680364_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680375_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680357_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680200_consumption' has phase imbalance of 113.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680180_consumption' has phase imbalance of 256.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679978_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680003_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680319_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus924751_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680164_consumption' has phase imbalance of 186.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus955088_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus947281_consumption' has phase imbalance of 287.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680386_consumption' has phase imbalance of 217.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680324_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680202_consumption' has phase imbalance of 213.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680172_consumption' has phase imbalance of 188.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680178_consumption' has phase imbalance of 144.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus983051_consumption' has phase imbalance of 249.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus981082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus962150_consumption' has phase imbalance of 247.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680102_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680044_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680256_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679944_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680299_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680019_consumption' has phase imbalance of 244.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680176_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680348_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus947282_consumption' has phase imbalance of 291.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680050_consumption' has phase imbalance of 282.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus962147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680066_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus992269_consumption' has phase imbalance of 281.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680209_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680236_consumption' has phase imbalance of 287.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679979_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680083_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680344_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680179_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680281_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680394_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680162_consumption' has phase imbalance of 187.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679990_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680238_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680278_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680165_consumption' has phase imbalance of 271.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680046_consumption' has phase imbalance of 295.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680388_consumption' has phase imbalance of 138.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679960_consumption' has phase imbalance of 228.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679995_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680329_consumption' has phase imbalance of 42.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680148_consumption' has phase imbalance of 229.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus967214_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680080_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680185_consumption' has phase imbalance of 275.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680345_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680336_consumption' has phase imbalance of 263.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680293_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680260_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680212_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680001_consumption' has phase imbalance of 212.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680065_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680258_consumption' has phase imbalance of 256.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679967_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680021_consumption' has phase imbalance of 250.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680040_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679948_consumption' has phase imbalance of 49.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679954_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus981035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680008_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679971_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus962152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680017_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679984_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680184_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus977618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus974864_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679962_consumption' has phase imbalance of 69.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680275_consumption' has phase imbalance of 169.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus953746_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680332_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus926461_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679994_consumption' has phase imbalance of 206.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus921647_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679945_consumption' has phase imbalance of 75.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680052_consumption' has phase imbalance of 281.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680266_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680196_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680015_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus955743_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000184_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679947_consumption' has phase imbalance of 89.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680320_consumption' has phase imbalance of 78.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000181_consumption' has phase imbalance of 281.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680298_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680204_consumption' has phase imbalance of 52.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus974863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680145_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680213_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679982_consumption' has phase imbalance of 111.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1008149_consumption' has phase imbalance of 24.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680126_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000182_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus921060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680032_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus947285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680363_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680259_consumption' has phase imbalance of 264.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680351_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679965_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus921646_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus953644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680012_consumption' has phase imbalance of 97.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680115_consumption' has phase imbalance of 252.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680306_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1008152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680239_consumption' has phase imbalance of 201.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus982190_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680254_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680177_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680171_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus953639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680300_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus962149_consumption' has phase imbalance of 281.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus947283_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680314_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680007_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680393_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus984521_consumption' has phase imbalance of 278.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680383_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus926946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000183_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680138_consumption' has phase imbalance of 278.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus984519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680265_consumption' has phase imbalance of 160.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679966_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680135_consumption' has phase imbalance of 228.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680123_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680193_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680075_consumption' has phase imbalance of 280.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680020_consumption' has phase imbalance of 268.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680170_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus948150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680296_consumption' has phase imbalance of 100.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1003427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680149_consumption' has phase imbalance of 271.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus962148_consumption' has phase imbalance of 65.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680279_consumption' has phase imbalance of 59.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680081_consumption' has phase imbalance of 237.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679975_consumption' has phase imbalance of 142.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus953643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680076_consumption' has phase imbalance of 271.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680006_consumption' has phase imbalance of 20.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680114_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679959_consumption' has phase imbalance of 187.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680272_consumption' has phase imbalance of 268.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680166_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus993637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679976_consumption' has phase imbalance of 222.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus974866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680307_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679977_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus984520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679953_consumption' has phase imbalance of 230.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680014_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680004_consumption' has phase imbalance of 120.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679940_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680041_consumption' has phase imbalance of 288.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679957_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679946_consumption' has phase imbalance of 215.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680384_consumption' has phase imbalance of 250.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000175_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680283_consumption' has phase imbalance of 277.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680226_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus978057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680346_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680358_consumption' has phase imbalance of 126.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680141_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680347_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680062_consumption' has phase imbalance of 68.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus977617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679931_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680197_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680263_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680338_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680174_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680261_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680219_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679983_consumption' has phase imbalance of 294.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus979785_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680186_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679937_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1000178_consumption' has phase imbalance of 263.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680253_consumption' has phase imbalance of 131.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680208_consumption' has phase imbalance of 117.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus921059_consumption' has phase imbalance of 284.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus679961_consumption' has phase imbalance of 116.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680396_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus948890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus680242_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 994 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_LVBus679986' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_LVBus680090' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_LVBus680228' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.736 MW |
| Total load Q | 520.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 27_MVLV17464_Transformer | 176.0 kVA | 18.5% |
| 27_MVLV07961_Transformer | 176.0 kVA | 28.7% |
| 27_MVLV18584_Transformer | 110.0 kVA | 0.0% |
| 27_MVLV66366_Transformer | 176.0 kVA | 12.5% |
| 27_MVLV75049_Transformer | 275.0 kVA | 20.2% |
| 27_MVLV58284_Transformer | 275.0 kVA | 13.2% |
| 27_MVLV15680_Transformer | 176.0 kVA | 14.8% |
| 27_MVLV40481_Transformer | 275.0 kVA | 18.2% |
| 27_MVLV17363_Transformer | 110.0 kVA | 1.7% |
| 27_MVLV01136_Transformer | 176.0 kVA | 18.7% |
| 27_MVLV50721_Transformer | 176.0 kVA | 0.0% |
| 27_MVLV58008_Transformer | 110.0 kVA | 1.2% |
| 27_MVLV21480_Transformer | 110.0 kVA | 10.5% |
| 27_MVLV63143_Transformer | 440.0 kVA | 28.0% |
| 27_MVLV19041_Transformer | 110.0 kVA | 1.7% |
| 27_MVLV43664_Transformer | 110.0 kVA | 6.9% |
| 27_MVLV18763_Transformer | 440.0 kVA | 36.6% |
| 27_MVLV06948_Transformer | 275.0 kVA | 21.8% |
| 27_MVLV18764_Transformer | 110.0 kVA | 2.9% |
| 27_MVLV83035_Transformer | 275.0 kVA | 31.5% |
| 27_MVLV39032_Transformer | 176.0 kVA | 7.1% |
| 27_MVLV03854_Transformer | 693.0 kVA | 30.5% |
| 27_MVLV75032_Transformer | 176.0 kVA | 30.3% |
| 27_MVLV70484_Transformer | 440.0 kVA | 30.6% |
| 27_MVLV09688_Transformer | 176.0 kVA | 14.4% |
| 27_MVLV17463_Transformer | 110.0 kVA | 13.2% |
| 27_MVLV62689_Transformer | 110.0 kVA | 0.1% |
| 27_MVLV75379_Transformer | 110.0 kVA | 9.3% |
| 27_MVLV18727_Transformer | 693.0 kVA | 26.3% |
| 27_MVLV43462_Transformer | 176.0 kVA | 12.4% |
| 27_MVLV30800_Transformer | 176.0 kVA | 27.3% |
| 27_MVLV66367_Transformer | 176.0 kVA | 7.7% |
| 27_MVLV74748_Transformer | 275.0 kVA | 24.4% |
| 27_MVLV72921_Transformer | 176.0 kVA | 13.1% |
| 27_MVLV21972_Transformer | 176.0 kVA | 6.7% |
| 27_MVLV23727_Transformer | 275.0 kVA | 20.5% |
| 27_MVLV45023_Transformer | 440.0 kVA | 28.9% |
| 27_MVLV07960_Transformer | 110.0 kVA | 5.6% |
| 27_MVLV04234_Transformer | 110.0 kVA | 5.7% |
| 27_MVLV41365_Transformer | 176.0 kVA | 12.6% |
| 27_MVLV43463_Transformer | 110.0 kVA | 0.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.74 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '27_AVALL' (MV, 11.78 kV) has an electrical reach of 20.75 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '27_LVBus1003427' (LV, 0.24 kV) has an electrical reach of 1.16 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '27_LVBus680123' (LV, 0.24 kV) has an electrical reach of 1.2 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '27_LVBus680224' (LV, 0.24 kV) has an electrical reach of 7.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '27_LVBus1005218' (LV, 0.24 kV) has an electrical reach of 1.53 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '27_LVBus679971' (LV, 0.24 kV) has an electrical reach of 1.1 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '27_LVBus680228' (LV, 0.24 kV) has an electrical reach of 10.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '27_LVBus680268' (LV, 0.24 kV) has an electrical reach of 3.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '27_LVBus680092' (LV, 0.24 kV) has an electrical reach of 26.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 626 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 626 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 41 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 93 |
| LV_236V | 4-wire | 533 / 533 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 533 |
| Neutral branches | 492 |
| Grounding points | 41 |
| Neutral sections | 41 |
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
| 11.78 kV | 93 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 50 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 42 |
| Islands without voltage reference | 0 |
| Line impedance spread | 3570.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 533 / 93 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 596 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 596 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus1000175_production, 27_LVBus1000176_production, 27_LVBus1000177_production, 27_LVBus1000178_production, 27_LVBus1000179_production, 27_LVBus1000180_consumption, 27_LVBus1000180_production, 27_LVBus1000181_production, 27_LVBus1000182_production, 27_LVBus1000183_production, 27_LVBus1000184_production, 27_LVBus1003427_production, 27_LVBus1004436_production, 27_LVBus1004437_consumption, 27_LVBus1004437_production, 27_LVBus1005218_consumption, 27_LVBus1005218_production, 27_LVBus1008149_production, 27_LVBus1008150_consumption, 27_LVBus1008150_production, 27_LVBus1008151_consumption, 27_LVBus1008151_production, 27_LVBus1008152_production, 27_LVBus679928_production, 27_LVBus679930_consumption, 27_LVBus679930_production, 27_LVBus679931_production, 27_LVBus679932_consumption, 27_LVBus679932_production, 27_LVBus679933_production, 27_LVBus679935_production, 27_LVBus679937_production, 27_LVBus679938_production, 27_LVBus679939_production, 27_LVBus679940_production, 27_LVBus679942_production, 27_LVBus679943_consumption, 27_LVBus679943_production, 27_LVBus679944_production, 27_LVBus679945_production, 27_LVBus679946_production, 27_LVBus679947_production, 27_LVBus679948_production, 27_LVBus679949_consumption, 27_LVBus679949_production, 27_LVBus679950_consumption, 27_LVBus679950_production, 27_LVBus679951_production, 27_LVBus679952_production, 27_LVBus679953_production, 27_LVBus679954_production, 27_LVBus679956_production, 27_LVBus679957_production, 27_LVBus679958_production, 27_LVBus679959_production, 27_LVBus679960_production, 27_LVBus679961_production, 27_LVBus679962_production, 27_LVBus679963_production, 27_LVBus679964_production, 27_LVBus679965_production, 27_LVBus679966_production, 27_LVBus679967_production, 27_LVBus679969_production, 27_LVBus679971_production, 27_LVBus679975_production, 27_LVBus679976_production, 27_LVBus679977_production, 27_LVBus679978_production, 27_LVBus679979_production, 27_LVBus679980_consumption, 27_LVBus679980_production, 27_LVBus679981_production, 27_LVBus679982_production, 27_LVBus679983_production, 27_LVBus679984_production, 27_LVBus679986_consumption, 27_LVBus679986_production, 27_LVBus679987_consumption, 27_LVBus679987_production, 27_LVBus679988_production, 27_LVBus679990_production, 27_LVBus679992_production, 27_LVBus679994_production, 27_LVBus679995_production, 27_LVBus679996_production, 27_LVBus679997_consumption, 27_LVBus679997_production, 27_LVBus679998_production, 27_LVBus679999_production, 27_LVBus680000_production, 27_LVBus680001_production, 27_LVBus680003_production, 27_LVBus680004_production, 27_LVBus680006_production, 27_LVBus680007_production, 27_LVBus680008_production, 27_LVBus680009_consumption, 27_LVBus680009_production, 27_LVBus680011_consumption, 27_LVBus680011_production, 27_LVBus680012_production, 27_LVBus680014_production, 27_LVBus680015_production, 27_LVBus680017_production, 27_LVBus680018_production, 27_LVBus680019_production, 27_LVBus680020_production, 27_LVBus680021_production, 27_LVBus680025_consumption, 27_LVBus680025_production, 27_LVBus680027_production, 27_LVBus680029_production, 27_LVBus680031_production, 27_LVBus680032_production, 27_LVBus680033_production, 27_LVBus680034_production, 27_LVBus680035_consumption, 27_LVBus680035_production, 27_LVBus680036_consumption, 27_LVBus680036_production, 27_LVBus680038_production, 27_LVBus680039_consumption, 27_LVBus680039_production, 27_LVBus680040_production, 27_LVBus680041_production, 27_LVBus680042_production, 27_LVBus680043_production, 27_LVBus680044_production, 27_LVBus680045_production, 27_LVBus680046_production, 27_LVBus680047_production, 27_LVBus680048_production, 27_LVBus680049_production, 27_LVBus680050_production, 27_LVBus680051_production, 27_LVBus680052_production, 27_LVBus680053_production, 27_LVBus680054_consumption, 27_LVBus680054_production, 27_LVBus680055_production, 27_LVBus680056_production, 27_LVBus680057_production, 27_LVBus680059_consumption, 27_LVBus680059_production, 27_LVBus680060_consumption, 27_LVBus680060_production, 27_LVBus680061_production, 27_LVBus680062_production, 27_LVBus680063_production, 27_LVBus680064_production, 27_LVBus680065_production, 27_LVBus680066_production, 27_LVBus680067_production, 27_LVBus680068_production, 27_LVBus680070_consumption, 27_LVBus680070_production, 27_LVBus680071_production, 27_LVBus680072_production, 27_LVBus680073_production, 27_LVBus680074_production, 27_LVBus680075_production, 27_LVBus680076_production, 27_LVBus680077_production, 27_LVBus680078_production, 27_LVBus680079_production, 27_LVBus680080_production, 27_LVBus680081_production, 27_LVBus680082_production, 27_LVBus680083_production, 27_LVBus680084_production, 27_LVBus680085_production, 27_LVBus680086_production, 27_LVBus680090_production, 27_LVBus680092_production, 27_LVBus680094_production, 27_LVBus680098_consumption, 27_LVBus680098_production, 27_LVBus680100_consumption, 27_LVBus680100_production, 27_LVBus680102_production, 27_LVBus680104_production, 27_LVBus680105_consumption, 27_LVBus680105_production, 27_LVBus680106_production, 27_LVBus680108_production, 27_LVBus680110_production, 27_LVBus680111_consumption, 27_LVBus680111_production, 27_LVBus680112_production, 27_LVBus680113_production, 27_LVBus680114_production, 27_LVBus680115_production, 27_LVBus680116_production, 27_LVBus680117_consumption, 27_LVBus680117_production, 27_LVBus680118_production, 27_LVBus680119_production, 27_LVBus680121_production, 27_LVBus680123_production, 27_LVBus680124_production, 27_LVBus680125_production, 27_LVBus680126_production, 27_LVBus680127_production, 27_LVBus680128_production, 27_LVBus680129_consumption, 27_LVBus680129_production, 27_LVBus680130_consumption, 27_LVBus680130_production, 27_LVBus680131_production, 27_LVBus680132_consumption, 27_LVBus680132_production, 27_LVBus680133_consumption, 27_LVBus680133_production, 27_LVBus680134_production, 27_LVBus680135_production, 27_LVBus680136_production, 27_LVBus680137_production, 27_LVBus680138_production, 27_LVBus680139_consumption, 27_LVBus680139_production, 27_LVBus680140_consumption, 27_LVBus680140_production, 27_LVBus680141_production, 27_LVBus680142_production, 27_LVBus680144_production, 27_LVBus680145_production, 27_LVBus680146_consumption, 27_LVBus680146_production, 27_LVBus680147_production, 27_LVBus680148_production, 27_LVBus680149_production, 27_LVBus680150_production, 27_LVBus680151_consumption, 27_LVBus680151_production, 27_LVBus680152_production, 27_LVBus680154_consumption, 27_LVBus680154_production, 27_LVBus680158_production, 27_LVBus680159_production, 27_LVBus680160_production, 27_LVBus680161_consumption, 27_LVBus680161_production, 27_LVBus680162_production, 27_LVBus680163_production, 27_LVBus680164_production, 27_LVBus680165_production, 27_LVBus680166_production, 27_LVBus680167_production, 27_LVBus680168_production, 27_LVBus680169_production, 27_LVBus680170_production, 27_LVBus680171_production, 27_LVBus680172_production, 27_LVBus680173_production, 27_LVBus680174_production, 27_LVBus680176_production, 27_LVBus680177_production, 27_LVBus680178_production, 27_LVBus680179_production, 27_LVBus680180_production, 27_LVBus680182_production, 27_LVBus680183_production, 27_LVBus680184_production, 27_LVBus680185_production, 27_LVBus680186_production, 27_LVBus680188_production, 27_LVBus680189_consumption, 27_LVBus680189_production, 27_LVBus680190_consumption, 27_LVBus680190_production, 27_LVBus680191_production, 27_LVBus680193_production, 27_LVBus680194_consumption, 27_LVBus680194_production, 27_LVBus680196_production, 27_LVBus680197_production, 27_LVBus680199_production, 27_LVBus680200_production, 27_LVBus680201_production, 27_LVBus680202_production, 27_LVBus680203_production, 27_LVBus680204_production, 27_LVBus680205_production, 27_LVBus680206_production, 27_LVBus680208_production, 27_LVBus680209_production, 27_LVBus680210_production, 27_LVBus680211_production, 27_LVBus680212_production, 27_LVBus680213_production, 27_LVBus680214_production, 27_LVBus680215_production, 27_LVBus680217_consumption, 27_LVBus680217_production, 27_LVBus680218_production, 27_LVBus680219_production, 27_LVBus680220_production, 27_LVBus680222_production, 27_LVBus680224_consumption, 27_LVBus680224_production, 27_LVBus680226_production, 27_LVBus680228_production, 27_LVBus680230_consumption, 27_LVBus680230_production, 27_LVBus680231_consumption, 27_LVBus680231_production, 27_LVBus680232_consumption, 27_LVBus680232_production, 27_LVBus680233_consumption, 27_LVBus680233_production, 27_LVBus680234_production, 27_LVBus680236_production, 27_LVBus680237_production, 27_LVBus680238_production, 27_LVBus680239_production, 27_LVBus680240_production, 27_LVBus680241_production, 27_LVBus680242_production, 27_LVBus680243_production, 27_LVBus680244_production, 27_LVBus680246_production, 27_LVBus680248_consumption, 27_LVBus680248_production, 27_LVBus680249_consumption, 27_LVBus680249_production, 27_LVBus680250_consumption, 27_LVBus680250_production, 27_LVBus680251_production, 27_LVBus680252_production, 27_LVBus680253_production, 27_LVBus680254_production, 27_LVBus680255_production, 27_LVBus680256_production, 27_LVBus680257_production, 27_LVBus680258_production, 27_LVBus680259_production, 27_LVBus680260_production, 27_LVBus680261_production, 27_LVBus680263_production, 27_LVBus680264_production, 27_LVBus680265_production, 27_LVBus680266_production, 27_LVBus680268_production, 27_LVBus680270_production, 27_LVBus680271_consumption, 27_LVBus680271_production, 27_LVBus680272_production, 27_LVBus680273_production, 27_LVBus680275_production, 27_LVBus680276_production, 27_LVBus680277_production, 27_LVBus680278_production, 27_LVBus680279_production, 27_LVBus680280_production, 27_LVBus680281_production, 27_LVBus680283_production, 27_LVBus680284_production, 27_LVBus680285_production, 27_LVBus680286_production, 27_LVBus680288_consumption, 27_LVBus680288_production, 27_LVBus680289_production, 27_LVBus680290_production, 27_LVBus680291_production, 27_LVBus680292_production, 27_LVBus680293_production, 27_LVBus680294_production, 27_LVBus680295_production, 27_LVBus680296_production, 27_LVBus680298_production, 27_LVBus680299_production, 27_LVBus680300_production, 27_LVBus680302_production, 27_LVBus680303_production, 27_LVBus680304_production, 27_LVBus680306_production, 27_LVBus680307_production, 27_LVBus680308_production, 27_LVBus680309_production, 27_LVBus680310_production, 27_LVBus680312_consumption, 27_LVBus680312_production, 27_LVBus680313_production, 27_LVBus680314_production, 27_LVBus680316_consumption, 27_LVBus680316_production, 27_LVBus680318_consumption, 27_LVBus680318_production, 27_LVBus680319_production, 27_LVBus680320_production, 27_LVBus680322_consumption, 27_LVBus680322_production, 27_LVBus680324_production, 27_LVBus680325_production, 27_LVBus680326_production, 27_LVBus680327_consumption, 27_LVBus680327_production, 27_LVBus680328_production, 27_LVBus680329_production, 27_LVBus680330_consumption, 27_LVBus680330_production, 27_LVBus680331_consumption, 27_LVBus680331_production, 27_LVBus680332_production, 27_LVBus680333_production, 27_LVBus680334_production, 27_LVBus680335_production, 27_LVBus680336_production, 27_LVBus680337_consumption, 27_LVBus680337_production, 27_LVBus680338_production, 27_LVBus680339_production, 27_LVBus680340_production, 27_LVBus680341_production, 27_LVBus680342_production, 27_LVBus680344_production, 27_LVBus680345_production, 27_LVBus680346_production, 27_LVBus680347_production, 27_LVBus680348_production, 27_LVBus680349_consumption, 27_LVBus680349_production, 27_LVBus680351_production, 27_LVBus680352_production, 27_LVBus680353_production, 27_LVBus680354_production, 27_LVBus680355_consumption, 27_LVBus680355_production, 27_LVBus680357_production, 27_LVBus680358_production, 27_LVBus680361_consumption, 27_LVBus680361_production, 27_LVBus680362_production, 27_LVBus680363_production, 27_LVBus680364_production, 27_LVBus680365_consumption, 27_LVBus680365_production, 27_LVBus680367_production, 27_LVBus680368_consumption, 27_LVBus680368_production, 27_LVBus680369_production, 27_LVBus680370_consumption, 27_LVBus680370_production, 27_LVBus680371_production, 27_LVBus680372_production, 27_LVBus680373_consumption, 27_LVBus680373_production, 27_LVBus680375_production, 27_LVBus680376_production, 27_LVBus680377_production, 27_LVBus680378_production, 27_LVBus680379_production, 27_LVBus680381_consumption, 27_LVBus680381_production, 27_LVBus680382_consumption, 27_LVBus680382_production, 27_LVBus680383_production, 27_LVBus680384_production, 27_LVBus680385_production, 27_LVBus680386_production, 27_LVBus680387_production, 27_LVBus680388_production, 27_LVBus680389_production, 27_LVBus680390_production, 27_LVBus680392_consumption, 27_LVBus680392_production, 27_LVBus680393_production, 27_LVBus680394_production, 27_LVBus680395_consumption, 27_LVBus680395_production, 27_LVBus680396_production, 27_LVBus921057_consumption, 27_LVBus921057_production, 27_LVBus921058_consumption, 27_LVBus921058_production, 27_LVBus921059_production, 27_LVBus921060_production, 27_LVBus921646_production, 27_LVBus921647_production, 27_LVBus921648_production, 27_LVBus924725_consumption, 27_LVBus924725_production, 27_LVBus924726_consumption, 27_LVBus924726_production, 27_LVBus924727_consumption, 27_LVBus924727_production, 27_LVBus924728_consumption, 27_LVBus924728_production, 27_LVBus924751_production, 27_LVBus926461_production, 27_LVBus926944_consumption, 27_LVBus926944_production, 27_LVBus926945_consumption, 27_LVBus926945_production, 27_LVBus926946_production, 27_LVBus936342_production, 27_LVBus940932_consumption, 27_LVBus940932_production, 27_LVBus945353_production, 27_LVBus946456_production, 27_LVBus947280_consumption, 27_LVBus947280_production, 27_LVBus947281_production, 27_LVBus947282_production, 27_LVBus947283_production, 27_LVBus947284_production, 27_LVBus947285_production, 27_LVBus948150_production, 27_LVBus948888_production, 27_LVBus948889_production, 27_LVBus948890_production, 27_LVBus950619_production, 27_LVBus953637_consumption, 27_LVBus953637_production, 27_LVBus953638_production, 27_LVBus953639_production, 27_LVBus953640_consumption, 27_LVBus953640_production, 27_LVBus953641_production, 27_LVBus953642_production, 27_LVBus953643_production, 27_LVBus953644_production, 27_LVBus953746_production, 27_LVBus955018_consumption, 27_LVBus955018_production, 27_LVBus955019_consumption, 27_LVBus955019_production, 27_LVBus955020_production, 27_LVBus955088_production, 27_LVBus955137_production, 27_LVBus955138_production, 27_LVBus955743_production, 27_LVBus962147_production, 27_LVBus962148_production, 27_LVBus962149_production, 27_LVBus962150_production, 27_LVBus962151_production, 27_LVBus962152_production, 27_LVBus962153_production, 27_LVBus967214_production, 27_LVBus968120_consumption, 27_LVBus968120_production, 27_LVBus968121_production, 27_LVBus968877_production, 27_LVBus970391_production, 27_LVBus970392_consumption, 27_LVBus970392_production, 27_LVBus973644_consumption, 27_LVBus973644_production, 27_LVBus974861_production, 27_LVBus974862_production, 27_LVBus974863_production, 27_LVBus974864_production, 27_LVBus974865_consumption, 27_LVBus974865_production, 27_LVBus974866_production, 27_LVBus974867_production, 27_LVBus977617_production, 27_LVBus977618_production, 27_LVBus978057_production, 27_LVBus979785_production, 27_LVBus979786_production, 27_LVBus979787_production, 27_LVBus979788_consumption, 27_LVBus979788_production, 27_LVBus981035_production, 27_LVBus981082_production, 27_LVBus982190_production, 27_LVBus983051_production, 27_LVBus984517_production, 27_LVBus984518_production, 27_LVBus984519_production, 27_LVBus984520_production, 27_LVBus984521_production, 27_LVBus985271_production, 27_LVBus985272_production, 27_LVBus986663_production, 27_LVBus986664_consumption, 27_LVBus986664_production, 27_LVBus992269_production, 27_LVBus992270_consumption, 27_LVBus992270_production, 27_LVBus993637_production, 27_LVBus999058_consumption, 27_LVBus999058_production, 27_MVLV03103_consumption, 27_MVLV03103_production, 27_MVLV07531_consumption, 27_MVLV07531_production, 27_MVLV38575_consumption, 27_MVLV38575_production, 27_MVLV66368_consumption, 27_MVLV66368_production, 27_MVLV67000_consumption, 27_MVLV67000_production.

## 9. Data Quality Summary

**Total findings:** 397 (0 errors, 4 warnings, 393 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  595 of 994 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.74 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  596 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus986663_consumption`  
  Load '27_LVBus986663_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus974862_consumption`  
  Load '27_LVBus974862_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680074_consumption`  
  Load '27_LVBus680074_consumption' has phase imbalance of 20.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus985271_consumption`  
  Load '27_LVBus985271_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680167_consumption`  
  Load '27_LVBus680167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680285_consumption`  
  Load '27_LVBus680285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680127_consumption`  
  Load '27_LVBus680127_consumption' has phase imbalance of 278.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680057_consumption`  
  Load '27_LVBus680057_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus962153_consumption`  
  Load '27_LVBus962153_consumption' has phase imbalance of 102.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680131_consumption`  
  Load '27_LVBus680131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680183_consumption`  
  Load '27_LVBus680183_consumption' has phase imbalance of 257.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680290_consumption`  
  Load '27_LVBus680290_consumption' has phase imbalance of 106.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680045_consumption`  
  Load '27_LVBus680045_consumption' has phase imbalance of 270.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus962151_consumption`  
  Load '27_LVBus962151_consumption' has phase imbalance of 107.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679958_consumption`  
  Load '27_LVBus679958_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus955137_consumption`  
  Load '27_LVBus955137_consumption' has phase imbalance of 258.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus950619_consumption`  
  Load '27_LVBus950619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680237_consumption`  
  Load '27_LVBus680237_consumption' has phase imbalance of 67.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680119_consumption`  
  Load '27_LVBus680119_consumption' has phase imbalance of 271.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus968121_consumption`  
  Load '27_LVBus968121_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680241_consumption`  
  Load '27_LVBus680241_consumption' has phase imbalance of 252.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680048_consumption`  
  Load '27_LVBus680048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680378_consumption`  
  Load '27_LVBus680378_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680053_consumption`  
  Load '27_LVBus680053_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus947284_consumption`  
  Load '27_LVBus947284_consumption' has phase imbalance of 234.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680244_consumption`  
  Load '27_LVBus680244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680125_consumption`  
  Load '27_LVBus680125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680118_consumption`  
  Load '27_LVBus680118_consumption' has phase imbalance of 282.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680268_consumption`  
  Load '27_LVBus680268_consumption' has phase imbalance of 24.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus953642_consumption`  
  Load '27_LVBus953642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus984518_consumption`  
  Load '27_LVBus984518_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680215_consumption`  
  Load '27_LVBus680215_consumption' has phase imbalance of 127.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680302_consumption`  
  Load '27_LVBus680302_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus968877_consumption`  
  Load '27_LVBus968877_consumption' has phase imbalance of 211.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679992_consumption`  
  Load '27_LVBus679992_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680251_consumption`  
  Load '27_LVBus680251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680034_consumption`  
  Load '27_LVBus680034_consumption' has phase imbalance of 105.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680372_consumption`  
  Load '27_LVBus680372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680029_consumption`  
  Load '27_LVBus680029_consumption' has phase imbalance of 181.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679981_consumption`  
  Load '27_LVBus679981_consumption' has phase imbalance of 57.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680335_consumption`  
  Load '27_LVBus680335_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679939_consumption`  
  Load '27_LVBus679939_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680340_consumption`  
  Load '27_LVBus680340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680031_consumption`  
  Load '27_LVBus680031_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680211_consumption`  
  Load '27_LVBus680211_consumption' has phase imbalance of 86.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679938_consumption`  
  Load '27_LVBus679938_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680067_consumption`  
  Load '27_LVBus680067_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680108_consumption`  
  Load '27_LVBus680108_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680289_consumption`  
  Load '27_LVBus680289_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680042_consumption`  
  Load '27_LVBus680042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680243_consumption`  
  Load '27_LVBus680243_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680092_consumption`  
  Load '27_LVBus680092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus945353_consumption`  
  Load '27_LVBus945353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus979787_consumption`  
  Load '27_LVBus979787_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679964_consumption`  
  Load '27_LVBus679964_consumption' has phase imbalance of 260.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680137_consumption`  
  Load '27_LVBus680137_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680214_consumption`  
  Load '27_LVBus680214_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680168_consumption`  
  Load '27_LVBus680168_consumption' has phase imbalance of 37.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680387_consumption`  
  Load '27_LVBus680387_consumption' has phase imbalance of 298.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680158_consumption`  
  Load '27_LVBus680158_consumption' has phase imbalance of 148.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680205_consumption`  
  Load '27_LVBus680205_consumption' has phase imbalance of 269.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680085_consumption`  
  Load '27_LVBus680085_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680078_consumption`  
  Load '27_LVBus680078_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680292_consumption`  
  Load '27_LVBus680292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680055_consumption`  
  Load '27_LVBus680055_consumption' has phase imbalance of 234.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680128_consumption`  
  Load '27_LVBus680128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1004436_consumption`  
  Load '27_LVBus1004436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680051_consumption`  
  Load '27_LVBus680051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680047_consumption`  
  Load '27_LVBus680047_consumption' has phase imbalance of 208.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680018_consumption`  
  Load '27_LVBus680018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680369_consumption`  
  Load '27_LVBus680369_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679956_consumption`  
  Load '27_LVBus679956_consumption' has phase imbalance of 140.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680385_consumption`  
  Load '27_LVBus680385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680376_consumption`  
  Load '27_LVBus680376_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680124_consumption`  
  Load '27_LVBus680124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680313_consumption`  
  Load '27_LVBus680313_consumption' has phase imbalance of 133.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus955020_consumption`  
  Load '27_LVBus955020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680334_consumption`  
  Load '27_LVBus680334_consumption' has phase imbalance of 261.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus970391_consumption`  
  Load '27_LVBus970391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680169_consumption`  
  Load '27_LVBus680169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680106_consumption`  
  Load '27_LVBus680106_consumption' has phase imbalance of 176.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680252_consumption`  
  Load '27_LVBus680252_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680389_consumption`  
  Load '27_LVBus680389_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680203_consumption`  
  Load '27_LVBus680203_consumption' has phase imbalance of 250.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680218_consumption`  
  Load '27_LVBus680218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680270_consumption`  
  Load '27_LVBus680270_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus979786_consumption`  
  Load '27_LVBus979786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus984517_consumption`  
  Load '27_LVBus984517_consumption' has phase imbalance of 23.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680152_consumption`  
  Load '27_LVBus680152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680206_consumption`  
  Load '27_LVBus680206_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680276_consumption`  
  Load '27_LVBus680276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus953638_consumption`  
  Load '27_LVBus953638_consumption' has phase imbalance of 239.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680310_consumption`  
  Load '27_LVBus680310_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus985272_consumption`  
  Load '27_LVBus985272_consumption' has phase imbalance of 218.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus974861_consumption`  
  Load '27_LVBus974861_consumption' has phase imbalance of 252.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680112_consumption`  
  Load '27_LVBus680112_consumption' has phase imbalance of 208.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680116_consumption`  
  Load '27_LVBus680116_consumption' has phase imbalance of 209.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680303_consumption`  
  Load '27_LVBus680303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680364_consumption`  
  Load '27_LVBus680364_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680375_consumption`  
  Load '27_LVBus680375_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680357_consumption`  
  Load '27_LVBus680357_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680200_consumption`  
  Load '27_LVBus680200_consumption' has phase imbalance of 113.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680159_consumption`  
  Load '27_LVBus680159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680033_consumption`  
  Load '27_LVBus680033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680180_consumption`  
  Load '27_LVBus680180_consumption' has phase imbalance of 256.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679978_consumption`  
  Load '27_LVBus679978_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679952_consumption`  
  Load '27_LVBus679952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680003_consumption`  
  Load '27_LVBus680003_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680319_consumption`  
  Load '27_LVBus680319_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus924751_consumption`  
  Load '27_LVBus924751_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680308_consumption`  
  Load '27_LVBus680308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680164_consumption`  
  Load '27_LVBus680164_consumption' has phase imbalance of 186.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus955088_consumption`  
  Load '27_LVBus955088_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus947281_consumption`  
  Load '27_LVBus947281_consumption' has phase imbalance of 287.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680386_consumption`  
  Load '27_LVBus680386_consumption' has phase imbalance of 217.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680324_consumption`  
  Load '27_LVBus680324_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680202_consumption`  
  Load '27_LVBus680202_consumption' has phase imbalance of 213.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680172_consumption`  
  Load '27_LVBus680172_consumption' has phase imbalance of 188.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680178_consumption`  
  Load '27_LVBus680178_consumption' has phase imbalance of 144.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus983051_consumption`  
  Load '27_LVBus983051_consumption' has phase imbalance of 249.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus981082_consumption`  
  Load '27_LVBus981082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680286_consumption`  
  Load '27_LVBus680286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus962150_consumption`  
  Load '27_LVBus962150_consumption' has phase imbalance of 247.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680160_consumption`  
  Load '27_LVBus680160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680371_consumption`  
  Load '27_LVBus680371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000176_consumption`  
  Load '27_LVBus1000176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680102_consumption`  
  Load '27_LVBus680102_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680000_consumption`  
  Load '27_LVBus680000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680377_consumption`  
  Load '27_LVBus680377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680044_consumption`  
  Load '27_LVBus680044_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680256_consumption`  
  Load '27_LVBus680256_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679944_consumption`  
  Load '27_LVBus679944_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680299_consumption`  
  Load '27_LVBus680299_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680019_consumption`  
  Load '27_LVBus680019_consumption' has phase imbalance of 244.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680176_consumption`  
  Load '27_LVBus680176_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680348_consumption`  
  Load '27_LVBus680348_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus947282_consumption`  
  Load '27_LVBus947282_consumption' has phase imbalance of 291.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680050_consumption`  
  Load '27_LVBus680050_consumption' has phase imbalance of 282.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus962147_consumption`  
  Load '27_LVBus962147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680066_consumption`  
  Load '27_LVBus680066_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus992269_consumption`  
  Load '27_LVBus992269_consumption' has phase imbalance of 281.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680209_consumption`  
  Load '27_LVBus680209_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680236_consumption`  
  Load '27_LVBus680236_consumption' has phase imbalance of 287.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680144_consumption`  
  Load '27_LVBus680144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680134_consumption`  
  Load '27_LVBus680134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679979_consumption`  
  Load '27_LVBus679979_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680083_consumption`  
  Load '27_LVBus680083_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680344_consumption`  
  Load '27_LVBus680344_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680150_consumption`  
  Load '27_LVBus680150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680179_consumption`  
  Load '27_LVBus680179_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680281_consumption`  
  Load '27_LVBus680281_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680394_consumption`  
  Load '27_LVBus680394_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680043_consumption`  
  Load '27_LVBus680043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680147_consumption`  
  Load '27_LVBus680147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680162_consumption`  
  Load '27_LVBus680162_consumption' has phase imbalance of 187.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679990_consumption`  
  Load '27_LVBus679990_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680182_consumption`  
  Load '27_LVBus680182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680238_consumption`  
  Load '27_LVBus680238_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680278_consumption`  
  Load '27_LVBus680278_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680165_consumption`  
  Load '27_LVBus680165_consumption' has phase imbalance of 271.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680046_consumption`  
  Load '27_LVBus680046_consumption' has phase imbalance of 295.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680388_consumption`  
  Load '27_LVBus680388_consumption' has phase imbalance of 138.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000179_consumption`  
  Load '27_LVBus1000179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680325_consumption`  
  Load '27_LVBus680325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680061_consumption`  
  Load '27_LVBus680061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679960_consumption`  
  Load '27_LVBus679960_consumption' has phase imbalance of 228.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679995_consumption`  
  Load '27_LVBus679995_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680329_consumption`  
  Load '27_LVBus680329_consumption' has phase imbalance of 42.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680038_consumption`  
  Load '27_LVBus680038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680148_consumption`  
  Load '27_LVBus680148_consumption' has phase imbalance of 229.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus967214_consumption`  
  Load '27_LVBus967214_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680080_consumption`  
  Load '27_LVBus680080_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680309_consumption`  
  Load '27_LVBus680309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680273_consumption`  
  Load '27_LVBus680273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680185_consumption`  
  Load '27_LVBus680185_consumption' has phase imbalance of 275.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680345_consumption`  
  Load '27_LVBus680345_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680336_consumption`  
  Load '27_LVBus680336_consumption' has phase imbalance of 263.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680293_consumption`  
  Load '27_LVBus680293_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680260_consumption`  
  Load '27_LVBus680260_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680257_consumption`  
  Load '27_LVBus680257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680339_consumption`  
  Load '27_LVBus680339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680379_consumption`  
  Load '27_LVBus680379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680212_consumption`  
  Load '27_LVBus680212_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680333_consumption`  
  Load '27_LVBus680333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680001_consumption`  
  Load '27_LVBus680001_consumption' has phase imbalance of 212.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680065_consumption`  
  Load '27_LVBus680065_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680258_consumption`  
  Load '27_LVBus680258_consumption' has phase imbalance of 256.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679967_consumption`  
  Load '27_LVBus679967_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680021_consumption`  
  Load '27_LVBus680021_consumption' has phase imbalance of 250.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680040_consumption`  
  Load '27_LVBus680040_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679948_consumption`  
  Load '27_LVBus679948_consumption' has phase imbalance of 49.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679954_consumption`  
  Load '27_LVBus679954_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680328_consumption`  
  Load '27_LVBus680328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus981035_consumption`  
  Load '27_LVBus981035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680008_consumption`  
  Load '27_LVBus680008_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679971_consumption`  
  Load '27_LVBus679971_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680191_consumption`  
  Load '27_LVBus680191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus962152_consumption`  
  Load '27_LVBus962152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680017_consumption`  
  Load '27_LVBus680017_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679984_consumption`  
  Load '27_LVBus679984_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680063_consumption`  
  Load '27_LVBus680063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680184_consumption`  
  Load '27_LVBus680184_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680064_consumption`  
  Load '27_LVBus680064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus977618_consumption`  
  Load '27_LVBus977618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680326_consumption`  
  Load '27_LVBus680326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680234_consumption`  
  Load '27_LVBus680234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus974864_consumption`  
  Load '27_LVBus974864_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679962_consumption`  
  Load '27_LVBus679962_consumption' has phase imbalance of 69.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680275_consumption`  
  Load '27_LVBus680275_consumption' has phase imbalance of 169.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus953746_consumption`  
  Load '27_LVBus953746_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680332_consumption`  
  Load '27_LVBus680332_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680277_consumption`  
  Load '27_LVBus680277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus926461_consumption`  
  Load '27_LVBus926461_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679998_consumption`  
  Load '27_LVBus679998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679994_consumption`  
  Load '27_LVBus679994_consumption' has phase imbalance of 206.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus921647_consumption`  
  Load '27_LVBus921647_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680304_consumption`  
  Load '27_LVBus680304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679945_consumption`  
  Load '27_LVBus679945_consumption' has phase imbalance of 75.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680052_consumption`  
  Load '27_LVBus680052_consumption' has phase imbalance of 281.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680266_consumption`  
  Load '27_LVBus680266_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680284_consumption`  
  Load '27_LVBus680284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680196_consumption`  
  Load '27_LVBus680196_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680199_consumption`  
  Load '27_LVBus680199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680110_consumption`  
  Load '27_LVBus680110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680015_consumption`  
  Load '27_LVBus680015_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus955743_consumption`  
  Load '27_LVBus955743_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000184_consumption`  
  Load '27_LVBus1000184_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680255_consumption`  
  Load '27_LVBus680255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679942_consumption`  
  Load '27_LVBus679942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679947_consumption`  
  Load '27_LVBus679947_consumption' has phase imbalance of 89.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680201_consumption`  
  Load '27_LVBus680201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680320_consumption`  
  Load '27_LVBus680320_consumption' has phase imbalance of 78.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000181_consumption`  
  Load '27_LVBus1000181_consumption' has phase imbalance of 281.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680068_consumption`  
  Load '27_LVBus680068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680173_consumption`  
  Load '27_LVBus680173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680298_consumption`  
  Load '27_LVBus680298_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680204_consumption`  
  Load '27_LVBus680204_consumption' has phase imbalance of 52.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus974863_consumption`  
  Load '27_LVBus974863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680145_consumption`  
  Load '27_LVBus680145_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680213_consumption`  
  Load '27_LVBus680213_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679982_consumption`  
  Load '27_LVBus679982_consumption' has phase imbalance of 111.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1008149_consumption`  
  Load '27_LVBus1008149_consumption' has phase imbalance of 24.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680126_consumption`  
  Load '27_LVBus680126_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680163_consumption`  
  Load '27_LVBus680163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000182_consumption`  
  Load '27_LVBus1000182_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus921060_consumption`  
  Load '27_LVBus921060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680032_consumption`  
  Load '27_LVBus680032_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus947285_consumption`  
  Load '27_LVBus947285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680363_consumption`  
  Load '27_LVBus680363_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680259_consumption`  
  Load '27_LVBus680259_consumption' has phase imbalance of 264.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679935_consumption`  
  Load '27_LVBus679935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680353_consumption`  
  Load '27_LVBus680353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680351_consumption`  
  Load '27_LVBus680351_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679965_consumption`  
  Load '27_LVBus679965_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus921646_consumption`  
  Load '27_LVBus921646_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680142_consumption`  
  Load '27_LVBus680142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus953644_consumption`  
  Load '27_LVBus953644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680012_consumption`  
  Load '27_LVBus680012_consumption' has phase imbalance of 97.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680115_consumption`  
  Load '27_LVBus680115_consumption' has phase imbalance of 252.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680306_consumption`  
  Load '27_LVBus680306_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1008152_consumption`  
  Load '27_LVBus1008152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680239_consumption`  
  Load '27_LVBus680239_consumption' has phase imbalance of 201.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus982190_consumption`  
  Load '27_LVBus982190_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680240_consumption`  
  Load '27_LVBus680240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680254_consumption`  
  Load '27_LVBus680254_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680177_consumption`  
  Load '27_LVBus680177_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680171_consumption`  
  Load '27_LVBus680171_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus953639_consumption`  
  Load '27_LVBus953639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680300_consumption`  
  Load '27_LVBus680300_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus962149_consumption`  
  Load '27_LVBus962149_consumption' has phase imbalance of 281.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus947283_consumption`  
  Load '27_LVBus947283_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680314_consumption`  
  Load '27_LVBus680314_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680007_consumption`  
  Load '27_LVBus680007_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680393_consumption`  
  Load '27_LVBus680393_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus984521_consumption`  
  Load '27_LVBus984521_consumption' has phase imbalance of 278.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680383_consumption`  
  Load '27_LVBus680383_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus926946_consumption`  
  Load '27_LVBus926946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000183_consumption`  
  Load '27_LVBus1000183_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680138_consumption`  
  Load '27_LVBus680138_consumption' has phase imbalance of 278.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus984519_consumption`  
  Load '27_LVBus984519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680265_consumption`  
  Load '27_LVBus680265_consumption' has phase imbalance of 160.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679966_consumption`  
  Load '27_LVBus679966_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680135_consumption`  
  Load '27_LVBus680135_consumption' has phase imbalance of 228.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680123_consumption`  
  Load '27_LVBus680123_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680193_consumption`  
  Load '27_LVBus680193_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680075_consumption`  
  Load '27_LVBus680075_consumption' has phase imbalance of 280.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680020_consumption`  
  Load '27_LVBus680020_consumption' has phase imbalance of 268.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680170_consumption`  
  Load '27_LVBus680170_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus948150_consumption`  
  Load '27_LVBus948150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680296_consumption`  
  Load '27_LVBus680296_consumption' has phase imbalance of 100.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1003427_consumption`  
  Load '27_LVBus1003427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680149_consumption`  
  Load '27_LVBus680149_consumption' has phase imbalance of 271.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus962148_consumption`  
  Load '27_LVBus962148_consumption' has phase imbalance of 65.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680279_consumption`  
  Load '27_LVBus680279_consumption' has phase imbalance of 59.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680121_consumption`  
  Load '27_LVBus680121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680081_consumption`  
  Load '27_LVBus680081_consumption' has phase imbalance of 237.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679999_consumption`  
  Load '27_LVBus679999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679975_consumption`  
  Load '27_LVBus679975_consumption' has phase imbalance of 142.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680071_consumption`  
  Load '27_LVBus680071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus953643_consumption`  
  Load '27_LVBus953643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680076_consumption`  
  Load '27_LVBus680076_consumption' has phase imbalance of 271.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680006_consumption`  
  Load '27_LVBus680006_consumption' has phase imbalance of 20.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680114_consumption`  
  Load '27_LVBus680114_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680220_consumption`  
  Load '27_LVBus680220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679959_consumption`  
  Load '27_LVBus679959_consumption' has phase imbalance of 187.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680272_consumption`  
  Load '27_LVBus680272_consumption' has phase imbalance of 268.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680166_consumption`  
  Load '27_LVBus680166_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus993637_consumption`  
  Load '27_LVBus993637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680367_consumption`  
  Load '27_LVBus680367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680354_consumption`  
  Load '27_LVBus680354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000177_consumption`  
  Load '27_LVBus1000177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679976_consumption`  
  Load '27_LVBus679976_consumption' has phase imbalance of 222.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680188_consumption`  
  Load '27_LVBus680188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus974866_consumption`  
  Load '27_LVBus974866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680341_consumption`  
  Load '27_LVBus680341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680307_consumption`  
  Load '27_LVBus680307_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679977_consumption`  
  Load '27_LVBus679977_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679996_consumption`  
  Load '27_LVBus679996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus984520_consumption`  
  Load '27_LVBus984520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679953_consumption`  
  Load '27_LVBus679953_consumption' has phase imbalance of 230.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680079_consumption`  
  Load '27_LVBus680079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680086_consumption`  
  Load '27_LVBus680086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680014_consumption`  
  Load '27_LVBus680014_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679963_consumption`  
  Load '27_LVBus679963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680004_consumption`  
  Load '27_LVBus680004_consumption' has phase imbalance of 120.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679940_consumption`  
  Load '27_LVBus679940_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680041_consumption`  
  Load '27_LVBus680041_consumption' has phase imbalance of 288.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679957_consumption`  
  Load '27_LVBus679957_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679946_consumption`  
  Load '27_LVBus679946_consumption' has phase imbalance of 215.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680384_consumption`  
  Load '27_LVBus680384_consumption' has phase imbalance of 250.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000175_consumption`  
  Load '27_LVBus1000175_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680283_consumption`  
  Load '27_LVBus680283_consumption' has phase imbalance of 277.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680226_consumption`  
  Load '27_LVBus680226_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus978057_consumption`  
  Load '27_LVBus978057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680346_consumption`  
  Load '27_LVBus680346_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680358_consumption`  
  Load '27_LVBus680358_consumption' has phase imbalance of 126.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680141_consumption`  
  Load '27_LVBus680141_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680072_consumption`  
  Load '27_LVBus680072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680347_consumption`  
  Load '27_LVBus680347_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680062_consumption`  
  Load '27_LVBus680062_consumption' has phase imbalance of 68.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus977617_consumption`  
  Load '27_LVBus977617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679931_consumption`  
  Load '27_LVBus679931_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680197_consumption`  
  Load '27_LVBus680197_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680263_consumption`  
  Load '27_LVBus680263_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680338_consumption`  
  Load '27_LVBus680338_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680390_consumption`  
  Load '27_LVBus680390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680174_consumption`  
  Load '27_LVBus680174_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680261_consumption`  
  Load '27_LVBus680261_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680219_consumption`  
  Load '27_LVBus680219_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679983_consumption`  
  Load '27_LVBus679983_consumption' has phase imbalance of 294.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680077_consumption`  
  Load '27_LVBus680077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus979785_consumption`  
  Load '27_LVBus979785_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680186_consumption`  
  Load '27_LVBus680186_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679937_consumption`  
  Load '27_LVBus679937_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1000178_consumption`  
  Load '27_LVBus1000178_consumption' has phase imbalance of 263.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680253_consumption`  
  Load '27_LVBus680253_consumption' has phase imbalance of 131.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680208_consumption`  
  Load '27_LVBus680208_consumption' has phase imbalance of 117.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680113_consumption`  
  Load '27_LVBus680113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus921059_consumption`  
  Load '27_LVBus921059_consumption' has phase imbalance of 284.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680264_consumption`  
  Load '27_LVBus680264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680084_consumption`  
  Load '27_LVBus680084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679951_consumption`  
  Load '27_LVBus679951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus679961_consumption`  
  Load '27_LVBus679961_consumption' has phase imbalance of 116.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680396_consumption`  
  Load '27_LVBus680396_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus948890_consumption`  
  Load '27_LVBus948890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus680242_consumption`  
  Load '27_LVBus680242_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 994 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_LVBus679986' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_LVBus680090' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_LVBus680228' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '27_AVALL' (MV, 11.78 kV) has an electrical reach of 20.75 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '27_LVBus1003427' (LV, 0.24 kV) has an electrical reach of 1.16 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '27_LVBus680123' (LV, 0.24 kV) has an electrical reach of 1.2 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '27_LVBus680224' (LV, 0.24 kV) has an electrical reach of 7.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '27_LVBus1005218' (LV, 0.24 kV) has an electrical reach of 1.53 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '27_LVBus679971' (LV, 0.24 kV) has an electrical reach of 1.1 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '27_LVBus680228' (LV, 0.24 kV) has an electrical reach of 10.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '27_LVBus680268' (LV, 0.24 kV) has an electrical reach of 3.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '27_LVBus680092' (LV, 0.24 kV) has an electrical reach of 26.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  626 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  276 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 27_LVBus1000175_consumption, 27_LVBus1000176_consumption, 27_LVBus1000177_consumption, 27_LVBus1000178_consumption, 27_LVBus1000179_consumption, 27_LVBus1000181_consumption, 27_LVBus1000182_consumption, 27_LVBus1000183_consumption, 27_LVBus1000184_consumption, 27_LVBus1003427_consumption, 27_LVBus1004436_consumption, 27_LVBus1008152_consumption, 27_LVBus679931_consumption, 27_LVBus679935_consumption, 27_LVBus679937_consumption, 27_LVBus679939_consumption, 27_LVBus679940_consumption, 27_LVBus679942_consumption, 27_LVBus679944_consumption, 27_LVBus679951_consumption, 27_LVBus679952_consumption, 27_LVBus679953_consumption, 27_LVBus679954_consumption, 27_LVBus679957_consumption, 27_LVBus679958_consumption, 27_LVBus679959_consumption, 27_LVBus679963_consumption, 27_LVBus679964_consumption, 27_LVBus679965_consumption, 27_LVBus679966_consumption, 27_LVBus679967_consumption, 27_LVBus679976_consumption, 27_LVBus679978_consumption, 27_LVBus679979_consumption, 27_LVBus679983_consumption, 27_LVBus679984_consumption, 27_LVBus679990_consumption, 27_LVBus679992_consumption, 27_LVBus679995_consumption, 27_LVBus679996_consumption, 27_LVBus679998_consumption, 27_LVBus679999_consumption, 27_LVBus680000_consumption, 27_LVBus680001_consumption, 27_LVBus680007_consumption, 27_LVBus680008_consumption, 27_LVBus680015_consumption, 27_LVBus680017_consumption, 27_LVBus680018_consumption, 27_LVBus680019_consumption, 27_LVBus680020_consumption, 27_LVBus680021_consumption, 27_LVBus680033_consumption, 27_LVBus680038_consumption, 27_LVBus680040_consumption, 27_LVBus680041_consumption, 27_LVBus680042_consumption, 27_LVBus680043_consumption, 27_LVBus680044_consumption, 27_LVBus680045_consumption, 27_LVBus680046_consumption, 27_LVBus680047_consumption, 27_LVBus680048_consumption, 27_LVBus680050_consumption, 27_LVBus680051_consumption, 27_LVBus680052_consumption, 27_LVBus680053_consumption, 27_LVBus680055_consumption, 27_LVBus680057_consumption, 27_LVBus680061_consumption, 27_LVBus680063_consumption, 27_LVBus680064_consumption, 27_LVBus680067_consumption, 27_LVBus680068_consumption, 27_LVBus680071_consumption, 27_LVBus680072_consumption, 27_LVBus680075_consumption, 27_LVBus680076_consumption, 27_LVBus680077_consumption, 27_LVBus680079_consumption, 27_LVBus680080_consumption, 27_LVBus680081_consumption, 27_LVBus680083_consumption, 27_LVBus680084_consumption, 27_LVBus680085_consumption, 27_LVBus680086_consumption, 27_LVBus680092_consumption, 27_LVBus680108_consumption, 27_LVBus680110_consumption, 27_LVBus680112_consumption, 27_LVBus680113_consumption, 27_LVBus680114_consumption, 27_LVBus680115_consumption, 27_LVBus680116_consumption, 27_LVBus680121_consumption, 27_LVBus680124_consumption, 27_LVBus680125_consumption, 27_LVBus680126_consumption, 27_LVBus680127_consumption, 27_LVBus680128_consumption, 27_LVBus680131_consumption, 27_LVBus680134_consumption, 27_LVBus680137_consumption, 27_LVBus680138_consumption, 27_LVBus680141_consumption, 27_LVBus680142_consumption, 27_LVBus680144_consumption, 27_LVBus680147_consumption, 27_LVBus680148_consumption, 27_LVBus680149_consumption, 27_LVBus680150_consumption, 27_LVBus680152_consumption, 27_LVBus680159_consumption, 27_LVBus680160_consumption, 27_LVBus680162_consumption, 27_LVBus680163_consumption, 27_LVBus680164_consumption, 27_LVBus680165_consumption, 27_LVBus680166_consumption, 27_LVBus680167_consumption, 27_LVBus680169_consumption, 27_LVBus680170_consumption, 27_LVBus680171_consumption, 27_LVBus680172_consumption, 27_LVBus680173_consumption, 27_LVBus680174_consumption, 27_LVBus680182_consumption, 27_LVBus680183_consumption, 27_LVBus680184_consumption, 27_LVBus680185_consumption, 27_LVBus680186_consumption, 27_LVBus680188_consumption, 27_LVBus680191_consumption, 27_LVBus680193_consumption, 27_LVBus680196_consumption, 27_LVBus680197_consumption, 27_LVBus680199_consumption, 27_LVBus680201_consumption, 27_LVBus680205_consumption, 27_LVBus680206_consumption, 27_LVBus680213_consumption, 27_LVBus680218_consumption, 27_LVBus680219_consumption, 27_LVBus680220_consumption, 27_LVBus680226_consumption, 27_LVBus680234_consumption, 27_LVBus680236_consumption, 27_LVBus680239_consumption, 27_LVBus680240_consumption, 27_LVBus680241_consumption, 27_LVBus680242_consumption, 27_LVBus680243_consumption, 27_LVBus680244_consumption, 27_LVBus680251_consumption, 27_LVBus680252_consumption, 27_LVBus680255_consumption, 27_LVBus680256_consumption, 27_LVBus680257_consumption, 27_LVBus680258_consumption, 27_LVBus680259_consumption, 27_LVBus680260_consumption, 27_LVBus680263_consumption, 27_LVBus680264_consumption, 27_LVBus680266_consumption, 27_LVBus680272_consumption, 27_LVBus680273_consumption, 27_LVBus680275_consumption, 27_LVBus680276_consumption, 27_LVBus680277_consumption, 27_LVBus680281_consumption, 27_LVBus680283_consumption, 27_LVBus680284_consumption, 27_LVBus680285_consumption, 27_LVBus680286_consumption, 27_LVBus680292_consumption, 27_LVBus680293_consumption, 27_LVBus680298_consumption, 27_LVBus680300_consumption, 27_LVBus680302_consumption, 27_LVBus680303_consumption, 27_LVBus680304_consumption, 27_LVBus680307_consumption, 27_LVBus680308_consumption, 27_LVBus680309_consumption, 27_LVBus680310_consumption, 27_LVBus680319_consumption, 27_LVBus680324_consumption, 27_LVBus680325_consumption, 27_LVBus680326_consumption, 27_LVBus680328_consumption, 27_LVBus680333_consumption, 27_LVBus680334_consumption, 27_LVBus680335_consumption, 27_LVBus680336_consumption, 27_LVBus680338_consumption, 27_LVBus680339_consumption, 27_LVBus680340_consumption, 27_LVBus680341_consumption, 27_LVBus680344_consumption, 27_LVBus680345_consumption, 27_LVBus680347_consumption, 27_LVBus680348_consumption, 27_LVBus680353_consumption, 27_LVBus680354_consumption, 27_LVBus680363_consumption, 27_LVBus680367_consumption, 27_LVBus680369_consumption, 27_LVBus680371_consumption, 27_LVBus680372_consumption, 27_LVBus680377_consumption, 27_LVBus680378_consumption, 27_LVBus680379_consumption, 27_LVBus680383_consumption, 27_LVBus680384_consumption, 27_LVBus680385_consumption, 27_LVBus680386_consumption, 27_LVBus680387_consumption, 27_LVBus680390_consumption, 27_LVBus680393_consumption, 27_LVBus680394_consumption, 27_LVBus680396_consumption, 27_LVBus921059_consumption, 27_LVBus921060_consumption, 27_LVBus921647_consumption, 27_LVBus926461_consumption, 27_LVBus926946_consumption, 27_LVBus945353_consumption, 27_LVBus947281_consumption, 27_LVBus947282_consumption, 27_LVBus947283_consumption, 27_LVBus947284_consumption, 27_LVBus947285_consumption, 27_LVBus948150_consumption, 27_LVBus948890_consumption, 27_LVBus950619_consumption, 27_LVBus953638_consumption, 27_LVBus953639_consumption, 27_LVBus953642_consumption, 27_LVBus953643_consumption, 27_LVBus953644_consumption, 27_LVBus953746_consumption, 27_LVBus955020_consumption, 27_LVBus955088_consumption, 27_LVBus955137_consumption, 27_LVBus955743_consumption, 27_LVBus962147_consumption, 27_LVBus962149_consumption, 27_LVBus962152_consumption, 27_LVBus967214_consumption, 27_LVBus968121_consumption, 27_LVBus968877_consumption, 27_LVBus970391_consumption, 27_LVBus974861_consumption, 27_LVBus974862_consumption, 27_LVBus974863_consumption, 27_LVBus974864_consumption, 27_LVBus974866_consumption, 27_LVBus977617_consumption, 27_LVBus977618_consumption, 27_LVBus978057_consumption, 27_LVBus979785_consumption, 27_LVBus979786_consumption, 27_LVBus979787_consumption, 27_LVBus981035_consumption, 27_LVBus981082_consumption, 27_LVBus982190_consumption, 27_LVBus983051_consumption, 27_LVBus984518_consumption, 27_LVBus984519_consumption, 27_LVBus984520_consumption, 27_LVBus984521_consumption, 27_LVBus985271_consumption, 27_LVBus985272_consumption, 27_LVBus986663_consumption, 27_LVBus992269_consumption, 27_LVBus993637_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  497 group(s) of loads (994 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  10 group(s) of series lines (23 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  596 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus1000175_production, 27_LVBus1000176_production, 27_LVBus1000177_production, 27_LVBus1000178_production, 27_LVBus1000179_production, 27_LVBus1000180_consumption, 27_LVBus1000180_production, 27_LVBus1000181_production, 27_LVBus1000182_production, 27_LVBus1000183_production, 27_LVBus1000184_production, 27_LVBus1003427_production, 27_LVBus1004436_production, 27_LVBus1004437_consumption, 27_LVBus1004437_production, 27_LVBus1005218_consumption, 27_LVBus1005218_production, 27_LVBus1008149_production, 27_LVBus1008150_consumption, 27_LVBus1008150_production, 27_LVBus1008151_consumption, 27_LVBus1008151_production, 27_LVBus1008152_production, 27_LVBus679928_production, 27_LVBus679930_consumption, 27_LVBus679930_production, 27_LVBus679931_production, 27_LVBus679932_consumption, 27_LVBus679932_production, 27_LVBus679933_production, 27_LVBus679935_production, 27_LVBus679937_production, 27_LVBus679938_production, 27_LVBus679939_production, 27_LVBus679940_production, 27_LVBus679942_production, 27_LVBus679943_consumption, 27_LVBus679943_production, 27_LVBus679944_production, 27_LVBus679945_production, 27_LVBus679946_production, 27_LVBus679947_production, 27_LVBus679948_production, 27_LVBus679949_consumption, 27_LVBus679949_production, 27_LVBus679950_consumption, 27_LVBus679950_production, 27_LVBus679951_production, 27_LVBus679952_production, 27_LVBus679953_production, 27_LVBus679954_production, 27_LVBus679956_production, 27_LVBus679957_production, 27_LVBus679958_production, 27_LVBus679959_production, 27_LVBus679960_production, 27_LVBus679961_production, 27_LVBus679962_production, 27_LVBus679963_production, 27_LVBus679964_production, 27_LVBus679965_production, 27_LVBus679966_production, 27_LVBus679967_production, 27_LVBus679969_production, 27_LVBus679971_production, 27_LVBus679975_production, 27_LVBus679976_production, 27_LVBus679977_production, 27_LVBus679978_production, 27_LVBus679979_production, 27_LVBus679980_consumption, 27_LVBus679980_production, 27_LVBus679981_production, 27_LVBus679982_production, 27_LVBus679983_production, 27_LVBus679984_production, 27_LVBus679986_consumption, 27_LVBus679986_production, 27_LVBus679987_consumption, 27_LVBus679987_production, 27_LVBus679988_production, 27_LVBus679990_production, 27_LVBus679992_production, 27_LVBus679994_production, 27_LVBus679995_production, 27_LVBus679996_production, 27_LVBus679997_consumption, 27_LVBus679997_production, 27_LVBus679998_production, 27_LVBus679999_production, 27_LVBus680000_production, 27_LVBus680001_production, 27_LVBus680003_production, 27_LVBus680004_production, 27_LVBus680006_production, 27_LVBus680007_production, 27_LVBus680008_production, 27_LVBus680009_consumption, 27_LVBus680009_production, 27_LVBus680011_consumption, 27_LVBus680011_production, 27_LVBus680012_production, 27_LVBus680014_production, 27_LVBus680015_production, 27_LVBus680017_production, 27_LVBus680018_production, 27_LVBus680019_production, 27_LVBus680020_production, 27_LVBus680021_production, 27_LVBus680025_consumption, 27_LVBus680025_production, 27_LVBus680027_production, 27_LVBus680029_production, 27_LVBus680031_production, 27_LVBus680032_production, 27_LVBus680033_production, 27_LVBus680034_production, 27_LVBus680035_consumption, 27_LVBus680035_production, 27_LVBus680036_consumption, 27_LVBus680036_production, 27_LVBus680038_production, 27_LVBus680039_consumption, 27_LVBus680039_production, 27_LVBus680040_production, 27_LVBus680041_production, 27_LVBus680042_production, 27_LVBus680043_production, 27_LVBus680044_production, 27_LVBus680045_production, 27_LVBus680046_production, 27_LVBus680047_production, 27_LVBus680048_production, 27_LVBus680049_production, 27_LVBus680050_production, 27_LVBus680051_production, 27_LVBus680052_production, 27_LVBus680053_production, 27_LVBus680054_consumption, 27_LVBus680054_production, 27_LVBus680055_production, 27_LVBus680056_production, 27_LVBus680057_production, 27_LVBus680059_consumption, 27_LVBus680059_production, 27_LVBus680060_consumption, 27_LVBus680060_production, 27_LVBus680061_production, 27_LVBus680062_production, 27_LVBus680063_production, 27_LVBus680064_production, 27_LVBus680065_production, 27_LVBus680066_production, 27_LVBus680067_production, 27_LVBus680068_production, 27_LVBus680070_consumption, 27_LVBus680070_production, 27_LVBus680071_production, 27_LVBus680072_production, 27_LVBus680073_production, 27_LVBus680074_production, 27_LVBus680075_production, 27_LVBus680076_production, 27_LVBus680077_production, 27_LVBus680078_production, 27_LVBus680079_production, 27_LVBus680080_production, 27_LVBus680081_production, 27_LVBus680082_production, 27_LVBus680083_production, 27_LVBus680084_production, 27_LVBus680085_production, 27_LVBus680086_production, 27_LVBus680090_production, 27_LVBus680092_production, 27_LVBus680094_production, 27_LVBus680098_consumption, 27_LVBus680098_production, 27_LVBus680100_consumption, 27_LVBus680100_production, 27_LVBus680102_production, 27_LVBus680104_production, 27_LVBus680105_consumption, 27_LVBus680105_production, 27_LVBus680106_production, 27_LVBus680108_production, 27_LVBus680110_production, 27_LVBus680111_consumption, 27_LVBus680111_production, 27_LVBus680112_production, 27_LVBus680113_production, 27_LVBus680114_production, 27_LVBus680115_production, 27_LVBus680116_production, 27_LVBus680117_consumption, 27_LVBus680117_production, 27_LVBus680118_production, 27_LVBus680119_production, 27_LVBus680121_production, 27_LVBus680123_production, 27_LVBus680124_production, 27_LVBus680125_production, 27_LVBus680126_production, 27_LVBus680127_production, 27_LVBus680128_production, 27_LVBus680129_consumption, 27_LVBus680129_production, 27_LVBus680130_consumption, 27_LVBus680130_production, 27_LVBus680131_production, 27_LVBus680132_consumption, 27_LVBus680132_production, 27_LVBus680133_consumption, 27_LVBus680133_production, 27_LVBus680134_production, 27_LVBus680135_production, 27_LVBus680136_production, 27_LVBus680137_production, 27_LVBus680138_production, 27_LVBus680139_consumption, 27_LVBus680139_production, 27_LVBus680140_consumption, 27_LVBus680140_production, 27_LVBus680141_production, 27_LVBus680142_production, 27_LVBus680144_production, 27_LVBus680145_production, 27_LVBus680146_consumption, 27_LVBus680146_production, 27_LVBus680147_production, 27_LVBus680148_production, 27_LVBus680149_production, 27_LVBus680150_production, 27_LVBus680151_consumption, 27_LVBus680151_production, 27_LVBus680152_production, 27_LVBus680154_consumption, 27_LVBus680154_production, 27_LVBus680158_production, 27_LVBus680159_production, 27_LVBus680160_production, 27_LVBus680161_consumption, 27_LVBus680161_production, 27_LVBus680162_production, 27_LVBus680163_production, 27_LVBus680164_production, 27_LVBus680165_production, 27_LVBus680166_production, 27_LVBus680167_production, 27_LVBus680168_production, 27_LVBus680169_production, 27_LVBus680170_production, 27_LVBus680171_production, 27_LVBus680172_production, 27_LVBus680173_production, 27_LVBus680174_production, 27_LVBus680176_production, 27_LVBus680177_production, 27_LVBus680178_production, 27_LVBus680179_production, 27_LVBus680180_production, 27_LVBus680182_production, 27_LVBus680183_production, 27_LVBus680184_production, 27_LVBus680185_production, 27_LVBus680186_production, 27_LVBus680188_production, 27_LVBus680189_consumption, 27_LVBus680189_production, 27_LVBus680190_consumption, 27_LVBus680190_production, 27_LVBus680191_production, 27_LVBus680193_production, 27_LVBus680194_consumption, 27_LVBus680194_production, 27_LVBus680196_production, 27_LVBus680197_production, 27_LVBus680199_production, 27_LVBus680200_production, 27_LVBus680201_production, 27_LVBus680202_production, 27_LVBus680203_production, 27_LVBus680204_production, 27_LVBus680205_production, 27_LVBus680206_production, 27_LVBus680208_production, 27_LVBus680209_production, 27_LVBus680210_production, 27_LVBus680211_production, 27_LVBus680212_production, 27_LVBus680213_production, 27_LVBus680214_production, 27_LVBus680215_production, 27_LVBus680217_consumption, 27_LVBus680217_production, 27_LVBus680218_production, 27_LVBus680219_production, 27_LVBus680220_production, 27_LVBus680222_production, 27_LVBus680224_consumption, 27_LVBus680224_production, 27_LVBus680226_production, 27_LVBus680228_production, 27_LVBus680230_consumption, 27_LVBus680230_production, 27_LVBus680231_consumption, 27_LVBus680231_production, 27_LVBus680232_consumption, 27_LVBus680232_production, 27_LVBus680233_consumption, 27_LVBus680233_production, 27_LVBus680234_production, 27_LVBus680236_production, 27_LVBus680237_production, 27_LVBus680238_production, 27_LVBus680239_production, 27_LVBus680240_production, 27_LVBus680241_production, 27_LVBus680242_production, 27_LVBus680243_production, 27_LVBus680244_production, 27_LVBus680246_production, 27_LVBus680248_consumption, 27_LVBus680248_production, 27_LVBus680249_consumption, 27_LVBus680249_production, 27_LVBus680250_consumption, 27_LVBus680250_production, 27_LVBus680251_production, 27_LVBus680252_production, 27_LVBus680253_production, 27_LVBus680254_production, 27_LVBus680255_production, 27_LVBus680256_production, 27_LVBus680257_production, 27_LVBus680258_production, 27_LVBus680259_production, 27_LVBus680260_production, 27_LVBus680261_production, 27_LVBus680263_production, 27_LVBus680264_production, 27_LVBus680265_production, 27_LVBus680266_production, 27_LVBus680268_production, 27_LVBus680270_production, 27_LVBus680271_consumption, 27_LVBus680271_production, 27_LVBus680272_production, 27_LVBus680273_production, 27_LVBus680275_production, 27_LVBus680276_production, 27_LVBus680277_production, 27_LVBus680278_production, 27_LVBus680279_production, 27_LVBus680280_production, 27_LVBus680281_production, 27_LVBus680283_production, 27_LVBus680284_production, 27_LVBus680285_production, 27_LVBus680286_production, 27_LVBus680288_consumption, 27_LVBus680288_production, 27_LVBus680289_production, 27_LVBus680290_production, 27_LVBus680291_production, 27_LVBus680292_production, 27_LVBus680293_production, 27_LVBus680294_production, 27_LVBus680295_production, 27_LVBus680296_production, 27_LVBus680298_production, 27_LVBus680299_production, 27_LVBus680300_production, 27_LVBus680302_production, 27_LVBus680303_production, 27_LVBus680304_production, 27_LVBus680306_production, 27_LVBus680307_production, 27_LVBus680308_production, 27_LVBus680309_production, 27_LVBus680310_production, 27_LVBus680312_consumption, 27_LVBus680312_production, 27_LVBus680313_production, 27_LVBus680314_production, 27_LVBus680316_consumption, 27_LVBus680316_production, 27_LVBus680318_consumption, 27_LVBus680318_production, 27_LVBus680319_production, 27_LVBus680320_production, 27_LVBus680322_consumption, 27_LVBus680322_production, 27_LVBus680324_production, 27_LVBus680325_production, 27_LVBus680326_production, 27_LVBus680327_consumption, 27_LVBus680327_production, 27_LVBus680328_production, 27_LVBus680329_production, 27_LVBus680330_consumption, 27_LVBus680330_production, 27_LVBus680331_consumption, 27_LVBus680331_production, 27_LVBus680332_production, 27_LVBus680333_production, 27_LVBus680334_production, 27_LVBus680335_production, 27_LVBus680336_production, 27_LVBus680337_consumption, 27_LVBus680337_production, 27_LVBus680338_production, 27_LVBus680339_production, 27_LVBus680340_production, 27_LVBus680341_production, 27_LVBus680342_production, 27_LVBus680344_production, 27_LVBus680345_production, 27_LVBus680346_production, 27_LVBus680347_production, 27_LVBus680348_production, 27_LVBus680349_consumption, 27_LVBus680349_production, 27_LVBus680351_production, 27_LVBus680352_production, 27_LVBus680353_production, 27_LVBus680354_production, 27_LVBus680355_consumption, 27_LVBus680355_production, 27_LVBus680357_production, 27_LVBus680358_production, 27_LVBus680361_consumption, 27_LVBus680361_production, 27_LVBus680362_production, 27_LVBus680363_production, 27_LVBus680364_production, 27_LVBus680365_consumption, 27_LVBus680365_production, 27_LVBus680367_production, 27_LVBus680368_consumption, 27_LVBus680368_production, 27_LVBus680369_production, 27_LVBus680370_consumption, 27_LVBus680370_production, 27_LVBus680371_production, 27_LVBus680372_production, 27_LVBus680373_consumption, 27_LVBus680373_production, 27_LVBus680375_production, 27_LVBus680376_production, 27_LVBus680377_production, 27_LVBus680378_production, 27_LVBus680379_production, 27_LVBus680381_consumption, 27_LVBus680381_production, 27_LVBus680382_consumption, 27_LVBus680382_production, 27_LVBus680383_production, 27_LVBus680384_production, 27_LVBus680385_production, 27_LVBus680386_production, 27_LVBus680387_production, 27_LVBus680388_production, 27_LVBus680389_production, 27_LVBus680390_production, 27_LVBus680392_consumption, 27_LVBus680392_production, 27_LVBus680393_production, 27_LVBus680394_production, 27_LVBus680395_consumption, 27_LVBus680395_production, 27_LVBus680396_production, 27_LVBus921057_consumption, 27_LVBus921057_production, 27_LVBus921058_consumption, 27_LVBus921058_production, 27_LVBus921059_production, 27_LVBus921060_production, 27_LVBus921646_production, 27_LVBus921647_production, 27_LVBus921648_production, 27_LVBus924725_consumption, 27_LVBus924725_production, 27_LVBus924726_consumption, 27_LVBus924726_production, 27_LVBus924727_consumption, 27_LVBus924727_production, 27_LVBus924728_consumption, 27_LVBus924728_production, 27_LVBus924751_production, 27_LVBus926461_production, 27_LVBus926944_consumption, 27_LVBus926944_production, 27_LVBus926945_consumption, 27_LVBus926945_production, 27_LVBus926946_production, 27_LVBus936342_production, 27_LVBus940932_consumption, 27_LVBus940932_production, 27_LVBus945353_production, 27_LVBus946456_production, 27_LVBus947280_consumption, 27_LVBus947280_production, 27_LVBus947281_production, 27_LVBus947282_production, 27_LVBus947283_production, 27_LVBus947284_production, 27_LVBus947285_production, 27_LVBus948150_production, 27_LVBus948888_production, 27_LVBus948889_production, 27_LVBus948890_production, 27_LVBus950619_production, 27_LVBus953637_consumption, 27_LVBus953637_production, 27_LVBus953638_production, 27_LVBus953639_production, 27_LVBus953640_consumption, 27_LVBus953640_production, 27_LVBus953641_production, 27_LVBus953642_production, 27_LVBus953643_production, 27_LVBus953644_production, 27_LVBus953746_production, 27_LVBus955018_consumption, 27_LVBus955018_production, 27_LVBus955019_consumption, 27_LVBus955019_production, 27_LVBus955020_production, 27_LVBus955088_production, 27_LVBus955137_production, 27_LVBus955138_production, 27_LVBus955743_production, 27_LVBus962147_production, 27_LVBus962148_production, 27_LVBus962149_production, 27_LVBus962150_production, 27_LVBus962151_production, 27_LVBus962152_production, 27_LVBus962153_production, 27_LVBus967214_production, 27_LVBus968120_consumption, 27_LVBus968120_production, 27_LVBus968121_production, 27_LVBus968877_production, 27_LVBus970391_production, 27_LVBus970392_consumption, 27_LVBus970392_production, 27_LVBus973644_consumption, 27_LVBus973644_production, 27_LVBus974861_production, 27_LVBus974862_production, 27_LVBus974863_production, 27_LVBus974864_production, 27_LVBus974865_consumption, 27_LVBus974865_production, 27_LVBus974866_production, 27_LVBus974867_production, 27_LVBus977617_production, 27_LVBus977618_production, 27_LVBus978057_production, 27_LVBus979785_production, 27_LVBus979786_production, 27_LVBus979787_production, 27_LVBus979788_consumption, 27_LVBus979788_production, 27_LVBus981035_production, 27_LVBus981082_production, 27_LVBus982190_production, 27_LVBus983051_production, 27_LVBus984517_production, 27_LVBus984518_production, 27_LVBus984519_production, 27_LVBus984520_production, 27_LVBus984521_production, 27_LVBus985271_production, 27_LVBus985272_production, 27_LVBus986663_production, 27_LVBus986664_consumption, 27_LVBus986664_production, 27_LVBus992269_production, 27_LVBus992270_consumption, 27_LVBus992270_production, 27_LVBus993637_production, 27_LVBus999058_consumption, 27_LVBus999058_production, 27_MVLV03103_consumption, 27_MVLV03103_production, 27_MVLV07531_consumption, 27_MVLV07531_production, 27_MVLV38575_consumption, 27_MVLV38575_production, 27_MVLV66368_consumption, 27_MVLV66368_production, 27_MVLV67000_consumption, 27_MVLV67000_production.

