# BMOPF Network Summary: 75_MVFeeder0165

**Generated:** 2026-10-01 23:34:21  
**Findings:** 0 errors · 5 warnings · 152 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 45 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 345 |  |
| line | 299 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 420 | 479.619 kW, 143.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 45 |  |
| switch | 0 |  |
| transformer | 45 | Dyn11×45 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 95 | 94 | 10 | 0 |
| LV_236V | 236.0 V | 250 | 205 | 410 | 0 |

**Transformer transitions:**

- `75_MVLV054034_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV117825_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV168305_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV165762_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV147561_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV123400_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV003892_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV034076_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV140894_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV053300_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV000126_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV063511_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV035650_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV118028_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV070064_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV054037_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV044023_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV147562_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV166555_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV099462_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036364_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV140892_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV117987_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV166377_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV140385_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV165764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV082414_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV016883_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV053298_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV118911_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV067410_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV141024_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV029913_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV089986_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV126896_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV111304_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV084381_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV147548_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV130240_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV031699_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036026_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV118893_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV013815_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV077525_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV137902_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 7 |
| Degree-1 buses | 115 |
| Tree depth (max hops) | 36 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 345 | 1 | 344 | 0 | 0 | 0 |
| Tier LV_236V | 250 | 45 | 205 | 0 | 0 | 0 |
| Tier MV_11.8kV | 95 | 1 | 94 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 45; skipped invalid branches: 0.

Galvanic zones: 46; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_AUBUS | MV_11.8kV | 95 | 0 | 0 | 45 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1285 declared bus terminals; 1102 mapped line/closed-switch conductor edges; 183 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 17400.0 | 3.769 | 1260 |
| q_nom | 0.0 | 5220.0 | 3.769 | 1260 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.931 | 2790.0 | 1.765 | 299 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.439 | 45 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 278 of 420 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0781995_consumption' has phase imbalance of 187.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782217_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782151_consumption' has phase imbalance of 178.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0781994_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782220_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782236_consumption' has phase imbalance of 41.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782021_consumption' has phase imbalance of 206.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782172_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782227_consumption' has phase imbalance of 285.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782171_consumption' has phase imbalance of 246.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782022_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782162_consumption' has phase imbalance of 147.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782238_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782242_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782181_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782080_consumption' has phase imbalance of 134.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782118_consumption' has phase imbalance of 227.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782053_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782197_consumption' has phase imbalance of 277.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782087_consumption' has phase imbalance of 216.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782155_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782016_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782158_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782249_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782107_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782046_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782119_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782092_consumption' has phase imbalance of 127.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782050_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782232_consumption' has phase imbalance of 203.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782032_consumption' has phase imbalance of 124.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782226_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782235_consumption' has phase imbalance of 284.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782082_consumption' has phase imbalance of 261.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782196_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782198_consumption' has phase imbalance of 263.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782047_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782142_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782231_consumption' has phase imbalance of 281.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782216_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782214_consumption' has phase imbalance of 264.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782010_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782176_consumption' has phase imbalance of 288.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782027_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782093_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782234_consumption' has phase imbalance of 229.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782055_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782100_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782161_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782193_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782175_consumption' has phase imbalance of 269.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782177_consumption' has phase imbalance of 258.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782062_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782254_consumption' has phase imbalance of 294.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0781996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782094_consumption' has phase imbalance of 130.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782147_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782023_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782008_consumption' has phase imbalance of 259.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782098_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782033_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782173_consumption' has phase imbalance of 282.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782056_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782065_consumption' has phase imbalance of 117.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0782048_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 420 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0782149' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0781998' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 479.619 kW |
| Total load Q | 143.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV054034_Transformer | 176.0 kVA | 14.6% |
| 75_MVLV117825_Transformer | 110.0 kVA | 16.9% |
| 75_MVLV168305_Transformer | 110.0 kVA | 12.0% |
| 75_MVLV165762_Transformer | 110.0 kVA | 4.3% |
| 75_MVLV147561_Transformer | 110.0 kVA | 4.7% |
| 75_MVLV123400_Transformer | 110.0 kVA | 8.9% |
| 75_MVLV003892_Transformer | 110.0 kVA | 0.3% |
| 75_MVLV034076_Transformer | 110.0 kVA | 1.9% |
| 75_MVLV140894_Transformer | 110.0 kVA | 17.5% |
| 75_MVLV053300_Transformer | 110.0 kVA | 6.1% |
| 75_MVLV000126_Transformer | 110.0 kVA | 4.6% |
| 75_MVLV063511_Transformer | 275.0 kVA | 25.0% |
| 75_MVLV035650_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV118028_Transformer | 110.0 kVA | 13.9% |
| 75_MVLV070064_Transformer | 110.0 kVA | 20.2% |
| 75_MVLV054037_Transformer | 110.0 kVA | 3.4% |
| 75_MVLV044023_Transformer | 110.0 kVA | 17.9% |
| 75_MVLV147562_Transformer | 110.0 kVA | 5.6% |
| 75_MVLV166555_Transformer | 110.0 kVA | 8.2% |
| 75_MVLV099462_Transformer | 110.0 kVA | 7.7% |
| 75_MVLV036364_Transformer | 110.0 kVA | 19.7% |
| 75_MVLV140892_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV117987_Transformer | 110.0 kVA | 9.2% |
| 75_MVLV166377_Transformer | 110.0 kVA | 1.3% |
| 75_MVLV140385_Transformer | 176.0 kVA | 17.5% |
| 75_MVLV165764_Transformer | 176.0 kVA | 6.6% |
| 75_MVLV082414_Transformer | 110.0 kVA | 0.0% |
| 75_MVLV016883_Transformer | 176.0 kVA | 11.2% |
| 75_MVLV053298_Transformer | 110.0 kVA | 2.6% |
| 75_MVLV118911_Transformer | 110.0 kVA | 3.1% |
| 75_MVLV067410_Transformer | 110.0 kVA | 2.3% |
| 75_MVLV141024_Transformer | 110.0 kVA | 5.5% |
| 75_MVLV029913_Transformer | 110.0 kVA | 15.8% |
| 75_MVLV089986_Transformer | 110.0 kVA | 1.1% |
| 75_MVLV126896_Transformer | 110.0 kVA | 5.9% |
| 75_MVLV111304_Transformer | 110.0 kVA | 0.6% |
| 75_MVLV084381_Transformer | 110.0 kVA | 5.6% |
| 75_MVLV147548_Transformer | 110.0 kVA | 12.3% |
| 75_MVLV130240_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV031699_Transformer | 110.0 kVA | 4.2% |
| 75_MVLV036026_Transformer | 110.0 kVA | 7.5% |
| 75_MVLV118893_Transformer | 110.0 kVA | 6.8% |
| 75_MVLV013815_Transformer | 110.0 kVA | 0.0% |
| 75_MVLV077525_Transformer | 110.0 kVA | 4.1% |
| 75_MVLV137902_Transformer | 440.0 kVA | 12.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.48 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_AUBUS' (MV, 11.78 kV) has an electrical reach of 27.31 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0782042' (LV, 0.24 kV) has an electrical reach of 27.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0782127' (LV, 0.24 kV) has an electrical reach of 18.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0781998' (LV, 0.24 kV) has an electrical reach of 10.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 345 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 345 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 45 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 95 |
| LV_236V | 4-wire | 250 / 250 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 250 |
| Neutral branches | 205 |
| Grounding points | 45 |
| Neutral sections | 45 |
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
| 11.78 kV | 95 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 46 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1370.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 250 / 95 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 279 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 279 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0781994_production, 75_LVBus0781995_production, 75_LVBus0781996_production, 75_LVBus0781998_production, 75_LVBus0782000_consumption, 75_LVBus0782000_production, 75_LVBus0782002_consumption, 75_LVBus0782002_production, 75_LVBus0782004_consumption, 75_LVBus0782004_production, 75_LVBus0782006_production, 75_LVBus0782008_production, 75_LVBus0782009_consumption, 75_LVBus0782009_production, 75_LVBus0782010_production, 75_LVBus0782012_consumption, 75_LVBus0782012_production, 75_LVBus0782014_production, 75_LVBus0782016_production, 75_LVBus0782017_consumption, 75_LVBus0782017_production, 75_LVBus0782018_consumption, 75_LVBus0782018_production, 75_LVBus0782019_consumption, 75_LVBus0782019_production, 75_LVBus0782020_production, 75_LVBus0782021_production, 75_LVBus0782022_production, 75_LVBus0782023_production, 75_LVBus0782024_consumption, 75_LVBus0782024_production, 75_LVBus0782025_production, 75_LVBus0782026_consumption, 75_LVBus0782026_production, 75_LVBus0782027_production, 75_LVBus0782031_production, 75_LVBus0782032_production, 75_LVBus0782033_production, 75_LVBus0782035_consumption, 75_LVBus0782035_production, 75_LVBus0782036_consumption, 75_LVBus0782036_production, 75_LVBus0782037_consumption, 75_LVBus0782037_production, 75_LVBus0782038_consumption, 75_LVBus0782038_production, 75_LVBus0782039_production, 75_LVBus0782040_consumption, 75_LVBus0782040_production, 75_LVBus0782042_consumption, 75_LVBus0782042_production, 75_LVBus0782044_production, 75_LVBus0782046_production, 75_LVBus0782047_production, 75_LVBus0782048_production, 75_LVBus0782049_production, 75_LVBus0782050_production, 75_LVBus0782051_production, 75_LVBus0782053_production, 75_LVBus0782054_consumption, 75_LVBus0782054_production, 75_LVBus0782055_production, 75_LVBus0782056_production, 75_LVBus0782057_production, 75_LVBus0782059_production, 75_LVBus0782060_consumption, 75_LVBus0782060_production, 75_LVBus0782061_production, 75_LVBus0782062_production, 75_LVBus0782064_production, 75_LVBus0782065_production, 75_LVBus0782066_production, 75_LVBus0782067_consumption, 75_LVBus0782067_production, 75_LVBus0782068_consumption, 75_LVBus0782068_production, 75_LVBus0782072_production, 75_LVBus0782073_production, 75_LVBus0782074_consumption, 75_LVBus0782074_production, 75_LVBus0782075_consumption, 75_LVBus0782075_production, 75_LVBus0782076_production, 75_LVBus0782077_consumption, 75_LVBus0782077_production, 75_LVBus0782078_production, 75_LVBus0782079_production, 75_LVBus0782080_production, 75_LVBus0782081_consumption, 75_LVBus0782081_production, 75_LVBus0782082_production, 75_LVBus0782083_consumption, 75_LVBus0782083_production, 75_LVBus0782084_production, 75_LVBus0782086_production, 75_LVBus0782087_production, 75_LVBus0782088_consumption, 75_LVBus0782088_production, 75_LVBus0782090_consumption, 75_LVBus0782090_production, 75_LVBus0782091_production, 75_LVBus0782092_production, 75_LVBus0782093_production, 75_LVBus0782094_production, 75_LVBus0782095_consumption, 75_LVBus0782095_production, 75_LVBus0782096_consumption, 75_LVBus0782096_production, 75_LVBus0782097_production, 75_LVBus0782098_production, 75_LVBus0782099_production, 75_LVBus0782100_production, 75_LVBus0782101_consumption, 75_LVBus0782101_production, 75_LVBus0782102_production, 75_LVBus0782103_consumption, 75_LVBus0782103_production, 75_LVBus0782106_consumption, 75_LVBus0782106_production, 75_LVBus0782107_production, 75_LVBus0782109_consumption, 75_LVBus0782109_production, 75_LVBus0782111_consumption, 75_LVBus0782111_production, 75_LVBus0782112_production, 75_LVBus0782113_production, 75_LVBus0782114_consumption, 75_LVBus0782114_production, 75_LVBus0782115_consumption, 75_LVBus0782115_production, 75_LVBus0782116_consumption, 75_LVBus0782116_production, 75_LVBus0782117_production, 75_LVBus0782118_production, 75_LVBus0782119_production, 75_LVBus0782121_consumption, 75_LVBus0782121_production, 75_LVBus0782123_production, 75_LVBus0782124_consumption, 75_LVBus0782124_production, 75_LVBus0782125_production, 75_LVBus0782127_consumption, 75_LVBus0782127_production, 75_LVBus0782129_production, 75_LVBus0782130_production, 75_LVBus0782131_consumption, 75_LVBus0782131_production, 75_LVBus0782132_production, 75_LVBus0782133_production, 75_LVBus0782137_consumption, 75_LVBus0782137_production, 75_LVBus0782138_consumption, 75_LVBus0782138_production, 75_LVBus0782139_production, 75_LVBus0782141_production, 75_LVBus0782142_production, 75_LVBus0782143_production, 75_LVBus0782145_consumption, 75_LVBus0782145_production, 75_LVBus0782147_production, 75_LVBus0782149_production, 75_LVBus0782151_production, 75_LVBus0782152_consumption, 75_LVBus0782152_production, 75_LVBus0782153_production, 75_LVBus0782155_production, 75_LVBus0782156_production, 75_LVBus0782157_consumption, 75_LVBus0782157_production, 75_LVBus0782158_production, 75_LVBus0782159_consumption, 75_LVBus0782159_production, 75_LVBus0782160_production, 75_LVBus0782161_production, 75_LVBus0782162_production, 75_LVBus0782163_consumption, 75_LVBus0782163_production, 75_LVBus0782164_production, 75_LVBus0782166_production, 75_LVBus0782167_production, 75_LVBus0782168_production, 75_LVBus0782169_production, 75_LVBus0782171_production, 75_LVBus0782172_production, 75_LVBus0782173_production, 75_LVBus0782175_production, 75_LVBus0782176_production, 75_LVBus0782177_production, 75_LVBus0782179_consumption, 75_LVBus0782179_production, 75_LVBus0782180_consumption, 75_LVBus0782180_production, 75_LVBus0782181_production, 75_LVBus0782182_production, 75_LVBus0782183_consumption, 75_LVBus0782183_production, 75_LVBus0782187_production, 75_LVBus0782189_consumption, 75_LVBus0782189_production, 75_LVBus0782191_production, 75_LVBus0782192_production, 75_LVBus0782193_production, 75_LVBus0782195_consumption, 75_LVBus0782195_production, 75_LVBus0782196_production, 75_LVBus0782197_production, 75_LVBus0782198_production, 75_LVBus0782199_production, 75_LVBus0782200_production, 75_LVBus0782201_production, 75_LVBus0782202_consumption, 75_LVBus0782202_production, 75_LVBus0782203_production, 75_LVBus0782204_production, 75_LVBus0782205_production, 75_LVBus0782209_consumption, 75_LVBus0782209_production, 75_LVBus0782211_consumption, 75_LVBus0782211_production, 75_LVBus0782212_production, 75_LVBus0782213_production, 75_LVBus0782214_production, 75_LVBus0782215_consumption, 75_LVBus0782215_production, 75_LVBus0782216_production, 75_LVBus0782217_production, 75_LVBus0782219_consumption, 75_LVBus0782219_production, 75_LVBus0782220_production, 75_LVBus0782222_consumption, 75_LVBus0782222_production, 75_LVBus0782223_production, 75_LVBus0782224_production, 75_LVBus0782226_production, 75_LVBus0782227_production, 75_LVBus0782228_production, 75_LVBus0782230_production, 75_LVBus0782231_production, 75_LVBus0782232_production, 75_LVBus0782234_production, 75_LVBus0782235_production, 75_LVBus0782236_production, 75_LVBus0782238_production, 75_LVBus0782239_production, 75_LVBus0782240_production, 75_LVBus0782242_production, 75_LVBus0782243_production, 75_LVBus0782244_production, 75_LVBus0782245_production, 75_LVBus0782247_consumption, 75_LVBus0782247_production, 75_LVBus0782248_production, 75_LVBus0782249_production, 75_LVBus0782250_production, 75_LVBus0782252_consumption, 75_LVBus0782252_production, 75_LVBus0782253_production, 75_LVBus0782254_production, 75_LVBus0782255_production, 75_LVBus0782257_production, 75_LVBus0782259_production, 75_LVBus0782260_consumption, 75_LVBus0782260_production, 75_LVBus0782261_production, 75_LVBus0782263_consumption, 75_LVBus0782263_production, 75_LVBus0782264_consumption, 75_LVBus0782264_production, 75_LVBus0782265_production, 75_MVLV007793_consumption, 75_MVLV007793_production, 75_MVLV073969_consumption, 75_MVLV073969_production, 75_MVLV089578_consumption, 75_MVLV089578_production, 75_MVLV140895_consumption, 75_MVLV140895_production, 75_MVLV165692_consumption, 75_MVLV165692_production.

## 9. Data Quality Summary

**Total findings:** 157 (0 errors, 5 warnings, 152 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  278 of 420 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.48 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  279 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0781995_consumption`  
  Load '75_LVBus0781995_consumption' has phase imbalance of 187.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782217_consumption`  
  Load '75_LVBus0782217_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782151_consumption`  
  Load '75_LVBus0782151_consumption' has phase imbalance of 178.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782169_consumption`  
  Load '75_LVBus0782169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0781994_consumption`  
  Load '75_LVBus0781994_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782220_consumption`  
  Load '75_LVBus0782220_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782236_consumption`  
  Load '75_LVBus0782236_consumption' has phase imbalance of 41.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782021_consumption`  
  Load '75_LVBus0782021_consumption' has phase imbalance of 206.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782172_consumption`  
  Load '75_LVBus0782172_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782257_consumption`  
  Load '75_LVBus0782257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782086_consumption`  
  Load '75_LVBus0782086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782227_consumption`  
  Load '75_LVBus0782227_consumption' has phase imbalance of 285.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782171_consumption`  
  Load '75_LVBus0782171_consumption' has phase imbalance of 246.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782133_consumption`  
  Load '75_LVBus0782133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782022_consumption`  
  Load '75_LVBus0782022_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782253_consumption`  
  Load '75_LVBus0782253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782261_consumption`  
  Load '75_LVBus0782261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782123_consumption`  
  Load '75_LVBus0782123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782162_consumption`  
  Load '75_LVBus0782162_consumption' has phase imbalance of 147.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782238_consumption`  
  Load '75_LVBus0782238_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782242_consumption`  
  Load '75_LVBus0782242_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782182_consumption`  
  Load '75_LVBus0782182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782129_consumption`  
  Load '75_LVBus0782129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782181_consumption`  
  Load '75_LVBus0782181_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782059_consumption`  
  Load '75_LVBus0782059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782080_consumption`  
  Load '75_LVBus0782080_consumption' has phase imbalance of 134.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782118_consumption`  
  Load '75_LVBus0782118_consumption' has phase imbalance of 227.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782053_consumption`  
  Load '75_LVBus0782053_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782091_consumption`  
  Load '75_LVBus0782091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782197_consumption`  
  Load '75_LVBus0782197_consumption' has phase imbalance of 277.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782057_consumption`  
  Load '75_LVBus0782057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782204_consumption`  
  Load '75_LVBus0782204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782087_consumption`  
  Load '75_LVBus0782087_consumption' has phase imbalance of 216.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782155_consumption`  
  Load '75_LVBus0782155_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782016_consumption`  
  Load '75_LVBus0782016_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782158_consumption`  
  Load '75_LVBus0782158_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782259_consumption`  
  Load '75_LVBus0782259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782249_consumption`  
  Load '75_LVBus0782249_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782107_consumption`  
  Load '75_LVBus0782107_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782039_consumption`  
  Load '75_LVBus0782039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782046_consumption`  
  Load '75_LVBus0782046_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782125_consumption`  
  Load '75_LVBus0782125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782084_consumption`  
  Load '75_LVBus0782084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782143_consumption`  
  Load '75_LVBus0782143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782153_consumption`  
  Load '75_LVBus0782153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782049_consumption`  
  Load '75_LVBus0782049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782244_consumption`  
  Load '75_LVBus0782244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782265_consumption`  
  Load '75_LVBus0782265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782166_consumption`  
  Load '75_LVBus0782166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782160_consumption`  
  Load '75_LVBus0782160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782119_consumption`  
  Load '75_LVBus0782119_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782072_consumption`  
  Load '75_LVBus0782072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782240_consumption`  
  Load '75_LVBus0782240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782092_consumption`  
  Load '75_LVBus0782092_consumption' has phase imbalance of 127.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782050_consumption`  
  Load '75_LVBus0782050_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782132_consumption`  
  Load '75_LVBus0782132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782199_consumption`  
  Load '75_LVBus0782199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782232_consumption`  
  Load '75_LVBus0782232_consumption' has phase imbalance of 203.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782164_consumption`  
  Load '75_LVBus0782164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782032_consumption`  
  Load '75_LVBus0782032_consumption' has phase imbalance of 124.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782226_consumption`  
  Load '75_LVBus0782226_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782235_consumption`  
  Load '75_LVBus0782235_consumption' has phase imbalance of 284.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782078_consumption`  
  Load '75_LVBus0782078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782082_consumption`  
  Load '75_LVBus0782082_consumption' has phase imbalance of 261.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782196_consumption`  
  Load '75_LVBus0782196_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782198_consumption`  
  Load '75_LVBus0782198_consumption' has phase imbalance of 263.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782047_consumption`  
  Load '75_LVBus0782047_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782142_consumption`  
  Load '75_LVBus0782142_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782192_consumption`  
  Load '75_LVBus0782192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782168_consumption`  
  Load '75_LVBus0782168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782231_consumption`  
  Load '75_LVBus0782231_consumption' has phase imbalance of 281.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782216_consumption`  
  Load '75_LVBus0782216_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782214_consumption`  
  Load '75_LVBus0782214_consumption' has phase imbalance of 264.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782010_consumption`  
  Load '75_LVBus0782010_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782025_consumption`  
  Load '75_LVBus0782025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782176_consumption`  
  Load '75_LVBus0782176_consumption' has phase imbalance of 288.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782027_consumption`  
  Load '75_LVBus0782027_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782093_consumption`  
  Load '75_LVBus0782093_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782234_consumption`  
  Load '75_LVBus0782234_consumption' has phase imbalance of 229.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782230_consumption`  
  Load '75_LVBus0782230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782066_consumption`  
  Load '75_LVBus0782066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782055_consumption`  
  Load '75_LVBus0782055_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782224_consumption`  
  Load '75_LVBus0782224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782102_consumption`  
  Load '75_LVBus0782102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782100_consumption`  
  Load '75_LVBus0782100_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782076_consumption`  
  Load '75_LVBus0782076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782161_consumption`  
  Load '75_LVBus0782161_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782201_consumption`  
  Load '75_LVBus0782201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782250_consumption`  
  Load '75_LVBus0782250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782130_consumption`  
  Load '75_LVBus0782130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782193_consumption`  
  Load '75_LVBus0782193_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782031_consumption`  
  Load '75_LVBus0782031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782061_consumption`  
  Load '75_LVBus0782061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782187_consumption`  
  Load '75_LVBus0782187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782175_consumption`  
  Load '75_LVBus0782175_consumption' has phase imbalance of 269.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782177_consumption`  
  Load '75_LVBus0782177_consumption' has phase imbalance of 258.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782064_consumption`  
  Load '75_LVBus0782064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782141_consumption`  
  Load '75_LVBus0782141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782239_consumption`  
  Load '75_LVBus0782239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782044_consumption`  
  Load '75_LVBus0782044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782228_consumption`  
  Load '75_LVBus0782228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782062_consumption`  
  Load '75_LVBus0782062_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782254_consumption`  
  Load '75_LVBus0782254_consumption' has phase imbalance of 294.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782051_consumption`  
  Load '75_LVBus0782051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782112_consumption`  
  Load '75_LVBus0782112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782139_consumption`  
  Load '75_LVBus0782139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782243_consumption`  
  Load '75_LVBus0782243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782248_consumption`  
  Load '75_LVBus0782248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0781996_consumption`  
  Load '75_LVBus0781996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782212_consumption`  
  Load '75_LVBus0782212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782223_consumption`  
  Load '75_LVBus0782223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782094_consumption`  
  Load '75_LVBus0782094_consumption' has phase imbalance of 130.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782147_consumption`  
  Load '75_LVBus0782147_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782023_consumption`  
  Load '75_LVBus0782023_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782113_consumption`  
  Load '75_LVBus0782113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782205_consumption`  
  Load '75_LVBus0782205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782203_consumption`  
  Load '75_LVBus0782203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782079_consumption`  
  Load '75_LVBus0782079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782008_consumption`  
  Load '75_LVBus0782008_consumption' has phase imbalance of 259.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782167_consumption`  
  Load '75_LVBus0782167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782073_consumption`  
  Load '75_LVBus0782073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782156_consumption`  
  Load '75_LVBus0782156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782098_consumption`  
  Load '75_LVBus0782098_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782245_consumption`  
  Load '75_LVBus0782245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782255_consumption`  
  Load '75_LVBus0782255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782200_consumption`  
  Load '75_LVBus0782200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782033_consumption`  
  Load '75_LVBus0782033_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782173_consumption`  
  Load '75_LVBus0782173_consumption' has phase imbalance of 282.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782056_consumption`  
  Load '75_LVBus0782056_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782065_consumption`  
  Load '75_LVBus0782065_consumption' has phase imbalance of 117.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0782048_consumption`  
  Load '75_LVBus0782048_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 420 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0782149' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0781998' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_AUBUS' (MV, 11.78 kV) has an electrical reach of 27.31 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0782042' (LV, 0.24 kV) has an electrical reach of 27.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0782127' (LV, 0.24 kV) has an electrical reach of 18.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0781998' (LV, 0.24 kV) has an electrical reach of 10.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  345 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  110 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0781994_consumption, 75_LVBus0781995_consumption, 75_LVBus0781996_consumption, 75_LVBus0782016_consumption, 75_LVBus0782021_consumption, 75_LVBus0782022_consumption, 75_LVBus0782023_consumption, 75_LVBus0782025_consumption, 75_LVBus0782027_consumption, 75_LVBus0782031_consumption, 75_LVBus0782039_consumption, 75_LVBus0782044_consumption, 75_LVBus0782046_consumption, 75_LVBus0782048_consumption, 75_LVBus0782049_consumption, 75_LVBus0782050_consumption, 75_LVBus0782051_consumption, 75_LVBus0782053_consumption, 75_LVBus0782055_consumption, 75_LVBus0782056_consumption, 75_LVBus0782057_consumption, 75_LVBus0782059_consumption, 75_LVBus0782061_consumption, 75_LVBus0782064_consumption, 75_LVBus0782066_consumption, 75_LVBus0782072_consumption, 75_LVBus0782073_consumption, 75_LVBus0782076_consumption, 75_LVBus0782078_consumption, 75_LVBus0782079_consumption, 75_LVBus0782084_consumption, 75_LVBus0782086_consumption, 75_LVBus0782087_consumption, 75_LVBus0782091_consumption, 75_LVBus0782093_consumption, 75_LVBus0782102_consumption, 75_LVBus0782112_consumption, 75_LVBus0782113_consumption, 75_LVBus0782119_consumption, 75_LVBus0782123_consumption, 75_LVBus0782125_consumption, 75_LVBus0782129_consumption, 75_LVBus0782130_consumption, 75_LVBus0782132_consumption, 75_LVBus0782133_consumption, 75_LVBus0782139_consumption, 75_LVBus0782141_consumption, 75_LVBus0782142_consumption, 75_LVBus0782143_consumption, 75_LVBus0782153_consumption, 75_LVBus0782155_consumption, 75_LVBus0782156_consumption, 75_LVBus0782158_consumption, 75_LVBus0782160_consumption, 75_LVBus0782164_consumption, 75_LVBus0782166_consumption, 75_LVBus0782167_consumption, 75_LVBus0782168_consumption, 75_LVBus0782169_consumption, 75_LVBus0782171_consumption, 75_LVBus0782172_consumption, 75_LVBus0782173_consumption, 75_LVBus0782175_consumption, 75_LVBus0782176_consumption, 75_LVBus0782177_consumption, 75_LVBus0782181_consumption, 75_LVBus0782182_consumption, 75_LVBus0782187_consumption, 75_LVBus0782192_consumption, 75_LVBus0782193_consumption, 75_LVBus0782196_consumption, 75_LVBus0782197_consumption, 75_LVBus0782198_consumption, 75_LVBus0782199_consumption, 75_LVBus0782200_consumption, 75_LVBus0782201_consumption, 75_LVBus0782203_consumption, 75_LVBus0782204_consumption, 75_LVBus0782205_consumption, 75_LVBus0782212_consumption, 75_LVBus0782214_consumption, 75_LVBus0782216_consumption, 75_LVBus0782217_consumption, 75_LVBus0782223_consumption, 75_LVBus0782224_consumption, 75_LVBus0782226_consumption, 75_LVBus0782227_consumption, 75_LVBus0782228_consumption, 75_LVBus0782230_consumption, 75_LVBus0782231_consumption, 75_LVBus0782232_consumption, 75_LVBus0782234_consumption, 75_LVBus0782235_consumption, 75_LVBus0782238_consumption, 75_LVBus0782239_consumption, 75_LVBus0782240_consumption, 75_LVBus0782242_consumption, 75_LVBus0782243_consumption, 75_LVBus0782244_consumption, 75_LVBus0782245_consumption, 75_LVBus0782248_consumption, 75_LVBus0782249_consumption, 75_LVBus0782250_consumption, 75_LVBus0782253_consumption, 75_LVBus0782254_consumption, 75_LVBus0782255_consumption, 75_LVBus0782257_consumption, 75_LVBus0782259_consumption, 75_LVBus0782261_consumption, 75_LVBus0782265_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  210 group(s) of loads (420 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  4 group(s) of series lines (9 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  279 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0781994_production, 75_LVBus0781995_production, 75_LVBus0781996_production, 75_LVBus0781998_production, 75_LVBus0782000_consumption, 75_LVBus0782000_production, 75_LVBus0782002_consumption, 75_LVBus0782002_production, 75_LVBus0782004_consumption, 75_LVBus0782004_production, 75_LVBus0782006_production, 75_LVBus0782008_production, 75_LVBus0782009_consumption, 75_LVBus0782009_production, 75_LVBus0782010_production, 75_LVBus0782012_consumption, 75_LVBus0782012_production, 75_LVBus0782014_production, 75_LVBus0782016_production, 75_LVBus0782017_consumption, 75_LVBus0782017_production, 75_LVBus0782018_consumption, 75_LVBus0782018_production, 75_LVBus0782019_consumption, 75_LVBus0782019_production, 75_LVBus0782020_production, 75_LVBus0782021_production, 75_LVBus0782022_production, 75_LVBus0782023_production, 75_LVBus0782024_consumption, 75_LVBus0782024_production, 75_LVBus0782025_production, 75_LVBus0782026_consumption, 75_LVBus0782026_production, 75_LVBus0782027_production, 75_LVBus0782031_production, 75_LVBus0782032_production, 75_LVBus0782033_production, 75_LVBus0782035_consumption, 75_LVBus0782035_production, 75_LVBus0782036_consumption, 75_LVBus0782036_production, 75_LVBus0782037_consumption, 75_LVBus0782037_production, 75_LVBus0782038_consumption, 75_LVBus0782038_production, 75_LVBus0782039_production, 75_LVBus0782040_consumption, 75_LVBus0782040_production, 75_LVBus0782042_consumption, 75_LVBus0782042_production, 75_LVBus0782044_production, 75_LVBus0782046_production, 75_LVBus0782047_production, 75_LVBus0782048_production, 75_LVBus0782049_production, 75_LVBus0782050_production, 75_LVBus0782051_production, 75_LVBus0782053_production, 75_LVBus0782054_consumption, 75_LVBus0782054_production, 75_LVBus0782055_production, 75_LVBus0782056_production, 75_LVBus0782057_production, 75_LVBus0782059_production, 75_LVBus0782060_consumption, 75_LVBus0782060_production, 75_LVBus0782061_production, 75_LVBus0782062_production, 75_LVBus0782064_production, 75_LVBus0782065_production, 75_LVBus0782066_production, 75_LVBus0782067_consumption, 75_LVBus0782067_production, 75_LVBus0782068_consumption, 75_LVBus0782068_production, 75_LVBus0782072_production, 75_LVBus0782073_production, 75_LVBus0782074_consumption, 75_LVBus0782074_production, 75_LVBus0782075_consumption, 75_LVBus0782075_production, 75_LVBus0782076_production, 75_LVBus0782077_consumption, 75_LVBus0782077_production, 75_LVBus0782078_production, 75_LVBus0782079_production, 75_LVBus0782080_production, 75_LVBus0782081_consumption, 75_LVBus0782081_production, 75_LVBus0782082_production, 75_LVBus0782083_consumption, 75_LVBus0782083_production, 75_LVBus0782084_production, 75_LVBus0782086_production, 75_LVBus0782087_production, 75_LVBus0782088_consumption, 75_LVBus0782088_production, 75_LVBus0782090_consumption, 75_LVBus0782090_production, 75_LVBus0782091_production, 75_LVBus0782092_production, 75_LVBus0782093_production, 75_LVBus0782094_production, 75_LVBus0782095_consumption, 75_LVBus0782095_production, 75_LVBus0782096_consumption, 75_LVBus0782096_production, 75_LVBus0782097_production, 75_LVBus0782098_production, 75_LVBus0782099_production, 75_LVBus0782100_production, 75_LVBus0782101_consumption, 75_LVBus0782101_production, 75_LVBus0782102_production, 75_LVBus0782103_consumption, 75_LVBus0782103_production, 75_LVBus0782106_consumption, 75_LVBus0782106_production, 75_LVBus0782107_production, 75_LVBus0782109_consumption, 75_LVBus0782109_production, 75_LVBus0782111_consumption, 75_LVBus0782111_production, 75_LVBus0782112_production, 75_LVBus0782113_production, 75_LVBus0782114_consumption, 75_LVBus0782114_production, 75_LVBus0782115_consumption, 75_LVBus0782115_production, 75_LVBus0782116_consumption, 75_LVBus0782116_production, 75_LVBus0782117_production, 75_LVBus0782118_production, 75_LVBus0782119_production, 75_LVBus0782121_consumption, 75_LVBus0782121_production, 75_LVBus0782123_production, 75_LVBus0782124_consumption, 75_LVBus0782124_production, 75_LVBus0782125_production, 75_LVBus0782127_consumption, 75_LVBus0782127_production, 75_LVBus0782129_production, 75_LVBus0782130_production, 75_LVBus0782131_consumption, 75_LVBus0782131_production, 75_LVBus0782132_production, 75_LVBus0782133_production, 75_LVBus0782137_consumption, 75_LVBus0782137_production, 75_LVBus0782138_consumption, 75_LVBus0782138_production, 75_LVBus0782139_production, 75_LVBus0782141_production, 75_LVBus0782142_production, 75_LVBus0782143_production, 75_LVBus0782145_consumption, 75_LVBus0782145_production, 75_LVBus0782147_production, 75_LVBus0782149_production, 75_LVBus0782151_production, 75_LVBus0782152_consumption, 75_LVBus0782152_production, 75_LVBus0782153_production, 75_LVBus0782155_production, 75_LVBus0782156_production, 75_LVBus0782157_consumption, 75_LVBus0782157_production, 75_LVBus0782158_production, 75_LVBus0782159_consumption, 75_LVBus0782159_production, 75_LVBus0782160_production, 75_LVBus0782161_production, 75_LVBus0782162_production, 75_LVBus0782163_consumption, 75_LVBus0782163_production, 75_LVBus0782164_production, 75_LVBus0782166_production, 75_LVBus0782167_production, 75_LVBus0782168_production, 75_LVBus0782169_production, 75_LVBus0782171_production, 75_LVBus0782172_production, 75_LVBus0782173_production, 75_LVBus0782175_production, 75_LVBus0782176_production, 75_LVBus0782177_production, 75_LVBus0782179_consumption, 75_LVBus0782179_production, 75_LVBus0782180_consumption, 75_LVBus0782180_production, 75_LVBus0782181_production, 75_LVBus0782182_production, 75_LVBus0782183_consumption, 75_LVBus0782183_production, 75_LVBus0782187_production, 75_LVBus0782189_consumption, 75_LVBus0782189_production, 75_LVBus0782191_production, 75_LVBus0782192_production, 75_LVBus0782193_production, 75_LVBus0782195_consumption, 75_LVBus0782195_production, 75_LVBus0782196_production, 75_LVBus0782197_production, 75_LVBus0782198_production, 75_LVBus0782199_production, 75_LVBus0782200_production, 75_LVBus0782201_production, 75_LVBus0782202_consumption, 75_LVBus0782202_production, 75_LVBus0782203_production, 75_LVBus0782204_production, 75_LVBus0782205_production, 75_LVBus0782209_consumption, 75_LVBus0782209_production, 75_LVBus0782211_consumption, 75_LVBus0782211_production, 75_LVBus0782212_production, 75_LVBus0782213_production, 75_LVBus0782214_production, 75_LVBus0782215_consumption, 75_LVBus0782215_production, 75_LVBus0782216_production, 75_LVBus0782217_production, 75_LVBus0782219_consumption, 75_LVBus0782219_production, 75_LVBus0782220_production, 75_LVBus0782222_consumption, 75_LVBus0782222_production, 75_LVBus0782223_production, 75_LVBus0782224_production, 75_LVBus0782226_production, 75_LVBus0782227_production, 75_LVBus0782228_production, 75_LVBus0782230_production, 75_LVBus0782231_production, 75_LVBus0782232_production, 75_LVBus0782234_production, 75_LVBus0782235_production, 75_LVBus0782236_production, 75_LVBus0782238_production, 75_LVBus0782239_production, 75_LVBus0782240_production, 75_LVBus0782242_production, 75_LVBus0782243_production, 75_LVBus0782244_production, 75_LVBus0782245_production, 75_LVBus0782247_consumption, 75_LVBus0782247_production, 75_LVBus0782248_production, 75_LVBus0782249_production, 75_LVBus0782250_production, 75_LVBus0782252_consumption, 75_LVBus0782252_production, 75_LVBus0782253_production, 75_LVBus0782254_production, 75_LVBus0782255_production, 75_LVBus0782257_production, 75_LVBus0782259_production, 75_LVBus0782260_consumption, 75_LVBus0782260_production, 75_LVBus0782261_production, 75_LVBus0782263_consumption, 75_LVBus0782263_production, 75_LVBus0782264_consumption, 75_LVBus0782264_production, 75_LVBus0782265_production, 75_MVLV007793_consumption, 75_MVLV007793_production, 75_MVLV073969_consumption, 75_MVLV073969_production, 75_MVLV089578_consumption, 75_MVLV089578_production, 75_MVLV140895_consumption, 75_MVLV140895_production, 75_MVLV165692_consumption, 75_MVLV165692_production.

