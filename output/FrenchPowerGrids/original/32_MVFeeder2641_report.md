# BMOPF Network Summary: 32_MVFeeder2641

**Generated:** 2026-10-01 23:34:08  
**Findings:** 0 errors · 6 warnings · 280 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 410 |  |
| line | 389 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 730 | 2.21 MW, 663.0 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 20 |  |
| switch | 0 |  |
| transformer | 20 | Dyn11×20 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 29 | 28 | 8 | 0 |
| LV_236V | 236.0 V | 381 | 361 | 722 | 0 |

**Transformer transitions:**

- `32_MVLV70815_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV36285_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV62913_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV50028_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV29924_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV70861_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV12587_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV64612_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV39096_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV13051_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV73936_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV50173_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV54511_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV60097_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV22872_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV22876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV70814_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV28242_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV38693_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV36284_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 136 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 410 | 1 | 409 | 0 | 0 | 0 |
| Tier LV_236V | 381 | 20 | 361 | 0 | 0 | 0 |
| Tier MV_11.8kV | 29 | 1 | 28 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 20; skipped invalid branches: 0.

Galvanic zones: 21; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_MVBus35731 | MV_11.8kV | 29 | 0 | 0 | 20 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1611 declared bus terminals; 1528 mapped line/closed-switch conductor edges; 83 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 26500.0 | 2.403 | 2190 |
| q_nom | 0.0 | 7950.0 | 2.403 | 2190 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.641 | 1060.0 | 1.279 | 389 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.543 | 20 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 444 of 730 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974210_consumption' has phase imbalance of 115.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974173_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974253_consumption' has phase imbalance of 147.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974335_consumption' has phase imbalance of 29.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974265_consumption' has phase imbalance of 75.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974230_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974394_consumption' has phase imbalance of 50.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974108_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1182507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1106531_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1106533_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974199_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1107332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974349_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974219_consumption' has phase imbalance of 126.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974407_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974356_consumption' has phase imbalance of 101.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974351_consumption' has phase imbalance of 20.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974119_consumption' has phase imbalance of 193.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974294_consumption' has phase imbalance of 127.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974403_consumption' has phase imbalance of 37.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974405_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974046_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974116_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974252_consumption' has phase imbalance of 124.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974240_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974068_consumption' has phase imbalance of 77.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974215_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974161_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974073_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974323_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974082_consumption' has phase imbalance of 138.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109361_consumption' has phase imbalance of 254.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974404_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974267_consumption' has phase imbalance of 60.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974388_consumption' has phase imbalance of 126.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1107333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974322_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974357_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974275_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974080_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974102_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974338_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1106521_consumption' has phase imbalance of 140.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974100_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974409_consumption' has phase imbalance of 125.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974311_consumption' has phase imbalance of 145.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974257_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109357_consumption' has phase imbalance of 55.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974393_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974066_consumption' has phase imbalance of 53.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974337_consumption' has phase imbalance of 108.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974234_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974127_consumption' has phase imbalance of 141.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974038_consumption' has phase imbalance of 242.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974281_consumption' has phase imbalance of 94.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974241_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974179_consumption' has phase imbalance of 25.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974342_consumption' has phase imbalance of 191.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1108125_consumption' has phase imbalance of 84.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974143_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974319_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974366_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974170_consumption' has phase imbalance of 114.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974247_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974358_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974096_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974051_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130040_consumption' has phase imbalance of 116.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974266_consumption' has phase imbalance of 43.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974125_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974190_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974255_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974176_consumption' has phase imbalance of 224.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974406_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974067_consumption' has phase imbalance of 232.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974182_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974035_consumption' has phase imbalance of 138.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974211_consumption' has phase imbalance of 41.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974162_consumption' has phase imbalance of 20.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974314_consumption' has phase imbalance of 95.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974354_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974049_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974141_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974383_consumption' has phase imbalance of 69.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974047_consumption' has phase imbalance of 208.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974081_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974142_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974263_consumption' has phase imbalance of 90.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974117_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974320_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974305_consumption' has phase imbalance of 54.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974256_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974381_consumption' has phase imbalance of 270.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974216_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974136_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974251_consumption' has phase imbalance of 142.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974377_consumption' has phase imbalance of 144.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974033_consumption' has phase imbalance of 230.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974336_consumption' has phase imbalance of 141.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1107334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974221_consumption' has phase imbalance of 164.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974111_consumption' has phase imbalance of 116.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130458_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974196_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974283_consumption' has phase imbalance of 40.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1106532_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974054_consumption' has phase imbalance of 38.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105904_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974175_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974037_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974370_consumption' has phase imbalance of 146.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974375_consumption' has phase imbalance of 41.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974115_consumption' has phase imbalance of 77.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974101_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974157_consumption' has phase imbalance of 31.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974369_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974372_consumption' has phase imbalance of 85.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974232_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974250_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105846_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1107336_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974217_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974368_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974376_consumption' has phase imbalance of 67.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974107_consumption' has phase imbalance of 277.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974128_consumption' has phase imbalance of 122.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974158_consumption' has phase imbalance of 278.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130461_consumption' has phase imbalance of 89.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974301_consumption' has phase imbalance of 37.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109360_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974331_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974264_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130460_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974137_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974159_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974110_consumption' has phase imbalance of 73.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974079_consumption' has phase imbalance of 71.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974135_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974092_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1107020_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974212_consumption' has phase imbalance of 224.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974126_consumption' has phase imbalance of 221.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974198_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974386_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109359_consumption' has phase imbalance of 135.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974150_consumption' has phase imbalance of 91.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974332_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974296_consumption' has phase imbalance of 39.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974174_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974224_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974352_consumption' has phase imbalance of 241.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109353_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974055_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974036_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974392_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974160_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974387_consumption' has phase imbalance of 86.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974246_consumption' has phase imbalance of 88.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974391_consumption' has phase imbalance of 36.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974382_consumption' has phase imbalance of 130.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974130_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974147_consumption' has phase imbalance of 95.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974034_consumption' has phase imbalance of 102.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974268_consumption' has phase imbalance of 107.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109358_consumption' has phase imbalance of 242.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1107019_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105903_consumption' has phase imbalance of 229.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1176262_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105473_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105905_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974295_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974309_consumption' has phase imbalance of 112.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974069_consumption' has phase imbalance of 127.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974312_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974237_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974144_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974277_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974398_consumption' has phase imbalance of 233.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974231_consumption' has phase imbalance of 80.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974120_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1105472_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974163_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974124_consumption' has phase imbalance of 239.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130459_consumption' has phase imbalance of 108.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1106520_consumption' has phase imbalance of 28.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1107335_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974321_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974371_consumption' has phase imbalance of 29.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974339_consumption' has phase imbalance of 240.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974262_consumption' has phase imbalance of 276.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974360_consumption' has phase imbalance of 95.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974123_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974380_consumption' has phase imbalance of 264.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974086_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974297_consumption' has phase imbalance of 92.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974118_consumption' has phase imbalance of 28.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974088_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974346_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974353_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974364_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974334_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974400_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974367_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974359_consumption' has phase imbalance of 210.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974276_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974223_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974214_consumption' has phase imbalance of 148.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974245_consumption' has phase imbalance of 207.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109356_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974408_consumption' has phase imbalance of 257.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974040_consumption' has phase imbalance of 211.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974274_consumption' has phase imbalance of 100.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974106_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974200_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974324_consumption' has phase imbalance of 189.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974186_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974220_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974185_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974177_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974341_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974308_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974105_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974304_consumption' has phase imbalance of 54.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974183_consumption' has phase imbalance of 61.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974239_consumption' has phase imbalance of 94.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1109354_consumption' has phase imbalance of 46.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974385_consumption' has phase imbalance of 80.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130463_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974333_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974191_consumption' has phase imbalance of 82.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130462_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974099_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974361_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974122_consumption' has phase imbalance of 99.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974310_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974399_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus974243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1108124_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 730 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus1127300' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus974226' has balanced aggregate load across 3 phase(s) (max spread 1.85%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.21 MW |
| Total load Q | 663.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV70815_Transformer | 275.0 kVA | 41.0% |
| 32_MVLV36285_Transformer | 275.0 kVA | 57.3% |
| 32_MVLV62913_Transformer | 440.0 kVA | 37.7% |
| 32_MVLV50028_Transformer | 176.0 kVA | 28.2% |
| 32_MVLV29924_Transformer | 110.0 kVA | 11.6% |
| 32_MVLV70861_Transformer | 176.0 kVA | 94.0% ⚠ |
| 32_MVLV12587_Transformer | 275.0 kVA | 27.3% |
| 32_MVLV64612_Transformer | 275.0 kVA | 67.5% |
| 32_MVLV39096_Transformer | 275.0 kVA | 34.4% |
| 32_MVLV13051_Transformer | 440.0 kVA | 48.3% |
| 32_MVLV73936_Transformer | 176.0 kVA | 53.8% |
| 32_MVLV50173_Transformer | 176.0 kVA | 32.4% |
| 32_MVLV54511_Transformer | 176.0 kVA | 58.6% |
| 32_MVLV60097_Transformer | 440.0 kVA | 36.6% |
| 32_MVLV22872_Transformer | 440.0 kVA | 38.3% |
| 32_MVLV22876_Transformer | 110.0 kVA | 43.6% |
| 32_MVLV70814_Transformer | 176.0 kVA | 50.2% |
| 32_MVLV28242_Transformer | 176.0 kVA | 47.1% |
| 32_MVLV38693_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV36284_Transformer | 693.0 kVA | 39.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.21 MW).
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '32_MVLV70861_Transformer' is at 94.0% utilisation at nominal load — little OPF headroom.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 410 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 410 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 29 |
| LV_236V | 4-wire | 381 / 381 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 381 |
| Neutral branches | 361 |
| Grounding points | 20 |
| Neutral sections | 20 |
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
| 11.78 kV | 29 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 21 |
| Islands without voltage reference | 0 |
| Line impedance spread | 702.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 381 / 29 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 445 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 445 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1105378_consumption, 32_LVBus1105378_production, 32_LVBus1105383_consumption, 32_LVBus1105383_production, 32_LVBus1105384_consumption, 32_LVBus1105384_production, 32_LVBus1105472_production, 32_LVBus1105473_production, 32_LVBus1105845_production, 32_LVBus1105846_production, 32_LVBus1105902_production, 32_LVBus1105903_production, 32_LVBus1105904_production, 32_LVBus1105905_production, 32_LVBus1106520_production, 32_LVBus1106521_production, 32_LVBus1106522_consumption, 32_LVBus1106522_production, 32_LVBus1106531_production, 32_LVBus1106532_production, 32_LVBus1106533_production, 32_LVBus1107019_production, 32_LVBus1107020_production, 32_LVBus1107332_production, 32_LVBus1107333_production, 32_LVBus1107334_production, 32_LVBus1107335_production, 32_LVBus1107336_production, 32_LVBus1108124_production, 32_LVBus1108125_production, 32_LVBus1109353_production, 32_LVBus1109354_production, 32_LVBus1109355_production, 32_LVBus1109356_production, 32_LVBus1109357_production, 32_LVBus1109358_production, 32_LVBus1109359_production, 32_LVBus1109360_production, 32_LVBus1109361_production, 32_LVBus1127300_production, 32_LVBus1127301_consumption, 32_LVBus1127301_production, 32_LVBus1130039_production, 32_LVBus1130040_production, 32_LVBus1130457_consumption, 32_LVBus1130457_production, 32_LVBus1130458_production, 32_LVBus1130459_production, 32_LVBus1130460_production, 32_LVBus1130461_production, 32_LVBus1130462_production, 32_LVBus1130463_production, 32_LVBus1130464_production, 32_LVBus1151850_consumption, 32_LVBus1151850_production, 32_LVBus1176262_production, 32_LVBus1178323_consumption, 32_LVBus1178323_production, 32_LVBus1182506_consumption, 32_LVBus1182506_production, 32_LVBus1182507_production, 32_LVBus974021_consumption, 32_LVBus974021_production, 32_LVBus974023_consumption, 32_LVBus974023_production, 32_LVBus974025_consumption, 32_LVBus974025_production, 32_LVBus974027_consumption, 32_LVBus974027_production, 32_LVBus974029_consumption, 32_LVBus974029_production, 32_LVBus974030_production, 32_LVBus974031_consumption, 32_LVBus974031_production, 32_LVBus974032_consumption, 32_LVBus974032_production, 32_LVBus974033_production, 32_LVBus974034_production, 32_LVBus974035_production, 32_LVBus974036_production, 32_LVBus974037_production, 32_LVBus974038_production, 32_LVBus974039_consumption, 32_LVBus974039_production, 32_LVBus974040_production, 32_LVBus974041_consumption, 32_LVBus974041_production, 32_LVBus974042_consumption, 32_LVBus974042_production, 32_LVBus974043_consumption, 32_LVBus974043_production, 32_LVBus974044_consumption, 32_LVBus974044_production, 32_LVBus974045_consumption, 32_LVBus974045_production, 32_LVBus974046_production, 32_LVBus974047_production, 32_LVBus974048_consumption, 32_LVBus974048_production, 32_LVBus974049_production, 32_LVBus974050_production, 32_LVBus974051_production, 32_LVBus974052_production, 32_LVBus974054_production, 32_LVBus974055_production, 32_LVBus974057_consumption, 32_LVBus974057_production, 32_LVBus974059_production, 32_LVBus974061_consumption, 32_LVBus974061_production, 32_LVBus974062_consumption, 32_LVBus974062_production, 32_LVBus974063_consumption, 32_LVBus974063_production, 32_LVBus974065_production, 32_LVBus974066_production, 32_LVBus974067_production, 32_LVBus974068_production, 32_LVBus974069_production, 32_LVBus974070_consumption, 32_LVBus974070_production, 32_LVBus974072_consumption, 32_LVBus974072_production, 32_LVBus974073_production, 32_LVBus974075_production, 32_LVBus974079_production, 32_LVBus974080_production, 32_LVBus974081_production, 32_LVBus974082_production, 32_LVBus974083_production, 32_LVBus974085_consumption, 32_LVBus974085_production, 32_LVBus974086_production, 32_LVBus974087_consumption, 32_LVBus974087_production, 32_LVBus974088_production, 32_LVBus974090_consumption, 32_LVBus974090_production, 32_LVBus974091_production, 32_LVBus974092_production, 32_LVBus974094_production, 32_LVBus974096_production, 32_LVBus974098_production, 32_LVBus974099_production, 32_LVBus974100_production, 32_LVBus974101_production, 32_LVBus974102_production, 32_LVBus974105_production, 32_LVBus974106_production, 32_LVBus974107_production, 32_LVBus974108_production, 32_LVBus974109_production, 32_LVBus974110_production, 32_LVBus974111_production, 32_LVBus974115_production, 32_LVBus974116_production, 32_LVBus974117_production, 32_LVBus974118_production, 32_LVBus974119_production, 32_LVBus974120_production, 32_LVBus974122_production, 32_LVBus974123_production, 32_LVBus974124_production, 32_LVBus974125_production, 32_LVBus974126_production, 32_LVBus974127_production, 32_LVBus974128_production, 32_LVBus974130_production, 32_LVBus974132_consumption, 32_LVBus974132_production, 32_LVBus974134_consumption, 32_LVBus974134_production, 32_LVBus974135_production, 32_LVBus974136_production, 32_LVBus974137_production, 32_LVBus974138_production, 32_LVBus974139_production, 32_LVBus974140_production, 32_LVBus974141_production, 32_LVBus974142_production, 32_LVBus974143_production, 32_LVBus974144_production, 32_LVBus974145_consumption, 32_LVBus974145_production, 32_LVBus974146_consumption, 32_LVBus974146_production, 32_LVBus974147_production, 32_LVBus974148_consumption, 32_LVBus974148_production, 32_LVBus974149_production, 32_LVBus974150_production, 32_LVBus974152_consumption, 32_LVBus974152_production, 32_LVBus974153_consumption, 32_LVBus974153_production, 32_LVBus974154_consumption, 32_LVBus974154_production, 32_LVBus974155_production, 32_LVBus974157_production, 32_LVBus974158_production, 32_LVBus974159_production, 32_LVBus974160_production, 32_LVBus974161_production, 32_LVBus974162_production, 32_LVBus974163_production, 32_LVBus974165_consumption, 32_LVBus974165_production, 32_LVBus974167_production, 32_LVBus974169_consumption, 32_LVBus974169_production, 32_LVBus974170_production, 32_LVBus974173_production, 32_LVBus974174_production, 32_LVBus974175_production, 32_LVBus974176_production, 32_LVBus974177_production, 32_LVBus974178_consumption, 32_LVBus974178_production, 32_LVBus974179_production, 32_LVBus974181_production, 32_LVBus974182_production, 32_LVBus974183_production, 32_LVBus974185_production, 32_LVBus974186_production, 32_LVBus974188_production, 32_LVBus974189_production, 32_LVBus974190_production, 32_LVBus974191_production, 32_LVBus974192_production, 32_LVBus974194_consumption, 32_LVBus974194_production, 32_LVBus974195_consumption, 32_LVBus974195_production, 32_LVBus974196_production, 32_LVBus974197_consumption, 32_LVBus974197_production, 32_LVBus974198_production, 32_LVBus974199_production, 32_LVBus974200_production, 32_LVBus974202_consumption, 32_LVBus974202_production, 32_LVBus974204_consumption, 32_LVBus974204_production, 32_LVBus974206_consumption, 32_LVBus974206_production, 32_LVBus974208_consumption, 32_LVBus974208_production, 32_LVBus974210_production, 32_LVBus974211_production, 32_LVBus974212_production, 32_LVBus974214_production, 32_LVBus974215_production, 32_LVBus974216_production, 32_LVBus974217_production, 32_LVBus974219_production, 32_LVBus974220_production, 32_LVBus974221_production, 32_LVBus974223_production, 32_LVBus974224_production, 32_LVBus974226_production, 32_LVBus974228_production, 32_LVBus974230_production, 32_LVBus974231_production, 32_LVBus974232_production, 32_LVBus974233_consumption, 32_LVBus974233_production, 32_LVBus974234_production, 32_LVBus974235_production, 32_LVBus974236_consumption, 32_LVBus974236_production, 32_LVBus974237_production, 32_LVBus974239_production, 32_LVBus974240_production, 32_LVBus974241_production, 32_LVBus974243_production, 32_LVBus974245_production, 32_LVBus974246_production, 32_LVBus974247_production, 32_LVBus974248_production, 32_LVBus974250_production, 32_LVBus974251_production, 32_LVBus974252_production, 32_LVBus974253_production, 32_LVBus974255_production, 32_LVBus974256_production, 32_LVBus974257_production, 32_LVBus974258_production, 32_LVBus974259_production, 32_LVBus974261_consumption, 32_LVBus974261_production, 32_LVBus974262_production, 32_LVBus974263_production, 32_LVBus974264_production, 32_LVBus974265_production, 32_LVBus974266_production, 32_LVBus974267_production, 32_LVBus974268_production, 32_LVBus974270_consumption, 32_LVBus974270_production, 32_LVBus974271_consumption, 32_LVBus974271_production, 32_LVBus974272_consumption, 32_LVBus974272_production, 32_LVBus974274_production, 32_LVBus974275_production, 32_LVBus974276_production, 32_LVBus974277_production, 32_LVBus974279_production, 32_LVBus974281_production, 32_LVBus974282_consumption, 32_LVBus974282_production, 32_LVBus974283_production, 32_LVBus974285_production, 32_LVBus974286_production, 32_LVBus974287_consumption, 32_LVBus974287_production, 32_LVBus974288_consumption, 32_LVBus974288_production, 32_LVBus974289_production, 32_LVBus974291_consumption, 32_LVBus974291_production, 32_LVBus974292_production, 32_LVBus974293_production, 32_LVBus974294_production, 32_LVBus974295_production, 32_LVBus974296_production, 32_LVBus974297_production, 32_LVBus974298_production, 32_LVBus974299_production, 32_LVBus974301_production, 32_LVBus974302_consumption, 32_LVBus974302_production, 32_LVBus974304_production, 32_LVBus974305_production, 32_LVBus974307_consumption, 32_LVBus974307_production, 32_LVBus974308_production, 32_LVBus974309_production, 32_LVBus974310_production, 32_LVBus974311_production, 32_LVBus974312_production, 32_LVBus974313_consumption, 32_LVBus974313_production, 32_LVBus974314_production, 32_LVBus974316_production, 32_LVBus974317_consumption, 32_LVBus974317_production, 32_LVBus974319_production, 32_LVBus974320_production, 32_LVBus974321_production, 32_LVBus974322_production, 32_LVBus974323_production, 32_LVBus974324_production, 32_LVBus974326_production, 32_LVBus974328_production, 32_LVBus974330_consumption, 32_LVBus974330_production, 32_LVBus974331_production, 32_LVBus974332_production, 32_LVBus974333_production, 32_LVBus974334_production, 32_LVBus974335_production, 32_LVBus974336_production, 32_LVBus974337_production, 32_LVBus974338_production, 32_LVBus974339_production, 32_LVBus974341_production, 32_LVBus974342_production, 32_LVBus974343_consumption, 32_LVBus974343_production, 32_LVBus974346_production, 32_LVBus974347_consumption, 32_LVBus974347_production, 32_LVBus974348_consumption, 32_LVBus974348_production, 32_LVBus974349_production, 32_LVBus974351_production, 32_LVBus974352_production, 32_LVBus974353_production, 32_LVBus974354_production, 32_LVBus974356_production, 32_LVBus974357_production, 32_LVBus974358_production, 32_LVBus974359_production, 32_LVBus974360_production, 32_LVBus974361_production, 32_LVBus974362_consumption, 32_LVBus974362_production, 32_LVBus974363_consumption, 32_LVBus974363_production, 32_LVBus974364_production, 32_LVBus974366_production, 32_LVBus974367_production, 32_LVBus974368_production, 32_LVBus974369_production, 32_LVBus974370_production, 32_LVBus974371_production, 32_LVBus974372_production, 32_LVBus974374_consumption, 32_LVBus974374_production, 32_LVBus974375_production, 32_LVBus974376_production, 32_LVBus974377_production, 32_LVBus974379_production, 32_LVBus974380_production, 32_LVBus974381_production, 32_LVBus974382_production, 32_LVBus974383_production, 32_LVBus974385_production, 32_LVBus974386_production, 32_LVBus974387_production, 32_LVBus974388_production, 32_LVBus974390_consumption, 32_LVBus974390_production, 32_LVBus974391_production, 32_LVBus974392_production, 32_LVBus974393_production, 32_LVBus974394_production, 32_LVBus974395_consumption, 32_LVBus974395_production, 32_LVBus974397_production, 32_LVBus974398_production, 32_LVBus974399_production, 32_LVBus974400_production, 32_LVBus974401_consumption, 32_LVBus974401_production, 32_LVBus974403_production, 32_LVBus974404_production, 32_LVBus974405_production, 32_LVBus974406_production, 32_LVBus974407_production, 32_LVBus974408_production, 32_LVBus974409_production, 32_LVBus974411_consumption, 32_LVBus974411_production, 32_LVBus974413_consumption, 32_LVBus974413_production, 32_MVLV18773_consumption, 32_MVLV18773_production, 32_MVLV33764_consumption, 32_MVLV33764_production, 32_MVLV50023_consumption, 32_MVLV50023_production, 32_MVLV74328_consumption, 32_MVLV74328_production.

## 9. Data Quality Summary

**Total findings:** 286 (0 errors, 6 warnings, 280 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  444 of 730 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.21 MW).
- **[W.OPS.XFMR_OVERLOADED]** `32_MVLV70861_Transformer`  
  Transformer '32_MVLV70861_Transformer' is at 94.0% utilisation at nominal load — little OPF headroom.
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  445 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974210_consumption`  
  Load '32_LVBus974210_consumption' has phase imbalance of 115.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974173_consumption`  
  Load '32_LVBus974173_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974253_consumption`  
  Load '32_LVBus974253_consumption' has phase imbalance of 147.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974335_consumption`  
  Load '32_LVBus974335_consumption' has phase imbalance of 29.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974265_consumption`  
  Load '32_LVBus974265_consumption' has phase imbalance of 75.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974230_consumption`  
  Load '32_LVBus974230_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974394_consumption`  
  Load '32_LVBus974394_consumption' has phase imbalance of 50.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974108_consumption`  
  Load '32_LVBus974108_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105902_consumption`  
  Load '32_LVBus1105902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1182507_consumption`  
  Load '32_LVBus1182507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1106531_consumption`  
  Load '32_LVBus1106531_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1106533_consumption`  
  Load '32_LVBus1106533_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974199_consumption`  
  Load '32_LVBus974199_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1107332_consumption`  
  Load '32_LVBus1107332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974349_consumption`  
  Load '32_LVBus974349_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974326_consumption`  
  Load '32_LVBus974326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974219_consumption`  
  Load '32_LVBus974219_consumption' has phase imbalance of 126.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974407_consumption`  
  Load '32_LVBus974407_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974356_consumption`  
  Load '32_LVBus974356_consumption' has phase imbalance of 101.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974351_consumption`  
  Load '32_LVBus974351_consumption' has phase imbalance of 20.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974119_consumption`  
  Load '32_LVBus974119_consumption' has phase imbalance of 193.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974294_consumption`  
  Load '32_LVBus974294_consumption' has phase imbalance of 127.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974403_consumption`  
  Load '32_LVBus974403_consumption' has phase imbalance of 37.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974405_consumption`  
  Load '32_LVBus974405_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974046_consumption`  
  Load '32_LVBus974046_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974116_consumption`  
  Load '32_LVBus974116_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974252_consumption`  
  Load '32_LVBus974252_consumption' has phase imbalance of 124.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974328_consumption`  
  Load '32_LVBus974328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974240_consumption`  
  Load '32_LVBus974240_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974068_consumption`  
  Load '32_LVBus974068_consumption' has phase imbalance of 77.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974181_consumption`  
  Load '32_LVBus974181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974215_consumption`  
  Load '32_LVBus974215_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974161_consumption`  
  Load '32_LVBus974161_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974073_consumption`  
  Load '32_LVBus974073_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974323_consumption`  
  Load '32_LVBus974323_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974082_consumption`  
  Load '32_LVBus974082_consumption' has phase imbalance of 138.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109361_consumption`  
  Load '32_LVBus1109361_consumption' has phase imbalance of 254.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974404_consumption`  
  Load '32_LVBus974404_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974267_consumption`  
  Load '32_LVBus974267_consumption' has phase imbalance of 60.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974388_consumption`  
  Load '32_LVBus974388_consumption' has phase imbalance of 126.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1107333_consumption`  
  Load '32_LVBus1107333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974322_consumption`  
  Load '32_LVBus974322_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974357_consumption`  
  Load '32_LVBus974357_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974298_consumption`  
  Load '32_LVBus974298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974149_consumption`  
  Load '32_LVBus974149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974275_consumption`  
  Load '32_LVBus974275_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974080_consumption`  
  Load '32_LVBus974080_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974102_consumption`  
  Load '32_LVBus974102_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974338_consumption`  
  Load '32_LVBus974338_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1106521_consumption`  
  Load '32_LVBus1106521_consumption' has phase imbalance of 140.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974100_consumption`  
  Load '32_LVBus974100_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974409_consumption`  
  Load '32_LVBus974409_consumption' has phase imbalance of 125.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974311_consumption`  
  Load '32_LVBus974311_consumption' has phase imbalance of 145.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974257_consumption`  
  Load '32_LVBus974257_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109357_consumption`  
  Load '32_LVBus1109357_consumption' has phase imbalance of 55.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974393_consumption`  
  Load '32_LVBus974393_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974066_consumption`  
  Load '32_LVBus974066_consumption' has phase imbalance of 53.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974052_consumption`  
  Load '32_LVBus974052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974337_consumption`  
  Load '32_LVBus974337_consumption' has phase imbalance of 108.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974234_consumption`  
  Load '32_LVBus974234_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974127_consumption`  
  Load '32_LVBus974127_consumption' has phase imbalance of 141.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974038_consumption`  
  Load '32_LVBus974038_consumption' has phase imbalance of 242.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974281_consumption`  
  Load '32_LVBus974281_consumption' has phase imbalance of 94.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974241_consumption`  
  Load '32_LVBus974241_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974179_consumption`  
  Load '32_LVBus974179_consumption' has phase imbalance of 25.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974342_consumption`  
  Load '32_LVBus974342_consumption' has phase imbalance of 191.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1108125_consumption`  
  Load '32_LVBus1108125_consumption' has phase imbalance of 84.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974143_consumption`  
  Load '32_LVBus974143_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974319_consumption`  
  Load '32_LVBus974319_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974050_consumption`  
  Load '32_LVBus974050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974366_consumption`  
  Load '32_LVBus974366_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974170_consumption`  
  Load '32_LVBus974170_consumption' has phase imbalance of 114.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974247_consumption`  
  Load '32_LVBus974247_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974358_consumption`  
  Load '32_LVBus974358_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974096_consumption`  
  Load '32_LVBus974096_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974051_consumption`  
  Load '32_LVBus974051_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130040_consumption`  
  Load '32_LVBus1130040_consumption' has phase imbalance of 116.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974266_consumption`  
  Load '32_LVBus974266_consumption' has phase imbalance of 43.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974125_consumption`  
  Load '32_LVBus974125_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974190_consumption`  
  Load '32_LVBus974190_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974255_consumption`  
  Load '32_LVBus974255_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974176_consumption`  
  Load '32_LVBus974176_consumption' has phase imbalance of 224.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974406_consumption`  
  Load '32_LVBus974406_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974067_consumption`  
  Load '32_LVBus974067_consumption' has phase imbalance of 232.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974182_consumption`  
  Load '32_LVBus974182_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974379_consumption`  
  Load '32_LVBus974379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974035_consumption`  
  Load '32_LVBus974035_consumption' has phase imbalance of 138.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974211_consumption`  
  Load '32_LVBus974211_consumption' has phase imbalance of 41.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974162_consumption`  
  Load '32_LVBus974162_consumption' has phase imbalance of 20.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974314_consumption`  
  Load '32_LVBus974314_consumption' has phase imbalance of 95.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974354_consumption`  
  Load '32_LVBus974354_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974049_consumption`  
  Load '32_LVBus974049_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974141_consumption`  
  Load '32_LVBus974141_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974383_consumption`  
  Load '32_LVBus974383_consumption' has phase imbalance of 69.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974047_consumption`  
  Load '32_LVBus974047_consumption' has phase imbalance of 208.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974081_consumption`  
  Load '32_LVBus974081_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974142_consumption`  
  Load '32_LVBus974142_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974263_consumption`  
  Load '32_LVBus974263_consumption' has phase imbalance of 90.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974117_consumption`  
  Load '32_LVBus974117_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974320_consumption`  
  Load '32_LVBus974320_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974305_consumption`  
  Load '32_LVBus974305_consumption' has phase imbalance of 54.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974256_consumption`  
  Load '32_LVBus974256_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974381_consumption`  
  Load '32_LVBus974381_consumption' has phase imbalance of 270.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974139_consumption`  
  Load '32_LVBus974139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974216_consumption`  
  Load '32_LVBus974216_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974136_consumption`  
  Load '32_LVBus974136_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974251_consumption`  
  Load '32_LVBus974251_consumption' has phase imbalance of 142.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974377_consumption`  
  Load '32_LVBus974377_consumption' has phase imbalance of 144.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974033_consumption`  
  Load '32_LVBus974033_consumption' has phase imbalance of 230.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974336_consumption`  
  Load '32_LVBus974336_consumption' has phase imbalance of 141.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1107334_consumption`  
  Load '32_LVBus1107334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974221_consumption`  
  Load '32_LVBus974221_consumption' has phase imbalance of 164.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974111_consumption`  
  Load '32_LVBus974111_consumption' has phase imbalance of 116.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130458_consumption`  
  Load '32_LVBus1130458_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974196_consumption`  
  Load '32_LVBus974196_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974283_consumption`  
  Load '32_LVBus974283_consumption' has phase imbalance of 40.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1106532_consumption`  
  Load '32_LVBus1106532_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974054_consumption`  
  Load '32_LVBus974054_consumption' has phase imbalance of 38.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130039_consumption`  
  Load '32_LVBus1130039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105904_consumption`  
  Load '32_LVBus1105904_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974175_consumption`  
  Load '32_LVBus974175_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974037_consumption`  
  Load '32_LVBus974037_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974370_consumption`  
  Load '32_LVBus974370_consumption' has phase imbalance of 146.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974375_consumption`  
  Load '32_LVBus974375_consumption' has phase imbalance of 41.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974115_consumption`  
  Load '32_LVBus974115_consumption' has phase imbalance of 77.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974101_consumption`  
  Load '32_LVBus974101_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974157_consumption`  
  Load '32_LVBus974157_consumption' has phase imbalance of 31.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974369_consumption`  
  Load '32_LVBus974369_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974372_consumption`  
  Load '32_LVBus974372_consumption' has phase imbalance of 85.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974232_consumption`  
  Load '32_LVBus974232_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974250_consumption`  
  Load '32_LVBus974250_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105846_consumption`  
  Load '32_LVBus1105846_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974259_consumption`  
  Load '32_LVBus974259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105845_consumption`  
  Load '32_LVBus1105845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1107336_consumption`  
  Load '32_LVBus1107336_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974217_consumption`  
  Load '32_LVBus974217_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974368_consumption`  
  Load '32_LVBus974368_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974376_consumption`  
  Load '32_LVBus974376_consumption' has phase imbalance of 67.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974107_consumption`  
  Load '32_LVBus974107_consumption' has phase imbalance of 277.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974128_consumption`  
  Load '32_LVBus974128_consumption' has phase imbalance of 122.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974158_consumption`  
  Load '32_LVBus974158_consumption' has phase imbalance of 278.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130461_consumption`  
  Load '32_LVBus1130461_consumption' has phase imbalance of 89.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974301_consumption`  
  Load '32_LVBus974301_consumption' has phase imbalance of 37.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109360_consumption`  
  Load '32_LVBus1109360_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974331_consumption`  
  Load '32_LVBus974331_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974264_consumption`  
  Load '32_LVBus974264_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130460_consumption`  
  Load '32_LVBus1130460_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974137_consumption`  
  Load '32_LVBus974137_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974159_consumption`  
  Load '32_LVBus974159_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974110_consumption`  
  Load '32_LVBus974110_consumption' has phase imbalance of 73.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974079_consumption`  
  Load '32_LVBus974079_consumption' has phase imbalance of 71.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974135_consumption`  
  Load '32_LVBus974135_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974092_consumption`  
  Load '32_LVBus974092_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1107020_consumption`  
  Load '32_LVBus1107020_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974188_consumption`  
  Load '32_LVBus974188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974212_consumption`  
  Load '32_LVBus974212_consumption' has phase imbalance of 224.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974126_consumption`  
  Load '32_LVBus974126_consumption' has phase imbalance of 221.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974198_consumption`  
  Load '32_LVBus974198_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974386_consumption`  
  Load '32_LVBus974386_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109359_consumption`  
  Load '32_LVBus1109359_consumption' has phase imbalance of 135.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974150_consumption`  
  Load '32_LVBus974150_consumption' has phase imbalance of 91.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974332_consumption`  
  Load '32_LVBus974332_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974296_consumption`  
  Load '32_LVBus974296_consumption' has phase imbalance of 39.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974174_consumption`  
  Load '32_LVBus974174_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974224_consumption`  
  Load '32_LVBus974224_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974352_consumption`  
  Load '32_LVBus974352_consumption' has phase imbalance of 241.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109353_consumption`  
  Load '32_LVBus1109353_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974285_consumption`  
  Load '32_LVBus974285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974055_consumption`  
  Load '32_LVBus974055_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974036_consumption`  
  Load '32_LVBus974036_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974392_consumption`  
  Load '32_LVBus974392_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974160_consumption`  
  Load '32_LVBus974160_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974387_consumption`  
  Load '32_LVBus974387_consumption' has phase imbalance of 86.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974246_consumption`  
  Load '32_LVBus974246_consumption' has phase imbalance of 88.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974391_consumption`  
  Load '32_LVBus974391_consumption' has phase imbalance of 36.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974382_consumption`  
  Load '32_LVBus974382_consumption' has phase imbalance of 130.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974130_consumption`  
  Load '32_LVBus974130_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974147_consumption`  
  Load '32_LVBus974147_consumption' has phase imbalance of 95.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974034_consumption`  
  Load '32_LVBus974034_consumption' has phase imbalance of 102.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974268_consumption`  
  Load '32_LVBus974268_consumption' has phase imbalance of 107.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109358_consumption`  
  Load '32_LVBus1109358_consumption' has phase imbalance of 242.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1107019_consumption`  
  Load '32_LVBus1107019_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105903_consumption`  
  Load '32_LVBus1105903_consumption' has phase imbalance of 229.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1176262_consumption`  
  Load '32_LVBus1176262_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105473_consumption`  
  Load '32_LVBus1105473_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105905_consumption`  
  Load '32_LVBus1105905_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974295_consumption`  
  Load '32_LVBus974295_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974309_consumption`  
  Load '32_LVBus974309_consumption' has phase imbalance of 112.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974069_consumption`  
  Load '32_LVBus974069_consumption' has phase imbalance of 127.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974312_consumption`  
  Load '32_LVBus974312_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974091_consumption`  
  Load '32_LVBus974091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974258_consumption`  
  Load '32_LVBus974258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974237_consumption`  
  Load '32_LVBus974237_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974235_consumption`  
  Load '32_LVBus974235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974292_consumption`  
  Load '32_LVBus974292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974144_consumption`  
  Load '32_LVBus974144_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974277_consumption`  
  Load '32_LVBus974277_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974398_consumption`  
  Load '32_LVBus974398_consumption' has phase imbalance of 233.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974231_consumption`  
  Load '32_LVBus974231_consumption' has phase imbalance of 80.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974120_consumption`  
  Load '32_LVBus974120_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1105472_consumption`  
  Load '32_LVBus1105472_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974163_consumption`  
  Load '32_LVBus974163_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974293_consumption`  
  Load '32_LVBus974293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974397_consumption`  
  Load '32_LVBus974397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974124_consumption`  
  Load '32_LVBus974124_consumption' has phase imbalance of 239.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130459_consumption`  
  Load '32_LVBus1130459_consumption' has phase imbalance of 108.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1106520_consumption`  
  Load '32_LVBus1106520_consumption' has phase imbalance of 28.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1107335_consumption`  
  Load '32_LVBus1107335_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974321_consumption`  
  Load '32_LVBus974321_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974371_consumption`  
  Load '32_LVBus974371_consumption' has phase imbalance of 29.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974339_consumption`  
  Load '32_LVBus974339_consumption' has phase imbalance of 240.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974262_consumption`  
  Load '32_LVBus974262_consumption' has phase imbalance of 276.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974360_consumption`  
  Load '32_LVBus974360_consumption' has phase imbalance of 95.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974123_consumption`  
  Load '32_LVBus974123_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974380_consumption`  
  Load '32_LVBus974380_consumption' has phase imbalance of 264.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974086_consumption`  
  Load '32_LVBus974086_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974297_consumption`  
  Load '32_LVBus974297_consumption' has phase imbalance of 92.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974118_consumption`  
  Load '32_LVBus974118_consumption' has phase imbalance of 28.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974088_consumption`  
  Load '32_LVBus974088_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974346_consumption`  
  Load '32_LVBus974346_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974353_consumption`  
  Load '32_LVBus974353_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974364_consumption`  
  Load '32_LVBus974364_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974334_consumption`  
  Load '32_LVBus974334_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974400_consumption`  
  Load '32_LVBus974400_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974367_consumption`  
  Load '32_LVBus974367_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974059_consumption`  
  Load '32_LVBus974059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974359_consumption`  
  Load '32_LVBus974359_consumption' has phase imbalance of 210.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974276_consumption`  
  Load '32_LVBus974276_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974223_consumption`  
  Load '32_LVBus974223_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974214_consumption`  
  Load '32_LVBus974214_consumption' has phase imbalance of 148.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974245_consumption`  
  Load '32_LVBus974245_consumption' has phase imbalance of 207.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974083_consumption`  
  Load '32_LVBus974083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109356_consumption`  
  Load '32_LVBus1109356_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974408_consumption`  
  Load '32_LVBus974408_consumption' has phase imbalance of 257.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974040_consumption`  
  Load '32_LVBus974040_consumption' has phase imbalance of 211.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974274_consumption`  
  Load '32_LVBus974274_consumption' has phase imbalance of 100.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974106_consumption`  
  Load '32_LVBus974106_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974200_consumption`  
  Load '32_LVBus974200_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974324_consumption`  
  Load '32_LVBus974324_consumption' has phase imbalance of 189.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974186_consumption`  
  Load '32_LVBus974186_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974220_consumption`  
  Load '32_LVBus974220_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974185_consumption`  
  Load '32_LVBus974185_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974177_consumption`  
  Load '32_LVBus974177_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974341_consumption`  
  Load '32_LVBus974341_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974308_consumption`  
  Load '32_LVBus974308_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974105_consumption`  
  Load '32_LVBus974105_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974304_consumption`  
  Load '32_LVBus974304_consumption' has phase imbalance of 54.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974183_consumption`  
  Load '32_LVBus974183_consumption' has phase imbalance of 61.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974239_consumption`  
  Load '32_LVBus974239_consumption' has phase imbalance of 94.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1109354_consumption`  
  Load '32_LVBus1109354_consumption' has phase imbalance of 46.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974385_consumption`  
  Load '32_LVBus974385_consumption' has phase imbalance of 80.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130463_consumption`  
  Load '32_LVBus1130463_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974333_consumption`  
  Load '32_LVBus974333_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974030_consumption`  
  Load '32_LVBus974030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974191_consumption`  
  Load '32_LVBus974191_consumption' has phase imbalance of 82.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130462_consumption`  
  Load '32_LVBus1130462_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974099_consumption`  
  Load '32_LVBus974099_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974361_consumption`  
  Load '32_LVBus974361_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974122_consumption`  
  Load '32_LVBus974122_consumption' has phase imbalance of 99.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974310_consumption`  
  Load '32_LVBus974310_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974399_consumption`  
  Load '32_LVBus974399_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus974243_consumption`  
  Load '32_LVBus974243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1108124_consumption`  
  Load '32_LVBus1108124_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 730 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus1127300' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus974226' has balanced aggregate load across 3 phase(s) (max spread 1.85%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  410 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  113 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus1105472_consumption, 32_LVBus1105473_consumption, 32_LVBus1105845_consumption, 32_LVBus1105846_consumption, 32_LVBus1105902_consumption, 32_LVBus1105903_consumption, 32_LVBus1105904_consumption, 32_LVBus1105905_consumption, 32_LVBus1106531_consumption, 32_LVBus1107019_consumption, 32_LVBus1107332_consumption, 32_LVBus1107333_consumption, 32_LVBus1107334_consumption, 32_LVBus1107335_consumption, 32_LVBus1107336_consumption, 32_LVBus1109353_consumption, 32_LVBus1109356_consumption, 32_LVBus1109358_consumption, 32_LVBus1109360_consumption, 32_LVBus1130039_consumption, 32_LVBus1182507_consumption, 32_LVBus974030_consumption, 32_LVBus974033_consumption, 32_LVBus974037_consumption, 32_LVBus974038_consumption, 32_LVBus974040_consumption, 32_LVBus974047_consumption, 32_LVBus974049_consumption, 32_LVBus974050_consumption, 32_LVBus974051_consumption, 32_LVBus974052_consumption, 32_LVBus974059_consumption, 32_LVBus974067_consumption, 32_LVBus974083_consumption, 32_LVBus974091_consumption, 32_LVBus974100_consumption, 32_LVBus974102_consumption, 32_LVBus974105_consumption, 32_LVBus974106_consumption, 32_LVBus974107_consumption, 32_LVBus974120_consumption, 32_LVBus974124_consumption, 32_LVBus974135_consumption, 32_LVBus974136_consumption, 32_LVBus974139_consumption, 32_LVBus974141_consumption, 32_LVBus974143_consumption, 32_LVBus974144_consumption, 32_LVBus974149_consumption, 32_LVBus974158_consumption, 32_LVBus974160_consumption, 32_LVBus974161_consumption, 32_LVBus974173_consumption, 32_LVBus974175_consumption, 32_LVBus974176_consumption, 32_LVBus974177_consumption, 32_LVBus974181_consumption, 32_LVBus974185_consumption, 32_LVBus974188_consumption, 32_LVBus974198_consumption, 32_LVBus974199_consumption, 32_LVBus974200_consumption, 32_LVBus974212_consumption, 32_LVBus974215_consumption, 32_LVBus974216_consumption, 32_LVBus974221_consumption, 32_LVBus974230_consumption, 32_LVBus974232_consumption, 32_LVBus974235_consumption, 32_LVBus974237_consumption, 32_LVBus974243_consumption, 32_LVBus974245_consumption, 32_LVBus974247_consumption, 32_LVBus974250_consumption, 32_LVBus974255_consumption, 32_LVBus974256_consumption, 32_LVBus974258_consumption, 32_LVBus974259_consumption, 32_LVBus974262_consumption, 32_LVBus974264_consumption, 32_LVBus974285_consumption, 32_LVBus974292_consumption, 32_LVBus974293_consumption, 32_LVBus974298_consumption, 32_LVBus974319_consumption, 32_LVBus974320_consumption, 32_LVBus974321_consumption, 32_LVBus974322_consumption, 32_LVBus974326_consumption, 32_LVBus974328_consumption, 32_LVBus974331_consumption, 32_LVBus974332_consumption, 32_LVBus974333_consumption, 32_LVBus974334_consumption, 32_LVBus974338_consumption, 32_LVBus974339_consumption, 32_LVBus974342_consumption, 32_LVBus974346_consumption, 32_LVBus974352_consumption, 32_LVBus974353_consumption, 32_LVBus974361_consumption, 32_LVBus974369_consumption, 32_LVBus974379_consumption, 32_LVBus974380_consumption, 32_LVBus974381_consumption, 32_LVBus974393_consumption, 32_LVBus974397_consumption, 32_LVBus974398_consumption, 32_LVBus974399_consumption, 32_LVBus974405_consumption, 32_LVBus974406_consumption, 32_LVBus974407_consumption, 32_LVBus974408_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  365 group(s) of loads (730 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (2 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  445 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1105378_consumption, 32_LVBus1105378_production, 32_LVBus1105383_consumption, 32_LVBus1105383_production, 32_LVBus1105384_consumption, 32_LVBus1105384_production, 32_LVBus1105472_production, 32_LVBus1105473_production, 32_LVBus1105845_production, 32_LVBus1105846_production, 32_LVBus1105902_production, 32_LVBus1105903_production, 32_LVBus1105904_production, 32_LVBus1105905_production, 32_LVBus1106520_production, 32_LVBus1106521_production, 32_LVBus1106522_consumption, 32_LVBus1106522_production, 32_LVBus1106531_production, 32_LVBus1106532_production, 32_LVBus1106533_production, 32_LVBus1107019_production, 32_LVBus1107020_production, 32_LVBus1107332_production, 32_LVBus1107333_production, 32_LVBus1107334_production, 32_LVBus1107335_production, 32_LVBus1107336_production, 32_LVBus1108124_production, 32_LVBus1108125_production, 32_LVBus1109353_production, 32_LVBus1109354_production, 32_LVBus1109355_production, 32_LVBus1109356_production, 32_LVBus1109357_production, 32_LVBus1109358_production, 32_LVBus1109359_production, 32_LVBus1109360_production, 32_LVBus1109361_production, 32_LVBus1127300_production, 32_LVBus1127301_consumption, 32_LVBus1127301_production, 32_LVBus1130039_production, 32_LVBus1130040_production, 32_LVBus1130457_consumption, 32_LVBus1130457_production, 32_LVBus1130458_production, 32_LVBus1130459_production, 32_LVBus1130460_production, 32_LVBus1130461_production, 32_LVBus1130462_production, 32_LVBus1130463_production, 32_LVBus1130464_production, 32_LVBus1151850_consumption, 32_LVBus1151850_production, 32_LVBus1176262_production, 32_LVBus1178323_consumption, 32_LVBus1178323_production, 32_LVBus1182506_consumption, 32_LVBus1182506_production, 32_LVBus1182507_production, 32_LVBus974021_consumption, 32_LVBus974021_production, 32_LVBus974023_consumption, 32_LVBus974023_production, 32_LVBus974025_consumption, 32_LVBus974025_production, 32_LVBus974027_consumption, 32_LVBus974027_production, 32_LVBus974029_consumption, 32_LVBus974029_production, 32_LVBus974030_production, 32_LVBus974031_consumption, 32_LVBus974031_production, 32_LVBus974032_consumption, 32_LVBus974032_production, 32_LVBus974033_production, 32_LVBus974034_production, 32_LVBus974035_production, 32_LVBus974036_production, 32_LVBus974037_production, 32_LVBus974038_production, 32_LVBus974039_consumption, 32_LVBus974039_production, 32_LVBus974040_production, 32_LVBus974041_consumption, 32_LVBus974041_production, 32_LVBus974042_consumption, 32_LVBus974042_production, 32_LVBus974043_consumption, 32_LVBus974043_production, 32_LVBus974044_consumption, 32_LVBus974044_production, 32_LVBus974045_consumption, 32_LVBus974045_production, 32_LVBus974046_production, 32_LVBus974047_production, 32_LVBus974048_consumption, 32_LVBus974048_production, 32_LVBus974049_production, 32_LVBus974050_production, 32_LVBus974051_production, 32_LVBus974052_production, 32_LVBus974054_production, 32_LVBus974055_production, 32_LVBus974057_consumption, 32_LVBus974057_production, 32_LVBus974059_production, 32_LVBus974061_consumption, 32_LVBus974061_production, 32_LVBus974062_consumption, 32_LVBus974062_production, 32_LVBus974063_consumption, 32_LVBus974063_production, 32_LVBus974065_production, 32_LVBus974066_production, 32_LVBus974067_production, 32_LVBus974068_production, 32_LVBus974069_production, 32_LVBus974070_consumption, 32_LVBus974070_production, 32_LVBus974072_consumption, 32_LVBus974072_production, 32_LVBus974073_production, 32_LVBus974075_production, 32_LVBus974079_production, 32_LVBus974080_production, 32_LVBus974081_production, 32_LVBus974082_production, 32_LVBus974083_production, 32_LVBus974085_consumption, 32_LVBus974085_production, 32_LVBus974086_production, 32_LVBus974087_consumption, 32_LVBus974087_production, 32_LVBus974088_production, 32_LVBus974090_consumption, 32_LVBus974090_production, 32_LVBus974091_production, 32_LVBus974092_production, 32_LVBus974094_production, 32_LVBus974096_production, 32_LVBus974098_production, 32_LVBus974099_production, 32_LVBus974100_production, 32_LVBus974101_production, 32_LVBus974102_production, 32_LVBus974105_production, 32_LVBus974106_production, 32_LVBus974107_production, 32_LVBus974108_production, 32_LVBus974109_production, 32_LVBus974110_production, 32_LVBus974111_production, 32_LVBus974115_production, 32_LVBus974116_production, 32_LVBus974117_production, 32_LVBus974118_production, 32_LVBus974119_production, 32_LVBus974120_production, 32_LVBus974122_production, 32_LVBus974123_production, 32_LVBus974124_production, 32_LVBus974125_production, 32_LVBus974126_production, 32_LVBus974127_production, 32_LVBus974128_production, 32_LVBus974130_production, 32_LVBus974132_consumption, 32_LVBus974132_production, 32_LVBus974134_consumption, 32_LVBus974134_production, 32_LVBus974135_production, 32_LVBus974136_production, 32_LVBus974137_production, 32_LVBus974138_production, 32_LVBus974139_production, 32_LVBus974140_production, 32_LVBus974141_production, 32_LVBus974142_production, 32_LVBus974143_production, 32_LVBus974144_production, 32_LVBus974145_consumption, 32_LVBus974145_production, 32_LVBus974146_consumption, 32_LVBus974146_production, 32_LVBus974147_production, 32_LVBus974148_consumption, 32_LVBus974148_production, 32_LVBus974149_production, 32_LVBus974150_production, 32_LVBus974152_consumption, 32_LVBus974152_production, 32_LVBus974153_consumption, 32_LVBus974153_production, 32_LVBus974154_consumption, 32_LVBus974154_production, 32_LVBus974155_production, 32_LVBus974157_production, 32_LVBus974158_production, 32_LVBus974159_production, 32_LVBus974160_production, 32_LVBus974161_production, 32_LVBus974162_production, 32_LVBus974163_production, 32_LVBus974165_consumption, 32_LVBus974165_production, 32_LVBus974167_production, 32_LVBus974169_consumption, 32_LVBus974169_production, 32_LVBus974170_production, 32_LVBus974173_production, 32_LVBus974174_production, 32_LVBus974175_production, 32_LVBus974176_production, 32_LVBus974177_production, 32_LVBus974178_consumption, 32_LVBus974178_production, 32_LVBus974179_production, 32_LVBus974181_production, 32_LVBus974182_production, 32_LVBus974183_production, 32_LVBus974185_production, 32_LVBus974186_production, 32_LVBus974188_production, 32_LVBus974189_production, 32_LVBus974190_production, 32_LVBus974191_production, 32_LVBus974192_production, 32_LVBus974194_consumption, 32_LVBus974194_production, 32_LVBus974195_consumption, 32_LVBus974195_production, 32_LVBus974196_production, 32_LVBus974197_consumption, 32_LVBus974197_production, 32_LVBus974198_production, 32_LVBus974199_production, 32_LVBus974200_production, 32_LVBus974202_consumption, 32_LVBus974202_production, 32_LVBus974204_consumption, 32_LVBus974204_production, 32_LVBus974206_consumption, 32_LVBus974206_production, 32_LVBus974208_consumption, 32_LVBus974208_production, 32_LVBus974210_production, 32_LVBus974211_production, 32_LVBus974212_production, 32_LVBus974214_production, 32_LVBus974215_production, 32_LVBus974216_production, 32_LVBus974217_production, 32_LVBus974219_production, 32_LVBus974220_production, 32_LVBus974221_production, 32_LVBus974223_production, 32_LVBus974224_production, 32_LVBus974226_production, 32_LVBus974228_production, 32_LVBus974230_production, 32_LVBus974231_production, 32_LVBus974232_production, 32_LVBus974233_consumption, 32_LVBus974233_production, 32_LVBus974234_production, 32_LVBus974235_production, 32_LVBus974236_consumption, 32_LVBus974236_production, 32_LVBus974237_production, 32_LVBus974239_production, 32_LVBus974240_production, 32_LVBus974241_production, 32_LVBus974243_production, 32_LVBus974245_production, 32_LVBus974246_production, 32_LVBus974247_production, 32_LVBus974248_production, 32_LVBus974250_production, 32_LVBus974251_production, 32_LVBus974252_production, 32_LVBus974253_production, 32_LVBus974255_production, 32_LVBus974256_production, 32_LVBus974257_production, 32_LVBus974258_production, 32_LVBus974259_production, 32_LVBus974261_consumption, 32_LVBus974261_production, 32_LVBus974262_production, 32_LVBus974263_production, 32_LVBus974264_production, 32_LVBus974265_production, 32_LVBus974266_production, 32_LVBus974267_production, 32_LVBus974268_production, 32_LVBus974270_consumption, 32_LVBus974270_production, 32_LVBus974271_consumption, 32_LVBus974271_production, 32_LVBus974272_consumption, 32_LVBus974272_production, 32_LVBus974274_production, 32_LVBus974275_production, 32_LVBus974276_production, 32_LVBus974277_production, 32_LVBus974279_production, 32_LVBus974281_production, 32_LVBus974282_consumption, 32_LVBus974282_production, 32_LVBus974283_production, 32_LVBus974285_production, 32_LVBus974286_production, 32_LVBus974287_consumption, 32_LVBus974287_production, 32_LVBus974288_consumption, 32_LVBus974288_production, 32_LVBus974289_production, 32_LVBus974291_consumption, 32_LVBus974291_production, 32_LVBus974292_production, 32_LVBus974293_production, 32_LVBus974294_production, 32_LVBus974295_production, 32_LVBus974296_production, 32_LVBus974297_production, 32_LVBus974298_production, 32_LVBus974299_production, 32_LVBus974301_production, 32_LVBus974302_consumption, 32_LVBus974302_production, 32_LVBus974304_production, 32_LVBus974305_production, 32_LVBus974307_consumption, 32_LVBus974307_production, 32_LVBus974308_production, 32_LVBus974309_production, 32_LVBus974310_production, 32_LVBus974311_production, 32_LVBus974312_production, 32_LVBus974313_consumption, 32_LVBus974313_production, 32_LVBus974314_production, 32_LVBus974316_production, 32_LVBus974317_consumption, 32_LVBus974317_production, 32_LVBus974319_production, 32_LVBus974320_production, 32_LVBus974321_production, 32_LVBus974322_production, 32_LVBus974323_production, 32_LVBus974324_production, 32_LVBus974326_production, 32_LVBus974328_production, 32_LVBus974330_consumption, 32_LVBus974330_production, 32_LVBus974331_production, 32_LVBus974332_production, 32_LVBus974333_production, 32_LVBus974334_production, 32_LVBus974335_production, 32_LVBus974336_production, 32_LVBus974337_production, 32_LVBus974338_production, 32_LVBus974339_production, 32_LVBus974341_production, 32_LVBus974342_production, 32_LVBus974343_consumption, 32_LVBus974343_production, 32_LVBus974346_production, 32_LVBus974347_consumption, 32_LVBus974347_production, 32_LVBus974348_consumption, 32_LVBus974348_production, 32_LVBus974349_production, 32_LVBus974351_production, 32_LVBus974352_production, 32_LVBus974353_production, 32_LVBus974354_production, 32_LVBus974356_production, 32_LVBus974357_production, 32_LVBus974358_production, 32_LVBus974359_production, 32_LVBus974360_production, 32_LVBus974361_production, 32_LVBus974362_consumption, 32_LVBus974362_production, 32_LVBus974363_consumption, 32_LVBus974363_production, 32_LVBus974364_production, 32_LVBus974366_production, 32_LVBus974367_production, 32_LVBus974368_production, 32_LVBus974369_production, 32_LVBus974370_production, 32_LVBus974371_production, 32_LVBus974372_production, 32_LVBus974374_consumption, 32_LVBus974374_production, 32_LVBus974375_production, 32_LVBus974376_production, 32_LVBus974377_production, 32_LVBus974379_production, 32_LVBus974380_production, 32_LVBus974381_production, 32_LVBus974382_production, 32_LVBus974383_production, 32_LVBus974385_production, 32_LVBus974386_production, 32_LVBus974387_production, 32_LVBus974388_production, 32_LVBus974390_consumption, 32_LVBus974390_production, 32_LVBus974391_production, 32_LVBus974392_production, 32_LVBus974393_production, 32_LVBus974394_production, 32_LVBus974395_consumption, 32_LVBus974395_production, 32_LVBus974397_production, 32_LVBus974398_production, 32_LVBus974399_production, 32_LVBus974400_production, 32_LVBus974401_consumption, 32_LVBus974401_production, 32_LVBus974403_production, 32_LVBus974404_production, 32_LVBus974405_production, 32_LVBus974406_production, 32_LVBus974407_production, 32_LVBus974408_production, 32_LVBus974409_production, 32_LVBus974411_consumption, 32_LVBus974411_production, 32_LVBus974413_consumption, 32_LVBus974413_production, 32_MVLV18773_consumption, 32_MVLV18773_production, 32_MVLV33764_consumption, 32_MVLV33764_production, 32_MVLV50023_consumption, 32_MVLV50023_production, 32_MVLV74328_consumption, 32_MVLV74328_production.

