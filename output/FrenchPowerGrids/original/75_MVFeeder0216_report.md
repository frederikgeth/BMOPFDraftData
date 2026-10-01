# BMOPF Network Summary: 75_MVFeeder0216

**Generated:** 2026-10-01 23:34:22  
**Findings:** 0 errors · 5 warnings · 182 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 22 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 501 |  |
| line | 478 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 898 | 7.664 MW, 2.3 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 22 |  |
| switch | 0 |  |
| transformer | 22 | Dyn11×22 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 44 | 43 | 28 | 0 |
| LV_236V | 236.0 V | 457 | 435 | 870 | 0 |

**Transformer transitions:**

- `75_MVLV107230_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV077408_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127491_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV026972_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV107765_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV131131_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV096955_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV089747_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV025127_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV094100_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV008217_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV171719_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV040219_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV022828_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV134802_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV026927_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV023961_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV025978_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV158895_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV040706_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV125096_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV115657_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 201 |
| Tree depth (max hops) | 38 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 501 | 1 | 500 | 0 | 0 | 0 |
| Tier LV_236V | 457 | 22 | 435 | 0 | 0 | 0 |
| Tier MV_11.8kV | 44 | 1 | 43 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 22; skipped invalid branches: 0.

Galvanic zones: 23; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_AUREN | MV_11.8kV | 44 | 0 | 0 | 22 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1960 declared bus terminals; 1869 mapped line/closed-switch conductor edges; 91 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 1.04e6 | 12.478 | 2694 |
| q_nom | 0.0 | 313000.0 | 12.478 | 2694 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.31 | 785.0 | 1.459 | 478 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 1.1e6 | 0.388 | 22 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 675 of 898 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478015_consumption' has phase imbalance of 29.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478055_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477896_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477858_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478026_consumption' has phase imbalance of 44.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477844_consumption' has phase imbalance of 54.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477934_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478022_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477925_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478081_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477906_consumption' has phase imbalance of 94.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478084_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477833_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477760_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478076_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478216_consumption' has phase imbalance of 243.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477911_consumption' has phase imbalance of 24.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478141_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477813_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478064_consumption' has phase imbalance of 182.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478241_consumption' has phase imbalance of 29.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478088_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478046_consumption' has phase imbalance of 67.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478214_consumption' has phase imbalance of 79.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478157_consumption' has phase imbalance of 213.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478128_consumption' has phase imbalance of 81.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478280_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477762_consumption' has phase imbalance of 52.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477946_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478151_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477928_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478139_consumption' has phase imbalance of 50.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477937_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478080_consumption' has phase imbalance of 76.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478102_consumption' has phase imbalance of 109.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477826_consumption' has phase imbalance of 67.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478105_consumption' has phase imbalance of 201.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477986_consumption' has phase imbalance of 85.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478148_consumption' has phase imbalance of 112.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478155_consumption' has phase imbalance of 85.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478077_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478126_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478174_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477900_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478110_consumption' has phase imbalance of 132.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477800_consumption' has phase imbalance of 75.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477855_consumption' has phase imbalance of 34.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477915_consumption' has phase imbalance of 20.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477940_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478202_consumption' has phase imbalance of 111.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478059_consumption' has phase imbalance of 133.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478163_consumption' has phase imbalance of 118.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477955_consumption' has phase imbalance of 22.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478112_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477923_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477865_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478254_consumption' has phase imbalance of 45.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478215_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477979_consumption' has phase imbalance of 93.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477921_consumption' has phase imbalance of 94.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478034_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477883_consumption' has phase imbalance of 80.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478211_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477851_consumption' has phase imbalance of 44.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478086_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478000_consumption' has phase imbalance of 127.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478108_consumption' has phase imbalance of 119.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477984_consumption' has phase imbalance of 167.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478222_consumption' has phase imbalance of 24.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478093_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478270_consumption' has phase imbalance of 41.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477752_consumption' has phase imbalance of 112.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478067_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478220_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477885_consumption' has phase imbalance of 33.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478089_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477995_consumption' has phase imbalance of 20.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477876_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477757_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477838_consumption' has phase imbalance of 51.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478134_consumption' has phase imbalance of 25.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478017_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477790_consumption' has phase imbalance of 40.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478146_consumption' has phase imbalance of 196.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477932_consumption' has phase imbalance of 58.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478161_consumption' has phase imbalance of 103.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477927_consumption' has phase imbalance of 88.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477893_consumption' has phase imbalance of 90.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477798_consumption' has phase imbalance of 58.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478060_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478181_consumption' has phase imbalance of 73.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477987_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478101_consumption' has phase imbalance of 42.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477992_consumption' has phase imbalance of 35.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478165_consumption' has phase imbalance of 55.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478099_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478098_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477890_consumption' has phase imbalance of 27.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478065_consumption' has phase imbalance of 101.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477931_consumption' has phase imbalance of 221.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478058_consumption' has phase imbalance of 82.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477815_consumption' has phase imbalance of 132.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478117_consumption' has phase imbalance of 132.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477880_consumption' has phase imbalance of 128.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477870_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477897_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478179_consumption' has phase imbalance of 27.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478278_consumption' has phase imbalance of 229.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478037_consumption' has phase imbalance of 49.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478057_consumption' has phase imbalance of 121.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478090_consumption' has phase imbalance of 71.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478013_consumption' has phase imbalance of 23.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477755_consumption' has phase imbalance of 203.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478056_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478061_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477922_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477919_consumption' has phase imbalance of 32.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477861_consumption' has phase imbalance of 143.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478169_consumption' has phase imbalance of 73.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478246_consumption' has phase imbalance of 32.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478004_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477845_consumption' has phase imbalance of 77.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478213_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478107_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478217_consumption' has phase imbalance of 217.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477793_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477840_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477997_consumption' has phase imbalance of 137.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477818_consumption' has phase imbalance of 155.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478087_consumption' has phase imbalance of 59.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478078_consumption' has phase imbalance of 47.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477924_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478005_consumption' has phase imbalance of 120.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477926_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477945_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478100_consumption' has phase imbalance of 261.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477827_consumption' has phase imbalance of 39.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0478120_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477828_consumption' has phase imbalance of 259.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477809_consumption' has phase imbalance of 112.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0477859_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 898 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0478224' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_AUREN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0477742' has balanced aggregate load across 3 phase(s) (max spread 0.78%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0478049' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0478257' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 7.664 MW |
| Total load Q | 2.3 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV107230_Transformer | 693.0 kVA | 33.6% |
| 75_MVLV077408_Transformer | 440.0 kVA | 35.1% |
| 75_MVLV127491_Transformer | 1.1 MVA | 19.4% |
| 75_MVLV026972_Transformer | 693.0 kVA | 46.9% |
| 75_MVLV107765_Transformer | 693.0 kVA | 38.7% |
| 75_MVLV131131_Transformer | 693.0 kVA | 12.5% |
| 75_MVLV096955_Transformer | 176.0 kVA | 0.8% |
| 75_MVLV089747_Transformer | 693.0 kVA | 26.8% |
| 75_MVLV025127_Transformer | 1.1 MVA | 42.2% |
| 75_MVLV094100_Transformer | 1.1 MVA | 38.0% |
| 75_MVLV008217_Transformer | 693.0 kVA | 17.2% |
| 75_MVLV171719_Transformer | 1.1 MVA | 15.9% |
| 75_MVLV040219_Transformer | 693.0 kVA | 19.8% |
| 75_MVLV022828_Transformer | 440.0 kVA | 29.1% |
| 75_MVLV134802_Transformer | 693.0 kVA | 14.1% |
| 75_MVLV026927_Transformer | 440.0 kVA | 25.4% |
| 75_MVLV023961_Transformer | 275.0 kVA | 17.3% |
| 75_MVLV025978_Transformer | 440.0 kVA | 9.2% |
| 75_MVLV158895_Transformer | 693.0 kVA | 32.2% |
| 75_MVLV040706_Transformer | 440.0 kVA | 13.1% |
| 75_MVLV125096_Transformer | 693.0 kVA | 22.0% |
| 75_MVLV115657_Transformer | 693.0 kVA | 16.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (7.66 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 501 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 501 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 22 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 44 |
| LV_236V | 4-wire | 457 / 457 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 457 |
| Neutral branches | 435 |
| Grounding points | 22 |
| Neutral sections | 22 |
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
| 11.78 kV | 44 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 49 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 58 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 23 |
| Islands without voltage reference | 0 |
| Line impedance spread | 557.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 457 / 44 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 676 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 676 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0477742_production, 75_LVBus0477744_consumption, 75_LVBus0477744_production, 75_LVBus0477746_production, 75_LVBus0477748_production, 75_LVBus0477750_consumption, 75_LVBus0477750_production, 75_LVBus0477752_production, 75_LVBus0477754_consumption, 75_LVBus0477754_production, 75_LVBus0477755_production, 75_LVBus0477757_production, 75_LVBus0477758_production, 75_LVBus0477759_consumption, 75_LVBus0477759_production, 75_LVBus0477760_production, 75_LVBus0477761_production, 75_LVBus0477762_production, 75_LVBus0477764_consumption, 75_LVBus0477764_production, 75_LVBus0477765_consumption, 75_LVBus0477765_production, 75_LVBus0477766_consumption, 75_LVBus0477766_production, 75_LVBus0477767_consumption, 75_LVBus0477767_production, 75_LVBus0477768_consumption, 75_LVBus0477768_production, 75_LVBus0477769_consumption, 75_LVBus0477769_production, 75_LVBus0477770_consumption, 75_LVBus0477770_production, 75_LVBus0477771_consumption, 75_LVBus0477771_production, 75_LVBus0477773_consumption, 75_LVBus0477773_production, 75_LVBus0477774_consumption, 75_LVBus0477774_production, 75_LVBus0477775_consumption, 75_LVBus0477775_production, 75_LVBus0477776_consumption, 75_LVBus0477776_production, 75_LVBus0477777_consumption, 75_LVBus0477777_production, 75_LVBus0477778_consumption, 75_LVBus0477778_production, 75_LVBus0477779_consumption, 75_LVBus0477779_production, 75_LVBus0477781_consumption, 75_LVBus0477781_production, 75_LVBus0477782_consumption, 75_LVBus0477782_production, 75_LVBus0477783_consumption, 75_LVBus0477783_production, 75_LVBus0477784_consumption, 75_LVBus0477784_production, 75_LVBus0477785_production, 75_LVBus0477786_consumption, 75_LVBus0477786_production, 75_LVBus0477787_consumption, 75_LVBus0477787_production, 75_LVBus0477788_production, 75_LVBus0477789_consumption, 75_LVBus0477789_production, 75_LVBus0477790_production, 75_LVBus0477792_consumption, 75_LVBus0477792_production, 75_LVBus0477793_production, 75_LVBus0477794_consumption, 75_LVBus0477794_production, 75_LVBus0477795_consumption, 75_LVBus0477795_production, 75_LVBus0477797_consumption, 75_LVBus0477797_production, 75_LVBus0477798_production, 75_LVBus0477799_consumption, 75_LVBus0477799_production, 75_LVBus0477800_production, 75_LVBus0477801_consumption, 75_LVBus0477801_production, 75_LVBus0477802_consumption, 75_LVBus0477802_production, 75_LVBus0477803_production, 75_LVBus0477804_production, 75_LVBus0477805_consumption, 75_LVBus0477805_production, 75_LVBus0477807_consumption, 75_LVBus0477807_production, 75_LVBus0477808_consumption, 75_LVBus0477808_production, 75_LVBus0477809_production, 75_LVBus0477810_consumption, 75_LVBus0477810_production, 75_LVBus0477811_consumption, 75_LVBus0477811_production, 75_LVBus0477812_consumption, 75_LVBus0477812_production, 75_LVBus0477813_production, 75_LVBus0477814_consumption, 75_LVBus0477814_production, 75_LVBus0477815_production, 75_LVBus0477817_consumption, 75_LVBus0477817_production, 75_LVBus0477818_production, 75_LVBus0477820_consumption, 75_LVBus0477820_production, 75_LVBus0477821_consumption, 75_LVBus0477821_production, 75_LVBus0477822_consumption, 75_LVBus0477822_production, 75_LVBus0477823_consumption, 75_LVBus0477823_production, 75_LVBus0477825_production, 75_LVBus0477826_production, 75_LVBus0477827_production, 75_LVBus0477828_production, 75_LVBus0477829_consumption, 75_LVBus0477829_production, 75_LVBus0477830_production, 75_LVBus0477831_production, 75_LVBus0477833_production, 75_LVBus0477834_consumption, 75_LVBus0477834_production, 75_LVBus0477835_consumption, 75_LVBus0477835_production, 75_LVBus0477836_consumption, 75_LVBus0477836_production, 75_LVBus0477837_consumption, 75_LVBus0477837_production, 75_LVBus0477838_production, 75_LVBus0477839_production, 75_LVBus0477840_production, 75_LVBus0477841_consumption, 75_LVBus0477841_production, 75_LVBus0477842_consumption, 75_LVBus0477842_production, 75_LVBus0477843_consumption, 75_LVBus0477843_production, 75_LVBus0477844_production, 75_LVBus0477845_production, 75_LVBus0477849_consumption, 75_LVBus0477849_production, 75_LVBus0477851_production, 75_LVBus0477853_consumption, 75_LVBus0477853_production, 75_LVBus0477855_production, 75_LVBus0477857_consumption, 75_LVBus0477857_production, 75_LVBus0477858_production, 75_LVBus0477859_production, 75_LVBus0477861_production, 75_LVBus0477862_consumption, 75_LVBus0477862_production, 75_LVBus0477863_consumption, 75_LVBus0477863_production, 75_LVBus0477864_consumption, 75_LVBus0477864_production, 75_LVBus0477865_production, 75_LVBus0477866_consumption, 75_LVBus0477866_production, 75_LVBus0477867_consumption, 75_LVBus0477867_production, 75_LVBus0477868_consumption, 75_LVBus0477868_production, 75_LVBus0477869_consumption, 75_LVBus0477869_production, 75_LVBus0477870_production, 75_LVBus0477871_consumption, 75_LVBus0477871_production, 75_LVBus0477872_production, 75_LVBus0477873_consumption, 75_LVBus0477873_production, 75_LVBus0477874_production, 75_LVBus0477875_production, 75_LVBus0477876_production, 75_LVBus0477877_production, 75_LVBus0477878_consumption, 75_LVBus0477878_production, 75_LVBus0477880_production, 75_LVBus0477881_consumption, 75_LVBus0477881_production, 75_LVBus0477882_consumption, 75_LVBus0477882_production, 75_LVBus0477883_production, 75_LVBus0477884_production, 75_LVBus0477885_production, 75_LVBus0477887_consumption, 75_LVBus0477887_production, 75_LVBus0477888_consumption, 75_LVBus0477888_production, 75_LVBus0477890_production, 75_LVBus0477892_consumption, 75_LVBus0477892_production, 75_LVBus0477893_production, 75_LVBus0477895_consumption, 75_LVBus0477895_production, 75_LVBus0477896_production, 75_LVBus0477897_production, 75_LVBus0477898_consumption, 75_LVBus0477898_production, 75_LVBus0477899_consumption, 75_LVBus0477899_production, 75_LVBus0477900_production, 75_LVBus0477902_consumption, 75_LVBus0477902_production, 75_LVBus0477903_consumption, 75_LVBus0477903_production, 75_LVBus0477905_consumption, 75_LVBus0477905_production, 75_LVBus0477906_production, 75_LVBus0477908_consumption, 75_LVBus0477908_production, 75_LVBus0477910_consumption, 75_LVBus0477910_production, 75_LVBus0477911_production, 75_LVBus0477913_consumption, 75_LVBus0477913_production, 75_LVBus0477914_production, 75_LVBus0477915_production, 75_LVBus0477916_consumption, 75_LVBus0477916_production, 75_LVBus0477918_consumption, 75_LVBus0477918_production, 75_LVBus0477919_production, 75_LVBus0477920_production, 75_LVBus0477921_production, 75_LVBus0477922_production, 75_LVBus0477923_production, 75_LVBus0477924_production, 75_LVBus0477925_production, 75_LVBus0477926_production, 75_LVBus0477927_production, 75_LVBus0477928_production, 75_LVBus0477929_production, 75_LVBus0477931_production, 75_LVBus0477932_production, 75_LVBus0477934_production, 75_LVBus0477935_production, 75_LVBus0477936_production, 75_LVBus0477937_production, 75_LVBus0477938_consumption, 75_LVBus0477938_production, 75_LVBus0477940_production, 75_LVBus0477942_consumption, 75_LVBus0477942_production, 75_LVBus0477943_consumption, 75_LVBus0477943_production, 75_LVBus0477944_consumption, 75_LVBus0477944_production, 75_LVBus0477945_production, 75_LVBus0477946_production, 75_LVBus0477948_production, 75_LVBus0477949_consumption, 75_LVBus0477949_production, 75_LVBus0477951_production, 75_LVBus0477952_consumption, 75_LVBus0477952_production, 75_LVBus0477953_consumption, 75_LVBus0477953_production, 75_LVBus0477954_consumption, 75_LVBus0477954_production, 75_LVBus0477955_production, 75_LVBus0477956_consumption, 75_LVBus0477956_production, 75_LVBus0477957_consumption, 75_LVBus0477957_production, 75_LVBus0477958_consumption, 75_LVBus0477958_production, 75_LVBus0477959_consumption, 75_LVBus0477959_production, 75_LVBus0477960_consumption, 75_LVBus0477960_production, 75_LVBus0477961_consumption, 75_LVBus0477961_production, 75_LVBus0477963_consumption, 75_LVBus0477963_production, 75_LVBus0477964_consumption, 75_LVBus0477964_production, 75_LVBus0477965_consumption, 75_LVBus0477965_production, 75_LVBus0477966_consumption, 75_LVBus0477966_production, 75_LVBus0477967_consumption, 75_LVBus0477967_production, 75_LVBus0477968_consumption, 75_LVBus0477968_production, 75_LVBus0477969_consumption, 75_LVBus0477969_production, 75_LVBus0477970_consumption, 75_LVBus0477970_production, 75_LVBus0477971_consumption, 75_LVBus0477971_production, 75_LVBus0477972_consumption, 75_LVBus0477972_production, 75_LVBus0477973_consumption, 75_LVBus0477973_production, 75_LVBus0477974_consumption, 75_LVBus0477974_production, 75_LVBus0477976_consumption, 75_LVBus0477976_production, 75_LVBus0477977_consumption, 75_LVBus0477977_production, 75_LVBus0477978_consumption, 75_LVBus0477978_production, 75_LVBus0477979_production, 75_LVBus0477980_consumption, 75_LVBus0477980_production, 75_LVBus0477981_consumption, 75_LVBus0477981_production, 75_LVBus0477983_consumption, 75_LVBus0477983_production, 75_LVBus0477984_production, 75_LVBus0477985_consumption, 75_LVBus0477985_production, 75_LVBus0477986_production, 75_LVBus0477987_production, 75_LVBus0477988_production, 75_LVBus0477990_production, 75_LVBus0477992_production, 75_LVBus0477993_production, 75_LVBus0477994_consumption, 75_LVBus0477994_production, 75_LVBus0477995_production, 75_LVBus0477997_production, 75_LVBus0477999_production, 75_LVBus0478000_production, 75_LVBus0478001_consumption, 75_LVBus0478001_production, 75_LVBus0478003_production, 75_LVBus0478004_production, 75_LVBus0478005_production, 75_LVBus0478007_consumption, 75_LVBus0478007_production, 75_LVBus0478008_production, 75_LVBus0478010_consumption, 75_LVBus0478010_production, 75_LVBus0478011_consumption, 75_LVBus0478011_production, 75_LVBus0478012_production, 75_LVBus0478013_production, 75_LVBus0478014_consumption, 75_LVBus0478014_production, 75_LVBus0478015_production, 75_LVBus0478017_production, 75_LVBus0478018_consumption, 75_LVBus0478018_production, 75_LVBus0478019_consumption, 75_LVBus0478019_production, 75_LVBus0478020_production, 75_LVBus0478021_production, 75_LVBus0478022_production, 75_LVBus0478023_consumption, 75_LVBus0478023_production, 75_LVBus0478024_consumption, 75_LVBus0478024_production, 75_LVBus0478025_consumption, 75_LVBus0478025_production, 75_LVBus0478026_production, 75_LVBus0478028_consumption, 75_LVBus0478028_production, 75_LVBus0478029_consumption, 75_LVBus0478029_production, 75_LVBus0478030_consumption, 75_LVBus0478030_production, 75_LVBus0478031_consumption, 75_LVBus0478031_production, 75_LVBus0478032_consumption, 75_LVBus0478032_production, 75_LVBus0478033_production, 75_LVBus0478034_production, 75_LVBus0478035_consumption, 75_LVBus0478035_production, 75_LVBus0478036_consumption, 75_LVBus0478036_production, 75_LVBus0478037_production, 75_LVBus0478038_consumption, 75_LVBus0478038_production, 75_LVBus0478039_consumption, 75_LVBus0478039_production, 75_LVBus0478040_consumption, 75_LVBus0478040_production, 75_LVBus0478041_consumption, 75_LVBus0478041_production, 75_LVBus0478042_consumption, 75_LVBus0478042_production, 75_LVBus0478043_consumption, 75_LVBus0478043_production, 75_LVBus0478044_consumption, 75_LVBus0478044_production, 75_LVBus0478046_production, 75_LVBus0478049_consumption, 75_LVBus0478049_production, 75_LVBus0478051_production, 75_LVBus0478053_consumption, 75_LVBus0478053_production, 75_LVBus0478055_production, 75_LVBus0478056_production, 75_LVBus0478057_production, 75_LVBus0478058_production, 75_LVBus0478059_production, 75_LVBus0478060_production, 75_LVBus0478061_production, 75_LVBus0478063_production, 75_LVBus0478064_production, 75_LVBus0478065_production, 75_LVBus0478066_consumption, 75_LVBus0478066_production, 75_LVBus0478067_production, 75_LVBus0478069_consumption, 75_LVBus0478069_production, 75_LVBus0478070_consumption, 75_LVBus0478070_production, 75_LVBus0478071_consumption, 75_LVBus0478071_production, 75_LVBus0478073_consumption, 75_LVBus0478073_production, 75_LVBus0478075_production, 75_LVBus0478076_production, 75_LVBus0478077_production, 75_LVBus0478078_production, 75_LVBus0478079_production, 75_LVBus0478080_production, 75_LVBus0478081_production, 75_LVBus0478083_production, 75_LVBus0478084_production, 75_LVBus0478086_production, 75_LVBus0478087_production, 75_LVBus0478088_production, 75_LVBus0478089_production, 75_LVBus0478090_production, 75_LVBus0478093_production, 75_LVBus0478095_consumption, 75_LVBus0478095_production, 75_LVBus0478097_production, 75_LVBus0478098_production, 75_LVBus0478099_production, 75_LVBus0478100_production, 75_LVBus0478101_production, 75_LVBus0478102_production, 75_LVBus0478103_consumption, 75_LVBus0478103_production, 75_LVBus0478104_consumption, 75_LVBus0478104_production, 75_LVBus0478105_production, 75_LVBus0478106_production, 75_LVBus0478107_production, 75_LVBus0478108_production, 75_LVBus0478109_production, 75_LVBus0478110_production, 75_LVBus0478111_consumption, 75_LVBus0478111_production, 75_LVBus0478112_production, 75_LVBus0478113_consumption, 75_LVBus0478113_production, 75_LVBus0478114_consumption, 75_LVBus0478114_production, 75_LVBus0478115_consumption, 75_LVBus0478115_production, 75_LVBus0478117_production, 75_LVBus0478119_consumption, 75_LVBus0478119_production, 75_LVBus0478120_production, 75_LVBus0478121_production, 75_LVBus0478122_consumption, 75_LVBus0478122_production, 75_LVBus0478123_consumption, 75_LVBus0478123_production, 75_LVBus0478124_consumption, 75_LVBus0478124_production, 75_LVBus0478125_consumption, 75_LVBus0478125_production, 75_LVBus0478126_production, 75_LVBus0478127_production, 75_LVBus0478128_production, 75_LVBus0478129_production, 75_LVBus0478130_consumption, 75_LVBus0478130_production, 75_LVBus0478131_production, 75_LVBus0478132_production, 75_LVBus0478133_consumption, 75_LVBus0478133_production, 75_LVBus0478134_production, 75_LVBus0478135_consumption, 75_LVBus0478135_production, 75_LVBus0478136_consumption, 75_LVBus0478136_production, 75_LVBus0478137_consumption, 75_LVBus0478137_production, 75_LVBus0478138_consumption, 75_LVBus0478138_production, 75_LVBus0478139_production, 75_LVBus0478141_production, 75_LVBus0478143_production, 75_LVBus0478144_consumption, 75_LVBus0478144_production, 75_LVBus0478145_consumption, 75_LVBus0478145_production, 75_LVBus0478146_production, 75_LVBus0478147_consumption, 75_LVBus0478147_production, 75_LVBus0478148_production, 75_LVBus0478149_consumption, 75_LVBus0478149_production, 75_LVBus0478150_consumption, 75_LVBus0478150_production, 75_LVBus0478151_production, 75_LVBus0478153_production, 75_LVBus0478154_production, 75_LVBus0478155_production, 75_LVBus0478157_production, 75_LVBus0478159_consumption, 75_LVBus0478159_production, 75_LVBus0478160_production, 75_LVBus0478161_production, 75_LVBus0478162_consumption, 75_LVBus0478162_production, 75_LVBus0478163_production, 75_LVBus0478165_production, 75_LVBus0478167_production, 75_LVBus0478169_production, 75_LVBus0478170_consumption, 75_LVBus0478170_production, 75_LVBus0478172_consumption, 75_LVBus0478172_production, 75_LVBus0478174_production, 75_LVBus0478176_consumption, 75_LVBus0478176_production, 75_LVBus0478177_production, 75_LVBus0478178_consumption, 75_LVBus0478178_production, 75_LVBus0478179_production, 75_LVBus0478181_production, 75_LVBus0478182_consumption, 75_LVBus0478182_production, 75_LVBus0478183_consumption, 75_LVBus0478183_production, 75_LVBus0478184_consumption, 75_LVBus0478184_production, 75_LVBus0478185_consumption, 75_LVBus0478185_production, 75_LVBus0478186_production, 75_LVBus0478187_consumption, 75_LVBus0478187_production, 75_LVBus0478188_consumption, 75_LVBus0478188_production, 75_LVBus0478189_consumption, 75_LVBus0478189_production, 75_LVBus0478190_consumption, 75_LVBus0478190_production, 75_LVBus0478191_consumption, 75_LVBus0478191_production, 75_LVBus0478192_consumption, 75_LVBus0478192_production, 75_LVBus0478193_consumption, 75_LVBus0478193_production, 75_LVBus0478194_consumption, 75_LVBus0478194_production, 75_LVBus0478195_production, 75_LVBus0478196_consumption, 75_LVBus0478196_production, 75_LVBus0478197_consumption, 75_LVBus0478197_production, 75_LVBus0478198_consumption, 75_LVBus0478198_production, 75_LVBus0478201_production, 75_LVBus0478202_production, 75_LVBus0478203_consumption, 75_LVBus0478203_production, 75_LVBus0478204_consumption, 75_LVBus0478204_production, 75_LVBus0478205_production, 75_LVBus0478206_consumption, 75_LVBus0478206_production, 75_LVBus0478208_consumption, 75_LVBus0478208_production, 75_LVBus0478210_production, 75_LVBus0478211_production, 75_LVBus0478212_production, 75_LVBus0478213_production, 75_LVBus0478214_production, 75_LVBus0478215_production, 75_LVBus0478216_production, 75_LVBus0478217_production, 75_LVBus0478219_consumption, 75_LVBus0478219_production, 75_LVBus0478220_production, 75_LVBus0478221_production, 75_LVBus0478222_production, 75_LVBus0478224_production, 75_LVBus0478226_consumption, 75_LVBus0478226_production, 75_LVBus0478228_consumption, 75_LVBus0478228_production, 75_LVBus0478229_production, 75_LVBus0478231_production, 75_LVBus0478233_consumption, 75_LVBus0478233_production, 75_LVBus0478235_consumption, 75_LVBus0478235_production, 75_LVBus0478237_consumption, 75_LVBus0478237_production, 75_LVBus0478238_consumption, 75_LVBus0478238_production, 75_LVBus0478239_consumption, 75_LVBus0478239_production, 75_LVBus0478240_consumption, 75_LVBus0478240_production, 75_LVBus0478241_production, 75_LVBus0478242_consumption, 75_LVBus0478242_production, 75_LVBus0478244_consumption, 75_LVBus0478244_production, 75_LVBus0478246_production, 75_LVBus0478247_consumption, 75_LVBus0478247_production, 75_LVBus0478248_consumption, 75_LVBus0478248_production, 75_LVBus0478249_production, 75_LVBus0478250_consumption, 75_LVBus0478250_production, 75_LVBus0478252_consumption, 75_LVBus0478252_production, 75_LVBus0478253_consumption, 75_LVBus0478253_production, 75_LVBus0478254_production, 75_LVBus0478255_production, 75_LVBus0478257_consumption, 75_LVBus0478257_production, 75_LVBus0478259_production, 75_LVBus0478261_production, 75_LVBus0478263_consumption, 75_LVBus0478263_production, 75_LVBus0478265_production, 75_LVBus0478267_production, 75_LVBus0478269_consumption, 75_LVBus0478269_production, 75_LVBus0478270_production, 75_LVBus0478271_production, 75_LVBus0478272_consumption, 75_LVBus0478272_production, 75_LVBus0478273_consumption, 75_LVBus0478273_production, 75_LVBus0478274_production, 75_LVBus0478275_consumption, 75_LVBus0478275_production, 75_LVBus0478276_production, 75_LVBus0478277_production, 75_LVBus0478278_production, 75_LVBus0478279_production, 75_LVBus0478280_production, 75_LVBus0478281_consumption, 75_LVBus0478281_production, 75_LVBus1927409_production, 75_MVLV005275_production, 75_MVLV021399_consumption, 75_MVLV021399_production, 75_MVLV025128_production, 75_MVLV055061_consumption, 75_MVLV055061_production, 75_MVLV058509_consumption, 75_MVLV058509_production, 75_MVLV058587_consumption, 75_MVLV058587_production, 75_MVLV066554_consumption, 75_MVLV066554_production, 75_MVLV069351_production, 75_MVLV069839_consumption, 75_MVLV069839_production, 75_MVLV099636_consumption, 75_MVLV099636_production, 75_MVLV107645_production, 75_MVLV107760_production, 75_MVLV158269_consumption, 75_MVLV158269_production, 75_MVLV158315_consumption, 75_MVLV158315_production.

## 9. Data Quality Summary

**Total findings:** 187 (0 errors, 5 warnings, 182 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  675 of 898 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (7.66 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  676 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478015_consumption`  
  Load '75_LVBus0478015_consumption' has phase imbalance of 29.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478131_consumption`  
  Load '75_LVBus0478131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478055_consumption`  
  Load '75_LVBus0478055_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477896_consumption`  
  Load '75_LVBus0477896_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477858_consumption`  
  Load '75_LVBus0477858_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478026_consumption`  
  Load '75_LVBus0478026_consumption' has phase imbalance of 44.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478109_consumption`  
  Load '75_LVBus0478109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477844_consumption`  
  Load '75_LVBus0477844_consumption' has phase imbalance of 54.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477934_consumption`  
  Load '75_LVBus0477934_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478022_consumption`  
  Load '75_LVBus0478022_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478153_consumption`  
  Load '75_LVBus0478153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477925_consumption`  
  Load '75_LVBus0477925_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478081_consumption`  
  Load '75_LVBus0478081_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477929_consumption`  
  Load '75_LVBus0477929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477906_consumption`  
  Load '75_LVBus0477906_consumption' has phase imbalance of 94.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478084_consumption`  
  Load '75_LVBus0478084_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477833_consumption`  
  Load '75_LVBus0477833_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477760_consumption`  
  Load '75_LVBus0477760_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478076_consumption`  
  Load '75_LVBus0478076_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477872_consumption`  
  Load '75_LVBus0477872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478216_consumption`  
  Load '75_LVBus0478216_consumption' has phase imbalance of 243.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477911_consumption`  
  Load '75_LVBus0477911_consumption' has phase imbalance of 24.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477875_consumption`  
  Load '75_LVBus0477875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478141_consumption`  
  Load '75_LVBus0478141_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477813_consumption`  
  Load '75_LVBus0477813_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478064_consumption`  
  Load '75_LVBus0478064_consumption' has phase imbalance of 182.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478241_consumption`  
  Load '75_LVBus0478241_consumption' has phase imbalance of 29.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478088_consumption`  
  Load '75_LVBus0478088_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478046_consumption`  
  Load '75_LVBus0478046_consumption' has phase imbalance of 67.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478214_consumption`  
  Load '75_LVBus0478214_consumption' has phase imbalance of 79.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478157_consumption`  
  Load '75_LVBus0478157_consumption' has phase imbalance of 213.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478128_consumption`  
  Load '75_LVBus0478128_consumption' has phase imbalance of 81.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478280_consumption`  
  Load '75_LVBus0478280_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477762_consumption`  
  Load '75_LVBus0477762_consumption' has phase imbalance of 52.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477946_consumption`  
  Load '75_LVBus0477946_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478151_consumption`  
  Load '75_LVBus0478151_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477928_consumption`  
  Load '75_LVBus0477928_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478139_consumption`  
  Load '75_LVBus0478139_consumption' has phase imbalance of 50.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477937_consumption`  
  Load '75_LVBus0477937_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478080_consumption`  
  Load '75_LVBus0478080_consumption' has phase imbalance of 76.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477935_consumption`  
  Load '75_LVBus0477935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478102_consumption`  
  Load '75_LVBus0478102_consumption' has phase imbalance of 109.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477826_consumption`  
  Load '75_LVBus0477826_consumption' has phase imbalance of 67.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478105_consumption`  
  Load '75_LVBus0478105_consumption' has phase imbalance of 201.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477986_consumption`  
  Load '75_LVBus0477986_consumption' has phase imbalance of 85.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478148_consumption`  
  Load '75_LVBus0478148_consumption' has phase imbalance of 112.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478155_consumption`  
  Load '75_LVBus0478155_consumption' has phase imbalance of 85.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478127_consumption`  
  Load '75_LVBus0478127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478077_consumption`  
  Load '75_LVBus0478077_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478126_consumption`  
  Load '75_LVBus0478126_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478003_consumption`  
  Load '75_LVBus0478003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478205_consumption`  
  Load '75_LVBus0478205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478174_consumption`  
  Load '75_LVBus0478174_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477900_consumption`  
  Load '75_LVBus0477900_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478075_consumption`  
  Load '75_LVBus0478075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478110_consumption`  
  Load '75_LVBus0478110_consumption' has phase imbalance of 132.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478143_consumption`  
  Load '75_LVBus0478143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477800_consumption`  
  Load '75_LVBus0477800_consumption' has phase imbalance of 75.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477855_consumption`  
  Load '75_LVBus0477855_consumption' has phase imbalance of 34.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477915_consumption`  
  Load '75_LVBus0477915_consumption' has phase imbalance of 20.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477940_consumption`  
  Load '75_LVBus0477940_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478202_consumption`  
  Load '75_LVBus0478202_consumption' has phase imbalance of 111.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478059_consumption`  
  Load '75_LVBus0478059_consumption' has phase imbalance of 133.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478163_consumption`  
  Load '75_LVBus0478163_consumption' has phase imbalance of 118.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477955_consumption`  
  Load '75_LVBus0477955_consumption' has phase imbalance of 22.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478112_consumption`  
  Load '75_LVBus0478112_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478097_consumption`  
  Load '75_LVBus0478097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477923_consumption`  
  Load '75_LVBus0477923_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477865_consumption`  
  Load '75_LVBus0477865_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478254_consumption`  
  Load '75_LVBus0478254_consumption' has phase imbalance of 45.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478215_consumption`  
  Load '75_LVBus0478215_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477979_consumption`  
  Load '75_LVBus0477979_consumption' has phase imbalance of 93.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477921_consumption`  
  Load '75_LVBus0477921_consumption' has phase imbalance of 94.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478034_consumption`  
  Load '75_LVBus0478034_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477883_consumption`  
  Load '75_LVBus0477883_consumption' has phase imbalance of 80.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478211_consumption`  
  Load '75_LVBus0478211_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478129_consumption`  
  Load '75_LVBus0478129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477851_consumption`  
  Load '75_LVBus0477851_consumption' has phase imbalance of 44.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478086_consumption`  
  Load '75_LVBus0478086_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478000_consumption`  
  Load '75_LVBus0478000_consumption' has phase imbalance of 127.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478108_consumption`  
  Load '75_LVBus0478108_consumption' has phase imbalance of 119.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478106_consumption`  
  Load '75_LVBus0478106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477984_consumption`  
  Load '75_LVBus0477984_consumption' has phase imbalance of 167.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478222_consumption`  
  Load '75_LVBus0478222_consumption' has phase imbalance of 24.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478093_consumption`  
  Load '75_LVBus0478093_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478270_consumption`  
  Load '75_LVBus0478270_consumption' has phase imbalance of 41.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477752_consumption`  
  Load '75_LVBus0477752_consumption' has phase imbalance of 112.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478067_consumption`  
  Load '75_LVBus0478067_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478220_consumption`  
  Load '75_LVBus0478220_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477885_consumption`  
  Load '75_LVBus0477885_consumption' has phase imbalance of 33.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478089_consumption`  
  Load '75_LVBus0478089_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477995_consumption`  
  Load '75_LVBus0477995_consumption' has phase imbalance of 20.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477876_consumption`  
  Load '75_LVBus0477876_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477757_consumption`  
  Load '75_LVBus0477757_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477838_consumption`  
  Load '75_LVBus0477838_consumption' has phase imbalance of 51.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478134_consumption`  
  Load '75_LVBus0478134_consumption' has phase imbalance of 25.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477993_consumption`  
  Load '75_LVBus0477993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478017_consumption`  
  Load '75_LVBus0478017_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477790_consumption`  
  Load '75_LVBus0477790_consumption' has phase imbalance of 40.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478146_consumption`  
  Load '75_LVBus0478146_consumption' has phase imbalance of 196.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477932_consumption`  
  Load '75_LVBus0477932_consumption' has phase imbalance of 58.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478161_consumption`  
  Load '75_LVBus0478161_consumption' has phase imbalance of 103.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477927_consumption`  
  Load '75_LVBus0477927_consumption' has phase imbalance of 88.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477893_consumption`  
  Load '75_LVBus0477893_consumption' has phase imbalance of 90.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477798_consumption`  
  Load '75_LVBus0477798_consumption' has phase imbalance of 58.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478060_consumption`  
  Load '75_LVBus0478060_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477988_consumption`  
  Load '75_LVBus0477988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478181_consumption`  
  Load '75_LVBus0478181_consumption' has phase imbalance of 73.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477987_consumption`  
  Load '75_LVBus0477987_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478101_consumption`  
  Load '75_LVBus0478101_consumption' has phase imbalance of 42.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477992_consumption`  
  Load '75_LVBus0477992_consumption' has phase imbalance of 35.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478165_consumption`  
  Load '75_LVBus0478165_consumption' has phase imbalance of 55.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478099_consumption`  
  Load '75_LVBus0478099_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478098_consumption`  
  Load '75_LVBus0478098_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477890_consumption`  
  Load '75_LVBus0477890_consumption' has phase imbalance of 27.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478065_consumption`  
  Load '75_LVBus0478065_consumption' has phase imbalance of 101.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477931_consumption`  
  Load '75_LVBus0477931_consumption' has phase imbalance of 221.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478058_consumption`  
  Load '75_LVBus0478058_consumption' has phase imbalance of 82.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477815_consumption`  
  Load '75_LVBus0477815_consumption' has phase imbalance of 132.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478117_consumption`  
  Load '75_LVBus0478117_consumption' has phase imbalance of 132.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477880_consumption`  
  Load '75_LVBus0477880_consumption' has phase imbalance of 128.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477870_consumption`  
  Load '75_LVBus0477870_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477897_consumption`  
  Load '75_LVBus0477897_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478179_consumption`  
  Load '75_LVBus0478179_consumption' has phase imbalance of 27.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478278_consumption`  
  Load '75_LVBus0478278_consumption' has phase imbalance of 229.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478037_consumption`  
  Load '75_LVBus0478037_consumption' has phase imbalance of 49.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478057_consumption`  
  Load '75_LVBus0478057_consumption' has phase imbalance of 121.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478090_consumption`  
  Load '75_LVBus0478090_consumption' has phase imbalance of 71.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478013_consumption`  
  Load '75_LVBus0478013_consumption' has phase imbalance of 23.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477755_consumption`  
  Load '75_LVBus0477755_consumption' has phase imbalance of 203.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478056_consumption`  
  Load '75_LVBus0478056_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478061_consumption`  
  Load '75_LVBus0478061_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477922_consumption`  
  Load '75_LVBus0477922_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477919_consumption`  
  Load '75_LVBus0477919_consumption' has phase imbalance of 32.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477861_consumption`  
  Load '75_LVBus0477861_consumption' has phase imbalance of 143.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478169_consumption`  
  Load '75_LVBus0478169_consumption' has phase imbalance of 73.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478246_consumption`  
  Load '75_LVBus0478246_consumption' has phase imbalance of 32.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478004_consumption`  
  Load '75_LVBus0478004_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477845_consumption`  
  Load '75_LVBus0477845_consumption' has phase imbalance of 77.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478276_consumption`  
  Load '75_LVBus0478276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478213_consumption`  
  Load '75_LVBus0478213_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478107_consumption`  
  Load '75_LVBus0478107_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478217_consumption`  
  Load '75_LVBus0478217_consumption' has phase imbalance of 217.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478083_consumption`  
  Load '75_LVBus0478083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477793_consumption`  
  Load '75_LVBus0477793_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477840_consumption`  
  Load '75_LVBus0477840_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477997_consumption`  
  Load '75_LVBus0477997_consumption' has phase imbalance of 137.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477818_consumption`  
  Load '75_LVBus0477818_consumption' has phase imbalance of 155.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477804_consumption`  
  Load '75_LVBus0477804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478087_consumption`  
  Load '75_LVBus0478087_consumption' has phase imbalance of 59.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478078_consumption`  
  Load '75_LVBus0478078_consumption' has phase imbalance of 47.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477924_consumption`  
  Load '75_LVBus0477924_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478005_consumption`  
  Load '75_LVBus0478005_consumption' has phase imbalance of 120.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477920_consumption`  
  Load '75_LVBus0477920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477926_consumption`  
  Load '75_LVBus0477926_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477945_consumption`  
  Load '75_LVBus0477945_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478100_consumption`  
  Load '75_LVBus0478100_consumption' has phase imbalance of 261.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477827_consumption`  
  Load '75_LVBus0477827_consumption' has phase imbalance of 39.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0478120_consumption`  
  Load '75_LVBus0478120_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477828_consumption`  
  Load '75_LVBus0477828_consumption' has phase imbalance of 259.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477809_consumption`  
  Load '75_LVBus0477809_consumption' has phase imbalance of 112.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0477859_consumption`  
  Load '75_LVBus0477859_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 898 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0478224' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_AUREN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0477742' has balanced aggregate load across 3 phase(s) (max spread 0.78%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0478049' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0478257' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  501 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  53 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0477804_consumption, 75_LVBus0477818_consumption, 75_LVBus0477828_consumption, 75_LVBus0477858_consumption, 75_LVBus0477872_consumption, 75_LVBus0477875_consumption, 75_LVBus0477896_consumption, 75_LVBus0477897_consumption, 75_LVBus0477900_consumption, 75_LVBus0477920_consumption, 75_LVBus0477922_consumption, 75_LVBus0477923_consumption, 75_LVBus0477925_consumption, 75_LVBus0477926_consumption, 75_LVBus0477928_consumption, 75_LVBus0477929_consumption, 75_LVBus0477935_consumption, 75_LVBus0477987_consumption, 75_LVBus0477988_consumption, 75_LVBus0477993_consumption, 75_LVBus0478003_consumption, 75_LVBus0478055_consumption, 75_LVBus0478056_consumption, 75_LVBus0478064_consumption, 75_LVBus0478075_consumption, 75_LVBus0478076_consumption, 75_LVBus0478077_consumption, 75_LVBus0478081_consumption, 75_LVBus0478083_consumption, 75_LVBus0478097_consumption, 75_LVBus0478098_consumption, 75_LVBus0478099_consumption, 75_LVBus0478100_consumption, 75_LVBus0478105_consumption, 75_LVBus0478106_consumption, 75_LVBus0478107_consumption, 75_LVBus0478109_consumption, 75_LVBus0478126_consumption, 75_LVBus0478127_consumption, 75_LVBus0478129_consumption, 75_LVBus0478131_consumption, 75_LVBus0478143_consumption, 75_LVBus0478146_consumption, 75_LVBus0478151_consumption, 75_LVBus0478153_consumption, 75_LVBus0478157_consumption, 75_LVBus0478205_consumption, 75_LVBus0478211_consumption, 75_LVBus0478216_consumption, 75_LVBus0478217_consumption, 75_LVBus0478220_consumption, 75_LVBus0478276_consumption, 75_LVBus0478278_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  449 group(s) of loads (898 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  2 group(s) of series lines (4 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  676 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0477742_production, 75_LVBus0477744_consumption, 75_LVBus0477744_production, 75_LVBus0477746_production, 75_LVBus0477748_production, 75_LVBus0477750_consumption, 75_LVBus0477750_production, 75_LVBus0477752_production, 75_LVBus0477754_consumption, 75_LVBus0477754_production, 75_LVBus0477755_production, 75_LVBus0477757_production, 75_LVBus0477758_production, 75_LVBus0477759_consumption, 75_LVBus0477759_production, 75_LVBus0477760_production, 75_LVBus0477761_production, 75_LVBus0477762_production, 75_LVBus0477764_consumption, 75_LVBus0477764_production, 75_LVBus0477765_consumption, 75_LVBus0477765_production, 75_LVBus0477766_consumption, 75_LVBus0477766_production, 75_LVBus0477767_consumption, 75_LVBus0477767_production, 75_LVBus0477768_consumption, 75_LVBus0477768_production, 75_LVBus0477769_consumption, 75_LVBus0477769_production, 75_LVBus0477770_consumption, 75_LVBus0477770_production, 75_LVBus0477771_consumption, 75_LVBus0477771_production, 75_LVBus0477773_consumption, 75_LVBus0477773_production, 75_LVBus0477774_consumption, 75_LVBus0477774_production, 75_LVBus0477775_consumption, 75_LVBus0477775_production, 75_LVBus0477776_consumption, 75_LVBus0477776_production, 75_LVBus0477777_consumption, 75_LVBus0477777_production, 75_LVBus0477778_consumption, 75_LVBus0477778_production, 75_LVBus0477779_consumption, 75_LVBus0477779_production, 75_LVBus0477781_consumption, 75_LVBus0477781_production, 75_LVBus0477782_consumption, 75_LVBus0477782_production, 75_LVBus0477783_consumption, 75_LVBus0477783_production, 75_LVBus0477784_consumption, 75_LVBus0477784_production, 75_LVBus0477785_production, 75_LVBus0477786_consumption, 75_LVBus0477786_production, 75_LVBus0477787_consumption, 75_LVBus0477787_production, 75_LVBus0477788_production, 75_LVBus0477789_consumption, 75_LVBus0477789_production, 75_LVBus0477790_production, 75_LVBus0477792_consumption, 75_LVBus0477792_production, 75_LVBus0477793_production, 75_LVBus0477794_consumption, 75_LVBus0477794_production, 75_LVBus0477795_consumption, 75_LVBus0477795_production, 75_LVBus0477797_consumption, 75_LVBus0477797_production, 75_LVBus0477798_production, 75_LVBus0477799_consumption, 75_LVBus0477799_production, 75_LVBus0477800_production, 75_LVBus0477801_consumption, 75_LVBus0477801_production, 75_LVBus0477802_consumption, 75_LVBus0477802_production, 75_LVBus0477803_production, 75_LVBus0477804_production, 75_LVBus0477805_consumption, 75_LVBus0477805_production, 75_LVBus0477807_consumption, 75_LVBus0477807_production, 75_LVBus0477808_consumption, 75_LVBus0477808_production, 75_LVBus0477809_production, 75_LVBus0477810_consumption, 75_LVBus0477810_production, 75_LVBus0477811_consumption, 75_LVBus0477811_production, 75_LVBus0477812_consumption, 75_LVBus0477812_production, 75_LVBus0477813_production, 75_LVBus0477814_consumption, 75_LVBus0477814_production, 75_LVBus0477815_production, 75_LVBus0477817_consumption, 75_LVBus0477817_production, 75_LVBus0477818_production, 75_LVBus0477820_consumption, 75_LVBus0477820_production, 75_LVBus0477821_consumption, 75_LVBus0477821_production, 75_LVBus0477822_consumption, 75_LVBus0477822_production, 75_LVBus0477823_consumption, 75_LVBus0477823_production, 75_LVBus0477825_production, 75_LVBus0477826_production, 75_LVBus0477827_production, 75_LVBus0477828_production, 75_LVBus0477829_consumption, 75_LVBus0477829_production, 75_LVBus0477830_production, 75_LVBus0477831_production, 75_LVBus0477833_production, 75_LVBus0477834_consumption, 75_LVBus0477834_production, 75_LVBus0477835_consumption, 75_LVBus0477835_production, 75_LVBus0477836_consumption, 75_LVBus0477836_production, 75_LVBus0477837_consumption, 75_LVBus0477837_production, 75_LVBus0477838_production, 75_LVBus0477839_production, 75_LVBus0477840_production, 75_LVBus0477841_consumption, 75_LVBus0477841_production, 75_LVBus0477842_consumption, 75_LVBus0477842_production, 75_LVBus0477843_consumption, 75_LVBus0477843_production, 75_LVBus0477844_production, 75_LVBus0477845_production, 75_LVBus0477849_consumption, 75_LVBus0477849_production, 75_LVBus0477851_production, 75_LVBus0477853_consumption, 75_LVBus0477853_production, 75_LVBus0477855_production, 75_LVBus0477857_consumption, 75_LVBus0477857_production, 75_LVBus0477858_production, 75_LVBus0477859_production, 75_LVBus0477861_production, 75_LVBus0477862_consumption, 75_LVBus0477862_production, 75_LVBus0477863_consumption, 75_LVBus0477863_production, 75_LVBus0477864_consumption, 75_LVBus0477864_production, 75_LVBus0477865_production, 75_LVBus0477866_consumption, 75_LVBus0477866_production, 75_LVBus0477867_consumption, 75_LVBus0477867_production, 75_LVBus0477868_consumption, 75_LVBus0477868_production, 75_LVBus0477869_consumption, 75_LVBus0477869_production, 75_LVBus0477870_production, 75_LVBus0477871_consumption, 75_LVBus0477871_production, 75_LVBus0477872_production, 75_LVBus0477873_consumption, 75_LVBus0477873_production, 75_LVBus0477874_production, 75_LVBus0477875_production, 75_LVBus0477876_production, 75_LVBus0477877_production, 75_LVBus0477878_consumption, 75_LVBus0477878_production, 75_LVBus0477880_production, 75_LVBus0477881_consumption, 75_LVBus0477881_production, 75_LVBus0477882_consumption, 75_LVBus0477882_production, 75_LVBus0477883_production, 75_LVBus0477884_production, 75_LVBus0477885_production, 75_LVBus0477887_consumption, 75_LVBus0477887_production, 75_LVBus0477888_consumption, 75_LVBus0477888_production, 75_LVBus0477890_production, 75_LVBus0477892_consumption, 75_LVBus0477892_production, 75_LVBus0477893_production, 75_LVBus0477895_consumption, 75_LVBus0477895_production, 75_LVBus0477896_production, 75_LVBus0477897_production, 75_LVBus0477898_consumption, 75_LVBus0477898_production, 75_LVBus0477899_consumption, 75_LVBus0477899_production, 75_LVBus0477900_production, 75_LVBus0477902_consumption, 75_LVBus0477902_production, 75_LVBus0477903_consumption, 75_LVBus0477903_production, 75_LVBus0477905_consumption, 75_LVBus0477905_production, 75_LVBus0477906_production, 75_LVBus0477908_consumption, 75_LVBus0477908_production, 75_LVBus0477910_consumption, 75_LVBus0477910_production, 75_LVBus0477911_production, 75_LVBus0477913_consumption, 75_LVBus0477913_production, 75_LVBus0477914_production, 75_LVBus0477915_production, 75_LVBus0477916_consumption, 75_LVBus0477916_production, 75_LVBus0477918_consumption, 75_LVBus0477918_production, 75_LVBus0477919_production, 75_LVBus0477920_production, 75_LVBus0477921_production, 75_LVBus0477922_production, 75_LVBus0477923_production, 75_LVBus0477924_production, 75_LVBus0477925_production, 75_LVBus0477926_production, 75_LVBus0477927_production, 75_LVBus0477928_production, 75_LVBus0477929_production, 75_LVBus0477931_production, 75_LVBus0477932_production, 75_LVBus0477934_production, 75_LVBus0477935_production, 75_LVBus0477936_production, 75_LVBus0477937_production, 75_LVBus0477938_consumption, 75_LVBus0477938_production, 75_LVBus0477940_production, 75_LVBus0477942_consumption, 75_LVBus0477942_production, 75_LVBus0477943_consumption, 75_LVBus0477943_production, 75_LVBus0477944_consumption, 75_LVBus0477944_production, 75_LVBus0477945_production, 75_LVBus0477946_production, 75_LVBus0477948_production, 75_LVBus0477949_consumption, 75_LVBus0477949_production, 75_LVBus0477951_production, 75_LVBus0477952_consumption, 75_LVBus0477952_production, 75_LVBus0477953_consumption, 75_LVBus0477953_production, 75_LVBus0477954_consumption, 75_LVBus0477954_production, 75_LVBus0477955_production, 75_LVBus0477956_consumption, 75_LVBus0477956_production, 75_LVBus0477957_consumption, 75_LVBus0477957_production, 75_LVBus0477958_consumption, 75_LVBus0477958_production, 75_LVBus0477959_consumption, 75_LVBus0477959_production, 75_LVBus0477960_consumption, 75_LVBus0477960_production, 75_LVBus0477961_consumption, 75_LVBus0477961_production, 75_LVBus0477963_consumption, 75_LVBus0477963_production, 75_LVBus0477964_consumption, 75_LVBus0477964_production, 75_LVBus0477965_consumption, 75_LVBus0477965_production, 75_LVBus0477966_consumption, 75_LVBus0477966_production, 75_LVBus0477967_consumption, 75_LVBus0477967_production, 75_LVBus0477968_consumption, 75_LVBus0477968_production, 75_LVBus0477969_consumption, 75_LVBus0477969_production, 75_LVBus0477970_consumption, 75_LVBus0477970_production, 75_LVBus0477971_consumption, 75_LVBus0477971_production, 75_LVBus0477972_consumption, 75_LVBus0477972_production, 75_LVBus0477973_consumption, 75_LVBus0477973_production, 75_LVBus0477974_consumption, 75_LVBus0477974_production, 75_LVBus0477976_consumption, 75_LVBus0477976_production, 75_LVBus0477977_consumption, 75_LVBus0477977_production, 75_LVBus0477978_consumption, 75_LVBus0477978_production, 75_LVBus0477979_production, 75_LVBus0477980_consumption, 75_LVBus0477980_production, 75_LVBus0477981_consumption, 75_LVBus0477981_production, 75_LVBus0477983_consumption, 75_LVBus0477983_production, 75_LVBus0477984_production, 75_LVBus0477985_consumption, 75_LVBus0477985_production, 75_LVBus0477986_production, 75_LVBus0477987_production, 75_LVBus0477988_production, 75_LVBus0477990_production, 75_LVBus0477992_production, 75_LVBus0477993_production, 75_LVBus0477994_consumption, 75_LVBus0477994_production, 75_LVBus0477995_production, 75_LVBus0477997_production, 75_LVBus0477999_production, 75_LVBus0478000_production, 75_LVBus0478001_consumption, 75_LVBus0478001_production, 75_LVBus0478003_production, 75_LVBus0478004_production, 75_LVBus0478005_production, 75_LVBus0478007_consumption, 75_LVBus0478007_production, 75_LVBus0478008_production, 75_LVBus0478010_consumption, 75_LVBus0478010_production, 75_LVBus0478011_consumption, 75_LVBus0478011_production, 75_LVBus0478012_production, 75_LVBus0478013_production, 75_LVBus0478014_consumption, 75_LVBus0478014_production, 75_LVBus0478015_production, 75_LVBus0478017_production, 75_LVBus0478018_consumption, 75_LVBus0478018_production, 75_LVBus0478019_consumption, 75_LVBus0478019_production, 75_LVBus0478020_production, 75_LVBus0478021_production, 75_LVBus0478022_production, 75_LVBus0478023_consumption, 75_LVBus0478023_production, 75_LVBus0478024_consumption, 75_LVBus0478024_production, 75_LVBus0478025_consumption, 75_LVBus0478025_production, 75_LVBus0478026_production, 75_LVBus0478028_consumption, 75_LVBus0478028_production, 75_LVBus0478029_consumption, 75_LVBus0478029_production, 75_LVBus0478030_consumption, 75_LVBus0478030_production, 75_LVBus0478031_consumption, 75_LVBus0478031_production, 75_LVBus0478032_consumption, 75_LVBus0478032_production, 75_LVBus0478033_production, 75_LVBus0478034_production, 75_LVBus0478035_consumption, 75_LVBus0478035_production, 75_LVBus0478036_consumption, 75_LVBus0478036_production, 75_LVBus0478037_production, 75_LVBus0478038_consumption, 75_LVBus0478038_production, 75_LVBus0478039_consumption, 75_LVBus0478039_production, 75_LVBus0478040_consumption, 75_LVBus0478040_production, 75_LVBus0478041_consumption, 75_LVBus0478041_production, 75_LVBus0478042_consumption, 75_LVBus0478042_production, 75_LVBus0478043_consumption, 75_LVBus0478043_production, 75_LVBus0478044_consumption, 75_LVBus0478044_production, 75_LVBus0478046_production, 75_LVBus0478049_consumption, 75_LVBus0478049_production, 75_LVBus0478051_production, 75_LVBus0478053_consumption, 75_LVBus0478053_production, 75_LVBus0478055_production, 75_LVBus0478056_production, 75_LVBus0478057_production, 75_LVBus0478058_production, 75_LVBus0478059_production, 75_LVBus0478060_production, 75_LVBus0478061_production, 75_LVBus0478063_production, 75_LVBus0478064_production, 75_LVBus0478065_production, 75_LVBus0478066_consumption, 75_LVBus0478066_production, 75_LVBus0478067_production, 75_LVBus0478069_consumption, 75_LVBus0478069_production, 75_LVBus0478070_consumption, 75_LVBus0478070_production, 75_LVBus0478071_consumption, 75_LVBus0478071_production, 75_LVBus0478073_consumption, 75_LVBus0478073_production, 75_LVBus0478075_production, 75_LVBus0478076_production, 75_LVBus0478077_production, 75_LVBus0478078_production, 75_LVBus0478079_production, 75_LVBus0478080_production, 75_LVBus0478081_production, 75_LVBus0478083_production, 75_LVBus0478084_production, 75_LVBus0478086_production, 75_LVBus0478087_production, 75_LVBus0478088_production, 75_LVBus0478089_production, 75_LVBus0478090_production, 75_LVBus0478093_production, 75_LVBus0478095_consumption, 75_LVBus0478095_production, 75_LVBus0478097_production, 75_LVBus0478098_production, 75_LVBus0478099_production, 75_LVBus0478100_production, 75_LVBus0478101_production, 75_LVBus0478102_production, 75_LVBus0478103_consumption, 75_LVBus0478103_production, 75_LVBus0478104_consumption, 75_LVBus0478104_production, 75_LVBus0478105_production, 75_LVBus0478106_production, 75_LVBus0478107_production, 75_LVBus0478108_production, 75_LVBus0478109_production, 75_LVBus0478110_production, 75_LVBus0478111_consumption, 75_LVBus0478111_production, 75_LVBus0478112_production, 75_LVBus0478113_consumption, 75_LVBus0478113_production, 75_LVBus0478114_consumption, 75_LVBus0478114_production, 75_LVBus0478115_consumption, 75_LVBus0478115_production, 75_LVBus0478117_production, 75_LVBus0478119_consumption, 75_LVBus0478119_production, 75_LVBus0478120_production, 75_LVBus0478121_production, 75_LVBus0478122_consumption, 75_LVBus0478122_production, 75_LVBus0478123_consumption, 75_LVBus0478123_production, 75_LVBus0478124_consumption, 75_LVBus0478124_production, 75_LVBus0478125_consumption, 75_LVBus0478125_production, 75_LVBus0478126_production, 75_LVBus0478127_production, 75_LVBus0478128_production, 75_LVBus0478129_production, 75_LVBus0478130_consumption, 75_LVBus0478130_production, 75_LVBus0478131_production, 75_LVBus0478132_production, 75_LVBus0478133_consumption, 75_LVBus0478133_production, 75_LVBus0478134_production, 75_LVBus0478135_consumption, 75_LVBus0478135_production, 75_LVBus0478136_consumption, 75_LVBus0478136_production, 75_LVBus0478137_consumption, 75_LVBus0478137_production, 75_LVBus0478138_consumption, 75_LVBus0478138_production, 75_LVBus0478139_production, 75_LVBus0478141_production, 75_LVBus0478143_production, 75_LVBus0478144_consumption, 75_LVBus0478144_production, 75_LVBus0478145_consumption, 75_LVBus0478145_production, 75_LVBus0478146_production, 75_LVBus0478147_consumption, 75_LVBus0478147_production, 75_LVBus0478148_production, 75_LVBus0478149_consumption, 75_LVBus0478149_production, 75_LVBus0478150_consumption, 75_LVBus0478150_production, 75_LVBus0478151_production, 75_LVBus0478153_production, 75_LVBus0478154_production, 75_LVBus0478155_production, 75_LVBus0478157_production, 75_LVBus0478159_consumption, 75_LVBus0478159_production, 75_LVBus0478160_production, 75_LVBus0478161_production, 75_LVBus0478162_consumption, 75_LVBus0478162_production, 75_LVBus0478163_production, 75_LVBus0478165_production, 75_LVBus0478167_production, 75_LVBus0478169_production, 75_LVBus0478170_consumption, 75_LVBus0478170_production, 75_LVBus0478172_consumption, 75_LVBus0478172_production, 75_LVBus0478174_production, 75_LVBus0478176_consumption, 75_LVBus0478176_production, 75_LVBus0478177_production, 75_LVBus0478178_consumption, 75_LVBus0478178_production, 75_LVBus0478179_production, 75_LVBus0478181_production, 75_LVBus0478182_consumption, 75_LVBus0478182_production, 75_LVBus0478183_consumption, 75_LVBus0478183_production, 75_LVBus0478184_consumption, 75_LVBus0478184_production, 75_LVBus0478185_consumption, 75_LVBus0478185_production, 75_LVBus0478186_production, 75_LVBus0478187_consumption, 75_LVBus0478187_production, 75_LVBus0478188_consumption, 75_LVBus0478188_production, 75_LVBus0478189_consumption, 75_LVBus0478189_production, 75_LVBus0478190_consumption, 75_LVBus0478190_production, 75_LVBus0478191_consumption, 75_LVBus0478191_production, 75_LVBus0478192_consumption, 75_LVBus0478192_production, 75_LVBus0478193_consumption, 75_LVBus0478193_production, 75_LVBus0478194_consumption, 75_LVBus0478194_production, 75_LVBus0478195_production, 75_LVBus0478196_consumption, 75_LVBus0478196_production, 75_LVBus0478197_consumption, 75_LVBus0478197_production, 75_LVBus0478198_consumption, 75_LVBus0478198_production, 75_LVBus0478201_production, 75_LVBus0478202_production, 75_LVBus0478203_consumption, 75_LVBus0478203_production, 75_LVBus0478204_consumption, 75_LVBus0478204_production, 75_LVBus0478205_production, 75_LVBus0478206_consumption, 75_LVBus0478206_production, 75_LVBus0478208_consumption, 75_LVBus0478208_production, 75_LVBus0478210_production, 75_LVBus0478211_production, 75_LVBus0478212_production, 75_LVBus0478213_production, 75_LVBus0478214_production, 75_LVBus0478215_production, 75_LVBus0478216_production, 75_LVBus0478217_production, 75_LVBus0478219_consumption, 75_LVBus0478219_production, 75_LVBus0478220_production, 75_LVBus0478221_production, 75_LVBus0478222_production, 75_LVBus0478224_production, 75_LVBus0478226_consumption, 75_LVBus0478226_production, 75_LVBus0478228_consumption, 75_LVBus0478228_production, 75_LVBus0478229_production, 75_LVBus0478231_production, 75_LVBus0478233_consumption, 75_LVBus0478233_production, 75_LVBus0478235_consumption, 75_LVBus0478235_production, 75_LVBus0478237_consumption, 75_LVBus0478237_production, 75_LVBus0478238_consumption, 75_LVBus0478238_production, 75_LVBus0478239_consumption, 75_LVBus0478239_production, 75_LVBus0478240_consumption, 75_LVBus0478240_production, 75_LVBus0478241_production, 75_LVBus0478242_consumption, 75_LVBus0478242_production, 75_LVBus0478244_consumption, 75_LVBus0478244_production, 75_LVBus0478246_production, 75_LVBus0478247_consumption, 75_LVBus0478247_production, 75_LVBus0478248_consumption, 75_LVBus0478248_production, 75_LVBus0478249_production, 75_LVBus0478250_consumption, 75_LVBus0478250_production, 75_LVBus0478252_consumption, 75_LVBus0478252_production, 75_LVBus0478253_consumption, 75_LVBus0478253_production, 75_LVBus0478254_production, 75_LVBus0478255_production, 75_LVBus0478257_consumption, 75_LVBus0478257_production, 75_LVBus0478259_production, 75_LVBus0478261_production, 75_LVBus0478263_consumption, 75_LVBus0478263_production, 75_LVBus0478265_production, 75_LVBus0478267_production, 75_LVBus0478269_consumption, 75_LVBus0478269_production, 75_LVBus0478270_production, 75_LVBus0478271_production, 75_LVBus0478272_consumption, 75_LVBus0478272_production, 75_LVBus0478273_consumption, 75_LVBus0478273_production, 75_LVBus0478274_production, 75_LVBus0478275_consumption, 75_LVBus0478275_production, 75_LVBus0478276_production, 75_LVBus0478277_production, 75_LVBus0478278_production, 75_LVBus0478279_production, 75_LVBus0478280_production, 75_LVBus0478281_consumption, 75_LVBus0478281_production, 75_LVBus1927409_production, 75_MVLV005275_production, 75_MVLV021399_consumption, 75_MVLV021399_production, 75_MVLV025128_production, 75_MVLV055061_consumption, 75_MVLV055061_production, 75_MVLV058509_consumption, 75_MVLV058509_production, 75_MVLV058587_consumption, 75_MVLV058587_production, 75_MVLV066554_consumption, 75_MVLV066554_production, 75_MVLV069351_production, 75_MVLV069839_consumption, 75_MVLV069839_production, 75_MVLV099636_consumption, 75_MVLV099636_production, 75_MVLV107645_production, 75_MVLV107760_production, 75_MVLV158269_consumption, 75_MVLV158269_production, 75_MVLV158315_consumption, 75_MVLV158315_production.

