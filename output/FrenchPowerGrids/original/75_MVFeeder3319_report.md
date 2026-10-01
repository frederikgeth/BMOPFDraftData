# BMOPF Network Summary: 75_MVFeeder3319

**Generated:** 2026-10-01 23:34:27  
**Findings:** 0 errors · 5 warnings · 454 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 47 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 786 |  |
| line | 738 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 1358 | 3.799 MW, 1.14 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 47 |  |
| switch | 0 |  |
| transformer | 47 | Dyn11×47 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 70 | 69 | 20 | 0 |
| LV_236V | 236.0 V | 716 | 669 | 1338 | 0 |

**Transformer transitions:**

- `75_MVLV042278_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV153064_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV058064_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062348_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV145164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV003029_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV053005_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV134483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV078635_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV018986_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV009679_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV024387_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV134468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV091959_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV052879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV107941_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV011050_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV097423_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV071083_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV104677_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV097117_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062434_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV030378_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066572_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062675_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV157479_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV153018_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV073046_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV144704_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV052995_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV145172_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV052813_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV078664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV012309_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV031667_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV153029_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV052772_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV145163_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV047029_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV168195_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV174446_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV013737_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV139026_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV073212_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV140178_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV056063_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV131468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 285 |
| Tree depth (max hops) | 33 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 786 | 1 | 785 | 0 | 0 | 0 |
| Tier LV_236V | 716 | 47 | 669 | 0 | 0 | 0 |
| Tier MV_11.8kV | 70 | 1 | 69 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 47; skipped invalid branches: 0.

Galvanic zones: 48; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MVBus100000 | MV_11.8kV | 70 | 0 | 0 | 47 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3074 declared bus terminals; 2883 mapped line/closed-switch conductor edges; 191 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 37800.0 | 2.79 | 4074 |
| q_nom | 0.0 | 11300.0 | 2.79 | 4074 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.361 | 3480.0 | 1.807 | 738 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.502 | 47 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 873 of 1358 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795673_consumption' has phase imbalance of 240.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795109_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1925974_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795589_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795806_consumption' has phase imbalance of 250.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795297_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795630_consumption' has phase imbalance of 285.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795291_consumption' has phase imbalance of 264.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795114_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795695_consumption' has phase imbalance of 131.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795120_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795437_consumption' has phase imbalance of 188.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795593_consumption' has phase imbalance of 89.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795341_consumption' has phase imbalance of 253.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795378_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795546_consumption' has phase imbalance of 157.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795172_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795591_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795797_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795774_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795796_consumption' has phase imbalance of 90.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795170_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795442_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795078_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795368_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795342_consumption' has phase imbalance of 78.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795472_consumption' has phase imbalance of 267.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795664_consumption' has phase imbalance of 50.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795665_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795051_consumption' has phase imbalance of 82.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795609_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795330_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795054_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795180_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795198_consumption' has phase imbalance of 29.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795050_consumption' has phase imbalance of 74.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795267_consumption' has phase imbalance of 146.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795765_consumption' has phase imbalance of 218.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795726_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795762_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1922180_consumption' has phase imbalance of 148.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795340_consumption' has phase imbalance of 68.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795725_consumption' has phase imbalance of 257.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795216_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2011495_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795162_consumption' has phase imbalance of 131.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795060_consumption' has phase imbalance of 230.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795656_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795657_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795448_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795331_consumption' has phase imbalance of 195.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795215_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795116_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795631_consumption' has phase imbalance of 229.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795411_consumption' has phase imbalance of 266.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1937807_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795412_consumption' has phase imbalance of 43.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795507_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795811_consumption' has phase imbalance of 228.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795357_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1923817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795177_consumption' has phase imbalance of 229.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795810_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795058_consumption' has phase imbalance of 21.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795410_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795548_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795460_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795299_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795290_consumption' has phase imbalance of 237.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795175_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795771_consumption' has phase imbalance of 169.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795617_consumption' has phase imbalance of 115.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795280_consumption' has phase imbalance of 256.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795484_consumption' has phase imbalance of 39.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795640_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795121_consumption' has phase imbalance of 183.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795124_consumption' has phase imbalance of 35.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795251_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795659_consumption' has phase imbalance of 287.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795269_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795279_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795426_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795623_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795196_consumption' has phase imbalance of 144.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795602_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795579_consumption' has phase imbalance of 85.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795165_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795606_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795287_consumption' has phase imbalance of 242.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795528_consumption' has phase imbalance of 252.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795429_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795600_consumption' has phase imbalance of 292.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795443_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795350_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795611_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795678_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795727_consumption' has phase imbalance of 117.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795503_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795141_consumption' has phase imbalance of 93.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795329_consumption' has phase imbalance of 291.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795760_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795044_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795404_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795207_consumption' has phase imbalance of 51.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795712_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795808_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795144_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795482_consumption' has phase imbalance of 91.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795669_consumption' has phase imbalance of 128.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795478_consumption' has phase imbalance of 116.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795583_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795508_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795432_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795134_consumption' has phase imbalance of 84.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795458_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795450_consumption' has phase imbalance of 197.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795752_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795800_consumption' has phase imbalance of 84.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795303_consumption' has phase imbalance of 217.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795362_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795633_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795436_consumption' has phase imbalance of 260.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795369_consumption' has phase imbalance of 275.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795666_consumption' has phase imbalance of 211.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795587_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795268_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795473_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795205_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795284_consumption' has phase imbalance of 234.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795255_consumption' has phase imbalance of 91.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795319_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795257_consumption' has phase imbalance of 78.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795086_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795553_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795603_consumption' has phase imbalance of 230.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795747_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795616_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795301_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795346_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795626_consumption' has phase imbalance of 266.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795256_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795336_consumption' has phase imbalance of 101.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795510_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795716_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795158_consumption' has phase imbalance of 254.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795555_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795077_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795208_consumption' has phase imbalance of 40.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795292_consumption' has phase imbalance of 251.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795557_consumption' has phase imbalance of 262.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795745_consumption' has phase imbalance of 123.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795694_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795594_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795681_consumption' has phase imbalance of 293.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795685_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795317_consumption' has phase imbalance of 189.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795661_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795485_consumption' has phase imbalance of 59.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795374_consumption' has phase imbalance of 222.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795288_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795764_consumption' has phase imbalance of 114.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795282_consumption' has phase imbalance of 201.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795576_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795302_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795802_consumption' has phase imbalance of 182.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795168_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795111_consumption' has phase imbalance of 278.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795135_consumption' has phase imbalance of 191.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795281_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795580_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795683_consumption' has phase imbalance of 188.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795396_consumption' has phase imbalance of 244.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795610_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795184_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795544_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795663_consumption' has phase imbalance of 234.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795283_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795688_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795355_consumption' has phase imbalance of 176.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795126_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795405_consumption' has phase imbalance of 29.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926458_consumption' has phase imbalance of 193.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1951435_consumption' has phase imbalance of 222.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795142_consumption' has phase imbalance of 74.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795163_consumption' has phase imbalance of 29.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795166_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795433_consumption' has phase imbalance of 219.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795143_consumption' has phase imbalance of 120.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795734_consumption' has phase imbalance of 123.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795085_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1937808_consumption' has phase imbalance of 227.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795738_consumption' has phase imbalance of 188.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795132_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795667_consumption' has phase imbalance of 118.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795629_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795504_consumption' has phase imbalance of 161.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926463_consumption' has phase imbalance of 97.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795763_consumption' has phase imbalance of 126.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus2011506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795119_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795298_consumption' has phase imbalance of 46.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795455_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795674_consumption' has phase imbalance of 41.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795619_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795407_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795421_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795194_consumption' has phase imbalance of 65.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795751_consumption' has phase imbalance of 137.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795767_consumption' has phase imbalance of 259.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795732_consumption' has phase imbalance of 243.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795157_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795307_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795613_consumption' has phase imbalance of 42.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795506_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795084_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795110_consumption' has phase imbalance of 229.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926466_consumption' has phase imbalance of 204.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795502_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795438_consumption' has phase imbalance of 205.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795471_consumption' has phase imbalance of 128.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795195_consumption' has phase imbalance of 86.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795306_consumption' has phase imbalance of 105.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795634_consumption' has phase imbalance of 119.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795183_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795620_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795188_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795145_consumption' has phase imbalance of 184.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795537_consumption' has phase imbalance of 218.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1951430_consumption' has phase imbalance of 222.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795315_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795636_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1951434_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795770_consumption' has phase imbalance of 138.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795068_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795740_consumption' has phase imbalance of 121.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795289_consumption' has phase imbalance of 231.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795803_consumption' has phase imbalance of 272.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795316_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795059_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795474_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795675_consumption' has phase imbalance of 259.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795359_consumption' has phase imbalance of 254.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795053_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795731_consumption' has phase imbalance of 253.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795441_consumption' has phase imbalance of 64.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795605_consumption' has phase imbalance of 55.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795481_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795772_consumption' has phase imbalance of 168.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795769_consumption' has phase imbalance of 122.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795403_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795155_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795483_consumption' has phase imbalance of 209.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795598_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795171_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795529_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795729_consumption' has phase imbalance of 222.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795358_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926465_consumption' has phase imbalance of 209.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795332_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795739_consumption' has phase imbalance of 45.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795065_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795486_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795643_consumption' has phase imbalance of 252.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795622_consumption' has phase imbalance of 108.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795066_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795136_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795776_consumption' has phase imbalance of 60.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795409_consumption' has phase imbalance of 111.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795334_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795361_consumption' has phase imbalance of 140.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795793_consumption' has phase imbalance of 94.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795173_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795743_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795399_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795757_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795125_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795440_consumption' has phase imbalance of 224.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795775_consumption' has phase imbalance of 60.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795146_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795638_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795217_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795596_consumption' has phase imbalance of 65.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795554_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795311_consumption' has phase imbalance of 261.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795477_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795635_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795295_consumption' has phase imbalance of 46.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795509_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795435_consumption' has phase imbalance of 126.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795604_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795347_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795690_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795462_consumption' has phase imbalance of 124.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795697_consumption' has phase imbalance of 269.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795415_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795186_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795680_consumption' has phase imbalance of 135.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795744_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1926462_consumption' has phase imbalance of 147.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795152_consumption' has phase imbalance of 248.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795197_consumption' has phase imbalance of 56.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795709_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795588_consumption' has phase imbalance of 56.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795252_consumption' has phase imbalance of 92.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795328_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795325_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795352_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795305_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795728_consumption' has phase imbalance of 281.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795206_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795431_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795127_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795310_consumption' has phase imbalance of 135.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795614_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795354_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795582_consumption' has phase imbalance of 239.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795309_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795400_consumption' has phase imbalance of 256.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795353_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795547_consumption' has phase imbalance of 120.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795108_consumption' has phase imbalance of 217.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795461_consumption' has phase imbalance of 118.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795076_consumption' has phase imbalance of 29.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795187_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795398_consumption' has phase imbalance of 106.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795575_consumption' has phase imbalance of 246.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795581_consumption' has phase imbalance of 269.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795335_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795608_consumption' has phase imbalance of 232.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795677_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795154_consumption' has phase imbalance of 45.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795584_consumption' has phase imbalance of 36.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795293_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1795417_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1358 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1795071' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1795512' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1795092' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1795563' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1795701' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1795488' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.799 MW |
| Total load Q | 1.14 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV042278_Transformer | 275.0 kVA | 28.2% |
| 75_MVLV153064_Transformer | 693.0 kVA | 33.1% |
| 75_MVLV058064_Transformer | 440.0 kVA | 26.8% |
| 75_MVLV062348_Transformer | 440.0 kVA | 27.5% |
| 75_MVLV145164_Transformer | 110.0 kVA | 1.2% |
| 75_MVLV003029_Transformer | 110.0 kVA | 16.1% |
| 75_MVLV053005_Transformer | 440.0 kVA | 44.3% |
| 75_MVLV134483_Transformer | 440.0 kVA | 31.8% |
| 75_MVLV078635_Transformer | 693.0 kVA | 18.6% |
| 75_MVLV018986_Transformer | 693.0 kVA | 24.1% |
| 75_MVLV009679_Transformer | 440.0 kVA | 24.5% |
| 75_MVLV024387_Transformer | 176.0 kVA | 18.5% |
| 75_MVLV134468_Transformer | 440.0 kVA | 10.8% |
| 75_MVLV091959_Transformer | 440.0 kVA | 13.0% |
| 75_MVLV052879_Transformer | 440.0 kVA | 18.9% |
| 75_MVLV107941_Transformer | 275.0 kVA | 20.2% |
| 75_MVLV011050_Transformer | 440.0 kVA | 13.4% |
| 75_MVLV097423_Transformer | 110.0 kVA | 7.0% |
| 75_MVLV071083_Transformer | 440.0 kVA | 19.0% |
| 75_MVLV104677_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV097117_Transformer | 110.0 kVA | 9.5% |
| 75_MVLV062434_Transformer | 176.0 kVA | 12.1% |
| 75_MVLV030378_Transformer | 440.0 kVA | 20.1% |
| 75_MVLV066572_Transformer | 440.0 kVA | 28.1% |
| 75_MVLV062675_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV157479_Transformer | 440.0 kVA | 45.1% |
| 75_MVLV153018_Transformer | 176.0 kVA | 16.0% |
| 75_MVLV073046_Transformer | 440.0 kVA | 26.1% |
| 75_MVLV144704_Transformer | 693.0 kVA | 30.8% |
| 75_MVLV052995_Transformer | 176.0 kVA | 2.9% |
| 75_MVLV145172_Transformer | 440.0 kVA | 9.9% |
| 75_MVLV052813_Transformer | 1.1 MVA | 22.0% |
| 75_MVLV078664_Transformer | 275.0 kVA | 39.4% |
| 75_MVLV012309_Transformer | 693.0 kVA | 14.7% |
| 75_MVLV031667_Transformer | 176.0 kVA | 21.8% |
| 75_MVLV153029_Transformer | 275.0 kVA | 17.1% |
| 75_MVLV052772_Transformer | 275.0 kVA | 11.4% |
| 75_MVLV145163_Transformer | 440.0 kVA | 21.9% |
| 75_MVLV047029_Transformer | 440.0 kVA | 35.1% |
| 75_MVLV168195_Transformer | 440.0 kVA | 10.0% |
| 75_MVLV174446_Transformer | 440.0 kVA | 30.7% |
| 75_MVLV013737_Transformer | 440.0 kVA | 9.2% |
| 75_MVLV139026_Transformer | 440.0 kVA | 18.3% |
| 75_MVLV073212_Transformer | 440.0 kVA | 19.8% |
| 75_MVLV140178_Transformer | 440.0 kVA | 16.2% |
| 75_MVLV056063_Transformer | 440.0 kVA | 25.0% |
| 75_MVLV131468_Transformer | 176.0 kVA | 0.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.8 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1795071' (LV, 0.24 kV) has an electrical reach of 18.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus1795540' (LV, 0.24 kV) has an electrical reach of 26.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 786 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 786 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 47 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 70 |
| LV_236V | 4-wire | 716 / 716 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 716 |
| Neutral branches | 669 |
| Grounding points | 47 |
| Neutral sections | 47 |
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
| 11.78 kV | 70 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 61 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 48 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2870.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 716 / 70 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 874 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 874 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1795042_production, 75_LVBus1795043_production, 75_LVBus1795044_production, 75_LVBus1795045_consumption, 75_LVBus1795045_production, 75_LVBus1795046_consumption, 75_LVBus1795046_production, 75_LVBus1795047_consumption, 75_LVBus1795047_production, 75_LVBus1795049_consumption, 75_LVBus1795049_production, 75_LVBus1795050_production, 75_LVBus1795051_production, 75_LVBus1795052_production, 75_LVBus1795053_production, 75_LVBus1795054_production, 75_LVBus1795056_consumption, 75_LVBus1795056_production, 75_LVBus1795057_consumption, 75_LVBus1795057_production, 75_LVBus1795058_production, 75_LVBus1795059_production, 75_LVBus1795060_production, 75_LVBus1795061_consumption, 75_LVBus1795061_production, 75_LVBus1795062_consumption, 75_LVBus1795062_production, 75_LVBus1795064_consumption, 75_LVBus1795064_production, 75_LVBus1795065_production, 75_LVBus1795066_production, 75_LVBus1795068_production, 75_LVBus1795069_consumption, 75_LVBus1795069_production, 75_LVBus1795071_production, 75_LVBus1795073_production, 75_LVBus1795075_consumption, 75_LVBus1795075_production, 75_LVBus1795076_production, 75_LVBus1795077_production, 75_LVBus1795078_production, 75_LVBus1795079_production, 75_LVBus1795081_consumption, 75_LVBus1795081_production, 75_LVBus1795082_production, 75_LVBus1795083_production, 75_LVBus1795084_production, 75_LVBus1795085_production, 75_LVBus1795086_production, 75_LVBus1795088_consumption, 75_LVBus1795088_production, 75_LVBus1795089_production, 75_LVBus1795090_consumption, 75_LVBus1795090_production, 75_LVBus1795092_consumption, 75_LVBus1795092_production, 75_LVBus1795094_consumption, 75_LVBus1795094_production, 75_LVBus1795096_consumption, 75_LVBus1795096_production, 75_LVBus1795098_consumption, 75_LVBus1795098_production, 75_LVBus1795100_production, 75_LVBus1795102_consumption, 75_LVBus1795102_production, 75_LVBus1795104_consumption, 75_LVBus1795104_production, 75_LVBus1795106_consumption, 75_LVBus1795106_production, 75_LVBus1795108_production, 75_LVBus1795109_production, 75_LVBus1795110_production, 75_LVBus1795111_production, 75_LVBus1795112_production, 75_LVBus1795113_consumption, 75_LVBus1795113_production, 75_LVBus1795114_production, 75_LVBus1795116_production, 75_LVBus1795117_consumption, 75_LVBus1795117_production, 75_LVBus1795118_consumption, 75_LVBus1795118_production, 75_LVBus1795119_production, 75_LVBus1795120_production, 75_LVBus1795121_production, 75_LVBus1795123_production, 75_LVBus1795124_production, 75_LVBus1795125_production, 75_LVBus1795126_production, 75_LVBus1795127_production, 75_LVBus1795129_consumption, 75_LVBus1795129_production, 75_LVBus1795130_production, 75_LVBus1795131_production, 75_LVBus1795132_production, 75_LVBus1795133_production, 75_LVBus1795134_production, 75_LVBus1795135_production, 75_LVBus1795136_production, 75_LVBus1795138_production, 75_LVBus1795139_production, 75_LVBus1795140_consumption, 75_LVBus1795140_production, 75_LVBus1795141_production, 75_LVBus1795142_production, 75_LVBus1795143_production, 75_LVBus1795144_production, 75_LVBus1795145_production, 75_LVBus1795146_production, 75_LVBus1795147_production, 75_LVBus1795148_consumption, 75_LVBus1795148_production, 75_LVBus1795149_consumption, 75_LVBus1795149_production, 75_LVBus1795152_production, 75_LVBus1795153_consumption, 75_LVBus1795153_production, 75_LVBus1795154_production, 75_LVBus1795155_production, 75_LVBus1795157_production, 75_LVBus1795158_production, 75_LVBus1795159_production, 75_LVBus1795160_production, 75_LVBus1795162_production, 75_LVBus1795163_production, 75_LVBus1795165_production, 75_LVBus1795166_production, 75_LVBus1795168_production, 75_LVBus1795169_production, 75_LVBus1795170_production, 75_LVBus1795171_production, 75_LVBus1795172_production, 75_LVBus1795173_production, 75_LVBus1795175_production, 75_LVBus1795176_production, 75_LVBus1795177_production, 75_LVBus1795178_consumption, 75_LVBus1795178_production, 75_LVBus1795180_production, 75_LVBus1795181_production, 75_LVBus1795182_production, 75_LVBus1795183_production, 75_LVBus1795184_production, 75_LVBus1795185_production, 75_LVBus1795186_production, 75_LVBus1795187_production, 75_LVBus1795188_production, 75_LVBus1795189_consumption, 75_LVBus1795189_production, 75_LVBus1795190_consumption, 75_LVBus1795190_production, 75_LVBus1795194_production, 75_LVBus1795195_production, 75_LVBus1795196_production, 75_LVBus1795197_production, 75_LVBus1795198_production, 75_LVBus1795199_production, 75_LVBus1795200_production, 75_LVBus1795201_consumption, 75_LVBus1795201_production, 75_LVBus1795202_consumption, 75_LVBus1795202_production, 75_LVBus1795203_production, 75_LVBus1795205_production, 75_LVBus1795206_production, 75_LVBus1795207_production, 75_LVBus1795208_production, 75_LVBus1795210_production, 75_LVBus1795212_production, 75_LVBus1795213_production, 75_LVBus1795214_consumption, 75_LVBus1795214_production, 75_LVBus1795215_production, 75_LVBus1795216_production, 75_LVBus1795217_production, 75_LVBus1795218_consumption, 75_LVBus1795218_production, 75_LVBus1795220_production, 75_LVBus1795221_production, 75_LVBus1795222_production, 75_LVBus1795224_consumption, 75_LVBus1795224_production, 75_LVBus1795225_production, 75_LVBus1795226_production, 75_LVBus1795227_production, 75_LVBus1795229_consumption, 75_LVBus1795229_production, 75_LVBus1795230_consumption, 75_LVBus1795230_production, 75_LVBus1795231_production, 75_LVBus1795232_production, 75_LVBus1795233_consumption, 75_LVBus1795233_production, 75_LVBus1795235_consumption, 75_LVBus1795235_production, 75_LVBus1795237_consumption, 75_LVBus1795237_production, 75_LVBus1795238_production, 75_LVBus1795239_production, 75_LVBus1795241_consumption, 75_LVBus1795241_production, 75_LVBus1795242_production, 75_LVBus1795244_consumption, 75_LVBus1795244_production, 75_LVBus1795245_consumption, 75_LVBus1795245_production, 75_LVBus1795246_consumption, 75_LVBus1795246_production, 75_LVBus1795247_production, 75_LVBus1795249_production, 75_LVBus1795251_production, 75_LVBus1795252_production, 75_LVBus1795254_production, 75_LVBus1795255_production, 75_LVBus1795256_production, 75_LVBus1795257_production, 75_LVBus1795259_production, 75_LVBus1795260_consumption, 75_LVBus1795260_production, 75_LVBus1795261_production, 75_LVBus1795262_production, 75_LVBus1795263_production, 75_LVBus1795264_consumption, 75_LVBus1795264_production, 75_LVBus1795265_consumption, 75_LVBus1795265_production, 75_LVBus1795266_production, 75_LVBus1795267_production, 75_LVBus1795268_production, 75_LVBus1795269_production, 75_LVBus1795271_consumption, 75_LVBus1795271_production, 75_LVBus1795273_production, 75_LVBus1795274_consumption, 75_LVBus1795274_production, 75_LVBus1795275_production, 75_LVBus1795276_production, 75_LVBus1795278_production, 75_LVBus1795279_production, 75_LVBus1795280_production, 75_LVBus1795281_production, 75_LVBus1795282_production, 75_LVBus1795283_production, 75_LVBus1795284_production, 75_LVBus1795286_production, 75_LVBus1795287_production, 75_LVBus1795288_production, 75_LVBus1795289_production, 75_LVBus1795290_production, 75_LVBus1795291_production, 75_LVBus1795292_production, 75_LVBus1795293_production, 75_LVBus1795294_production, 75_LVBus1795295_production, 75_LVBus1795297_production, 75_LVBus1795298_production, 75_LVBus1795299_production, 75_LVBus1795301_production, 75_LVBus1795302_production, 75_LVBus1795303_production, 75_LVBus1795304_production, 75_LVBus1795305_production, 75_LVBus1795306_production, 75_LVBus1795307_production, 75_LVBus1795309_production, 75_LVBus1795310_production, 75_LVBus1795311_production, 75_LVBus1795312_production, 75_LVBus1795313_production, 75_LVBus1795314_consumption, 75_LVBus1795314_production, 75_LVBus1795315_production, 75_LVBus1795316_production, 75_LVBus1795317_production, 75_LVBus1795319_production, 75_LVBus1795320_consumption, 75_LVBus1795320_production, 75_LVBus1795321_production, 75_LVBus1795323_consumption, 75_LVBus1795323_production, 75_LVBus1795324_production, 75_LVBus1795325_production, 75_LVBus1795326_production, 75_LVBus1795327_consumption, 75_LVBus1795327_production, 75_LVBus1795328_production, 75_LVBus1795329_production, 75_LVBus1795330_production, 75_LVBus1795331_production, 75_LVBus1795332_production, 75_LVBus1795333_production, 75_LVBus1795334_production, 75_LVBus1795335_production, 75_LVBus1795336_production, 75_LVBus1795338_consumption, 75_LVBus1795338_production, 75_LVBus1795339_consumption, 75_LVBus1795339_production, 75_LVBus1795340_production, 75_LVBus1795341_production, 75_LVBus1795342_production, 75_LVBus1795346_production, 75_LVBus1795347_production, 75_LVBus1795349_production, 75_LVBus1795350_production, 75_LVBus1795351_production, 75_LVBus1795352_production, 75_LVBus1795353_production, 75_LVBus1795354_production, 75_LVBus1795355_production, 75_LVBus1795357_production, 75_LVBus1795358_production, 75_LVBus1795359_production, 75_LVBus1795361_production, 75_LVBus1795362_production, 75_LVBus1795364_consumption, 75_LVBus1795364_production, 75_LVBus1795365_consumption, 75_LVBus1795365_production, 75_LVBus1795366_consumption, 75_LVBus1795366_production, 75_LVBus1795367_production, 75_LVBus1795368_production, 75_LVBus1795369_production, 75_LVBus1795370_consumption, 75_LVBus1795370_production, 75_LVBus1795371_consumption, 75_LVBus1795371_production, 75_LVBus1795372_production, 75_LVBus1795373_production, 75_LVBus1795374_production, 75_LVBus1795375_production, 75_LVBus1795376_consumption, 75_LVBus1795376_production, 75_LVBus1795377_production, 75_LVBus1795378_production, 75_LVBus1795380_consumption, 75_LVBus1795380_production, 75_LVBus1795381_consumption, 75_LVBus1795381_production, 75_LVBus1795382_consumption, 75_LVBus1795382_production, 75_LVBus1795383_consumption, 75_LVBus1795383_production, 75_LVBus1795385_consumption, 75_LVBus1795385_production, 75_LVBus1795386_consumption, 75_LVBus1795386_production, 75_LVBus1795387_consumption, 75_LVBus1795387_production, 75_LVBus1795388_consumption, 75_LVBus1795388_production, 75_LVBus1795389_consumption, 75_LVBus1795389_production, 75_LVBus1795390_consumption, 75_LVBus1795390_production, 75_LVBus1795395_production, 75_LVBus1795396_production, 75_LVBus1795397_production, 75_LVBus1795398_production, 75_LVBus1795399_production, 75_LVBus1795400_production, 75_LVBus1795401_production, 75_LVBus1795403_production, 75_LVBus1795404_production, 75_LVBus1795405_production, 75_LVBus1795406_production, 75_LVBus1795407_production, 75_LVBus1795409_production, 75_LVBus1795410_production, 75_LVBus1795411_production, 75_LVBus1795412_production, 75_LVBus1795414_production, 75_LVBus1795415_production, 75_LVBus1795416_consumption, 75_LVBus1795416_production, 75_LVBus1795417_production, 75_LVBus1795418_consumption, 75_LVBus1795418_production, 75_LVBus1795420_production, 75_LVBus1795421_production, 75_LVBus1795423_production, 75_LVBus1795425_consumption, 75_LVBus1795425_production, 75_LVBus1795426_production, 75_LVBus1795428_production, 75_LVBus1795429_production, 75_LVBus1795430_production, 75_LVBus1795431_production, 75_LVBus1795432_production, 75_LVBus1795433_production, 75_LVBus1795434_consumption, 75_LVBus1795434_production, 75_LVBus1795435_production, 75_LVBus1795436_production, 75_LVBus1795437_production, 75_LVBus1795438_production, 75_LVBus1795440_production, 75_LVBus1795441_production, 75_LVBus1795442_production, 75_LVBus1795443_production, 75_LVBus1795444_production, 75_LVBus1795445_production, 75_LVBus1795446_production, 75_LVBus1795447_consumption, 75_LVBus1795447_production, 75_LVBus1795448_production, 75_LVBus1795449_production, 75_LVBus1795450_production, 75_LVBus1795452_consumption, 75_LVBus1795452_production, 75_LVBus1795453_consumption, 75_LVBus1795453_production, 75_LVBus1795454_consumption, 75_LVBus1795454_production, 75_LVBus1795455_production, 75_LVBus1795456_consumption, 75_LVBus1795456_production, 75_LVBus1795457_consumption, 75_LVBus1795457_production, 75_LVBus1795458_production, 75_LVBus1795460_production, 75_LVBus1795461_production, 75_LVBus1795462_production, 75_LVBus1795463_production, 75_LVBus1795464_consumption, 75_LVBus1795464_production, 75_LVBus1795465_consumption, 75_LVBus1795465_production, 75_LVBus1795466_consumption, 75_LVBus1795466_production, 75_LVBus1795467_consumption, 75_LVBus1795467_production, 75_LVBus1795468_consumption, 75_LVBus1795468_production, 75_LVBus1795469_production, 75_LVBus1795470_consumption, 75_LVBus1795470_production, 75_LVBus1795471_production, 75_LVBus1795472_production, 75_LVBus1795473_production, 75_LVBus1795474_production, 75_LVBus1795476_production, 75_LVBus1795477_production, 75_LVBus1795478_production, 75_LVBus1795479_production, 75_LVBus1795481_production, 75_LVBus1795482_production, 75_LVBus1795483_production, 75_LVBus1795484_production, 75_LVBus1795485_production, 75_LVBus1795486_production, 75_LVBus1795488_consumption, 75_LVBus1795488_production, 75_LVBus1795490_consumption, 75_LVBus1795490_production, 75_LVBus1795492_production, 75_LVBus1795494_consumption, 75_LVBus1795494_production, 75_LVBus1795496_consumption, 75_LVBus1795496_production, 75_LVBus1795498_consumption, 75_LVBus1795498_production, 75_LVBus1795500_production, 75_LVBus1795502_production, 75_LVBus1795503_production, 75_LVBus1795504_production, 75_LVBus1795506_production, 75_LVBus1795507_production, 75_LVBus1795508_production, 75_LVBus1795509_production, 75_LVBus1795510_production, 75_LVBus1795512_consumption, 75_LVBus1795512_production, 75_LVBus1795514_consumption, 75_LVBus1795514_production, 75_LVBus1795516_consumption, 75_LVBus1795516_production, 75_LVBus1795518_production, 75_LVBus1795520_consumption, 75_LVBus1795520_production, 75_LVBus1795522_production, 75_LVBus1795524_consumption, 75_LVBus1795524_production, 75_LVBus1795526_production, 75_LVBus1795528_production, 75_LVBus1795529_production, 75_LVBus1795531_consumption, 75_LVBus1795531_production, 75_LVBus1795532_consumption, 75_LVBus1795532_production, 75_LVBus1795533_production, 75_LVBus1795536_consumption, 75_LVBus1795536_production, 75_LVBus1795537_production, 75_LVBus1795538_consumption, 75_LVBus1795538_production, 75_LVBus1795540_consumption, 75_LVBus1795540_production, 75_LVBus1795541_consumption, 75_LVBus1795541_production, 75_LVBus1795544_production, 75_LVBus1795545_production, 75_LVBus1795546_production, 75_LVBus1795547_production, 75_LVBus1795548_production, 75_LVBus1795549_production, 75_LVBus1795550_production, 75_LVBus1795551_consumption, 75_LVBus1795551_production, 75_LVBus1795552_consumption, 75_LVBus1795552_production, 75_LVBus1795553_production, 75_LVBus1795554_production, 75_LVBus1795555_production, 75_LVBus1795556_production, 75_LVBus1795557_production, 75_LVBus1795561_consumption, 75_LVBus1795561_production, 75_LVBus1795563_consumption, 75_LVBus1795563_production, 75_LVBus1795565_consumption, 75_LVBus1795565_production, 75_LVBus1795567_production, 75_LVBus1795568_consumption, 75_LVBus1795568_production, 75_LVBus1795569_consumption, 75_LVBus1795569_production, 75_LVBus1795571_consumption, 75_LVBus1795571_production, 75_LVBus1795573_consumption, 75_LVBus1795573_production, 75_LVBus1795575_production, 75_LVBus1795576_production, 75_LVBus1795577_consumption, 75_LVBus1795577_production, 75_LVBus1795579_production, 75_LVBus1795580_production, 75_LVBus1795581_production, 75_LVBus1795582_production, 75_LVBus1795583_production, 75_LVBus1795584_production, 75_LVBus1795586_production, 75_LVBus1795587_production, 75_LVBus1795588_production, 75_LVBus1795589_production, 75_LVBus1795590_production, 75_LVBus1795591_production, 75_LVBus1795592_consumption, 75_LVBus1795592_production, 75_LVBus1795593_production, 75_LVBus1795594_production, 75_LVBus1795595_consumption, 75_LVBus1795595_production, 75_LVBus1795596_production, 75_LVBus1795597_production, 75_LVBus1795598_production, 75_LVBus1795599_production, 75_LVBus1795600_production, 75_LVBus1795602_production, 75_LVBus1795603_production, 75_LVBus1795604_production, 75_LVBus1795605_production, 75_LVBus1795606_production, 75_LVBus1795608_production, 75_LVBus1795609_production, 75_LVBus1795610_production, 75_LVBus1795611_production, 75_LVBus1795613_production, 75_LVBus1795614_production, 75_LVBus1795616_production, 75_LVBus1795617_production, 75_LVBus1795618_consumption, 75_LVBus1795618_production, 75_LVBus1795619_production, 75_LVBus1795620_production, 75_LVBus1795621_production, 75_LVBus1795622_production, 75_LVBus1795623_production, 75_LVBus1795624_consumption, 75_LVBus1795624_production, 75_LVBus1795626_production, 75_LVBus1795627_production, 75_LVBus1795628_production, 75_LVBus1795629_production, 75_LVBus1795630_production, 75_LVBus1795631_production, 75_LVBus1795633_production, 75_LVBus1795634_production, 75_LVBus1795635_production, 75_LVBus1795636_production, 75_LVBus1795638_production, 75_LVBus1795639_production, 75_LVBus1795640_production, 75_LVBus1795641_production, 75_LVBus1795642_production, 75_LVBus1795643_production, 75_LVBus1795644_production, 75_LVBus1795646_production, 75_LVBus1795648_production, 75_LVBus1795650_consumption, 75_LVBus1795650_production, 75_LVBus1795652_production, 75_LVBus1795654_consumption, 75_LVBus1795654_production, 75_LVBus1795655_production, 75_LVBus1795656_production, 75_LVBus1795657_production, 75_LVBus1795658_production, 75_LVBus1795659_production, 75_LVBus1795660_production, 75_LVBus1795661_production, 75_LVBus1795662_production, 75_LVBus1795663_production, 75_LVBus1795664_production, 75_LVBus1795665_production, 75_LVBus1795666_production, 75_LVBus1795667_production, 75_LVBus1795669_production, 75_LVBus1795670_consumption, 75_LVBus1795670_production, 75_LVBus1795673_production, 75_LVBus1795674_production, 75_LVBus1795675_production, 75_LVBus1795676_production, 75_LVBus1795677_production, 75_LVBus1795678_production, 75_LVBus1795679_production, 75_LVBus1795680_production, 75_LVBus1795681_production, 75_LVBus1795683_production, 75_LVBus1795684_consumption, 75_LVBus1795684_production, 75_LVBus1795685_production, 75_LVBus1795686_production, 75_LVBus1795687_production, 75_LVBus1795688_production, 75_LVBus1795690_production, 75_LVBus1795691_production, 75_LVBus1795692_production, 75_LVBus1795693_production, 75_LVBus1795694_production, 75_LVBus1795695_production, 75_LVBus1795697_production, 75_LVBus1795699_consumption, 75_LVBus1795699_production, 75_LVBus1795701_production, 75_LVBus1795703_consumption, 75_LVBus1795703_production, 75_LVBus1795705_production, 75_LVBus1795708_production, 75_LVBus1795709_production, 75_LVBus1795710_production, 75_LVBus1795712_production, 75_LVBus1795714_consumption, 75_LVBus1795714_production, 75_LVBus1795716_production, 75_LVBus1795718_production, 75_LVBus1795720_production, 75_LVBus1795721_production, 75_LVBus1795723_consumption, 75_LVBus1795723_production, 75_LVBus1795725_production, 75_LVBus1795726_production, 75_LVBus1795727_production, 75_LVBus1795728_production, 75_LVBus1795729_production, 75_LVBus1795730_consumption, 75_LVBus1795730_production, 75_LVBus1795731_production, 75_LVBus1795732_production, 75_LVBus1795733_production, 75_LVBus1795734_production, 75_LVBus1795736_consumption, 75_LVBus1795736_production, 75_LVBus1795738_production, 75_LVBus1795739_production, 75_LVBus1795740_production, 75_LVBus1795742_production, 75_LVBus1795743_production, 75_LVBus1795744_production, 75_LVBus1795745_production, 75_LVBus1795747_production, 75_LVBus1795748_production, 75_LVBus1795750_production, 75_LVBus1795751_production, 75_LVBus1795752_production, 75_LVBus1795753_consumption, 75_LVBus1795753_production, 75_LVBus1795754_production, 75_LVBus1795755_production, 75_LVBus1795757_production, 75_LVBus1795759_production, 75_LVBus1795760_production, 75_LVBus1795762_production, 75_LVBus1795763_production, 75_LVBus1795764_production, 75_LVBus1795765_production, 75_LVBus1795767_production, 75_LVBus1795768_production, 75_LVBus1795769_production, 75_LVBus1795770_production, 75_LVBus1795771_production, 75_LVBus1795772_production, 75_LVBus1795774_production, 75_LVBus1795775_production, 75_LVBus1795776_production, 75_LVBus1795778_production, 75_LVBus1795779_consumption, 75_LVBus1795779_production, 75_LVBus1795780_consumption, 75_LVBus1795780_production, 75_LVBus1795781_consumption, 75_LVBus1795781_production, 75_LVBus1795783_consumption, 75_LVBus1795783_production, 75_LVBus1795785_consumption, 75_LVBus1795785_production, 75_LVBus1795786_consumption, 75_LVBus1795786_production, 75_LVBus1795787_consumption, 75_LVBus1795787_production, 75_LVBus1795788_consumption, 75_LVBus1795788_production, 75_LVBus1795789_consumption, 75_LVBus1795789_production, 75_LVBus1795791_consumption, 75_LVBus1795791_production, 75_LVBus1795792_consumption, 75_LVBus1795792_production, 75_LVBus1795793_production, 75_LVBus1795795_production, 75_LVBus1795796_production, 75_LVBus1795797_production, 75_LVBus1795798_production, 75_LVBus1795800_production, 75_LVBus1795801_consumption, 75_LVBus1795801_production, 75_LVBus1795802_production, 75_LVBus1795803_production, 75_LVBus1795804_production, 75_LVBus1795805_production, 75_LVBus1795806_production, 75_LVBus1795807_production, 75_LVBus1795808_production, 75_LVBus1795809_production, 75_LVBus1795810_production, 75_LVBus1795811_production, 75_LVBus1921355_consumption, 75_LVBus1921355_production, 75_LVBus1921365_consumption, 75_LVBus1921365_production, 75_LVBus1922180_production, 75_LVBus1923817_production, 75_LVBus1925890_consumption, 75_LVBus1925890_production, 75_LVBus1925973_consumption, 75_LVBus1925973_production, 75_LVBus1925974_production, 75_LVBus1926453_consumption, 75_LVBus1926453_production, 75_LVBus1926454_production, 75_LVBus1926455_consumption, 75_LVBus1926455_production, 75_LVBus1926456_consumption, 75_LVBus1926456_production, 75_LVBus1926457_production, 75_LVBus1926458_production, 75_LVBus1926459_consumption, 75_LVBus1926459_production, 75_LVBus1926460_production, 75_LVBus1926461_consumption, 75_LVBus1926461_production, 75_LVBus1926462_production, 75_LVBus1926463_production, 75_LVBus1926464_consumption, 75_LVBus1926464_production, 75_LVBus1926465_production, 75_LVBus1926466_production, 75_LVBus1928448_consumption, 75_LVBus1928448_production, 75_LVBus1928449_consumption, 75_LVBus1928449_production, 75_LVBus1937807_production, 75_LVBus1937808_production, 75_LVBus1951430_production, 75_LVBus1951431_consumption, 75_LVBus1951431_production, 75_LVBus1951432_consumption, 75_LVBus1951432_production, 75_LVBus1951433_consumption, 75_LVBus1951433_production, 75_LVBus1951434_production, 75_LVBus1951435_production, 75_LVBus1981591_consumption, 75_LVBus1981591_production, 75_LVBus1989415_consumption, 75_LVBus1989415_production, 75_LVBus1989416_consumption, 75_LVBus1989416_production, 75_LVBus1989417_consumption, 75_LVBus1989417_production, 75_LVBus1989418_consumption, 75_LVBus1989418_production, 75_LVBus1989419_consumption, 75_LVBus1989419_production, 75_LVBus1989420_consumption, 75_LVBus1989420_production, 75_LVBus1989421_consumption, 75_LVBus1989421_production, 75_LVBus1990622_consumption, 75_LVBus1990622_production, 75_LVBus2007155_consumption, 75_LVBus2007155_production, 75_LVBus2007156_consumption, 75_LVBus2007156_production, 75_LVBus2007157_consumption, 75_LVBus2007157_production, 75_LVBus2007158_production, 75_LVBus2007159_consumption, 75_LVBus2007159_production, 75_LVBus2007160_consumption, 75_LVBus2007160_production, 75_LVBus2007161_production, 75_LVBus2007162_consumption, 75_LVBus2007162_production, 75_LVBus2011492_consumption, 75_LVBus2011492_production, 75_LVBus2011493_consumption, 75_LVBus2011493_production, 75_LVBus2011494_consumption, 75_LVBus2011494_production, 75_LVBus2011495_production, 75_LVBus2011496_consumption, 75_LVBus2011496_production, 75_LVBus2011497_consumption, 75_LVBus2011497_production, 75_LVBus2011498_consumption, 75_LVBus2011498_production, 75_LVBus2011499_consumption, 75_LVBus2011499_production, 75_LVBus2011500_consumption, 75_LVBus2011500_production, 75_LVBus2011501_consumption, 75_LVBus2011501_production, 75_LVBus2011502_consumption, 75_LVBus2011502_production, 75_LVBus2011503_consumption, 75_LVBus2011503_production, 75_LVBus2011504_consumption, 75_LVBus2011504_production, 75_LVBus2011505_consumption, 75_LVBus2011505_production, 75_LVBus2011506_production, 75_MVLV009176_consumption, 75_MVLV009176_production, 75_MVLV009184_consumption, 75_MVLV009184_production, 75_MVLV067377_consumption, 75_MVLV067377_production, 75_MVLV070397_consumption, 75_MVLV070397_production, 75_MVLV099197_consumption, 75_MVLV099197_production, 75_MVLV106479_consumption, 75_MVLV106479_production, 75_MVLV107944_consumption, 75_MVLV107944_production, 75_MVLV116462_consumption, 75_MVLV116462_production, 75_MVLV146358_consumption, 75_MVLV146358_production, 75_MVLV154864_consumption, 75_MVLV154864_production.

## 9. Data Quality Summary

**Total findings:** 459 (0 errors, 5 warnings, 454 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  873 of 1358 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.8 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  874 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795673_consumption`  
  Load '75_LVBus1795673_consumption' has phase imbalance of 240.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795276_consumption`  
  Load '75_LVBus1795276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795109_consumption`  
  Load '75_LVBus1795109_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795169_consumption`  
  Load '75_LVBus1795169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1925974_consumption`  
  Load '75_LVBus1925974_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795589_consumption`  
  Load '75_LVBus1795589_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795795_consumption`  
  Load '75_LVBus1795795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795806_consumption`  
  Load '75_LVBus1795806_consumption' has phase imbalance of 250.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795297_consumption`  
  Load '75_LVBus1795297_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795630_consumption`  
  Load '75_LVBus1795630_consumption' has phase imbalance of 285.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795291_consumption`  
  Load '75_LVBus1795291_consumption' has phase imbalance of 264.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795114_consumption`  
  Load '75_LVBus1795114_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795695_consumption`  
  Load '75_LVBus1795695_consumption' has phase imbalance of 131.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795120_consumption`  
  Load '75_LVBus1795120_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795437_consumption`  
  Load '75_LVBus1795437_consumption' has phase imbalance of 188.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795593_consumption`  
  Load '75_LVBus1795593_consumption' has phase imbalance of 89.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795341_consumption`  
  Load '75_LVBus1795341_consumption' has phase imbalance of 253.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795742_consumption`  
  Load '75_LVBus1795742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795378_consumption`  
  Load '75_LVBus1795378_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795546_consumption`  
  Load '75_LVBus1795546_consumption' has phase imbalance of 157.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795172_consumption`  
  Load '75_LVBus1795172_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795591_consumption`  
  Load '75_LVBus1795591_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795797_consumption`  
  Load '75_LVBus1795797_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795774_consumption`  
  Load '75_LVBus1795774_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795395_consumption`  
  Load '75_LVBus1795395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795796_consumption`  
  Load '75_LVBus1795796_consumption' has phase imbalance of 90.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795170_consumption`  
  Load '75_LVBus1795170_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795660_consumption`  
  Load '75_LVBus1795660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795442_consumption`  
  Load '75_LVBus1795442_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795078_consumption`  
  Load '75_LVBus1795078_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795368_consumption`  
  Load '75_LVBus1795368_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795342_consumption`  
  Load '75_LVBus1795342_consumption' has phase imbalance of 78.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795472_consumption`  
  Load '75_LVBus1795472_consumption' has phase imbalance of 267.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795686_consumption`  
  Load '75_LVBus1795686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795664_consumption`  
  Load '75_LVBus1795664_consumption' has phase imbalance of 50.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795665_consumption`  
  Load '75_LVBus1795665_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795051_consumption`  
  Load '75_LVBus1795051_consumption' has phase imbalance of 82.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795609_consumption`  
  Load '75_LVBus1795609_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795330_consumption`  
  Load '75_LVBus1795330_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795054_consumption`  
  Load '75_LVBus1795054_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795180_consumption`  
  Load '75_LVBus1795180_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795198_consumption`  
  Load '75_LVBus1795198_consumption' has phase imbalance of 29.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795050_consumption`  
  Load '75_LVBus1795050_consumption' has phase imbalance of 74.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795267_consumption`  
  Load '75_LVBus1795267_consumption' has phase imbalance of 146.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795765_consumption`  
  Load '75_LVBus1795765_consumption' has phase imbalance of 218.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795726_consumption`  
  Load '75_LVBus1795726_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795762_consumption`  
  Load '75_LVBus1795762_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1922180_consumption`  
  Load '75_LVBus1922180_consumption' has phase imbalance of 148.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795340_consumption`  
  Load '75_LVBus1795340_consumption' has phase imbalance of 68.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795725_consumption`  
  Load '75_LVBus1795725_consumption' has phase imbalance of 257.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795216_consumption`  
  Load '75_LVBus1795216_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2011495_consumption`  
  Load '75_LVBus2011495_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795162_consumption`  
  Load '75_LVBus1795162_consumption' has phase imbalance of 131.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795060_consumption`  
  Load '75_LVBus1795060_consumption' has phase imbalance of 230.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795656_consumption`  
  Load '75_LVBus1795656_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795657_consumption`  
  Load '75_LVBus1795657_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795448_consumption`  
  Load '75_LVBus1795448_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795331_consumption`  
  Load '75_LVBus1795331_consumption' has phase imbalance of 195.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795215_consumption`  
  Load '75_LVBus1795215_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795294_consumption`  
  Load '75_LVBus1795294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795116_consumption`  
  Load '75_LVBus1795116_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795631_consumption`  
  Load '75_LVBus1795631_consumption' has phase imbalance of 229.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795411_consumption`  
  Load '75_LVBus1795411_consumption' has phase imbalance of 266.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795479_consumption`  
  Load '75_LVBus1795479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1937807_consumption`  
  Load '75_LVBus1937807_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926454_consumption`  
  Load '75_LVBus1926454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795412_consumption`  
  Load '75_LVBus1795412_consumption' has phase imbalance of 43.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795507_consumption`  
  Load '75_LVBus1795507_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795811_consumption`  
  Load '75_LVBus1795811_consumption' has phase imbalance of 228.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795357_consumption`  
  Load '75_LVBus1795357_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1923817_consumption`  
  Load '75_LVBus1923817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795177_consumption`  
  Load '75_LVBus1795177_consumption' has phase imbalance of 229.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795810_consumption`  
  Load '75_LVBus1795810_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795058_consumption`  
  Load '75_LVBus1795058_consumption' has phase imbalance of 21.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795410_consumption`  
  Load '75_LVBus1795410_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795548_consumption`  
  Load '75_LVBus1795548_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795460_consumption`  
  Load '75_LVBus1795460_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795299_consumption`  
  Load '75_LVBus1795299_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795290_consumption`  
  Load '75_LVBus1795290_consumption' has phase imbalance of 237.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795175_consumption`  
  Load '75_LVBus1795175_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795278_consumption`  
  Load '75_LVBus1795278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795771_consumption`  
  Load '75_LVBus1795771_consumption' has phase imbalance of 169.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795617_consumption`  
  Load '75_LVBus1795617_consumption' has phase imbalance of 115.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795280_consumption`  
  Load '75_LVBus1795280_consumption' has phase imbalance of 256.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795484_consumption`  
  Load '75_LVBus1795484_consumption' has phase imbalance of 39.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795640_consumption`  
  Load '75_LVBus1795640_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795073_consumption`  
  Load '75_LVBus1795073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795121_consumption`  
  Load '75_LVBus1795121_consumption' has phase imbalance of 183.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795203_consumption`  
  Load '75_LVBus1795203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795124_consumption`  
  Load '75_LVBus1795124_consumption' has phase imbalance of 35.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795251_consumption`  
  Load '75_LVBus1795251_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795052_consumption`  
  Load '75_LVBus1795052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795659_consumption`  
  Load '75_LVBus1795659_consumption' has phase imbalance of 287.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795269_consumption`  
  Load '75_LVBus1795269_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795185_consumption`  
  Load '75_LVBus1795185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795279_consumption`  
  Load '75_LVBus1795279_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795426_consumption`  
  Load '75_LVBus1795426_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795623_consumption`  
  Load '75_LVBus1795623_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795428_consumption`  
  Load '75_LVBus1795428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795196_consumption`  
  Load '75_LVBus1795196_consumption' has phase imbalance of 144.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795602_consumption`  
  Load '75_LVBus1795602_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795579_consumption`  
  Load '75_LVBus1795579_consumption' has phase imbalance of 85.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795445_consumption`  
  Load '75_LVBus1795445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795351_consumption`  
  Load '75_LVBus1795351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795165_consumption`  
  Load '75_LVBus1795165_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795606_consumption`  
  Load '75_LVBus1795606_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795449_consumption`  
  Load '75_LVBus1795449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795287_consumption`  
  Load '75_LVBus1795287_consumption' has phase imbalance of 242.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795528_consumption`  
  Load '75_LVBus1795528_consumption' has phase imbalance of 252.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795429_consumption`  
  Load '75_LVBus1795429_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795304_consumption`  
  Load '75_LVBus1795304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795600_consumption`  
  Load '75_LVBus1795600_consumption' has phase imbalance of 292.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795443_consumption`  
  Load '75_LVBus1795443_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795350_consumption`  
  Load '75_LVBus1795350_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795611_consumption`  
  Load '75_LVBus1795611_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795754_consumption`  
  Load '75_LVBus1795754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795678_consumption`  
  Load '75_LVBus1795678_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795727_consumption`  
  Load '75_LVBus1795727_consumption' has phase imbalance of 117.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795212_consumption`  
  Load '75_LVBus1795212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795798_consumption`  
  Load '75_LVBus1795798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795503_consumption`  
  Load '75_LVBus1795503_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795141_consumption`  
  Load '75_LVBus1795141_consumption' has phase imbalance of 93.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795329_consumption`  
  Load '75_LVBus1795329_consumption' has phase imbalance of 291.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795760_consumption`  
  Load '75_LVBus1795760_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795324_consumption`  
  Load '75_LVBus1795324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795044_consumption`  
  Load '75_LVBus1795044_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795404_consumption`  
  Load '75_LVBus1795404_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795207_consumption`  
  Load '75_LVBus1795207_consumption' has phase imbalance of 51.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795712_consumption`  
  Load '75_LVBus1795712_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795808_consumption`  
  Load '75_LVBus1795808_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795144_consumption`  
  Load '75_LVBus1795144_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795130_consumption`  
  Load '75_LVBus1795130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795043_consumption`  
  Load '75_LVBus1795043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795482_consumption`  
  Load '75_LVBus1795482_consumption' has phase imbalance of 91.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795669_consumption`  
  Load '75_LVBus1795669_consumption' has phase imbalance of 128.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795478_consumption`  
  Load '75_LVBus1795478_consumption' has phase imbalance of 116.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795583_consumption`  
  Load '75_LVBus1795583_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795123_consumption`  
  Load '75_LVBus1795123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795349_consumption`  
  Load '75_LVBus1795349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795275_consumption`  
  Load '75_LVBus1795275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795508_consumption`  
  Load '75_LVBus1795508_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795432_consumption`  
  Load '75_LVBus1795432_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795134_consumption`  
  Load '75_LVBus1795134_consumption' has phase imbalance of 84.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795458_consumption`  
  Load '75_LVBus1795458_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795450_consumption`  
  Load '75_LVBus1795450_consumption' has phase imbalance of 197.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795752_consumption`  
  Load '75_LVBus1795752_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795800_consumption`  
  Load '75_LVBus1795800_consumption' has phase imbalance of 84.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795303_consumption`  
  Load '75_LVBus1795303_consumption' has phase imbalance of 217.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795362_consumption`  
  Load '75_LVBus1795362_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795633_consumption`  
  Load '75_LVBus1795633_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795436_consumption`  
  Load '75_LVBus1795436_consumption' has phase imbalance of 260.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795369_consumption`  
  Load '75_LVBus1795369_consumption' has phase imbalance of 275.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795666_consumption`  
  Load '75_LVBus1795666_consumption' has phase imbalance of 211.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795587_consumption`  
  Load '75_LVBus1795587_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795268_consumption`  
  Load '75_LVBus1795268_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795473_consumption`  
  Load '75_LVBus1795473_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795205_consumption`  
  Load '75_LVBus1795205_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795284_consumption`  
  Load '75_LVBus1795284_consumption' has phase imbalance of 234.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795255_consumption`  
  Load '75_LVBus1795255_consumption' has phase imbalance of 91.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795319_consumption`  
  Load '75_LVBus1795319_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795257_consumption`  
  Load '75_LVBus1795257_consumption' has phase imbalance of 78.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795086_consumption`  
  Load '75_LVBus1795086_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795553_consumption`  
  Load '75_LVBus1795553_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795603_consumption`  
  Load '75_LVBus1795603_consumption' has phase imbalance of 230.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795747_consumption`  
  Load '75_LVBus1795747_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795616_consumption`  
  Load '75_LVBus1795616_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795301_consumption`  
  Load '75_LVBus1795301_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795346_consumption`  
  Load '75_LVBus1795346_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795550_consumption`  
  Load '75_LVBus1795550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795626_consumption`  
  Load '75_LVBus1795626_consumption' has phase imbalance of 266.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795549_consumption`  
  Load '75_LVBus1795549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795256_consumption`  
  Load '75_LVBus1795256_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795336_consumption`  
  Load '75_LVBus1795336_consumption' has phase imbalance of 101.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795510_consumption`  
  Load '75_LVBus1795510_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795716_consumption`  
  Load '75_LVBus1795716_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795199_consumption`  
  Load '75_LVBus1795199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795158_consumption`  
  Load '75_LVBus1795158_consumption' has phase imbalance of 254.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795555_consumption`  
  Load '75_LVBus1795555_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795077_consumption`  
  Load '75_LVBus1795077_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795208_consumption`  
  Load '75_LVBus1795208_consumption' has phase imbalance of 40.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795292_consumption`  
  Load '75_LVBus1795292_consumption' has phase imbalance of 251.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795557_consumption`  
  Load '75_LVBus1795557_consumption' has phase imbalance of 262.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795745_consumption`  
  Load '75_LVBus1795745_consumption' has phase imbalance of 123.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795694_consumption`  
  Load '75_LVBus1795694_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795594_consumption`  
  Load '75_LVBus1795594_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795469_consumption`  
  Load '75_LVBus1795469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795681_consumption`  
  Load '75_LVBus1795681_consumption' has phase imbalance of 293.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795685_consumption`  
  Load '75_LVBus1795685_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795317_consumption`  
  Load '75_LVBus1795317_consumption' has phase imbalance of 189.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795112_consumption`  
  Load '75_LVBus1795112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795313_consumption`  
  Load '75_LVBus1795313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795661_consumption`  
  Load '75_LVBus1795661_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795485_consumption`  
  Load '75_LVBus1795485_consumption' has phase imbalance of 59.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795374_consumption`  
  Load '75_LVBus1795374_consumption' has phase imbalance of 222.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795288_consumption`  
  Load '75_LVBus1795288_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795764_consumption`  
  Load '75_LVBus1795764_consumption' has phase imbalance of 114.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795282_consumption`  
  Load '75_LVBus1795282_consumption' has phase imbalance of 201.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795576_consumption`  
  Load '75_LVBus1795576_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795302_consumption`  
  Load '75_LVBus1795302_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795802_consumption`  
  Load '75_LVBus1795802_consumption' has phase imbalance of 182.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795375_consumption`  
  Load '75_LVBus1795375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795168_consumption`  
  Load '75_LVBus1795168_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795111_consumption`  
  Load '75_LVBus1795111_consumption' has phase imbalance of 278.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795135_consumption`  
  Load '75_LVBus1795135_consumption' has phase imbalance of 191.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795463_consumption`  
  Load '75_LVBus1795463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795281_consumption`  
  Load '75_LVBus1795281_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795807_consumption`  
  Load '75_LVBus1795807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795580_consumption`  
  Load '75_LVBus1795580_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795597_consumption`  
  Load '75_LVBus1795597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795683_consumption`  
  Load '75_LVBus1795683_consumption' has phase imbalance of 188.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795333_consumption`  
  Load '75_LVBus1795333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795396_consumption`  
  Load '75_LVBus1795396_consumption' has phase imbalance of 244.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795254_consumption`  
  Load '75_LVBus1795254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795586_consumption`  
  Load '75_LVBus1795586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795692_consumption`  
  Load '75_LVBus1795692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795200_consumption`  
  Load '75_LVBus1795200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795610_consumption`  
  Load '75_LVBus1795610_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795184_consumption`  
  Load '75_LVBus1795184_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795544_consumption`  
  Load '75_LVBus1795544_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795663_consumption`  
  Load '75_LVBus1795663_consumption' has phase imbalance of 234.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795283_consumption`  
  Load '75_LVBus1795283_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795688_consumption`  
  Load '75_LVBus1795688_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795545_consumption`  
  Load '75_LVBus1795545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795446_consumption`  
  Load '75_LVBus1795446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795355_consumption`  
  Load '75_LVBus1795355_consumption' has phase imbalance of 176.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795126_consumption`  
  Load '75_LVBus1795126_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795405_consumption`  
  Load '75_LVBus1795405_consumption' has phase imbalance of 29.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926458_consumption`  
  Load '75_LVBus1926458_consumption' has phase imbalance of 193.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1951435_consumption`  
  Load '75_LVBus1951435_consumption' has phase imbalance of 222.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795621_consumption`  
  Load '75_LVBus1795621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795142_consumption`  
  Load '75_LVBus1795142_consumption' has phase imbalance of 74.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795163_consumption`  
  Load '75_LVBus1795163_consumption' has phase imbalance of 29.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795166_consumption`  
  Load '75_LVBus1795166_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795433_consumption`  
  Load '75_LVBus1795433_consumption' has phase imbalance of 219.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795143_consumption`  
  Load '75_LVBus1795143_consumption' has phase imbalance of 120.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795734_consumption`  
  Load '75_LVBus1795734_consumption' has phase imbalance of 123.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795085_consumption`  
  Load '75_LVBus1795085_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795687_consumption`  
  Load '75_LVBus1795687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1937808_consumption`  
  Load '75_LVBus1937808_consumption' has phase imbalance of 227.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795738_consumption`  
  Load '75_LVBus1795738_consumption' has phase imbalance of 188.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795132_consumption`  
  Load '75_LVBus1795132_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795667_consumption`  
  Load '75_LVBus1795667_consumption' has phase imbalance of 118.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795629_consumption`  
  Load '75_LVBus1795629_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795504_consumption`  
  Load '75_LVBus1795504_consumption' has phase imbalance of 161.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926463_consumption`  
  Load '75_LVBus1926463_consumption' has phase imbalance of 97.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795763_consumption`  
  Load '75_LVBus1795763_consumption' has phase imbalance of 126.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus2011506_consumption`  
  Load '75_LVBus2011506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795119_consumption`  
  Load '75_LVBus1795119_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795160_consumption`  
  Load '75_LVBus1795160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795298_consumption`  
  Load '75_LVBus1795298_consumption' has phase imbalance of 46.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795455_consumption`  
  Load '75_LVBus1795455_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795674_consumption`  
  Load '75_LVBus1795674_consumption' has phase imbalance of 41.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795619_consumption`  
  Load '75_LVBus1795619_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795407_consumption`  
  Load '75_LVBus1795407_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795079_consumption`  
  Load '75_LVBus1795079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795421_consumption`  
  Load '75_LVBus1795421_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795194_consumption`  
  Load '75_LVBus1795194_consumption' has phase imbalance of 65.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795751_consumption`  
  Load '75_LVBus1795751_consumption' has phase imbalance of 137.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795767_consumption`  
  Load '75_LVBus1795767_consumption' has phase imbalance of 259.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795732_consumption`  
  Load '75_LVBus1795732_consumption' has phase imbalance of 243.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926460_consumption`  
  Load '75_LVBus1926460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795533_consumption`  
  Load '75_LVBus1795533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795157_consumption`  
  Load '75_LVBus1795157_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795307_consumption`  
  Load '75_LVBus1795307_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795613_consumption`  
  Load '75_LVBus1795613_consumption' has phase imbalance of 42.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795506_consumption`  
  Load '75_LVBus1795506_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795084_consumption`  
  Load '75_LVBus1795084_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795590_consumption`  
  Load '75_LVBus1795590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795110_consumption`  
  Load '75_LVBus1795110_consumption' has phase imbalance of 229.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926466_consumption`  
  Load '75_LVBus1926466_consumption' has phase imbalance of 204.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795502_consumption`  
  Load '75_LVBus1795502_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795397_consumption`  
  Load '75_LVBus1795397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795438_consumption`  
  Load '75_LVBus1795438_consumption' has phase imbalance of 205.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795471_consumption`  
  Load '75_LVBus1795471_consumption' has phase imbalance of 128.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795420_consumption`  
  Load '75_LVBus1795420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795195_consumption`  
  Load '75_LVBus1795195_consumption' has phase imbalance of 86.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795321_consumption`  
  Load '75_LVBus1795321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795306_consumption`  
  Load '75_LVBus1795306_consumption' has phase imbalance of 105.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795634_consumption`  
  Load '75_LVBus1795634_consumption' has phase imbalance of 119.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795750_consumption`  
  Load '75_LVBus1795750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795183_consumption`  
  Load '75_LVBus1795183_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795620_consumption`  
  Load '75_LVBus1795620_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795273_consumption`  
  Load '75_LVBus1795273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795188_consumption`  
  Load '75_LVBus1795188_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795145_consumption`  
  Load '75_LVBus1795145_consumption' has phase imbalance of 184.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795537_consumption`  
  Load '75_LVBus1795537_consumption' has phase imbalance of 218.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795710_consumption`  
  Load '75_LVBus1795710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1951430_consumption`  
  Load '75_LVBus1951430_consumption' has phase imbalance of 222.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795315_consumption`  
  Load '75_LVBus1795315_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795042_consumption`  
  Load '75_LVBus1795042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795636_consumption`  
  Load '75_LVBus1795636_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1951434_consumption`  
  Load '75_LVBus1951434_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795691_consumption`  
  Load '75_LVBus1795691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795770_consumption`  
  Load '75_LVBus1795770_consumption' has phase imbalance of 138.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795068_consumption`  
  Load '75_LVBus1795068_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795740_consumption`  
  Load '75_LVBus1795740_consumption' has phase imbalance of 121.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795289_consumption`  
  Load '75_LVBus1795289_consumption' has phase imbalance of 231.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795803_consumption`  
  Load '75_LVBus1795803_consumption' has phase imbalance of 272.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795316_consumption`  
  Load '75_LVBus1795316_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795059_consumption`  
  Load '75_LVBus1795059_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795138_consumption`  
  Load '75_LVBus1795138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795474_consumption`  
  Load '75_LVBus1795474_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795675_consumption`  
  Load '75_LVBus1795675_consumption' has phase imbalance of 259.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795359_consumption`  
  Load '75_LVBus1795359_consumption' has phase imbalance of 254.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795053_consumption`  
  Load '75_LVBus1795053_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795731_consumption`  
  Load '75_LVBus1795731_consumption' has phase imbalance of 253.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795261_consumption`  
  Load '75_LVBus1795261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795662_consumption`  
  Load '75_LVBus1795662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795441_consumption`  
  Load '75_LVBus1795441_consumption' has phase imbalance of 64.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795679_consumption`  
  Load '75_LVBus1795679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795605_consumption`  
  Load '75_LVBus1795605_consumption' has phase imbalance of 55.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795481_consumption`  
  Load '75_LVBus1795481_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795772_consumption`  
  Load '75_LVBus1795772_consumption' has phase imbalance of 168.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795769_consumption`  
  Load '75_LVBus1795769_consumption' has phase imbalance of 122.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795628_consumption`  
  Load '75_LVBus1795628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795403_consumption`  
  Load '75_LVBus1795403_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795155_consumption`  
  Load '75_LVBus1795155_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795483_consumption`  
  Load '75_LVBus1795483_consumption' has phase imbalance of 209.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926457_consumption`  
  Load '75_LVBus1926457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795598_consumption`  
  Load '75_LVBus1795598_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795693_consumption`  
  Load '75_LVBus1795693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795171_consumption`  
  Load '75_LVBus1795171_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795529_consumption`  
  Load '75_LVBus1795529_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795259_consumption`  
  Load '75_LVBus1795259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795729_consumption`  
  Load '75_LVBus1795729_consumption' has phase imbalance of 222.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795147_consumption`  
  Load '75_LVBus1795147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795358_consumption`  
  Load '75_LVBus1795358_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926465_consumption`  
  Load '75_LVBus1926465_consumption' has phase imbalance of 209.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795332_consumption`  
  Load '75_LVBus1795332_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795182_consumption`  
  Load '75_LVBus1795182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795739_consumption`  
  Load '75_LVBus1795739_consumption' has phase imbalance of 45.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795159_consumption`  
  Load '75_LVBus1795159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795065_consumption`  
  Load '75_LVBus1795065_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795486_consumption`  
  Load '75_LVBus1795486_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795643_consumption`  
  Load '75_LVBus1795643_consumption' has phase imbalance of 252.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795423_consumption`  
  Load '75_LVBus1795423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795622_consumption`  
  Load '75_LVBus1795622_consumption' has phase imbalance of 108.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795066_consumption`  
  Load '75_LVBus1795066_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795136_consumption`  
  Load '75_LVBus1795136_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795776_consumption`  
  Load '75_LVBus1795776_consumption' has phase imbalance of 60.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795768_consumption`  
  Load '75_LVBus1795768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795409_consumption`  
  Load '75_LVBus1795409_consumption' has phase imbalance of 111.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795599_consumption`  
  Load '75_LVBus1795599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795334_consumption`  
  Load '75_LVBus1795334_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795361_consumption`  
  Load '75_LVBus1795361_consumption' has phase imbalance of 140.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795793_consumption`  
  Load '75_LVBus1795793_consumption' has phase imbalance of 94.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795173_consumption`  
  Load '75_LVBus1795173_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795743_consumption`  
  Load '75_LVBus1795743_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795399_consumption`  
  Load '75_LVBus1795399_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795757_consumption`  
  Load '75_LVBus1795757_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795125_consumption`  
  Load '75_LVBus1795125_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795440_consumption`  
  Load '75_LVBus1795440_consumption' has phase imbalance of 224.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795627_consumption`  
  Load '75_LVBus1795627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795775_consumption`  
  Load '75_LVBus1795775_consumption' has phase imbalance of 60.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795146_consumption`  
  Load '75_LVBus1795146_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795176_consumption`  
  Load '75_LVBus1795176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795804_consumption`  
  Load '75_LVBus1795804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795638_consumption`  
  Load '75_LVBus1795638_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795326_consumption`  
  Load '75_LVBus1795326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795217_consumption`  
  Load '75_LVBus1795217_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795367_consumption`  
  Load '75_LVBus1795367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795596_consumption`  
  Load '75_LVBus1795596_consumption' has phase imbalance of 65.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795554_consumption`  
  Load '75_LVBus1795554_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795311_consumption`  
  Load '75_LVBus1795311_consumption' has phase imbalance of 261.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795477_consumption`  
  Load '75_LVBus1795477_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795635_consumption`  
  Load '75_LVBus1795635_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795295_consumption`  
  Load '75_LVBus1795295_consumption' has phase imbalance of 46.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795509_consumption`  
  Load '75_LVBus1795509_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795435_consumption`  
  Load '75_LVBus1795435_consumption' has phase imbalance of 126.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795604_consumption`  
  Load '75_LVBus1795604_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795401_consumption`  
  Load '75_LVBus1795401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795286_consumption`  
  Load '75_LVBus1795286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795347_consumption`  
  Load '75_LVBus1795347_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795372_consumption`  
  Load '75_LVBus1795372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795690_consumption`  
  Load '75_LVBus1795690_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795083_consumption`  
  Load '75_LVBus1795083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795644_consumption`  
  Load '75_LVBus1795644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795462_consumption`  
  Load '75_LVBus1795462_consumption' has phase imbalance of 124.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795697_consumption`  
  Load '75_LVBus1795697_consumption' has phase imbalance of 269.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795415_consumption`  
  Load '75_LVBus1795415_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795186_consumption`  
  Load '75_LVBus1795186_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795680_consumption`  
  Load '75_LVBus1795680_consumption' has phase imbalance of 135.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795744_consumption`  
  Load '75_LVBus1795744_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1926462_consumption`  
  Load '75_LVBus1926462_consumption' has phase imbalance of 147.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795312_consumption`  
  Load '75_LVBus1795312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795139_consumption`  
  Load '75_LVBus1795139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795377_consumption`  
  Load '75_LVBus1795377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795373_consumption`  
  Load '75_LVBus1795373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795152_consumption`  
  Load '75_LVBus1795152_consumption' has phase imbalance of 248.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795197_consumption`  
  Load '75_LVBus1795197_consumption' has phase imbalance of 56.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795709_consumption`  
  Load '75_LVBus1795709_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795588_consumption`  
  Load '75_LVBus1795588_consumption' has phase imbalance of 56.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795252_consumption`  
  Load '75_LVBus1795252_consumption' has phase imbalance of 92.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795328_consumption`  
  Load '75_LVBus1795328_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795325_consumption`  
  Load '75_LVBus1795325_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795352_consumption`  
  Load '75_LVBus1795352_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795305_consumption`  
  Load '75_LVBus1795305_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795728_consumption`  
  Load '75_LVBus1795728_consumption' has phase imbalance of 281.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795759_consumption`  
  Load '75_LVBus1795759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795206_consumption`  
  Load '75_LVBus1795206_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795431_consumption`  
  Load '75_LVBus1795431_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795127_consumption`  
  Load '75_LVBus1795127_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795181_consumption`  
  Load '75_LVBus1795181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795310_consumption`  
  Load '75_LVBus1795310_consumption' has phase imbalance of 135.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795614_consumption`  
  Load '75_LVBus1795614_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795354_consumption`  
  Load '75_LVBus1795354_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795582_consumption`  
  Load '75_LVBus1795582_consumption' has phase imbalance of 239.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795556_consumption`  
  Load '75_LVBus1795556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795309_consumption`  
  Load '75_LVBus1795309_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795400_consumption`  
  Load '75_LVBus1795400_consumption' has phase imbalance of 256.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795353_consumption`  
  Load '75_LVBus1795353_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795639_consumption`  
  Load '75_LVBus1795639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795641_consumption`  
  Load '75_LVBus1795641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795213_consumption`  
  Load '75_LVBus1795213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795547_consumption`  
  Load '75_LVBus1795547_consumption' has phase imbalance of 120.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795108_consumption`  
  Load '75_LVBus1795108_consumption' has phase imbalance of 217.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795461_consumption`  
  Load '75_LVBus1795461_consumption' has phase imbalance of 118.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795076_consumption`  
  Load '75_LVBus1795076_consumption' has phase imbalance of 29.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795187_consumption`  
  Load '75_LVBus1795187_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795398_consumption`  
  Load '75_LVBus1795398_consumption' has phase imbalance of 106.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795575_consumption`  
  Load '75_LVBus1795575_consumption' has phase imbalance of 246.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795266_consumption`  
  Load '75_LVBus1795266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795581_consumption`  
  Load '75_LVBus1795581_consumption' has phase imbalance of 269.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795335_consumption`  
  Load '75_LVBus1795335_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795608_consumption`  
  Load '75_LVBus1795608_consumption' has phase imbalance of 232.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795677_consumption`  
  Load '75_LVBus1795677_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795154_consumption`  
  Load '75_LVBus1795154_consumption' has phase imbalance of 45.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795584_consumption`  
  Load '75_LVBus1795584_consumption' has phase imbalance of 36.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795293_consumption`  
  Load '75_LVBus1795293_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795805_consumption`  
  Load '75_LVBus1795805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1795417_consumption`  
  Load '75_LVBus1795417_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1358 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1795071' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1795512' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1795092' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1795563' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1795701' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1795488' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1795071' (LV, 0.24 kV) has an electrical reach of 18.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus1795540' (LV, 0.24 kV) has an electrical reach of 26.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  786 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  298 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1795042_consumption, 75_LVBus1795043_consumption, 75_LVBus1795044_consumption, 75_LVBus1795052_consumption, 75_LVBus1795054_consumption, 75_LVBus1795059_consumption, 75_LVBus1795065_consumption, 75_LVBus1795073_consumption, 75_LVBus1795078_consumption, 75_LVBus1795079_consumption, 75_LVBus1795083_consumption, 75_LVBus1795084_consumption, 75_LVBus1795085_consumption, 75_LVBus1795086_consumption, 75_LVBus1795108_consumption, 75_LVBus1795110_consumption, 75_LVBus1795111_consumption, 75_LVBus1795112_consumption, 75_LVBus1795114_consumption, 75_LVBus1795116_consumption, 75_LVBus1795119_consumption, 75_LVBus1795121_consumption, 75_LVBus1795123_consumption, 75_LVBus1795126_consumption, 75_LVBus1795127_consumption, 75_LVBus1795130_consumption, 75_LVBus1795136_consumption, 75_LVBus1795138_consumption, 75_LVBus1795139_consumption, 75_LVBus1795144_consumption, 75_LVBus1795145_consumption, 75_LVBus1795146_consumption, 75_LVBus1795147_consumption, 75_LVBus1795152_consumption, 75_LVBus1795157_consumption, 75_LVBus1795158_consumption, 75_LVBus1795159_consumption, 75_LVBus1795160_consumption, 75_LVBus1795165_consumption, 75_LVBus1795166_consumption, 75_LVBus1795168_consumption, 75_LVBus1795169_consumption, 75_LVBus1795170_consumption, 75_LVBus1795171_consumption, 75_LVBus1795172_consumption, 75_LVBus1795173_consumption, 75_LVBus1795175_consumption, 75_LVBus1795176_consumption, 75_LVBus1795177_consumption, 75_LVBus1795180_consumption, 75_LVBus1795181_consumption, 75_LVBus1795182_consumption, 75_LVBus1795184_consumption, 75_LVBus1795185_consumption, 75_LVBus1795187_consumption, 75_LVBus1795199_consumption, 75_LVBus1795200_consumption, 75_LVBus1795203_consumption, 75_LVBus1795205_consumption, 75_LVBus1795206_consumption, 75_LVBus1795212_consumption, 75_LVBus1795213_consumption, 75_LVBus1795216_consumption, 75_LVBus1795217_consumption, 75_LVBus1795251_consumption, 75_LVBus1795254_consumption, 75_LVBus1795256_consumption, 75_LVBus1795259_consumption, 75_LVBus1795261_consumption, 75_LVBus1795266_consumption, 75_LVBus1795268_consumption, 75_LVBus1795269_consumption, 75_LVBus1795273_consumption, 75_LVBus1795275_consumption, 75_LVBus1795276_consumption, 75_LVBus1795278_consumption, 75_LVBus1795279_consumption, 75_LVBus1795281_consumption, 75_LVBus1795283_consumption, 75_LVBus1795284_consumption, 75_LVBus1795286_consumption, 75_LVBus1795287_consumption, 75_LVBus1795288_consumption, 75_LVBus1795289_consumption, 75_LVBus1795290_consumption, 75_LVBus1795291_consumption, 75_LVBus1795292_consumption, 75_LVBus1795293_consumption, 75_LVBus1795294_consumption, 75_LVBus1795297_consumption, 75_LVBus1795301_consumption, 75_LVBus1795302_consumption, 75_LVBus1795303_consumption, 75_LVBus1795304_consumption, 75_LVBus1795305_consumption, 75_LVBus1795311_consumption, 75_LVBus1795312_consumption, 75_LVBus1795313_consumption, 75_LVBus1795315_consumption, 75_LVBus1795316_consumption, 75_LVBus1795317_consumption, 75_LVBus1795319_consumption, 75_LVBus1795321_consumption, 75_LVBus1795324_consumption, 75_LVBus1795325_consumption, 75_LVBus1795326_consumption, 75_LVBus1795328_consumption, 75_LVBus1795329_consumption, 75_LVBus1795331_consumption, 75_LVBus1795332_consumption, 75_LVBus1795333_consumption, 75_LVBus1795334_consumption, 75_LVBus1795335_consumption, 75_LVBus1795341_consumption, 75_LVBus1795347_consumption, 75_LVBus1795349_consumption, 75_LVBus1795350_consumption, 75_LVBus1795351_consumption, 75_LVBus1795352_consumption, 75_LVBus1795353_consumption, 75_LVBus1795354_consumption, 75_LVBus1795357_consumption, 75_LVBus1795362_consumption, 75_LVBus1795367_consumption, 75_LVBus1795369_consumption, 75_LVBus1795372_consumption, 75_LVBus1795373_consumption, 75_LVBus1795375_consumption, 75_LVBus1795377_consumption, 75_LVBus1795378_consumption, 75_LVBus1795395_consumption, 75_LVBus1795396_consumption, 75_LVBus1795397_consumption, 75_LVBus1795399_consumption, 75_LVBus1795400_consumption, 75_LVBus1795401_consumption, 75_LVBus1795404_consumption, 75_LVBus1795410_consumption, 75_LVBus1795415_consumption, 75_LVBus1795417_consumption, 75_LVBus1795420_consumption, 75_LVBus1795423_consumption, 75_LVBus1795426_consumption, 75_LVBus1795428_consumption, 75_LVBus1795429_consumption, 75_LVBus1795431_consumption, 75_LVBus1795432_consumption, 75_LVBus1795433_consumption, 75_LVBus1795436_consumption, 75_LVBus1795437_consumption, 75_LVBus1795438_consumption, 75_LVBus1795440_consumption, 75_LVBus1795443_consumption, 75_LVBus1795445_consumption, 75_LVBus1795446_consumption, 75_LVBus1795448_consumption, 75_LVBus1795449_consumption, 75_LVBus1795450_consumption, 75_LVBus1795455_consumption, 75_LVBus1795458_consumption, 75_LVBus1795460_consumption, 75_LVBus1795463_consumption, 75_LVBus1795469_consumption, 75_LVBus1795472_consumption, 75_LVBus1795479_consumption, 75_LVBus1795481_consumption, 75_LVBus1795483_consumption, 75_LVBus1795486_consumption, 75_LVBus1795503_consumption, 75_LVBus1795504_consumption, 75_LVBus1795506_consumption, 75_LVBus1795507_consumption, 75_LVBus1795509_consumption, 75_LVBus1795528_consumption, 75_LVBus1795529_consumption, 75_LVBus1795533_consumption, 75_LVBus1795537_consumption, 75_LVBus1795544_consumption, 75_LVBus1795545_consumption, 75_LVBus1795548_consumption, 75_LVBus1795549_consumption, 75_LVBus1795550_consumption, 75_LVBus1795553_consumption, 75_LVBus1795555_consumption, 75_LVBus1795556_consumption, 75_LVBus1795557_consumption, 75_LVBus1795575_consumption, 75_LVBus1795576_consumption, 75_LVBus1795580_consumption, 75_LVBus1795581_consumption, 75_LVBus1795582_consumption, 75_LVBus1795586_consumption, 75_LVBus1795587_consumption, 75_LVBus1795589_consumption, 75_LVBus1795590_consumption, 75_LVBus1795591_consumption, 75_LVBus1795594_consumption, 75_LVBus1795597_consumption, 75_LVBus1795599_consumption, 75_LVBus1795600_consumption, 75_LVBus1795602_consumption, 75_LVBus1795603_consumption, 75_LVBus1795604_consumption, 75_LVBus1795606_consumption, 75_LVBus1795608_consumption, 75_LVBus1795609_consumption, 75_LVBus1795611_consumption, 75_LVBus1795614_consumption, 75_LVBus1795616_consumption, 75_LVBus1795619_consumption, 75_LVBus1795620_consumption, 75_LVBus1795621_consumption, 75_LVBus1795623_consumption, 75_LVBus1795626_consumption, 75_LVBus1795627_consumption, 75_LVBus1795628_consumption, 75_LVBus1795629_consumption, 75_LVBus1795630_consumption, 75_LVBus1795631_consumption, 75_LVBus1795635_consumption, 75_LVBus1795638_consumption, 75_LVBus1795639_consumption, 75_LVBus1795640_consumption, 75_LVBus1795641_consumption, 75_LVBus1795643_consumption, 75_LVBus1795644_consumption, 75_LVBus1795659_consumption, 75_LVBus1795660_consumption, 75_LVBus1795661_consumption, 75_LVBus1795662_consumption, 75_LVBus1795663_consumption, 75_LVBus1795665_consumption, 75_LVBus1795666_consumption, 75_LVBus1795673_consumption, 75_LVBus1795675_consumption, 75_LVBus1795677_consumption, 75_LVBus1795678_consumption, 75_LVBus1795679_consumption, 75_LVBus1795681_consumption, 75_LVBus1795683_consumption, 75_LVBus1795685_consumption, 75_LVBus1795686_consumption, 75_LVBus1795687_consumption, 75_LVBus1795688_consumption, 75_LVBus1795690_consumption, 75_LVBus1795691_consumption, 75_LVBus1795692_consumption, 75_LVBus1795693_consumption, 75_LVBus1795694_consumption, 75_LVBus1795697_consumption, 75_LVBus1795710_consumption, 75_LVBus1795712_consumption, 75_LVBus1795716_consumption, 75_LVBus1795725_consumption, 75_LVBus1795726_consumption, 75_LVBus1795728_consumption, 75_LVBus1795729_consumption, 75_LVBus1795731_consumption, 75_LVBus1795732_consumption, 75_LVBus1795738_consumption, 75_LVBus1795742_consumption, 75_LVBus1795743_consumption, 75_LVBus1795747_consumption, 75_LVBus1795750_consumption, 75_LVBus1795754_consumption, 75_LVBus1795759_consumption, 75_LVBus1795765_consumption, 75_LVBus1795767_consumption, 75_LVBus1795768_consumption, 75_LVBus1795771_consumption, 75_LVBus1795772_consumption, 75_LVBus1795774_consumption, 75_LVBus1795795_consumption, 75_LVBus1795797_consumption, 75_LVBus1795798_consumption, 75_LVBus1795802_consumption, 75_LVBus1795803_consumption, 75_LVBus1795804_consumption, 75_LVBus1795805_consumption, 75_LVBus1795806_consumption, 75_LVBus1795807_consumption, 75_LVBus1795808_consumption, 75_LVBus1795811_consumption, 75_LVBus1923817_consumption, 75_LVBus1925974_consumption, 75_LVBus1926454_consumption, 75_LVBus1926457_consumption, 75_LVBus1926458_consumption, 75_LVBus1926460_consumption, 75_LVBus1926465_consumption, 75_LVBus1926466_consumption, 75_LVBus1937807_consumption, 75_LVBus1937808_consumption, 75_LVBus1951430_consumption, 75_LVBus1951434_consumption, 75_LVBus1951435_consumption, 75_LVBus2011495_consumption, 75_LVBus2011506_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  679 group(s) of loads (1358 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (2 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  874 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1795042_production, 75_LVBus1795043_production, 75_LVBus1795044_production, 75_LVBus1795045_consumption, 75_LVBus1795045_production, 75_LVBus1795046_consumption, 75_LVBus1795046_production, 75_LVBus1795047_consumption, 75_LVBus1795047_production, 75_LVBus1795049_consumption, 75_LVBus1795049_production, 75_LVBus1795050_production, 75_LVBus1795051_production, 75_LVBus1795052_production, 75_LVBus1795053_production, 75_LVBus1795054_production, 75_LVBus1795056_consumption, 75_LVBus1795056_production, 75_LVBus1795057_consumption, 75_LVBus1795057_production, 75_LVBus1795058_production, 75_LVBus1795059_production, 75_LVBus1795060_production, 75_LVBus1795061_consumption, 75_LVBus1795061_production, 75_LVBus1795062_consumption, 75_LVBus1795062_production, 75_LVBus1795064_consumption, 75_LVBus1795064_production, 75_LVBus1795065_production, 75_LVBus1795066_production, 75_LVBus1795068_production, 75_LVBus1795069_consumption, 75_LVBus1795069_production, 75_LVBus1795071_production, 75_LVBus1795073_production, 75_LVBus1795075_consumption, 75_LVBus1795075_production, 75_LVBus1795076_production, 75_LVBus1795077_production, 75_LVBus1795078_production, 75_LVBus1795079_production, 75_LVBus1795081_consumption, 75_LVBus1795081_production, 75_LVBus1795082_production, 75_LVBus1795083_production, 75_LVBus1795084_production, 75_LVBus1795085_production, 75_LVBus1795086_production, 75_LVBus1795088_consumption, 75_LVBus1795088_production, 75_LVBus1795089_production, 75_LVBus1795090_consumption, 75_LVBus1795090_production, 75_LVBus1795092_consumption, 75_LVBus1795092_production, 75_LVBus1795094_consumption, 75_LVBus1795094_production, 75_LVBus1795096_consumption, 75_LVBus1795096_production, 75_LVBus1795098_consumption, 75_LVBus1795098_production, 75_LVBus1795100_production, 75_LVBus1795102_consumption, 75_LVBus1795102_production, 75_LVBus1795104_consumption, 75_LVBus1795104_production, 75_LVBus1795106_consumption, 75_LVBus1795106_production, 75_LVBus1795108_production, 75_LVBus1795109_production, 75_LVBus1795110_production, 75_LVBus1795111_production, 75_LVBus1795112_production, 75_LVBus1795113_consumption, 75_LVBus1795113_production, 75_LVBus1795114_production, 75_LVBus1795116_production, 75_LVBus1795117_consumption, 75_LVBus1795117_production, 75_LVBus1795118_consumption, 75_LVBus1795118_production, 75_LVBus1795119_production, 75_LVBus1795120_production, 75_LVBus1795121_production, 75_LVBus1795123_production, 75_LVBus1795124_production, 75_LVBus1795125_production, 75_LVBus1795126_production, 75_LVBus1795127_production, 75_LVBus1795129_consumption, 75_LVBus1795129_production, 75_LVBus1795130_production, 75_LVBus1795131_production, 75_LVBus1795132_production, 75_LVBus1795133_production, 75_LVBus1795134_production, 75_LVBus1795135_production, 75_LVBus1795136_production, 75_LVBus1795138_production, 75_LVBus1795139_production, 75_LVBus1795140_consumption, 75_LVBus1795140_production, 75_LVBus1795141_production, 75_LVBus1795142_production, 75_LVBus1795143_production, 75_LVBus1795144_production, 75_LVBus1795145_production, 75_LVBus1795146_production, 75_LVBus1795147_production, 75_LVBus1795148_consumption, 75_LVBus1795148_production, 75_LVBus1795149_consumption, 75_LVBus1795149_production, 75_LVBus1795152_production, 75_LVBus1795153_consumption, 75_LVBus1795153_production, 75_LVBus1795154_production, 75_LVBus1795155_production, 75_LVBus1795157_production, 75_LVBus1795158_production, 75_LVBus1795159_production, 75_LVBus1795160_production, 75_LVBus1795162_production, 75_LVBus1795163_production, 75_LVBus1795165_production, 75_LVBus1795166_production, 75_LVBus1795168_production, 75_LVBus1795169_production, 75_LVBus1795170_production, 75_LVBus1795171_production, 75_LVBus1795172_production, 75_LVBus1795173_production, 75_LVBus1795175_production, 75_LVBus1795176_production, 75_LVBus1795177_production, 75_LVBus1795178_consumption, 75_LVBus1795178_production, 75_LVBus1795180_production, 75_LVBus1795181_production, 75_LVBus1795182_production, 75_LVBus1795183_production, 75_LVBus1795184_production, 75_LVBus1795185_production, 75_LVBus1795186_production, 75_LVBus1795187_production, 75_LVBus1795188_production, 75_LVBus1795189_consumption, 75_LVBus1795189_production, 75_LVBus1795190_consumption, 75_LVBus1795190_production, 75_LVBus1795194_production, 75_LVBus1795195_production, 75_LVBus1795196_production, 75_LVBus1795197_production, 75_LVBus1795198_production, 75_LVBus1795199_production, 75_LVBus1795200_production, 75_LVBus1795201_consumption, 75_LVBus1795201_production, 75_LVBus1795202_consumption, 75_LVBus1795202_production, 75_LVBus1795203_production, 75_LVBus1795205_production, 75_LVBus1795206_production, 75_LVBus1795207_production, 75_LVBus1795208_production, 75_LVBus1795210_production, 75_LVBus1795212_production, 75_LVBus1795213_production, 75_LVBus1795214_consumption, 75_LVBus1795214_production, 75_LVBus1795215_production, 75_LVBus1795216_production, 75_LVBus1795217_production, 75_LVBus1795218_consumption, 75_LVBus1795218_production, 75_LVBus1795220_production, 75_LVBus1795221_production, 75_LVBus1795222_production, 75_LVBus1795224_consumption, 75_LVBus1795224_production, 75_LVBus1795225_production, 75_LVBus1795226_production, 75_LVBus1795227_production, 75_LVBus1795229_consumption, 75_LVBus1795229_production, 75_LVBus1795230_consumption, 75_LVBus1795230_production, 75_LVBus1795231_production, 75_LVBus1795232_production, 75_LVBus1795233_consumption, 75_LVBus1795233_production, 75_LVBus1795235_consumption, 75_LVBus1795235_production, 75_LVBus1795237_consumption, 75_LVBus1795237_production, 75_LVBus1795238_production, 75_LVBus1795239_production, 75_LVBus1795241_consumption, 75_LVBus1795241_production, 75_LVBus1795242_production, 75_LVBus1795244_consumption, 75_LVBus1795244_production, 75_LVBus1795245_consumption, 75_LVBus1795245_production, 75_LVBus1795246_consumption, 75_LVBus1795246_production, 75_LVBus1795247_production, 75_LVBus1795249_production, 75_LVBus1795251_production, 75_LVBus1795252_production, 75_LVBus1795254_production, 75_LVBus1795255_production, 75_LVBus1795256_production, 75_LVBus1795257_production, 75_LVBus1795259_production, 75_LVBus1795260_consumption, 75_LVBus1795260_production, 75_LVBus1795261_production, 75_LVBus1795262_production, 75_LVBus1795263_production, 75_LVBus1795264_consumption, 75_LVBus1795264_production, 75_LVBus1795265_consumption, 75_LVBus1795265_production, 75_LVBus1795266_production, 75_LVBus1795267_production, 75_LVBus1795268_production, 75_LVBus1795269_production, 75_LVBus1795271_consumption, 75_LVBus1795271_production, 75_LVBus1795273_production, 75_LVBus1795274_consumption, 75_LVBus1795274_production, 75_LVBus1795275_production, 75_LVBus1795276_production, 75_LVBus1795278_production, 75_LVBus1795279_production, 75_LVBus1795280_production, 75_LVBus1795281_production, 75_LVBus1795282_production, 75_LVBus1795283_production, 75_LVBus1795284_production, 75_LVBus1795286_production, 75_LVBus1795287_production, 75_LVBus1795288_production, 75_LVBus1795289_production, 75_LVBus1795290_production, 75_LVBus1795291_production, 75_LVBus1795292_production, 75_LVBus1795293_production, 75_LVBus1795294_production, 75_LVBus1795295_production, 75_LVBus1795297_production, 75_LVBus1795298_production, 75_LVBus1795299_production, 75_LVBus1795301_production, 75_LVBus1795302_production, 75_LVBus1795303_production, 75_LVBus1795304_production, 75_LVBus1795305_production, 75_LVBus1795306_production, 75_LVBus1795307_production, 75_LVBus1795309_production, 75_LVBus1795310_production, 75_LVBus1795311_production, 75_LVBus1795312_production, 75_LVBus1795313_production, 75_LVBus1795314_consumption, 75_LVBus1795314_production, 75_LVBus1795315_production, 75_LVBus1795316_production, 75_LVBus1795317_production, 75_LVBus1795319_production, 75_LVBus1795320_consumption, 75_LVBus1795320_production, 75_LVBus1795321_production, 75_LVBus1795323_consumption, 75_LVBus1795323_production, 75_LVBus1795324_production, 75_LVBus1795325_production, 75_LVBus1795326_production, 75_LVBus1795327_consumption, 75_LVBus1795327_production, 75_LVBus1795328_production, 75_LVBus1795329_production, 75_LVBus1795330_production, 75_LVBus1795331_production, 75_LVBus1795332_production, 75_LVBus1795333_production, 75_LVBus1795334_production, 75_LVBus1795335_production, 75_LVBus1795336_production, 75_LVBus1795338_consumption, 75_LVBus1795338_production, 75_LVBus1795339_consumption, 75_LVBus1795339_production, 75_LVBus1795340_production, 75_LVBus1795341_production, 75_LVBus1795342_production, 75_LVBus1795346_production, 75_LVBus1795347_production, 75_LVBus1795349_production, 75_LVBus1795350_production, 75_LVBus1795351_production, 75_LVBus1795352_production, 75_LVBus1795353_production, 75_LVBus1795354_production, 75_LVBus1795355_production, 75_LVBus1795357_production, 75_LVBus1795358_production, 75_LVBus1795359_production, 75_LVBus1795361_production, 75_LVBus1795362_production, 75_LVBus1795364_consumption, 75_LVBus1795364_production, 75_LVBus1795365_consumption, 75_LVBus1795365_production, 75_LVBus1795366_consumption, 75_LVBus1795366_production, 75_LVBus1795367_production, 75_LVBus1795368_production, 75_LVBus1795369_production, 75_LVBus1795370_consumption, 75_LVBus1795370_production, 75_LVBus1795371_consumption, 75_LVBus1795371_production, 75_LVBus1795372_production, 75_LVBus1795373_production, 75_LVBus1795374_production, 75_LVBus1795375_production, 75_LVBus1795376_consumption, 75_LVBus1795376_production, 75_LVBus1795377_production, 75_LVBus1795378_production, 75_LVBus1795380_consumption, 75_LVBus1795380_production, 75_LVBus1795381_consumption, 75_LVBus1795381_production, 75_LVBus1795382_consumption, 75_LVBus1795382_production, 75_LVBus1795383_consumption, 75_LVBus1795383_production, 75_LVBus1795385_consumption, 75_LVBus1795385_production, 75_LVBus1795386_consumption, 75_LVBus1795386_production, 75_LVBus1795387_consumption, 75_LVBus1795387_production, 75_LVBus1795388_consumption, 75_LVBus1795388_production, 75_LVBus1795389_consumption, 75_LVBus1795389_production, 75_LVBus1795390_consumption, 75_LVBus1795390_production, 75_LVBus1795395_production, 75_LVBus1795396_production, 75_LVBus1795397_production, 75_LVBus1795398_production, 75_LVBus1795399_production, 75_LVBus1795400_production, 75_LVBus1795401_production, 75_LVBus1795403_production, 75_LVBus1795404_production, 75_LVBus1795405_production, 75_LVBus1795406_production, 75_LVBus1795407_production, 75_LVBus1795409_production, 75_LVBus1795410_production, 75_LVBus1795411_production, 75_LVBus1795412_production, 75_LVBus1795414_production, 75_LVBus1795415_production, 75_LVBus1795416_consumption, 75_LVBus1795416_production, 75_LVBus1795417_production, 75_LVBus1795418_consumption, 75_LVBus1795418_production, 75_LVBus1795420_production, 75_LVBus1795421_production, 75_LVBus1795423_production, 75_LVBus1795425_consumption, 75_LVBus1795425_production, 75_LVBus1795426_production, 75_LVBus1795428_production, 75_LVBus1795429_production, 75_LVBus1795430_production, 75_LVBus1795431_production, 75_LVBus1795432_production, 75_LVBus1795433_production, 75_LVBus1795434_consumption, 75_LVBus1795434_production, 75_LVBus1795435_production, 75_LVBus1795436_production, 75_LVBus1795437_production, 75_LVBus1795438_production, 75_LVBus1795440_production, 75_LVBus1795441_production, 75_LVBus1795442_production, 75_LVBus1795443_production, 75_LVBus1795444_production, 75_LVBus1795445_production, 75_LVBus1795446_production, 75_LVBus1795447_consumption, 75_LVBus1795447_production, 75_LVBus1795448_production, 75_LVBus1795449_production, 75_LVBus1795450_production, 75_LVBus1795452_consumption, 75_LVBus1795452_production, 75_LVBus1795453_consumption, 75_LVBus1795453_production, 75_LVBus1795454_consumption, 75_LVBus1795454_production, 75_LVBus1795455_production, 75_LVBus1795456_consumption, 75_LVBus1795456_production, 75_LVBus1795457_consumption, 75_LVBus1795457_production, 75_LVBus1795458_production, 75_LVBus1795460_production, 75_LVBus1795461_production, 75_LVBus1795462_production, 75_LVBus1795463_production, 75_LVBus1795464_consumption, 75_LVBus1795464_production, 75_LVBus1795465_consumption, 75_LVBus1795465_production, 75_LVBus1795466_consumption, 75_LVBus1795466_production, 75_LVBus1795467_consumption, 75_LVBus1795467_production, 75_LVBus1795468_consumption, 75_LVBus1795468_production, 75_LVBus1795469_production, 75_LVBus1795470_consumption, 75_LVBus1795470_production, 75_LVBus1795471_production, 75_LVBus1795472_production, 75_LVBus1795473_production, 75_LVBus1795474_production, 75_LVBus1795476_production, 75_LVBus1795477_production, 75_LVBus1795478_production, 75_LVBus1795479_production, 75_LVBus1795481_production, 75_LVBus1795482_production, 75_LVBus1795483_production, 75_LVBus1795484_production, 75_LVBus1795485_production, 75_LVBus1795486_production, 75_LVBus1795488_consumption, 75_LVBus1795488_production, 75_LVBus1795490_consumption, 75_LVBus1795490_production, 75_LVBus1795492_production, 75_LVBus1795494_consumption, 75_LVBus1795494_production, 75_LVBus1795496_consumption, 75_LVBus1795496_production, 75_LVBus1795498_consumption, 75_LVBus1795498_production, 75_LVBus1795500_production, 75_LVBus1795502_production, 75_LVBus1795503_production, 75_LVBus1795504_production, 75_LVBus1795506_production, 75_LVBus1795507_production, 75_LVBus1795508_production, 75_LVBus1795509_production, 75_LVBus1795510_production, 75_LVBus1795512_consumption, 75_LVBus1795512_production, 75_LVBus1795514_consumption, 75_LVBus1795514_production, 75_LVBus1795516_consumption, 75_LVBus1795516_production, 75_LVBus1795518_production, 75_LVBus1795520_consumption, 75_LVBus1795520_production, 75_LVBus1795522_production, 75_LVBus1795524_consumption, 75_LVBus1795524_production, 75_LVBus1795526_production, 75_LVBus1795528_production, 75_LVBus1795529_production, 75_LVBus1795531_consumption, 75_LVBus1795531_production, 75_LVBus1795532_consumption, 75_LVBus1795532_production, 75_LVBus1795533_production, 75_LVBus1795536_consumption, 75_LVBus1795536_production, 75_LVBus1795537_production, 75_LVBus1795538_consumption, 75_LVBus1795538_production, 75_LVBus1795540_consumption, 75_LVBus1795540_production, 75_LVBus1795541_consumption, 75_LVBus1795541_production, 75_LVBus1795544_production, 75_LVBus1795545_production, 75_LVBus1795546_production, 75_LVBus1795547_production, 75_LVBus1795548_production, 75_LVBus1795549_production, 75_LVBus1795550_production, 75_LVBus1795551_consumption, 75_LVBus1795551_production, 75_LVBus1795552_consumption, 75_LVBus1795552_production, 75_LVBus1795553_production, 75_LVBus1795554_production, 75_LVBus1795555_production, 75_LVBus1795556_production, 75_LVBus1795557_production, 75_LVBus1795561_consumption, 75_LVBus1795561_production, 75_LVBus1795563_consumption, 75_LVBus1795563_production, 75_LVBus1795565_consumption, 75_LVBus1795565_production, 75_LVBus1795567_production, 75_LVBus1795568_consumption, 75_LVBus1795568_production, 75_LVBus1795569_consumption, 75_LVBus1795569_production, 75_LVBus1795571_consumption, 75_LVBus1795571_production, 75_LVBus1795573_consumption, 75_LVBus1795573_production, 75_LVBus1795575_production, 75_LVBus1795576_production, 75_LVBus1795577_consumption, 75_LVBus1795577_production, 75_LVBus1795579_production, 75_LVBus1795580_production, 75_LVBus1795581_production, 75_LVBus1795582_production, 75_LVBus1795583_production, 75_LVBus1795584_production, 75_LVBus1795586_production, 75_LVBus1795587_production, 75_LVBus1795588_production, 75_LVBus1795589_production, 75_LVBus1795590_production, 75_LVBus1795591_production, 75_LVBus1795592_consumption, 75_LVBus1795592_production, 75_LVBus1795593_production, 75_LVBus1795594_production, 75_LVBus1795595_consumption, 75_LVBus1795595_production, 75_LVBus1795596_production, 75_LVBus1795597_production, 75_LVBus1795598_production, 75_LVBus1795599_production, 75_LVBus1795600_production, 75_LVBus1795602_production, 75_LVBus1795603_production, 75_LVBus1795604_production, 75_LVBus1795605_production, 75_LVBus1795606_production, 75_LVBus1795608_production, 75_LVBus1795609_production, 75_LVBus1795610_production, 75_LVBus1795611_production, 75_LVBus1795613_production, 75_LVBus1795614_production, 75_LVBus1795616_production, 75_LVBus1795617_production, 75_LVBus1795618_consumption, 75_LVBus1795618_production, 75_LVBus1795619_production, 75_LVBus1795620_production, 75_LVBus1795621_production, 75_LVBus1795622_production, 75_LVBus1795623_production, 75_LVBus1795624_consumption, 75_LVBus1795624_production, 75_LVBus1795626_production, 75_LVBus1795627_production, 75_LVBus1795628_production, 75_LVBus1795629_production, 75_LVBus1795630_production, 75_LVBus1795631_production, 75_LVBus1795633_production, 75_LVBus1795634_production, 75_LVBus1795635_production, 75_LVBus1795636_production, 75_LVBus1795638_production, 75_LVBus1795639_production, 75_LVBus1795640_production, 75_LVBus1795641_production, 75_LVBus1795642_production, 75_LVBus1795643_production, 75_LVBus1795644_production, 75_LVBus1795646_production, 75_LVBus1795648_production, 75_LVBus1795650_consumption, 75_LVBus1795650_production, 75_LVBus1795652_production, 75_LVBus1795654_consumption, 75_LVBus1795654_production, 75_LVBus1795655_production, 75_LVBus1795656_production, 75_LVBus1795657_production, 75_LVBus1795658_production, 75_LVBus1795659_production, 75_LVBus1795660_production, 75_LVBus1795661_production, 75_LVBus1795662_production, 75_LVBus1795663_production, 75_LVBus1795664_production, 75_LVBus1795665_production, 75_LVBus1795666_production, 75_LVBus1795667_production, 75_LVBus1795669_production, 75_LVBus1795670_consumption, 75_LVBus1795670_production, 75_LVBus1795673_production, 75_LVBus1795674_production, 75_LVBus1795675_production, 75_LVBus1795676_production, 75_LVBus1795677_production, 75_LVBus1795678_production, 75_LVBus1795679_production, 75_LVBus1795680_production, 75_LVBus1795681_production, 75_LVBus1795683_production, 75_LVBus1795684_consumption, 75_LVBus1795684_production, 75_LVBus1795685_production, 75_LVBus1795686_production, 75_LVBus1795687_production, 75_LVBus1795688_production, 75_LVBus1795690_production, 75_LVBus1795691_production, 75_LVBus1795692_production, 75_LVBus1795693_production, 75_LVBus1795694_production, 75_LVBus1795695_production, 75_LVBus1795697_production, 75_LVBus1795699_consumption, 75_LVBus1795699_production, 75_LVBus1795701_production, 75_LVBus1795703_consumption, 75_LVBus1795703_production, 75_LVBus1795705_production, 75_LVBus1795708_production, 75_LVBus1795709_production, 75_LVBus1795710_production, 75_LVBus1795712_production, 75_LVBus1795714_consumption, 75_LVBus1795714_production, 75_LVBus1795716_production, 75_LVBus1795718_production, 75_LVBus1795720_production, 75_LVBus1795721_production, 75_LVBus1795723_consumption, 75_LVBus1795723_production, 75_LVBus1795725_production, 75_LVBus1795726_production, 75_LVBus1795727_production, 75_LVBus1795728_production, 75_LVBus1795729_production, 75_LVBus1795730_consumption, 75_LVBus1795730_production, 75_LVBus1795731_production, 75_LVBus1795732_production, 75_LVBus1795733_production, 75_LVBus1795734_production, 75_LVBus1795736_consumption, 75_LVBus1795736_production, 75_LVBus1795738_production, 75_LVBus1795739_production, 75_LVBus1795740_production, 75_LVBus1795742_production, 75_LVBus1795743_production, 75_LVBus1795744_production, 75_LVBus1795745_production, 75_LVBus1795747_production, 75_LVBus1795748_production, 75_LVBus1795750_production, 75_LVBus1795751_production, 75_LVBus1795752_production, 75_LVBus1795753_consumption, 75_LVBus1795753_production, 75_LVBus1795754_production, 75_LVBus1795755_production, 75_LVBus1795757_production, 75_LVBus1795759_production, 75_LVBus1795760_production, 75_LVBus1795762_production, 75_LVBus1795763_production, 75_LVBus1795764_production, 75_LVBus1795765_production, 75_LVBus1795767_production, 75_LVBus1795768_production, 75_LVBus1795769_production, 75_LVBus1795770_production, 75_LVBus1795771_production, 75_LVBus1795772_production, 75_LVBus1795774_production, 75_LVBus1795775_production, 75_LVBus1795776_production, 75_LVBus1795778_production, 75_LVBus1795779_consumption, 75_LVBus1795779_production, 75_LVBus1795780_consumption, 75_LVBus1795780_production, 75_LVBus1795781_consumption, 75_LVBus1795781_production, 75_LVBus1795783_consumption, 75_LVBus1795783_production, 75_LVBus1795785_consumption, 75_LVBus1795785_production, 75_LVBus1795786_consumption, 75_LVBus1795786_production, 75_LVBus1795787_consumption, 75_LVBus1795787_production, 75_LVBus1795788_consumption, 75_LVBus1795788_production, 75_LVBus1795789_consumption, 75_LVBus1795789_production, 75_LVBus1795791_consumption, 75_LVBus1795791_production, 75_LVBus1795792_consumption, 75_LVBus1795792_production, 75_LVBus1795793_production, 75_LVBus1795795_production, 75_LVBus1795796_production, 75_LVBus1795797_production, 75_LVBus1795798_production, 75_LVBus1795800_production, 75_LVBus1795801_consumption, 75_LVBus1795801_production, 75_LVBus1795802_production, 75_LVBus1795803_production, 75_LVBus1795804_production, 75_LVBus1795805_production, 75_LVBus1795806_production, 75_LVBus1795807_production, 75_LVBus1795808_production, 75_LVBus1795809_production, 75_LVBus1795810_production, 75_LVBus1795811_production, 75_LVBus1921355_consumption, 75_LVBus1921355_production, 75_LVBus1921365_consumption, 75_LVBus1921365_production, 75_LVBus1922180_production, 75_LVBus1923817_production, 75_LVBus1925890_consumption, 75_LVBus1925890_production, 75_LVBus1925973_consumption, 75_LVBus1925973_production, 75_LVBus1925974_production, 75_LVBus1926453_consumption, 75_LVBus1926453_production, 75_LVBus1926454_production, 75_LVBus1926455_consumption, 75_LVBus1926455_production, 75_LVBus1926456_consumption, 75_LVBus1926456_production, 75_LVBus1926457_production, 75_LVBus1926458_production, 75_LVBus1926459_consumption, 75_LVBus1926459_production, 75_LVBus1926460_production, 75_LVBus1926461_consumption, 75_LVBus1926461_production, 75_LVBus1926462_production, 75_LVBus1926463_production, 75_LVBus1926464_consumption, 75_LVBus1926464_production, 75_LVBus1926465_production, 75_LVBus1926466_production, 75_LVBus1928448_consumption, 75_LVBus1928448_production, 75_LVBus1928449_consumption, 75_LVBus1928449_production, 75_LVBus1937807_production, 75_LVBus1937808_production, 75_LVBus1951430_production, 75_LVBus1951431_consumption, 75_LVBus1951431_production, 75_LVBus1951432_consumption, 75_LVBus1951432_production, 75_LVBus1951433_consumption, 75_LVBus1951433_production, 75_LVBus1951434_production, 75_LVBus1951435_production, 75_LVBus1981591_consumption, 75_LVBus1981591_production, 75_LVBus1989415_consumption, 75_LVBus1989415_production, 75_LVBus1989416_consumption, 75_LVBus1989416_production, 75_LVBus1989417_consumption, 75_LVBus1989417_production, 75_LVBus1989418_consumption, 75_LVBus1989418_production, 75_LVBus1989419_consumption, 75_LVBus1989419_production, 75_LVBus1989420_consumption, 75_LVBus1989420_production, 75_LVBus1989421_consumption, 75_LVBus1989421_production, 75_LVBus1990622_consumption, 75_LVBus1990622_production, 75_LVBus2007155_consumption, 75_LVBus2007155_production, 75_LVBus2007156_consumption, 75_LVBus2007156_production, 75_LVBus2007157_consumption, 75_LVBus2007157_production, 75_LVBus2007158_production, 75_LVBus2007159_consumption, 75_LVBus2007159_production, 75_LVBus2007160_consumption, 75_LVBus2007160_production, 75_LVBus2007161_production, 75_LVBus2007162_consumption, 75_LVBus2007162_production, 75_LVBus2011492_consumption, 75_LVBus2011492_production, 75_LVBus2011493_consumption, 75_LVBus2011493_production, 75_LVBus2011494_consumption, 75_LVBus2011494_production, 75_LVBus2011495_production, 75_LVBus2011496_consumption, 75_LVBus2011496_production, 75_LVBus2011497_consumption, 75_LVBus2011497_production, 75_LVBus2011498_consumption, 75_LVBus2011498_production, 75_LVBus2011499_consumption, 75_LVBus2011499_production, 75_LVBus2011500_consumption, 75_LVBus2011500_production, 75_LVBus2011501_consumption, 75_LVBus2011501_production, 75_LVBus2011502_consumption, 75_LVBus2011502_production, 75_LVBus2011503_consumption, 75_LVBus2011503_production, 75_LVBus2011504_consumption, 75_LVBus2011504_production, 75_LVBus2011505_consumption, 75_LVBus2011505_production, 75_LVBus2011506_production, 75_MVLV009176_consumption, 75_MVLV009176_production, 75_MVLV009184_consumption, 75_MVLV009184_production, 75_MVLV067377_consumption, 75_MVLV067377_production, 75_MVLV070397_consumption, 75_MVLV070397_production, 75_MVLV099197_consumption, 75_MVLV099197_production, 75_MVLV106479_consumption, 75_MVLV106479_production, 75_MVLV107944_consumption, 75_MVLV107944_production, 75_MVLV116462_consumption, 75_MVLV116462_production, 75_MVLV146358_consumption, 75_MVLV146358_production, 75_MVLV154864_consumption, 75_MVLV154864_production.

