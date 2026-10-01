# BMOPF Network Summary: 27_MVFeeder1284

**Generated:** 2026-10-01 23:34:00  
**Findings:** 0 errors · 4 warnings · 182 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 323 |  |
| line | 309 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 592 | 5.709 MW, 1.71 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 13 |  |
| switch | 0 |  |
| transformer | 13 | Dyn11×13 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 19 | 18 | 10 | 0 |
| LV_236V | 236.0 V | 304 | 291 | 582 | 0 |

**Transformer transitions:**

- `27_MVLV36612_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV27143_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV19488_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV13358_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV22743_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV58600_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV03485_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV38734_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV18840_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV32124_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV38695_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV44590_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV84304_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 138 |
| Tree depth (max hops) | 24 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 323 | 1 | 322 | 0 | 0 | 0 |
| Tier LV_236V | 304 | 13 | 291 | 0 | 0 | 0 |
| Tier MV_11.8kV | 19 | 1 | 18 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 13; skipped invalid branches: 0.

Galvanic zones: 14; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 27_L.SAU | MV_11.8kV | 19 | 0 | 0 | 13 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1273 declared bus terminals; 1218 mapped line/closed-switch conductor edges; 55 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 529000.0 | 7.281 | 1776 |
| q_nom | 0.0 | 159000.0 | 7.281 | 1776 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.814 | 930.0 | 1.443 | 309 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 1.1e6 | 0.492 | 13 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 384 of 592 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723135_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723308_consumption' has phase imbalance of 88.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723130_consumption' has phase imbalance of 21.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723043_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723010_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723213_consumption' has phase imbalance of 104.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723100_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723106_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723232_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723079_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723076_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723056_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723104_consumption' has phase imbalance of 92.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723013_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723328_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723219_consumption' has phase imbalance of 53.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723165_consumption' has phase imbalance of 80.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723326_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723315_consumption' has phase imbalance of 139.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723134_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723250_consumption' has phase imbalance of 38.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723251_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723334_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723045_consumption' has phase imbalance of 98.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723164_consumption' has phase imbalance of 117.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723087_consumption' has phase imbalance of 123.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723305_consumption' has phase imbalance of 254.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723258_consumption' has phase imbalance of 66.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723256_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723161_consumption' has phase imbalance of 41.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723055_consumption' has phase imbalance of 220.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723148_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723237_consumption' has phase imbalance of 66.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723289_consumption' has phase imbalance of 208.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723293_consumption' has phase imbalance of 71.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723299_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723235_consumption' has phase imbalance of 23.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723302_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723283_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723033_consumption' has phase imbalance of 21.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723329_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723093_consumption' has phase imbalance of 21.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723102_consumption' has phase imbalance of 112.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723270_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723194_consumption' has phase imbalance of 248.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723234_consumption' has phase imbalance of 95.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723064_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723233_consumption' has phase imbalance of 61.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723217_consumption' has phase imbalance of 207.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723333_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723199_consumption' has phase imbalance of 22.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723036_consumption' has phase imbalance of 242.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723249_consumption' has phase imbalance of 30.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723303_consumption' has phase imbalance of 155.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723275_consumption' has phase imbalance of 83.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723116_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723180_consumption' has phase imbalance of 95.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723252_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723063_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus722992_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723223_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723285_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723131_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723040_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723221_consumption' has phase imbalance of 263.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723327_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723290_consumption' has phase imbalance of 134.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723024_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723022_consumption' has phase imbalance of 54.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723108_consumption' has phase imbalance of 184.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723127_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723212_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723054_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723071_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723218_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723314_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723141_consumption' has phase imbalance of 262.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723273_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723211_consumption' has phase imbalance of 35.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723280_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723210_consumption' has phase imbalance of 53.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723204_consumption' has phase imbalance of 58.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723300_consumption' has phase imbalance of 238.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723085_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723027_consumption' has phase imbalance of 118.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723044_consumption' has phase imbalance of 186.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723115_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723094_consumption' has phase imbalance of 192.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723047_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723335_consumption' has phase imbalance of 182.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723012_consumption' has phase imbalance of 24.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723311_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723205_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723034_consumption' has phase imbalance of 256.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723245_consumption' has phase imbalance of 198.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723321_consumption' has phase imbalance of 102.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723049_consumption' has phase imbalance of 92.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723229_consumption' has phase imbalance of 98.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723236_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723239_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723214_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723162_consumption' has phase imbalance of 119.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723203_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723265_consumption' has phase imbalance of 82.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723089_consumption' has phase imbalance of 104.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723331_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723143_consumption' has phase imbalance of 110.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723330_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723301_consumption' has phase imbalance of 239.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723037_consumption' has phase imbalance of 95.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723114_consumption' has phase imbalance of 173.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723279_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723072_consumption' has phase imbalance of 110.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723231_consumption' has phase imbalance of 83.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus722988_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723310_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723320_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus722985_consumption' has phase imbalance of 134.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723261_consumption' has phase imbalance of 112.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723110_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723070_consumption' has phase imbalance of 99.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723146_consumption' has phase imbalance of 81.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723147_consumption' has phase imbalance of 86.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723269_consumption' has phase imbalance of 255.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723253_consumption' has phase imbalance of 43.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus722998_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723113_consumption' has phase imbalance of 31.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus722981_consumption' has phase imbalance of 105.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723082_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723228_consumption' has phase imbalance of 118.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723097_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723294_consumption' has phase imbalance of 90.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723297_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723208_consumption' has phase imbalance of 62.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723197_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723296_consumption' has phase imbalance of 255.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723284_consumption' has phase imbalance of 39.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723092_consumption' has phase imbalance of 78.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723096_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723304_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723306_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723019_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723336_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723266_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus723271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 592 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_L.SAU' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 5.709 MW |
| Total load Q | 1.71 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 27_MVLV36612_Transformer | 275.0 kVA | 70.1% |
| 27_MVLV27143_Transformer | 440.0 kVA | 48.8% |
| 27_MVLV19488_Transformer | 693.0 kVA | 54.4% |
| 27_MVLV13358_Transformer | 693.0 kVA | 62.0% |
| 27_MVLV22743_Transformer | 693.0 kVA | 50.2% |
| 27_MVLV58600_Transformer | 275.0 kVA | 51.1% |
| 27_MVLV03485_Transformer | 1.1 MVA | 40.0% |
| 27_MVLV38734_Transformer | 693.0 kVA | 57.3% |
| 27_MVLV18840_Transformer | 275.0 kVA | 22.3% |
| 27_MVLV32124_Transformer | 440.0 kVA | 43.5% |
| 27_MVLV38695_Transformer | 693.0 kVA | 70.9% |
| 27_MVLV44590_Transformer | 275.0 kVA | 49.9% |
| 27_MVLV84304_Transformer | 275.0 kVA | 40.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.71 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 323 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 323 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 19 |
| LV_236V | 4-wire | 304 / 304 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 304 |
| Neutral branches | 291 |
| Grounding points | 13 |
| Neutral sections | 13 |
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
| 11.78 kV | 19 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 51 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 14 |
| Islands without voltage reference | 0 |
| Line impedance spread | 485.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 304 / 19 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 385 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 385 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus722979_consumption, 27_LVBus722979_production, 27_LVBus722980_consumption, 27_LVBus722980_production, 27_LVBus722981_production, 27_LVBus722982_consumption, 27_LVBus722982_production, 27_LVBus722983_consumption, 27_LVBus722983_production, 27_LVBus722984_production, 27_LVBus722985_production, 27_LVBus722986_production, 27_LVBus722987_consumption, 27_LVBus722987_production, 27_LVBus722988_production, 27_LVBus722989_production, 27_LVBus722991_production, 27_LVBus722992_production, 27_LVBus722993_production, 27_LVBus722995_production, 27_LVBus722997_consumption, 27_LVBus722997_production, 27_LVBus722998_production, 27_LVBus722999_production, 27_LVBus723001_consumption, 27_LVBus723001_production, 27_LVBus723003_production, 27_LVBus723005_consumption, 27_LVBus723005_production, 27_LVBus723007_consumption, 27_LVBus723007_production, 27_LVBus723009_consumption, 27_LVBus723009_production, 27_LVBus723010_production, 27_LVBus723011_consumption, 27_LVBus723011_production, 27_LVBus723012_production, 27_LVBus723013_production, 27_LVBus723015_consumption, 27_LVBus723015_production, 27_LVBus723016_production, 27_LVBus723017_consumption, 27_LVBus723017_production, 27_LVBus723018_consumption, 27_LVBus723018_production, 27_LVBus723019_production, 27_LVBus723020_production, 27_LVBus723022_production, 27_LVBus723024_production, 27_LVBus723026_consumption, 27_LVBus723026_production, 27_LVBus723027_production, 27_LVBus723028_production, 27_LVBus723029_production, 27_LVBus723030_production, 27_LVBus723031_production, 27_LVBus723032_production, 27_LVBus723033_production, 27_LVBus723034_production, 27_LVBus723036_production, 27_LVBus723037_production, 27_LVBus723038_production, 27_LVBus723039_production, 27_LVBus723040_production, 27_LVBus723041_consumption, 27_LVBus723041_production, 27_LVBus723043_production, 27_LVBus723044_production, 27_LVBus723045_production, 27_LVBus723046_production, 27_LVBus723047_production, 27_LVBus723049_production, 27_LVBus723051_consumption, 27_LVBus723051_production, 27_LVBus723052_production, 27_LVBus723053_production, 27_LVBus723054_production, 27_LVBus723055_production, 27_LVBus723056_production, 27_LVBus723057_production, 27_LVBus723059_production, 27_LVBus723061_production, 27_LVBus723063_production, 27_LVBus723064_production, 27_LVBus723065_production, 27_LVBus723066_consumption, 27_LVBus723066_production, 27_LVBus723068_production, 27_LVBus723069_consumption, 27_LVBus723069_production, 27_LVBus723070_production, 27_LVBus723071_production, 27_LVBus723072_production, 27_LVBus723073_production, 27_LVBus723075_consumption, 27_LVBus723075_production, 27_LVBus723076_production, 27_LVBus723077_production, 27_LVBus723078_consumption, 27_LVBus723078_production, 27_LVBus723079_production, 27_LVBus723080_production, 27_LVBus723082_production, 27_LVBus723083_production, 27_LVBus723084_consumption, 27_LVBus723084_production, 27_LVBus723085_production, 27_LVBus723086_production, 27_LVBus723087_production, 27_LVBus723088_consumption, 27_LVBus723088_production, 27_LVBus723089_production, 27_LVBus723090_production, 27_LVBus723091_consumption, 27_LVBus723091_production, 27_LVBus723092_production, 27_LVBus723093_production, 27_LVBus723094_production, 27_LVBus723096_production, 27_LVBus723097_production, 27_LVBus723098_consumption, 27_LVBus723098_production, 27_LVBus723099_production, 27_LVBus723100_production, 27_LVBus723101_consumption, 27_LVBus723101_production, 27_LVBus723102_production, 27_LVBus723103_consumption, 27_LVBus723103_production, 27_LVBus723104_production, 27_LVBus723106_production, 27_LVBus723107_production, 27_LVBus723108_production, 27_LVBus723109_production, 27_LVBus723110_production, 27_LVBus723111_production, 27_LVBus723112_consumption, 27_LVBus723112_production, 27_LVBus723113_production, 27_LVBus723114_production, 27_LVBus723115_production, 27_LVBus723116_production, 27_LVBus723117_consumption, 27_LVBus723117_production, 27_LVBus723118_consumption, 27_LVBus723118_production, 27_LVBus723119_consumption, 27_LVBus723119_production, 27_LVBus723120_consumption, 27_LVBus723120_production, 27_LVBus723121_consumption, 27_LVBus723121_production, 27_LVBus723122_consumption, 27_LVBus723122_production, 27_LVBus723123_consumption, 27_LVBus723123_production, 27_LVBus723124_consumption, 27_LVBus723124_production, 27_LVBus723125_consumption, 27_LVBus723125_production, 27_LVBus723126_consumption, 27_LVBus723126_production, 27_LVBus723127_production, 27_LVBus723128_consumption, 27_LVBus723128_production, 27_LVBus723129_consumption, 27_LVBus723129_production, 27_LVBus723130_production, 27_LVBus723131_production, 27_LVBus723133_consumption, 27_LVBus723133_production, 27_LVBus723134_production, 27_LVBus723135_production, 27_LVBus723136_consumption, 27_LVBus723136_production, 27_LVBus723137_consumption, 27_LVBus723137_production, 27_LVBus723138_consumption, 27_LVBus723138_production, 27_LVBus723139_consumption, 27_LVBus723139_production, 27_LVBus723140_production, 27_LVBus723141_production, 27_LVBus723142_production, 27_LVBus723143_production, 27_LVBus723145_consumption, 27_LVBus723145_production, 27_LVBus723146_production, 27_LVBus723147_production, 27_LVBus723148_production, 27_LVBus723153_consumption, 27_LVBus723153_production, 27_LVBus723154_consumption, 27_LVBus723154_production, 27_LVBus723155_consumption, 27_LVBus723155_production, 27_LVBus723156_consumption, 27_LVBus723156_production, 27_LVBus723158_consumption, 27_LVBus723158_production, 27_LVBus723160_consumption, 27_LVBus723160_production, 27_LVBus723161_production, 27_LVBus723162_production, 27_LVBus723163_production, 27_LVBus723164_production, 27_LVBus723165_production, 27_LVBus723167_production, 27_LVBus723169_consumption, 27_LVBus723169_production, 27_LVBus723171_consumption, 27_LVBus723171_production, 27_LVBus723173_consumption, 27_LVBus723173_production, 27_LVBus723174_consumption, 27_LVBus723174_production, 27_LVBus723175_consumption, 27_LVBus723175_production, 27_LVBus723176_consumption, 27_LVBus723176_production, 27_LVBus723177_consumption, 27_LVBus723177_production, 27_LVBus723178_production, 27_LVBus723179_consumption, 27_LVBus723179_production, 27_LVBus723180_production, 27_LVBus723182_consumption, 27_LVBus723182_production, 27_LVBus723184_consumption, 27_LVBus723184_production, 27_LVBus723186_consumption, 27_LVBus723186_production, 27_LVBus723188_consumption, 27_LVBus723188_production, 27_LVBus723190_consumption, 27_LVBus723190_production, 27_LVBus723192_production, 27_LVBus723194_production, 27_LVBus723196_consumption, 27_LVBus723196_production, 27_LVBus723197_production, 27_LVBus723198_consumption, 27_LVBus723198_production, 27_LVBus723199_production, 27_LVBus723201_consumption, 27_LVBus723201_production, 27_LVBus723203_production, 27_LVBus723204_production, 27_LVBus723205_production, 27_LVBus723206_production, 27_LVBus723208_production, 27_LVBus723210_production, 27_LVBus723211_production, 27_LVBus723212_production, 27_LVBus723213_production, 27_LVBus723214_production, 27_LVBus723216_production, 27_LVBus723217_production, 27_LVBus723218_production, 27_LVBus723219_production, 27_LVBus723220_consumption, 27_LVBus723220_production, 27_LVBus723221_production, 27_LVBus723222_production, 27_LVBus723223_production, 27_LVBus723225_consumption, 27_LVBus723225_production, 27_LVBus723227_production, 27_LVBus723228_production, 27_LVBus723229_production, 27_LVBus723231_production, 27_LVBus723232_production, 27_LVBus723233_production, 27_LVBus723234_production, 27_LVBus723235_production, 27_LVBus723236_production, 27_LVBus723237_production, 27_LVBus723239_production, 27_LVBus723241_consumption, 27_LVBus723241_production, 27_LVBus723242_consumption, 27_LVBus723242_production, 27_LVBus723243_consumption, 27_LVBus723243_production, 27_LVBus723244_consumption, 27_LVBus723244_production, 27_LVBus723245_production, 27_LVBus723246_consumption, 27_LVBus723246_production, 27_LVBus723247_production, 27_LVBus723249_production, 27_LVBus723250_production, 27_LVBus723251_production, 27_LVBus723252_production, 27_LVBus723253_production, 27_LVBus723255_consumption, 27_LVBus723255_production, 27_LVBus723256_production, 27_LVBus723258_production, 27_LVBus723259_production, 27_LVBus723261_production, 27_LVBus723263_consumption, 27_LVBus723263_production, 27_LVBus723264_production, 27_LVBus723265_production, 27_LVBus723266_production, 27_LVBus723268_production, 27_LVBus723269_production, 27_LVBus723270_production, 27_LVBus723271_production, 27_LVBus723272_production, 27_LVBus723273_production, 27_LVBus723275_production, 27_LVBus723277_consumption, 27_LVBus723277_production, 27_LVBus723278_consumption, 27_LVBus723278_production, 27_LVBus723279_production, 27_LVBus723280_production, 27_LVBus723282_consumption, 27_LVBus723282_production, 27_LVBus723283_production, 27_LVBus723284_production, 27_LVBus723285_production, 27_LVBus723287_consumption, 27_LVBus723287_production, 27_LVBus723288_production, 27_LVBus723289_production, 27_LVBus723290_production, 27_LVBus723291_production, 27_LVBus723292_production, 27_LVBus723293_production, 27_LVBus723294_production, 27_LVBus723295_consumption, 27_LVBus723295_production, 27_LVBus723296_production, 27_LVBus723297_production, 27_LVBus723299_production, 27_LVBus723300_production, 27_LVBus723301_production, 27_LVBus723302_production, 27_LVBus723303_production, 27_LVBus723304_production, 27_LVBus723305_production, 27_LVBus723306_production, 27_LVBus723307_production, 27_LVBus723308_production, 27_LVBus723310_production, 27_LVBus723311_production, 27_LVBus723313_production, 27_LVBus723314_production, 27_LVBus723315_production, 27_LVBus723316_production, 27_LVBus723317_consumption, 27_LVBus723317_production, 27_LVBus723318_consumption, 27_LVBus723318_production, 27_LVBus723319_consumption, 27_LVBus723319_production, 27_LVBus723320_production, 27_LVBus723321_production, 27_LVBus723322_consumption, 27_LVBus723322_production, 27_LVBus723323_consumption, 27_LVBus723323_production, 27_LVBus723324_consumption, 27_LVBus723324_production, 27_LVBus723325_production, 27_LVBus723326_production, 27_LVBus723327_production, 27_LVBus723328_production, 27_LVBus723329_production, 27_LVBus723330_production, 27_LVBus723331_production, 27_LVBus723332_production, 27_LVBus723333_production, 27_LVBus723334_production, 27_LVBus723335_production, 27_LVBus723336_production, 27_MVLV13552_consumption, 27_MVLV13552_production, 27_MVLV18845_production, 27_MVLV34028_production, 27_MVLV53263_production, 27_MVLV84302_production.

## 9. Data Quality Summary

**Total findings:** 186 (0 errors, 4 warnings, 182 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  384 of 592 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.71 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  385 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723135_consumption`  
  Load '27_LVBus723135_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723308_consumption`  
  Load '27_LVBus723308_consumption' has phase imbalance of 88.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723325_consumption`  
  Load '27_LVBus723325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723130_consumption`  
  Load '27_LVBus723130_consumption' has phase imbalance of 21.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723043_consumption`  
  Load '27_LVBus723043_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723010_consumption`  
  Load '27_LVBus723010_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723213_consumption`  
  Load '27_LVBus723213_consumption' has phase imbalance of 104.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723100_consumption`  
  Load '27_LVBus723100_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723106_consumption`  
  Load '27_LVBus723106_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723232_consumption`  
  Load '27_LVBus723232_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723079_consumption`  
  Load '27_LVBus723079_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723076_consumption`  
  Load '27_LVBus723076_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723056_consumption`  
  Load '27_LVBus723056_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723313_consumption`  
  Load '27_LVBus723313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723104_consumption`  
  Load '27_LVBus723104_consumption' has phase imbalance of 92.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723013_consumption`  
  Load '27_LVBus723013_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723328_consumption`  
  Load '27_LVBus723328_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723032_consumption`  
  Load '27_LVBus723032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723219_consumption`  
  Load '27_LVBus723219_consumption' has phase imbalance of 53.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723165_consumption`  
  Load '27_LVBus723165_consumption' has phase imbalance of 80.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723326_consumption`  
  Load '27_LVBus723326_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723315_consumption`  
  Load '27_LVBus723315_consumption' has phase imbalance of 139.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723134_consumption`  
  Load '27_LVBus723134_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723250_consumption`  
  Load '27_LVBus723250_consumption' has phase imbalance of 38.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723251_consumption`  
  Load '27_LVBus723251_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723334_consumption`  
  Load '27_LVBus723334_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723045_consumption`  
  Load '27_LVBus723045_consumption' has phase imbalance of 98.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723164_consumption`  
  Load '27_LVBus723164_consumption' has phase imbalance of 117.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723087_consumption`  
  Load '27_LVBus723087_consumption' has phase imbalance of 123.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723305_consumption`  
  Load '27_LVBus723305_consumption' has phase imbalance of 254.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723258_consumption`  
  Load '27_LVBus723258_consumption' has phase imbalance of 66.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723256_consumption`  
  Load '27_LVBus723256_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723161_consumption`  
  Load '27_LVBus723161_consumption' has phase imbalance of 41.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723055_consumption`  
  Load '27_LVBus723055_consumption' has phase imbalance of 220.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723148_consumption`  
  Load '27_LVBus723148_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723237_consumption`  
  Load '27_LVBus723237_consumption' has phase imbalance of 66.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723307_consumption`  
  Load '27_LVBus723307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723289_consumption`  
  Load '27_LVBus723289_consumption' has phase imbalance of 208.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723293_consumption`  
  Load '27_LVBus723293_consumption' has phase imbalance of 71.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723299_consumption`  
  Load '27_LVBus723299_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723235_consumption`  
  Load '27_LVBus723235_consumption' has phase imbalance of 23.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723302_consumption`  
  Load '27_LVBus723302_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723283_consumption`  
  Load '27_LVBus723283_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723033_consumption`  
  Load '27_LVBus723033_consumption' has phase imbalance of 21.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723329_consumption`  
  Load '27_LVBus723329_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723093_consumption`  
  Load '27_LVBus723093_consumption' has phase imbalance of 21.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723102_consumption`  
  Load '27_LVBus723102_consumption' has phase imbalance of 112.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723270_consumption`  
  Load '27_LVBus723270_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723194_consumption`  
  Load '27_LVBus723194_consumption' has phase imbalance of 248.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723234_consumption`  
  Load '27_LVBus723234_consumption' has phase imbalance of 95.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723064_consumption`  
  Load '27_LVBus723064_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723233_consumption`  
  Load '27_LVBus723233_consumption' has phase imbalance of 61.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723217_consumption`  
  Load '27_LVBus723217_consumption' has phase imbalance of 207.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723333_consumption`  
  Load '27_LVBus723333_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723199_consumption`  
  Load '27_LVBus723199_consumption' has phase imbalance of 22.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723036_consumption`  
  Load '27_LVBus723036_consumption' has phase imbalance of 242.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723249_consumption`  
  Load '27_LVBus723249_consumption' has phase imbalance of 30.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723303_consumption`  
  Load '27_LVBus723303_consumption' has phase imbalance of 155.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723275_consumption`  
  Load '27_LVBus723275_consumption' has phase imbalance of 83.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723116_consumption`  
  Load '27_LVBus723116_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723180_consumption`  
  Load '27_LVBus723180_consumption' has phase imbalance of 95.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723046_consumption`  
  Load '27_LVBus723046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723031_consumption`  
  Load '27_LVBus723031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723288_consumption`  
  Load '27_LVBus723288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723252_consumption`  
  Load '27_LVBus723252_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723063_consumption`  
  Load '27_LVBus723063_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus722992_consumption`  
  Load '27_LVBus722992_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723223_consumption`  
  Load '27_LVBus723223_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723285_consumption`  
  Load '27_LVBus723285_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723131_consumption`  
  Load '27_LVBus723131_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723040_consumption`  
  Load '27_LVBus723040_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723221_consumption`  
  Load '27_LVBus723221_consumption' has phase imbalance of 263.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723327_consumption`  
  Load '27_LVBus723327_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723028_consumption`  
  Load '27_LVBus723028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723290_consumption`  
  Load '27_LVBus723290_consumption' has phase imbalance of 134.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723140_consumption`  
  Load '27_LVBus723140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723024_consumption`  
  Load '27_LVBus723024_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723022_consumption`  
  Load '27_LVBus723022_consumption' has phase imbalance of 54.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723108_consumption`  
  Load '27_LVBus723108_consumption' has phase imbalance of 184.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723268_consumption`  
  Load '27_LVBus723268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723127_consumption`  
  Load '27_LVBus723127_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723332_consumption`  
  Load '27_LVBus723332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723212_consumption`  
  Load '27_LVBus723212_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723054_consumption`  
  Load '27_LVBus723054_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723264_consumption`  
  Load '27_LVBus723264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723071_consumption`  
  Load '27_LVBus723071_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723218_consumption`  
  Load '27_LVBus723218_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723314_consumption`  
  Load '27_LVBus723314_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723141_consumption`  
  Load '27_LVBus723141_consumption' has phase imbalance of 262.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723273_consumption`  
  Load '27_LVBus723273_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723211_consumption`  
  Load '27_LVBus723211_consumption' has phase imbalance of 35.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723280_consumption`  
  Load '27_LVBus723280_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723210_consumption`  
  Load '27_LVBus723210_consumption' has phase imbalance of 53.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723204_consumption`  
  Load '27_LVBus723204_consumption' has phase imbalance of 58.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723300_consumption`  
  Load '27_LVBus723300_consumption' has phase imbalance of 238.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723085_consumption`  
  Load '27_LVBus723085_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723027_consumption`  
  Load '27_LVBus723027_consumption' has phase imbalance of 118.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723272_consumption`  
  Load '27_LVBus723272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723044_consumption`  
  Load '27_LVBus723044_consumption' has phase imbalance of 186.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723292_consumption`  
  Load '27_LVBus723292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723115_consumption`  
  Load '27_LVBus723115_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723094_consumption`  
  Load '27_LVBus723094_consumption' has phase imbalance of 192.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723047_consumption`  
  Load '27_LVBus723047_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723335_consumption`  
  Load '27_LVBus723335_consumption' has phase imbalance of 182.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723012_consumption`  
  Load '27_LVBus723012_consumption' has phase imbalance of 24.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723142_consumption`  
  Load '27_LVBus723142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723311_consumption`  
  Load '27_LVBus723311_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723205_consumption`  
  Load '27_LVBus723205_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723034_consumption`  
  Load '27_LVBus723034_consumption' has phase imbalance of 256.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723245_consumption`  
  Load '27_LVBus723245_consumption' has phase imbalance of 198.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723321_consumption`  
  Load '27_LVBus723321_consumption' has phase imbalance of 102.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723049_consumption`  
  Load '27_LVBus723049_consumption' has phase imbalance of 92.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723229_consumption`  
  Load '27_LVBus723229_consumption' has phase imbalance of 98.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723316_consumption`  
  Load '27_LVBus723316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723236_consumption`  
  Load '27_LVBus723236_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723239_consumption`  
  Load '27_LVBus723239_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723109_consumption`  
  Load '27_LVBus723109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723214_consumption`  
  Load '27_LVBus723214_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723162_consumption`  
  Load '27_LVBus723162_consumption' has phase imbalance of 119.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723203_consumption`  
  Load '27_LVBus723203_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723265_consumption`  
  Load '27_LVBus723265_consumption' has phase imbalance of 82.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723089_consumption`  
  Load '27_LVBus723089_consumption' has phase imbalance of 104.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723331_consumption`  
  Load '27_LVBus723331_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723143_consumption`  
  Load '27_LVBus723143_consumption' has phase imbalance of 110.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723330_consumption`  
  Load '27_LVBus723330_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723301_consumption`  
  Load '27_LVBus723301_consumption' has phase imbalance of 239.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723037_consumption`  
  Load '27_LVBus723037_consumption' has phase imbalance of 95.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723107_consumption`  
  Load '27_LVBus723107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723114_consumption`  
  Load '27_LVBus723114_consumption' has phase imbalance of 173.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723279_consumption`  
  Load '27_LVBus723279_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723072_consumption`  
  Load '27_LVBus723072_consumption' has phase imbalance of 110.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723231_consumption`  
  Load '27_LVBus723231_consumption' has phase imbalance of 83.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus722988_consumption`  
  Load '27_LVBus722988_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723310_consumption`  
  Load '27_LVBus723310_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723320_consumption`  
  Load '27_LVBus723320_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723039_consumption`  
  Load '27_LVBus723039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus722985_consumption`  
  Load '27_LVBus722985_consumption' has phase imbalance of 134.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723261_consumption`  
  Load '27_LVBus723261_consumption' has phase imbalance of 112.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723110_consumption`  
  Load '27_LVBus723110_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723070_consumption`  
  Load '27_LVBus723070_consumption' has phase imbalance of 99.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723146_consumption`  
  Load '27_LVBus723146_consumption' has phase imbalance of 81.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723147_consumption`  
  Load '27_LVBus723147_consumption' has phase imbalance of 86.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723269_consumption`  
  Load '27_LVBus723269_consumption' has phase imbalance of 255.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723253_consumption`  
  Load '27_LVBus723253_consumption' has phase imbalance of 43.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723206_consumption`  
  Load '27_LVBus723206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus722998_consumption`  
  Load '27_LVBus722998_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723113_consumption`  
  Load '27_LVBus723113_consumption' has phase imbalance of 31.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus722981_consumption`  
  Load '27_LVBus722981_consumption' has phase imbalance of 105.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723082_consumption`  
  Load '27_LVBus723082_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723228_consumption`  
  Load '27_LVBus723228_consumption' has phase imbalance of 118.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723097_consumption`  
  Load '27_LVBus723097_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723294_consumption`  
  Load '27_LVBus723294_consumption' has phase imbalance of 90.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723297_consumption`  
  Load '27_LVBus723297_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723065_consumption`  
  Load '27_LVBus723065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723208_consumption`  
  Load '27_LVBus723208_consumption' has phase imbalance of 62.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723197_consumption`  
  Load '27_LVBus723197_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723296_consumption`  
  Load '27_LVBus723296_consumption' has phase imbalance of 255.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723038_consumption`  
  Load '27_LVBus723038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723284_consumption`  
  Load '27_LVBus723284_consumption' has phase imbalance of 39.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723092_consumption`  
  Load '27_LVBus723092_consumption' has phase imbalance of 78.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723096_consumption`  
  Load '27_LVBus723096_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723304_consumption`  
  Load '27_LVBus723304_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723306_consumption`  
  Load '27_LVBus723306_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723019_consumption`  
  Load '27_LVBus723019_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723336_consumption`  
  Load '27_LVBus723336_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723266_consumption`  
  Load '27_LVBus723266_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus723271_consumption`  
  Load '27_LVBus723271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 592 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_L.SAU' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  323 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  73 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 27_LVBus723028_consumption, 27_LVBus723031_consumption, 27_LVBus723032_consumption, 27_LVBus723034_consumption, 27_LVBus723036_consumption, 27_LVBus723038_consumption, 27_LVBus723039_consumption, 27_LVBus723040_consumption, 27_LVBus723043_consumption, 27_LVBus723044_consumption, 27_LVBus723046_consumption, 27_LVBus723047_consumption, 27_LVBus723055_consumption, 27_LVBus723063_consumption, 27_LVBus723065_consumption, 27_LVBus723094_consumption, 27_LVBus723096_consumption, 27_LVBus723097_consumption, 27_LVBus723100_consumption, 27_LVBus723106_consumption, 27_LVBus723107_consumption, 27_LVBus723108_consumption, 27_LVBus723109_consumption, 27_LVBus723110_consumption, 27_LVBus723115_consumption, 27_LVBus723116_consumption, 27_LVBus723127_consumption, 27_LVBus723131_consumption, 27_LVBus723134_consumption, 27_LVBus723135_consumption, 27_LVBus723140_consumption, 27_LVBus723141_consumption, 27_LVBus723142_consumption, 27_LVBus723194_consumption, 27_LVBus723205_consumption, 27_LVBus723206_consumption, 27_LVBus723221_consumption, 27_LVBus723245_consumption, 27_LVBus723264_consumption, 27_LVBus723268_consumption, 27_LVBus723269_consumption, 27_LVBus723271_consumption, 27_LVBus723272_consumption, 27_LVBus723283_consumption, 27_LVBus723285_consumption, 27_LVBus723288_consumption, 27_LVBus723289_consumption, 27_LVBus723292_consumption, 27_LVBus723296_consumption, 27_LVBus723297_consumption, 27_LVBus723299_consumption, 27_LVBus723300_consumption, 27_LVBus723301_consumption, 27_LVBus723303_consumption, 27_LVBus723305_consumption, 27_LVBus723306_consumption, 27_LVBus723307_consumption, 27_LVBus723311_consumption, 27_LVBus723313_consumption, 27_LVBus723314_consumption, 27_LVBus723316_consumption, 27_LVBus723320_consumption, 27_LVBus723325_consumption, 27_LVBus723326_consumption, 27_LVBus723327_consumption, 27_LVBus723329_consumption, 27_LVBus723330_consumption, 27_LVBus723331_consumption, 27_LVBus723332_consumption, 27_LVBus723333_consumption, 27_LVBus723334_consumption, 27_LVBus723335_consumption, 27_LVBus723336_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  296 group(s) of loads (592 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  385 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus722979_consumption, 27_LVBus722979_production, 27_LVBus722980_consumption, 27_LVBus722980_production, 27_LVBus722981_production, 27_LVBus722982_consumption, 27_LVBus722982_production, 27_LVBus722983_consumption, 27_LVBus722983_production, 27_LVBus722984_production, 27_LVBus722985_production, 27_LVBus722986_production, 27_LVBus722987_consumption, 27_LVBus722987_production, 27_LVBus722988_production, 27_LVBus722989_production, 27_LVBus722991_production, 27_LVBus722992_production, 27_LVBus722993_production, 27_LVBus722995_production, 27_LVBus722997_consumption, 27_LVBus722997_production, 27_LVBus722998_production, 27_LVBus722999_production, 27_LVBus723001_consumption, 27_LVBus723001_production, 27_LVBus723003_production, 27_LVBus723005_consumption, 27_LVBus723005_production, 27_LVBus723007_consumption, 27_LVBus723007_production, 27_LVBus723009_consumption, 27_LVBus723009_production, 27_LVBus723010_production, 27_LVBus723011_consumption, 27_LVBus723011_production, 27_LVBus723012_production, 27_LVBus723013_production, 27_LVBus723015_consumption, 27_LVBus723015_production, 27_LVBus723016_production, 27_LVBus723017_consumption, 27_LVBus723017_production, 27_LVBus723018_consumption, 27_LVBus723018_production, 27_LVBus723019_production, 27_LVBus723020_production, 27_LVBus723022_production, 27_LVBus723024_production, 27_LVBus723026_consumption, 27_LVBus723026_production, 27_LVBus723027_production, 27_LVBus723028_production, 27_LVBus723029_production, 27_LVBus723030_production, 27_LVBus723031_production, 27_LVBus723032_production, 27_LVBus723033_production, 27_LVBus723034_production, 27_LVBus723036_production, 27_LVBus723037_production, 27_LVBus723038_production, 27_LVBus723039_production, 27_LVBus723040_production, 27_LVBus723041_consumption, 27_LVBus723041_production, 27_LVBus723043_production, 27_LVBus723044_production, 27_LVBus723045_production, 27_LVBus723046_production, 27_LVBus723047_production, 27_LVBus723049_production, 27_LVBus723051_consumption, 27_LVBus723051_production, 27_LVBus723052_production, 27_LVBus723053_production, 27_LVBus723054_production, 27_LVBus723055_production, 27_LVBus723056_production, 27_LVBus723057_production, 27_LVBus723059_production, 27_LVBus723061_production, 27_LVBus723063_production, 27_LVBus723064_production, 27_LVBus723065_production, 27_LVBus723066_consumption, 27_LVBus723066_production, 27_LVBus723068_production, 27_LVBus723069_consumption, 27_LVBus723069_production, 27_LVBus723070_production, 27_LVBus723071_production, 27_LVBus723072_production, 27_LVBus723073_production, 27_LVBus723075_consumption, 27_LVBus723075_production, 27_LVBus723076_production, 27_LVBus723077_production, 27_LVBus723078_consumption, 27_LVBus723078_production, 27_LVBus723079_production, 27_LVBus723080_production, 27_LVBus723082_production, 27_LVBus723083_production, 27_LVBus723084_consumption, 27_LVBus723084_production, 27_LVBus723085_production, 27_LVBus723086_production, 27_LVBus723087_production, 27_LVBus723088_consumption, 27_LVBus723088_production, 27_LVBus723089_production, 27_LVBus723090_production, 27_LVBus723091_consumption, 27_LVBus723091_production, 27_LVBus723092_production, 27_LVBus723093_production, 27_LVBus723094_production, 27_LVBus723096_production, 27_LVBus723097_production, 27_LVBus723098_consumption, 27_LVBus723098_production, 27_LVBus723099_production, 27_LVBus723100_production, 27_LVBus723101_consumption, 27_LVBus723101_production, 27_LVBus723102_production, 27_LVBus723103_consumption, 27_LVBus723103_production, 27_LVBus723104_production, 27_LVBus723106_production, 27_LVBus723107_production, 27_LVBus723108_production, 27_LVBus723109_production, 27_LVBus723110_production, 27_LVBus723111_production, 27_LVBus723112_consumption, 27_LVBus723112_production, 27_LVBus723113_production, 27_LVBus723114_production, 27_LVBus723115_production, 27_LVBus723116_production, 27_LVBus723117_consumption, 27_LVBus723117_production, 27_LVBus723118_consumption, 27_LVBus723118_production, 27_LVBus723119_consumption, 27_LVBus723119_production, 27_LVBus723120_consumption, 27_LVBus723120_production, 27_LVBus723121_consumption, 27_LVBus723121_production, 27_LVBus723122_consumption, 27_LVBus723122_production, 27_LVBus723123_consumption, 27_LVBus723123_production, 27_LVBus723124_consumption, 27_LVBus723124_production, 27_LVBus723125_consumption, 27_LVBus723125_production, 27_LVBus723126_consumption, 27_LVBus723126_production, 27_LVBus723127_production, 27_LVBus723128_consumption, 27_LVBus723128_production, 27_LVBus723129_consumption, 27_LVBus723129_production, 27_LVBus723130_production, 27_LVBus723131_production, 27_LVBus723133_consumption, 27_LVBus723133_production, 27_LVBus723134_production, 27_LVBus723135_production, 27_LVBus723136_consumption, 27_LVBus723136_production, 27_LVBus723137_consumption, 27_LVBus723137_production, 27_LVBus723138_consumption, 27_LVBus723138_production, 27_LVBus723139_consumption, 27_LVBus723139_production, 27_LVBus723140_production, 27_LVBus723141_production, 27_LVBus723142_production, 27_LVBus723143_production, 27_LVBus723145_consumption, 27_LVBus723145_production, 27_LVBus723146_production, 27_LVBus723147_production, 27_LVBus723148_production, 27_LVBus723153_consumption, 27_LVBus723153_production, 27_LVBus723154_consumption, 27_LVBus723154_production, 27_LVBus723155_consumption, 27_LVBus723155_production, 27_LVBus723156_consumption, 27_LVBus723156_production, 27_LVBus723158_consumption, 27_LVBus723158_production, 27_LVBus723160_consumption, 27_LVBus723160_production, 27_LVBus723161_production, 27_LVBus723162_production, 27_LVBus723163_production, 27_LVBus723164_production, 27_LVBus723165_production, 27_LVBus723167_production, 27_LVBus723169_consumption, 27_LVBus723169_production, 27_LVBus723171_consumption, 27_LVBus723171_production, 27_LVBus723173_consumption, 27_LVBus723173_production, 27_LVBus723174_consumption, 27_LVBus723174_production, 27_LVBus723175_consumption, 27_LVBus723175_production, 27_LVBus723176_consumption, 27_LVBus723176_production, 27_LVBus723177_consumption, 27_LVBus723177_production, 27_LVBus723178_production, 27_LVBus723179_consumption, 27_LVBus723179_production, 27_LVBus723180_production, 27_LVBus723182_consumption, 27_LVBus723182_production, 27_LVBus723184_consumption, 27_LVBus723184_production, 27_LVBus723186_consumption, 27_LVBus723186_production, 27_LVBus723188_consumption, 27_LVBus723188_production, 27_LVBus723190_consumption, 27_LVBus723190_production, 27_LVBus723192_production, 27_LVBus723194_production, 27_LVBus723196_consumption, 27_LVBus723196_production, 27_LVBus723197_production, 27_LVBus723198_consumption, 27_LVBus723198_production, 27_LVBus723199_production, 27_LVBus723201_consumption, 27_LVBus723201_production, 27_LVBus723203_production, 27_LVBus723204_production, 27_LVBus723205_production, 27_LVBus723206_production, 27_LVBus723208_production, 27_LVBus723210_production, 27_LVBus723211_production, 27_LVBus723212_production, 27_LVBus723213_production, 27_LVBus723214_production, 27_LVBus723216_production, 27_LVBus723217_production, 27_LVBus723218_production, 27_LVBus723219_production, 27_LVBus723220_consumption, 27_LVBus723220_production, 27_LVBus723221_production, 27_LVBus723222_production, 27_LVBus723223_production, 27_LVBus723225_consumption, 27_LVBus723225_production, 27_LVBus723227_production, 27_LVBus723228_production, 27_LVBus723229_production, 27_LVBus723231_production, 27_LVBus723232_production, 27_LVBus723233_production, 27_LVBus723234_production, 27_LVBus723235_production, 27_LVBus723236_production, 27_LVBus723237_production, 27_LVBus723239_production, 27_LVBus723241_consumption, 27_LVBus723241_production, 27_LVBus723242_consumption, 27_LVBus723242_production, 27_LVBus723243_consumption, 27_LVBus723243_production, 27_LVBus723244_consumption, 27_LVBus723244_production, 27_LVBus723245_production, 27_LVBus723246_consumption, 27_LVBus723246_production, 27_LVBus723247_production, 27_LVBus723249_production, 27_LVBus723250_production, 27_LVBus723251_production, 27_LVBus723252_production, 27_LVBus723253_production, 27_LVBus723255_consumption, 27_LVBus723255_production, 27_LVBus723256_production, 27_LVBus723258_production, 27_LVBus723259_production, 27_LVBus723261_production, 27_LVBus723263_consumption, 27_LVBus723263_production, 27_LVBus723264_production, 27_LVBus723265_production, 27_LVBus723266_production, 27_LVBus723268_production, 27_LVBus723269_production, 27_LVBus723270_production, 27_LVBus723271_production, 27_LVBus723272_production, 27_LVBus723273_production, 27_LVBus723275_production, 27_LVBus723277_consumption, 27_LVBus723277_production, 27_LVBus723278_consumption, 27_LVBus723278_production, 27_LVBus723279_production, 27_LVBus723280_production, 27_LVBus723282_consumption, 27_LVBus723282_production, 27_LVBus723283_production, 27_LVBus723284_production, 27_LVBus723285_production, 27_LVBus723287_consumption, 27_LVBus723287_production, 27_LVBus723288_production, 27_LVBus723289_production, 27_LVBus723290_production, 27_LVBus723291_production, 27_LVBus723292_production, 27_LVBus723293_production, 27_LVBus723294_production, 27_LVBus723295_consumption, 27_LVBus723295_production, 27_LVBus723296_production, 27_LVBus723297_production, 27_LVBus723299_production, 27_LVBus723300_production, 27_LVBus723301_production, 27_LVBus723302_production, 27_LVBus723303_production, 27_LVBus723304_production, 27_LVBus723305_production, 27_LVBus723306_production, 27_LVBus723307_production, 27_LVBus723308_production, 27_LVBus723310_production, 27_LVBus723311_production, 27_LVBus723313_production, 27_LVBus723314_production, 27_LVBus723315_production, 27_LVBus723316_production, 27_LVBus723317_consumption, 27_LVBus723317_production, 27_LVBus723318_consumption, 27_LVBus723318_production, 27_LVBus723319_consumption, 27_LVBus723319_production, 27_LVBus723320_production, 27_LVBus723321_production, 27_LVBus723322_consumption, 27_LVBus723322_production, 27_LVBus723323_consumption, 27_LVBus723323_production, 27_LVBus723324_consumption, 27_LVBus723324_production, 27_LVBus723325_production, 27_LVBus723326_production, 27_LVBus723327_production, 27_LVBus723328_production, 27_LVBus723329_production, 27_LVBus723330_production, 27_LVBus723331_production, 27_LVBus723332_production, 27_LVBus723333_production, 27_LVBus723334_production, 27_LVBus723335_production, 27_LVBus723336_production, 27_MVLV13552_consumption, 27_MVLV13552_production, 27_MVLV18845_production, 27_MVLV34028_production, 27_MVLV53263_production, 27_MVLV84302_production.

